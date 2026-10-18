#Requires -Version 7.0
<#
.SYNOPSIS
  RimTestMod 可复现编译脚本 —— RimWorld 1.7.4981 rev136 / net10.0 实测通过。

.DESCRIPTION
  把 Source\*.cs 编成 RimTestMod.dll，把 Source\Patches\*.cs 编成
  RimTestMod.Patches.dll，产物一律落在 ..\Assemblies\。

  两条编译路径：
    默认      dotnet build（自动生成临时 csproj，由 SDK 处理 net10.0 引用框架）
    -UseCsc   dotnet exec "<sdk>\Roslyn\bincore\csc.dll"
              手动 -r: 全部 net10.0 ref pack + 游戏 DLL，不做 restore

  游戏目录 / Harmony 目录：优先用 -GameDir / -HarmonyDir 指定；未指定时按
  环境变量 RIMWORLD_DIR / HARMONY_DIR → Steam 注册表与库清单（libraryfolders.vdf）自动探测，
  探不到就报错并说明怎么指定。脚本不写死任何本机路径。

  硬约束（脚本自身保证）：
    * 绝不把游戏 DLL 复制进 Assemblies\（所有 <Reference> 都是 Private=false）
    * 从不写入游戏安装目录，只读取
    * 不复制 0Harmony.dll：它由创意工坊 Harmony mod（brrainz.harmony）提供，
      本 mod 只在编译期引用它。

.EXAMPLE
  pwsh -File .\build.ps1
  pwsh -File .\build.ps1 -UseCsc
  pwsh -File .\build.ps1 -GameDir '<游戏安装目录>'
  $env:RIMWORLD_DIR = '<游戏安装目录>'; pwsh -File .\build.ps1
