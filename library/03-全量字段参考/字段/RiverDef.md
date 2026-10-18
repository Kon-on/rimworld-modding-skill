# RiverDef

- **所属线**：世界线
- **原版实例数**：4
- **字段路径数**：14
- **资料片**：Core
- **原版出处**：`Core/Defs/RiverDefs/RiverDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<RiverDef>
    <defName>Creek</defName>
    <label>creek</label>
    <degradeThreshold>20000</degradeThreshold>
    <widthOnWorld>0.2</widthOnWorld>
    <widthOnMap>4</widthOnMap>
    <debugOpacity>0.05</debugOpacity>
  </RiverDef>
```

> 来自 `Core/Defs/RiverDefs/RiverDefs.xml`，defName = `Creek`，XML 节点数 7（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
branches/li                                    [容器]
branches/li/chance                             [数值]  例：0.3 / 0.6
branches/li/child                              [文本]  例：Creek / HugeRiver / LargeRiver
branches/li/minFlow                            [数值]  例：100000 / 125000 / 75000
debugOpacity                                   [数值]  例：0.05 / 0.2 / 0.4
defName                                        [文本]  例：Creek / HugeRiver / LargeRiver
degradeThreshold                               [数值]  例：20000 / 250000 / 50000
label                                          [文本]  例：creek / huge river / large river
widthOnMap                                     [数值]  例：14 / 30 / 4
widthOnWorld                                   [数值]  例：0.2 / 0.4 / 0.6
```

## 三、全量字段表（14 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `branches` | 75.0% (3/4) | 容器 |  |
| `branches/li` | 125.0% (5/4) | 容器 |  |
| `branches/li/chance` | 125.0% (5/4) | 数值 | 0.3 / 0.6 |
| `branches/li/child` | 125.0% (5/4) | 文本 | Creek / HugeRiver / LargeRiver |
| `branches/li/minFlow` | 125.0% (5/4) | 数值 | 100000 / 125000 / 75000 |
| `debugOpacity` | 100.0% (4/4) | 数值 | 0.05 / 0.2 / 0.4 |
| `defName` | 100.0% (4/4) | 文本 | Creek / HugeRiver / LargeRiver |
| `degradeChild` | 75.0% (3/4) | 文本 | Creek / LargeRiver / River |
| `degradeThreshold` | 100.0% (4/4) | 数值 | 20000 / 250000 / 50000 |
| `label` | 100.0% (4/4) | 文本 | creek / huge river / large river |
| `spawnChance` | 75.0% (3/4) | 数值 | 0.5 / 0.75 / 1 |
| `spawnFlowThreshold` | 75.0% (3/4) | 数值 | 100000 / 1000000 / 500000 |
| `widthOnMap` | 100.0% (4/4) | 数值 | 14 / 30 / 4 |
| `widthOnWorld` | 100.0% (4/4) | 数值 | 0.2 / 0.4 / 0.6 |

## 四、原版 defName 一览（共 4 个，列出前 60）

```text
`Creek`                           `LargeRiver`                      `River`                           `HugeRiver`                     
```
