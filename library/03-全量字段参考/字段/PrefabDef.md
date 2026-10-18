# PrefabDef

- **所属线**：表现线
- **原版实例数**：176
- **字段路径数**：673
- **资料片**：Biotech、Core、Odyssey
- **原版出处**：`Odyssey/Defs/PrefabDefs/AncientExteriorPrefabs.xml`、`Odyssey/Defs/PrefabDefs/AncientPrefabs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<PrefabDef>
    <defName>Exterior_ShipChunk_Mech</defName>
    <size>(2,2)</size>
    <things>
      <ShipChunk_Mech>
      </ShipChunk_Mech>
    </things>
  </PrefabDef>

  
```

> 来自 `Odyssey/Defs/PrefabDefs/AncientExteriorPrefabs.xml`，defName = `Exterior_ShipChunk_Mech`，XML 节点数 5（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：AncientBandNode_Cluster / AncientBasicRecharger_Edge / AncientLargeMechGestator
size                                           [文本]  例：(3,1) / (4,3) / (5,4)
things                                         [容器]
```

## 三、全量字段表（673 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (176/176) | 文本 | AncientBandNode_Cluster / AncientBasicRecharger_Edge / AncientLargeMechGestator |
| `edgeOnly` | 18.2% (32/176) | 布尔 | true |
| `prefabs` | 1.1% (2/176) | 容器 |  |
| `prefabs/Exterior_AncientLaunchSite_LaunchPad_GridEntry` | 1.1% (2/176) | 容器 |  |
| `prefabs/Exterior_AncientLaunchSite_LaunchPad_GridEntry/positions` | 1.1% (2/176) | 容器 |  |
| `prefabs/Exterior_AncientLaunchSite_LaunchPad_GridEntry/positions/li` | 8.5% (15/176) | 文本 | (10, 0, 2) / (2, 0, 2) / (2, 0, 6) |
| `rotations` | 10.2% (18/176) | 文本 | North / North, South |
| `size` | 100.0% (176/176) | 文本 | (3,1) / (4,3) / (5,4) |
| `terrain` | 17.6% (31/176) | 容器 |  |
| `terrain/AncientConcrete` | 7.4% (13/176) | 容器 |  |
| `terrain/AncientConcrete/chance` | 4.0% (7/176) | 数值 | 0.9 / 0.95 |
| `terrain/AncientConcrete/rects` | 7.4% (13/176) | 容器 |  |
| `terrain/AncientConcrete/rects/li` | 10.2% (18/176) | 文本 | (0,0,10,10) / (1,1,10,17) / (1,1,5,5) |
| `terrain/AncientTile` | 8.0% (14/176) | 容器 |  |
| `terrain/AncientTile/chance` | 5.1% (9/176) | 数值 | 0.4 / 0.8 / 0.95 |
| `terrain/AncientTile/rects` | 8.0% (14/176) | 容器 |  |
| `terrain/AncientTile/rects/li` | 17.6% (31/176) | 文本 | (0,0,6,0) / (0,1,0,6) / (1,6,5,6) |
| `terrain/AncientWoodPlankFloor` | 0.6% (1/176) | 容器 |  |
| `terrain/AncientWoodPlankFloor/rects` | 0.6% (1/176) | 容器 |  |
| `terrain/AncientWoodPlankFloor/rects/li` | 0.6% (1/176) | 文本 | (3,2,7,6) |
| `terrain/Concrete` | 1.1% (2/176) | 容器 |  |
| `terrain/Concrete/rects` | 1.1% (2/176) | 容器 |  |
| `terrain/Concrete/rects/li` | 3.4% (6/176) | 文本 | (0,0,5,5) / (0,4,0,6) / (1,1,5,7) |
| `terrain/InsectSludge` | 1.7% (3/176) | 容器 |  |
| `terrain/InsectSludge/chance` | 1.7% (3/176) | 数值 | 0.85 |
| `terrain/InsectSludge/rects` | 1.7% (3/176) | 容器 |  |
| `terrain/InsectSludge/rects/li` | 1.7% (3/176) | 文本 | (1,1,10,9) / (1,1,7,6) / (1,1,8,6) |
| `terrain/MechanoidPlatform` | 2.3% (4/176) | 容器 |  |
| `terrain/MechanoidPlatform/rects` | 2.3% (4/176) | 容器 |  |
| `terrain/MechanoidPlatform/rects/li` | 26.1% (46/176) | 文本 | (0,2,2,8) / (27,0,28,25) / (3,0,25,0) |
| `terrain/Space` | 0.6% (1/176) | 容器 |  |
| `terrain/Space/rects` | 0.6% (1/176) | 容器 |  |
| `terrain/Space/rects/li` | 0.6% (1/176) | 文本 | (0,0,1,1) |
| `things` | 97.7% (172/176) | 容器 |  |
| `things/AncientAmmoStack` | 1.1% (2/176) | 容器 |  |
| `things/AncientAmmoStack/chance` | 1.1% (2/176) | 数值 | 0.75 |
| `things/AncientAmmoStack/position` | 0.6% (1/176) | 文本 | (3,0,5) |
| `things/AncientAmmoStack/rects` | 0.6% (1/176) | 容器 |  |
| `things/AncientAmmoStack/rects/li` | 0.6% (1/176) | 文本 | (0,0,1,1) |
| `things/AncientAntenna` | 1.1% (2/176) | 容器 |  |
| `things/AncientAntenna/chance` | 0.6% (1/176) | 数值 | 0.5 |
| `things/AncientAntenna/positions` | 0.6% (1/176) | 容器 |  |
| `things/AncientAntenna/positions/li` | 5.1% (9/176) | 文本 | (0, 0, 0) / (0, 0, 3) / (3, 0, 0) |
| `things/AncientAntenna/rects` | 0.6% (1/176) | 容器 |  |
| `things/AncientAntenna/rects/li` | 2.3% (4/176) | 文本 | (17,13,18,14) / (17,6,18,7) / (2,13,3,14) |
| `things/AncientArmchair` | 0.6% (1/176) | 容器 |  |
| `things/AncientArmchair/chance` | 0.6% (1/176) | 数值 | 0.35 |
| `things/AncientArmchair/positions` | 0.6% (1/176) | 容器 |  |
| `things/AncientArmchair/positions/li` | 1.1% (2/176) | 文本 | (0, 0, 0) / (2, 0, 0) |
| `things/AncientAutocannonTurret` | 1.1% (2/176) | 容器 |  |
| `things/AncientAutocannonTurret/position` | 1.1% (2/176) | 文本 | (17, 0, 17) / (6,0,6) |
| `things/AncientBandNode` | 0.6% (1/176) | 容器 |  |
| `things/AncientBandNode/chance` | 0.6% (1/176) | 数值 | 0.75 |
| `things/AncientBandNode/positions` | 0.6% (1/176) | 容器 |  |
| `things/AncientBandNode/positions/li` | 2.3% (4/176) | 文本 | (0, 0, 0) / (0, 0, 2) / (3, 0, 0) |
| `things/AncientBarrel` | 5.7% (10/176) | 容器 |  |
| `things/AncientBarrel/chance` | 2.8% (5/176) | 数值 | 0.25 / 0.4 / 0.5 |
| `things/AncientBarrel/hp` | 1.1% (2/176) | 数值 | 30 / 40 |
| `things/AncientBarrel/position` | 1.1% (2/176) | 文本 | (1,0,1) / (6,0,1) |
| `things/AncientBarrel/positions` | 2.8% (5/176) | 容器 |  |
| `things/AncientBarrel/positions/li` | 25.0% (44/176) | 文本 | (0, 0, 0) / (0, 0, 1) / (1, 0, 0) |
| `things/AncientBarrel/rects` | 1.7% (3/176) | 容器 |  |
| `things/AncientBarrel/rects/li` | 3.4% (6/176) | 文本 | (0,1,0,1) / (2,0,2,2) / (2,3,2,3) |
| `things/AncientBarrierLong` | 1.7% (3/176) | 容器 |  |
| `things/AncientBarrierLong/chance` | 1.1% (2/176) | 数值 | 0.85 / 0.9 |
| `things/AncientBarrierLong/positions` | 1.7% (3/176) | 容器 |  |
| `things/AncientBarrierLong/positions/li` | 9.7% (17/176) | 文本 | (1, 0, 4) / (7, 0, 1) / (7, 0, 4) |
| `things/AncientBarrierLong/relativeRotation` | 1.7% (3/176) | 文本 | Counterclockwise / Opposite |
| `things/AncientBasicRecharger` | 1.7% (3/176) | 容器 |  |
| `things/AncientBasicRecharger/chance` | 1.1% (2/176) | 数值 | 0.85 |
| `things/AncientBasicRecharger/position` | 0.6% (1/176) | 文本 | (1, 0, 0) |
| `things/AncientBasicRecharger/positions` | 1.1% (2/176) | 容器 |  |
| `things/AncientBasicRecharger/positions/li` | 2.3% (4/176) | 文本 | (1, 0, 0) / (1, 0, 2) / (4, 0, 0) |
| `things/AncientBasicRecharger/relativeRotation` | 1.1% (2/176) | 文本 | Opposite |
| `things/AncientBathtub` | 0.6% (1/176) | 容器 |  |
| `things/AncientBathtub/position` | 0.6% (1/176) | 文本 | (0,0,1) |
| `things/AncientBathtub/relativeRotation` | 0.6% (1/176) | 文本 | Opposite |
| `things/AncientBed` | 1.1% (2/176) | 容器 |  |
| `things/AncientBed/position` | 0.6% (1/176) | 文本 | (1,0,4) |
| `things/AncientBed/positions` | 0.6% (1/176) | 容器 |  |
| `things/AncientBed/positions/li` | 3.4% (6/176) | 文本 | (0, 0, 0) / (0, 0, 2) / (2, 0, 0) |
| `things/AncientBlastDoor` | 1.1% (2/176) | 容器 |  |
| `things/AncientBlastDoor/canOverrideData` | 0.6% (1/176) | 布尔 | false |
| `things/AncientBlastDoor/chance` | 1.1% (2/176) | 数值 | 0.4 / 0.6 |
| `things/AncientBlastDoor/position` | 0.6% (1/176) | 文本 | (3,0,1) |
| `things/AncientBlastDoor/rects` | 0.6% (1/176) | 容器 |  |
| `things/AncientBlastDoor/rects/li` | 1.1% (2/176) | 文本 | (3,8,3,8) / (4,0,4,0) |
| `things/AncientBox_ComponentIndustrial` | 2.3% (4/176) | 容器 |  |
| `things/AncientBox_ComponentIndustrial/chance` | 2.3% (4/176) | 数值 | 0.25 |
| `things/AncientBox_ComponentIndustrial/position` | 2.3% (4/176) | 文本 | (0,0,1) / (1,0,1) / (1,0,8) |
| `things/AncientBox_ComponentSpacer` | 0.6% (1/176) | 容器 |  |
| `things/AncientBox_ComponentSpacer/chance` | 0.6% (1/176) | 数值 | 0.4 |
| `things/AncientBox_ComponentSpacer/position` | 0.6% (1/176) | 文本 | (1,0,1) |
| `things/AncientBox_SteelSlag` | 0.6% (1/176) | 容器 |  |
| `things/AncientBox_SteelSlag/chance` | 0.6% (1/176) | 数值 | 0.7 |
| `things/AncientBox_SteelSlag/position` | 0.6% (1/176) | 文本 | (2,0,0) |
| `things/AncientCardboardBox` | 1.1% (2/176) | 容器 |  |
| `things/AncientCardboardBox/chance` | 0.6% (1/176) | 数值 | 0.75 |
| `things/AncientCardboardBox/positions` | 1.1% (2/176) | 容器 |  |
| `things/AncientCardboardBox/positions/li` | 4.0% (7/176) | 文本 | (0, 0, 0) / (11, 0, 3) / (11, 0, 4) |
| `things/AncientChembarrel` | 4.5% (8/176) | 容器 |  |
| `things/AncientChembarrel/chance` | 4.5% (8/176) | 数值 | 0.5 / 0.6 / 0.75 |
| `things/AncientChembarrel/positions` | 2.3% (4/176) | 容器 |  |
| `things/AncientChembarrel/positions/li` | 16.5% (29/176) | 文本 | (2, 0, 0) / (2, 0, 1) / (5, 0, 0) |
| `things/AncientChembarrel/rects` | 2.3% (4/176) | 容器 |  |
| `things/AncientChembarrel/rects/li` | 17.6% (31/176) | 文本 | (12,9,12,9) / (5,1,5,1) / (7,1,7,1) |
| `things/AncientChembarrelPallet` | 2.3% (4/176) | 容器 |  |
| `things/AncientChembarrelPallet/chance` | 1.1% (2/176) | 数值 | 0.8 / 0.85 |
| `things/AncientChembarrelPallet/positions` | 2.3% (4/176) | 容器 |  |
| `things/AncientChembarrelPallet/positions/li` | 12.5% (22/176) | 文本 | (14, 0, 1) / (17, 0, 0) / (6, 0, 2) |
| `things/AncientChemfuelCanister` | 1.7% (3/176) | 容器 |  |
| `things/AncientChemfuelCanister/chance` | 1.1% (2/176) | 数值 | 0.5 / 0.8 |
| `things/AncientChemfuelCanister/positions` | 1.1% (2/176) | 容器 |  |
| `things/AncientChemfuelCanister/positions/li` | 3.4% (6/176) | 文本 | (0, 0, 0) / (0, 0, 1) / (1, 0, 0) |
| `things/AncientChemfuelCanister/rects` | 0.6% (1/176) | 容器 |  |
| `things/AncientChemfuelCanister/rects/li` | 4.5% (8/176) | 文本 | (16,7,16,7) / (17,4,17,4) / (17,6,17,6) |
| `things/AncientChemtruck` | 2.3% (4/176) | 容器 |  |
| `things/AncientChemtruck/chance` | 2.3% (4/176) | 数值 | 0.5 / 0.8 / 0.85 |
| `things/AncientChemtruck/position` | 0.6% (1/176) | 文本 | (14,0,1) |
| `things/AncientChemtruck/positions` | 1.7% (3/176) | 容器 |  |
| `things/AncientChemtruck/positions/li` | 4.5% (8/176) | 文本 | (10, 0, 2) / (10, 0, 5) / (10, 0, 7) |
| `things/AncientChemtruck/relativeRotation` | 1.7% (3/176) | 文本 | Clockwise / Counterclockwise |
| `things/AncientConcreteBarrier` | 4.5% (8/176) | 容器 |  |
| `things/AncientConcreteBarrier/hp` | 3.4% (6/176) | 数值 | 292 / 382 / 399 |
| `things/AncientConcreteBarrier/position` | 4.0% (7/176) | 文本 | (1,0,1) / (1,0,9) / (14,0,1) |
| `things/AncientConcreteBarrier/rects` | 0.6% (1/176) | 容器 |  |
| `things/AncientConcreteBarrier/rects/li` | 1.1% (2/176) | 文本 | (5,4,5,4) / (8,4,8,4) |
| `things/AncientCraneBase` | 0.6% (1/176) | 容器 |  |
| `things/AncientCraneBase/hp` | 0.6% (1/176) | 数值 | 490 |
| `things/AncientCraneBase/position` | 0.6% (1/176) | 文本 | (4,0,8) |
| `things/AncientCraneColumn` | 2.8% (5/176) | 容器 |  |
| `things/AncientCraneColumn/hp` | 2.8% (5/176) | 数值 | 190 / 200 / 210 |
| `things/AncientCraneColumn/position` | 2.3% (4/176) | 文本 | (11,0,8) / (15,0,8) / (18,0,8) |
| `things/AncientCraneColumn/positions` | 0.6% (1/176) | 容器 |  |
| `things/AncientCraneColumn/positions/li` | 1.1% (2/176) | 文本 | (25, 0, 8) / (9, 0, 10) |
| `things/AncientCrate` | 1.1% (2/176) | 容器 |  |
| `things/AncientCrate/chance` | 1.1% (2/176) | 数值 | 0.4 / 0.5 |
| `things/AncientCrate/positions` | 1.1% (2/176) | 容器 |  |
| `things/AncientCrate/positions/li` | 4.5% (8/176) | 文本 | (10, 0, 2) / (10, 0, 3) / (8, 0, 3) |
| `things/AncientCratePallet` | 1.7% (3/176) | 容器 |  |
| `things/AncientCratePallet/chance` | 1.1% (2/176) | 数值 | 0.5 / 0.8 |
| `things/AncientCratePallet/positions` | 1.7% (3/176) | 容器 |  |
| `things/AncientCratePallet/positions/li` | 4.5% (8/176) | 文本 | (0, 0, 0) / (1, 0, 15) / (2, 0, 0) |
| `things/AncientDestroyedConsole` | 2.3% (4/176) | 容器 |  |
| `things/AncientDestroyedConsole/position` | 1.1% (2/176) | 文本 | (1,0,0) / (2,0,1) |
| `things/AncientDestroyedConsole/positions` | 1.1% (2/176) | 容器 |  |
| `things/AncientDestroyedConsole/positions/li` | 2.3% (4/176) | 文本 | (0, 0, 1) / (1, 0, 0) / (2, 0, 1) |
| `things/AncientDestroyedConsole/relativeRotation` | 1.7% (3/176) | 文本 | Opposite |
| `things/AncientDestroyedConsoleLarge` | 1.1% (2/176) | 容器 |  |
| `things/AncientDestroyedConsoleLarge/position` | 1.1% (2/176) | 文本 | (1,0,2) / (3,0,2) |
| `things/AncientDestroyedConsoleLarge/relativeRotation` | 1.1% (2/176) | 文本 | Clockwise / Counterclockwise |
| `things/AncientDisplayBank` | 0.6% (1/176) | 容器 |  |
| `things/AncientDisplayBank/position` | 0.6% (1/176) | 文本 | (1,0,0) |
| `things/AncientDisplayBank/relativeRotation` | 0.6% (1/176) | 文本 | Opposite |
| `things/AncientDoubleBed` | 0.6% (1/176) | 容器 |  |
| `things/AncientDoubleBed/position` | 0.6% (1/176) | 文本 | (1, 0, 1) |
| `things/AncientDoubleBed/relativeRotation` | 0.6% (1/176) | 文本 | Opposite |
| `things/AncientEmergencyLight_Blue` | 1.7% (3/176) | 容器 |  |
| `things/AncientEmergencyLight_Blue/position` | 1.1% (2/176) | 文本 | (1,0,3) / (3,0,1) |
| `things/AncientEmergencyLight_Blue/rects` | 0.6% (1/176) | 容器 |  |
| `things/AncientEmergencyLight_Blue/rects/li` | 1.1% (2/176) | 文本 | (3,0,3,0) / (3,3,3,3) |
| `things/AncientEquipmentBlocks` | 0.6% (1/176) | 容器 |  |
| `things/AncientEquipmentBlocks/positions` | 0.6% (1/176) | 容器 |  |
| `things/AncientEquipmentBlocks/positions/li` | 1.1% (2/176) | 文本 | (1, 0, 0) / (1, 0, 2) |
| `things/AncientExplosivesCrate` | 0.6% (1/176) | 容器 |  |
| `things/AncientExplosivesCrate/position` | 0.6% (1/176) | 文本 | (1,0,1) |
| `things/AncientFence` | 1.1% (2/176) | 容器 |  |
| `things/AncientFence/chance` | 1.1% (2/176) | 数值 | 0.5 / 0.95 |
| `things/AncientFence/rects` | 1.1% (2/176) | 容器 |  |
| `things/AncientFence/rects/li` | 7.4% (13/176) | 文本 | (0,0,15,0) / (0,1,0,1) / (0,9,0,10) |
| `things/AncientFilingCabinet` | 1.7% (3/176) | 容器 |  |
| `things/AncientFilingCabinet/chance` | 1.1% (2/176) | 数值 | 0.5 / 0.75 |
| `things/AncientFilingCabinet/position` | 1.1% (2/176) | 文本 | (0,0,1) / (1,0,4) |
| `things/AncientFilingCabinet/positions` | 0.6% (1/176) | 容器 |  |
| `things/AncientFilingCabinet/positions/li` | 1.7% (3/176) | 文本 | (0, 0, 0) / (1, 0, 0) / (2, 0, 0) |
| `things/AncientFilingCabinet/relativeRotation` | 1.7% (3/176) | 文本 | Counterclockwise / Opposite |
| `things/AncientForklift` | 1.7% (3/176) | 容器 |  |
| `things/AncientForklift/chance` | 1.1% (2/176) | 数值 | 0.5 |
| `things/AncientForklift/position` | 1.7% (3/176) | 文本 | (1, 0, 1) / (1,0,4) / (1,0,9) |
| `things/AncientForklift/relativeRotation` | 1.7% (3/176) | 文本 | Clockwise |
| `things/AncientFortifiedWall` | 11.4% (20/176) | 容器 |  |
| `things/AncientFortifiedWall/chance` | 0.6% (1/176) | 数值 | 0.95 |
| `things/AncientFortifiedWall/position` | 0.6% (1/176) | 文本 | (1,0,0) |
| `things/AncientFortifiedWall/positions` | 10.2% (18/176) | 容器 |  |
| `things/AncientFortifiedWall/positions/li` | 88.6% (156/176) | 文本 | (0, 0, 1) / (1, 0, 1) / (2, 0, 1) |
| `things/AncientFortifiedWall/rects` | 0.6% (1/176) | 容器 |  |
| `things/AncientFortifiedWall/rects/li` | 0.6% (1/176) | 文本 | (0,0,1,0) |
| `things/AncientFuelNode` | 1.1% (2/176) | 容器 |  |
| `things/AncientFuelNode/positions` | 0.6% (1/176) | 容器 |  |
| `things/AncientFuelNode/positions/li` | 2.3% (4/176) | 文本 | (0, 0, 0) / (0, 0, 2) / (2, 0, 0) |
| `things/AncientGenerator` | 2.3% (4/176) | 容器 |  |
| `things/AncientGenerator/position` | 0.6% (1/176) | 文本 | (3, 0, 3) |
| `things/AncientGenerator/positions` | 1.1% (2/176) | 容器 |  |
| `things/AncientGenerator/positions/li` | 3.4% (6/176) | 文本 | (0, 0, 0) / (0, 0, 1) / (3, 0, 0) |
| `things/AncientIndustrialShelf` | 2.8% (5/176) | 容器 |  |
| `things/AncientIndustrialShelf/chance` | 0.6% (1/176) | 数值 | 0.85 |
| `things/AncientIndustrialShelf/hp` | 0.6% (1/176) | 数值 | 90 |
| `things/AncientIndustrialShelf/position` | 1.1% (2/176) | 文本 | (21,0,6) / (23,0,10) |
| `things/AncientIndustrialShelf/positions` | 1.7% (3/176) | 容器 |  |
| `things/AncientIndustrialShelf/positions/li` | 8.5% (15/176) | 文本 | (0, 0, 0) / (0, 0, 2) / (2, 0, 0) |
| `things/AncientIndustrialTruck` | 2.3% (4/176) | 容器 |  |
| `things/AncientIndustrialTruck/chance` | 1.7% (3/176) | 数值 | 0.5 |
| `things/AncientIndustrialTruck/position` | 1.7% (3/176) | 文本 | (14, 0, 3) / (4,0,3) / (4,0,6) |
| `things/AncientIndustrialTruck/positions` | 0.6% (1/176) | 容器 |  |
| `things/AncientIndustrialTruck/positions/li` | 1.1% (2/176) | 文本 | (14, 0, 12) / (14, 0, 5) |
| `things/AncientIndustrialTruck/relativeRotation` | 2.3% (4/176) | 文本 | Clockwise / Counterclockwise |
| `things/AncientLamp` | 1.7% (3/176) | 容器 |  |
| `things/AncientLamp/chance` | 0.6% (1/176) | 数值 | 0.75 |
| `things/AncientLamp/position` | 1.7% (3/176) | 文本 | (0, 0, 0) / (2,0,2) |
| `things/AncientLamppost` | 4.0% (7/176) | 容器 |  |
| `things/AncientLamppost/hp` | 3.4% (6/176) | 数值 | 178 / 251 / 266 |
| `things/AncientLamppost/position` | 4.0% (7/176) | 文本 | (10, 0, 10) / (18, 0, 10) / (2, 0, 10) |
| `things/AncientLargeContainer` | 0.6% (1/176) | 容器 |  |
| `things/AncientLargeContainer/chance` | 0.6% (1/176) | 数值 | 0.5 |
| `things/AncientLargeContainer/position` | 0.6% (1/176) | 文本 | (2,0,4) |
| `things/AncientLargeMechGestator` | 0.6% (1/176) | 容器 |  |
| `things/AncientLargeMechGestator/position` | 0.6% (1/176) | 文本 | (1, 0, 1) |
| `things/AncientLargeRustedEngineBlock` | 0.6% (1/176) | 容器 |  |
| `things/AncientLargeRustedEngineBlock/chance` | 0.6% (1/176) | 数值 | 0.75 |
| `things/AncientLargeRustedEngineBlock/positions` | 0.6% (1/176) | 容器 |  |
| `things/AncientLargeRustedEngineBlock/positions/li` | 1.7% (3/176) | 文本 | (0, 0, 0) / (0, 0, 2) / (3, 0, 0) |
| `things/AncientLockerBank` | 0.6% (1/176) | 容器 |  |
| `things/AncientLockerBank/positions` | 0.6% (1/176) | 容器 |  |
| `things/AncientLockerBank/positions/li` | 1.1% (2/176) | 文本 | (1, 0, 0) / (4, 0, 0) |
| `things/AncientLockerBank/relativeRotation` | 0.6% (1/176) | 文本 | Opposite |
| `things/AncientLockers` | 0.6% (1/176) | 容器 |  |
| `things/AncientLockers/chance` | 0.6% (1/176) | 数值 | 0.9 |
| `things/AncientLockers/positions` | 0.6% (1/176) | 容器 |  |
| `things/AncientLockers/positions/li` | 2.3% (4/176) | 文本 | (0, 0, 0) / (1, 0, 0) / (2, 0, 0) |
| `things/AncientLockers/relativeRotation` | 0.6% (1/176) | 文本 | Opposite |
| `things/AncientLongCrate` | 0.6% (1/176) | 容器 |  |
| `things/AncientLongCrate/chance` | 0.6% (1/176) | 数值 | 0.5 |
| `things/AncientLongCrate/positions` | 0.6% (1/176) | 容器 |  |
| `things/AncientLongCrate/positions/li` | 1.7% (3/176) | 文本 | (0, 0, 0) / (0, 0, 1) / (1, 0, 0) |
| `things/AncientMachine` | 0.6% (1/176) | 容器 |  |
| `things/AncientMachine/positions` | 0.6% (1/176) | 容器 |  |
| `things/AncientMachine/positions/li` | 1.1% (2/176) | 文本 | (2, 0, 1) / (2, 0, 5) |
| `things/AncientMechGestator` | 0.6% (1/176) | 容器 |  |
| `things/AncientMechGestator/positions` | 0.6% (1/176) | 容器 |  |
| `things/AncientMechGestator/positions/li` | 1.1% (2/176) | 文本 | (1, 0, 2) / (5, 0, 2) |
| `things/AncientMechGestator/relativeRotation` | 0.6% (1/176) | 文本 | Opposite |
| `things/AncientMechGestatorTank` | 0.6% (1/176) | 容器 |  |
| `things/AncientMechGestatorTank/chance` | 0.6% (1/176) | 数值 | 0.95 |
| `things/AncientMechGestatorTank/positions` | 0.6% (1/176) | 容器 |  |
| `things/AncientMechGestatorTank/positions/li` | 1.7% (3/176) | 文本 | (0, 0, 0) / (0, 0, 3) / (3, 0, 3) |
| `things/AncientMediumContainer` | 1.7% (3/176) | 容器 |  |
| `things/AncientMediumContainer/chance` | 0.6% (1/176) | 数值 | 0.5 |
| `things/AncientMediumContainer/position` | 1.1% (2/176) | 文本 | (10,0,2) / (7,0,3) |
| `things/AncientMediumContainer/positions` | 0.6% (1/176) | 容器 |  |
| `things/AncientMediumContainer/positions/li` | 2.3% (4/176) | 文本 | (2, 0, 13) / (2, 0, 9) / (7, 0, 12) |
| `things/AncientMediumContainer/relativeRotation` | 1.7% (3/176) | 文本 | Clockwise |
| `things/AncientMegaCannonBarrel` | 0.6% (1/176) | 容器 |  |
| `things/AncientMegaCannonBarrel/chance` | 0.6% (1/176) | 数值 | 0.5 |
| `things/AncientMegaCannonBarrel/position` | 0.6% (1/176) | 文本 | (1,0,3) |
| `things/AncientMegaCannonBarrel/relativeRotation` | 0.6% (1/176) | 文本 | Opposite |
| `things/AncientMegaCannonTripod` | 0.6% (1/176) | 容器 |  |
| `things/AncientMegaCannonTripod/position` | 0.6% (1/176) | 文本 | (3,0,3) |
| `things/AncientMetalCrate` | 1.1% (2/176) | 容器 |  |
| `things/AncientMetalCrate/chance` | 1.1% (2/176) | 数值 | 0.6 / 0.8 |
| `things/AncientMetalCrate/positions` | 0.6% (1/176) | 容器 |  |
| `things/AncientMetalCrate/positions/li` | 4.0% (7/176) | 文本 | (0, 0, 2) / (2, 0, 0) / (5, 0, 0) |
| `things/AncientMetalCrate/rects` | 0.6% (1/176) | 容器 |  |
| `things/AncientMetalCrate/rects/li` | 1.1% (2/176) | 文本 | (11,1,12,1) / (12,2,12,3) |
| `things/AncientMilitaryBarrier` | 2.8% (5/176) | 容器 |  |
| `things/AncientMilitaryBarrier/chance` | 2.3% (4/176) | 数值 | 0.7 / 0.9 |
| `things/AncientMilitaryBarrier/positions` | 2.8% (5/176) | 容器 |  |
| `things/AncientMilitaryBarrier/positions/li` | 9.7% (17/176) | 文本 | (2, 0, 1) / (5, 0, 1) / (8, 0, 1) |
| `things/AncientMilitaryBarrier/relativeRotation` | 2.8% (5/176) | 文本 | Clockwise / Counterclockwise / Opposite |
| `things/AncientMilitaryCrate` | 1.7% (3/176) | 容器 |  |
| `things/AncientMilitaryCrate/chance` | 0.6% (1/176) | 数值 | 0.75 |
| `things/AncientMilitaryCrate/position` | 1.1% (2/176) | 文本 | (3,0,4) / (6,0,6) |
| `things/AncientMilitaryCrate/rects` | 0.6% (1/176) | 容器 |  |
| `things/AncientMilitaryCrate/rects/li` | 0.6% (1/176) | 文本 | (0,0,1,1) |
| `things/AncientMilitaryGeneratorSmall` | 0.6% (1/176) | 容器 |  |
| `things/AncientMilitaryGeneratorSmall/position` | 0.6% (1/176) | 文本 | (5,0,4) |
| `things/AncientMiningCharge` | 0.6% (1/176) | 容器 |  |
| `things/AncientMiningCharge/chance` | 0.6% (1/176) | 数值 | 0.5 |
| `things/AncientMiningCharge/positions` | 0.6% (1/176) | 容器 |  |
| `things/AncientMiningCharge/positions/li` | 2.8% (5/176) | 文本 | (0, 0, 0) / (0, 0, 1) / (1, 0, 0) |
| `things/AncientOpenContainer` | 2.3% (4/176) | 容器 |  |
| `things/AncientOpenContainer/chance` | 0.6% (1/176) | 数值 | 0.5 |
| `things/AncientOpenContainer/position` | 1.1% (2/176) | 文本 | (1,0,0) / (7,0,14) |
| `things/AncientOpenContainer/positions` | 1.1% (2/176) | 容器 |  |
| `things/AncientOpenContainer/positions/li` | 2.3% (4/176) | 文本 | (10, 0, 4) / (15, 0, 4) / (7, 0, 5) |
| `things/AncientOperatingTable` | 0.6% (1/176) | 容器 |  |
| `things/AncientOperatingTable/positions` | 0.6% (1/176) | 容器 |  |
| `things/AncientOperatingTable/positions/li` | 3.4% (6/176) | 文本 | (0, 0, 0) / (0, 0, 3) / (2, 0, 0) |
| `things/AncientPallet_SteelSlag` | 1.1% (2/176) | 容器 |  |
| `things/AncientPallet_SteelSlag/position` | 1.1% (2/176) | 文本 | (0, 0, 0) / (1,0,2) |
| `things/AncientPipe` | 1.1% (2/176) | 容器 |  |
| `things/AncientPipe/chance` | 1.1% (2/176) | 数值 | 0.75 / 0.8 |
| `things/AncientPipe/positions` | 1.1% (2/176) | 容器 |  |
| `things/AncientPipe/positions/li` | 17.6% (31/176) | 文本 | (4, 0, 1) / (4, 0, 3) / (5, 0, 1) |
| `things/AncientPlantPot` | 1.7% (3/176) | 容器 |  |
| `things/AncientPlantPot/chance` | 1.1% (2/176) | 数值 | 0.3 / 0.5 |
| `things/AncientPlantPot/position` | 1.1% (2/176) | 文本 | (2,0,0) / (3,0,1) |
| `things/AncientPlantPot/positions` | 0.6% (1/176) | 容器 |  |
| `things/AncientPlantPot/positions/li` | 6.8% (12/176) | 文本 | (1, 0, 1) / (2, 0, 1) / (3, 0, 1) |
| `things/AncientPodCar` | 1.1% (2/176) | 容器 |  |
| `things/AncientPodCar/chance` | 1.1% (2/176) | 数值 | 0.5 |
| `things/AncientPodCar/position` | 1.1% (2/176) | 文本 | (10, 0, 6) / (23, 0, 7) |
| `things/AncientRazorWire` | 4.5% (8/176) | 容器 |  |
| `things/AncientRazorWire/chance` | 2.8% (5/176) | 数值 | 0.85 / 0.9 / 0.95 |
| `things/AncientRazorWire/positions` | 2.8% (5/176) | 容器 |  |
| `things/AncientRazorWire/positions/li` | 60.2% (106/176) | 文本 | (4, 0, 0) / (5, 0, 0) / (6, 0, 0) |
| `things/AncientRazorWire/rects` | 1.7% (3/176) | 容器 |  |
| `things/AncientRazorWire/rects/li` | 7.4% (13/176) | 文本 | (0,0,6,0) / (13,1,13,9) / (4,0,13,0) |
| `things/AncientRustedCar` | 1.1% (2/176) | 容器 |  |
| `things/AncientRustedCar/chance` | 1.1% (2/176) | 数值 | 0.5 |
| `things/AncientRustedCar/position` | 1.1% (2/176) | 文本 | (15, 0, 7) / (6, 0, 2) |
| `things/AncientRustedCar/relativeRotation` | 1.1% (2/176) | 文本 | Clockwise / Counterclockwise |
| `things/AncientRustedEngineBlock` | 0.6% (1/176) | 容器 |  |
| `things/AncientRustedEngineBlock/chance` | 0.6% (1/176) | 数值 | 0.75 |
| `things/AncientRustedEngineBlock/rects` | 0.6% (1/176) | 容器 |  |
| `things/AncientRustedEngineBlock/rects/li` | 0.6% (1/176) | 文本 | (3,2,4,2) |
| `things/AncientSafe` | 1.1% (2/176) | 容器 |  |
| `things/AncientSafe/chance` | 1.1% (2/176) | 数值 | 0.2 / 0.75 |
| `things/AncientSafe/position` | 0.6% (1/176) | 文本 | (2,0,4) |
| `things/AncientSealedContainer` | 0.6% (1/176) | 容器 |  |
| `things/AncientSealedContainer/position` | 0.6% (1/176) | 文本 | (2,0,2) |
| `things/AncientSealedContainer_GravshipUpgrade` | 0.6% (1/176) | 容器 |  |
| `things/AncientSealedContainer_GravshipUpgrade/chance` | 0.6% (1/176) | 数值 | 0.33 |
| `things/AncientSealedContainer_GravshipUpgrade/position` | 0.6% (1/176) | 文本 | (2,0,2) |
| `things/AncientSealedCrate` | 4.0% (7/176) | 容器 |  |
| `things/AncientSealedCrate/chance` | 2.3% (4/176) | 数值 | 0.15 / 0.75 |
| `things/AncientSealedCrate/position` | 2.3% (4/176) | 文本 | (1,0,1) / (2,0,4) / (3,0,1) |
| `things/AncientSealedCrate/rects` | 1.1% (2/176) | 容器 |  |
| `things/AncientSealedCrate/rects/li` | 1.1% (2/176) | 文本 | (3,0,3,0) / (4,1,4,1) |
| `things/AncientSealedCrate_Gravlite` | 0.6% (1/176) | 容器 |  |
| `things/AncientSealedCrate_Gravlite/chance` | 0.6% (1/176) | 数值 | 0.85 |
| `things/AncientSealedCrate_Gravlite/positions` | 0.6% (1/176) | 容器 |  |
| `things/AncientSealedCrate_Gravlite/positions/li` | 2.3% (4/176) | 文本 | (0, 0, 0) / (0, 0, 2) / (1, 0, 1) |
| `things/AncientSealedCrate_Shells` | 0.6% (1/176) | 容器 |  |
| `things/AncientSealedCrate_Shells/chance` | 0.6% (1/176) | 数值 | 0.75 |
| `things/AncientSealedCrate_Shells/rects` | 0.6% (1/176) | 容器 |  |
| `things/AncientSealedCrate_Shells/rects/li` | 1.1% (2/176) | 文本 | (1,1,1,1) / (3,0,3,1) |
| `things/AncientSecurityTerminal` | 0.6% (1/176) | 容器 |  |
| `things/AncientSecurityTerminal/relativeRotation` | 0.6% (1/176) | 文本 | Opposite |
| `things/AncientSecurityTurret` | 1.7% (3/176) | 容器 |  |
| `things/AncientSecurityTurret/chance` | 1.1% (2/176) | 数值 | 0.75 |
| `things/AncientSecurityTurret/positions` | 0.6% (1/176) | 容器 |  |
| `things/AncientSecurityTurret/positions/li` | 1.1% (2/176) | 文本 | (3, 0, 7) / (7, 0, 3) |
| `things/AncientSecurityTurret/rects` | 1.1% (2/176) | 容器 |  |
| `things/AncientSecurityTurret/rects/li` | 3.4% (6/176) | 文本 | (1,1,1,1) / (10,3,10,3) / (3,10,3,10) |
| `things/AncientShipBeacon` | 1.7% (3/176) | 容器 |  |
| `things/AncientShipBeacon/chance` | 0.6% (1/176) | 数值 | 0.5 |
| `things/AncientShipBeacon/rects` | 1.7% (3/176) | 容器 |  |
| `things/AncientShipBeacon/rects/li` | 6.8% (12/176) | 文本 | (0,0,0,0) / (0,12,0,12) / (12,0,12,0) |
| `things/AncientShower` | 0.6% (1/176) | 容器 |  |
| `things/AncientShower/relativeRotation` | 0.6% (1/176) | 文本 | Counterclockwise |
| `things/AncientSimpleResearchBench` | 0.6% (1/176) | 容器 |  |
| `things/AncientSimpleResearchBench/position` | 0.6% (1/176) | 文本 | (1,0,1) |
| `things/AncientSingleBed` | 2.3% (4/176) | 容器 |  |
| `things/AncientSingleBed/chance` | 0.6% (1/176) | 数值 | 0.5 |
| `things/AncientSingleBed/position` | 0.6% (1/176) | 文本 | (0, 0, 1) |
| `things/AncientSingleBed/positions` | 1.7% (3/176) | 容器 |  |
| `things/AncientSingleBed/positions/li` | 3.4% (6/176) | 文本 | (0, 0, 1) / (1, 0, 2) / (2, 0, 1) |
| `things/AncientSingleBed/relativeRotation` | 2.3% (4/176) | 文本 | Opposite |
| `things/AncientSmallContainer` | 1.1% (2/176) | 容器 |  |
| `things/AncientSmallContainer/chance` | 1.1% (2/176) | 数值 | 0.5 / 0.85 |
| `things/AncientSmallContainer/positions` | 1.1% (2/176) | 容器 |  |
| `things/AncientSmallContainer/positions/li` | 2.3% (4/176) | 文本 | (1, 0, 5) / (5, 0, 2) / (6, 0, 4) |
| `things/AncientSmallCrate` | 0.6% (1/176) | 容器 |  |
| `things/AncientSmallCrate/position` | 0.6% (1/176) | 文本 | (24,0,6) |
| `things/AncientSpacerCrate` | 6.8% (12/176) | 容器 |  |
| `things/AncientSpacerCrate/chance` | 6.2% (11/176) | 数值 | 0.25 / 0.5 / 0.75 |
| `things/AncientSpacerCrate/position` | 0.6% (1/176) | 文本 | (2,0,0) |
| `things/AncientSpacerCrate/positions` | 3.4% (6/176) | 容器 |  |
| `things/AncientSpacerCrate/positions/li` | 26.1% (46/176) | 文本 | (2, 0, 0) / (2, 0, 1) / (3, 0, 0) |
| `things/AncientSpacerCrate/rects` | 2.3% (4/176) | 容器 |  |
| `things/AncientSpacerCrate/rects/li` | 14.2% (25/176) | 文本 | (1,6,1,8) / (2,7,2,8) / (22,6,22,8) |
| `things/AncientStandardRecharger` | 0.6% (1/176) | 容器 |  |
| `things/AncientStandardRecharger/position` | 0.6% (1/176) | 文本 | (1, 0, 0) |
| `things/AncientStorageCylinder` | 1.1% (2/176) | 容器 |  |
| `things/AncientStorageCylinder/position` | 0.6% (1/176) | 文本 | (1,0,0) |
| `things/AncientStorageCylinder/positions` | 0.6% (1/176) | 容器 |  |
| `things/AncientStorageCylinder/positions/li` | 3.4% (6/176) | 文本 | (0, 0, 0) / (0, 0, 2) / (3, 0, 0) |
| `things/AncientStove` | 1.1% (2/176) | 容器 |  |
| `things/AncientStove/hp` | 0.6% (1/176) | 数值 | 30 |
| `things/AncientStove/position` | 0.6% (1/176) | 文本 | (6,0,2) |
| `things/AncientStove/positions` | 0.6% (1/176) | 容器 |  |
| `things/AncientStove/positions/li` | 2.3% (4/176) | 文本 | (0, 0, 0) / (0, 0, 1) / (1, 0, 0) |
| `things/AncientStove/relativeRotation` | 1.1% (2/176) | 文本 | Opposite |
| `things/AncientSystemRack` | 1.1% (2/176) | 容器 |  |
| `things/AncientSystemRack/position` | 0.6% (1/176) | 文本 | (0,0,1) |
| `things/AncientSystemRack/positions` | 0.6% (1/176) | 容器 |  |
| `things/AncientSystemRack/positions/li` | 1.7% (3/176) | 文本 | (0, 0, 1) / (2, 0, 1) / (4, 0, 1) |
| `things/AncientTableDrugLab` | 1.1% (2/176) | 容器 |  |
| `things/AncientTableDrugLab/position` | 1.1% (2/176) | 文本 | (1,0,1) / (5, 0, 1) |
| `things/AncientTableMachining` | 2.3% (4/176) | 容器 |  |
| `things/AncientTableMachining/position` | 1.7% (3/176) | 文本 | (1, 0, 1) / (2,0,1) / (3,0,1) |
| `things/AncientTableMachining/positions` | 0.6% (1/176) | 容器 |  |
| `things/AncientTableMachining/positions/li` | 2.3% (4/176) | 文本 | (1, 0, 1) / (1, 0, 3) / (5, 0, 1) |
| `things/AncientTableStoveElectric` | 0.6% (1/176) | 容器 |  |
| `things/AncientTableStoveElectric/position` | 0.6% (1/176) | 文本 | (1,0,0) |
| `things/AncientTableTailorElectric` | 0.6% (1/176) | 容器 |  |
| `things/AncientTableTailorElectric/positions` | 0.6% (1/176) | 容器 |  |
| `things/AncientTableTailorElectric/positions/li` | 1.1% (2/176) | 文本 | (1, 0, 3) / (5, 0, 3) |
| `things/AncientTank` | 1.7% (3/176) | 容器 |  |
| `things/AncientTank/chance` | 0.6% (1/176) | 数值 | 0.85 |
| `things/AncientTank/position` | 1.1% (2/176) | 文本 | (2, 0, 1) / (2,0,7) |
| `things/AncientTank/positions` | 0.6% (1/176) | 容器 |  |
| `things/AncientTank/positions/li` | 4.5% (8/176) | 文本 | (10, 0, 3) / (10, 0, 8) / (3, 0, 3) |
| `things/AncientTankTrap` | 1.7% (3/176) | 容器 |  |
| `things/AncientTankTrap/chance` | 1.7% (3/176) | 数值 | 0.75 / 0.8 / 0.85 |
| `things/AncientTankTrap/positions` | 1.7% (3/176) | 容器 |  |
| `things/AncientTankTrap/positions/li` | 9.1% (16/176) | 文本 | (14, 0, 21) / (15, 0, 11) / (6, 0, 21) |
| `things/AncientTerraformer` | 0.6% (1/176) | 容器 |  |
| `things/AncientTerraformer/position` | 0.6% (1/176) | 文本 | (1,0,1) |
| `things/AncientToilet` | 0.6% (1/176) | 容器 |  |
| `things/AncientToilet/position` | 0.6% (1/176) | 文本 | (2,0,0) |
| `things/AncientToilet/relativeRotation` | 0.6% (1/176) | 文本 | Opposite |
| `things/AncientTransportPod` | 1.1% (2/176) | 容器 |  |
| `things/AncientTransportPod/chance` | 0.6% (1/176) | 数值 | 0.3 |
| `things/AncientTransportPod/position` | 1.1% (2/176) | 文本 | (1, 0, 1) / (2, 0, 2) |
| `things/AncientTV` | 0.6% (1/176) | 容器 |  |
| `things/AncientTV/position` | 0.6% (1/176) | 文本 | (1,0,2) |
| `things/AncientTV/relativeRotation` | 0.6% (1/176) | 文本 | Opposite |
| `things/AncientUplink` | 0.6% (1/176) | 容器 |  |
| `things/AncientUplink/position` | 0.6% (1/176) | 文本 | (1,0,1) |
| `things/AncientUraniumSlugTurret` | 1.7% (3/176) | 容器 |  |
| `things/AncientUraniumSlugTurret/chance` | 0.6% (1/176) | 数值 | 0.75 |
| `things/AncientUraniumSlugTurret/position` | 1.1% (2/176) | 文本 | (1,0,1) / (2, 0, 2) |
| `things/AncientUraniumSlugTurret/positions` | 0.6% (1/176) | 容器 |  |
| `things/AncientUraniumSlugTurret/positions/li` | 1.7% (3/176) | 文本 | (11, 0, 11) / (11, 0, 8) / (8, 0, 8) |
| `things/AncientWheel` | 0.6% (1/176) | 容器 |  |
| `things/AncientWheel/position` | 0.6% (1/176) | 文本 | (3,0,4) |
| `things/AncientWoodenCrate` | 1.7% (3/176) | 容器 |  |
| `things/AncientWoodenCrate/chance` | 1.7% (3/176) | 数值 | 0.7 / 0.8 / 0.85 |
| `things/AncientWoodenCrate/positions` | 1.1% (2/176) | 容器 |  |
| `things/AncientWoodenCrate/positions/li` | 6.8% (12/176) | 文本 | (0, 0, 0) / (1, 0, 0) / (1, 0, 1) |
| `things/AncientWoodenCrate/rects` | 0.6% (1/176) | 容器 |  |
| `things/AncientWoodenCrate/rects/li` | 1.1% (2/176) | 文本 | (1,8,2,8) / (2,9,2,9) |
| `things/AnimalFlap` | 0.6% (1/176) | 容器 |  |
| `things/AnimalFlap/position` | 0.6% (1/176) | 文本 | (5, 0, 6) |
| `things/AnimalFlap/stuff` | 0.6% (1/176) | 文本 | Cloth |
| `things/Armchair` | 0.6% (1/176) | 容器 |  |
| `things/Armchair/positions` | 0.6% (1/176) | 容器 |  |
| `things/Armchair/positions/li` | 1.1% (2/176) | 文本 | (0, 0, 0) / (1, 0, 0) |
| `things/Armchair/relativeRotation` | 0.6% (1/176) | 文本 | Opposite |
| `things/Armchair/stuff` | 0.6% (1/176) | 文本 | Leather_Plain |
| `things/Barricade` | 11.9% (21/176) | 容器 |  |
| `things/Barricade/hp` | 7.4% (13/176) | 数值 | 260 / 270 / 280 |
| `things/Barricade/position` | 6.8% (12/176) | 文本 | (1,0,0) / (2,0,2) / (3,0,0) |
| `things/Barricade/positions` | 0.6% (1/176) | 容器 |  |
| `things/Barricade/positions/li` | 4.5% (8/176) | 文本 | (0, 0, 1) / (1, 0, 0) / (2, 0, 0) |
| `things/Barricade/rects` | 4.5% (8/176) | 容器 |  |
| `things/Barricade/rects/li` | 35.2% (62/176) | 文本 | (0,0,0,1) / (1,1,1,1) / (5,0,5,1) |
| `things/Barricade/stuff` | 11.9% (21/176) | 文本 | Steel |
| `things/Battery` | 1.7% (3/176) | 容器 |  |
| `things/Battery/positions` | 1.7% (3/176) | 容器 |  |
| `things/Battery/positions/li` | 3.4% (6/176) | 文本 | (10, 0, 11) / (10, 0, 8) / (11, 0, 10) |
| `things/Battery/relativeRotation` | 0.6% (1/176) | 文本 | Clockwise |
| `things/BilliardsTable` | 0.6% (1/176) | 容器 |  |
| `things/BilliardsTable/position` | 0.6% (1/176) | 文本 | (1,0,1) |
| `things/BilliardsTable/relativeRotation` | 0.6% (1/176) | 文本 | Clockwise |
| `things/BilliardsTable/stuff` | 0.6% (1/176) | 文本 | WoodLog |
| `things/BiofuelRefinery` | 0.6% (1/176) | 容器 |  |
| `things/BiofuelRefinery/positions` | 0.6% (1/176) | 容器 |  |
| `things/BiofuelRefinery/positions/li` | 2.3% (4/176) | 文本 | (1, 0, 1) / (1, 0, 4) / (5, 0, 1) |
| `things/Blackboard` | 0.6% (1/176) | 容器 |  |
| `things/Blackboard/chance` | 0.6% (1/176) | 数值 | 0.75 |
| `things/Blackboard/positions` | 0.6% (1/176) | 容器 |  |
| `things/Blackboard/positions/li` | 1.1% (2/176) | 文本 | (1, 0, 4) / (4, 0, 4) |
| `things/Blackboard/relativeRotation` | 0.6% (1/176) | 文本 | Opposite |
| `things/Blackboard/stuff` | 0.6% (1/176) | 文本 | Steel |
| `things/BurrowWall` | 3.4% (6/176) | 容器 |  |
| `things/BurrowWall/chance` | 3.4% (6/176) | 数值 | 0.85 / 0.95 |
| `things/BurrowWall/positions` | 1.1% (2/176) | 容器 |  |
| `things/BurrowWall/positions/li` | 21.0% (37/176) | 文本 | (2, 0, 0) / (3, 0, 0) / (4, 0, 0) |
| `things/BurrowWall/rects` | 2.3% (4/176) | 容器 |  |
| `things/BurrowWall/rects/li` | 24.4% (43/176) | 文本 | (1,3,2,4) / (2,2,3,2) / (4,1,5,2) |
| `things/ChessTable` | 0.6% (1/176) | 容器 |  |
| `things/ChessTable/position` | 0.6% (1/176) | 文本 | (1,0,0) |
| `things/ChessTable/stuff` | 0.6% (1/176) | 文本 | WoodLog |
| `things/CollapsedRocks` | 0.6% (1/176) | 容器 |  |
| `things/CollapsedRocks/chance` | 0.6% (1/176) | 数值 | 0.75 |
| `things/CollapsedRocks/rects` | 0.6% (1/176) | 容器 |  |
| `things/CollapsedRocks/rects/li` | 1.1% (2/176) | 文本 | (0,0,1,1) / (2,1,2,1) |
| `things/Couch` | 1.1% (2/176) | 容器 |  |
| `things/Couch/position` | 1.1% (2/176) | 文本 | (1,0,0) / (1,0,2) |
| `things/Couch/relativeRotation` | 1.1% (2/176) | 文本 | Opposite |
| `things/Couch/stuff` | 1.1% (2/176) | 文本 | Leather_Plain |
| `things/Crib` | 0.6% (1/176) | 容器 |  |
| `things/Crib/positions` | 0.6% (1/176) | 容器 |  |
| `things/Crib/positions/li` | 2.3% (4/176) | 文本 | (1, 0, 1) / (1, 0, 3) / (3, 0, 1) |
| `things/Crib/relativeRotation` | 0.6% (1/176) | 文本 | Opposite |
| `things/Crib/stuff` | 0.6% (1/176) | 文本 | WoodLog |
| `things/DiningChair` | 4.0% (7/176) | 容器 |  |
| `things/DiningChair/chance` | 3.4% (6/176) | 数值 | 0.35 / 0.75 |
| `things/DiningChair/position` | 1.1% (2/176) | 文本 | (1,0,0) / (2,0,1) |
| `things/DiningChair/positions` | 2.8% (5/176) | 容器 |  |
| `things/DiningChair/positions/li` | 8.0% (14/176) | 文本 | (1, 0, 3) / (2, 0, 3) / (3, 0, 1) |
| `things/DiningChair/relativeRotation` | 2.8% (5/176) | 文本 | Clockwise / Counterclockwise / Opposite |
| `things/DiningChair/stuff` | 4.0% (7/176) | 文本 | Steel / WoodLog |
| `things/Door` | 4.0% (7/176) | 容器 |  |
| `things/Door/chance` | 1.1% (2/176) | 数值 | 0.5 / 0.8 |
| `things/Door/hp` | 0.6% (1/176) | 数值 | 140 |
| `things/Door/position` | 1.7% (3/176) | 文本 | (2,0,0) / (20,0,7) |
| `things/Door/positions` | 1.1% (2/176) | 容器 |  |
| `things/Door/positions/li` | 3.4% (6/176) | 文本 | (2, 0, 3) / (2, 0, 6) / (7, 0, 3) |
| `things/Door/rects` | 1.1% (2/176) | 容器 |  |
| `things/Door/rects/li` | 4.5% (8/176) | 文本 | (15,3,15,3) / (15,6,15,6) / (4,6,4,6) |
| `things/Door/relativeRotation` | 1.1% (2/176) | 文本 | Clockwise |
| `things/Door/stuff` | 4.0% (7/176) | 文本 | BlocksGranite / Steel |
| `things/Dresser` | 0.6% (1/176) | 容器 |  |
| `things/Dresser/position` | 0.6% (1/176) | 文本 | (1, 0, 2) |
| `things/Dresser/relativeRotation` | 0.6% (1/176) | 文本 | Opposite |
| `things/Dresser/stuff` | 0.6% (1/176) | 文本 | WoodLog |
| `things/EggBox` | 0.6% (1/176) | 容器 |  |
| `things/EggBox/chance` | 0.6% (1/176) | 数值 | 0.85 |
| `things/EggBox/rects` | 0.6% (1/176) | 容器 |  |
| `things/EggBox/rects/li` | 2.3% (4/176) | 文本 | (4,3,4,3) / (4,5,4,5) / (6,3,6,3) |
| `things/EggBox/stuff` | 0.6% (1/176) | 文本 | WoodLog |
| `things/ElectricStove` | 0.6% (1/176) | 容器 |  |
| `things/ElectricStove/position` | 0.6% (1/176) | 文本 | (2,0,2) |
| `things/EndTable` | 1.7% (3/176) | 容器 |  |
| `things/EndTable/chance` | 0.6% (1/176) | 数值 | 0.75 |
| `things/EndTable/position` | 1.1% (2/176) | 文本 | (1, 0, 1) / (2, 0, 2) |
| `things/EndTable/positions` | 0.6% (1/176) | 容器 |  |
| `things/EndTable/positions/li` | 0.6% (1/176) | 文本 | (0, 0, 2) |
| `things/EndTable/relativeRotation` | 1.7% (3/176) | 文本 | Opposite |
| `things/EndTable/stuff` | 1.7% (3/176) | 文本 | Steel / WoodLog |
| `things/Fence` | 0.6% (1/176) | 容器 |  |
| `things/Fence/rects` | 0.6% (1/176) | 容器 |  |
| `things/Fence/rects/li` | 2.8% (5/176) | 文本 | (0,2,2,2) / (0,3,0,9) / (1,9,1,9) |
| `things/Fence/stuff` | 0.6% (1/176) | 文本 | WoodLog |
| `things/FenceGate` | 0.6% (1/176) | 容器 |  |
| `things/FenceGate/position` | 0.6% (1/176) | 文本 | (2, 0, 9) |
| `things/FenceGate/stuff` | 0.6% (1/176) | 文本 | WoodLog |
| `things/Filth_BlastMark` | 1.7% (3/176) | 容器 |  |
| `things/Filth_BlastMark/chance` | 0.6% (1/176) | 数值 | 0.2 |
| `things/Filth_BlastMark/hp` | 1.7% (3/176) | 数值 | -1 |
| `things/Filth_BlastMark/position` | 1.7% (3/176) | 文本 | (1, 0, 1) / (2,0,2) / (5,0,1) |
| `things/Filth_Blood` | 2.8% (5/176) | 容器 |  |
| `things/Filth_Blood/hp` | 2.8% (5/176) | 数值 | -1 |
| `things/Filth_Blood/rects` | 2.8% (5/176) | 容器 |  |
| `things/Filth_Blood/rects/li` | 11.4% (20/176) | 文本 | (1,0,1,0) / (2,0,2,0) / (3,1,4,1) |
| `things/Filth_MachineBits` | 0.6% (1/176) | 容器 |  |
| `things/Filth_MachineBits/hp` | 0.6% (1/176) | 数值 | -1 |
| `things/Filth_MachineBits/rects` | 0.6% (1/176) | 容器 |  |
| `things/Filth_MachineBits/rects/li` | 1.7% (3/176) | 文本 | (3,0,3,0) / (4,1,4,1) / (6,2,6,2) |
| `things/Filth_OilSmear` | 0.6% (1/176) | 容器 |  |
| `things/Filth_OilSmear/rects` | 0.6% (1/176) | 容器 |  |
| `things/Filth_OilSmear/rects/li` | 1.7% (3/176) | 文本 | (2,5,2,5) / (6,4,6,4) / (7,5,7,5) |
| `things/FirefoamPopper` | 0.6% (1/176) | 容器 |  |
| `things/FlatscreenTelevision` | 0.6% (1/176) | 容器 |  |
| `things/FueledStove` | 0.6% (1/176) | 容器 |  |
| `things/FueledStove/position` | 0.6% (1/176) | 文本 | (1,0,1) |
| `things/Gloomlight` | 0.6% (1/176) | 容器 |  |
| `things/Gloomlight/rects` | 0.6% (1/176) | 容器 |  |
| `things/Gloomlight/rects/li` | 2.3% (4/176) | 文本 | (1,1,1,1) / (1,5,1,5) / (5,1,5,1) |
| `things/HiddenConduit` | 1.1% (2/176) | 容器 |  |
| `things/HiddenConduit/positions` | 0.6% (1/176) | 容器 |  |
| `things/HiddenConduit/positions/li` | 10.8% (19/176) | 文本 | (0, 0, 0) / (1, 0, 0) / (2, 0, 0) |
| `things/HiddenConduit/rects` | 0.6% (1/176) | 容器 |  |
| `things/HiddenConduit/rects/li` | 6.2% (11/176) | 文本 | (10,4,10,4) / (15,4,15,4) / (4,5,4,5) |
| `things/HydroponicsBasin` | 1.7% (3/176) | 容器 |  |
| `things/HydroponicsBasin/position` | 1.1% (2/176) | 文本 | (2,0,0) / (2,0,4) |
| `things/HydroponicsBasin/positions` | 0.6% (1/176) | 容器 |  |
| `things/HydroponicsBasin/positions/li` | 1.1% (2/176) | 文本 | (0, 0, 2) / (4, 0, 1) |
| `things/HydroponicsBasin/relativeRotation` | 1.1% (2/176) | 文本 | Clockwise / Counterclockwise |
| `things/InsectLairEntrance` | 0.6% (1/176) | 容器 |  |
| `things/InsectLairEntrance/position` | 0.6% (1/176) | 文本 | (2, 0, 2) |
| `things/MalfunctioningTransportPod` | 0.6% (1/176) | 容器 |  |
| `things/MechanoidProcessor` | 3.4% (6/176) | 容器 |  |
| `things/MechanoidProcessor/position` | 0.6% (1/176) | 文本 | (2,0,2) |
| `things/MechanoidProcessor/positions` | 2.8% (5/176) | 容器 |  |
| `things/MechanoidProcessor/positions/li` | 10.2% (18/176) | 文本 | (13, 0, 5) / (33, 0, 5) / (41, 0, 13) |
| `things/MechhiveAssembler` | 0.6% (1/176) | 容器 |  |
| `things/MechhiveAssembler/positions` | 0.6% (1/176) | 容器 |  |
| `things/MechhiveAssembler/positions/li` | 2.3% (4/176) | 文本 | (41, 0, 41) / (41, 0, 5) / (5, 0, 41) |
| `things/MechPylon` | 2.3% (4/176) | 容器 |  |
| `things/MechPylon/rects` | 2.3% (4/176) | 容器 |  |
| `things/MechPylon/rects/li` | 10.2% (18/176) | 文本 | (11,17,11,17) / (17,11,17,11) / (23,11,23,11) |
| `things/MechRelay` | 0.6% (1/176) | 容器 |  |
| `things/MechRelay/position` | 0.6% (1/176) | 文本 | (14, 0, 14) |
| `things/OrbitalAncientFortifiedWall` | 4.5% (8/176) | 容器 |  |
| `things/OrbitalAncientFortifiedWall/chance` | 2.8% (5/176) | 数值 | 0.8 / 0.99 |
| `things/OrbitalAncientFortifiedWall/positions` | 0.6% (1/176) | 容器 |  |
| `things/OrbitalAncientFortifiedWall/positions/li` | 2.3% (4/176) | 文本 | (4, 0, 0) / (4, 0, 1) / (4, 0, 2) |
| `things/OrbitalAncientFortifiedWall/rects` | 4.0% (7/176) | 容器 |  |
| `things/OrbitalAncientFortifiedWall/rects/li` | 31.2% (55/176) | 文本 | (0,0,8,0) / (0,1,0,8) / (3,1,3,1) |
| `things/Pallet_Medicine` | 0.6% (1/176) | 容器 |  |
| `things/Pallet_Medicine/chance` | 0.6% (1/176) | 数值 | 0.75 |
| `things/Pallet_SurvivalMeals` | 0.6% (1/176) | 容器 |  |
| `things/Pallet_SurvivalMeals/chance` | 0.6% (1/176) | 数值 | 0.5 |
| `things/PokerTable` | 0.6% (1/176) | 容器 |  |
| `things/PokerTable/position` | 0.6% (1/176) | 文本 | (1,0,1) |
| `things/PokerTable/stuff` | 0.6% (1/176) | 文本 | WoodLog |
| `things/RubblePile` | 2.8% (5/176) | 容器 |  |
| `things/RubblePile/chance` | 2.8% (5/176) | 数值 | 0.5 / 0.75 / 0.8 |
| `things/RubblePile/positions` | 0.6% (1/176) | 容器 |  |
| `things/RubblePile/positions/li` | 5.1% (9/176) | 文本 | (0, 0, 0) / (0, 0, 1) / (1, 0, 0) |
| `things/RubblePile/rects` | 2.3% (4/176) | 容器 |  |
| `things/RubblePile/rects/li` | 15.3% (27/176) | 文本 | (2,1,2,2) / (2,6,4,6) / (6,2,7,2) |
| `things/Sandbags` | 1.1% (2/176) | 容器 |  |
| `things/Sandbags/chance` | 1.1% (2/176) | 数值 | 0.85 / 0.9 |
| `things/Sandbags/positions` | 1.1% (2/176) | 容器 |  |
| `things/Sandbags/positions/li` | 36.4% (64/176) | 文本 | (0, 0, 0) / (1, 0, 0) / (2, 0, 0) |
| `things/Sandbags/stuff` | 1.1% (2/176) | 文本 | Cloth |
| `things/SchoolDesk` | 0.6% (1/176) | 容器 |  |
| `things/SchoolDesk/positions` | 0.6% (1/176) | 容器 |  |
| `things/SchoolDesk/positions/li` | 2.3% (4/176) | 文本 | (0, 0, 0) / (0, 0, 2) / (3, 0, 0) |
| `things/SchoolDesk/stuff` | 0.6% (1/176) | 文本 | WoodLog |
| `things/SculptureSmall` | 0.6% (1/176) | 容器 |  |
| `things/SculptureSmall/stuff` | 0.6% (1/176) | 文本 | WoodLog |
| `things/Shelf` | 2.3% (4/176) | 容器 |  |
| `things/Shelf/position` | 0.6% (1/176) | 文本 | (1,0,1) |
| `things/Shelf/positions` | 1.7% (3/176) | 容器 |  |
| `things/Shelf/positions/li` | 6.2% (11/176) | 文本 | (0, 0, 1) / (0, 0, 4) / (2, 0, 1) |
| `things/Shelf/relativeRotation` | 1.7% (3/176) | 文本 | Opposite |
| `things/Shelf/stuff` | 2.3% (4/176) | 文本 | Steel / WoodLog |
| `things/ShelfSmall` | 0.6% (1/176) | 容器 |  |
| `things/ShelfSmall/position` | 0.6% (1/176) | 文本 | (0,0,1) |
| `things/ShelfSmall/relativeRotation` | 0.6% (1/176) | 文本 | Opposite |
| `things/ShelfSmall/stuff` | 0.6% (1/176) | 文本 | Steel |
| `things/ShipChunk_Mech` | 0.6% (1/176) | 容器 |  |
| `things/ShuttleCrashed` | 0.6% (1/176) | 容器 |  |
| `things/ShuttleCrashed/hp` | 0.6% (1/176) | 数值 | 158 |
| `things/ShuttleCrashed/position` | 0.6% (1/176) | 文本 | (3,0,2) |
| `things/SolarGenerator` | 1.1% (2/176) | 容器 |  |
| `things/SolarGenerator/positions` | 1.1% (2/176) | 容器 |  |
| `things/SolarGenerator/positions/li` | 9.1% (16/176) | 文本 | (12, 0, 2) / (17, 0, 2) / (2, 0, 2) |
| `things/SolidIce` | 2.8% (5/176) | 容器 |  |
| `things/SolidIce/chance` | 1.7% (3/176) | 数值 | 0.95 |
| `things/SolidIce/positions` | 2.8% (5/176) | 容器 |  |
| `things/SolidIce/positions/li` | 31.8% (56/176) | 文本 | (0, 0, 0) / (0, 0, 1) / (1, 0, 0) |
| `things/Stool` | 10.8% (19/176) | 容器 |  |
| `things/Stool/chance` | 9.1% (16/176) | 数值 | 0.3 / 0.5 / 0.66 |
| `things/Stool/position` | 2.8% (5/176) | 文本 | (1,0,0) / (1,0,1) / (2,0,0) |
| `things/Stool/positions` | 5.7% (10/176) | 容器 |  |
| `things/Stool/positions/li` | 13.6% (24/176) | 文本 | (0, 0, 0) / (0, 0, 1) / (2, 0, 0) |
| `things/Stool/rects` | 2.3% (4/176) | 容器 |  |
| `things/Stool/rects/li` | 8.0% (14/176) | 文本 | (0,0,0,3) / (1,0,1,0) / (3,0,3,3) |
| `things/Stool/relativeRotation` | 4.5% (8/176) | 文本 | Clockwise / Counterclockwise / Opposite |
| `things/Stool/stuff` | 10.8% (19/176) | 文本 | Steel / WoodLog |
| `things/SunLamp` | 0.6% (1/176) | 容器 |  |
| `things/SunLamp/position` | 0.6% (1/176) | 文本 | (2,0,2) |
| `things/SurveyScanner` | 0.6% (1/176) | 容器 |  |
| `things/SurveyScanner/position` | 0.6% (1/176) | 文本 | (4,0,4) |
| `things/Table1x2c` | 0.6% (1/176) | 容器 |  |
| `things/Table1x2c/position` | 0.6% (1/176) | 文本 | (1,0,0) |
| `things/Table1x2c/stuff` | 0.6% (1/176) | 文本 | Steel |
| `things/Table2x2c` | 1.1% (2/176) | 容器 |  |
| `things/Table2x2c/position` | 1.1% (2/176) | 文本 | (1,0,1) |
| `things/Table2x2c/stuff` | 1.1% (2/176) | 文本 | Steel / WoodLog |
| `things/Table2x4c` | 1.1% (2/176) | 容器 |  |
| `things/Table2x4c/position` | 1.1% (2/176) | 文本 | (1,0,1) |
| `things/Table2x4c/stuff` | 1.1% (2/176) | 文本 | Steel / WoodLog |
| `things/Turret_Autocannon` | 0.6% (1/176) | 容器 |  |
| `things/Turret_Autocannon/chance` | 0.6% (1/176) | 数值 | 0.85 |
| `things/Turret_Autocannon/position` | 0.6% (1/176) | 文本 | (2, 0, 17) |
| `things/Turret_AutoChargeBlaster` | 0.6% (1/176) | 容器 |  |
| `things/Turret_AutoChargeBlaster/positions` | 0.6% (1/176) | 容器 |  |
| `things/Turret_AutoChargeBlaster/positions/li` | 1.1% (2/176) | 文本 | (11, 0, 11) / (35, 0, 35) |
| `things/Turret_AutoInferno` | 0.6% (1/176) | 容器 |  |
| `things/Turret_AutoInferno/positions` | 0.6% (1/176) | 容器 |  |
| `things/Turret_AutoInferno/positions/li` | 1.1% (2/176) | 文本 | (11, 0, 35) / (35, 0, 11) |
| `things/Turret_Sniper` | 1.1% (2/176) | 容器 |  |
| `things/Turret_Sniper/chance` | 0.6% (1/176) | 数值 | 0.85 |
| `things/Turret_Sniper/position` | 1.1% (2/176) | 文本 | (17, 0, 2) / (8, 0, 11) |
| `things/Vent` | 0.6% (1/176) | 容器 |  |
| `things/Vent/position` | 0.6% (1/176) | 文本 | (2,0,2) |
| `things/Wall` | 7.4% (13/176) | 容器 |  |
| `things/Wall/chance` | 1.1% (2/176) | 数值 | 0.25 / 0.9 |
| `things/Wall/hp` | 4.5% (8/176) | 数值 | 450 / 470 / 490 |
| `things/Wall/position` | 2.3% (4/176) | 文本 | (1,0,3) / (20,0,8) / (3,0,6) |
| `things/Wall/positions` | 3.4% (6/176) | 容器 |  |
| `things/Wall/positions/li` | 33.0% (58/176) | 文本 | (20, 0, 10) / (24, 0, 5) / (25, 0, 6) |
| `things/Wall/rects` | 1.7% (3/176) | 容器 |  |
| `things/Wall/rects/li` | 16.5% (29/176) | 文本 | (1,3,2,3) / (2,2,7,2) / (4,3,4,5) |
| `things/Wall/stuff` | 7.4% (13/176) | 文本 | BlocksGranite / BlocksLimestone / WoodLog |

## 四、原版 defName 一览（共 176 个，列出前 60）

```text
`Exterior_ShipChunk_Mech`         `AncientSealedCrate`              `MalfunctioningTransportPod`      `AncientSpacerCrate`            
`FirefoamPopper`                  `AncientLargeMechGestator`        `AncientStandardRecharger`        `AncientLamp_Single`            
`AncientSteelPallet`              `AncientSafe`                     `MedicinePallet`                  `SurvivalMealPallet`            
`AncientOpenContainer`            `AncientTank`                     `InsectLairEntrance`              `SculptureSmall`                
`AncientSystemRack`               `AncientStorageCylinder_Edge`     `AncientSecurityTerminal`         `AncientLamp_Edge`              
`AncientTableStoveElectric_Edge`  `AncientForklift`                 `AncientTerraformer`              `SpaceTerrain`                  
`AncientBasicRecharger_Edge`      `AncientDisplayBank_Edge`         `AncientMachine_Rows`             `AncientEquipmentBlocks_Rows`   
`AncientDestroyedConsole_VerySmall`  `AncientCratePallet_Cluster`      `AncientMilitaryCrate_Cluster`    `AncientAmmoStack_Cluster`      
`AncientChembarrelPallet_Cluster`  `BilliardsTable`                  `AncientFortifiedWall_Edge`       `OrbitalRelay_Scatter_3`        
`CollapsedRocks_Cluster`          `Subroom_Partialwall`             `IndustrialShelf_Edge`            `FueledStove`                   
`Shelf`                           `Couch_Edge`                      `OrbitalRelay_Scatter_1`          `OrbitalRelay_Scatter_2`        
`AncientMechGestator_Cluster`     `AncientSystemRacks_Rows`         `AncientLockerBank_Row`           `AncientFortifiedWall_PillarGroup`
`AncientFuelNodeArray`            `SolidIce_AlongWall`              `FlatscreenTelevision`            `MechanoidProcessor`            
`Exterior_AncientLaunchSite_LaunchPad_GridEntry`  `AncientSimpleResearchBench`      `BathtubWithStool`                `AncientChemfuelCanister_Cluster`
`AncientStove_Cluster`            `AncientFilingCabinet_Edge`       `AncientCardboardBox_Cluster`     `AncientSpacerCrate_Cluster`    
```

_余下 116 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
