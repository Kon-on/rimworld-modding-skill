# SubcameraDef

- **所属线**：表现线
- **原版实例数**：2
- **字段路径数**：7
- **资料片**：Core、Odyssey
- **原版出处**：`Core/Defs/Misc/SubcameraDefs/Subcameras.xml`、`Odyssey/Defs/Misc/SubcameraDefs/Subcameras.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<SubcameraDef>
    <defName>WaterDepth</defName>
    <layer>WaterDepth</layer>
    <depth>100</depth>
    <format>RFloat</format>
  </SubcameraDef>
```

> 来自 `Core/Defs/Misc/SubcameraDefs/Subcameras.xml`，defName = `WaterDepth`，XML 节点数 5（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：GravshipMask / WaterDepth
depth                                          [数值]  例：1 / 100
format                                         [文本]  例：ARGB32 / RFloat
layer                                          [文本]  例：GravshipMask / WaterDepth
```

## 三、全量字段表（7 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `backgroundColor` | 50.0% (1/2) | 文本 | (0.0, 0.0, 0.0, 0.0) |
| `defName` | 100.0% (2/2) | 文本 | GravshipMask / WaterDepth |
| `depth` | 100.0% (2/2) | 数值 | 1 / 100 |
| `doNotUpdate` | 50.0% (1/2) | 布尔 | true |
| `format` | 100.0% (2/2) | 文本 | ARGB32 / RFloat |
| `layer` | 100.0% (2/2) | 文本 | GravshipMask / WaterDepth |
| `startEnabled` | 50.0% (1/2) | 布尔 | false |

## 四、原版 defName 一览（共 2 个，列出前 60）

```text
`WaterDepth`                      `GravshipMask`                  
```
