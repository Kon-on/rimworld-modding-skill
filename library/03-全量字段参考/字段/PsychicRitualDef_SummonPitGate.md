# PsychicRitualDef_SummonPitGate

- **所属线**：世界线
- **原版实例数**：1
- **字段路径数**：18
- **资料片**：Anomaly
- **原版出处**：`Anomaly/Defs/PsychicRitualDefs/PsychicRituals.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<PsychicRitualDef_SummonPitGate>
    <defName>SummonPitGate</defName>
    <label>provoke pit gate</label>
    <description>Use a psychic pulse to provoke underground fleshbeasts into opening a massive pit gate in the ground somewhere in the local area. The massive sinkhole will lead down to a fleshbeast-infested cavern which can be explored for resources.</description>
    <iconPath>UI/PsychicRituals/PsychicRitual_SummonPitGate</iconPath>
    <researchPrerequisite>SummonPitGate</researchPrerequisite>
    <outcomeDescription>A higher-quality ritual will attract more fleshbeasts. The fleshbeasts can be captured and studied, or butchered for twisted meat.</outcomeDescription>
    <hoursUntilOutcome>6</hoursUntilOutcome>
    <castableOnPocketMaps>false</castableOnPocketMaps>
    <layerWhitelist>
      <li>Surface</li>
    </layerWhitelist>
    <combatPointMultiplierFromQualityRange>0.5~1.25</combatPointMultiplierFromQualityRange>
    <requiredOffering>
      <filter>
        <thingDefs>
          <li>Bioferrite</li>
        </thingDefs>
      </filter>
      <count>75</count>
    </requiredOffering>
    <cooldownHours>1080</cooldownHours>
    <chanterRole>ChanterAdvanced</chanterRole>
  </PsychicRitualDef_SummonPitGate>

  
```

> 来自 `Anomaly/Defs/PsychicRitualDefs/PsychicRituals.xml`，defName = `SummonPitGate`，XML 节点数 19（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
castableOnPocketMaps                           [布尔]  例：false
chanterRole                                    [文本]  例：ChanterAdvanced
combatPointMultiplierFromQualityRange          [文本]  例：0.5~1.25
cooldownHours                                  [数值]  例：1080
defName                                        [文本]  例：SummonPitGate
description                                    [文本]  例：Use a psychic pulse to provoke underground fleshbeasts into opening a massive pi
hoursUntilOutcome                              [数值]  例：6
iconPath                                       [文本]  例：UI/PsychicRituals/PsychicRitual_SummonPitGate
label                                          [文本]  例：provoke pit gate
layerWhitelist                                 [容器]
layerWhitelist/li                              [文本]  例：Surface
outcomeDescription                             [文本]  例：A higher-quality ritual will attract more fleshbeasts. The fleshbeasts can be ca
requiredOffering                               [容器]
requiredOffering/count                         [数值]  例：75
requiredOffering/filter                        [容器]
requiredOffering/filter/thingDefs              [容器]
requiredOffering/filter/thingDefs/li           [文本]  例：Bioferrite
researchPrerequisite                           [文本]  例：SummonPitGate
```

## 三、全量字段表（18 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `castableOnPocketMaps` | 100.0% (1/1) | 布尔 | false |
| `chanterRole` | 100.0% (1/1) | 文本 | ChanterAdvanced |
| `combatPointMultiplierFromQualityRange` | 100.0% (1/1) | 文本 | 0.5~1.25 |
| `cooldownHours` | 100.0% (1/1) | 数值 | 1080 |
| `defName` | 100.0% (1/1) | 文本 | SummonPitGate |
| `description` | 100.0% (1/1) | 文本 | Use a psychic pulse to provoke underground fleshbeasts into opening a massive pi |
| `hoursUntilOutcome` | 100.0% (1/1) | 数值 | 6 |
| `iconPath` | 100.0% (1/1) | 文本 | UI/PsychicRituals/PsychicRitual_SummonPitGate |
| `label` | 100.0% (1/1) | 文本 | provoke pit gate |
| `layerWhitelist` | 100.0% (1/1) | 容器 |  |
| `layerWhitelist/li` | 100.0% (1/1) | 文本 | Surface |
| `outcomeDescription` | 100.0% (1/1) | 文本 | A higher-quality ritual will attract more fleshbeasts. The fleshbeasts can be ca |
| `requiredOffering` | 100.0% (1/1) | 容器 |  |
| `requiredOffering/count` | 100.0% (1/1) | 数值 | 75 |
| `requiredOffering/filter` | 100.0% (1/1) | 容器 |  |
| `requiredOffering/filter/thingDefs` | 100.0% (1/1) | 容器 |  |
| `requiredOffering/filter/thingDefs/li` | 100.0% (1/1) | 文本 | Bioferrite |
| `researchPrerequisite` | 100.0% (1/1) | 文本 | SummonPitGate |

## 四、原版 defName 一览（共 1 个，列出前 60）

```text
`SummonPitGate`                 
```
