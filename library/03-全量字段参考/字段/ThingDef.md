# ThingDef

- **所属线**：物品线
- **原版实例数**：2054
- **字段路径数**：2699
- **资料片**：Anomaly、Biotech、Core、Ideology、Odyssey、Royalty
- **原版出处**：`Anomaly/Defs/ThingDefs_Buildings/Buildings_Fleshmass.xml`、`Odyssey/Defs/ThingDefs_Buildings/Buildings_Ancient_OpenableContainers.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<ThingDef ParentName="Fleshmass">
    <defName>Fleshmass_Active</defName>
  </ThingDef>

  
```

> 来自 `Anomaly/Defs/ThingDefs_Buildings/Buildings_Fleshmass.xml`，defName = `Fleshmass_Active`，XML 节点数 2（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

_该类型没有出现率≥90% 的字段（字段高度自由）。_

## 三、全量字段表（2699 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `allowedArchonexusCount` | 2.9% (59/2054) | 数值 | -1 / 1 / 200 |
| `altitudeLayer` | 23.5% (483/2054) | 文本 | MetaOverlays / MoteLow / MoteOverhead |
| `alwaysFlee` | 0.2% (5/2054) | 布尔 | true |
| `alwaysHaulable` | 1.1% (22/2054) | 布尔 | True / false / true |
| `apparel` | 6.2% (128/2054) | 容器 |  |
| `apparel/abilities` | 0.1% (1/2054) | 容器 |  |
| `apparel/abilities/li` | 0.1% (3/2054) | 文本 | CallDropPods / CallMechanoids / DeactivateMechanoid |
| `apparel/ai_pickUpOpportunistically` | 0.1% (3/2054) | 布尔 | true |
| `apparel/anyTechLevelCanUseForWarmth` | 0.1% (2/2054) | 布尔 | true |
| `apparel/blocksAddedPartWoundGraphics` | 0.1% (1/2054) | 布尔 | true |
| `apparel/blocksVision` | 0.1% (1/2054) | 布尔 | true |
| `apparel/bodyPartGroups` | 4.6% (95/2054) | 容器 |  |
| `apparel/bodyPartGroups/li` | 8.7% (178/2054) | 文本 | FullHead / Neck / Torso |
| `apparel/canBeDesiredForIdeo` | 1.2% (25/2054) | 布尔 | false / true |
| `apparel/canBeGeneratedToSatisfyToxicEnvironmentResistance` | 1.2% (24/2054) | 布尔 | false |
| `apparel/canBeGeneratedToSatisfyWarmth` | 1.2% (25/2054) | 布尔 | false |
| `apparel/careIfDamaged` | 1.0% (20/2054) | 布尔 | false |
| `apparel/careIfWornByCorpse` | 1.0% (20/2054) | 布尔 | false |
| `apparel/countsAsClothingForNudity` | 2.4% (49/2054) | 布尔 | false |
| `apparel/defaultOutfitTags` | 2.6% (53/2054) | 容器 |  |
| `apparel/defaultOutfitTags/li` | 3.9% (79/2054) | 文本 | Nudist / Soldier / Spacefarer |
| `apparel/developmentalStageFilter` | 1.2% (24/2054) | 文本 | Child / Child, Adult |
| `apparel/drawData` | 0.4% (9/2054) | 容器 |  |
| `apparel/drawData/dataNorth` | 0.3% (7/2054) | 容器 |  |
| `apparel/drawData/dataNorth/layer` | 0.3% (7/2054) | 数值 | -3 / 68 |
| `apparel/drawData/defaultData` | 0.1% (3/2054) | 容器 |  |
| `apparel/drawData/defaultData/layer` | 0.1% (3/2054) | 数值 | 48 / 61 / 83 |
| `apparel/forceEyesVisibleForRotations` | 0.5% (10/2054) | 容器 |  |
| `apparel/forceEyesVisibleForRotations/li` | 1.5% (30/2054) | 数值 | 1 / 2 / 3 |
| `apparel/gender` | 0.2% (4/2054) | 文本 | Female / Male |
| `apparel/ideoDesireAllowedFactionCategoryTags` | 0.1% (2/2054) | 容器 |  |
| `apparel/ideoDesireAllowedFactionCategoryTags/li` | 0.1% (2/2054) | 文本 | Tribal |
| `apparel/ideoDesireDisallowedFactionCategoryTags` | 0.1% (2/2054) | 容器 |  |
| `apparel/ideoDesireDisallowedFactionCategoryTags/li` | 0.1% (2/2054) | 文本 | Tribal |
| `apparel/ignoredByNonViolent` | 0.3% (6/2054) | 布尔 | true |
| `apparel/immuneToToxGasExposure` | 0.1% (2/2054) | 布尔 | true |
| `apparel/layers` | 4.3% (89/2054) | 容器 |  |
| `apparel/layers/li` | 4.7% (96/2054) | 文本 | Belt / OnSkin / Overhead |
| `apparel/legsNakedUnlessCoveredBySomethingElse` | 0.1% (1/2054) | 布尔 | true |
| `apparel/mechanitorApparel` | 0.3% (6/2054) | 布尔 | true |
| `apparel/parentTagDef` | 0.5% (11/2054) | 文本 | ApparelBody / ApparelHead |
| `apparel/renderSkipFlags` | 0.6% (13/2054) | 容器 |  |
| `apparel/renderSkipFlags/li` | 0.6% (13/2054) | 文本 | Head / None |
| `apparel/scoreOffset` | 1.1% (23/2054) | 数值 | -10 / 4 |
| `apparel/shellRenderedBehindHead` | 0.1% (1/2054) | 布尔 | true |
| `apparel/slaveApparel` | 0.1% (2/2054) | 布尔 | true |
| `apparel/soundRemove` | 0.2% (5/2054) | 文本 | Remove_PowerArmor |
| `apparel/soundWear` | 0.2% (5/2054) | 文本 | Wear_PowerArmor |
| `apparel/tags` | 2.9% (59/2054) | 容器 |  |
| `apparel/tags/li` | 3.9% (81/2054) | 文本 | Horaxian / HoraxianCeremonial / IndustrialBasic |
| `apparel/useDeflectMetalEffect` | 0.4% (8/2054) | 布尔 | true |
| `apparel/useWornGraphicMask` | 0.3% (6/2054) | 布尔 | true |
| `apparel/wearPerDay` | 1.0% (20/2054) | 数值 | 0 |
| `apparel/wornGraphicData` | 1.0% (20/2054) | 容器 |  |
| `apparel/wornGraphicData/east` | 1.0% (20/2054) | 容器 |  |
| `apparel/wornGraphicData/east/fat` | 0.8% (17/2054) | 容器 |  |
| `apparel/wornGraphicData/east/fat/offset` | 0.8% (17/2054) | 文本 | (-0.1,0) / (-0.15,0) / (-0.15,0.05) |
| `apparel/wornGraphicData/east/female` | 0.1% (1/2054) | 容器 |  |
| `apparel/wornGraphicData/east/female/offset` | 0.1% (1/2054) | 文本 | (0.05,0.05) |
| `apparel/wornGraphicData/east/hulk` | 0.8% (17/2054) | 容器 |  |
| `apparel/wornGraphicData/east/hulk/offset` | 0.8% (17/2054) | 文本 | (-0.1,0) / (-0.15,0) |
| `apparel/wornGraphicData/east/male` | 0.2% (5/2054) | 容器 |  |
| `apparel/wornGraphicData/east/male/offset` | 0.2% (5/2054) | 文本 | (0,0.1) |
| `apparel/wornGraphicData/east/offset` | 1.0% (20/2054) | 文本 | (-0.05,-0.3) / (-0.35,-0.05) / (-0.35,-0.1) |
| `apparel/wornGraphicData/east/scale` | 0.3% (7/2054) | 文本 | (0.65,0.65) / (0.75,0.75) / (0.83,0.83) |
| `apparel/wornGraphicData/east/thin` | 0.8% (17/2054) | 容器 |  |
| `apparel/wornGraphicData/east/thin/offset` | 0.8% (17/2054) | 文本 | (0,0.1) / (0.05,0) / (0.05,0.1) |
| `apparel/wornGraphicData/fat` | 0.7% (15/2054) | 容器 |  |
| `apparel/wornGraphicData/fat/scale` | 0.7% (15/2054) | 文本 | (0.45,0.45) / (0.75,0.75) / (0.8,0.8) |
| `apparel/wornGraphicData/female` | 0.7% (15/2054) | 容器 |  |
| `apparel/wornGraphicData/female/scale` | 0.7% (15/2054) | 文本 | (0.4,0.4) / (0.6,0.6) / (0.7,0.7) |
| `apparel/wornGraphicData/hulk` | 0.7% (15/2054) | 容器 |  |
| `apparel/wornGraphicData/hulk/scale` | 0.7% (15/2054) | 文本 | (0.45,0.45) / (0.75,0.75) / (0.8,0.8) |
| `apparel/wornGraphicData/male` | 0.7% (15/2054) | 容器 |  |
| `apparel/wornGraphicData/male/scale` | 0.7% (15/2054) | 文本 | (0.4,0.4) / (0.6,0.6) / (0.75,0.75) |
| `apparel/wornGraphicData/north` | 0.9% (19/2054) | 容器 |  |
| `apparel/wornGraphicData/north/fat` | 0.1% (3/2054) | 容器 |  |
| `apparel/wornGraphicData/north/fat/offset` | 0.1% (3/2054) | 文本 | (0.45,-0.25) |
| `apparel/wornGraphicData/north/female` | 0.1% (3/2054) | 容器 |  |
| `apparel/wornGraphicData/north/female/offset` | 0.1% (3/2054) | 文本 | (0.25,-0.25) |
| `apparel/wornGraphicData/north/hulk` | 0.1% (3/2054) | 容器 |  |
| `apparel/wornGraphicData/north/hulk/offset` | 0.1% (3/2054) | 文本 | (0.25,-0.3) |
| `apparel/wornGraphicData/north/male` | 0.1% (3/2054) | 容器 |  |
| `apparel/wornGraphicData/north/male/offset` | 0.1% (3/2054) | 文本 | (0.25, -0.25) |
| `apparel/wornGraphicData/north/offset` | 0.5% (11/2054) | 文本 | (0,-0.15) / (0,0) |
| `apparel/wornGraphicData/north/scale` | 0.2% (5/2054) | 文本 | (0.65,0.65) / (0.7,0.7) / (0.85,0.85) |
| `apparel/wornGraphicData/north/thin` | 0.1% (3/2054) | 容器 |  |
| `apparel/wornGraphicData/north/thin/offset` | 0.1% (3/2054) | 文本 | (0.15,-0.25) |
| `apparel/wornGraphicData/renderUtilityAsPack` | 1.0% (20/2054) | 布尔 | true |
| `apparel/wornGraphicData/south` | 0.9% (18/2054) | 容器 |  |
| `apparel/wornGraphicData/south/fat` | 0.1% (3/2054) | 容器 |  |
| `apparel/wornGraphicData/south/fat/offset` | 0.1% (3/2054) | 文本 | (-0.5,-0.25) |
| `apparel/wornGraphicData/south/female` | 0.1% (3/2054) | 容器 |  |
| `apparel/wornGraphicData/south/female/offset` | 0.1% (3/2054) | 文本 | (-0.3,-0.25) |
| `apparel/wornGraphicData/south/hulk` | 0.1% (3/2054) | 容器 |  |
| `apparel/wornGraphicData/south/hulk/offset` | 0.1% (3/2054) | 文本 | (-0.3,-0.3) |
| `apparel/wornGraphicData/south/male` | 0.1% (3/2054) | 容器 |  |
| `apparel/wornGraphicData/south/male/offset` | 0.1% (3/2054) | 文本 | (-0.3, -0.25) |
| `apparel/wornGraphicData/south/offset` | 0.7% (15/2054) | 文本 | (0,-0.15) / (0,0) / (0,0.1) |
| `apparel/wornGraphicData/south/scale` | 0.4% (8/2054) | 文本 | (0.65,0.65) / (0.7,0.7) / (0.85,0.85) |
| `apparel/wornGraphicData/south/thin` | 0.1% (3/2054) | 容器 |  |
| `apparel/wornGraphicData/south/thin/offset` | 0.1% (3/2054) | 文本 | (-0.2,-0.25) |
| `apparel/wornGraphicData/thin` | 0.7% (15/2054) | 容器 |  |
| `apparel/wornGraphicData/thin/scale` | 0.7% (15/2054) | 文本 | (0.35,0.35) / (0.4,0.4) / (0.6,0.6) |
| `apparel/wornGraphicData/west` | 0.8% (17/2054) | 容器 |  |
| `apparel/wornGraphicData/west/fat` | 0.8% (17/2054) | 容器 |  |
| `apparel/wornGraphicData/west/fat/offset` | 0.8% (17/2054) | 文本 | (0.1,0) / (0.15,0) / (0.15,0.05) |
| `apparel/wornGraphicData/west/female` | 0.1% (1/2054) | 容器 |  |
| `apparel/wornGraphicData/west/female/offset` | 0.1% (1/2054) | 文本 | (-0.05,0.05) |
| `apparel/wornGraphicData/west/hulk` | 0.8% (17/2054) | 容器 |  |
| `apparel/wornGraphicData/west/hulk/offset` | 0.8% (17/2054) | 文本 | (0.1,0) / (0.15,0) |
| `apparel/wornGraphicData/west/male` | 0.2% (5/2054) | 容器 |  |
| `apparel/wornGraphicData/west/male/offset` | 0.2% (5/2054) | 文本 | (0,0.1) |
| `apparel/wornGraphicData/west/offset` | 0.8% (17/2054) | 文本 | (0.35,-0.05) / (0.35,-0.1) / (0.35,-0.1)) |
| `apparel/wornGraphicData/west/scale` | 0.3% (7/2054) | 文本 | (0.65,0.65) / (0.75,0.75) / (0.83,0.83) |
| `apparel/wornGraphicData/west/thin` | 0.8% (17/2054) | 容器 |  |
| `apparel/wornGraphicData/west/thin/offset` | 0.8% (17/2054) | 文本 | (-0.05,0) / (-0.05,0.1) / (0,0.1) |
| `apparel/wornGraphicPath` | 5.1% (104/2054) | 文本 | Things/Pawn/Humanlike/Apparel/DisruptorFlarePack/DisruptorFlarePack / Things/Pawn/Humanlike/Apparel/TurretPack |
| `apparel/wornGraphicPaths` | 0.1% (2/2054) | 容器 |  |
| `apparel/wornGraphicPaths/li` | 0.3% (6/2054) | 文本 | Things/Pawn/Humanlike/Apparel/SliceCap/SliceCapA / Things/Pawn/Humanlike/Apparel/VisageMask/VisageMaskA / Thin |
| `autoTargetNearbyIdenticalThings` | 0.1% (2/2054) | 布尔 | true |
| `blockLight` | 0.9% (18/2054) | 布尔 | false / true |
| `blockPlants` | 0.1% (3/2054) | 布尔 | true |
| `blocksAltitudes` | 0.1% (1/2054) | 容器 |  |
| `blocksAltitudes/li` | 0.1% (1/2054) | 文本 | FloorCoverings |
| `blockWeather` | 0.1% (3/2054) | 布尔 | true |
| `blockWind` | 3.1% (63/2054) | 布尔 | false / true |
| `bringAlongOnGravship` | 0.2% (5/2054) | 布尔 | false |
| `building` | 19.4% (398/2054) | 容器 |  |
| `building/ai_chillDestination` | 3.0% (61/2054) | 布尔 | false |
| `building/ai_combatDangerous` | 0.4% (9/2054) | 布尔 | false / true |
| `building/ai_neverTrashThis` | 0.3% (6/2054) | 布尔 | true |
| `building/allowAutoroof` | 0.1% (1/2054) | 布尔 | false |
| `building/allowWireConnection` | 0.1% (1/2054) | 布尔 | false |
| `building/alwaysDeconstructible` | 0.4% (9/2054) | 布尔 | false / true |
| `building/alwaysExchangeVacuum` | 0.1% (1/2054) | 布尔 | true |
| `building/alwaysShowRelatedBuildCommands` | 0.1% (1/2054) | 布尔 | true |
| `building/alwaysUninstallable` | 0.1% (1/2054) | 布尔 | true |
| `building/artificialForMeditationPurposes` | 1.6% (32/2054) | 布尔 | false / true |
| `building/barDrawData` | 0.2% (4/2054) | 容器 |  |
| `building/barDrawData/east` | 0.2% (4/2054) | 容器 |  |
| `building/barDrawData/east/preRotationOffset` | 0.2% (4/2054) | 文本 | (0.04148867,0.6301422) / (0.1157379,-0.006530767) / (1.06, -0.97) |
| `building/barDrawData/east/size` | 0.2% (4/2054) | 文本 | (0.4066238,0.1425552) / (0.4481201,0.1160278) / (0.7, 0.13) |
| `building/barDrawData/north` | 0.2% (4/2054) | 容器 |  |
| `building/barDrawData/north/preRotationOffset` | 0.2% (4/2054) | 文本 | (-0.01598358,0.0255661) / (-1.06, 0.91) / (-1.59, 1.4) |
| `building/barDrawData/north/size` | 0.2% (4/2054) | 文本 | (0.4398041,0.1365509) / (0.5505219,0.1139069) / (0.7, 0.13) |
| `building/barDrawData/south` | 0.2% (4/2054) | 容器 |  |
| `building/barDrawData/south/preRotationOffset` | 0.2% (4/2054) | 文本 | (-0.002609305,-0.6002655) / (-1.06, 0.82) / (-1.59, 1.33) |
| `building/barDrawData/south/size` | 0.2% (4/2054) | 文本 | (0.4398041,0.121376) / (0.5479813,0.1345978) / (0.7, 0.13) |
| `building/barDrawData/west` | 0.2% (4/2054) | 容器 |  |
| `building/barDrawData/west/preRotationOffset` | 0.2% (4/2054) | 文本 | (-0.02767944,0.6171188) / (-0.1114426,-0.005119322) / (-1.06, -0.97) |
| `building/barDrawData/west/size` | 0.2% (4/2054) | 文本 | (0.397522,0.1395264) / (0.4646759,0.1281815) / (0.7, 0.13) |
| `building/bed_canBeMedical` | 0.1% (1/2054) | 布尔 | false |
| `building/bed_caravansCanUse` | 0.1% (2/2054) | 布尔 | true |
| `building/bed_countsForBedroomOrBarracks` | 0.1% (1/2054) | 布尔 | false |
| `building/bed_crib` | 0.1% (1/2054) | 布尔 | True |
| `building/bed_defaultMedical` | 0.1% (1/2054) | 布尔 | true |
| `building/bed_DisplayOwnersInInspectString` | 0.1% (1/2054) | 布尔 | false |
| `building/bed_DisplayOwnerType` | 0.1% (3/2054) | 布尔 | false |
| `building/bed_emptyCountsForBarracks` | 0.1% (1/2054) | 布尔 | false |
| `building/bed_healPerDay` | 0.4% (8/2054) | 数值 | 1 / 10 / 4 |
| `building/bed_humanlike` | 0.1% (2/2054) | 布尔 | false |
| `building/bed_maxBodySize` | 0.1% (3/2054) | 数值 | 0.25 / 0.55 |
| `building/bed_pawnDrawOffset` | 0.1% (1/2054) | 数值 | -0.15 |
| `building/bed_showSleeperBody` | 0.6% (13/2054) | 布尔 | False / True / false |
| `building/bed_slabBed` | 0.1% (2/2054) | 布尔 | true |
| `building/bed_UseSheetColor` | 0.1% (1/2054) | 布尔 | false |
| `building/biomeSpecific` | 0.1% (1/2054) | 布尔 | true |
| `building/blueprintClass` | 0.4% (8/2054) | 文本 | Blueprint_Build / Blueprint_Door / Blueprint_Storage |
| `building/blueprintGraphicData` | 0.7% (14/2054) | 容器 |  |
| `building/blueprintGraphicData/allowFlip` | 0.1% (1/2054) | 布尔 | false |
| `building/blueprintGraphicData/drawRotated` | 0.1% (1/2054) | 布尔 | false |
| `building/blueprintGraphicData/drawSize` | 0.1% (3/2054) | 文本 | (1.5,1.5) / (2.6, 3.1) |
| `building/blueprintGraphicData/graphicClass` | 0.3% (7/2054) | 文本 | Graphic_Appearances / Graphic_Multi / Graphic_Single |
| `building/blueprintGraphicData/shaderType` | 0.2% (4/2054) | 文本 | EdgeDetect / Transparent |
| `building/blueprintGraphicData/texPath` | 0.7% (14/2054) | 文本 | Things/Building/Linked/PowerConduit_Blueprint_Atlas / Things/Building/Linked/Sandbags_Blueprint_Atlas / Things |
| `building/bookendGraphicEast` | 0.1% (2/2054) | 容器 |  |
| `building/bookendGraphicEast/addTopAltitudeBias` | 0.1% (2/2054) | 布尔 | true |
| `building/bookendGraphicEast/drawSize` | 0.1% (2/2054) | 文本 | (2,2) / (2,3) |
| `building/bookendGraphicEast/graphicClass` | 0.1% (2/2054) | 文本 | Graphic_Single |
| `building/bookendGraphicEast/texPath` | 0.1% (2/2054) | 文本 | Things/Building/Furniture/Bookcase/BookcaseSmall_Bookend_east / Things/Building/Furniture/Bookcase/Bookcase_Bo |
| `building/bookendGraphicNorth` | 0.1% (2/2054) | 容器 |  |
| `building/bookendGraphicNorth/addTopAltitudeBias` | 0.1% (2/2054) | 布尔 | true |
| `building/bookendGraphicNorth/drawSize` | 0.1% (2/2054) | 文本 | (2,2) / (3,2) |
| `building/bookendGraphicNorth/graphicClass` | 0.1% (2/2054) | 文本 | Graphic_Single |
| `building/bookendGraphicNorth/texPath` | 0.1% (2/2054) | 文本 | Things/Building/Furniture/Bookcase/BookcaseSmall_Bookend_north / Things/Building/Furniture/Bookcase/Bookcase_B |
| `building/boughtConceptLearnOpportunity` | 0.1% (3/2054) | 文本 | TVForSickPeople |
| `building/buildingSizeCategory` | 0.3% (7/2054) | 文本 | Medium / Small |
| `building/buildingTags` | 3.3% (67/2054) | 容器 |  |
| `building/buildingTags/li` | 3.8% (77/2054) | 文本 | Anomaly / Bed / Biotech |
| `building/canBeDamagedByAttacks` | 0.1% (1/2054) | 布尔 | false |
| `building/canBuildNonEdificesUnder` | 0.8% (17/2054) | 布尔 | false / true |
| `building/canConstructInCorner` | 0.1% (1/2054) | 布尔 | true |
| `building/canExchangeVacuum` | 0.1% (2/2054) | 布尔 | true |
| `building/canLandGravshipOn` | 1.3% (26/2054) | 布尔 | true |
| `building/canPlaceOverImpassablePlant` | 0.6% (12/2054) | 布尔 | false |
| `building/canPlaceOverWall` | 0.1% (3/2054) | 布尔 | true |
| `building/claimable` | 4.0% (82/2054) | 布尔 | false / true |
| `building/combatPower` | 0.9% (18/2054) | 数值 | 150 / 190 / 250 |
| `building/crater` | 0.1% (1/2054) | 布尔 | true |
| `building/deconstructible` | 3.3% (68/2054) | 布尔 | false |
| `building/defaultPlantToGrow` | 0.1% (3/2054) | 文本 | Plant_Daylily / Plant_Rice / Plant_TreeBonsai |
| `building/defaultStorageSettings` | 0.5% (10/2054) | 容器 |  |
| `building/defaultStorageSettings/filter` | 0.5% (10/2054) | 容器 |  |
| `building/defaultStorageSettings/filter/categories` | 0.5% (10/2054) | 容器 |  |
| `building/defaultStorageSettings/filter/categories/li` | 0.8% (16/2054) | 文本 | Foods / Items / Manufactured |
| `building/defaultStorageSettings/filter/disallowedCategories` | 0.1% (3/2054) | 容器 |  |
| `building/defaultStorageSettings/filter/disallowedCategories/li` | 0.2% (4/2054) | 文本 | ApparelUtility / EggsFertilized / Weapons |
| `building/defaultStorageSettings/filter/disallowedThingDefs` | 0.2% (4/2054) | 容器 |  |
| `building/defaultStorageSettings/filter/disallowedThingDefs/li` | 0.8% (17/2054) | 文本 | InsectJelly / MealLavish / MealLavish_Meat |
| `building/defaultStorageSettings/filter/specialFiltersToAllow` | 0.1% (1/2054) | 容器 |  |
| `building/defaultStorageSettings/filter/specialFiltersToAllow/li` | 0.1% (2/2054) | 文本 | AllowCorpsesSlave / AllowCorpsesStranger |
| `building/defaultStorageSettings/filter/specialFiltersToDisallow` | 0.1% (2/2054) | 容器 |  |
| `building/defaultStorageSettings/filter/specialFiltersToDisallow/li` | 0.1% (2/2054) | 文本 | AllowCorpsesColonist / AllowCorpsesStranger |
| `building/defaultStorageSettings/priority` | 0.3% (7/2054) | 文本 | Critical / Important / Preferred |
| `building/destroyBrain` | 0.1% (1/2054) | 布尔 | true |
| `building/destroyEffecter` | 0.3% (7/2054) | 文本 | Broadshield_Burnout / FleshmassDestroyed / FleshmassHeartDestroyed |
| `building/destroyShakeAmount` | 0.3% (7/2054) | 数值 | 0 |
| `building/destroySound` | 3.1% (64/2054) | 文本 | BuildingDestroyed_Metal_Big / BuildingDestroyed_Metal_Small / BuildingDestroyed_Soft_Medium |
| `building/displayAttackToDestroyOnInspectPane` | 0.1% (3/2054) | 布尔 | true |
| `building/doorSupportGraphic` | 0.1% (2/2054) | 容器 |  |
| `building/doorSupportGraphic/color` | 0.1% (1/2054) | 文本 | (105,105,105) |
| `building/doorSupportGraphic/drawSize` | 0.1% (2/2054) | 文本 | (3,2.4) / (3.1, 2.3) |
| `building/doorSupportGraphic/graphicClass` | 0.1% (2/2054) | 文本 | Graphic_Multi |
| `building/doorSupportGraphic/texPath` | 0.1% (2/2054) | 文本 | Things/Building/OrnateDoor/OrnateDoor2x1_Support / Things/Building/SecurityDoor/SecurityDoor2x1_Support |
| `building/doorTopGraphic` | 0.2% (4/2054) | 容器 |  |
| `building/doorTopGraphic/color` | 0.1% (1/2054) | 文本 | (105,105,105) |
| `building/doorTopGraphic/drawSize` | 0.2% (4/2054) | 文本 | (1.5,1.5) / (2,2.2) / (3,2.4) |
| `building/doorTopGraphic/graphicClass` | 0.2% (4/2054) | 文本 | Graphic_Multi |
| `building/doorTopGraphic/texPath` | 0.2% (4/2054) | 文本 | Things/Building/Ancient/BlastDoor/AncientBlastDoor_Top / Things/Building/OrnateDoor/OrnateDoor2x1_Top / Things |
| `building/doorTopHorizontalOffset` | 0.1% (1/2054) | 文本 | (0,0,0.05) |
| `building/draftAttackNonDeconstructable` | 0.1% (2/2054) | 布尔 | false |
| `building/effectWatching` | 0.1% (3/2054) | 文本 | WatchingTelevision |
| `building/expandHomeArea` | 1.6% (32/2054) | 布尔 | false |
| `building/fixedStorageSettings` | 0.6% (12/2054) | 容器 |  |
| `building/fixedStorageSettings/filter` | 0.6% (12/2054) | 容器 |  |
| `building/fixedStorageSettings/filter/categories` | 0.5% (10/2054) | 容器 |  |
| `building/fixedStorageSettings/filter/categories/li` | 0.5% (11/2054) | 文本 | Books / Corpses / Foods |
| `building/fixedStorageSettings/filter/disallowedCategories` | 0.1% (3/2054) | 容器 |  |
| `building/fixedStorageSettings/filter/disallowedCategories/li` | 0.2% (5/2054) | 文本 | Buildings / Chunks / CorpsesDrone |
| `building/fixedStorageSettings/filter/disallowedThingDefs` | 0.1% (2/2054) | 容器 |  |
| `building/fixedStorageSettings/filter/disallowedThingDefs/li` | 0.1% (2/2054) | 文本 | Hay / Wastepack |
| `building/fixedStorageSettings/filter/disallowNotEverStorable` | 0.1% (2/2054) | 布尔 | true |
| `building/fixedStorageSettings/filter/specialFiltersToDisallow` | 0.3% (6/2054) | 容器 |  |
| `building/fixedStorageSettings/filter/specialFiltersToDisallow/li` | 0.3% (6/2054) | 文本 | AllowAdultOnlyApparel / AllowChildOnlyApparel / AllowLargeCorpses |
| `building/fixedStorageSettings/priority` | 0.1% (1/2054) | 文本 | Important |
| `building/forcedCostLeavings` | 0.1% (3/2054) | 容器 |  |
| `building/forcedCostLeavings/li` | 0.1% (2/2054) | 文本 | ShuttleEngine |
| `building/forceShowRoomStats` | 0.1% (2/2054) | 布尔 | true |
| `building/formingGraphicData` | 0.1% (2/2054) | 容器 |  |
| `building/formingGraphicData/drawSize` | 0.1% (2/2054) | 文本 | (1,1) / (1.65,1.65) |
| `building/formingGraphicData/graphicClass` | 0.1% (2/2054) | 文本 | Graphic_Single |
| `building/formingGraphicData/texPath` | 0.1% (2/2054) | 文本 | Things/Pawn/Mechanoid/HalfGestatedMechLarge / Things/Pawn/Mechanoid/HalfGestatedMechSmall |
| `building/formingMechBobSpeed` | 0.1% (1/2054) | 数值 | 0.0005 |
| `building/formingMechPerRotationOffset` | 0.1% (2/2054) | 容器 |  |
| `building/formingMechPerRotationOffset/li` | 0.4% (8/2054) | 文本 | (-0.15, 0, 0.225) / (0, 0, 0.225) / (0, 0, 0.45) |
| `building/formingMechYBobDistance` | 0.1% (1/2054) | 数值 | 0.08 |
| `building/fullGraveGraphicData` | 0.1% (2/2054) | 容器 |  |
| `building/fullGraveGraphicData/drawSize` | 0.1% (2/2054) | 文本 | (3,4) |
| `building/fullGraveGraphicData/graphicClass` | 0.1% (2/2054) | 文本 | Graphic_Multi |
| `building/fullGraveGraphicData/texPath` | 0.1% (2/2054) | 文本 | Things/Building/Misc/GraveFull / Things/Building/Misc/SarcophagusFull |
| `building/gestatorCycleCompleteMote` | 0.1% (2/2054) | 容器 |  |
| `building/gestatorCycleCompleteMote/east` | 0.1% (2/2054) | 文本 | MechGestatorCycleCompleteLarge_East / MechGestatorCycleComplete_East |
| `building/gestatorCycleCompleteMote/north` | 0.1% (2/2054) | 文本 | MechGestatorCycleCompleteLarge_North / MechGestatorCycleComplete_North |
| `building/gestatorCycleCompleteMote/south` | 0.1% (2/2054) | 文本 | MechGestatorCycleCompleteLarge_South / MechGestatorCycleComplete_South |
| `building/gestatorCycleCompleteMote/west` | 0.1% (2/2054) | 文本 | MechGestatorCycleCompleteLarge_West / MechGestatorCycleComplete_East |
| `building/gestatorFormedMote` | 0.1% (2/2054) | 容器 |  |
| `building/gestatorFormedMote/east` | 0.1% (2/2054) | 文本 | MechGestatorFormedLarge_East / MechGestatorFormed_East |
| `building/gestatorFormedMote/north` | 0.1% (2/2054) | 文本 | MechGestatorFormedLarge_North / MechGestatorFormed_North |
| `building/gestatorFormedMote/south` | 0.1% (2/2054) | 文本 | MechGestatorFormedLarge_South / MechGestatorFormed_South |
| `building/gestatorFormedMote/west` | 0.1% (2/2054) | 文本 | MechGestatorFormedLarge_West / MechGestatorFormed_East |
| `building/gestatorFormingMote` | 0.1% (2/2054) | 容器 |  |
| `building/gestatorFormingMote/east` | 0.1% (2/2054) | 文本 | MechGestatorFormingLarge_East / MechGestatorForming_East |
| `building/gestatorFormingMote/north` | 0.1% (2/2054) | 文本 | MechGestatorFormingLarge_North / MechGestatorForming_North |
| `building/gestatorFormingMote/south` | 0.1% (2/2054) | 文本 | MechGestatorFormingLarge_South / MechGestatorForming_South |
| `building/gestatorFormingMote/west` | 0.1% (2/2054) | 文本 | MechGestatorFormingLarge_West / MechGestatorForming_East |
| `building/gibbetCagePlaceCorpseEffecter` | 0.1% (1/2054) | 文本 | GibbetCage_PlaceCorpse |
| `building/gibbetCageTopGraphicData` | 0.1% (1/2054) | 容器 |  |
| `building/gibbetCageTopGraphicData/drawSize` | 0.1% (1/2054) | 文本 | (1.3,1.3) |
| `building/gibbetCageTopGraphicData/graphicClass` | 0.1% (1/2054) | 文本 | Graphic_Single |
| `building/gibbetCageTopGraphicData/shaderType` | 0.1% (1/2054) | 文本 | Cutout |
| `building/gibbetCageTopGraphicData/texPath` | 0.1% (1/2054) | 文本 | Things/Building/Misc/GibbetCageTop |
| `building/gibbetCorposeDrawOffset` | 0.1% (1/2054) | 文本 | (0, 0, 0.15) |
| `building/groundSpawnerCompleteEffecter` | 0.2% (4/2054) | 文本 | EmergencePointComplete2X2 / EmergencePointComplete3X3 / EmergencePointComplete8X8 |
| `building/groundSpawnerDestroyAdjacent` | 0.1% (3/2054) | 布尔 | true |
| `building/groundSpawnerLetterLabel` | 0.1% (2/2054) | 文本 | Fleshmass heart / Pit gate opened |
| `building/groundSpawnerLetterText` | 0.1% (2/2054) | 文本 | A fleshmass heart has emerged! This cancer-like creature will expand its living  / The shifting terrain has fa |
| `building/groundSpawnerSpawnDelay` | 0.1% (3/2054) | 数值/文本 | 2500~5000 / 5000~20000 / 600 |
| `building/groundSpawnerSustainedEffecter` | 0.2% (4/2054) | 文本 | EmergencePointSustained2X2 / EmergencePointSustained3X3 / EmergencePointSustained8X8 |
| `building/groundSpawnerSustainerSound` | 0.1% (3/2054) | 文本 | FleshmassHeart_Emerge / PitBurrowOpening / PitGateOpening |
| `building/groundSpawnerThingToSpawn` | 0.1% (3/2054) | 文本 | FleshmassHeart / PitBurrow / PitGate |
| `building/hasFuelingPort` | 0.1% (1/2054) | 布尔 | true |
| `building/haulToContainerDuration` | 0.3% (6/2054) | 数值 | 120 / 500 |
| `building/heatPerTickWhileWorking` | 0.2% (4/2054) | 数值 | 0.10 / 0.32 |
| `building/ignoreStoredThingsBeauty` | 0.1% (3/2054) | 布尔 | false / true |
| `building/instrumentRange` | 0.1% (3/2054) | 数值 | 12 / 16 / 20 |
| `building/isAirtight` | 0.6% (12/2054) | 布尔 | true |
| `building/isAttachment` | 0.2% (5/2054) | 布尔 | true |
| `building/isEdifice` | 1.2% (24/2054) | 布尔 | false / true |
| `building/isEscapableContainer` | 0.1% (2/2054) | 布尔 | true |
| `building/isFence` | 0.1% (3/2054) | 布尔 | true |
| `building/isHopper` | 0.1% (1/2054) | 布尔 | true |
| `building/isInert` | 3.0% (62/2054) | 布尔 | false / true |
| `building/isInsectCocoon` | 0.1% (1/2054) | 布尔 | true |
| `building/isMealSource` | 0.2% (4/2054) | 布尔 | true |
| `building/isNaturalRock` | 0.5% (11/2054) | 布尔 | false / true |
| `building/isPlaceOverableWall` | 0.1% (3/2054) | 布尔 | true |
| `building/isPlayerEjectable` | 0.1% (1/2054) | 布尔 | true |
| `building/isPowerConduit` | 0.1% (1/2054) | 布尔 | true |
| `building/isResourceRock` | 0.4% (8/2054) | 布尔 | true |
| `building/isSittable` | 0.3% (6/2054) | 布尔 | true |
| `building/isStuffableAirtight` | 0.1% (3/2054) | 布尔 | true |
| `building/isSupportDoor` | 0.2% (4/2054) | 布尔 | true |
| `building/isTargetable` | 1.5% (31/2054) | 布尔 | false / true |
| `building/isTrap` | 0.2% (4/2054) | 布尔 | true |
| `building/isWall` | 0.1% (1/2054) | 布尔 | true |
| `building/joyKind` | 0.5% (11/2054) | 文本 | Gaming_Cerebral / Gaming_Dexterity / Telescope |
| `building/leaveTerrain` | 0.1% (1/2054) | 文本 | Ice |
| `building/maxItemsInCell` | 0.1% (2/2054) | 数值 | 3 / 5 |
| `building/mechGestatorCylinderGraphic` | 0.1% (2/2054) | 容器 |  |
| `building/mechGestatorCylinderGraphic/drawSize` | 0.1% (2/2054) | 文本 | (5.6,4) / (6, 5) |
| `building/mechGestatorCylinderGraphic/graphicClass` | 0.1% (2/2054) | 文本 | Graphic_Multi |
| `building/mechGestatorCylinderGraphic/shaderType` | 0.1% (2/2054) | 文本 | Transparent |
| `building/mechGestatorCylinderGraphic/texPath` | 0.1% (2/2054) | 文本 | Things/Building/Production/MechGestatorLargeGlass / Things/Building/Production/MechGestatorStandardGlass |
| `building/mechGestatorTopGraphic` | 0.1% (2/2054) | 容器 |  |
| `building/mechGestatorTopGraphic/drawSize` | 0.1% (2/2054) | 文本 | (5.6,4) / (6, 5) |
| `building/mechGestatorTopGraphic/graphicClass` | 0.1% (2/2054) | 文本 | Graphic_Multi |
| `building/mechGestatorTopGraphic/texPath` | 0.1% (2/2054) | 文本 | Things/Building/Production/MechGestatorLargeTop / Things/Building/Production/MechGestatorStandardTop |
| `building/minDistanceToSameTypeOfBuilding` | 0.1% (1/2054) | 数值 | 7 |
| `building/mineableDropChance` | 0.3% (6/2054) | 数值 | 0.25 |
| `building/mineablePreventMeteorite` | 0.2% (5/2054) | 布尔 | true |
| `building/mineablePreventNaturalRockOnSurface` | 0.1% (1/2054) | 布尔 | true |
| `building/mineableScatterCommonality` | 0.3% (7/2054) | 数值 | 0.07 / 0.10 / 0.12 |
| `building/mineableScatterLumpSizeRange` | 0.4% (8/2054) | 文本 | 2~8 / 30~40 / 4~12 |
| `building/mineableThing` | 0.7% (14/2054) | 文本 | Gold / Silver / Steel |
| `building/mineableYield` | 0.4% (8/2054) | 数值 | 2 / 40 |
| `building/mineableYieldWasteable` | 0.1% (2/2054) | 布尔 | false |
| `building/minMechClusterPoints` | 0.2% (5/2054) | 数值 | 1000 / 570 / 660 |
| `building/multiSittable` | 0.1% (3/2054) | 布尔 | true |
| `building/naturalTerrain` | 0.1% (1/2054) | 文本 | Ice |
| `building/neverBuildable` | 0.4% (8/2054) | 布尔 | true |
| `building/nutritionCostPerDispense` | 0.1% (1/2054) | 数值 | 0.3 |
| `building/openingEffect` | 0.1% (3/2054) | 文本 | GrayBoxOpened / HermeticCrateOpened / SecurityCrateOpened |
| `building/openingStartedSound` | 0.1% (2/2054) | 文本 | Building_Deconstructed / CrateOpeningStarted |
| `building/paintable` | 3.6% (74/2054) | 布尔 | false / true |
| `building/playTargetAcquiredSound` | 0.1% (2/2054) | 布尔 | false |
| `building/poweredDoorOpenSpeedFactor` | 0.1% (1/2054) | 数值 | 4 |
| `building/preferConnectingToFences` | 0.1% (1/2054) | 布尔 | true |
| `building/preventDeteriorationInside` | 0.1% (2/2054) | 布尔 | true |
| `building/preventDeteriorationOnTop` | 0.1% (1/2054) | 布尔 | true |
| `building/quickTargetable` | 0.3% (7/2054) | 布尔 | true |
| `building/relatedBuildCommands` | 0.8% (16/2054) | 容器 |  |
| `building/relatedBuildCommands/li` | 1.6% (32/2054) | 文本 | DeathrestAccelerator / GlucosoidPump / HemogenAmplifier |
| `building/relatedTerrain` | 0.1% (2/2054) | 容器 |  |
| `building/relatedTerrain/li` | 0.1% (2/2054) | 文本 | Substructure |
| `building/repairable` | 1.5% (31/2054) | 布尔 | false |
| `building/requiredMechWeightClasses` | 0.1% (2/2054) | 容器 |  |
| `building/requiredMechWeightClasses/li` | 0.2% (4/2054) | 文本 | Heavy / Light / Medium |
| `building/roamerCanOpen` | 0.1% (1/2054) | 布尔 | true |
| `building/roofCollapseDamageMultiplier` | 0.2% (4/2054) | 数值 | 0.2 |
| `building/shipPart` | 0.3% (6/2054) | 布尔 | true |
| `building/sitIgnoreOrientation` | 0.1% (2/2054) | 布尔 | true |
| `building/smoothedThing` | 0.7% (14/2054) | 容器/文本 | SmoothedGranite / SmoothedLimestone / SmoothedSandstone |
| `building/soundDispense` | 0.1% (1/2054) | 文本 | DispensePaste |
| `building/soundDoorCloseEnd` | 0.1% (1/2054) | 文本 | SecurityDoor_EndClosing |
| `building/soundDoorCloseManual` | 0.1% (3/2054) | 文本 | Door_CloseManual / Door_FenceGateManual / SecurityDoor_BeginClosing |
| `building/soundDoorClosePowered` | 0.1% (2/2054) | 文本 | Door_ClosePowered / SecurityDoor_BeginClosing |
| `building/soundDoorOpenManual` | 0.1% (3/2054) | 文本 | Door_FenceGateManual / Door_OpenManual / SecurityDoor_Open |
| `building/soundDoorOpenPowered` | 0.1% (2/2054) | 文本 | Door_OpenPowered / SecurityDoor_Open |
| `building/soundMeleeHitOverride` | 0.1% (1/2054) | 文本 | ObeliskDamaged |
| `building/sowTag` | 0.7% (14/2054) | 文本 | Decorative / DecorativeTree / Hydroponic |
| `building/spawnedConceptLearnOpportunity` | 1.1% (23/2054) | 文本 | BillsTab / TVForSickPeople |
| `building/storageGroupTag` | 0.2% (5/2054) | 文本 | Bookcase / Hopper / OutfitStand |
| `building/subcoreScannerComplete` | 0.1% (2/2054) | 文本 | SubcoreRipscanner_Complete / SubcoreSoftscanner_Complete |
| `building/subcoreScannerFixedIngredients` | 0.1% (1/2054) | 容器 |  |
| `building/subcoreScannerFixedIngredients/li` | 0.1% (2/2054) | 容器 |  |
| `building/subcoreScannerFixedIngredients/li/count` | 0.1% (2/2054) | 数值 | 4 / 50 |
| `building/subcoreScannerFixedIngredients/li/filter` | 0.1% (2/2054) | 容器 |  |
| `building/subcoreScannerFixedIngredients/li/filter/thingDefs` | 0.1% (2/2054) | 容器 |  |
| `building/subcoreScannerFixedIngredients/li/filter/thingDefs/li` | 0.1% (2/2054) | 文本 | ComponentIndustrial / Steel |
| `building/subcoreScannerHediff` | 0.1% (1/2054) | 文本 | ScanningSickness |
| `building/subcoreScannerOutputDef` | 0.1% (2/2054) | 文本 | SubcoreHigh / SubcoreRegular |
| `building/subcoreScannerStartEffect` | 0.1% (2/2054) | 文本 | SubcoreRipscanner_Start / SubcoreSoftscanner_Start |
| `building/subcoreScannerWorking` | 0.1% (2/2054) | 文本 | SubcoreRipscanner_Working / SubcoreSoftscanner_Working |
| `building/supportsWallAttachments` | 0.2% (5/2054) | 布尔 | true |
| `building/trapDamageCategory` | 0.1% (1/2054) | 文本 | Sharp |
| `building/trapDestroyOnSpring` | 0.1% (3/2054) | 布尔 | true |
| `building/trapPeacefulWildAnimalsSpringChanceFactor` | 0.1% (1/2054) | 数值 | 0.25 |
| `building/turretBurstCooldownTime` | 0.6% (12/2054) | 数值 | 17.0 / 2.4 / 2.5 |
| `building/turretBurstWarmupTime` | 0.2% (5/2054) | 数值 | 0 / 0.5 / 4.0 |
| `building/turretGunDef` | 0.6% (12/2054) | 文本 | Gun_ChargeBlasterHeavyTurret / Gun_InfernoCannonTurret / Gun_MiniTurretMech |
| `building/turretInitialCooldownTime` | 0.1% (1/2054) | 数值 | 120 |
| `building/turretTopDrawSize` | 0.3% (6/2054) | 数值 | 1.2 / 1.75 / 1.8 |
| `building/turretTopLoadedGraphic` | 0.1% (1/2054) | 容器 |  |
| `building/turretTopLoadedGraphic/graphicClass` | 0.1% (1/2054) | 文本 | Graphic_Single |
| `building/turretTopLoadedGraphic/texPath` | 0.1% (1/2054) | 文本 | Things/Building/Security/TurretRocketFull_Top |
| `building/turretTopOffset` | 0.1% (3/2054) | 文本 | (0, 0.05) |
| `building/uninstallWork` | 0.3% (6/2054) | 数值 | 1250 / 1800 / 2500 |
| `building/unpoweredDoorCloseSpeedFactor` | 0.1% (1/2054) | 数值 | 2 |
| `building/unpoweredDoorOpenSpeedFactor` | 0.1% (2/2054) | 数值 | 1.2 / 2 |
| `building/unpoweredWorkTableWorkSpeedFactor` | 0.1% (1/2054) | 数值 | 0.5 |
| `building/upperMoverGraphic` | 0.1% (1/2054) | 容器 |  |
| `building/upperMoverGraphic/color` | 0.1% (1/2054) | 文本 | (105,105,105) |
| `building/upperMoverGraphic/graphicClass` | 0.1% (1/2054) | 文本 | Graphic_Single |
| `building/upperMoverGraphic/texPath` | 0.1% (1/2054) | 文本 | Things/Building/SecurityDoor/SecurityDoor2x1_Upper_Mover |
| `building/useIdeoColor` | 0.1% (2/2054) | 布尔 | true |
| `building/veinMineable` | 0.4% (8/2054) | 布尔 | true |
| `building/wakeDormantPawnsOnConstruction` | 0.5% (11/2054) | 布尔 | false |
| `building/wantsHopperAdjacent` | 0.1% (1/2054) | 布尔 | true |
| `building/wastepackAtomizerBottomGraphic` | 0.1% (1/2054) | 容器 |  |
| `building/wastepackAtomizerBottomGraphic/drawSize` | 0.1% (1/2054) | 文本 | (3,2) |
| `building/wastepackAtomizerBottomGraphic/graphicClass` | 0.1% (1/2054) | 文本 | Graphic_Multi |
| `building/wastepackAtomizerBottomGraphic/texPath` | 0.1% (1/2054) | 文本 | Things/Building/Misc/WastepackAtomizer_BottomLayer |
| `building/wastepackAtomizerOperationEffecter` | 0.1% (1/2054) | 文本 | WastepackAtomizer_Operating |
| `building/wastepackAtomizerWindowGraphic` | 0.1% (1/2054) | 容器 |  |
| `building/wastepackAtomizerWindowGraphic/drawSize` | 0.1% (1/2054) | 文本 | (3,2) |
| `building/wastepackAtomizerWindowGraphic/graphicClass` | 0.1% (1/2054) | 文本 | Graphic_Multi |
| `building/wastepackAtomizerWindowGraphic/texPath` | 0.1% (1/2054) | 文本 | Things/Building/Misc/WastepackAtomizerWindow |
| `building/watchBuildingInSameRoom` | 0.2% (5/2054) | 布尔 | true |
| `building/watchBuildingStandDistanceRange` | 0.2% (5/2054) | 文本 | 2~4 / 2~6 / 2~7 |
| `building/watchBuildingStandRectWidth` | 0.2% (5/2054) | 数值 | 3 / 5 / 6 |
| `building/workTableNotInRoomRoleFactor` | 0.9% (19/2054) | 数值 | 0.8 |
| `building/workTableRoomRole` | 1.3% (27/2054) | 容器/文本 | Kitchen / Laboratory / Workshop |
| `burnableByRecipe` | 1.5% (31/2054) | 布尔 | false / true |
| `butcherProducts` | 0.8% (16/2054) | 容器 |  |
| `butcherProducts/BlocksGranite` | 0.1% (1/2054) | 数值 | 20 |
| `butcherProducts/BlocksLimestone` | 0.1% (1/2054) | 数值 | 20 |
| `butcherProducts/BlocksMarble` | 0.1% (1/2054) | 数值 | 20 |
| `butcherProducts/BlocksSandstone` | 0.1% (1/2054) | 数值 | 20 |
| `butcherProducts/BlocksSlate` | 0.1% (1/2054) | 数值 | 20 |
| `butcherProducts/BlocksVacstone` | 0.1% (1/2054) | 数值 | 20 |
| `butcherProducts/InsectJelly` | 0.1% (1/2054) | 数值 | 150 |
| `butcherProducts/Plasteel` | 0.2% (4/2054) | 数值 | 10 / 20 |
| `butcherProducts/Steel` | 0.4% (9/2054) | 数值 | 10 / 20 / 30 |
| `canBeUsedUnderRoof` | 0.4% (9/2054) | 布尔 | false |
| `canDeteriorateUnspawned` | 0.1% (1/2054) | 布尔 | true |
| `canEditAnyStyle` | 0.1% (1/2054) | 布尔 | true |
| `canGenerateDefaultDesignator` | 0.4% (9/2054) | 布尔 | false |
| `canInteractThroughCorners` | 0.1% (1/2054) | 布尔 | true |
| `canLoadIntoCaravan` | 0.1% (1/2054) | 布尔 | false |
| `canOverlapZones` | 5.7% (116/2054) | 布尔 | false / true |
| `canScatterOver` | 0.2% (5/2054) | 布尔 | false |
| `castEdgeShadows` | 4.8% (99/2054) | 布尔 | True / false / true |
| `category` | 3.6% (74/2054) | 文本 | Building / Item / Mote |
| `clearBuildingArea` | 0.1% (3/2054) | 布尔 | false |
| `colorGenerator` | 3.0% (62/2054) | 容器 |  |
| `colorGenerator/options` | 1.6% (33/2054) | 容器 |  |
| `colorGenerator/options/li` | 5.7% (117/2054) | 容器 |  |
| `colorGenerator/options/li/max` | 1.3% (26/2054) | 文本 | (0.5,0.5,0.5) / (0.5,0.5,0.5,1) / (1,1,1) |
| `colorGenerator/options/li/min` | 1.3% (26/2054) | 文本 | (0.3,0.3,0.3) / (0.3,0.3,0.3,1) / (0.5,0.5,0.5) |
| `colorGenerator/options/li/only` | 4.4% (91/2054) | 文本 | (0.33,0.33,0.33) / (0.4,0.3,0.15) / (0.65,0.65,0.65) |
| `colorGenerator/options/li/weight` | 4.9% (100/2054) | 数值 | 10 / 15 / 20 |
| `colorGeneratorInTraderStock` | 0.1% (1/2054) | 容器 |  |
| `colorGeneratorInTraderStock/options` | 0.1% (1/2054) | 容器 |  |
| `colorGeneratorInTraderStock/options/li` | 0.1% (3/2054) | 容器 |  |
| `colorGeneratorInTraderStock/options/li/max` | 0.1% (1/2054) | 文本 | (0.9,0.9,0.9,1) |
| `colorGeneratorInTraderStock/options/li/min` | 0.1% (1/2054) | 文本 | (0.3,0.3,0.3,1) |
| `colorGeneratorInTraderStock/options/li/only` | 0.1% (2/2054) | 文本 | (0.33,0.33,0.33,1) / (0.9,0.9,0.9,1) |
| `colorGeneratorInTraderStock/options/li/weight` | 0.1% (3/2054) | 数值 | 10 / 5 |
| `colorPerStuff` | 0.1% (2/2054) | 容器 |  |
| `colorPerStuff/li` | 0.1% (2/2054) | 容器 |  |
| `colorPerStuff/li/color` | 0.1% (2/2054) | 文本 | (139,122,87) / (255,255,255) |
| `colorPerStuff/li/stuff` | 0.1% (2/2054) | 文本 | Cloth / WoodLog |
| `comps` | 33.3% (684/2054) | 容器 |  |
| `comps/li` | 76.1% (1564/2054) | 容器 |  |
| `comps/li/abilityDef` | 0.2% (5/2054) | 文本 | EggSpew / HellcatBurner / IncineratorBurner |
| `comps/li/activated` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/activateDescString` | 1.0% (21/2054) | 文本 | Choose someone to decipher this floor etching. / Choose someone to force this door open. / Permanently and saf |
| `comps/li/activatedMessageKey` | 0.1% (1/2054) | 文本 | MessageMechanoidsReinforcementsDrop |
| `comps/li/activateLabelString` | 1.0% (21/2054) | 文本 | Deactivate... / Decipher... / Force open... |
| `comps/li/activateMessageKey` | 0.1% (2/2054) | 文本 | MessageCocoonDisturbed / MessageFingerspikeDisturbed |
| `comps/li/activatePluralMessageKey` | 0.1% (2/2054) | 文本 | MessageCocoonDisturbedPlural / MessageFingerspikeDisturbedPlural |
| `comps/li/activateTexPath` | 1.3% (26/2054) | 文本 | UI/Commands/DecipherEtchings / UI/Commands/DisableObelisk / UI/Commands/ForceOpenDoor |
| `comps/li/activatingString` | 0.6% (13/2054) | 文本 | Deciphering floor etching: {1}s / Inducing tachycardiac death: {1}s / deactivating obelisk: {1}s |
| `comps/li/activatingStringPending` | 0.7% (14/2054) | 文本 | Deciphering floor etching / Inducing tachycardiac death / deactivating obelisk |
| `comps/li/activeDuration` | 0.1% (1/2054) | 数值 | 6000 |
| `comps/li/activeInspectString` | 0.1% (1/2054) | 文本 | Hack or destroy relay stabilizers to obtain gravcore. |
| `comps/li/activeInspectStringKey` | 0.1% (3/2054) | 文本 | AncientHeatVentActive / AncientSmokeVentActive / AncientToxVentActive |
| `comps/li/activeSound` | 0.5% (11/2054) | 文本 | AncientVent_Ambient / Broadshield_Ambience / BulletShield_Ambience |
| `comps/li/activeTicks` | 0.5% (11/2054) | 数值 | 1 / 60 |
| `comps/li/activityMeatPerDayCurve` | 0.1% (1/2054) | 容器 |  |
| `comps/li/activityMeatPerDayCurve/points` | 0.1% (1/2054) | 容器 |  |
| `comps/li/activityMeatPerDayCurve/points/li` | 0.1% (2/2054) | 文本 | 0.1, 20 / 0.9, 120 |
| `comps/li/activityOnRoofCollapsed` | 0.1% (2/2054) | 数值 | 0.4 |
| `comps/li/activityResearchFactorCurve` | 0.1% (3/2054) | 容器 |  |
| `comps/li/activityResearchFactorCurve/points` | 0.1% (3/2054) | 容器 |  |
| `comps/li/activityResearchFactorCurve/points/li` | 0.4% (9/2054) | 文本 | 0, 0.5 / 0.5, 1 / 0.99, 2 |
| `comps/li/adaptableDamageDefs` | 0.2% (5/2054) | 容器 |  |
| `comps/li/adaptableDamageDefs/li` | 0.2% (5/2054) | 文本 | EMP |
| `comps/li/addictiveness` | 0.5% (10/2054) | 数值 | 0.010 / 0.026 / 0.05 |
| `comps/li/addsHediff` | 0.1% (1/2054) | 文本 | ResurrectionComa |
| `comps/li/affectedDamageDefs` | 1.1% (23/2054) | 容器 |  |
| `comps/li/affectedDamageDefs/li` | 1.8% (36/2054) | 文本 | EMP / Stun |
| `comps/li/affectLabel` | 0.1% (1/2054) | 布尔 | false |
| `comps/li/ageYearsRange` | 0.2% (5/2054) | 文本 | 0~100 / 100~200 / 500~2000 |
| `comps/li/airPerSecondPerHundredCells` | 0.1% (2/2054) | 数值 | 0.005 / 0.01 |
| `comps/li/allowedMutants` | 0.1% (1/2054) | 容器 |  |
| `comps/li/allowedMutants/li` | 0.1% (1/2054) | 文本 | Ghoul |
| `comps/li/allowMechs` | 0.1% (1/2054) | 布尔 | false |
| `comps/li/allowNonPlayer` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/allowRepeatAnalysis` | 0.1% (3/2054) | 布尔 | true |
| `comps/li/allowRepeatedUse` | 0.2% (4/2054) | 布尔 | true |
| `comps/li/alwaysDisplayAsUsingPower` | 0.1% (2/2054) | 布尔 | true |
| `comps/li/alwaysDrawParent` | 0.2% (4/2054) | 布尔 | true |
| `comps/li/alwaysShowHitpointsGizmo` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/ammoCountPerCharge` | 0.4% (8/2054) | 数值 | 10 / 20 / 25 |
| `comps/li/ammoCountToRefill` | 0.1% (3/2054) | 数值 | 10 / 30 / 35 |
| `comps/li/ammoDef` | 0.5% (11/2054) | 文本 | Bioferrite / Chemfuel / Steel |
| `comps/li/analysisDurationHours` | 0.3% (6/2054) | 数值 | 0.375 / 0.5 / 0.75 |
| `comps/li/analysisID` | 0.1% (3/2054) | 数值 | 123417683 / 652343245 / 92349061 |
| `comps/li/analysisRequiredRange` | 0.1% (3/2054) | 数值/文本 | 2~3 / 3 |
| `comps/li/angleOffset` | 0.1% (3/2054) | 数值 | -90 |
| `comps/li/anomalyKnowledge` | 0.9% (18/2054) | 数值 | 1 / 2 / 2.5 |
| `comps/li/applyDamageToExplosionCellsNeighbors` | 0.2% (5/2054) | 布尔 | false / true |
| `comps/li/attachSpawnedEffecter` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/attachSpawnedMechEffecter` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/attacks` | 0.1% (1/2054) | 容器 |  |
| `comps/li/attacks/li` | 0.1% (3/2054) | 容器 |  |
| `comps/li/attacks/li/ability` | 0.1% (3/2054) | 文本 | AgonyPulse / FleshmelterBolt / Heatspikes |
| `comps/li/autoAttack` | 0.1% (1/2054) | 布尔 | false |
| `comps/li/autohackWarningString` | 0.1% (1/2054) | 文本 | Hacking this {0} will alert enemies and cause them to attack. |
| `comps/li/autoRefuelPercent` | 0.5% (11/2054) | 数值 | 0 / 0.05 / 0.5 |
| `comps/li/awakeStateLabelKey` | 0.1% (2/2054) | 文本 | DormantCompExpired / OpenedDaysAgo |
| `comps/li/baseChainFastenerTexPath` | 0.1% (2/2054) | 文本 | Things/Building/HoldingPlatform/HoldingPlatform_ChainFastener |
| `comps/li/baseEscapeIntervalMtbDays` | 0.5% (11/2054) | 数值 | -1 / 45 / 50 |
| `comps/li/basePowerConsumption` | 4.4% (91/2054) | 数值 | 1500 / 50 / 70 |
| `comps/li/baseReloadTicks` | 0.5% (11/2054) | 数值 | 60 |
| `comps/li/becomingUnstableInspectText` | 0.1% (1/2054) | 文本 | Becoming unstable |
| `comps/li/biocodeOnEquip` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/bioferriteDensity` | 0.6% (13/2054) | 数值 | 1.5 / 2 / 3 |
| `comps/li/biotunedCycleSpeedFactor` | 0.1% (1/2054) | 数值 | 1.25 |
| `comps/li/blocksRangedWeapons` | 0.1% (1/2054) | 布尔 | false |
| `comps/li/bodyPart` | 0.4% (9/2054) | 文本 | Brain |
| `comps/li/bodyPartsToRestore` | 0.1% (1/2054) | 容器 |  |
| `comps/li/bodyPartsToRestore/li` | 0.3% (6/2054) | 文本 | Ear / Eye / Finger |
| `comps/li/bodySizeDigestTimeCurve` | 0.1% (1/2054) | 容器 |  |
| `comps/li/bodySizeDigestTimeCurve/points` | 0.1% (1/2054) | 容器 |  |
| `comps/li/bodySizeDigestTimeCurve/points/li` | 0.1% (3/2054) | 文本 | (0.2, 10) / (1, 30) / (3.5, 60) |
| `comps/li/bossgroupDef` | 0.1% (3/2054) | 文本 | Apocriton / Diabolus / Warqueen |
| `comps/li/brainDamageChance` | 0.2% (4/2054) | 数值 | 0.3 |
| `comps/li/burstCount` | 0.1% (2/2054) | 数值 | 2 / 35 |
| `comps/li/canBeActivityDeactivated` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/canBeEnjoyedAsArt` | 0.2% (4/2054) | 布尔 | true |
| `comps/li/canBeExecuted` | 0.1% (1/2054) | 布尔 | false |
| `comps/li/canChangeAssignedThingsAfterStarting` | 0.2% (5/2054) | 布尔 | true |
| `comps/li/canEjectFuel` | 0.5% (11/2054) | 布尔 | true |
| `comps/li/cannotHaveHediff` | 0.1% (1/2054) | 文本 | SentienceCatalyst |
| `comps/li/canSpawnOverPlayerSownPlants` | 0.1% (1/2054) | 布尔 | false |
| `comps/li/canStudyInPlace` | 0.1% (3/2054) | 布尔 | true |
| `comps/li/canTargetSelf` | 0.1% (1/2054) | 布尔 | false |
| `comps/li/canUpgrade` | 0.3% (7/2054) | 布尔 | true |
| `comps/li/canWakeUpFogged` | 0.1% (1/2054) | 布尔 | false |
| `comps/li/capturedLetterLabel` | 0.1% (1/2054) | 文本 | Revenant reformed |
| `comps/li/capturedLetterText` | 0.1% (1/2054) | 文本 | After {PAWN_nameDef} chained the revenant spine to a holding platform, the reven |
| `comps/li/cascadeThingDefs` | 0.1% (1/2054) | 容器 |  |
| `comps/li/cascadeThingDefs/li` | 0.1% (2/2054) | 文本 | Fleshmass / Fleshmass_Active |
| `comps/li/cellsToFill` | 0.1% (3/2054) | 数值 | 20 / 45 |
| `comps/li/cellsToPollute` | 0.1% (1/2054) | 数值 | 6 |
| `comps/li/cellsToPollutePerDay` | 0.1% (1/2054) | 数值 | 6 |
| `comps/li/cellsToPollutePerDissolution` | 0.1% (1/2054) | 数值 | 6 |
| `comps/li/chanceNeverExplodeFromDamage` | 0.6% (13/2054) | 数值 | 0.5 / 0.8 / 1 |
| `comps/li/chanceOverDistance` | 0.2% (4/2054) | 容器 |  |
| `comps/li/chanceOverDistance/points` | 0.2% (4/2054) | 容器 |  |
| `comps/li/chanceOverDistance/points/li` | 0.9% (19/2054) | 文本 | (0,  0) / (16,  0) / (16.01,  0.01) |
| `comps/li/chanceToStartFire` | 0.1% (3/2054) | 数值 | 0.22 / 1 |
| `comps/li/changePerDamage` | 0.1% (2/2054) | 数值 | 0 / 0.001 |
| `comps/li/changePerDayBase` | 0.1% (1/2054) | 数值 | 0.2 |
| `comps/li/changePerDayOutside` | 0.1% (2/2054) | 数值 | 0.05 |
| `comps/li/chargedSoundDef` | 0.1% (1/2054) | 文本 | NeuralSupercharger_Ready |
| `comps/li/chargeDurationTicks` | 0.2% (5/2054) | 数值 | 10000 / 1800 / 5400 |
| `comps/li/chargeIntervalTicks` | 0.1% (2/2054) | 数值 | 600000 |
| `comps/li/chargeNoun` | 1.0% (21/2054) | 文本 | burner charge / charge / flare |
| `comps/li/checkInterval` | 0.1% (3/2054) | 数值 | 60 |
| `comps/li/checkRoomVacuum` | 0.1% (1/2054) | 布尔 | false |
| `comps/li/chemical` | 0.5% (11/2054) | 文本 | Alcohol / Ambrosia / GoJuice |
| `comps/li/chooseSingleTypeToSpawn` | 0.1% (1/2054) | 布尔 | True |
| `comps/li/cloudFleck` | 0.1% (1/2054) | 文本 | AutobongSmoke |
| `comps/li/cloudRadius` | 0.1% (1/2054) | 数值 | 4.9 |
| `comps/li/color` | 0.6% (12/2054) | 文本 | (0.36, 0.21, 0.13, 1) / (0.4, 0.4, 0.4) / (0.5, 0.5, 0.5, 1) |
| `comps/li/colorA` | 0.3% (7/2054) | 文本 | (0,235,31,255) / (0.2,0.2,0.2,1) / (214,46,31,255) |
| `comps/li/colorB` | 0.3% (7/2054) | 文本 | (0,235,31,255) / (0.4,0.4,0.4,1) / (214,46,31,255) |
| `comps/li/colorPickerEnabled` | 0.1% (3/2054) | 布尔 | true |
| `comps/li/colors` | 0.1% (1/2054) | 容器 |  |
| `comps/li/colors/li` | 0.2% (4/2054) | 文本 | (0.9, 0.75, 0.5) / (0.9, 0.85, 0.7) / (1, 0.75, 0.6) |
| `comps/li/commandDescKey` | 0.1% (1/2054) | 文本 | CommandDesignateOpenCloseVentDesc |
| `comps/li/commandLabelKey` | 0.1% (1/2054) | 文本 | CommandDesignateOpenCloseVentLabel |
| `comps/li/commandTexture` | 0.1% (1/2054) | 文本 | UI/Commands/Vent |
| `comps/li/compClass` | 13.8% (284/2054) | 文本 | CompDestroyHeart / CompFleshmassHeart / CompFleshmassSpitter |
| `comps/li/completeDigestionDamage` | 0.1% (1/2054) | 数值 | 200 |
| `comps/li/completedLetter` | 0.3% (6/2054) | 文本 | By studying the signal chip, {PAWN_labelShort} has acquired the insight needed f / While analyzing the fleshma |
| `comps/li/completedLetterDef` | 0.3% (6/2054) | 文本 | NeutralEvent / PositiveEvent / ThreatSmall |
| `comps/li/completedLetterLabel` | 0.3% (6/2054) | 文本 | Analysis complete / Analysis progress / Powerfocus chip studied: {RESEARCH} unlocked |
| `comps/li/completedQuest` | 0.1% (1/2054) | 文本 | AncientSignalActivation |
| `comps/li/componentTypeDef` | 0.2% (5/2054) | 文本 | Controls / FuelStorage / SignalJammer |
| `comps/li/conditionDef` | 0.5% (11/2054) | 文本 | DeepFreeze / PsychicDroner / SunBlocker |
| `comps/li/conditionsToPossiblyCure` | 0.1% (2/2054) | 容器 |  |
| `comps/li/conditionsToPossiblyCure/li` | 0.7% (14/2054) | 文本 | Asthma / BadBack / Blindness |
| `comps/li/conditionToCause` | 0.1% (3/2054) | 文本 | DarkenedSkies / HeatVentHeat / ToxicFallout |
| `comps/li/connectionLossDailyPerBuildingDistanceCurve` | 0.1% (1/2054) | 容器 |  |
| `comps/li/connectionLossDailyPerBuildingDistanceCurve/points` | 0.1% (1/2054) | 容器 |  |
| `comps/li/connectionLossDailyPerBuildingDistanceCurve/points/li` | 0.1% (2/2054) | 文本 | (0,0.07) / (7.9,0.01) |
| `comps/li/connectionLossPerLevelCurve` | 0.1% (1/2054) | 容器 |  |
| `comps/li/connectionLossPerLevelCurve/points` | 0.1% (1/2054) | 容器 |  |
| `comps/li/connectionLossPerLevelCurve/points/li` | 0.2% (4/2054) | 文本 | (0, 0) / (0.001, 0.02) / (0.33, 0.04) |
| `comps/li/connectionStrengthGainPerHourPruningBase` | 0.1% (1/2054) | 数值 | 0.01 |
| `comps/li/connectionStrengthGainPerPlantSkill` | 0.1% (1/2054) | 容器 |  |
| `comps/li/connectionStrengthGainPerPlantSkill/points` | 0.1% (1/2054) | 容器 |  |
| `comps/li/connectionStrengthGainPerPlantSkill/points/li` | 0.1% (3/2054) | 文本 | (0, 0.8) / (20, 1.2) / (8, 1) |
| `comps/li/connectionStrengthLossPerDryadDeath` | 0.1% (1/2054) | 数值 | 0.1 |
| `comps/li/consumeFuelOnlyWhenPowered` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/consumeFuelOnlyWhenUsed` | 0.6% (12/2054) | 布尔 | true |
| `comps/li/containedThingOffset` | 0.1% (1/2054) | 文本 | (0,0,1) |
| `comps/li/containmentFactor` | 0.1% (1/2054) | 数值 | 0.7 |
| `comps/li/contents` | 0.7% (14/2054) | 文本 | Reward_AncientBox_ComponentIndustrial / Reward_AncientBox_ComponentSpacer / Reward_Pallet_Medicine |
| `comps/li/contentsDrawOffset` | 0.1% (1/2054) | 文本 | (0.05, 0, 0.2) |
| `comps/li/convertTerrainDef` | 0.1% (1/2054) | 文本 | SoilRich |
| `comps/li/cooldownEndedMessage` | 0.1% (1/2054) | 文本 | {0} is ready to launch again. |
| `comps/li/cooldownFleck` | 0.1% (2/2054) | 文本 | FlashRed |
| `comps/li/cooldownFleckScale` | 0.1% (2/2054) | 数值 | 0.7 |
| `comps/li/cooldownFleckSpawnIntervalTicks` | 0.1% (2/2054) | 数值 | 60 |
| `comps/li/cooldownPreventsRefuel` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/cooldownTicks` | 0.3% (7/2054) | 数值 | 120000 / 1800000 / 300000 |
| `comps/li/costPerPawn` | 0.1% (1/2054) | 数值 | 25 |
| `comps/li/countdownCurveTicks` | 0.1% (1/2054) | 容器 |  |
| `comps/li/countdownCurveTicks/points` | 0.1% (1/2054) | 容器 |  |
| `comps/li/countdownCurveTicks/points/li` | 0.2% (4/2054) | 文本 | (1200000, 0) / (599, 0) / (600, 1) |
| `comps/li/countdownLabel` | 0.1% (1/2054) | 文本 | Burnout in |
| `comps/li/countsTowardsBuildingLimit` | 0.1% (1/2054) | 布尔 | false |
| `comps/li/crashedLetterLabel` | 0.1% (1/2054) | 文本 | Relay crash |
| `comps/li/crashedLetterText` | 0.1% (1/2054) | 文本 | The mechanoid relay has crashed to the ground. Destroy it to obtain a gravcore.\ |
| `comps/li/crashedThingDef` | 0.1% (1/2054) | 文本 | MechRelay_Crashed |
| `comps/li/cycleCountOnSpawn` | 0.1% (3/2054) | 数值 | 4 |
| `comps/li/damage` | 0.1% (1/2054) | 数值 | 1 |
| `comps/li/damagedActivityMultiplierCurve` | 0.1% (1/2054) | 容器 |  |
| `comps/li/damagedActivityMultiplierCurve/points` | 0.1% (1/2054) | 容器 |  |
| `comps/li/damagedActivityMultiplierCurve/points/li` | 0.2% (4/2054) | 文本 | 0.25, 100 / 0.5, 10 / 0.75, 2 |
| `comps/li/damageDef` | 0.1% (1/2054) | 文本 | Deterioration |
| `comps/li/damageFactor` | 0.1% (1/2054) | 数值 | 6 |
| `comps/li/damageFalloff` | 0.1% (3/2054) | 布尔 | false / true |
| `comps/li/damagePerCycle` | 0.1% (3/2054) | 数值 | 10 |
| `comps/li/damagePerTickRare` | 0.1% (1/2054) | 数值 | 10 |
| `comps/li/darklightToggle` | 0.1% (3/2054) | 布尔 | true |
| `comps/li/daysToComplete` | 0.1% (3/2054) | 数值 | 3 / 4 / 5 |
| `comps/li/daysToRadius` | 0.1% (1/2054) | 数值 | 60 |
| `comps/li/daysToRotStart` | 1.1% (23/2054) | 数值 | 14 / 2 / 5 |
| `comps/li/deathrestEffectivenessFactor` | 0.1% (2/2054) | 数值 | 1.1 / 1.2 |
| `comps/li/defaultStudyAmount` | 0.1% (1/2054) | 数值 | 2 |
| `comps/li/defence` | 0.6% (12/2054) | 数值 | 180 / 200 / 45000 |
| `comps/li/delayedWakeUpDoesZs` | 0.1% (1/2054) | 布尔 | false |
| `comps/li/delayTicks` | 0.6% (12/2054) | 数值 | 120 / 14400 / 30000 |
| `comps/li/delayUntilFeralCheck` | 0.1% (1/2054) | 数值 | 60000 |
| `comps/li/departingMessage` | 0.1% (1/2054) | 文本 | The nociosphere is departing. |
| `comps/li/description` | 0.2% (4/2054) | 文本 | Heal all fresh wounds, blood loss, and one random infectious disease. / Heal all fresh wounds, heal one random |
| `comps/li/descriptionMaker` | 1.5% (31/2054) | 文本 | ArtDescription_CubeSculpture / ArtDescription_VoidSculpture / ArtDescription_WeaponGun |
| `comps/li/destabilizationInspectString` | 0.1% (1/2054) | 文本 | Destabilizing |
| `comps/li/destabilizationMessage` | 0.1% (1/2054) | 文本 | The mechanoid relay has begun to destabilize. |
| `comps/li/destroyAfterSpawn` | 0.2% (4/2054) | 布尔 | true |
| `comps/li/destroyedLetterDef` | 0.1% (1/2054) | 文本 | PositiveEvent |
| `comps/li/destroyedLetterLabel` | 0.1% (1/2054) | 文本 | Gravcore obtained |
| `comps/li/destroyedLetterText` | 0.1% (1/2054) | 文本 | You've obtained a gravcore from the ancient reactor.\n\nThe reactor is shutting  |
| `comps/li/destroyedOnAnalyzed` | 0.3% (6/2054) | 布尔 | false / true |
| `comps/li/destroyMode` | 0.1% (1/2054) | 文本 | KillFinalize |
| `comps/li/destroyOnEmpty` | 0.6% (13/2054) | 布尔 | true |
| `comps/li/destroyThingOnExplosionSize` | 0.2% (4/2054) | 数值 | 2 / 9999 |
| `comps/li/destroyWarningEffecterDef` | 0.1% (1/2054) | 文本 | DisruptorDestroyWarning |
| `comps/li/digestingInspector` | 0.1% (1/2054) | 文本 | Digesting {PAWN_nameDef}: {SECONDS} seconds left |
| `comps/li/directionChangeInterval` | 0.1% (1/2054) | 文本 | 150~500 |
| `comps/li/directionInfluence` | 0.1% (2/2054) | 数值 | 20 / 30 |
| `comps/li/dirtyGraphicsOnActivityChange` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/disabledByArtificialBuildings` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/disabledOnUnpowered` | 0.1% (3/2054) | 布尔 | true |
| `comps/li/disableIfHatcher` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/disableOnHacked` | 0.1% (3/2054) | 布尔 | true |
| `comps/li/disarmedByEmpForTicks` | 0.3% (7/2054) | 数值 | 1080 / 1500 / 3200 |
| `comps/li/displayCountdownOnLabel` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/displayGizmoWhileUndrafted` | 1.0% (21/2054) | 布尔 | false / true |
| `comps/li/displayPriorityInCategory` | 0.1% (1/2054) | 数值 | 300 |
| `comps/li/displayTimeActive` | 0.1% (2/2054) | 布尔 | false |
| `comps/li/dissolutinFactorIndoors` | 0.1% (1/2054) | 数值 | 0.5 |
| `comps/li/dissolutionAfterDays` | 0.1% (1/2054) | 数值 | 8 |
| `comps/li/dissolutionFactorRain` | 0.1% (1/2054) | 数值 | 2 |
| `comps/li/doCameraShake` | 0.2% (4/2054) | 布尔 | true |
| `comps/li/doers` | 0.2% (5/2054) | 容器 |  |
| `comps/li/doers/li` | 0.4% (9/2054) | 容器 |  |
| `comps/li/doers/li/chancePerHourRange` | 0.1% (1/2054) | 文本 | 0.01~0.05 |
| `comps/li/doers/li/exclude` | 0.1% (1/2054) | 容器 |  |
| `comps/li/doers/li/exclude/AdvancedGravtech` | 0.1% (1/2054) | 容器 |  |
| `comps/li/doers/li/exclude/BasicGravtech` | 0.1% (1/2054) | 容器 |  |
| `comps/li/doers/li/exclude/BasicMechtech` | 0.1% (1/2054) | 容器 |  |
| `comps/li/doers/li/exclude/HighMechtech` | 0.1% (1/2054) | 容器 |  |
| `comps/li/doers/li/exclude/StandardGravtech` | 0.1% (1/2054) | 容器 |  |
| `comps/li/doers/li/exclude/StandardMechtech` | 0.1% (1/2054) | 容器 |  |
| `comps/li/doers/li/exclude/UltraMechtech` | 0.1% (1/2054) | 容器 |  |
| `comps/li/doers/li/ignoreZeroBaseCost` | 0.1% (1/2054) | 布尔 | false |
| `comps/li/doers/li/questChance` | 0.2% (4/2054) | 数值 | 0.01 / 0.05 / 0.15 |
| `comps/li/doers/li/tabs` | 0.1% (2/2054) | 容器 |  |
| `comps/li/doers/li/tabs/Anomaly` | 0.1% (1/2054) | 容器 |  |
| `comps/li/doers/li/tabs/Main` | 0.1% (1/2054) | 容器 |  |
| `comps/li/doers/li/usesHiddenProjects` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/dontShowDevGizmos` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/dontWipePlant` | 0.1% (2/2054) | 文本 | Plant_GrassAnima / Plant_TreeAnima |
| `comps/li/dormantGraphic` | 0.1% (1/2054) | 容器 |  |
| `comps/li/dormantGraphic/addTopAltitudeBias` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/dormantGraphic/drawSize` | 0.1% (1/2054) | 文本 | (4,4) |
| `comps/li/dormantGraphic/graphicClass` | 0.1% (1/2054) | 文本 | Graphic_Multi |
| `comps/li/dormantGraphic/shadowData` | 0.1% (1/2054) | 容器 |  |
| `comps/li/dormantGraphic/shadowData/volume` | 0.1% (1/2054) | 文本 | (1.8, 2, 1.8) |
| `comps/li/dormantGraphic/texPath` | 0.1% (1/2054) | 文本 | Things/Building/Mech/AncientMechGestatorIntact_Full/AncientMechGestatorIntact_Fu |
| `comps/li/dormantStateLabelKey` | 0.1% (3/2054) | 文本 | DormantCompBeacon / DormantCompSealed / MetalhorrorDormant |
| `comps/li/doVisualEffects` | 0.1% (1/2054) | 布尔 | false |
| `comps/li/drawAssignmentOverlay` | 0.5% (10/2054) | 布尔 | false / true |
| `comps/li/drawContainedThing` | 0.1% (3/2054) | 布尔 | false |
| `comps/li/drawContents` | 0.1% (2/2054) | 布尔 | true |
| `comps/li/drawFuelGaugeInMap` | 0.1% (3/2054) | 布尔 | false / true |
| `comps/li/drawLines` | 0.1% (1/2054) | 布尔 | false |
| `comps/li/drawMote` | 0.1% (2/2054) | 布尔 | true |
| `comps/li/drawOutOfFuelOverlay` | 0.2% (4/2054) | 布尔 | false |
| `comps/li/drawStackLabel` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/drawUnownedAssignmentOverlay` | 0.1% (1/2054) | 布尔 | false |
| `comps/li/drawWick` | 0.1% (1/2054) | 布尔 | false |
| `comps/li/drawWithNoSelection` | 0.1% (3/2054) | 布尔 | True |
| `comps/li/droneLevel` | 0.1% (1/2054) | 数值 | 2 |
| `comps/li/droneLevelIncreaseInterval` | 0.1% (1/2054) | 数值 | 150000 |
| `comps/li/dropEffecterDef` | 0.1% (2/2054) | 文本 | MechChargerWasteRemoved |
| `comps/li/dropInPods` | 0.1% (1/2054) | 布尔 | True |
| `comps/li/dropOnDestroyed` | 0.1% (1/2054) | 容器 |  |
| `comps/li/dropOnDestroyed/Gravcore` | 0.1% (1/2054) | 容器 |  |
| `comps/li/dropOnHacked` | 0.1% (1/2054) | 容器 |  |
| `comps/li/dropOnHacked/Gravcore` | 0.1% (1/2054) | 容器 |  |
| `comps/li/drugExposure` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/durationDays` | 0.2% (4/2054) | 数值 | 25 / 4 / 6 |
| `comps/li/durationSeconds` | 0.2% (4/2054) | 数值 | 10 / 12.75 / 30 |
| `comps/li/edgeLengthRange` | 0.1% (1/2054) | 文本 | 9~25 |
| `comps/li/effect` | 0.1% (2/2054) | 文本 | CocoonDestroyed |
| `comps/li/effectCharged` | 0.1% (1/2054) | 文本 | NeuralSuperchargerCharged |
| `comps/li/effecter` | 0.3% (6/2054) | 文本 | BurnbongSmoke / ChristmasTreeTwinkle / FireSmoke |
| `comps/li/effecterDef` | 0.9% (19/2054) | 文本 | AtmosphericHeaterAmbience / Shell_AcidSpitLaunched / Shell_AcidSpitStream |
| `comps/li/effecterOnUsed` | 0.1% (1/2054) | 文本 | BiomutationPulserUsed |
| `comps/li/effecterReleasing` | 0.1% (3/2054) | 文本 | DeadlifeReleasing / ToxGasReleasing |
| `comps/li/effectHacking` | 0.5% (11/2054) | 文本 | HackingTerminal |
| `comps/li/effectInUse` | 0.1% (1/2054) | 文本 | SleepAcceleratorActive |
| `comps/li/effectStages` | 0.1% (1/2054) | 容器 |  |
| `comps/li/effectStages/li` | 0.1% (2/2054) | 容器 |  |
| `comps/li/effectStages/li/effecterDef` | 0.1% (2/2054) | 文本 | Power_Cell_Burning / Power_Cell_Sparks |
| `comps/li/effectStages/li/minHitPointsPercent` | 0.1% (2/2054) | 数值 | 0.1666 / 9999 |
| `comps/li/efficiency` | 0.1% (1/2054) | 数值 | 0.5 |
| `comps/li/eggCountRange` | 1.2% (24/2054) | 数值/文本 | 1 / 1~1 / 1~2 |
| `comps/li/eggFertilizationCountMax` | 1.2% (24/2054) | 数值 | 1 |
| `comps/li/eggFertilizedDef` | 1.2% (24/2054) | 文本 | EggCassowaryFertilized / EggChickenFertilized / EggEmuFertilized |
| `comps/li/eggLayIntervalDays` | 1.2% (24/2054) | 数值 | 1 / 1.333 / 2 |
| `comps/li/eggProgressUnfertilizedMax` | 1.0% (21/2054) | 数值 | 0.5 |
| `comps/li/eggUnfertilizedDef` | 1.2% (24/2054) | 文本 | EggCassowaryUnfertilized / EggChickenUnfertilized / EggEmuUnfertilized |
| `comps/li/emissionInterval` | 1.0% (21/2054) | 数值 | 100 / 150 / 350 |
| `comps/li/empChancePerTick` | 0.2% (4/2054) | 数值 | 0.03 / 0.3 / 0.5 |
| `comps/li/empEffecterDimensions` | 0.1% (2/2054) | 文本 | (1.8,0,0.5) / (2.0,0,1.6) |
| `comps/li/empEffecterOffset` | 0.1% (1/2054) | 文本 | (0,0,-0.5) |
| `comps/li/emptyGraphic` | 0.1% (1/2054) | 容器 |  |
| `comps/li/emptyGraphic/addTopAltitudeBias` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/emptyGraphic/drawSize` | 0.1% (1/2054) | 文本 | (4,4) |
| `comps/li/emptyGraphic/graphicClass` | 0.1% (1/2054) | 文本 | Graphic_Multi |
| `comps/li/emptyGraphic/shadowData` | 0.1% (1/2054) | 容器 |  |
| `comps/li/emptyGraphic/shadowData/volume` | 0.1% (1/2054) | 文本 | (1.8, 2, 1.8) |
| `comps/li/emptyGraphic/texPath` | 0.1% (1/2054) | 文本 | Things/Building/Mech/AncientMechGestatorIntact_Empty/AncientMechGestatorIntact_E |
| `comps/li/enableAfterTicks` | 0.1% (1/2054) | 数值 | 1200 |
| `comps/li/endTime` | 0.1% (1/2054) | 数值 | 0.8 |
| `comps/li/energyLossPerDamage` | 0.1% (1/2054) | 数值 | 0.01 |
| `comps/li/energyOnReset` | 0.1% (1/2054) | 数值 | 4.0 |
| `comps/li/energyPerSecond` | 0.1% (2/2054) | 数值 | -21 / 21 |
| `comps/li/enoughPlantsLetterLabel` | 0.1% (1/2054) | 文本 | About: Anima tree linking |
| `comps/li/enoughPlantsLetterText` | 0.1% (1/2054) | 文本 | The anima tree now has {0} anima grass around it. This is enough for a tribal pe |
| `comps/li/enterSound` | 0.1% (1/2054) | 文本 | BiosculpterPod_Enter |
| `comps/li/entityLungeSoundHi` | 0.1% (1/2054) | 文本 | EntityChainHigh |
| `comps/li/entityLungeSoundLow` | 0.1% (1/2054) | 文本 | EntityChainLow |
| `comps/li/exclusionAreaOffset` | 0.1% (2/2054) | 文本 | (0, 0, -5) / (0, 0, -7) |
| `comps/li/exclusionAreaSize` | 0.1% (2/2054) | 文本 | (1, 0, 5) / (2, 0, 7) |
| `comps/li/exhaustSettings` | 0.1% (2/2054) | 容器 |  |
| `comps/li/exhaustSettings/emissionsPerSecond` | 0.1% (2/2054) | 数值 | 40.0 |
| `comps/li/exhaustSettings/exhaustFleckDef` | 0.1% (2/2054) | 文本 | GravshipThrusterExhaust |
| `comps/li/exhaustSettings/rotationOverTimeRange` | 0.1% (2/2054) | 文本 | -180.0~180.0 |
| `comps/li/exhaustSettings/scaleRange` | 0.1% (2/2054) | 文本 | 1.5~3.0 / 3.0~5.0 |
| `comps/li/exhaustSettings/spawnRadiusRange` | 0.1% (2/2054) | 文本 | 0.0~0.5 |
| `comps/li/exhaustSettings/velocity` | 0.1% (2/2054) | 文本 | (0.0,0.0,-20.0) |
| `comps/li/exhaustSettings/velocityMultiplierRange` | 0.1% (2/2054) | 文本 | 0.8~1.2 |
| `comps/li/exhaustSettings/velocityRotationRange` | 0.1% (2/2054) | 文本 | -10.0~10.0 |
| `comps/li/existingAddictionSeverityOffset` | 0.4% (9/2054) | 数值 | 0.1 / 0.15 / 0.20 |
| `comps/li/exitSound` | 0.1% (1/2054) | 文本 | BiosculpterPod_Exit |
| `comps/li/expireEffect` | 0.1% (1/2054) | 文本 | RaisedRock_Collapse |
| `comps/li/explodeOnKilled` | 0.5% (10/2054) | 布尔 | true |
| `comps/li/explosionDamageAmount` | 0.1% (1/2054) | 数值 | 40 |
| `comps/li/explosionDamageType` | 0.1% (1/2054) | 文本 | Bomb |
| `comps/li/explosionEffect` | 0.3% (6/2054) | 文本 | ExtinguisherExplosion / GiantExplosion |
| `comps/li/explosionRadius` | 0.1% (1/2054) | 数值 | 2.9 |
| `comps/li/explosionSound` | 0.2% (4/2054) | 文本 | Explosion_FirefoamPopPack / Explosion_FirefoamPopper / Explosion_GiantBomb |
| `comps/li/explosiveDamageType` | 2.6% (54/2054) | 文本 | Bomb / DeadlifeDust / Flame |
| `comps/li/explosiveExpandPerFuel` | 0.1% (3/2054) | 数值 | 0.06 / 0.95 / 1.25 |
| `comps/li/explosiveExpandPerStackcount` | 0.3% (6/2054) | 数值 | 0.037 / 0.4 |
| `comps/li/explosiveRadius` | 2.6% (54/2054) | 数值 | 3.9 / 4 / 5 |
| `comps/li/externalTicking` | 0.1% (2/2054) | 布尔 | true |
| `comps/li/extraInspectStringKey` | 0.2% (5/2054) | 文本 | ExplosionOnDamageWarning / MechStunPulseWarning |
| `comps/li/extraRequiredIngredients` | 0.1% (1/2054) | 容器 |  |
| `comps/li/extraRequiredIngredients/MedicineUltratech` | 0.1% (1/2054) | 数值 | 2 |
| `comps/li/factorByDifficulty` | 0.2% (5/2054) | 布尔 | false / true |
| `comps/li/fadeInSecs` | 0.1% (1/2054) | 数值 | 2.0 |
| `comps/li/fadeOutSecs` | 0.1% (1/2054) | 数值 | 2.0 |
| `comps/li/feralCascadeRadialDistance` | 0.1% (1/2054) | 数值 | 25 |
| `comps/li/feralMtbDays` | 0.1% (1/2054) | 数值 | 10 |
| `comps/li/fieldRadius` | 0.1% (1/2054) | 数值 | 8.9 |
| `comps/li/filthDef` | 0.2% (5/2054) | 文本 | Filth_LooseGround / Filth_Slime |
| `comps/li/finalFireSize` | 0.1% (2/2054) | 数值 | 0.5 / 1.75 |
| `comps/li/fireGrowthDurationTicks` | 0.1% (1/2054) | 数值 | 500 |
| `comps/li/fireSize` | 0.6% (12/2054) | 数值 | 0.4 / 0.5 / 0.8 |
| `comps/li/fixedIngredient` | 0.1% (1/2054) | 文本 | Steel |
| `comps/li/fixedLaunchDistanceMax` | 0.1% (3/2054) | 数值 | 53 / 62 / 67 |
| `comps/li/flameOffsetsPerDirection` | 0.1% (2/2054) | 容器 |  |
| `comps/li/flameOffsetsPerDirection/li` | 0.4% (8/2054) | 文本 | (0, 0, 0.5) / (0, 0, 1.0) |
| `comps/li/flameShaderParameters` | 0.1% (2/2054) | 容器 |  |
| `comps/li/flameShaderParameters/_MainTex` | 0.1% (2/2054) | 文本 | /Things/Mote/LargeThruster_Burn / /Things/Mote/SmallThruster_Burn |
| `comps/li/flameShaderType` | 0.1% (2/2054) | 文本 | MoteGlow |
| `comps/li/flameSize` | 0.1% (2/2054) | 数值 | 4.0 |
| `comps/li/fleck` | 0.5% (11/2054) | 文本 | DustSlow / Music / Smoke |
| `comps/li/fleckDef` | 0.6% (12/2054) | 文本 | AncientSmoke / PsycastPsychicEffect / PsycastPsychicLine |
| `comps/li/fleckOnTarget` | 0.1% (3/2054) | 文本 | PsycastPsychicEffect |
| `comps/li/fleckOnUsed` | 0.2% (5/2054) | 文本 | PsycastAreaEffect |
| `comps/li/fleckOnUsedScale` | 0.2% (5/2054) | 数值 | 10 |
| `comps/li/fleckScale` | 0.2% (4/2054) | 数值 | 2.0 / 4 / 4.0 |
| `comps/li/fleckSpawnMTB` | 0.1% (1/2054) | 数值 | 25 |
| `comps/li/fleshbeastBirthThresholdRange` | 0.1% (1/2054) | 文本 | 125~200 |
| `comps/li/fleshbeastPointsByThreat` | 0.1% (1/2054) | 容器 |  |
| `comps/li/fleshbeastPointsByThreat/points` | 0.1% (1/2054) | 容器 |  |
| `comps/li/fleshbeastPointsByThreat/points/li` | 0.2% (4/2054) | 文本 | (0, 100) / (1600, 400) / (5000, 600) |
| `comps/li/fleshCorpsesOnly` | 0.1% (2/2054) | 布尔 | true |
| `comps/li/floatMenuFactionIcon` | 0.1% (3/2054) | 文本 | Mechanoid |
| `comps/li/floatMenuOptionPriority` | 0.1% (1/2054) | 文本 | SummonThreat |
| `comps/li/focusTypes` | 1.2% (25/2054) | 容器 |  |
| `comps/li/focusTypes/li` | 1.2% (25/2054) | 文本 | Artistic / Flame / Morbid |
| `comps/li/forbidOnMake` | 0.1% (3/2054) | 布尔 | true |
| `comps/li/forceEnabled` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/forceNormalSpeedOnInteracting` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/freezeNeeds` | 0.1% (1/2054) | 容器 |  |
| `comps/li/freezeNeeds/li` | 0.1% (1/2054) | 文本 | Food |
| `comps/li/frequencyTicks` | 0.9% (19/2054) | 数值 | 120000 |
| `comps/li/fuelCapacity` | 1.3% (27/2054) | 数值 | 20.0 / 5 / 60.0 |
| `comps/li/fuelConsumptionPerTickInRain` | 0.4% (8/2054) | 数值 | 0.0006 |
| `comps/li/fuelConsumptionRate` | 0.8% (17/2054) | 数值 | 0.5 / 1.5 / 6 |
| `comps/li/fuelFilter` | 1.3% (27/2054) | 容器 |  |
| `comps/li/fuelFilter/thingDefs` | 1.3% (27/2054) | 容器 |  |
| `comps/li/fuelFilter/thingDefs/li` | 1.3% (27/2054) | 文本 | Bioferrite / Chemfuel / HemogenPack |
| `comps/li/fuelGizmoLabel` | 0.4% (9/2054) | 文本 | Barrel durability / Foam / Rockets |
| `comps/li/fuelIconPath` | 0.3% (6/2054) | 文本 | Things/Item/Resource/Chemfuel / Things/Item/Resource/ReinforcedBarrel/ReinforcedBarrel / UI/Overlays/Barrel |
| `comps/li/fuelIsMortarBarrel` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/fuelLabel` | 0.5% (10/2054) | 文本 | Foam / Hemogen / Shots until barrel change |
| `comps/li/fuelMultiplier` | 0.3% (6/2054) | 数值 | 0.14 / 0.5 / 0.75 |
| `comps/li/fuelPerTile` | 0.1% (1/2054) | 数值 | 3 |
| `comps/li/fuelSavingsPercent` | 0.1% (1/2054) | 数值 | 0.3 |
| `comps/li/functionsInVacuum` | 0.4% (8/2054) | 布尔 | false |
| `comps/li/gainThoughtOnCompletion` | 0.1% (1/2054) | 文本 | AgeReversalReceived |
| `comps/li/gas` | 0.1% (1/2054) | 文本 | DeadlifeDust |
| `comps/li/gasType` | 0.1% (3/2054) | 文本 | DeadlifeDust / ToxGas |
| `comps/li/getsColdContainmentBonus` | 0.1% (3/2054) | 布尔 | true |
| `comps/li/gizmoTipKey` | 0.2% (4/2054) | 文本 | GravshipShieldTip / ProjectileInterceptorTip / RemoteMechShieldTip |
| `comps/li/glowColor` | 3.6% (75/2054) | 文本 | (200, 0, 0, 0) / (230,100,100,0) / (74, 37, 2, 0) |
| `comps/li/glowRadius` | 3.6% (75/2054) | 数值 | 11 / 4.9 / 5 |
| `comps/li/goodwillImpact` | 0.4% (8/2054) | 数值 | -200 |
| `comps/li/graphicData` | 0.9% (19/2054) | 容器 |  |
| `comps/li/graphicData/drawRotated` | 0.1% (1/2054) | 布尔 | false |
| `comps/li/graphicData/drawSize` | 0.9% (19/2054) | 文本 | (1, 1) / (1, 2) / (2, 2) |
| `comps/li/graphicData/graphicClass` | 0.9% (19/2054) | 文本 | Graphic_Multi / Graphic_Single |
| `comps/li/graphicData/texPath` | 0.9% (19/2054) | 文本 | Things/Building/GrayBox/GrayBox_Open / Things/Building/Ruins/AncientHermeticCrateOpen / Things/Building/Ruins/ |
| `comps/li/graphicDrawerType` | 0.1% (1/2054) | 文本 | RealtimeOnly |
| `comps/li/graphics` | 0.2% (4/2054) | 容器 |  |
| `comps/li/graphics/li` | 0.2% (4/2054) | 容器 |  |
| `comps/li/graphics/li/drawOffset` | 0.2% (4/2054) | 文本 | (0, -0.01, 0) / (0, 0.01, 0) / (0, 0.01, 0.7) |
| `comps/li/graphics/li/drawSize` | 0.2% (4/2054) | 文本 | (2.3, 2.3) / (3,3) / (3.3, 3.3) |
| `comps/li/graphics/li/graphicClass` | 0.2% (4/2054) | 文本 | Graphic_Random / Graphic_Single |
| `comps/li/graphics/li/shaderType` | 0.1% (1/2054) | 文本 | Transparent |
| `comps/li/graphics/li/texPath` | 0.2% (4/2054) | 文本 | Things/Building/AncientHatchExit/AncientHatchExit_Ladder / Things/Building/VoidmetalMass/Outline_Large / Thing |
| `comps/li/growthCyclePointsByThreat` | 0.1% (1/2054) | 容器 |  |
| `comps/li/growthCyclePointsByThreat/points` | 0.1% (1/2054) | 容器 |  |
| `comps/li/growthCyclePointsByThreat/points/li` | 0.2% (4/2054) | 文本 | (0, 75) / (1600, 200) / (5000, 250) |
| `comps/li/guiLabelString` | 1.0% (20/2054) | 文本 | Choose who should analyze this / Choose who should deactivate this. / Choose who should do this |
| `comps/li/hackedGraphicData` | 0.1% (2/2054) | 容器 |  |
| `comps/li/hackedGraphicData/drawSize` | 0.1% (2/2054) | 文本 | (2, 2) / (5, 5) |
| `comps/li/hackedGraphicData/graphicClass` | 0.1% (2/2054) | 文本 | Graphic_Multi |
| `comps/li/hackedGraphicData/texPath` | 0.1% (2/2054) | 文本 | Things/Building/Ancient/GravReactor/AncientGravReactor_Off / Things/Building/MechanoidStabilizer/MechanoidStab |
| `comps/li/hackedInspectString` | 0.2% (4/2054) | 文本 | Deactivated. / Disabled / Hacked. |
| `comps/li/hackedLetterDef` | 0.1% (1/2054) | 文本 | PositiveEvent |
| `comps/li/hackedLetterLabel` | 0.1% (1/2054) | 文本 | Gravcore obtained |
| `comps/li/hackedLetterText` | 0.1% (1/2054) | 文本 | You've obtained a gravcore from the ancient reactor.\n\nThe reactor is shutting  |
| `comps/li/hackedMessage` | 0.2% (5/2054) | 文本 | {HACKER_labelShort} has finished hacking {SUBJECT_definite}. / {HACKER_labelShort} has finished hacking {SUBJE |
| `comps/li/hackingCompletedSound` | 0.1% (2/2054) | 文本 | AncientCommsConsoleActivated / AncientHatchOpened |
| `comps/li/harmFrequencyPerArea` | 0.1% (1/2054) | 数值 | 0.0077 |
| `comps/li/hasAnimation` | 0.1% (1/2054) | 布尔 | false |
| `comps/li/hatcherDaystoHatch` | 1.2% (24/2054) | 数值 | 3.5 / 4.5 / 6 |
| `comps/li/hatcherPawn` | 1.2% (24/2054) | 文本 | Chicken / Cobra / Iguana |
| `comps/li/heatPerSecond` | 1.1% (22/2054) | 数值 | 12 / 120 / 3 |
| `comps/li/heatPushMaxTemperature` | 0.5% (10/2054) | 数值 | 20 / 23 / 28 |
| `comps/li/heatPushMinTemperature` | 0.1% (1/2054) | 数值 | 17 |
| `comps/li/heatToPush` | 0.1% (3/2054) | 数值 | 200 / 40 |
| `comps/li/hediff` | 0.3% (7/2054) | 文本 | BandNode / MechBoost / PainField |
| `comps/li/hediffDef` | 0.6% (13/2054) | 文本 | JuggernautSerum / Metalblood / MindNumbSerum |
| `comps/li/hediffToApply` | 0.1% (3/2054) | 文本 | GlucosoidRush / HemogenAmplified / PsychofluidRush |
| `comps/li/heldPawnKind` | 0.1% (1/2054) | 文本 | Revenant |
| `comps/li/hemogenLimitOffset` | 0.1% (1/2054) | 数值 | 0.25 |
| `comps/li/hideSource` | 0.1% (2/2054) | 布尔 | true |
| `comps/li/hitPoints` | 0.2% (4/2054) | 数值 | 200 / 26 / 300 |
| `comps/li/hitPointsRestoreInstantlyAfterCharge` | 0.1% (3/2054) | 布尔 | false / true |
| `comps/li/hotKey` | 1.0% (21/2054) | 文本 | Misc4 |
| `comps/li/iconPath` | 0.2% (4/2054) | 文本 | UI/Gizmos/BiosculpterCycleAgeReversal / UI/Gizmos/BiosculpterCycleBioregeneration / UI/Gizmos/BiosculpterCycle |
| `comps/li/idlePowerDraw` | 0.4% (9/2054) | 数值 | 0 / 25 / 50 |
| `comps/li/idlePulseSpeed` | 0.1% (1/2054) | 数值 | 3 |
| `comps/li/ignoreForbidden` | 0.2% (5/2054) | 布尔 | true |
| `comps/li/ignoreMechs` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/ignoreOtherReservations` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/ignorePlayerFactionPawns` | 0.1% (3/2054) | 布尔 | True |
| `comps/li/ignoreSpecialTrees` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/incidentTargetWhileStarting` | 0.1% (1/2054) | 文本 | Map_RaidBeacon |
| `comps/li/inheritFaction` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/initialAllowAutoRefuel` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/initialConfigurableTargetFuelLevel` | 0.2% (4/2054) | 数值 | 150 / 250 / 400 |
| `comps/li/initialConnectionStrengthRange` | 0.1% (1/2054) | 文本 | 0.25~0.45 |
| `comps/li/initialFuelPercent` | 0.8% (17/2054) | 数值 | 0 / 0.1 / 1 |
| `comps/li/initialGrowthRange` | 0.1% (1/2054) | 文本 | 0.2~0.8 |
| `comps/li/initialPawnsPoints` | 0.1% (1/2054) | 数值 | 200 |
| `comps/li/inspectString` | 1.2% (24/2054) | 文本 | Contains: Unknown\nDestroy noctoliths to end the unnatural darkness. / Kill to collect: Neural lump / Send a c |
| `comps/li/inspectStringLabel` | 0.1% (1/2054) | 文本 | skull of |
| `comps/li/intellectualSkillPrerequisite` | 0.2% (5/2054) | 数值 | 4 / 6 / 7 |
| `comps/li/interactionEffectCooldownDays` | 0.1% (3/2054) | 数值 | 0 / 40 / 5 |
| `comps/li/interactionEffecter` | 0.1% (1/2054) | 文本 | VoidStructureActivating |
| `comps/li/interceptAirProjectiles` | 0.1% (2/2054) | 布尔 | true |
| `comps/li/interceptEffect` | 0.1% (1/2054) | 文本 | Interceptor_BlockedProjectilePsychic |
| `comps/li/interceptGroundProjectiles` | 0.3% (7/2054) | 布尔 | true |
| `comps/li/interceptNonHostileProjectiles` | 0.1% (3/2054) | 布尔 | true |
| `comps/li/interceptOutgoingProjectiles` | 0.1% (3/2054) | 布尔 | false / true |
| `comps/li/intervalTicks` | 0.1% (2/2054) | 数值 | 15000 / 25000 |
| `comps/li/inUsePowerConsumption` | 0.1% (1/2054) | 数值 | 400 |
| `comps/li/isCombatEnhancingDrug` | 0.1% (2/2054) | 布尔 | true |
| `comps/li/jammed` | 0.1% (1/2054) | 容器 |  |
| `comps/li/jammed/graphicClass` | 0.1% (1/2054) | 文本 | Graphic_Single |
| `comps/li/jammed/ignoreThingDrawColor` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/jammed/texPath` | 0.1% (1/2054) | 文本 | Things/Building/GrayDoor/GrayDoor_Jammed |
| `comps/li/jobDormancy` | 0.1% (2/2054) | 布尔 | true |
| `comps/li/jobString` | 1.3% (26/2054) | 文本 | Deactivate obelisk / Decipher floor etching / Force this door open |
| `comps/li/key` | 0.2% (4/2054) | 文本 | ageReversal / bioregeneration / medic |
| `comps/li/killWhenDepleted` | 0.1% (1/2054) | 布尔 | false |
| `comps/li/knowledgeCategory` | 0.9% (18/2054) | 文本 | Advanced / Basic |
| `comps/li/label` | 0.4% (9/2054) | 文本 | Dreadmeld released / age reversal / bioregeneration |
| `comps/li/labelOverride` | 0.1% (2/2054) | 文本 | Battery power |
| `comps/li/landingAreaTerrainSupport` | 0.1% (1/2054) | 文本 | Light |
| `comps/li/largeOverdoseChance` | 0.2% (4/2054) | 数值 | 0.005 / 0.01 / 0.015 |
| `comps/li/layerWhitelist` | 0.1% (2/2054) | 容器 |  |
| `comps/li/layerWhitelist/li` | 0.1% (2/2054) | 文本 | Surface |
| `comps/li/leavings` | 0.1% (1/2054) | 容器 |  |
| `comps/li/leavings/Shard` | 0.1% (1/2054) | 数值 | 1 |
| `comps/li/leavingsFilter` | 0.1% (1/2054) | 容器 |  |
| `comps/li/leavingsFilter/thingDefs` | 0.1% (1/2054) | 容器 |  |
| `comps/li/leavingsFilter/thingDefs/li` | 0.1% (1/2054) | 文本 | MechanoidTransponder |
| `comps/li/leftLetterLabel` | 0.1% (1/2054) | 文本 | Nociosphere departed |
| `comps/li/leftLetterText` | 0.1% (1/2054) | 文本 | The nociosphere has disappeared, ending its onslaught.\n\nIt's unclear where the |
| `comps/li/letterDef` | 0.5% (11/2054) | 文本 | NeutralEvent / PositiveEvent / ThreatBig |
| `comps/li/letterDesc` | 0.1% (2/2054) | 文本 | The fleshmass nucleus has grown a critical mass of new flesh. It has developed i / The nociosphere's activity  |
| `comps/li/letterDoorOpenedLabel` | 0.1% (1/2054) | 文本 | Blast door opened |
| `comps/li/letterDoorOpenedText` | 0.1% (1/2054) | 文本 | {HACKER_nameDef} used the ancient security terminal to open a blast door. |
| `comps/li/letterLabel` | 0.2% (5/2054) | 文本 | Available: {LEAVINGS1_label} / Fallen monolith / Gray statue activated |
| `comps/li/letterText` | 0.2% (5/2054) | 文本 | A {LEAVINGS1_label} has been left behind after an explosion. It can be decrypted / After approaching the stran |
| `comps/li/letterTitle` | 0.1% (2/2054) | 文本 | Fleshmass transformation / Nociosphere activated |
| `comps/li/letterTurretDisabledLabel` | 0.1% (1/2054) | 文本 | Turret disabled |
| `comps/li/letterTurretDisabledText` | 0.1% (1/2054) | 文本 | {HACKER_nameDef} used the ancient security terminal to disable a turret. |
| `comps/li/letterTurretHackedLabel` | 0.1% (1/2054) | 文本 | Turret reprogrammed |
| `comps/li/letterTurretHackedText` | 0.1% (1/2054) | 文本 | {HACKER_nameDef} used the ancient security terminal to reprogram a turret. The t |
| `comps/li/lifespanTicks` | 0.1% (2/2054) | 数值 | 10000 / 1200000 |
| `comps/li/linkableFacilities` | 1.2% (25/2054) | 容器 |  |
| `comps/li/linkableFacilities/li` | 2.3% (48/2054) | 文本 | BioferriteHarvester / ElectricInhibitor / Electroharvester |
| `comps/li/linkSound` | 0.1% (1/2054) | 文本 | AnimaTreeLink |
| `comps/li/listOrder` | 0.6% (12/2054) | 数值 | 10 / 1200 / 200 |
| `comps/li/lockoutDurationHoursRange` | 0.2% (5/2054) | 文本 | 12~18 / 2~3 / 6~18 |
| `comps/li/lookForTargetOnEscape` | 0.1% (1/2054) | 布尔 | false |
| `comps/li/lordJob` | 0.4% (9/2054) | 文本 | LordJob_AssaultColony / LordJob_DefendAndExpandHive / LordJob_MechanoidsDefend |
| `comps/li/lordJoinRadius` | 0.1% (1/2054) | 数值 | 10 |
| `comps/li/lowPowerConsumptionFactor` | 0.1% (3/2054) | 数值 | 0.05 / 0.1 |
| `comps/li/mag` | 0.1% (1/2054) | 数值 | 0.03 |
| `comps/li/maintain` | 0.1% (3/2054) | 布尔 | True |
| `comps/li/maintainProgress` | 0.1% (2/2054) | 布尔 | true |
| `comps/li/manWorkType` | 0.1% (1/2054) | 文本 | Violent |
| `comps/li/massCapacity` | 0.1% (3/2054) | 数值 | 1000 / 2000 / 500 |
| `comps/li/materialsAddedSound` | 0.1% (1/2054) | 文本 | WastepackAtomizer_MaterialInserted |
| `comps/li/max1PerGroup` | 0.2% (5/2054) | 布尔 | true |
| `comps/li/maxCapacity` | 0.1% (1/2054) | 数值 | 4 |
| `comps/li/maxCharges` | 1.2% (24/2054) | 数值 | 1 / 2 / 4 |
| `comps/li/maxDeviationFromStartingAngle` | 0.1% (1/2054) | 数值 | 35 |
| `comps/li/maxDistance` | 0.9% (19/2054) | 数值 | 10 / 4 / 5.1 |
| `comps/li/maxDistAwakenByOther` | 0.1% (3/2054) | 数值 | 3 |
| `comps/li/maxDrawSize` | 0.1% (1/2054) | 数值 | 2.8 |
| `comps/li/maxDryadsPerConnectionStrengthCurve` | 0.1% (1/2054) | 容器 |  |
| `comps/li/maxDryadsPerConnectionStrengthCurve/points` | 0.1% (1/2054) | 容器 |  |
| `comps/li/maxDryadsPerConnectionStrengthCurve/points/li` | 0.2% (5/2054) | 文本 | (0, 0) / (0.05, 1) / (0.25, 2) |
| `comps/li/maxDryadsWild` | 0.1% (1/2054) | 数值 | 2 |
| `comps/li/maxGrowthCycleHours` | 0.1% (1/2054) | 数值 | 36 |
| `comps/li/maxIngredientCount` | 0.1% (1/2054) | 数值 | 600 |
| `comps/li/maxPawnsToSpawn` | 0.1% (1/2054) | 数值 | 4 |
| `comps/li/maxPlants` | 0.1% (2/2054) | 数值 | 35 / 60 |
| `comps/li/maxRadius` | 0.2% (5/2054) | 数值 | 50 / 7.9 |
| `comps/li/maxRotationRate` | 0.1% (3/2054) | 数值 | 10.0 / 20.0 |
| `comps/li/maxSafeTemperature` | 0.1% (2/2054) | 数值 | 32 / 50 |
| `comps/li/maxSeverity` | 0.1% (1/2054) | 数值 | 3 |
| `comps/li/maxSimultaneous` | 1.1% (22/2054) | 数值 | 1 / 3 / 4 |
| `comps/li/maxSpawnedPawnsPoints` | 0.1% (1/2054) | 数值 | 500 |
| `comps/li/maxSpeakerDistance` | 0.1% (1/2054) | 数值 | 12 |
| `comps/li/maxVelocityAngle` | 0.1% (3/2054) | 数值 | 20.0 |
| `comps/li/maxVelocitySpeed` | 0.1% (3/2054) | 数值 | 0.1 / 0.7 |
| `comps/li/mechKindOptions` | 0.1% (1/2054) | 容器 |  |
| `comps/li/mechKindOptions/Mech_Cyclops` | 0.1% (1/2054) | 容器 |  |
| `comps/li/mechKindOptions/Mech_Lancer` | 0.1% (1/2054) | 容器 |  |
| `comps/li/mechKindOptions/Mech_Scorcher` | 0.1% (1/2054) | 容器 |  |
| `comps/li/mechKindOptions/Mech_Scyther` | 0.1% (1/2054) | 容器 |  |
| `comps/li/mechKindOptions/Mech_Tesseron` | 0.1% (1/2054) | 容器 |  |
| `comps/li/mentalState` | 0.2% (4/2054) | 文本 | CocoonDisturbed |
| `comps/li/message` | 0.1% (1/2054) | 文本 | The anima tree has died and emitted a disturbing psychic scream. |
| `comps/li/messageActivating` | 0.1% (1/2054) | 文本 | The obelisk has begun to activate. |
| `comps/li/messageCompletedString` | 0.3% (7/2054) | 文本 | {PAWN_nameDef} has successfully deactivated the obelisk. / {PAWN_nameDef} has successfully deciphered the floo |
| `comps/li/messageCooldownEnded` | 0.1% (3/2054) | 文本 | The corrupted obelisk is ready to use again. / The twisted obelisk is ready to use again. / The warped obelisk |
| `comps/li/messageDigested` | 0.1% (1/2054) | 文本 | A devourer swallowed {PAWN_nameDef} whole! Kill the devourer before it digests { |
| `comps/li/messageDigestionCompleted` | 0.1% (1/2054) | 文本 | The devourer has regurgitated {PAWN_nameDef}. |
| `comps/li/messageEmerged` | 0.1% (1/2054) | 文本 | {PAWN_nameDef} emerged from the devourer. |
| `comps/li/messageEmergedCorpse` | 0.1% (1/2054) | 文本 | {PAWN_nameDef} emerged from the devourer's corpse. |
| `comps/li/messageNoValidTarget` | 0.1% (1/2054) | 文本 | {HACKER_nameDef} couldn't find any security systems using the ancient security t |
| `comps/li/messageOnCropDeath` | 0.1% (1/2054) | 布尔 | false |
| `comps/li/milkAmount` | 0.3% (7/2054) | 数值 | 11 / 12 / 14 |
| `comps/li/milkDef` | 0.3% (7/2054) | 文本 | Chemfuel / Milk |
| `comps/li/milkFemaleOnly` | 0.1% (1/2054) | 布尔 | false |
| `comps/li/milkIntervalDays` | 0.3% (7/2054) | 数值 | 1 / 2 / 3 |
| `comps/li/minAlpha` | 0.1% (2/2054) | 数值 | 0.2 / 0.5 |
| `comps/li/minCountToEmpty` | 0.1% (1/2054) | 数值 | 20 |
| `comps/li/minDistance` | 0.1% (1/2054) | 数值 | 1 |
| `comps/li/minDrawSize` | 0.1% (1/2054) | 数值 | 2.5 |
| `comps/li/minFuelCost` | 0.1% (1/2054) | 数值 | 50 |
| `comps/li/minGrowthCycleHours` | 0.1% (1/2054) | 数值 | 12 |
| `comps/li/minGrowthForSpawn` | 0.1% (1/2054) | 数值 | 0.6 |
| `comps/li/minIdleAlpha` | 0.1% (3/2054) | 数值 | 0.05 / 0.2 |
| `comps/li/minimumFueledThreshold` | 0.3% (6/2054) | 数值 | 1 / 12 |
| `comps/li/minMonolithLevelForStudy` | 0.9% (19/2054) | 数值 | 1 |
| `comps/li/minOnslaughtTicks` | 0.1% (1/2054) | 数值 | 1800 |
| `comps/li/minQualityForArtistic` | 1.0% (21/2054) | 文本 | Awful / Excellent |
| `comps/li/minRadius` | 0.1% (1/2054) | 数值 | 10 |
| `comps/li/minRitualProgress` | 0.1% (2/2054) | 数值 | 0.25 |
| `comps/li/minRotationRate` | 0.1% (3/2054) | 数值 | -10.0 / -20.0 |
| `comps/li/minSafeTemperature` | 0.1% (2/2054) | 数值 | -1 / 0 |
| `comps/li/minSeverity` | 0.1% (1/2054) | 数值 | 3 |
| `comps/li/minToleranceToAddict` | 0.2% (5/2054) | 数值 | 0.10 / 0.15 / 0.25 |
| `comps/li/minVelocityAngle` | 0.1% (3/2054) | 数值 | -20.0 |
| `comps/li/minVelocitySpeed` | 0.1% (3/2054) | 数值 | 0.0 / 0.5 |
| `comps/li/mote` | 0.6% (12/2054) | 文本 | Mote_PsychicConditionCauserEffect / Mote_PsychicEmanatorEffect / Mote_SkyLanternOuterGlow |
| `comps/li/moteDef` | 0.2% (4/2054) | 文本 | Mote_BioFerriteHarvested / Mote_ChargingElectroCables / Mote_NoctolEyes |
| `comps/li/mtbGrowthCycleHours` | 0.1% (1/2054) | 数值 | 20 |
| `comps/li/mtbTicks` | 0.1% (2/2054) | 数值 | 15000 |
| `comps/li/mustBeFullGrave` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/mustBeLayingInToBind` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/mustBePlacedAdjacent` | 0.1% (2/2054) | 布尔 | true |
| `comps/li/mustBePlacedAdjacentCardinalToAndFacingBedHead` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/mustBePlacedAdjacentCardinalToBedHead` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/mustBePlacedFacingThingLinear` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/mutantFilter` | 0.1% (1/2054) | 文本 | Ghoul |
| `comps/li/nameMaker` | 1.6% (32/2054) | 文本 | NamerArtCubeSculpture / NamerArtVoidSculpture / NamerArtWeaponGun |
| `comps/li/namerLabels` | 0.6% (13/2054) | 容器 |  |
| `comps/li/namerLabels/li` | 2.6% (53/2054) | 文本 | hammer / iron / revolver |
| `comps/li/needLevelOffset` | 0.5% (10/2054) | 数值 | 0.9 |
| `comps/li/needsOverseerEffect` | 0.1% (1/2054) | 文本 | MechUncontrolled |
| `comps/li/nextSpawnInspectStringKey` | 0.1% (1/2054) | 文本 | MechAssemblyCompleteIn |
| `comps/li/nextSpawnInspectStringKeyDormant` | 0.1% (1/2054) | 文本 | MechAssemblyNextType |
| `comps/li/noAssignablePawnsDesc` | 0.1% (1/2054) | 文本 | Throne ownership requires a person with a royal title. |
| `comps/li/noIngredientsFoodKind` | 0.3% (7/2054) | 文本 | Meat / NonMeat |
| `comps/li/nonDessicatedCorpsesOnly` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/noPawnsLeftToSpawnKey` | 0.1% (1/2054) | 文本 | ShutDown |
| `comps/li/notHackedInspectString` | 0.4% (8/2054) | 文本 | Hack to access ancient supply satellite. / Hack to access computer. / Hack to call nearby enemies. |
| `comps/li/offDurationMtbDays` | 0.1% (3/2054) | 数值 | 4 |
| `comps/li/offMessage` | 0.1% (1/2054) | 文本 | Off for plant resting period |
| `comps/li/offset` | 0.5% (10/2054) | 数值/文本 | (0,0,0.1) / (0,0,0.2) / (0,0,0.5) |
| `comps/li/offsetDistance` | 0.1% (2/2054) | 数值 | 0.5 / 1.75 |
| `comps/li/offsetEast` | 0.1% (2/2054) | 文本 | (-0.45,0,0.35) / (-0.575, 0, 0.24) |
| `comps/li/offsetMax` | 0.6% (12/2054) | 文本 | (0,0,0.9) / (0.3,0,-0.7) / (0.3,0,0.35) |
| `comps/li/offsetMin` | 0.6% (12/2054) | 文本 | (-0.3,0,-0.7) / (-0.3,0,0.35) / (-0.6,0,0.3) |
| `comps/li/offsetNorth` | 0.1% (2/2054) | 文本 | (0, 0, -0.34) / (0,0,0) |
| `comps/li/offsets` | 1.0% (21/2054) | 容器 |  |
| `comps/li/offsets/li` | 2.3% (47/2054) | 容器 |  |
| `comps/li/offsets/li/curve` | 0.3% (7/2054) | 容器 |  |
| `comps/li/offsets/li/curve/points` | 0.3% (7/2054) | 容器 |  |
| `comps/li/offsets/li/curve/points/li` | 1.7% (35/2054) | 文本 | (0,0.12) / (1,0.16) / (2,0.20) |
| `comps/li/offsets/li/defs` | 0.9% (18/2054) | 容器 |  |
| `comps/li/offsets/li/defs/AnimusStone` | 0.2% (4/2054) | 数值 | 0.02 |
| `comps/li/offsets/li/defs/li` | 3.0% (62/2054) | 文本 | SculptureLarge / SculptureSmall / ShardBeacon |
| `comps/li/offsets/li/defs/NatureShrine_Large` | 0.1% (1/2054) | 数值 | 0.01 |
| `comps/li/offsets/li/defs/NatureShrine_Small` | 0.1% (1/2054) | 数值 | 0.01 |
| `comps/li/offsets/li/drawRingRadius` | 0.3% (7/2054) | 布尔 | false |
| `comps/li/offsets/li/explanationKey` | 0.9% (18/2054) | 文本 | MeditationFocusPerBuilding / MeditationFocusPerFlame / MeditationFocusPerGrave |
| `comps/li/offsets/li/explanationKeyAbstract` | 0.9% (18/2054) | 文本 | MeditationFocusPerBuildingAbstract / MeditationFocusPerFlameAbstract / MeditationFocusPerGraveAbstract |
| `comps/li/offsets/li/focusPerFullGrave` | 0.1% (2/2054) | 数值 | 0.01 |
| `comps/li/offsets/li/focusPerQuality` | 0.1% (2/2054) | 容器 |  |
| `comps/li/offsets/li/focusPerQuality/points` | 0.1% (2/2054) | 容器 |  |
| `comps/li/offsets/li/focusPerQuality/points/li` | 0.7% (14/2054) | 文本 | (0,0.0) / (1,0.0) / (2,0.01) |
| `comps/li/offsets/li/li` | 1.6% (32/2054) | 文本 | (-0.2, 0, 0.65) / (-0.4, 0, 0.65) / (0.2, 0, 0.65) |
| `comps/li/offsets/li/maxBuildings` | 0.9% (18/2054) | 数值 | 4 / 6 / 8 |
| `comps/li/offsets/li/offset` | 0.7% (14/2054) | 数值 | 0.1 / 0.10 / 0.12 |
| `comps/li/offsets/li/offsetPerBuilding` | 0.6% (12/2054) | 数值 | 0.01 / 0.02 |
| `comps/li/offsets/li/radius` | 1.1% (22/2054) | 数值 | 27.9 / 9.9 |
| `comps/li/offsetSouth` | 0.1% (2/2054) | 文本 | (0, 0, 0.66) / (0,0,0.55) |
| `comps/li/offsetWest` | 0.1% (2/2054) | 文本 | (0.45,0,0.35) / (0.575, 0, 0.24) |
| `comps/li/onCooldownString` | 0.3% (6/2054) | 文本 | Duplication cooldown / Mutation cooldown / Nociosphere onslaught cooldown |
| `comps/li/onDurationMtbDays` | 0.1% (3/2054) | 数值 | 12 / 3 |
| `comps/li/onlyHumanlike` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/onlyRemotelyHackable` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/onlySendSignalOnce` | 0.1% (1/2054) | 布尔 | false |
| `comps/li/onlyTargetMechs` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/onslaughtEndedMessage` | 0.1% (1/2054) | 文本 | The nociosphere has ended its onslaught and has returned to its initial location |
| `comps/li/onslaughtInspectText` | 0.1% (1/2054) | 文本 | Onslaught mode: {0} seconds left |
| `comps/li/openGraphic` | 0.2% (5/2054) | 容器 |  |
| `comps/li/openGraphic/drawSize` | 0.2% (5/2054) | 数值 | 0.7 |
| `comps/li/openGraphic/graphicClass` | 0.2% (5/2054) | 文本 | Graphic_Multi |
| `comps/li/openGraphic/texPath` | 0.2% (5/2054) | 文本 | Things/Item/Book/Novel/Novel_Open / Things/Item/Book/Schematic/Schematic_Open / Things/Item/Book/Textbook/Text |
| `comps/li/operatingColor` | 0.2% (4/2054) | 文本 | (0.554,0.887,1.000) / (1.000,0.585,0.158) / (1.000,0.918,0.000) |
| `comps/li/operatingEffecter` | 0.1% (1/2054) | 文本 | BiosculpterPod_Operating |
| `comps/li/options` | 0.1% (1/2054) | 容器 |  |
| `comps/li/options/Mech_CentipedeBlaster` | 0.1% (1/2054) | 数值 | 6 |
| `comps/li/options/Mech_CentipedeBurner` | 0.1% (1/2054) | 数值 | 2 |
| `comps/li/options/Mech_CentipedeGunner` | 0.1% (1/2054) | 数值 | 4 |
| `comps/li/options/Mech_Centurion` | 0.1% (1/2054) | 数值 | 1 |
| `comps/li/options/Mech_Cyclops` | 0.1% (1/2054) | 数值 | 3 |
| `comps/li/options/Mech_Diabolus` | 0.1% (1/2054) | 数值 | 1 |
| `comps/li/options/Mech_Lancer` | 0.1% (1/2054) | 数值 | 10 |
| `comps/li/options/Mech_Legionary` | 0.1% (1/2054) | 数值 | 1 |
| `comps/li/options/Mech_Militor` | 0.1% (1/2054) | 数值 | 22 |
| `comps/li/options/Mech_Pikeman` | 0.1% (1/2054) | 数值 | 10 |
| `comps/li/options/Mech_Scorcher` | 0.1% (1/2054) | 数值 | 3 |
| `comps/li/options/Mech_Scyther` | 0.1% (1/2054) | 数值 | 15 |
| `comps/li/options/Mech_Tesseron` | 0.1% (1/2054) | 数值 | 3 |
| `comps/li/outOfFuelMessage` | 0.3% (6/2054) | 文本 | Needs new barrel / Needs new reinforced barrel / No slugs |
| `comps/li/overdoseSeverityOffset` | 0.3% (6/2054) | 文本 | 0.08~0.14 / 0.18~0.35 |
| `comps/li/overlightRadius` | 0.1% (3/2054) | 数值 | 1.5 / 2.0 / 7.0 |
| `comps/li/overrideIsCavePlant` | 0.1% (3/2054) | 布尔 | true |
| `comps/li/part` | 0.1% (2/2054) | 文本 | Head |
| `comps/li/pawnExitSound` | 0.1% (3/2054) | 文本 | Shuttle_PawnExit |
| `comps/li/pawnKind` | 0.1% (2/2054) | 文本 | Dryad_Basic / Larva |
| `comps/li/pawnLoadedSound` | 0.1% (2/2054) | 文本 | Shuttle_PawnLoaded |
| `comps/li/pawnsLeftToSpawnKey` | 0.1% (1/2054) | 文本 | MessageMechanoidsLeftToAssemble |
| `comps/li/pawnSpawnIntervalDays` | 0.1% (1/2054) | 数值 | 1 |
| `comps/li/pawnSpawnRadius` | 0.2% (5/2054) | 数值/文本 | 0 / 10~30 |
| `comps/li/performMergeCompatibilityChecks` | 0.1% (2/2054) | 布尔 | false |
| `comps/li/perRotationMotes` | 0.1% (1/2054) | 容器 |  |
| `comps/li/perRotationMotes/li` | 0.2% (4/2054) | 文本 | Mote_SubcoreEncoderEast / Mote_SubcoreEncoderNorth / Mote_SubcoreEncoderSouth |
| `comps/li/planetLayerWhitelist` | 0.1% (1/2054) | 容器 |  |
| `comps/li/planetLayerWhitelist/li` | 0.1% (1/2054) | 文本 | Surface |
| `comps/li/plantDefToSpawn` | 0.2% (4/2054) | 文本 | Plant_TreeArchean / Plant_TreeGauranlen / Plant_TreeHarbinger |
| `comps/li/plantsToNotOverwrite` | 0.1% (1/2054) | 容器 |  |
| `comps/li/plantsToNotOverwrite/li` | 0.1% (3/2054) | 文本 | Plant_GrassAnima / Plant_PodGauranlen / Plant_TreeAnima |
| `comps/li/points` | 1.2% (24/2054) | 数值/文本 | 150 / 40 / 55 |
| `comps/li/points/li` | 3.6% (74/2054) | 容器 |  |
| `comps/li/points/li/offset` | 3.6% (74/2054) | 文本 | (-1.32, 0, -1.3) / (-1.32, 0, 1.3) / (1.32, 0, -1.3) |
| `comps/li/points/li/type` | 3.6% (74/2054) | 文本 | PlatformRestraint0 / PlatformRestraint1 / PlatformRestraint2 |
| `comps/li/pollutionIntervalTicks` | 0.1% (1/2054) | 数值 | 180000 |
| `comps/li/postExplosionGasAmount` | 0.1% (1/2054) | 数值 | 100 |
| `comps/li/postExplosionGasRadiusOverride` | 0.1% (1/2054) | 数值 | 4.9 |
| `comps/li/postExplosionGasType` | 0.3% (7/2054) | 文本 | BlindSmoke / DeadlifeDust / ToxGas |
| `comps/li/postExplosionSpawnChance` | 0.2% (5/2054) | 数值 | 1 |
| `comps/li/postExplosionSpawnThingCount` | 0.2% (4/2054) | 数值 | 1 / 3 |
| `comps/li/postExplosionSpawnThingDef` | 0.2% (5/2054) | 文本 | Filth_FireFoam / Filth_Fuel |
| `comps/li/powerConsumptionIdle` | 0.1% (1/2054) | 数值 | 100 |
| `comps/li/powerUpgrades` | 0.1% (3/2054) | 容器 |  |
| `comps/li/powerUpgrades/li` | 0.1% (3/2054) | 容器 |  |
| `comps/li/powerUpgrades/li/factor` | 0.1% (3/2054) | 数值 | 0.5 |
| `comps/li/powerUpgrades/li/researchProject` | 0.1% (3/2054) | 文本 | ColoredLights |
| `comps/li/preExplosionSpawnChance` | 0.2% (4/2054) | 数值 | 0.25 / 1 |
| `comps/li/preExplosionSpawnSingleThingDef` | 0.3% (6/2054) | 文本 | CraterMedium / Filth_BlastMark |
| `comps/li/preExplosionSpawnThingDef` | 0.2% (4/2054) | 文本 | Filth_Fuel |
| `comps/li/prepareEffecterDef` | 0.1% (2/2054) | 文本 | MechBandAntennaPrepared / MechBandDishPrepared |
| `comps/li/preventConditionStacking` | 0.1% (3/2054) | 布尔 | false |
| `comps/li/prewarmCycles` | 0.1% (3/2054) | 数值 | 1.0 |
| `comps/li/progressedLetterDef` | 0.1% (3/2054) | 文本 | NeutralEvent |
| `comps/li/progressedLetterLabel` | 0.1% (3/2054) | 文本 | Analysis progress |
| `comps/li/progressedLetters` | 0.1% (3/2054) | 容器 |  |
| `comps/li/progressedLetters/li` | 0.2% (4/2054) | 文本 | {PAWN_nameDef} has finished analyzing the fleshmass neural lump. The sample carr / {PAWN_nameDef} has finished |
| `comps/li/progressPerDegreePerTick` | 0.1% (2/2054) | 数值 | 0.00001 / 0.00003 |
| `comps/li/propagationSpeed` | 0.1% (2/2054) | 数值 | 0.5 / 0.6 |
| `comps/li/providesFuel` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/psychicSensitiveTargetsOnly` | 0.2% (4/2054) | 布尔 | true |
| `comps/li/pulseSpeed` | 0.1% (1/2054) | 数值 | 0.5 |
| `comps/li/pumpEffecterDef` | 0.1% (2/2054) | 文本 | PollutionExtractedPoluxTree / PollutionPumped |
| `comps/li/pumpsPerWastepack` | 0.1% (2/2054) | 数值 | 0 / 6 |
| `comps/li/quest` | 0.1% (2/2054) | 文本 | MechanitorShip / MechanitorStartingMech |
| `comps/li/radius` | 1.4% (29/2054) | 数值 | 2 / 4 / 8 |
| `comps/li/radiusCheckInspectPaneKey` | 0.1% (1/2054) | 文本 | TriggerRadius |
| `comps/li/radiusPerDayCurve` | 0.1% (3/2054) | 容器 |  |
| `comps/li/radiusPerDayCurve/points` | 0.1% (3/2054) | 容器 |  |
| `comps/li/radiusPerDayCurve/points/li` | 0.5% (10/2054) | 文本 | 0  , 5 / 0, 4 / 1.5, 18 |
| `comps/li/rampDownTime` | 0.1% (1/2054) | 数值 | 20.0 |
| `comps/li/rampUpTime` | 0.1% (1/2054) | 数值 | 5.0 |
| `comps/li/range` | 0.1% (3/2054) | 数值 | 4.9 / 5.9 / 9.9 |
| `comps/li/reactivateEffect` | 0.3% (6/2054) | 文本 | BulletShieldGenerator_Reactivate / MortarShieldGenerator_Reactivate |
| `comps/li/readyEffecter` | 0.1% (1/2054) | 文本 | BiosculpterPod_Ready |
| `comps/li/rechargeHitPointsIntervalTicks` | 0.1% (2/2054) | 数值 | 120 / 75 |
| `comps/li/remainingSecondsInInspectString` | 0.1% (3/2054) | 布尔 | true |
| `comps/li/renderNodeProperties` | 0.1% (3/2054) | 容器 |  |
| `comps/li/renderNodeProperties/li` | 0.1% (3/2054) | 容器 |  |
| `comps/li/renderNodeProperties/li/baseLayer` | 0.1% (3/2054) | 数值 | 20 |
| `comps/li/renderNodeProperties/li/drawData` | 0.1% (3/2054) | 容器 |  |
| `comps/li/renderNodeProperties/li/drawData/dataWest` | 0.1% (3/2054) | 容器 |  |
| `comps/li/renderNodeProperties/li/drawData/dataWest/rotationOffset` | 0.1% (3/2054) | 数值 | 180 |
| `comps/li/renderNodeProperties/li/nodeClass` | 0.1% (3/2054) | 文本 | PawnRenderNode_TurretGun |
| `comps/li/renderNodeProperties/li/overrideMeshSize` | 0.1% (3/2054) | 文本 | (1, 1) |
| `comps/li/renderNodeProperties/li/parentTagDef` | 0.1% (3/2054) | 文本 | Body |
| `comps/li/renderNodeProperties/li/pawnType` | 0.1% (3/2054) | 文本 | Any |
| `comps/li/renderNodeProperties/li/workerClass` | 0.1% (3/2054) | 文本 | PawnRenderNodeWorker_TurretGun |
| `comps/li/repeatCompletedLetter` | 0.1% (3/2054) | 文本 | {PAWN_nameDef} has completed {PAWN_possessive} analysis of the gray flesh sample / {PAWN_nameDef} has finished |
| `comps/li/repeatCompletedLetterDef` | 0.1% (3/2054) | 文本 | NeutralEvent |
| `comps/li/repeatCompletedLetterLabel` | 0.1% (3/2054) | 文本 | Analysis complete |
| `comps/li/reportText` | 0.1% (1/2054) | 文本 | A multiplier on how quickly children learn during lessons which are assisted by  |
| `comps/li/requiredDamageTypeToExplode` | 0.3% (6/2054) | 文本 | Flame |
| `comps/li/requiredFocus` | 0.1% (1/2054) | 文本 | Natural |
| `comps/li/requiredResearch` | 0.1% (1/2054) | 容器 |  |
| `comps/li/requiredResearch/li` | 0.1% (1/2054) | 文本 | Bioregeneration |
| `comps/li/requiredSubplantCountPerPsylinkLevel` | 0.1% (1/2054) | 容器 |  |
| `comps/li/requiredSubplantCountPerPsylinkLevel/li` | 0.3% (6/2054) | 数值 | 20 |
| `comps/li/requiresExistingHediff` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/requiresFuelingPort` | 0.1% (2/2054) | 布尔 | false |
| `comps/li/requiresHoldingPlatform` | 0.6% (13/2054) | 布尔 | true |
| `comps/li/requiresImprisonment` | 0.1% (2/2054) | 布尔 | true |
| `comps/li/requiresLOS` | 0.5% (10/2054) | 布尔 | false |
| `comps/li/requiresMechanitor` | 0.1% (3/2054) | 布尔 | true |
| `comps/li/requiresPower` | 0.2% (4/2054) | 布尔 | false / true |
| `comps/li/requiresPsychicallySensitive` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/resetLastRecreationalDrugTick` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/resolveEffecter` | 0.1% (1/2054) | 文本 | AtomizerResolve |
| `comps/li/restEffectiveness` | 0.1% (3/2054) | 数值 | 0.8 |
| `comps/li/retuningEffect` | 0.1% (1/2054) | 文本 | BandNodeRetuning |
| `comps/li/rotationRate` | 0.3% (6/2054) | 文本 | -15~15 / -180~180 / -30~30 |
| `comps/li/rotDestroys` | 1.1% (23/2054) | 布尔 | true |
| `comps/li/saveKeysPrefix` | 0.5% (10/2054) | 文本 | grass / jelly / pod |
| `comps/li/scale` | 0.5% (10/2054) | 文本 | 0.6~0.9 / 1~1.1 / 1~2.5 |
| `comps/li/scanFindGuaranteedDays` | 0.1% (2/2054) | 数值 | 6 / 8 |
| `comps/li/scanFindMtbDays` | 0.1% (2/2054) | 数值 | 3 / 4 |
| `comps/li/scanSpeedStat` | 0.1% (2/2054) | 文本 | ResearchSpeed |
| `comps/li/secondsPerConvert` | 0.1% (1/2054) | 数值 | 20 |
| `comps/li/selectCycleColor` | 0.1% (1/2054) | 文本 | (0.321, 1, 0.349) |
| `comps/li/sentOnslaughtDurationSeconds` | 0.1% (1/2054) | 文本 | 90~120 |
| `comps/li/severity` | 0.1% (1/2054) | 数值 | 0.01 |
| `comps/li/severityPerSecond` | 0.1% (1/2054) | 数值 | 0.005 |
| `comps/li/shardsRequired` | 0.1% (2/2054) | 数值 | 2 |
| `comps/li/shearIntervalDays` | 0.3% (7/2054) | 数值 | 10 / 15 / 20 |
| `comps/li/shipDef` | 0.1% (1/2054) | 文本 | Ship_PassengerShuttle |
| `comps/li/shortCircuitInRain` | 1.0% (21/2054) | 布尔 | true |
| `comps/li/shouldJoinParentLord` | 0.3% (7/2054) | 布尔 | True |
| `comps/li/showAllowAutoRefuelToggle` | 1.0% (21/2054) | 布尔 | true |
| `comps/li/showContentsInInspectPane` | 0.1% (1/2054) | 布尔 | false |
| `comps/li/showFuelGizmo` | 0.5% (10/2054) | 布尔 | true |
| `comps/li/showGizmoOnNonPlayerControlled` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/showLetterOnActivated` | 0.1% (2/2054) | 布尔 | true |
| `comps/li/showLetterOnManualActivation` | 0.1% (1/2054) | 布尔 | false |
| `comps/li/showMassInInspectString` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/showMaxSimultaneous` | 0.2% (4/2054) | 布尔 | false |
| `comps/li/showMessageIfOwned` | 0.2% (4/2054) | 布尔 | true |
| `comps/li/showMustBeActivatedByColonist` | 0.4% (8/2054) | 布尔 | false |
| `comps/li/showNextSpawnInInspect` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/showOverallStats` | 0.1% (2/2054) | 布尔 | false |
| `comps/li/showPowerNeededIfOff` | 0.1% (2/2054) | 布尔 | false |
| `comps/li/showProgress` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/showProgressAfterHackCompletion` | 0.2% (5/2054) | 布尔 | false |
| `comps/li/showSleepingZs` | 0.1% (1/2054) | 布尔 | false |
| `comps/li/showToggleGizmo` | 0.3% (6/2054) | 布尔 | true |
| `comps/li/showUseGizmo` | 0.4% (9/2054) | 布尔 | true |
| `comps/li/shutdownMessageKey` | 0.1% (3/2054) | 文本 | AncientHeatVentShutdown / AncientSmokeVentShutdown / AncientToxVentShutdown |
| `comps/li/signalTag` | 0.1% (2/2054) | 文本 | CompCanBeDormant.WakeUp |
| `comps/li/simpleAnimalLabel` | 0.1% (1/2054) | 文本 | chimera |
| `comps/li/size` | 0.2% (5/2054) | 数值 | 1 / 2 / 3 |
| `comps/li/skipIfMechlinkAlreadySentMechs` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/skyColors` | 0.1% (1/2054) | 容器 |  |
| `comps/li/skyColors/overlay` | 0.1% (1/2054) | 文本 | (255, 255, 255) |
| `comps/li/skyColors/saturation` | 0.1% (1/2054) | 数值 | 1.3 |
| `comps/li/skyColors/shadow` | 0.1% (1/2054) | 文本 | (225, 220, 185) |
| `comps/li/skyColors/sky` | 0.1% (1/2054) | 文本 | (255, 230, 200) |
| `comps/li/skyfallerLeaving` | 0.2% (4/2054) | 文本 | DropPodLeaving / DropPodLeavingAncient / DropPodLeavingMechanoid |
| `comps/li/solidTimeSecs` | 0.1% (1/2054) | 数值 | 160 |
| `comps/li/sound` | 1.6% (32/2054) | 文本 | CrashedShipPart_Ambience / FleshmassHeart_Ambience / PsychicAnimalPulserCast |
| `comps/li/soundActivate` | 0.2% (4/2054) | 文本 | FoamTurret_Activate / GravshipShieldGenerator_Activate / PsychicAnimalPulserCast |
| `comps/li/soundAmbientProducingPower` | 0.3% (6/2054) | 文本 | ChemfuelFiredGenerator_Ambience / WaterMill_Ambience / WoodFiredGenerator_Ambience |
| `comps/li/soundDefsPerSpeakerCount` | 0.1% (1/2054) | 容器 |  |
| `comps/li/soundDefsPerSpeakerCount/li` | 0.3% (6/2054) | 文本 | Loudspeaker_Music_1 / Loudspeaker_Music_2 / Loudspeaker_Music_3 |
| `comps/li/soundEmitting` | 0.1% (1/2054) | 文本 | ActivatorProximity_Ambience |
| `comps/li/soundEnd` | 0.2% (5/2054) | 文本 | DeathrestCasket_Exit / GlucosoidPump_Stop / HemogenAmplifier_Stop |
| `comps/li/soundOnEmission` | 0.2% (4/2054) | 文本 | ActivatorCountdown_Ambience / Archonexus_Throb |
| `comps/li/soundOnUsed` | 0.5% (11/2054) | 文本 | DeathrestCapacitySerum_Consume / MechSerumUsed / MechlinkInstalled |
| `comps/li/soundReload` | 0.6% (12/2054) | 文本 | Standard_Reload |
| `comps/li/soundStart` | 0.2% (5/2054) | 文本 | DeathrestCasket_Enter / GlucosoidPump_Start / HemogenAmplifier_Start |
| `comps/li/soundWorking` | 0.4% (8/2054) | 文本 | GlucosoidPump_Ambience / HemogenAmplifier_Ambience / Hemopump_Ambience |
| `comps/li/sourceStreamEffect` | 0.1% (1/2054) | 文本 | BurnbongSmoke |
| `comps/li/spawnablePawnKinds` | 0.4% (8/2054) | 容器 |  |
| `comps/li/spawnablePawnKinds/li` | 1.0% (20/2054) | 文本 | Locust / Megascarab / Megaspider |
| `comps/li/spawnChance` | 0.1% (3/2054) | 数值 | 0.05 |
| `comps/li/spawnCount` | 0.3% (6/2054) | 数值 | 1 / 20 / 32 |
| `comps/li/spawnCountOnSpawn` | 0.1% (2/2054) | 数值 | 10 |
| `comps/li/spawnDays` | 0.1% (1/2054) | 数值 | 8 |
| `comps/li/spawnedMechEffecter` | 0.1% (1/2054) | 文本 | WarUrchinSpawned |
| `comps/li/spawnEffecter` | 0.1% (2/2054) | 文本 | MechDropBeaconActivated / WarqueenWarUrchinsSpawned |
| `comps/li/spawnForbidden` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/spawningPodOffset` | 0.1% (1/2054) | 文本 | (-0.15, 0, -0.55) |
| `comps/li/spawningPodSizeRange` | 0.1% (1/2054) | 文本 | 0.4~0.65 |
| `comps/li/spawnIntervalRange` | 0.3% (6/2054) | 数值/文本 | 120000 / 26000~30000 / 30000~60000 |
| `comps/li/spawnIntervalRange/max` | 0.1% (1/2054) | 数值 | 600000 |
| `comps/li/spawnIntervalRange/min` | 0.1% (1/2054) | 数值 | 600000 |
| `comps/li/spawnKilledLeavings` | 0.1% (2/2054) | 布尔 | true |
| `comps/li/spawnLetterLabelKey` | 0.1% (1/2054) | 文本 | LetterLabelCommsConsoleSpawned |
| `comps/li/spawnLetterTextKey` | 0.1% (1/2054) | 文本 | LetterCommsConsoleSpawned |
| `comps/li/spawnMaxAdjacent` | 0.1% (2/2054) | 数值 | 1 / 40 |
| `comps/li/spawnMessageKey` | 0.1% (1/2054) | 文本 | MessageMechanoidsAssembled |
| `comps/li/spawnMtbHours` | 0.1% (2/2054) | 数值 | 4 |
| `comps/li/spawnOffsetFromCenter` | 0.1% (3/2054) | 文本 | (0.0,0.0,0.0) / (0.5,0.0,-0.5) / (0.5,0.0,0.5) |
| `comps/li/spawnPawnKind` | 0.1% (1/2054) | 文本 | Mech_WarUrchin |
| `comps/li/spawnRadius` | 0.2% (5/2054) | 数值 | 0.2 / 1 / 2.0 |
| `comps/li/spawnSound` | 0.2% (4/2054) | 文本 | AnimaTreeProgress / CryptosleepCasket_Eject / Hive_Spawn |
| `comps/li/splitTransferableFoodKind` | 0.2% (4/2054) | 布尔 | true |
| `comps/li/stackLimit` | 0.4% (9/2054) | 数值 | 1 / 10 / 2 |
| `comps/li/startingGrowthPointsByThreat` | 0.1% (1/2054) | 容器 |  |
| `comps/li/startingGrowthPointsByThreat/points` | 0.1% (1/2054) | 容器 |  |
| `comps/li/startingGrowthPointsByThreat/points/li` | 0.2% (4/2054) | 文本 | (0, 500) / (1600, 1000) / (5000, 1250) |
| `comps/li/startingIngredientCount` | 0.1% (1/2054) | 数值 | 600 |
| `comps/li/startingRange` | 0.1% (3/2054) | 文本 | 0.2~0.4 |
| `comps/li/startingTicksToReset` | 0.1% (1/2054) | 数值 | 36000 |
| `comps/li/startsDormant` | 0.1% (2/2054) | 布尔 | true |
| `comps/li/startTime` | 0.1% (1/2054) | 数值 | 0.25 |
| `comps/li/startupMessageKey` | 0.1% (3/2054) | 文本 | AncientHeatVentStartUp / AncientSmokeVentStartUp / AncientToxVentStartUp |
| `comps/li/startWickHitPointsPercent` | 1.2% (25/2054) | 数值 | 0.15 / 0.166666 / 0.2 |
| `comps/li/startWickOnDamageTaken` | 0.5% (10/2054) | 容器 |  |
| `comps/li/startWickOnDamageTaken/li` | 1.3% (26/2054) | 文本 | Arrow / ArrowHighVelocity / Bullet |
| `comps/li/startWickOnInternalDamageTaken` | 0.1% (1/2054) | 容器 |  |
| `comps/li/startWickOnInternalDamageTaken/li` | 0.1% (1/2054) | 文本 | Deterioration |
| `comps/li/startWithMaxHitPoints` | 0.1% (1/2054) | 布尔 | false |
| `comps/li/statCategoryDef` | 0.1% (1/2054) | 文本 | Building |
| `comps/li/statDef` | 1.2% (25/2054) | 文本 | MeditationFocusStrength |
| `comps/li/statLabel` | 0.1% (1/2054) | 文本 | Learning rate bonus |
| `comps/li/statOffsets` | 0.7% (14/2054) | 容器 |  |
| `comps/li/statOffsets/BedHungerRateFactor` | 0.1% (1/2054) | 数值 | 0.20 |
| `comps/li/statOffsets/BedRestEffectiveness` | 0.1% (1/2054) | 数值 | 0.35 |
| `comps/li/statOffsets/Comfort` | 0.1% (2/2054) | 数值 | 0.05 |
| `comps/li/statOffsets/ContainmentStrength` | 0.2% (4/2054) | 数值 | -15 / -25 / 10 |
| `comps/li/statOffsets/GravshipRange` | 0.1% (2/2054) | 数值 | 10 / 16 |
| `comps/li/statOffsets/ImmunityGainSpeedFactor` | 0.1% (1/2054) | 数值 | 0.02 |
| `comps/li/statOffsets/MedicalTendQualityOffset` | 0.1% (1/2054) | 数值 | 0.07 |
| `comps/li/statOffsets/PsychicRitualQuality` | 0.1% (1/2054) | 数值 | 0.08 |
| `comps/li/statOffsets/ResearchSpeedFactor` | 0.1% (1/2054) | 数值 | 0.1 |
| `comps/li/statOffsets/SubstructureSupport` | 0.1% (1/2054) | 数值 | 250 |
| `comps/li/statOffsets/SurgerySuccessChanceFactor` | 0.1% (1/2054) | 数值 | 0.05 |
| `comps/li/statOffsets/WorkTableWorkSpeedFactor` | 0.1% (1/2054) | 数值 | 0.06 |
| `comps/li/statOffsetsPerQuality` | 0.1% (1/2054) | 容器 |  |
| `comps/li/statOffsetsPerQuality/li` | 0.1% (1/2054) | 容器 |  |
| `comps/li/statOffsetsPerQuality/li/key` | 0.1% (1/2054) | 文本 | PsychicRitualQuality |
| `comps/li/statOffsetsPerQuality/li/value` | 0.1% (1/2054) | 容器 |  |
| `comps/li/statOffsetsPerQuality/li/value/li` | 0.3% (7/2054) | 容器 |  |
| `comps/li/statOffsetsPerQuality/li/value/li/key` | 0.3% (7/2054) | 文本 | Excellent / Good / Legendary |
| `comps/li/statOffsetsPerQuality/li/value/li/value` | 0.3% (7/2054) | 数值 | 0.01 / 0.02 / 0.03 |
| `comps/li/statueBaseGraphic` | 0.1% (1/2054) | 容器 |  |
| `comps/li/statueBaseGraphic/drawSize` | 0.1% (1/2054) | 文本 | (1.5, 1.5) |
| `comps/li/statueBaseGraphic/graphicClass` | 0.1% (1/2054) | 文本 | Graphic_Single |
| `comps/li/statueBaseGraphic/texPath` | 0.1% (1/2054) | 文本 | Things/Building/StatueBase |
| `comps/li/storedEnergyMax` | 0.1% (1/2054) | 数值 | 600 |
| `comps/li/studyAmountToComplete` | 0.1% (2/2054) | 数值 | 2100 / 3200 |
| `comps/li/studyEnabledByDefault` | 0.2% (4/2054) | 布尔 | false |
| `comps/li/studyNotes` | 0.3% (6/2054) | 容器 |  |
| `comps/li/studyNotes/li` | 0.8% (16/2054) | 容器 |  |
| `comps/li/studyNotes/li/label` | 0.8% (16/2054) | 文本 | Monolith study complete / Monolith study progress / Obelisk study complete |
| `comps/li/studyNotes/li/studyKnowledgeAmount` | 0.1% (3/2054) | 数值 | 2.5 / 3 / 4 |
| `comps/li/studyNotes/li/text` | 0.8% (16/2054) | 文本 | Investigation of the obelisk has revealed some information. It is an archotechno / You've learned more about t |
| `comps/li/studyNotes/li/threshold` | 0.6% (12/2054) | 数值 | 10 / 2 / 30 |
| `comps/li/studyNotes/li/thresholdRange` | 0.2% (4/2054) | 文本 | 24~40 / 2~3 / 5~6 |
| `comps/li/subplant` | 0.3% (6/2054) | 文本 | Plant_GrassAnima / Plant_MossGauranlen / Plant_TreeAnima |
| `comps/li/subplantSpawnDays` | 0.1% (1/2054) | 数值 | 1 |
| `comps/li/sustainerActive` | 0.1% (1/2054) | 文本 | ShipReactor_Ambience |
| `comps/li/target` | 0.1% (1/2054) | 文本 | Fire |
| `comps/li/targetChainFastenerTexPath` | 0.1% (2/2054) | 文本 | Things/Building/HoldingPlatform/HoldingPlatform_ChainFastener_StrongOutline |
| `comps/li/targetFuelLevelConfigurable` | 0.2% (4/2054) | 布尔 | true |
| `comps/li/targetingParameters` | 1.3% (26/2054) | 容器 |  |
| `comps/li/targetingParameters/canTargetAnimals` | 1.3% (26/2054) | 布尔 | false |
| `comps/li/targetingParameters/canTargetBuildings` | 1.3% (26/2054) | 布尔 | false |
| `comps/li/targetingParameters/canTargetMechs` | 1.3% (26/2054) | 布尔 | false |
| `comps/li/targetingParameters/onlyTargetControlledPawns` | 1.3% (26/2054) | 布尔 | true |
| `comps/li/teetotalerCanConsume` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/text` | 0.2% (4/2054) | 文本 | You've discovered a fleshbeast dreadmeld! This mammoth creature seems to be made / You've discovered the ancie |
| `comps/li/thickness` | 0.1% (3/2054) | 数值 | 2 / 5 |
| `comps/li/thingDef` | 0.1% (1/2054) | 文本 | Wastepack |
| `comps/li/thingToSpawn` | 0.3% (6/2054) | 文本 | Chemfuel / GlowPod / InsectJelly |
| `comps/li/thought` | 0.1% (1/2054) | 文本 | AnimaScream |
| `comps/li/ticksBetweenDamage` | 0.2% (4/2054) | 数值 | 60 / 6000 |
| `comps/li/ticksHealthy` | 0.1% (1/2054) | 数值 | 60000 |
| `comps/li/ticksNeedsMaintenance` | 0.1% (1/2054) | 数值 | 60000 |
| `comps/li/ticksPerAtomize` | 0.1% (1/2054) | 数值 | 30000 |
| `comps/li/ticksPerHeal` | 0.3% (6/2054) | 数值 | 2000 / 6000 |
| `comps/li/ticksSinceLastEmittedMaxOffset` | 0.1% (1/2054) | 数值 | 17 |
| `comps/li/ticksToActivate` | 0.9% (19/2054) | 数值 | 180 / 2500 / 3600 |
| `comps/li/ticksToRecharge` | 0.1% (1/2054) | 数值 | 60000 |
| `comps/li/tilePollutionPerDissolution` | 0.1% (1/2054) | 数值 | 0.0005 |
| `comps/li/tilingChainTexPath` | 0.1% (2/2054) | 文本 | Things/Building/HoldingPlatform/HoldingPlatform_EntityChain_StrongOutline / Things/Building/HoldingPlatform/Ho |
| `comps/li/timeDamageCurve` | 0.1% (1/2054) | 容器 |  |
| `comps/li/timeDamageCurve/points` | 0.1% (1/2054) | 容器 |  |
| `comps/li/timeDamageCurve/points/li` | 0.1% (2/2054) | 文本 | (0, 10) / (60, 40) |
| `comps/li/tooltipOverride` | 0.1% (2/2054) | 文本 | Drones have limited battery life. When the battery runs dry, the drone dies. / This turret has a limited batte |
| `comps/li/totalPowerTicks` | 0.1% (3/2054) | 数值 | 12500 / 15000 |
| `comps/li/transmitsPower` | 1.2% (24/2054) | 布尔 | true |
| `comps/li/triggeredMessage` | 0.1% (1/2054) | 文本 | A {0_labelShort} has emerged from a mech vat. |
| `comps/li/triggerRadiusRange` | 0.1% (1/2054) | 文本 | 3~8 |
| `comps/li/triggerSound` | 0.1% (1/2054) | 文本 | GestatorGlassShattered |
| `comps/li/tryAvoidSludge` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/tunedEffect` | 0.1% (1/2054) | 文本 | BandNodeTuned |
| `comps/li/tuningCompleteSound` | 0.1% (1/2054) | 文本 | BandNodeTuning_Complete |
| `comps/li/tuningEffect` | 0.1% (1/2054) | 文本 | BandNodeTuning |
| `comps/li/turretDef` | 0.1% (3/2054) | 文本 | Gun_ChargeBlasterTurret |
| `comps/li/type` | 0.1% (1/2054) | 文本 | ToxGas |
| `comps/li/unhackedGraphicData` | 0.1% (3/2054) | 容器 |  |
| `comps/li/unhackedGraphicData/drawSize` | 0.1% (2/2054) | 文本 | (2, 2) / (5, 5) |
| `comps/li/unhackedGraphicData/graphicClass` | 0.1% (3/2054) | 文本 | Graphic_Multi |
| `comps/li/unhackedGraphicData/texPath` | 0.1% (3/2054) | 文本 | Things/Building/Ancient/BlastDoor/AncientBlastDoor_HackingTerminal / Things/Building/Ancient/GravReactor/Ancie |
| `comps/li/unhackedGraphicOffset` | 0.1% (1/2054) | 文本 | (0,0.05,0) |
| `comps/li/unlockedChance` | 0.1% (1/2054) | 数值 | 0.3 |
| `comps/li/unlockedLetterLabelKey` | 0.1% (2/2054) | 文本 | LetterLabelBossgroupCallerUnlocked |
| `comps/li/unlockedLetterTextKey` | 0.1% (2/2054) | 文本 | LetterBossgroupCallerUnlocked |
| `comps/li/unstableInspectText` | 0.1% (1/2054) | 文本 | Unstable: cannot be suppressed |
| `comps/li/unstableWarning` | 0.1% (1/2054) | 文本 | Warning: the nociosphere will resist suppression in {0} days. |
| `comps/li/untetheredGraphicTexPath` | 0.1% (2/2054) | 文本 | Things/Building/HoldingPlatform/HoldingPlatform_ChainsUntethered / Things/Building/HoldingPlatform/HoldingPlat |
| `comps/li/untunedEffect` | 0.1% (1/2054) | 文本 | BandNodeUntuned |
| `comps/li/useDuration` | 0.4% (9/2054) | 数值 | 0 / 132 / 300 |
| `comps/li/useJob` | 1.1% (23/2054) | 文本 | Ingest / InstallMechlink / SmashThing |
| `comps/li/useLabel` | 1.1% (23/2054) | 文本 | Implant sublink / Install {0_label} to become mechanitor / Smash {0_label} |
| `comps/li/useLargeEMPEffecter` | 0.5% (10/2054) | 布尔 | true |
| `comps/li/useMessage` | 0.1% (1/2054) | 文本 | {PAWN_nameDef} smashed the revenant spine. It dissolved to reveal a shard of dar |
| `comps/li/useParentRotation` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/userMustHaveHediff` | 0.3% (6/2054) | 文本 | MechlinkImplant |
| `comps/li/useStackCountAsFactor` | 0.1% (1/2054) | 布尔 | true |
| `comps/li/velocityX` | 0.2% (5/2054) | 文本 | -40~40 / -50~50 / 0.3~0.7 |
| `comps/li/velocityY` | 0.2% (5/2054) | 文本 | 0.5~1 / 0.5~1.8 / 0.7~1.0 |
| `comps/li/verticalGraphic` | 0.2% (5/2054) | 容器 |  |
| `comps/li/verticalGraphic/addTopAltitudeBias` | 0.2% (5/2054) | 布尔 | true |
| `comps/li/verticalGraphic/graphicClass` | 0.2% (5/2054) | 文本 | Graphic_Multi |
| `comps/li/verticalGraphic/texPath` | 0.2% (5/2054) | 文本 | Things/Item/Book/Novel/Novel_Vertical / Things/Item/Book/Schematic/Schematic_Vertical / Things/Item/Book/Textb |
| `comps/li/wakeUpCheckRadius` | 0.2% (5/2054) | 数值 | 2.9 / 30 / 4.9 |
| `comps/li/wakeUpDelayRange` | 0.1% (3/2054) | 数值/文本 | 100~200 / 162 |
| `comps/li/wakeUpDelayStateLabelKey` | 0.1% (1/2054) | 文本 | DormantCompOpening |
| `comps/li/wakeUpEffect` | 0.1% (1/2054) | 文本 | CocoonWakingUp |
| `comps/li/wakeUpIfAnyTargetClose` | 0.1% (3/2054) | 布尔 | true |
| `comps/li/wakeUpOnDamage` | 0.2% (5/2054) | 布尔 | true |
| `comps/li/wakeUpOnThingConstructedRadius` | 0.1% (2/2054) | 数值 | 0 / 4.9 |
| `comps/li/wakeUpRepeatSignalDelayRange` | 0.1% (1/2054) | 文本 | 30~60 |
| `comps/li/wakeUpSound` | 0.7% (14/2054) | 文本 | MechanoidsWakeUp |
| `comps/li/wakeUpTargetingParams` | 0.1% (3/2054) | 容器 |  |
| `comps/li/wakeUpTargetingParams/canTargetAnimals` | 0.1% (3/2054) | 布尔 | false |
| `comps/li/wakeUpTargetingParams/canTargetBuildings` | 0.1% (3/2054) | 布尔 | false |
| `comps/li/wakeUpTargetingParams/canTargetHumans` | 0.1% (3/2054) | 布尔 | true |
| `comps/li/wakeUpTargetingParams/canTargetMechs` | 0.1% (3/2054) | 布尔 | false |
| `comps/li/wakeUpWithDelay` | 0.1% (3/2054) | 布尔 | true |
| `comps/li/warmupEffecter` | 0.1% (1/2054) | 文本 | BiomutationPulserWarmup |
| `comps/li/warmupMote` | 0.1% (1/2054) | 文本 | Mote_ResurrectAbility |
| `comps/li/warmupPulseFadeInTime` | 0.1% (1/2054) | 数值 | 0.12 |
| `comps/li/warmupPulseFadeOutTime` | 0.1% (1/2054) | 数值 | 0.6 |
| `comps/li/warmupPulseSolidTime` | 0.1% (1/2054) | 数值 | 0.15 |
| `comps/li/warmupSound` | 0.2% (4/2054) | 文本 | BiomutationPulserWarmup / PsychicArtifactWarmupSustained / PsychicSoothePulserWarmupSustained |
| `comps/li/warning` | 0.1% (1/2054) | 数值 | 0.9 |
| `comps/li/waterTilePollutionFactor` | 0.1% (1/2054) | 数值 | 8 |
| `comps/li/weaponCategories` | 0.6% (13/2054) | 容器 |  |
| `comps/li/weaponCategories/li` | 3.5% (71/2054) | 文本 | BulletFiring / Gun / Pistol |
| `comps/li/wickMessages` | 0.1% (2/2054) | 容器 |  |
| `comps/li/wickMessages/li` | 0.2% (4/2054) | 容器 |  |
| `comps/li/wickMessages/li/messageType` | 0.2% (4/2054) | 文本 | NeutralEvent / ThreatBig |
| `comps/li/wickMessages/li/ticksLeft` | 0.2% (4/2054) | 数值 | 1200 / 1800 / 589 |
| `comps/li/wickMessages/li/wickMessagekey` | 0.2% (4/2054) | 文本 | MessageAboutToExplode / SelfDestructCountdown |
| `comps/li/wickTicks` | 2.0% (42/2054) | 数值/文本 | 15 / 240 / 30~60 |
| `comps/li/width` | 0.1% (2/2054) | 数值 | 0.2 / 8 |
| `comps/li/withSideEffects` | 0.1% (1/2054) | 布尔 | false |
| `comps/li/woolAmount` | 0.3% (7/2054) | 数值 | 120 / 200 / 45 |
| `comps/li/woolDef` | 0.3% (7/2054) | 文本 | WoolAlpaca / WoolBison / WoolMuffalo |
| `comps/li/workerClass` | 0.1% (3/2054) | 文本 | NociosphereActivityWorker / ObeliskActivityWorker / PawnActivityWorker |
| `comps/li/workingEffecter` | 0.1% (1/2054) | 文本 | WastepackAtomizer_Working |
| `comps/li/workSpeedStat` | 0.2% (5/2054) | 文本 | ResearchSpeedFactor / WorkTableWorkSpeedFactor |
| `comps/li/worldObjectDef` | 0.1% (1/2054) | 文本 | PassengerShuttle |
| `comps/li/worldRange` | 0.5% (11/2054) | 数值 | 0 / 1 / 10 |
| `comps/li/writeTimeLeftToSpawn` | 0.2% (4/2054) | 布尔 | true |
| `constructEffect` | 1.4% (29/2054) | 文本 | ConstructDirt / ConstructMetal / ConstructWood |
| `constructionSkillPrerequisite` | 5.0% (102/2054) | 数值 | 4 / 5 / 6 |
| `containedItemsSelectable` | 0.1% (3/2054) | 布尔 | true |
| `containedPawnsSelectable` | 0.6% (13/2054) | 布尔 | true |
| `costList` | 17.0% (350/2054) | 容器 |  |
| `costList/AIPersonaCore` | 0.1% (1/2054) | 数值 | 1 |
| `costList/Bioferrite` | 1.7% (34/2054) | 数值 | 10 / 20 / 35 |
| `costList/BlocksVacstone` | 0.1% (2/2054) | 数值 | 5 / 50 |
| `costList/BroadshieldCore` | 0.1% (3/2054) | 数值 | 1 |
| `costList/Chemfuel` | 0.8% (17/2054) | 数值 | 10 / 140 / 20 |
| `costList/Cloth` | 0.5% (10/2054) | 数值 | 3 / 30 / 50 |
| `costList/ComponentIndustrial` | 8.4% (173/2054) | 数值 | 1 / 2 / 4 |
| `costList/ComponentSpacer` | 3.2% (65/2054) | 数值 | 2 / 3 / 4 |
| `costList/Gold` | 0.6% (13/2054) | 数值 | 20 / 4 / 50 |
| `costList/Gravcore` | 0.1% (3/2054) | 数值 | 1 |
| `costList/GravlitePanel` | 0.4% (9/2054) | 数值 | 15 / 35 / 40 |
| `costList/HemogenPack` | 0.2% (4/2054) | 数值 | 5 |
| `costList/Meat_Human` | 0.1% (1/2054) | 数值 | 120 |
| `costList/Meat_Twisted` | 0.2% (5/2054) | 数值 | 10 / 20 / 30 |
| `costList/MedicineHerbal` | 0.1% (1/2054) | 数值 | 1 |
| `costList/NanostructuringChip` | 0.2% (4/2054) | 数值 | 1 / 2 |
| `costList/Neutroamine` | 0.3% (6/2054) | 数值 | 1 / 2 |
| `costList/Plasteel` | 4.0% (82/2054) | 数值 | 100 / 15 / 25 |
| `costList/PowerfocusChip` | 0.2% (5/2054) | 数值 | 1 |
| `costList/PsychoidLeaves` | 0.1% (3/2054) | 数值 | 4 / 8 |
| `costList/RawFungus` | 0.1% (1/2054) | 数值 | 20 |
| `costList/RevenantSpine` | 0.1% (1/2054) | 数值 | 1 |
| `costList/Shard` | 0.7% (14/2054) | 数值 | 1 / 2 |
| `costList/Shell_AntigrainWarhead` | 0.1% (1/2054) | 数值 | 1 |
| `costList/Shell_Deadlife` | 0.1% (1/2054) | 数值 | 2 |
| `costList/Shell_EMP` | 0.1% (1/2054) | 数值 | 2 |
| `costList/Shell_Firefoam` | 0.1% (1/2054) | 数值 | 2 |
| `costList/Shell_HighExplosive` | 0.1% (1/2054) | 数值 | 2 |
| `costList/Shell_Incendiary` | 0.1% (1/2054) | 数值 | 2 |
| `costList/Shell_Smoke` | 0.1% (1/2054) | 数值 | 2 |
| `costList/Shell_Toxic` | 0.1% (1/2054) | 数值 | 2 |
| `costList/ShuttleEngine` | 0.1% (2/2054) | 数值 | 1 |
| `costList/SignalChip` | 0.2% (4/2054) | 数值 | 1 / 2 |
| `costList/Skull` | 0.1% (1/2054) | 数值 | 1 |
| `costList/SmokeleafLeaves` | 0.1% (3/2054) | 数值 | 150 / 25 / 4 |
| `costList/Steel` | 10.0% (206/2054) | 数值 | 15 / 150 / 25 |
| `costList/Uranium` | 0.4% (9/2054) | 数值 | 14 / 5 / 60 |
| `costList/WoodLog` | 1.2% (25/2054) | 数值 | 15 / 20 / 25 |
| `costList/Yayo` | 0.1% (1/2054) | 数值 | 1 |
| `costListForDifficulty` | 0.3% (7/2054) | 容器 |  |
| `costListForDifficulty/costList` | 0.3% (7/2054) | 容器 |  |
| `costListForDifficulty/costList/Chemfuel` | 0.1% (3/2054) | 数值 | 15 / 20 |
| `costListForDifficulty/costList/ComponentIndustrial` | 0.1% (2/2054) | 数值 | 2 / 6 |
| `costListForDifficulty/costList/ReinforcedBarrel` | 0.1% (1/2054) | 数值 | 1 |
| `costListForDifficulty/costList/Steel` | 0.3% (6/2054) | 数值 | 15 / 20 / 25 |
| `costListForDifficulty/costStuffCount` | 0.1% (1/2054) | 数值 | 50 |
| `costListForDifficulty/difficultyVar` | 0.3% (7/2054) | 文本 | classicMortars |
| `costListForDifficulty/invert` | 0.1% (1/2054) | 布尔 | true |
| `costStuffCount` | 8.4% (172/2054) | 数值 | 20 / 25 / 70 |
| `coversFloor` | 0.3% (7/2054) | 布尔 | false / true |
| `damageMultipliers` | 0.5% (11/2054) | 容器 |  |
| `damageMultipliers/li` | 0.6% (12/2054) | 容器 |  |
| `damageMultipliers/li/damageDef` | 0.6% (12/2054) | 文本 | Bomb / Flame / Thump |
| `damageMultipliers/li/multiplier` | 0.6% (12/2054) | 数值 | 0 / 2 / 4 |
| `deepCommonality` | 0.3% (6/2054) | 数值 | 0.5 / 1 / 4 |
| `deepCountPerPortion` | 0.3% (6/2054) | 数值 | 10 / 45 / 70 |
| `deepLumpSizeRange` | 0.3% (6/2054) | 文本 | 1~4 / 20~30 / 2~10 |
| `defaultPlacingRot` | 3.7% (76/2054) | 文本 | East / North / South |
| `defaultStuff` | 0.1% (1/2054) | 文本 | BlocksGranite |
| `defName` | 88.2% (1811/2054) | 文本 | Bullet_Heatspike / Spike_Fingerspike / Spike_Toughspike |
| `description` | 64.6% (1326/2054) | 文本 | A book which explores dark psychic powers, the void hidden under space, and the  / A number of barbed bioferri |
| `descriptionHyperlinks` | 6.1% (126/2054) | 容器 |  |
| `descriptionHyperlinks/HediffDef` | 2.2% (46/2054) | 文本 | ControlSublinkImplant / MechFormfeederImplant / MechlinkImplant |
| `descriptionHyperlinks/RecipeDef` | 3.0% (62/2054) | 文本 | InstallAdrenalHeart / InstallCorrosiveHeart / InstallGhoulBarbs |
| `descriptionHyperlinks/ThingDef` | 3.3% (67/2054) | 文本 | BioferriteHarvester / ElectricInhibitor / Electroharvester |
| `deselectedSelectionBracketFactor` | 0.1% (1/2054) | 数值 | 0.3 |
| `designateHaulable` | 0.1% (2/2054) | 布尔 | false / true |
| `designationCategory` | 8.1% (166/2054) | 容器/文本 | Anomaly / Biotech / Furniture |
| `designationHotKey` | 4.8% (98/2054) | 文本 | Misc1 / Misc11 / Misc12 |
| `destroyable` | 1.4% (28/2054) | 布尔 | false |
| `destroyOnDrop` | 0.6% (12/2054) | 布尔 | True / true |
| `deteriorateFromEnvironmentalEffects` | 0.1% (1/2054) | 布尔 | false |
| `devNote` | 2.6% (53/2054) | 文本 | chicken-1 / cow-1 / squirrel-1 |
| `displayNumbersBetweenSameDefDistRange` | 0.1% (1/2054) | 文本 | 9~25 |
| `dominantStyleCategory` | 0.5% (10/2054) | 文本 | Morbid / Rustic / Spikecore |
| `dontPrint` | 0.1% (3/2054) | 布尔 | true |
| `drawDamagedOverlay` | 0.1% (1/2054) | 布尔 | false |
| `drawerType` | 7.9% (163/2054) | 文本 | MapMeshAndRealTime / MapMeshOnly / None |
| `drawGUIOverlay` | 1.9% (39/2054) | 布尔 | True / false / true |
| `drawGUIOverlayQuality` | 0.1% (1/2054) | 布尔 | false |
| `drawHighlight` | 0.6% (13/2054) | 布尔 | true |
| `drawHighlightOnlyForHostile` | 0.5% (10/2054) | 布尔 | true |
| `drawOffscreen` | 1.8% (38/2054) | 布尔 | true |
| `drawPlaceWorkersWhileInstallBlueprintSelected` | 0.1% (2/2054) | 布尔 | true |
| `drawPlaceWorkersWhileSelected` | 2.5% (51/2054) | 布尔 | True / false / true |
| `drawStyleCategory` | 0.2% (5/2054) | 文本 | Conduits / Defenses / Walls |
| `dropPodActive` | 0.1% (2/2054) | 文本 | ActiveDropPodAncient / ActiveDropPodMechanoid |
| `dropPodFaller` | 0.1% (2/2054) | 文本 | DropPodIncomingAncient / DropPodIncomingMechanoidSoft |
| `equipmentType` | 0.1% (3/2054) | 文本 | Primary |
| `equippedAngleOffset` | 1.1% (23/2054) | 数值 | -150 / -20 / -25 |
| `equippedDistanceOffset` | 0.1% (2/2054) | 数值 | -0.14 |
| `equippedStatOffsets` | 3.2% (66/2054) | 容器 |  |
| `equippedStatOffsets/EntityStudyRate` | 0.1% (1/2054) | 数值 | 0.1 |
| `equippedStatOffsets/Flammability` | 0.1% (1/2054) | 数值 | -0.68 |
| `equippedStatOffsets/MechBandwidth` | 0.4% (8/2054) | 数值 | 12 / 3 / 6 |
| `equippedStatOffsets/MechControlGroups` | 0.1% (1/2054) | 数值 | 1 |
| `equippedStatOffsets/MeleeHitChance` | 0.1% (2/2054) | 数值 | -0.5 |
| `equippedStatOffsets/MoveSpeed` | 0.5% (11/2054) | 数值 | -0.12 / -0.25 / -0.4 |
| `equippedStatOffsets/PainShockThreshold` | 0.1% (3/2054) | 数值 | 0.05 / 0.10 / 0.15 |
| `equippedStatOffsets/PsychicEntropyRecoveryRate` | 0.6% (12/2054) | 数值 | 0.033 / 0.05 / 0.066 |
| `equippedStatOffsets/PsychicSensitivity` | 0.3% (7/2054) | 数值 | -0.90 / 0.05 |
| `equippedStatOffsets/PsychicSensitivityOffset` | 0.3% (6/2054) | 数值 | 0.10 / 0.15 / 0.20 |
| `equippedStatOffsets/RangedCooldownFactor` | 0.1% (1/2054) | 数值 | -0.2 |
| `equippedStatOffsets/ResearchSpeed` | 0.1% (1/2054) | 数值 | 0.05 |
| `equippedStatOffsets/ShootingAccuracyPawn` | 0.1% (3/2054) | 数值 | -5 / 3 |
| `equippedStatOffsets/SlaveSuppressionOffset` | 1.3% (26/2054) | 数值 | -0.05 / -0.1 / -0.3 |
| `equippedStatOffsets/SocialImpact` | 0.4% (9/2054) | 数值 | 0.1 / 0.10 / 0.15 |
| `equippedStatOffsets/SuppressionPower` | 0.1% (1/2054) | 数值 | 0.1 |
| `equippedStatOffsets/ToxicEnvironmentResistance` | 0.2% (5/2054) | 数值 | 0.2 / 0.35 / 0.5 |
| `equippedStatOffsets/VacuumResistance` | 0.6% (13/2054) | 数值 | 0 / 0.3 / 0.65 |
| `equippedStatOffsets/WorkSpeedGlobalOffsetMech` | 0.1% (1/2054) | 数值 | 0.12 |
| `fertility` | 0.5% (10/2054) | 数值 | 0 / 1.0 / 2.8 |
| `fillPercent` | 17.7% (363/2054) | 数值 | 0.3 / 0.4 / 0.75 |
| `filth` | 2.0% (41/2054) | 容器 |  |
| `filth/allowsFire` | 0.1% (2/2054) | 布尔 | false |
| `filth/canFilthAttach` | 1.5% (31/2054) | 布尔 | false / true |
| `filth/cleaningSound` | 1.7% (34/2054) | 文本 | Interact_CleanFilth / Interact_CleanFilth_Dirt / Interact_CleanFilth_Fluid |
| `filth/cleaningWorkToReduceThickness` | 1.9% (40/2054) | 数值 | 160 / 2000 / 70 |
| `filth/disappearsInDays` | 1.9% (39/2054) | 文本 | 10~15 / 35~40 / 45~50 |
| `filth/ignoreFilthMultiplierStat` | 1.0% (21/2054) | 布尔 | true |
| `filth/maxThickness` | 0.5% (10/2054) | 数值 | 1 / 5 |
| `filth/placementMask` | 0.3% (6/2054) | 容器 |  |
| `filth/placementMask/li` | 0.4% (9/2054) | 文本 | Terrain / Unnatural |
| `filth/rainWashes` | 1.1% (23/2054) | 布尔 | false / true |
| `filthLeaving` | 0.6% (13/2054) | 文本 | Filth_Fleshmass / Filth_MachineBits / Filth_RubbleBuilding |
| `forceDebugSpawnable` | 0.6% (12/2054) | 布尔 | true |
| `forceLeavingsAllowed` | 0.1% (2/2054) | 布尔 | true |
| `forceMoveItemsBeforeConstruction` | 0.1% (1/2054) | 布尔 | true |
| `generateAllowChance` | 1.0% (20/2054) | 数值 | 0 / 0.15 |
| `generateCommonality` | 0.8% (17/2054) | 数值 | 0.3 / 0.5 / 2 |
| `genericMarketSellable` | 1.0% (20/2054) | 布尔 | false / true |
| `graphicData` | 75.2% (1545/2054) | 容器 |  |
| `graphicData/addTopAltitudeBias` | 0.5% (11/2054) | 布尔 | true |
| `graphicData/allowFlip` | 0.2% (4/2054) | 布尔 | false |
| `graphicData/asymmetricLink` | 0.1% (1/2054) | 容器 |  |
| `graphicData/asymmetricLink/drawDoorBorderEast` | 0.1% (1/2054) | 容器 |  |
| `graphicData/asymmetricLink/drawDoorBorderEast/color` | 0.1% (1/2054) | 文本 | (0,0,0) |
| `graphicData/asymmetricLink/drawDoorBorderEast/offset` | 0.1% (1/2054) | 文本 | (0.5, 0, -0.08) |
| `graphicData/asymmetricLink/drawDoorBorderEast/size` | 0.1% (1/2054) | 文本 | (0.04, 0.77) |
| `graphicData/asymmetricLink/drawDoorBorderWest` | 0.1% (1/2054) | 容器 |  |
| `graphicData/asymmetricLink/drawDoorBorderWest/color` | 0.1% (1/2054) | 文本 | (0,0,0) |
| `graphicData/asymmetricLink/drawDoorBorderWest/offset` | 0.1% (1/2054) | 文本 | (-0.5, 0, -0.08) |
| `graphicData/asymmetricLink/drawDoorBorderWest/size` | 0.1% (1/2054) | 文本 | (0.04, 0.77) |
| `graphicData/asymmetricLink/linkFlags` | 0.1% (1/2054) | 容器 |  |
| `graphicData/asymmetricLink/linkFlags/li` | 0.1% (2/2054) | 文本 | Rock / Wall |
| `graphicData/asymmetricLink/linkToDoors` | 0.1% (1/2054) | 布尔 | true |
| `graphicData/color` | 10.6% (218/2054) | 文本 | (0, 0, 0, .5) / (171, 27, 17, 120) / (171, 27, 17, 170) |
| `graphicData/colorTwo` | 0.4% (8/2054) | 文本 | (147,144,134) / (155,133,107) / (187,173,25) |
| `graphicData/cornerOverlayPath` | 0.1% (1/2054) | 文本 | Things/Building/Linked/FleshmassPiece |
| `graphicData/damageData` | 7.9% (163/2054) | 容器 |  |
| `graphicData/damageData/cornerBL` | 2.1% (44/2054) | 文本 | Damage/Corner |
| `graphicData/damageData/cornerBR` | 2.2% (46/2054) | 文本 | Damage/Corner |
| `graphicData/damageData/cornerTL` | 2.3% (47/2054) | 文本 | Damage/Corner |
| `graphicData/damageData/cornerTR` | 2.4% (49/2054) | 文本 | Damage/Corner |
| `graphicData/damageData/edgeBot` | 0.1% (2/2054) | 文本 | Damage/Edge |
| `graphicData/damageData/edgeLeft` | 0.1% (2/2054) | 文本 | Damage/Edge |
| `graphicData/damageData/edgeRight` | 0.1% (2/2054) | 文本 | Damage/Edge |
| `graphicData/damageData/edgeTop` | 0.1% (2/2054) | 文本 | Damage/Edge |
| `graphicData/damageData/enabled` | 0.6% (13/2054) | 布尔 | false |
| `graphicData/damageData/rect` | 5.0% (103/2054) | 文本 | (0.15, 0.15, 0.7, 0.7) / (0.15, 0.15, 0.75, 0.75) / (0.2,0.2,0.6,0.6) |
| `graphicData/damageData/rectE` | 0.4% (8/2054) | 文本 | (0,0,0.84375,0.625) / (0.234375,0.296875,0.5,0.546875) / (0.28125,0.25,0.453125,0.25) |
| `graphicData/damageData/rectN` | 0.4% (8/2054) | 文本 | (0,0,1,0.703125) / (0.1, 0.3, 1.8, 0.5) / (0.125,0.296875,0.734375,0.421875) |
| `graphicData/damageData/rectS` | 0.4% (8/2054) | 文本 | (0.09375,0,0.84375,1) / (0.1, 0.3, 1.8, 0.5) / (0.125,0.296875,0.734375,0.421875) |
| `graphicData/damageData/rectW` | 0.4% (8/2054) | 文本 | (0.15625,0,0.84375,0.625) / (0.234375,0.296875,0.5,0.546875) / (0.28125,0.25,0.453125,0.25) |
| `graphicData/damageData/scratches` | 0.2% (5/2054) | 容器 |  |
| `graphicData/damageData/scratches/li` | 0.7% (15/2054) | 文本 | Damage/FleshScratch1 / Damage/FleshScratch2 / Damage/FleshScratch3 |
| `graphicData/drawOffset` | 1.6% (32/2054) | 文本 | (0, 0, 0.5) / (0, 0.02, 0) / (0,0,0.3) |
| `graphicData/drawOffsetEast` | 0.2% (5/2054) | 文本 | (0.9,0,0) |
| `graphicData/drawOffsetNorth` | 0.4% (8/2054) | 文本 | (0,0,0.08) / (0,0,0.2) / (0,0,0.25) |
| `graphicData/drawOffsetSouth` | 0.3% (6/2054) | 文本 | (0,0,-0.9) / (0,0,0.2) |
| `graphicData/drawOffsetWest` | 0.2% (5/2054) | 文本 | (-0.9,0,0) |
| `graphicData/drawRotated` | 0.6% (13/2054) | 布尔 | False / false |
| `graphicData/drawSize` | 35.4% (726/2054) | 数值/文本 | (1.4, 1.4) / (1.5, 3) / 0.8 |
| `graphicData/flipExtraRotation` | 0.1% (1/2054) | 数值 | 80 |
| `graphicData/graphicClass` | 57.6% (1183/2054) | 文本 | Graphic_MoteRandom / Graphic_MoteWithAgeSecs / Graphic_Random |
| `graphicData/ignoreThingDrawColor` | 0.1% (2/2054) | 布尔 | true |
| `graphicData/linkFlags` | 0.6% (13/2054) | 容器 |  |
| `graphicData/linkFlags/li` | 0.9% (18/2054) | 文本 | Fleshmass / MapEdge / Rock |
| `graphicData/linkType` | 0.6% (13/2054) | 文本 | Basic / CornerFiller / CornerOverlay |
| `graphicData/maxSnS` | 0.1% (2/2054) | 文本 | (.9, .95) |
| `graphicData/offsetSnS` | 0.1% (2/2054) | 文本 | (.5, -.45) |
| `graphicData/onGroundRandomRotateAngle` | 0.4% (8/2054) | 数值 | 35 / 360 |
| `graphicData/renderInstanced` | 0.2% (4/2054) | 布尔 | false / true |
| `graphicData/renderQueue` | 0.1% (2/2054) | 数值 | 4000 |
| `graphicData/shaderParameters` | 5.6% (115/2054) | 容器 |  |
| `graphicData/shaderParameters/_AgeScalarNoise` | 0.1% (1/2054) | 文本 | /Things/Mote/IncineratorBeamAgeNoise |
| `graphicData/shaderParameters/_ageToNoiseRatio` | 0.1% (1/2054) | 数值 | 0 |
| `graphicData/shaderParameters/_AmbientShake` | 0.1% (2/2054) | 数值 | .05 |
| `graphicData/shaderParameters/_BrightnessMultiplier` | 0.1% (1/2054) | 数值 | 1.1 |
| `graphicData/shaderParameters/_brightnessMultiplier` | 1.0% (21/2054) | 数值 | 1.15 / 1.3 / 1.5 |
| `graphicData/shaderParameters/_ChangeSpeed` | 0.1% (2/2054) | 数值 | 0.5 |
| `graphicData/shaderParameters/_Delay` | 0.1% (1/2054) | 数值 | 0.8 |
| `graphicData/shaderParameters/_desaturationIntensity` | 0.1% (1/2054) | 数值 | 0.8 |
| `graphicData/shaderParameters/_Detail` | 0.1% (2/2054) | 数值 | 2 |
| `graphicData/shaderParameters/_DetailDistortion` | 0.1% (2/2054) | 数值 | 0.1 / 0.3 |
| `graphicData/shaderParameters/_detailIntensity` | 0.1% (3/2054) | 数值 | 1.3 |
| `graphicData/shaderParameters/_DetailOffset` | 0.1% (2/2054) | 文本 | (0.1, 0.0) / (0.345, 0.0) |
| `graphicData/shaderParameters/_DetailScale` | 0.1% (3/2054) | 数值 | 0.75 / 0.9 / 1.25 |
| `graphicData/shaderParameters/_DetailScrollSpeed` | 0.1% (1/2054) | 文本 | (0.0, 0.25, 0) |
| `graphicData/shaderParameters/_detailScrollSpeed` | 0.1% (2/2054) | 文本 | (0.15, 0.15, 0) / (0.2, 0.0, 0) |
| `graphicData/shaderParameters/_DetailTex` | 0.2% (4/2054) | 文本 | /Things/Mote/Electicity / /Things/Mote/Speckles / /Things/Mote/SubcoreEncoder_Detail |
| `graphicData/shaderParameters/_DissolveTex` | 0.1% (2/2054) | 文本 | /Things/Building/VoidNode/Core_m |
| `graphicData/shaderParameters/_Distortion` | 0.3% (6/2054) | 数值 | 0.6 / 1 |
| `graphicData/shaderParameters/_DistortionIntensity` | 0.3% (7/2054) | 数值 | 0.08 / 0.12 / 0.5 |
| `graphicData/shaderParameters/_distortionIntensity` | 1.3% (27/2054) | 数值 | 0 / 0.025 / 0.12 |
| `graphicData/shaderParameters/_DistortionScale` | 0.4% (8/2054) | 数值 | 0.082 / 0.1 / 0.5 |
| `graphicData/shaderParameters/_distortionScale` | 0.1% (3/2054) | 数值 | 0.1 / 25 / 40 |
| `graphicData/shaderParameters/_DistortionScrollSpeed` | 0.1% (3/2054) | 文本 | (0.25, 0.25) / (0.3, 0.75, 0) / (1.35, 1.35) |
| `graphicData/shaderParameters/_distortionScrollSpeed` | 0.1% (1/2054) | 文本 | (0.07, 0.07, 0.0) |
| `graphicData/shaderParameters/_DistortionSpeed` | 0.1% (1/2054) | 数值 | 1 |
| `graphicData/shaderParameters/_DistortionTex` | 1.3% (26/2054) | 文本 | /Things/Mote/Cloudy_C / /Things/Mote/PsychicDistortionCurrents / /Things/Mote/RadiationDistortion_A |
| `graphicData/shaderParameters/_distortionTint` | 0.4% (8/2054) | 文本 | (.5, .5, .5, 0) / (0.15, 0, 0, 0) / (0.23, 0, 0, 0) |
| `graphicData/shaderParameters/_DustTex` | 0.1% (2/2054) | 文本 | /Things/Building/VoidNode/InternalDust |
| `graphicData/shaderParameters/_ExtraTex` | 0.1% (2/2054) | 文本 | /Things/Mote/RitualEffects/GlowRays / /Weather/Overlays/FlashstormPsychicExtra |
| `graphicData/shaderParameters/_ExtraTexA` | 0.1% (2/2054) | 文本 | /Things/Mote/BeamSecondaryNoise_A |
| `graphicData/shaderParameters/_ExtraTexB` | 0.1% (2/2054) | 文本 | /Things/Mote/BeamSecondaryNoise_B |
| `graphicData/shaderParameters/_FadeTex` | 0.1% (1/2054) | 文本 | /Things/Mote/PollutionWave |
| `graphicData/shaderParameters/_FallBehaviorEnabled` | 0.1% (1/2054) | 数值 | 1 |
| `graphicData/shaderParameters/_FallColorDestination` | 0.1% (1/2054) | 文本 | /Other/TreeFallGradient |
| `graphicData/shaderParameters/_FallColorSource` | 0.1% (3/2054) | 文本 | (0.373, 0.427, 0.313) / (0.3803, 0.4352, 0.1451) |
| `graphicData/shaderParameters/_FallTransitionRange` | 0.1% (3/2054) | 文本 | (0.02, 0.10) / (0.02, 0.14) |
| `graphicData/shaderParameters/_FlameTex` | 0.1% (3/2054) | 文本 | /Things/Mote/Candles/CandleFlame |
| `graphicData/shaderParameters/_FlickerAmount` | 0.1% (3/2054) | 数值 | 0.6 |
| `graphicData/shaderParameters/_FlickerFrequency` | 0.1% (3/2054) | 数值 | 0.25 |
| `graphicData/shaderParameters/_FlipHorizontally` | 0.1% (2/2054) | 数值 | 1 |
| `graphicData/shaderParameters/_FramesPerSec` | 0.5% (11/2054) | 数值 | 1.35 / 12 / 7 |
| `graphicData/shaderParameters/_GradientScale` | 0.1% (3/2054) | 数值 | 0.5 / 0.6 |
| `graphicData/shaderParameters/_GradientTex` | 0.2% (5/2054) | 文本 | /Things/Mote/IncineratorBeamGradient / /Things/Mote/RitualEffects/DustyGradient / /Things/Mote/RitualEffects/G |
| `graphicData/shaderParameters/_InnerCircleIntensity` | 0.1% (3/2054) | 数值 | 0.1 |
| `graphicData/shaderParameters/_InnerCircleShimmerAmount` | 0.1% (3/2054) | 数值 | 0.14 |
| `graphicData/shaderParameters/_InnerCircleSize` | 0.1% (3/2054) | 数值 | 0.1 / 0.4 |
| `graphicData/shaderParameters/_InnerFadeAmount` | 0.1% (2/2054) | 数值 | 0 / 1 |
| `graphicData/shaderParameters/_Intensity` | 0.8% (16/2054) | 数值 | 0 / 0.5 / 1 |
| `graphicData/shaderParameters/_Interval` | 0.3% (6/2054) | 数值 | .05 / .5 / 0.04 |
| `graphicData/shaderParameters/_MainTex` | 0.1% (1/2054) | 文本 | /Things/Mote/ActivatorProximityRadius |
| `graphicData/shaderParameters/_MaskTex` | 0.7% (14/2054) | 文本 | /Things/Building/VoidNode/InternalDustMask / /Things/Mote/PollutionWave / /Things/Mote/PsychicDistortionRingIn |
| `graphicData/shaderParameters/_MaxAlpha` | 0.1% (1/2054) | 数值 | 0.3 |
| `graphicData/shaderParameters/_MinAlpha` | 0.1% (1/2054) | 数值 | 0.1 |
| `graphicData/shaderParameters/_MistOpacityTex` | 0.3% (7/2054) | 文本 | /Things/Building/Production/MechGestatorLargeGlassGlowSoft_south / /Things/Building/Production/MechGestatorSta |
| `graphicData/shaderParameters/_MistScrollSpeed` | 0.1% (1/2054) | 数值 | 0.2 |
| `graphicData/shaderParameters/_MistTex` | 0.1% (1/2054) | 文本 | /Things/Mote/SmokeTiled |
| `graphicData/shaderParameters/_MultiplyTex` | 0.3% (7/2054) | 文本 | /Things/Mote/RadiationDistortion_A / /Things/Mote/RadiationDistortion_B |
| `graphicData/shaderParameters/_MultiplyTexA` | 0.1% (3/2054) | 文本 | /Things/Mote/Cloudy_A / /Things/Mote/Cloudy_B |
| `graphicData/shaderParameters/_MultiplyTexB` | 0.1% (3/2054) | 文本 | /Things/Mote/Cloudy_C |
| `graphicData/shaderParameters/_noiseIntensity` | 0.3% (6/2054) | 数值 | 0 / 10 / 2 |
| `graphicData/shaderParameters/_NoiseTex` | 0.5% (10/2054) | 文本 | /Things/Mote/HarshNoise / /Things/Mote/PsycastNoise / /Things/Mote/SoftNoise |
| `graphicData/shaderParameters/_NumFrames` | 0.5% (11/2054) | 数值 | 10 / 12 / 4 |
| `graphicData/shaderParameters/_OutlineMultiplier` | 0.1% (1/2054) | 数值 | 0.42 |
| `graphicData/shaderParameters/_PulseInterval` | 0.1% (1/2054) | 数值 | 0.5 |
| `graphicData/shaderParameters/_PulseMax` | 0.1% (1/2054) | 数值 | 1 |
| `graphicData/shaderParameters/_PulseMin` | 0.1% (1/2054) | 数值 | .8 |
| `graphicData/shaderParameters/_pulseSpeed` | 0.8% (17/2054) | 数值 | 0.3 / 1 / 2 |
| `graphicData/shaderParameters/_PulseTex` | 0.1% (3/2054) | 文本 | /Things/Mote/ApocritonWaves / /Things/Mote/ObeliskPulseWaves |
| `graphicData/shaderParameters/_RandomTex` | 0.1% (3/2054) | 文本 | /Things/Mote/RandomFlicker |
| `graphicData/shaderParameters/_rotationSpeed` | 0.1% (1/2054) | 数值 | 0.1 |
| `graphicData/shaderParameters/_ScanIntensity` | 0.1% (1/2054) | 数值 | 4 |
| `graphicData/shaderParameters/_ScanMask` | 0.1% (2/2054) | 文本 | /Things/Mote/FleshmelterBolt_Target_Scan_Mask / /Things/Mote/MoteHellfireCannon_Target_Scan_Mask |
| `graphicData/shaderParameters/_ScanOffset` | 0.3% (6/2054) | 数值 | -0.05 / -0.09 / -0.11 |
| `graphicData/shaderParameters/_ScanPow` | 0.1% (2/2054) | 数值 | 7 / 9 |
| `graphicData/shaderParameters/_ScanScale` | 0.3% (6/2054) | 数值 | 11.25 / 12 / 12.5 |
| `graphicData/shaderParameters/_ScanSpeed` | 0.1% (3/2054) | 数值 | .1 / 1.0 / 1.5 |
| `graphicData/shaderParameters/_ScanSpeedAccel` | 0.1% (1/2054) | 数值 | .1 |
| `graphicData/shaderParameters/_ScanTex` | 0.1% (3/2054) | 文本 | /Things/Mote/ActivatorProximityScanning / /Things/Mote/FleshmelterBolt_Target_Scan / /Things/Mote/MoteHellfire |
| `graphicData/shaderParameters/_ScrollDir` | 0.1% (2/2054) | 数值 | -1 / 1 |
| `graphicData/shaderParameters/_ScrollScale` | 0.2% (5/2054) | 数值 | 0.14 / 0.22 |
| `graphicData/shaderParameters/_ScrollScalse` | 0.1% (1/2054) | 文本 | (0.1, 0.1, 0, 0) |
| `graphicData/shaderParameters/_ScrollSpeed` | 0.9% (19/2054) | 数值/文本 | -.1 / -0.9 / -1.2 |
| `graphicData/shaderParameters/_ScrollSpeedA` | 0.1% (3/2054) | 数值 | -4 / 0 |
| `graphicData/shaderParameters/_ScrollSpeedB` | 0.1% (3/2054) | 数值 | 0 / 3 |
| `graphicData/shaderParameters/_shadowMultiplier` | 0.1% (1/2054) | 数值 | 0.23 |
| `graphicData/shaderParameters/_smokeAmount` | 0.1% (1/2054) | 数值 | 0.5 |
| `graphicData/shaderParameters/_smokeScrollSpeed` | 0.1% (1/2054) | 数值 | 0.1 |
| `graphicData/shaderParameters/_SmokeTex` | 0.1% (1/2054) | 文本 | /Things/Mote/SmokeTiled |
| `graphicData/shaderParameters/_SmokeTex1` | 0.3% (6/2054) | 文本 | /Things/Mote/RitualEffects/Smoke1 / /Things/Mote/RitualEffects/Smoke1_Dust / /Things/Mote/RitualEffects/Smoke1 |
| `graphicData/shaderParameters/_SmokeTex2` | 0.3% (6/2054) | 文本 | /Things/Mote/RitualEffects/Smoke2 / /Things/Mote/RitualEffects/Smoke2_Dust / /Things/Mote/RitualEffects/Smoke2 |
| `graphicData/shaderParameters/_snakeParticlesFactor` | 0.1% (2/2054) | 数值 | 1.0 / 1.1 |
| `graphicData/shaderParameters/_SoftEdgeSize` | 0.1% (1/2054) | 数值 | 0.7 |
| `graphicData/shaderParameters/_SquashNStretch` | 0.1% (1/2054) | 文本 | (.9, .95, .5, -.5) |
| `graphicData/shaderParameters/_texAScale` | 0.6% (12/2054) | 数值 | 0.2 / 0.3 / 0.4 |
| `graphicData/shaderParameters/_texAScaleDist` | 0.2% (4/2054) | 数值 | 0.5 |
| `graphicData/shaderParameters/_TexAScaleDivisorPerProgress` | 0.1% (2/2054) | 数值 | 0 / 1.5 |
| `graphicData/shaderParameters/_texAScrollSpeed` | 0.6% (12/2054) | 数值/文本 | (0, 0.15, 0) / 0 / 0.15 |
| `graphicData/shaderParameters/_texBScale` | 0.6% (12/2054) | 数值 | 0.3 / 0.35 / 0.4 |
| `graphicData/shaderParameters/_texBScrollSpeed` | 0.6% (12/2054) | 数值/文本 | (0.1, -0.15, 0) / -.4 / -0.4 |
| `graphicData/shaderParameters/_TextureScale` | 0.1% (1/2054) | 数值 | 1.4 |
| `graphicData/shaderParameters/_Thickness` | 0.3% (6/2054) | 数值 | 10 / 13 / 19 |
| `graphicData/shaderParameters/_VerticalScale` | 0.1% (1/2054) | 数值 | 1.36 |
| `graphicData/shaderParameters/_wordSpaceDistortionToggle` | 0.1% (1/2054) | 数值 | 1 |
| `graphicData/shaderType` | 14.3% (293/2054) | 文本 | Mote / MoteGlow / Transparent |
| `graphicData/shadowData` | 15.2% (313/2054) | 容器 |  |
| `graphicData/shadowData/offset` | 7.1% (146/2054) | 文本 | (0, 0, -0.2) / (0, 0, -0.5) / (0, 0, 0.1) |
| `graphicData/shadowData/volume` | 15.2% (313/2054) | 文本 | (0.27,0.25,0.27) / (0.3, 0.45, 0.3) / (0.6, 0.5, 1.8) |
| `graphicData/texPath` | 68.2% (1401/2054) | 文本 | Things/Projectile/Nociosphere_Heatspike / Things/Projectile/Projectile_Fingerspike / Things/Projectile/Project |
| `hasCustomRectForSelector` | 0.1% (2/2054) | 布尔 | true |
| `hasInteractionCell` | 2.9% (60/2054) | 布尔 | True / false / true |
| `hasTooltip` | 0.5% (11/2054) | 布尔 | true |
| `healthAffectsPrice` | 1.7% (34/2054) | 布尔 | false / true |
| `hiddenWhileUndiscovered` | 0.9% (19/2054) | 布尔 | true |
| `hideAtSnowOrSandDepth` | 0.6% (12/2054) | 数值 | 0.5 |
| `hideInspect` | 0.1% (3/2054) | 布尔 | true |
| `hideMainDesc` | 0.1% (1/2054) | 布尔 | true |
| `hideStats` | 0.1% (3/2054) | 布尔 | true |
| `highlightColor` | 0.1% (2/2054) | 文本 | (0.56, 0.62, 0.9) |
| `holdsRoof` | 0.8% (17/2054) | 布尔 | false / true |
| `ideoBuilding` | 0.1% (2/2054) | 布尔 | true |
| `ideoBuildingNamerBase` | 0.4% (9/2054) | 文本 | NamerAltar / NamerChristmasTree / NamerIdeoSculpture |
| `ingestible` | 5.3% (109/2054) | 容器 |  |
| `ingestible/ateEvent` | 0.1% (1/2054) | 文本 | AteNutrientPaste |
| `ingestible/babiesCanIngest` | 0.1% (3/2054) | 布尔 | true |
| `ingestible/baseIngestTicks` | 0.5% (10/2054) | 数值 | 100 / 210 / 650 |
| `ingestible/canAutoSelectAsFoodForCaravan` | 0.4% (9/2054) | 布尔 | false |
| `ingestible/chairSearchRadius` | 0.4% (8/2054) | 数值 | 0 / 25 / 4 |
| `ingestible/defaultNumToIngestAtOnce` | 0.2% (4/2054) | 数值 | 1 / 4 |
| `ingestible/drugCategory` | 0.6% (12/2054) | 文本 | Hard / Medical / Social |
| `ingestible/foodType` | 1.6% (32/2054) | 文本 | Fluid / Meal / Meat |
| `ingestible/humanlikeOnly` | 0.1% (1/2054) | 布尔 | true |
| `ingestible/ingestCommandString` | 0.4% (9/2054) | 文本 | Drink {0} / Ingest {0} / Inject {0} |
| `ingestible/ingestEffect` | 0.7% (15/2054) | 文本 | EatMeat / EatVegetarian / Smoke_Flake |
| `ingestible/ingestEffectEat` | 0.1% (2/2054) | 文本 | EatVegetarian |
| `ingestible/ingestHoldOffsetStanding` | 0.3% (6/2054) | 容器 |  |
| `ingestible/ingestHoldOffsetStanding/east` | 0.1% (1/2054) | 容器 |  |
| `ingestible/ingestHoldOffsetStanding/east/offset` | 0.1% (1/2054) | 文本 | (0.45,0,0.08) |
| `ingestible/ingestHoldOffsetStanding/northDefault` | 0.3% (6/2054) | 容器 |  |
| `ingestible/ingestHoldOffsetStanding/northDefault/behind` | 0.1% (1/2054) | 布尔 | true |
| `ingestible/ingestHoldOffsetStanding/northDefault/offset` | 0.3% (6/2054) | 文本 | (0.18,0,0) / (0.21,0,0.05) / (0.23,0,0.065) |
| `ingestible/ingestHoldOffsetStanding/south` | 0.1% (1/2054) | 容器 |  |
| `ingestible/ingestHoldOffsetStanding/south/offset` | 0.1% (1/2054) | 文本 | (0.27,0,0.08) |
| `ingestible/ingestHoldOffsetStanding/west` | 0.1% (1/2054) | 容器 |  |
| `ingestible/ingestHoldOffsetStanding/west/flip` | 0.1% (1/2054) | 布尔 | true |
| `ingestible/ingestHoldOffsetStanding/west/offset` | 0.1% (1/2054) | 文本 | (-0.50,0,0.08) |
| `ingestible/ingestHoldUsesTable` | 0.3% (7/2054) | 布尔 | false |
| `ingestible/ingestReportString` | 0.4% (9/2054) | 文本 | Drinking {0}. / Ingesting {0}. / Injecting {0}. |
| `ingestible/ingestReportStringEat` | 0.1% (1/2054) | 文本 | Consuming {0}. |
| `ingestible/ingestSound` | 1.2% (24/2054) | 文本 | HemogenPack_Consume / Ingest_Pill / RawMeat_Eat |
| `ingestible/joy` | 0.5% (11/2054) | 数值 | 0.17 / 0.40 / 0.5 |
| `ingestible/joyKind` | 0.5% (11/2054) | 文本 | Chemical / Gluttonous |
| `ingestible/lowPriorityCaravanFood` | 0.1% (1/2054) | 布尔 | true |
| `ingestible/maxNumToIngestAtOnce` | 0.2% (4/2054) | 数值 | 1 / 4 |
| `ingestible/nurseable` | 0.3% (6/2054) | 布尔 | true |
| `ingestible/optimalityOffsetFeedingAnimals` | 0.4% (8/2054) | 数值 | -100 / -25 / -75 |
| `ingestible/optimalityOffsetHumanlikes` | 0.2% (4/2054) | 数值 | -30 / -5 / 16 |
| `ingestible/outcomeDoers` | 0.6% (13/2054) | 容器 |  |
| `ingestible/outcomeDoers/li` | 1.4% (28/2054) | 容器 |  |
| `ingestible/outcomeDoers/li/chanceBreakdown` | 0.1% (1/2054) | 数值 | 0.04 |
| `ingestible/outcomeDoers/li/chanceInspiration` | 0.1% (1/2054) | 数值 | 0.06 |
| `ingestible/outcomeDoers/li/divideByBodySize` | 0.3% (7/2054) | 布尔 | true |
| `ingestible/outcomeDoers/li/doToGeneratedPawnIfAddicted` | 0.1% (1/2054) | 布尔 | true |
| `ingestible/outcomeDoers/li/hediffDef` | 0.9% (18/2054) | 文本 | AlcoholHigh / AlcoholTolerance / AmbrosiaHigh |
| `ingestible/outcomeDoers/li/multiplyByGeneToleranceFactors` | 0.3% (7/2054) | 布尔 | true |
| `ingestible/outcomeDoers/li/need` | 0.3% (6/2054) | 文本 | Rest |
| `ingestible/outcomeDoers/li/offset` | 0.4% (8/2054) | 数值 | 0.1 / 0.15 / 0.2 |
| `ingestible/outcomeDoers/li/severity` | 0.9% (18/2054) | 数值 | 0.016 / 0.032 / 0.15 |
| `ingestible/outcomeDoers/li/toleranceChemical` | 1.0% (21/2054) | 文本 | Alcohol / Ambrosia / GoJuice |
| `ingestible/preferability` | 1.6% (32/2054) | 文本 | DesperateOnly / MealTerrible / NeverForNutrition |
| `ingestible/showIngestFloatOption` | 0.1% (1/2054) | 布尔 | false |
| `ingestible/specialThoughtAsIngredient` | 0.1% (1/2054) | 文本 | AteTwistedMeat |
| `ingestible/specialThoughtDirect` | 0.1% (2/2054) | 文本 | AteTwistedMeat / IngestedHemogenPack |
| `ingestible/tableDesired` | 0.1% (1/2054) | 布尔 | false |
| `ingestible/tasteThought` | 0.5% (10/2054) | 容器/文本 | AteBabyFood / AteFineMeal / AteKibble |
| `ingestible/useEatingSpeedStat` | 0.2% (4/2054) | 布尔 | false |
| `ingredient` | 0.2% (4/2054) | 容器 |  |
| `ingredient/mergeCompatibilityTags` | 0.2% (4/2054) | 容器 |  |
| `ingredient/mergeCompatibilityTags/li` | 0.2% (4/2054) | 文本 | Fungus / HumanMeat / InsectMeat |
| `inspectorTabs` | 3.2% (66/2054) | 容器 |  |
| `inspectorTabs/li` | 4.2% (87/2054) | 文本 | ITab_Bills / ITab_ContentsMapPortal / ITab_Entity |
| `interactionCellIcon` | 0.2% (5/2054) | 文本 | DiningChair |
| `interactionCellIconReverse` | 0.1% (2/2054) | 布尔 | true |
| `interactionCellOffset` | 3.2% (65/2054) | 文本 | (0, 0, 2) / (0,0,-1) / (0,0,-2) |
| `intricate` | 0.4% (9/2054) | 布尔 | true |
| `isAltar` | 0.1% (2/2054) | 布尔 | true |
| `isMechClusterThreat` | 0.3% (7/2054) | 布尔 | false / true |
| `isSaveable` | 0.1% (2/2054) | 布尔 | false |
| `isTechHediff` | 0.1% (3/2054) | 布尔 | true |
| `isUnfinishedThing` | 0.1% (1/2054) | 布尔 | true |
| `killedLeavings` | 4.1% (85/2054) | 容器 |  |
| `killedLeavings/AIPersonaCore` | 0.1% (1/2054) | 数值 | 1 |
| `killedLeavings/Bioferrite` | 0.1% (2/2054) | 数值 | 30 / 35 |
| `killedLeavings/ChunkMechanoidSlag` | 0.1% (1/2054) | 数值 | 1 |
| `killedLeavings/ChunkSlagSteel` | 3.6% (74/2054) | 数值 | 1 / 2 / 4 |
| `killedLeavings/ComponentIndustrial` | 0.4% (9/2054) | 数值 | 1 / 3 / 4 |
| `killedLeavings/ComponentSpacer` | 0.1% (2/2054) | 数值 | 1 / 5 |
| `killedLeavings/Filth_Fuel` | 0.1% (1/2054) | 数值 | 1 |
| `killedLeavings/Filth_MachineBits` | 0.1% (1/2054) | 数值 | 4 |
| `killedLeavings/Gravcore` | 0.1% (3/2054) | 数值 | 1 |
| `killedLeavings/GravlitePanel` | 0.2% (4/2054) | 数值 | 15 / 165 / 25 |
| `killedLeavings/InsectJelly` | 0.1% (1/2054) | 数值 | 30 |
| `killedLeavings/Meat_Human` | 0.1% (1/2054) | 数值 | 120 |
| `killedLeavings/MechanoidTransponder` | 0.1% (1/2054) | 数值 | 1 |
| `killedLeavings/Plasteel` | 0.5% (11/2054) | 数值 | 10 / 100 / 50 |
| `killedLeavings/ReinforcedBarrel` | 0.1% (1/2054) | 数值 | 1 |
| `killedLeavings/Shard` | 0.1% (3/2054) | 数值 | 1 / 2 / 3 |
| `killedLeavings/ShuttleEngine` | 0.1% (1/2054) | 数值 | 1 |
| `killedLeavings/SmokeleafLeaves` | 0.1% (1/2054) | 数值 | 150 |
| `killedLeavings/Steel` | 0.5% (11/2054) | 数值 | 200 / 25 / 4 |
| `killedLeavings/Uranium` | 0.1% (3/2054) | 数值 | 3 / 50 |
| `killedLeavingsChance` | 0.1% (1/2054) | 数值 | 0.5 |
| `killedLeavingsPlayerHostile` | 0.1% (3/2054) | 容器 |  |
| `killedLeavingsPlayerHostile/NanostructuringChip` | 0.1% (1/2054) | 数值 | 1 |
| `killedLeavingsPlayerHostile/PowerfocusChip` | 0.1% (1/2054) | 数值 | 1 |
| `killedLeavingsPlayerHostile/SignalChip` | 0.1% (1/2054) | 数值 | 1 |
| `killedLeavingsRanges` | 0.2% (5/2054) | 容器 |  |
| `killedLeavingsRanges/Bioferrite` | 0.1% (2/2054) | 文本 | 10~20 / 30~50 |
| `killedLeavingsRanges/Meat_Twisted` | 0.1% (3/2054) | 文本 | 100~200 / 200~300 / 4~8 |
| `killedLeavingsRanges/Shard` | 0.1% (3/2054) | 数值/文本 | 0~1 / 1 / 2 |
| `label` | 74.5% (1531/2054) | 文本 | fleshmelter bolt / heatspike shot / spike |
| `leaveResourcesWhenKilled` | 2.2% (45/2054) | 布尔 | True / false / true |
| `maxTechLevelToBuild` | 0.1% (2/2054) | 文本 | Neolithic |
| `meleeHitSound` | 0.3% (6/2054) | 文本 | MeleeHit_BladelinkMonoSword / MeleeHit_BladelinkPlasmaSword / MeleeHit_BladelinkZeusHammer |
| `mergeVerbGizmos` | 0.2% (5/2054) | 布尔 | false |
| `messageOnDeteriorateInStorage` | 0.1% (1/2054) | 布尔 | false |
| `mineable` | 0.2% (4/2054) | 布尔 | false / true |
| `minifiedDef` | 4.5% (93/2054) | 容器/文本 | MinifiedGravEngine / MinifiedThing / MinifiedThingRealtimeDraw |
| `minifiedDrawOffset` | 0.2% (4/2054) | 文本 | (0, 0, 0.2) |
| `minifiedDrawScale` | 0.1% (1/2054) | 数值 | 0.5 |
| `minifiedManualDraw` | 0.1% (1/2054) | 布尔 | true |
| `minMonolithLevel` | 0.1% (1/2054) | 数值 | 1 |
| `minRewardCount` | 0.6% (12/2054) | 数值 | 10 / 30 |
| `minTechLevelToBuild` | 0.2% (5/2054) | 文本 | Industrial / Medieval |
| `mote` | 8.7% (178/2054) | 容器 |  |
| `mote/acceleration` | 0.1% (2/2054) | 文本 | (0,0,0.0014) |
| `mote/archDuration` | 0.2% (5/2054) | 数值 | 0.5 / 3 |
| `mote/archHeight` | 0.2% (5/2054) | 数值 | 0.5 / 2 |
| `mote/attachedDrawOffset` | 0.4% (8/2054) | 文本 | (0.2, 0, 0.2) / (0.45, 0, 0.45) / (0.75, 0, 0.75) |
| `mote/attachedToHead` | 0.1% (2/2054) | 布尔 | True / true |
| `mote/collide` | 0.3% (7/2054) | 布尔 | true |
| `mote/fadeInTime` | 7.2% (149/2054) | 数值 | 0.03 / 0.05 / 0.1 |
| `mote/fadeOutTime` | 7.4% (152/2054) | 数值 | 0.1 / 0.2 / 1.3 |
| `mote/fadeOutUnmaintained` | 1.0% (20/2054) | 布尔 | True / true |
| `mote/growthRate` | 1.8% (37/2054) | 数值 | -2 / 120 / 2 |
| `mote/needsMaintenance` | 3.5% (73/2054) | 布尔 | False / True / false |
| `mote/realTime` | 0.1% (1/2054) | 布尔 | true |
| `mote/rotateTowardsMoveDirection` | 0.1% (2/2054) | 布尔 | true |
| `mote/rotateTowardsTarget` | 0.8% (16/2054) | 布尔 | True / true |
| `mote/scalers` | 0.1% (1/2054) | 容器 |  |
| `mote/scalers/li` | 0.1% (2/2054) | 容器 |  |
| `mote/scalers/li/axisMask` | 0.1% (2/2054) | 文本 | (0, 1, 1) / (1, 0, 0) |
| `mote/scalers/li/curve` | 0.1% (2/2054) | 容器 |  |
| `mote/scalers/li/curve/points` | 0.1% (2/2054) | 容器 |  |
| `mote/scalers/li/curve/points/li` | 2.5% (52/2054) | 文本 | (0,-1) / (0.04,-0.8541513) / (0.08,-0.7187468) |
| `mote/scalers/li/scaleAmt` | 0.1% (2/2054) | 数值 | 1 |
| `mote/scalers/li/scaleTime` | 0.1% (2/2054) | 数值 | 1 / 1.2 |
| `mote/scaleToConnectTargets` | 0.5% (10/2054) | 布尔 | False / True |
| `mote/solidTime` | 8.7% (178/2054) | 数值 | 0.2 / 0.4 / 0.87 |
| `mote/speedPerTime` | 0.3% (7/2054) | 数值 | -0.12 / -10 / -22 |
| `mote/unattachedDrawOffset` | 0.1% (2/2054) | 文本 | (0, 0.0, 0.18) / (0,0,40) |
| `mote/updateOffsetToMatchTargetRotation` | 0.1% (3/2054) | 布尔 | True |
| `mote/yFightingOffsetScalar01` | 0.3% (6/2054) | 数值 | 0 |
| `multipleInteractionCellOffsets` | 0.1% (1/2054) | 容器 |  |
| `multipleInteractionCellOffsets/li` | 0.1% (2/2054) | 文本 | (0,0,-1) / (1,0,-1) |
| `neverMultiSelect` | 2.5% (51/2054) | 布尔 | True / false / true |
| `neverOverlapFloors` | 0.1% (3/2054) | 布尔 | false / true |
| `noRightClickDraftAttack` | 1.8% (37/2054) | 布尔 | true |
| `notifyMapRemoved` | 0.1% (2/2054) | 布尔 | true |
| `onlyShowInspectString` | 0.1% (1/2054) | 布尔 | true |
| `orderedTakeGroup` | 0.1% (3/2054) | 文本 | Drug / Medicine |
| `overrideMinifiedRot` | 0.2% (4/2054) | 文本 | North |
| `passability` | 15.6% (321/2054) | 文本 | Impassable / PassThroughOnly / Standable |
| `pathCost` | 14.3% (294/2054) | 数值 | 0 / 14 / 30 |
| `pathCostIgnoreRepeat` | 0.4% (8/2054) | 布尔 | false / true |
| `pathfinderDangerous` | 0.1% (1/2054) | 布尔 | true |
| `pawnFlyer` | 0.1% (3/2054) | 容器 |  |
| `pawnFlyer/flightDurationMin` | 0.1% (2/2054) | 数值 | 0.5 / 0.75 |
| `pawnFlyer/flightSpeed` | 0.1% (2/2054) | 数值 | 12 / 8 |
| `pawnFlyer/heightFactor` | 0.1% (2/2054) | 数值 | 0.5 / 2 |
| `pawnFlyer/progressCurve` | 0.1% (1/2054) | 容器 |  |
| `pawnFlyer/progressCurve/points` | 0.1% (1/2054) | 容器 |  |
| `pawnFlyer/progressCurve/points/li` | 0.1% (3/2054) | 文本 | (0, 0) / (0.1, 0.15) / (1, 1) |
| `pawnFlyer/stunDurationTicksRange` | 0.1% (1/2054) | 文本 | 60~180 |
| `pawnFlyer/workerClass` | 0.1% (1/2054) | 文本 | PawnFlyerWorker |
| `placeWorkers` | 7.6% (157/2054) | 容器 |  |
| `placeWorkers/li` | 10.1% (208/2054) | 文本 | PlaceWorker_ElectricInhibitor / PlaceWorker_MultiCellDoor / PlaceWorker_ShowTurretRadius |
| `plant` | 5.1% (104/2054) | 容器 |  |
| `plant/allowAutoCut` | 0.3% (7/2054) | 布尔 | false |
| `plant/autoHarvestable` | 0.1% (1/2054) | 布尔 | false |
| `plant/blockAdjacentSow` | 0.2% (4/2054) | 布尔 | false / true |
| `plant/burnedThingDef` | 0.2% (5/2054) | 容器/文本 | BurnedTree |
| `plant/canDeteriorate` | 0.1% (1/2054) | 布尔 | true |
| `plant/cavePlant` | 0.1% (3/2054) | 布尔 | false / true |
| `plant/cavePlantWeight` | 0.1% (2/2054) | 数值 | 0 / 0.17 |
| `plant/choppedThingDef` | 0.5% (10/2054) | 容器/文本 | ChoppedStump / ChoppedStump_Harbinger / ChoppedStump_Polluted |
| `plant/completelyIgnoreFertility` | 0.1% (2/2054) | 布尔 | true |
| `plant/destroyedByFlooding` | 0.1% (1/2054) | 布尔 | false |
| `plant/dieFromToxicFallout` | 0.3% (7/2054) | 布尔 | False |
| `plant/dieIfLeafless` | 1.0% (20/2054) | 布尔 | false / true |
| `plant/dieIfNoSunlight` | 0.2% (5/2054) | 布尔 | False / false |
| `plant/diesToLight` | 0.2% (5/2054) | 布尔 | true |
| `plant/drugForHarvestPurposes` | 0.1% (3/2054) | 布尔 | True |
| `plant/fertilityMin` | 1.8% (37/2054) | 数值 | 0.05 / 0.08 / 0.5 |
| `plant/fertilitySensitivity` | 2.2% (46/2054) | 数值 | 0 / 0.3 / 0.5 |
| `plant/forceIsTree` | 0.1% (1/2054) | 布尔 | true |
| `plant/growDays` | 3.9% (80/2054) | 数值 | 10 / 2.5 / 3 |
| `plant/growMinGlow` | 0.8% (16/2054) | 数值 | 0 / 0.3 |
| `plant/growOptimalGlow` | 0.3% (6/2054) | 数值 | 0 |
| `plant/harvestAfterGrowth` | 0.2% (5/2054) | 数值 | 0 / 0.3 / 0.30 |
| `plant/harvestedThingDef` | 1.3% (27/2054) | 文本 | Bioferrite / RawFungus / RawToxipotato |
| `plant/harvestFailable` | 0.2% (4/2054) | 布尔 | false / true |
| `plant/harvestMinGrowth` | 0.1% (3/2054) | 数值 | 0 / 0.2 / 0.40 |
| `plant/harvestTag` | 1.4% (28/2054) | 文本 | Standard / Wood |
| `plant/harvestWork` | 2.2% (45/2054) | 数值 | 1000 / 200 / 40 |
| `plant/harvestYield` | 2.4% (50/2054) | 数值 | 15 / 30 / 6 |
| `plant/harvestYieldAffectedByDifficulty` | 0.1% (1/2054) | 布尔 | false |
| `plant/humanFoodPlant` | 0.2% (5/2054) | 布尔 | true |
| `plant/immatureGraphicPath` | 1.5% (31/2054) | 容器/文本 | Things/Plant/PotatoPlant_Immature / Things/Plant/RicePlant_Immature / Things/Plant/Toxipotato_Immature |
| `plant/immatureSnowOverlayGraphicPath` | 0.4% (9/2054) | 文本 | Things/Plant/TreeCocoa_LeaflessImmatureSnowy / Things/Plant/TreeCypress_LeaflessSnowyImmature / Things/Plant/T |
| `plant/interferesWithRoof` | 0.1% (3/2054) | 布尔 | false / true |
| `plant/isStump` | 0.1% (1/2054) | 布尔 | true |
| `plant/leaflessGraphicPath` | 1.2% (25/2054) | 容器/文本 | Things/Plant/Ambrosia_Leafless / Things/Plant/Graygrass_Leafless / Things/Plant/Ripthorn_Leafless |
| `plant/leaflessImmatureGraphicPath` | 0.3% (7/2054) | 文本 | Things/Plant/TreeCypress_LeaflessImmature / Things/Plant/TreeMaple_LeaflessImmature / Things/Plant/TreeOak_Lea |
| `plant/leaflessSnowOverlayGraphicPath` | 0.5% (10/2054) | 文本 | Things/Plant/Brambles_LeaflessSnowy / Things/Plant/Bush_LeaflessSnowy / Things/Plant/TreeCypress_LeaflessSnowy |
| `plant/lifespanDaysPerGrowDays` | 0.6% (13/2054) | 数值 | 0 / 3 / 5 |
| `plant/maxGrowthTemperature` | 0.6% (12/2054) | 数值 | 74 / 75 |
| `plant/maxMeshCount` | 1.2% (25/2054) | 数值 | 25 / 4 / 9 |
| `plant/maxOptimalGrowthTemperature` | 0.1% (1/2054) | 数值 | 68 |
| `plant/minSpacingBetweenSamePlant` | 0.2% (4/2054) | 数值 | 2.9 / 4.9 |
| `plant/mustBePermanentDarknessToSow` | 0.1% (1/2054) | 布尔 | true |
| `plant/mustBeWildToSow` | 0.1% (2/2054) | 布尔 | false / true |
| `plant/neverBlightable` | 0.5% (10/2054) | 布尔 | true |
| `plant/plantRespawningCommonalityFactor` | 0.1% (1/2054) | 数值 | 0.04 |
| `plant/pollutedGraphicPath` | 0.3% (7/2054) | 文本 | Things/Plant/Brambles_Polluted / Things/Plant/Chokevine_Polluted / Things/Plant/Grass_Polluted |
| `plant/pollution` | 1.0% (20/2054) | 文本 | Any / PollutedOnly |
| `plant/purpose` | 1.0% (21/2054) | 文本 | Beauty / Food / Health |
| `plant/showGrowthInInspectPane` | 0.2% (4/2054) | 布尔 | false / true |
| `plant/showInFrozenWater` | 0.1% (1/2054) | 布尔 | false |
| `plant/skipDeteriorationMessage` | 0.1% (1/2054) | 布尔 | true |
| `plant/smashedThingDef` | 0.5% (10/2054) | 容器/文本 | SmashedStump / SmashedStump_Harbinger / SmashedStump_Polluted |
| `plant/snowOverlayGraphicPath` | 0.2% (4/2054) | 文本 | Things/Plant/BerryPlant_Snowy / Things/Plant/SaguaroCactus_Snowy / Things/Plant/TreeCocoa_Snowy |
| `plant/soundHarvestFinish` | 0.1% (3/2054) | 文本 | Harvest_Standard_Finish / Harvest_Tree_Finish |
| `plant/soundHarvesting` | 0.1% (3/2054) | 文本 | Harvest_Standard / Harvest_Tree |
| `plant/sowMinSkill` | 0.7% (15/2054) | 数值 | 0 / 10 / 5 |
| `plant/sowResearchPrerequisites` | 0.5% (10/2054) | 容器 |  |
| `plant/sowResearchPrerequisites/li` | 0.1% (3/2054) | 文本 | Cocoa / Devilstrand / TreeSowing |
| `plant/sowTags` | 1.6% (32/2054) | 容器 |  |
| `plant/sowTags/li` | 1.6% (33/2054) | 文本 | Decorative / DecorativeTree / Ground |
| `plant/sowWork` | 0.6% (12/2054) | 数值 | 170 / 400 / 4000 |
| `plant/terraformable` | 0.1% (1/2054) | 布尔 | true |
| `plant/terrainBlacklist` | 0.1% (1/2054) | 容器 |  |
| `plant/terrainBlacklist/li` | 0.1% (1/2054) | 文本 | Ice |
| `plant/topWindExposure` | 2.9% (59/2054) | 数值 | 0.1 / 0.15 / 0.20 |
| `plant/treeCategory` | 0.3% (7/2054) | 文本 | Full / Mini / Super |
| `plant/treeLoversCareIfChopped` | 0.3% (7/2054) | 布尔 | false / true |
| `plant/vacuumResistant` | 0.1% (1/2054) | 布尔 | true |
| `plant/visualSizeRange` | 3.3% (68/2054) | 文本 | 0.4~0.6 / 0.7~0.85 / 0.8~1.5 |
| `plant/warnIfMarkedForCut` | 0.2% (5/2054) | 布尔 | true |
| `plant/wildClusterRadius` | 2.0% (42/2054) | 数值 | 3 / 4 / 5 |
| `plant/wildClusterWeight` | 2.3% (48/2054) | 数值 | 0 / 200 / 24 |
| `plant/wildEqualLocalDistribution` | 0.2% (5/2054) | 布尔 | false |
| `plant/wildOrder` | 1.9% (39/2054) | 数值 | 1 / 2 / 3 |
| `plant/wildPlantUseDistanceToShore` | 0.1% (2/2054) | 布尔 | true |
| `plant/wildTerrainTags` | 0.2% (5/2054) | 容器 |  |
| `plant/wildTerrainTags/li` | 0.5% (11/2054) | 文本 | Mud / WaterFreshShallow / WaterFreshShallowStill |
| `portal` | 0.1% (3/2054) | 容器 |  |
| `portal/enteredLetterDef` | 0.1% (1/2054) | 文本 | ThreatBig |
| `portal/enteredLetterLabel` | 0.1% (1/2054) | 文本 | Fleshbeast lair |
| `portal/enteredLetterText` | 0.1% (1/2054) | 文本 | In the depths of the pit gate, you have discovered a massive cavern system infes |
| `portal/exitDef` | 0.1% (3/2054) | 文本 | AncientHatchExit / CaveExit |
| `portal/pocketMapGenerator` | 0.1% (3/2054) | 文本 | AncientStockpile / InsectLair / Undercave |
| `portal/pocketMapSize` | 0.1% (1/2054) | 数值 | 75 |
| `portal/traverseSound` | 0.1% (1/2054) | 文本 | TraversePitGate |
| `possessionCount` | 5.1% (105/2054) | 数值 | 1 / 2 / 20 |
| `preventDroppingThingsOn` | 0.1% (3/2054) | 布尔 | true |
| `preventGravshipLandingOn` | 0.1% (1/2054) | 布尔 | true |
| `preventSkyfallersLandingOn` | 0.7% (15/2054) | 布尔 | true |
| `preventSpawningInResourcePod` | 0.1% (2/2054) | 布尔 | true |
| `projectile` | 3.8% (78/2054) | 容器 |  |
| `projectile/ai_IsIncendiary` | 0.3% (6/2054) | 布尔 | true |
| `projectile/alwaysFreeIntercept` | 0.1% (1/2054) | 布尔 | true |
| `projectile/applyDamageToExplosionCellsNeighbors` | 0.1% (1/2054) | 布尔 | true |
| `projectile/arcHeightFactor` | 0.7% (14/2054) | 数值 | 0.2 / 0.4 / 1 |
| `projectile/armorPenetrationBase` | 0.8% (17/2054) | 数值 | 0.12 / 0.15 / 0.8 |
| `projectile/beamMoteDef` | 0.1% (1/2054) | 文本 | Mote_BeamRepeaterLaser |
| `projectile/beamStartOffset` | 0.1% (1/2054) | 数值 | 0.5 |
| `projectile/damageAmountBase` | 2.3% (48/2054) | 数值 | 12 / 18 / 7 |
| `projectile/damageDef` | 3.3% (67/2054) | 文本 | AcidBurn / EnergyBolt / NociosphereVaporize |
| `projectile/doExplosionVFX` | 0.1% (1/2054) | 布尔 | false |
| `projectile/explosionChanceToStartFire` | 0.1% (2/2054) | 数值 | 0.22 / 0.75 |
| `projectile/explosionDamageFalloff` | 0.1% (1/2054) | 布尔 | true |
| `projectile/explosionDelay` | 0.1% (3/2054) | 数值 | 100 |
| `projectile/explosionEffect` | 0.1% (3/2054) | 文本 | ExtinguisherExplosion / GiantExplosion / Shell_AcidSpitImpact |
| `projectile/explosionEffectLifetimeTicks` | 0.1% (1/2054) | 数值 | 60 |
| `projectile/explosionRadius` | 1.4% (28/2054) | 数值 | 0.1 / 2.49 / 3.9 |
| `projectile/explosionRadiusDisplayPadding` | 0.1% (2/2054) | 数值 | 2 |
| `projectile/explosionSpawnsSingleFilth` | 0.1% (2/2054) | 布尔 | true |
| `projectile/filth` | 0.4% (8/2054) | 文本 | Filth_BlastMark / Filth_FireFoam / Filth_Slime |
| `projectile/filthChance` | 0.1% (2/2054) | 数值 | 0.25 |
| `projectile/filthCount` | 0.4% (9/2054) | 数值/文本 | 1 / 1~3 |
| `projectile/flyOverhead` | 0.4% (9/2054) | 布尔 | true |
| `projectile/landedEffecter` | 0.1% (2/2054) | 文本 | DisruptorFlareLanded / ExtinguisherPuffSmall |
| `projectile/numExtraHitCells` | 0.1% (2/2054) | 数值 | 0 / 4 |
| `projectile/postExplosionGasType` | 0.2% (4/2054) | 文本 | BlindSmoke / ToxGas |
| `projectile/postExplosionSpawnChance` | 0.1% (1/2054) | 数值 | 1 |
| `projectile/postExplosionSpawnThingCount` | 0.1% (1/2054) | 数值 | 3 |
| `projectile/postExplosionSpawnThingDef` | 0.2% (4/2054) | 文本 | Filth_FireFoam / Shell_Deadlife_Releasing / Shell_Toxic_Releasing |
| `projectile/postExplosionSpawnThingDefWater` | 0.1% (1/2054) | 文本 | Shell_Toxic_Releasing_Water |
| `projectile/preExplosionSpawnChance` | 0.1% (3/2054) | 数值 | 0.25 / 0.27 / 0.6 |
| `projectile/preExplosionSpawnSingleThingDef` | 0.1% (2/2054) | 文本 | CraterMedium / Filth_BlastMark |
| `projectile/preExplosionSpawnThingDef` | 0.2% (4/2054) | 文本 | Filth_Fuel |
| `projectile/screenShakeFactor` | 0.3% (6/2054) | 数值 | 0.5 / 1.25 / 1.5 |
| `projectile/shadowSize` | 0.6% (12/2054) | 数值 | 0 / 0.4 / 0.6 |
| `projectile/soundAmbient` | 0.4% (8/2054) | 文本 | FleshmelterBolt_Launch / MortarRound_Ambient |
| `projectile/soundExplode` | 0.6% (12/2054) | 文本 | Explosion_Rocket / MortarBomb_Explode / SpitterSpitLands |
| `projectile/soundHitThickRoof` | 0.3% (7/2054) | 文本 | Artillery_HitThickRoof |
| `projectile/soundImpact` | 0.1% (1/2054) | 文本 | Foam_Impact |
| `projectile/soundImpactAnticipate` | 0.3% (7/2054) | 文本 | MortarRound_PreImpact |
| `projectile/spawnsPawnKind` | 0.1% (1/2054) | 文本 | Drone_Hunter |
| `projectile/spawnsThingDef` | 0.1% (3/2054) | 文本 | DisruptorFlare / EggSac / Turret_TacticalTurret |
| `projectile/spawnTerrain` | 0.1% (2/2054) | 文本 | InsectSludge |
| `projectile/speed` | 3.4% (70/2054) | 数值 | 25 / 55 / 75 |
| `projectile/spinRate` | 0.1% (2/2054) | 数值 | 20 / 3 |
| `projectile/stoppingPower` | 1.0% (21/2054) | 数值 | 1 / 1.5 / 2.5 |
| `projectile/terrainChance` | 0.1% (2/2054) | 数值 | 0.75 |
| `projectile/tryAdjacentFreeSpaces` | 0.1% (3/2054) | 布尔 | true |
| `projectile/useGraphicClass` | 0.1% (1/2054) | 布尔 | True |
| `projectileWhenLoaded` | 0.4% (8/2054) | 文本 | Bullet_Shell_Deadlife / Bullet_Shell_HighExplosive / Bullet_Shell_Incendiary |
| `race` | 8.6% (176/2054) | 容器 |  |
| `race/ageGenerationCurve` | 0.1% (1/2054) | 容器 |  |
| `race/ageGenerationCurve/points` | 0.1% (1/2054) | 容器 |  |
| `race/ageGenerationCurve/points/li` | 0.8% (17/2054) | 文本 | (0,0) / (0.001,43) / (12.5,118) |
| `race/allowedOnCaravan` | 0.1% (1/2054) | 布尔 | false |
| `race/alwaysAwake` | 0.1% (2/2054) | 布尔 | true |
| `race/alwaysViolent` | 0.1% (2/2054) | 布尔 | true |
| `race/animalType` | 0.3% (7/2054) | 文本 | Canine / Dryad |
| `race/anomalyKnowledge` | 0.1% (2/2054) | 数值 | 1 / 2 |
| `race/baseBodySize` | 6.1% (125/2054) | 数值 | 0.8 / 1 / 2 |
| `race/baseHealthScale` | 6.3% (129/2054) | 数值 | 0.6 / 0.75 / 1.5 |
| `race/baseHungerRate` | 4.5% (92/2054) | 数值 | 0.2 / 0.28 / 0.35 |
| `race/bleedRateFactor` | 0.3% (6/2054) | 数值 | 0.5 |
| `race/bloodDef` | 0.6% (12/2054) | 容器/文本 | Filth_Blood / Filth_BloodInsect / Filth_DarkBlood |
| `race/bloodSmearDef` | 0.1% (3/2054) | 文本 | Filth_BloodSmear |
| `race/body` | 5.7% (116/2054) | 文本 | Human / Metalhorror / Nociosphere |
| `race/bulletStaggerEffecterDef` | 0.1% (1/2054) | 文本 | TunnelerSlowedDown |
| `race/canBecomeShambler` | 0.4% (8/2054) | 布尔 | true |
| `race/canBePredatorPrey` | 0.1% (3/2054) | 布尔 | false |
| `race/canBeVacuumBurnt` | 0.1% (1/2054) | 布尔 | false |
| `race/canCrossBreedWith` | 0.1% (2/2054) | 容器 |  |
| `race/canCrossBreedWith/li` | 0.1% (2/2054) | 文本 | AlphaThrumbo / Thrumbo |
| `race/canFishForFood` | 0.4% (8/2054) | 布尔 | true |
| `race/canFlyIntoMap` | 0.2% (5/2054) | 布尔 | true |
| `race/canFlyInVacuum` | 0.1% (2/2054) | 布尔 | true |
| `race/canLeaveMapFlying` | 0.2% (4/2054) | 布尔 | true |
| `race/canOpenFactionlessDoors` | 0.1% (1/2054) | 布尔 | false |
| `race/canReleaseToWild` | 0.1% (1/2054) | 布尔 | false |
| `race/corpseHiddenWhileUndiscovered` | 0.3% (6/2054) | 布尔 | true |
| `race/crossAggroWith` | 0.1% (2/2054) | 容器 |  |
| `race/crossAggroWith/li` | 0.1% (2/2054) | 文本 | AlphaThrumbo / Thrumbo |
| `race/deathAction` | 0.3% (7/2054) | 容器 |  |
| `race/deathAction/divideBloodFilthCountRange` | 0.1% (3/2054) | 文本 | 1~2 / 3~4 |
| `race/deathAction/dividePawnCount` | 0.1% (2/2054) | 数值 | 3 / 4 |
| `race/deathAction/dividePawnKindAdditionalForced` | 0.1% (1/2054) | 容器 |  |
| `race/deathAction/dividePawnKindAdditionalForced/li` | 0.1% (3/2054) | 文本 | Bulbfreak / Toughspike / Trispike |
| `race/deathAction/dividePawnKindOptions` | 0.1% (2/2054) | 容器 |  |
| `race/deathAction/dividePawnKindOptions/li` | 0.1% (3/2054) | 文本 | Fingerspike / Toughspike / Trispike |
| `race/deathAction/filth` | 0.1% (1/2054) | 文本 | Filth_TwistedFlesh |
| `race/deathAction/filthCountRange` | 0.1% (1/2054) | 文本 | 1~3 |
| `race/deathAction/meatExplosionSize` | 0.1% (1/2054) | 文本 | Small |
| `race/deathAction/workerClass` | 0.2% (4/2054) | 文本 | DeathActionWorker_BigExplosion / DeathActionWorker_SmallExplosion / DeathActionWorker_ToxCloud |
| `race/detritusLeavings` | 0.6% (13/2054) | 容器 |  |
| `race/detritusLeavings/li` | 1.8% (36/2054) | 容器 |  |
| `race/detritusLeavings/li/def` | 1.8% (36/2054) | 文本 | ChunkMechanoidSlag |
| `race/detritusLeavings/li/spawnChance` | 1.8% (36/2054) | 数值 | 0.1 / 0.5 / 0.75 |
| `race/detritusLeavings/li/texOverrideIndex` | 1.8% (36/2054) | 数值 | 0 / 1 / 11 |
| `race/disableAreaControl` | 0.1% (2/2054) | 布尔 | false / true |
| `race/disableIgniteVerb` | 0.4% (9/2054) | 布尔 | true |
| `race/doesntMove` | 0.1% (1/2054) | 布尔 | true |
| `race/dutyBoss` | 0.1% (1/2054) | 文本 | Warqueen |
| `race/executionRange` | 0.1% (2/2054) | 数值 | 4 / 6 |
| `race/fleshType` | 0.6% (12/2054) | 文本 | EntityFlesh / EntityMechanical / Fleshbeast |
| `race/flightSpeedFactor` | 0.1% (1/2054) | 数值 | 2.5 |
| `race/flightStartChanceOnJobStart` | 0.3% (6/2054) | 数值 | 0.025 / 0.05 / 0.1 |
| `race/foodType` | 4.9% (101/2054) | 文本 | CarnivoreAnimal, OvivoreAnimal / None / OmnivoreAnimal, OvivoreAnimal |
| `race/forceGender` | 0.1% (1/2054) | 文本 | Female |
| `race/gestationPeriodDays` | 3.4% (70/2054) | 数值 | 10 / 12 / 5.61 |
| `race/giveNonToolUserBeatFireVerb` | 0.1% (1/2054) | 布尔 | true |
| `race/hasCorpse` | 0.3% (7/2054) | 布尔 | false / true |
| `race/hasGenders` | 0.6% (12/2054) | 布尔 | false / true |
| `race/hasMeat` | 0.1% (1/2054) | 布尔 | false |
| `race/hasUnnaturalCorpse` | 0.1% (1/2054) | 布尔 | true |
| `race/headPosPerRotation` | 4.8% (99/2054) | 容器 |  |
| `race/headPosPerRotation/li` | 19.3% (396/2054) | 文本 | (-.2, 0, 0) / (.2, 0, 0) / (0, 0, .25) |
| `race/hediffGiverSets` | 0.6% (12/2054) | 容器 |  |
| `race/hediffGiverSets/li` | 0.6% (12/2054) | 文本 | AnomalyEntity / Fleshbeast / Human |
| `race/herdAnimal` | 2.1% (44/2054) | 布尔 | false / true |
| `race/herdMigrationAllowed` | 0.1% (3/2054) | 布尔 | false |
| `race/hideTrainingTab` | 0.1% (2/2054) | 布尔 | true |
| `race/intelligence` | 0.7% (15/2054) | 文本 | Humanlike / ToolUser |
| `race/isImmuneToInfections` | 0.3% (6/2054) | 布尔 | true |
| `race/knowledgeCategory` | 0.1% (2/2054) | 文本 | Advanced / Basic |
| `race/leatherDef` | 3.8% (77/2054) | 文本 | Leather_Bear / Leather_Bird / Leather_Dread |
| `race/leaveMapOnFleeChance` | 0.2% (4/2054) | 数值 | 0.25 / 0.8 / 1 |
| `race/lifeExpectancy` | 5.4% (110/2054) | 数值 | 100 / 1000 / 250 |
| `race/lifeStageAges` | 7.1% (146/2054) | 容器 |  |
| `race/lifeStageAges/li` | 17.3% (355/2054) | 容器 |  |
| `race/lifeStageAges/li/def` | 17.3% (355/2054) | 文本 | EntityFullyFormed / MetalhorrorJuvenile / MetalhorrorLarva |
| `race/lifeStageAges/li/minAge` | 16.1% (331/2054) | 数值 | 0 / 0.016667 / 0.05 |
| `race/lifeStageAges/li/soundAngry` | 4.9% (101/2054) | 文本 | Pawn_Bear_Angry / Pawn_Chick_Call / Pawn_Cougar_Angry |
| `race/lifeStageAges/li/soundAttack` | 0.1% (3/2054) | 文本 | Pawn_Devourer_Attack / Pawn_Gorehulk_Attack / Pawn_Nociosphere_Attack |
| `race/lifeStageAges/li/soundCall` | 7.8% (161/2054) | 文本 | Pawn_Nociosphere_Call / Pawn_Noctol_Call / Pawn_Revenant_Call |
| `race/lifeStageAges/li/soundDeath` | 7.4% (153/2054) | 文本 | Pawn_Gorehulk_Death / Pawn_Noctol_Death / Pawn_Revenant_Death |
| `race/lifeStageAges/li/soundWounded` | 7.9% (163/2054) | 文本 | Pawn_Nociosphere_Wounded / Pawn_Noctol_Wounded / Pawn_Revenant_Wounded |
| `race/lifeStageWorkSettings` | 0.1% (1/2054) | 容器 |  |
| `race/lifeStageWorkSettings/Art` | 0.1% (1/2054) | 数值 | 10 |
| `race/lifeStageWorkSettings/BasicWorker` | 0.1% (1/2054) | 数值 | 3 |
| `race/lifeStageWorkSettings/Childcare` | 0.1% (1/2054) | 数值 | 0 |
| `race/lifeStageWorkSettings/Cleaning` | 0.1% (1/2054) | 数值 | 3 |
| `race/lifeStageWorkSettings/Construction` | 0.1% (1/2054) | 数值 | 10 |
| `race/lifeStageWorkSettings/Cooking` | 0.1% (1/2054) | 数值 | 7 |
| `race/lifeStageWorkSettings/Crafting` | 0.1% (1/2054) | 数值 | 7 |
| `race/lifeStageWorkSettings/DarkStudy` | 0.1% (1/2054) | 数值 | 13 |
| `race/lifeStageWorkSettings/Doctor` | 0.1% (1/2054) | 数值 | 10 |
| `race/lifeStageWorkSettings/Firefighter` | 0.1% (1/2054) | 数值 | 7 |
| `race/lifeStageWorkSettings/Growing` | 0.1% (1/2054) | 数值 | 7 |
| `race/lifeStageWorkSettings/Handling` | 0.1% (1/2054) | 数值 | 7 |
| `race/lifeStageWorkSettings/Hauling` | 0.1% (1/2054) | 数值 | 3 |
| `race/lifeStageWorkSettings/Hunting` | 0.1% (1/2054) | 数值 | 7 |
| `race/lifeStageWorkSettings/Mining` | 0.1% (1/2054) | 数值 | 7 |
| `race/lifeStageWorkSettings/Patient` | 0.1% (1/2054) | 数值 | 0 |
| `race/lifeStageWorkSettings/PatientBedRest` | 0.1% (1/2054) | 数值 | 0 |
| `race/lifeStageWorkSettings/PlantCutting` | 0.1% (1/2054) | 数值 | 7 |
| `race/lifeStageWorkSettings/Research` | 0.1% (1/2054) | 数值 | 13 |
| `race/lifeStageWorkSettings/Smithing` | 0.1% (1/2054) | 数值 | 13 |
| `race/lifeStageWorkSettings/Tailoring` | 0.1% (1/2054) | 数值 | 7 |
| `race/lifeStageWorkSettings/Warden` | 0.1% (1/2054) | 数值 | 10 |
| `race/linkedCorpseKind` | 0.1% (1/2054) | 文本 | Human |
| `race/litterSizeCurve` | 1.7% (35/2054) | 容器 |  |
| `race/litterSizeCurve/points` | 1.7% (35/2054) | 容器 |  |
| `race/litterSizeCurve/points/li` | 7.2% (149/2054) | 文本 | (0.5, 0) / (1, 1) / (2, 1.7) |
| `race/makesFootprints` | 0.1% (1/2054) | 布尔 | true |
| `race/manhunterOnDamageChance` | 2.0% (42/2054) | 数值 | 0.1 / 0.5 / 0.50 |
| `race/manhunterOnTameFailChance` | 1.5% (31/2054) | 数值 | 0.10 / 0.2 / 0.30 |
| `race/manhunterPackUseLabelFrom` | 0.1% (1/2054) | 文本 | Thrumbo |
| `race/mateMtbHours` | 0.7% (14/2054) | 数值 | 8 |
| `race/maxPreyBodySize` | 0.5% (11/2054) | 数值 | 0.25 / 0.35 / 1.0 |
| `race/meatColor` | 0.1% (1/2054) | 文本 | (160,168,139) |
| `race/meatLabel` | 0.6% (12/2054) | 文本 | bear meat / beef / bird meat |
| `race/meatMarketValue` | 0.1% (2/2054) | 数值 | 0.5 / 0.8 |
| `race/mechEnabledWorkTypes` | 0.3% (7/2054) | 容器 |  |
| `race/mechEnabledWorkTypes/li` | 0.6% (13/2054) | 文本 | Construction / Crafting / Hauling |
| `race/mechWeightClass` | 0.4% (9/2054) | 文本 | Heavy / Light / Medium |
| `race/mechWorkTypePriorities` | 0.1% (1/2054) | 容器 |  |
| `race/mechWorkTypePriorities/PlantCutting` | 0.1% (1/2054) | 数值 | 2 |
| `race/nameCategory` | 0.1% (1/2054) | 文本 | HumanStandard |
| `race/nameGenerator` | 0.1% (3/2054) | 文本 | NamerAnimalGenericMale / NamerMech |
| `race/nameGeneratorFemale` | 0.1% (1/2054) | 文本 | NamerAnimalGenericFemale |
| `race/nameOnTameChance` | 0.5% (11/2054) | 数值 | 1 |
| `race/needsRest` | 0.6% (12/2054) | 布尔 | false |
| `race/neverIncludeInQuests` | 0.1% (1/2054) | 布尔 | true |
| `race/nuzzleMtbHours` | 0.5% (10/2054) | 数值 | 12 / 24 / 48 |
| `race/packAnimal` | 0.4% (9/2054) | 布尔 | true |
| `race/petness` | 1.5% (31/2054) | 数值 | 0.3 / 0.30 / 0.50 |
| `race/playerCanChangeMaster` | 0.1% (1/2054) | 布尔 | false |
| `race/predator` | 0.5% (10/2054) | 布尔 | true |
| `race/renderTree` | 0.6% (12/2054) | 文本 | Devourer / Misc / Nociosphere |
| `race/roamMtbDays` | 1.6% (32/2054) | 数值 | 2 / 3 / 5 |
| `race/showTrainables` | 0.1% (1/2054) | 布尔 | false |
| `race/soundAmbience` | 0.1% (1/2054) | 文本 | Pawn_Mech_Apocriton_Ambience |
| `race/soundCallIntervalFriendlyFactor` | 0.1% (2/2054) | 数值 | 2 |
| `race/soundCallIntervalRange` | 0.3% (6/2054) | 文本 | 1000~2000 / 120~240 / 2000~5000 |
| `race/soundEating` | 3.9% (81/2054) | 文本 | Bird_Eat / PredatorLarge_Eat / PredatorSmall_Eat |
| `race/soundMeleeDodge` | 0.4% (9/2054) | 文本 | Pawn_MeleeDodge |
| `race/soundMeleeHitBuilding` | 4.4% (91/2054) | 文本 | Pawn_Melee_BigBash_HitBuilding / Pawn_Melee_MechanoidBash_HitBuilding / Pawn_Melee_MechanoidSlash_HitBuilding |
| `race/soundMeleeHitPawn` | 4.4% (91/2054) | 文本 | Pawn_Melee_BigBash_HitPawn / Pawn_Melee_MechanoidBash_HitPawn / Pawn_Melee_MechanoidSlash_HitPawn |
| `race/soundMeleeMiss` | 4.4% (91/2054) | 文本 | Pawn_Melee_BigBash_Miss / Pawn_Melee_MechanoidBash_Miss / Pawn_Melee_MechanoidSlash_Miss |
| `race/soundMoving` | 0.1% (2/2054) | 文本 | Pawn_Fleshbeast_Bulbfreak_Moving / Pawn_Fleshbeast_Dreadmeld_Moving |
| `race/specialShadowData` | 0.1% (1/2054) | 容器 |  |
| `race/specialShadowData/offset` | 0.1% (1/2054) | 文本 | (0,0,-0.3) |
| `race/specialShadowData/volume` | 0.1% (1/2054) | 文本 | (0.3, 0.8, 0.4) |
| `race/specialTrainables` | 1.4% (28/2054) | 容器 |  |
| `race/specialTrainables/li` | 1.4% (28/2054) | 文本 | AttackTarget / Comfort / Dig |
| `race/specificMeatDef` | 0.3% (6/2054) | 文本 | Meat_Twisted |
| `race/startingAnimation` | 0.1% (1/2054) | 文本 | RevenantSpasm |
| `race/thinkTreeConstant` | 0.9% (19/2054) | 文本 | MetalhorrorConstant / NociosphereConstant / RevenantConstant |
| `race/thinkTreeMain` | 1.0% (20/2054) | 文本 | Metalhorror / Nociosphere / Revenant |
| `race/trainability` | 4.2% (87/2054) | 文本 | Advanced / Intermediate / None |
| `race/trainableTags` | 0.1% (3/2054) | 容器 |  |
| `race/trainableTags/li` | 0.2% (5/2054) | 文本 | Basic / Combat / Work |
| `race/untrainableTags` | 0.1% (3/2054) | 容器 |  |
| `race/untrainableTags/li` | 0.3% (7/2054) | 文本 | Basic / Combat / Help |
| `race/useMeatFrom` | 1.3% (26/2054) | 文本 | Bear_Grizzly / Cassowary / Hare |
| `race/waterCellCost` | 0.7% (15/2054) | 数值 | 1 / 10 |
| `race/waterSeeker` | 0.6% (13/2054) | 布尔 | true |
| `race/willNeverEat` | 0.1% (2/2054) | 容器 |  |
| `race/willNeverEat/li` | 0.5% (10/2054) | 文本 | Plant_TreeAnima / Plant_TreeGauranlen / Plant_TreeHarbinger |
| `randomizeRotationOnSpawn` | 0.1% (2/2054) | 布尔 | true |
| `randomStyle` | 0.1% (3/2054) | 容器 |  |
| `randomStyle/li` | 0.3% (7/2054) | 容器 |  |
| `randomStyle/li/styleDef` | 0.3% (7/2054) | 文本 | CultistMask_Dreadmask / CultistMask_SpikedApex / CultistMask_Spikemask |
| `randomStyleChance` | 0.2% (4/2054) | 数值 | 0.5 / 1 |
| `receivesSignals` | 1.1% (23/2054) | 布尔 | true |
| `recipeMaker` | 11.9% (245/2054) | 容器 |  |
| `recipeMaker/bulkRecipeCount` | 0.1% (3/2054) | 数值 | 4 |
| `recipeMaker/defaultIngredientFilter` | 0.5% (10/2054) | 容器 |  |
| `recipeMaker/defaultIngredientFilter/categories` | 0.5% (10/2054) | 容器 |  |
| `recipeMaker/defaultIngredientFilter/categories/li` | 0.5% (10/2054) | 文本 | Root |
| `recipeMaker/defaultIngredientFilter/disallowedThingDefs` | 0.5% (10/2054) | 容器 |  |
| `recipeMaker/defaultIngredientFilter/disallowedThingDefs/li` | 2.4% (49/2054) | 文本 | Gold / Jade / Plasteel |
| `recipeMaker/displayPriority` | 7.3% (151/2054) | 数值 | 110 / 140 / 150 |
| `recipeMaker/effectWorking` | 2.6% (53/2054) | 文本 | Cook / Sculpt / Smith |
| `recipeMaker/factionPrerequisiteTags` | 0.1% (2/2054) | 容器 |  |
| `recipeMaker/factionPrerequisiteTags/li` | 0.1% (2/2054) | 文本 | Tribal |
| `recipeMaker/mechanitorOnlyRecipe` | 0.1% (1/2054) | 布尔 | true |
| `recipeMaker/memePrerequisitesAny` | 0.1% (2/2054) | 容器 |  |
| `recipeMaker/memePrerequisitesAny/li` | 0.1% (3/2054) | 文本 | Blindsight / Guilty / PainIsVirtue |
| `recipeMaker/productCount` | 0.1% (1/2054) | 数值 | 1 |
| `recipeMaker/recipeUsers` | 4.6% (94/2054) | 容器 |  |
| `recipeMaker/recipeUsers/li` | 6.1% (125/2054) | 文本 | BioferriteShaper / CraftingSpot / SerumCentrifuge |
| `recipeMaker/requiredGiverWorkType` | 0.1% (1/2054) | 文本 | Cooking |
| `recipeMaker/researchPrerequisite` | 8.1% (167/2054) | 容器/文本 | GhoulEnhancements / InsanityWeaponry / RevenantInvisibility |
| `recipeMaker/researchPrerequisites` | 0.1% (1/2054) | 容器 |  |
| `recipeMaker/researchPrerequisites/li` | 0.1% (2/2054) | 文本 | JumpPack / ReconArmor |
| `recipeMaker/skillRequirements` | 4.4% (90/2054) | 容器 |  |
| `recipeMaker/skillRequirements/Artistic` | 0.1% (1/2054) | 数值 | 4 |
| `recipeMaker/skillRequirements/Cooking` | 0.1% (1/2054) | 数值 | 2 |
| `recipeMaker/skillRequirements/Crafting` | 4.3% (88/2054) | 数值 | 3 / 4 / 6 |
| `recipeMaker/skillRequirements/Intellectual` | 0.1% (1/2054) | 数值 | 4 |
| `recipeMaker/soundWorking` | 2.8% (57/2054) | 文本 | Recipe_Machining / Recipe_Sculpt / Recipe_Smith |
| `recipeMaker/targetCountAdjustment` | 0.1% (1/2054) | 数值 | 5 |
| `recipeMaker/unfinishedThingDef` | 3.1% (64/2054) | 文本 | UnfinishedBelt / UnfinishedHealthItemBionic / UnfinishedHealthItemGhoul |
| `recipeMaker/useIngredientsForColor` | 0.5% (10/2054) | 布尔 | false |
| `recipeMaker/workAmount` | 0.3% (6/2054) | 数值 | 1080 / 1320 / 720 |
| `recipeMaker/workSkill` | 3.0% (62/2054) | 文本 | Artistic / Cooking / Crafting |
| `recipeMaker/workSpeedStat` | 2.9% (60/2054) | 文本 | DrugCookingSpeed / DrugSynthesisSpeed / GeneralLaborSpeed |
| `recipes` | 0.8% (16/2054) | 容器 |  |
| `recipes/li` | 6.2% (127/2054) | 文本 | Agrihand / Constructoid / Lifter |
| `recoilPower` | 0.1% (1/2054) | 数值 | 3 |
| `relicChance` | 1.8% (38/2054) | 数值 | 0 / 1 / 2 |
| `repairEffect` | 1.0% (20/2054) | 文本 | ConstructDirt / ConstructMetal / Repair |
| `replaceTags` | 0.6% (12/2054) | 容器 |  |
| `replaceTags/li` | 0.6% (12/2054) | 文本 | Bed / Chair / Conduit |
| `requiresFactionToAcquire` | 0.1% (1/2054) | 文本 | Mechanoid |
| `researchPrerequisites` | 7.3% (151/2054) | 容器 |  |
| `researchPrerequisites/li` | 7.3% (151/2054) | 文本 | AtmosphericHeater / EntityContainment / ProximityDetector |
| `resourceReadoutAlwaysShow` | 0.1% (1/2054) | 布尔 | true |
| `resourceReadoutPriority` | 1.5% (30/2054) | 文本 | First / Last / Middle |
| `resourcesFractionWhenDeconstructed` | 0.9% (18/2054) | 数值 | 0 / 0.25 / 1 |
| `ritualFocus` | 0.5% (10/2054) | 容器 |  |
| `ritualFocus/allowedSpectateSides` | 0.4% (9/2054) | 文本 | All / Down / Up |
| `ritualFocus/consumable` | 0.1% (1/2054) | 布尔 | true |
| `ritualFocus/spectateDistance` | 0.5% (10/2054) | 数值/文本 | 1 / 1~2 / 2 |
| `rotatable` | 13.4% (276/2054) | 布尔 | True / false / true |
| `rotateInShelves` | 0.3% (6/2054) | 布尔 | false |
| `saveCompressible` | 0.6% (12/2054) | 布尔 | false / true |
| `scatterableOnMapGen` | 1.2% (24/2054) | 布尔 | false |
| `seeThroughFog` | 0.1% (2/2054) | 布尔 | true |
| `selectable` | 6.4% (132/2054) | 布尔 | False / True / false |
| `showInSearch` | 0.1% (1/2054) | 布尔 | false |
| `size` | 19.2% (395/2054) | 文本 | (2, 2) / (2,2) / (3,3) |
| `skyfaller` | 1.1% (22/2054) | 容器 |  |
| `skyfaller/angleCurve` | 0.3% (6/2054) | 容器 |  |
| `skyfaller/angleCurve/points` | 0.3% (6/2054) | 容器 |  |
| `skyfaller/angleCurve/points/li` | 0.6% (12/2054) | 文本 | (0,-60) / (0,-65) / (0,90) |
| `skyfaller/anticipationSound` | 0.5% (11/2054) | 文本 | DropPod_Fall / DropPod_Fall_Mechanoid / DropPod_Leaving |
| `skyfaller/anticipationSoundTicks` | 0.5% (10/2054) | 数值 | -10 / 100 / 180 |
| `skyfaller/cameraShake` | 0.1% (3/2054) | 数值 | 1 |
| `skyfaller/explosionDamage` | 0.3% (7/2054) | 文本 | Bomb / Flame |
| `skyfaller/explosionDamageFactor` | 0.1% (2/2054) | 数值 | 0.1 / 0.5 |
| `skyfaller/explosionRadius` | 0.3% (7/2054) | 数值 | 2 / 3 / 4 |
| `skyfaller/fadeOutTicks` | 0.1% (1/2054) | 数值 | 40 |
| `skyfaller/floatingSound` | 0.1% (1/2054) | 文本 | SkylanternFloating |
| `skyfaller/hitRoof` | 0.1% (1/2054) | 布尔 | false |
| `skyfaller/impactSound` | 0.2% (5/2054) | 文本 | DropPod_Impact / Shuttle_Impact / WarpedObelisk_Impact |
| `skyfaller/metalShrapnelCountRange` | 0.1% (2/2054) | 容器 |  |
| `skyfaller/metalShrapnelCountRange/max` | 0.1% (2/2054) | 数值 | 10 |
| `skyfaller/metalShrapnelCountRange/min` | 0.1% (2/2054) | 数值 | 6 |
| `skyfaller/moteSpawnTime` | 0.1% (2/2054) | 数值 | 0.05 |
| `skyfaller/motesPerCell` | 0.4% (9/2054) | 数值 | 0 / 1 |
| `skyfaller/movementType` | 0.5% (10/2054) | 文本 | Accelerate / ConstantSpeed / Decelerate |
| `skyfaller/reversed` | 0.2% (5/2054) | 布尔 | true |
| `skyfaller/rotateGraphicTowardsDirection` | 0.2% (4/2054) | 布尔 | true |
| `skyfaller/rotationCurve` | 0.3% (7/2054) | 容器 |  |
| `skyfaller/rotationCurve/points` | 0.3% (7/2054) | 容器 |  |
| `skyfaller/rotationCurve/points/li` | 1.4% (28/2054) | 文本 | (0,20) / (0.49,5) / (0.6,5) |
| `skyfaller/rubbleShrapnelCountRange` | 0.1% (2/2054) | 容器 |  |
| `skyfaller/rubbleShrapnelCountRange/max` | 0.1% (2/2054) | 数值 | 400 |
| `skyfaller/rubbleShrapnelCountRange/min` | 0.1% (2/2054) | 数值 | 300 |
| `skyfaller/shadow` | 0.4% (9/2054) | 文本 | Things/Skyfaller/SkyfallerShadowDropPod / Things/Skyfaller/SkyfallerShadowRectangle |
| `skyfaller/shadowSize` | 0.8% (16/2054) | 数值/文本 | (2, 2) / (2.5, 2.5) / (3, 3) |
| `skyfaller/shrapnelDistanceFactor` | 0.1% (1/2054) | 数值 | 0.2 |
| `skyfaller/spawnThing` | 0.1% (1/2054) | 文本 | CraterMedium |
| `skyfaller/speed` | 0.1% (3/2054) | 数值 | 0.8 / 0.9 / 1.2 |
| `skyfaller/speedCurve` | 0.4% (8/2054) | 容器 |  |
| `skyfaller/speedCurve/points` | 0.4% (8/2054) | 容器 |  |
| `skyfaller/speedCurve/points/li` | 0.8% (16/2054) | 文本 | (0.0, 0.05) / (0.4, 0.15) / (0.60,0.10) |
| `skyfaller/ticksToDiscardInReverse` | 0.1% (1/2054) | 文本 | 2700~3600 |
| `skyfaller/ticksToImpactRange` | 0.6% (12/2054) | 数值/文本 | 150~200 / 600~650 / 60~120 |
| `skyfaller/ticksToImpactRange/max` | 0.1% (1/2054) | 数值 | -15 |
| `skyfaller/ticksToImpactRange/min` | 0.1% (1/2054) | 数值 | -40 |
| `skyfaller/zPositionCurve` | 0.3% (7/2054) | 容器 |  |
| `skyfaller/zPositionCurve/points` | 0.3% (7/2054) | 容器 |  |
| `skyfaller/zPositionCurve/points/li` | 0.7% (15/2054) | 文本 | (0,0) / (0,3.5) / (0.8,2.5) |
| `slagDef` | 0.1% (1/2054) | 文本 | ChunkSlagSteel |
| `smallVolume` | 0.1% (2/2054) | 布尔 | true |
| `smeltable` | 2.1% (44/2054) | 布尔 | false / true |
| `smeltProducts` | 0.1% (1/2054) | 容器 |  |
| `smeltProducts/Steel` | 0.1% (1/2054) | 数值 | 15 |
| `socialPropernessMatters` | 1.8% (36/2054) | 布尔 | false / true |
| `soundDrop` | 1.7% (34/2054) | 文本 | Grain_Drop / Metal_Drop / Silver_Drop |
| `soundImpactDefault` | 1.5% (31/2054) | 文本 | BulletImpact_Flesh / BulletImpact_Ground / BulletImpact_Metal |
| `soundInteract` | 3.2% (65/2054) | 文本 | Bow_Recurve / Interact_Rifle / Metal_Drop |
| `soundOpen` | 0.1% (2/2054) | 文本 | DropPod_Open / DropPod_Open_Mechanoid |
| `soundPlayInstrument` | 0.1% (3/2054) | 文本 | Harp_Play / Harpsichord_Play / Piano_Play |
| `soundSpawned` | 0.1% (2/2054) | 文本 | SpitterSpawn |
| `specialDisplayRadius` | 0.7% (15/2054) | 数值 | 10.9 / 5.8 / 5.9 |
| `stackLimit` | 2.9% (59/2054) | 数值 | 1 / 10 / 5 |
| `startingHpRange` | 0.1% (3/2054) | 文本 | 0.5~1.3 |
| `startingHpRange/max` | 0.1% (1/2054) | 数值 | 1 |
| `startingHpRange/min` | 0.1% (1/2054) | 数值 | 0.5 |
| `statBases` | 62.1% (1275/2054) | 容器 |  |
| `statBases/AccuracyLong` | 2.1% (43/2054) | 数值 | 0.24 / 0.25 / 0.35 |
| `statBases/AccuracyMedium` | 2.0% (41/2054) | 数值 | 0.45 / 0.65 / 0.7 |
| `statBases/AccuracyShort` | 2.0% (41/2054) | 数值 | 0.65 / 0.70 / 0.78 |
| `statBases/AccuracyTouch` | 2.0% (41/2054) | 数值 | 0.60 / 0.70 / 0.75 |
| `statBases/ArmorRating_Blunt` | 2.6% (53/2054) | 数值 | 0.18 / 0.3 / 0.5 |
| `statBases/ArmorRating_Heat` | 1.6% (32/2054) | 数值 | 0 / 0.2 / 0.345 |
| `statBases/ArmorRating_Sharp` | 2.6% (53/2054) | 数值 | 0.2 / 0.28 / 0.5 |
| `statBases/AssemblySpeedFactor` | 0.1% (1/2054) | 数值 | 1.0 |
| `statBases/BabyPlayGainFactor` | 0.1% (2/2054) | 数值 | 1.1 / 1.25 |
| `statBases/BandwidthCost` | 0.6% (13/2054) | 数值 | 1 / 2 / 3 |
| `statBases/Beauty` | 12.1% (249/2054) | 数值 | -12 / -25 / -6 |
| `statBases/BeautyOutdoors` | 1.9% (40/2054) | 数值 | -1 / -10 / 0 |
| `statBases/BedRestEffectiveness` | 0.7% (14/2054) | 数值 | 0.85 / 0.95 / 1 |
| `statBases/BiosculpterPodSpeedFactor` | 0.1% (1/2054) | 数值 | 1 |
| `statBases/BirthRitualQualityOffset` | 0.1% (3/2054) | 数值 | 0 / 2 / 5 |
| `statBases/BluntDamageMultiplier` | 0.5% (10/2054) | 数值 | 0 / 0.9 / 1 |
| `statBases/CaravanRidingSpeedFactor` | 0.3% (7/2054) | 数值 | 1.3 / 1.6 / 2.0 |
| `statBases/CleaningSpeed` | 0.1% (1/2054) | 数值 | 0.5 |
| `statBases/Cleanliness` | 2.0% (41/2054) | 数值 | -15 / -2 / -20 |
| `statBases/Comfort` | 1.1% (22/2054) | 数值 | 0.4 / 0.55 / 0.65 |
| `statBases/ComfyTemperatureMax` | 2.4% (49/2054) | 数值 | 250 / 50 / 55 |
| `statBases/ComfyTemperatureMin` | 5.5% (113/2054) | 数值 | -100 / -40 / -55 |
| `statBases/ConstructionSpeed` | 0.1% (1/2054) | 数值 | 0.5 |
| `statBases/ConstructionSpeedFactor` | 0.1% (1/2054) | 数值 | 0.8 |
| `statBases/ControlTakingTime` | 0.3% (6/2054) | 数值 | 12 / 18 / 24 |
| `statBases/DeteriorationRate` | 3.6% (74/2054) | 数值 | 0 / 2.0 / 5 |
| `statBases/DoorOpenSpeed` | 0.1% (1/2054) | 数值 | 1.15 |
| `statBases/EMPResistance` | 0.2% (4/2054) | 数值 | 0.50 / 0.6 / 0.7 |
| `statBases/EnergyShieldEnergyMax` | 0.3% (7/2054) | 数值 | 1.5 / 2.5 / 3 |
| `statBases/EnergyShieldRechargeRate` | 0.3% (6/2054) | 数值 | 0.013 / 0.13 / 0.25 |
| `statBases/EquipDelay` | 4.5% (93/2054) | 数值 | 1 / 1.5 / 2 |
| `statBases/FilthRate` | 2.8% (58/2054) | 数值 | 2 / 20 / 4 |
| `statBases/Flammability` | 22.2% (456/2054) | 数值 | 0 / 0.4 / 0.5 |
| `statBases/FlightCooldown` | 0.3% (7/2054) | 数值 | 10 / 20 / 5 |
| `statBases/FoodPoisonChance` | 0.1% (1/2054) | 数值 | 0.001 |
| `statBases/FoodPoisonChanceFixedHuman` | 0.4% (9/2054) | 数值 | 0.01 / 0.02 / 0.04 |
| `statBases/GeneticComplexityIncrease` | 0.1% (1/2054) | 数值 | 2 |
| `statBases/GravshipRange` | 0.1% (1/2054) | 数值 | 0 |
| `statBases/ImmunityGainSpeedFactor` | 0.5% (11/2054) | 数值 | 0.95 / 1.05 / 1.07 |
| `statBases/InjuryHealingFactor` | 0.1% (1/2054) | 数值 | 0 |
| `statBases/Insulation_Cold` | 1.1% (22/2054) | 数值 | 0 / 1.5 / 3 |
| `statBases/Insulation_Heat` | 1.0% (21/2054) | 数值 | 0 / 1.5 / 2 |
| `statBases/JoyGainFactor` | 0.7% (14/2054) | 数值 | 0.8 / 1 / 1.25 |
| `statBases/JumpRange` | 0.1% (2/2054) | 数值 | 23.9 |
| `statBases/LeatherAmount` | 1.0% (21/2054) | 数值 | 0 / 20 / 36 |
| `statBases/MarketValue` | 17.5% (359/2054) | 数值 | 200 / 250 / 60 |
| `statBases/Mass` | 23.9% (490/2054) | 数值 | 0.3 / 3 / 30 |
| `statBases/MaxFlightTime` | 0.4% (9/2054) | 数值 | 10 / 3 / 30 |
| `statBases/MaxHitPoints` | 32.4% (665/2054) | 数值 | 100 / 150 / 35 |
| `statBases/MaxInstallCount` | 0.2% (5/2054) | 数值 | 3 / 6 |
| `statBases/MeatAmount` | 0.6% (12/2054) | 数值 | 0 / 140 / 2 |
| `statBases/MechEnergyLossPerHP` | 0.2% (5/2054) | 数值 | 0.15 / 0.2 / 0.33 |
| `statBases/MedicalPotency` | 0.1% (3/2054) | 数值 | 0.60 / 1.00 / 1.60 |
| `statBases/MedicalQualityMax` | 0.1% (3/2054) | 数值 | 0.70 / 1.00 / 1.30 |
| `statBases/MedicalTendQualityOffset` | 0.1% (1/2054) | 数值 | 0.10 |
| `statBases/MeditationFocusStrength` | 1.0% (20/2054) | 数值 | 0 / 0.08 / 0.24 |
| `statBases/MeditationPlantGrowthOffset` | 0.1% (1/2054) | 数值 | 0 |
| `statBases/MeleeDoorDamageFactor` | 0.1% (2/2054) | 数值 | 1.5 |
| `statBases/MinimumContainmentStrength` | 0.6% (12/2054) | 数值 | 110 / 30 / 60 |
| `statBases/MinimumHandlingSkill` | 0.1% (1/2054) | 数值 | 5 |
| `statBases/MoveSpeed` | 6.7% (137/2054) | 数值 | 0 / 3.2 / 4.83 |
| `statBases/Nutrition` | 4.9% (101/2054) | 数值 | 0.05 / 0.1 / 0.25 |
| `statBases/PackRadius` | 0.1% (2/2054) | 数值 | 4.9 |
| `statBases/PainShockThreshold` | 0.1% (1/2054) | 数值 | 100 |
| `statBases/PlantWorkSpeed` | 0.1% (1/2054) | 数值 | 0.80 |
| `statBases/PsychicSensitivity` | 0.6% (13/2054) | 数值 | 0.5 / 1 / 1.5 |
| `statBases/RangedWeapon_Cooldown` | 2.5% (52/2054) | 数值 | 1.65 / 1.70 / 3 |
| `statBases/ResearchSpeedFactor` | 0.1% (2/2054) | 数值 | 0.75 / 1.0 |
| `statBases/RoyalFavorValue` | 0.1% (2/2054) | 数值 | 0.015 / 3 |
| `statBases/SellPriceFactor` | 0.2% (4/2054) | 数值 | 0.20 / 0.70 / 1 |
| `statBases/SharpDamageMultiplier` | 0.6% (12/2054) | 数值 | 0 / 0.75 / 0.85 |
| `statBases/ShootingAccuracyTurret` | 0.5% (11/2054) | 数值 | 0.9 / 0.96 / 0.98 |
| `statBases/StaggerDurationFactor` | 0.1% (1/2054) | 数值 | 0 |
| `statBases/StuffEffectMultiplierArmor` | 2.3% (47/2054) | 数值 | 0.2 / 0.3 / 0.4 |
| `statBases/StuffEffectMultiplierInsulation_Cold` | 2.3% (48/2054) | 数值 | 0.2 / 0.22 / 0.5 |
| `statBases/StuffEffectMultiplierInsulation_Heat` | 2.3% (48/2054) | 数值 | 0.08 / 0.1 / 0.10 |
| `statBases/StuffPower_Armor_Blunt` | 1.3% (26/2054) | 数值 | 0.24 / 0.36 / 0.45 |
| `statBases/StuffPower_Armor_Heat` | 0.8% (17/2054) | 数值 | 0.36 / 0.5 / 0.60 |
| `statBases/StuffPower_Armor_Sharp` | 1.8% (38/2054) | 数值 | 0.72 / 0.9 / 1.1 |
| `statBases/StuffPower_Insulation_Cold` | 2.2% (46/2054) | 数值 | 2.5 / 20 / 3 |
| `statBases/StuffPower_Insulation_Heat` | 2.1% (44/2054) | 数值 | 0 / 12 / 18 |
| `statBases/StyleDominance` | 1.5% (30/2054) | 数值 | 10 / 20 / 40 |
| `statBases/SubstructureSupport` | 0.1% (1/2054) | 数值 | 500 |
| `statBases/SurgerySuccessChanceFactor` | 0.5% (11/2054) | 数值 | 0.65 / 0.7 / 1 |
| `statBases/TerrorSource` | 0.1% (3/2054) | 数值 | 0 / 25 |
| `statBases/ToxicEnvironmentResistance` | 0.9% (19/2054) | 数值 | 0.8 / 0.9 / 0.95 |
| `statBases/ToxicResistance` | 1.0% (21/2054) | 数值 | 0.5 / 0.8 / 1 |
| `statBases/TrapMeleeDamage` | 0.1% (1/2054) | 数值 | 100 |
| `statBases/TrapSpringChance` | 0.2% (4/2054) | 数值 | 1.0 |
| `statBases/VacuumResistance` | 0.3% (6/2054) | 数值 | 1 |
| `statBases/WastepacksPerRecharge` | 0.1% (1/2054) | 数值 | 5 |
| `statBases/Wildness` | 4.8% (98/2054) | 数值 | 0 / 0.8 / 0.85 |
| `statBases/WorkSpeedGlobal` | 0.1% (3/2054) | 数值 | 0.5 / 1.5 |
| `statBases/WorkTableEfficiencyFactor` | 0.1% (1/2054) | 数值 | 0.7 |
| `statBases/WorkTableWorkSpeedFactor` | 0.1% (3/2054) | 数值 | 0.5 |
| `statBases/WorkToBuild` | 14.5% (297/2054) | 数值 | 0 / 1800 / 2000 |
| `statBases/WorkToMake` | 8.1% (167/2054) | 数值 | 13200 / 24000 / 6000 |
| `staticSunShadowHeight` | 3.9% (80/2054) | 数值 | 0 / 0.15 / 0.20 |
| `stealable` | 0.9% (18/2054) | 布尔 | false / true |
| `storedConceptLearnOpportunity` | 0.1% (1/2054) | 文本 | DrugPolicies |
| `stuffCategories` | 8.2% (168/2054) | 容器 |  |
| `stuffCategories/li` | 15.2% (313/2054) | 文本 | Bioferrite / Fabric / Leathery |
| `stuffProps` | 2.8% (58/2054) | 容器 |  |
| `stuffProps/allowColorGenerators` | 0.1% (1/2054) | 布尔 | true |
| `stuffProps/allowedInStuffGeneration` | 0.1% (2/2054) | 布尔 | false |
| `stuffProps/appearance` | 0.4% (9/2054) | 文本 | Bricks / Metal / Planks |
| `stuffProps/canSuggestUseDefaultStuff` | 0.6% (12/2054) | 布尔 | true |
| `stuffProps/categories` | 0.8% (16/2054) | 容器 |  |
| `stuffProps/categories/li` | 0.9% (18/2054) | 文本 | Bioferrite / Metallic / Stony |
| `stuffProps/color` | 2.6% (54/2054) | 文本 | (100, 80, 80) / (112,89,43) / (180,173,150) |
| `stuffProps/commonality` | 2.1% (44/2054) | 数值 | 0 / 0.02 / 0.05 |
| `stuffProps/constructEffect` | 0.5% (10/2054) | 文本 | ConstructMetal / ConstructWood |
| `stuffProps/isAirtight` | 0.3% (6/2054) | 布尔 | true |
| `stuffProps/soundImpactBullet` | 0.8% (16/2054) | 文本 | BulletImpact_Ground / BulletImpact_Metal / BulletImpact_Wood |
| `stuffProps/soundImpactMelee` | 0.8% (16/2054) | 文本 | Pawn_Melee_Punch_HitBuilding_Metal / Pawn_Melee_Punch_HitBuilding_Stone / Pawn_Melee_Punch_HitBuilding_Wood |
| `stuffProps/soundMeleeHitBlunt` | 0.8% (16/2054) | 文本 | MeleeHit_Metal_Blunt / MeleeHit_Stone / MeleeHit_Wood |
| `stuffProps/soundMeleeHitSharp` | 0.8% (16/2054) | 文本 | MeleeHit_Metal_Sharp / MeleeHit_Stone / MeleeHit_Wood |
| `stuffProps/statFactors` | 2.2% (46/2054) | 容器 |  |
| `stuffProps/statFactors/Beauty` | 1.9% (39/2054) | 数值 | 0.25 / 1 / 2 |
| `stuffProps/statFactors/BedRestEffectiveness` | 0.1% (3/2054) | 数值 | 0.85 / 0.9 |
| `stuffProps/statFactors/DoorOpenSpeed` | 0.2% (4/2054) | 数值 | 0.45 / 0.75 / 1 |
| `stuffProps/statFactors/Flammability` | 0.8% (16/2054) | 数值 | 0 / 0.4 / 0.75 |
| `stuffProps/statFactors/MarketValue` | 0.1% (1/2054) | 数值 | 0.4 |
| `stuffProps/statFactors/MaxHitPoints` | 1.8% (38/2054) | 数值 | 0.6 / 0.7 / 1 |
| `stuffProps/statFactors/MeleeWeapon_CooldownMultiplier` | 0.3% (7/2054) | 数值 | 0.8 / 1 / 1.0 |
| `stuffProps/statFactors/WorkToBuild` | 0.5% (10/2054) | 数值 | 0.7 / 0.9 / 2.2 |
| `stuffProps/statFactors/WorkToMake` | 0.5% (10/2054) | 数值 | 0.7 / 0.9 / 2.2 |
| `stuffProps/statFactorsQuality` | 0.1% (1/2054) | 容器 |  |
| `stuffProps/statFactorsQuality/li` | 0.1% (1/2054) | 容器 |  |
| `stuffProps/statFactorsQuality/li/awful` | 0.1% (1/2054) | 数值 | 1.06 |
| `stuffProps/statFactorsQuality/li/excellent` | 0.1% (1/2054) | 数值 | 1.15 |
| `stuffProps/statFactorsQuality/li/good` | 0.1% (1/2054) | 数值 | 1.13 |
| `stuffProps/statFactorsQuality/li/legendary` | 0.1% (1/2054) | 数值 | 1.20 |
| `stuffProps/statFactorsQuality/li/masterwork` | 0.1% (1/2054) | 数值 | 1.17 |
| `stuffProps/statFactorsQuality/li/normal` | 0.1% (1/2054) | 数值 | 1.1 |
| `stuffProps/statFactorsQuality/li/poor` | 0.1% (1/2054) | 数值 | 1.08 |
| `stuffProps/statFactorsQuality/li/stat` | 0.1% (1/2054) | 文本 | PsychicSensitivityFactor |
| `stuffProps/statOffsets` | 0.4% (8/2054) | 容器 |  |
| `stuffProps/statOffsets/Beauty` | 0.3% (7/2054) | 数值 | 0 / 10 / 20 |
| `stuffProps/statOffsets/WorkToBuild` | 0.1% (1/2054) | 数值 | 140 |
| `stuffProps/statOffsetsQuality` | 0.1% (1/2054) | 容器 |  |
| `stuffProps/statOffsetsQuality/li` | 0.1% (2/2054) | 容器 |  |
| `stuffProps/statOffsetsQuality/li/awful` | 0.1% (2/2054) | 数值 | 0.04 / 4 |
| `stuffProps/statOffsetsQuality/li/excellent` | 0.1% (2/2054) | 数值 | 0.04 / 13 |
| `stuffProps/statOffsetsQuality/li/good` | 0.1% (2/2054) | 数值 | 0.04 / 11 |
| `stuffProps/statOffsetsQuality/li/legendary` | 0.1% (2/2054) | 数值 | 0.04 / 18 |
| `stuffProps/statOffsetsQuality/li/masterwork` | 0.1% (2/2054) | 数值 | 0.04 / 15 |
| `stuffProps/statOffsetsQuality/li/normal` | 0.1% (2/2054) | 数值 | 0.04 / 8 |
| `stuffProps/statOffsetsQuality/li/poor` | 0.1% (2/2054) | 数值 | 0.04 / 6 |
| `stuffProps/statOffsetsQuality/li/stat` | 0.1% (2/2054) | 文本 | PsychicEntropyMaxOffset / PsychicEntropyRecoveryRateOffset |
| `stuffProps/stuffAdjective` | 0.4% (8/2054) | 文本 | golden / granite / sandstone |
| `surfaceType` | 1.5% (30/2054) | 文本 | Eat / Item / None |
| `techHediffsTags` | 1.4% (28/2054) | 容器 |  |
| `techHediffsTags/li` | 1.4% (29/2054) | 文本 | Advanced / Anomaly / Ghoul |
| `techLevel` | 6.1% (126/2054) | 文本 | Archotech / Industrial / Medieval |
| `terrainAffordanceNeeded` | 8.3% (170/2054) | 容器/文本 | Diggable / Heavy / Light |
| `thingCategories` | 12.7% (260/2054) | 容器 |  |
| `thingCategories/li` | 12.4% (255/2054) | 文本 | BodyPartsGhoul / BuildingsArt / BuildingsMisc |
| `thingClass` | 23.3% (479/2054) | 文本 | Book / MoteThrownAttached / Projectile_Explosive |
| `thingSetMakerTags` | 6.6% (135/2054) | 容器 |  |
| `thingSetMakerTags/li` | 7.3% (150/2054) | 文本 | RewardStandardHighFreq / RewardStandardLowFreq / RewardStandardMidFreq |
| `tickerType` | 13.9% (285/2054) | 文本 | Long / Never / Normal |
| `tools` | 8.9% (183/2054) | 容器 |  |
| `tools/li` | 24.2% (498/2054) | 容器 |  |
| `tools/li/alwaysTreatAsWeapon` | 1.5% (30/2054) | 布尔 | true |
| `tools/li/armorPenetration` | 0.4% (8/2054) | 数值 | 0.2 / 0.50 / 0.8 |
| `tools/li/capacities` | 24.2% (498/2054) | 容器 |  |
| `tools/li/capacities/li` | 28.3% (581/2054) | 文本 | Blunt / Cut / Poke |
| `tools/li/chanceFactor` | 8.7% (178/2054) | 数值 | 0.1 / 0.2 / 0.5 |
| `tools/li/cooldownTime` | 24.2% (498/2054) | 数值 | 1.25 / 1.5 / 2 |
| `tools/li/ensureLinkedBodyPartsGroupAlwaysUsable` | 5.9% (122/2054) | 布尔 | true |
| `tools/li/extraMeleeDamages` | 0.3% (7/2054) | 容器 |  |
| `tools/li/extraMeleeDamages/li` | 0.3% (7/2054) | 容器 |  |
| `tools/li/extraMeleeDamages/li/amount` | 0.3% (7/2054) | 数值 | 10 / 3 / 9 |
| `tools/li/extraMeleeDamages/li/chance` | 0.2% (4/2054) | 数值 | 0.5 / 0.7 |
| `tools/li/extraMeleeDamages/li/def` | 0.3% (7/2054) | 文本 | EMP / Flame / Stun |
| `tools/li/label` | 21.0% (431/2054) | 文本 | barrel / head / limb |
| `tools/li/labelNoLocation` | 7.3% (151/2054) | 文本 | blade / claw / fin |
| `tools/li/labelUsedInLogging` | 0.3% (6/2054) | 布尔 | false |
| `tools/li/linkedBodyPartsGroup` | 19.0% (390/2054) | 文本 | HeadAttackTool / LeftBlade / RightBlade |
| `tools/li/power` | 24.2% (498/2054) | 数值 | 20 / 3 / 7.0 |
| `tools/li/soundMeleeHit` | 0.9% (19/2054) | 文本 | Pawn_Dreadmeld_Attack_Spike / Pawn_Fleshbeast_Attack_Blunt / Pawn_Fleshbeast_Attack_Spike |
| `tools/li/soundMeleeMiss` | 0.1% (1/2054) | 文本 | Pawn_Melee_HumanBite_Miss |
| `tools/li/surpriseAttack` | 2.4% (49/2054) | 容器 |  |
| `tools/li/surpriseAttack/extraMeleeDamages` | 2.4% (49/2054) | 容器 |  |
| `tools/li/surpriseAttack/extraMeleeDamages/li` | 2.4% (49/2054) | 容器 |  |
| `tools/li/surpriseAttack/extraMeleeDamages/li/amount` | 2.4% (49/2054) | 数值 | 10 / 14 / 16 |
| `tools/li/surpriseAttack/extraMeleeDamages/li/def` | 2.4% (49/2054) | 文本 | Stun |
| `tradeability` | 3.5% (72/2054) | 文本 | Buyable / None / Sellable |
| `tradeNeverGenerateStacked` | 0.1% (2/2054) | 布尔 | true |
| `tradeNeverStack` | 0.6% (13/2054) | 布尔 | true |
| `tradeTags` | 11.4% (234/2054) | 容器 |  |
| `tradeTags/li` | 14.1% (290/2054) | 文本 | ExoticMisc / HoraxArmor / Serum |
| `uiIconColor` | 0.1% (1/2054) | 文本 | (105,105,105) |
| `uiIconColorTwo` | 0.1% (1/2054) | 文本 | (161,213,180) |
| `uiIconForStackCount` | 0.1% (2/2054) | 数值 | 1 |
| `uiIconOffset` | 0.7% (15/2054) | 文本 | (0, -0.05) / (0, 0.02) / (0, 0.03) |
| `uiIconPath` | 3.5% (72/2054) | 文本 | Things/Building/FleshmassHeart / Things/Building/Linked/GreyWall_MenuIcon / Things/Item/Book/Tome/Tome |
| `uiIconPathsStuff` | 0.1% (2/2054) | 容器 |  |
| `uiIconPathsStuff/li` | 0.1% (3/2054) | 容器 |  |
| `uiIconPathsStuff/li/appearance` | 0.1% (3/2054) | 文本 | Bricks / Metal / Planks |
| `uiIconPathsStuff/li/iconPath` | 0.1% (3/2054) | 文本 | Things/Building/Linked/FenceMetal_MenuIcon / Things/Building/Linked/WallBricks_MenuIcon / Things/Building/Link |
| `uiIconScale` | 7.3% (150/2054) | 数值 | 0.7 / 0.75 / 0.8 |
| `uiOrder` | 7.4% (152/2054) | 数值 | 100 / 105 / 106 |
| `useBlueprintGraphicAsGhost` | 0.2% (4/2054) | 布尔 | true |
| `useHitPoints` | 7.4% (153/2054) | 布尔 | False / True / false |
| `useSameGraphicForGhost` | 0.1% (1/2054) | 布尔 | true |
| `useStuffTerrainAffordance` | 0.4% (8/2054) | 布尔 | false / true |
| `verbs` | 3.9% (80/2054) | 容器 |  |
| `verbs/li` | 3.9% (80/2054) | 容器 |  |
| `verbs/li/ai_AvoidFriendlyFireRadius` | 0.5% (10/2054) | 数值 | 3 / 5 / 6 |
| `verbs/li/ai_BeamIsIncendiary` | 0.1% (1/2054) | 布尔 | true |
| `verbs/li/ai_IsBuildingDestroyer` | 0.4% (8/2054) | 布尔 | false / true |
| `verbs/li/ai_ProjectileLaunchingIgnoresMeleeThreats` | 0.1% (1/2054) | 布尔 | true |
| `verbs/li/ai_RangedAlawaysShootGroundBelowTarget` | 0.1% (1/2054) | 布尔 | true |
| `verbs/li/ai_TargetHasRangedAttackScoreOffset` | 0.1% (1/2054) | 数值 | 50 |
| `verbs/li/aimingChargeMote` | 0.1% (2/2054) | 文本 | Mote_BeamRepeater_Charge / Mote_HellsphereCannon_Charge |
| `verbs/li/aimingChargeMoteOffset` | 0.1% (2/2054) | 数值 | 1.07 |
| `verbs/li/aimingLineMote` | 0.1% (1/2054) | 文本 | Mote_HellsphereCannon_Aim |
| `verbs/li/aimingLineMoteFixedLength` | 0.1% (1/2054) | 数值 | 15.9 |
| `verbs/li/aimingTargetEffecter` | 0.1% (1/2054) | 文本 | BiomutationLanceWarmup |
| `verbs/li/aimingTargetMote` | 0.1% (1/2054) | 文本 | Mote_HellsphereCannon_Target |
| `verbs/li/beamCantHitWithinMinRange` | 0.1% (1/2054) | 布尔 | true |
| `verbs/li/beamChanceToAttachFire` | 0.1% (1/2054) | 数值 | 0.85 |
| `verbs/li/beamChanceToStartFire` | 0.1% (2/2054) | 数值 | 0.85 |
| `verbs/li/beamCurvature` | 0.1% (2/2054) | 数值 | 0 / 0.6 |
| `verbs/li/beamDamageDef` | 0.1% (2/2054) | 文本 | Beam / Flame |
| `verbs/li/beamEndEffecterDef` | 0.1% (2/2054) | 文本 | GraserBeam_End / IncineratorBeam_End |
| `verbs/li/beamFireSizeRange` | 0.1% (2/2054) | 文本 | 0.55~0.85 |
| `verbs/li/beamFleckChancePerTick` | 0.1% (2/2054) | 数值 | 0.32 |
| `verbs/li/beamFullWidthRange` | 0.1% (2/2054) | 数值 | 11 / 6.9 |
| `verbs/li/beamGroundFleckDef` | 0.1% (2/2054) | 文本 | Fleck_BeamBurn / Fleck_IncineratorBeamBurn |
| `verbs/li/beamHitsNeighborCells` | 0.1% (1/2054) | 布尔 | true |
| `verbs/li/beamHitsNeighborCellsRequiresLOS` | 0.1% (1/2054) | 布尔 | true |
| `verbs/li/beamLineFleckChanceCurve` | 0.1% (2/2054) | 容器 |  |
| `verbs/li/beamLineFleckChanceCurve/points` | 0.1% (2/2054) | 容器 |  |
| `verbs/li/beamLineFleckChanceCurve/points/li` | 0.3% (6/2054) | 文本 | (0, 0) / (0.65, 0.02) / (0.65, 0.4) |
| `verbs/li/beamLineFleckDef` | 0.1% (2/2054) | 文本 | Fleck_BeamSpark / Fleck_IncineratorBeamSmoke |
| `verbs/li/beamMaxDeviation` | 0.1% (2/2054) | 数值 | 0.5 / 1.5 |
| `verbs/li/beamMoteDef` | 0.1% (1/2054) | 文本 | Mote_GraserBeamBase |
| `verbs/li/beamSetsGroundOnFire` | 0.1% (1/2054) | 布尔 | true |
| `verbs/li/beamStartOffset` | 0.1% (2/2054) | 数值 | .5 / 0.8 |
| `verbs/li/beamTargetsGround` | 0.1% (1/2054) | 布尔 | true |
| `verbs/li/beamWidth` | 0.1% (2/2054) | 数值 | 6 |
| `verbs/li/burstShotCount` | 2.2% (46/2054) | 数值 | 1 / 2 / 20 |
| `verbs/li/canGoWild` | 0.2% (5/2054) | 布尔 | false |
| `verbs/li/colonyWideTaleDef` | 0.1% (1/2054) | 文本 | TornadoFromItem |
| `verbs/li/commandIcon` | 0.1% (1/2054) | 文本 | Things/Pawn/Humanlike/Apparel/JumpPack/JumpPack |
| `verbs/li/consumeFuelPerBurst` | 0.1% (1/2054) | 数值 | 1 |
| `verbs/li/consumeFuelPerShot` | 0.3% (6/2054) | 数值 | 1 |
| `verbs/li/defaultCooldownTime` | 0.1% (1/2054) | 数值 | 2.5 |
| `verbs/li/defaultProjectile` | 3.0% (61/2054) | 文本 | Bullet_Shell_AcidSpit / Bullet_TacticalTurret / Grenade_DisruptorFlare |
| `verbs/li/drawHighlightWithLineOfSight` | 0.1% (2/2054) | 布尔 | true |
| `verbs/li/ensureLinkedBodyPartsGroupAlwaysUsable` | 0.1% (1/2054) | 布尔 | true |
| `verbs/li/explosionRadiusRingColor` | 0.1% (1/2054) | 文本 | (0.8, 0.8, 0.4, 1) |
| `verbs/li/flammabilityAttachFireChanceCurve` | 0.1% (1/2054) | 容器 |  |
| `verbs/li/flammabilityAttachFireChanceCurve/points` | 0.1% (1/2054) | 容器 |  |
| `verbs/li/flammabilityAttachFireChanceCurve/points/li` | 0.1% (3/2054) | 文本 | (0.6, 0) / (0.7, 0.2) / (1.2, 0.8) |
| `verbs/li/flightEffecterDef` | 0.1% (2/2054) | 文本 | JumpFlightEffect |
| `verbs/li/forcedMissEvenDispersal` | 0.1% (1/2054) | 布尔 | true |
| `verbs/li/forcedMissRadius` | 1.0% (20/2054) | 数值 | 0.1 / 1.9 / 3 |
| `verbs/li/forcedMissRadiusClassicMortars` | 0.1% (1/2054) | 数值 | 13 |
| `verbs/li/forceNormalTimeSpeed` | 0.2% (4/2054) | 布尔 | false |
| `verbs/li/hasStandardCommand` | 3.3% (68/2054) | 布尔 | true |
| `verbs/li/highlightColor` | 0.1% (1/2054) | 文本 | (180, 60, 10) |
| `verbs/li/invalidTargetPawn` | 0.2% (4/2054) | 文本 | psychic insanity immune / psychic shock immune |
| `verbs/li/isMortar` | 0.1% (2/2054) | 布尔 | true |
| `verbs/li/label` | 1.0% (21/2054) | 文本 | deploy deadlife dust / deploy flare / deploy turret |
| `verbs/li/linkedBodyPartsGroup` | 0.1% (1/2054) | 文本 | BulbTurret |
| `verbs/li/minRange` | 0.5% (10/2054) | 数值 | 29.9 / 3.9 / 5.9 |
| `verbs/li/muzzleFlashScale` | 2.4% (49/2054) | 数值 | 14 / 16 / 6 |
| `verbs/li/noiseRadius` | 0.3% (7/2054) | 数值 | 4 |
| `verbs/li/nonInterruptingSelfCast` | 0.2% (4/2054) | 布尔 | true |
| `verbs/li/onlyManualCast` | 1.1% (22/2054) | 布尔 | True / true |
| `verbs/li/range` | 3.6% (74/2054) | 数值 | 19.9 / 22.9 / 23.9 |
| `verbs/li/rangedFireRulepack` | 0.6% (12/2054) | 文本 | Combat_RangedFire_Thrown / Combat_RangedFlamethrower |
| `verbs/li/requireLineOfSight` | 0.3% (6/2054) | 布尔 | false / true |
| `verbs/li/secondaryHighlightColor` | 0.1% (1/2054) | 文本 | (220, 210, 20) |
| `verbs/li/showBurstShotStats` | 0.1% (2/2054) | 布尔 | false |
| `verbs/li/soundAiming` | 0.5% (10/2054) | 文本 | BiomutationLanceWarmup / HellsphereCannon_Aiming / OrbitalTargeter_Aiming |
| `verbs/li/soundCast` | 3.5% (71/2054) | 文本 | FlareLaunch / GunShotA / SpitterSpit |
| `verbs/li/soundCastBeam` | 0.1% (2/2054) | 文本 | BeamGraser_Shooting / Flamethrower_Firing |
| `verbs/li/soundCastTail` | 2.3% (47/2054) | 文本 | GunTail_Heavy / GunTail_Light / GunTail_Medium |
| `verbs/li/soundLanding` | 0.1% (1/2054) | 文本 | JumpPackLand |
| `verbs/li/spawnDef` | 0.1% (1/2054) | 文本 | Tornado |
| `verbs/li/sprayArching` | 0.1% (1/2054) | 数值 | 1.5 |
| `verbs/li/sprayEffecterDef` | 0.1% (1/2054) | 文本 | FoamSpray_Directional |
| `verbs/li/sprayNumExtraCells` | 0.1% (1/2054) | 数值 | 40 |
| `verbs/li/sprayThicknessCells` | 0.1% (1/2054) | 数值 | 4 |
| `verbs/li/sprayWidth` | 0.1% (1/2054) | 数值 | 5.5 |
| `verbs/li/stopBurstWithoutLos` | 0.1% (1/2054) | 布尔 | false |
| `verbs/li/targetable` | 0.6% (13/2054) | 布尔 | false / true |
| `verbs/li/targetParams` | 1.7% (34/2054) | 容器 |  |
| `verbs/li/targetParams/canTargetBuildings` | 0.6% (12/2054) | 布尔 | false |
| `verbs/li/targetParams/canTargetLocations` | 1.4% (29/2054) | 布尔 | true |
| `verbs/li/targetParams/canTargetPawns` | 0.4% (8/2054) | 布尔 | false |
| `verbs/li/targetParams/neverTargetIncapacitated` | 0.2% (5/2054) | 布尔 | true |
| `verbs/li/ticksBetweenBurstShots` | 1.3% (26/2054) | 数值 | 10 / 2 / 4 |
| `verbs/li/useableInPocketMaps` | 0.2% (4/2054) | 布尔 | false |
| `verbs/li/useableInVacuum` | 0.1% (1/2054) | 布尔 | false |
| `verbs/li/verbClass` | 3.9% (80/2054) | 文本 | Verb_LaunchProjectileStatic / Verb_LaunchProjectileStaticOneUse / Verb_LaunchProjectileStaticPsychic |
| `verbs/li/violent` | 0.4% (8/2054) | 布尔 | false |
| `verbs/li/warmupEffecter` | 0.1% (2/2054) | 文本 | JumpWarmupEffect |
| `verbs/li/warmupTime` | 3.5% (73/2054) | 数值 | 0 / 0.5 / 1.0 |
| `violentTechHediff` | 0.2% (5/2054) | 布尔 | true |
| `weaponClasses` | 3.1% (63/2054) | 容器 |  |
| `weaponClasses/li` | 4.2% (86/2054) | 文本 | LongShots / Ranged / RangedHeavy |
| `weaponTags` | 3.1% (63/2054) | 容器 |  |
| `weaponTags/li` | 4.2% (86/2054) | 文本 | AssaultRifle / Flamethrower / IndustrialGunAdvanced |
| `wipesPlants` | 0.1% (1/2054) | 布尔 | true |

## 四、原版 defName 一览（共 2054 个，列出前 60）

```text
`Fleshmass_Active`                ``                                ``                                `MinifiedGravEngine`            
`PitGateExit`                     `FleshbeastGroundSpawner`         ``                                `Mote_ProgressBarAlwaysVisible` 
``                                `MinifiedThingRealtimeDraw`       `SignalAction_Letter`             `SignalAction_Ambush`           
`SignalAction_Message`            `SignalAction_SoundOneShot`       `SignalAction_OpenDoor`           `SignalAction_Incident`         
`SignalAction_OpenCasket`         `SignalAction_Infestation`        `SignalAction_DormancyWakeUp`     `SignalAction_StartWick`        
`SignalAction_Delay`              `Proj_GrenadeFrag`                `Mech_CentipedeBlaster`           `Mech_CentipedeGunner`          
`Mech_CentipedeBurner`            ``                                ``                                `PawnFlyer_ConsumeLeap`         
`Filth_GrayFleshNoticeable`       `MechGestatorCycleComplete_South`  `MechGestatorCycleComplete_East`  `MechGestatorCycleComplete_North`
`MechGestatorFormed_South`        `MechGestatorFormed_East`         `MechGestatorFormed_North`        `MechGestatorCycleCompleteLarge_South`
`MechGestatorCycleCompleteLarge_East`  `MechGestatorCycleCompleteLarge_West`  `MechGestatorCycleCompleteLarge_North`  `MechGestatorFormedLarge_South` 
`MechGestatorFormedLarge_East`    `MechGestatorFormedLarge_West`    `MechGestatorFormedLarge_North`   `Mote_SubcoreEncoderNorth`      
`Mote_SubcoreEncoderSouth`        `Mote_SubcoreEncoderEast`         `Mote_CoagulateA`                 `Mote_CoagulateB`               
``                                ``                                `Mote_ThoughtGood`                `Mote_ThoughtBad`               
`Mote_CocoonBreaking`             ``                                ``                                `MinifiedTree`                  
`MeteoriteCraterIncoming`         ``                                ``                                ``                              
```

_余下 1994 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
