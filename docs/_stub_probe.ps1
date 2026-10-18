
$ErrorActionPreference='Stop'
$dir='E:\SteamLibrary\steamapps\common\RimWorld'
$us=[System.Reflection.Assembly]::LoadFrom((Join-Path $dir 'UnityStubs.dll'))
$sw=$us.GetType('UnityStubs.Internal.StubWarner')
"StubWarner: " + $sw.FullName
foreach($m in $sw.GetMethods([System.Reflection.BindingFlags]'Public,NonPublic,Static,Instance,DeclaredOnly')){ "  " + $m.Name + " token=" + $m.MetadataToken }
$inp=$us.GetType('UnityEngine.Input')
"Input methods: " + ($inp.GetMethods([System.Reflection.BindingFlags]'Public,Static,DeclaredOnly')).Count
$m=$inp.GetMethod('GetAxis',[System.Reflection.BindingFlags]'Public,Static')
try { $b=$m.GetMethodBody(); "GetMethodBody OK, IL len=" + $b.GetILAsByteArray().Length } catch { "GetMethodBody FAILED: " + $_.Exception.GetType().Name + " :: " + $_.Exception.Message }
$mod=$us.ManifestModule
"Module: " + $mod.Name
