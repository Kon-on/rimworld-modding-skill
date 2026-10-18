# SlaveInteractionModeDef

- **所属线**：系统线
- **原版实例数**：5
- **字段路径数**：4
- **资料片**：Ideology
- **原版出处**：`Ideology/Defs/SlaveInteractionModeDefs/SlaveInteractionMode.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<SlaveInteractionModeDef>
    <defName>NoInteraction</defName>
    <label>no interaction</label>
    <listOrder>0</listOrder>
    <description>Wardens will not interact with this slave.</description>
  </SlaveInteractionModeDef>

  
```

> 来自 `Ideology/Defs/SlaveInteractionModeDefs/SlaveInteractionMode.xml`，defName = `NoInteraction`，XML 节点数 5（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Emancipate / Imprison / NoInteraction
description                                    [文本]  例：A warden will free this slave. / A warden will imprison this slave. Once imprisoned, they can be recruited, or en / Wardens will not interact with this slave.
label                                          [文本]  例：emancipate / imprison / no interaction
listOrder                                      [数值]  例：0 / 10 / 20
```

## 三、全量字段表（4 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (5/5) | 文本 | Emancipate / Imprison / NoInteraction |
| `description` | 100.0% (5/5) | 文本 | A warden will free this slave. / A warden will imprison this slave. Once imprisoned, they can be recruited, or |
| `label` | 100.0% (5/5) | 文本 | emancipate / imprison / no interaction |
| `listOrder` | 100.0% (5/5) | 数值 | 0 / 10 / 20 |

## 四、原版 defName 一览（共 5 个，列出前 60）

```text
`NoInteraction`                   `Suppress`                        `Imprison`                        `Emancipate`                    
`Execute`                       
```
