
$ErrorActionPreference='Stop'
# 仓库根 = 本脚本所在目录（docs/）的上一级；换机器、换 clone 都不用改路径
$Docs = Join-Path (Split-Path -Parent $PSScriptRoot) 'docs'
$dir='E:\SteamLibrary\steamapps\common\RimWorld'
$out=Join-Path $Docs 'unitystubs-stubs.txt'
$us=[System.Reflection.Assembly]::LoadFrom((Join-Path $dir 'UnityStubs.dll'))
$sw=$us.GetType('UnityStubs.Internal.StubWarner')
$logstub=$sw.GetMethod('LogStub',[System.Reflection.BindingFlags]'Public,NonPublic,Static,Instance')
$tok=$logstub.MetadataToken
$pat=@([byte]($tok -band 0xFF),[byte](($tok -shr 8) -band 0xFF),[byte](($tok -shr 16) -band 0xFF),[byte](($tok -shr 24) -band 0xFF))
"LogStub token=" + $tok + " pattern=" + ($pat -join ',')

function Get-Types($asm){ try { return $asm.GetTypes() } catch [System.Reflection.ReflectionTypeLoadException] { return ($_.Exception.Types | Where-Object { $_ -ne $null }) } }
$types = Get-Types $us
$flags=[System.Reflection.BindingFlags]'Public,NonPublic,Instance,Static,DeclaredOnly'
$lines=New-Object 'System.Collections.Generic.List[string]'
$stubCount=0; $typeSet=New-Object 'System.Collections.Generic.HashSet[string]'; $perType=@{}
$totalMethods=0
foreach($t in $types){
  try{ $tms=$t.GetMethods($flags) }catch{ continue }
  $totalMethods += $tms.Count
  foreach($m in $tms){
    try{ $b=$m.GetMethodBody() }catch{ continue }
    if($b -eq $null){ continue }
    $il=$b.GetILAsByteArray(); if($il -eq $null -or $il.Length -lt 5){ continue }
    $hit=$false
    for($i=0;$i -le $il.Length-4;$i++){ if($il[$i] -eq $pat[0] -and $il[$i+1] -eq $pat[1] -and $il[$i+2] -eq $pat[2] -and $il[$i+3] -eq $pat[3]){ $hit=$true; break } }
    if($hit){
      $stubCount++
      $null=$typeSet.Add($t.FullName)
      if(-not $perType.ContainsKey($t.FullName)){ $perType[$t.FullName]=New-Object 'System.Collections.Generic.List[string]' }
      $perType[$t.FullName].Add($m.Name)
      $lines.Add($t.FullName + ' :: ' + $m.Name)
    }
  }
}
$lines | Set-Content -Path $out -Encoding UTF8
"stubMethodHits=" + $stubCount + " stubTypeCount=" + $typeSet.Count + " totalMethodsInStubs=" + $totalMethods
"--- per type (>=1) ---"
$perType.GetEnumerator() | Sort-Object { -$_.Value.Count } | ForEach-Object { $_.Key + " (" + $_.Value.Count + "): " + (($_.Value | Select-Object -First 8) -join ', ') }
