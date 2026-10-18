# PsychicRitualDef_VoidProvocation

- **所属线**：世界线
- **原版实例数**：1
- **字段路径数**：15
- **资料片**：Anomaly
- **原版出处**：`Anomaly/Defs/PsychicRitualDefs/PsychicRituals.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<PsychicRitualDef_VoidProvocation>
    <defName>VoidProvocation</defName>
    <label>void provocation</label>
    <description>Psychically commune with the void, attracting an entity which can be captured and studied. There's a chance that the invoker will fall into a coma for several hours.</description>
    <iconPath>UI/PsychicRituals/PsychicRitual_VoidProvocation</iconPath>
    <outcomeDescription>With the current quality, there's a {0} chance the invoker will receive dark psychic shock.</outcomeDescription>
    <hoursUntilOutcome>2</hoursUntilOutcome>
    <cooldownHours>120</cooldownHours>
    <layerWhitelist>
      <li>Surface</li>
    </layerWhitelist>
    <psychicShockChanceFromQualityCurve>
      <points>
        <li>(0, 0.9)</li>
        <li>(0.5, 0.25)</li>
        <li>(0.9, 0.05)</li>
        <li>(1, 0.01)</li>
      </points>
    </psychicShockChanceFromQualityCurve>
    <darkPsychicShockDurarionHoursRange>2~4</darkPsychicShockDurarionHoursRange>
    <incidentDelayHoursRange>2~4</incidentDelayHoursRange>
    <researchPrerequisite>BasicPsychicRituals</researchPrerequisite>
  </PsychicRitualDef_VoidProvocation>

  
```

> 来自 `Anomaly/Defs/PsychicRitualDefs/PsychicRituals.xml`，defName = `VoidProvocation`，XML 节点数 19（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
cooldownHours                                  [数值]  例：120
darkPsychicShockDurarionHoursRange             [文本]  例：2~4
defName                                        [文本]  例：VoidProvocation
description                                    [文本]  例：Psychically commune with the void, attracting an entity which can be captured an
hoursUntilOutcome                              [数值]  例：2
iconPath                                       [文本]  例：UI/PsychicRituals/PsychicRitual_VoidProvocation
incidentDelayHoursRange                        [文本]  例：2~4
label                                          [文本]  例：void provocation
layerWhitelist                                 [容器]
layerWhitelist/li                              [文本]  例：Surface
outcomeDescription                             [文本]  例：With the current quality, there's a {0} chance the invoker will receive dark psy
psychicShockChanceFromQualityCurve             [容器]
psychicShockChanceFromQualityCurve/points      [容器]
psychicShockChanceFromQualityCurve/points/li   [文本]  例：(0, 0.9) / (0.5, 0.25) / (0.9, 0.05)
researchPrerequisite                           [文本]  例：BasicPsychicRituals
```

## 三、全量字段表（15 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `cooldownHours` | 100.0% (1/1) | 数值 | 120 |
| `darkPsychicShockDurarionHoursRange` | 100.0% (1/1) | 文本 | 2~4 |
| `defName` | 100.0% (1/1) | 文本 | VoidProvocation |
| `description` | 100.0% (1/1) | 文本 | Psychically commune with the void, attracting an entity which can be captured an |
| `hoursUntilOutcome` | 100.0% (1/1) | 数值 | 2 |
| `iconPath` | 100.0% (1/1) | 文本 | UI/PsychicRituals/PsychicRitual_VoidProvocation |
| `incidentDelayHoursRange` | 100.0% (1/1) | 文本 | 2~4 |
| `label` | 100.0% (1/1) | 文本 | void provocation |
| `layerWhitelist` | 100.0% (1/1) | 容器 |  |
| `layerWhitelist/li` | 100.0% (1/1) | 文本 | Surface |
| `outcomeDescription` | 100.0% (1/1) | 文本 | With the current quality, there's a {0} chance the invoker will receive dark psy |
| `psychicShockChanceFromQualityCurve` | 100.0% (1/1) | 容器 |  |
| `psychicShockChanceFromQualityCurve/points` | 100.0% (1/1) | 容器 |  |
| `psychicShockChanceFromQualityCurve/points/li` | 400.0% (4/1) | 文本 | (0, 0.9) / (0.5, 0.25) / (0.9, 0.05) |
| `researchPrerequisite` | 100.0% (1/1) | 文本 | BasicPsychicRituals |

## 四、原版 defName 一览（共 1 个，列出前 60）

```text
`VoidProvocation`               
```
