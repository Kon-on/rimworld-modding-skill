# RitualAttachableOutcomeEffectDef

- **所属线**：理念线
- **原版实例数**：7
- **字段路径数**：10
- **资料片**：Ideology、Royalty
- **原版出处**：`Ideology/Defs/PreceptDefs/Ritual_AttachableOutcomes_Special.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<RitualAttachableOutcomeEffectDef>
    <defName>NearbyFactionGoodwill</defName>
    <label>nearby faction goodwill</label>
    <effectDesc>you will gain goodwill from the nearest faction base.</effectDesc>
    <letterInfoText>You gained {AMOUNT} goodwill with {FACTION_name}.</letterInfoText>
    <workerClass>RitualAttachableOutcomeEffectWorker_NearbyFactionGoodwill</workerClass>
  </RitualAttachableOutcomeEffectDef>

  
```

> 来自 `Ideology/Defs/PreceptDefs/Ritual_AttachableOutcomes_Special.xml`，defName = `NearbyFactionGoodwill`，XML 节点数 6（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：FarmAnimalsWanderIn / GauranlenTreePod / InsectJellyTunnels
effectDesc                                     [文本]  例：a Gauranlen pod will sprout at a random location on the map, if it can. / a group of farm animals will be attracted and join the colony. / insect jelly deposits will be deposited from underground.
label                                          [文本]  例：farm animals wander in / gauranlen pod sprout / insect jelly
letterInfoText                                 [文本]  例：A Gauranlen pod sprouted nearby. / A giant insect colony underground has deposited some insect jelly. / Curious farm animals have wandered in, attracted by the commotion.
workerClass                                    [文本]  例：RitualAttachableOutcomeEffectWorker_FarmAnimalsWanderIn / RitualAttachableOutcomeEffectWorker_GauranlenPosSprout / RitualAttachableOutcomeEffectWorker_InsectJellyTunnels
```

## 三、全量字段表（10 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (7/7) | 文本 | FarmAnimalsWanderIn / GauranlenTreePod / InsectJellyTunnels |
| `disallowedRituals` | 14.3% (1/7) | 容器 |  |
| `disallowedRituals/li` | 28.6% (2/7) | 文本 | FuneralNoCorpse / FuneralStandard |
| `effectDesc` | 100.0% (7/7) | 文本 | a Gauranlen pod will sprout at a random location on the map, if it can. / a group of farm animals will be attr |
| `label` | 100.0% (7/7) | 文本 | farm animals wander in / gauranlen pod sprout / insect jelly |
| `letterInfoText` | 100.0% (7/7) | 文本 | A Gauranlen pod sprouted nearby. / A giant insect colony underground has deposited some insect jelly. / Curiou |
| `requiredFaction` | 14.3% (1/7) | 文本 | Insect |
| `requiredMemeAny` | 42.9% (3/7) | 容器 |  |
| `requiredMemeAny/li` | 85.7% (6/7) | 文本 | AnimalPersonhood / NaturePrimacy / Rancher |
| `workerClass` | 100.0% (7/7) | 文本 | RitualAttachableOutcomeEffectWorker_FarmAnimalsWanderIn / RitualAttachableOutcomeEffectWorker_GauranlenPosSpro |

## 四、原版 defName 一览（共 7 个，列出前 60）

```text
`NearbyFactionGoodwill`           `DiscoverAncientComplex`          `RechargePsyfocus`                `GauranlenTreePod`              
`InsectJellyTunnels`              `RandomRecruit`                   `FarmAnimalsWanderIn`           
```
