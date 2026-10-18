# StatCategoryDef

- **所属线**：系统线
- **原版实例数**：40
- **字段路径数**：4
- **资料片**：Anomaly、Biotech、Core
- **原版出处**：`Anomaly/Defs/StatDefs/Stats_Containment.xml`、`Core/Defs/Stats/StatCategories.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<StatCategoryDef>
    <defName>Containment</defName>
    <label>Containment</label>
    <displayOrder>600</displayOrder>
  </StatCategoryDef>

  
```

> 来自 `Anomaly/Defs/StatDefs/Stats_Containment.xml`，defName = `Containment`，XML 节点数 4（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Containment / Mechanitor / PsychicRituals
displayOrder                                   [数值]  例：105 / 500 / 600
label                                          [文本]  例：Containment / Mechanitor / Psychic ritual
```

## 三、全量字段表（4 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (40/40) | 文本 | Containment / Mechanitor / PsychicRituals |
| `displayAllByDefault` | 25.0% (10/40) | 布尔 | True / true |
| `displayOrder` | 100.0% (40/40) | 数值 | 105 / 500 / 600 |
| `label` | 100.0% (40/40) | 文本 | Containment / Mechanitor / Psychic ritual |

## 四、原版 defName 一览（共 40 个，列出前 60）

```text
`Containment`                     `PsychicRituals`                  `Serum`                           `BasicsPawnImportant`           
`BasicsNonPawnImportant`          `BasicsPawn`                      `BasicsNonPawn`                   `Source`                        
`Animals`                         `AnimalProductivity`              `Apparel`                         `Implant`                       
`Weapon`                          `Weapon_Ranged`                   `Weapon_Melee`                    `Building`                      
`Ability`                         `Drug`                            `DrugAddiction`                   `Terrain`                       
`EquippedStatOffsets`             `PawnResistances`                 `PawnPsyfocus`                    `PawnHealth`                    
`PawnFood`                        `PawnCombat`                      `PawnSocial`                      `PawnMisc`                      
`PawnWork`                        `Genetics`                        `Mechanitor`                      `Basics`                        
`BasicsImportant`                 `StuffStatFactors`                `StuffStatOffsets`                `StuffOfEquipmentStatFactors`   
`Surgery`                         `CapacityEffects`                 `Meditation`                      `Mechanoid`                     
```
