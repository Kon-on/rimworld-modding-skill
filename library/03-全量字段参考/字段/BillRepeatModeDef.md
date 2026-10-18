# BillRepeatModeDef

- **所属线**：系统线
- **原版实例数**：3
- **字段路径数**：3
- **资料片**：Core
- **原版出处**：`Core/Defs/Misc/BillDefs/BillRepeatModeDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<BillRepeatModeDef>
    <defName>RepeatCount</defName>
    <label>do X times</label>
    <listOrder>0</listOrder>
  </BillRepeatModeDef>

  
```

> 来自 `Core/Defs/Misc/BillDefs/BillRepeatModeDefs.xml`，defName = `RepeatCount`，XML 节点数 4（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Forever / RepeatCount / TargetCount
label                                          [文本]  例：do X times / do forever / do until you have X
listOrder                                      [数值]  例：0 / 10 / 20
```

## 三、全量字段表（3 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (3/3) | 文本 | Forever / RepeatCount / TargetCount |
| `label` | 100.0% (3/3) | 文本 | do X times / do forever / do until you have X |
| `listOrder` | 100.0% (3/3) | 数值 | 0 / 10 / 20 |

## 四、原版 defName 一览（共 3 个，列出前 60）

```text
`RepeatCount`                     `TargetCount`                     `Forever`                       
```
