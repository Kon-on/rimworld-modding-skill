# PsychicRitualDef_SummonFleshbeastsPlayer

- **所属线**：世界线
- **原版实例数**：1
- **字段路径数**：20
- **资料片**：Anomaly
- **原版出处**：`Anomaly/Defs/PsychicRitualDefs/PsychicRituals.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<PsychicRitualDef_SummonFleshbeastsPlayer>
    <defName>SummonFleshbeastsPlayer</defName>
    <label>draw fleshbeasts</label>
    <description>Create a psychic pulse which will draw fleshbeasts to dig upwards and emerge near your enemies. They will attack anyone they find, including your enemies and allies. The fleshbeasts can be captured and studied, or butchered for twisted meat.</description>
    <researchPrerequisite>SummonFleshbeastsPlayer</researchPrerequisite>
    <outcomeDescription>A higher quality ritual will attract more fleshbeasts.</outcomeDescription>
    <hoursUntilOutcome>2</hoursUntilOutcome>
    <castableOnPocketMaps>false</castableOnPocketMaps>
    <layerWhitelist>
      <li>Surface</li>
    </layerWhitelist>
    <requiredOffering>
      <filter>
        <thingDefs>
          <li>Bioferrite</li>
        </thingDefs>
      </filter>
      <count>50</count>
    </requiredOffering>
    <cooldownHours>120</cooldownHours>
    <chanterRole>ChanterAdvanced</chanterRole>
    <fleshbeastCombatPointsFromQualityCurve>
      <points>
        <li>(0, 200)</li>
        <li>(0.7, 600)</li>
        <li>(0.9, 1200)</li>
        <li>(1, 2400)</li>
      </points>
    </fleshbeastCombatPointsFromQualityCurve>
    <iconPath>UI/PsychicRituals/PsychicRitual_SummonFleshbeasts</iconPath>
  </PsychicRitualDef_SummonFleshbeastsPlayer>
```

> 来自 `Anomaly/Defs/PsychicRitualDefs/PsychicRituals.xml`，defName = `SummonFleshbeastsPlayer`，XML 节点数 24（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
castableOnPocketMaps                           [布尔]  例：false
chanterRole                                    [文本]  例：ChanterAdvanced
cooldownHours                                  [数值]  例：120
defName                                        [文本]  例：SummonFleshbeastsPlayer
description                                    [文本]  例：Create a psychic pulse which will draw fleshbeasts to dig upwards and emerge nea
fleshbeastCombatPointsFromQualityCurve         [容器]
fleshbeastCombatPointsFromQualityCurve/points  [容器]
fleshbeastCombatPointsFromQualityCurve/points/li [文本]  例：(0, 200) / (0.7, 600) / (0.9, 1200)
hoursUntilOutcome                              [数值]  例：2
iconPath                                       [文本]  例：UI/PsychicRituals/PsychicRitual_SummonFleshbeasts
label                                          [文本]  例：draw fleshbeasts
layerWhitelist                                 [容器]
layerWhitelist/li                              [文本]  例：Surface
outcomeDescription                             [文本]  例：A higher quality ritual will attract more fleshbeasts.
requiredOffering                               [容器]
requiredOffering/count                         [数值]  例：50
requiredOffering/filter                        [容器]
requiredOffering/filter/thingDefs              [容器]
requiredOffering/filter/thingDefs/li           [文本]  例：Bioferrite
researchPrerequisite                           [文本]  例：SummonFleshbeastsPlayer
```

## 三、全量字段表（20 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `castableOnPocketMaps` | 100.0% (1/1) | 布尔 | false |
| `chanterRole` | 100.0% (1/1) | 文本 | ChanterAdvanced |
| `cooldownHours` | 100.0% (1/1) | 数值 | 120 |
| `defName` | 100.0% (1/1) | 文本 | SummonFleshbeastsPlayer |
| `description` | 100.0% (1/1) | 文本 | Create a psychic pulse which will draw fleshbeasts to dig upwards and emerge nea |
| `fleshbeastCombatPointsFromQualityCurve` | 100.0% (1/1) | 容器 |  |
| `fleshbeastCombatPointsFromQualityCurve/points` | 100.0% (1/1) | 容器 |  |
| `fleshbeastCombatPointsFromQualityCurve/points/li` | 400.0% (4/1) | 文本 | (0, 200) / (0.7, 600) / (0.9, 1200) |
| `hoursUntilOutcome` | 100.0% (1/1) | 数值 | 2 |
| `iconPath` | 100.0% (1/1) | 文本 | UI/PsychicRituals/PsychicRitual_SummonFleshbeasts |
| `label` | 100.0% (1/1) | 文本 | draw fleshbeasts |
| `layerWhitelist` | 100.0% (1/1) | 容器 |  |
| `layerWhitelist/li` | 100.0% (1/1) | 文本 | Surface |
| `outcomeDescription` | 100.0% (1/1) | 文本 | A higher quality ritual will attract more fleshbeasts. |
| `requiredOffering` | 100.0% (1/1) | 容器 |  |
| `requiredOffering/count` | 100.0% (1/1) | 数值 | 50 |
| `requiredOffering/filter` | 100.0% (1/1) | 容器 |  |
| `requiredOffering/filter/thingDefs` | 100.0% (1/1) | 容器 |  |
| `requiredOffering/filter/thingDefs/li` | 100.0% (1/1) | 文本 | Bioferrite |
| `researchPrerequisite` | 100.0% (1/1) | 文本 | SummonFleshbeastsPlayer |

## 四、原版 defName 一览（共 1 个，列出前 60）

```text
`SummonFleshbeastsPlayer`       
```
