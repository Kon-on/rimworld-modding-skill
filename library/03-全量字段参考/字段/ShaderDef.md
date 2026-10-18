# ShaderDef

- **所属线**：表现线
- **原版实例数**：194
- **字段路径数**：28
- **资料片**：Core
- **原版出处**：`Core/Defs/ShaderDefs/Shaders.World.xml`、`Core/Defs/ShaderDefs/Shaders.Map.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<ShaderDef>
    <defName>UngeneratedPlanetParts</defName>
    <shaderProgram>
      <fragmentShaderFileName>UngeneratedPlanetParts.frag.glsl</fragmentShaderFileName>
      <useTexture>false</useTexture>
    </shaderProgram>
  </ShaderDef>

  
```

> 来自 `Core/Defs/ShaderDefs/Shaders.World.xml`，defName = `UngeneratedPlanetParts`，XML 节点数 5（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Cutout / TerrainFade / TerrainHard
shaderProgram                                  [容器]
shaderProgram/fragmentShaderFileName           [文本]  例：Cutout.frag.glsl / TerrainFade.frag.glsl / TerrainHard.frag.glsl
shaderProgram/renderQueue                      [数值/文本]  例：2000 / 2001 / 2900
```

## 三、全量字段表（28 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (194/194) | 文本 | Cutout / TerrainFade / TerrainHard |
| `shaderProgram` | 100.0% (194/194) | 容器 |  |
| `shaderProgram/blendDstFactor` | 1.6% (3/194) | 文本 | One / OneMinusSrcColor / SrcColor |
| `shaderProgram/blendMode` | 27.3% (53/194) | 文本 | Additive / Custom / MultiplyDestination |
| `shaderProgram/blendSrcFactor` | 1.6% (3/194) | 文本 | DstColor / OneMinusDstColor / SrcAlpha |
| `shaderProgram/colorWrite` | 3.6% (7/194) | 布尔 | false |
| `shaderProgram/cullMode` | 6.7% (13/194) | 文本 | None |
| `shaderProgram/depthTest` | 10.3% (20/194) | 布尔 | false / true |
| `shaderProgram/depthWrite` | 89.7% (174/194) | 布尔 | false / true |
| `shaderProgram/flipTextureST` | 55.7% (108/194) | 布尔 | false |
| `shaderProgram/fragmentShaderFileName` | 100.0% (194/194) | 文本 | Cutout.frag.glsl / TerrainFade.frag.glsl / TerrainHard.frag.glsl |
| `shaderProgram/renderQueue` | 94.8% (184/194) | 数值/文本 | 2000 / 2001 / 2900 |
| `shaderProgram/sceneGrab` | 10.3% (20/194) | 容器 |  |
| `shaderProgram/sceneGrab/name` | 10.3% (20/194) | 文本 | Darkness / Distortion / DistortionBackground |
| `shaderProgram/sceneGrab/queue` | 10.3% (20/194) | 数值 | 3151 / 3152 / 3178 |
| `shaderProgram/stencilCompare` | 13.4% (26/194) | 文本 | Always / Equal / Greater |
| `shaderProgram/stencilEnabled` | 13.4% (26/194) | 布尔 | true |
| `shaderProgram/stencilPassOp` | 7.7% (15/194) | 文本 | Replace |
| `shaderProgram/stencilReadMask` | 6.7% (13/194) | 数值 | 128 / 17 / 2 |
| `shaderProgram/stencilRef` | 13.4% (26/194) | 数值 | 0 / 12 / 128 |
| `shaderProgram/stencilWriteMask` | 7.7% (15/194) | 数值 | 12 / 128 / 17 |
| `shaderProgram/textureWrapOverrides` | 46.4% (90/194) | 容器 |  |
| `shaderProgram/textureWrapOverrides/li` | 84.0% (163/194) | 容器 |  |
| `shaderProgram/textureWrapOverrides/li/key` | 84.0% (163/194) | 文本 | _AlphaAddTex / _DetailTex / _MainTex |
| `shaderProgram/textureWrapOverrides/li/value` | 84.0% (163/194) | 文本 | Clamp / Mirror / Repeat |
| `shaderProgram/transparent` | 64.4% (125/194) | 布尔 | true |
| `shaderProgram/useTexture` | 11.9% (23/194) | 布尔 | false |
| `shaderProgram/vertexShaderFileName` | 51.5% (100/194) | 文本 | MapWorldUV.vert.glsl / PlantWindSway.vert.glsl / TerrainWater.vert.glsl |

## 四、原版 defName 一览（共 194 个，列出前 60）

```text
`UngeneratedPlanetParts`          `WorldOverlayTransparentLit`      `CutoutOverlay`                   `CutoutComplexBlend`            
`WorldOverlayCutout`              `Cutout`                          `CutoutComplex`                   `MotePulse`                     
`MoteGlowPulse`                   `MoteGlowPulseLow`                `MoteGlowMasked`                  `MotePawnBodyColor`             
`MotePawnBodyGlow`                `MoteGradientScan`                `MoteHateChantShadow`             `Edgedetect`                    
`Silhouette`                      `CutoutSkin`                      `CutoutHair`                      `CutoutSkinOverride`            
`CutoutSkinOverlay`               `CutoutWithOverlay`               `CutoutFlying`                    `CutoutFlying01`                
`BuildingWorking`                 `HighlightRing`                   `TransparentColoredMask`          `WorldOverlayAdditive`          
`WorldVertexColor`                `CutoutPlant`                     `EdgeShadow`                      `Mote`                          
`MoteGlow`                        `MoteGlowPulseLink`               `MoteGlowParentRotation`          `MoteSoftScannerGlow`           
`MoteSubcoreEncoder`              `TransparentPostLight`            `WoundSkin`                       `VertexColor`                   
`SolidColor`                      `SolidColorBehind`                `TransparentPlant`                `BioferriteHarvester`           
`CaveExitRope`                    `CutoutAnimated`                  `FerroWave`                       `TransparentColorLerp`          
`TransparentShaking`              `WorldOverlayAdditiveTwoSided`    `WorldOverlayTransparent`         `PlanetGlow`                    
`CutoutComplexUI`                 `GrayscaleGUI`                    `OrbitalDebris`                   `VacuumOverlay`                 
`GravshipBlit`                    `PsychicRitualCandleMote`         `MoteWater`                       `AdditiveChangeHue`             
```

_余下 134 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
