# PsychicRitualDef_Chronophagy

- **所属线**：世界线
- **原版实例数**：1
- **字段路径数**：18
- **资料片**：Anomaly
- **原版出处**：`Anomaly/Defs/PsychicRitualDefs/PsychicRituals.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<PsychicRitualDef_Chronophagy>
    <defName>Chronophagy</defName>
    <label>chronophagy</label>
    <description>Induce a distant archotech to transfer entropy from one person to another. This causes the target to age rapidly while the invoker becomes younger, potentially healing scarring or age-related illnesses. The target will suffer brain damage, causing them to fall into a coma for several days.</description>
    <researchPrerequisite>Chronophagy</researchPrerequisite>
    <outcomeDescription>At the current ritual quality, the invoker will become {0} years younger and the target will become {1} years older.\n\nThe target will suffer brain damage and fall into a coma.</outcomeDescription>
    <targetRole>ChronophagyTarget</targetRole>
    <hoursUntilOutcome>4</hoursUntilOutcome>
    <requiredOffering>
      <filter>
        <thingDefs>
          <li>Bioferrite</li>
        </thingDefs>
      </filter>
      <count>20</count>
    </requiredOffering>
    <yearsTransferredFromQualityRange>1~25</yearsTransferredFromQualityRange>
    <cooldownHours>120</cooldownHours>
    <iconPath>UI/PsychicRituals/PsychicRitual_Chronophagy</iconPath>
    <brainDamageFromAgeCurve>
      <points>
        <li>(0, 1)</li>
        <li>(70, 1)</li>
        <li>(90, 5)</li>
        <li>(100, 8)</li>
        <li>(140, 10)</li>
        <li>(200, 200)</li>
      </points>
    </brainDamageFromAgeCurve>
  </PsychicRitualDef_Chronophagy>

  
```

> 来自 `Anomaly/Defs/PsychicRitualDefs/PsychicRituals.xml`，defName = `Chronophagy`，XML 节点数 24（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
brainDamageFromAgeCurve                        [容器]
brainDamageFromAgeCurve/points                 [容器]
brainDamageFromAgeCurve/points/li              [文本]  例：(0, 1) / (100, 8) / (70, 1)
cooldownHours                                  [数值]  例：120
defName                                        [文本]  例：Chronophagy
description                                    [文本]  例：Induce a distant archotech to transfer entropy from one person to another. This 
hoursUntilOutcome                              [数值]  例：4
iconPath                                       [文本]  例：UI/PsychicRituals/PsychicRitual_Chronophagy
label                                          [文本]  例：chronophagy
outcomeDescription                             [文本]  例：At the current ritual quality, the invoker will become {0} years younger and the
requiredOffering                               [容器]
requiredOffering/count                         [数值]  例：20
requiredOffering/filter                        [容器]
requiredOffering/filter/thingDefs              [容器]
requiredOffering/filter/thingDefs/li           [文本]  例：Bioferrite
researchPrerequisite                           [文本]  例：Chronophagy
targetRole                                     [文本]  例：ChronophagyTarget
yearsTransferredFromQualityRange               [文本]  例：1~25
```

## 三、全量字段表（18 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `brainDamageFromAgeCurve` | 100.0% (1/1) | 容器 |  |
| `brainDamageFromAgeCurve/points` | 100.0% (1/1) | 容器 |  |
| `brainDamageFromAgeCurve/points/li` | 600.0% (6/1) | 文本 | (0, 1) / (100, 8) / (70, 1) |
| `cooldownHours` | 100.0% (1/1) | 数值 | 120 |
| `defName` | 100.0% (1/1) | 文本 | Chronophagy |
| `description` | 100.0% (1/1) | 文本 | Induce a distant archotech to transfer entropy from one person to another. This  |
| `hoursUntilOutcome` | 100.0% (1/1) | 数值 | 4 |
| `iconPath` | 100.0% (1/1) | 文本 | UI/PsychicRituals/PsychicRitual_Chronophagy |
| `label` | 100.0% (1/1) | 文本 | chronophagy |
| `outcomeDescription` | 100.0% (1/1) | 文本 | At the current ritual quality, the invoker will become {0} years younger and the |
| `requiredOffering` | 100.0% (1/1) | 容器 |  |
| `requiredOffering/count` | 100.0% (1/1) | 数值 | 20 |
| `requiredOffering/filter` | 100.0% (1/1) | 容器 |  |
| `requiredOffering/filter/thingDefs` | 100.0% (1/1) | 容器 |  |
| `requiredOffering/filter/thingDefs/li` | 100.0% (1/1) | 文本 | Bioferrite |
| `researchPrerequisite` | 100.0% (1/1) | 文本 | Chronophagy |
| `targetRole` | 100.0% (1/1) | 文本 | ChronophagyTarget |
| `yearsTransferredFromQualityRange` | 100.0% (1/1) | 文本 | 1~25 |

## 四、原版 defName 一览（共 1 个，列出前 60）

```text
`Chronophagy`                   
```
