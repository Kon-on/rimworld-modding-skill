# PsychicRitualDef_SummonAnimals

- **所属线**：世界线
- **原版实例数**：1
- **字段路径数**：18
- **资料片**：Anomaly
- **原版出处**：`Anomaly/Defs/PsychicRitualDefs/PsychicRituals.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<PsychicRitualDef_SummonAnimals>
    <defName>SummonAnimals</defName>
    <label>draw animals</label>
    <description>Create a psychic pulse which will draw a distant herd of animals into the local area. You can then hunt or make use of them as you choose. If not done correctly, this may attract scaria-infected manhunters.</description>
    <researchPrerequisite>SummonAnimals</researchPrerequisite>
    <outcomeDescription>With the current ritual quality, there is a {0} chance that the animals will arrive as manhunters.</outcomeDescription>
    <hoursUntilOutcome>4</hoursUntilOutcome>
    <layerWhitelist>
      <li>Surface</li>
    </layerWhitelist>
    <manhunterSpawnChanceFromQualityCurve>
      <points>
        <li>(0, 0.75)</li>
        <li>(0.75, 0.1)</li>
        <li>(0.9, 0.05)</li>
        <li>(1, 0.01)</li>
      </points>
    </manhunterSpawnChanceFromQualityCurve>
    <requiredOffering>
      <filter>
        <thingDefs>
          <li>Bioferrite</li>
        </thingDefs>
      </filter>
      <count>10</count>
    </requiredOffering>
    <cooldownHours>240</cooldownHours>
    <iconPath>UI/PsychicRituals/PsychicRitual_SummonAnimals</iconPath>
  </PsychicRitualDef_SummonAnimals>

  
```

> 来自 `Anomaly/Defs/PsychicRitualDefs/PsychicRituals.xml`，defName = `SummonAnimals`，XML 节点数 22（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
cooldownHours                                  [数值]  例：240
defName                                        [文本]  例：SummonAnimals
description                                    [文本]  例：Create a psychic pulse which will draw a distant herd of animals into the local 
hoursUntilOutcome                              [数值]  例：4
iconPath                                       [文本]  例：UI/PsychicRituals/PsychicRitual_SummonAnimals
label                                          [文本]  例：draw animals
layerWhitelist                                 [容器]
layerWhitelist/li                              [文本]  例：Surface
manhunterSpawnChanceFromQualityCurve           [容器]
manhunterSpawnChanceFromQualityCurve/points    [容器]
manhunterSpawnChanceFromQualityCurve/points/li [文本]  例：(0, 0.75) / (0.75, 0.1) / (0.9, 0.05)
outcomeDescription                             [文本]  例：With the current ritual quality, there is a {0} chance that the animals will arr
requiredOffering                               [容器]
requiredOffering/count                         [数值]  例：10
requiredOffering/filter                        [容器]
requiredOffering/filter/thingDefs              [容器]
requiredOffering/filter/thingDefs/li           [文本]  例：Bioferrite
researchPrerequisite                           [文本]  例：SummonAnimals
```

## 三、全量字段表（18 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `cooldownHours` | 100.0% (1/1) | 数值 | 240 |
| `defName` | 100.0% (1/1) | 文本 | SummonAnimals |
| `description` | 100.0% (1/1) | 文本 | Create a psychic pulse which will draw a distant herd of animals into the local  |
| `hoursUntilOutcome` | 100.0% (1/1) | 数值 | 4 |
| `iconPath` | 100.0% (1/1) | 文本 | UI/PsychicRituals/PsychicRitual_SummonAnimals |
| `label` | 100.0% (1/1) | 文本 | draw animals |
| `layerWhitelist` | 100.0% (1/1) | 容器 |  |
| `layerWhitelist/li` | 100.0% (1/1) | 文本 | Surface |
| `manhunterSpawnChanceFromQualityCurve` | 100.0% (1/1) | 容器 |  |
| `manhunterSpawnChanceFromQualityCurve/points` | 100.0% (1/1) | 容器 |  |
| `manhunterSpawnChanceFromQualityCurve/points/li` | 400.0% (4/1) | 文本 | (0, 0.75) / (0.75, 0.1) / (0.9, 0.05) |
| `outcomeDescription` | 100.0% (1/1) | 文本 | With the current ritual quality, there is a {0} chance that the animals will arr |
| `requiredOffering` | 100.0% (1/1) | 容器 |  |
| `requiredOffering/count` | 100.0% (1/1) | 数值 | 10 |
| `requiredOffering/filter` | 100.0% (1/1) | 容器 |  |
| `requiredOffering/filter/thingDefs` | 100.0% (1/1) | 容器 |  |
| `requiredOffering/filter/thingDefs/li` | 100.0% (1/1) | 文本 | Bioferrite |
| `researchPrerequisite` | 100.0% (1/1) | 文本 | SummonAnimals |

## 四、原版 defName 一览（共 1 个，列出前 60）

```text
`SummonAnimals`                 
```
