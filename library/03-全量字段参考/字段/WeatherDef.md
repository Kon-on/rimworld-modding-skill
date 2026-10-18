# WeatherDef

- **所属线**：世界线
- **原版实例数**：25
- **字段路径数**：61
- **资料片**：Anomaly、Core、Odyssey
- **原版出处**：`Anomaly/Defs/WeatherDefs/Weathers.xml`、`Odyssey/Defs/WeatherDefs/Weathers.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<WeatherDef ParentName="UnnaturalDarknessBase">
    <defName>UnnaturalDarkness_Stage1</defName>
    <description>A psychic phenomenon affecting your colonists. The sky is cracking and dissolving, immersing the world in an unnatural darkness. This darkness will deepen and become dangerous over time.</description>
    <ambientSounds>
      <li>Ambient_UnnaturalDarkness_Phase1</li>
    </ambientSounds>
  </WeatherDef>

  
```

> 来自 `Anomaly/Defs/WeatherDefs/Weathers.xml`，defName = `UnnaturalDarkness_Stage1`，XML 节点数 5（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
ambientSounds/li                               [文本]  例：Ambient_Rain / Ambient_UnnaturalDarkness_Phase1 / Ambient_UnnaturalDarkness_Phase2
commonalityRainfallFactor/points/li            [文本]  例：(0, 0) / (1300, 1) / (4000, 2.0)
defName                                        [文本]  例：BloodRain / Undercave / UnnaturalDarkness_Stage1
label                                          [文本]  例：blood rain / metal hell / undercave
```

## 三、全量字段表（61 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `accuracyMultiplier` | 56.0% (14/25) | 数值 | 0.5 / 0.7 / 0.75 |
| `ambientSounds` | 84.0% (21/25) | 容器 |  |
| `ambientSounds/li` | 96.0% (24/25) | 文本 | Ambient_Rain / Ambient_UnnaturalDarkness_Phase1 / Ambient_UnnaturalDarkness_Phase2 |
| `canOccurAsRandomForcedEvent` | 16.0% (4/25) | 布尔 | false |
| `canOccurInAmbientHorror` | 4.0% (1/25) | 布尔 | true |
| `commonalityRainfallFactor` | 48.0% (12/25) | 容器 |  |
| `commonalityRainfallFactor/points` | 48.0% (12/25) | 容器 |  |
| `commonalityRainfallFactor/points/li` | 124.0% (31/25) | 文本 | (0, 0) / (1300, 1) / (4000, 2.0) |
| `defName` | 96.0% (24/25) | 文本 | BloodRain / Undercave / UnnaturalDarkness_Stage1 |
| `description` | 88.0% (22/25) | 文本 | A death-gray cloud of black dust has descended on this area. The smell is ancien / A psychic phenomenon affect |
| `doToxicBuildup` | 4.0% (1/25) | 布尔 | true |
| `durationRange` | 12.0% (3/25) | 文本 | 15000~40000 / 30000~90000 |
| `eventMakers` | 8.0% (2/25) | 容器 |  |
| `eventMakers/li` | 16.0% (4/25) | 容器 |  |
| `eventMakers/li/averageInterval` | 16.0% (4/25) | 数值 | 1200 |
| `eventMakers/li/eventClass` | 16.0% (4/25) | 文本 | WeatherEvent_LightningFlash / WeatherEvent_LightningStrike |
| `favorability` | 80.0% (20/25) | 文本 | Bad / Good / Neutral |
| `isBad` | 40.0% (10/25) | 布尔 | false / true |
| `label` | 92.0% (23/25) | 文本 | blood rain / metal hell / undercave |
| `letterDef` | 12.0% (3/25) | 文本 | ThreatSmall |
| `letterLabel` | 12.0% (3/25) | 文本 | Blind fog / Torrential rain / Tox rain |
| `letterText` | 12.0% (3/25) | 文本 | A thick fog is setting in, dramatically reducing vision. Ranged weapons will be  / Heavy rain is beginning to  |
| `maxGlow` | 4.0% (1/25) | 数值 | 0.95 |
| `maxRangeCap` | 4.0% (1/25) | 数值 | 22.9 |
| `minMonolithLevel` | 4.0% (1/25) | 数值 | 1 |
| `moveSpeedMultiplier` | 40.0% (10/25) | 数值 | 0.7 / 0.8 / 0.9 |
| `overlayClasses` | 56.0% (14/25) | 容器 |  |
| `overlayClasses/li` | 72.0% (18/25) | 文本 | WeatherOverlay_BloodFog / WeatherOverlay_BloodRain / WeatherOverlay_DeathpallFog |
| `perceivePriority` | 84.0% (21/25) | 数值 | 0 / 1 / 2 |
| `preventSkygaze` | 4.0% (1/25) | 布尔 | true |
| `preventsShuttleLaunch` | 12.0% (3/25) | 布尔 | true |
| `rainRate` | 36.0% (9/25) | 数值 | 1 |
| `repeatable` | 16.0% (4/25) | 布尔 | true |
| `sandRate` | 4.0% (1/25) | 数值 | 1.6 |
| `skyColorsDay` | 88.0% (22/25) | 容器 |  |
| `skyColorsDay/overlay` | 88.0% (22/25) | 文本 | (0.25,0.2,0.2) / (0.5, 0.5, 0.5) / (0.6, 0.6, 0.6) |
| `skyColorsDay/saturation` | 88.0% (22/25) | 数值 | 0.5 / 0.75 / 0.9 |
| `skyColorsDay/shadow` | 88.0% (22/25) | 文本 | (0.718,0.745,0.757) / (0.85, 0.85, 0.85) / (0.92,0.92,0.92) |
| `skyColorsDay/sky` | 88.0% (22/25) | 文本 | (0.4, 0.5, 0.5) / (0.482, 0.603, 0.682) / (0.482,0.603,0.682) |
| `skyColorsDusk` | 88.0% (22/25) | 容器 |  |
| `skyColorsDusk/overlay` | 88.0% (22/25) | 文本 | (0.25,0.2,0.2) / (0.5, 0.5, 0.5) / (0.6, 0.6, 0.6) |
| `skyColorsDusk/saturation` | 88.0% (22/25) | 数值 | 0.5 / 0.75 / 0.9 |
| `skyColorsDusk/shadow` | 88.0% (22/25) | 文本 | (0.85, 0.85, 0.85) / (0.92,0.92,0.92) / (0.955,0.886,0.914) |
| `skyColorsDusk/sky` | 88.0% (22/25) | 文本 | (0.4, 0.5, 0.5) / (0.482, 0.603, 0.682) / (0.482,0.603,0.682) |
| `skyColorsNightEdge` | 88.0% (22/25) | 容器 |  |
| `skyColorsNightEdge/overlay` | 88.0% (22/25) | 文本 | (0.15,0.1,0.1) / (0.5, 0.5, 0.5) / (0.6, 0.6, 0.6) |
| `skyColorsNightEdge/saturation` | 88.0% (22/25) | 数值 | 0.5 / 0.75 / 0.9 |
| `skyColorsNightEdge/shadow` | 88.0% (22/25) | 文本 | (0.85, 0.85, 0.85) / (0.92,0.92,0.92) / (1,1,1) |
| `skyColorsNightEdge/sky` | 88.0% (22/25) | 文本 | (0.35,0.40,0.45) / (0.4, 0.5, 0.5) / (0.482, 0.603, 0.682) |
| `skyColorsNightMid` | 88.0% (22/25) | 容器 |  |
| `skyColorsNightMid/overlay` | 88.0% (22/25) | 文本 | (0.15,0.1,0.1) / (0.5, 0.5, 0.5) / (0.6, 0.6, 0.6) |
| `skyColorsNightMid/saturation` | 88.0% (22/25) | 数值 | 0.5 / 0.75 / 0.9 |
| `skyColorsNightMid/shadow` | 88.0% (22/25) | 文本 | (0.85, 0.85, 0.85) / (0.92,0.92,0.92) / (1,1,1) |
| `skyColorsNightMid/sky` | 88.0% (22/25) | 文本 | (0.35,0.40,0.45) / (0.4, 0.5, 0.5) / (0.482, 0.603, 0.682) |
| `snowRate` | 12.0% (3/25) | 数值 | 0.8 / 1.2 / 1.5 |
| `temperatureRange` | 40.0% (10/25) | 文本 | -999~-0.5 / 0~100 / 0~999 |
| `transitionTicksOverride` | 8.0% (2/25) | 数值 | 600 |
| `weatherThought` | 36.0% (9/25) | 文本 | DeathPall / GrayPall / SoakingWet |
| `windSpeedFactor` | 60.0% (15/25) | 数值 | 0.5 / 1.5 |
| `windSpeedOffset` | 20.0% (5/25) | 数值 | 1.25 / 1.5 |
| `workerClass` | 4.0% (1/25) | 文本 | WeatherWorker_TorrentialRain |

## 四、原版 defName 一览（共 25 个，列出前 60）

```text
`UnnaturalDarkness_Stage1`        `UnnaturalDarkness_Stage2`        `Undercave`                       `MetalHell`                     
``                                `Underground`                     `Orbit`                           `Overcast`                      
`Clear`                           `Windy`                           `Fog`                             `BloodRain`                     
`Sandstorm`                       `SnowGentle`                      `UnnaturalFog`                    `Rain`                          
`DryThunderstorm`                 `SnowHard`                        `GrayPall`                        `BlindFog`                      
`FoggyRain`                       `Blizzard`                        `ToxRain`                         `TorrentialRain`                
`RainyThunderstorm`             
```
