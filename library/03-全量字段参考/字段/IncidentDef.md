# IncidentDef

- **所属线**：世界线
- **原版实例数**：139
- **字段路径数**：70
- **资料片**：Anomaly、Biotech、Core、Ideology、Odyssey、Royalty
- **原版出处**：`Anomaly/Defs/Storyteller/Incidents_Map_Misc.xml`、`Biotech/Defs/IncidentDefs/Incidents_Map_Special.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<IncidentDef Abstract="True" Name="AnomalyIncidentBase">
    <minAnomalyThreatLevel>0</minAnomalyThreatLevel>
  </IncidentDef>
  
  
```

> 来自 `Anomaly/Defs/Storyteller/Incidents_Map_Misc.xml`，defName = ``，XML 节点数 2（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：DeathPall / MetalhorrorImplantation / UnnaturalDarkness
label                                          [文本]  例：death pall / metalhorror implantation / twisted obelisk
```

## 三、全量字段表（70 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `allowedBiomes` | 7.9% (11/139) | 容器 |  |
| `allowedBiomes/li` | 15.1% (21/139) | 文本 | TemperateForest / TemperateSwamp / TropicalRainforest |
| `baseChance` | 72.7% (101/139) | 数值 | 0.2 / 0.5 / 0.75 |
| `baseChanceWithRoyalty` | 2.9% (4/139) | 数值 | 0.4 / 0.95 / 1.9 |
| `canOccurOnAllPlanetLayers` | 9.3% (13/139) | 布尔 | true |
| `category` | 74.1% (103/139) | 文本 | Misc / Special / ThreatBig |
| `defName` | 94.2% (131/139) | 文本 | DeathPall / MetalhorrorImplantation / UnnaturalDarkness |
| `disabledWhen` | 6.5% (9/139) | 容器 |  |
| `disabledWhen/extremeWeatherIncidentsDisabled` | 6.5% (9/139) | 布尔 | true |
| `disallowedBiomes` | 0.7% (1/139) | 容器 |  |
| `disallowedBiomes/li` | 1.4% (2/139) | 文本 | IceSheet / SeaIce |
| `diseaseDevelopmentStage` | 0.7% (1/139) | 文本 | Adult, Child |
| `diseaseIncident` | 9.3% (13/139) | 文本 | Flu / Malaria / Plague |
| `diseaseLethalLetterText` | 0.7% (1/139) | 文本 | Without a cure or replacement of some kind, {PAWN_labelShort} will die. |
| `diseaseMaxVictims` | 0.7% (1/139) | 数值 | 1 |
| `diseasePartsToAffect` | 1.4% (2/139) | 容器 |  |
| `diseasePartsToAffect/li` | 2.9% (4/139) | 文本 | Heart / Kidney / Lung |
| `diseaseVictimFractionRange` | 2.9% (4/139) | 文本 | 0.2~0.5 / 0.3~0.7 / 0~0.2 |
| `durationDays` | 12.2% (17/139) | 文本 | 0.33~1.5 / 1.5~3.0 / 1~2 |
| `earliestDay` | 19.4% (27/139) | 数值 | 15 / 30 / 45 |
| `gameCondition` | 12.2% (17/139) | 文本 | BloodRain / DeathPall / NoxiousHaze |
| `hidden` | 2.9% (4/139) | 布尔 | true |
| `ignoreRecentSelectionWeighting` | 2.2% (3/139) | 布尔 | true |
| `label` | 93.5% (130/139) | 文本 | death pall / metalhorror implantation / twisted obelisk |
| `layerWhitelist` | 0.7% (1/139) | 容器 |  |
| `layerWhitelist/li` | 0.7% (1/139) | 文本 | Orbit |
| `letterDef` | 36.7% (51/139) | 文本 | NeutralEvent / PositiveEvent / ThreatBig |
| `letterHyperlinkHediffDefs` | 1.4% (2/139) | 容器 |  |
| `letterHyperlinkHediffDefs/li` | 1.4% (2/139) | 文本 | Scaria |
| `letterLabel` | 54.0% (75/139) | 文本 | Corrupted obelisk / Death pall / Twisted obelisk |
| `letterSingularForm` | 0.7% (1/139) | 布尔 | true |
| `letterText` | 28.8% (40/139) | 文本 | A mysterious obelisk has crashed nearby.\n\nThe obelisk hums with putrid psychic / A small circle of terrain h |
| `letterTextPlural` | 1.4% (2/139) | 文本 | Harbinger trees have sprouted nearby. These gnarled trees grow flesh-like coveri / Several sinkholes have star |
| `mechClusterBuilding` | 1.4% (2/139) | 文本 | DefoliatorShipPart / PsychicDronerShipPart |
| `minAnomalyThreatLevel` | 20.9% (29/139) | 数值 | 0 / 1 / 2 |
| `minGreatestPopulation` | 1.4% (2/139) | 数值 | 3 |
| `minPopulation` | 3.6% (5/139) | 数值 | 4 / 5 |
| `minRefireDays` | 36.7% (51/139) | 数值 | 120 / 30 / 45 |
| `minThreatPoints` | 12.2% (17/139) | 数值 | 200 / 250 / 300 |
| `mtbDaysByBiome` | 2.9% (4/139) | 容器 |  |
| `mtbDaysByBiome/AridShrubland` | 2.9% (4/139) | 数值 | 10 / 20 |
| `mtbDaysByBiome/BorealForest` | 2.9% (4/139) | 数值 | 10 / 20 |
| `mtbDaysByBiome/ColdBog` | 2.9% (4/139) | 数值 | 25 / 35 |
| `mtbDaysByBiome/Desert` | 2.9% (4/139) | 数值 | 15 / 30 |
| `mtbDaysByBiome/ExtremeDesert` | 2.9% (4/139) | 数值 | 25 / 35 |
| `mtbDaysByBiome/IceSheet` | 2.9% (4/139) | 数值 | 35 / 40 |
| `mtbDaysByBiome/SeaIce` | 2.9% (4/139) | 数值 | 60 / 80 |
| `mtbDaysByBiome/TemperateForest` | 2.9% (4/139) | 数值 | 10 / 20 |
| `mtbDaysByBiome/TemperateSwamp` | 2.9% (4/139) | 数值 | 15 / 30 |
| `mtbDaysByBiome/TropicalRainforest` | 2.9% (4/139) | 数值 | 10 / 20 |
| `mtbDaysByBiome/TropicalSwamp` | 2.9% (4/139) | 数值 | 15 / 30 |
| `mtbDaysByBiome/Tundra` | 2.9% (4/139) | 数值 | 15 / 30 |
| `pawnFixedGender` | 1.4% (2/139) | 文本 | Male |
| `pawnKind` | 2.2% (3/139) | 文本 | StrangerInBlack / Villager |
| `pawnMustBeCapableOfViolence` | 1.4% (2/139) | 布尔 | true |
| `pointsScaleable` | 19.4% (27/139) | 布尔 | true |
| `populationEffect` | 4.3% (6/139) | 文本 | IncreaseEasy / IncreaseHard / IncreaseMedium |
| `questScriptDef` | 17.3% (24/139) | 文本 | CreepJoinerArrival / CreepJoinerArrival_Metalhorror / MysteriousCargoUnnaturalCorpse |
| `refireCheckTags` | 3.6% (5/139) | 容器 |  |
| `refireCheckTags/li` | 3.6% (5/139) | 文本 | CreepjoinerJoin / MechanoidShip / WastepackInfestation |
| `requireColonistsPresent` | 11.5% (16/139) | 布尔 | True / true |
| `tags` | 1.4% (2/139) | 容器 |  |
| `tags/li` | 1.4% (2/139) | 文本 | MechanoidShip |
| `tale` | 18.0% (25/139) | 文本 | DeathPall / NoxiousHaze / Raid |
| `targetTags` | 72.7% (101/139) | 容器 |  |
| `targetTags/li` | 85.6% (119/139) | 文本 | Map_Misc / Map_PlayerHome / Map_RaidBeacon |
| `treeDef` | 2.2% (3/139) | 文本 | Plant_TreeAnima / Plant_TreeHarbinger / Plant_TreePolux |
| `treeGenStepDef` | 2.2% (3/139) | 文本 | AnimaTrees / HarbingerTrees / PoluxTrees |
| `treeGrowth` | 2.2% (3/139) | 数值 | 0.05 / 0.15 |
| `workerClass` | 79.9% (111/139) | 文本 | IncidentWorker_DeathPall / IncidentWorker_GiveQuest / IncidentWorker_MetalhorrorImplantation |

## 四、原版 defName 一览（共 139 个，列出前 60）

```text
``                                `MysteriousCargoUnnaturalCorpse`  `MysteriousCargoCube`             `MysteriousCargoRevenantSpine`  
`WarpedObelisk_Mutator`           `WarpedObelisk_Duplicator`        `WarpedObelisk_Abductor`          ``                              
`DevourerWaterAssault`            `Disease_Flu`                     `Disease_Plague`                  `Disease_Malaria`               
`Disease_SleepingSickness`        `Disease_FibrousMechanites`       `Disease_SensoryMechanites`       `Disease_MuscleParasites`       
`Disease_AnimalFlu`               `Disease_AnimalPlague`            `GiveQuest_Random`                ``                              
`GiveQuest_EndGame_RoyalAscent`   `GiveQuest_Intro_Wimp`            `GiveQuest_Intro_Deserter`        ``                              
`ShamblerSwarm`                   `ShamblerSwarmAnimals`            `ChimeraAssault`                  `Disease_GutWorms`              
`GiveQuest_EndGame_ShipEscape`    `GiveQuest_EndGame_ArchonexusVictory`  `RefugeePodCrash_Ghoul`           `FarmAnimalsWanderIn`           
`GiveQuest_WorkSite`              `Disease_Abasia`                  `Disease_BloodRot`                `VoidCuriosity`                 
`SmallShamblerSwarm`              `ResourcePodCrash`                `SelfTame`                        `ThrumboPasses`                 
`ShipChunkDrop`                   `TraderCaravanArrival`            `AnimalInsanitySingle`            ``                              
`SeasonalFlooding`                ``                                `GiveQuest_DistressCall`          `UnnaturalCorpseArrival`        
`HarbingerTreeProvoked`           `SightstealerSwarm`               `FrenziedAnimals`                 `GorehulkAssault`               
`DevourerAssault`                 `RefugeePodCrash_Baby`            `ShortCircuit`                    `CropBlight`                    
`OrbitalTraderArrival`            `VisitorGroup`                    `TravelerGroup`                   `AnimalInsanityMass`            
```

_余下 79 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
