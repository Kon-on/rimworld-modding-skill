# PsychicRitualDef_Philophagy

- **所属线**：世界线
- **原版实例数**：1
- **字段路径数**：18
- **资料片**：Anomaly
- **原版出处**：`Anomaly/Defs/PsychicRitualDefs/PsychicRituals.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<PsychicRitualDef_Philophagy>
    <defName>Philophagy</defName>
    <label>philophagy</label>
    <description>Psychically draw experiences from the victim's mind and transfer them to the invoker, targeting the victim's highest skill. The target will suffer brain damage, causing them to fall into a coma for several days.</description>
    <researchPrerequisite>Philophagy</researchPrerequisite>
    <outcomeDescription>With the current ritual quality, the invoker will steal {0} of the target's XP in their best skill.\n\nThe target will suffer brain damage and fall into a coma.</outcomeDescription>
    <targetRole>PhilophagyTarget</targetRole>
    <hoursUntilOutcome>4</hoursUntilOutcome>
    <requiredOffering>
      <filter>
        <thingDefs>
          <li>Shard</li>
        </thingDefs>
      </filter>
      <count>1</count>
    </requiredOffering>
    <brainDamageRange>3~5</brainDamageRange>
    <xpTransferFromQualityCurve>
      <points>
        <li>(0, 0.1)</li>
        <li>(0.5, 0.3)</li>
        <li>(0.9, 0.5)</li>
        <li>(1, 0.8)</li>
      </points>
    </xpTransferFromQualityCurve>
    <cooldownHours>120</cooldownHours>
    <iconPath>UI/PsychicRituals/PsychicRitual_Philophagy</iconPath>
  </PsychicRitualDef_Philophagy>

  
```

> 来自 `Anomaly/Defs/PsychicRitualDefs/PsychicRituals.xml`，defName = `Philophagy`，XML 节点数 22（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
brainDamageRange                               [文本]  例：3~5
cooldownHours                                  [数值]  例：120
defName                                        [文本]  例：Philophagy
description                                    [文本]  例：Psychically draw experiences from the victim's mind and transfer them to the inv
hoursUntilOutcome                              [数值]  例：4
iconPath                                       [文本]  例：UI/PsychicRituals/PsychicRitual_Philophagy
label                                          [文本]  例：philophagy
outcomeDescription                             [文本]  例：With the current ritual quality, the invoker will steal {0} of the target's XP i
requiredOffering                               [容器]
requiredOffering/count                         [数值]  例：1
requiredOffering/filter                        [容器]
requiredOffering/filter/thingDefs              [容器]
requiredOffering/filter/thingDefs/li           [文本]  例：Shard
researchPrerequisite                           [文本]  例：Philophagy
targetRole                                     [文本]  例：PhilophagyTarget
xpTransferFromQualityCurve                     [容器]
xpTransferFromQualityCurve/points              [容器]
xpTransferFromQualityCurve/points/li           [文本]  例：(0, 0.1) / (0.5, 0.3) / (0.9, 0.5)
```

## 三、全量字段表（18 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `brainDamageRange` | 100.0% (1/1) | 文本 | 3~5 |
| `cooldownHours` | 100.0% (1/1) | 数值 | 120 |
| `defName` | 100.0% (1/1) | 文本 | Philophagy |
| `description` | 100.0% (1/1) | 文本 | Psychically draw experiences from the victim's mind and transfer them to the inv |
| `hoursUntilOutcome` | 100.0% (1/1) | 数值 | 4 |
| `iconPath` | 100.0% (1/1) | 文本 | UI/PsychicRituals/PsychicRitual_Philophagy |
| `label` | 100.0% (1/1) | 文本 | philophagy |
| `outcomeDescription` | 100.0% (1/1) | 文本 | With the current ritual quality, the invoker will steal {0} of the target's XP i |
| `requiredOffering` | 100.0% (1/1) | 容器 |  |
| `requiredOffering/count` | 100.0% (1/1) | 数值 | 1 |
| `requiredOffering/filter` | 100.0% (1/1) | 容器 |  |
| `requiredOffering/filter/thingDefs` | 100.0% (1/1) | 容器 |  |
| `requiredOffering/filter/thingDefs/li` | 100.0% (1/1) | 文本 | Shard |
| `researchPrerequisite` | 100.0% (1/1) | 文本 | Philophagy |
| `targetRole` | 100.0% (1/1) | 文本 | PhilophagyTarget |
| `xpTransferFromQualityCurve` | 100.0% (1/1) | 容器 |  |
| `xpTransferFromQualityCurve/points` | 100.0% (1/1) | 容器 |  |
| `xpTransferFromQualityCurve/points/li` | 400.0% (4/1) | 文本 | (0, 0.1) / (0.5, 0.3) / (0.9, 0.5) |

## 四、原版 defName 一览（共 1 个，列出前 60）

```text
`Philophagy`                    
```
