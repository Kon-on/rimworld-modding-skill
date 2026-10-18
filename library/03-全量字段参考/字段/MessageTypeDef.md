# MessageTypeDef

- **所属线**：系统线
- **原版实例数**：12
- **字段路径数**：2
- **资料片**：Core
- **原版出处**：`Core/Defs/Misc/MessageTypeDefs/MessageTypeDef.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<MessageTypeDef>
    <defName>SituationResolved</defName>
  </MessageTypeDef>

  
```

> 来自 `Core/Defs/Misc/MessageTypeDefs/MessageTypeDef.xml`，defName = `SituationResolved`，XML 节点数 2（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：NegativeHealthEvent / PawnDeath / ThreatBig
```

## 三、全量字段表（2 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (12/12) | 文本 | NegativeHealthEvent / PawnDeath / ThreatBig |
| `sound` | 83.3% (10/12) | 文本 | Message_NegativeHealthEvent / Message_PawnDeath / Message_ThreatBig |

## 四、原版 defName 一览（共 12 个，列出前 60）

```text
`SituationResolved`               `SilentInput`                     `ThreatBig`                       `ThreatSmall`                   
`PawnDeath`                       `NegativeHealthEvent`             `NegativeEvent`                   `NeutralEvent`                  
`TaskCompletion`                  `PositiveEvent`                   `RejectInput`                     `CautionInput`                  
```
