# PsychicRitualDef_Psychophagy

- **所属线**：世界线
- **原版实例数**：1
- **字段路径数**：18
- **资料片**：Anomaly
- **原版出处**：`Anomaly/Defs/PsychicRitualDefs/PsychicRituals.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<PsychicRitualDef_Psychophagy>
    <defName>Psychophagy</defName>
    <label>psychophagy</label>
    <description>Consume the psychic sensitivity of a target. The invoker will increase their psychic sensitivity for a period of time. The effect does not stack. The target will suffer brain damage, causing them to fall into a coma for several days.</description>
    <researchPrerequisite>Psychophagy</researchPrerequisite>
    <outcomeDescription>At the current ritual quality, the invoker will increase their psychic sensitivity for {0}.\n\nThe target will suffer brain damage and fall into a coma.</outcomeDescription>
    <targetRole>PsychophagyTarget</targetRole>
    <hoursUntilOutcome>4</hoursUntilOutcome>
    <requiredOffering>
      <filter>
        <thingDefs>
          <li>Bioferrite</li>
        </thingDefs>
      </filter>
      <count>20</count>
    </requiredOffering>
    <cooldownHours>120</cooldownHours>
    <effectDurationDaysFromQualityCurve>
      <points>
        <li>(0, 10)</li>
        <li>(0.5, 30)</li>
        <li>(1, 120)</li>
      </points>
    </effectDurationDaysFromQualityCurve>
    <brainDamageRange>3~5</brainDamageRange>
    <iconPath>UI/PsychicRituals/PsychicRitual_Psychophagy</iconPath>
  </PsychicRitualDef_Psychophagy>

  
```

> 来自 `Anomaly/Defs/PsychicRitualDefs/PsychicRituals.xml`，defName = `Psychophagy`，XML 节点数 21（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
brainDamageRange                               [文本]  例：3~5
cooldownHours                                  [数值]  例：120
defName                                        [文本]  例：Psychophagy
description                                    [文本]  例：Consume the psychic sensitivity of a target. The invoker will increase their psy
effectDurationDaysFromQualityCurve             [容器]
effectDurationDaysFromQualityCurve/points      [容器]
effectDurationDaysFromQualityCurve/points/li   [文本]  例：(0, 10) / (0.5, 30) / (1, 120)
hoursUntilOutcome                              [数值]  例：4
iconPath                                       [文本]  例：UI/PsychicRituals/PsychicRitual_Psychophagy
label                                          [文本]  例：psychophagy
outcomeDescription                             [文本]  例：At the current ritual quality, the invoker will increase their psychic sensitivi
requiredOffering                               [容器]
requiredOffering/count                         [数值]  例：20
requiredOffering/filter                        [容器]
requiredOffering/filter/thingDefs              [容器]
requiredOffering/filter/thingDefs/li           [文本]  例：Bioferrite
researchPrerequisite                           [文本]  例：Psychophagy
targetRole                                     [文本]  例：PsychophagyTarget
```

## 三、全量字段表（18 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `brainDamageRange` | 100.0% (1/1) | 文本 | 3~5 |
| `cooldownHours` | 100.0% (1/1) | 数值 | 120 |
| `defName` | 100.0% (1/1) | 文本 | Psychophagy |
| `description` | 100.0% (1/1) | 文本 | Consume the psychic sensitivity of a target. The invoker will increase their psy |
| `effectDurationDaysFromQualityCurve` | 100.0% (1/1) | 容器 |  |
| `effectDurationDaysFromQualityCurve/points` | 100.0% (1/1) | 容器 |  |
| `effectDurationDaysFromQualityCurve/points/li` | 300.0% (3/1) | 文本 | (0, 10) / (0.5, 30) / (1, 120) |
| `hoursUntilOutcome` | 100.0% (1/1) | 数值 | 4 |
| `iconPath` | 100.0% (1/1) | 文本 | UI/PsychicRituals/PsychicRitual_Psychophagy |
| `label` | 100.0% (1/1) | 文本 | psychophagy |
| `outcomeDescription` | 100.0% (1/1) | 文本 | At the current ritual quality, the invoker will increase their psychic sensitivi |
| `requiredOffering` | 100.0% (1/1) | 容器 |  |
| `requiredOffering/count` | 100.0% (1/1) | 数值 | 20 |
| `requiredOffering/filter` | 100.0% (1/1) | 容器 |  |
| `requiredOffering/filter/thingDefs` | 100.0% (1/1) | 容器 |  |
| `requiredOffering/filter/thingDefs/li` | 100.0% (1/1) | 文本 | Bioferrite |
| `researchPrerequisite` | 100.0% (1/1) | 文本 | Psychophagy |
| `targetRole` | 100.0% (1/1) | 文本 | PsychophagyTarget |

## 四、原版 defName 一览（共 1 个，列出前 60）

```text
`Psychophagy`                   
```
