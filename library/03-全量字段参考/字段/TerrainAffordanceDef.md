# TerrainAffordanceDef

- **所属线**：世界线
- **原版实例数**：12
- **字段路径数**：6
- **资料片**：Core、Odyssey
- **原版出处**：`Core/Defs/Misc/TerrainAffordanceDefs/TerrainAffordances.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<TerrainAffordanceDef>
    <defName>Bridgeable</defName>
    <label>bridgeable</label>
    <order>2400</order>
  </TerrainAffordanceDef>
  
  
```

> 来自 `Core/Defs/Misc/TerrainAffordanceDefs/TerrainAffordances.xml`，defName = `Bridgeable`，XML 节点数 4（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Heavy / Light / Medium
label                                          [文本]  例：heavy / light / medium
order                                          [数值]  例：1200 / 1300 / 1400
```

## 三、全量字段表（6 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `affordanceOverlayColor` | 33.3% (4/12) | 文本 | (0,0,100) / (0,0,200) / (255,130,0) |
| `blockAffordanceOverlay` | 8.3% (1/12) | 布尔 | true |
| `defName` | 100.0% (12/12) | 文本 | Heavy / Light / Medium |
| `label` | 100.0% (12/12) | 文本 | heavy / light / medium |
| `order` | 100.0% (12/12) | 数值 | 1200 / 1300 / 1400 |
| `visualizeOnAffordanceOverlay` | 33.3% (4/12) | 布尔 | true |

## 四、原版 defName 一览（共 12 个，列出前 60）

```text
`Bridgeable`                      `GrowSoil`                        `Diggable`                        `SmoothableStone`               
`Walkable`                        `Heavy`                           `WaterproofConduitable`           `Substructure`                  
`Light`                           `Medium`                          `ShallowWater`                    `MovingFluid`                   
```
