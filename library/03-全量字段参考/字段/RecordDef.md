# RecordDef

- **所属线**：系统线
- **原版实例数**：70
- **字段路径数**：8
- **资料片**：Anomaly、Biotech、Core
- **原版出处**：`Core/Defs/Misc/RecordDefs/Records_Misc.xml`、`Anomaly/Defs/RecordDefs/Records_Misc.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<RecordDef>
    <defName>ShotsFired</defName>
    <label>shots fired</label>
    <description>The number of shots I have fired.</description>
    <type>Int</type>
  </RecordDef>
  
  
```

> 来自 `Core/Defs/Misc/RecordDefs/Records_Misc.xml`，defName = `ShotsFired`，XML 节点数 5（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Kills / KillsEntities / PawnsDownedEntities
description                                    [文本]  例：The number of creatures I have killed. / The number of entities I have downed. / The number of entities I have killed.
label                                          [文本]  例：enemies downed (entities) / kills / kills (entities)
type                                           [文本]  例：Float / Int / Time
```

## 三、全量字段表（8 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (70/70) | 文本 | Kills / KillsEntities / PawnsDownedEntities |
| `description` | 100.0% (70/70) | 文本 | The number of creatures I have killed. / The number of entities I have downed. / The number of entities I have |
| `displayOrder` | 14.3% (10/70) | 数值 | 0 / 1 |
| `label` | 100.0% (70/70) | 文本 | enemies downed (entities) / kills / kills (entities) |
| `measuredTimeJobs` | 17.1% (12/70) | 容器 |  |
| `measuredTimeJobs/li` | 42.9% (30/70) | 文本 | Ingest / Milk / PredatorHunt |
| `type` | 100.0% (70/70) | 文本 | Float / Int / Time |
| `workerClass` | 18.6% (13/70) | 文本 | RecordWorker_TimeAsChildInColony / RecordWorker_TimeAsColonistOrColonyAnimal / RecordWorker_TimeAsPrisoner |

## 四、原版 defName 一览（共 70 个，列出前 60）

```text
`ShotsFired`                      `Headshots`                       `DamageDealt`                     `DamageTaken`                   
`TimesInMentalState`              `TimesOnFire`                     `FiresExtinguished`               `OperationsReceived`            
`OperationsPerformed`             `TimesTendedTo`                   `TimesTendedOther`                `PeopleCaptured`                
`PrisonersRecruited`              `PrisonersChatted`                `AnimalsTamed`                    `AnimalsSlaughtered`            
`MealsCooked`                     `ThingsConstructed`               `ThingsInstalled`                 `ThingsRepaired`                
`ThingsCrafted`                   `ThingsHauled`                    `PlantsSown`                      `PlantsHarvested`               
`CellsMined`                      `MessesCleaned`                   `ResearchPointsResearched`        `CorpsesBuried`                 
`NutritionEaten`                  `BodiesStripped`                  `ThingsUninstalled`               `ThingsDeconstructed`           
`ArtifactsActivated`              `ContainersOpened`                `SwitchesFlicked`                 `KillsEntities`                 
`PawnsDownedEntities`             `TimeAsChildInColony`             `Kills`                           `KillsHumanlikes`               
`KillsAnimals`                    `KillsMechanoids`                 `PawnsDowned`                     `PawnsDownedHumanlikes`         
`PawnsDownedAnimals`              `PawnsDownedMechanoids`           `TimeAsColonistOrColonyAnimal`    `TimeAsQuestLodger`             
`TimeAsPrisoner`                  `TimeInBed`                       `TimeInBedForMedicalReasons`      `TimeDowned`                    
`TimeGettingJoy`                  `TimeUnderRoof`                   `TimeDrafted`                     `TimeOnFire`                    
`TimeInMentalState`               `TimeHauling`                     `TimeResearching`                 `TimeCleaning`                  
```

_余下 10 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
