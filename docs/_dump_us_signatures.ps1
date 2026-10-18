$ErrorActionPreference='Stop'
$dir='E:\SteamLibrary\steamapps\common\RimWorld'
$us=[System.Reflection.Assembly]::LoadFrom((Join-Path $dir 'UnityStubs.dll'))
function Get-Types($asm){ try { return $asm.GetTypes() } catch [System.Reflection.ReflectionTypeLoadException] { return ($_.Exception.Types | Where-Object { $_ -ne $null }) } }
$types=Get-Types $us
$map=@{}
foreach($line in (Get-Content '<REPO_ROOT>\docs\unitystubs-stubs.txt')){
  if($line -notmatch ' :: '){ continue }
  $parts=$line -split ' :: ',2
  $tn=$parts[0].Trim(); $mn=$parts[1].Trim()
  if(-not $map.ContainsKey($tn)){ $map[$tn]=New-Object 'System.Collections.Generic.HashSet[string]' }
  $null=$map[$tn].Add($mn)
}
$flags=[System.Reflection.BindingFlags]'Public,NonPublic,Instance,Static,DeclaredOnly'
$out=New-Object 'System.Collections.Generic.List[string]'
foreach($tn in ($map.Keys | Sort-Object)){
  $t=$types | Where-Object { $_.FullName -eq $tn } | Select-Object -First 1
  if($t -eq $null){ $out.Add('MISSING-TYPE :: ' + $tn); continue }
  $all=$t.GetMethods($flags)
  foreach($mn in ($map[$tn] | Sort-Object)){
    $ms=@($all | Where-Object { $_.Name -eq $mn })
    if($ms.Count -eq 0){ $out.Add($tn + ' :: ' + $mn + ' (no such method)'); continue }
    foreach($m in $ms){
      $ps=@(); foreach($p in $m.GetParameters()){ $ps += ($p.ParameterType.Name + ' ' + $p.Name) }
      $st=''; if($m.IsStatic){$st='static '}
      $out.Add($tn + ' :: ' + $st + $m.ReturnType.Name + ' ' + $m.Name + '(' + ($ps -join ', ') + ')')
    }
  }
}
$out | Set-Content -Path '<REPO_ROOT>\docs\unitystubs-stub-signatures.txt' -Encoding UTF8
'sigLines=' + $out.Count
'=== TYPE METHOD TOTALS ==='
$common=@('UnityEngine.Vector3','UnityEngine.Vector2','UnityEngine.Rect','UnityEngine.Mathf','UnityEngine.Color','UnityEngine.Color32','UnityEngine.GameObject','UnityEngine.Transform','UnityEngine.MonoBehaviour','UnityEngine.Texture2D','UnityEngine.Material','UnityEngine.Shader','UnityEngine.GUI','UnityEngine.Screen','UnityEngine.Application','UnityEngine.Debug','UnityEngine.Input','UnityEngine.Time','UnityEngine.CullingGroup','UnityEngine.CommandBuffer','UnityEngine.ComputeShader','UnityEngine.Camera','UnityEngine.Graphics','UnityEngine.Resources','UnityEngine.Mesh','UnityEngine.RenderTexture','UnityEngine.SceneManagement.SceneManager')
foreach($n in $common){
  $t=$types | Where-Object { $_.FullName -eq $n } | Select-Object -First 1
  if($t -eq $null){ 'MISSING|' + $n; continue }
  $c=0; try{ $c=$t.GetMethods($flags).Count }catch{}
  $s=0; if($map.ContainsKey($n)){ $s=$map[$n].Count }
  $n + '|methods=' + $c + '|stubNames=' + $s
}