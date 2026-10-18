# PsychicRitualDef_PleasurePulse

- **所属线**：世界线
- **原版实例数**：1
- **字段路径数**：17
- **资料片**：Anomaly
- **原版出处**：`Anomaly/Defs/PsychicRitualDefs/PsychicRituals.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<PsychicRitualDef_PleasurePulse>
    <defName>PleasurePulse</defName>
    <label>pleasure pulse</label>
    <description>Emit an intense psychic pulse that makes any psychically sensitive individual in the region happier but reduces their desire to work. This will replace the effect of other active pulses.</description>
    <researchPrerequisite>PleasurePulse</researchPrerequisite>
    <outcomeDescription>At the current ritual quality, the effect will last for {0}.</outcomeDescription>
    <hoursUntilOutcome>4</hoursUntilOutcome>
    <requiredOffering>
      <filter>
        <thingDefs>
          <li>Bioferrite</li>
        </thingDefs>
      </filter>
      <count>30</count>
    </requiredOffering>
    <durationDaysFromQualityCurve>
      <points>
        <li>(0, 1)</li>
        <li>(0.5, 5)</li>
        <li>(0.75, 10)</li>
        <li>(1, 25)</li>
      </points>
    </durationDaysFromQualityCurve>
    <cooldownHours>120</cooldownHours>
    <chanterRole>ChanterAdvanced</chanterRole>
    <iconPath>UI/PsychicRituals/PsychicRitual_PleasurePulse</iconPath>
  </PsychicRitualDef_PleasurePulse>

  
```

> 来自 `Anomaly/Defs/PsychicRitualDefs/PsychicRituals.xml`，defName = `PleasurePulse`，XML 节点数 21（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
chanterRole                                    [文本]  例：ChanterAdvanced
cooldownHours                                  [数值]  例：120
defName                                        [文本]  例：PleasurePulse
description                                    [文本]  例：Emit an intense psychic pulse that makes any psychically sensitive individual in
durationDaysFromQualityCurve                   [容器]
durationDaysFromQualityCurve/points            [容器]
durationDaysFromQualityCurve/points/li         [文本]  例：(0, 1) / (0.5, 5) / (0.75, 10)
hoursUntilOutcome                              [数值]  例：4
iconPath                                       [文本]  例：UI/PsychicRituals/PsychicRitual_PleasurePulse
label                                          [文本]  例：pleasure pulse
outcomeDescription                             [文本]  例：At the current ritual quality, the effect will last for {0}.
requiredOffering                               [容器]
requiredOffering/count                         [数值]  例：30
requiredOffering/filter                        [容器]
requiredOffering/filter/thingDefs              [容器]
requiredOffering/filter/thingDefs/li           [文本]  例：Bioferrite
researchPrerequisite                           [文本]  例：PleasurePulse
```

## 三、全量字段表（17 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `chanterRole` | 100.0% (1/1) | 文本 | ChanterAdvanced |
| `cooldownHours` | 100.0% (1/1) | 数值 | 120 |
| `defName` | 100.0% (1/1) | 文本 | PleasurePulse |
| `description` | 100.0% (1/1) | 文本 | Emit an intense psychic pulse that makes any psychically sensitive individual in |
| `durationDaysFromQualityCurve` | 100.0% (1/1) | 容器 |  |
| `durationDaysFromQualityCurve/points` | 100.0% (1/1) | 容器 |  |
| `durationDaysFromQualityCurve/points/li` | 400.0% (4/1) | 文本 | (0, 1) / (0.5, 5) / (0.75, 10) |
| `hoursUntilOutcome` | 100.0% (1/1) | 数值 | 4 |
| `iconPath` | 100.0% (1/1) | 文本 | UI/PsychicRituals/PsychicRitual_PleasurePulse |
| `label` | 100.0% (1/1) | 文本 | pleasure pulse |
| `outcomeDescription` | 100.0% (1/1) | 文本 | At the current ritual quality, the effect will last for {0}. |
| `requiredOffering` | 100.0% (1/1) | 容器 |  |
| `requiredOffering/count` | 100.0% (1/1) | 数值 | 30 |
| `requiredOffering/filter` | 100.0% (1/1) | 容器 |  |
| `requiredOffering/filter/thingDefs` | 100.0% (1/1) | 容器 |  |
| `requiredOffering/filter/thingDefs/li` | 100.0% (1/1) | 文本 | Bioferrite |
| `researchPrerequisite` | 100.0% (1/1) | 文本 | PleasurePulse |

## 四、原版 defName 一览（共 1 个，列出前 60）

```text
`PleasurePulse`                 
```
