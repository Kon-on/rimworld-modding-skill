# PsychicRitualRoleDef_DeathRefusalTarget

- **所属线**：世界线
- **原版实例数**：1
- **字段路径数**：6
- **资料片**：Anomaly
- **原版出处**：`Anomaly/Defs/PsychicRitualDefs/PsychicRitualRoles.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<PsychicRitualRoleDef_DeathRefusalTarget>
    <defName>DeathRefusalTarget</defName>
    <label>target</label>
    <allowedCount>1</allowedCount>
    <allowedConditions>Default, Downed, Prisoner, Sleeping, IdeoUnwilling</allowedConditions>
    <psychicRitualLeaveReason_MaxDeathRefusal>{PAWN_labelShort} cannot have any more death refusals stacked</psychicRitualLeaveReason_MaxDeathRefusal>
    <applyPowerOffset>false</applyPowerOffset>
  </PsychicRitualRoleDef_DeathRefusalTarget>

  
```

> 来自 `Anomaly/Defs/PsychicRitualDefs/PsychicRitualRoles.xml`，defName = `DeathRefusalTarget`，XML 节点数 7（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
allowedConditions                              [文本]  例：Default, Downed, Prisoner, Sleeping, IdeoUnwilling
allowedCount                                   [数值]  例：1
applyPowerOffset                               [布尔]  例：false
defName                                        [文本]  例：DeathRefusalTarget
label                                          [文本]  例：target
psychicRitualLeaveReason_MaxDeathRefusal       [文本]  例：{PAWN_labelShort} cannot have any more death refusals stacked
```

## 三、全量字段表（6 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `allowedConditions` | 100.0% (1/1) | 文本 | Default, Downed, Prisoner, Sleeping, IdeoUnwilling |
| `allowedCount` | 100.0% (1/1) | 数值 | 1 |
| `applyPowerOffset` | 100.0% (1/1) | 布尔 | false |
| `defName` | 100.0% (1/1) | 文本 | DeathRefusalTarget |
| `label` | 100.0% (1/1) | 文本 | target |
| `psychicRitualLeaveReason_MaxDeathRefusal` | 100.0% (1/1) | 文本 | {PAWN_labelShort} cannot have any more death refusals stacked |

## 四、原版 defName 一览（共 1 个，列出前 60）

```text
`DeathRefusalTarget`            
```
