# RoadWorldLayerDef

- **所属线**：世界线
- **原版实例数**：5
- **字段路径数**：3
- **资料片**：Core
- **原版出处**：`Core/Defs/RoadDefs/RoadWorldLayerDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<RoadWorldLayerDef>
    <defName>Outline</defName>
    <order>0</order>
    <color>(0.1, 0.1, 0.1)</color>
  </RoadWorldLayerDef>
  
  
```

> 来自 `Core/Defs/RoadDefs/RoadWorldLayerDefs.xml`，defName = `Outline`，XML 节点数 4（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
color                                          [文本]  例：(0.1, 0.1, 0.1) / (0.4, 0.4, 0.4) / (0.5, 0.4, 0.3)
defName                                        [文本]  例：Dirt / Gravel / Outline
order                                          [数值]  例：0 / 100 / 200
```

## 三、全量字段表（3 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `color` | 100.0% (5/5) | 文本 | (0.1, 0.1, 0.1) / (0.4, 0.4, 0.4) / (0.5, 0.4, 0.3) |
| `defName` | 100.0% (5/5) | 文本 | Dirt / Gravel / Outline |
| `order` | 100.0% (5/5) | 数值 | 0 / 100 / 200 |

## 四、原版 defName 一览（共 5 个，列出前 60）

```text
`Outline`                         `Dirt`                            `Stone`                           `Gravel`                        
`Asphalt`                       
```
