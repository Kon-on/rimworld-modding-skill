# PawnColumnDef

- **所属线**：表现线
- **原版实例数**：52
- **字段路径数**：14
- **资料片**：Biotech、Core、Ideology、Odyssey
- **原版出处**：`Core/Defs/Misc/PawnColumnDefs/PawnColumns_CopyPaste.xml`、`Core/Defs/Misc/PawnColumnDefs/PawnColumns_Misc.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<PawnColumnDef>
    <defName>CopyPasteWorkPriorities</defName>
    <workerClass>PawnColumnWorker_CopyPasteWorkPriorities</workerClass>
  </PawnColumnDef>

  
```

> 来自 `Core/Defs/Misc/PawnColumnDefs/PawnColumns_CopyPaste.xml`，defName = `CopyPasteWorkPriorities`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：AutoRepair / Energy / Overseer
workerClass                                    [文本]  例：PawnColumnWorker_AutoRepair / PawnColumnWorker_Energy / PawnColumnWorker_Overseer
```

## 三、全量字段表（14 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (52/52) | 文本 | AutoRepair / Energy / Overseer |
| `gap` | 7.7% (4/52) | 数值 | 10 / 17 / 26 |
| `groupable` | 3.9% (2/52) | 布尔 | true |
| `headerIcon` | 36.5% (19/52) | 文本 | UI/Designators/ReleaseToTheWild / UI/Icons/Animal/Slaughter / UI/Icons/Animal/Sterile |
| `headerTip` | 38.5% (20/52) | 文本 | Allowed areas only apply for mechs in work and recharge modes. / Slaughter / Sterilize |
| `ignoreWhenCalculatingOptimalTableSize` | 1.9% (1/52) | 布尔 | true |
| `label` | 32.7% (17/52) | 文本 | auto repair / control group / energy |
| `paintable` | 25.0% (13/52) | 布尔 | true |
| `showIcon` | 1.9% (1/52) | 布尔 | true |
| `sortable` | 63.5% (33/52) | 布尔 | false / true |
| `useLabelShort` | 1.9% (1/52) | 布尔 | true |
| `width` | 5.8% (3/52) | 数值 | 30 / 45 |
| `widthPriority` | 3.9% (2/52) | 数值 | -1000 / 100 |
| `workerClass` | 94.2% (49/52) | 文本 | PawnColumnWorker_AutoRepair / PawnColumnWorker_Energy / PawnColumnWorker_Overseer |

## 四、原版 defName 一览（共 52 个，列出前 60）

```text
`CopyPasteWorkPriorities`         `CopyPasteTimetable`              `MentalState`                     `Faction`                       
`LabelWithIcon`                   `LabelShortWithIcon`              `Guest`                           `Energy`                        
`AllowedAreaMech`                 `Pregnant`                        `Info`                            `GapTiny`                       
`GapSmall`                        `Gap`                             `GapWide`                         `Timetable`                     
`AutoRepair`                      `Overseer`                        `ControlGroup`                    `WorkMode`                      
`DraftMech`                       `Gender`                          `LifeStage`                       `Predator`                      
`RemainingSpace`                  `Master`                          `AllowedArea`                     `AllowedAreaWide`               
`Outfit`                          `DrugPolicy`                      `FoodRestriction`                 `Reading`                       
`Carry`                           `Xenotype`                        `Bond`                            `Age`                           
`MedicalCare`                     `HostilityResponse`               `Ideo`                            `Slaughter`                     
`Sterile`                         `ReleaseAnimalToWild`             `FollowDrafted`                   `FollowFieldwork`               
`Hunt`                            `Tame`                            `Label`                           `ManhunterOnDamageChance`       
`ManhunterOnTameFailChance`       `SpecialTrainable`                `AnimalForage`                    `AnimalDig`                     
```
