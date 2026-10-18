$ErrorActionPreference='Stop'
$dir='E:\SteamLibrary\steamapps\common\RimWorld'
$ac=[System.Reflection.Assembly]::LoadFrom((Join-Path $dir 'Assembly-CSharp.dll'))
$harm=[System.Reflection.Assembly]::LoadFrom('E:\SteamLibrary\steamapps\workshop\content\294100\2009463077\1.7\Assemblies\0Harmony.dll')
function Get-Types($asm){ try { return $asm.GetTypes() } catch [System.Reflection.ReflectionTypeLoadException] { return ($_.Exception.Types | Where-Object { $_ -ne $null }) } }
$acTypes=Get-Types $ac
$all=[System.Reflection.BindingFlags]::Public -bor [System.Reflection.BindingFlags]::NonPublic -bor [System.Reflection.BindingFlags]::Instance -bor [System.Reflection.BindingFlags]::Static -bor [System.Reflection.BindingFlags]::DeclaredOnly
function Sig($m){ $ps=@(); foreach($p in $m.GetParameters()){ $o=''; if($p.IsOptional){$o=' [opt]'}; $ps += ($p.ParameterType.Name + ' ' + $p.Name + $o) }; return $m.Name + '(' + ($ps -join ', ') + ')' }
$targets=@('Verse.Scribe_Values','Verse.AI.ReservationUtility','Verse.AI.ToilEffects','Verse.AI.ToilFailConditions','RimWorld.WorkGiver_Scanner','Verse.Hediff','Verse.Pawn','Verse.AI.Toils_Goto')
foreach($n in $targets){
  $t=$acTypes | Where-Object { $_.FullName -eq $n } | Select-Object -First 1
  if($t -eq $null){ 'MISSING ' + $n; continue }
  '=== ' + $n + ' ==='
  try{ foreach($m in $t.GetMethods($all)){ if($m.Name -like 'Look*' -or $m.Name -like '*CanReserve*' -or $m.Name -like 'Reserve*' -or $m.Name -like '*ProgressBar*' -or $m.Name -like 'FailOnDespawnedNullOrForbidden' -or $m.Name -like 'HasJobOnThing' -or $m.Name -like 'JobOnThing' -or $m.Name -like 'Severity*' -or $m.Name -like 'RemoveHediff' -or $m.Name -like 'Goto*' -or $m.Name -like 'get_*Severity*' -or $m.Name -eq 'Kill' ){ '  M ' + $(if($m.IsStatic){'static '}else{''}) + $m.ReturnType.Name + ' ' + (Sig $m) } } }catch{ '  (err)' }
  try{ foreach($p in $t.GetProperties($all)){ if($p.Name -like '*everity*' -or $p.Name -eq 'health' -or $p.Name -eq 'pawn'){ '  P ' + $p.PropertyType.Name + ' ' + $p.Name } } }catch{}
  try{ foreach($f in $t.GetFields($all)){ if($f.Name -eq 'health' -or $f.Name -eq 'pawn' -or $f.Name -eq 'severityInt'){ '  F ' + $f.FieldType.Name + ' ' + $f.Name } } }catch{}
}
'=== Harmony 构造与方法 ==='
$hTypes=Get-Types $harm
$h=$hTypes | Where-Object { $_.FullName -eq 'HarmonyLib.Harmony' } | Select-Object -First 1
foreach($c in $h.GetConstructors($all)){ '  C ' + ($c.GetParameters() | ForEach-Object { $_.ParameterType.Name + ' ' + $_.Name }) -join ', ' }
foreach($m in $h.GetMethods([System.Reflection.BindingFlags]'Public,Instance,DeclaredOnly')){ if($m.Name -in @('Patch','PatchAll','UnpatchAll','Unpatch')){ '  M ' + $m.ReturnType.Name + ' ' + (Sig $m) } }
foreach($n in @('HarmonyLib.HarmonyMethod','HarmonyLib.HarmonyAttribute')){ $t=$hTypes | Where-Object { $_.FullName -eq $n } | Select-Object -First 1; if($t){ '  TYPE ' + $n + ' base=' + $(if($t.BaseType){$t.BaseType.Name}else{''}) } else { '  MISSING ' + $n } }