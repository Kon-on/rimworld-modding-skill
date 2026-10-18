
$ErrorActionPreference='Stop'
$dir='E:\SteamLibrary\steamapps\common\RimWorld'
$out='<REPO_ROOT>\docs\csharp-api.json'

$us=[System.Reflection.Assembly]::LoadFrom((Join-Path $dir 'UnityStubs.dll'))
$ac=[System.Reflection.Assembly]::LoadFrom((Join-Path $dir 'Assembly-CSharp.dll'))
$harm=[System.Reflection.Assembly]::LoadFrom('E:\SteamLibrary\steamapps\workshop\content\294100\2009463077\1.7\Assemblies\0Harmony.dll')
function Get-Types($asm){ try { return $asm.GetTypes() } catch [System.Reflection.ReflectionTypeLoadException] { return ($_.Exception.Types | Where-Object { $_ -ne $null }) } }
$acTypes = Get-Types $ac; $usTypes = Get-Types $us; $hTypes = Get-Types $harm
$idx=New-Object 'System.Collections.Generic.List[string]'
foreach($t in $usTypes){ try{ $idx.Add('U|' + $t.FullName) }catch{} }
foreach($t in $hTypes){ try{ $idx.Add('H|' + $t.FullName) }catch{} }
foreach($t in $acTypes){ try{ $idx.Add('A|' + $t.FullName) }catch{} }

$roots=@(
 'Verse.Mod','Verse.ModContentPack','Verse.ModAssemblyHandler','Verse.ModSettings','Verse.DefModExtension','Verse.Def',
 'Verse.ThingComp','Verse.CompProperties','Verse.HediffComp','Verse.HediffCompProperties','Verse.HediffWithComps','Verse.Hediff',
 'Verse.Pawn','Verse.Thing','Verse.ThingWithComps','Verse.Log','Verse.Scribe_Values','Verse.Scribe_Collections','Verse.Scribe_Defs',
 'Verse.AI.JobDriver','Verse.AI.Job','Verse.AI.Toil','Verse.AI.Toils_Goto','Verse.AI.ToilCompleteMode','Verse.AI.TargetIndex',
 'Verse.ThingRequest','Verse.AI.PathEndMode','Verse.JobMaker','Verse.ToilMaker','Verse.JobDef','Verse.ThingDef','Verse.DefDatabase\`1',
 'RimWorld.WorkGiver_Scanner','RimWorld.WorkGiver','RimWorld.DefOf','RimWorld.ToilFailConditions','RimWorld.ToilEffects',
 'HarmonyLib.Harmony','HarmonyLib.HarmonyPatch','HarmonyLib.HarmonyPrefix','HarmonyLib.HarmonyPostfix',
 'UnityStubs.Internal.StubWarner','Verse.StaticConstructorOnStartup'
)
$members=New-Object 'System.Collections.Generic.List[string]'
foreach($fn in $roots){
  $t=$acTypes | Where-Object { $_.FullName -eq $fn } | Select-Object -First 1; $a='A'
  if($t -eq $null){ $t=$hTypes | Where-Object { $_.FullName -eq $fn } | Select-Object -First 1; $a='H' }
  if($t -eq $null){ $t=$usTypes | Where-Object { $_.FullName -eq $fn } | Select-Object -First 1; $a='U' }
  if($t -eq $null){ $members.Add('## ' + $fn + ' :: MISSING'); continue }
  $members.Add('## ROOT ' + $fn + ' asm=' + $a)
  $flags=[System.Reflection.BindingFlags]'Public,NonPublic,Instance,Static,DeclaredOnly'
  $cur=$t; $depth=0
  while($cur -ne $null -and $depth -lt 8){
    $cn=$cur.FullName
    $members.Add('## LEVEL' + $depth + ' ' + $cn)
    try{
      foreach($m in $cur.GetMethods($flags)){
        $ps=@(); foreach($p in $m.GetParameters()){ $ps += ($p.ParameterType.Name + ' ' + $p.Name) }
        $mods=@(); if($m.IsPublic){$mods+='public'}else{$mods+='nonpublic'}; if($m.IsStatic){$mods+='static'}
        if($m.IsVirtual){$mods+='virtual'}; if($m.IsAbstract){$mods+='abstract'}
        $members.Add('  M|' + ($mods -join ' ') + '|' + $m.ReturnType.Name + ' ' + $m.Name + '(' + ($ps -join ', ') + ')')
      }
      foreach($p in $cur.GetProperties($flags)){
        $acc=@(); if($p.GetMethod){$acc+='get'}; if($p.SetMethod){$acc+='set'}
        $vt=''; try{ $vt=$p.PropertyType.Name }catch{}
        $members.Add('  P|' + $vt + '|' + $p.Name + '|' + ($acc -join '/'))
      }
      foreach($f in $cur.GetFields($flags)){
        $ft=''; try{ $ft=$f.FieldType.Name }catch{}
        $members.Add('  F|' + $ft + '|' + $f.Name)
      }
    }catch{ $members.Add('  !err ' + $cn) }
    $cur=$cur.BaseType; $depth++
  }
}
$res=@{ asmVersion=$ac.GetName().Version.ToString(); harmony=$harm.GetName().Version.ToString(); acTypeCount=$acTypes.Count; usTypeCount=$usTypes.Count; hTypeCount=$hTypes.Count; types=$idx; members=$members }
$res | ConvertTo-Json -Depth 4 -Compress | Set-Content -Path $out -Encoding UTF8
"OK bytes=" + (Get-Item $out).Length + " roots=" + $roots.Count + " harmony=" + $harm.GetName().Version
