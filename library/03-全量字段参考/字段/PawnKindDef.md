# PawnKindDef

- **所属线**：人物线
- **原版实例数**：333
- **字段路径数**：277
- **资料片**：Anomaly、Biotech、Core、Ideology、Odyssey、Royalty
- **原版出处**：`Core/Defs/ThingDefs_Races/Races_Animal_Base.xml`、`Biotech/Defs/ThingDefs_Races/Races_Mechanoids_SuperHeavy.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<PawnKindDef Name="AnimalKindBase" Abstract="True">
  </PawnKindDef>
  
```

> 来自 `Core/Defs/ThingDefs_Races/Races_Animal_Base.xml`，defName = ``，XML 节点数 1（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
lifeStages/li                                  [容器]
lifeStages/li/bodyGraphicData                  [容器]
lifeStages/li/bodyGraphicData/drawSize         [数值]  例：1.2 / 1.6 / 1.7
lifeStages/li/bodyGraphicData/texPath          [文本]  例：Things/Pawn/Metalhorror/Metalhorror_Juvenile / Things/Pawn/Metalhorror/Metalhorror_Larva / Things/Pawn/Metalhorror/Metalhorror_Mature
lifeStages/li/dessicatedBodyGraphicData        [容器]
lifeStages/li/dessicatedBodyGraphicData/drawSize [数值]  例：1.7 / 2 / 2.7
lifeStages/li/dessicatedBodyGraphicData/texPath [文本]  例：Things/Pawn/Devourer/Dessicated_Devourer / Things/Pawn/Gorehulk/Dessicated_Gorehulk / Things/Pawn/Noctol/Dessicated_Noctol
```

## 三、全量字段表（277 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `abilities` | 4.8% (16/333) | 容器 |  |
| `abilities/li` | 6.3% (21/333) | 文本 | AgonyPulse / EntitySkip / FleshmelterBolt |
| `acceptArrestChanceFactor` | 0.3% (1/333) | 数值 | 0.5 |
| `aiAvoidCover` | 0.9% (3/333) | 布尔 | true |
| `allowInMechClusters` | 2.7% (9/333) | 布尔 | false |
| `allowOldAgeInjuries` | 1.2% (4/333) | 布尔 | false |
| `allowRoyalApparelRequirements` | 0.3% (1/333) | 布尔 | False |
| `allowRoyalRoomRequirements` | 0.6% (2/333) | 布尔 | False |
| `alternateGraphicChance` | 2.1% (7/333) | 数值 | 0.75 / 0.8 / 0.833 |
| `alternateGraphics` | 2.1% (7/333) | 容器 |  |
| `alternateGraphics/li` | 8.1% (27/333) | 容器 |  |
| `alternateGraphics/li/attachPoints` | 3.3% (11/333) | 容器 |  |
| `alternateGraphics/li/attachPoints/li` | 13.2% (44/333) | 容器 |  |
| `alternateGraphics/li/attachPoints/li/offset` | 13.2% (44/333) | 文本 | (-.1, 0, .4) / (-.15, 0, -.2) / (.25, 0, -.2) |
| `alternateGraphics/li/attachPoints/li/type` | 13.2% (44/333) | 文本 | PlatformRestraint0 / PlatformRestraint1 / PlatformRestraint2 |
| `alternateGraphics/li/color` | 0.6% (2/333) | 文本 | (0.333,0.333,0.333,1) / (0.494,0.356,0.164,1) |
| `alternateGraphics/li/dessicatedGraphicData` | 3.3% (11/333) | 容器 |  |
| `alternateGraphics/li/dessicatedGraphicData/attachPoints` | 3.3% (11/333) | 容器 |  |
| `alternateGraphics/li/dessicatedGraphicData/attachPoints/li` | 13.2% (44/333) | 容器 |  |
| `alternateGraphics/li/dessicatedGraphicData/attachPoints/li/offset` | 13.2% (44/333) | 文本 | (-.15, 0, -.6) / (-.2, 0, .3) / (.12, 0, -.55) |
| `alternateGraphics/li/dessicatedGraphicData/attachPoints/li/type` | 13.2% (44/333) | 文本 | PlatformRestraint0 / PlatformRestraint1 / PlatformRestraint2 |
| `alternateGraphics/li/dessicatedGraphicData/drawSize` | 0.9% (3/333) | 数值 | 1.7 |
| `alternateGraphics/li/dessicatedGraphicData/texPath` | 0.9% (3/333) | 文本 | Things/Pawn/Sightstealer/Dessicated_Sightstealer |
| `alternateGraphics/li/dessicatedTexPath` | 3.3% (11/333) | 文本 | Things/Pawn/Chimera/Dessicated/DessicatedChimera_B / Things/Pawn/Chimera/Dessicated/DessicatedChimera_C / Thin |
| `alternateGraphics/li/stationaryTexPath` | 0.9% (3/333) | 文本 | Things/Pawn/Animal/HermitCrab/HermitCrabA_Stationary / Things/Pawn/Animal/HermitCrab/HermitCrabB_Stationary /  |
| `alternateGraphics/li/texPath` | 7.5% (25/333) | 文本 | Things/Pawn/Gorehulk/Gorehulk_F / Things/Pawn/Sightstealer/Sightstealer_B / Things/Pawn/Sightstealer/Sightstea |
| `apparelAllowHeadgearChance` | 15.3% (51/333) | 数值 | 0 / 0.1 / 0.25 |
| `apparelColor` | 3.6% (12/333) | 文本 | (0.2, 0.2, 0.2) / (250,250,250) / (255,255,255) |
| `apparelDisallowTags` | 1.8% (6/333) | 容器 |  |
| `apparelDisallowTags/li` | 1.8% (6/333) | 文本 | Western |
| `apparelIgnorePollution` | 2.4% (8/333) | 布尔 | true |
| `apparelIgnoreSeasons` | 2.7% (9/333) | 布尔 | true |
| `apparelMoney` | 22.8% (76/333) | 数值/文本 | 0~100 / 200~3000 / 400~1000 |
| `apparelRequired` | 10.8% (36/333) | 容器 |  |
| `apparelRequired/li` | 16.5% (55/333) | 文本 | Apparel_CollarShirt / Apparel_Duster / Apparel_FlakVest |
| `apparelTags` | 17.7% (59/333) | 容器 |  |
| `apparelTags/li` | 45.6% (152/333) | 文本 | Horaxian / IndustrialBasic / IndustrialMilitaryBasic |
| `appearsRandomlyInCombatGroups` | 0.3% (1/333) | 布尔 | false |
| `backstoryCryptosleepCommonality` | 7.8% (26/333) | 数值 | 0.08 / 0.1 / 0.25 |
| `backstoryFilters` | 0.6% (2/333) | 容器 |  |
| `backstoryFilters/li` | 0.6% (2/333) | 容器 |  |
| `backstoryFilters/li/categories` | 0.6% (2/333) | 容器 |  |
| `backstoryFilters/li/categories/li` | 1.2% (4/333) | 文本 | Offworld / Pirate / Scientist |
| `backstoryFiltersOverride` | 4.2% (14/333) | 容器 |  |
| `backstoryFiltersOverride/li` | 4.2% (14/333) | 容器 |  |
| `backstoryFiltersOverride/li/categories` | 1.8% (6/333) | 容器 |  |
| `backstoryFiltersOverride/li/categories/li` | 3.3% (11/333) | 文本 | ImperialCommon / Offworld / Outlander |
| `backstoryFiltersOverride/li/categoriesAdulthood` | 2.4% (8/333) | 容器 |  |
| `backstoryFiltersOverride/li/categoriesAdulthood/li` | 2.4% (8/333) | 文本 | Hunter / Miner / TribalHunter |
| `backstoryFiltersOverride/li/categoriesChildhood` | 1.2% (4/333) | 容器 |  |
| `backstoryFiltersOverride/li/categoriesChildhood/li` | 1.2% (4/333) | 文本 | Tribal |
| `biocodeWeaponChance` | 3.9% (13/333) | 数值 | 0.1 / 0.2 / 0.3 |
| `canArriveManhunter` | 1.2% (4/333) | 布尔 | false |
| `canBeSapper` | 3.6% (12/333) | 布尔 | true |
| `canBeScattered` | 0.3% (1/333) | 布尔 | false |
| `canMeleeAttack` | 0.6% (2/333) | 布尔 | false |
| `canOpenAnyDoor` | 0.9% (3/333) | 布尔 | true |
| `canOpenDoors` | 0.9% (3/333) | 布尔 | false / true |
| `canStrip` | 1.5% (5/333) | 布尔 | false |
| `chemicalAddictionChance` | 7.2% (24/333) | 数值 | 0.05 / 0.06 / 0.08 |
| `chronologicalAgeRange` | 0.3% (1/333) | 文本 | 300~2000 |
| `collidesWithPawns` | 0.9% (3/333) | 布尔 | false |
| `combatEnhancingDrugsChance` | 4.8% (16/333) | 数值 | 0.05 / 0.1 / 0.15 |
| `combatEnhancingDrugsCount` | 3.6% (12/333) | 文本 | 0~2 / 1~2 |
| `combatPower` | 65.5% (218/333) | 数值 | 300 / 70 / 80 |
| `controlGroupPortraitZoom` | 2.1% (7/333) | 数值 | 0.8 / 1 / 1.2 |
| `defaultFactionDef` | 19.8% (66/333) | 容器/文本 | Entities / HoraxCult / PlayerColony |
| `defendPointRadius` | 0.3% (1/333) | 数值 | 0 |
| `defName` | 85.6% (285/333) | 文本 | Metalhorror / Nociosphere / Revenant |
| `destroyGearOnDrop` | 0.6% (2/333) | 布尔 | true |
| `disabledWorkTags` | 0.3% (1/333) | 容器 |  |
| `disabledWorkTags/li` | 0.3% (1/333) | 文本 | Violent |
| `disallowedTraits` | 6.9% (23/333) | 容器 |  |
| `disallowedTraits/li` | 7.8% (26/333) | 文本 | BodyPurist / Brawler / Immunity |
| `disallowedTraitsWithDegree` | 0.9% (3/333) | 容器 |  |
| `disallowedTraitsWithDegree/PsychicSensitivity` | 1.2% (4/333) | 数值 | -1 / -2 |
| `ecoSystemWeight` | 27.0% (90/333) | 数值 | 0.20 / 0.22 / 0.5 |
| `factionHostileOnDeath` | 0.3% (1/333) | 布尔 | true |
| `factionLeader` | 1.8% (6/333) | 布尔 | true |
| `favoriteColor` | 0.3% (1/333) | 文本 | Black |
| `fixedRotation` | 0.6% (2/333) | 文本 | South |
| `flyingAnimationDrawSize` | 4.2% (14/333) | 数值 | 1.35 / 1.7 / 2 |
| `flyingAnimationDrawSizeIsMultiplier` | 4.2% (14/333) | 布尔 | false / true |
| `flyingAnimationFrameCount` | 4.2% (14/333) | 数值 | 5 / 8 |
| `flyingAnimationFramePathPrefix` | 4.2% (14/333) | 文本 | Things/Pawn/Animal/Chicken/Chicken_Flying_ / Things/Pawn/Animal/Duck/DuckMale_Flying_ / Things/Pawn/Animal/Goo |
| `flyingAnimationFramePathPrefixFemale` | 0.9% (3/333) | 文本 | Things/Pawn/Animal/Duck/DuckFemale_Flying_ / Things/Pawn/Animal/Peacock/PeacockFemale_Flying_ / Things/Pawn/An |
| `flyingAnimationInheritColors` | 4.2% (14/333) | 布尔 | false / true |
| `flyingAnimationTicksPerFrame` | 4.2% (14/333) | 数值 | 2 |
| `forceDeathOnDowned` | 0.9% (3/333) | 布尔 | true |
| `forcedTraits` | 0.6% (2/333) | 容器 |  |
| `forcedTraits/Recluse` | 0.3% (1/333) | 数值 | 0 |
| `forceNoDeathNotification` | 0.6% (2/333) | 布尔 | true |
| `forceNormalGearQuality` | 1.8% (6/333) | 布尔 | true |
| `forceWeaponQuality` | 0.3% (1/333) | 文本 | Masterwork |
| `gearHealthRange` | 13.5% (45/333) | 文本 | 0.2~0.4 / 0.5~1.8 / 0.7~2.3 |
| `generateInitialNonFamilyRelations` | 0.6% (2/333) | 布尔 | false |
| `hostileToAll` | 0.6% (2/333) | 布尔 | true |
| `humanPregnancyChance` | 1.5% (5/333) | 数值 | 0 / 0.06 |
| `ignoreApparelAllowChance` | 0.3% (1/333) | 布尔 | true |
| `ignoreFactionApparelStuffRequirements` | 0.3% (1/333) | 布尔 | true |
| `ignoreIdeoApparelColors` | 0.3% (1/333) | 布尔 | true |
| `ignoresPainShock` | 0.6% (2/333) | 布尔 | true |
| `immuneToGameConditionEffects` | 2.7% (9/333) | 布尔 | true |
| `immuneToTraps` | 1.2% (4/333) | 布尔 | true |
| `initialResistanceRange` | 30.9% (103/333) | 文本 | 13~21 / 55~65 / 6~10 |
| `initialWillRange` | 20.1% (67/333) | 数值/文本 | 0 / 0~1 / 2~4 |
| `inventoryOptions` | 5.1% (17/333) | 容器 |  |
| `inventoryOptions/skipChance` | 4.8% (16/333) | 数值 | 0.70 / 0.9 / 0.95 |
| `inventoryOptions/subOptionsChooseOne` | 4.8% (16/333) | 容器 |  |
| `inventoryOptions/subOptionsChooseOne/li` | 6.0% (20/333) | 容器 |  |
| `inventoryOptions/subOptionsChooseOne/li/countRange` | 6.0% (20/333) | 数值/文本 | 1 / 10~25 / 3 |
| `inventoryOptions/subOptionsChooseOne/li/thingDef` | 6.0% (20/333) | 文本 | MedicineHerbal / MedicineIndustrial / Silver |
| `inventoryOptions/subOptionsTakeAll` | 0.3% (1/333) | 容器 |  |
| `inventoryOptions/subOptionsTakeAll/li` | 0.3% (1/333) | 容器 |  |
| `inventoryOptions/subOptionsTakeAll/li/countRange` | 0.3% (1/333) | 文本 | 30~100 |
| `inventoryOptions/subOptionsTakeAll/li/thingDef` | 0.3% (1/333) | 文本 | Silver |
| `invFoodDef` | 0.9% (3/333) | 文本 | HemogenPack / Pemmican |
| `invNutrition` | 4.5% (15/333) | 数值 | 0 / 0.5 / 1 |
| `isBoss` | 1.5% (5/333) | 布尔 | true |
| `isFighter` | 6.9% (23/333) | 布尔 | false / true |
| `isGoodBreacher` | 1.5% (5/333) | 布尔 | true |
| `isGoodPsychicRitualInvoker` | 0.9% (3/333) | 布尔 | false / true |
| `itemQuality` | 10.5% (35/333) | 文本 | Awful / Good / Normal |
| `label` | 76.3% (254/333) | 文本 | metalhorror / nociosphere / revenant |
| `labelFemale` | 3.3% (11/333) | 文本 | goat doe / hen / wild woman |
| `labelFemalePlural` | 0.3% (1/333) | 文本 | wild women |
| `labelMale` | 2.4% (8/333) | 文本 | bull / man in black / rooster |
| `labelPlural` | 12.3% (41/333) | 文本 | scorchers / war queens / war urchins |
| `lifeStages` | 46.9% (156/333) | 容器 |  |
| `lifeStages/li` | 117.4% (391/333) | 容器 |  |
| `lifeStages/li/bodyGraphicData` | 117.4% (391/333) | 容器 |  |
| `lifeStages/li/bodyGraphicData/color` | 33.6% (112/333) | 文本 | (112,82,65) / (133,107,96) / (180,180,180) |
| `lifeStages/li/bodyGraphicData/drawOffset` | 0.3% (1/333) | 文本 | (0, 0, 0.1) |
| `lifeStages/li/bodyGraphicData/drawOffsetEast` | 0.9% (3/333) | 文本 | (-0.2, 0.0, 0.0) |
| `lifeStages/li/bodyGraphicData/drawOffsetWest` | 0.9% (3/333) | 文本 | (0.2, 0.0, 0.0) |
| `lifeStages/li/bodyGraphicData/drawSize` | 117.4% (391/333) | 数值 | 1.2 / 1.6 / 1.7 |
| `lifeStages/li/bodyGraphicData/graphicClass` | 18.3% (61/333) | 文本 | Graphic_ActivityStaged / Graphic_Multi / Graphic_Single |
| `lifeStages/li/bodyGraphicData/maskPath` | 13.8% (46/333) | 文本 | Things/Pawn/Mechanoid/AllegianceOverlays/Mech_Constructoid / Things/Pawn/Mechanoid/AllegianceOverlays/Mech_Lif |
| `lifeStages/li/bodyGraphicData/shaderType` | 32.1% (107/333) | 文本 | Cutout / CutoutComplex / CutoutSkin |
| `lifeStages/li/bodyGraphicData/shadowData` | 56.8% (189/333) | 容器 |  |
| `lifeStages/li/bodyGraphicData/shadowData/offset` | 49.2% (164/333) | 文本 | (0,0,-0.1) / (0,0,-0.2) / (0,0,-0.25) |
| `lifeStages/li/bodyGraphicData/shadowData/volume` | 56.8% (189/333) | 文本 | (0.4, 0.3, 0.3) / (0.6, 0.45, 0.45) / (0.6, 0.8, 0.6) |
| `lifeStages/li/bodyGraphicData/texPath` | 117.4% (391/333) | 文本 | Things/Pawn/Metalhorror/Metalhorror_Juvenile / Things/Pawn/Metalhorror/Metalhorror_Larva / Things/Pawn/Metalho |
| `lifeStages/li/butcherBodyPart` | 1.2% (4/333) | 容器 |  |
| `lifeStages/li/butcherBodyPart/bodyPartGroup` | 1.2% (4/333) | 文本 | HornAttackTool / TuskAttackTool |
| `lifeStages/li/butcherBodyPart/thing` | 1.2% (4/333) | 文本 | AlphaThrumboHorn / ElephantTusk / MastodonTusk |
| `lifeStages/li/corpseGraphicData` | 2.7% (9/333) | 容器 |  |
| `lifeStages/li/corpseGraphicData/drawSize` | 2.7% (9/333) | 数值 | 1.0 / 1.5 / 2.0 |
| `lifeStages/li/corpseGraphicData/texPath` | 2.7% (9/333) | 文本 | Things/Pawn/Animal/Boomalope/Corpse_Boomalope / Things/Pawn/Animal/Boomrat/Corpse_Boomrat / Things/Pawn/Animal |
| `lifeStages/li/dessicatedBodyGraphicData` | 99.4% (331/333) | 容器 |  |
| `lifeStages/li/dessicatedBodyGraphicData/attachPoints` | 1.8% (6/333) | 容器 |  |
| `lifeStages/li/dessicatedBodyGraphicData/attachPoints/li` | 7.2% (24/333) | 容器 |  |
| `lifeStages/li/dessicatedBodyGraphicData/attachPoints/li/offset` | 7.2% (24/333) | 文本 | (-.15, 0, -.6) / (-.2, 0, .3) / (.12, 0, -.55) |
| `lifeStages/li/dessicatedBodyGraphicData/attachPoints/li/type` | 7.2% (24/333) | 文本 | PlatformRestraint0 / PlatformRestraint1 / PlatformRestraint2 |
| `lifeStages/li/dessicatedBodyGraphicData/drawOffsetEast` | 0.9% (3/333) | 文本 | (-0.2, 0.0, 0.0) |
| `lifeStages/li/dessicatedBodyGraphicData/drawOffsetWest` | 0.9% (3/333) | 文本 | (0.2, 0.0, 0.0) |
| `lifeStages/li/dessicatedBodyGraphicData/drawSize` | 99.4% (331/333) | 数值 | 1.7 / 2 / 2.7 |
| `lifeStages/li/dessicatedBodyGraphicData/graphicClass` | 1.2% (4/333) | 文本 | Graphic_Multi |
| `lifeStages/li/dessicatedBodyGraphicData/texPath` | 99.4% (331/333) | 文本 | Things/Pawn/Devourer/Dessicated_Devourer / Things/Pawn/Gorehulk/Dessicated_Gorehulk / Things/Pawn/Noctol/Dessi |
| `lifeStages/li/femaleDessicatedBodyGraphicData` | 8.4% (28/333) | 容器 |  |
| `lifeStages/li/femaleDessicatedBodyGraphicData/drawSize` | 8.4% (28/333) | 数值 | 0.73 / 0.85 / 0.89 |
| `lifeStages/li/femaleDessicatedBodyGraphicData/texPath` | 8.4% (28/333) | 文本 | Things/Pawn/Animal/Chicken/Dessicated_Chicken / Things/Pawn/Animal/Goose/Dessicated_Goose / Things/Pawn/Animal |
| `lifeStages/li/femaleGraphicData` | 11.1% (37/333) | 容器 |  |
| `lifeStages/li/femaleGraphicData/color` | 2.4% (8/333) | 文本 | (133,107,96) / (153,129,113) / (200,200,200) |
| `lifeStages/li/femaleGraphicData/drawOffsetEast` | 0.9% (3/333) | 文本 | (-0.2, 0.0, 0.0) |
| `lifeStages/li/femaleGraphicData/drawOffsetWest` | 0.9% (3/333) | 文本 | (0.2, 0.0, 0.0) |
| `lifeStages/li/femaleGraphicData/drawSize` | 11.1% (37/333) | 数值 | 0.73 / 0.85 / 0.89 |
| `lifeStages/li/femaleGraphicData/shaderType` | 1.5% (5/333) | 文本 | CutoutComplex / CutoutSkin |
| `lifeStages/li/femaleGraphicData/shadowData` | 7.2% (24/333) | 容器 |  |
| `lifeStages/li/femaleGraphicData/shadowData/offset` | 7.2% (24/333) | 文本 | (0,0,-0.05) / (0,0,-0.2) / (0,0,-0.25) |
| `lifeStages/li/femaleGraphicData/shadowData/volume` | 7.2% (24/333) | 文本 | (0.4, 0.3, 0.3) / (0.4, 0.4, 0.4) / (0.6, 0.45, 0.45) |
| `lifeStages/li/femaleGraphicData/texPath` | 11.1% (37/333) | 文本 | Things/Pawn/Animal/Chicken/Chicken / Things/Pawn/Animal/Duck/DuckFemale / Things/Pawn/Animal/Ostrich/Ostrich |
| `lifeStages/li/femaleSwimmingGraphicData` | 1.5% (5/333) | 容器 |  |
| `lifeStages/li/femaleSwimmingGraphicData/drawSize` | 1.5% (5/333) | 数值 | 0.73 / 0.85 / 1.5 |
| `lifeStages/li/femaleSwimmingGraphicData/graphicClass` | 1.5% (5/333) | 文本 | Graphic_Multi |
| `lifeStages/li/femaleSwimmingGraphicData/texPath` | 1.5% (5/333) | 文本 | Things/Pawn/Animal/Duck/SwimmingDuckFemale / Things/Pawn/Animal/SeaLion/Swimming_SeaLionFemale |
| `lifeStages/li/label` | 11.4% (38/333) | 文本 | kitten / lynx kitten / toxalope calf |
| `lifeStages/li/labelMale` | 0.3% (1/333) | 文本 | cockerel |
| `lifeStages/li/labelPlural` | 8.7% (29/333) | 文本 | husky puppies / labrador puppies / toxalope calves |
| `lifeStages/li/silhouetteGraphicData` | 1.2% (4/333) | 容器 |  |
| `lifeStages/li/silhouetteGraphicData/drawSize` | 1.2% (4/333) | 数值 | 2 |
| `lifeStages/li/silhouetteGraphicData/graphicClass` | 1.2% (4/333) | 文本 | Graphic_Single |
| `lifeStages/li/silhouetteGraphicData/texPath` | 1.2% (4/333) | 文本 | Things/Pawn/Fleshbeast/Fingerspike/Fingerspike_MenuIcon / Things/Pawn/Fleshbeast/Toughspike/Toughspike_MenuIco |
| `lifeStages/li/stationaryGraphicData` | 0.9% (3/333) | 容器 |  |
| `lifeStages/li/stationaryGraphicData/drawSize` | 0.9% (3/333) | 数值 | 0.4 |
| `lifeStages/li/stationaryGraphicData/texPath` | 0.9% (3/333) | 文本 | Things/Pawn/Animal/HermitCrab/HermitCrabA_Stationary |
| `lifeStages/li/swimmingGraphicData` | 13.8% (46/333) | 容器 |  |
| `lifeStages/li/swimmingGraphicData/color` | 2.7% (9/333) | 文本 | (109,84,49) / (112,82,65) / (180,180,180) |
| `lifeStages/li/swimmingGraphicData/drawSize` | 13.8% (46/333) | 数值 | 1.4 / 2 / 2.7 |
| `lifeStages/li/swimmingGraphicData/graphicClass` | 13.8% (46/333) | 文本 | Graphic_Multi |
| `lifeStages/li/swimmingGraphicData/texPath` | 13.8% (46/333) | 文本 | Things/Pawn/Animal/Bear/SwimmingBear / Things/Pawn/Animal/Duck/SwimmingDuckFemale / Things/Pawn/Animal/Duck/Sw |
| `maxGenerationAge` | 4.8% (16/333) | 数值 | 45 / 55 / 60 |
| `maxPerGroup` | 1.2% (4/333) | 数值 | 3 |
| `meleeAttackInfectionPathways` | 1.5% (5/333) | 容器 |  |
| `meleeAttackInfectionPathways/li` | 1.5% (5/333) | 文本 | EntityAttacked |
| `minGenerationAge` | 2.4% (8/333) | 数值 | 20 / 200 / 30 |
| `minTitleRequired` | 0.9% (3/333) | 文本 | Freeholder |
| `moveSpeedFactorByTerrainTag` | 2.1% (7/333) | 容器 |  |
| `moveSpeedFactorByTerrainTag/li` | 2.1% (7/333) | 容器 |  |
| `moveSpeedFactorByTerrainTag/li/key` | 2.1% (7/333) | 文本 | Insect / Water |
| `moveSpeedFactorByTerrainTag/li/value` | 2.1% (7/333) | 数值 | 1.25 / 2.0 |
| `mutant` | 0.9% (3/333) | 文本 | Ghoul / Shambler |
| `nakedChance` | 0.6% (2/333) | 数值 | 0 / 0.5 |
| `overrideDeathOnDownedChance` | 1.2% (4/333) | 数值 | 0.25 / 0.9 / 1 |
| `overrideDebugActionCategory` | 3.3% (11/333) | 文本 | Entity |
| `pawnGroupDevelopmentStage` | 0.9% (3/333) | 文本 | Child |
| `preventIdeo` | 1.2% (4/333) | 布尔 | true |
| `race` | 55.9% (186/333) | 文本 | Metalhorror / Nociosphere / Revenant |
| `requiredWorkTags` | 4.5% (15/333) | 容器 |  |
| `requiredWorkTags/li` | 6.6% (22/333) | 文本 | Caring / Intellectual / Social |
| `royalTitleChance` | 0.9% (3/333) | 数值 | 0.1 / 1 |
| `skills` | 4.8% (16/333) | 容器 |  |
| `skills/li` | 4.8% (16/333) | 容器 |  |
| `skills/li/range` | 4.8% (16/333) | 文本 | 10~15 / 4~14 / 4~18 |
| `skills/li/skill` | 4.8% (16/333) | 文本 | Melee / Shooting |
| `skipResistant` | 0.3% (1/333) | 布尔 | true |
| `specificApparelRequirements` | 7.5% (25/333) | 容器 |  |
| `specificApparelRequirements/li` | 22.2% (74/333) | 容器 |  |
| `specificApparelRequirements/li/alternateTagChoices` | 5.7% (19/333) | 容器 |  |
| `specificApparelRequirements/li/alternateTagChoices/li` | 6.0% (20/333) | 容器 |  |
| `specificApparelRequirements/li/alternateTagChoices/li/chance` | 6.0% (20/333) | 数值 | 0.1 / 0.2 / 0.25 |
| `specificApparelRequirements/li/alternateTagChoices/li/tag` | 6.0% (20/333) | 文本 | BestowerHood / Cape / Gunlink |
| `specificApparelRequirements/li/apparelLayer` | 8.4% (28/333) | 文本 | Middle / OnSkin / Shell |
| `specificApparelRequirements/li/bodyPartGroup` | 20.4% (68/333) | 文本 | FullHead / Legs / Torso |
| `specificApparelRequirements/li/color` | 6.0% (20/333) | 文本 | (204, 180, 150) / (58, 58, 58) / (68,68,68) |
| `specificApparelRequirements/li/colorGenerator` | 1.2% (4/333) | 容器 |  |
| `specificApparelRequirements/li/colorGenerator/options` | 1.2% (4/333) | 容器 |  |
| `specificApparelRequirements/li/colorGenerator/options/li` | 7.8% (26/333) | 容器 |  |
| `specificApparelRequirements/li/colorGenerator/options/li/only` | 7.8% (26/333) | 文本 | (107, 94, 64) / (58, 58, 58) / (74, 1, 9) |
| `specificApparelRequirements/li/requiredTag` | 10.5% (35/333) | 文本 | Horaxian / HoraxianCeremonial / RoyalTier2 |
| `specificApparelRequirements/li/stuff` | 8.1% (27/333) | 文本 | Cloth / Hyperweave / Steel |
| `specificApparelRequirements/li/useRandomStyleDef` | 0.6% (2/333) | 布尔 | true |
| `startingHediffs` | 2.7% (9/333) | 容器 |  |
| `startingHediffs/li` | 3.9% (13/333) | 容器 |  |
| `startingHediffs/li/chance` | 1.2% (4/333) | 数值 | 0.05 / 0.15 |
| `startingHediffs/li/def` | 3.9% (13/333) | 文本 | HoraxianInvisibility / Inhumanized / LightExposure |
| `startingHediffs/li/durationTicksRange` | 0.3% (1/333) | 文本 | 60000~300000 |
| `startingHediffs/li/severity` | 0.6% (2/333) | 数值 | 0.1 / 1 |
| `studiableAsPrisoner` | 0.6% (2/333) | 布尔 | true |
| `styleItemTags` | 1.2% (4/333) | 容器 |  |
| `styleItemTags/li` | 1.2% (4/333) | 容器 |  |
| `styleItemTags/li/baseWeight` | 1.2% (4/333) | 数值 | 1 / 5 |
| `styleItemTags/li/tag` | 1.2% (4/333) | 文本 | Cultist / Royalty / Soldier |
| `styleItemTags/li/weightFactor` | 1.2% (4/333) | 数值 | 1 |
| `techHediffsChance` | 17.7% (59/333) | 数值 | 0.03 / 0.15 / 0.2 |
| `techHediffsDisallowTags` | 1.5% (5/333) | 容器 |  |
| `techHediffsDisallowTags/li` | 1.5% (5/333) | 文本 | PainCauser |
| `techHediffsMaxAmount` | 2.4% (8/333) | 数值 | 1 / 2 / 3 |
| `techHediffsMoney` | 21.3% (71/333) | 数值/文本 | 0~1800 / 1000~2000 / 50~800 |
| `techHediffsRequired` | 2.4% (8/333) | 容器 |  |
| `techHediffsRequired/li` | 3.0% (10/333) | 文本 | ArmorskinGland / BionicEye / DeathAcidifier |
| `techHediffsTags` | 15.6% (52/333) | 容器 |  |
| `techHediffsTags/li` | 29.1% (97/333) | 文本 | Advanced / AdvancedWeapon / Ghoul |
| `titleRequired` | 2.7% (9/333) | 文本 | Acolyte / Knight / Praetor |
| `titleSelectOne` | 1.2% (4/333) | 容器 |  |
| `titleSelectOne/li` | 2.7% (9/333) | 文本 | Acolyte / Freeholder / Knight |
| `trader` | 0.9% (3/333) | 布尔 | true |
| `useFactionXenotypes` | 5.4% (18/333) | 布尔 | false |
| `useFixedRotation` | 0.6% (2/333) | 布尔 | true |
| `weaponMoney` | 21.3% (71/333) | 数值/文本 | 100~160 / 300~500 / 300~900 |
| `weaponTags` | 28.2% (94/333) | 容器 |  |
| `weaponTags/li` | 36.3% (121/333) | 文本 | MedievalMeleeDecent / NeolithicMeleeBasic / ShortShots |
| `wildGroupSize` | 10.5% (35/333) | 文本 | 3~6 / 3~7 / 3~8 |
| `xenotypeSet` | 9.0% (30/333) | 容器 |  |
| `xenotypeSet/xenotypeChances` | 9.0% (30/333) | 容器 |  |
| `xenotypeSet/xenotypeChances/Baseliner` | 0.3% (1/333) | 数值 | 1 |
| `xenotypeSet/xenotypeChances/Dirtmole` | 0.6% (2/333) | 数值 | 0.05 / 0.1 |
| `xenotypeSet/xenotypeChances/Genie` | 6.0% (20/333) | 数值 | 0.025 / 0.03 / 0.05 |
| `xenotypeSet/xenotypeChances/Highmate` | 1.8% (6/333) | 数值 | 0.025 / 0.03 / 0.04 |
| `xenotypeSet/xenotypeChances/Hussar` | 6.6% (22/333) | 数值 | 0.03 / 0.05 / 0.1 |
| `xenotypeSet/xenotypeChances/Impid` | 0.3% (1/333) | 数值 | 0.025 |
| `xenotypeSet/xenotypeChances/Neanderthal` | 6.0% (20/333) | 数值 | 0.025 / 0.03 / 0.2 |
| `xenotypeSet/xenotypeChances/Pigskin` | 0.3% (1/333) | 数值 | 0.025 |
| `xenotypeSet/xenotypeChances/Sanguophage` | 2.4% (8/333) | 数值 | 0.05 / 0.15 / 0.25 |
| `xenotypeSet/xenotypeChances/Starjack` | 0.3% (1/333) | 数值 | 0.025 |
| `xenotypeSet/xenotypeChances/Waster` | 0.3% (1/333) | 数值 | 0.025 |
| `xenotypeSet/xenotypeChances/Yttakin` | 0.3% (1/333) | 数值 | 0.025 |

## 四、原版 defName 一览（共 333 个，列出前 60）

```text
``                                ``                                ``                                `Tribal_Child_Fire`             
`Villager_Child_Pig`              `Mercenary_Gunner`                `Mercenary_Sniper`                `Mercenary_Slasher`             
`Mercenary_Elite`                 ``                                ``                                ``                              
``                                ``                                ``                                `TradersGuild_Slasher`          
`TradersGuild_Elite`              ``                                ``                                `ShamblerGorehulk`              
`Town_Trader_Pig`                 `Mercenary_Slasher_Yttakin`       `Mercenary_Gunner_Acidifier`      `Mercenary_Sniper_Acidifier`    
`Mercenary_Slasher_Acidifier`     `Mercenary_Elite_Acidifier`       `Salvager_Scrapper`               `Slave_Empire`                  
`Tribal_Archer_Fire`              `Tribal_Hunter_Fire`              `Villager_Pig`                    `Town_Guard_Pig`                
`Town_Councilman_Pig`             `Villager_Child`                  `Drifter_Yttakin`                 `SpaceRefugee`                  
`Mech_CentipedeBlaster`           `Salvager_Elite`                  ``                                `Tribal_Warrior_Fire`           
`Tribal_Penitent_Fire`            `Mercenary_Gunner_Pig`            `Mercenary_Elite_Pig`             `Mechanitor_Basic`              
`Mercenary_SlasherTox`            `Mercenary_Sniper_Yttakin`        ``                                ``                              
`Grenadier_EMP`                   `PirateBoss`                      ``                                `Tribal_ChiefMelee`             
``                                ``                                `TradersGuild_Child`              `Pirate_Yttakin`                
`Scavenger_Yttakin`               `Thrasher_Yttakin`                `Mercenary_Heavy_Yttakin`         `Mercenary_Elite_Yttakin`       
```

_余下 273 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
