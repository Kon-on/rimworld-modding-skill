# IssueDef

- **所属线**：理念线
- **原版实例数**：72
- **字段路径数**：5
- **资料片**：Anomaly、Biotech、Core、Ideology、Odyssey
- **原版出处**：`Anomaly/Defs/PreceptDefs/Precepts_PsychicRituals.xml`、`Ideology/Defs/PreceptDefs/Precepts_KillingInnocentAnimals.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<IssueDef>
    <defName>PsychicRituals</defName>
    <label>psychic rituals</label>
    <iconPath>UI/Issues/PsychicRituals</iconPath>
  </IssueDef>
  
  
```

> 来自 `Anomaly/Defs/PreceptDefs/Precepts_PsychicRituals.xml`，defName = `PsychicRituals`，XML 节点数 4（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Bloodfeeders / Inhumanizing / PsychicRituals
label                                          [文本]  例：bloodfeeders / inhumanizing / psychic rituals
```

## 三、全量字段表（5 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `allowMultiplePrecepts` | 12.5% (9/72) | 布尔 | true |
| `defName` | 100.0% (72/72) | 文本 | Bloodfeeders / Inhumanizing / PsychicRituals |
| `forceWriteLabelInPreceptFloatMenuOption` | 1.4% (1/72) | 布尔 | true |
| `iconPath` | 87.5% (63/72) | 文本 | UI/Issues/Bloodfeeders / UI/Issues/Inhumanizing / UI/Issues/PsychicRituals |
| `label` | 100.0% (72/72) | 文本 | bloodfeeders / inhumanizing / psychic rituals |

## 四、原版 defName 一览（共 72 个，列出前 60）

```text
`PsychicRituals`                  `VoidStudy`                       `Bloodfeeders`                    `ChildLabor`                    
`GrowthVat`                       `MechanoidLabor`                  `PreferredXenotypes`              `NutrientPasteEating`           
`Cannibalism`                     `Corpses`                         `InsectMeat`                      `Lovin`                         
`MarriageName`                    `OrganUse`                        `Execution`                       `Ritual`                        
`SlaveTrading`                    `SpouseCount_Male`                `SpouseCount_Female`              `AnimalsVenerated`              
`AnimalConnection`                `AnimalSlaughter`                 `Apostasy`                        `ApparelDesire`                 
`AutonomousWeapons`               `BlindPsysense`                   `Blindness`                       `BodyModification`              
`Bonding`                         `IdeoBuilding`                    `Charity`                         `Comfort`                       
`SlabBed`                         `DrugUse`                         `FungusEating`                    `IdeoDiversity`                 
`KillingInnocentAnimals`          `Lighting`                        `DarknessCombat`                  `Eclipse`                       
`MeatEating`                      `Mining`                          `MiningYield`                     `Nudity_Male`                   
`Nudity_Female`                   `Pain`                            `Proselytizing`                   `Raiding`                       
`Ranching`                        `IdeoRelic`                       `Research`                        `IdeoRitualSeat`                
`IdeoRole`                        `RoughLiving`                     `Scarification`                   `Skullspike`                    
`Slavery`                         `Indoors`                         `Temperature`                     `SleepAccelerator`              
```

_余下 12 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
