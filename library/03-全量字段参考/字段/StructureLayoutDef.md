# StructureLayoutDef

- **所属线**：世界线
- **原版实例数**：33
- **字段路径数**：349
- **资料片**：Odyssey
- **原版出处**：`Odyssey/Defs/LayoutDefs/Layouts_CrashedMechanoidPlatform.xml`、`Odyssey/Defs/LayoutDefs/Layouts_OrbitalPlatform.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<StructureLayoutDef ParentName="CrashedMechanoidPlatformBase">
    <defName>CrashedMechanoidPlatform_Standard</defName>
  </StructureLayoutDef>
  
  
```

> 来自 `Odyssey/Defs/LayoutDefs/Layouts_CrashedMechanoidPlatform.xml`，defName = `CrashedMechanoidPlatform_Standard`，XML 节点数 2（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

_该类型没有出现率≥90% 的字段（字段高度自由）。_

## 三、全量字段表（349 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `areaPrunePercent` | 12.1% (4/33) | 数值 | 0.05 / 0.1 / 0.15 |
| `canConnectRoomsExternally` | 3.0% (1/33) | 布尔 | false |
| `canDisconnectRooms` | 9.1% (3/33) | 布尔 | false / true |
| `canHaveMultipleLayoutsInRoom` | 45.5% (15/33) | 布尔 | true |
| `clearDoorFaction` | 3.0% (1/33) | 布尔 | false |
| `clearRoomsEntirely` | 12.1% (4/33) | 布尔 | true |
| `corridorDef` | 24.2% (8/33) | 文本 | AncientCorridorDefense / AncientOrbitalCorridor / AncientRuinsReactorCorridor |
| `corridorShapes` | 15.2% (5/33) | 文本 | AsymmetricCross, H, Cross, T / Cross, T |
| `defaultAffordanceTerrainDef` | 3.0% (1/33) | 文本 | MechanoidPlatform |
| `defName` | 81.8% (27/33) | 文本 | AncientRuinsGlacier / AncientRuinsReactor_Standard / AncientRuins_Scarlands |
| `doorDef` | 3.0% (1/33) | 文本 | Door |
| `doorStuffDef` | 15.2% (5/33) | 文本 | Steel |
| `ensureOneDoorUnlocked` | 15.2% (5/33) | 布尔 | true |
| `exteriorDoorDef` | 15.2% (5/33) | 文本 | AncientBlastDoor |
| `exteriorDoorStuffDef` | 3.0% (1/33) | 容器 |  |
| `importantRoomDef` | 18.2% (6/33) | 文本 | AncientRuinsReactor / AncientRuinsTerraformer / MechanoidEngineRoom |
| `junkScaterrers` | 51.5% (17/33) | 容器 |  |
| `junkScaterrers/AncientBarrel` | 3.0% (1/33) | 容器 |  |
| `junkScaterrers/AncientBarrel/groupDistRange` | 3.0% (1/33) | 文本 | 3~5 |
| `junkScaterrers/AncientBarrel/groupsPerHundredCells` | 3.0% (1/33) | 文本 | 1~3 |
| `junkScaterrers/AncientBarrel/itemsPerGroup` | 3.0% (1/33) | 文本 | 2~4 |
| `junkScaterrers/AncientCardboardBox` | 3.0% (1/33) | 容器 |  |
| `junkScaterrers/AncientCardboardBox/groupDistRange` | 3.0% (1/33) | 文本 | 3~5 |
| `junkScaterrers/AncientCardboardBox/groupsPerHundredCells` | 3.0% (1/33) | 文本 | 1~2 |
| `junkScaterrers/AncientCardboardBox/itemsPerGroup` | 3.0% (1/33) | 文本 | 2~5 |
| `junkScaterrers/AncientMilitaryCrate` | 3.0% (1/33) | 容器 |  |
| `junkScaterrers/AncientMilitaryCrate/groupDistRange` | 3.0% (1/33) | 文本 | 3~5 |
| `junkScaterrers/AncientMilitaryCrate/groupsPerHundredCells` | 3.0% (1/33) | 文本 | 0~1 |
| `junkScaterrers/AncientMilitaryCrate/itemsPerGroup` | 3.0% (1/33) | 文本 | 2~4 |
| `junkScaterrers/AncientWoodenCrate` | 3.0% (1/33) | 容器 |  |
| `junkScaterrers/AncientWoodenCrate/groupDistRange` | 3.0% (1/33) | 文本 | 2~3 |
| `junkScaterrers/AncientWoodenCrate/groupsPerHundredCells` | 3.0% (1/33) | 文本 | 1~2 |
| `junkScaterrers/AncientWoodenCrate/itemsPerGroup` | 3.0% (1/33) | 文本 | 1~4 |
| `junkScaterrers/AncientWoodenCrate/minGroups` | 3.0% (1/33) | 数值 | 1 |
| `junkScaterrers/BurrowWall` | 3.0% (1/33) | 容器 |  |
| `junkScaterrers/BurrowWall/groupDistRange` | 3.0% (1/33) | 文本 | 5~8 |
| `junkScaterrers/BurrowWall/groupsPerHundredCells` | 3.0% (1/33) | 文本 | 2~3 |
| `junkScaterrers/BurrowWall/itemsPerGroup` | 3.0% (1/33) | 文本 | 5~15 |
| `junkScaterrers/ChunkMechanoidSlag` | 6.1% (2/33) | 容器 |  |
| `junkScaterrers/ChunkMechanoidSlag/groupDistRange` | 6.1% (2/33) | 文本 | 5~6 |
| `junkScaterrers/ChunkMechanoidSlag/groupsPerHundredCells` | 6.1% (2/33) | 文本 | 1~2 |
| `junkScaterrers/ChunkMechanoidSlag/itemsPerGroup` | 6.1% (2/33) | 文本 | 2~4 |
| `junkScaterrers/ChunkSlagSteel` | 3.0% (1/33) | 容器 |  |
| `junkScaterrers/ChunkSlagSteel/groupsPerHundredCells` | 3.0% (1/33) | 文本 | -2~1 |
| `junkScaterrers/ChunkSlagSteel/itemsPerGroup` | 3.0% (1/33) | 文本 | 1~1 |
| `junkScaterrers/Filth_BlastMark` | 21.2% (7/33) | 容器 |  |
| `junkScaterrers/Filth_BlastMark/groupsPerHundredCells` | 21.2% (7/33) | 文本 | -2~1 |
| `junkScaterrers/Filth_BlastMark/itemsPerGroup` | 21.2% (7/33) | 文本 | 1~1 |
| `junkScaterrers/Filth_BloodInsect` | 3.0% (1/33) | 容器 |  |
| `junkScaterrers/Filth_BloodInsect/groupDistRange` | 3.0% (1/33) | 文本 | 3~5 |
| `junkScaterrers/Filth_BloodInsect/groupsPerHundredCells` | 3.0% (1/33) | 文本 | 0~1 |
| `junkScaterrers/Filth_BloodInsect/itemsPerGroup` | 3.0% (1/33) | 文本 | 2~4 |
| `junkScaterrers/Filth_ChemfuelStain` | 3.0% (1/33) | 容器 |  |
| `junkScaterrers/Filth_ChemfuelStain/groupDistRange` | 3.0% (1/33) | 文本 | 3~5 |
| `junkScaterrers/Filth_ChemfuelStain/groupsPerHundredCells` | 3.0% (1/33) | 文本 | 2~3 |
| `junkScaterrers/Filth_ChemfuelStain/itemsPerGroup` | 3.0% (1/33) | 文本 | 1~2 |
| `junkScaterrers/Filth_MachineBits` | 24.2% (8/33) | 容器 |  |
| `junkScaterrers/Filth_MachineBits/groupDistRange` | 24.2% (8/33) | 文本 | 2~4 |
| `junkScaterrers/Filth_MachineBits/groupsPerHundredCells` | 24.2% (8/33) | 文本 | -1~1 / 0~3 |
| `junkScaterrers/Filth_MachineBits/itemsPerGroup` | 24.2% (8/33) | 文本 | 2~4 |
| `junkScaterrers/Filth_MoldyUniform` | 3.0% (1/33) | 容器 |  |
| `junkScaterrers/Filth_MoldyUniform/groupDistRange` | 3.0% (1/33) | 文本 | 3~5 |
| `junkScaterrers/Filth_MoldyUniform/groupsPerHundredCells` | 3.0% (1/33) | 文本 | 1~2 |
| `junkScaterrers/Filth_MoldyUniform/itemsPerGroup` | 3.0% (1/33) | 文本 | 1~2 |
| `junkScaterrers/Filth_OilSmear` | 12.1% (4/33) | 容器 |  |
| `junkScaterrers/Filth_OilSmear/groupDistRange` | 12.1% (4/33) | 文本 | 3~5 |
| `junkScaterrers/Filth_OilSmear/groupsPerHundredCells` | 12.1% (4/33) | 文本 | 0~1 / 0~3 |
| `junkScaterrers/Filth_OilSmear/itemsPerGroup` | 12.1% (4/33) | 文本 | 2~4 |
| `junkScaterrers/Filth_RubbleRock` | 36.4% (12/33) | 容器 |  |
| `junkScaterrers/Filth_RubbleRock/groupDistRange` | 36.4% (12/33) | 文本 | 3~5 |
| `junkScaterrers/Filth_RubbleRock/groupsPerHundredCells` | 36.4% (12/33) | 文本 | 1~2 / 1~3 / 2~4 |
| `junkScaterrers/Filth_RubbleRock/itemsPerGroup` | 36.4% (12/33) | 文本 | 3~5 / 3~8 |
| `junkScaterrers/Filth_RubbleRock/minGroups` | 12.1% (4/33) | 数值 | 1 |
| `junkScaterrers/Filth_ScatteredDocuments` | 6.1% (2/33) | 容器 |  |
| `junkScaterrers/Filth_ScatteredDocuments/groupDistRange` | 6.1% (2/33) | 文本 | 3~5 |
| `junkScaterrers/Filth_ScatteredDocuments/groupsPerHundredCells` | 6.1% (2/33) | 文本 | 1~1 / 2~4 |
| `junkScaterrers/Filth_ScatteredDocuments/itemsPerGroup` | 6.1% (2/33) | 文本 | 1~1 / 1~3 |
| `junkScaterrers/Filth_ScatteredDocuments/minGroups` | 3.0% (1/33) | 数值 | 1 |
| `junkScaterrers/Filth_Trash` | 15.2% (5/33) | 容器 |  |
| `junkScaterrers/Filth_Trash/groupDistRange` | 15.2% (5/33) | 文本 | 3~5 |
| `junkScaterrers/Filth_Trash/groupsPerHundredCells` | 15.2% (5/33) | 文本 | 0~3 |
| `junkScaterrers/Filth_Trash/itemsPerGroup` | 15.2% (5/33) | 文本 | 2~4 |
| `junkScaterrers/GlowPod` | 3.0% (1/33) | 容器 |  |
| `junkScaterrers/GlowPod/groupDistRange` | 3.0% (1/33) | 文本 | 3~5 |
| `junkScaterrers/GlowPod/groupsPerHundredCells` | 3.0% (1/33) | 文本 | 1~2 |
| `junkScaterrers/GlowPod/itemsPerGroup` | 3.0% (1/33) | 数值 | 1 |
| `junkScaterrers/Granite` | 3.0% (1/33) | 容器 |  |
| `junkScaterrers/Granite/groupDistRange` | 3.0% (1/33) | 文本 | 1~2 |
| `junkScaterrers/Granite/groupsPerHundredCells` | 3.0% (1/33) | 文本 | 1~2 |
| `junkScaterrers/Granite/itemsPerGroup` | 3.0% (1/33) | 文本 | 3~8 |
| `junkScaterrers/Granite/minGroups` | 3.0% (1/33) | 数值 | 1 |
| `junkScaterrers/RubblePile` | 30.3% (10/33) | 容器 |  |
| `junkScaterrers/RubblePile/groupDistRange` | 30.3% (10/33) | 文本 | 3~5 / 5~6 |
| `junkScaterrers/RubblePile/groupsPerHundredCells` | 30.3% (10/33) | 文本 | 1~2 / 1~3 / 2~4 |
| `junkScaterrers/RubblePile/itemsPerGroup` | 30.3% (10/33) | 文本 | 2~4 |
| `junkScaterrers/RubblePile/minGroups` | 12.1% (4/33) | 数值 | 1 |
| `junkScaterrers/SolidIce` | 3.0% (1/33) | 容器 |  |
| `junkScaterrers/SolidIce/groupDistRange` | 3.0% (1/33) | 文本 | 1~2 |
| `junkScaterrers/SolidIce/groupsPerHundredCells` | 3.0% (1/33) | 文本 | 5~10 |
| `junkScaterrers/SolidIce/itemsPerGroup` | 3.0% (1/33) | 文本 | 7~8 |
| `junkScaterrers/SolidIce/minGroups` | 3.0% (1/33) | 数值 | 1 |
| `minRoomHeight` | 33.3% (11/33) | 数值 | 10 / 8 / 9 |
| `minRoomWidth` | 33.3% (11/33) | 数值 | 10 / 7 / 8 |
| `parts` | 24.2% (8/33) | 容器 |  |
| `parts/Breached` | 21.2% (7/33) | 数值 | 0.05 / 0.1 / 0.25 |
| `parts/Gore` | 24.2% (8/33) | 数值 | 0.1 / 0.15 / 0.2 |
| `roomDefs` | 81.8% (27/33) | 容器 |  |
| `roomDefs/AncientCanteen` | 9.1% (3/33) | 数值 | 0.5 / 0.75 / 2 |
| `roomDefs/AncientChemfuelRefineryExplosivesRoom` | 3.0% (1/33) | 数值 | 2 |
| `roomDefs/AncientChemfuelRefineryProductionRoom` | 3.0% (1/33) | 容器 |  |
| `roomDefs/AncientChemfuelRefineryProductionRoom/countRange` | 3.0% (1/33) | 文本 | 1~2 |
| `roomDefs/AncientChemfuelRefineryWorkshop` | 3.0% (1/33) | 数值 | 2 |
| `roomDefs/AncientChemfuelStorage` | 6.1% (2/33) | 容器 |  |
| `roomDefs/AncientChemfuelStorage/countRange` | 6.1% (2/33) | 数值 | 1 |
| `roomDefs/AncientComputerRoom` | 21.2% (7/33) | 数值 | 0.5 / 1 |
| `roomDefs/AncientComputerRoom/countRange` | 6.1% (2/33) | 数值/文本 | 0~2 / 1 |
| `roomDefs/AncientCryptosleepRoom_Hostile` | 12.1% (4/33) | 容器 |  |
| `roomDefs/AncientCryptosleepRoom_Hostile/countRange` | 12.1% (4/33) | 文本 | 0~1 / 1~2 |
| `roomDefs/AncientGarrisonBarracks` | 3.0% (1/33) | 数值 | 1 |
| `roomDefs/AncientGarrisonShellStorageRoom` | 3.0% (1/33) | 容器 |  |
| `roomDefs/AncientGarrisonShellStorageRoom/countRange` | 3.0% (1/33) | 数值 | 1 |
| `roomDefs/AncientLivingArea` | 15.2% (5/33) | 数值 | 0.25 / 0.5 / 1 |
| `roomDefs/AncientOrbitalUplink` | 27.3% (9/33) | 数值 | 0.05 / 0.1 |
| `roomDefs/AncientOrbitalUplink/countRange` | 6.1% (2/33) | 文本 | 0~1 / 1~1 |
| `roomDefs/AncientRuinsBarracks` | 15.2% (5/33) | 数值 | 0.75 / 1 |
| `roomDefs/AncientRuinsChemfuelBarrelRoom` | 6.1% (2/33) | 数值 | 1 |
| `roomDefs/AncientRuinsChemfuelWorkshop` | 15.2% (5/33) | 数值 | 1 / 2 |
| `roomDefs/AncientRuinsChemfuelWorkshop/countRange` | 3.0% (1/33) | 文本 | 1~2 |
| `roomDefs/AncientRuinsCryptosleepCasket` | 9.1% (3/33) | 数值 | 0.05 / 0.2 / 0.25 |
| `roomDefs/AncientRuinsCryptosleepCasketNoThreat` | 9.1% (3/33) | 容器/数值 | 0.05 / 0.25 |
| `roomDefs/AncientRuinsDiningHall` | 12.1% (4/33) | 数值 | 1 |
| `roomDefs/AncientRuinsEmpty` | 6.1% (2/33) | 数值 | 4 / 5 |
| `roomDefs/AncientRuinsFrozenChemfuelWorkshop` | 6.1% (2/33) | 数值 | 1 / 2 |
| `roomDefs/AncientRuinsFrozenGravliteStoreRoom` | 3.0% (1/33) | 容器 |  |
| `roomDefs/AncientRuinsFrozenGravliteStoreRoom/countRange` | 3.0% (1/33) | 文本 | 1~1 |
| `roomDefs/AncientRuinsFrozenLab` | 6.1% (2/33) | 数值 | 1 / 2 |
| `roomDefs/AncientRuinsFrozenLivingQuarters` | 6.1% (2/33) | 数值 | 2 |
| `roomDefs/AncientRuinsFrozenLivingQuarters/countRange` | 3.0% (1/33) | 文本 | 1~2 |
| `roomDefs/AncientRuinsFrozenOperationRoom` | 6.1% (2/33) | 数值 | 0.5 |
| `roomDefs/AncientRuinsFrozenOperationRoom/countRange` | 3.0% (1/33) | 文本 | 1~1 |
| `roomDefs/AncientRuinsFrozenStorageRoom` | 6.1% (2/33) | 数值 | 1 / 2 |
| `roomDefs/AncientRuinsIndustrialStorage` | 15.2% (5/33) | 数值 | 0.5 / 1 / 2 |
| `roomDefs/AncientRuinsInsectHive` | 6.1% (2/33) | 数值 | 0.1 / 0.2 |
| `roomDefs/AncientRuinsInsectHive_Underground` | 6.1% (2/33) | 数值 | 0.1 / 0.5 |
| `roomDefs/AncientRuinsKitchen` | 12.1% (4/33) | 数值 | 1 |
| `roomDefs/AncientRuinsLockerRoom` | 6.1% (2/33) | 数值 | 1 / 2 |
| `roomDefs/AncientRuinsMechsWithLoot` | 12.1% (4/33) | 数值 | 0.1 / 0.3 / 0.4 |
| `roomDefs/AncientRuinsOperatingRoom` | 12.1% (4/33) | 数值 | 1 |
| `roomDefs/AncientRuinsReactorGravliteStoreRoom` | 3.0% (1/33) | 容器 |  |
| `roomDefs/AncientRuinsReactorGravliteStoreRoom/countRange` | 3.0% (1/33) | 文本 | 1~1 |
| `roomDefs/AncientRuinsReactorToxicWaterRoom` | 6.1% (2/33) | 数值 | 0.15 / 2 |
| `roomDefs/AncientRuinsRubble` | 12.1% (4/33) | 数值 | 2 / 3 |
| `roomDefs/AncientRuinsSecureRoom` | 9.1% (3/33) | 数值 | 1 |
| `roomDefs/AncientRuinsShelfRoom` | 15.2% (5/33) | 数值 | 1 / 4 |
| `roomDefs/AncientRuinsShelfRoomWithLoot` | 12.1% (4/33) | 数值 | 0.05 / 0.1 |
| `roomDefs/AncientRuinsShelfWithLootRoom` | 6.1% (2/33) | 容器 |  |
| `roomDefs/AncientRuinsShelfWithLootRoom/countRange` | 6.1% (2/33) | 数值/文本 | 0~1 / 1 |
| `roomDefs/AncientRuinsShelfWithLootRoom_Underground` | 6.1% (2/33) | 数值 | 1 |
| `roomDefs/AncientRuinsShelfWithLootRoom_Underground/countRange` | 3.0% (1/33) | 文本 | 1~2 |
| `roomDefs/AncientRuinsStorage` | 12.1% (4/33) | 数值 | 1 / 2 |
| `roomDefs/AncientSatelliteEquipmentBlockRoom` | 3.0% (1/33) | 数值 | 0.75 |
| `roomDefs/AncientSatelliteLootRoom` | 3.0% (1/33) | 容器 |  |
| `roomDefs/AncientSatelliteLootRoom/countRange` | 3.0% (1/33) | 文本 | 1~1 |
| `roomDefs/AncientSatelliteMachineRoom` | 3.0% (1/33) | 数值 | 1 |
| `roomDefs/AncientSatelliteSecondaryLootRoom` | 3.0% (1/33) | 容器 |  |
| `roomDefs/AncientSatelliteSecondaryLootRoom/countRange` | 3.0% (1/33) | 文本 | 1~1 |
| `roomDefs/AncientSatelliteSystemRoom` | 3.0% (1/33) | 数值 | 0.75 |
| `roomDefs/AncientSatelliteVentRoom` | 3.0% (1/33) | 容器 |  |
| `roomDefs/AncientSatelliteVentRoom/countRange` | 3.0% (1/33) | 文本 | 0~2 |
| `roomDefs/AncientSleepingArea` | 15.2% (5/33) | 数值 | 1 |
| `roomDefs/AncientStockpileEntrance` | 3.0% (1/33) | 容器 |  |
| `roomDefs/AncientStockpileEntrance/countRange` | 3.0% (1/33) | 数值 | 1 |
| `roomDefs/AncientStockpileSecurityRoom` | 3.0% (1/33) | 数值 | 0.25 |
| `roomDefs/AncientStockpileStockpile` | 3.0% (1/33) | 容器 |  |
| `roomDefs/AncientStockpileStockpile/countRange` | 3.0% (1/33) | 数值 | 1 |
| `roomDefs/AncientWarehousePalletRoom` | 3.0% (1/33) | 数值 | 1 |
| `roomDefs/AncientWarehouseStorageRoom` | 3.0% (1/33) | 数值 | 2 |
| `roomDefs/AncientWeaponStorage` | 3.0% (1/33) | 容器 |  |
| `roomDefs/AncientWeaponStorage/countRange` | 3.0% (1/33) | 数值 | 1 |
| `roomDefs/AncientWorkshop` | 3.0% (1/33) | 数值 | 1 |
| `roomDefs/InfestedColonyBedroom` | 3.0% (1/33) | 容器 |  |
| `roomDefs/InfestedColonyBedroom/countRange` | 3.0% (1/33) | 文本 | 1~3 |
| `roomDefs/InfestedHiveEntrance` | 3.0% (1/33) | 容器 |  |
| `roomDefs/InfestedHiveEntrance/countRange` | 3.0% (1/33) | 文本 | 1~1 |
| `roomDefs/InfestedKitchen` | 3.0% (1/33) | 数值 | 1 |
| `roomDefs/InfestedLootRoom` | 3.0% (1/33) | 容器 |  |
| `roomDefs/InfestedLootRoom/countRange` | 3.0% (1/33) | 文本 | 1~1 |
| `roomDefs/InfestedOperationRoom` | 3.0% (1/33) | 数值 | 1 |
| `roomDefs/InfestedRecRoom` | 3.0% (1/33) | 数值 | 1 |
| `roomDefs/InfestedWorkshop` | 3.0% (1/33) | 数值 | 1 |
| `roomDefs/InnerCourtyard` | 15.2% (5/33) | 数值 | 0.3 / 0.5 / 0.65 |
| `roomDefs/InnerCourtyardRooms` | 18.2% (6/33) | 数值 | 0.25 / 0.75 / 1 |
| `roomDefs/InnerCourtyardRooms/countRange` | 6.1% (2/33) | 数值/文本 | 0~1 / 5 |
| `roomDefs/LaunchPad` | 6.1% (2/33) | 容器 |  |
| `roomDefs/LaunchPad/countRange` | 6.1% (2/33) | 数值/文本 | 1 / 1~1 |
| `roomDefs/MechChargingRoom` | 12.1% (4/33) | 容器 |  |
| `roomDefs/MechChargingRoom/countRange` | 12.1% (4/33) | 数值/文本 | 1 / 1~2 |
| `roomDefs/MechGestationRoom` | 15.2% (5/33) | 数值 | 1 |
| `roomDefs/MechGloomlightRoom` | 12.1% (4/33) | 数值 | 0.25 / 1 |
| `roomDefs/MechGravlitePanelRoom` | 6.1% (2/33) | 容器 |  |
| `roomDefs/MechGravlitePanelRoom/countRange` | 6.1% (2/33) | 数值 | 1 |
| `roomDefs/MechLootRoom` | 3.0% (1/33) | 容器 |  |
| `roomDefs/MechLootRoom/countRange` | 3.0% (1/33) | 文本 | 1~1 |
| `roomDefs/MechProcessorRoom` | 15.2% (5/33) | 数值 | 1 |
| `roomDefs/MechStorageRoom` | 12.1% (4/33) | 数值 | 0.5 / 0.75 / 1.4 |
| `roomDefs/NarrowHalls` | 21.2% (7/33) | 数值 | 1 / 1.5 / 2.25 |
| `roomDefs/OrbitalBarracks` | 9.1% (3/33) | 数值 | 1 |
| `roomDefs/OrbitalComputerRoom` | 9.1% (3/33) | 数值 | 1 |
| `roomDefs/OrbitalDiningRoom` | 9.1% (3/33) | 数值 | 1 |
| `roomDefs/OrbitalHydroponics` | 9.1% (3/33) | 数值 | 1 |
| `roomDefs/OrbitalItemStash_ItemRoom` | 3.0% (1/33) | 容器 |  |
| `roomDefs/OrbitalItemStash_ItemRoom/countRange` | 3.0% (1/33) | 数值 | 1 |
| `roomDefs/OrbitalNursery` | 9.1% (3/33) | 容器 |  |
| `roomDefs/OrbitalNursery/countRange` | 9.1% (3/33) | 文本 | 1~1 |
| `roomDefs/OrbitalRuinsAdvancedComponentRoom` | 3.0% (1/33) | 数值 | 0.5 |
| `roomDefs/OrbitalRuinsComputerRoom` | 3.0% (1/33) | 数值 | 0.2 |
| `roomDefs/OrbitalRuinsDestroyedFloor` | 3.0% (1/33) | 数值 | 1.75 |
| `roomDefs/OrbitalRuinsHermeticCrate` | 3.0% (1/33) | 容器 |  |
| `roomDefs/OrbitalRuinsHermeticCrate/countRange` | 3.0% (1/33) | 文本 | 0~1 |
| `roomDefs/OrbitalRuinsLootroom` | 3.0% (1/33) | 数值 | 0.15 |
| `roomDefs/OrbitalRuinsShelves` | 3.0% (1/33) | 数值 | 2 |
| `roomDefs/OrbitalRuinsSteelRoom` | 3.0% (1/33) | 数值 | 0.5 |
| `roomDefs/OrbitalRuinsStoreroom` | 3.0% (1/33) | 数值 | 1.5 |
| `roomDefs/OrbitalStoreroom` | 9.1% (3/33) | 数值 | 2 |
| `roomDefs/OrbitalStoreroom_GravshipUpgrade` | 6.1% (2/33) | 数值 | 0.1 |
| `roomDefs/OrbitalStoreroom_GravshipUpgrade/countRange` | 3.0% (1/33) | 文本 | 1~1 |
| `roomDefs/OrbitalStoreroom_Loot` | 3.0% (1/33) | 容器 |  |
| `roomDefs/OrbitalStoreroom_Loot/countRange` | 3.0% (1/33) | 文本 | 1~1 |
| `roomDefs/OrbitalTransportRoom` | 15.2% (5/33) | 数值 | 0.5 / 1 |
| `roomDefs/OrbitalWreckRubble` | 3.0% (1/33) | 数值 | 0.5 |
| `roomDefs/RecRoom` | 12.1% (4/33) | 容器 |  |
| `roomDefs/RecRoom/countRange` | 12.1% (4/33) | 数值/文本 | 1 / 1~1 |
| `roomToExteriorDoorRatio` | 6.1% (2/33) | 数值 | 0 / 0.05 |
| `scatteredPrefabs` | 3.0% (1/33) | 容器 |  |
| `scatteredPrefabs/li` | 3.0% (1/33) | 容器 |  |
| `scatteredPrefabs/li/countPer10kCellsRange` | 3.0% (1/33) | 文本 | 0.5~0.7 |
| `scatteredPrefabs/li/maxDistFromStructure` | 3.0% (1/33) | 数值 | 50 |
| `scatteredPrefabs/li/minSpacing` | 3.0% (1/33) | 数值 | 10 |
| `scatteredPrefabs/li/prefabs` | 3.0% (1/33) | 容器 |  |
| `scatteredPrefabs/li/prefabs/Exterior_AncientBunker` | 3.0% (1/33) | 容器 |  |
| `scatteredPrefabs/li/prefabs/Exterior_AncientBunker/filthChance` | 3.0% (1/33) | 数值 | 0.4 |
| `scatteredPrefabs/li/prefabs/Exterior_AncientBunker/filthDef` | 3.0% (1/33) | 文本 | Filth_RubbleRock |
| `scatteredPrefabs/li/prefabs/Exterior_AncientBunker/filthExpandBy` | 3.0% (1/33) | 数值 | 1 |
| `scatteredPrefabs/li/prefabs/Exterior_AncientBunker/indoorRuin` | 3.0% (1/33) | 布尔 | false |
| `scatteredPrefabs/li/prefabs/Exterior_AncientBunker/max` | 3.0% (1/33) | 数值 | 2 |
| `scatteredPrefabs/li/prefabs/Exterior_AncientBunker/weight` | 3.0% (1/33) | 数值 | 0.25 |
| `scatteredPrefabs/li/prefabs/Exterior_AncientContainerForklift` | 3.0% (1/33) | 容器 |  |
| `scatteredPrefabs/li/prefabs/Exterior_AncientContainerForklift/filthChance` | 3.0% (1/33) | 数值 | 0.4 |
| `scatteredPrefabs/li/prefabs/Exterior_AncientContainerForklift/filthDef` | 3.0% (1/33) | 文本 | Filth_RubbleRock |
| `scatteredPrefabs/li/prefabs/Exterior_AncientContainerForklift/filthExpandBy` | 3.0% (1/33) | 数值 | 1 |
| `scatteredPrefabs/li/prefabs/Exterior_AncientContainerForklift/indoorRuin` | 3.0% (1/33) | 布尔 | false |
| `scatteredPrefabs/li/prefabs/Exterior_AncientContainerForklift/max` | 3.0% (1/33) | 数值 | 1 |
| `scatteredPrefabs/li/prefabs/Exterior_AncientContainerForklift/weight` | 3.0% (1/33) | 数值 | 1.0 |
| `scatteredPrefabs/li/prefabs/Exterior_AncientMegaCannonEmplacement` | 3.0% (1/33) | 容器 |  |
| `scatteredPrefabs/li/prefabs/Exterior_AncientMegaCannonEmplacement/filthChance` | 3.0% (1/33) | 数值 | 0.4 |
| `scatteredPrefabs/li/prefabs/Exterior_AncientMegaCannonEmplacement/filthDef` | 3.0% (1/33) | 文本 | Filth_RubbleRock |
| `scatteredPrefabs/li/prefabs/Exterior_AncientMegaCannonEmplacement/filthExpandBy` | 3.0% (1/33) | 数值 | 1 |
| `scatteredPrefabs/li/prefabs/Exterior_AncientMegaCannonEmplacement/indoorRuin` | 3.0% (1/33) | 布尔 | false |
| `scatteredPrefabs/li/prefabs/Exterior_AncientMegaCannonEmplacement/max` | 3.0% (1/33) | 数值 | 2 |
| `scatteredPrefabs/li/prefabs/Exterior_AncientMegaCannonEmplacement/weight` | 3.0% (1/33) | 数值 | 0.25 |
| `scatteredPrefabs/li/prefabs/Exterior_AncientRoad_Long` | 3.0% (1/33) | 容器 |  |
| `scatteredPrefabs/li/prefabs/Exterior_AncientRoad_Long/filthChance` | 3.0% (1/33) | 数值 | 0.4 |
| `scatteredPrefabs/li/prefabs/Exterior_AncientRoad_Long/filthDef` | 3.0% (1/33) | 文本 | Filth_RubbleRock |
| `scatteredPrefabs/li/prefabs/Exterior_AncientRoad_Long/filthExpandBy` | 3.0% (1/33) | 数值 | 1 |
| `scatteredPrefabs/li/prefabs/Exterior_AncientRoad_Long/indoorRuin` | 3.0% (1/33) | 布尔 | false |
| `scatteredPrefabs/li/prefabs/Exterior_AncientRoad_Long/max` | 3.0% (1/33) | 数值 | 2 |
| `scatteredPrefabs/li/prefabs/Exterior_AncientRoad_Long/weight` | 3.0% (1/33) | 数值 | 1.0 |
| `scatteredPrefabs/li/prefabs/Exterior_AncientTank_Cluster` | 3.0% (1/33) | 容器 |  |
| `scatteredPrefabs/li/prefabs/Exterior_AncientTank_Cluster/filthChance` | 3.0% (1/33) | 数值 | 0.4 |
| `scatteredPrefabs/li/prefabs/Exterior_AncientTank_Cluster/filthDef` | 3.0% (1/33) | 文本 | Filth_RubbleRock |
| `scatteredPrefabs/li/prefabs/Exterior_AncientTank_Cluster/filthExpandBy` | 3.0% (1/33) | 数值 | 1 |
| `scatteredPrefabs/li/prefabs/Exterior_AncientTank_Cluster/indoorRuin` | 3.0% (1/33) | 布尔 | false |
| `scatteredPrefabs/li/prefabs/Exterior_AncientTank_Cluster/max` | 3.0% (1/33) | 数值 | 2 |
| `scatteredPrefabs/li/prefabs/Exterior_AncientTank_Cluster/weight` | 3.0% (1/33) | 数值 | 1.0 |
| `scatteredPrefabs/li/prefabs/Exterior_AncientTankBlockade` | 3.0% (1/33) | 容器 |  |
| `scatteredPrefabs/li/prefabs/Exterior_AncientTankBlockade/filthChance` | 3.0% (1/33) | 数值 | 0.4 |
| `scatteredPrefabs/li/prefabs/Exterior_AncientTankBlockade/filthDef` | 3.0% (1/33) | 文本 | Filth_RubbleRock |
| `scatteredPrefabs/li/prefabs/Exterior_AncientTankBlockade/filthExpandBy` | 3.0% (1/33) | 数值 | 1 |
| `scatteredPrefabs/li/prefabs/Exterior_AncientTankBlockade/indoorRuin` | 3.0% (1/33) | 布尔 | false |
| `scatteredPrefabs/li/prefabs/Exterior_AncientTankBlockade/max` | 3.0% (1/33) | 数值 | 2 |
| `scatteredPrefabs/li/prefabs/Exterior_AncientTankBlockade/weight` | 3.0% (1/33) | 数值 | 1.0 |
| `scatteredPrefabs/li/prefabs/Exterior_AncientTankTraps` | 3.0% (1/33) | 容器 |  |
| `scatteredPrefabs/li/prefabs/Exterior_AncientTankTraps/filthChance` | 3.0% (1/33) | 数值 | 0.4 |
| `scatteredPrefabs/li/prefabs/Exterior_AncientTankTraps/filthDef` | 3.0% (1/33) | 文本 | Filth_RubbleRock |
| `scatteredPrefabs/li/prefabs/Exterior_AncientTankTraps/filthExpandBy` | 3.0% (1/33) | 数值 | 1 |
| `scatteredPrefabs/li/prefabs/Exterior_AncientTankTraps/indoorRuin` | 3.0% (1/33) | 布尔 | false |
| `scatteredPrefabs/li/prefabs/Exterior_AncientTankTraps/max` | 3.0% (1/33) | 数值 | 2 |
| `scatteredPrefabs/li/prefabs/Exterior_AncientTankTraps/weight` | 3.0% (1/33) | 数值 | 1.0 |
| `scatteredPrefabs/li/prefabs/Exterior_ChembarrelStorage` | 3.0% (1/33) | 容器 |  |
| `scatteredPrefabs/li/prefabs/Exterior_ChembarrelStorage/filthChance` | 3.0% (1/33) | 数值 | 0.4 |
| `scatteredPrefabs/li/prefabs/Exterior_ChembarrelStorage/filthDef` | 3.0% (1/33) | 文本 | Filth_RubbleRock |
| `scatteredPrefabs/li/prefabs/Exterior_ChembarrelStorage/filthExpandBy` | 3.0% (1/33) | 数值 | 1 |
| `scatteredPrefabs/li/prefabs/Exterior_ChembarrelStorage/indoorRuin` | 3.0% (1/33) | 布尔 | false |
| `scatteredPrefabs/li/prefabs/Exterior_ChembarrelStorage/max` | 3.0% (1/33) | 数值 | 2 |
| `scatteredPrefabs/li/prefabs/Exterior_ChembarrelStorage/weight` | 3.0% (1/33) | 数值 | 1.0 |
| `scatteredPrefabs/li/prefabs/Exterior_ChemtruckParkingLot` | 3.0% (1/33) | 容器 |  |
| `scatteredPrefabs/li/prefabs/Exterior_ChemtruckParkingLot/filthChance` | 3.0% (1/33) | 数值 | 0.4 |
| `scatteredPrefabs/li/prefabs/Exterior_ChemtruckParkingLot/filthDef` | 3.0% (1/33) | 文本 | Filth_RubbleRock |
| `scatteredPrefabs/li/prefabs/Exterior_ChemtruckParkingLot/filthExpandBy` | 3.0% (1/33) | 数值 | 1 |
| `scatteredPrefabs/li/prefabs/Exterior_ChemtruckParkingLot/indoorRuin` | 3.0% (1/33) | 布尔 | false |
| `scatteredPrefabs/li/prefabs/Exterior_ChemtruckParkingLot/max` | 3.0% (1/33) | 数值 | 2 |
| `scatteredPrefabs/li/prefabs/Exterior_ChemtruckParkingLot/weight` | 3.0% (1/33) | 数值 | 1.0 |
| `scatteredPrefabs/li/prefabs/Exterior_ChemtruckParkingLot_Long` | 3.0% (1/33) | 容器 |  |
| `scatteredPrefabs/li/prefabs/Exterior_ChemtruckParkingLot_Long/filthChance` | 3.0% (1/33) | 数值 | 0.4 |
| `scatteredPrefabs/li/prefabs/Exterior_ChemtruckParkingLot_Long/filthDef` | 3.0% (1/33) | 文本 | Filth_RubbleRock |
| `scatteredPrefabs/li/prefabs/Exterior_ChemtruckParkingLot_Long/filthExpandBy` | 3.0% (1/33) | 数值 | 1 |
| `scatteredPrefabs/li/prefabs/Exterior_ChemtruckParkingLot_Long/indoorRuin` | 3.0% (1/33) | 布尔 | false |
| `scatteredPrefabs/li/prefabs/Exterior_ChemtruckParkingLot_Long/max` | 3.0% (1/33) | 数值 | 2 |
| `scatteredPrefabs/li/prefabs/Exterior_ChemtruckParkingLot_Long/weight` | 3.0% (1/33) | 数值 | 1.0 |
| `scatteredPrefabs/li/prefabs/Exterior_ContainerSite` | 3.0% (1/33) | 容器 |  |
| `scatteredPrefabs/li/prefabs/Exterior_ContainerSite/filthChance` | 3.0% (1/33) | 数值 | 0.4 |
| `scatteredPrefabs/li/prefabs/Exterior_ContainerSite/filthDef` | 3.0% (1/33) | 文本 | Filth_RubbleRock |
| `scatteredPrefabs/li/prefabs/Exterior_ContainerSite/filthExpandBy` | 3.0% (1/33) | 数值 | 1 |
| `scatteredPrefabs/li/prefabs/Exterior_ContainerSite/indoorRuin` | 3.0% (1/33) | 布尔 | false |
| `scatteredPrefabs/li/prefabs/Exterior_ContainerSite/max` | 3.0% (1/33) | 数值 | 2 |
| `scatteredPrefabs/li/prefabs/Exterior_ContainerSite/weight` | 3.0% (1/33) | 数值 | 1.0 |
| `scatteredPrefabs/li/prefabs/Exterior_CrashedCrane` | 3.0% (1/33) | 容器 |  |
| `scatteredPrefabs/li/prefabs/Exterior_CrashedCrane/filthChance` | 3.0% (1/33) | 数值 | 0.4 |
| `scatteredPrefabs/li/prefabs/Exterior_CrashedCrane/filthDef` | 3.0% (1/33) | 文本 | Filth_RubbleRock |
| `scatteredPrefabs/li/prefabs/Exterior_CrashedCrane/filthExpandBy` | 3.0% (1/33) | 数值 | 1 |
| `scatteredPrefabs/li/prefabs/Exterior_CrashedCrane/indoorRuin` | 3.0% (1/33) | 布尔 | false |
| `scatteredPrefabs/li/prefabs/Exterior_CrashedCrane/max` | 3.0% (1/33) | 数值 | 1 |
| `scatteredPrefabs/li/prefabs/Exterior_CrashedCrane/weight` | 3.0% (1/33) | 数值 | 1.0 |
| `scatteredPrefabs/li/prefabs/Exterior_FourSmallBuildings` | 3.0% (1/33) | 容器 |  |
| `scatteredPrefabs/li/prefabs/Exterior_FourSmallBuildings/filthChance` | 3.0% (1/33) | 数值 | 0.4 |
| `scatteredPrefabs/li/prefabs/Exterior_FourSmallBuildings/filthDef` | 3.0% (1/33) | 文本 | Filth_RubbleRock |
| `scatteredPrefabs/li/prefabs/Exterior_FourSmallBuildings/filthExpandBy` | 3.0% (1/33) | 数值 | 1 |
| `scatteredPrefabs/li/prefabs/Exterior_FourSmallBuildings/indoorRuin` | 3.0% (1/33) | 布尔 | false |
| `scatteredPrefabs/li/prefabs/Exterior_FourSmallBuildings/max` | 3.0% (1/33) | 数值 | 1 |
| `scatteredPrefabs/li/prefabs/Exterior_FourSmallBuildings/weight` | 3.0% (1/33) | 数值 | 0.2 |
| `scatteredPrefabs/li/prefabs/Exterior_MilitaryBlockade` | 3.0% (1/33) | 容器 |  |
| `scatteredPrefabs/li/prefabs/Exterior_MilitaryBlockade/filthChance` | 3.0% (1/33) | 数值 | 0.4 |
| `scatteredPrefabs/li/prefabs/Exterior_MilitaryBlockade/filthDef` | 3.0% (1/33) | 文本 | Filth_RubbleRock |
| `scatteredPrefabs/li/prefabs/Exterior_MilitaryBlockade/filthExpandBy` | 3.0% (1/33) | 数值 | 1 |
| `scatteredPrefabs/li/prefabs/Exterior_MilitaryBlockade/indoorRuin` | 3.0% (1/33) | 布尔 | false |
| `scatteredPrefabs/li/prefabs/Exterior_MilitaryBlockade/max` | 3.0% (1/33) | 数值 | 2 |
| `scatteredPrefabs/li/prefabs/Exterior_MilitaryBlockade/weight` | 3.0% (1/33) | 数值 | 1.0 |
| `shouldDamage` | 12.1% (4/33) | 布尔 | true |
| `surroundingScatterTerrainDef` | 3.0% (1/33) | 文本 | PackedDirt |
| `surroundingTerrainDef` | 12.1% (4/33) | 容器/文本 | MechanoidPlatform |
| `terrainDef` | 9.1% (3/33) | 文本 | MechanoidPlatform / OrbitalPlatform |
| `wallAttachments` | 9.1% (3/33) | 容器 |  |
| `wallAttachments/LifeSupportUnit` | 9.1% (3/33) | 容器 |  |
| `wallAttachments/LifeSupportUnit/countRange` | 9.1% (3/33) | 文本 | 1~1 |
| `wallDamageRange` | 6.1% (2/33) | 文本 | 500~1000 |
| `wallDef` | 18.2% (6/33) | 文本 | AncientFortifiedWall / OrbitalAncientFortifiedWall |
| `wallLampChancePerPosition` | 12.1% (4/33) | 数值 | 0 / 0.7 / 1 |
| `wallLampDef` | 36.4% (12/33) | 文本 | AncientEmergencyLight_Blue / AncientEmergencyLight_Green / AncientEmergencyLight_Red |
| `workerClass` | 51.5% (17/33) | 文本 | LayoutWorker_AncientRuins / LayoutWorker_AncientRuins_Reactor / LayoutWorker_AncientRuins_Terraformer |

## 四、原版 defName 一览（共 33 个，列出前 60）

```text
`CrashedMechanoidPlatform_Standard`  `Opportunity_AbandonedPlatform_Enterable`  ``                                ``                              
`SpaceRuins`                      `CrashedMechanoidPlatform_Engine`  `Mechhive_SingleRoom`             ``                              
`AncientStockpileFake`            `AncientStockpile`                `Mechhive`                        `Opportunity_OrbitalMechanoidPlatform`
`OrbitalMechanoidPlatform`        ``                                `OrbitalSettlementPlatform`       `Opportunity_AbandonedPlatform` 
`OrbitalAncientPlatform`          `AncientLaunchSite`               `AncientRuinsGlacier`             ``                              
`OpportunitySite_Satellite`       `AncientRuins_Scarlands`          `Opportunity_OrbitalWreck`        `AncientGarrison`               
`AncientInfestedSettlement`       `AncientRuinsReactor_Standard`    ``                                `AncientWarehouse`              
`AncientChemfuelRefinery`         `AncientRuinsReactor_Reactor`     `OrbitalItemStash`                `AncientRuinsFrozenTerraformer` 
`AncientRuins_Special`          
```
