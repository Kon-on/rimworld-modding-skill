# GenStepDef

- **所属线**：世界线
- **原版实例数**：170
- **字段路径数**：319
- **资料片**：Anomaly、Biotech、Core、Ideology、Odyssey、Royalty
- **原版出处**：`Royalty/Defs/ThingDefs_Buildings/Buildings_ConditionCausers.xml`、`Odyssey/Defs/Sites/GravcoreLocations.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<GenStepDef ParentName="ConditionCauserGenStepBase">
    <defName>SunBlocker</defName>
    <linkWithSite>SunBlocker</linkWithSite>
  </GenStepDef>

  
```

> 来自 `Royalty/Defs/ThingDefs_Buildings/Buildings_ConditionCausers.xml`，defName = `SunBlocker`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：HarbingerTrees / Labyrinth / MetalHell
genStep                                        [容器]
order                                          [数值]  例：10 / 1100 / 1600
```

## 三、全量字段表（319 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 98.2% (167/170) | 文本 | HarbingerTrees / Labyrinth / MetalHell |
| `genStep` | 95.3% (162/170) | 容器 |  |
| `genStep/allowFoggedPositions` | 1.2% (2/170) | 布尔 | false |
| `genStep/allowGeneratingFarms` | 2.4% (4/170) | 布尔 | false |
| `genStep/allowGeneratingThronerooms` | 2.4% (4/170) | 布尔 | false |
| `genStep/allowInWaterBiome` | 7.1% (12/170) | 布尔 | false |
| `genStep/allowMechanoidDatacoreReadOrLost` | 0.6% (1/170) | 布尔 | false |
| `genStep/allowRoofed` | 5.3% (9/170) | 布尔 | false |
| `genStep/archeanTreeChance` | 1.8% (3/170) | 数值 | 0.25 |
| `genStep/attackWhenPlayerBecameEnemy` | 0.6% (1/170) | 布尔 | true |
| `genStep/bloodFrequency` | 0.6% (1/170) | 数值 | 0 |
| `genStep/bloodThreshold` | 0.6% (1/170) | 数值 | 0 |
| `genStep/canBeOnEdge` | 1.2% (2/170) | 布尔 | true |
| `genStep/cannonDef` | 0.6% (1/170) | 文本 | GaussCannon |
| `genStep/centerPrefabs` | 0.6% (1/170) | 容器 |  |
| `genStep/centerPrefabs/OrbitalRelay_Center_1` | 0.6% (1/170) | 容器 |  |
| `genStep/clearSpaceSize` | 1.2% (2/170) | 数值 | 30 |
| `genStep/clearSurroundingArea` | 0.6% (1/170) | 布尔 | true |
| `genStep/count` | 10.0% (17/170) | 数值 | 1 / 5 |
| `genStep/countPer10kCellsRange` | 15.9% (27/170) | 数值/文本 | 0.2~0.4 / 0.7~1 / 0~3 |
| `genStep/countPer10kCellsRange/max` | 0.6% (1/170) | 数值 | 0.25 |
| `genStep/countPer10kCellsRange/min` | 0.6% (1/170) | 数值 | 0.12 |
| `genStep/createUsedRect` | 2.9% (5/170) | 布尔 | true |
| `genStep/densityByDistance` | 0.6% (1/170) | 容器 |  |
| `genStep/densityByDistance/points` | 0.6% (1/170) | 容器 |  |
| `genStep/densityByDistance/points/li` | 2.9% (5/170) | 文本 | (0, 0) / (10, 0.85) / (15, 0.15) |
| `genStep/destroyChanceExp` | 0.6% (1/170) | 数值 | 3 |
| `genStep/exteriorPrefabs` | 1.2% (2/170) | 容器 |  |
| `genStep/exteriorPrefabs/BaricadeTurret` | 1.2% (2/170) | 文本 | 2~5 |
| `genStep/exteriorPrefabs/CrashedShuttle` | 1.2% (2/170) | 文本 | 0~1 |
| `genStep/extraNoBuildEdgeDist` | 1.2% (2/170) | 数值 | 4 |
| `genStep/extraRangeToRectOfInterest` | 0.6% (1/170) | 数值 | 3 |
| `genStep/factionDef` | 4.7% (8/170) | 文本 | AncientsHostile / Mechanoid / Salvagers |
| `genStep/factor` | 0.6% (1/170) | 数值 | 0.93 |
| `genStep/fallbackValidators` | 1.2% (2/170) | 容器 |  |
| `genStep/fallbackValidators/li` | 1.2% (2/170) | 容器 |  |
| `genStep/fallbackValidators/li/affordance` | 1.2% (2/170) | 文本 | Heavy / Light |
| `genStep/fallbackValidators/li/radius` | 1.2% (2/170) | 数值 | 3 / 5 |
| `genStep/filthChance` | 0.6% (1/170) | 数值 | 0.4 |
| `genStep/filthDef` | 0.6% (1/170) | 文本 | Filth_MachineBits |
| `genStep/filthExpandBy` | 0.6% (1/170) | 数值 | 1 |
| `genStep/fleshFrequency` | 1.2% (2/170) | 数值 | 0.07 / 0.15 |
| `genStep/fleshmassCanReplaceBuildings` | 0.6% (1/170) | 布尔 | true |
| `genStep/fleshmassFalloffRadius` | 0.6% (1/170) | 数值 | 20 |
| `genStep/fleshTerrainThreshold` | 0.6% (1/170) | 数值 | 0.35 |
| `genStep/fleshThreshold` | 1.2% (2/170) | 数值 | 0.2 / 0.4 |
| `genStep/floraToScatter` | 0.6% (1/170) | 容器 |  |
| `genStep/floraToScatter/Agarilux` | 0.6% (1/170) | 数值 | 1.0 |
| `genStep/floraToScatter/Bryolux` | 0.6% (1/170) | 数值 | 0.1 |
| `genStep/floraToScatter/Plant_Nightgrass` | 0.6% (1/170) | 数值 | 2.0 |
| `genStep/fogOfWarColor` | 1.2% (2/170) | 文本 | (52,55,45) |
| `genStep/forceAtLeastOneShard` | 0.6% (1/170) | 布尔 | true |
| `genStep/forceNoConditionCauser` | 0.6% (1/170) | 布尔 | true |
| `genStep/generateLoot` | 2.4% (4/170) | 布尔 | false |
| `genStep/generatePawns` | 1.2% (2/170) | 布尔 | false |
| `genStep/groups` | 8.2% (14/170) | 容器 |  |
| `genStep/groups/Exterior_AncientContainerForklift` | 0.6% (1/170) | 容器 |  |
| `genStep/groups/Exterior_AncientContainerForklift/filthChance` | 0.6% (1/170) | 数值 | 0.4 |
| `genStep/groups/Exterior_AncientContainerForklift/filthDef` | 0.6% (1/170) | 文本 | Filth_MachineBits |
| `genStep/groups/Exterior_AncientContainerForklift/filthExpandBy` | 0.6% (1/170) | 数值 | 1 |
| `genStep/groups/Exterior_AncientContainerForklift/indoorRuin` | 0.6% (1/170) | 布尔 | false |
| `genStep/groups/Exterior_AncientContainerForklift/max` | 0.6% (1/170) | 数值 | 1 |
| `genStep/groups/Exterior_AncientContainerForklift/weight` | 0.6% (1/170) | 数值 | 1.0 |
| `genStep/groups/Exterior_AncientRoad_Long` | 0.6% (1/170) | 容器 |  |
| `genStep/groups/Exterior_AncientRoad_Long/filthChance` | 0.6% (1/170) | 数值 | 0.4 |
| `genStep/groups/Exterior_AncientRoad_Long/filthDef` | 0.6% (1/170) | 文本 | Filth_RubbleRock |
| `genStep/groups/Exterior_AncientRoad_Long/filthExpandBy` | 0.6% (1/170) | 数值 | 1 |
| `genStep/groups/Exterior_AncientRoad_Long/indoorRuin` | 0.6% (1/170) | 布尔 | false |
| `genStep/groups/Exterior_AncientRoad_Long/max` | 0.6% (1/170) | 数值 | 1 |
| `genStep/groups/Exterior_AncientRoad_Long/weight` | 0.6% (1/170) | 数值 | 2.0 |
| `genStep/groups/Exterior_AncientRoad_Short` | 0.6% (1/170) | 容器 |  |
| `genStep/groups/Exterior_AncientRoad_Short/filthChance` | 0.6% (1/170) | 数值 | 0.4 |
| `genStep/groups/Exterior_AncientRoad_Short/filthDef` | 0.6% (1/170) | 文本 | Filth_RubbleRock |
| `genStep/groups/Exterior_AncientRoad_Short/filthExpandBy` | 0.6% (1/170) | 数值 | 1 |
| `genStep/groups/Exterior_AncientRoad_Short/indoorRuin` | 0.6% (1/170) | 布尔 | false |
| `genStep/groups/Exterior_AncientRoad_Short/max` | 0.6% (1/170) | 数值 | 1 |
| `genStep/groups/Exterior_AncientRoad_Short/weight` | 0.6% (1/170) | 数值 | 1.0 |
| `genStep/groups/Exterior_ContainerSite` | 0.6% (1/170) | 容器 |  |
| `genStep/groups/Exterior_ContainerSite/filthChance` | 0.6% (1/170) | 数值 | 0.4 |
| `genStep/groups/Exterior_ContainerSite/filthDef` | 0.6% (1/170) | 文本 | Filth_MachineBits |
| `genStep/groups/Exterior_ContainerSite/filthExpandBy` | 0.6% (1/170) | 数值 | 1 |
| `genStep/groups/Exterior_ContainerSite/indoorRuin` | 0.6% (1/170) | 布尔 | false |
| `genStep/groups/Exterior_ContainerSite/max` | 0.6% (1/170) | 数值 | 1 |
| `genStep/groups/Exterior_ContainerSite/weight` | 0.6% (1/170) | 数值 | 1.0 |
| `genStep/groups/Exterior_CrashedCrane` | 0.6% (1/170) | 容器 |  |
| `genStep/groups/Exterior_CrashedCrane/filthChance` | 0.6% (1/170) | 数值 | 0.4 |
| `genStep/groups/Exterior_CrashedCrane/filthDef` | 0.6% (1/170) | 文本 | Filth_MachineBits |
| `genStep/groups/Exterior_CrashedCrane/filthExpandBy` | 0.6% (1/170) | 数值 | 1 |
| `genStep/groups/Exterior_CrashedCrane/indoorRuin` | 0.6% (1/170) | 布尔 | false |
| `genStep/groups/Exterior_CrashedCrane/max` | 0.6% (1/170) | 数值 | 1 |
| `genStep/groups/Exterior_CrashedCrane/weight` | 0.6% (1/170) | 数值 | 0.5 |
| `genStep/groups/Exterior_FourSmallBuildings` | 0.6% (1/170) | 容器 |  |
| `genStep/groups/Exterior_FourSmallBuildings/filthChance` | 0.6% (1/170) | 数值 | 0.4 |
| `genStep/groups/Exterior_FourSmallBuildings/filthDef` | 0.6% (1/170) | 文本 | Filth_MachineBits |
| `genStep/groups/Exterior_FourSmallBuildings/filthExpandBy` | 0.6% (1/170) | 数值 | 1 |
| `genStep/groups/Exterior_FourSmallBuildings/indoorRuin` | 0.6% (1/170) | 布尔 | false |
| `genStep/groups/Exterior_FourSmallBuildings/max` | 0.6% (1/170) | 数值 | 3 |
| `genStep/groups/Exterior_FourSmallBuildings/weight` | 0.6% (1/170) | 数值 | 0.5 |
| `genStep/groups/Exterior_MilitaryBlockade` | 0.6% (1/170) | 容器 |  |
| `genStep/groups/Exterior_MilitaryBlockade/filthChance` | 0.6% (1/170) | 数值 | 0.4 |
| `genStep/groups/Exterior_MilitaryBlockade/filthDef` | 0.6% (1/170) | 文本 | Filth_MachineBits |
| `genStep/groups/Exterior_MilitaryBlockade/filthExpandBy` | 0.6% (1/170) | 数值 | 1 |
| `genStep/groups/Exterior_MilitaryBlockade/indoorRuin` | 0.6% (1/170) | 布尔 | false |
| `genStep/groups/Exterior_MilitaryBlockade/max` | 0.6% (1/170) | 数值 | 4 |
| `genStep/groups/Exterior_MilitaryBlockade/weight` | 0.6% (1/170) | 数值 | 1.0 |
| `genStep/groups/li` | 18.2% (31/170) | 容器 |  |
| `genStep/groups/li/clusterRectRadius` | 18.2% (31/170) | 数值/文本 | 2~3 / 3~5 / 4~5 |
| `genStep/groups/li/coveredCellsPer10Cells` | 17.6% (30/170) | 文本 | 0.25~0.5 / 0.2~0.4 / 0.5~1.5 |
| `genStep/groups/li/filthChance` | 15.3% (26/170) | 数值 | 0.05 / 0.2 / 0.3 |
| `genStep/groups/li/filthDef` | 15.3% (26/170) | 文本 | Filth_MachineBits / Filth_OilSmear |
| `genStep/groups/li/filthExpandBy` | 15.3% (26/170) | 数值 | 1 |
| `genStep/groups/li/indoorRuin` | 14.1% (24/170) | 布尔 | false / true |
| `genStep/groups/li/spawnAtCenter` | 1.8% (3/170) | 文本 | AncientMechDropBeacon / Filth_BlastMark / ShipChunk_Mech |
| `genStep/groups/li/spawnAtCenterFilthDef` | 0.6% (1/170) | 文本 | Filth_MachineBits |
| `genStep/groups/li/spawnForbidden` | 0.6% (1/170) | 布尔 | true |
| `genStep/groups/li/stackSizeRange` | 0.6% (1/170) | 文本 | 5~10 |
| `genStep/groups/li/things` | 17.6% (30/170) | 容器 |  |
| `genStep/groups/li/things/AncientAirConditioner` | 1.2% (2/170) | 数值 | 0.1 / 0.2 |
| `genStep/groups/li/things/AncientAmmoStack` | 0.6% (1/170) | 数值 | 0.3 |
| `genStep/groups/li/things/AncientAPC` | 0.6% (1/170) | 数值 | 0.3 |
| `genStep/groups/li/things/AncientATM` | 0.6% (1/170) | 数值 | 0.1 |
| `genStep/groups/li/things/AncientBandNode` | 1.2% (2/170) | 数值 | 0.6 / 1 |
| `genStep/groups/li/things/AncientBarrel` | 1.2% (2/170) | 数值 | 0.2 / 0.3 |
| `genStep/groups/li/things/AncientBed` | 1.2% (2/170) | 数值 | 0.25 |
| `genStep/groups/li/things/AncientChembarrel` | 0.6% (1/170) | 数值 | 0.3 |
| `genStep/groups/li/things/AncientChembarrelPallet` | 1.2% (2/170) | 数值 | 0.0221 / 0.2 |
| `genStep/groups/li/things/AncientChemtruck` | 0.6% (1/170) | 数值 | 0.2 |
| `genStep/groups/li/things/AncientCraneBase` | 0.6% (1/170) | 数值 | 0.1 |
| `genStep/groups/li/things/AncientCraneColumn` | 0.6% (1/170) | 数值 | 1 |
| `genStep/groups/li/things/AncientCrate` | 1.8% (3/170) | 数值 | 0.0166 / 0.0221 / 0.0833 |
| `genStep/groups/li/things/AncientCratePallet` | 1.2% (2/170) | 数值 | 0.0221 / 0.1 |
| `genStep/groups/li/things/AncientDropshipEngine` | 0.6% (1/170) | 数值 | 0.2 |
| `genStep/groups/li/things/AncientGenerator` | 0.6% (1/170) | 数值 | 0.2 |
| `genStep/groups/li/things/AncientGiantWheel` | 0.6% (1/170) | 数值 | 1 |
| `genStep/groups/li/things/AncientIndustrialShelf` | 1.2% (2/170) | 数值 | 0.25 / 0.3 |
| `genStep/groups/li/things/AncientIndustrialTruck` | 1.2% (2/170) | 数值 | 0.05 / 0.2 |
| `genStep/groups/li/things/AncientJetEngine` | 0.6% (1/170) | 数值 | 0.2 |
| `genStep/groups/li/things/AncientKitchenSink` | 1.2% (2/170) | 数值 | 0.1 / 0.2 |
| `genStep/groups/li/things/AncientLamp` | 0.6% (1/170) | 数值 | 0.25 |
| `genStep/groups/li/things/AncientLargeContainer` | 1.2% (2/170) | 数值 | 0.1 / 0.15 |
| `genStep/groups/li/things/AncientLargeCrate` | 1.8% (3/170) | 数值 | 0.0166 / 0.0221 / 0.0833 |
| `genStep/groups/li/things/AncientLargeRustedEngineBlock` | 0.6% (1/170) | 数值 | 0.3 |
| `genStep/groups/li/things/AncientLockerBank` | 0.6% (1/170) | 数值 | 0.25 |
| `genStep/groups/li/things/AncientLongCrate` | 1.8% (3/170) | 数值 | 0.0166 / 0.0221 / 0.0833 |
| `genStep/groups/li/things/AncientMediumContainer` | 1.2% (2/170) | 数值 | 0.15 / 0.2 |
| `genStep/groups/li/things/AncientMegaCannonBarrel` | 0.6% (1/170) | 数值 | 0.3 |
| `genStep/groups/li/things/AncientMegaCannonTripod` | 0.6% (1/170) | 数值 | 0.1 |
| `genStep/groups/li/things/AncientMetalCrate` | 2.4% (4/170) | 数值 | 0.0221 / 0.0833 / 0.2 |
| `genStep/groups/li/things/AncientMicrowave` | 0.6% (1/170) | 数值 | 0.1 |
| `genStep/groups/li/things/AncientMilitaryCrate` | 3.5% (6/170) | 数值 | 0.0166 / 0.0221 / 0.0833 |
| `genStep/groups/li/things/AncientMilitaryGeneratorSmall` | 0.6% (1/170) | 数值 | 0.1 |
| `genStep/groups/li/things/AncientMiniWarwalkerRemains` | 0.6% (1/170) | 数值 | 0.2 |
| `genStep/groups/li/things/AncientOpenContainer` | 1.8% (3/170) | 数值 | 0.1 / 0.3 / 0.5 |
| `genStep/groups/li/things/AncientOperatingTable` | 0.6% (1/170) | 数值 | 0.3 |
| `genStep/groups/li/things/AncientOven` | 0.6% (1/170) | 数值 | 0.1 |
| `genStep/groups/li/things/AncientPipe` | 0.6% (1/170) | 数值 | 0.2 |
| `genStep/groups/li/things/AncientPipes` | 1.2% (2/170) | 数值 | 0.1 |
| `genStep/groups/li/things/AncientPlantPot` | 0.6% (1/170) | 数值 | 0.2 |
| `genStep/groups/li/things/AncientPodCar` | 0.6% (1/170) | 数值 | 0.2 |
| `genStep/groups/li/things/AncientPostbox` | 0.6% (1/170) | 数值 | 0.1 |
| `genStep/groups/li/things/AncientRefrigerator` | 1.2% (2/170) | 数值 | 0.1 / 0.3 |
| `genStep/groups/li/things/AncientRustedCar` | 0.6% (1/170) | 数值 | 0.2 |
| `genStep/groups/li/things/AncientRustedCarFrame` | 0.6% (1/170) | 数值 | 0.2 |
| `genStep/groups/li/things/AncientRustedDropship` | 0.6% (1/170) | 数值 | 0.2 |
| `genStep/groups/li/things/AncientRustedEngineBlock` | 0.6% (1/170) | 数值 | 0.2 |
| `genStep/groups/li/things/AncientRustedJeep` | 0.6% (1/170) | 数值 | 0.2 |
| `genStep/groups/li/things/AncientSecurityTurret` | 0.6% (1/170) | 数值 | 0.3 |
| `genStep/groups/li/things/AncientShoppingCart` | 0.6% (1/170) | 数值 | 0.5 |
| `genStep/groups/li/things/AncientSmallContainer` | 1.2% (2/170) | 数值 | 0.1 / 0.5 |
| `genStep/groups/li/things/AncientSmallCrate` | 3.5% (6/170) | 数值 | 0.0221 / 0.1 / 0.2 |
| `genStep/groups/li/things/AncientSpacerCrate` | 2.4% (4/170) | 数值 | 0.0166 / 0.0221 / 0.0833 |
| `genStep/groups/li/things/AncientStorageCylinder` | 1.2% (2/170) | 数值 | 0.2 / 0.3 |
| `genStep/groups/li/things/AncientStove` | 0.6% (1/170) | 数值 | 0.1 |
| `genStep/groups/li/things/AncientTableStoveElectric` | 1.2% (2/170) | 数值 | 0.1 |
| `genStep/groups/li/things/AncientTableTailorElectric` | 0.6% (1/170) | 数值 | 0.1 |
| `genStep/groups/li/things/AncientTableTailorHand` | 0.6% (1/170) | 数值 | 0.1 |
| `genStep/groups/li/things/AncientTank` | 0.6% (1/170) | 数值 | 0.2 |
| `genStep/groups/li/things/AncientTankTrap` | 0.6% (1/170) | 数值 | 0.3 |
| `genStep/groups/li/things/AncientToilet` | 1.2% (2/170) | 数值 | 0.1 |
| `genStep/groups/li/things/AncientToxifierGenerator` | 1.2% (2/170) | 数值 | 0.4 / 1 |
| `genStep/groups/li/things/AncientTunnelerClaw` | 2.4% (4/170) | 数值 | 0.2 / 0.4 |
| `genStep/groups/li/things/AncientVendingMachine` | 0.6% (1/170) | 数值 | 0.1 |
| `genStep/groups/li/things/AncientWarspiderRemains` | 0.6% (1/170) | 数值 | 0.2 |
| `genStep/groups/li/things/AncientWarwalkerClaw` | 0.6% (1/170) | 数值 | 0.3 |
| `genStep/groups/li/things/AncientWarwalkerFoot` | 0.6% (1/170) | 数值 | 0.3 |
| `genStep/groups/li/things/AncientWarwalkerLeg` | 0.6% (1/170) | 数值 | 0.3 |
| `genStep/groups/li/things/AncientWarwalkerShell` | 0.6% (1/170) | 数值 | 0.2 |
| `genStep/groups/li/things/AncientWarwalkerTorso` | 0.6% (1/170) | 数值 | 0.2 |
| `genStep/groups/li/things/AncientWashingMachine` | 0.6% (1/170) | 数值 | 0.1 |
| `genStep/groups/li/things/AncientWheel` | 1.8% (3/170) | 数值 | 0.1 / 0.3 / 0.5 |
| `genStep/groups/li/things/AncientWindTurbineBody` | 0.6% (1/170) | 数值 | 0.05 |
| `genStep/groups/li/things/AncientWoodenCrate` | 1.8% (3/170) | 数值 | 0.0221 / 0.3 |
| `genStep/groups/li/things/ChunkMechanoidSlag` | 2.9% (5/170) | 数值 | 0.8 / 1 |
| `genStep/groups/li/things/Filth_OilSmear` | 0.6% (1/170) | 数值 | 1 |
| `genStep/groups/li/things/Fleshbulb` | 1.2% (2/170) | 数值 | 1 |
| `genStep/groups/li/things/GlowPod` | 0.6% (1/170) | 数值 | 1 |
| `genStep/groups/li/things/GravlitePanel` | 0.6% (1/170) | 数值 | 0.2 |
| `genStep/groups/li/weight` | 0.6% (1/170) | 数值 | 1 |
| `genStep/guardsCountRange` | 0.6% (1/170) | 容器 |  |
| `genStep/guardsCountRange/max` | 0.6% (1/170) | 数值 | 1 |
| `genStep/guardsCountRange/min` | 0.6% (1/170) | 数值 | 1 |
| `genStep/ignoreMaxIfGravship` | 0.6% (1/170) | 布尔 | true |
| `genStep/ignoreUsedRects` | 1.2% (2/170) | 布尔 | true |
| `genStep/isJunk` | 5.9% (10/170) | 布尔 | true |
| `genStep/layout` | 0.6% (1/170) | 容器 |  |
| `genStep/layout/li` | 3.5% (6/170) | 容器 |  |
| `genStep/layout/li/filthDef` | 3.5% (6/170) | 文本 | Filth_MachineBits |
| `genStep/layout/li/filthExpandBy` | 3.5% (6/170) | 数值 | 1 |
| `genStep/layout/li/offset` | 2.9% (5/170) | 文本 | (-1, 0, 2) / (-3, 0, 1) / (-4, 0, 0) |
| `genStep/layout/li/rotation` | 0.6% (1/170) | 文本 | West |
| `genStep/layout/li/thing` | 3.5% (6/170) | 文本 | AncientExostriderCannon / AncientExostriderHead / AncientExostriderLeg |
| `genStep/layoutDef` | 5.3% (9/170) | 文本 | AncientRuins_Scarlands / AncientRuins_Special / Opportunity_AbandonedPlatform_Enterable |
| `genStep/layouts` | 0.6% (1/170) | 容器 |  |
| `genStep/layouts/Opportunity_OrbitalWreck` | 0.6% (1/170) | 容器 |  |
| `genStep/letterDesc` | 0.6% (1/170) | 文本 | The orbital wreck contains a number of scavengers. Be prepared for their assault |
| `genStep/letterLabel` | 0.6% (1/170) | 文本 | Hostile salvagers |
| `genStep/maxMineableValue` | 0.6% (1/170) | 数值 | 0 |
| `genStep/minDistToPlayerStartPct` | 1.2% (2/170) | 数值 | 0.166667 / 0.333 |
| `genStep/mineableCounts` | 1.8% (3/170) | 容器 |  |
| `genStep/mineableCounts/MineableComponentsIndustrial` | 1.2% (2/170) | 文本 | 65~85 |
| `genStep/mineableCounts/MineableGold` | 1.8% (3/170) | 文本 | 14~22 / 33~42 |
| `genStep/mineableCounts/MineableJade` | 1.2% (2/170) | 文本 | 20~35 |
| `genStep/mineableCounts/MineablePlasteel` | 1.8% (3/170) | 文本 | 12~15 / 35~48 |
| `genStep/mineableCounts/MineableSilver` | 1.2% (2/170) | 文本 | 50~70 |
| `genStep/mineableCounts/MineableSteel` | 1.2% (2/170) | 文本 | 80~110 |
| `genStep/mineableCounts/MineableUranium` | 1.8% (3/170) | 文本 | 15~25 / 52~72 |
| `genStep/mineables` | 0.6% (1/170) | 容器 |  |
| `genStep/mineables/li` | 4.1% (7/170) | 文本 | MineableGold / MineablePlasteel / MineableSilver |
| `genStep/minEdgeDistPct` | 1.2% (2/170) | 数值 | 0.166667 |
| `genStep/minPollution` | 0.6% (1/170) | 数值 | 0.25 |
| `genStep/minProximityToSameTree` | 1.2% (2/170) | 数值 | 16 |
| `genStep/minSpacing` | 12.3% (21/170) | 数值 | 20 / 25 / 50 |
| `genStep/mustBeStandable` | 0.6% (1/170) | 布尔 | true |
| `genStep/nearMapCenter` | 7.6% (13/170) | 布尔 | true |
| `genStep/noiseOctaves` | 0.6% (1/170) | 数值 | 2 |
| `genStep/numChunks` | 1.8% (3/170) | 文本 | 4~6 / 5~8 |
| `genStep/numFleshSacksFromPoints` | 1.2% (2/170) | 容器 |  |
| `genStep/numFleshSacksFromPoints/points` | 1.2% (2/170) | 容器 |  |
| `genStep/numFleshSacksFromPoints/points/li` | 4.7% (8/170) | 文本 | (0, 3) / (1000, 7) / (500, 5) |
| `genStep/onlyOnStartingMap` | 1.2% (2/170) | 布尔 | true |
| `genStep/orbitalDebrisDef` | 4.1% (7/170) | 文本 | Manmade / Mechanoid |
| `genStep/overrideBlotchesPer10kCells` | 0.6% (1/170) | 数值 | 10 |
| `genStep/pawnGroupKindDef` | 1.2% (2/170) | 文本 | Combat / Settlement_RangedOnly |
| `genStep/platformTerrain` | 3.5% (6/170) | 文本 | MechanoidPlatform / OrbitalPlatform |
| `genStep/pollutionExtreme` | 1.2% (2/170) | 数值 | 3 |
| `genStep/pollutionLight` | 1.2% (2/170) | 数值 | 0 |
| `genStep/pollutionModerate` | 1.2% (2/170) | 数值 | 1 |
| `genStep/pollutionNone` | 1.2% (2/170) | 数值 | 0 |
| `genStep/postProcessSettlementParams` | 0.6% (1/170) | 容器 |  |
| `genStep/postProcessSettlementParams/clearBuildingFaction` | 0.6% (1/170) | 布尔 | true |
| `genStep/prefabs` | 1.2% (2/170) | 容器 |  |
| `genStep/prefabs/AncientAntenna_Rows` | 0.6% (1/170) | 数值 | 0.5 |
| `genStep/prefabs/AncientTransportPod` | 0.6% (1/170) | 容器 |  |
| `genStep/prefabs/AutoturretBarricade` | 0.6% (1/170) | 容器 |  |
| `genStep/prefabs/Exterior_OrbitalRuinsLargeRectangle` | 0.6% (1/170) | 数值 | 2 |
| `genStep/prefabs/Exterior_OrbitalRuinsRoomWithSteel` | 0.6% (1/170) | 数值 | 0.05 |
| `genStep/prefabs/Exterior_OrbitalRuinsSmallSquare` | 0.6% (1/170) | 数值 | 0.5 |
| `genStep/prefabs/Exterior_OrbitalRuinsSquare` | 0.6% (1/170) | 数值 | 0.05 |
| `genStep/prefabs/Exterior_OrbitalRuinsWall` | 0.6% (1/170) | 容器 |  |
| `genStep/prefabs/Exterior_ShipChunk_Mech` | 0.6% (1/170) | 数值 | 0.5 |
| `genStep/prefabs/SolarArray` | 0.6% (1/170) | 容器 |  |
| `genStep/requiredGravcoreRooms` | 0.6% (1/170) | 数值 | 1 |
| `genStep/requiredWorshippedTerminalRooms` | 0.6% (1/170) | 数值 | 1 |
| `genStep/requiresRoof` | 0.6% (1/170) | 布尔 | true |
| `genStep/requireUnfogged` | 0.6% (1/170) | 布尔 | true |
| `genStep/ruinsChance` | 1.8% (3/170) | 数值 | 0 / 0.1 / 0.5 |
| `genStep/ruinSizeChanceCurve` | 0.6% (1/170) | 容器 |  |
| `genStep/ruinSizeChanceCurve/points` | 0.6% (1/170) | 容器 |  |
| `genStep/ruinSizeChanceCurve/points/li` | 1.8% (3/170) | 文本 | (10, 0) / (6, 0) / (6.001, 4) |
| `genStep/sackClumpSize` | 0.6% (1/170) | 数值 | 15 |
| `genStep/satellitePrefabs` | 0.6% (1/170) | 容器 |  |
| `genStep/satellitePrefabs/OrbitalRelay_Satellite_1` | 0.6% (1/170) | 容器 |  |
| `genStep/satellitePrefabs/OrbitalRelay_Satellite_1/minMaxRange` | 0.6% (1/170) | 文本 | 1~2 |
| `genStep/satellitePrefabs/OrbitalRelay_Satellite_2` | 0.6% (1/170) | 容器 |  |
| `genStep/satellitePrefabs/OrbitalRelay_Satellite_2/minMaxRange` | 0.6% (1/170) | 文本 | 1~1 |
| `genStep/satellitePrefabs/OrbitalRelay_Satellite_3` | 0.6% (1/170) | 容器 |  |
| `genStep/satellitePrefabs/OrbitalRelay_Satellite_3/minMaxRange` | 0.6% (1/170) | 文本 | 1~1 |
| `genStep/satelliteRange` | 0.6% (1/170) | 文本 | 3~5 |
| `genStep/scatterPrefabs` | 0.6% (1/170) | 容器 |  |
| `genStep/scatterPrefabs/OrbitalRelay_Scatter_1` | 0.6% (1/170) | 容器 |  |
| `genStep/scatterPrefabs/OrbitalRelay_Scatter_2` | 0.6% (1/170) | 容器 |  |
| `genStep/scatterPrefabs/OrbitalRelay_Scatter_3` | 0.6% (1/170) | 数值 | 0.5 |
| `genStep/scatterRange` | 0.6% (1/170) | 文本 | 2~3 |
| `genStep/settlementDontGeneratePawns` | 2.4% (4/170) | 布尔 | true |
| `genStep/size` | 0.6% (1/170) | 数值 | 29 |
| `genStep/skipRoofed` | 1.8% (3/170) | 布尔 | true |
| `genStep/spawnSentryDrones` | 2.4% (4/170) | 布尔 | false / true |
| `genStep/spawnSurroundingFleshmass` | 0.6% (1/170) | 布尔 | false |
| `genStep/spotMustBeStandable` | 4.7% (8/170) | 布尔 | true |
| `genStep/symbolName` | 2.4% (4/170) | 文本 | WorkSite_farming / WorkSite_hunting / WorkSite_logging |
| `genStep/temperature` | 2.4% (4/170) | 数值 | 20 |
| `genStep/terrainValidationAllowed` | 0.6% (1/170) | 容器 |  |
| `genStep/terrainValidationAllowed/li` | 0.6% (1/170) | 文本 | NaturalRock |
| `genStep/terrainValidationDisallowed` | 1.2% (2/170) | 容器 |  |
| `genStep/terrainValidationDisallowed/li` | 1.2% (2/170) | 文本 | Road |
| `genStep/terrainValidationRadius` | 1.8% (3/170) | 数值 | 1 / 4 |
| `genStep/thingDef` | 8.2% (14/170) | 文本 | AncientPipelineSection / CraterLarge / CraterMedium |
| `genStep/totalValueRange` | 0.6% (1/170) | 容器 |  |
| `genStep/totalValueRange/max` | 0.6% (1/170) | 数值 | 5000 |
| `genStep/totalValueRange/min` | 0.6% (1/170) | 数值 | 3500 |
| `genStep/treeDef` | 1.8% (3/170) | 文本 | Plant_TreeAnima / Plant_TreeHarbinger / Plant_TreePolux |
| `genStep/trySpawnInRoom` | 0.6% (1/170) | 布尔 | true |
| `genStep/unfogged` | 0.6% (1/170) | 布尔 | true |
| `genStep/useSiteFaction` | 0.6% (1/170) | 布尔 | true |
| `genStep/validators` | 12.3% (21/170) | 容器 |  |
| `genStep/validators/li` | 20.6% (35/170) | 容器 |  |
| `genStep/validators/li/affordance` | 7.6% (13/170) | 文本 | Heavy / Light |
| `genStep/validators/li/radius` | 9.4% (16/170) | 数值 | 1 / 4 / 5 |
| `genStep/validators/li/roofDef` | 0.6% (1/170) | 容器 |  |
| `genStep/validators/li/size` | 1.2% (2/170) | 文本 | (5, 5) / (6, 6) |
| `genStep/validators/li/terrainDef` | 4.7% (8/170) | 文本 | Flesh / InsectSludge / MechanoidPlatform |
| `genStep/warnOnFail` | 2.4% (4/170) | 布尔 | false |
| `genStep/widthRange` | 0.6% (1/170) | 容器 |  |
| `genStep/widthRange/max` | 0.6% (1/170) | 数值 | 4 |
| `genStep/widthRange/min` | 0.6% (1/170) | 数值 | 3 |
| `linkWithSite` | 44.7% (76/170) | 文本 | AmbushEdge / AmbushHidden / AncientComplex_Mechanitor |
| `order` | 91.8% (156/170) | 数值 | 10 / 1100 / 1600 |
| `preventsGenSteps` | 1.8% (3/170) | 容器 |  |
| `preventsGenSteps/li` | 2.9% (5/170) | 文本 | AncientJunkClusters / AncientRuins_Scarlands / FrozenRuins |

## 四、原版 defName 一览（共 170 个，列出前 60）

```text
`SunBlocker`                      `SmokeSpewer`                     `ToxicSpewer`                     `WeatherController`             
`ClimateAdjuster`                 `PsychicDroner`                   `PsychicSuppressor`               `EMIDynamo`                     
`Labyrinth`                       `MetalHell`                       `Dreadmeld`                       `UndercaveInterest`             
`SettlementPower`                 `CaveHives`                       `ElevationFertility`              `MutatorPostElevationFertility` 
`RocksFromGrid`                   `Terrain`                         `MutatorPostTerrain`              `RemoveTinyIslands`             
`Roads`                           `RockChunks`                      `MutatorCriticalStructures`       `MutatorNonCriticalStructures`  
`FindPlayerStartSpot`             `ScenParts`                       `Plants`                          `Snow`                          
`Animals`                         `Fog`                             `MutatorFinal`                    `PlaceCaveExit`                 
`ScatterRoadDebris`               `ScatterCaveDebris`               `AncientUtilityBuilding`          `AncientTurret`                 
`AncientMechs`                    `AncientLandingPad`               `AncientFences`                   `AncientPipelineSection`        
`AncientStockpile`                `ReserveGravshipArea`             `GravshipMarker`                  `Glaciers`                      
`FrozenRuins`                     `InsectLair_Cave`                 `OrbitalMechhive`                 `Space`                         
`AsteroidItemStash`               `FogSpace`                        ``                                `DistressCall_PitBurrows`       
`DistressCall_BurntPatches`       `Pollution`                       `AncientComplex_Mechanitor`       `Underground_RocksFromGrid`     
`AmbushEdge`                      `AmbushHidden`                    `BanditCamp`                      `BanditCampPower`               
```

_余下 110 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
