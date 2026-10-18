# FleckDef

- **所属线**：表现线
- **原版实例数**：327
- **字段路径数**：115
- **资料片**：Anomaly、Biotech、Core、Ideology、Odyssey、Royalty
- **原版出处**：`Core/Defs/Effects/Fleck_Visual.xml`、`Ideology/Defs/Effects/Fleck_Visual.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<FleckDef ParentName="FleckBase" Name="FleckBase_Thrown" Abstract="True">
    <fleckSystemClass>FleckSystemThrown</fleckSystemClass>
  </FleckDef>

  
```

> 来自 `Core/Defs/Effects/Fleck_Visual.xml`，defName = ``，XML 节点数 2（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
altitudeLayer                                  [文本]  例：LowPlant / MoteLow / MoteOverhead
defName                                        [文本]  例：FleckShamblerDecay / MeatExplosionSplatter / MeatExplosionSplatterTerrain
fadeOutTime                                    [数值]  例：0 / 0.65 / 1
scalers/li/curve/points/li                     [文本]  例：(0,0) / (0.04,0.2381762) / (0.08,0.4249946)
solidTime                                      [数值]  例：1 / 3 / 4
```

## 三、全量字段表（115 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `acceleration` | 4.3% (14/327) | 文本 | (0, 0, 0) / (0, 0, 2) / (0, 0, 6) |
| `altitudeLayer` | 91.7% (300/327) | 文本 | LowPlant / MoteLow / MoteOverhead |
| `altitudeLayerIncOffset` | 1.5% (5/327) | 数值 | -0.5 / -1.5 / 13 |
| `archCurve` | 2.8% (9/327) | 容器 |  |
| `archCurve/points` | 2.8% (9/327) | 容器 |  |
| `archCurve/points/li` | 71.6% (234/327) | 文本 | (0,1) / (0.04,0.9756736) / (0.08,0.9500062) |
| `archDuration` | 3.1% (10/327) | 数值/文本 | .5 / .55 / .9~1.5 |
| `archHeight` | 3.4% (11/327) | 数值/文本 | .25 / .75 / 12~16 |
| `attachedToHead` | 0.6% (2/327) | 布尔 | True |
| `defName` | 96.6% (316/327) | 文本 | FleckShamblerDecay / MeatExplosionSplatter / MeatExplosionSplatterTerrain |
| `drawOffscreen` | 0.9% (3/327) | 布尔 | true |
| `fadeInTime` | 78.9% (258/327) | 数值 | .25 / 0.04 / 0.1 |
| `fadeOutTime` | 91.7% (300/327) | 数值 | 0 / 0.65 / 1 |
| `fleckSystemClass` | 9.2% (30/327) | 文本 | FleckSystemSplash / FleckSystemStatic / FleckSystemThrown |
| `graphicData` | 87.5% (286/327) | 容器 |  |
| `graphicData/borderMipMaps` | 0.3% (1/327) | 布尔 | true |
| `graphicData/color` | 21.1% (69/327) | 文本 | (0, 0, 0, 1) / (0, 0, 0, 150) / (1, 1, 1, .1) |
| `graphicData/drawOffset` | 0.9% (3/327) | 文本 | (0, 0, 0.1) / (0,0,4.0) / (0.0, 0, 0.65) |
| `graphicData/drawSize` | 47.4% (155/327) | 数值/文本 | (6, 6) / 1 / 1.0 |
| `graphicData/graphicClass` | 36.1% (118/327) | 文本 | Graphic_Fleck / Graphic_FleckPulse / Graphic_FleckSplash |
| `graphicData/renderInstanced` | 20.8% (68/327) | 布尔 | false / true |
| `graphicData/renderQueue` | 1.2% (4/327) | 数值 | 3181 / 3200 / 4000 |
| `graphicData/shaderParameters` | 34.9% (114/327) | 容器 |  |
| `graphicData/shaderParameters/_AgeOffset` | 0.6% (2/327) | 数值 | 0.07 |
| `graphicData/shaderParameters/_ageToNoiseRatio` | 2.5% (8/327) | 数值 | 0 / 10 / 2 |
| `graphicData/shaderParameters/_AlphaClip` | 0.3% (1/327) | 数值 | .9 |
| `graphicData/shaderParameters/_Amplitude` | 0.3% (1/327) | 文本 | (0.03, 0.0, 0.02, 0) |
| `graphicData/shaderParameters/_bounceAmplitude` | 1.2% (4/327) | 数值 | -0.23 / .03 / 0.05 |
| `graphicData/shaderParameters/_bounceSpeed` | 1.2% (4/327) | 数值 | .1 / 0.1 / 0.15 |
| `graphicData/shaderParameters/_BounceTex` | 1.2% (4/327) | 文本 | /Things/Mote/DeathRefusalBounceHeight / /Things/Mote/RitualEffects/BounceHeight / /Things/Mote/RitualEffects/S |
| `graphicData/shaderParameters/_brightnessMultiplier` | 10.1% (33/327) | 数值 | -20 / 0.0 / 1.15 |
| `graphicData/shaderParameters/_Clip` | 0.6% (2/327) | 数值 | 0 |
| `graphicData/shaderParameters/_Color` | 3.1% (10/327) | 文本 | (0, 0, 0, 0) / (0, 0, 0, 1.0) / (1, .2, .2, .2) |
| `graphicData/shaderParameters/_Color2` | 7.3% (24/327) | 文本 | (0, 0, 0, .5) / (0, 0, 0, 1) / (1, 1, 1, 0.5) |
| `graphicData/shaderParameters/_ColorLerp` | 0.6% (2/327) | 文本 | /Things/Mote/AcidSplashColorLerp / /Things/Mote/IncineratorSmokeColorLerp |
| `graphicData/shaderParameters/_dayColor` | 0.3% (1/327) | 文本 | (1, .73, .56, .8) |
| `graphicData/shaderParameters/_DissolveTex` | 0.3% (1/327) | 文本 | /Things/Mote/DownUpDissolveNoise |
| `graphicData/shaderParameters/_DistortionIntensity` | 3.1% (10/327) | 数值 | 0.01 / 0.5 / 1 |
| `graphicData/shaderParameters/_distortionIntensity` | 9.8% (32/327) | 数值 | .5 / 0.1 / 0.12 |
| `graphicData/shaderParameters/_distortionScale` | 0.3% (1/327) | 数值 | 0.1 |
| `graphicData/shaderParameters/_distortionScrollSpeed` | 0.9% (3/327) | 文本 | (0.15, 0.15, 0) / (0.2, 0.0, 0.0) |
| `graphicData/shaderParameters/_DistortionSpeed` | 0.3% (1/327) | 数值 | 0.6 |
| `graphicData/shaderParameters/_DistortionTex` | 10.7% (35/327) | 文本 | /Things/Mote/MoteHellfireCannon_HeatWaveDistortion / /Things/Mote/PsychicDistortionCurrents / /Things/Mote/Psy |
| `graphicData/shaderParameters/_Duration` | 0.6% (2/327) | 数值 | .2 / 1 |
| `graphicData/shaderParameters/_DustTex1` | 0.3% (1/327) | 文本 | /Things/Mote/LightshaftNoise |
| `graphicData/shaderParameters/_ExtraTex` | 0.3% (1/327) | 文本 | /Things/Mote/Sparks_Radial_B |
| `graphicData/shaderParameters/_FadeTex` | 0.6% (2/327) | 文本 | /Things/Mote/PollutionWave |
| `graphicData/shaderParameters/_FramesPerSec` | 1.8% (6/327) | 数值 | 16 / 4 / 5 |
| `graphicData/shaderParameters/_InnerFadeAmount` | 2.8% (9/327) | 数值 | 0 |
| `graphicData/shaderParameters/_innerRingSize` | 0.6% (2/327) | 数值 | 0.55 / 0.65 |
| `graphicData/shaderParameters/_Intensity` | 4.3% (14/327) | 数值 | 0.5 / 1 / 13 |
| `graphicData/shaderParameters/_Interval` | 3.7% (12/327) | 数值 | .04 / 0.04 / 0.05 |
| `graphicData/shaderParameters/_inTime` | 1.2% (4/327) | 数值 | 0.0 / 0.2 |
| `graphicData/shaderParameters/_Loop` | 0.3% (1/327) | 数值 | 0 |
| `graphicData/shaderParameters/_MaskTex` | 0.6% (2/327) | 文本 | /Things/Building/AncientHeatVentM / /Things/Mote/HeatVentDistortionMask |
| `graphicData/shaderParameters/_MultiplyTex` | 1.2% (4/327) | 文本 | /Things/Mote/RadiationDistortion_A |
| `graphicData/shaderParameters/_nightColor` | 0.3% (1/327) | 文本 | (.37, .8, .89, .8) |
| `graphicData/shaderParameters/_Noise` | 0.6% (2/327) | 文本 | /Things/Mote/SkipFlashNoise |
| `graphicData/shaderParameters/_NoiseIntensity` | 1.8% (6/327) | 数值 | 10 / 100 |
| `graphicData/shaderParameters/_noiseIntensity` | 2.5% (8/327) | 数值 | 1 / 10 / 6 |
| `graphicData/shaderParameters/_NoiseScale` | 0.3% (1/327) | 数值 | 10 |
| `graphicData/shaderParameters/_NoiseTex` | 7.3% (24/327) | 文本 | /Things/Mote/PsycastNoise |
| `graphicData/shaderParameters/_NumFrames` | 1.8% (6/327) | 数值 | 4 / 5 / 8 |
| `graphicData/shaderParameters/_outerRingSize` | 0.3% (1/327) | 数值 | 1.0 |
| `graphicData/shaderParameters/_outTime` | 0.9% (3/327) | 数值 | 0.1 |
| `graphicData/shaderParameters/_PulseMax` | 0.3% (1/327) | 数值 | 1 |
| `graphicData/shaderParameters/_PulseMin` | 0.3% (1/327) | 数值 | .8 |
| `graphicData/shaderParameters/_RampTime` | 0.3% (1/327) | 数值 | 0 |
| `graphicData/shaderParameters/_rotationAmplitude` | 0.6% (2/327) | 数值 | 0.2 |
| `graphicData/shaderParameters/_RotationFromOffset` | 0.6% (2/327) | 数值 | -4 / 4 |
| `graphicData/shaderParameters/_rotationSpeed` | 0.6% (2/327) | 数值 | 0.3 |
| `graphicData/shaderParameters/_RotationTex` | 0.6% (2/327) | 文本 | /Things/Mote/RitualEffects/RotationSlightlyIrregular |
| `graphicData/shaderParameters/_solidTime` | 0.9% (3/327) | 数值 | 0.2 |
| `graphicData/shaderParameters/_Speed` | 0.3% (1/327) | 数值 | 5 |
| `graphicData/shaderParameters/_SwimFrequency` | 0.3% (1/327) | 数值 | 5.0 |
| `graphicData/shaderParameters/_SwimSpeed` | 0.3% (1/327) | 数值 | 0.4 |
| `graphicData/shaderParameters/_texAScale` | 3.4% (11/327) | 数值 | 0.4 / 0.5 |
| `graphicData/shaderParameters/_TexAScaleDivisorPerProgress` | 2.8% (9/327) | 数值 | 0 / 1.5 |
| `graphicData/shaderParameters/_texAScrollSpeed` | 3.7% (12/327) | 数值 | -0.15 / -0.75 / 0 |
| `graphicData/shaderParameters/_texBScale` | 4.0% (13/327) | 数值 | 0.2 / 0.5 / 2 |
| `graphicData/shaderParameters/_texBScrollSpeed` | 4.3% (14/327) | 数值 | -.4 / -0.4 / -0.5 |
| `graphicData/shaderParameters/_texScale` | 0.3% (1/327) | 数值 | 0.2 |
| `graphicData/shaderParameters/_UnmaskedContribution` | 0.3% (1/327) | 数值 | 0.7 |
| `graphicData/shaderType` | 59.6% (195/327) | 文本 | DarkHighlightRing / MoteLargeDistortionWave / MoteMultiplyAddCircular |
| `graphicData/texPath` | 83.2% (272/327) | 文本 | Things/Mote/Black / Things/Mote/HoraxianGeo / Things/Mote/HoraxianLineGlow |
| `growthRate` | 44.6% (146/327) | 数值 | -.16 / -3 / .08 |
| `landSound` | 0.6% (2/327) | 文本 | HorseshoeImpact / StoneImpact |
| `randomGraphics` | 11.3% (37/327) | 容器 |  |
| `randomGraphics/li` | 38.5% (126/327) | 容器 |  |
| `randomGraphics/li/color` | 15.6% (51/327) | 文本 | (120, 27, 17, 170) / (171, 27, 17, 170) / (23, 27, 17, 170) |
| `randomGraphics/li/drawSize` | 32.1% (105/327) | 数值/文本 | (1.5, 1.5) / 0.4 / 0.8 |
| `randomGraphics/li/graphicClass` | 38.5% (126/327) | 文本 | Graphic_Fleck / Graphic_FleckPulse |
| `randomGraphics/li/renderInstanced` | 7.6% (25/327) | 布尔 | false / true |
| `randomGraphics/li/shaderParameters` | 4.6% (15/327) | 容器 |  |
| `randomGraphics/li/shaderParameters/_Color` | 0.9% (3/327) | 文本 | (1, .8, .9, 1) |
| `randomGraphics/li/shaderParameters/_FlameTex` | 0.9% (3/327) | 文本 | /Things/Mote/Candles/CandleFlame |
| `randomGraphics/li/shaderParameters/_Interval` | 1.8% (6/327) | 数值 | 0.02 / 1 |
| `randomGraphics/li/shaderType` | 38.5% (126/327) | 文本 | Mote / MoteGlowPulse / PsychicRitualCandleMote |
| `randomGraphics/li/texPath` | 38.5% (126/327) | 文本 | Things/Mote/ShamblerDecayParticles/ShamblerDecayParticlesG / Things/Mote/ShamblerDecayParticles/ShamblerDecayP |
| `realTime` | 0.6% (2/327) | 布尔 | true |
| `rotateTowardsMoveDirection` | 3.1% (10/327) | 布尔 | true |
| `rotateTowardsMoveDirectionExtraAngle` | 0.9% (3/327) | 数值 | -90 |
| `scalers` | 5.5% (18/327) | 容器 |  |
| `scalers/li` | 5.8% (19/327) | 容器 |  |
| `scalers/li/axisMask` | 2.1% (7/327) | 文本 | (0, 0, 1) / (0, 1, 1) / (1, 0, 0) |
| `scalers/li/curve` | 5.8% (19/327) | 容器 |  |
| `scalers/li/curve/points` | 5.8% (19/327) | 容器 |  |
| `scalers/li/curve/points/li` | 151.1% (494/327) | 文本 | (0,0) / (0.04,0.2381762) / (0.08,0.4249946) |
| `scalers/li/scaleAmt` | 5.8% (19/327) | 数值/文本 | .8~1 / 1 / 1~4 |
| `scalers/li/scaleTime` | 5.8% (19/327) | 数值/文本 | .2~6 / 2 / 2~6 |
| `scalingAnchor` | 0.6% (2/327) | 文本 | (.5, .2, 0) / (.5, 0, 0) |
| `solidTime` | 92.3% (302/327) | 数值 | 1 / 3 / 4 |
| `speedPerTime` | 4.0% (13/327) | 数值/文本 | -20 / -6~10 / .01~.1 |
| `unattachedDrawOffset` | 1.5% (5/327) | 文本 | (0, 0, 0) / (0, 0, 8) / (0, 0.2, 0) |
| `useAttachLink` | 4.6% (15/327) | 布尔 | True / true |

## 四、原版 defName 一览（共 327 个，列出前 60）

```text
``                                ``                                ``                                `BandNodeRedPulse`              
`BandNodeGreenPulse`              `BandNodeYellowPulse`             `Fleck_WastePackDissolutionCell_Performant`  `FeedbackGoto`                  
`FeedbackShoot`                   `FeedbackMelee`                   `FeedbackEquip`                   `FeedbackExtinguish`            
``                                `GauranlenDebrisA`                `GauranlenDebrisB`                `GauranlenDebrisC`              
`FishShadowReverse`               `FlashstormAreaEffect`            `BulletShieldAreaEffect`          `MicroSparksFast`               
``                                `PsycastSkipOuterRingEntry`       `PsycastSkipOuterRingExit`        ``                              
`PsycastSkipInnerEntry`           ``                                ``                                `AtomizerFlash`                 
``                                `Heart`                           `HealingCross`                    `SleepZ`                        
`IncapIcon`                       `Horseshoe`                       `Stone`                           `ExplosionFlash`                
`ShotFlash`                       `SparkFlash`                      `YellowSparkFlash`                `BloodSplash`                   
`BodyImpact`                      `PlainFlash`                      `PsycastSkipInnerExit`            `ShotHit_Dirt`                  
`SandInEyes`                      `Music`                           `BlastExtinguisher`               `JumpSmoke`                     
`Flash`                           `PreachHealth`                    `FlashHollow`                     `BloodFeedSplash`               
`AtomizerFlashGrowing`            `Meditating`                      `SleepZ_Small`                    `SleepZ_Tiny`                   
`Footprint`                       `AirPuff`                         `DustPuff`                        `DustPuffThick`                 
```

_余下 267 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
