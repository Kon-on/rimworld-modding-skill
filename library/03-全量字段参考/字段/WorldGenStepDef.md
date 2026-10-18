# WorldGenStepDef

- **所属线**：世界线
- **原版实例数**：12
- **字段路径数**：6
- **资料片**：Biotech、Core、Odyssey
- **原版出处**：`Biotech/Defs/WorldGeneration/WorldGenerator.xml`、`Core/Defs/WorldGeneration/WorldGenerator.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<WorldGenStepDef>
    <defName>Pollution</defName>
    <order>450</order>
    <worldGenStep Class="WorldGenStep_Pollution"/>
  </WorldGenStepDef>
```

> 来自 `Biotech/Defs/WorldGeneration/WorldGenerator.xml`，defName = `Pollution`，XML 节点数 4（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Lakes / Pollution / Terrain
order                                          [数值]  例：0 / 150 / 450
worldGenStep                                   [容器]
```

## 三、全量字段表（6 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (12/12) | 文本 | Lakes / Pollution / Terrain |
| `order` | 100.0% (12/12) | 数值 | 0 / 150 / 450 |
| `worldGenStep` | 100.0% (12/12) | 容器 |  |
| `worldGenStep/ancientSitesPer100kTiles` | 8.3% (1/12) | 文本 | 10~20 |
| `worldGenStep/maximumSegmentCurviness` | 8.3% (1/12) | 数值 | 1.5 |
| `worldGenStep/maximumSiteCurve` | 8.3% (1/12) | 数值 | 15 |

## 四、原版 defName 一览（共 12 个，列出前 60）

```text
`Pollution`                       `Terrain`                         `Tiles`                           `Lakes`                         
`Rivers`                          `Factions`                        `Roads`                           `Features`                      
`AncientSites`                    `Mutators`                        `Landmarks`                       `AncientRoads`                  
```
