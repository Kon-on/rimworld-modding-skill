$ErrorActionPreference='Stop'
$dir='E:\SteamLibrary\steamapps\common\RimWorld'
$ac=[System.Reflection.Assembly]::LoadFrom((Join-Path $dir 'Assembly-CSharp.dll'))
function Get-Types($asm){ try { return $asm.GetTypes() } catch [System.Reflection.ReflectionTypeLoadException] { return ($_.Exception.Types | Where-Object { $_ -ne $null }) } }
$acTypes=Get-Types $ac
$all=[System.Reflection.BindingFlags]::Public -bor [System.Reflection.BindingFlags]::NonPublic -bor [System.Reflection.BindingFlags]::Instance -bor [System.Reflection.BindingFlags]::Static -bor [System.Reflection.BindingFlags]::DeclaredOnly
function Dump($name){
  $t = $acTypes | Where-Object { $_.FullName -eq $name } | Select-Object -First 1
  if($t -eq $null){ '  MISSING ' + $name; return }
  $b=''; if($t.BaseType){$b=$t.BaseType.FullName}
  '  ' + $name + '  base=' + $b
  try{ foreach($c in $t.GetConstructors($all)){ '      C ' + (($c.GetParameters() | ForEach-Object { $_.ParameterType.Name + ' ' + $_.Name }) -join ', ') } }catch{}
  if($name -like '*JobDriver*' -or $name -like '*WorkGiver*' -or $name -eq 'Verse.Mod' -or $name -eq 'Verse.Def'){
    try{ foreach($f in $t.GetFields($all)){ '      F ' + $f.FieldType.Name + ' ' + $f.Name } }catch{}
    try{ foreach($p in $t.GetProperties($all)){ '      P ' + $p.PropertyType.Name + ' ' + $p.Name } }catch{}
  }
}
foreach($n in @('Verse.Mod','Verse.Def','Verse.DefModExtension','Verse.ModContentPack','Verse.Pawn_HealthTracker','Verse.HediffWithComps','RimWorld.WorkGiver','Verse.AI.PathEndMode','Verse.AI.TargetIndex','Verse.StaticConstructorOnStartup','Verse.AI.ReservationUtility','RimWorld.ForbidUtility','Verse.AI.ToilEffects','Verse.AI.ToilFailConditions')){ Dump $n }
'=== RemoveHediff ==='
foreach($t in $acTypes){ try{ foreach($m in $t.GetMethods($all)){ if($m.Name -eq 'RemoveHediff'){ '  ' + $t.FullName + ' :: V ' + $m.Name + '(' + (($m.GetParameters() | ForEach-Object { $_.ParameterType.Name + ' ' + $_.Name }) -join ', ') + ')' } } }catch{} }
'=== ToilEffects / ToilFailConditions 公开方法（前 25 个）==='
foreach($n in @('Verse.AI.ToilEffects','Verse.AI.ToilFailConditions')){
  $t=$acTypes | Where-Object { $_.FullName -eq $n } | Select-Object -First 1
  if($t){ foreach($m in ($t.GetMethods([System.Reflection.BindingFlags]'Public,Static,DeclaredOnly') | Select-Object -First 25)){ '  ' + $n + ' :: ' + $m.ReturnType.Name + ' ' + $m.Name + '(' + (($m.GetParameters() | ForEach-Object { $_.ParameterType.Name + ' ' + $_.Name }) -join ', ') + ')' } }
}
'=== StaticConstructorOnStartup 用法确认 ==='
foreach($t in $acTypes){ if($t.Name -eq 'StaticConstructorOnStartup'){ '  full=' + $t.FullName + ' base=' + $t.BaseType.FullName } }