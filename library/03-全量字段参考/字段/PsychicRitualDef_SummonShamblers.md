# PsychicRitualDef_SummonShamblers

- **所属线**：世界线
- **原版实例数**：1
- **字段路径数**：16
- **资料片**：Anomaly
- **原版出处**：`Anomaly/Defs/PsychicRitualDefs/PsychicRituals.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<PsychicRitualDef_SummonShamblers>
    <defName>SummonShamblers</defName>
    <label>draw shamblers</label>
    <description>Create a psychic pulse which will draw a distant horde of animated corpses towards your local area. While they attack any humans that they see, they won't attack your colony directly. You can capture them for study.</description>
    <researchPrerequisite>SummonShamblers</researchPrerequisite>
    <outcomeDescription>The higher the ritual quality, the more shamblers that will be summoned.</outcomeDescription>
    <hoursUntilOutcome>2</hoursUntilOutcome>
    <combatPointsFromQualityRange>200~2500</combatPointsFromQualityRange>
    <layerWhitelist>
      <li>Surface</li>
    </layerWhitelist>
    <requiredOffering>
      <filter>
        <thingDefs>
          <li>Bioferrite</li>
        </thingDefs>
      </filter>
      <count>20</count>
    </requiredOffering>
    <cooldownHours>120</cooldownHours>
    <iconPath>UI/PsychicRituals/PsychicRitual_SummonShamblers</iconPath>
  </PsychicRitualDef_SummonShamblers>

  
```

> 来自 `Anomaly/Defs/PsychicRitualDefs/PsychicRituals.xml`，defName = `SummonShamblers`，XML 节点数 17（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
combatPointsFromQualityRange                   [文本]  例：200~2500
cooldownHours                                  [数值]  例：120
defName                                        [文本]  例：SummonShamblers
description                                    [文本]  例：Create a psychic pulse which will draw a distant horde of animated corpses towar
hoursUntilOutcome                              [数值]  例：2
iconPath                                       [文本]  例：UI/PsychicRituals/PsychicRitual_SummonShamblers
label                                          [文本]  例：draw shamblers
layerWhitelist                                 [容器]
layerWhitelist/li                              [文本]  例：Surface
outcomeDescription                             [文本]  例：The higher the ritual quality, the more shamblers that will be summoned.
requiredOffering                               [容器]
requiredOffering/count                         [数值]  例：20
requiredOffering/filter                        [容器]
requiredOffering/filter/thingDefs              [容器]
requiredOffering/filter/thingDefs/li           [文本]  例：Bioferrite
researchPrerequisite                           [文本]  例：SummonShamblers
```

## 三、全量字段表（16 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `combatPointsFromQualityRange` | 100.0% (1/1) | 文本 | 200~2500 |
| `cooldownHours` | 100.0% (1/1) | 数值 | 120 |
| `defName` | 100.0% (1/1) | 文本 | SummonShamblers |
| `description` | 100.0% (1/1) | 文本 | Create a psychic pulse which will draw a distant horde of animated corpses towar |
| `hoursUntilOutcome` | 100.0% (1/1) | 数值 | 2 |
| `iconPath` | 100.0% (1/1) | 文本 | UI/PsychicRituals/PsychicRitual_SummonShamblers |
| `label` | 100.0% (1/1) | 文本 | draw shamblers |
| `layerWhitelist` | 100.0% (1/1) | 容器 |  |
| `layerWhitelist/li` | 100.0% (1/1) | 文本 | Surface |
| `outcomeDescription` | 100.0% (1/1) | 文本 | The higher the ritual quality, the more shamblers that will be summoned. |
| `requiredOffering` | 100.0% (1/1) | 容器 |  |
| `requiredOffering/count` | 100.0% (1/1) | 数值 | 20 |
| `requiredOffering/filter` | 100.0% (1/1) | 容器 |  |
| `requiredOffering/filter/thingDefs` | 100.0% (1/1) | 容器 |  |
| `requiredOffering/filter/thingDefs/li` | 100.0% (1/1) | 文本 | Bioferrite |
| `researchPrerequisite` | 100.0% (1/1) | 文本 | SummonShamblers |

## 四、原版 defName 一览（共 1 个，列出前 60）

```text
`SummonShamblers`               
```
