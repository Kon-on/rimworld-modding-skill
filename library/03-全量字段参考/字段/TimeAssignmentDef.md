# TimeAssignmentDef

- **所属线**：系统线
- **原版实例数**：5
- **字段路径数**：5
- **资料片**：Core、Royalty
- **原版出处**：`Core/Defs/Misc/TimeAssignmentDefs/TimeAssignments.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<TimeAssignmentDef>
    <defName>Anything</defName>
    <label>anything</label>
    <color>(114,114,114)</color>
  </TimeAssignmentDef>

  
```

> 来自 `Core/Defs/Misc/TimeAssignmentDefs/TimeAssignments.xml`，defName = `Anything`，XML 节点数 4（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
color                                          [文本]  例：(114,114,114) / (115, 74, 138) / (133, 133, 61)
defName                                        [文本]  例：Anything / Joy / Sleep
label                                          [文本]  例：anything / recreation / sleep
```

## 三、全量字段表（5 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `allowJoy` | 20.0% (1/5) | 布尔 | false |
| `allowRest` | 40.0% (2/5) | 布尔 | false |
| `color` | 100.0% (5/5) | 文本 | (114,114,114) / (115, 74, 138) / (133, 133, 61) |
| `defName` | 100.0% (5/5) | 文本 | Anything / Joy / Sleep |
| `label` | 100.0% (5/5) | 文本 | anything / recreation / sleep |

## 四、原版 defName 一览（共 5 个，列出前 60）

```text
`Anything`                        `Joy`                             `Sleep`                           `Meditate`                      
`Work`                          
```
