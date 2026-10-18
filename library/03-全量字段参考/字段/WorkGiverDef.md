# WorkGiverDef

- **所属线**：系统线
- **原版实例数**：155
- **字段路径数**：33
- **资料片**：Anomaly、Biotech、Core、Ideology、Odyssey
- **原版出处**：`Biotech/Defs/WorkGiverDefs/WorkGivers.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<WorkGiverDef ParentName="HaulToBase">
    <defName>HaulToCarrier</defName>
    <label>haul resources to carrier</label>
    <giverClass>WorkGiver_HaulResourcesToCarrier</giverClass>
  </WorkGiverDef>

  
```

> 来自 `Biotech/Defs/WorkGiverDefs/WorkGivers.xml`，defName = `HaulToCarrier`，XML 节点数 4（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：DoBillsBioferriteShaper / DoBillsSerumCentrifuge / ReleaseEntity
gerund                                         [文本]  例：capturing / releasing / transferring
giverClass                                     [文本]  例：WorkGiver_DoBill / WorkGiver_ReleaseEntity / WorkGiver_TakeEntityToHoldingPlatform
label                                          [文本]  例：capture entity / make things at bioferrite shaper / make things at serum lab
priorityInType                                 [数值]  例：300 / 64 / 65
verb                                           [文本]  例：capture / release / transfer
workType                                       [文本]  例：Crafting / Hauling / Smithing
```

## 三、全量字段表（33 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `autoTakeablePriorityDrafted` | 0.7% (1/155) | 数值 | 20 |
| `billGiversAllAnimals` | 0.7% (1/155) | 布尔 | true |
| `billGiversAllAnimalsCorpses` | 0.7% (1/155) | 布尔 | true |
| `billGiversAllHumanlikes` | 0.7% (1/155) | 布尔 | true |
| `billGiversAllHumanlikesCorpses` | 0.7% (1/155) | 布尔 | true |
| `canBeDoneByMechs` | 20.6% (32/155) | 布尔 | false / true |
| `canBeDoneWhileDrafted` | 3.2% (5/155) | 布尔 | true |
| `defName` | 99.4% (154/155) | 文本 | DoBillsBioferriteShaper / DoBillsSerumCentrifuge / ReleaseEntity |
| `directOrderable` | 1.3% (2/155) | 布尔 | false |
| `doesSmoothing` | 1.3% (2/155) | 布尔 | true |
| `emergency` | 2.6% (4/155) | 布尔 | True / true |
| `equivalenceGroup` | 4.5% (7/155) | 文本 | AssistInConstruction / FeedPatientAnimals / ReleasePrisoner |
| `feedAnimalsOnly` | 0.7% (1/155) | 布尔 | true |
| `feedHumanlikesOnly` | 0.7% (1/155) | 布尔 | true |
| `fixedBillGiverDefs` | 12.9% (20/155) | 容器 |  |
| `fixedBillGiverDefs/li` | 16.1% (25/155) | 文本 | BioferriteShaper / LargeMechGestator / MechGestator |
| `forceFleck` | 0.7% (1/155) | 文本 | FeedbackExtinguish |
| `gerund` | 94.8% (147/155) | 文本 | capturing / releasing / transferring |
| `giverClass` | 98.1% (152/155) | 文本 | WorkGiver_DoBill / WorkGiver_ReleaseEntity / WorkGiver_TakeEntityToHoldingPlatform |
| `label` | 97.4% (151/155) | 文本 | capture entity / make things at bioferrite shaper / make things at serum lab |
| `nonColonistsCanDo` | 4.5% (7/155) | 布尔 | true |
| `prioritizeSustains` | 29.0% (45/155) | 布尔 | true |
| `priorityInType` | 94.2% (146/155) | 数值 | 300 / 64 / 65 |
| `requiredCapacities` | 88.4% (137/155) | 容器 |  |
| `requiredCapacities/li` | 89.7% (139/155) | 文本 | Manipulation / Moving / Talking |
| `scanCells` | 7.7% (12/155) | 布尔 | true |
| `scannerDef` | 1.3% (2/155) | 文本 | GroundPenetratingScanner / LongRangeMineralScanner |
| `scanThings` | 7.7% (12/155) | 布尔 | false |
| `tagToGive` | 4.5% (7/155) | 文本 | Fieldwork / RestingForMedicalReasons |
| `verb` | 94.8% (147/155) | 文本 | capture / release / transfer |
| `workTags` | 1.3% (2/155) | 容器 |  |
| `workTags/li` | 1.3% (2/155) | 文本 | Intellectual / Social |
| `workType` | 94.2% (146/155) | 文本 | Crafting / Hauling / Smithing |

## 四、原版 defName 一览（共 155 个，列出前 60）

```text
`HaulToCarrier`                   `HaulToSubcoreScanner`            `HaulToWastepackAtomizer`         `BasicReleasePrisoner`          
`HandlingFeedPatientAnimals`      `DoctorTendToSelfEmergency`       `TakeRoamingAnimalsToPen`         `RebalanceAnimalsInPens`        
``                                `TakeEntityToHoldingPlatform`     `PatientGoToBedTreatment`         `PatientGoToBedRecuperate`      
`ChangeTreeMode`                  `StudyInteract`                   `EnterGeneExtractor`              `EnterGrowthVat`                
`EnterSubcoreScanner`             `PatientGoToBedEmergencyTreatment`  `Flick`                           `PlantsCut`                     
`StudyArchotechStructures`        `ReleaseEntity`                   `TransferEntity`                  `ActivitySuppression`           
`ExecuteEntity`                   `InterrogatePrisoner`             `FillIn`                          `DeliverHemogenToPrisoner`      
`HaulToGeneBank`                  `PlayWithBaby`                    `ChildcarerTeach`                 `HaulToGrowthVat`               
`EmptyWasteContainer`             `CarryToSubcoreScanner`           `TakeToBedToOperate`              `Open`                          
`EjectFuel`                       `DoExecution`                     `ExecuteGuiltyColonist`           `TakePrisonerToBed`             
`FeedPrisoner`                    `DeliverFoodToPrisoner`           `ChatWithPrisoner`                `Slaughter`                     
`ReleaseToWild`                   `Milk`                            `Shear`                           `CookFillHopper`                
`Uninstall`                       `DeconstructForBlueprint`         `FillIn`                          `Deconstruct`                   
`HelpGatheringItemsForCaravan`    `LoadTransporters`                `HaulToPortal`                    `HaulCorpses`                   
`HaulGeneral`                     `HaulMerge`                       `EmptyEggBox`                     `CleanFilth`                    
```

_余下 95 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
