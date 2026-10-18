# HeadTypeDef

- **所属线**：人物线
- **原版实例数**：43
- **字段路径数**：13
- **资料片**：Anomaly、Biotech、Core
- **原版出处**：`Biotech/Defs/HeadTypeDefs/HeadTypeDefs.xml`、`Core/Defs/HeadTypeDefs/HeadTypeDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<HeadTypeDef ParentName="FurskinAverageBase">
    <defName>Furskin_Average1</defName>
    <graphicPath>Things/Pawn/Humanlike/Heads/FurCovered_Average1_Normal</graphicPath>
  </HeadTypeDef>

  
```

> 来自 `Biotech/Defs/HeadTypeDefs/HeadTypeDefs.xml`，defName = `Furskin_Average1`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

_该类型没有出现率≥90% 的字段（字段高度自由）。_

## 三、全量字段表（13 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `beardMeshSize` | 9.3% (4/43) | 文本 | (1.2, 1.5) / (1.5, 1.5) / (1.7, 1.5) |
| `beardOffset` | 2.3% (1/43) | 文本 | (0, 0, -0.05) |
| `beardOffsetXEast` | 2.3% (1/43) | 数值 | -0.05 |
| `defName` | 86.1% (37/43) | 文本 | Ghoul_Heavy / Ghoul_Narrow / Ghoul_Normal |
| `eyeOffsetEastWest` | 55.8% (24/43) | 文本 | (0.13, 0, 0.17) / (0.13, 0, 0.18) / (0.15, 0, 0.18) |
| `gender` | 67.4% (29/43) | 文本 | Female / Male / None |
| `graphicPath` | 86.1% (37/43) | 文本 | Things/Pawn/Ghoul/Heads/GhoulskinHead_Heavy / Things/Pawn/Ghoul/Heads/GhoulskinHead_Narrow / Things/Pawn/Ghoul |
| `hairMeshSize` | 9.3% (4/43) | 文本 | (1.3, 1.5) / (1.5, 1.5) |
| `narrow` | 2.3% (1/43) | 布尔 | true |
| `randomChosen` | 41.9% (18/43) | 布尔 | false |
| `requiredGenes` | 16.3% (7/43) | 容器 |  |
| `requiredGenes/li` | 20.9% (9/43) | 文本 | Furskin / Head_Gaunt / Jaw_Heavy |
| `selectionWeight` | 9.3% (4/43) | 数值 | 0 / 99999 |

## 四、原版 defName 一览（共 43 个，列出前 60）

```text
`Furskin_Average1`                `Furskin_Average2`                `Furskin_Average3`                `Furskin_Narrow1`               
`Furskin_Narrow2`                 `Furskin_Narrow3`                 `Furskin_Heavy1`                  `Furskin_Heavy2`                
`Furskin_Heavy3`                  ``                                `Male_NarrowNormal`               `Male_NarrowPointy`             
`Male_NarrowWide`                 `Female_NarrowNormal`             `Female_NarrowPointy`             `Female_NarrowWide`             
`CultEscapee`                     `TimelessOne`                     `Male_HeavyJawNormal`             `Female_HeavyJawNormal`         
`Male_AverageNormal`              `Male_AveragePointy`              `Male_AverageWide`                `Female_AverageNormal`          
`Female_AveragePointy`            `Female_AverageWide`              `Ghoul_Normal`                    `Ghoul_Heavy`                   
`Ghoul_Narrow`                    `DarkScholar_Female`              `DarkScholar_Male`                `Leathery_Female`               
`Leathery_Male`                   ``                                ``                                ``                              
`Skull`                           `Stump`                           ``                                `Gaunt`                         
``                                `Ghoul_Wide`                      `Furskin_Gaunt`                 
```
