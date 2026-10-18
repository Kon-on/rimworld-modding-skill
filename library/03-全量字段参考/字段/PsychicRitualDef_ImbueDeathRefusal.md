# PsychicRitualDef_ImbueDeathRefusal

- **所属线**：世界线
- **原版实例数**：1
- **字段路径数**：18
- **资料片**：Anomaly
- **原版出处**：`Anomaly/Defs/PsychicRitualDefs/PsychicRituals.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<PsychicRitualDef_ImbueDeathRefusal>
    <defName>ImbueDeathRefusal</defName>
    <label>imbue death refusal</label>
    <description>Link a target with a distant archotechnological engine that can bring them back from the dead in seconds. This process is not without side-effects.</description>
    <researchPrerequisite>DeathRefusal</researchPrerequisite>
    <outcomeDescription>The target will gain death refusal.\n\nWith the current quality, all the target's skills will also be reduced by {0}.</outcomeDescription>
    <hoursUntilOutcome>6</hoursUntilOutcome>
    <targetRole>DeathRefusalTarget</targetRole>
    <requiredOffering>
      <filter>
        <thingDefs>
          <li>Shard</li>
        </thingDefs>
      </filter>
      <count>1</count>
    </requiredOffering>
    <skillOffsetPercentFromQualityCurve>
      <points>
        <li>(0, -0.5)</li>
        <li>(0.5, -0.15)</li>
        <li>(0.75, -0.05)</li>
        <li>(1, -0.01)</li>
      </points>
    </skillOffsetPercentFromQualityCurve>
    <cooldownHours>360</cooldownHours>
    <chanterRole>ChanterAdvanced</chanterRole>
    <iconPath>UI/PsychicRituals/PsychicRitual_ImbueDeathRefusal</iconPath>
  </PsychicRitualDef_ImbueDeathRefusal>

  
```

> 来自 `Anomaly/Defs/PsychicRitualDefs/PsychicRituals.xml`，defName = `ImbueDeathRefusal`，XML 节点数 22（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
chanterRole                                    [文本]  例：ChanterAdvanced
cooldownHours                                  [数值]  例：360
defName                                        [文本]  例：ImbueDeathRefusal
description                                    [文本]  例：Link a target with a distant archotechnological engine that can bring them back 
hoursUntilOutcome                              [数值]  例：6
iconPath                                       [文本]  例：UI/PsychicRituals/PsychicRitual_ImbueDeathRefusal
label                                          [文本]  例：imbue death refusal
outcomeDescription                             [文本]  例：The target will gain death refusal.\n\nWith the current quality, all the target'
requiredOffering                               [容器]
requiredOffering/count                         [数值]  例：1
requiredOffering/filter                        [容器]
requiredOffering/filter/thingDefs              [容器]
requiredOffering/filter/thingDefs/li           [文本]  例：Shard
researchPrerequisite                           [文本]  例：DeathRefusal
skillOffsetPercentFromQualityCurve             [容器]
skillOffsetPercentFromQualityCurve/points      [容器]
skillOffsetPercentFromQualityCurve/points/li   [文本]  例：(0, -0.5) / (0.5, -0.15) / (0.75, -0.05)
targetRole                                     [文本]  例：DeathRefusalTarget
```

## 三、全量字段表（18 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `chanterRole` | 100.0% (1/1) | 文本 | ChanterAdvanced |
| `cooldownHours` | 100.0% (1/1) | 数值 | 360 |
| `defName` | 100.0% (1/1) | 文本 | ImbueDeathRefusal |
| `description` | 100.0% (1/1) | 文本 | Link a target with a distant archotechnological engine that can bring them back  |
| `hoursUntilOutcome` | 100.0% (1/1) | 数值 | 6 |
| `iconPath` | 100.0% (1/1) | 文本 | UI/PsychicRituals/PsychicRitual_ImbueDeathRefusal |
| `label` | 100.0% (1/1) | 文本 | imbue death refusal |
| `outcomeDescription` | 100.0% (1/1) | 文本 | The target will gain death refusal.\n\nWith the current quality, all the target' |
| `requiredOffering` | 100.0% (1/1) | 容器 |  |
| `requiredOffering/count` | 100.0% (1/1) | 数值 | 1 |
| `requiredOffering/filter` | 100.0% (1/1) | 容器 |  |
| `requiredOffering/filter/thingDefs` | 100.0% (1/1) | 容器 |  |
| `requiredOffering/filter/thingDefs/li` | 100.0% (1/1) | 文本 | Shard |
| `researchPrerequisite` | 100.0% (1/1) | 文本 | DeathRefusal |
| `skillOffsetPercentFromQualityCurve` | 100.0% (1/1) | 容器 |  |
| `skillOffsetPercentFromQualityCurve/points` | 100.0% (1/1) | 容器 |  |
| `skillOffsetPercentFromQualityCurve/points/li` | 400.0% (4/1) | 文本 | (0, -0.5) / (0.5, -0.15) / (0.75, -0.05) |
| `targetRole` | 100.0% (1/1) | 文本 | DeathRefusalTarget |

## 四、原版 defName 一览（共 1 个，列出前 60）

```text
`ImbueDeathRefusal`             
```
