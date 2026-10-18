# 定位 RimWorld 安装目录与创意工坊 Harmony 目录 —— 不写死任何本机路径。
#
# 解析顺序：环境变量 RIMWORLD_DIR / HARMONY_DIR → Steam 注册表 → Steam 库清单
#           steamapps\libraryfolders.vdf → 常见默认位置。找不到时报错并说明怎么设置。
#
# 用法：. (Join-Path $PSScriptRoot '_rimworld.ps1')
#       $dir  = Get-RimWorldDir
#       $harm = Get-RimWorldHarmonyDir -GameDir $dir

# Harmony 创意工坊 id（公开 id，与本机无关）
$script:HarmonyWorkshopId = '2009463077'

function Get-SteamLibraryRoots {
    $roots = New-Object 'System.Collections.Generic.List[string]'
    foreach ($k in @('HKCU:\Software\Valve\Steam', 'HKLM:\SOFTWARE\WOW6432Node\Valve\Steam', 'HKLM:\SOFTWARE\Valve\Steam')) {
        try {
            $p = Get-ItemProperty -Path $k -ErrorAction Stop
            foreach ($n in @('SteamPath', 'InstallPath')) {
                $prop = $p.PSObject.Properties[$n]
                if ($prop -and $prop.Value) { $roots.Add(([string]$prop.Value).Replace('/', '\')) }
            }
        } catch { }
    }
    foreach ($n in @(${env:ProgramFiles(x86)}, $env:ProgramFiles)) {
        if ($n) { $roots.Add((Join-Path $n 'Steam')) }
    }
    return ($roots | Where-Object { $_ -and (Test-Path -LiteralPath $_ -ErrorAction SilentlyContinue) } | Select-Object -Unique)
}

function Get-SteamLibraryDirs {
    $libs = New-Object 'System.Collections.Generic.List[string]'
    foreach ($root in Get-SteamLibraryRoots) {
        $libs.Add($root)
        $vdf = Join-Path $root 'steamapps\libraryfolders.vdf'
        if (Test-Path -LiteralPath $vdf -ErrorAction SilentlyContinue) {
            $txt = Get-Content -LiteralPath $vdf -Raw
            foreach ($m in [regex]::Matches($txt, '"path"\s+"([^"]+)"')) {
                $libs.Add(($m.Groups[1].Value -replace '\\\\', '\'))
            }
        }
    }
    return ($libs | Where-Object { $_ -and (Test-Path -LiteralPath $_ -ErrorAction SilentlyContinue) } | Select-Object -Unique)
}

function Get-RimWorldDir {
    $cands = New-Object 'System.Collections.Generic.List[string]'
    if ($env:RIMWORLD_DIR) { $cands.Add($env:RIMWORLD_DIR) }
    foreach ($lib in Get-SteamLibraryDirs) { $cands.Add((Join-Path $lib 'steamapps\common\RimWorld')) }
    foreach ($c in $cands) {
        if ($c -and (Test-Path -LiteralPath (Join-Path $c 'Assembly-CSharp.dll') -ErrorAction SilentlyContinue)) { return (Resolve-Path -LiteralPath $c -ErrorAction SilentlyContinue).Path }
    }
    throw "找不到 RimWorld 安装目录。请把游戏根目录（含 Assembly-CSharp.dll 的那一层）写进环境变量 RIMWORLD_DIR 再重跑，例如：`$env:RIMWORLD_DIR = '<游戏安装目录>'"
}

function Get-RimWorldHarmonyDir {
    param([string]$GameDir)
    $tail = Join-Path 'workshop\content\294100' (Join-Path $script:HarmonyWorkshopId '1.7\Assemblies')
    $cands = New-Object 'System.Collections.Generic.List[string]'
    if ($env:HARMONY_DIR) { $cands.Add($env:HARMONY_DIR) }
    if ($GameDir) {
        # <Steam 库>\steamapps\common\RimWorld 的祖父目录就是 <Steam 库>\steamapps
        $steamapps = Split-Path -Parent (Split-Path -Parent (Resolve-Path -LiteralPath $GameDir).Path)
        $cands.Add((Join-Path $steamapps $tail))
        foreach ($lib in Get-SteamLibraryDirs) { $cands.Add((Join-Path (Join-Path $lib 'steamapps') $tail)) }
    }
    foreach ($c in $cands) {
        if ($c -and (Test-Path -LiteralPath (Join-Path $c '0Harmony.dll') -ErrorAction SilentlyContinue)) { return (Resolve-Path -LiteralPath $c -ErrorAction SilentlyContinue).Path }
    }
    throw "找不到 0Harmony.dll。请订阅创意工坊 Harmony mod（id $($script:HarmonyWorkshopId)），或用环境变量 HARMONY_DIR 指向含 0Harmony.dll 的目录"
}
