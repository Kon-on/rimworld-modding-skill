# PsychicRitualDef_SkipAbduction

- **所属线**：世界线
- **原版实例数**：1
- **字段路径数**：12
- **资料片**：Anomaly
- **原版出处**：`Anomaly/Defs/PsychicRitualDefs/PsychicRituals.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<PsychicRitualDef_SkipAbduction>
    <defName>SkipAbduction</defName>
    <label>skip abduction</label>
    <description>Teleport a random hostile person to the ritual location and place them in a coma.</description>
    <outcomeDescription>The target will be teleported to the invoker's location and fall into a coma.</outcomeDescription>
    <letterAICompleteLabel>Skip abduction</letterAICompleteLabel>
    <letterAICompleteText>{PAWN_nameDef} has been abducted by the cultists!</letterAICompleteText>
    <aiCastable>true</aiCastable>
    <playerCastable>false</playerCastable>
    <hoursUntilOutcome>4</hoursUntilOutcome>
    <nonRequiredPawnsMayLeave>true</nonRequiredPawnsMayLeave>
    <defenderRole>Defender</defenderRole>
    <letterAIArrivedText>They intend to use a psychic ritual to abduct a colonist via teleportation.</letterAIArrivedText>
  </PsychicRitualDef_SkipAbduction>

  
```

> 来自 `Anomaly/Defs/PsychicRitualDefs/PsychicRituals.xml`，defName = `SkipAbduction`，XML 节点数 13（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
aiCastable                                     [布尔]  例：true
defenderRole                                   [文本]  例：Defender
defName                                        [文本]  例：SkipAbduction
description                                    [文本]  例：Teleport a random hostile person to the ritual location and place them in a coma
hoursUntilOutcome                              [数值]  例：4
label                                          [文本]  例：skip abduction
letterAIArrivedText                            [文本]  例：They intend to use a psychic ritual to abduct a colonist via teleportation.
letterAICompleteLabel                          [文本]  例：Skip abduction
letterAICompleteText                           [文本]  例：{PAWN_nameDef} has been abducted by the cultists!
nonRequiredPawnsMayLeave                       [布尔]  例：true
outcomeDescription                             [文本]  例：The target will be teleported to the invoker's location and fall into a coma.
playerCastable                                 [布尔]  例：false
```

## 三、全量字段表（12 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `aiCastable` | 100.0% (1/1) | 布尔 | true |
| `defenderRole` | 100.0% (1/1) | 文本 | Defender |
| `defName` | 100.0% (1/1) | 文本 | SkipAbduction |
| `description` | 100.0% (1/1) | 文本 | Teleport a random hostile person to the ritual location and place them in a coma |
| `hoursUntilOutcome` | 100.0% (1/1) | 数值 | 4 |
| `label` | 100.0% (1/1) | 文本 | skip abduction |
| `letterAIArrivedText` | 100.0% (1/1) | 文本 | They intend to use a psychic ritual to abduct a colonist via teleportation. |
| `letterAICompleteLabel` | 100.0% (1/1) | 文本 | Skip abduction |
| `letterAICompleteText` | 100.0% (1/1) | 文本 | {PAWN_nameDef} has been abducted by the cultists! |
| `nonRequiredPawnsMayLeave` | 100.0% (1/1) | 布尔 | true |
| `outcomeDescription` | 100.0% (1/1) | 文本 | The target will be teleported to the invoker's location and fall into a coma. |
| `playerCastable` | 100.0% (1/1) | 布尔 | false |

## 四、原版 defName 一览（共 1 个，列出前 60）

```text
`SkipAbduction`                 
```
