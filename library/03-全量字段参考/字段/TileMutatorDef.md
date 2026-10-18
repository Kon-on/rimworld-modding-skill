# TileMutatorDef

- **所属线**：世界线
- **原版实例数**：95
- **字段路径数**：247
- **资料片**：Core、Odyssey
- **原版出处**：`Odyssey/Defs/TileMutators/TileMutators_ManMade.xml`、`Odyssey/Defs/TileMutators/TileMutators_Natural.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<TileMutatorDef ParentName="AbandonedColonyMutatorBase">
    <defName>AbandonedColonyTribal</defName>
    <workerClass>TileMutatorWorker_AbandonedColonyTribal</workerClass>
  </TileMutatorDef>

  
```

> 来自 `Odyssey/Defs/TileMutators/TileMutators_ManMade.xml`，defName = `AbandonedColonyTribal`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
biomeWhitelist/li                              [文本]  例：AridShrubland / BorealForest / ColdBog
defName                                        [文本]  例：Caves / Coast / Mountain
```

## 三、全量字段表（247 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `additionalGameConditions` | 1.1% (1/95) | 容器 |  |
| `additionalGameConditions/li` | 1.1% (1/95) | 文本 | WindyGameCondition |
| `additionalWildPlants` | 1.1% (1/95) | 容器 |  |
| `additionalWildPlants/Plant_Grass` | 1.1% (1/95) | 数值 | 6 |
| `additionalWildPlants/Plant_GrayGrass` | 1.1% (1/95) | 数值 | 5 |
| `additionalWildPlants/Plant_RatPalm` | 1.1% (1/95) | 数值 | 4 |
| `additionalWildPlants/Plant_Reeds` | 1.1% (1/95) | 数值 | 1 |
| `additionalWildPlants/Plant_TreePalm` | 1.1% (1/95) | 数值 | 5 |
| `allowRoofedEdgeWalkIn` | 1.1% (1/95) | 布尔 | true |
| `animalDensityFactor` | 2.1% (2/95) | 数值 | 0.5 / 1.5 |
| `animalDensityRange` | 2.1% (2/95) | 文本 | 0.3~4 / 0.3~7 |
| `averageTemperatureRange` | 2.1% (2/95) | 文本 | -100~0 / 20~60 |
| `biomeBlacklist` | 13.7% (13/95) | 容器 |  |
| `biomeBlacklist/li` | 26.3% (25/95) | 文本 | GlacialPlain / IceSheet / Scarlands |
| `biomeWhitelist` | 39.0% (37/95) | 容器 |  |
| `biomeWhitelist/li` | 254.7% (242/95) | 文本 | AridShrubland / BorealForest / ColdBog |
| `blacklistedRaidStrategies` | 1.1% (1/95) | 容器 |  |
| `blacklistedRaidStrategies/li` | 1.1% (1/95) | 文本 | Siege |
| `canSpawnOnLandmark` | 2.1% (2/95) | 布尔 | false |
| `canSpawnOnRiver` | 13.7% (13/95) | 布尔 | false |
| `canSpawnOnRoad` | 7.4% (7/95) | 布尔 | false |
| `categories` | 54.7% (52/95) | 容器 |  |
| `categories/li` | 61.1% (58/95) | 文本 | BaseCaves / Caves / Coast |
| `chanceOnNonLandmarkTile` | 23.2% (22/95) | 数值 | 0 / 0.01 / 0.02 |
| `chunkDensityFactor` | 1.1% (1/95) | 数值 | 0.15 |
| `coastSidesRange` | 14.7% (14/95) | 文本 | 0~0 / 1~5 / 2~5 |
| `defName` | 91.6% (87/95) | 文本 | Caves / Coast / Mountain |
| `description` | 85.3% (81/95) | 文本 | A mountain fills one side of this tile. / A stream of fresh water flows through here. / Small cave networks ca |
| `displayPriority` | 1.1% (1/95) | 数值 | -50 |
| `extraGenSteps` | 2.1% (2/95) | 容器 |  |
| `extraGenSteps/li` | 7.4% (7/95) | 文本 | AncientDrillPlatform / AncientExcavator / AncientExplosivesCrate |
| `fishPopulationFactor` | 2.1% (2/95) | 数值 | 0.35 / 1.5 |
| `genOrder` | 26.3% (25/95) | 数值 | -100 / -200 / 100 |
| `geyserCountFactor` | 3.2% (3/95) | 数值 | 0 / 2 |
| `hillinessForElevationGen` | 2.1% (2/95) | 文本 | Flat |
| `hillinessForOreGeneration` | 3.2% (3/95) | 文本 | LargeHills / Mountainous |
| `hillinessLabel` | 3.2% (3/95) | 文本 | LargeHills / Mountainous |
| `junkDensityFactor` | 3.2% (3/95) | 数值 | 0 / 15 |
| `label` | 87.4% (83/95) | 文本 | caves / coast / mountain |
| `maxHilliness` | 7.4% (7/95) | 文本 | Flat / SmallHills |
| `minHilliness` | 10.5% (10/95) | 文本 | Mountainous |
| `overrideCategories` | 2.1% (2/95) | 容器 |  |
| `overrideCategories/li` | 2.1% (2/95) | 文本 | BaseCaves / Mountain |
| `overrideDensityForFertilityCurve` | 1.1% (1/95) | 容器 |  |
| `overrideDensityForFertilityCurve/points` | 1.1% (1/95) | 容器 |  |
| `overrideDensityForFertilityCurve/points/li` | 5.3% (5/95) | 文本 | (0, 0.05) / (0.001, -1) / (0.999, -1) |
| `overrideLakeBeachTerrain` | 4.2% (4/95) | 文本 | Marsh / Mud / Sand |
| `overrideMudTerrain` | 3.2% (3/95) | 文本 | Marsh / Mud / Sand |
| `overrideRiverbankTerrain` | 5.3% (5/95) | 文本 | Marsh / Mud / Sand |
| `plantDensityFactor` | 3.2% (3/95) | 数值 | 0 / 0.5 / 1.3 |
| `plantDensityRange` | 4.2% (4/95) | 文本 | 0.0001~0.7 / 0.3~4 |
| `plantKinds` | 3.2% (3/95) | 容器 |  |
| `plantKinds/li` | 17.9% (17/95) | 文本 | Plant_TreeBirch / Plant_TreeOak / Plant_TreePine |
| `pollutionRange` | 8.4% (8/95) | 文本 | 0~0.25 |
| `preventGenSteps` | 2.1% (2/95) | 容器 |  |
| `preventGenSteps/li` | 5.3% (5/95) | 文本 | AncientUtilityBuilding / CaveHives / ScatterRuinsSimple |
| `preventNaturalElevation` | 7.4% (7/95) | 布尔 | true |
| `preventPatches` | 1.1% (1/95) | 布尔 | true |
| `preventsLandmarks` | 2.1% (2/95) | 布尔 | true |
| `preventsPondGeneration` | 11.6% (11/95) | 布尔 | true |
| `priority` | 21.1% (20/95) | 数值 | -1 / 1 / 2 |
| `requiresFactionOfDef` | 2.1% (2/95) | 文本 | Insect |
| `resourceBlacklist` | 1.1% (1/95) | 容器 |  |
| `resourceBlacklist/li` | 1.1% (1/95) | 文本 | MineableObsidian |
| `structureGenParms` | 5.3% (5/95) | 容器 |  |
| `structureGenParms/perimeterExpandBy` | 5.3% (5/95) | 数值 | 2 / 3 / 5 |
| `structureGenParms/perimeterScatteredThings` | 5.3% (5/95) | 容器 |  |
| `structureGenParms/perimeterScatteredThings/AncientBarrel` | 2.1% (2/95) | 数值 | 2 / 8 |
| `structureGenParms/perimeterScatteredThings/AncientChembarrel` | 2.1% (2/95) | 数值 | 20 |
| `structureGenParms/perimeterScatteredThings/AncientChemtruck` | 3.2% (3/95) | 数值 | 1 / 2 |
| `structureGenParms/perimeterScatteredThings/AncientForklift` | 1.1% (1/95) | 数值 | 6 |
| `structureGenParms/perimeterScatteredThings/AncientGenerator` | 1.1% (1/95) | 数值 | 3 |
| `structureGenParms/perimeterScatteredThings/AncientIndustrialTruck` | 3.2% (3/95) | 数值 | 1 / 4 |
| `structureGenParms/perimeterScatteredThings/AncientLargeContainer` | 1.1% (1/95) | 数值 | 4 |
| `structureGenParms/perimeterScatteredThings/AncientMediumContainer` | 1.1% (1/95) | 数值 | 6 |
| `structureGenParms/perimeterScatteredThings/AncientMilitaryBarrier` | 1.1% (1/95) | 数值 | 3 |
| `structureGenParms/perimeterScatteredThings/AncientMortar` | 1.1% (1/95) | 数值 | 3 |
| `structureGenParms/perimeterScatteredThings/AncientOpenContainer` | 1.1% (1/95) | 数值 | 6 |
| `structureGenParms/perimeterScatteredThings/AncientSecurityTurret` | 1.1% (1/95) | 数值 | 3 |
| `structureGenParms/perimeterScatteredThings/AncientTank` | 1.1% (1/95) | 数值 | 1 |
| `structureGenParms/perimeterScatteredThings/ChunkSlagSteel` | 2.1% (2/95) | 数值 | 5 |
| `structureGenParms/perimeterScatteredThings/Filth_BlastMark` | 1.1% (1/95) | 数值 | 1 |
| `structureGenParms/perimeterScatteredThings/Filth_BloodInsect` | 1.1% (1/95) | 数值 | 10 |
| `structureGenParms/perimeterScatteredThings/Filth_OilSmear` | 4.2% (4/95) | 数值 | 1 / 2 |
| `structureGenParms/perimeterScatteredThings/GlowPod` | 1.1% (1/95) | 数值 | 1 |
| `structureGenParms/perimeterScatterTerrain` | 4.2% (4/95) | 容器 |  |
| `structureGenParms/perimeterScatterTerrain/AncientConcrete` | 2.1% (2/95) | 容器 |  |
| `structureGenParms/perimeterScatterTerrain/AncientConcrete/groupDistRange` | 2.1% (2/95) | 文本 | 2~3 |
| `structureGenParms/perimeterScatterTerrain/AncientConcrete/groupsPerHundredCells` | 2.1% (2/95) | 文本 | 0~1 |
| `structureGenParms/perimeterScatterTerrain/AncientConcrete/itemsPerGroup` | 2.1% (2/95) | 文本 | 3~8 |
| `structureGenParms/perimeterScatterTerrain/InsectSludge` | 1.1% (1/95) | 容器 |  |
| `structureGenParms/perimeterScatterTerrain/InsectSludge/groupDistRange` | 1.1% (1/95) | 文本 | 2~3 |
| `structureGenParms/perimeterScatterTerrain/InsectSludge/groupsPerHundredCells` | 1.1% (1/95) | 文本 | 1~2 |
| `structureGenParms/perimeterScatterTerrain/InsectSludge/itemsPerGroup` | 1.1% (1/95) | 文本 | 10~15 |
| `structureGenParms/perimeterScatterTerrain/Soil` | 1.1% (1/95) | 容器 |  |
| `structureGenParms/perimeterScatterTerrain/Soil/groupDistRange` | 1.1% (1/95) | 文本 | 2~3 |
| `structureGenParms/perimeterScatterTerrain/Soil/groupsPerHundredCells` | 1.1% (1/95) | 文本 | 0~1 |
| `structureGenParms/perimeterScatterTerrain/Soil/itemsPerGroup` | 1.1% (1/95) | 文本 | 2~3 |
| `structureGenParms/perimeterTerrainDef` | 4.2% (4/95) | 文本 | AncientConcrete / AncientTile |
| `structureGenParms/perimeterWallChance` | 4.2% (4/95) | 数值 | 0.9 / 0.95 |
| `structureGenParms/perimeterWallDef` | 4.2% (4/95) | 文本 | AncientFence / AncientRazorWire |
| `structureGenParms/scatteredPrefabs` | 5.3% (5/95) | 容器 |  |
| `structureGenParms/scatteredPrefabs/li` | 5.3% (5/95) | 容器 |  |
| `structureGenParms/scatteredPrefabs/li/countPer10kCellsRange` | 5.3% (5/95) | 文本 | 0.2~0.4 / 1~1 |
| `structureGenParms/scatteredPrefabs/li/maxDistFromStructure` | 5.3% (5/95) | 数值 | 24 / 50 / 60 |
| `structureGenParms/scatteredPrefabs/li/minSpacing` | 5.3% (5/95) | 数值 | 0 / 10 / 35 |
| `structureGenParms/scatteredPrefabs/li/prefabs` | 5.3% (5/95) | 容器 |  |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientBunker` | 1.1% (1/95) | 容器 |  |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientBunker/filthChance` | 1.1% (1/95) | 数值 | 0.4 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientBunker/filthDef` | 1.1% (1/95) | 文本 | Filth_MachineBits |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientBunker/filthExpandBy` | 1.1% (1/95) | 数值 | 1 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientBunker/indoorRuin` | 1.1% (1/95) | 布尔 | false |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientBunker/max` | 1.1% (1/95) | 数值 | 1 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientBunker/weight` | 1.1% (1/95) | 数值 | 1.0 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientContainerForklift` | 2.1% (2/95) | 容器 |  |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientContainerForklift/filthChance` | 2.1% (2/95) | 数值 | 0.4 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientContainerForklift/filthDef` | 2.1% (2/95) | 文本 | Filth_MachineBits |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientContainerForklift/filthExpandBy` | 2.1% (2/95) | 数值 | 1 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientContainerForklift/indoorRuin` | 2.1% (2/95) | 布尔 | false |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientContainerForklift/max` | 2.1% (2/95) | 数值 | 1 / 3 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientContainerForklift/weight` | 2.1% (2/95) | 数值 | 1.0 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientLaunchSite_LaunchPad_Large` | 1.1% (1/95) | 容器 |  |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientLaunchSite_LaunchPad_Large/filthChance` | 1.1% (1/95) | 数值 | 0.05 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientLaunchSite_LaunchPad_Large/filthDef` | 1.1% (1/95) | 文本 | Filth_RubbleRock |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientLaunchSite_LaunchPad_Large/filthExpandBy` | 1.1% (1/95) | 数值 | 0 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientLaunchSite_LaunchPad_Large/indoorRuin` | 1.1% (1/95) | 布尔 | false |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientLaunchSite_LaunchPad_Large/max` | 1.1% (1/95) | 数值 | 2 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientLaunchSite_LaunchPad_Large/weight` | 1.1% (1/95) | 数值 | 1.0 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientLaunchSite_LaunchPad_Small` | 1.1% (1/95) | 容器 |  |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientLaunchSite_LaunchPad_Small/filthChance` | 1.1% (1/95) | 数值 | 0.05 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientLaunchSite_LaunchPad_Small/filthDef` | 1.1% (1/95) | 文本 | Filth_RubbleRock |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientLaunchSite_LaunchPad_Small/filthExpandBy` | 1.1% (1/95) | 数值 | 0 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientLaunchSite_LaunchPad_Small/indoorRuin` | 1.1% (1/95) | 布尔 | false |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientLaunchSite_LaunchPad_Small/max` | 1.1% (1/95) | 数值 | 2 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientLaunchSite_LaunchPad_Small/weight` | 1.1% (1/95) | 数值 | 1.0 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientMegaCannonEmplacement` | 1.1% (1/95) | 容器 |  |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientMegaCannonEmplacement/filthChance` | 1.1% (1/95) | 数值 | 0.4 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientMegaCannonEmplacement/filthDef` | 1.1% (1/95) | 文本 | Filth_MachineBits |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientMegaCannonEmplacement/filthExpandBy` | 1.1% (1/95) | 数值 | 1 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientMegaCannonEmplacement/indoorRuin` | 1.1% (1/95) | 布尔 | false |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientMegaCannonEmplacement/max` | 1.1% (1/95) | 数值 | 4 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientMegaCannonEmplacement/weight` | 1.1% (1/95) | 数值 | 3.0 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientTank_Cluster` | 1.1% (1/95) | 容器 |  |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientTank_Cluster/filthChance` | 1.1% (1/95) | 数值 | 0.4 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientTank_Cluster/filthDef` | 1.1% (1/95) | 文本 | Filth_MachineBits |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientTank_Cluster/filthExpandBy` | 1.1% (1/95) | 数值 | 1 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientTank_Cluster/indoorRuin` | 1.1% (1/95) | 布尔 | false |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientTank_Cluster/max` | 1.1% (1/95) | 数值 | 1 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientTank_Cluster/weight` | 1.1% (1/95) | 数值 | 3.0 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientTankBlockade` | 1.1% (1/95) | 容器 |  |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientTankBlockade/filthChance` | 1.1% (1/95) | 数值 | 0.4 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientTankBlockade/filthDef` | 1.1% (1/95) | 文本 | Filth_MachineBits |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientTankBlockade/filthExpandBy` | 1.1% (1/95) | 数值 | 1 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientTankBlockade/indoorRuin` | 1.1% (1/95) | 布尔 | false |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientTankBlockade/max` | 1.1% (1/95) | 数值 | 1 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientTankBlockade/weight` | 1.1% (1/95) | 数值 | 0.5 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientTankTraps` | 1.1% (1/95) | 容器 |  |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientTankTraps/filthChance` | 1.1% (1/95) | 数值 | 0.4 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientTankTraps/filthDef` | 1.1% (1/95) | 文本 | Filth_MachineBits |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientTankTraps/filthExpandBy` | 1.1% (1/95) | 数值 | 1 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientTankTraps/indoorRuin` | 1.1% (1/95) | 布尔 | false |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientTankTraps/max` | 1.1% (1/95) | 数值 | 1 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_AncientTankTraps/weight` | 1.1% (1/95) | 数值 | 0.5 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_BurrowWallCluster_Large` | 1.1% (1/95) | 容器 |  |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_BurrowWallCluster_Large/filthChance` | 1.1% (1/95) | 数值 | 0.05 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_BurrowWallCluster_Large/filthDef` | 1.1% (1/95) | 文本 | Filth_BloodInsect |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_BurrowWallCluster_Large/filthExpandBy` | 1.1% (1/95) | 数值 | 1 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_BurrowWallCluster_Large/indoorRuin` | 1.1% (1/95) | 布尔 | false |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_BurrowWallCluster_Large/max` | 1.1% (1/95) | 数值 | 3 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_BurrowWallCluster_Large/weight` | 1.1% (1/95) | 数值 | 1.0 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_BurrowWallCluster_Medium` | 1.1% (1/95) | 容器 |  |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_BurrowWallCluster_Medium/filthChance` | 1.1% (1/95) | 数值 | 0.05 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_BurrowWallCluster_Medium/filthDef` | 1.1% (1/95) | 文本 | Filth_BloodInsect |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_BurrowWallCluster_Medium/filthExpandBy` | 1.1% (1/95) | 数值 | 1 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_BurrowWallCluster_Medium/indoorRuin` | 1.1% (1/95) | 布尔 | false |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_BurrowWallCluster_Medium/max` | 1.1% (1/95) | 数值 | 3 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_BurrowWallCluster_Medium/weight` | 1.1% (1/95) | 数值 | 2.0 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_BurrowWallFarm` | 1.1% (1/95) | 容器 |  |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_BurrowWallFarm/filthChance` | 1.1% (1/95) | 数值 | 0.05 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_BurrowWallFarm/filthDef` | 1.1% (1/95) | 文本 | Filth_BloodInsect |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_BurrowWallFarm/filthExpandBy` | 1.1% (1/95) | 数值 | 1 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_BurrowWallFarm/indoorRuin` | 1.1% (1/95) | 布尔 | true |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_BurrowWallFarm/max` | 1.1% (1/95) | 数值 | 1 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_BurrowWallFarm/weight` | 1.1% (1/95) | 数值 | 0.5 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_BurrowWallGenerator` | 1.1% (1/95) | 容器 |  |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_BurrowWallGenerator/filthChance` | 1.1% (1/95) | 数值 | 0.05 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_BurrowWallGenerator/filthDef` | 1.1% (1/95) | 文本 | Filth_BloodInsect |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_BurrowWallGenerator/filthExpandBy` | 1.1% (1/95) | 数值 | 1 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_BurrowWallGenerator/indoorRuin` | 1.1% (1/95) | 布尔 | false |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_BurrowWallGenerator/max` | 1.1% (1/95) | 数值 | 3 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_BurrowWallGenerator/weight` | 1.1% (1/95) | 数值 | 1.0 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_ChembarrelStorage` | 1.1% (1/95) | 容器 |  |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_ChembarrelStorage/filthChance` | 1.1% (1/95) | 数值 | 0.05 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_ChembarrelStorage/filthDef` | 1.1% (1/95) | 文本 | Filth_OilSmear |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_ChembarrelStorage/filthExpandBy` | 1.1% (1/95) | 数值 | 1 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_ChembarrelStorage/indoorRuin` | 1.1% (1/95) | 布尔 | false |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_ChembarrelStorage/max` | 1.1% (1/95) | 数值 | 3 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_ChembarrelStorage/weight` | 1.1% (1/95) | 数值 | 1.0 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_ChembarrelStorageBuilding` | 1.1% (1/95) | 容器 |  |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_ChembarrelStorageBuilding/filthChance` | 1.1% (1/95) | 数值 | 0.05 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_ChembarrelStorageBuilding/filthDef` | 1.1% (1/95) | 文本 | Filth_OilSmear |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_ChembarrelStorageBuilding/filthExpandBy` | 1.1% (1/95) | 数值 | 1 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_ChembarrelStorageBuilding/indoorRuin` | 1.1% (1/95) | 布尔 | true |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_ChembarrelStorageBuilding/max` | 1.1% (1/95) | 数值 | 1 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_ChembarrelStorageBuilding/weight` | 1.1% (1/95) | 数值 | 2.0 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_ChemtruckParkingLot` | 1.1% (1/95) | 容器 |  |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_ChemtruckParkingLot/filthChance` | 1.1% (1/95) | 数值 | 0.05 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_ChemtruckParkingLot/filthDef` | 1.1% (1/95) | 文本 | Filth_OilSmear |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_ChemtruckParkingLot/filthExpandBy` | 1.1% (1/95) | 数值 | 1 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_ChemtruckParkingLot/indoorRuin` | 1.1% (1/95) | 布尔 | false |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_ChemtruckParkingLot/max` | 1.1% (1/95) | 数值 | 1 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_ChemtruckParkingLot/weight` | 1.1% (1/95) | 数值 | 1.0 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_ChemtruckParkingLot_Long` | 1.1% (1/95) | 容器 |  |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_ChemtruckParkingLot_Long/filthChance` | 1.1% (1/95) | 数值 | 0.05 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_ChemtruckParkingLot_Long/filthDef` | 1.1% (1/95) | 文本 | Filth_OilSmear |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_ChemtruckParkingLot_Long/filthExpandBy` | 1.1% (1/95) | 数值 | 1 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_ChemtruckParkingLot_Long/indoorRuin` | 1.1% (1/95) | 布尔 | false |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_ChemtruckParkingLot_Long/max` | 1.1% (1/95) | 数值 | 2 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_ChemtruckParkingLot_Long/weight` | 1.1% (1/95) | 数值 | 2.0 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_ContainerSite` | 2.1% (2/95) | 容器 |  |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_ContainerSite/filthChance` | 2.1% (2/95) | 数值 | 0.4 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_ContainerSite/filthDef` | 2.1% (2/95) | 文本 | Filth_MachineBits |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_ContainerSite/filthExpandBy` | 2.1% (2/95) | 数值 | 1 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_ContainerSite/indoorRuin` | 2.1% (2/95) | 布尔 | false |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_ContainerSite/max` | 2.1% (2/95) | 数值 | 1 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_ContainerSite/weight` | 2.1% (2/95) | 数值 | 1.0 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_MilitaryBlockade` | 1.1% (1/95) | 容器 |  |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_MilitaryBlockade/filthChance` | 1.1% (1/95) | 数值 | 0.4 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_MilitaryBlockade/filthDef` | 1.1% (1/95) | 文本 | Filth_MachineBits |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_MilitaryBlockade/filthExpandBy` | 1.1% (1/95) | 数值 | 1 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_MilitaryBlockade/indoorRuin` | 1.1% (1/95) | 布尔 | false |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_MilitaryBlockade/max` | 1.1% (1/95) | 数值 | 2 |
| `structureGenParms/scatteredPrefabs/li/prefabs/Exterior_MilitaryBlockade/weight` | 1.1% (1/95) | 数值 | 0.5 |
| `structureGenParms/structureLayoutDef` | 5.3% (5/95) | 文本 | AncientChemfuelRefinery / AncientGarrison / AncientInfestedSettlement |
| `structureGenParms/structureSizeRange` | 5.3% (5/95) | 文本 | 35~55 / 36~44 / 40~50 |
| `terrainPatchMakers` | 4.2% (4/95) | 容器 |  |
| `terrainPatchMakers/li` | 4.2% (4/95) | 容器 |  |
| `terrainPatchMakers/li/perlinFrequency` | 4.2% (4/95) | 数值 | 0.035 |
| `terrainPatchMakers/li/thresholds` | 4.2% (4/95) | 容器 |  |
| `terrainPatchMakers/li/thresholds/li` | 5.3% (5/95) | 容器 |  |
| `terrainPatchMakers/li/thresholds/li/max` | 5.3% (5/95) | 数值 | 0.7 / 999 |
| `terrainPatchMakers/li/thresholds/li/min` | 5.3% (5/95) | 数值 | 0.5 / 0.64 / 0.7 |
| `terrainPatchMakers/li/thresholds/li/terrain` | 5.3% (5/95) | 文本 | Marsh / MarshyTerrain / Sand |
| `weatherFrequencyOffset` | 4.2% (4/95) | 数值 | 10 |
| `weathersToAffect` | 4.2% (4/95) | 容器 |  |
| `weathersToAffect/li` | 9.5% (9/95) | 文本 | Clear / Fog / Rain |
| `workerClass` | 80.0% (76/95) | 文本 | TileMutatorWorker_Caves / TileMutatorWorker_Coast / TileMutatorWorker_Mountain |

