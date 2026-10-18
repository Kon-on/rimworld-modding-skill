# IncidentCategoryDef

- **所属线**：世界线
- **原版实例数**：13
- **字段路径数**：4
- **资料片**：Core
- **原版出处**：`Core/Defs/Misc/IncidentCategoryDefs/IncidentCategoryDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<IncidentCategoryDef>
    <defName>Special</defName>
  </IncidentCategoryDef>

  
```

> 来自 `Core/Defs/Misc/IncidentCategoryDefs/IncidentCategoryDefs.xml`，defName = `Special`，XML 节点数 2（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Misc / Special / ThreatBig
```

## 三、全量字段表（4 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `canUseAnomalyChance` | 15.4% (2/13) | 布尔 | true |
| `defName` | 100.0% (13/13) | 文本 | Misc / Special / ThreatBig |
| `needsParmsPoints` | 38.5% (5/13) | 布尔 | true |
| `tale` | 7.7% (1/13) | 文本 | MajorThreat |

## 四、原版 defName 一览（共 13 个，列出前 60）

```text
`Special`                         `FactionArrival`                  `OrbitalVisitor`                  `ShipChunkDrop`                 
`DiseaseHuman`                    `DiseaseAnimal`                   `AllyAssistance`                  `EndGame_ShipEscape`            
`Misc`                            `GiveQuest`                       `DeepDrillInfestation`            `ThreatSmall`                   
`ThreatBig`                     
```
