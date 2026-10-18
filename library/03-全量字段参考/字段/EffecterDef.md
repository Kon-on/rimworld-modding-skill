# EffecterDef

- **所属线**：表现线
- **原版实例数**：285
- **字段路径数**：82
- **资料片**：Anomaly、Biotech、Core、Ideology、Odyssey、Royalty
- **原版出处**：`Anomaly/Defs/Effects/Effecter_Misc.xml`、`Biotech/Defs/Effects/Effecter_Misc.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<EffecterDef>
    <defName>TestCameraFX</defName>
    <children>
      <li>
        <subEffecterClass>SubEffecter_CameraShakeSingle</subEffecterClass>
        <cameraShake>1</cameraShake>
      </li>
    </children>
  </EffecterDef>


  
```

> 来自 `Anomaly/Defs/Effects/Effecter_Misc.xml`，defName = `TestCameraFX`，XML 节点数 6（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
children                                       [容器]
children/li                                    [容器]
children/li/burstCount                         [数值/文本]  例：1 / 1~1 / 1~4
children/li/fleckDef                           [文本]  例：EnergyCrackle / HoraxianSparks / NociosphereDepartingRing
children/li/positionRadius                     [数值]  例：0 / 0.6 / 1
children/li/scale                              [数值/文本]  例：.15~.25 / 10 / 2
children/li/spawnLocType                       [文本]  例：BetweenPositions / OnSource / OnTarget
children/li/speed                              [数值/文本]  例：0 / 0.6~1.1 / 0.8~1.2
children/li/subEffecterClass                   [文本]  例：SubEffecter_CameraShakeSingle / SubEffecter_SoundTriggered / SubEffecter_SprayerChance
defName                                        [文本]  例：MeatExplosionSmall / MeatExplosionTiny / NociosphereDepartComplete
```

## 三、全量字段表（82 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `children` | 100.0% (285/285) | 容器 |  |
| `children/li` | 241.0% (687/285) | 容器 |  |
| `children/li/absoluteAngle` | 26.7% (76/285) | 布尔 | False / True / false |
| `children/li/airTime` | 3.2% (9/285) | 数值/文本 | 0.02~0.05 / 0.08~0.1 / 0.08~0.16 |
| `children/li/angle` | 70.5% (201/285) | 数值/文本 | 0 / 0~0 / 0~360 |
| `children/li/attachPoint` | 0.7% (2/285) | 文本 | Exhaust |
| `children/li/attachToSpawnThing` | 12.6% (36/285) | 布尔 | true |
| `children/li/avoidLastPositionRadius` | 1.4% (4/285) | 数值 | 0.3 / 0.35 / 1 |
| `children/li/burstCount` | 129.5% (369/285) | 数值/文本 | 1 / 1~1 / 1~4 |
| `children/li/cameraShake` | 3.2% (9/285) | 数值 | .2 / .25 / .5 |
| `children/li/chancePeriodTicks` | 26.0% (74/285) | 数值 | 15 / 20 / 3 |
| `children/li/chancePerTick` | 60.7% (173/285) | 数值 | .05 / .1 / 0.1 |
| `children/li/children` | 2.1% (6/285) | 容器 |  |
| `children/li/children/li` | 7.7% (22/285) | 容器 |  |
| `children/li/children/li/absoluteAngle` | 5.6% (16/285) | 布尔 | False / True |
| `children/li/children/li/angle` | 6.0% (17/285) | 数值/文本 | 0 / 0~0 / 0~360 |
| `children/li/children/li/avoidLastPositionRadius` | 3.5% (10/285) | 数值 | 1 |
| `children/li/children/li/burstCount` | 6.3% (18/285) | 数值/文本 | 1 / 2~4 / 2~6 |
| `children/li/children/li/cameraShake` | 0.7% (2/285) | 文本 | .1~.2 / .1~.3 |
| `children/li/children/li/chancePeriodTicks` | 1.8% (5/285) | 数值 | 30 / 40 / 420 |
| `children/li/children/li/chancePerTick` | 3.9% (11/285) | 数值 | .1 / .25 / .5 |
| `children/li/children/li/color` | 1.8% (5/285) | 文本 | (1, 1, 1, .75) |
| `children/li/children/li/distanceAttenuationMax` | 1.4% (4/285) | 数值 | 20 / 25 / 30 |
| `children/li/children/li/distanceAttenuationScale` | 1.4% (4/285) | 数值 | 1 |
| `children/li/children/li/fleckDef` | 6.3% (18/285) | 文本 | DarkHighlightRing / GroundCrack / Lightshaft |
| `children/li/children/li/fleckUsesAngleForVelocity` | 5.3% (15/285) | 布尔 | False / True |
| `children/li/children/li/initialDelayTicks` | 4.9% (14/285) | 数值 | 0 |
| `children/li/children/li/makeMoteOnSubtrigger` | 5.3% (15/285) | 布尔 | true |
| `children/li/children/li/positionOffset` | 6.3% (18/285) | 文本 | (-.25, 0, -.25) / (-.5, 0, -.5) / (0, 0, 0) |
| `children/li/children/li/positionRadius` | 6.3% (18/285) | 数值 | 0 / 2 / 4 |
| `children/li/children/li/positionRadiusMin` | 4.9% (14/285) | 数值 | 0 / 1 / 2 |
| `children/li/children/li/randomWeight` | 0.4% (1/285) | 数值 | .3 |
| `children/li/children/li/rotation` | 6.3% (18/285) | 数值/文本 | 0 / 0~360 / 15 |
| `children/li/children/li/rotationRate` | 6.3% (18/285) | 数值/文本 | -10~10 / -60~60 / 0 |
| `children/li/children/li/scale` | 7.0% (20/285) | 数值/文本 | .1 / .5~1 / .75~2 |
| `children/li/children/li/soundDef` | 0.7% (2/285) | 文本 | Emergence_Quake |
| `children/li/children/li/spawnLocType` | 6.3% (18/285) | 文本 | OnSource / OnTarget |
| `children/li/children/li/speed` | 6.3% (18/285) | 数值/文本 | .1~1 / .6~.75 / 0 |
| `children/li/children/li/subEffecterClass` | 7.7% (22/285) | 文本 | SubEffecter_CameraShakeChance / SubEffecter_CameraShakeSingle / SubEffecter_SprayerChance |
| `children/li/color` | 14.4% (41/285) | 文本 | (.8, .7, .7, .5) / (1, 0, 0, .25) / (1, 1, 1, .5) |
| `children/li/destroyMoteOnCleanup` | 3.2% (9/285) | 布尔 | True / false / true |
| `children/li/distanceAttenuationMax` | 1.4% (4/285) | 数值 | 10 / 100 |
| `children/li/distanceAttenuationScale` | 2.8% (8/285) | 数值 | .5 / 1 |
| `children/li/fleckDef` | 139.3% (397/285) | 文本 | EnergyCrackle / HoraxianSparks / NociosphereDepartingRing |
| `children/li/fleckUsesAngleForVelocity` | 47.0% (134/285) | 布尔 | False / True / false |
| `children/li/initialDelayTicks` | 25.6% (73/285) | 数值 | 550 / 660 / 69 |
| `children/li/intermittentSoundInterval` | 0.4% (1/285) | 容器 |  |
| `children/li/intermittentSoundInterval/max` | 0.4% (1/285) | 数值 | 4300 |
| `children/li/intermittentSoundInterval/min` | 0.4% (1/285) | 数值 | 750 |
| `children/li/lifespanMaxTicks` | 5.6% (16/285) | 数值 | 1 / 240 / 440 |
| `children/li/makeMoteOnSubtrigger` | 1.4% (4/285) | 布尔 | true |
| `children/li/maxMoteCount` | 4.2% (12/285) | 数值 | 1 / 14 / 3 |
| `children/li/moteDef` | 57.9% (165/285) | 文本 | Mote_MeatExplosionFlyingPiece / Mote_MeatExplosionFlyingSplatter / Mote_MeatExplosionMist |
| `children/li/orbitOrigin` | 2.8% (8/285) | 布尔 | true |
| `children/li/orbitSnapStrength` | 2.8% (8/285) | 数值 | .8 / 1.0 |
| `children/li/orbitSpeed` | 0.7% (2/285) | 文本 | -5~-1 / -6~-1 |
| `children/li/perRotationOffsets` | 1.8% (5/285) | 容器 |  |
| `children/li/perRotationOffsets/li` | 7.0% (20/285) | 文本 | (0, 0, 0) / (0, 1, 0) / -0.72, 0, 0.1 |
| `children/li/positionDimensions` | 2.1% (6/285) | 文本 | (0.32, 0, 0.2) / (0.7, 0, 0.15) / (3.5, 0, 1.3) |
| `children/li/positionLerpFactor` | 20.7% (59/285) | 数值 | .3 / 0.65 / 0.75 |
| `children/li/positionOffset` | 52.6% (150/285) | 文本 | (-.5, 0, -.5) / (0, .1, 0) / (0, 0, 0) |
| `children/li/positionRadius` | 124.2% (354/285) | 数值 | 0 / 0.6 / 1 |
| `children/li/positionRadiusMin` | 32.6% (93/285) | 数值 | 0 / 2 / 3 |
| `children/li/rotateTowardsTargetCenter` | 8.4% (24/285) | 布尔 | True / true |
| `children/li/rotation` | 82.5% (235/285) | 数值/文本 | -150~-150 / -150~150 / 0 |
| `children/li/rotationRate` | 55.4% (158/285) | 数值/文本 | -200~200 / -5~5 / 0 |
| `children/li/scale` | 150.2% (428/285) | 数值/文本 | .15~.25 / 10 / 2 |
| `children/li/soundDef` | 41.8% (119/285) | 文本 | MeatExplosionLarge / MeatExplosionNormal / MeatExplosionSmall |
| `children/li/spawnLocType` | 177.5% (506/285) | 文本 | BetweenPositions / OnSource / OnTarget |
| `children/li/speed` | 110.5% (315/285) | 数值/文本 | 0 / 0.6~1.1 / 0.8~1.2 |
| `children/li/subEffecterClass` | 241.0% (687/285) | 文本 | SubEffecter_CameraShakeSingle / SubEffecter_SoundTriggered / SubEffecter_SprayerChance |
| `children/li/ticksBeforeSustainerStart` | 1.4% (4/285) | 数值 | 120 / 35 / 600 |
| `children/li/ticksBetweenMotes` | 30.5% (87/285) | 数值 | 120 / 2 / 30 |
| `children/li/useTargetABodyAngle` | 0.4% (1/285) | 布尔 | true |
| `children/li/useTargetAInitialRotation` | 3.5% (10/285) | 布尔 | true |
| `children/li/useTargetBInitialRotation` | 1.8% (5/285) | 布尔 | true |
| `defName` | 99.3% (283/285) | 文本 | MeatExplosionSmall / MeatExplosionTiny / NociosphereDepartComplete |
| `maintainTicks` | 8.1% (23/285) | 数值 | 120 / 130 / 60 |
| `offsetMode` | 0.7% (2/285) | 文本 | Free |
| `offsetTowardsTarget` | 2.8% (8/285) | 文本 | 0.25~0.25 / 0.31~0.31 |
| `positionRadius` | 2.8% (8/285) | 数值 | 0.1 |
| `randomWeight` | 1.1% (3/285) | 数值 | .3 / 1 |

## 四、原版 defName 一览（共 285 个，列出前 60）

```text
`TestCameraFX`                    `BabyCrying`                      `LaborEarly`                      `LaborLate`                     
`BandNodeTuning`                  `SubcoreSoftscanner_Start`        `SubcoreRipscanner_Start`         `Radiotalking`                  
`Floordrawing`                    `Breastfeeding`                   `Birth`                           `PlayStatic`                    
`ProgressBar`                     `ProgressBarAlwaysVisible`        `Harvest_MetaOnly`                `CommsConsoleBossgroupSummoned` 
`MechChargerWasteProduced`        `MechChargerWasteRemoved`         `PollutionPumped`                 `PollutionExtractedPoluxTree`   
`WastepackAtomizer_Working`       `BandNodeUntuned`                 `VanishChristmasTree`             `RipScannerHeadGlow`            
`AncientExostriderRemainsPulse`   `AnimalWarcallMentalState`        `EatVegetarian`                   `EatMeat`                       
`Paint`                           `RoofWork`                        `Vomit`                           `ExtinguisherExplosion`         
`ExtinguisherPuffSmall`           `RaisedRock_Collapse`             `ButcherFlesh`                    `ButcherMechanoid`              
`Surgery`                         `CutStone`                        `Tailor`                          `Smith`                         
`Sculpt`                          `MakeWoodPlanks_Hand`             `MakeWoodPlanks_Electric`         `Smelt`                         
`Cook`                            `Cremate`                         `BurnDrug`                        `BiosculpterPod_Ready`          
`MechStabilizerPulse`             `HoraxianSpellLight_Warmup`       `HoraxianSpellDark_Warmup`        `BandNodeRetuning`              
`BandNodeTuned`                   `TunnelerSlowedDown`              `MechUncontrolled`                `AnimalWarcall_CastOnTarget`    
`Impact_Toxic`                    `Smoke_Joint`                     `Smoke_Flake`                     `GiantExplosion`                
```

_余下 225 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
