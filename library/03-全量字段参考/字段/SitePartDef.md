# SitePartDef

- **所属线**：世界线
- **原版实例数**：64
- **字段路径数**：45
- **资料片**：Anomaly、Biotech、Core、Ideology、Odyssey、Royalty
- **原版出处**：`Odyssey/Defs/Sites/GravcoreLocations.xml`、`Odyssey/Defs/Sites/BanditGang.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<SitePartDef Name="SpaceGravcoreLocationBase" ParentName="GravcoreLocationBase" Abstract="True">
    <leaveAbandonedSettlement>false</leaveAbandonedSettlement>
  </SitePartDef>
  
  
```

> 来自 `Odyssey/Defs/Sites/GravcoreLocations.xml`，defName = ``，XML 节点数 2（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
tags/li                                        [文本]  例：AncientComplex_Mechanitor / DistressCall / ItemStashQuestThreat
```

## 三、全量字段表（45 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `activeThreatDisturbanceFactor` | 3.1% (2/64) | 数值 | 0.2 / 0.4 |
| `applyFactionColorToSiteTexture` | 7.8% (5/64) | 布尔 | true |
| `approachingReportString` | 14.1% (9/64) | 文本 | Attacking {0}. / Investigating {0}. |
| `approachOrderString` | 15.6% (10/64) | 文本 | Attack {0} / Investigate {0} |
| `arrivedLetter` | 14.1% (9/64) | 文本 | There are a few sleeping hostile mechanoids in this area.\n\nThe mechanoids may  / There are enemy turrets in  |
| `arrivedLetterDef` | 18.8% (12/64) | 文本 | NegativeEvent / NeutralEvent |
| `arrivedLetterHediffHyperlinks` | 1.6% (1/64) | 容器 |  |
| `arrivedLetterHediffHyperlinks/li` | 1.6% (1/64) | 文本 | Scaria |
| `badEvenIfNoMap` | 3.1% (2/64) | 布尔 | true |
| `conditionCauserDef` | 12.5% (8/64) | 文本 | SmokeSpewer / SunBlocker / ToxicSpewer |
| `considerEnteringAsAttack` | 12.5% (8/64) | 布尔 | false |
| `copyQuestName` | 7.8% (5/64) | 布尔 | true |
| `defaultHidden` | 3.1% (2/64) | 布尔 | true |
| `defName` | 89.1% (57/64) | 文本 | AmbushEdge / AmbushHidden / AncientComplex_Mechanitor |
| `description` | 81.2% (52/64) | 文本 | A bandit camp. / An ambush. / An ancient complex containing the corpse of a mechanitor. You can try to penetra |
| `disallowsAutomaticDetectionTimerStart` | 9.4% (6/64) | 布尔 | true |
| `displayOnInspectPane` | 1.6% (1/64) | 布尔 | false |
| `excludesTags` | 10.9% (7/64) | 容器 |  |
| `excludesTags/li` | 35.9% (23/64) | 文本 | Manhunters / MechCluster / MechClusterForceNoConditionCauser |
| `expandingIconTexture` | 56.2% (36/64) | 文本 | World/WorldObjects/Expanding/Sites/Ambush / World/WorldObjects/Expanding/Sites/AncientMechanitorComplex / Worl |
| `forceExitAndRemoveMapCountdownDurationDays` | 4.7% (3/64) | 数值 | 11 / 16 / 6 |
| `forceMutators` | 1.6% (1/64) | 容器 |  |
| `forceMutators/li` | 1.6% (1/64) | 文本 | Cavern |
| `gravShipsCanLandOn` | 32.8% (21/64) | 布尔 | false / true |
| `handlesWorldObjectTimeoutInspectString` | 6.2% (4/64) | 布尔 | true |
| `ignoreIllegalLabelCharacterConfigError` | 3.1% (2/64) | 布尔 | true |
| `increasesPopulation` | 3.1% (2/64) | 布尔 | true |
| `label` | 79.7% (51/64) | 文本 | ambush / ancient mechanitor complex / bandit camp |
| `leaveAbandonedSettlement` | 3.1% (2/64) | 布尔 | false / true |
| `lootTable` | 3.1% (2/64) | 容器 |  |
| `lootTable/li` | 7.8% (5/64) | 容器 |  |
| `lootTable/li/thing` | 7.8% (5/64) | 文本 | ComponentIndustrial / Gold / Silver |
| `lootTable/li/weight` | 7.8% (5/64) | 数值 | 0.25 / 0.5 / 1 |
| `mainPartAllThreatsLabel` | 6.2% (4/64) | 容器/文本 | Contains: Grav engine / Contains: Gravcore / Hostile activity detected. |
| `minFactionTechLevel` | 1.6% (1/64) | 文本 | Industrial |
| `minMapSize` | 14.1% (9/64) | 文本 | (200, 0, 200) / (250, 1, 250) |
| `minThreatPoints` | 7.8% (5/64) | 数值 | 300 / 350 / 400 |
| `requiresFaction` | 9.4% (6/64) | 布尔 | true |
| `selectionWeight` | 7.8% (5/64) | 数值 | 1 / 2 / 4 |
| `showFactionInInspectString` | 7.8% (5/64) | 布尔 | true |
| `siteTexture` | 40.6% (26/64) | 文本 | World/WorldObjects/Sites/GenericSite / World/WorldObjects/Sites/GravcoreLocation / World/WorldObjects/Sites/Gr |
| `tags` | 67.2% (43/64) | 容器 |  |
| `tags/li` | 120.3% (77/64) | 文本 | AncientComplex_Mechanitor / DistressCall / ItemStashQuestThreat |
| `wantsThreatPoints` | 29.7% (19/64) | 布尔 | true |
| `workerClass` | 51.6% (33/64) | 文本 | SitePartWorker_Ambush / SitePartWorker_AncientComplex / SitePartWorker_DistressCall_Fleshbeasts |

## 四、原版 defName 一览（共 64 个，列出前 60）

```text
``                                `DistressCall_Fleshbeasts`        `OpportunitySite_AncientLaunchSite`  `OpportunitySite_AncientGarrison`
`OpportunitySite_AncientChemfuelRefinery`  `OpportunitySite_AncientWarehouse`  `OpportunitySite_AncientInfestedSettlement`  ``                              
`MechClusterForceNoConditionCauser`  `SmokeSpewer`                     `ToxicSpewer`                     `WorkSite_Hunting`              
`WorkSite_Farming`                `AncientReactor`                  `OrbitalMechanoidPlatform`        `AncientStockpile`              
`CrashedMechanoidPlatform`        `OrbitalAncientPlatform`          `FrozenTerraformer`               `PsychicDroner`                 
`PsychicSuppressor`               `BanditCamp`                      `OrbitalFugitivePlatform`         `AbandonedSettlement`           
`MechanoidRelay`                  `WeatherController`               `ClimateAdjuster`                 `EMIDynamo`                     
`Opportunity_MechanoidPlatform`   `OpportunitySite_Satellite`       `PossibleUnknownThreatMarker`     ``                              
`BanditGang`                      `InsectLair`                      `Opportunity_AbandonedPlatform`   `Opportunity_OrbitalWreck`      
`WorkSite_Logging`                ``                                `OrbitalMechhive`                 ``                              
`SunBlocker`                      `ItemStash`                       `AlphaThrumboSighting`            `PreciousLump`                  
`Archonexus`                      `WorshippedTerminal`              `GravshipWreckage`                `Opportunity_SurveySite`        
`DownedRefugee`                   `PrisonerWillingToJoin`           `AncientComplex_Mechanitor`       `AncientAltar`                  
``                                `AncientComplex`                  ``                                `SleepingMechanoids`            
`MechCluster`                     `AmbushEdge`                      `AmbushHidden`                    `Manhunters`                    
```

_余下 4 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
