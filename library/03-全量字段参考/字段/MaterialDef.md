# MaterialDef

- **所属线**：表现线
- **原版实例数**：81
- **字段路径数**：21
- **资料片**：Core
- **原版出处**：`Core/Defs/MaterialDefs/Materials.Generated.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<MaterialDef>
    <defName>EdgeShadow</defName>
    <resourcePath>Lighting/EdgeShadow</resourcePath>
    <shader>EdgeShadow</shader>
  </MaterialDef>

  
```

> 来自 `Core/Defs/MaterialDefs/Materials.Generated.xml`，defName = `EdgeShadow`，XML 节点数 4（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
colors/li                                      [容器]
colors/li/name                                 [文本]  例：_BackgroundColor / _Color / _Color2
colors/li/value                                [文本]  例：(0.482, 0.603, 0.682, 0) / (0.8, 0.8, 0.8, 0) / (0.85725003, 0.85725003, 0.85725003, 1)
defName                                        [文本]  例：EdgeShadow / LightOverlay / LightOverlayGravship
resourcePath                                   [文本]  例：Lighting/EdgeShadow / Lighting/LightOverlay / Lighting/LightOverlayGravship
shader                                         [文本]  例：EdgeShadow / LightOverlay / SunShadow
textures/li                                    [容器]
textures/li/name                               [文本]  例：_MainTex / _MaskTex / _NoiseTex
textures/li/path                               [文本]  例：Other/Perlin / Other/TerrainCurtainMask / Things/Mote/BrightFlash
```

## 三、全量字段表（21 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `colors` | 65.4% (53/81) | 容器 |  |
| `colors/li` | 145.7% (118/81) | 容器 |  |
| `colors/li/name` | 145.7% (118/81) | 文本 | _BackgroundColor / _Color / _Color2 |
| `colors/li/value` | 145.7% (118/81) | 文本 | (0.482, 0.603, 0.682, 0) / (0.8, 0.8, 0.8, 0) / (0.85725003, 0.85725003, 0.85725003, 1) |
| `defName` | 100.0% (81/81) | 文本 | EdgeShadow / LightOverlay / LightOverlayGravship |
| `floats` | 23.5% (19/81) | 容器 |  |
| `floats/li` | 65.4% (53/81) | 容器 |  |
| `floats/li/name` | 65.4% (53/81) | 文本 | _FlickerSpeed / _MaxOpacity / _MinBrightness |
| `floats/li/value` | 65.4% (53/81) | 数值 | 0.1 / 0.75 / 1 |
| `keywords` | 1.2% (1/81) | 容器 |  |
| `keywords/li` | 1.2% (1/81) | 文本 | UNITY_UI_ALPHACLIP |
| `renderQueue` | 14.8% (12/81) | 数值 | 3170 / 3171 / 3181 |
| `resourcePath` | 100.0% (81/81) | 文本 | Lighting/EdgeShadow / Lighting/LightOverlay / Lighting/LightOverlayGravship |
| `shader` | 100.0% (81/81) | 文本 | EdgeShadow / LightOverlay / SunShadow |
| `textures` | 61.7% (50/81) | 容器 |  |
| `textures/li` | 114.8% (93/81) | 容器 |  |
| `textures/li/alphaFromGrayscale` | 22.2% (18/81) | 布尔 | true |
| `textures/li/name` | 114.8% (93/81) | 文本 | _MainTex / _MaskTex / _NoiseTex |
| `textures/li/offset` | 53.1% (43/81) | 文本 | (-153.051, 153.051) / (-267.83926, -267.83926) / (0.5, 0.5) |
| `textures/li/path` | 114.8% (93/81) | 文本 | Other/Perlin / Other/TerrainCurtainMask / Things/Mote/BrightFlash |
| `textures/li/scale` | 63.0% (51/81) | 文本 | (0.25, 0.35) / (0.25, 0.375) / (0.5, 0.5) |

## 四、原版 defName 一览（共 81 个，列出前 60）

```text
`EdgeShadow`                      `Gravship`                        `GravshipBlit`                    `GravshipChromaKey`             
`GravshipMask`                    `FilledMask`                      `IndoorMask`                      `RoofedOutdoorMask`             
`ShadowMask`                      `Clouds`                          `PlanetGlow`                      `Rivers`                        
`Roads`                           `Sun`                             `WorldVertexColor`                `GravshipMaskTerrainCurtain`    
`IndoorMaskGravship`              `IndoorMaskTerrainCurtain`        `WorldVertexColorTransparent`     `GrayscaleGUI`                  
`LightOverlay`                    `SunShadow`                       `SunShadowFade`                   `Stars`                         
`WorldIce`                        `WorldTerrain`                    `DebugOverlay`                    `LightOverlayGravship`          
`GravshipOpaqueBase`              `Darkness`                        `RiversBorder`                    `UngeneratedPlanetParts`        
`WorldOcean`                      `GravshipDistortion`              `Warning`                         `DiagonalStripes`               
`FieldEdge`                       `LightningBolt`                   `Sand`                            `Snow`                          
`FakeTerrain`                     `VacuumWarning`                   `FogOfWar`                        `HateChantOverlayWorld`         
`GravEngineGlow`                  `GravshipDownwash`                `DarknessOverlayWorld`            `SnowOverlayWorld`              
`GravshipShadow`                  `VacuumOverlay`                   `VacuumOverlayDesaturated`        `RainOverlayWorld`              
`ToxRainOverlayWorld`             `BloodRainOverlayWorld`           `DeathpallAshesOverlayWorld`      `FogOverlayWorld`               
`GraypallAshesOverlayWorld`       `NoxiousHazeOverlayWorld`         `VacuumOverlayTransition`         `BlindFogOverlayWorld`          
```

_余下 21 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
