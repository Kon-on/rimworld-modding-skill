# SoundDef

- **所属线**：表现线
- **原版实例数**：1233
- **字段路径数**：113
- **资料片**：Anomaly、Biotech、Core、Ideology、Odyssey、Royalty
- **原版出处**：`Core/Defs/SoundDefs/UI_Oneshots_Designation.xml`、`Anomaly/Defs/SoundDefs/Pawn_Devourer_Vox.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<SoundDef ParentName="Designate_DragStandard_Changed">
    <defName>Designate_DragStandard_Changed_NoCam</defName>
  </SoundDef>

  
```

> 来自 `Core/Defs/SoundDefs/UI_Oneshots_Designation.xml`，defName = `Designate_DragStandard_Changed_NoCam`，XML 节点数 2（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：FleshmassHeart_Destroyed / FleshmassHeart_Throb / Fleshmass_Damaged
subSounds                                      [容器]
subSounds/li                                   [容器]
subSounds/li/grains                            [容器]
subSounds/li/grains/li                         [容器]
subSounds/li/volumeRange                       [数值/文本]  例：10 / 10~15 / 20~25
```

## 三、全量字段表（113 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `context` | 88.1% (1086/1233) | 文本 | MapOnly / WorldOnly |
| `defName` | 99.8% (1231/1233) | 文本 | FleshmassHeart_Destroyed / FleshmassHeart_Throb / Fleshmass_Damaged |
| `maxSimultaneous` | 47.0% (580/1233) | 数值 | 1 / 2 / 3 |
| `maxVoices` | 7.7% (95/1233) | 数值 | 1 / 15 / 2 |
| `priorityMode` | 25.9% (320/1233) | 文本 | PrioritizeExisting / PrioritizeNearest |
| `slot` | 0.2% (2/1233) | 文本 | Radio |
| `subSounds` | 99.8% (1230/1233) | 容器 |  |
| `subSounds/li` | 102.0% (1258/1233) | 容器 |  |
| `subSounds/li/canVacuumDampen` | 0.1% (1/1233) | 布尔 | false |
| `subSounds/li/distRange` | 50.4% (622/1233) | 文本 | 15~30 / 15~60 / 25~50 |
| `subSounds/li/distRange/max` | 0.2% (2/1233) | 数值 | 20 / 200 |
| `subSounds/li/distRange/min` | 0.2% (2/1233) | 数值 | 100 / 5 |
| `subSounds/li/filters` | 0.6% (7/1233) | 容器 |  |
| `subSounds/li/filters/li` | 0.6% (7/1233) | 容器 |  |
| `subSounds/li/filters/li/baseSetup` | 0.1% (1/1233) | 容器 |  |
| `subSounds/li/filters/li/baseSetup/decayHFRatio` | 0.1% (1/1233) | 数值 | 0.5 |
| `subSounds/li/filters/li/baseSetup/decayTime` | 0.1% (1/1233) | 数值 | 1 |
| `subSounds/li/filters/li/baseSetup/density` | 0.1% (1/1233) | 数值 | 100 |
| `subSounds/li/filters/li/baseSetup/diffusion` | 0.1% (1/1233) | 数值 | 100 |
| `subSounds/li/filters/li/baseSetup/dryLevel` | 0.1% (1/1233) | 数值 | 0 |
| `subSounds/li/filters/li/baseSetup/hfReference` | 0.1% (1/1233) | 数值 | 5000 |
| `subSounds/li/filters/li/baseSetup/lfReference` | 0.1% (1/1233) | 数值 | 250 |
| `subSounds/li/filters/li/baseSetup/reflectionsDelay` | 0.1% (1/1233) | 数值 | 0 |
| `subSounds/li/filters/li/baseSetup/reflectionsLevel` | 0.1% (1/1233) | 数值 | -10000 |
| `subSounds/li/filters/li/baseSetup/reverbDelay` | 0.1% (1/1233) | 数值 | 0.04 |
| `subSounds/li/filters/li/baseSetup/reverbLevel` | 0.1% (1/1233) | 数值 | 0 |
| `subSounds/li/filters/li/baseSetup/room` | 0.1% (1/1233) | 数值 | 0 |
| `subSounds/li/filters/li/baseSetup/roomHF` | 0.1% (1/1233) | 数值 | 0 |
| `subSounds/li/filters/li/baseSetup/roomLF` | 0.1% (1/1233) | 数值 | 0 |
| `subSounds/li/filters/li/cutoffFrequency` | 0.3% (4/1233) | 数值 | 10000 / 2180.26 / 50 |
| `subSounds/li/filters/li/decayRatio` | 0.2% (2/1233) | 数值 | 0.5433328 |
| `subSounds/li/filters/li/delay` | 0.2% (2/1233) | 数值 | 1112.654 |
| `subSounds/li/filters/li/dryMix` | 0.2% (2/1233) | 数值 | 1 |
| `subSounds/li/filters/li/lowpassResonaceQ` | 0.2% (3/1233) | 数值 | 1 |
| `subSounds/li/filters/li/wetMix` | 0.2% (2/1233) | 数值 | 0.1333435 |
| `subSounds/li/gameSpeedRange` | 2.4% (29/1233) | 数值/文本 | 0~2 / 1 / 1~2 |
| `subSounds/li/grains` | 102.0% (1258/1233) | 容器 |  |
| `subSounds/li/grains/li` | 102.2% (1260/1233) | 容器 |  |
| `subSounds/li/grains/li/clipFolderPath` | 65.6% (809/1233) | 文本 | Building/Fleshmass/Damaged / Building/Fleshmass/Destroyed / Building/FleshmassHeart/Destroyed |
| `subSounds/li/grains/li/clipPath` | 36.6% (451/1233) | 文本 | Building/FleshmassHeart/Emergence_Point_Fleshmass_Heart_Loop_A / Building/FleshmassHeart/Fleshmass_Heart_Ambie |
| `subSounds/li/grains/li/forceToMono` | 0.4% (5/1233) | 布尔 | false |
| `subSounds/li/muteWhenPaused` | 19.0% (234/1233) | 布尔 | True / true |
| `subSounds/li/name` | 1.7% (21/1233) | 容器/文本 | Main / RageSpeed / Shot |
| `subSounds/li/onCamera` | 15.2% (188/1233) | 布尔 | True / true |
| `subSounds/li/paramMappings` | 2.4% (29/1233) | 容器 |  |
| `subSounds/li/paramMappings/li` | 5.3% (65/1233) | 容器 |  |
| `subSounds/li/paramMappings/li/curve` | 3.6% (45/1233) | 容器 |  |
| `subSounds/li/paramMappings/li/curve/points` | 3.6% (45/1233) | 容器 |  |
| `subSounds/li/paramMappings/li/curve/points/li` | 9.7% (120/1233) | 文本 | (0,0.93) / (0,500) / (1,1.07) |
| `subSounds/li/paramMappings/li/curve/points/li/loc` | 9.4% (116/1233) | 容器 |  |
| `subSounds/li/paramMappings/li/curve/points/li/loc/x` | 9.4% (116/1233) | 数值 | 0 / 1 / 40.93931 |
| `subSounds/li/paramMappings/li/curve/points/li/loc/y` | 9.4% (116/1233) | 数值 | -0.001349449 / 0 / 0.9981107 |
| `subSounds/li/paramMappings/li/inParam` | 5.3% (65/1233) | 容器 |  |
| `subSounds/li/paramMappings/li/inParam/defaultValue` | 1.0% (12/1233) | 数值 | 0 / 1 / 2000 |
| `subSounds/li/paramMappings/li/inParam/inParamName` | 1.0% (12/1233) | 文本 | LerpFactor / PowerOutput / TimeSinceDrag |
| `subSounds/li/paramMappings/li/inParam/timeType` | 0.1% (1/1233) | 文本 | Ticks |
| `subSounds/li/paramMappings/li/outParam` | 5.3% (65/1233) | 容器 |  |
| `subSounds/li/paramMappings/li/outParam/baseSetup` | 0.1% (1/1233) | 容器 |  |
| `subSounds/li/paramMappings/li/outParam/baseSetup/decayHFRatio` | 0.1% (1/1233) | 数值 | 0.1 |
| `subSounds/li/paramMappings/li/outParam/baseSetup/decayTime` | 0.1% (1/1233) | 数值 | 0.17 |
| `subSounds/li/paramMappings/li/outParam/baseSetup/density` | 0.1% (1/1233) | 数值 | 100 |
| `subSounds/li/paramMappings/li/outParam/baseSetup/diffusion` | 0.1% (1/1233) | 数值 | 100 |
| `subSounds/li/paramMappings/li/outParam/baseSetup/dryLevel` | 0.1% (1/1233) | 数值 | 0 |
| `subSounds/li/paramMappings/li/outParam/baseSetup/hfReference` | 0.1% (1/1233) | 数值 | 5000 |
| `subSounds/li/paramMappings/li/outParam/baseSetup/lfReference` | 0.1% (1/1233) | 数值 | 250 |
| `subSounds/li/paramMappings/li/outParam/baseSetup/reflectionsDelay` | 0.1% (1/1233) | 数值 | 0 |
| `subSounds/li/paramMappings/li/outParam/baseSetup/reflectionsLevel` | 0.1% (1/1233) | 数值 | -1204 |
| `subSounds/li/paramMappings/li/outParam/baseSetup/reverbDelay` | 0.1% (1/1233) | 数值 | 0.002 |
| `subSounds/li/paramMappings/li/outParam/baseSetup/reverbLevel` | 0.1% (1/1233) | 数值 | 207 |
| `subSounds/li/paramMappings/li/outParam/baseSetup/room` | 0.1% (1/1233) | 数值 | -1000 |
| `subSounds/li/paramMappings/li/outParam/baseSetup/roomHF` | 0.1% (1/1233) | 数值 | -6000 |
| `subSounds/li/paramMappings/li/outParam/baseSetup/roomLF` | 0.1% (1/1233) | 数值 | 0 |
| `subSounds/li/paramMappings/li/outParam/filterProperty` | 0.2% (3/1233) | 文本 | Cutoff |
| `subSounds/li/paramMappings/li/outParam/pitchType` | 0.1% (1/1233) | 文本 | Multiply |
| `subSounds/li/paramMappings/li/outParam/targetSetup` | 0.1% (1/1233) | 容器 |  |
| `subSounds/li/paramMappings/li/outParam/targetSetup/decayHFRatio` | 0.1% (1/1233) | 数值 | 0.7 |
| `subSounds/li/paramMappings/li/outParam/targetSetup/decayTime` | 0.1% (1/1233) | 数值 | 3.92 |
| `subSounds/li/paramMappings/li/outParam/targetSetup/density` | 0.1% (1/1233) | 数值 | 100 |
| `subSounds/li/paramMappings/li/outParam/targetSetup/diffusion` | 0.1% (1/1233) | 数值 | 100 |
| `subSounds/li/paramMappings/li/outParam/targetSetup/dryLevel` | 0.1% (1/1233) | 数值 | 0 |
| `subSounds/li/paramMappings/li/outParam/targetSetup/hfReference` | 0.1% (1/1233) | 数值 | 5000 |
| `subSounds/li/paramMappings/li/outParam/targetSetup/lfReference` | 0.1% (1/1233) | 数值 | 250 |
| `subSounds/li/paramMappings/li/outParam/targetSetup/reflectionsDelay` | 0.1% (1/1233) | 数值 | 0 |
| `subSounds/li/paramMappings/li/outParam/targetSetup/reflectionsLevel` | 0.1% (1/1233) | 数值 | -1230 |
| `subSounds/li/paramMappings/li/outParam/targetSetup/reverbDelay` | 0.1% (1/1233) | 数值 | 0.029 |
| `subSounds/li/paramMappings/li/outParam/targetSetup/reverbLevel` | 0.1% (1/1233) | 数值 | -2 |
| `subSounds/li/paramMappings/li/outParam/targetSetup/room` | 0.1% (1/1233) | 数值 | -1000 |
| `subSounds/li/paramMappings/li/outParam/targetSetup/roomHF` | 0.1% (1/1233) | 数值 | -500 |
| `subSounds/li/paramMappings/li/outParam/targetSetup/roomLF` | 0.1% (1/1233) | 数值 | 0 |
| `subSounds/li/paramMappings/li/paramUpdateMode` | 3.6% (45/1233) | 文本 | Constant |
| `subSounds/li/pitchRange` | 55.4% (683/1233) | 数值/文本 | 0.85~1.15 / 0.95~1.05 / 0.9770588~1.137647 |
| `subSounds/li/randomStartPoint` | 0.7% (9/1233) | 布尔 | true |
| `subSounds/li/repeatMode` | 7.3% (90/1233) | 文本 | Any / NeverLastHalf / NeverTwice |
| `subSounds/li/startDelayRange` | 0.9% (11/1233) | 数值/文本 | 1 / 1.15 / 4 |
| `subSounds/li/sustainAttack` | 4.1% (51/1233) | 数值 | 2 / 2.5 / 3 |
| `subSounds/li/sustainIntervalFactorByAggregateSize` | 0.1% (1/1233) | 容器 |  |
| `subSounds/li/sustainIntervalFactorByAggregateSize/points` | 0.1% (1/1233) | 容器 |  |
| `subSounds/li/sustainIntervalFactorByAggregateSize/points/li` | 0.2% (3/1233) | 容器 |  |
| `subSounds/li/sustainIntervalFactorByAggregateSize/points/li/loc` | 0.2% (3/1233) | 容器 |  |
| `subSounds/li/sustainIntervalFactorByAggregateSize/points/li/loc/x` | 0.2% (3/1233) | 数值 | 1 / 10 / 100 |
| `subSounds/li/sustainIntervalFactorByAggregateSize/points/li/loc/y` | 0.2% (3/1233) | 数值 | 1 / 2 / 3 |
| `subSounds/li/sustainIntervalRange` | 5.4% (67/1233) | 数值/文本 | 0.5~2 / 1~3 / 3~5 |
| `subSounds/li/sustainLoop` | 40.4% (498/1233) | 布尔 | False / false / true |
| `subSounds/li/sustainLoopDurationRange` | 1.3% (16/1233) | 数值/文本 | 0.7166 / 10~20 / 12 |
| `subSounds/li/sustainRelease` | 2.8% (35/1233) | 数值 | 0.125 / 1 / 2 |
| `subSounds/li/sustainSkipFirstAttack` | 1.3% (16/1233) | 布尔 | False / false |
| `subSounds/li/tempoAffectedByGameSpeed` | 4.7% (58/1233) | 布尔 | false / true |
| `subSounds/li/volumeRange` | 99.8% (1230/1233) | 数值/文本 | 10 / 10~15 / 20~25 |
| `sustain` | 20.3% (250/1233) | 布尔 | False / True / false |
| `sustainFadeoutStartSound` | 0.2% (2/1233) | 文本 | Pawn_Shambler_RiseEnd / ShieldMech_Complete |
| `sustainFadeoutTime` | 1.5% (19/1233) | 数值 | 0.1 / 0.25 / 1 |
| `sustainStartSound` | 1.5% (19/1233) | 文本 | BioferriteHarvester_AmbientStart / GeothermalPlant_Ambience_Start / RepairMech_Remote_Start |
| `sustainStopSound` | 1.9% (23/1233) | 文本 | BioferriteHarvester_AmbientStop / FleshbeastDigging_End / FleshmassHeart_Emerge_End |

## 四、原版 defName 一览（共 1233 个，列出前 60）

```text
`Designate_DragStandard_Changed_NoCam`  `Designate_DragStandard_Changed`  ``                                `Designate_DragStandard`        
`VoidStructure_Activate`          `PitGateOpen`                     `FlareImpact`                     `DeadlifeRelease`               
`MechBandShockwave`               `PollutionPumped`                 `PollutionExtractedPoluxTree`     `Hacking_Started`               
`Hacking_Completed`               `Hacking_Suspended`               `Standard_Reload`                 ``                              
`ToxicShellLanded`                `Interact_Revolver`               `Interact_Autopistol`             `Shot_ChargeRifle`              
`RocketswarmLauncher_Fire`        `AncientRelicRoomReveal`          `AncientRelicTakenAlarm`          `GibbetCage_CorpsePlaced`       
`AncientCommsConsoleActivated`    `DryadCasteSet`                   `PsychicEntropyOverloaded`        `PsychicEntropyHyperloaded`     
`PsychicEntropyBrainCharring`     `PsychicEntropyBrainRoasting`     `Psycast_WordOf_Effect`           `SpitterSpawn`                  
`SpitterSpit`                     `SpitterSpitLands`                `FleshmassBirth`                  `GrayBoxOpening`                
`VoidNode_Explode`                `PitBurrow_Collapse`              `BioferriteHarvester_AmbientStart`  `BioferriteHarvester_AmbientStop`
`EntityChainHigh`                 `EntityChainLow`                  `VoidMonolith_ActivatedL0L1`      `VoidMonolith_ActivateL1L2`     
`VoidMonolith_ActivatedL1L2`      `VoidMonolith_ActivateL2L3`       `AgonyPulse_Cast`                 `FleshmelterBolt_Blast`         
`DarknessDamage`                  `TraversePitGate`                 `Zap_Loud`                        `Zap_Quiet`                     
`MechlinkInstalled`               `Birth`                           `HumanPregnancy`                  `MechSelfShutdown`              
`WarUrchinSpawned`                `MechResurrectCast`               `LetterArrive_Bossgroup`          `DatacoreRead`                  
```

_余下 1173 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
