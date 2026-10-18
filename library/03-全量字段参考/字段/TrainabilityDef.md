# TrainabilityDef

- **所属线**：人物线
- **原版实例数**：3
- **字段路径数**：3
- **资料片**：Core
- **原版出处**：`Core/Defs/Misc/TrainabilityDefs/TrainabilityDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<TrainabilityDef>
    <defName>None</defName>
    <label>none</label>
    <intelligenceOrder>0</intelligenceOrder>
  </TrainabilityDef>

  
```

> 来自 `Core/Defs/Misc/TrainabilityDefs/TrainabilityDefs.xml`，defName = `None`，XML 节点数 4（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Advanced / Intermediate / None
intelligenceOrder                              [数值]  例：0 / 20 / 30
label                                          [文本]  例：advanced / intermediate / none
```

## 三、全量字段表（3 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (3/3) | 文本 | Advanced / Intermediate / None |
| `intelligenceOrder` | 100.0% (3/3) | 数值 | 0 / 20 / 30 |
| `label` | 100.0% (3/3) | 文本 | advanced / intermediate / none |

## 四、原版 defName 一览（共 3 个，列出前 60）

```text
`None`                            `Intermediate`                    `Advanced`                      
```
