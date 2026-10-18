$ErrorActionPreference='Stop'
$dir='E:\SteamLibrary\steamapps\common\RimWorld'
$ac=[System.Reflection.Assembly]::LoadFrom((Join-Path $dir 'Assembly-CSharp.dll'))
$harm=[System.Reflection.Assembly]::LoadFrom('E:\SteamLibrary\steamapps\workshop\content\294100\2009463077\1.7\Assemblies\0Harmony.dll')
function Get-Types($asm){ try { return $asm.GetTypes() } catch [System.Reflection.ReflectionTypeLoadException] { return ($_.Exception.Types | Where-Object { $_ -ne $null }) } }
$acTypes=Get-Types $ac
'acTypes=' + $acTypes.Count
$allFlags=[System.Reflection.BindingFlags]::Public -bor [System.Reflection.BindingFlags]::NonPublic -bor [System.Reflection.BindingFlags]::Instance -bor [System.Reflection.BindingFlags]::Static -bor [System.Reflection.BindingFlags]::DeclaredOnly
$pubFlags=[System.Reflection.BindingFlags]'Public,Instance,Static,DeclaredOnly'
$want=@('CanReserve','Reserve','IsForbidden','FailOnDespawnedNullOrForbidden','WithProgressBar','GetNamed','FailOnThingDestroyed')
foreach($w in $want){
  '=== ' + $w + ' ==='
  $found=$false
  foreach($t in $acTypes){
    try{ $ms=$t.GetMethods($allFlags) }catch{ continue }
    foreach($m in $ms){
      if($m.Name -ne $w){ continue }
      $found=$true
      $ps=@()
      foreach($p in $m.GetParameters()){ $o=''; if($p.IsOptional){$o='=opt'} ; $ps += ($p.ParameterType.Name + ' ' + $p.Name + $o) }
      $st='' ; if($m.IsStatic){$st='static '}
      '  ' + $t.FullName + ' :: ' + $st + $m.ReturnType.Name + ' ' + $m.Name + '(' + ($ps -join ', ') + ')'
    }
  }
  if(-not $found){ '  (全局无此方法名)' }
}
'=== Toil 相关类型 ==='
foreach($t in $acTypes){ if($t.FullName -like '*Toil*'){ '  ' + $t.FullName } }
'=== Harmony 程序集 ==='
$hTypes=Get-Types $harm
'hTypes=' + $hTypes.Count
foreach($n in @('HarmonyLib.Harmony','HarmonyLib.HarmonyPatch','HarmonyLib.HarmonyPrefix','HarmonyLib.HarmonyPostfix','HarmonyLib.HarmonyPatchAll')){
  $t=$hTypes | Where-Object { $_.FullName -eq $n } | Select-Object -First 1
  if($t -eq $null){ '  MISSING ' + $n; continue }
  $b=''; if($t.BaseType){$b=$t.BaseType.Name}
  '  ' + $n + ' base=' + $b
  foreach($m in $t.GetMethods($pubFlags)){ '      M ' + $m.ReturnType.Name + ' ' + $m.Name + '(' + (($m.GetParameters() | ForEach-Object { $_.ParameterType.Name + ' ' + $_.Name }) -join ', ') + ')' }
}
'=== DefDatabase GetNamed ==='
foreach($x in ($acTypes | Where-Object { $_.FullName -like 'Verse.DefDatabase*' })){
  '  type: ' + $x.FullName
  try{ foreach($m in $x.GetMethods($pubFlags)){ if($m.Name -like '*GetNamed*'){ '      M ' + $m.ReturnType.Name + ' ' + $m.Name + '(' + (($m.GetParameters() | ForEach-Object { $_.ParameterType.Name + ' ' + $_.Name }) -join ', ') + ')' } } }catch{ '      (报错)' }
}
'=== DefOf 相关类型 ==='
foreach($t in $acTypes){ if($t.Name -like 'DefOf*'){ $b=''; if($t.BaseType){$b=$t.BaseType.Name}; '  ' + $t.FullName + ' (base=' + $b + ')' } }
'=== Toils_Goto 第三参 IsOptional ==='
foreach($t in $acTypes){ if($t.FullName -eq 'Verse.AI.Toils_Goto'){ foreach($m in $t.GetMethods($pubFlags)){ if($m.Name -eq 'GotoThing'){ '  ' + $m.Name + '(' + (($m.GetParameters() | ForEach-Object { $_.ParameterType.Name + ' ' + $_.Name + $(if($_.IsOptional){'=opt'}else{''}) }) -join ', ') + ')' } } } }
'=== Hediff 字段 ==='
foreach($t in $acTypes){ if($t.FullName -eq 'Verse.Hediff'){ foreach($f in $t.GetFields($allFlags)){ '  F ' + $f.FieldType.Name + ' ' + $f.Name } } }