# ShaderTypeDef

- **所属线**：表现线
- **原版实例数**：122
- **字段路径数**：3
- **资料片**：Anomaly、Biotech、Core、Ideology、Odyssey、Royalty
- **原版出处**：`Anomaly/Defs/Misc/ShaderTypeDefs/ShaderTypes.xml`、`Core/Defs/Misc/ShaderTypeDefs/ShaderTypes.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<ShaderTypeDef>
    <defName>MoteHateChant</defName>
    <shaderPath>Map/MoteHateChant</shaderPath>
  </ShaderTypeDef>
  
```

> 来自 `Anomaly/Defs/Misc/ShaderTypeDefs/ShaderTypes.xml`，defName = `MoteHateChant`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Ember / MoteHateChant / MoteHateChantShadow
shaderPath                                     [文本]  例：Map/Ember / Map/MoteHateChant / Map/MoteHateChantShadow
```

## 三、全量字段表（3 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (122/122) | 文本 | Ember / MoteHateChant / MoteHateChantShadow |
| `shaderPath` | 100.0% (122/122) | 文本 | Map/Ember / Map/MoteHateChant / Map/MoteHateChantShadow |
| `uiShaderPath` | 0.8% (1/122) | 文本 | Map/CutoutComplexUI |

## 四、原版 defName 一览（共 122 个，列出前 60）

```text
`MoteHateChant`                   `MoteHateChantShadow`             `VoidNodeParallax`                `Ember`                         
`EmberGlow`                       `TransparentColorLerp`            `TransparentAnimatedColorLerp`    `BuildingSquashNStretch`        
`RevenantDeath`                   `Metalblood`                      `MoteMultiplyCircular`            `HoraxianSnake`                 
`BioferriteHarvester`             `MoteHeatDistortion`              `FerroBlob`                       `FerroWave`                     
`BuildingWorking`                 `GroundFog`                       `VoidNodeDistortion`              `MoteObeliskExplosionPulse`     
`EndlessPit`                      `MoteMechGestatorGlow`            `MotePollutionPump`               `MoteSoftScannerGlow`           
`MoteSubcoreEncoder`              `MoteGlowParentRotation`          `MotePawnBodyColor`               `MotePawnBodyGlow`              
`PollutionCloud`                  `TerrainWaterPolluted`            `TerrainFadeRoughLinearBurn`      `MoteGradientScan`              
`RitualSmokeNoMask`               `TransparentShaking`              `TransparentColoredMask`          `MoteGlowCircularScrollingDistortion`
`MoteApocritonPulse`              `Cutout`                          `CutoutHair`                      `CutoutWithOverlay`             
`CutoutTiling`                    `CutoutFlying`                    `CutoutFlying01`                  `CutoutPlant`                   
`CutoutComplexUI`                 `ExpandingIcon`                   `CutoutComplexBlend`              `CutoutSkin`                    
`CutoutSkinOverlay`               `Transparent`                     `TransparentPostLight`            `TransparentPlant`              
`MetaOverlay`                     `Mote`                            `MoteGlow`                        `MoteGlowDistorted`             
`MoteDistorted`                   `MoteGlowDistortBackground`       `MoteGlowPulseLink`               `MotePulse`                     
```

_余下 62 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
