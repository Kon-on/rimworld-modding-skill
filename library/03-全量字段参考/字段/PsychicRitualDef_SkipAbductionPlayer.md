# PsychicRitualDef_SkipAbductionPlayer

- **所属线**：世界线
- **原版实例数**：1
- **字段路径数**：16
- **资料片**：Anomaly
- **原版出处**：`Anomaly/Defs/PsychicRitualDefs/PsychicRituals.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<PsychicRitualDef_SkipAbductionPlayer>
    <defName>SkipAbductionPlayer</defName>
    <label>skip abduction</label>
    <description>Abduct a random hostile person from anywhere in the world, prioritizing those nearby. The ritual induces a dark archotech to warp space, teleporting a distant person to the center of the ritual circle. The process causes the target to fall into a short coma.</description>
    <researchPrerequisite>SkipAbductionPlayer</researchPrerequisite>
    <outcomeDescription>At the current ritual quality, the target will remain in a coma for {0}.</outcomeDescription>
    <hoursUntilOutcome>2</hoursUntilOutcome>
    <requiredOffering>
      <filter>
        <thingDefs>
          <li>Bioferrite</li>
        </thingDefs>
      </filter>
      <count>60</count>
    </requiredOffering>
    <cooldownHours>240</cooldownHours>
    <comaDurationDaysFromQualityCurve>
      <points>
        <li>(0, 30)</li>
        <li>(0.5, 10)</li>
        <li>(0.75, 5)</li>
        <li>(1, 0.4166)</li>
      </points>
    </comaDurationDaysFromQualityCurve>
    <iconPath>UI/PsychicRituals/PsychicRitual_SkipAbduction</iconPath>
  </PsychicRitualDef_SkipAbductionPlayer>

  
```

> 来自 `Anomaly/Defs/PsychicRitualDefs/PsychicRituals.xml`，defName = `SkipAbductionPlayer`，XML 节点数 20（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
comaDurationDaysFromQualityCurve               [容器]
comaDurationDaysFromQualityCurve/points        [容器]
comaDurationDaysFromQualityCurve/points/li     [文本]  例：(0, 30) / (0.5, 10) / (0.75, 5)
cooldownHours                                  [数值]  例：240
defName                                        [文本]  例：SkipAbductionPlayer
description                                    [文本]  例：Abduct a random hostile person from anywhere in the world, prioritizing those ne
hoursUntilOutcome                              [数值]  例：2
iconPath                                       [文本]  例：UI/PsychicRituals/PsychicRitual_SkipAbduction
label                                          [文本]  例：skip abduction
outcomeDescription                             [文本]  例：At the current ritual quality, the target will remain in a coma for {0}.
requiredOffering                               [容器]
requiredOffering/count                         [数值]  例：60
requiredOffering/filter                        [容器]
requiredOffering/filter/thingDefs              [容器]
requiredOffering/filter/thingDefs/li           [文本]  例：Bioferrite
researchPrerequisite                           [文本]  例：SkipAbductionPlayer
```

## 三、全量字段表（16 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `comaDurationDaysFromQualityCurve` | 100.0% (1/1) | 容器 |  |
| `comaDurationDaysFromQualityCurve/points` | 100.0% (1/1) | 容器 |  |
| `comaDurationDaysFromQualityCurve/points/li` | 400.0% (4/1) | 文本 | (0, 30) / (0.5, 10) / (0.75, 5) |
| `cooldownHours` | 100.0% (1/1) | 数值 | 240 |
| `defName` | 100.0% (1/1) | 文本 | SkipAbductionPlayer |
| `description` | 100.0% (1/1) | 文本 | Abduct a random hostile person from anywhere in the world, prioritizing those ne |
| `hoursUntilOutcome` | 100.0% (1/1) | 数值 | 2 |
| `iconPath` | 100.0% (1/1) | 文本 | UI/PsychicRituals/PsychicRitual_SkipAbduction |
| `label` | 100.0% (1/1) | 文本 | skip abduction |
| `outcomeDescription` | 100.0% (1/1) | 文本 | At the current ritual quality, the target will remain in a coma for {0}. |
| `requiredOffering` | 100.0% (1/1) | 容器 |  |
| `requiredOffering/count` | 100.0% (1/1) | 数值 | 60 |
| `requiredOffering/filter` | 100.0% (1/1) | 容器 |  |
| `requiredOffering/filter/thingDefs` | 100.0% (1/1) | 容器 |  |
| `requiredOffering/filter/thingDefs/li` | 100.0% (1/1) | 文本 | Bioferrite |
| `researchPrerequisite` | 100.0% (1/1) | 文本 | SkipAbductionPlayer |

## 四、原版 defName 一览（共 1 个，列出前 60）

```text
`SkipAbductionPlayer`           
```
