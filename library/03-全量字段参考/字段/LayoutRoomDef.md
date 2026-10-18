# LayoutRoomDef

- **所属线**：世界线
- **原版实例数**：140
- **字段路径数**：504
- **资料片**：Anomaly、Biotech、Core、Ideology、Odyssey
- **原版出处**：`Anomaly/Defs/LayoutRoomDefs/LayoutRooms_Labyrinth.xml`、`Ideology/Defs/LayoutRoomDefs/LayoutRooms_AncientComplex.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<LayoutRoomDef>
    <defName>LabyrinthEmpty</defName>
  </LayoutRoomDef>

  
```

> 来自 `Anomaly/Defs/LayoutRoomDefs/LayoutRooms_Labyrinth.xml`，defName = `LabyrinthEmpty`，XML 节点数 2（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：LabyrinthEmpty / LabyrinthEndlessPit / LabyrinthFloorEtchings
```

## 三、全量字段表（504 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `canBeInMixedRoom` | 9.3% (13/140) | 布尔 | false / true |
| `canMergeWithAdjacentRoom` | 34.3% (48/140) | 布尔 | true |
| `canRemoveBorderDoors` | 0.7% (1/140) | 布尔 | true |
| `canRemoveBorderWalls` | 0.7% (1/140) | 布尔 | true |
| `defName` | 100.0% (140/140) | 文本 | LabyrinthEmpty / LabyrinthEndlessPit / LabyrinthFloorEtchings |
| `dontDestroyWallsDoors` | 15.7% (22/140) | 布尔 | true |
| `dontPlaceRandomly` | 4.3% (6/140) | 布尔 | true |
| `edgeTerrain` | 10.0% (14/140) | 文本 | AncientTile / MetalTile |
| `fillEdges` | 1.4% (2/140) | 容器 |  |
| `fillEdges/AncientDisplayBank` | 0.7% (1/140) | 容器 |  |
| `fillEdges/AncientDisplayBank/groupCountRange` | 0.7% (1/140) | 文本 | 1~2 |
| `fillEdges/AncientDisplayBank/groupsPerTenEdgeCells` | 0.7% (1/140) | 文本 | 1~3 |
| `fillEdges/AncientLockerBank` | 0.7% (1/140) | 容器 |  |
| `fillEdges/AncientLockerBank/groupCountRange` | 0.7% (1/140) | 文本 | 1~2 |
| `fillEdges/AncientLockerBank/groupsPerTenEdgeCells` | 0.7% (1/140) | 文本 | 1~3 |
| `fillInterior` | 2.1% (3/140) | 容器 |  |
| `fillInterior/AncientBed` | 0.7% (1/140) | 容器 |  |
| `fillInterior/AncientBed/alignWithRect` | 0.7% (1/140) | 布尔 | true |
| `fillInterior/AncientBed/thingsPerHundredCells` | 0.7% (1/140) | 文本 | 2~3 |
| `fillInterior/AncientOperatingTable` | 0.7% (1/140) | 容器 |  |
| `fillInterior/AncientOperatingTable/alignWithRect` | 0.7% (1/140) | 布尔 | true |
| `fillInterior/AncientOperatingTable/thingsPerHundredCells` | 0.7% (1/140) | 文本 | 1~2 |
| `fillInterior/AncientSystemRack` | 0.7% (1/140) | 容器 |  |
| `fillInterior/AncientSystemRack/alignWithRect` | 0.7% (1/140) | 布尔 | true |
| `fillInterior/AncientSystemRack/thingsPerHundredCells` | 0.7% (1/140) | 文本 | 10~20 |
| `floorTypes` | 53.6% (75/140) | 容器 |  |
| `floorTypes/li` | 62.9% (88/140) | 文本 | AncientConcrete / AncientTile / AncientWoodPlankFloor |
| `isValidPlayerSpawnRoom` | 7.9% (11/140) | 布尔 | false |
| `itemsPer100CellsRange` | 0.7% (1/140) | 文本 | 2~4 |
| `minAdjRooms` | 1.4% (2/140) | 数值 | 2 |
| `minSingleRectHeight` | 35.0% (49/140) | 数值 | 10 / 6 / 7 |
| `minSingleRectWidth` | 35.0% (49/140) | 数值 | 10 / 6 / 7 |
| `noRoof` | 2.9% (4/140) | 布尔 | true |
| `parts` | 54.3% (76/140) | 容器 |  |
| `parts/AncientBarricades` | 10.0% (14/140) | 容器 |  |
| `parts/AncientEngine` | 1.4% (2/140) | 容器 |  |
| `parts/AncientWeaponStorage` | 0.7% (1/140) | 容器 |  |
| `parts/Breached` | 0.7% (1/140) | 容器 |  |
| `parts/CenterSpace` | 0.7% (1/140) | 容器 |  |
| `parts/ConnectConduits` | 0.7% (1/140) | 容器 |  |
| `parts/CornerArmoredTurret` | 14.3% (20/140) | 容器/数值 | 0.1 / 0.3 / 0.4 |
| `parts/CornerArmoredTurret/countRange` | 2.1% (3/140) | 文本 | 1~1 / 2~3 / 4~4 |
| `parts/CornerMechPylon` | 5.7% (8/140) | 容器 |  |
| `parts/CornerMechPylon/countRange` | 5.0% (7/140) | 文本 | 0~2 / 1~4 / 2~3 |
| `parts/CornerMiniTurret` | 4.3% (6/140) | 容器/数值 | 0.5 |
| `parts/CornerMiniTurret/countRange` | 0.7% (1/140) | 文本 | 1~2 |
| `parts/Corpse` | 18.6% (26/140) | 容器/数值 | 0.1 / 0.15 / 0.25 |
| `parts/DormantMechCluster` | 7.1% (10/140) | 容器/数值 | 0.5 |
| `parts/DormantMechCluster/threatPointsRange` | 1.4% (2/140) | 文本 | 100~150 / 80~125 |
| `parts/GestationTanks` | 0.7% (1/140) | 容器 |  |
| `parts/Gore` | 1.4% (2/140) | 数值 | 0.75 |
| `parts/HermetricCrate_LowValue` | 1.4% (2/140) | 容器/数值 | 0.75 |
| `parts/HunterDrone` | 24.3% (34/140) | 容器/数值 | 0.15 / 0.2 / 0.3 |
| `parts/HunterDrone/countRange` | 5.7% (8/140) | 数值/文本 | 0~1 / 0~2 / 1 |
| `parts/InsectHive` | 6.4% (9/140) | 容器/数值 | 0.1 / 0.5 |
| `parts/WaspDrone` | 17.1% (24/140) | 数值 | 0.05 / 0.1 / 0.3 |
| `parts/WaspDrone/countRange` | 0.7% (1/140) | 文本 | 1~1 |
| `prefabs` | 58.6% (82/140) | 容器 |  |
| `prefabs/AncientAmmoStack_Cluster` | 0.7% (1/140) | 容器 |  |
| `prefabs/AncientAmmoStack_Cluster/countPerHundredCells` | 0.7% (1/140) | 数值 | 3 |
| `prefabs/AncientAmmoStack_Cluster/minMaxRange` | 0.7% (1/140) | 文本 | 2~5 |
| `prefabs/AncientBandNode_Cluster` | 0.7% (1/140) | 容器 |  |
| `prefabs/AncientBandNode_Cluster/countPerHundredCells` | 0.7% (1/140) | 数值 | 10 |
| `prefabs/AncientBandNode_Cluster/minMaxRange` | 0.7% (1/140) | 文本 | 5~15 |
| `prefabs/AncientBarrel_Cluster` | 3.6% (5/140) | 容器 |  |
| `prefabs/AncientBarrel_Cluster/countPerHundredCells` | 3.6% (5/140) | 数值 | 2 / 5 |
| `prefabs/AncientBarrel_Cluster/minMaxRange` | 3.6% (5/140) | 文本 | 1~5 |
| `prefabs/AncientBasicRecharger_Edge` | 0.7% (1/140) | 容器 |  |
| `prefabs/AncientBasicRecharger_Edge/countPerTenEdgeCells` | 0.7% (1/140) | 数值 | 2 |
| `prefabs/AncientBasicRecharger_Edge/minMaxRange` | 0.7% (1/140) | 文本 | 5~15 |
| `prefabs/AncientBasicRecharger_Rows` | 0.7% (1/140) | 容器 |  |
| `prefabs/AncientBasicRecharger_Rows/countPerHundredCells` | 0.7% (1/140) | 数值 | 3 |
| `prefabs/AncientBasicRecharger_Rows/minMaxRange` | 0.7% (1/140) | 文本 | 1~1 |
| `prefabs/AncientBed_Rows` | 1.4% (2/140) | 容器 |  |
| `prefabs/AncientBed_Rows/countPerHundredCells` | 1.4% (2/140) | 数值 | 3 |
| `prefabs/AncientBed_Rows/minMaxRange` | 1.4% (2/140) | 文本 | 1~1 |
| `prefabs/AncientBedRooms_Edge` | 0.7% (1/140) | 容器 |  |
| `prefabs/AncientBedRooms_Edge/countPerTenEdgeCells` | 0.7% (1/140) | 数值 | 3 |
| `prefabs/AncientBedRooms_Edge/minMaxRange` | 0.7% (1/140) | 文本 | 5~15 |
| `prefabs/AncientCardboardBox_Cluster` | 5.7% (8/140) | 容器 |  |
| `prefabs/AncientCardboardBox_Cluster/countPerHundredCells` | 5.7% (8/140) | 数值 | 1 / 15 / 2 |
| `prefabs/AncientCardboardBox_Cluster/minMaxRange` | 5.7% (8/140) | 文本 | 0~1 / 0~5 / 1~2 |
| `prefabs/AncientChembarrelPallet_Cluster` | 3.6% (5/140) | 容器 |  |
| `prefabs/AncientChembarrelPallet_Cluster/countPerHundredCells` | 3.6% (5/140) | 数值 | 2.5 / 5 |
| `prefabs/AncientChembarrelPallet_Cluster/minMaxRange` | 3.6% (5/140) | 文本 | 0~2 / 1~2 / 1~3 |
| `prefabs/AncientChemfuelCanister_Cluster` | 3.6% (5/140) | 容器 |  |
| `prefabs/AncientChemfuelCanister_Cluster/countPerHundredCells` | 3.6% (5/140) | 数值 | 5 |
| `prefabs/AncientChemfuelCanister_Cluster/minMaxRange` | 3.6% (5/140) | 文本 | 1~1 / 1~2 / 1~3 |
| `prefabs/AncientCratePallet_Cluster` | 6.4% (9/140) | 容器 |  |
| `prefabs/AncientCratePallet_Cluster/countPerHundredCells` | 6.4% (9/140) | 数值 | 1 / 2.5 |
| `prefabs/AncientCratePallet_Cluster/minMaxRange` | 6.4% (9/140) | 文本 | 0~1 / 1~3 |
| `prefabs/AncientCratesWithComponents` | 5.7% (8/140) | 容器 |  |
| `prefabs/AncientCratesWithComponents/countPerHundredCells` | 5.7% (8/140) | 数值 | 1 |
| `prefabs/AncientCratesWithComponents/minMaxRange` | 5.7% (8/140) | 数值/文本 | 0~1 / 1 / 1~1 |
| `prefabs/AncientDestroyedConsole_Cluster` | 1.4% (2/140) | 容器 |  |
| `prefabs/AncientDestroyedConsole_Cluster/countPerHundredCells` | 1.4% (2/140) | 数值 | 1 |
| `prefabs/AncientDestroyedConsole_Cluster/minMaxRange` | 1.4% (2/140) | 文本 | 0~1 / 6~12 |
| `prefabs/AncientDestroyedConsole_Large` | 2.9% (4/140) | 容器 |  |
| `prefabs/AncientDestroyedConsole_Large/countPerTenEdgeCells` | 2.9% (4/140) | 数值 | 5 |
| `prefabs/AncientDestroyedConsole_Large/minMaxRange` | 2.9% (4/140) | 文本 | 1~2 / 2~8 |
| `prefabs/AncientDestroyedConsole_Small` | 3.6% (5/140) | 容器 |  |
| `prefabs/AncientDestroyedConsole_Small/countPerTenEdgeCells` | 3.6% (5/140) | 数值 | 2 |
| `prefabs/AncientDestroyedConsole_Small/minMaxRange` | 3.6% (5/140) | 文本 | 1~2 / 1~5 / 2~8 |
| `prefabs/AncientDestroyedConsole_VerySmall` | 1.4% (2/140) | 容器 |  |
| `prefabs/AncientDestroyedConsole_VerySmall/countPerTenEdgeCells` | 1.4% (2/140) | 数值 | 2 |
| `prefabs/AncientDestroyedConsole_VerySmall/minMaxRange` | 1.4% (2/140) | 文本 | 2~5 / 5~10 |
| `prefabs/AncientDisplayBank_Edge` | 2.9% (4/140) | 容器 |  |
| `prefabs/AncientDisplayBank_Edge/countPerTenEdgeCells` | 2.9% (4/140) | 数值 | 2 / 3 |
| `prefabs/AncientDisplayBank_Edge/minMaxRange` | 2.9% (4/140) | 文本 | 0~50 / 2~6 |
| `prefabs/AncientDoubleBed` | 0.7% (1/140) | 容器 |  |
| `prefabs/AncientDoubleBed/countPerTenEdgeCells` | 0.7% (1/140) | 数值 | 1 |
| `prefabs/AncientDoubleBed/minMaxRange` | 0.7% (1/140) | 文本 | 1~2 |
| `prefabs/AncientEquipmentBlocks_Rows` | 2.9% (4/140) | 容器 |  |
| `prefabs/AncientEquipmentBlocks_Rows/countPerHundredCells` | 2.9% (4/140) | 数值 | 2 / 5 |
| `prefabs/AncientEquipmentBlocks_Rows/minMaxRange` | 2.9% (4/140) | 文本 | 1~2 / 5~10 |
| `prefabs/AncientFilingCabinet_Edge` | 1.4% (2/140) | 容器 |  |
| `prefabs/AncientFilingCabinet_Edge/countPerTenEdgeCells` | 1.4% (2/140) | 数值 | 5 |
| `prefabs/AncientFilingCabinet_Edge/minMaxRange` | 1.4% (2/140) | 文本 | 1~2 |
| `prefabs/AncientForklift` | 0.7% (1/140) | 容器 |  |
| `prefabs/AncientForklift/countPerHundredCells` | 0.7% (1/140) | 数值 | 1 |
| `prefabs/AncientForklift/minMaxRange` | 0.7% (1/140) | 文本 | 0~1 |
| `prefabs/AncientFortifiedWall_Edge` | 4.3% (6/140) | 容器 |  |
| `prefabs/AncientFortifiedWall_Edge/countPerTenEdgeCells` | 4.3% (6/140) | 数值 | 5 |
| `prefabs/AncientFortifiedWall_Edge/minMaxRange` | 4.3% (6/140) | 文本 | 5~20 |
| `prefabs/AncientFortifiedWall_LargeCorner` | 0.7% (1/140) | 容器 |  |
| `prefabs/AncientFortifiedWall_LargeCorner/countPerHundredCells` | 0.7% (1/140) | 数值 | 5 |
| `prefabs/AncientFortifiedWall_LargeCorner/minMaxRange` | 0.7% (1/140) | 文本 | 0~1 |
| `prefabs/AncientFortifiedWall_Pillar3x3` | 7.9% (11/140) | 容器 |  |
| `prefabs/AncientFortifiedWall_Pillar3x3/countPerHundredCells` | 7.9% (11/140) | 数值 | 1 / 2 / 5 |
| `prefabs/AncientFortifiedWall_Pillar3x3/minMaxRange` | 7.9% (11/140) | 文本 | 0~1 / 1~2 |
| `prefabs/AncientFortifiedWall_PillarGroup` | 0.7% (1/140) | 容器 |  |
| `prefabs/AncientFortifiedWall_PillarGroup/countPerHundredCells` | 0.7% (1/140) | 数值 | 2 |
| `prefabs/AncientFortifiedWall_PillarGroup/minMaxRange` | 0.7% (1/140) | 文本 | 1~2 |
| `prefabs/AncientFuelNodeWithChembarrels` | 3.6% (5/140) | 容器 |  |
| `prefabs/AncientFuelNodeWithChembarrels/countPerHundredCells` | 3.6% (5/140) | 数值 | 2 / 5 |
| `prefabs/AncientFuelNodeWithChembarrels/minMaxRange` | 3.6% (5/140) | 文本 | 1~2 / 1~3 |
| `prefabs/AncientGenerator_Cluster` | 1.4% (2/140) | 容器 |  |
| `prefabs/AncientGenerator_Cluster/countPerHundredCells` | 1.4% (2/140) | 数值 | 2 |
| `prefabs/AncientGenerator_Cluster/minMaxRange` | 1.4% (2/140) | 文本 | 0~2 |
| `prefabs/AncientGenerator_SmallCluster` | 1.4% (2/140) | 容器 |  |
| `prefabs/AncientGenerator_SmallCluster/countPerHundredCells` | 1.4% (2/140) | 数值 | 2 |
| `prefabs/AncientGenerator_SmallCluster/minMaxRange` | 1.4% (2/140) | 文本 | 1~2 |
| `prefabs/AncientGeneratorSingle` | 0.7% (1/140) | 容器 |  |
| `prefabs/AncientGeneratorSingle/countPerHundredCells` | 0.7% (1/140) | 数值 | 5 |
| `prefabs/AncientGeneratorSingle/minMaxRange` | 0.7% (1/140) | 文本 | 1~10 |
| `prefabs/AncientLamp_Edge` | 5.0% (7/140) | 容器 |  |
| `prefabs/AncientLamp_Edge/countPerTenEdgeCells` | 5.0% (7/140) | 数值 | 1 |
| `prefabs/AncientLamp_Edge/minMaxRange` | 5.0% (7/140) | 文本 | 1~2 |
| `prefabs/AncientLamp_Single` | 2.1% (3/140) | 容器 |  |
| `prefabs/AncientLamp_Single/countPerHundredCells` | 2.1% (3/140) | 数值 | 5 |
| `prefabs/AncientLamp_Single/minMaxRange` | 2.1% (3/140) | 文本 | 0~1 |
| `prefabs/AncientLargeMechGestator` | 1.4% (2/140) | 容器 |  |
| `prefabs/AncientLargeMechGestator/countPerHundredCells` | 1.4% (2/140) | 数值 | 5 |
| `prefabs/AncientLargeMechGestator/minMaxRange` | 1.4% (2/140) | 文本 | 1~1 / 1~5 |
| `prefabs/AncientLockerBank_Row` | 3.6% (5/140) | 容器 |  |
| `prefabs/AncientLockerBank_Row/countPerTenEdgeCells` | 3.6% (5/140) | 数值 | 3 |
| `prefabs/AncientLockerBank_Row/minMaxRange` | 3.6% (5/140) | 文本 | 5~15 |
| `prefabs/AncientLockers_Row` | 5.0% (7/140) | 容器 |  |
| `prefabs/AncientLockers_Row/countPerHundredCells` | 0.7% (1/140) | 数值 | 15 |
| `prefabs/AncientLockers_Row/countPerTenEdgeCells` | 4.3% (6/140) | 数值 | 3 |
| `prefabs/AncientLockers_Row/minMaxRange` | 5.0% (7/140) | 文本 | 5~15 / 5~20 |
| `prefabs/AncientMachine_Rows` | 1.4% (2/140) | 容器 |  |
| `prefabs/AncientMachine_Rows/countPerHundredCells` | 1.4% (2/140) | 数值 | 5 |
| `prefabs/AncientMachine_Rows/minMaxRange` | 1.4% (2/140) | 文本 | 2~3 |
| `prefabs/AncientMechGestator_Cluster` | 0.7% (1/140) | 容器 |  |
| `prefabs/AncientMechGestator_Cluster/countPerHundredCells` | 0.7% (1/140) | 数值 | 5 |
| `prefabs/AncientMechGestator_Cluster/minMaxRange` | 0.7% (1/140) | 文本 | 1~5 |
| `prefabs/AncientMilitaryCrate_Cluster` | 2.9% (4/140) | 容器 |  |
| `prefabs/AncientMilitaryCrate_Cluster/countPerHundredCells` | 2.9% (4/140) | 数值 | 1 / 4 |
| `prefabs/AncientMilitaryCrate_Cluster/minMaxRange` | 2.9% (4/140) | 文本 | 3~10 / 3~5 |
| `prefabs/AncientOpenContainer` | 0.7% (1/140) | 容器 |  |
| `prefabs/AncientOpenContainer/countPerHundredCells` | 0.7% (1/140) | 数值 | 1 |
| `prefabs/AncientOpenContainer/minMaxRange` | 0.7% (1/140) | 文本 | 0~1 |
| `prefabs/AncientSafe` | 3.6% (5/140) | 容器 |  |
| `prefabs/AncientSafe/countPerHundredCells` | 3.6% (5/140) | 数值 | 1 |
| `prefabs/AncientSafe/minMaxRange` | 3.6% (5/140) | 数值/文本 | 0~1 / 1 / 1~1 |
| `prefabs/AncientSealedContainer` | 0.7% (1/140) | 容器 |  |
| `prefabs/AncientSealedContainer/countPerHundredCells` | 0.7% (1/140) | 数值 | 5 |
| `prefabs/AncientSealedContainer/minMaxRange` | 0.7% (1/140) | 文本 | 1~1 |
| `prefabs/AncientSealedContainer_GravshipUpgrade` | 2.1% (3/140) | 容器 |  |
| `prefabs/AncientSealedContainer_GravshipUpgrade/countPerHundredCells` | 1.4% (2/140) | 数值 | 1 |
| `prefabs/AncientSealedContainer_GravshipUpgrade/countRange` | 0.7% (1/140) | 文本 | 1~1 |
| `prefabs/AncientSealedContainer_GravshipUpgrade/minMaxRange` | 1.4% (2/140) | 文本 | 1~1 |
| `prefabs/AncientSealedCrate` | 5.0% (7/140) | 容器 |  |
| `prefabs/AncientSealedCrate/countRange` | 5.0% (7/140) | 文本 | 0~1 / 1~1 / 1~2 |
| `prefabs/AncientSealedCrate_Gravlite` | 2.9% (4/140) | 容器 |  |
| `prefabs/AncientSealedCrate_Gravlite/countRange` | 2.9% (4/140) | 文本 | 1~1 |
| `prefabs/AncientSealedCrate_Shells` | 0.7% (1/140) | 容器 |  |
| `prefabs/AncientSealedCrate_Shells/countRange` | 0.7% (1/140) | 文本 | 0~2 |
| `prefabs/AncientSecurityTerminal` | 2.9% (4/140) | 容器 |  |
| `prefabs/AncientSecurityTerminal/countPerHundredCells` | 2.9% (4/140) | 数值 | 2 |
| `prefabs/AncientSecurityTerminal/minMaxRange` | 2.9% (4/140) | 文本 | 0~2 / 1~2 |
| `prefabs/AncientSimpleResearchBench` | 0.7% (1/140) | 容器 |  |
| `prefabs/AncientSimpleResearchBench/countPerTenEdgeCells` | 0.7% (1/140) | 数值 | 5 |
| `prefabs/AncientSimpleResearchBench/minMaxRange` | 0.7% (1/140) | 文本 | 2~3 |
| `prefabs/AncientSingleBed` | 0.7% (1/140) | 容器 |  |
| `prefabs/AncientSingleBed/countPerTenEdgeCells` | 0.7% (1/140) | 数值 | 1 |
| `prefabs/AncientSingleBed/minMaxRange` | 0.7% (1/140) | 文本 | 1~2 |
| `prefabs/AncientSpacerCrate` | 0.7% (1/140) | 容器 |  |
| `prefabs/AncientSpacerCrate/countPerHundredCells` | 0.7% (1/140) | 数值 | 10 |
| `prefabs/AncientSpacerCrate/minMaxRange` | 0.7% (1/140) | 文本 | 0~10 |
| `prefabs/AncientSpacerCrate_Cluster` | 9.3% (13/140) | 容器 |  |
| `prefabs/AncientSpacerCrate_Cluster/countPerHundredCells` | 9.3% (13/140) | 数值 | 10 / 2 / 5 |
| `prefabs/AncientSpacerCrate_Cluster/minMaxRange` | 9.3% (13/140) | 文本 | 0~5 / 2~10 / 2~4 |
| `prefabs/AncientSpacerCrateWithComponentSpacer` | 3.6% (5/140) | 容器 |  |
| `prefabs/AncientSpacerCrateWithComponentSpacer/countPerHundredCells` | 3.6% (5/140) | 数值 | 1 / 5 |
| `prefabs/AncientSpacerCrateWithComponentSpacer/minMaxRange` | 3.6% (5/140) | 文本 | 0~1 / 1~1 / 1~2 |
| `prefabs/AncientStandardRecharger` | 0.7% (1/140) | 容器 |  |
| `prefabs/AncientStandardRecharger/countPerHundredCells` | 0.7% (1/140) | 数值 | 5 |
| `prefabs/AncientStandardRecharger/minMaxRange` | 0.7% (1/140) | 文本 | 1~1 |
| `prefabs/AncientSteelPallet` | 0.7% (1/140) | 容器 |  |
| `prefabs/AncientSteelPallet/countPerHundredCells` | 0.7% (1/140) | 数值 | 1 |
| `prefabs/AncientSteelPallet/minMaxRange` | 0.7% (1/140) | 文本 | 0~1 |
| `prefabs/AncientStorageCylinder_Edge` | 5.7% (8/140) | 容器 |  |
| `prefabs/AncientStorageCylinder_Edge/countPerTenEdgeCells` | 5.7% (8/140) | 数值 | 3 |
| `prefabs/AncientStorageCylinder_Edge/minMaxRange` | 5.7% (8/140) | 文本 | 5~10 |
| `prefabs/AncientStove_Cluster` | 2.1% (3/140) | 容器 |  |
| `prefabs/AncientStove_Cluster/countPerHundredCells` | 0.7% (1/140) | 数值 | 2 |
| `prefabs/AncientStove_Cluster/countPerTenEdgeCells` | 1.4% (2/140) | 数值 | 2 |
| `prefabs/AncientStove_Cluster/minMaxRange` | 2.1% (3/140) | 文本 | 0~1 / 1~1 |
| `prefabs/AncientSystemRack` | 0.7% (1/140) | 容器 |  |
| `prefabs/AncientSystemRack/countPerHundredCells` | 0.7% (1/140) | 数值 | 4 |
| `prefabs/AncientSystemRack/minMaxRange` | 0.7% (1/140) | 文本 | 1~10 |
| `prefabs/AncientSystemRacks_Rows` | 4.3% (6/140) | 容器 |  |
| `prefabs/AncientSystemRacks_Rows/countPerHundredCells` | 4.3% (6/140) | 数值 | 5 |
| `prefabs/AncientSystemRacks_Rows/minMaxRange` | 4.3% (6/140) | 文本 | 1~10 / 5~10 |
| `prefabs/AncientTableDrugLab` | 2.1% (3/140) | 容器 |  |
| `prefabs/AncientTableDrugLab/countPerTenEdgeCells` | 2.1% (3/140) | 数值 | 2 / 3 |
| `prefabs/AncientTableDrugLab/minMaxRange` | 2.1% (3/140) | 文本 | 1~1 / 2~4 |
| `prefabs/AncientTableMachining_Cluster` | 0.7% (1/140) | 容器 |  |
| `prefabs/AncientTableMachining_Cluster/countPerHundredCells` | 0.7% (1/140) | 数值 | 1 |
| `prefabs/AncientTableMachining_Cluster/minMaxRange` | 0.7% (1/140) | 文本 | 1~2 |
| `prefabs/AncientTableMachining_Edge` | 0.7% (1/140) | 容器 |  |
| `prefabs/AncientTableMachining_Edge/countPerTenEdgeCells` | 0.7% (1/140) | 数值 | 3 |
| `prefabs/AncientTableMachining_Edge/minMaxRange` | 0.7% (1/140) | 文本 | 1~2 |
| `prefabs/AncientTableStoveElectric_Edge` | 2.9% (4/140) | 容器 |  |
| `prefabs/AncientTableStoveElectric_Edge/countPerTenEdgeCells` | 2.9% (4/140) | 数值 | 3 / 5 |
| `prefabs/AncientTableStoveElectric_Edge/minMaxRange` | 2.9% (4/140) | 文本 | 1~2 / 5~15 |
| `prefabs/AncientTank` | 0.7% (1/140) | 容器 |  |
| `prefabs/AncientTank/countPerHundredCells` | 0.7% (1/140) | 数值 | 1 |
| `prefabs/AncientTank/minMaxRange` | 0.7% (1/140) | 文本 | 0~1 |
| `prefabs/AncientTerraformer` | 0.7% (1/140) | 容器 |  |
| `prefabs/AncientTerraformer/countRange` | 0.7% (1/140) | 文本 | 1~1 |
| `prefabs/AncientUplink` | 0.7% (1/140) | 容器 |  |
| `prefabs/AncientUplink/countPerHundredCells` | 0.7% (1/140) | 数值 | 3 |
| `prefabs/AncientUplink/minMaxRange` | 0.7% (1/140) | 文本 | 1~1 |
| `prefabs/AncientWorkbenchs` | 0.7% (1/140) | 容器 |  |
| `prefabs/AncientWorkbenchs/countPerHundredCells` | 0.7% (1/140) | 数值 | 2 |
| `prefabs/AncientWorkbenchs/minMaxRange` | 0.7% (1/140) | 文本 | 1~2 |
| `prefabs/Armchairs_Edge` | 0.7% (1/140) | 容器 |  |
| `prefabs/Armchairs_Edge/countPerTenEdgeCells` | 0.7% (1/140) | 数值 | 5 |
| `prefabs/Armchairs_Edge/minMaxRange` | 0.7% (1/140) | 文本 | 3~5 |
| `prefabs/BathtubWithStool` | 1.4% (2/140) | 容器 |  |
| `prefabs/BathtubWithStool/countPerHundredCells` | 1.4% (2/140) | 数值 | 10 |
| `prefabs/BathtubWithStool/minMaxRange` | 1.4% (2/140) | 文本 | 0~1 |
| `prefabs/BilliardsTable` | 0.7% (1/140) | 容器 |  |
| `prefabs/BilliardsTable/countRange` | 0.7% (1/140) | 文本 | 0~2 |
| `prefabs/BiofuelRefinery_Cluster` | 0.7% (1/140) | 容器 |  |
| `prefabs/BiofuelRefinery_Cluster/minMaxRange` | 0.7% (1/140) | 文本 | 1~3 |
| `prefabs/BurrowWall_Large` | 5.0% (7/140) | 容器 |  |
| `prefabs/BurrowWall_Large/countPerHundredCells` | 5.0% (7/140) | 数值 | 1 |
| `prefabs/BurrowWall_Large/minMaxRange` | 5.0% (7/140) | 数值 | 1 |
| `prefabs/BurrowWall_Medium` | 5.0% (7/140) | 容器 |  |
| `prefabs/BurrowWall_Medium/countPerHundredCells` | 5.0% (7/140) | 数值 | 1 |
| `prefabs/BurrowWall_Medium/minMaxRange` | 5.0% (7/140) | 文本 | 1~2 |
| `prefabs/Chembarrel_Cluster` | 1.4% (2/140) | 容器 |  |
| `prefabs/Chembarrel_Cluster/countPerHundredCells` | 1.4% (2/140) | 数值 | 5 |
| `prefabs/Chembarrel_Cluster/minMaxRange` | 1.4% (2/140) | 文本 | 1~3 |
| `prefabs/ChemfuelWorkstation` | 1.4% (2/140) | 容器 |  |
| `prefabs/ChemfuelWorkstation/countPerTenEdgeCells` | 1.4% (2/140) | 数值 | 1 |
| `prefabs/ChemfuelWorkstation/minMaxRange` | 1.4% (2/140) | 文本 | 1~3 |
| `prefabs/ChessTable` | 1.4% (2/140) | 容器 |  |
| `prefabs/ChessTable/countPerHundredCells` | 1.4% (2/140) | 数值 | 3 |
| `prefabs/ChessTable/minMaxRange` | 1.4% (2/140) | 文本 | 0~1 / 0~2 |
| `prefabs/CollapsedRocks_Cluster` | 1.4% (2/140) | 容器 |  |
| `prefabs/CollapsedRocks_Cluster/countPerHundredCells` | 0.7% (1/140) | 数值 | 1 |
| `prefabs/CollapsedRocks_Cluster/countRange` | 0.7% (1/140) | 文本 | 1~2 |
| `prefabs/CollapsedRocks_Cluster/minMaxRange` | 0.7% (1/140) | 文本 | 1~1 |
| `prefabs/CorridorBarricade` | 1.4% (2/140) | 容器 |  |
| `prefabs/CorridorBarricade/countPerHundredCells` | 1.4% (2/140) | 数值 | 1 |
| `prefabs/CorridorBarricade/ensureNoBlocks` | 1.4% (2/140) | 布尔 | false |
| `prefabs/CorridorBarricade/minMaxRange` | 1.4% (2/140) | 文本 | 1~3 |
| `prefabs/CorridorBarricadeIntersection` | 1.4% (2/140) | 容器 |  |
| `prefabs/CorridorBarricadeIntersection/countRange` | 1.4% (2/140) | 文本 | 1~1 |
| `prefabs/Couch_Edge` | 1.4% (2/140) | 容器 |  |
| `prefabs/Couch_Edge/countPerTenEdgeCells` | 1.4% (2/140) | 数值 | 2 |
| `prefabs/Couch_Edge/minMaxRange` | 1.4% (2/140) | 文本 | 0~1 |
| `prefabs/DiningTable_Large` | 0.7% (1/140) | 容器 |  |
| `prefabs/DiningTable_Large/countPerHundredCells` | 0.7% (1/140) | 文本 | 1~2 |
| `prefabs/DiningTable_Large/minMaxRange` | 0.7% (1/140) | 文本 | 1~3 |
| `prefabs/DiningTable_VeryLarge` | 0.7% (1/140) | 容器 |  |
| `prefabs/DiningTable_VeryLarge/countPerHundredCells` | 0.7% (1/140) | 文本 | 1~2 |
| `prefabs/DiningTable_VeryLarge/minMaxRange` | 0.7% (1/140) | 文本 | 1~1 |
| `prefabs/FirefoamPopper` | 1.4% (2/140) | 容器 |  |
| `prefabs/FirefoamPopper/countPerHundredCells` | 1.4% (2/140) | 数值 | 1 |
| `prefabs/FirefoamPopper/minMaxRange` | 1.4% (2/140) | 文本 | 1~2 |
| `prefabs/FlatscreenTelevision` | 0.7% (1/140) | 容器 |  |
| `prefabs/FlatscreenTelevision/countPerTenEdgeCells` | 0.7% (1/140) | 数值 | 1 |
| `prefabs/FlatscreenTelevision/minMaxRange` | 0.7% (1/140) | 文本 | 0~1 |
| `prefabs/GestatorTanksWithLoot` | 0.7% (1/140) | 容器 |  |
| `prefabs/GestatorTanksWithLoot/countPerHundredCells` | 0.7% (1/140) | 数值 | 5 |
| `prefabs/GestatorTanksWithLoot/minMaxRange` | 0.7% (1/140) | 文本 | 1~1 |
| `prefabs/Gloomlight_Cluster` | 0.7% (1/140) | 容器 |  |
| `prefabs/Gloomlight_Cluster/countPerHundredCells` | 0.7% (1/140) | 数值 | 5 |
| `prefabs/Gloomlight_Cluster/minMaxRange` | 0.7% (1/140) | 文本 | 1~1 |
| `prefabs/HydroponicsBasin_Cluster` | 0.7% (1/140) | 容器 |  |
| `prefabs/HydroponicsBasin_Cluster/countPerHundredCells` | 0.7% (1/140) | 数值 | 3 |
| `prefabs/HydroponicsBasin_Cluster/minMaxRange` | 0.7% (1/140) | 文本 | 2~3 |
| `prefabs/IndustrialShelf_Edge` | 15.7% (22/140) | 容器 |  |
| `prefabs/IndustrialShelf_Edge/countPerTenEdgeCells` | 15.7% (22/140) | 数值 | 10 / 2 / 3 |
| `prefabs/IndustrialShelf_Edge/minMaxRange` | 15.7% (22/140) | 文本 | 10~20 / 1~20 / 1~5 |
| `prefabs/IndustrialShelf_InnerWall` | 2.9% (4/140) | 容器 |  |
| `prefabs/IndustrialShelf_InnerWall/countPerHundredCells` | 2.9% (4/140) | 数值 | 2 |
| `prefabs/IndustrialShelf_InnerWall/minMaxRange` | 2.9% (4/140) | 文本 | 0~1 |
| `prefabs/IndustrialShelf_Rows` | 9.3% (13/140) | 容器 |  |
| `prefabs/IndustrialShelf_Rows/countPerHundredCells` | 9.3% (13/140) | 数值 | 1 / 2 / 3 |
| `prefabs/IndustrialShelf_Rows/minMaxRange` | 9.3% (13/140) | 文本 | 1~10 / 1~2 |
| `prefabs/InsectLairEntrance` | 0.7% (1/140) | 容器 |  |
| `prefabs/InsectLairEntrance/countPerHundredCells` | 0.7% (1/140) | 数值 | 10 |
| `prefabs/InsectLairEntrance/minMaxRange` | 0.7% (1/140) | 文本 | 1~1 |
| `prefabs/MechanoidProcessor` | 2.1% (3/140) | 容器 |  |
| `prefabs/MechanoidProcessor/countPerHundredCells` | 2.1% (3/140) | 数值 | 5 |
| `prefabs/MechanoidProcessor/minMaxRange` | 2.1% (3/140) | 文本 | 1~1 |
| `prefabs/MechanoidProcessor_Cluster` | 0.7% (1/140) | 容器 |  |
| `prefabs/MechanoidProcessor_Cluster/countPerHundredCells` | 0.7% (1/140) | 数值 | 5 |
| `prefabs/MechanoidProcessor_Cluster/minMaxRange` | 0.7% (1/140) | 文本 | 1~2 |
| `prefabs/MechPylon_Structure_Edge` | 4.3% (6/140) | 容器 |  |
| `prefabs/MechPylon_Structure_Edge/countPerTenEdgeCells` | 4.3% (6/140) | 数值 | 2 |
| `prefabs/MechPylon_Structure_Edge/minMaxRange` | 4.3% (6/140) | 文本 | 3~6 |
| `prefabs/MechPylon_StructureCross` | 0.7% (1/140) | 容器 |  |
| `prefabs/MechPylon_StructureCross/countPerHundredCells` | 0.7% (1/140) | 数值 | 5 |
| `prefabs/MechPylon_StructureCross/minMaxRange` | 0.7% (1/140) | 文本 | 1~4 |
| `prefabs/MechStorageCylinder_Cluster` | 1.4% (2/140) | 容器 |  |
| `prefabs/MechStorageCylinder_Cluster/countPerHundredCells` | 1.4% (2/140) | 数值 | 5 |
| `prefabs/MechStorageCylinder_Cluster/minMaxRange` | 1.4% (2/140) | 文本 | 1~1 / 1~2 |
| `prefabs/MedicinePallet` | 3.6% (5/140) | 容器 |  |
| `prefabs/MedicinePallet/countPerTenEdgeCells` | 1.4% (2/140) | 数值 | 1 |
| `prefabs/MedicinePallet/countRange` | 2.1% (3/140) | 文本 | 0~1 |
| `prefabs/MedicinePallet/minMaxRange` | 1.4% (2/140) | 文本 | 0~1 |
| `prefabs/MiningCharge_Cluster` | 3.6% (5/140) | 容器 |  |
| `prefabs/MiningCharge_Cluster/countPerHundredCells` | 1.4% (2/140) | 数值 | 1 |
| `prefabs/MiningCharge_Cluster/countPerTenEdgeCells` | 2.1% (3/140) | 数值 | 1 |
| `prefabs/MiningCharge_Cluster/minMaxRange` | 3.6% (5/140) | 文本 | 0~1 / 1~1 / 1~3 |
| `prefabs/OperatingTables` | 2.1% (3/140) | 容器 |  |
| `prefabs/OperatingTables/countPerHundredCells` | 2.1% (3/140) | 数值 | 10 |
| `prefabs/OperatingTables/minMaxRange` | 2.1% (3/140) | 文本 | 0~1 |
| `prefabs/PokerTable` | 1.4% (2/140) | 容器 |  |
| `prefabs/PokerTable/countRange` | 1.4% (2/140) | 文本 | 0~1 / 0~2 |
| `prefabs/RubblePile_Cluster` | 0.7% (1/140) | 容器 |  |
| `prefabs/RubblePile_Cluster/countPerHundredCells` | 0.7% (1/140) | 数值 | 10 |
| `prefabs/RubblePile_Cluster/minMaxRange` | 0.7% (1/140) | 文本 | 5~10 |
| `prefabs/RustedEngine_Cluster` | 0.7% (1/140) | 容器 |  |
| `prefabs/RustedEngine_Cluster/countPerHundredCells` | 0.7% (1/140) | 数值 | 3 |
| `prefabs/RustedEngine_Cluster/minMaxRange` | 0.7% (1/140) | 文本 | 1~2 |
| `prefabs/SchoolDesksAndBlackboards` | 0.7% (1/140) | 容器 |  |
| `prefabs/SchoolDesksAndBlackboards/countPerHundredCells` | 0.7% (1/140) | 数值 | 3 |
| `prefabs/SchoolDesksAndBlackboards/minMaxRange` | 0.7% (1/140) | 文本 | 2~3 |
| `prefabs/SculptureSmall` | 0.7% (1/140) | 容器 |  |
| `prefabs/SculptureSmall/countRange` | 0.7% (1/140) | 文本 | -2~2 |
| `prefabs/Shelf` | 0.7% (1/140) | 容器 |  |
| `prefabs/Shelf/countPerTenEdgeCells` | 0.7% (1/140) | 文本 | 2~4 |
| `prefabs/Shelf/minMaxRange` | 0.7% (1/140) | 文本 | 0~10 |
| `prefabs/Shelves_Rows` | 4.3% (6/140) | 容器 |  |
| `prefabs/Shelves_Rows/countPerHundredCells` | 4.3% (6/140) | 数值 | 2 |
| `prefabs/Shelves_Rows/minMaxRange` | 4.3% (6/140) | 文本 | 0~1 / 1~2 |
| `prefabs/ShowerAndToilet_Edge` | 2.9% (4/140) | 容器 |  |
| `prefabs/ShowerAndToilet_Edge/countPerTenEdgeCells` | 2.9% (4/140) | 数值 | 2 |
| `prefabs/ShowerAndToilet_Edge/minMaxRange` | 2.9% (4/140) | 文本 | 0~1 / 1~2 |
| `prefabs/SolidIce_AlongWall` | 2.9% (4/140) | 容器 |  |
| `prefabs/SolidIce_AlongWall/countPerTenEdgeCells` | 2.9% (4/140) | 数值 | 10 |
| `prefabs/SolidIce_AlongWall/minMaxRange` | 2.9% (4/140) | 文本 | 0~50 |
| `prefabs/SolidIce_Large` | 1.4% (2/140) | 容器 |  |
| `prefabs/SolidIce_Large/countPerHundredCells` | 1.4% (2/140) | 数值 | 10 / 15 |
| `prefabs/SolidIce_Large/minMaxRange` | 1.4% (2/140) | 文本 | 0~20 / 1~1 |
| `prefabs/SolidIce_Loot` | 0.7% (1/140) | 容器 |  |
| `prefabs/SolidIce_Loot/countPerHundredCells` | 0.7% (1/140) | 数值 | 1 |
| `prefabs/SolidIce_Loot/minMaxRange` | 0.7% (1/140) | 文本 | 0~1 |
| `prefabs/SolidIce_Medium` | 2.1% (3/140) | 容器 |  |
| `prefabs/SolidIce_Medium/countPerHundredCells` | 2.1% (3/140) | 数值 | 10 / 15 |
| `prefabs/SolidIce_Medium/minMaxRange` | 2.1% (3/140) | 文本 | 0~20 / 0~5 / 3~20 |
| `prefabs/SolidIce_Small` | 2.9% (4/140) | 容器 |  |
| `prefabs/SolidIce_Small/countPerHundredCells` | 2.9% (4/140) | 数值 | 10 / 15 |
| `prefabs/SolidIce_Small/minMaxRange` | 2.9% (4/140) | 文本 | 0~20 / 3~20 |
| `prefabs/SpaceTerrain` | 0.7% (1/140) | 容器 |  |
| `prefabs/SpaceTerrain/countPerHundredCells` | 0.7% (1/140) | 数值 | 20 |
| `prefabs/SpaceTerrain/minMaxRange` | 0.7% (1/140) | 文本 | 2~10 |
| `prefabs/Subroom_Bedrooms` | 0.7% (1/140) | 容器 |  |
| `prefabs/Subroom_Bedrooms/countPerHundredCells` | 0.7% (1/140) | 数值 | 1 |
| `prefabs/Subroom_Bedrooms/minMaxRange` | 0.7% (1/140) | 文本 | 0~1 |
| `prefabs/Subroom_Crib` | 0.7% (1/140) | 容器 |  |
| `prefabs/Subroom_Crib/countPerTenEdgeCells` | 0.7% (1/140) | 数值 | 5 |
| `prefabs/Subroom_Crib/minMaxRange` | 0.7% (1/140) | 文本 | 1~2 |
| `prefabs/Subroom_ElectricStove` | 0.7% (1/140) | 容器 |  |
| `prefabs/Subroom_ElectricStove/countPerTenEdgeCells` | 0.7% (1/140) | 数值 | 1 |
| `prefabs/Subroom_ElectricStove/minMaxRange` | 0.7% (1/140) | 文本 | 1~2 |
| `prefabs/Subroom_LootInVents` | 0.7% (1/140) | 容器 |  |
| `prefabs/Subroom_LootInVents/countPerHundredCells` | 0.7% (1/140) | 数值 | 5 |
| `prefabs/Subroom_LootInVents/minMaxRange` | 0.7% (1/140) | 文本 | 0~1 |
| `prefabs/Subroom_Partialwall` | 2.9% (4/140) | 容器 |  |
| `prefabs/Subroom_Partialwall/countPerHundredCells` | 2.9% (4/140) | 数值 | 5 |
| `prefabs/Subroom_Partialwall/minMaxRange` | 2.9% (4/140) | 文本 | 1~5 |
| `prefabs/Subroom_Rectangle` | 0.7% (1/140) | 容器 |  |
| `prefabs/Subroom_Rectangle/countPerHundredCells` | 0.7% (1/140) | 数值 | 5 |
| `prefabs/Subroom_Rectangle/minMaxRange` | 0.7% (1/140) | 文本 | 0~1 |
| `prefabs/Subroom_SpacerCrates` | 0.7% (1/140) | 容器 |  |
| `prefabs/Subroom_SpacerCrates/countPerHundredCells` | 0.7% (1/140) | 数值 | 1 |
| `prefabs/Subroom_SpacerCrates/minMaxRange` | 0.7% (1/140) | 文本 | 0~1 |
| `prefabs/SurvivalMealPallet` | 4.3% (6/140) | 容器 |  |
| `prefabs/SurvivalMealPallet/countPerHundredCells` | 2.9% (4/140) | 数值 | 1 / 2 |
| `prefabs/SurvivalMealPallet/countRange` | 1.4% (2/140) | 文本 | 0~1 / 1~1 |
| `prefabs/SurvivalMealPallet/minMaxRange` | 2.9% (4/140) | 文本 | 0~1 / 1~1 |
| `prefabs/TableWithStools_1x2` | 4.3% (6/140) | 容器 |  |
| `prefabs/TableWithStools_1x2/countPerHundredCells` | 4.3% (6/140) | 数值 | 1 / 2 |
| `prefabs/TableWithStools_1x2/minMaxRange` | 4.3% (6/140) | 文本 | 0~3 / 1~1 / 1~2 |
| `prefabs/TableWithStools_2x2` | 2.9% (4/140) | 容器 |  |
| `prefabs/TableWithStools_2x2/countPerHundredCells` | 2.9% (4/140) | 数值 | 1 / 2 |
| `prefabs/TableWithStools_2x2/minMaxRange` | 2.9% (4/140) | 文本 | 0~1 / 1~1 |
| `prefabs/TableWithStools_2x4` | 0.7% (1/140) | 容器 |  |
| `prefabs/TableWithStools_2x4/countPerHundredCells` | 0.7% (1/140) | 数值 | 3 |
| `prefabs/TableWithStools_2x4/minMaxRange` | 0.7% (1/140) | 文本 | 1~2 |
| `prefabs/TVWithArmchairs` | 2.1% (3/140) | 容器 |  |
| `prefabs/TVWithArmchairs/countPerTenEdgeCells` | 2.1% (3/140) | 数值 | 1 / 2 |
| `prefabs/TVWithArmchairs/minMaxRange` | 2.1% (3/140) | 文本 | 0~1 / 1~1 |
| `prefabs/WoodenCrate_Cluster` | 7.1% (10/140) | 容器 |  |
| `prefabs/WoodenCrate_Cluster/countPerHundredCells` | 7.1% (10/140) | 数值 | 1 / 10 / 2 |
| `prefabs/WoodenCrate_Cluster/minMaxRange` | 7.1% (10/140) | 文本 | 0~1 / 1~2 |
| `prefabs/WoodenCratesWithSomeLoot` | 6.4% (9/140) | 容器 |  |
| `prefabs/WoodenCratesWithSomeLoot/countPerHundredCells` | 6.4% (9/140) | 数值 | 1 / 2 |
| `prefabs/WoodenCratesWithSomeLoot/minMaxRange` | 6.4% (9/140) | 文本 | 0~1 / 1~1 / 1~2 |
| `requiresSingleRectRoom` | 3.6% (5/140) | 布尔 | true |
| `roomContentsWorkerType` | 35.7% (50/140) | 文本 | RoomContents_EndlessPit / RoomContents_Etchings / RoomContents_Obelisk |
| `scatter` | 8.6% (12/140) | 容器 |  |
| `scatter/AncientBarrel` | 0.7% (1/140) | 容器 |  |
| `scatter/AncientBarrel/groupDistRange` | 0.7% (1/140) | 文本 | 2~4 |
| `scatter/AncientBarrel/groupsPerHundredCells` | 0.7% (1/140) | 文本 | 2~3 |
| `scatter/AncientBarrel/itemsPerGroup` | 0.7% (1/140) | 文本 | 1~5 |
| `scatter/AncientBarrel/minGroups` | 0.7% (1/140) | 数值 | 1 |
| `scatter/AncientLargeCrate` | 0.7% (1/140) | 容器 |  |
| `scatter/AncientLargeCrate/groupDistRange` | 0.7% (1/140) | 文本 | 2~5 |
| `scatter/AncientLargeCrate/groupsPerHundredCells` | 0.7% (1/140) | 文本 | 2~4 |
| `scatter/AncientLargeCrate/itemsPerGroup` | 0.7% (1/140) | 文本 | 3~6 |
| `scatter/AncientSpacerCrate` | 2.1% (3/140) | 容器 |  |
| `scatter/AncientSpacerCrate/groupDistRange` | 2.1% (3/140) | 文本 | 3~5 |
| `scatter/AncientSpacerCrate/groupsPerHundredCells` | 2.1% (3/140) | 文本 | 3~5 |
| `scatter/AncientSpacerCrate/itemsPerGroup` | 2.1% (3/140) | 文本 | 3~8 |
| `scatter/AncientSpacerCrate/minGroups` | 2.1% (3/140) | 数值 | 1 |
| `scatter/BabyDecoration` | 0.7% (1/140) | 容器 |  |
| `scatter/BabyDecoration/groupsPerHundredCells` | 0.7% (1/140) | 文本 | 1~3 |
| `scatter/BabyDecoration/itemsPerGroup` | 0.7% (1/140) | 文本 | 1~1 |
| `scatter/BabyDecoration/minGroups` | 0.7% (1/140) | 数值 | 1 |
| `scatter/BabyDecoration/stuff` | 0.7% (1/140) | 文本 | WoodLog |
| `scatter/ChunkMechanoidSlag` | 2.1% (3/140) | 容器 |  |
| `scatter/ChunkMechanoidSlag/groupDistRange` | 2.1% (3/140) | 文本 | 3~5 |
| `scatter/ChunkMechanoidSlag/groupsPerHundredCells` | 2.1% (3/140) | 文本 | 2~4 |
| `scatter/ChunkMechanoidSlag/itemsPerGroup` | 2.1% (3/140) | 文本 | 1~2 |
| `scatter/ChunkMechanoidSlag/minGroups` | 2.1% (3/140) | 数值 | 1 |
| `scatter/Filth_BlastMark` | 0.7% (1/140) | 容器 |  |
| `scatter/Filth_BlastMark/groupDistRange` | 0.7% (1/140) | 文本 | 3~5 |
| `scatter/Filth_BlastMark/groupsPerHundredCells` | 0.7% (1/140) | 文本 | 1~2 |
| `scatter/Filth_BlastMark/itemsPerGroup` | 0.7% (1/140) | 文本 | 1~2 |
| `scatter/Filth_BlastMark/minGroups` | 0.7% (1/140) | 数值 | 1 |
| `scatter/Filth_OilSmear` | 0.7% (1/140) | 容器 |  |
| `scatter/Filth_OilSmear/groupDistRange` | 0.7% (1/140) | 文本 | 3~5 |
| `scatter/Filth_OilSmear/groupsPerHundredCells` | 0.7% (1/140) | 文本 | 2~4 |
| `scatter/Filth_OilSmear/itemsPerGroup` | 0.7% (1/140) | 文本 | 1~2 |
| `scatter/Filth_OilSmear/minGroups` | 0.7% (1/140) | 数值 | 1 |
| `scatter/Filth_RubbleRock` | 0.7% (1/140) | 容器 |  |
| `scatter/Filth_RubbleRock/groupDistRange` | 0.7% (1/140) | 文本 | 3~5 |
| `scatter/Filth_RubbleRock/groupsPerHundredCells` | 0.7% (1/140) | 文本 | 3~5 |
| `scatter/Filth_RubbleRock/itemsPerGroup` | 0.7% (1/140) | 文本 | 3~8 |
| `scatter/Filth_RubbleRock/minGroups` | 0.7% (1/140) | 数值 | 1 |
| `scatter/RubblePile` | 0.7% (1/140) | 容器 |  |
| `scatter/RubblePile/groupDistRange` | 0.7% (1/140) | 文本 | 3~5 |
| `scatter/RubblePile/groupsPerHundredCells` | 0.7% (1/140) | 文本 | 2~4 |
| `scatter/RubblePile/itemsPerGroup` | 0.7% (1/140) | 文本 | 2~4 |
| `scatter/RubblePile/minGroups` | 0.7% (1/140) | 数值 | 1 |
| `scatter/ToyBox` | 0.7% (1/140) | 容器 |  |
| `scatter/ToyBox/groupsPerHundredCells` | 0.7% (1/140) | 文本 | 0~1 |
| `scatter/ToyBox/itemsPerGroup` | 0.7% (1/140) | 文本 | 1~1 |
| `scatter/ToyBox/minGroups` | 0.7% (1/140) | 数值 | 1 |
| `scatter/ToyBox/stuff` | 0.7% (1/140) | 文本 | WoodLog |
| `scatterTerrain` | 18.6% (26/140) | 容器 |  |
| `scatterTerrain/AncientConcrete` | 10.0% (14/140) | 容器 |  |
| `scatterTerrain/AncientConcrete/groupDistRange` | 10.0% (14/140) | 文本 | 1~5 |
| `scatterTerrain/AncientConcrete/groupsPerHundredCells` | 10.0% (14/140) | 文本 | 5~8 |
| `scatterTerrain/AncientConcrete/itemsPerGroup` | 10.0% (14/140) | 文本 | 10~15 |
| `scatterTerrain/Ice` | 3.6% (5/140) | 容器 |  |
| `scatterTerrain/Ice/groupDistRange` | 3.6% (5/140) | 文本 | 1~5 |
| `scatterTerrain/Ice/groupsPerHundredCells` | 3.6% (5/140) | 文本 | 5~8 |
| `scatterTerrain/Ice/itemsPerGroup` | 3.6% (5/140) | 文本 | 10~15 |
| `scatterTerrain/InsectSludge` | 4.3% (6/140) | 容器 |  |
| `scatterTerrain/InsectSludge/groupDistRange` | 4.3% (6/140) | 文本 | 1~5 |
| `scatterTerrain/InsectSludge/groupsPerHundredCells` | 4.3% (6/140) | 文本 | 5~8 |
| `scatterTerrain/InsectSludge/itemsPerGroup` | 4.3% (6/140) | 文本 | 10~15 |
| `scatterTerrain/Soil` | 0.7% (1/140) | 容器 |  |
| `scatterTerrain/Soil/groupDistRange` | 0.7% (1/140) | 文本 | 2~3 |
| `scatterTerrain/Soil/groupsPerHundredCells` | 0.7% (1/140) | 文本 | 2~3 |
| `scatterTerrain/Soil/itemsPerGroup` | 0.7% (1/140) | 文本 | 4~6 |
| `sketchResolverDef` | 1.4% (2/140) | 文本 | AncientBarracks / AncientStorageRoom |
| `spawnJunk` | 4.3% (6/140) | 布尔 | false |
| `thingSetMakerDef` | 0.7% (1/140) | 文本 | MapGen_OrbitalItemStash |
| `threatPointsScaleCurve` | 5.7% (8/140) | 容器 |  |
| `threatPointsScaleCurve/points` | 5.7% (8/140) | 容器 |  |
| `threatPointsScaleCurve/points/li` | 25.0% (35/140) | 文本 | (100, 100) / (1000, 300) / (2000, 500) |

## 四、原版 defName 一览（共 140 个，列出前 60）

```text
`LabyrinthEmpty`                  `LabyrinthEndlessPit`             `LabyrinthChildRoom`              `ComplexCorridor`               
`AncientRuinsEmpty`               `AncientRuinsCorridor`            `AncientRuinsShelfedCorridor`     `AncientWarehouseCorridor`      
`AncientRuinsKitchen`             `AncientRuinsOperatingRoom`       `AncientRuinsFuelRoom`            `AncientOrbitalCorridor`        
`LabyrinthFloorEtchings`          `LabyrinthDeadBody`               `LabyrinthCorpseRoom`             `LabyrinthAbandonedCamp`        
`LabyrinthAnimalCorpses`          `LabyrinthAnimals`                `LabyrinthHarbinger`              `LabyrinthTrees`                
`LabyrinthGrayBox`                `LabyrinthLargeGrayBox`           `LabyrinthLargeEmptyGrayBox`      `LabyrinthFloorRamblings`       
`LabyrinthObelisk`                `LabyrinthSleepingFleshbeast`     `AncientRuinsReactorToxicWaterRoom`  `AncientStockpileHermeticCrateRoom`
`LaunchPad`                       `AncientStockpileEntrance`        `AncientCryptosleepRoom`          `LabyrinthStatueDeadlife`       
`LabyrinthStatueTeleporter`       `AncientChemfuelStorage`          `AncientStockpileSecurityRoom`    `AncientRuinsReactorControlRoom`
`AncientStockpileStockpile`       `AncientRuinsReactorCorridor`     `AncientRuinsDiningHall`          `InnerCourtyardRooms`           
`OrbitalTransportRoom`            `OrbitalItemStash_ItemRoom`       `AncientStorageRoom`              `InnerCourtyard`                
`OrbitalRuinsDestroyedFloor`      `AncientBarracks`                 `AncientRuinsInsectHive`          `AncientOrbitalCorridorDefense` 
`NarrowHalls`                     `MechGestationRoom`               `OrbitalWreckRubble`              `AncientCorridorDefense`        
`AncientRuinsIndustrialStorage`   `AncientRuinsStorage`             `AncientRuinsBarracks`            `AncientRuinsCryptosleepCasketNoThreat`
`AncientRuinsReactorCorpseRoom`   `AncientRuinsInsectHive_Underground`  `AncientCryptosleepRoom_Hostile`  `AncientLab`                    
```

_余下 80 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
