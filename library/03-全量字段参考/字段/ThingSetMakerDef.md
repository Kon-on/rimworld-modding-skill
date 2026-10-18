# ThingSetMakerDef

- **所属线**：世界线
- **原版实例数**：52
- **字段路径数**：108
- **资料片**：Anomaly、Core、Ideology、Odyssey、Royalty
- **原版出处**：`Core/Defs/ThingSetMakerDefs/ThingSetMakers_MapGen.xml`、`Odyssey/Defs/ThingSetMakerDefs/ThingSetMakers_Fishing.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<ThingSetMakerDef>
    <defName>MapGen_AncientPodContents</defName>
    <root Class="ThingSetMaker_MapGen_AncientPodContents"/>
  </ThingSetMakerDef>

  
```

> 来自 `Core/Defs/ThingSetMakerDefs/ThingSetMakers_MapGen.xml`，defName = `MapGen_AncientPodContents`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：MapGen_FleshSackLoot / MechanoidRaidLootMaker / Reward_GrayBox
root                                           [容器]
root/options/li                                [容器]
root/options/li/thingSetMaker                  [容器]
root/options/li/thingSetMaker/fixedParams      [容器]
root/options/li/thingSetMaker/fixedParams/countRange [数值/文本]  例：1 / 15~30 / 1~2
root/options/li/thingSetMaker/fixedParams/filter [容器]
root/options/li/thingSetMaker/fixedParams/filter/thingDefs [容器]
root/options/li/thingSetMaker/fixedParams/filter/thingDefs/li [文本]  例：Apparel_BiomutationLance / Apparel_DisruptorFlarePack / PsychicEmanator
root/options/li/weight                         [数值]  例：0.15 / 0.25 / 0.5
```

## 三、全量字段表（108 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `debugParams` | 9.6% (5/52) | 容器 |  |
| `debugParams/countRange` | 5.8% (3/52) | 文本 | 6~6 / 8~8 |
| `debugParams/totalMarketValueRange` | 7.7% (4/52) | 文本 | 1000~1000 / 100~500 / 500~500 |
| `defName` | 98.1% (51/52) | 文本 | MapGen_FleshSackLoot / MechanoidRaidLootMaker / Reward_GrayBox |
| `root` | 100.0% (52/52) | 容器 |  |
| `root/fixedParams` | 17.3% (9/52) | 容器 |  |
| `root/fixedParams/filter` | 13.5% (7/52) | 容器 |  |
| `root/fixedParams/filter/thingDefs` | 11.5% (6/52) | 容器 |  |
| `root/fixedParams/filter/thingDefs/li` | 55.8% (29/52) | 文本 | ComponentIndustrial / MedicineIndustrial / Plasteel |
| `root/fixedParams/filter/thingSetMakerTagsToAllow` | 1.9% (1/52) | 容器 |  |
| `root/fixedParams/filter/thingSetMakerTagsToAllow/li` | 3.9% (2/52) | 文本 | RewardStandardLowFreq / RewardStandardQualitySuper |
| `root/fixedParams/qualityGenerator` | 3.9% (2/52) | 文本 | Gift / Trader |
| `root/options` | 75.0% (39/52) | 容器 |  |
| `root/options/li` | 450.0% (234/52) | 容器 |  |
| `root/options/li/chance` | 28.8% (15/52) | 数值 | 0.35 / 0.5 / 0.6 |
| `root/options/li/maxMarketValue` | 1.9% (1/52) | 数值 | 5500 |
| `root/options/li/minMarketValue` | 1.9% (1/52) | 数值 | 150 |
| `root/options/li/minTotalMarketValue` | 1.9% (1/52) | 数值 | 5500 |
| `root/options/li/thingSetMaker` | 450.0% (234/52) | 容器 |  |
| `root/options/li/thingSetMaker/alive` | 46.2% (24/52) | 布尔 | false |
| `root/options/li/thingSetMaker/corpseAgeRangeDays` | 46.2% (24/52) | 文本 | 10~300 / 5~10 |
| `root/options/li/thingSetMaker/def` | 1.9% (1/52) | 文本 | MapGen_DefaultStockpile |
| `root/options/li/thingSetMaker/fixedParams` | 382.7% (199/52) | 容器 |  |
| `root/options/li/thingSetMaker/fixedParams/countRange` | 309.6% (161/52) | 数值/文本 | 1 / 15~30 / 1~2 |
| `root/options/li/thingSetMaker/fixedParams/filter` | 376.9% (196/52) | 容器 |  |
| `root/options/li/thingSetMaker/fixedParams/filter/categories` | 21.1% (11/52) | 容器 |  |
| `root/options/li/thingSetMaker/fixedParams/filter/categories/li` | 26.9% (14/52) | 文本 | Artifacts / Foods / ResourcesRaw |
| `root/options/li/thingSetMaker/fixedParams/filter/disallowCheaperThan` | 1.9% (1/52) | 数值 | 6 |
| `root/options/li/thingSetMaker/fixedParams/filter/disallowedThingDefs` | 7.7% (4/52) | 容器 |  |
| `root/options/li/thingSetMaker/fixedParams/filter/disallowedThingDefs/li` | 7.7% (4/52) | 文本 | Apparel_SmokepopBelt / InsectJelly / WoodLog |
| `root/options/li/thingSetMaker/fixedParams/filter/disallowInedibleByHuman` | 3.9% (2/52) | 布尔 | true |
| `root/options/li/thingSetMaker/fixedParams/filter/disallowWithComp` | 3.9% (2/52) | 文本 | CompHatcher |
| `root/options/li/thingSetMaker/fixedParams/filter/disallowWorsePreferability` | 3.9% (2/52) | 文本 | RawBad |
| `root/options/li/thingSetMaker/fixedParams/filter/thingDefs` | 336.5% (175/52) | 容器 |  |
| `root/options/li/thingSetMaker/fixedParams/filter/thingDefs/li` | 792.3% (412/52) | 文本 | Apparel_BiomutationLance / Apparel_DisruptorFlarePack / PsychicEmanator |
| `root/options/li/thingSetMaker/fixedParams/filter/thingSetMakerTagsToAllow` | 23.1% (12/52) | 容器 |  |
| `root/options/li/thingSetMaker/fixedParams/filter/thingSetMakerTagsToAllow/li` | 26.9% (14/52) | 文本 | SingleUseWeapon / SkillNeurotrainer / Techprint |
| `root/options/li/thingSetMaker/fixedParams/filter/thingSetMakerTagsToDisallow` | 13.5% (7/52) | 容器 |  |
| `root/options/li/thingSetMaker/fixedParams/filter/thingSetMakerTagsToDisallow/li` | 26.9% (14/52) | 文本 | RewardStandardCore / RewardStandardHighFreq |
| `root/options/li/thingSetMaker/fixedParams/minSingleItemMarketValuePct` | 1.9% (1/52) | 数值 | 0.15 |
| `root/options/li/thingSetMaker/fixedParams/qualityGenerator` | 38.5% (20/52) | 文本 | Reward / Super |
| `root/options/li/thingSetMaker/fixedParams/totalMarketValueRange` | 1.9% (1/52) | 文本 | 1000~2000 |
| `root/options/li/thingSetMaker/fixedParams/totalNutritionRange` | 3.9% (2/52) | 文本 | 4~8 |
| `root/options/li/thingSetMaker/makingFaction` | 1.9% (1/52) | 文本 | Empire |
| `root/options/li/thingSetMaker/options` | 7.7% (4/52) | 容器 |  |
| `root/options/li/thingSetMaker/options/li` | 42.3% (22/52) | 容器 |  |
| `root/options/li/thingSetMaker/options/li/thingSetMaker` | 42.3% (22/52) | 容器 |  |
| `root/options/li/thingSetMaker/options/li/thingSetMaker/fixedParams` | 30.8% (16/52) | 容器 |  |
| `root/options/li/thingSetMaker/options/li/thingSetMaker/fixedParams/allowNonStackableDuplicates` | 11.5% (6/52) | 布尔 | False |
| `root/options/li/thingSetMaker/options/li/thingSetMaker/fixedParams/filter` | 30.8% (16/52) | 容器 |  |
| `root/options/li/thingSetMaker/options/li/thingSetMaker/fixedParams/filter/categories` | 13.5% (7/52) | 容器 |  |
| `root/options/li/thingSetMaker/options/li/thingSetMaker/fixedParams/filter/categories/li` | 13.5% (7/52) | 文本 | Apparel / ResourcesRaw / Weapons |
| `root/options/li/thingSetMaker/options/li/thingSetMaker/fixedParams/filter/disallowCheaperThan` | 1.9% (1/52) | 数值 | 7 |
| `root/options/li/thingSetMaker/options/li/thingSetMaker/fixedParams/filter/disallowedThingDefs` | 7.7% (4/52) | 容器 |  |
| `root/options/li/thingSetMaker/options/li/thingSetMaker/fixedParams/filter/disallowedThingDefs/li` | 13.5% (7/52) | 文本 | BlocksVacstone / ElephantTusk / GravlitePanel |
| `root/options/li/thingSetMaker/options/li/thingSetMaker/fixedParams/filter/thingDefs` | 5.8% (3/52) | 容器 |  |
| `root/options/li/thingSetMaker/options/li/thingSetMaker/fixedParams/filter/thingDefs/li` | 5.8% (3/52) | 文本 | Gold / Plasteel / Uranium |
| `root/options/li/thingSetMaker/options/li/thingSetMaker/fixedParams/filter/thingSetMakerTagsToAllow` | 11.5% (6/52) | 容器 |  |
| `root/options/li/thingSetMaker/options/li/thingSetMaker/fixedParams/filter/thingSetMakerTagsToAllow/li` | 11.5% (6/52) | 文本 | RewardStandardHighFreq / RewardStandardLowFreq / RewardStandardMidFreq |
| `root/options/li/thingSetMaker/options/li/thingSetMaker/fixedParams/filter/thingSetMakerTagsToDisallow` | 13.5% (7/52) | 容器 |  |
| `root/options/li/thingSetMaker/options/li/thingSetMaker/fixedParams/filter/thingSetMakerTagsToDisallow/li` | 30.8% (16/52) | 文本 | NonStandardReward / RewardStandardCore / RewardStandardHighFreq |
| `root/options/li/thingSetMaker/options/li/thingSetMaker/fixedParams/maxThingMarketValue` | 11.5% (6/52) | 数值 | 300 |
| `root/options/li/thingSetMaker/options/li/thingSetMaker/fixedParams/qualityGenerator` | 11.5% (6/52) | 文本 | Reward / Super |
| `root/options/li/thingSetMaker/options/li/thingSetMaker/makingFaction` | 3.9% (2/52) | 文本 | Empire / Sanguophages |
| `root/options/li/thingSetMaker/options/li/thingSetMaker/makingFactionCategories` | 1.9% (1/52) | 容器 |  |
| `root/options/li/thingSetMaker/options/li/thingSetMaker/makingFactionCategories/li` | 1.9% (1/52) | 文本 | Tribal |
| `root/options/li/thingSetMaker/options/li/thingSetMaker/marketValueFactor` | 3.9% (2/52) | 数值 | 1.4 |
| `root/options/li/thingSetMaker/options/li/thingSetMaker/minMaxTotalMarketValue` | 1.9% (1/52) | 数值 | 2500 |
| `root/options/li/thingSetMaker/options/li/thingSetMaker/requireNonNull` | 5.8% (3/52) | 布尔 | true |
| `root/options/li/thingSetMaker/options/li/thingSetMaker/thingSetMaker` | 7.7% (4/52) | 容器 |  |
| `root/options/li/thingSetMaker/options/li/thingSetMaker/thingSetMaker/fixedParams` | 5.8% (3/52) | 容器 |  |
| `root/options/li/thingSetMaker/options/li/thingSetMaker/thingSetMaker/fixedParams/allowNonStackableDuplicates` | 1.9% (1/52) | 布尔 | False |
| `root/options/li/thingSetMaker/options/li/thingSetMaker/thingSetMaker/fixedParams/filter` | 5.8% (3/52) | 容器 |  |
| `root/options/li/thingSetMaker/options/li/thingSetMaker/thingSetMaker/fixedParams/filter/thingDefs` | 3.9% (2/52) | 容器 |  |
| `root/options/li/thingSetMaker/options/li/thingSetMaker/thingSetMaker/fixedParams/filter/thingDefs/li` | 3.9% (2/52) | 文本 | AnimusStone / DeathrestCapacitySerum |
| `root/options/li/thingSetMaker/options/li/thingSetMaker/thingSetMaker/fixedParams/filter/thingSetMakerTagsToAllow` | 1.9% (1/52) | 容器 |  |
| `root/options/li/thingSetMaker/options/li/thingSetMaker/thingSetMaker/fixedParams/filter/thingSetMakerTagsToAllow/li` | 3.9% (2/52) | 文本 | ImplantEmpireRoyal / WeaponBladelink |
| `root/options/li/thingSetMaker/options/li/thingSetMaker/thingSetMaker/fixedParams/filter/thingSetMakerTagsToDisallow` | 1.9% (1/52) | 容器 |  |
| `root/options/li/thingSetMaker/options/li/thingSetMaker/thingSetMaker/fixedParams/filter/thingSetMakerTagsToDisallow/li` | 1.9% (1/52) | 文本 | RewardNonEmpireFactionsOnly |
| `root/options/li/thingSetMaker/options/li/thingSetMaker/thingSetMaker/fixedParams/filter/tradeTagsToAllow` | 1.9% (1/52) | 容器 |  |
| `root/options/li/thingSetMaker/options/li/thingSetMaker/thingSetMaker/fixedParams/filter/tradeTagsToAllow/li` | 3.9% (2/52) | 文本 | PsychicApparel / PsychicWeapon |
| `root/options/li/thingSetMaker/options/li/thingSetMaker/thingSetMaker/fixedParams/qualityGenerator` | 1.9% (1/52) | 文本 | Reward |
| `root/options/li/thingSetMaker/options/li/thingSetMaker/thingSetMaker/researchProject` | 1.9% (1/52) | 文本 | MultiAnalyzer |
| `root/options/li/thingSetMaker/options/li/thingSetMaker/thingSetMaker/thingSetMaker` | 1.9% (1/52) | 容器 |  |
| `root/options/li/thingSetMaker/options/li/thingSetMaker/thingSetMaker/thingSetMaker/fixedParams` | 1.9% (1/52) | 容器 |  |
| `root/options/li/thingSetMaker/options/li/thingSetMaker/thingSetMaker/thingSetMaker/fixedParams/filter` | 1.9% (1/52) | 容器 |  |
| `root/options/li/thingSetMaker/options/li/thingSetMaker/thingSetMaker/thingSetMaker/fixedParams/filter/thingDefs` | 1.9% (1/52) | 容器 |  |
| `root/options/li/thingSetMaker/options/li/thingSetMaker/thingSetMaker/thingSetMaker/fixedParams/filter/thingDefs/li` | 1.9% (1/52) | 文本 | AIPersonaCore |
| `root/options/li/thingSetMaker/options/li/weight` | 42.3% (22/52) | 数值 | 0 / 1 / 10 |
| `root/options/li/thingSetMaker/options/li/weightIfPlayerHasNoItem` | 1.9% (1/52) | 数值 | 1 |
| `root/options/li/thingSetMaker/options/li/weightIfPlayerHasNoItemItem` | 1.9% (1/52) | 文本 | AIPersonaCore |
| `root/options/li/thingSetMaker/options/li/weightIfPlayerHasXenotype` | 1.9% (1/52) | 数值 | 20 |
| `root/options/li/thingSetMaker/options/li/weightIfPlayerHasXenotypeXenotype` | 1.9% (1/52) | 文本 | Sanguophage |
| `root/options/li/thingSetMaker/pawnKind` | 48.1% (25/52) | 文本 | Pirate / PirateBoss / Salvager_Pirate |
| `root/options/li/thingSetMaker/requireNonNull` | 1.9% (1/52) | 布尔 | true |
| `root/options/li/thingSetMaker/thingSetMaker` | 1.9% (1/52) | 容器 |  |
| `root/options/li/thingSetMaker/thingSetMaker/fixedParams` | 1.9% (1/52) | 容器 |  |
| `root/options/li/thingSetMaker/thingSetMaker/fixedParams/countRange` | 1.9% (1/52) | 文本 | 2~3 |
| `root/options/li/thingSetMaker/thingSetMaker/fixedParams/filter` | 1.9% (1/52) | 容器 |  |
| `root/options/li/thingSetMaker/thingSetMaker/fixedParams/filter/thingSetMakerTagsToAllow` | 1.9% (1/52) | 容器 |  |
| `root/options/li/thingSetMaker/thingSetMaker/fixedParams/filter/thingSetMakerTagsToAllow/li` | 3.9% (2/52) | 文本 | ImplantEmpireRoyal / WeaponBladelink |
| `root/options/li/thingSetMaker/thingSetMaker/fixedParams/filter/thingSetMakerTagsToDisallow` | 1.9% (1/52) | 容器 |  |
| `root/options/li/thingSetMaker/thingSetMaker/fixedParams/filter/thingSetMakerTagsToDisallow/li` | 1.9% (1/52) | 文本 | RewardNonEmpireFactionsOnly |
| `root/options/li/thingSetMaker/thingSetMaker/fixedParams/filter/tradeTagsToAllow` | 1.9% (1/52) | 容器 |  |
| `root/options/li/thingSetMaker/thingSetMaker/fixedParams/filter/tradeTagsToAllow/li` | 3.9% (2/52) | 文本 | PsychicApparel / PsychicWeapon |
| `root/options/li/thingSetMaker/weightAccordingToPlayerNeeds` | 3.9% (2/52) | 布尔 | false |
| `root/options/li/weight` | 403.9% (210/52) | 数值 | 0.15 / 0.25 / 0.5 |
| `root/resolveInOrder` | 5.8% (3/52) | 布尔 | true |

## 四、原版 defName 一览（共 52 个，列出前 60）

```text
`MapGen_AncientPodContents`       `ResourcePod`                     `RefugeePod`                      `Meteorite`                     
`MapGen_ScarlandsAncientPodContents`  `TraderStock`                     `Reward_UniqueWeapon`             `MechanoidRaidLootMaker`        
`Reward_ReliquaryPilgrims`        `TribeRaidLootMaker`              `MapGen_OrbitalItemStash`         `EmpireRaidLootMaker`           
`OutlanderRaidLootMaker`          `TradersGuildRaidLootMaker`       `Reward_Pallet_Medicine`          `Reward_Pallet_SurvivalMeals`   
`Reward_AncientBox_ComponentIndustrial`  `Reward_AncientBox_ComponentSpacer`  `Reward_AncientBox_SteelSlag`     `Reward_AncientPallet_SteelSlag`
`Reward_AncientChemfuelCanister`  `Reward_AncientSealedCrateBase_Gravlite`  `Reward_ArcheanSeed`              `PirateRaidLootMaker`           
`Reward_AncientSealedCrate_Shells`  `MapGen_PrisonCellStockpile`      `RareFishingCatches_Glowforest`   `DebugQuestDropPodsContents`    
`Reward_AncientSealedContainer`   `Reward_GravshipUpgrade`          `RareFishingCatches_Hot`          `Reward_GrayBoxLowReward`       
`RareFishingCatches_Cold`         `DebugCaravanInventory`           `RareFishingCatches_Temperate`    `RareFishingCatches_Tropical`   
`MapGen_AbandonedColonyStockpile`  `VisitorGift`                     `MapGen_DefaultStockpile`         `Reward_AncientSafe`            
`Reward_MalfunctioningTransportPod`  `MapGen_AncientTempleContents`    `MapGen_AncientComplexRoomLoot_Default`  `MapGen_AncientComplexRoomLoot_Default`
`MapGen_HighValueCrate`           `Reward_GrayBox`                  `MapGen_ScarlandsHermeticCrate`   `MapGen_AncientComplex_SecurityCrate`
`MapGen_AncientComplexRoomLoot_Better`  `Reward_ItemsStandard`            ``                                `MapGen_FleshSackLoot`          
```
