# GameConditionDef

- **所属线**：世界线
- **原版实例数**：38
- **字段路径数**：37
- **资料片**：Anomaly、Biotech、Core、Odyssey、Royalty
- **原版出处**：`Core/Defs/GameConditionDefs/GameConditions_Misc.xml`、`Odyssey/Defs/GameConditionDefs/GameConditions_Misc.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<GameConditionDef>
    <defName>Planetkiller</defName>
    <conditionClass>GameCondition_Planetkiller</conditionClass>
    <label>planetkiller</label>
    <description>An interstellar planetkiller weapon is approaching this planet. It will smash the planet apart like a rifle bullet hitting an egg, annihilating all life.</description>
  </GameConditionDef>
  
  
```

> 来自 `Core/Defs/GameConditionDefs/GameConditions_Misc.xml`，defName = `Planetkiller`，XML 节点数 5（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
conditionClass                                 [文本]  例：GameCondition_DeathPall / GameCondition_GrayPall / GameCondition_HateChantDrone
defName                                        [文本]  例：DeathPall / GrayPall / HateChantDrone
description                                    [文本]  例：A putrid stench fills the air, making people unhappy. The smell is worse outside / Cultists of Horax are performing a psychically tuned chant. The ominous chanting / The dead will rise! Burn, bury, destroy, or move corpses indoors to prevent them
label                                          [文本]  例：death pall resurrection / gray pall stench / hate chanting
```

## 三、全量字段表（37 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `allowUnderground` | 42.1% (16/38) | 布尔 | false |
| `canAffectAllPlanetLayers` | 10.5% (4/38) | 布尔 | true |
| `canBePermanent` | 84.2% (32/38) | 布尔 | false / true |
| `causesTraderCaravanExit` | 2.6% (1/38) | 布尔 | true |
| `conditionClass` | 100.0% (38/38) | 文本 | GameCondition_DeathPall / GameCondition_GrayPall / GameCondition_HateChantDrone |
| `defaultDroneLevel` | 5.3% (2/38) | 文本 | BadMedium / GoodMedium |
| `defName` | 100.0% (38/38) | 文本 | DeathPall / GrayPall / HateChantDrone |
| `description` | 100.0% (38/38) | 文本 | A putrid stench fills the air, making people unhappy. The smell is worse outside / Cultists of Horax are perfo |
| `descriptionFuture` | 23.7% (9/38) | 文本 | a [psychicDroneLevel] psychic drone will buzz the area around [map_definite] for / a cloud of toxic fallout wi |
| `displayOnUI` | 7.9% (3/38) | 布尔 | false |
| `endMessage` | 52.6% (20/38) | 文本 | The acidic smog is lifting. / The blood rain is ending. / The eclipse is ending. |
| `exclusiveConditions` | 15.8% (6/38) | 容器 |  |
| `exclusiveConditions/li` | 18.4% (7/38) | 文本 | ColdSnap / PsychicDrone / PsychicSoothe |
| `fishPopulationOffsetPerDay` | 2.6% (1/38) | 数值 | -0.15 |
| `jumpToSourceKey` | 2.6% (1/38) | 文本 | ClickToJumpToFlashstorm |
| `label` | 100.0% (38/38) | 文本 | death pall resurrection / gray pall stench / hate chanting |
| `letterDef` | 50.0% (19/38) | 文本 | NegativeEvent / NeutralEvent / PositiveEvent |
| `letterHyperlinks` | 2.6% (1/38) | 容器 |  |
| `letterHyperlinks/li` | 5.3% (2/38) | 文本 | Cooler / PassiveCooler |
| `letterText` | 68.4% (26/38) | 文本 | A blanket of gritty fog has descended on this area. It smells somehow ancient an / A death-gray cloud has desc |
| `minNearbyPollution` | 2.6% (1/38) | 数值 | 0.05 |
| `mtbOverNearbyPollutionCurve` | 2.6% (1/38) | 容器 |  |
| `mtbOverNearbyPollutionCurve/points` | 2.6% (1/38) | 容器 |  |
| `mtbOverNearbyPollutionCurve/points/li` | 15.8% (6/38) | 文本 | (0.05, 240) / (1, 180) / (10, 60) |
| `natural` | 36.8% (14/38) | 布尔 | false |
| `pennedAnimalsSeekShelter` | 7.9% (3/38) | 布尔 | true |
| `preventIncidents` | 2.6% (1/38) | 布尔 | true |
| `preventNeutralVisitors` | 7.9% (3/38) | 布尔 | true |
| `preventRain` | 7.9% (3/38) | 布尔 | true |
| `preventShuttleLaunch` | 2.6% (1/38) | 布尔 | true |
| `requireFish` | 2.6% (1/38) | 布尔 | true |
| `showPermanentInTooltip` | 2.6% (1/38) | 布尔 | false |
| `silencedByConditions` | 13.2% (5/38) | 容器 |  |
| `silencedByConditions/li` | 13.2% (5/38) | 文本 | ToxicFallout / UnnaturalDarkness |
| `spreadsFilth` | 2.6% (1/38) | 文本 | Filth_VolcanicAsh |
| `startMessage` | 2.6% (1/38) | 文本 | Acidic smog has begun due to pollution in this region of the world. |
| `weatherDef` | 13.2% (5/38) | 文本 | BloodRain / GrayPall / UnnaturalDarkness_Stage1 |

## 四、原版 defName 一览（共 38 个，列出前 60）

```text
`Planetkiller`                    `HateChantDrone`                  `UnnaturalHeat`                   `DarkenedSkies`                 
`WindyGameCondition`              `HeatVentHeat`                    `ClimateCycle`                    `VolcanicDebris`                
`PsychicDroner`                   `LavaFlow`                        `DeepFreeze`                      `GiantSmokeCloud`               
`ToxicSpewer`                     `GillRot`                         `SunBlocker`                      `ClimateAdjustment`             
`GrayPall`                        `DeathPall`                       `VolcanicWinter`                  `Drought`                       
`PsychicSuppression`              `EMIField`                        `ToxicFallout`                    `ColdSnap`                      
`Flashstorm`                      `VolcanicAsh`                     `BioluminescentSpores`            `DroughtInitial`                
`UnnaturalDarkness`               `BloodRain`                       `SolarFlare`                      `Eclipse`                       
`Aurora`                          `WeatherController`               `PsychicSoothe`                   `PsychicDrone`                  
`HeatWave`                        `NoxiousHaze`                   
```
