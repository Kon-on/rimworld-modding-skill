# RecipeDef

- **所属线**：物品线
- **原版实例数**：212
- **字段路径数**：163
- **资料片**：Anomaly、Biotech、Core、Odyssey、Royalty
- **原版出处**：`Core/Defs/HediffDefs/BodyParts/Hediffs_BodyParts_Base.xml`、`Core/Defs/HediffDefs/BodyParts/Hediffs_BodyParts_Prosthetic.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<RecipeDef Name="SurgeryInstallBodyPartArtificialBase" ParentName="SurgeryInstallImplantBase" Abstract="True">
    <workerClass>Recipe_InstallArtificialBodyPart</workerClass>
  </RecipeDef>

  
```

> 来自 `Core/Defs/HediffDefs/BodyParts/Hediffs_BodyParts_Base.xml`，defName = ``，XML 节点数 2（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
ingredients/li                                 [容器]
ingredients/li/count                           [数值]  例：0.25 / 1 / 2
ingredients/li/filter                          [容器]
```

## 三、全量字段表（163 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `addsHediff` | 32.6% (69/212) | 文本 | AdrenalHeart / CorrosiveHeart / GhoulBarbs |
| `addsHediffOnFailure` | 1.9% (4/212) | 文本 | Sterilized |
| `allowedForQuestLodgers` | 0.5% (1/212) | 布尔 | false |
| `allowMixingIngredients` | 7.5% (16/212) | 布尔 | true |
| `anesthetize` | 5.2% (11/212) | 布尔 | false |
| `appliedOnFixedBodyPartGroups` | 0.9% (2/212) | 容器 |  |
| `appliedOnFixedBodyPartGroups/li` | 0.9% (2/212) | 文本 | MiddleFingers / Teeth |
| `appliedOnFixedBodyParts` | 30.2% (64/212) | 容器 |  |
| `appliedOnFixedBodyParts/li` | 30.2% (64/212) | 文本 | Heart / Lung / Spine |
| `autoStripCorpses` | 0.5% (1/212) | 布尔 | false |
| `conceptLearned` | 0.5% (1/212) | 文本 | DrugBurning |
| `deathOnFailedSurgeryChance` | 4.7% (10/212) | 数值 | 0 / 0.02 / 0.1 |
| `defaultIngredientFilter` | 7.1% (15/212) | 容器 |  |
| `defaultIngredientFilter/categories` | 6.1% (13/212) | 容器 |  |
| `defaultIngredientFilter/categories/li` | 7.1% (15/212) | 文本 | Apparel / CorpsesAnimal / CorpsesDrone |
| `defaultIngredientFilter/disallowedCategories` | 1.4% (3/212) | 容器 |  |
| `defaultIngredientFilter/disallowedCategories/li` | 1.9% (4/212) | 文本 | AnimalProductRaw / EggsFertilized / MeatRaw |
| `defaultIngredientFilter/disallowedThingDefs` | 3.8% (8/212) | 容器 |  |
| `defaultIngredientFilter/disallowedThingDefs/li` | 10.8% (23/212) | 文本 | Apparel_ShieldBelt / Apparel_SmokepopBelt / InsectJelly |
| `defaultIngredientFilter/disallowMedicalDrugs` | 0.5% (1/212) | 布尔 | true |
| `defaultIngredientFilter/specialFiltersToAllow` | 1.4% (3/212) | 容器 |  |
| `defaultIngredientFilter/specialFiltersToAllow/li` | 3.3% (7/212) | 文本 | AllowCorpsesColonist / AllowCorpsesMechEnemy / AllowCorpsesSlave |
| `defaultIngredientFilter/specialFiltersToDisallow` | 0.5% (1/212) | 容器 |  |
| `defaultIngredientFilter/specialFiltersToDisallow/li` | 0.5% (1/212) | 文本 | AllowCorpsesMechFriendly |
| `defaultIngredientFilter/thingDefs` | 0.9% (2/212) | 容器 |  |
| `defaultIngredientFilter/thingDefs/li` | 0.9% (2/212) | 文本 | Corpse_Human |
| `defName` | 88.7% (188/212) | 文本 | InstallAdrenalHeart / InstallCorrosiveHeart / InstallGhoulBarbs |
| `description` | 88.7% (188/212) | 文本 | Install adrenal heart. / Install corrosive heart. / Install ghoul barbs. |
| `descriptionHyperlinks` | 51.9% (110/212) | 容器 |  |
| `descriptionHyperlinks/HediffDef` | 37.3% (79/212) | 文本 | AdrenalHeart / CorrosiveHeart / GhoulBarbs |
| `descriptionHyperlinks/ThingDef` | 51.9% (110/212) | 文本 | AdrenalHeart / CorrosiveHeart / GhoulBarbs |
| `developmentalStageFilter` | 1.4% (3/212) | 文本 | Child, Adult |
| `displayPriority` | 14.6% (31/212) | 数值 | 100 / 1430 / 1431 |
| `dontShowIfAnyIngredientMissing` | 0.5% (1/212) | 布尔 | true |
| `effectWorking` | 16.0% (34/212) | 文本 | ButcherFlesh / ButcherMechanoid / Cook |
| `efficiencyStat` | 0.9% (2/212) | 文本 | ButcheryFleshEfficiency / ButcheryMechanoidEfficiency |
| `fixedIngredientFilter` | 59.9% (127/212) | 容器 |  |
| `fixedIngredientFilter/categories` | 17.0% (36/212) | 容器 |  |
| `fixedIngredientFilter/categories/li` | 18.4% (39/212) | 文本 | Corpses / CorpsesHumanlike / FoodRaw |
| `fixedIngredientFilter/disallowDoesntProduceMeat` | 0.5% (1/212) | 布尔 | true |
| `fixedIngredientFilter/disallowedCategories` | 7.1% (15/212) | 容器 |  |
| `fixedIngredientFilter/disallowedCategories/li` | 10.4% (22/212) | 文本 | CorpsesDrone / CorpsesMechanoid / EggsFertilized |
| `fixedIngredientFilter/disallowedThingDefs` | 1.9% (4/212) | 容器 |  |
| `fixedIngredientFilter/disallowedThingDefs/li` | 3.8% (8/212) | 文本 | Dye / Hay / HemogenPack |
| `fixedIngredientFilter/specialFiltersToAllow` | 0.5% (1/212) | 容器 |  |
| `fixedIngredientFilter/specialFiltersToAllow/li` | 0.5% (1/212) | 文本 | AllowCorpsesMechFriendly |
| `fixedIngredientFilter/specialFiltersToDisallow` | 3.8% (8/212) | 容器 |  |
| `fixedIngredientFilter/specialFiltersToDisallow/li` | 3.8% (8/212) | 文本 | AllowNonBurnableApparel / AllowNonBurnableWeapons / AllowPlantFood |
| `fixedIngredientFilter/thingDefs` | 39.6% (84/212) | 容器 |  |
| `fixedIngredientFilter/thingDefs/li` | 50.9% (108/212) | 文本 | AdrenalHeart / CorrosiveHeart / GhoulBarbs |
| `forceHiddenSpecialFilters` | 2.8% (6/212) | 容器 |  |
| `forceHiddenSpecialFilters/li` | 6.6% (14/212) | 文本 | AllowBurnableApparel / AllowCorpsesMechFriendly / AllowFresh |
| `formingTicks` | 0.9% (2/212) | 数值 | 120000 / 30000 |
| `genderPrerequisite` | 2.4% (5/212) | 文本 | Female / Male |
| `gestationCycles` | 3.3% (7/212) | 数值 | 1 / 12 / 4 |
| `hideBodyPartNames` | 7.1% (15/212) | 布尔 | false / true |
| `ignoreIngredientCountTakeEntireStacks` | 0.5% (1/212) | 布尔 | true |
| `incompatibleWithHediffTags` | 3.3% (7/212) | 容器 |  |
| `incompatibleWithHediffTags/li` | 3.3% (7/212) | 文本 | ArmorGland / OvumExtracted / Sterilized |
| `ingredients` | 71.2% (151/212) | 容器 |  |
| `ingredients/li` | 100.0% (212/212) | 容器 |  |
| `ingredients/li/count` | 99.5% (211/212) | 数值 | 0.25 / 1 / 2 |
| `ingredients/li/filter` | 100.0% (212/212) | 容器 |  |
| `ingredients/li/filter/categories` | 28.8% (61/212) | 容器 |  |
| `ingredients/li/filter/categories/li` | 35.9% (76/212) | 文本 | AnimalProductRaw / Corpses / Medicine |
| `ingredients/li/filter/customSummary` | 7.1% (15/212) | 文本 | feedstock / greens / protein |
| `ingredients/li/filter/disallowedCategories` | 0.5% (1/212) | 容器 |  |
| `ingredients/li/filter/disallowedCategories/li` | 0.5% (1/212) | 文本 | FoodMeals |
| `ingredients/li/filter/disallowedThingDefs` | 0.9% (2/212) | 容器 |  |
| `ingredients/li/filter/disallowedThingDefs/li` | 1.9% (4/212) | 文本 | Dye / Hay / Leather_AlphaThrumbo |
| `ingredients/li/filter/thingDefs` | 71.7% (152/212) | 容器 |  |
| `ingredients/li/filter/thingDefs/li` | 72.2% (153/212) | 文本 | AdrenalHeart / CorrosiveHeart / GhoulBarbs |
| `ingredientValueGetterClass` | 6.6% (14/212) | 文本 | IngredientValueGetter_Nutrition |
| `interruptIfIngredientIsRotting` | 0.5% (1/212) | 布尔 | true |
| `isViolation` | 6.6% (14/212) | 布尔 | false / true |
| `jobString` | 75.0% (159/212) | 文本 | Installing adrenal heart. / Installing corrosive heart. / Installing ghoul barbs. |
| `label` | 88.7% (188/212) | 文本 | install adrenal heart / install corrosive heart / install ghoul barbs |
| `mechanitorOnlyRecipe` | 0.5% (1/212) | 布尔 | true |
| `mechResurrection` | 0.5% (1/212) | 布尔 | true |
| `minAllowedAge` | 1.4% (3/212) | 数值 | 13 / 16 |
| `mustBeFertile` | 0.5% (1/212) | 布尔 | true |
| `mutantBlacklist` | 0.5% (1/212) | 容器 |  |
| `mutantBlacklist/li` | 0.5% (1/212) | 文本 | Ghoul |
| `mutantPrerequisite` | 2.8% (6/212) | 容器 |  |
| `mutantPrerequisite/li` | 2.8% (6/212) | 文本 | Ghoul |
| `products` | 26.9% (57/212) | 容器 |  |
| `products/BabyFood` | 0.9% (2/212) | 数值 | 10 / 40 |
| `products/Bioferrite` | 0.5% (1/212) | 数值 | 15 |
| `products/BlocksGranite` | 0.5% (1/212) | 数值 | 20 |
| `products/BlocksLimestone` | 0.5% (1/212) | 数值 | 20 |
| `products/BlocksMarble` | 0.5% (1/212) | 数值 | 20 |
| `products/BlocksSandstone` | 0.5% (1/212) | 数值 | 20 |
| `products/BlocksSlate` | 0.5% (1/212) | 数值 | 20 |
| `products/BlocksVacstone` | 0.5% (1/212) | 数值 | 20 |
| `products/Chemfuel` | 0.9% (2/212) | 数值 | 35 |
| `products/ComponentIndustrial` | 0.5% (1/212) | 数值 | 1 |
| `products/ComponentSpacer` | 0.5% (1/212) | 数值 | 1 |
| `products/Gun_BeamGraser` | 0.5% (1/212) | 数值 | 1 |
| `products/Kibble` | 0.5% (1/212) | 数值 | 50 |
| `products/Leather_Patch` | 0.5% (1/212) | 数值 | 50 |
| `products/MealFine` | 0.9% (2/212) | 数值 | 1 / 4 |
| `products/MealFine_Meat` | 0.9% (2/212) | 数值 | 1 / 4 |
| `products/MealFine_Veg` | 0.9% (2/212) | 数值 | 1 / 4 |
| `products/MealLavish` | 0.9% (2/212) | 数值 | 1 / 4 |
| `products/MealLavish_Meat` | 0.9% (2/212) | 数值 | 1 / 4 |
| `products/MealLavish_Veg` | 0.9% (2/212) | 数值 | 1 / 4 |
| `products/MealSimple` | 0.9% (2/212) | 数值 | 1 / 4 |
| `products/MealSurvivalPack` | 0.9% (2/212) | 数值 | 1 / 4 |
| `products/Mech_Agrihand` | 0.5% (1/212) | 数值 | 1 |
| `products/Mech_CentipedeBlaster` | 0.5% (1/212) | 数值 | 1 |
| `products/Mech_CentipedeBurner` | 0.5% (1/212) | 数值 | 1 |
| `products/Mech_CentipedeGunner` | 0.5% (1/212) | 数值 | 1 |
| `products/Mech_Centurion` | 0.5% (1/212) | 数值 | 1 |
| `products/Mech_Cleansweeper` | 0.5% (1/212) | 数值 | 1 |
| `products/Mech_Constructoid` | 0.5% (1/212) | 数值 | 1 |
| `products/Mech_Cyclops` | 0.5% (1/212) | 数值 | 1 |
| `products/Mech_Diabolus` | 0.5% (1/212) | 数值 | 1 |
| `products/Mech_Fabricor` | 0.5% (1/212) | 数值 | 1 |
| `products/Mech_Lancer` | 0.5% (1/212) | 数值 | 1 |
| `products/Mech_Legionary` | 0.5% (1/212) | 数值 | 1 |
| `products/Mech_Lifter` | 0.5% (1/212) | 数值 | 1 |
| `products/Mech_Militor` | 0.5% (1/212) | 数值 | 1 |
| `products/Mech_Paramedic` | 0.5% (1/212) | 数值 | 1 |
| `products/Mech_Pikeman` | 0.5% (1/212) | 数值 | 1 |
| `products/Mech_Scorcher` | 0.5% (1/212) | 数值 | 1 |
| `products/Mech_Scyther` | 0.5% (1/212) | 数值 | 1 |
| `products/Mech_Tesseron` | 0.5% (1/212) | 数值 | 1 |
| `products/Mech_Tunneler` | 0.5% (1/212) | 数值 | 1 |
| `products/Mech_Warqueen` | 0.5% (1/212) | 数值 | 1 |
| `products/Pemmican` | 0.9% (2/212) | 数值 | 16 / 64 |
| `products/Steel` | 0.5% (1/212) | 数值 | 15 |
| `products/Wort` | 0.5% (1/212) | 数值 | 5 |
| `recipeUsers` | 2.8% (6/212) | 容器 |  |
| `recipeUsers/li` | 4.2% (9/212) | 文本 | CreepJoiner / ElectricTailoringBench / Human |
| `removesHediff` | 14.6% (31/212) | 文本 | Carcinoma / ImplantedIUD / Painstopper |
| `requiredGiverWorkType` | 4.2% (9/212) | 文本 | Cooking / Hauling |
| `researchPrerequisite` | 9.9% (21/212) | 文本 | BasicMechtech / HighMechtech / StandardMechtech |
| `researchPrerequisite/li` | 0.9% (2/212) | 文本 | BlissLobotomy / GhoulInfusion |
| `researchPrerequisites` | 0.5% (1/212) | 容器 |  |
| `researchPrerequisites/li` | 0.5% (1/212) | 文本 | FertilityProcedures |
| `skillRequirements` | 13.7% (29/212) | 容器 |  |
| `skillRequirements/Cooking` | 2.8% (6/212) | 数值 | 6 / 8 |
| `skillRequirements/Crafting` | 1.4% (3/212) | 数值 | 8 |
| `skillRequirements/Medicine` | 8.0% (17/212) | 数值 | 3 / 4 / 5 |
| `smeltingWorkAmount` | 0.5% (1/212) | 数值 | 1600 |
| `soundWorking` | 17.0% (36/212) | 文本 | MechGestatorCycle_Initiating / Recipe_Brewing / Recipe_ButcherCorpseFlesh |
| `specialProducts` | 2.8% (6/212) | 容器 |  |
| `specialProducts/li` | 2.8% (6/212) | 文本 | Butchery / Smelted / StoneBlocks |
| `successfullyRemovedHediffMessage` | 4.7% (10/212) | 文本 | {0} has successfully implanted an IUD in {1}. / {0} has successfully performed a vasectomy on {1}. / {0} has s |
| `surgeryIgnoreEnvironment` | 0.5% (1/212) | 布尔 | true |
| `surgeryOutcomeEffect` | 6.6% (14/212) | 容器/文本 | ImplantXenogerm / SurgeryOutcomeBase / SurgeryOutcomeMinorFailure |
| `surgerySuccessChanceFactor` | 3.3% (7/212) | 数值 | 1.2 / 1.5 / 2 |
| `targetCountAdjustment` | 1.4% (3/212) | 数值 | 1 / 20 / 50 |
| `targetsBodyPart` | 7.5% (16/212) | 布尔 | false |
| `uiIconPath` | 0.9% (2/212) | 文本 | Things/Item/Special/PorcupineQuill / UI/Icons/SurgicalInspection |
| `uiIconThing` | 4.2% (9/212) | 文本 | HemogenPack / HumanEmbryo / HumanOvum |
| `unfinishedThingDef` | 1.4% (3/212) | 文本 | UnfinishedComponent / UnfinishedGun |
| `workAmount` | 25.5% (54/212) | 数值 | 1200 / 2000 / 450 |
| `workerClass` | 13.2% (28/212) | 文本 | Recipe_AddHediff / Recipe_ExtractHemogen / Recipe_GhoulInfusion |
| `workerCounterClass` | 0.9% (2/212) | 文本 | RecipeWorkerCounter_ButcherAnimals / RecipeWorkerCounter_MakeStoneBlocks |
| `workSkill` | 8.0% (17/212) | 文本 | Cooking / Crafting / Medicine |
| `workSkillLearnFactor` | 1.4% (3/212) | 数值 | 0 / 16 / 2 |
| `workSpeedStat` | 17.0% (36/212) | 文本 | CookSpeed / DrugCookingSpeed / GeneralLaborSpeed |

## 四、原版 defName 一览（共 212 个，列出前 60）

```text
``                                ``                                ``                                ``                              
``                                ``                                ``                                `ButcherCorpseMechanoid`        
`SmashCorpseMechanoid`            ``                                `CentipedeGunner`                 `CentipedeBurner`               
`Militor`                         `Lifter`                          `Constructoid`                    `Legionary`                     
`ImplantEmbryo`                   ``                                ``                                `RemoveArmorskinGland`          
`RemoveStoneskinGland`            ``                                `Agrihand`                        `Cleansweeper`                  
``                                `RemovePainstopper`               ``                                ``                              
`RemovePilotAssistant`            `RemovePsychicSensitizer`         `RemovePsychicHarmonizer`         `RemovePsychicReader`           
`RemoveNeurocalculator`           `RemoveLearningAssistant`         `RemoveGastroAnalyzer`            `RemoveImmunoenhancer`          
`RemoveCoagulator`                `RemoveHealingEnhancer`           `RemoveToughskinGland`            `RemoveAestheticShaper`         
`RemoveAestheticNose`             `RemoveLoveEnhancer`              `RemoveCircadianAssistant`        `RemoveCircadianHalfCycler`     
`RemoveHandTalon`                 `RemoveElbowBlade`                `RemoveKneeSpike`                 `RemoveVenomFangs`              
`RemoveVenomTalon`                `TubalLigation`                   `InstallPegLeg`                   `InstallWoodenHand`             
`InstallDenture`                  ``                                `Vasectomy`                       `ImplantIUD`                    
`InstallWoodenFoot`               ``                                ``                                `ExtractHemogenPack`            
```

_余下 152 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
