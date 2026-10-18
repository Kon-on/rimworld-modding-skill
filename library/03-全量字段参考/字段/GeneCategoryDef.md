# GeneCategoryDef

- **所属线**：人物线
- **原版实例数**：21
- **字段路径数**：4
- **资料片**：Biotech、Core
- **原版出处**：`Biotech/Defs/GeneDefs/GeneCategoryDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<GeneCategoryDef>
    <defName>Archite</defName>
    <label>archite</label>
    <displayPriorityInXenotype>1000</displayPriorityInXenotype>
  </GeneCategoryDef>

  
```

> 来自 `Biotech/Defs/GeneDefs/GeneCategoryDefs.xml`，defName = `Archite`，XML 节点数 4（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Ability / Archite / Healing
displayPriorityInXenotype                      [数值]  例：1000 / 500 / 510
label                                          [文本]  例：archite / health / hemogen
```

## 三、全量字段表（4 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (21/21) | 文本 | Ability / Archite / Healing |
| `displayPriorityInGenepack` | 14.3% (3/21) | 数值 | -100 / -110 / -120 |
| `displayPriorityInXenotype` | 100.0% (21/21) | 数值 | 1000 / 500 / 510 |
| `label` | 100.0% (21/21) | 文本 | archite / health / hemogen |

## 四、原版 defName 一览（共 21 个，列出前 60）

```text
`Archite`                         `Ability`                         `Hemogen`                         `Healing`                       
`Psychic`                         `Beauty`                          `Movement`                        `Mood`                          
`Temperature`                     `ResistanceAndWeakness`           `Violence`                        `Sleep`                         
`Pain`                            `Aptitudes`                       `Drugs`                           `Reproduction`                  
`Cosmetic_Hair`                   `Miscellaneous`                   `Cosmetic_Body`                   `Cosmetic`                      
`Cosmetic_Skin`                 
```
