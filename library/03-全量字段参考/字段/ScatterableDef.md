# ScatterableDef

- **所属线**：世界线
- **原版实例数**：12
- **字段路径数**：7
- **资料片**：Core、Odyssey
- **原版出处**：`Core/Defs/Misc/ScatterableDefs/Scatterables.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<ScatterableDef ParentName="StoneRoot">
    <defName>DebrisStoneA</defName>
    <texturePath>Terrain/Scatter/DebrisStoneA</texturePath>
  </ScatterableDef>

  
```

> 来自 `Core/Defs/Misc/ScatterableDefs/Scatterables.xml`，defName = `DebrisStoneA`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

_该类型没有出现率≥90% 的字段（字段高度自由）。_

## 三、全量字段表（7 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 75.0% (9/12) | 文本 | DebrisStoneA / DebrisStoneB / DirtSmearA |
| `maxSize` | 25.0% (3/12) | 数值 | 1.0 / 3.0 / 7.0 |
| `minSize` | 25.0% (3/12) | 数值 | 0.4 / 1.0 / 1.5 |
| `placeUnderNaturalRoofs` | 8.3% (1/12) | 布尔 | false |
| `scatterChance` | 8.3% (1/12) | 数值 | 0.3 |
| `scatterType` | 66.7% (8/12) | 文本 | Craters / Rocky / SoftDry |
| `texturePath` | 75.0% (9/12) | 文本 | Terrain/Scatter/DebrisStoneA / Terrain/Scatter/DebrisStoneB / Terrain/Scatter/DirtSmearA |

## 四、原版 defName 一览（共 12 个，列出前 60）

```text
`DebrisStoneA`                    `DebrisStoneB`                    ``                                ``                              
`DirtSmearA`                      `DirtSmearB`                      `GraySmearA`                      `GraySmearB`                    
`MicrocraterA`                    `MicrocraterB`                    `MicrocraterC`                    ``                              
```
