# PsychicRitualRoleDef

- **所属线**：世界线
- **原版实例数**：9
- **字段路径数**：10
- **资料片**：Anomaly
- **原版出处**：`Anomaly/Defs/PsychicRitualDefs/PsychicRitualRoles.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<PsychicRitualRoleDef ParentName="ChanterBase">
    <defName>Chanter</defName>
    <allowedCount>0~4</allowedCount>
  </PsychicRitualRoleDef>

  
```

> 来自 `Anomaly/Defs/PsychicRitualDefs/PsychicRitualRoles.xml`，defName = `Chanter`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

_该类型没有出现率≥90% 的字段（字段高度自由）。_

## 三、全量字段表（10 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `allowedConditions` | 66.7% (6/9) | 文本 | Default, Downed, Prisoner, Sleeping, IdeoUnwilling / Default, Sleeping, Downed, Bleeding, Burning, NoPsychicSe |
| `allowedCount` | 88.9% (8/9) | 数值/文本 | 0~4 / 0~6 / 0~9999 |
| `applyPowerOffset` | 44.4% (4/9) | 布尔 | false |
| `canHandleOfferings` | 11.1% (1/9) | 布尔 | true |
| `defName` | 88.9% (8/9) | 文本 | Chanter / ChanterAdvanced / Defender |
| `description` | 22.2% (2/9) | 文本 | Chanters add psychic power to the ritual. / Defenders protect the ritual participants from harm. |
| `label` | 77.8% (7/9) | 文本 | chanter / defenders / invoker |
| `psychicRitualWaitsForArrival` | 11.1% (1/9) | 布尔 | false |
| `removeOnLost` | 44.4% (4/9) | 布尔 | false |
| `showInvocationVfx` | 22.2% (2/9) | 布尔 | true |

## 四、原版 defName 一览（共 9 个，列出前 60）

```text
`Chanter`                         ``                                `ChanterAdvanced`                 `Invoker`                       
`Defender`                        `PhilophagyTarget`                `ChronophagyTarget`               `BrainwipeTarget`               
`PsychophagyTarget`             
```
