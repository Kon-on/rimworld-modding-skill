# LifeStageDef

- **所属线**：人物线
- **原版实例数**：19
- **字段路径数**：54
- **资料片**：Anomaly、Biotech、Core
- **原版出处**：`Anomaly/Defs/LifeStageDefs/LifeStages.xml`、`Core/Defs/Misc/LifeStageDefs/LifeStages.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<LifeStageDef ParentName="EntityFullyFormed">
    <defName>FullyFormed_Toughspike</defName>
    <bodyDrawOffset>(0, 0, 0.25)</bodyDrawOffset>
  </LifeStageDef>

  
```

> 来自 `Anomaly/Defs/LifeStageDefs/LifeStages.xml`，defName = `FullyFormed_Toughspike`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：EntityFullyFormed / FullyFormed_Toughspike / MetalhorrorJuvenile
```

## 三、全量字段表（54 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `adjective` | 5.3% (1/19) | 文本 | teenage |
| `alwaysDowned` | 5.3% (1/19) | 布尔 | true |
| `attachPointScaleFactor` | 10.5% (2/19) | 数值 | .5 / .7 |
| `bodyDrawOffset` | 15.8% (3/19) | 文本 | (0, 0, -0.03) / (0, 0, -0.1) / (0, 0, 0.25) |
| `bodySizeFactor` | 63.2% (12/19) | 数值 | 0.5 / 0.58 / 0.8 |
| `bodyWidth` | 10.5% (2/19) | 数值 | 0.95 / 1.125 |
| `canDoRandomMentalBreaks` | 5.3% (1/19) | 布尔 | false |
| `canInitiateSocialInteraction` | 5.3% (1/19) | 布尔 | false |
| `canSleepWhenStarving` | 5.3% (1/19) | 布尔 | false |
| `canSleepWhileHeld` | 5.3% (1/19) | 布尔 | true |
| `canVoluntarilySleep` | 5.3% (1/19) | 布尔 | false |
| `caravanRideable` | 5.3% (1/19) | 布尔 | true |
| `claimable` | 5.3% (1/19) | 布尔 | true |
| `customMoodTipString` | 5.3% (1/19) | 文本 | Mood represents how happy or stressed someone is. Babies with low mood are more  |
| `defName` | 94.7% (18/19) | 文本 | EntityFullyFormed / FullyFormed_Toughspike / MetalhorrorJuvenile |
| `developmentalStage` | 10.5% (2/19) | 文本 | Baby / Child |
| `equipmentDrawDistanceFactor` | 10.5% (2/19) | 数值 | 0.55 / 0.65 |
| `eyeSizeFactor` | 10.5% (2/19) | 数值 | 0.7 / 0.85 |
| `fallAsleepMaxThresholdOverride` | 5.3% (1/19) | 数值 | .60 |
| `foodMaxFactor` | 47.4% (9/19) | 数值 | 0.625 / 1.25 / 1.552 |
| `hairStyleFilter` | 5.3% (1/19) | 容器 |  |
| `hairStyleFilter/tags` | 5.3% (1/19) | 容器 |  |
| `hairStyleFilter/tags/li` | 5.3% (1/19) | 文本 | Balding |
| `hairStyleFilter/whitelist` | 5.3% (1/19) | 布尔 | false |
| `headSizeFactor` | 10.5% (2/19) | 数值 | 0.5 / 0.75 |
| `healthScaleFactor` | 52.6% (10/19) | 数值 | 0.2 / 0.5 / 0.7 |
| `hungerRateFactor` | 36.8% (7/19) | 数值 | 0.125 / 0.4 / 0.8 |
| `involuntarySleepIsNegativeEvent` | 5.3% (1/19) | 布尔 | false |
| `involuntarySleepMTBDaysFromRest` | 5.3% (1/19) | 容器 |  |
| `involuntarySleepMTBDaysFromRest/points` | 5.3% (1/19) | 容器 |  |
| `involuntarySleepMTBDaysFromRest/points/li` | 31.6% (6/19) | 文本 | (.00, 0) / (.01, .01) / (.15, .166) |
| `label` | 84.2% (16/19) | 文本 | fully-formed / juvenile / larva |
| `marketValueFactor` | 36.8% (7/19) | 数值 | 0.4 / 0.5 / 0.9 |
| `meleeDamageFactor` | 52.6% (10/19) | 数值 | 0.4 / 0.5 / 0.725 |
| `milkable` | 10.5% (2/19) | 布尔 | true |
| `naturalWakeThresholdOverride` | 5.3% (1/19) | 数值 | 1.0 |
| `reproductive` | 15.8% (3/19) | 布尔 | true |
| `shearable` | 5.3% (1/19) | 布尔 | true |
| `silhouetteGraphicData` | 21.1% (4/19) | 容器 |  |
| `silhouetteGraphicData/drawSize` | 21.1% (4/19) | 数值 | 1 |
| `silhouetteGraphicData/graphicClass` | 21.1% (4/19) | 文本 | Graphic_Single |
| `silhouetteGraphicData/texPath` | 21.1% (4/19) | 文本 | Things/Pawn/Humanlike/Silhouettes/Silhouette_HumanAdult / Things/Pawn/Humanlike/Silhouettes/Silhouette_HumanBa |
| `sittingOffset` | 15.8% (3/19) | 数值 | 0.18 / 0.23 / 0.3 |
| `statFactors` | 42.1% (8/19) | 容器 |  |
| `statFactors/MoveSpeed` | 42.1% (8/19) | 数值 | 0.2 / 0.75 / 0.85 |
| `statOffsets` | 5.3% (1/19) | 容器 |  |
| `statOffsets/ComfyTemperatureMax` | 5.3% (1/19) | 数值 | 4 |
| `statOffsets/ComfyTemperatureMin` | 5.3% (1/19) | 数值 | -46 |
| `thinkTreeConstantOverride` | 5.3% (1/19) | 文本 | HumanlikeBabyConstant |
| `thinkTreeMainOverride` | 5.3% (1/19) | 文本 | HumanlikeBaby |
| `visible` | 26.3% (5/19) | 布尔 | false |
| `voxPitch` | 31.6% (6/19) | 数值 | 1.2 / 1.6 |
| `voxVolume` | 10.5% (2/19) | 数值 | 0.4 / 0.8 |
| `workerClass` | 15.8% (3/19) | 文本 | LifeStageWorker_HumanlikeAdult / LifeStageWorker_HumanlikeChild |

## 四、原版 defName 一览（共 19 个，列出前 60）

```text
`FullyFormed_Toughspike`          `EntityFullyFormed`               `MetalhorrorMature`               `MechanoidFullyFormed`          
`AnimalBabyTiny`                  ``                                `EusocialInsectAdult`             `MetalhorrorLarva`              
`MetalhorrorJuvenile`             `AnimalAdult`                     `HumanlikeAdult`                  `HumanlikePreTeenager`          
`EusocialInsectJuvenile`          `AnimalJuvenile`                  `EusocialInsectLarva`             `AnimalBaby`                    
`HumanlikeTeenager`               `HumanlikeChild`                  `HumanlikeBaby`                 
```