#>
[CmdletBinding()]
param(
    [string]$GameDir    = '',   # 留空则自动定位（RIMWORLD_DIR → Steam 注册表/库清单）
    [string]$HarmonyDir = '',   # 留空则自动定位（HARMONY_DIR → 创意工坊 294100 下找 0Harmony.dll）
    [string]$Configuration = 'Release',
    [switch]$UseCsc,
    [switch]$SkipVerify
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

# ---------------------------------------------------------------- 路径基线
$SourceDir     = $PSScriptRoot
$ModDir        = Split-Path -Parent $SourceDir
$AssembliesDir = Join-Path $ModDir 'Assemblies'
$WorkDir       = Join-Path $ModDir 'obj\build'   # 生成物与中间产物，全部留在 mod 的 obj\ 下

function Say([string]$m)  { Write-Host $m }
function Ok([string]$m)   { Write-Host "  [OK]   $m"   -ForegroundColor Green }
function Bad([string]$m)  { Write-Host "  [FAIL] $m"   -ForegroundColor Red }
function Info([string]$m) { Write-Host "  [info] $m"   -ForegroundColor DarkGray }
function Head([string]$m) { Write-Host ""; Write-Host "== $m" -ForegroundColor Cyan }

$script:Failures = 0
function Fail([string]$m) { $script:Failures++; Bad $m }
function XmlEsc([string]$s) {
    return $s.Replace('&','&amp;').Replace('<','&lt;').Replace('>','&gt;').Replace('"','&quot;')
}

# ------------------------------------------------- 定位辅助（不写死本机路径）
# 优先级：显式参数 > 环境变量 > Steam 注册表与库清单（libraryfolders.vdf）
function Get-SteamLibraryDirs {
    $roots = New-Object System.Collections.Generic.List[string]
    foreach ($k in @(
            @{ p = 'HKCU:\Software\Valve\Steam';             v = 'SteamPath'   },
            @{ p = 'HKLM:\SOFTWARE\WOW6432Node\Valve\Steam'; v = 'InstallPath' })) {
        try {
            $v = (Get-ItemProperty -Path $k.p -Name $k.v -ErrorAction Stop).($k.v)
            if ($v) { $roots.Add([string]$v) }
        } catch { }
    }
    foreach ($e in @(${env:ProgramFiles(x86)}, $env:ProgramFiles)) {
        if ($e) { $roots.Add((Join-Path $e 'Steam')) }
    }

    $libs = New-Object System.Collections.Generic.List[string]
    foreach ($r in $roots) {
        if (-not (Test-Path -LiteralPath $r -ErrorAction SilentlyContinue)) { continue }
        $libs.Add($r)
        $vdf = Join-Path $r 'steamapps\libraryfolders.vdf'
        if (Test-Path -LiteralPath $vdf -ErrorAction SilentlyContinue) {
            foreach ($m in [regex]::Matches((Get-Content -LiteralPath $vdf -Raw), '"path"\s+"([^"]+)"')) {
                $libs.Add($m.Groups[1].Value.Replace('\\', '\'))
            }
        }
    }
    return ($libs | Select-Object -Unique)
}

function Find-RimWorldDir {
    $cands = New-Object System.Collections.Generic.List[string]
    if ($env:RIMWORLD_DIR) { $cands.Add($env:RIMWORLD_DIR) }
    foreach ($lib in Get-SteamLibraryDirs) { $cands.Add((Join-Path $lib 'steamapps\common\RimWorld')) }
    foreach ($c in $cands) {
        if (Test-Path -LiteralPath (Join-Path $c 'Assembly-CSharp.dll') -ErrorAction SilentlyContinue) {
            return (Resolve-Path -LiteralPath $c).Path
        }
    }
    return ''
}

function Find-RimWorldHarmonyDir([string]$GameDir) {
    if ($env:HARMONY_DIR) { return $env:HARMONY_DIR }
    # 创意工坊里不止 Harmony 一个 mod 会附带 0Harmony.dll（例如 Killfeed 带的是 1.0.9.1），
    # 所以先认官方 Harmony mod 的固定 id，再兜底扫描（1.7 目录优先、版本号次之）。
    $roots = New-Object System.Collections.Generic.List[string]
    if ($GameDir) { $roots.Add((Split-Path -Parent (Split-Path -Parent (Resolve-Path -LiteralPath $GameDir).Path))) }
    foreach ($lib in Get-SteamLibraryDirs) { $roots.Add((Join-Path $lib 'steamapps')) }

    $KnownId = '2009463077'   # 官方 Harmony mod 的公开创意工坊 id
    foreach ($r in ($roots | Select-Object -Unique)) {
        foreach ($sub in @('1.7\Assemblies', 'Assemblies', '1.6\Assemblies')) {
            $d = Join-Path (Join-Path (Join-Path $r 'workshop\content\294100') $KnownId) $sub
            if (Test-Path -LiteralPath (Join-Path $d '0Harmony.dll') -ErrorAction SilentlyContinue) { return $d }
        }
    }

    $best = ''; $bestScore = -1
    foreach ($r in ($roots | Select-Object -Unique)) {
        $content = Join-Path $r 'workshop\content\294100'
        if (-not (Test-Path -LiteralPath $content -ErrorAction SilentlyContinue)) { continue }
        foreach ($mod in Get-ChildItem -LiteralPath $content -Directory -ErrorAction SilentlyContinue) {
            foreach ($sub in @('1.7\Assemblies', 'Assemblies', '1.6\Assemblies')) {
                $dll = Join-Path (Join-Path $mod.FullName $sub) '0Harmony.dll'
                if (-not (Test-Path -LiteralPath $dll -ErrorAction SilentlyContinue)) { continue }
                $ver = [version]'0.0'
                try { $ver = [version]((Get-Item -LiteralPath $dll).VersionInfo.FileVersion) } catch { }
                $score = $ver.Major * 10 + $ver.Minor + $(if ($sub -eq '1.7\Assemblies') { 100 } else { 0 })
                if ($score -gt $bestScore) { $bestScore = $score; $best = (Join-Path $mod.FullName $sub) }
            }
        }
    }
    return $best
}

Head "RimTestMod build.ps1"
Say "  Source : $SourceDir"
Say "  Output : $AssembliesDir"
Say "  配置   : $Configuration / 编译路径 = $(if ($UseCsc) { 'Roslyn csc.dll (手动 -r:)' } else { 'dotnet build' })"

# ---------------------------------------------------------------- 0. 定位游戏目录
if (-not $GameDir)    { $GameDir    = Find-RimWorldDir }
if (-not $HarmonyDir) { $HarmonyDir = Find-RimWorldHarmonyDir -GameDir $GameDir }
if (-not $GameDir) {
    Bad "找不到 RimWorld 游戏目录（该层应含 Assembly-CSharp.dll）"
    Say '  指定方式：-GameDir "<游戏安装目录>"，或先设环境变量 RIMWORLD_DIR'
    exit 1
}
if (-not $HarmonyDir) {
    Bad "找不到含 0Harmony.dll 的目录"
    Say '  指定方式：-HarmonyDir "<含 0Harmony.dll 的目录>"，或先设环境变量 HARMONY_DIR'
    exit 1
}
Info "GameDir    = $GameDir"
Info "HarmonyDir = $HarmonyDir"

# ---------------------------------------------------------------- 1. 依赖校验
Head "1. 检查外部依赖（只读，不修改游戏目录）"

$GameRefs  = @('Assembly-CSharp.dll', 'UnityStubs.dll', 'RimWorld.dll')
$GamePaths = @{}
foreach ($n in $GameRefs) {
    $p = Join-Path $GameDir $n
    if (Test-Path -LiteralPath $p) {
        $GamePaths[$n] = $p
        Ok ("{0}  {1:N0} B" -f $n, (Get-Item -LiteralPath $p).Length)
    } else {
        Fail "$n 不存在：$p"
    }
}
if (Test-Path -LiteralPath (Join-Path $GameDir 'RimWorldWin64_Data\Managed')) {
    Info "RimWorldWin64_Data\Managed 存在（1.7 实测不存在，若换机器编译可作兜底搜索路径）"
}

$HarmonyDll = $null
foreach ($cand in @(
        (Join-Path $HarmonyDir '0Harmony.dll'),
        (Join-Path $GameDir    '0Harmony.dll'),
        (Join-Path $GameDir    'Managed\0Harmony.dll'))) {
    if (Test-Path -LiteralPath $cand) { $HarmonyDll = $cand; break }
}
if ($HarmonyDll) {
    $hv = [System.Reflection.AssemblyName]::GetAssemblyName($HarmonyDll)
    Ok ("0Harmony.dll  {0:N0} B  程序集 {1} v{2}" -f (Get-Item -LiteralPath $HarmonyDll).Length, $hv.Name, $hv.Version)
    Say "         来源：$HarmonyDll"
    Say "         Harmony (MIT License, Copyright (c) 2017 Andreas Pardeike) —— 仅编译期引用，不复制进 mod"
} else {
    Fail "找不到 0Harmony.dll（检查 Harmony mod 是否已订阅/启用，或用 -HarmonyDir 指定）"
}

$sources      = @(Get-ChildItem -LiteralPath $SourceDir -Filter *.cs -File | Sort-Object Name)
$patchDir     = Join-Path $SourceDir 'Patches'
$patchSources = @()
if (Test-Path -LiteralPath $patchDir) { $patchSources = @(Get-ChildItem -LiteralPath $patchDir -Filter *.cs -File | Sort-Object Name) }
Ok ("主程序集源文件 {0} 个；补丁源文件 {1} 个" -f $sources.Count, $patchSources.Count)
foreach ($f in $sources)      { Info ("  main : " + $f.Name) }
foreach ($f in $patchSources) { Info ("  patch: " + $f.Name) }

if ($script:Failures -gt 0) { Bad "依赖校验未通过，终止。"; exit 1 }

# ---------------------------------------------------------------- 2. 输出目录
Head "2. 准备输出目录"
if (-not (Test-Path -LiteralPath $AssembliesDir)) { New-Item -ItemType Directory -Path $AssembliesDir -Force | Out-Null }
Get-ChildItem -LiteralPath $AssembliesDir -File -ErrorAction SilentlyContinue | ForEach-Object {
    Remove-Item -LiteralPath $_.FullName -Force
    Info "清理旧产物 $($_.Name)"
}
if (-not (Test-Path -LiteralPath $WorkDir)) { New-Item -ItemType Directory -Path $WorkDir -Force | Out-Null }
Ok "输出目录就绪：$AssembliesDir"

$MainDll    = Join-Path $AssembliesDir 'RimTestMod.dll'
$PatchesDll = Join-Path $AssembliesDir 'RimTestMod.Patches.dll'

# 生成 csproj 片段：所有外部引用都是 Private=false（= 不复制到输出目录）
function New-RefItem([string]$name, [string]$path) {
    return @"
    <Reference Include="$name">
      <HintPath>$(XmlEsc $path)</HintPath>
      <Private>false</Private>
      <SpecificVersion>false</SpecificVersion>
    </Reference>
"@
}

function New-Csproj {
    param([string]$AssemblyName, [string[]]$CompileFiles, [hashtable]$Refs, [string[]]$ProjectRefDlls)
    $nl = [char]10
    $items = ($CompileFiles | ForEach-Object { '    <Compile Include="' + (XmlEsc $_) + '" />' }) -join $nl
    $refItems = ''
    foreach ($k in $Refs.Keys) { $refItems += (New-RefItem $k $Refs[$k]) }
    foreach ($d in $ProjectRefDlls) { $refItems += (New-RefItem ([System.IO.Path]::GetFileNameWithoutExtension($d)) $d) }
    return @"
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net10.0</TargetFramework>
    <AssemblyName>$AssemblyName</AssemblyName>
    <RootNamespace>Demo.RimTestMod</RootNamespace>
    <LangVersion>latest</LangVersion>
    <Nullable>disable</Nullable>
    <ImplicitUsings>disable</ImplicitUsings>
    <EnableDefaultCompileItems>false</EnableDefaultCompileItems>
    <EnableDefaultItems>false</EnableDefaultItems>
    <GenerateDocumentationFile>false</GenerateDocumentationFile>
    <GenerateDependencyFile>false</GenerateDependencyFile>
    <CopyLocalLockFileAssemblies>false</CopyLocalLockFileAssemblies>
    <ProduceReferenceAssembly>false</ProduceReferenceAssembly>
    <DebugType>none</DebugType>
    <DebugSymbols>false</DebugSymbols>
    <Deterministic>true</Deterministic>
    <Optimize>true</Optimize>
    <NoWarn>CS0436;CS0169;CS0649</NoWarn>
    <AutoGenerateBindingRedirects>false</AutoGenerateBindingRedirects>
    <OutDir>$(XmlEsc $AssembliesDir)\</OutDir>
    <BaseOutputPath>$(XmlEsc $AssembliesDir)\</BaseOutputPath>
  </PropertyGroup>
  <ItemGroup>
$items
  </ItemGroup>
  <ItemGroup>
$refItems
  </ItemGroup>
</Project>
"@
}

# ---------------------------------------------------------------- 3. 编译
$mainSrcList    = @($sources      | ForEach-Object { $_.FullName })
$patchesSrcList = @($patchSources | ForEach-Object { $_.FullName })

if (-not $UseCsc) {
    Head "3. 编译（dotnet build）"

    $projectDir = Join-Path $WorkDir 'proj'
    New-Item -ItemType Directory -Path $projectDir -Force | Out-Null

    $refsMain = @{ 'Assembly-CSharp' = $GamePaths['Assembly-CSharp.dll']; 'RimWorld' = $GamePaths['RimWorld.dll']; 'UnityStubs' = $GamePaths['UnityStubs.dll'] }
    $mainProj = Join-Path $projectDir 'RimTestMod.csproj'
    Set-Content -LiteralPath $mainProj -Encoding UTF8 -Value (New-Csproj -AssemblyName 'RimTestMod' -CompileFiles $mainSrcList -Refs $refsMain -ProjectRefDlls @())
    Ok "生成 $mainProj"

    $refsPatch = @{ 'Assembly-CSharp' = $GamePaths['Assembly-CSharp.dll']; 'RimWorld' = $GamePaths['RimWorld.dll']; 'UnityStubs' = $GamePaths['UnityStubs.dll'] }
    if ($HarmonyDll) { $refsPatch['0Harmony'] = $HarmonyDll }
    $patchProj = Join-Path $projectDir 'RimTestMod.Patches.csproj'
    Set-Content -LiteralPath $patchProj -Encoding UTF8 -Value (New-Csproj -AssemblyName 'RimTestMod.Patches' -CompileFiles $patchesSrcList -Refs $refsPatch -ProjectRefDlls @($MainDll))
    Ok "生成 $patchProj"

    foreach ($p in @(@{ f = $mainProj; n = 'RimTestMod' }, @{ f = $patchProj; n = 'RimTestMod.Patches' })) {
        Say "  --- dotnet build -c $Configuration $($p.n) ---"
        & dotnet build $p.f -c $Configuration --nologo -v minimal -p:NuGetAudit=false -p:UseSharedCompilation=false
        $code = $LASTEXITCODE
        if ($code -ne 0) { Fail "dotnet build $($p.n) 退出码 $code"; break }
        Ok "dotnet build $($p.n) 退出码 0"
    }
} else {
    Head "3. 编译（Roslyn csc.dll，手动 -r:）"

    $dotnetRoot = if ($env:ProgramFiles) { Join-Path $env:ProgramFiles 'dotnet' } else { 'C:\Program Files\dotnet' }
    $cscDll = Get-ChildItem (Join-Path $dotnetRoot 'sdk') -Directory |
        Sort-Object { [version]($_.Name -replace '[^0-9.].*$','') } -Descending |
        ForEach-Object { Join-Path $_.FullName 'Roslyn\bincore\csc.dll' } |
        Where-Object { Test-Path -LiteralPath $_ } | Select-Object -First 1
    if (-not $cscDll) { Fail "找不到 Roslyn csc.dll"; exit 1 }
    Ok "csc.dll = $cscDll"

    $refPack = Get-ChildItem (Join-Path $dotnetRoot 'packs\Microsoft.NETCore.App.Ref') -Directory -ErrorAction SilentlyContinue |
        Where-Object { Test-Path -LiteralPath (Join-Path $_.FullName 'ref\net10.0') } |
        Sort-Object Name -Descending | Select-Object -First 1
    if (-not $refPack) { Fail "找不到 Microsoft.NETCore.App.Ref\*\ref\net10.0"; exit 1 }
    $refDir  = Join-Path $refPack.FullName 'ref\net10.0'
    $refDlls = @(Get-ChildItem -LiteralPath $refDir -Filter *.dll -File | ForEach-Object { $_.FullName })
    Ok "引用框架 = $refDir（$($refDlls.Count) 个 DLL）"

    function Invoke-Csc {
        param([string]$OutDll, [string[]]$CompileFiles, [string[]]$Refs)
        $rsp = Join-Path $WorkDir ("csc-" + [System.IO.Path]::GetFileNameWithoutExtension($OutDll) + ".rsp")
        # csc 没有「设置程序集版本」的命令行开关：-version 是「打印编译器版本后退出」，
        # 加上它会打印一行版本号、exit 0、且什么都不编译（已实测踩坑）。
        # 版本号只能来自源文件特性，所以这里补一个临时 AssemblyInfo 一起编。
        $aiPath = Join-Path $WorkDir ("AssemblyInfo." + [System.IO.Path]::GetFileNameWithoutExtension($OutDll) + ".cs")
        Set-Content -LiteralPath $aiPath -Encoding UTF8 -Value @'
using System.Reflection;
[assembly: AssemblyVersion("1.0.0.0")]
[assembly: AssemblyFileVersion("1.0.0.0")]
'@
        $CompileFiles = @($aiPath) + $CompileFiles
        $lines = @('-nologo','-nostdlib+','-target:library','-langversion:latest','-optimize+','-deterministic+','-platform:anycpu','-debug-','-warn:4')
        $lines += ('-out:"' + $OutDll + '"')
        foreach ($r in ($Refs + $refDlls)) { $lines += ('-r:"' + $r + '"') }
        $lines += ($CompileFiles | ForEach-Object { '"' + $_ + '"' })
        Set-Content -LiteralPath $rsp -Encoding UTF8 -Value $lines
        # 注意：csc 的输出必须显式转给 Write-Host。若让它落到函数输出流里，
        # 函数会把「csc 的 stdout 行」和退出码一起返回成数组，$c1 就不是数字了。
        & dotnet exec $cscDll "@$rsp" 2>&1 | ForEach-Object { Write-Host "    $_" }
        return $LASTEXITCODE
    }

    $refsMain = @($GamePaths['Assembly-CSharp.dll'], $GamePaths['RimWorld.dll'], $GamePaths['UnityStubs.dll'])
    Say "  --- csc RimTestMod.dll ---"
    $c1 = Invoke-Csc -OutDll $MainDll -CompileFiles $mainSrcList -Refs $refsMain
    if ($c1 -ne 0) { Fail "csc 编译主程序集失败，退出码 $c1" } else { Ok "csc RimTestMod.dll 退出码 0" }

    $refsPatch = @($GamePaths['Assembly-CSharp.dll'], $GamePaths['RimWorld.dll'], $GamePaths['UnityStubs.dll'], $MainDll)
    if ($HarmonyDll) { $refsPatch += $HarmonyDll }
    Say "  --- csc RimTestMod.Patches.dll ---"
    $c2 = Invoke-Csc -OutDll $PatchesDll -CompileFiles $patchesSrcList -Refs $refsPatch
    if ($c2 -ne 0) { Fail "csc 编译补丁程序集失败，退出码 $c2" } else { Ok "csc RimTestMod.Patches.dll 退出码 0" }
}

# ---------------------------------------------------------------- 4. 产物核验
Head "4. 产物核验"

function Get-AssemblyRefs([string]$Path) {
    $fs = $null; $pe = $null
    try {
        $fs = [System.IO.File]::Open($Path, [System.IO.FileMode]::Open, [System.IO.FileAccess]::Read, [System.IO.FileShare]::ReadWrite)
        $pe = [System.Reflection.PortableExecutable.PEReader]::new($fs)
        $mr = [System.Reflection.Metadata.PEReaderExtensions]::GetMetadataReader($pe)
        $out = @()
        foreach ($h in $mr.AssemblyReferences) { $out += $mr.GetString($mr.GetAssemblyReference($h).Name) }
        return $out
    } finally {
        if ($pe) { $pe.Dispose() }
        if ($fs) { $fs.Dispose() }
    }
}

$results = @()
foreach ($item in @(
        [pscustomobject]@{ File = $MainDll;    Label = "RimTestMod";         MustNotRefHarmony = $true  },
        [pscustomobject]@{ File = $PatchesDll; Label = "RimTestMod.Patches"; MustNotRefHarmony = $false })) {
    if (-not (Test-Path -LiteralPath $item.File)) { Fail "$($item.Label).dll 没有生成"; continue }
    $fi = Get-Item -LiteralPath $item.File
    $id = [System.Reflection.AssemblyName]::GetAssemblyName($item.File)
    Ok ("{0}.dll  {1:N0} B  ({2:N2} KB)  程序集 {3} v{4}" -f $item.Label, $fi.Length, ($fi.Length / 1KB), $id.Name, $id.Version)
    $results += [pscustomobject]@{ 名称 = $item.Label; 字节 = $fi.Length; 版本 = $id.Version.ToString() }

    if ($SkipVerify) { continue }
    try {
        $refs = @(Get-AssemblyRefs $item.File)
        $hasHarmony = $refs -contains "0Harmony"
        Info ("引用程序集： " + ($refs -join ", "))
        if ($refs -contains "Assembly-CSharp") { Ok "$($item.Label) 引用 Assembly-CSharp（预期）" } else { Fail "$($item.Label) 未引用 Assembly-CSharp" }
        if ($refs -contains "UnityStubs") { Ok "$($item.Label) 引用 UnityStubs（1.7 的 Unity 兼容层）" }
        if ($item.MustNotRefHarmony) {
            if ($hasHarmony) { Fail "主程序集竟然引用了 0Harmony —— 违反「主程序集必须能独立加载」约束" }
            else { Ok "主程序集不引用 0Harmony（约束满足：没有 Harmony 也能加载）" }
        } else {
            if ($hasHarmony) { Ok "$($item.Label) 引用 0Harmony（运行时由 Harmony mod 提供）" } else { Fail "$($item.Label) 未引用 0Harmony" }
            if ($refs -contains "RimTestMod") { Ok "$($item.Label) 引用主程序集 RimTestMod（跨程序集调用已接线）" }
        }
    } catch {
        Info "元数据读取失败（跳过引用核验）：$($_.Exception.Message)"
    }
}

# ---------------------------------------------------------------- 5. 反向检查
Head "5. 反向检查：Assemblies 里有没有混进不该有的 DLL"
$forbidden = @('Assembly-CSharp.dll','RimWorld.dll','UnityStubs.dll','mscorlib.dll','netstandard.dll','0Harmony.dll','UnityEngine.dll')
$found = @(Get-ChildItem -LiteralPath $AssembliesDir -File | Where-Object { $forbidden -contains $_.Name })
if ($found.Count -gt 0) {
    foreach ($f in $found) { Fail "Assemblies 里出现了不该打包的文件：$($f.Name)" }
} else {
    Ok "Assemblies 里只有本 mod 自己的产物：没有游戏 DLL、没有 0Harmony.dll"
}
Say "  目录内容："
Get-ChildItem -LiteralPath $AssembliesDir -File | ForEach-Object { Say ("    {0,-26} {1,10:N0} B" -f $_.Name, $_.Length) }

# ---------------------------------------------------------------- 6. 摘要
Head "6. 摘要"
$results | Format-Table -AutoSize | Out-String | Write-Host

if ($script:Failures -gt 0) {
    Bad "构建结束：$($script:Failures) 项失败"
    exit 1
}
Ok "构建结束：全部检查通过"
exit 0
