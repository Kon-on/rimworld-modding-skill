# ConceptDef

- **所属线**：系统线
- **原版实例数**：86
- **字段路径数**：10
- **资料片**：Anomaly、Biotech、Core、Ideology、Odyssey、Royalty
- **原版出处**：`Core/Defs/Tutor/Concepts_NotedOpportunistic.xml`、`Odyssey/Defs/Tutor/Tutor.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<ConceptDef Abstract="True" Name="NotedOpportunisticBase">
    <priority>50</priority>
    <needsOpportunity>True</needsOpportunity>
  </ConceptDef>

  
```

> 来自 `Core/Defs/Tutor/Concepts_NotedOpportunistic.xml`，defName = ``，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：CapturingEntities / ContainingEntities / EntityCodex
helpText                                       [文本]  例：Colonists assigned to 'Dark study' work will STUDY diverse entities including cr / It's best to hold entities in secure chambers with high CONTAINMENT STRENGTH or  / Use the entity codex to track which entities you've discovered.\n\nDiscovering n
label                                          [文本]  例：capturing entities / containing entities / entity codex
```

## 三、全量字段表（10 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 98.8% (85/86) | 文本 | CapturingEntities / ContainingEntities / EntityCodex |
| `gameMode` | 3.5% (3/86) | 文本 | Entry |
| `helpText` | 98.8% (85/86) | 文本 | Colonists assigned to 'Dark study' work will STUDY diverse entities including cr / It's best to hold entities  |
| `helpTextController` | 12.8% (11/86) | 文本 | To rescue a wounded person, select a healthy colonist and then press the left tr / When an enemy is downed on  |
| `highlightTags` | 50.0% (43/86) | 容器 |  |
| `highlightTags/li` | 88.4% (76/86) | 文本 | DesignationCategoryButton-Anomaly-Closed / Designator-Build-HoldingPlatform / ITab-Entity-Closed |
| `label` | 98.8% (85/86) | 文本 | capturing entities / containing entities / entity codex |
| `needsOpportunity` | 23.3% (20/86) | 布尔 | True / true |
| `opportunityDecays` | 3.5% (3/86) | 布尔 | false |
| `priority` | 73.3% (63/86) | 数值 | 15 / 20 / 25 |

## 四、原版 defName 一览（共 86 个，列出前 60）

```text
``                                `ShieldBelts`                     `AnimalsDontAttackDoors`          `TVForSickPeople`               
`DoorOpenSpeed`                   `Rescuing`                        `Capturing`                       `InteractingWithTraders`        
`GroupGotoHereDragging`           `OpeningComms`                    `QueueOrders`                     `CoverAndShooting`              
`SpoilageAndFreezers`             `Deterioration`                   `MedicalOperations`               `GettingMoreTraders`            
`TileInspector`                   `FirePreparation`                 `ShotAccuracyTooltip`             `FriendlyFireSafety`            
`TradeGoodsMustBeNearBeacon`      `ArrestingCreatesEnemies`         `SwitchFlickingDesignation`       `MaxNumberOfPlayerSettlements`  
`TradingRequiresPermit`           `SteamDeckControlsMainMenu`       `SteamDeckControlsGame`           `AnomalyResearch`               
`ColonyGhouls`                    `VoidProvocation`                 `Babies`                          `Children`                      
`Deathrest`                       `GenesAndXenotypes`               `Mechanitors`                     `MechsInCaravans`               
`Drafting`                        `DrugAddiction`                   `PrisonerTab`                     `CameraDolly`                   
`CameraZoom`                      `EquippingWeapons`                `Gravship`                        `Orbit`                         
`Fishing`                         `MeditationDesiredPsyfocus`       `ReformCaravan`                   `BillsTab`                      
`DrugPolicies`                    `SetGrowingZonePlant`             `Shelves`                         `Books`                         
`Pause`                           `Forbidding`                      `Alerts`                          `WorkTab`                       
`ForbiddingDoors`                 `AnimalTraining`                  `InfoCard`                        `StorageTab`                    
```

_余下 26 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
