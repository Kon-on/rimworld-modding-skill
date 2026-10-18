# PsychicRitualDef_Brainwipe

- **所属线**：世界线
- **原版实例数**：1
- **字段路径数**：18
- **资料片**：Anomaly
- **原版出处**：`Anomaly/Defs/PsychicRitualDefs/PsychicRituals.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<PsychicRitualDef_Brainwipe>
    <defName>Brainwipe</defName>
    <label>brainwipe</label>
    <description>Erase a person's memories. Traumatic events will be forgotten. Prisoners will forget their allegiance and become easier to recruit, even if they were unwavering before. Inhumanized individuals will forget their connection to the void. Unfortunately, the disruptive effect of the ritual will induce a coma that could last a long time, especially if the ritual is of poor quality.</description>
    <outcomeDescription>The target will be brainwiped.\n\nWith the current ritual quality, the target will also enter a coma for {0}.</outcomeDescription>
    <researchPrerequisite>Brainwipe</researchPrerequisite>
    <hoursUntilOutcome>6</hoursUntilOutcome>
    <targetRole>BrainwipeTarget</targetRole>
    <requiredOffering>
      <filter>
        <thingDefs>
          <li>Shard</li>
        </thingDefs>
      </filter>
      <count>1</count>
    </requiredOffering>
    <comaDurationDaysFromQualityCurve>
      <points>
        <li>(0, 60)</li>
        <li>(0.5, 14)</li>
        <li>(1, 1)</li>
      </points>
    </comaDurationDaysFromQualityCurve>
    <cooldownHours>480</cooldownHours>
    <chanterRole>ChanterAdvanced</chanterRole>
    <iconPath>UI/PsychicRituals/PsychicRitual_Brainwipe</iconPath>
  </PsychicRitualDef_Brainwipe>

  
```

> 来自 `Anomaly/Defs/PsychicRitualDefs/PsychicRituals.xml`，defName = `Brainwipe`，XML 节点数 21（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
chanterRole                                    [文本]  例：ChanterAdvanced
comaDurationDaysFromQualityCurve               [容器]
comaDurationDaysFromQualityCurve/points        [容器]
comaDurationDaysFromQualityCurve/points/li     [文本]  例：(0, 60) / (0.5, 14) / (1, 1)
cooldownHours                                  [数值]  例：480
defName                                        [文本]  例：Brainwipe
description                                    [文本]  例：Erase a person's memories. Traumatic events will be forgotten. Prisoners will fo
hoursUntilOutcome                              [数值]  例：6
iconPath                                       [文本]  例：UI/PsychicRituals/PsychicRitual_Brainwipe
label                                          [文本]  例：brainwipe
outcomeDescription                             [文本]  例：The target will be brainwiped.\n\nWith the current ritual quality, the target wi
requiredOffering                               [容器]
requiredOffering/count                         [数值]  例：1
requiredOffering/filter                        [容器]
requiredOffering/filter/thingDefs              [容器]
requiredOffering/filter/thingDefs/li           [文本]  例：Shard
researchPrerequisite                           [文本]  例：Brainwipe
targetRole                                     [文本]  例：BrainwipeTarget
```

## 三、全量字段表（18 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `chanterRole` | 100.0% (1/1) | 文本 | ChanterAdvanced |
| `comaDurationDaysFromQualityCurve` | 100.0% (1/1) | 容器 |  |
| `comaDurationDaysFromQualityCurve/points` | 100.0% (1/1) | 容器 |  |
| `comaDurationDaysFromQualityCurve/points/li` | 300.0% (3/1) | 文本 | (0, 60) / (0.5, 14) / (1, 1) |
| `cooldownHours` | 100.0% (1/1) | 数值 | 480 |
| `defName` | 100.0% (1/1) | 文本 | Brainwipe |
| `description` | 100.0% (1/1) | 文本 | Erase a person's memories. Traumatic events will be forgotten. Prisoners will fo |
| `hoursUntilOutcome` | 100.0% (1/1) | 数值 | 6 |
| `iconPath` | 100.0% (1/1) | 文本 | UI/PsychicRituals/PsychicRitual_Brainwipe |
| `label` | 100.0% (1/1) | 文本 | brainwipe |
| `outcomeDescription` | 100.0% (1/1) | 文本 | The target will be brainwiped.\n\nWith the current ritual quality, the target wi |
| `requiredOffering` | 100.0% (1/1) | 容器 |  |
| `requiredOffering/count` | 100.0% (1/1) | 数值 | 1 |
| `requiredOffering/filter` | 100.0% (1/1) | 容器 |  |
| `requiredOffering/filter/thingDefs` | 100.0% (1/1) | 容器 |  |
| `requiredOffering/filter/thingDefs/li` | 100.0% (1/1) | 文本 | Shard |
| `researchPrerequisite` | 100.0% (1/1) | 文本 | Brainwipe |
| `targetRole` | 100.0% (1/1) | 文本 | BrainwipeTarget |

## 四、原版 defName 一览（共 1 个，列出前 60）

```text
`Brainwipe`                     
```
