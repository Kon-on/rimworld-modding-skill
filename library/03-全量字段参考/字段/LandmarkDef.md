# LandmarkDef

- **所属线**：世界线
- **原版实例数**：51
- **字段路径数**：109
- **资料片**：Odyssey
- **原版出处**：`Odyssey/Defs/TileMutators/Landmarks.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<LandmarkDef ParentName="LakeWithIsland">
    <defName>LakeWithIslands</defName>
    <mutatorChances Inherit="False">
      <LakeWithIslands Required="True"/>
    </mutatorChances>
  </LandmarkDef>

  
```

> 来自 `Odyssey/Defs/TileMutators/Landmarks.xml`，defName = `LakeWithIslands`，XML 节点数 4（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
mutatorChances                                 [容器]
```

## 三、全量字段表（109 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `atlasSize` | 62.7% (32/51) | 文本 | (2, 2) |
| `category` | 45.1% (23/51) | 文本 | coastal / lake / mountain |
| `coastRotateMode` | 7.8% (4/51) | 文本 | AwayFromCoast / ToCoast |
| `comboLandmarkMutators` | 27.5% (14/51) | 容器 |  |
| `comboLandmarkMutators/AncientHeatVent` | 7.8% (4/51) | 数值 | 0.02 |
| `comboLandmarkMutators/AncientQuarry` | 5.9% (3/51) | 数值 | 0.02 |
| `comboLandmarkMutators/AncientSmokeVent` | 7.8% (4/51) | 数值 | 0.02 |
| `comboLandmarkMutators/AncientToxVent` | 7.8% (4/51) | 数值 | 0.02 |
| `comboLandmarkMutators/Bay` | 7.8% (4/51) | 数值 | 0.02 / 0.1 / 0.5 |
| `comboLandmarkMutators/Cavern` | 3.9% (2/51) | 数值 | 0.1 |
| `comboLandmarkMutators/Chasm` | 3.9% (2/51) | 数值 | 0.1 |
| `comboLandmarkMutators/HotSprings` | 7.8% (4/51) | 数值 | 0.02 |
| `comboLandmarkMutators/Lake` | 11.8% (6/51) | 数值 | 0.02 |
| `comboLandmarkMutators/LakeWithIsland` | 7.8% (4/51) | 数值 | 0.02 |
| `comboLandmarkMutators/LakeWithIslands` | 11.8% (6/51) | 数值 | 0.02 |
| `comboLandmarkMutators/Oasis` | 2.0% (1/51) | 数值 | 0.1 |
| `comboLandmarkMutators/Plateau` | 2.0% (1/51) | 数值 | 0.02 |
| `comboLandmarkMutators/Pond` | 17.6% (9/51) | 数值 | 0.02 / 0.05 |
| `comboLandmarkMutators/TerraformingScar` | 2.0% (1/51) | 数值 | 0.1 |
| `comboLandmarkMutators/Valley` | 3.9% (2/51) | 数值 | 0.1 |
| `comboLandmarkMutators/Wetland` | 17.6% (9/51) | 数值 | 0.02 |
| `commonality` | 64.7% (33/51) | 数值 | 0.15 / 0.2 / 0.25 |
| `defName` | 88.2% (45/51) | 文本 | Lake / LakeWithIsland / LakeWithIslands |
| `drawAboveRoads` | 11.8% (6/51) | 布尔 | true |
| `drawScale` | 19.6% (10/51) | 数值 | 0.6 / 0.7 / 0.8 |
| `drawType` | 15.7% (8/51) | 文本 | TerrainMask |
| `iconTexturePath` | 66.7% (34/51) | 文本 | World/Landmarks/Lake / World/Landmarks/LakeWithIsland / World/Landmarks/Oasis |
| `label` | 72.5% (37/51) | 文本 | dry lake / lake / oasis |
| `mutatorChances` | 100.0% (51/51) | 容器 |  |
| `mutatorChances/AbandonedColonyOutlander` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/AbandonedColonyTribal` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/AncientChemfuelRefinery` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/AncientGarrison` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/AncientHeatVent` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/AncientInfestedSettlement` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/AncientLaunchSite` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/AncientQuarry` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/AncientRuins` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/AncientRuins_Frozen` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/AncientSmokeVent` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/AncientToxVent` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/AncientUplink` | 62.7% (32/51) | 数值 | 0.02 / 0.15 |
| `mutatorChances/AncientWarehouse` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/AnimalHabitat` | 37.2% (19/51) | 数值 | 0.05 / 0.15 / 0.25 |
| `mutatorChances/AnimalLife_Decreased` | 29.4% (15/51) | 容器/数值 | 0.05 / 0.15 / 0.5 |
| `mutatorChances/AnimalLife_Increased` | 33.3% (17/51) | 数值 | 0.05 / 0.75 |
| `mutatorChances/ArcheanTrees` | 41.2% (21/51) | 数值 | 0.01 |
| `mutatorChances/Archipelago` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/Basin` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/Bay` | 3.9% (2/51) | 容器 |  |
| `mutatorChances/CaveLakes` | 11.8% (6/51) | 数值 | 0.15 |
| `mutatorChances/Cavern` | 3.9% (2/51) | 容器 |  |
| `mutatorChances/Caves` | 2.0% (1/51) | 数值 | 0.4 |
| `mutatorChances/Chasm` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/Cliffs` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/CoastalAtoll` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/CoastalIsland` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/Cove` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/Crevasse` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/DryGround` | 21.6% (11/51) | 数值 | 0.05 / 0.15 |
| `mutatorChances/DryLake` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/Dunes` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/Fertile` | 47.1% (24/51) | 数值 | 0.05 |
| `mutatorChances/Fish_Decreased` | 21.6% (11/51) | 数值 | 0.01 |
| `mutatorChances/Fish_Increased` | 21.6% (11/51) | 数值 | 0.05 |
| `mutatorChances/Fjord` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/FoggyMutator` | 35.3% (18/51) | 数值 | 0.05 / 0.3 |
| `mutatorChances/Harbor` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/Hollow` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/HotSprings` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/Iceberg` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/IceCaves` | 2.0% (1/51) | 数值 | 0.5 |
| `mutatorChances/IceDunes` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/InsectMegahive` | 29.4% (15/51) | 数值 | 0.01 / 0.02 |
| `mutatorChances/Junkyard` | 15.7% (8/51) | 数值 | 0.05 / 0.1 / 0.2 |
| `mutatorChances/Lake` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/LakeWithIsland` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/LakeWithIslands` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/LavaCaves` | 3.9% (2/51) | 数值 | 0.1 |
| `mutatorChances/LavaCrater` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/LavaFlow` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/LavaLake` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/Marshy` | 31.4% (16/51) | 数值 | 0.05 |
| `mutatorChances/MineralRich` | 25.5% (13/51) | 容器/数值 | 0.03 / 0.05 / 0.1 |
| `mutatorChances/MixedBiome` | 33.3% (17/51) | 数值 | 0.5 |
| `mutatorChances/Muddy` | 51.0% (26/51) | 数值 | 0.05 |
| `mutatorChances/Oasis` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/ObsidianDeposits` | 3.9% (2/51) | 数值 | 0.25 |
| `mutatorChances/Peninsula` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/PlantGrove` | 39.2% (20/51) | 数值 | 0.05 / 0.1 / 0.15 |
| `mutatorChances/PlantLife_Increased` | 31.4% (16/51) | 数值 | 0.03 / 0.05 / 0.1 |
| `mutatorChances/Plateau` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/Pollution_Increased` | 41.2% (21/51) | 数值 | 0.01 / 0.02 / 0.05 |
| `mutatorChances/Pond` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/Sandy` | 51.0% (26/51) | 数值 | 0.05 |
| `mutatorChances/SteamGeysers_Increased` | 13.7% (7/51) | 数值 | 0.03 / 0.1 / 0.25 |
| `mutatorChances/Stockpile` | 62.7% (32/51) | 数值 | 0.05 / 0.15 / 0.25 |
| `mutatorChances/SunnyMutator` | 56.9% (29/51) | 数值 | 0.05 / 0.1 / 0.15 |
| `mutatorChances/TerraformingScar` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/ToxicLake` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/Valley` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/WetClimate` | 45.1% (23/51) | 数值 | 0 / 0.05 / 0.1 |
| `mutatorChances/Wetland` | 2.0% (1/51) | 容器 |  |
| `mutatorChances/WildPlants` | 41.2% (21/51) | 数值 | 0.05 / 0.1 |
| `mutatorChances/WildTropicalPlants` | 41.2% (21/51) | 数值 | 0.03 |
| `mutatorChances/WindyMutator` | 45.1% (23/51) | 数值 | 0.05 / 0.15 / 0.25 |
| `nameMaker` | 82.3% (42/51) | 文本 | NamerLandmark_DryLake / NamerLandmark_Lake / NamerLandmark_Oasis |
| `terrainParameters` | 2.0% (1/51) | 容器 |  |
| `terrainParameters/_Blend` | 2.0% (1/51) | 数值 | 0 |

## 四、原版 defName 一览（共 51 个，列出前 60）

```text
`LakeWithIslands`                 `Bay`                             `Cove`                            `LavaLake`                      
`LavaCrater`                      `Lake`                            `LakeWithIsland`                  `AbandonedColonyTribal`         
`AbandonedColonyOutlander`        `Pond`                            `AncientSmokeVent`                `AncientLaunchSite`             
`AncientGarrison`                 `AncientWarehouse`                `AncientChemfuelRefinery`         `AncientInfestedSettlement`     
`AncientToxVent`                  `AncientHeatVent`                 `IceDunes`                        `Dunes`                         
`FrozenRuins`                     `Oasis`                           `Crevasse`                        `DryLake`                       
`Iceberg`                         `LavaFlow`                        ``                                `ToxicLake`                     
``                                `Wetland`                         ``                                `Archipelago`                   
`CoastalIsland`                   `CoastalAtoll`                    `Peninsula`                       `Fjord`                         
``                                `Harbor`                          `Cavern`                          ``                              
`AncientQuarry`                   `TerraformingScar`                `HotSprings`                      `Chasm`                         
`Hollow`                          `Basin`                           `Ruins`                           `Plateau`                       
`Cliffs`                          `Valley`                          ``                              
```
