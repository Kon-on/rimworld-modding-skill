# PsychicRitualDef_BloodRain

- **所属线**：世界线
- **原版实例数**：1
- **字段路径数**：18
- **资料片**：Anomaly
- **原版出处**：`Anomaly/Defs/PsychicRitualDefs/PsychicRituals.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<PsychicRitualDef_BloodRain>
    <defName>BloodRain</defName>
    <label>blood rain</label>
    <description>Cast a ritual which causes blood-like psychofluid to fall from the sky. The fluid will slowly drive exposed humans and animals into a berserk frenzy. Traits and psychic sensitivity modulate the effect.</description>
    <researchPrerequisite>BloodRain</researchPrerequisite>
    <outcomeDescription>At the current ritual quality, the blood rain will last for {0}.</outcomeDescription>
    <hoursUntilOutcome>2</hoursUntilOutcome>
    <durationHoursFromQualityRange>3~16</durationHoursFromQualityRange>
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
      <count>70</count>
    </requiredOffering>
    <cooldownHours>600</cooldownHours>
    <chanterRole>ChanterAdvanced</chanterRole>
    <iconPath>UI/PsychicRituals/PsychicRitual_BloodRain</iconPath>
  </PsychicRitualDef_BloodRain>
  
  
```

> 来自 `Anomaly/Defs/PsychicRitualDefs/PsychicRituals.xml`，defName = `BloodRain`，XML 节点数 19（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
castableOnPocketMaps                           [布尔]  例：false
chanterRole                                    [文本]  例：ChanterAdvanced
cooldownHours                                  [数值]  例：600
defName                                        [文本]  例：BloodRain
description                                    [文本]  例：Cast a ritual which causes blood-like psychofluid to fall from the sky. The flui
durationHoursFromQualityRange                  [文本]  例：3~16
hoursUntilOutcome                              [数值]  例：2
iconPath                                       [文本]  例：UI/PsychicRituals/PsychicRitual_BloodRain
label                                          [文本]  例：blood rain
layerWhitelist                                 [容器]
layerWhitelist/li                              [文本]  例：Surface
outcomeDescription                             [文本]  例：At the current ritual quality, the blood rain will last for {0}.
requiredOffering                               [容器]
requiredOffering/count                         [数值]  例：70
requiredOffering/filter                        [容器]
requiredOffering/filter/thingDefs              [容器]
requiredOffering/filter/thingDefs/li           [文本]  例：Bioferrite
researchPrerequisite                           [文本]  例：BloodRain
```

## 三、全量字段表（18 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `castableOnPocketMaps` | 100.0% (1/1) | 布尔 | false |
| `chanterRole` | 100.0% (1/1) | 文本 | ChanterAdvanced |
| `cooldownHours` | 100.0% (1/1) | 数值 | 600 |
| `defName` | 100.0% (1/1) | 文本 | BloodRain |
| `description` | 100.0% (1/1) | 文本 | Cast a ritual which causes blood-like psychofluid to fall from the sky. The flui |
| `durationHoursFromQualityRange` | 100.0% (1/1) | 文本 | 3~16 |
| `hoursUntilOutcome` | 100.0% (1/1) | 数值 | 2 |
| `iconPath` | 100.0% (1/1) | 文本 | UI/PsychicRituals/PsychicRitual_BloodRain |
| `label` | 100.0% (1/1) | 文本 | blood rain |
| `layerWhitelist` | 100.0% (1/1) | 容器 |  |
| `layerWhitelist/li` | 100.0% (1/1) | 文本 | Surface |
| `outcomeDescription` | 100.0% (1/1) | 文本 | At the current ritual quality, the blood rain will last for {0}. |
| `requiredOffering` | 100.0% (1/1) | 容器 |  |
| `requiredOffering/count` | 100.0% (1/1) | 数值 | 70 |
| `requiredOffering/filter` | 100.0% (1/1) | 容器 |  |
| `requiredOffering/filter/thingDefs` | 100.0% (1/1) | 容器 |  |
| `requiredOffering/filter/thingDefs/li` | 100.0% (1/1) | 文本 | Bioferrite |
| `researchPrerequisite` | 100.0% (1/1) | 文本 | BloodRain |

## 四、原版 defName 一览（共 1 个，列出前 60）

```text
`BloodRain`                     
```
