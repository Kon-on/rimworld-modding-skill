# TerrainDef

- **所属线**：世界线
- **原版实例数**：137
- **字段路径数**：160
- **资料片**：Anomaly、Core、Ideology、Odyssey、Royalty
- **原版出处**：`Ideology/Defs/TerrainDefs/Terrain_Floors.xml`、`Odyssey/Defs/TerrainDefs/Terrain_Temporary.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<TerrainDef ParentName="Carpet_Mindbend">
    <defName>Carpet_MindbendA</defName>
    <label>diamond mindbend carpet</label>
    <texturePath>Terrain/Surfaces/MindbendCarpet/MindbendCarpet_a</texturePath>
  </TerrainDef>

  
```

> 来自 `Ideology/Defs/TerrainDefs/Terrain_Floors.xml`，defName = `Carpet_MindbendA`，XML 节点数 4（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

_该类型没有出现率≥90% 的字段（字段高度自由）。_

## 三、全量字段表（160 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `affordances` | 29.2% (40/137) | 容器 |  |
| `affordances/li` | 86.9% (119/137) | 文本 | Diggable / Heavy / Light |
| `autoRebuildable` | 0.7% (1/137) | 布尔 | true |
| `avoidWander` | 5.1% (7/137) | 布尔 | false / true |
| `bridge` | 0.7% (1/137) | 布尔 | true |
| `bridgePropsPath` | 2.2% (3/137) | 文本 | Terrain/Misc/AncientWoodBridgeProps / Terrain/Misc/BridgeProps / Terrain/Misc/HeavyBridgeProps |
| `burnDamage` | 0.7% (1/137) | 数值 | 3 |
| `burnedDef` | 3.6% (5/137) | 文本 | BurnedBioferritePlate / BurnedCarpet / BurnedStrawMatting |
| `burnIntervalTicks` | 0.7% (1/137) | 数值 | 120 |
| `canBePolluted` | 0.7% (1/137) | 布尔 | false |
| `canEverTerraform` | 2.2% (3/137) | 布尔 | false |
| `canFreeze` | 5.8% (8/137) | 布尔 | false / true |
| `canGenerateDefaultDesignator` | 4.4% (6/137) | 布尔 | false |
| `categoryType` | 10.9% (15/137) | 文本 | Misc / Sand / Soil |
| `changeable` | 0.7% (1/137) | 布尔 | false |
| `color` | 38.7% (53/137) | 文本 | (0.369, 0.369, 0.369) / (100, 80, 80) / (108,78,55) |
| `constructEffect` | 5.8% (8/137) | 文本 | ConstructDirt / ConstructMetal / ConstructWood |
| `constructionSkillPrerequisite` | 7.3% (10/137) | 数值 | 3 / 6 |
| `costList` | 38.0% (52/137) | 容器 |  |
| `costList/Bioferrite` | 0.7% (1/137) | 数值 | 4 |
| `costList/BlocksGranite` | 4.4% (6/137) | 数值 | 20 / 4 |
| `costList/BlocksLimestone` | 4.4% (6/137) | 数值 | 20 / 4 |
| `costList/BlocksMarble` | 4.4% (6/137) | 数值 | 20 / 4 |
| `costList/BlocksSandstone` | 4.4% (6/137) | 数值 | 20 / 4 |
| `costList/BlocksSlate` | 4.4% (6/137) | 数值 | 20 / 4 |
| `costList/BlocksVacstone` | 4.4% (6/137) | 数值 | 20 / 4 |
| `costList/Cloth` | 0.7% (1/137) | 数值 | 35 |
| `costList/Gold` | 0.7% (1/137) | 数值 | 70 |
| `costList/GravlitePanel` | 0.7% (1/137) | 数值 | 1 |
| `costList/Hay` | 0.7% (1/137) | 数值 | 2 |
| `costList/Silver` | 1.5% (2/137) | 数值 | 12 / 70 |
| `costList/Steel` | 5.8% (8/137) | 数值 | 1 / 2 / 3 |
| `costList/WoodLog` | 2.2% (3/137) | 数值 | 12 / 20 / 3 |
| `cropIcon` | 0.7% (1/137) | 布尔 | false |
| `customShader` | 1.5% (2/137) | 文本 | ShallowLava |
| `customShaderParameters` | 1.5% (2/137) | 容器 |  |
| `customShaderParameters/_BrightSpotScale` | 0.7% (1/137) | 数值 | 1.5 |
| `customShaderParameters/_BrightSpotSpeed` | 0.7% (1/137) | 数值 | 0.02 |
| `customShaderParameters/_LavaBrightness` | 0.7% (1/137) | 数值 | 0.2 |
| `customShaderParameters/_MaskTex` | 1.5% (2/137) | 文本 | /Terrain/Surfaces/DeepLavaMask / /Terrain/Surfaces/ShallowLavaMask |
| `customShaderParameters/_NoiseTex` | 1.5% (2/137) | 文本 | /Other/Perlin |
| `dangerous` | 0.7% (1/137) | 布尔 | true |
| `defName` | 83.2% (114/137) | 文本 | BioferritePlate / BurnedBioferritePlate / Flesh |
| `description` | 24.1% (33/137) | 文本 | A dense mat of organic flesh that clings loosely to the ground. / Burned-out bioferrite plating. / Heavy plate |
| `designationCategory` | 10.2% (14/137) | 容器/文本 | Floors / Odyssey / Structure |
| `designationHotKey` | 8.8% (12/137) | 文本 | Misc6 / Misc7 / Misc8 |
| `designatorDropdown` | 5.8% (8/137) | 文本 | Floor_Flagstone / Floor_Morbid_Stone / Floor_Tile |
| `destroyBuildingsOnDestroyed` | 0.7% (1/137) | 布尔 | true |
| `destroyEffect` | 0.7% (1/137) | 文本 | Bridge_Collapse |
| `destroyEffectWater` | 0.7% (1/137) | 文本 | Bridge_CollapseWater |
| `destroyOnBombDamageThreshold` | 1.5% (2/137) | 数值 | 35 / 45 |
| `dominantStyleCategory` | 4.4% (6/137) | 文本 | Morbid / Spikecore / Techist |
| `dontRender` | 0.7% (1/137) | 布尔 | true |
| `drawStyleCategory` | 2.2% (3/137) | 文本 | FilledRectangle / Floors / Foundations |
| `driesTo` | 9.5% (13/137) | 容器/文本 | Gravel / Sand / Soil |
| `edgeType` | 27.0% (37/137) | 文本 | FadeRough / Hard / Water |
| `exposesToVacuum` | 0.7% (1/137) | 布尔 | true |
| `extinguishesFire` | 1.5% (2/137) | 布尔 | true |
| `extraDeteriorationFactor` | 1.5% (2/137) | 数值 | 3 / 600 |
| `extraDraftedPerceivedPathCost` | 0.7% (1/137) | 数值 | 18 |
| `extraNonDraftedPerceivedPathCost` | 0.7% (1/137) | 数值 | 180 |
| `fertility` | 25.6% (35/137) | 数值 | 0 / 1 / 1.0 |
| `filthAcceptanceMask` | 5.1% (7/137) | 容器 |  |
| `filthAcceptanceMask/li` | 5.1% (7/137) | 文本 | None / Unnatural |
| `fleckData` | 0.7% (1/137) | 容器 |  |
| `fleckData/fleck` | 0.7% (1/137) | 文本 | AirPuff |
| `fleckData/rotationSpeedRange` | 0.7% (1/137) | 文本 | -50~50 |
| `fleckData/scaleRange` | 0.7% (1/137) | 文本 | 1.5~3 |
| `fleckData/solidTicksRange` | 0.7% (1/137) | 文本 | 1~3 |
| `fleckData/velocityAngleRange` | 0.7% (1/137) | 文本 | -90~90 |
| `fleckData/velocitySpeedRange` | 0.7% (1/137) | 文本 | 0.01~0.5 |
| `floodTerrain` | 6.6% (9/137) | 文本 | MarshFlood / ShallowFloodwater / SpringFlood |
| `forcePassableByFlyingPawns` | 0.7% (1/137) | 布尔 | true |
| `generatedFilth` | 13.1% (18/137) | 文本 | Filth_Dirt / Filth_Sand / Filth_Slime |
| `glowColor` | 0.7% (1/137) | 文本 | (214,94,4,0) |
| `glowRadius` | 0.7% (1/137) | 数值 | 3 |
| `gravshipReplacementTerrain` | 2.2% (3/137) | 文本 | VolcanicRock / WaterOceanShallow / WaterShallow |
| `heatPerTick` | 1.5% (2/137) | 数值 | 0.01 / 0.25 |
| `holdSnowOrSand` | 2.2% (3/137) | 布尔 | false |
| `ignitePawnsIntervalTicks` | 0.7% (1/137) | 数值 | 240 |
| `igniteRadius` | 0.7% (1/137) | 数值 | 1.9 |
| `isFoundation` | 1.5% (2/137) | 布尔 | true |
| `isPaintable` | 11.7% (16/137) | 布尔 | true |
| `label` | 83.2% (114/137) | 文本 | bioferrite plate / burned bioferrite plate / flesh |
| `layerable` | 5.8% (8/137) | 布尔 | false / true |
| `meltSnowRadius` | 1.5% (2/137) | 数值 | 4 |
| `natural` | 2.9% (4/137) | 布尔 | true |
| `passability` | 2.2% (3/137) | 文本 | Impassable |
| `pathCost` | 24.8% (34/137) | 数值 | 1 / 14 / 2 |
| `placeWorkers` | 1.5% (2/137) | 容器 |  |
| `placeWorkers/li` | 2.2% (3/137) | 文本 | PlaceWorker_BuildingsValidOverSubstructure / PlaceWorker_InSubstructureFootprint / Placeworker_OnlyUnderThickR |
| `pollutedTexturePath` | 19.7% (27/137) | 文本 | Terrain/Surfaces/MossyPolluted / Terrain/Surfaces/SoilPolluted / Terrain/Surfaces/SoilRichPolluted |
| `pollutionCloudColor` | 0.7% (1/137) | 文本 | (1, 1, 1, 0.66) |
| `pollutionColor` | 10.2% (14/137) | 文本 | (1, 1, 1, 0.15) / (1, 1, 1, 0.43) / (1, 1, 1, 0.8) |
| `pollutionOverlayScale` | 3.6% (5/137) | 文本 | (0.66, 0.66) / (0.75, 0.75) / (0.8, 0.8) |
| `pollutionOverlayScrollSpeed` | 0.7% (1/137) | 数值 | 0.007 |
| `pollutionOverlayTexturePath` | 13.1% (18/137) | 容器/文本 | Terrain/Surfaces/PollutionFloorSmooth / Terrain/Surfaces/PollutionMarsh / Terrain/Surfaces/PollutionMossy |
| `pollutionShaderType` | 8.8% (12/137) | 文本 | TerrainFadeRoughLinearAdd / TerrainFadeRoughLinearBurn / TerrainFadeRoughSoftLight |
| `pollutionTintColor` | 2.9% (4/137) | 文本 | (0.95, 0.95, 0.93, 1) / (1, 1, 1, 1) / (1,1,1,1) |
| `preventCraters` | 3.6% (5/137) | 布尔 | true |
| `renderPrecedence` | 50.4% (69/137) | 数值 | 240 / 251 / 340 |
| `requireInspectedGravEngine` | 0.7% (1/137) | 布尔 | true |
| `researchPrerequisites` | 7.3% (10/137) | 容器 |  |
| `researchPrerequisites/li` | 7.3% (10/137) | 文本 | BioferriteShaping / Smithing / SterileMaterials |
| `resourcesFractionWhenDeconstructed` | 3.6% (5/137) | 数值 | 0 / 1 |
| `scatterType` | 9.5% (13/137) | 文本 | Rocky / SoftDry / SoftGray |
| `smoothedTerrain` | 0.7% (1/137) | 文本 | VolcanicRock_Smooth |
| `spaceBridgePropsPath` | 0.7% (1/137) | 文本 | Terrain/Misc/BridgeSpaceProps |
| `spaceEdgeGraphicData` | 3.6% (5/137) | 容器 |  |
| `spaceEdgeGraphicData/CornerInnerTexPath` | 2.2% (3/137) | 文本 | Terrain/Surfaces/Asteroid/BorderInside/AsteroidBorderInside_CornerInner / Terrain/Surfaces/MechanoidPlatform/B |
| `spaceEdgeGraphicData/CornerOuterTexPath` | 2.2% (3/137) | 文本 | Terrain/Surfaces/Asteroid/BorderInside/AsteroidBorderInside_CornerOuter / Terrain/Surfaces/MechanoidPlatform/B |
| `spaceEdgeGraphicData/FlatTexPath` | 2.2% (3/137) | 文本 | Terrain/Surfaces/Asteroid/BorderInside/AsteroidBorderInside_Flat / Terrain/Surfaces/MechanoidPlatform/BorderIn |
| `spaceEdgeGraphicData/LoopLeftTexPath` | 2.2% (3/137) | 文本 | Terrain/Surfaces/Asteroid/AsteroidEdge_Left / Terrain/Surfaces/MechanoidPlatform/MechanoidPlatformEdge_Left /  |
| `spaceEdgeGraphicData/LoopRightTexPath` | 2.2% (3/137) | 文本 | Terrain/Surfaces/Asteroid/AsteroidEdge_Right / Terrain/Surfaces/MechanoidPlatform/MechanoidPlatformEdge_Right  |
| `spaceEdgeGraphicData/LoopSingleTexPath` | 2.2% (3/137) | 文本 | Terrain/Surfaces/Asteroid/AsteroidEdge_Single / Terrain/Surfaces/MechanoidPlatform/MechanoidPlatformEdge_Singl |
| `spaceEdgeGraphicData/LoopTexPaths` | 2.2% (3/137) | 容器 |  |
| `spaceEdgeGraphicData/LoopTexPaths/li` | 10.9% (15/137) | 文本 | Terrain/Surfaces/Asteroid/Loop/AsteroidEdge_Loop1 / Terrain/Surfaces/Asteroid/Loop/AsteroidEdge_Loop2 / Terrai |
| `spaceEdgeGraphicData/OShapeTexPath` | 2.2% (3/137) | 文本 | Terrain/Surfaces/Asteroid/BorderInside/AsteroidBorderInside_OShape / Terrain/Surfaces/MechanoidPlatform/Border |
| `spaceEdgeGraphicData/overrideColor` | 0.7% (1/137) | 文本 | (0.27, 0.22, 0.18, 1) |
| `spaceEdgeGraphicData/UShapeTexPath` | 2.2% (3/137) | 文本 | Terrain/Surfaces/Asteroid/BorderInside/AsteroidBorderInside_UShape / Terrain/Surfaces/MechanoidPlatform/Border |
| `statBases` | 40.2% (55/137) | 容器 |  |
| `statBases/Beauty` | 32.9% (45/137) | 数值 | -1 / -10 / -2 |
| `statBases/BeautyOutdoors` | 10.2% (14/137) | 数值 | -5 / 0 |
| `statBases/CleaningTimeFactor` | 15.3% (21/137) | 数值 | 0.6 / 0.8 / 1.5 |
| `statBases/Cleanliness` | 20.4% (28/137) | 数值 | -0.1 / -3 / 0.2 |
| `statBases/ContainmentStrength` | 0.7% (1/137) | 数值 | 15 |
| `statBases/FilthMultiplier` | 0.7% (1/137) | 数值 | 0.05 |
| `statBases/Flammability` | 8.0% (11/137) | 数值 | 0.15 / 0.22 / 0.32 |
| `statBases/MarketValue` | 3.6% (5/137) | 数值 | 0 / 5 |
| `statBases/StyleDominance` | 3.6% (5/137) | 数值 | 1 |
| `statBases/WorkToBuild` | 16.1% (22/137) | 数值 | 100 / 120 / 300 |
| `supportsRock` | 0.7% (1/137) | 布尔 | false |
| `tags` | 29.9% (41/137) | 容器 |  |
| `tags/li` | 32.1% (44/137) | 文本 | FineFloor / Floor / Road |
| `takeFootprints` | 10.9% (15/137) | 布尔 | True / true |
| `takeSplashes` | 0.7% (1/137) | 布尔 | true |
| `temporary` | 4.4% (6/137) | 布尔 | true |
| `tempTerrain` | 1.5% (2/137) | 容器 |  |
| `tempTerrain/destroysFloors` | 0.7% (1/137) | 布尔 | true |
| `tempTerrain/removedByExplosions` | 0.7% (1/137) | 布尔 | true |
| `tempTerrain/replaceableByBridge` | 0.7% (1/137) | 布尔 | true |
| `tempTerrain/terrainOnRemoved` | 0.7% (1/137) | 文本 | CooledLava |
| `terrainAffordanceNeeded` | 2.2% (3/137) | 文本 | Bridgeable / Heavy / Walkable |
| `texturePath` | 52.5% (72/137) | 文本 | Terrain/Surfaces/BioferritePlateFloor / Terrain/Surfaces/BurnedBioferritePlateFloor / Terrain/Surfaces/Flesh |
| `throwFleckChance` | 0.7% (1/137) | 数值 | 0.25 |
| `tools` | 8.8% (12/137) | 容器 |  |
| `tools/li` | 8.8% (12/137) | 容器 |  |
| `tools/li/capacities` | 8.8% (12/137) | 容器 |  |
| `tools/li/capacities/li` | 8.8% (12/137) | 文本 | KickMaterialInEyes |
| `tools/li/cooldownTime` | 8.8% (12/137) | 数值 | 1.5 |
| `tools/li/hediff` | 8.8% (12/137) | 文本 | DirtInEyes / GravelInEyes / MudInEyes |
| `tools/li/label` | 8.8% (12/137) | 文本 | dirt / gravel / mud |
| `toxicBuildupFactor` | 2.2% (3/137) | 数值 | 3 |
| `traversedThought` | 3.6% (5/137) | 文本 | HotSpring / SoakingWet / ToxWater |
| `uiIconPath` | 1.5% (2/137) | 文本 | Terrain/Misc/HeavyBridge_MenuIcon / Terrain/Surfaces/Bridge_MenuIcon |
| `uiOrder` | 9.5% (13/137) | 数值 | 2010 / 2020 / 2030 |
| `waterBodyType` | 7.3% (10/137) | 文本 | Freshwater / Other / Saltwater |
| `waterDepthShader` | 5.8% (8/137) | 文本 | Map/WaterDepth |
| `waterDepthShaderParameters` | 2.9% (4/137) | 容器 |  |
| `waterDepthShaderParameters/_UseWaterOffset` | 2.9% (4/137) | 数值 | 1 |

