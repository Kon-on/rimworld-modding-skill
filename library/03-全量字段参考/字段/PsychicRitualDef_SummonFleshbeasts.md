# PsychicRitualDef_SummonFleshbeasts

- **所属线**：世界线
- **原版实例数**：1
- **字段路径数**：17
- **资料片**：Anomaly
- **原版出处**：`Anomaly/Defs/PsychicRitualDefs/PsychicRituals.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<PsychicRitualDef_SummonFleshbeasts>
    <defName>SummonFleshbeasts</defName>
    <label>draw fleshbeasts</label>
    <description>Create a psychic pulse which will draw fleshbeasts to dig upwards and emerge near your enemies. They will attack anyone they find, including your enemies and allies. The fleshbeasts can be captured and studied, or butchered for twisted meat.</description>
    <outcomeDescription>Create a psychic pulse which will draw a horde of fleshbeasts.</outcomeDescription>
    <letterAICompleteLabel>Fleshbeasts emerging</letterAICompleteLabel>
    <letterAICompleteText>Fleshbeasts are clawing their way out of the ground. Prepare for their attack!</letterAICompleteText>
    <aiCastable>true</aiCastable>
    <playerCastable>false</playerCastable>
    <hoursUntilOutcome>4</hoursUntilOutcome>
    <nonRequiredPawnsMayLeave>true</nonRequiredPawnsMayLeave>
    <defenderRole>Defender</defenderRole>
    <letterAIArrivedText>They intend to use a psychic ritual to summon hideous fleshbeasts to attack you.</letterAIArrivedText>
    <layerWhitelist>
      <li>Surface</li>
    </layerWhitelist>
    <fleshbeastPointsFromThreatPointsCurve>
      <points>
        <li>(250, 100)</li>
        <li>(1000, 300)</li>
        <li>(5000, 600)</li>
      </points>
    </fleshbeastPointsFromThreatPointsCurve>
  </PsychicRitualDef_SummonFleshbeasts>

  
```

> 来自 `Anomaly/Defs/PsychicRitualDefs/PsychicRituals.xml`，defName = `SummonFleshbeasts`，XML 节点数 20（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
aiCastable                                     [布尔]  例：true
defenderRole                                   [文本]  例：Defender
defName                                        [文本]  例：SummonFleshbeasts
description                                    [文本]  例：Create a psychic pulse which will draw fleshbeasts to dig upwards and emerge nea
fleshbeastPointsFromThreatPointsCurve          [容器]
fleshbeastPointsFromThreatPointsCurve/points   [容器]
fleshbeastPointsFromThreatPointsCurve/points/li [文本]  例：(1000, 300) / (250, 100) / (5000, 600)
hoursUntilOutcome                              [数值]  例：4
label                                          [文本]  例：draw fleshbeasts
layerWhitelist                                 [容器]
layerWhitelist/li                              [文本]  例：Surface
letterAIArrivedText                            [文本]  例：They intend to use a psychic ritual to summon hideous fleshbeasts to attack you.
letterAICompleteLabel                          [文本]  例：Fleshbeasts emerging
letterAICompleteText                           [文本]  例：Fleshbeasts are clawing their way out of the ground. Prepare for their attack!
nonRequiredPawnsMayLeave                       [布尔]  例：true
outcomeDescription                             [文本]  例：Create a psychic pulse which will draw a horde of fleshbeasts.
playerCastable                                 [布尔]  例：false
```

## 三、全量字段表（17 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `aiCastable` | 100.0% (1/1) | 布尔 | true |
| `defenderRole` | 100.0% (1/1) | 文本 | Defender |
| `defName` | 100.0% (1/1) | 文本 | SummonFleshbeasts |
| `description` | 100.0% (1/1) | 文本 | Create a psychic pulse which will draw fleshbeasts to dig upwards and emerge nea |
| `fleshbeastPointsFromThreatPointsCurve` | 100.0% (1/1) | 容器 |  |
| `fleshbeastPointsFromThreatPointsCurve/points` | 100.0% (1/1) | 容器 |  |
| `fleshbeastPointsFromThreatPointsCurve/points/li` | 300.0% (3/1) | 文本 | (1000, 300) / (250, 100) / (5000, 600) |
| `hoursUntilOutcome` | 100.0% (1/1) | 数值 | 4 |
| `label` | 100.0% (1/1) | 文本 | draw fleshbeasts |
| `layerWhitelist` | 100.0% (1/1) | 容器 |  |
| `layerWhitelist/li` | 100.0% (1/1) | 文本 | Surface |
| `letterAIArrivedText` | 100.0% (1/1) | 文本 | They intend to use a psychic ritual to summon hideous fleshbeasts to attack you. |
| `letterAICompleteLabel` | 100.0% (1/1) | 文本 | Fleshbeasts emerging |
| `letterAICompleteText` | 100.0% (1/1) | 文本 | Fleshbeasts are clawing their way out of the ground. Prepare for their attack! |
| `nonRequiredPawnsMayLeave` | 100.0% (1/1) | 布尔 | true |
| `outcomeDescription` | 100.0% (1/1) | 文本 | Create a psychic pulse which will draw a horde of fleshbeasts. |
| `playerCastable` | 100.0% (1/1) | 布尔 | false |

## 四、原版 defName 一览（共 1 个，列出前 60）

```text
`SummonFleshbeasts`             
```
