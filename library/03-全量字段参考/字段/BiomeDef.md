# BiomeDef

- **所属线**：世界线
- **原版实例数**：25
- **字段路径数**：288
- **资料片**：Anomaly、Core、Odyssey
- **原版出处**：`Odyssey/Defs/BiomeDefs/Space.xml`、`Odyssey/Defs/BiomeDefs/Scarlands.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<BiomeDef ParentName="SpaceBiome">
    <defName>Orbit</defName>
    <label>orbit</label>
    <description>Empty space a few hundred kilometers above the surface of the world.</description>
  </BiomeDef>
```

> 来自 `Odyssey/Defs/BiomeDefs/Space.xml`，defName = `Orbit`，XML 节点数 4（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
allowedPackAnimals/li                          [文本]  例：Alpaca / Dromedary / Elephant
defName                                        [文本]  例：BorealForest / Labyrinth / MetalHell
description                                    [文本]  例：Forests of coniferous trees. Despite the harsh winters, boreal forests sustain a / The room is made entirely of gray metal with jagged and twisted shapes that seem / This cave is filled with the putrid stench of rotting flesh.
diseases/li                                    [容器]
diseases/li/commonality                        [数值]  例：100 / 20 / 30
diseases/li/diseaseInc                         [文本]  例：Disease_AnimalFlu / Disease_AnimalPlague / Disease_MuscleParasites
label                                          [文本]  例：boreal forest / labyrinth / metal hell
terrainPatchMakers/li                          [容器]
terrainPatchMakers/li/perlinFrequency          [数值]  例：0.015 / 0.027 / 0.028
terrainPatchMakers/li/thresholds               [容器]
terrainPatchMakers/li/thresholds/li            [容器]
terrainPatchMakers/li/thresholds/li/max        [数值]  例：0.32 / 0.76 / 0.83
terrainPatchMakers/li/thresholds/li/min        [数值]  例：0.0 / 0.32 / 0.76
terrainPatchMakers/li/thresholds/li/terrain    [文本]  例：Marsh / MossyTerrain / Mud
terrainsByFertility/li                         [容器]
terrainsByFertility/li/max                     [数值]  例：0.45 / 0.87 / 0.90
terrainsByFertility/li/min                     [数值]  例：-999 / 0.45 / 0.87
terrainsByFertility/li/terrain                 [文本]  例：Ice / Sand / Soil
```

## 三、全量字段表（288 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `allowedPackAnimals` | 68.0% (17/25) | 容器 |  |
| `allowedPackAnimals/li` | 136.0% (34/25) | 文本 | Alpaca / Dromedary / Elephant |
| `allowFarmingCamps` | 44.0% (11/25) | 布尔 | false / true |
| `allowPollution` | 4.0% (1/25) | 布尔 | true |
| `allowRivers` | 24.0% (6/25) | 布尔 | false / true |
| `allowRoads` | 24.0% (6/25) | 布尔 | false |
| `animalDensity` | 84.0% (21/25) | 数值 | 0 / 1.1 / 2.8 |
| `baseWeatherCommonalities` | 88.0% (22/25) | 容器 |  |
| `baseWeatherCommonalities/BlindFog` | 16.0% (4/25) | 数值 | 1 |
| `baseWeatherCommonalities/Blizzard` | 20.0% (5/25) | 数值 | 1 / 2 |
| `baseWeatherCommonalities/Clear` | 72.0% (18/25) | 数值 | 1 / 12 / 18 |
| `baseWeatherCommonalities/DryThunderstorm` | 68.0% (17/25) | 数值 | 0.3 / 1 / 2 |
| `baseWeatherCommonalities/Fog` | 60.0% (15/25) | 数值 | 0 / 1 / 2 |
| `baseWeatherCommonalities/FoggyRain` | 60.0% (15/25) | 数值 | 0 / 0.5 / 1 |
| `baseWeatherCommonalities/GrayPall` | 68.0% (17/25) | 数值 | 1 |
| `baseWeatherCommonalities/MetalHell` | 4.0% (1/25) | 数值 | 1 |
| `baseWeatherCommonalities/Orbit` | 4.0% (1/25) | 数值 | 1 |
| `baseWeatherCommonalities/Overcast` | 52.0% (13/25) | 数值 | 1 / 2 / 6 |
| `baseWeatherCommonalities/Rain` | 68.0% (17/25) | 数值 | 0 / 1 / 2 |
| `baseWeatherCommonalities/RainyThunderstorm` | 68.0% (17/25) | 数值 | 0 / 1 / 1.7 |
| `baseWeatherCommonalities/Sandstorm` | 8.0% (2/25) | 数值 | 1 / 2 |
| `baseWeatherCommonalities/SnowGentle` | 68.0% (17/25) | 数值 | 1.5 / 20 / 4 |
| `baseWeatherCommonalities/SnowHard` | 68.0% (17/25) | 数值 | 1 / 4 / 40 |
| `baseWeatherCommonalities/TorrentialRain` | 24.0% (6/25) | 数值 | 0.5 |
| `baseWeatherCommonalities/ToxRain` | 4.0% (1/25) | 数值 | 1 |
| `baseWeatherCommonalities/Undercave` | 4.0% (1/25) | 数值 | 1 |
| `baseWeatherCommonalities/Underground` | 4.0% (1/25) | 数值 | 1 |
| `baseWeatherCommonalities/Windy` | 24.0% (6/25) | 数值 | 1 / 2 / 4 |
| `biomeMapConditions` | 4.0% (1/25) | 容器 |  |
| `biomeMapConditions/li` | 4.0% (1/25) | 文本 | DarkenedSkies |
| `campSelectionWeight` | 40.0% (10/25) | 数值 | 0.1 / 0.9 |
| `canAutoChoose` | 12.0% (3/25) | 布尔 | false |
| `canBuildBase` | 8.0% (2/25) | 布尔 | false |
| `canExitMap` | 4.0% (1/25) | 布尔 | false |
| `coastalBeachTerrain` | 12.0% (3/25) | 文本 | Ice / Mud |
| `coastalWildAnimals` | 64.0% (16/25) | 容器 |  |
| `coastalWildAnimals/HermitCrab` | 28.0% (7/25) | 数值 | 0.1 |
| `coastalWildAnimals/Otter` | 12.0% (3/25) | 数值 | 0.1 |
| `coastalWildAnimals/Penguin` | 12.0% (3/25) | 数值 | 0.1 |
| `coastalWildAnimals/Seal` | 20.0% (5/25) | 数值 | 0.1 |
| `coastalWildAnimals/SeaLion` | 20.0% (5/25) | 数值 | 0.1 |
| `coastalWildAnimals/SeaTurtle` | 16.0% (4/25) | 数值 | 0.1 |
| `coastalWildAnimals/StoneCrab` | 28.0% (7/25) | 数值 | 0.1 |
| `coastalWildAnimals/Walrus` | 24.0% (6/25) | 数值 | 0.1 |
| `constantOutdoorTemperature` | 4.0% (1/25) | 数值 | -75 |
| `defName` | 100.0% (25/25) | 文本 | BorealForest / Labyrinth / MetalHell |
| `description` | 100.0% (25/25) | 文本 | Forests of coniferous trees. Despite the harsh winters, boreal forests sustain a / The room is made entirely o |
| `diseaseMtbDays` | 80.0% (20/25) | 数值 | 0 / 45 / 60 |
| `diseases` | 80.0% (20/25) | 容器 |  |
| `diseases/li` | 700.0% (175/25) | 容器 |  |
| `diseases/li/commonality` | 700.0% (175/25) | 数值 | 100 / 20 / 30 |
| `diseases/li/diseaseInc` | 700.0% (175/25) | 文本 | Disease_AnimalFlu / Disease_AnimalPlague / Disease_MuscleParasites |
| `extraGenSteps` | 16.0% (4/25) | 容器 |  |
| `extraGenSteps/li` | 40.0% (10/25) | 文本 | FrozenRuins / GeothermalVents / Glaciers |
| `extraRockTypes` | 4.0% (1/25) | 容器 |  |
| `extraRockTypes/li` | 4.0% (1/25) | 文本 | SolidIce |
| `fishTypes` | 64.0% (16/25) | 容器 |  |
| `fishTypes/freshwater_Common` | 64.0% (16/25) | 容器 |  |
| `fishTypes/freshwater_Common/Fish_Bass` | 20.0% (5/25) | 数值 | 1 |
| `fishTypes/freshwater_Common/Fish_Guppy` | 8.0% (2/25) | 数值 | 1 |
| `fishTypes/freshwater_Common/Fish_Salmon` | 28.0% (7/25) | 数值 | 1 |
| `fishTypes/freshwater_Common/Fish_Tilapia` | 12.0% (3/25) | 数值 | 1 |
| `fishTypes/freshwater_Uncommon` | 64.0% (16/25) | 容器 |  |
| `fishTypes/freshwater_Uncommon/Fish_Catfish` | 28.0% (7/25) | 数值 | 1 |
| `fishTypes/freshwater_Uncommon/Fish_Frostfish` | 24.0% (6/25) | 数值 | 1 |
| `fishTypes/freshwater_Uncommon/Fish_Piranha` | 8.0% (2/25) | 数值 | 1 |
| `fishTypes/freshwater_Uncommon/Fish_Tilapia` | 8.0% (2/25) | 数值 | 1 |
| `fishTypes/rareCatchesSetMaker` | 64.0% (16/25) | 文本 | RareFishingCatches_Cold / RareFishingCatches_Hot / RareFishingCatches_Temperate |
| `fishTypes/saltwater_Common` | 64.0% (16/25) | 容器 |  |
| `fishTypes/saltwater_Common/Fish_Bluefish` | 40.0% (10/25) | 数值 | 1 |
| `fishTypes/saltwater_Common/Fish_Cod` | 24.0% (6/25) | 数值 | 1 |
| `fishTypes/saltwater_Common/Fish_Salmon` | 28.0% (7/25) | 数值 | 1 |
| `fishTypes/saltwater_Uncommon` | 64.0% (16/25) | 容器 |  |
| `fishTypes/saltwater_Uncommon/Fish_Dogfish` | 24.0% (6/25) | 数值 | 1 |
| `fishTypes/saltwater_Uncommon/Fish_Flounder` | 28.0% (7/25) | 数值 | 1 |
| `fishTypes/saltwater_Uncommon/Fish_Marlin` | 20.0% (5/25) | 数值 | 1 |
| `fishTypes/saltwater_Uncommon/Fish_Tuna` | 20.0% (5/25) | 数值 | 1 |
| `forageability` | 68.0% (17/25) | 数值 | 0 / 0.5 / 0.75 |
| `foragedFood` | 52.0% (13/25) | 文本 | RawAgave / RawBerries / RawFungus |
| `forceRockTypes` | 4.0% (1/25) | 容器 |  |
| `forceRockTypes/li` | 4.0% (1/25) | 文本 | Vacstone |
| `generatesNaturally` | 16.0% (4/25) | 布尔 | false |
| `geyserCountFactor` | 12.0% (3/25) | 数值 | 0 / 1.5 |
| `hasBedrock` | 12.0% (3/25) | 布尔 | false / true |
| `hasVirtualPlants` | 28.0% (7/25) | 布尔 | false / true |
| `impassable` | 8.0% (2/25) | 布尔 | true |
| `inVacuum` | 4.0% (1/25) | 布尔 | true |
| `isBackgroundBiome` | 8.0% (2/25) | 布尔 | true |
| `isExtremeBiome` | 16.0% (4/25) | 布尔 | true |
| `isWaterBiome` | 8.0% (2/25) | 布尔 | true |
| `label` | 100.0% (25/25) | 文本 | boreal forest / labyrinth / metal hell |
| `lakeBeachTerrain` | 68.0% (17/25) | 文本 | Gravel / Ice / Marsh |
| `maxFishPopulation` | 76.0% (19/25) | 数值 | 200 / 500 / 600 |
| `movementDifficulty` | 68.0% (17/25) | 数值 | 1 / 1.5 / 2 |
| `mudTerrain` | 36.0% (9/25) | 文本 | Gravel / Ice / Marsh |
| `noAmbientWind` | 4.0% (1/25) | 布尔 | true |
| `noGravel` | 8.0% (2/25) | 布尔 | true |
| `oceanDeepTerrain` | 4.0% (1/25) | 文本 | ToxicWaterOceanDeep |
| `oceanShallowTerrain` | 4.0% (1/25) | 文本 | ToxicWaterOceanShallow |
| `plantDensity` | 84.0% (21/25) | 数值 | 0 / 0.19 / 0.40 |
| `pollutionOffset` | 4.0% (1/25) | 数值 | 0.05 |
| `pollutionWildAnimals` | 60.0% (15/25) | 容器 |  |
| `pollutionWildAnimals/Boomalope` | 36.0% (9/25) | 数值 | 0.1 / 0.4 |
| `pollutionWildAnimals/Boomrat` | 24.0% (6/25) | 数值 | 0.4 |
| `pollutionWildAnimals/Iguana` | 16.0% (4/25) | 数值 | 1 |
| `pollutionWildAnimals/Megascarab` | 16.0% (4/25) | 数值 | 0.2 / 1 |
| `pollutionWildAnimals/MonitorLizard` | 4.0% (1/25) | 数值 | 0.5 |
| `pollutionWildAnimals/Raccoon` | 40.0% (10/25) | 数值 | 0.25 / 0.5 |
| `pollutionWildAnimals/Rat` | 48.0% (12/25) | 数值 | 0.5 / 0.6 / 1 |
| `pollutionWildAnimals/Toxalope` | 36.0% (9/25) | 数值 | 0.1 / 0.4 |
| `pollutionWildAnimals/Warg` | 36.0% (9/25) | 数值 | 0.05 |
| `pollutionWildAnimals/WasteRat` | 36.0% (9/25) | 数值 | 0.1 / 0.5 / 1 |
| `preventGenSteps` | 8.0% (2/25) | 容器 |  |
| `preventGenSteps/li` | 48.0% (12/25) | 文本 | AncientTurret / AncientUtilityBuilding / RockChunks |
| `riverbankSizeRange` | 48.0% (12/25) | 文本 | 6~12 / 6~8 |
| `riverbankTerrain` | 52.0% (13/25) | 文本 | Gravel / Mud / Riverbank |
| `settlementSelectionWeight` | 68.0% (17/25) | 数值 | 0.15 / 0.17 / 0.32 |
| `settleWarning` | 24.0% (6/25) | 文本 | Ice sheet is extremely inhospitable. There is no soil for plants and almost no a / Large sulfur spouts permane |
| `soundsAmbient` | 64.0% (16/25) | 容器 |  |
| `soundsAmbient/li` | 76.0% (19/25) | 文本 | Ambient_DayInsects_Jungle / Ambient_NightInsects_Jungle / Ambient_NightInsects_Standard |
| `terrainPatchMakers` | 64.0% (16/25) | 容器 |  |
| `terrainPatchMakers/li` | 92.0% (23/25) | 容器 |  |
| `terrainPatchMakers/li/isPond` | 36.0% (9/25) | 布尔 | true |
| `terrainPatchMakers/li/maxFertility` | 4.0% (1/25) | 数值 | 0.8 |
| `terrainPatchMakers/li/minSize` | 8.0% (2/25) | 数值 | 13 |
| `terrainPatchMakers/li/perlinFrequency` | 92.0% (23/25) | 数值 | 0.015 / 0.027 / 0.028 |
| `terrainPatchMakers/li/perlinLacunarity` | 4.0% (1/25) | 数值 | 1.5 |
| `terrainPatchMakers/li/perlinOctaves` | 4.0% (1/25) | 数值 | 6 |
| `terrainPatchMakers/li/thresholds` | 92.0% (23/25) | 容器 |  |
| `terrainPatchMakers/li/thresholds/li` | 172.0% (43/25) | 容器 |  |
| `terrainPatchMakers/li/thresholds/li/max` | 172.0% (43/25) | 数值 | 0.32 / 0.76 / 0.83 |
| `terrainPatchMakers/li/thresholds/li/min` | 172.0% (43/25) | 数值 | 0.0 / 0.32 / 0.76 |
| `terrainPatchMakers/li/thresholds/li/terrain` | 172.0% (43/25) | 文本 | Marsh / MossyTerrain / Mud |
| `terrainsByFertility` | 68.0% (17/25) | 容器 |  |
| `terrainsByFertility/li` | 128.0% (32/25) | 容器 |  |
| `terrainsByFertility/li/max` | 128.0% (32/25) | 数值 | 0.45 / 0.87 / 0.90 |
| `terrainsByFertility/li/min` | 128.0% (32/25) | 数值 | -999 / 0.45 / 0.87 |
| `terrainsByFertility/li/terrain` | 128.0% (32/25) | 文本 | Ice / Sand / Soil |
| `texture` | 76.0% (19/25) | 文本 | World/Biomes/BorealForest / World/Biomes/ColdBog / World/Biomes/IceSheet |
| `waterDeepTerrain` | 4.0% (1/25) | 文本 | ToxicWaterDeep |
| `waterMovingChestDeepTerrain` | 4.0% (1/25) | 文本 | ToxicWaterMovingChestDeep |
| `waterMovingShallowTerrain` | 4.0% (1/25) | 文本 | ToxicWaterMovingShallow |
| `waterShallowTerrain` | 4.0% (1/25) | 文本 | ToxicWaterShallow |
| `wildAnimals` | 68.0% (17/25) | 容器 |  |
| `wildAnimals/Alligator` | 8.0% (2/25) | 数值 | 0.07 |
| `wildAnimals/Alpaca` | 16.0% (4/25) | 数值 | 0.5 |
| `wildAnimals/Armadillo` | 8.0% (2/25) | 数值 | 0.2 |
| `wildAnimals/Badger` | 16.0% (4/25) | 数值 | 0.2 |
| `wildAnimals/Bear_Grizzly` | 28.0% (7/25) | 数值 | 0.07 |
| `wildAnimals/Bear_Polar` | 16.0% (4/25) | 数值 | 0.07 / 0.1 |
| `wildAnimals/Bison` | 12.0% (3/25) | 数值 | 0.07 / 0.1 / 0.5 |
| `wildAnimals/Bluebird` | 12.0% (3/25) | 数值 | 0.1 / 0.5 |
| `wildAnimals/BogHound` | 4.0% (1/25) | 数值 | 0.5 |
| `wildAnimals/Boomalope` | 40.0% (10/25) | 数值 | 0.4 / 0.5 / 0.6 |
| `wildAnimals/Boomrat` | 20.0% (5/25) | 数值 | 0.4 / 0.5 |
| `wildAnimals/Bullfrog` | 12.0% (3/25) | 数值 | 0.2 / 0.4 / 0.5 |
| `wildAnimals/Capybara` | 12.0% (3/25) | 数值 | 0.5 |
| `wildAnimals/Caribou` | 16.0% (4/25) | 数值 | 0.5 / 2 |
| `wildAnimals/Cassowary` | 12.0% (3/25) | 数值 | 0.5 |
| `wildAnimals/Cat_Scimitar` | 4.0% (1/25) | 数值 | 0.1 |
| `wildAnimals/Chinchilla` | 12.0% (3/25) | 数值 | 0.1 / 0.5 |
| `wildAnimals/Cobra` | 12.0% (3/25) | 数值 | 0.15 / 0.2 |
| `wildAnimals/ColossusToad` | 8.0% (2/25) | 数值 | 0.1 / 0.25 |
| `wildAnimals/Cougar` | 36.0% (9/25) | 数值 | 0.07 / 0.15 |
| `wildAnimals/Crow` | 16.0% (4/25) | 数值 | 0.5 |
| `wildAnimals/Deer` | 24.0% (6/25) | 数值 | 0.25 / 0.5 |
| `wildAnimals/Donkey` | 24.0% (6/25) | 数值 | 0.15 / 0.2 / 0.20 |
| `wildAnimals/Dromedary` | 12.0% (3/25) | 数值 | 0.2 / 0.7 |
| `wildAnimals/Duck` | 8.0% (2/25) | 数值 | 0.5 |
| `wildAnimals/Elephant` | 12.0% (3/25) | 数值 | 0.5 |
| `wildAnimals/Elk` | 16.0% (4/25) | 数值 | 0.5 / 2 |
| `wildAnimals/Emu` | 12.0% (3/25) | 数值 | 0.6 / 0.7 |
| `wildAnimals/Flamingo` | 8.0% (2/25) | 数值 | 0.5 |
| `wildAnimals/Fox_Arctic` | 20.0% (5/25) | 数值 | 0.07 / 0.1 |
| `wildAnimals/Fox_Fennec` | 20.0% (5/25) | 数值 | 0.07 / 0.1 / 0.15 |
| `wildAnimals/Fox_Red` | 24.0% (6/25) | 数值 | 0.07 |
| `wildAnimals/Gazelle` | 16.0% (4/25) | 数值 | 0.3 / 0.6 / 0.7 |
| `wildAnimals/Gorilla` | 8.0% (2/25) | 数值 | 0.02 / 0.05 |
| `wildAnimals/GuineaPig` | 36.0% (9/25) | 数值 | 0.07 / 0.15 / 0.25 |
| `wildAnimals/Hare` | 36.0% (9/25) | 数值 | 1 / 1.0 / 1.3 |
| `wildAnimals/Heron` | 8.0% (2/25) | 数值 | 0.2 / 0.5 |
| `wildAnimals/Hippo` | 8.0% (2/25) | 数值 | 0.1 / 0.25 |
| `wildAnimals/Horse` | 24.0% (6/25) | 数值 | 0.1 / 0.15 / 0.20 |
| `wildAnimals/Ibex` | 28.0% (7/25) | 数值 | 0.5 / 2 |
| `wildAnimals/Iguana` | 20.0% (5/25) | 数值 | 0.22 / 0.7 / 1.2 |
| `wildAnimals/LavaSnail` | 4.0% (1/25) | 数值 | 0.5 |
| `wildAnimals/Lynx` | 32.0% (8/25) | 数值 | 0.07 / 0.1 |
| `wildAnimals/Macaw` | 8.0% (2/25) | 数值 | 0.25 |
| `wildAnimals/Mastodon` | 8.0% (2/25) | 数值 | 0.1 / 0.2 |
| `wildAnimals/Megasloth` | 32.0% (8/25) | 数值 | 0.1 / 0.2 |
| `wildAnimals/Megavole` | 4.0% (1/25) | 数值 | 0.25 |
| `wildAnimals/Mink` | 16.0% (4/25) | 数值 | 0.1 / 0.2 |
| `wildAnimals/MonitorLizard` | 20.0% (5/25) | 数值 | 0.5 |
| `wildAnimals/Monkey` | 8.0% (2/25) | 数值 | 1 |
| `wildAnimals/Moose` | 16.0% (4/25) | 数值 | 0.2 |
| `wildAnimals/Muffalo` | 32.0% (8/25) | 数值 | 0.1 / 0.5 / 1 |
| `wildAnimals/Muskox` | 8.0% (2/25) | 数值 | 0.25 / 1 |
| `wildAnimals/Ostrich` | 8.0% (2/25) | 数值 | 0.6 / 0.7 |
| `wildAnimals/Panda` | 8.0% (2/25) | 数值 | 0.05 |
| `wildAnimals/Panther` | 12.0% (3/25) | 数值 | 0.07 / 0.15 |
| `wildAnimals/Peacock` | 12.0% (3/25) | 数值 | 0.25 / 0.5 |
| `wildAnimals/Pig` | 4.0% (1/25) | 数值 | 0.07 |
| `wildAnimals/Porcupine` | 16.0% (4/25) | 数值 | 0.2 |
| `wildAnimals/PrairieDog` | 4.0% (1/25) | 数值 | 1 |
| `wildAnimals/Quail` | 8.0% (2/25) | 数值 | 0.5 |
| `wildAnimals/Raccoon` | 32.0% (8/25) | 数值 | 0.5 |
| `wildAnimals/Rat` | 44.0% (11/25) | 数值 | 1 / 1.0 / 1.00 |
| `wildAnimals/Rhinoceros` | 20.0% (5/25) | 数值 | 0.1 / 0.5 |
| `wildAnimals/Snowhare` | 12.0% (3/25) | 数值 | 2 |
| `wildAnimals/Sparrow` | 28.0% (7/25) | 数值 | 0.25 / 0.5 |
| `wildAnimals/Squirrel` | 24.0% (6/25) | 数值 | 1 / 1.0 |
| `wildAnimals/Swan` | 16.0% (4/25) | 数值 | 0.1 |
| `wildAnimals/Tiger` | 8.0% (2/25) | 数值 | 0.05 |
| `wildAnimals/Tortoise` | 20.0% (5/25) | 数值 | 0.3 / 0.5 / 0.6 |
| `wildAnimals/Turkey` | 20.0% (5/25) | 数值 | 0.5 |
| `wildAnimals/Vulture` | 20.0% (5/25) | 数值 | 0.5 / 1 |
| `wildAnimals/Warg` | 28.0% (7/25) | 数值 | 0.07 |
| `wildAnimals/WildBoar` | 32.0% (8/25) | 数值 | 0.5 |
| `wildAnimals/Wolf_Arctic` | 20.0% (5/25) | 数值 | 0.07 / 0.1 |
| `wildAnimals/Wolf_Great` | 16.0% (4/25) | 数值 | 0.02 / 0.07 |
| `wildAnimals/Wolf_Timber` | 28.0% (7/25) | 数值 | 0.07 |
| `wildAnimals/Wolverine` | 20.0% (5/25) | 数值 | 0.07 |
| `wildAnimals/Yak` | 20.0% (5/25) | 数值 | 0.04 / 0.06 / 0.12 |
| `wildAnimalsCanWanderInto` | 16.0% (4/25) | 布尔 | false |
| `wildAnimalScariaChance` | 4.0% (1/25) | 数值 | 0.5 |
| `wildPlantRegrowDays` | 56.0% (14/25) | 数值 | 15 / 20 / 25 |
| `wildPlants` | 60.0% (15/25) | 容器 |  |
| `wildPlants/Agarilux` | 4.0% (1/25) | 数值 | 0.01 |
| `wildPlants/Boomshroom` | 4.0% (1/25) | 数值 | 0.01 |
| `wildPlants/Bryolux` | 4.0% (1/25) | 数值 | 0.05 |
| `wildPlants/BurnedTree` | 4.0% (1/25) | 数值 | 0.1 |
| `wildPlants/Glowstool` | 4.0% (1/25) | 数值 | 0.01 |
| `wildPlants/Plant_Agave` | 16.0% (4/25) | 数值 | 0.05 / 0.2 / 0.25 |
| `wildPlants/Plant_Alocasia` | 8.0% (2/25) | 数值 | 0.8 |
| `wildPlants/Plant_Astragalus` | 8.0% (2/25) | 数值 | 0.1 |
| `wildPlants/Plant_Berry` | 44.0% (11/25) | 数值 | 0.05 / 0.07 / 0.10 |
| `wildPlants/Plant_Berry_Leafless` | 4.0% (1/25) | 数值 | 0.02 |
| `wildPlants/Plant_Brambles` | 12.0% (3/25) | 数值 | 1.0 / 2.0 |
| `wildPlants/Plant_Brambles_Leafless` | 4.0% (1/25) | 数值 | 1.0 |
| `wildPlants/Plant_Bulrush` | 20.0% (5/25) | 数值 | 0.2 |
| `wildPlants/Plant_Bush` | 48.0% (12/25) | 数值 | 0.2 / 0.3 / 0.6 |
| `wildPlants/Plant_Bush_Leafless` | 4.0% (1/25) | 数值 | 0.6 |
| `wildPlants/Plant_Chokevine` | 12.0% (3/25) | 数值 | 0.8 / 3.0 |
| `wildPlants/Plant_Clivia` | 8.0% (2/25) | 数值 | 0.07 |
| `wildPlants/Plant_Dandelion` | 28.0% (7/25) | 数值 | 0.1 / 0.3 / 0.5 |
| `wildPlants/Plant_Fireweed` | 8.0% (2/25) | 数值 | 0.1 / 9.0 |
| `wildPlants/Plant_Grass` | 36.0% (9/25) | 数值 | 3.0 / 3.6 / 5.0 |
| `wildPlants/Plant_GrayGrass` | 44.0% (11/25) | 数值 | 2 / 3 / 5 |
| `wildPlants/Plant_HealrootWild` | 28.0% (7/25) | 数值 | 0.05 / 0.16 |
| `wildPlants/Plant_LilyPad` | 24.0% (6/25) | 数值 | 0.1 / 0.2 |
| `wildPlants/Plant_Lotus` | 8.0% (2/25) | 数值 | 0.1 |
| `wildPlants/Plant_MagmaCactus` | 4.0% (1/25) | 数值 | 1.0 |
| `wildPlants/Plant_Moss` | 16.0% (4/25) | 数值 | 0.5 / 4.0 |
| `wildPlants/Plant_Nightgrass` | 4.0% (1/25) | 数值 | 12.0 |
| `wildPlants/Plant_NightRafflesia` | 4.0% (1/25) | 数值 | 0.01 |
| `wildPlants/Plant_PebbleCactus` | 16.0% (4/25) | 数值 | 0.6 / 1 |
| `wildPlants/Plant_PincushionCactus` | 12.0% (3/25) | 数值 | 0.2 / 0.6 / 1 |
| `wildPlants/Plant_Psilocap` | 4.0% (1/25) | 数值 | 0.01 |
| `wildPlants/Plant_Rafflesia` | 8.0% (2/25) | 数值 | 0.0008 |
| `wildPlants/Plant_RatPalm` | 8.0% (2/25) | 数值 | 0.3 / 1.5 |
| `wildPlants/Plant_Reeds` | 44.0% (11/25) | 数值 | 1 / 1.2 |
| `wildPlants/Plant_Ripthorn` | 16.0% (4/25) | 数值 | 0.8 / 4 |
| `wildPlants/Plant_SaguaroCactus` | 12.0% (3/25) | 数值 | 0.26 / 1 / 1.0 |
| `wildPlants/Plant_ShrubLow` | 8.0% (2/25) | 数值 | 2.0 |
| `wildPlants/Plant_TallGrass` | 20.0% (5/25) | 数值 | 2.0 / 2.4 / 3.2 |
| `wildPlants/Plant_Thornvine` | 4.0% (1/25) | 数值 | 8.0 |
| `wildPlants/Plant_Timbershroom` | 4.0% (1/25) | 数值 | 0.1 |
| `wildPlants/Plant_TreeBamboo` | 4.0% (1/25) | 数值 | 0.3 |
| `wildPlants/Plant_TreeBirch` | 8.0% (2/25) | 数值 | 0.08 / 1.5 |
| `wildPlants/Plant_TreeCecropia` | 4.0% (1/25) | 数值 | 0.3 |
| `wildPlants/Plant_TreeCypress` | 8.0% (2/25) | 数值 | 1.0 / 1.72 |
| `wildPlants/Plant_TreeDrago` | 12.0% (3/25) | 数值 | 0.2 / 0.20 / 0.45 |
| `wildPlants/Plant_TreeGrayPine` | 12.0% (3/25) | 数值 | 0.08 / 4 |
| `wildPlants/Plant_TreeMaple` | 12.0% (3/25) | 数值 | 0.6 / 1.0 / 1.72 |
| `wildPlants/Plant_TreeOak` | 8.0% (2/25) | 数值 | 0.02 / 0.5 |
| `wildPlants/Plant_TreePalm` | 4.0% (1/25) | 数值 | 0.3 |
| `wildPlants/Plant_TreePine` | 12.0% (3/25) | 数值 | 0.08 / 5.0 |
| `wildPlants/Plant_TreePoplar` | 12.0% (3/25) | 数值 | 0.05 / 0.5 / 1.2 |
| `wildPlants/Plant_TreeSnagroot` | 4.0% (1/25) | 数值 | 0.4 |
| `wildPlants/Plant_TreeTeak` | 4.0% (1/25) | 数值 | 0.2 |
| `wildPlants/Plant_TreeWillow` | 12.0% (3/25) | 数值 | 1.0 / 1.2 / 1.72 |
| `wildPlants/Plant_Willowgill` | 4.0% (1/25) | 数值 | 0.2 |
| `wildPlants/Plant_Witchwood` | 12.0% (3/25) | 数值 | 0.5 / 1.0 |
| `wildPlants/Plant_YellowGrass` | 8.0% (2/25) | 数值 | 2.0 / 9.0 |
| `wildPlants/Plant_YellowTallGrass` | 4.0% (1/25) | 数值 | 9.0 |
| `wildPlantsAreCavePlants` | 4.0% (1/25) | 布尔 | true |
| `wildPlantsCareAboutLocalFertility` | 8.0% (2/25) | 布尔 | false |
| `workerClass` | 80.0% (20/25) | 文本 | BiomeWorker_BorealForest / BiomeWorker_ColdBog / BiomeWorker_IceSheet |

## 四、原版 defName 一览（共 25 个，列出前 60）

```text
`Orbit`                           `Undercave`                       `MetalHell`                       `Ocean`                         
`Lake`                            `Space`                           `Underground`                     `Labyrinth`                     
`IceSheet`                        `SeaIce`                          `ExtremeDesert`                   `Desert`                        
`Scarlands`                       `Grasslands`                      `AridShrubland`                   `Tundra`                        
`LavaField`                       `GlacialPlain`                    `BorealForest`                    `TropicalRainforest`            
`TemperateForest`                 `TemperateSwamp`                  `Glowforest`                      `ColdBog`                       
`TropicalSwamp`                 
```