## 四、原版 defName 一览（共 137 个，列出前 60）

```text
`Carpet_MindbendA`                `Carpet_MindbendB`                `Carpet_MindbendC`                `Carpet_MindbendD`              
`Carpet_MindbendE`                `ToxicWaterDeep`                  ``                                ``                              
``                                `ToxicWaterShallow`               `TileSandstone`                   `TileGranite`                   
`TileLimestone`                   `TileSlate`                       `TileMarble`                      `FlagstoneSandstone`            
`FlagstoneGranite`                `FlagstoneLimestone`              `FlagstoneSlate`                  `FlagstoneMarble`               
``                                `Tile_MorbidSandstone`            `Tile_MorbidGranite`              `Tile_MorbidLimestone`          
`Tile_MorbidSlate`                `Tile_MorbidMarble`               `Tile_MorbidVacstone`             `Tile_SpikecoreSandstone`       
`Tile_SpikecoreGranite`           `Tile_SpikecoreLimestone`         `Tile_SpikecoreSlate`             `Tile_SpikecoreMarble`          
`Tile_SpikecoreVacstone`          `Tile_TotemicSandstone`           `Tile_TotemicGranite`             `Tile_TotemicLimestone`         
`Tile_TotemicMarble`              `Tile_TotemicVacstone`            `TileVacstone`                    `FlagstoneVacstone`             
`ToxicWaterOceanDeep`             `FineTileSandstone`               `FineTileGranite`                 `FineTileLimestone`             
`FineTileSlate`                   `FineTileMarble`                  `FineTileVacstone`                `BurnedWoodPlankFloor`          
`BurnedCarpet`                    `BurnedStrawMatting`              `Underwall`                       `WaterDeep`                     
`Tile_TotemicSlate`               `Carpet_Mindbend`                 `ToxicWaterOceanShallow`          `BurnedBioferritePlate`         
``                                ``                                `WaterOceanDeep`                  ``                              
```

_余下 77 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