## 四、原版 defName 一览（共 95 个，列出前 60）

```text
`AbandonedColonyTribal`           `AbandonedColonyOutlander`        `LakeWithIslands`                 `Cove`                          
`LavaLake`                        `LavaCrater`                      `AncientSmokeVent`                `AncientToxVent`                
`AncientUplink`                   `Lake`                            ``                                `LakeWithIsland`                
``                                `Pollution_Increased`             `Bay`                             `Fjord`                         
`InsectMegahive`                  `Coast`                           `AncientRuins_Frozen`             `Stockpile`                     
`AnimalLife_Decreased`            ``                                `ObsidianDeposits`                `RiverConfluence`               
`Lakeshore`                       `Peninsula`                       `Mountain`                        `River`                         
`UndergroundCave`                 `AncientRuins`                    `AncientHeatVent`                 `Harbor`                        
`AnimalHabitat`                   `PlantLife_Decreased`             `SteamGeysers_Increased`          `RiverIsland`                   
`Caves`                           `AnimalLife_Increased`            `WildTropicalPlants`              `Junkyard`                      
`MineralRich`                     `Fish_Decreased`                  ``                                `Headwater`                     
`RiverDelta`                      `Archipelago`                     `CoastalIsland`                   `IceCaves`                      
`DryGround`                       ``                                `ToxicLake`                       `Valley`                        
`Chasm`                           `IceDunes`                        `Hollow`                          `CaveLakes`                     
``                                `PlantLife_Increased`             `SunnyMutator`                    `Fish_Increased`                
```

_余下 35 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
