# PreceptDef

- **所属线**：理念线
- **原版实例数**：223
- **字段路径数**：245
- **资料片**：Anomaly、Biotech、Core、Ideology、Odyssey、Royalty
- **原版出处**：`Ideology/Defs/PreceptDefs/Precepts_Ritual.xml`、`Ideology/Defs/PreceptDefs/Precepts_Lovin.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<PreceptDef ParentName="FuneralBase">
    <defName>Funeral</defName>
    <label>funeral</label>
    <extraTextPawnDeathLetter>{PAWN_nameDef} should be buried and given a funeral so {PAWN_possessive} friends and family can say farewell.</extraTextPawnDeathLetter>
  </PreceptDef>

  
```

> 来自 `Ideology/Defs/PreceptDefs/Precepts_Ritual.xml`，defName = `Funeral`，XML 节点数 4（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
comps/li                                       [容器]
comps/li/eventDef                              [文本]  例：BloodfeederDied / InvolvedInPsychicRitual / PropagateBloodfeederGene
comps/li/thought                               [文本]  例：Inhumanizing_Required_Human / InvolvedInPsychicRitual_Abhorrent / InvolvedInPsychicRitual_Social_Abhorrent
defName                                        [文本]  例：Inhumanizing_Required / PsychicRituals_Abhorrent / PsychicRituals_Disapproved
description                                    [文本]  例：Connecting with psychic flows brings us closer to truth. / Human morality and feeling are a distraction. We must leave humanity behind.\n\n / Psychic rituals are utterly evil.
label                                          [文本]  例：abhorrent / disapproved / exalted
```

## 三、全量字段表（245 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `abilityStatFactors` | 0.4% (1/223) | 容器 |  |
| `abilityStatFactors/li` | 0.4% (1/223) | 容器 |  |
| `abilityStatFactors/li/ability` | 0.4% (1/223) | 文本 | WorkDrive |
| `abilityStatFactors/li/modifiers` | 0.4% (1/223) | 容器 |  |
| `abilityStatFactors/li/modifiers/Ability_Duration` | 0.4% (1/223) | 数值 | 3 |
| `activationBelieverCount` | 0.4% (1/223) | 数值 | 3 |
| `allowDuplicates` | 3.1% (7/223) | 布尔 | false / true |
| `allowOptionalRitualObligations` | 0.4% (1/223) | 布尔 | true |
| `apparelPreceptSwapDef` | 0.9% (2/223) | 文本 | ApparelDesired_Soft_Subordinate / ApparelDesired_Strong_Subordinate |
| `approvesOfBlindness` | 1.8% (4/223) | 布尔 | true |
| `approvesOfCharity` | 1.4% (3/223) | 布尔 | true |
| `approvesOfRaiding` | 0.4% (1/223) | 布尔 | true |
| `approvesOfSlavery` | 1.4% (3/223) | 布尔 | true |
| `associatedMemes` | 39.5% (88/223) | 容器 |  |
| `associatedMemes/li` | 52.0% (116/223) | 文本 | Collectivist / FleshPurity / Individualist |
| `biosculpterPodCycleSpeedFactor` | 0.4% (1/223) | 数值 | 2 |
| `blindPawnChance` | 1.4% (3/223) | 数值 | 0.1 / 0.25 / 0.5 |
| `blindPsychicSensitivityOffset` | 0.4% (1/223) | 数值 | 0.3 |
| `buildingDefChances` | 0.9% (2/223) | 容器 |  |
| `buildingDefChances/Altar_Grand` | 0.4% (1/223) | 数值 | 1 |
| `buildingDefChances/Altar_Large` | 0.4% (1/223) | 数值 | 1 |
| `buildingDefChances/Altar_Medium` | 0.4% (1/223) | 数值 | 1 |
| `buildingDefChances/Altar_Small` | 0.4% (1/223) | 数值 | 1 |
| `buildingDefChances/ChristmasTree` | 0.4% (1/223) | 数值 | 0 |
| `buildingDefChances/Ideogram` | 0.4% (1/223) | 数值 | 4 |
| `buildingDefChances/KneelPillow` | 0.4% (1/223) | 数值 | 1 |
| `buildingDefChances/KneelSheet` | 0.4% (1/223) | 数值 | 1 |
| `buildingDefChances/Pew` | 0.4% (1/223) | 数值 | 1 |
| `buildingDefChances/SculptureGrand` | 0.4% (1/223) | 数值 | 1 |
| `buildingDefChances/SculptureLarge` | 0.4% (1/223) | 数值 | 1 |
| `buildingDefChances/SculptureSmall` | 0.4% (1/223) | 数值 | 1 |
| `buildingMinExpectations` | 0.9% (2/223) | 容器 |  |
| `buildingMinExpectations/li` | 2.2% (5/223) | 文本 | High / Low / Moderate |
| `buildingRoomRequirements` | 0.4% (1/223) | 容器 |  |
| `buildingRoomRequirements/li` | 1.8% (4/223) | 容器 |  |
| `buildingRoomRequirements/li/area` | 0.4% (1/223) | 数值 | 25 |
| `buildingRoomRequirements/li/count` | 0.4% (1/223) | 数值 | 4 |
| `buildingRoomRequirements/li/impressiveness` | 0.4% (1/223) | 数值 | 60 |
| `buildingRoomRequirements/li/labelKey` | 0.4% (1/223) | 文本 | RoomRequirementAllFloored |
| `buildingRoomRequirements/li/tags` | 0.4% (1/223) | 容器 |  |
| `buildingRoomRequirements/li/tags/li` | 0.9% (2/223) | 文本 | FineFloor / Floor |
| `buildingRoomRequirements/li/thingDef` | 0.4% (1/223) | 文本 | Column |
| `buildingRoomRequirementsFixed` | 0.4% (1/223) | 容器 |  |
| `buildingRoomRequirementsFixed/li` | 0.9% (2/223) | 容器 |  |
| `buildingRoomRequirementsFixed/li/buildingTags` | 0.9% (2/223) | 容器 |  |
| `buildingRoomRequirementsFixed/li/buildingTags/li` | 0.9% (2/223) | 文本 | Bed / Production |
| `buildingRoomRequirementsFixed/li/labelKey` | 0.9% (2/223) | 文本 | RoomRequirementNoBeds / RoomRequirementNoProductionFacilities |
| `canGenerateAsSpecialPrecept` | 4.5% (10/223) | 布尔 | false |
| `canRemoveInUI` | 1.4% (3/223) | 布尔 | false |
| `canUseAlreadyUsedThingDef` | 0.4% (1/223) | 布尔 | true |
| `capitalizeAsTitle` | 0.9% (2/223) | 布尔 | false |
| `certaintyLossFactor` | 0.4% (1/223) | 数值 | 0.5 |
| `classic` | 12.1% (27/223) | 布尔 | true |
| `classicExtra` | 2.2% (5/223) | 布尔 | true |
| `classicModeOnly` | 0.9% (2/223) | 布尔 | true |
| `comps` | 67.7% (151/223) | 容器 |  |
| `comps/li` | 233.6% (521/223) | 容器 |  |
| `comps/li/buildingDef` | 0.4% (1/223) | 文本 | GrowthVat |
| `comps/li/chance` | 1.8% (4/223) | 数值 | 0.75 / 0.95 |
| `comps/li/description` | 53.4% (119/223) | 文本 | Bloodfeeder / No psychic ritual for {DURATION} / Participate in psychic ritual |
| `comps/li/displayDescription` | 5.4% (12/223) | 布尔 | false |
| `comps/li/doerMustBeMyIdeo` | 1.4% (3/223) | 布尔 | true |
| `comps/li/eventDef` | 164.1% (366/223) | 文本 | BloodfeederDied / InvolvedInPsychicRitual / PropagateBloodfeederGene |
| `comps/li/eventLabel` | 3.6% (8/223) | 文本 | blinded someone / converted new member / enslaved a prisoner |
| `comps/li/gender` | 10.8% (24/223) | 文本 | Female / Male / SubordinateGender |
| `comps/li/mentalBreakDef` | 0.4% (1/223) | 文本 | HumanityBreak |
| `comps/li/nullifyingHediffs` | 0.9% (2/223) | 容器 |  |
| `comps/li/nullifyingHediffs/li` | 0.9% (2/223) | 文本 | Inhumanized |
| `comps/li/nullifyingTraits` | 3.6% (8/223) | 容器 |  |
| `comps/li/nullifyingTraits/DrugDesire` | 5.4% (12/223) | 数值 | 1 / 2 |
| `comps/li/nullifyingTraits/li` | 1.4% (3/223) | 文本 | Bloodlust / Psychopath |
| `comps/li/onlyForNonSlaves` | 4.0% (9/223) | 布尔 | true |
| `comps/li/points` | 9.4% (21/223) | 数值 | 1 / 2 / 3 |
| `comps/li/removesThought` | 2.7% (6/223) | 文本 | CharityFulfilled_Essential_Beggars / CharityFulfilled_Important_Beggars / CharityRefused_Essential_Pilgrims |
| `comps/li/requireFacility` | 0.4% (1/223) | 容器 |  |
| `comps/li/requireFacility/def` | 0.4% (1/223) | 文本 | SleepAccelerator |
| `comps/li/thought` | 196.9% (439/223) | 文本 | Inhumanizing_Required_Human / InvolvedInPsychicRitual_Abhorrent / InvolvedInPsychicRitual_Social_Abhorrent |
| `comps/li/thoughtStageDescriptions` | 11.2% (25/223) | 容器 |  |
| `comps/li/thoughtStageDescriptions/li` | 29.6% (66/223) | 文本 | All preferred xenotypes / Bloodfeeder master / No bloodfeeder master |
| `comps/li/tooltipShowMoodRange` | 5.4% (12/223) | 布尔 | true |
| `conditionalStatAffecters` | 0.4% (1/223) | 容器 |  |
| `conditionalStatAffecters/li` | 0.4% (1/223) | 容器 |  |
| `conditionalStatAffecters/li/statOffsets` | 0.4% (1/223) | 容器 |  |
| `conditionalStatAffecters/li/statOffsets/WorkSpeedGlobal` | 0.4% (1/223) | 数值 | 0.2 |
| `conflictingMemes` | 18.4% (41/223) | 容器 |  |
| `conflictingMemes/li` | 22.9% (51/223) | 文本 | Blindsight / Guilty / HumanPrimacy |
| `convertPowerFactor` | 0.4% (1/223) | 数值 | 2 |
| `countsTowardsPreceptLimit` | 10.3% (23/223) | 布尔 | false / true |
| `createsRoleEmptyThought` | 0.4% (1/223) | 布尔 | False |
| `deactivationBelieverCount` | 0.4% (1/223) | 数值 | 1 |
| `defaultDrugPolicyOverride` | 0.9% (2/223) | 文本 | NoDrugs |
| `defaultSelectionWeight` | 15.2% (34/223) | 数值 | 0 / 1 |
| `defName` | 96.4% (215/223) | 文本 | Inhumanizing_Required / PsychicRituals_Abhorrent / PsychicRituals_Disapproved |
| `description` | 91.9% (205/223) | 文本 | Connecting with psychic flows brings us closer to truth. / Human morality and feeling are a distraction. We mu |
| `disablesNeeds` | 0.4% (1/223) | 容器 |  |
| `disablesNeeds/li` | 0.4% (1/223) | 文本 | Outdoors |
| `disallowFarmingCamps` | 1.4% (3/223) | 布尔 | true |
| `disallowHuntingCamps` | 4.0% (9/223) | 布尔 | true |
| `disallowLoggingCamps` | 1.4% (3/223) | 布尔 | true |
| `disallowMiningCamps` | 1.4% (3/223) | 布尔 | true |
| `displayOrderInImpact` | 55.6% (124/223) | 数值 | -100 / 100 / 1000 |
| `displayOrderInIssue` | 63.7% (142/223) | 数值 | 0 / 10 / 20 |
| `enabledForNPCFactions` | 1.8% (4/223) | 布尔 | false |
| `enablesNeeds` | 0.4% (1/223) | 容器 |  |
| `enablesNeeds/li` | 0.4% (1/223) | 文本 | Indoors |
| `exclusionTags` | 7.6% (17/223) | 容器 |  |
| `exclusionTags/li` | 10.3% (23/223) | 文本 | InsectMeatEatingLoved / KillingAnimalsBad / SlaughteringAnimalsBad |
| `expectationsOffset` | 0.9% (2/223) | 数值 | 2 |
| `extraTextPawnDeathLetter` | 0.4% (1/223) | 文本 | {PAWN_nameDef} should be buried and given a funeral so {PAWN_possessive} friends |
| `genderPrefersNudity` | 1.8% (4/223) | 文本 | Female / Male |
| `grantedAbilities` | 4.5% (10/223) | 容器 |  |
| `grantedAbilities/li` | 7.6% (17/223) | 文本 | ConversionRitual / Convert / Counsel |
| `growthVatSpeedFactor` | 0.4% (1/223) | 数值 | 1.3 |
| `iconIgnoresIdeoColor` | 0.4% (1/223) | 布尔 | true |
| `iconPath` | 11.2% (25/223) | 文本 | UI/Icons/Rituals/GiveBirth / UI/Icons/Rituals/RitualFestival / UI/Icons/Rituals/RitualFuneral |
| `ignoreLimitsInEditMode` | 3.1% (7/223) | 布尔 | false / true |
| `ignoreNameUniqueness` | 1.8% (4/223) | 布尔 | true |
| `impact` | 84.3% (188/223) | 文本 | High / Low / Medium |
| `issue` | 88.3% (197/223) | 文本 | Bloodfeeders / Inhumanizing / PsychicRituals |
| `label` | 93.7% (209/223) | 文本 | abhorrent / disapproved / exalted |
| `leaderRole` | 0.4% (1/223) | 布尔 | true |
| `likesHumanLeatherApparel` | 1.4% (3/223) | 布尔 | true |
| `listedForRoles` | 0.4% (1/223) | 布尔 | false |
| `maxCount` | 1.4% (3/223) | 数值 | 18 / 3 / 5 |
| `mergeRitualGizmosFromAllIdeos` | 1.8% (4/223) | 布尔 | true |
| `nameMaker` | 5.4% (12/223) | 文本 | NamerIdeoBuilding / NamerIdeoRelic / NamerRoleMoralist |
| `notifyPlayerOnOpportunity` | 0.9% (2/223) | 布尔 | false |
| `opposedWorkTypes` | 2.7% (6/223) | 容器 |  |
| `opposedWorkTypes/li` | 2.7% (6/223) | 文本 | Hunting / Mining |
| `preceptClass` | 10.8% (24/223) | 文本 | Precept_Animal / Precept_Apparel / Precept_Ritual |
| `preceptInstanceCountCurve` | 1.4% (3/223) | 容器 |  |
| `preceptInstanceCountCurve/points` | 1.4% (3/223) | 容器 |  |
| `preceptInstanceCountCurve/points/li` | 2.7% (6/223) | 文本 | (0.5, 1) / (0.5, 2) / (1.0, 2) |
| `prefersDarkness` | 0.4% (1/223) | 布尔 | true |
| `prefersNudity` | 1.8% (4/223) | 布尔 | true |
| `prefersSlabBed` | 0.4% (1/223) | 布尔 | true |
| `proselytizes` | 0.4% (1/223) | 布尔 | true |
| `receivesExpectationsQualityOffset` | 2.2% (5/223) | 布尔 | true |
| `requiredMemes` | 19.3% (43/223) | 容器 |  |
| `requiredMemes/li` | 29.1% (65/223) | 文本 | AnimalPersonhood / Inhuman / Shipborn |
| `requiredScars` | 1.4% (3/223) | 数值 | 1 / 3 / 5 |
| `restrictToSupremeGenderChance` | 0.9% (2/223) | 数值 | 0.5 / 1 |
| `ritualPatternBase` | 9.4% (21/223) | 文本 | CelebrationPartyChat / ChildBirth / FuneralNoCorpse |
| `roleApparelRequirementCountCurve` | 1.4% (3/223) | 容器 |  |
| `roleApparelRequirementCountCurve/points` | 1.4% (3/223) | 容器 |  |
| `roleApparelRequirementCountCurve/points/li` | 2.7% (6/223) | 文本 | (0, 1) / (0.5, 1) / (1, 1) |
| `roleApparelRequirements` | 2.7% (6/223) | 容器 |  |
| `roleApparelRequirements/li` | 13.9% (31/223) | 容器 |  |
| `roleApparelRequirements/li/allowedFactionCategoryTags` | 2.2% (5/223) | 容器 |  |
| `roleApparelRequirements/li/allowedFactionCategoryTags/li` | 2.2% (5/223) | 文本 | Tribal |
| `roleApparelRequirements/li/anyMemeRequired` | 2.7% (6/223) | 容器 |  |
| `roleApparelRequirements/li/anyMemeRequired/li` | 3.1% (7/223) | 文本 | Rancher / Ritualist / Supremacist |
| `roleApparelRequirements/li/disallowedFactionCategoryTags` | 2.2% (5/223) | 容器 |  |
| `roleApparelRequirements/li/disallowedFactionCategoryTags/li` | 2.2% (5/223) | 文本 | Tribal |
| `roleApparelRequirements/li/requirement` | 13.9% (31/223) | 容器 |  |
| `roleApparelRequirements/li/requirement/bodyPartGroupsMatchAny` | 13.9% (31/223) | 容器 |  |
| `roleApparelRequirements/li/requirement/bodyPartGroupsMatchAny/li` | 25.6% (57/223) | 文本 | FullHead / Legs / Torso |
| `roleApparelRequirements/li/requirement/requiredDefs` | 13.0% (29/223) | 容器 |  |
| `roleApparelRequirements/li/requirement/requiredDefs/li` | 13.0% (29/223) | 文本 | Apparel_CeremonialCultistMask / Apparel_Slicecap / Apparel_VisageMask |
| `roleApparelRequirements/li/requirement/requiredTags` | 0.9% (2/223) | 容器 |  |
| `roleApparelRequirements/li/requirement/requiredTags/li` | 0.9% (2/223) | 文本 | Cape |
| `roleDisabledWorkTags` | 3.6% (8/223) | 容器 |  |
| `roleDisabledWorkTags/li` | 17.0% (38/223) | 文本 | Cooking / Crafting / Mining |
| `roleEffects` | 3.6% (8/223) | 容器 |  |
| `roleEffects/li` | 10.3% (23/223) | 容器 |  |
| `roleEffects/li/factor` | 0.4% (1/223) | 数值 | 0.2 |
| `roleEffects/li/modifier` | 8.1% (18/223) | 数值 | -0.5 / 0.3 / 0.7 |
| `roleEffects/li/offset` | 0.4% (1/223) | 数值 | 1 |
| `roleEffects/li/statDef` | 8.1% (18/223) | 文本 | AimingDelayFactor / MeleeDodgeChance / MeleeHitChance |
| `roleEffects/li/thoughtDef` | 0.4% (1/223) | 文本 | TendedByMedicalSpecialist |
| `roleRequiredWorkTagAny` | 1.8% (4/223) | 容器 |  |
| `roleRequiredWorkTagAny/li` | 2.2% (5/223) | 文本 | Animals / Constructing / Crafting |
| `roleRequiredWorkTags` | 2.2% (5/223) | 容器 |  |
| `roleRequiredWorkTags/li` | 2.7% (6/223) | 文本 | Intellectual / Shooting / Social |
| `roleRequirements` | 4.5% (10/223) | 容器 |  |
| `roleRequirements/li` | 4.9% (11/223) | 容器 |  |
| `roleRequirements/li/labelKey` | 1.4% (3/223) | 文本 | RoleRequirementLabelSameIdeo / RoleRequirementLabelSupremeGender |
| `roleRequirements/li/skills` | 3.6% (8/223) | 容器 |  |
| `roleRequirements/li/skills/Animals` | 0.4% (1/223) | 数值 | 6 |
| `roleRequirements/li/skills/Construction` | 0.4% (1/223) | 数值 | 6 |
| `roleRequirements/li/skills/Crafting` | 0.4% (1/223) | 数值 | 6 |
| `roleRequirements/li/skills/Intellectual` | 0.4% (1/223) | 数值 | 6 |
| `roleRequirements/li/skills/Medicine` | 0.4% (1/223) | 数值 | 6 |
| `roleRequirements/li/skills/Melee` | 0.4% (1/223) | 数值 | 6 |
| `roleRequirements/li/skills/Mining` | 0.4% (1/223) | 数值 | 6 |
| `roleRequirements/li/skills/Plants` | 0.4% (1/223) | 数值 | 6 |
| `roleRequirements/li/skills/Shooting` | 0.4% (1/223) | 数值 | 6 |
| `roleTags` | 4.5% (10/223) | 容器 |  |
| `roleTags/li` | 4.5% (10/223) | 文本 | Leader / MeleeSpecialist / Moralist |
| `roomRequirementCountCurve` | 0.4% (1/223) | 容器 |  |
| `roomRequirementCountCurve/points` | 0.4% (1/223) | 容器 |  |
| `roomRequirementCountCurve/points/li` | 0.9% (2/223) | 文本 | (0.5, 1) / (1.0, 2) |
| `selectionWeight` | 5.8% (13/223) | 数值 | 0.75 / 1.0 |
| `showRitualFloatMenuOption` | 1.4% (3/223) | 布尔 | false |
| `skipOpportunityLettersBeforeDay` | 0.4% (1/223) | 数值 | 0 |
| `sourceAbilityDef` | 0.9% (2/223) | 文本 | ConversionRitual / LeaderSpeech |
| `sourcePawnRoleDef` | 0.9% (2/223) | 文本 | IdeoRole_Leader / IdeoRole_Moralist |
| `statFactors` | 8.1% (18/223) | 容器 |  |
| `statFactors/AnimalGatherYield` | 0.4% (1/223) | 数值 | 1.2 |
| `statFactors/AnimalsLearningFactor` | 0.4% (1/223) | 数值 | 2.0 |
| `statFactors/BondAnimalChanceFactor` | 0.4% (1/223) | 数值 | 2 |
| `statFactors/ButcheryFleshEfficiency` | 0.4% (1/223) | 数值 | 1.2 |
| `statFactors/CertaintyLossFactor` | 1.4% (3/223) | 数值 | 0.4 / 0.6 / 0.8 |
| `statFactors/DrugHarvestYield` | 0.4% (1/223) | 数值 | 1.5 |
| `statFactors/DrugSynthesisSpeed` | 0.4% (1/223) | 数值 | 1.5 |
| `statFactors/PlantWorkSpeed` | 0.4% (1/223) | 数值 | 0.70 |
| `statFactors/ResearchSpeed` | 2.2% (5/223) | 数值 | 0.25 / 0.5 / 0.75 |
| `statFactors/SocialIdeoSpreadFrequencyFactor` | 1.4% (3/223) | 数值 | 3 / 5 / 7 |
| `statFactors/StudyEfficiency` | 1.8% (4/223) | 数值 | 0.5 / 0.75 / 1.25 |
| `statFactors/TameAnimalChance` | 0.9% (2/223) | 数值 | 1.2 / 2 |
| `statOffsets` | 6.3% (14/223) | 容器 |  |
| `statOffsets/AnimalProductsSellImprovement` | 0.4% (1/223) | 数值 | 0.1 |
| `statOffsets/CaravanBonusSpeedFactor` | 0.4% (1/223) | 数值 | 0.3 |
| `statOffsets/DrugSellPriceImprovement` | 0.4% (1/223) | 数值 | 0.1 |
| `statOffsets/FishingSpeed` | 0.4% (1/223) | 数值 | -0.25 |
| `statOffsets/FishingYield` | 0.9% (2/223) | 数值 | -0.10 / 0.10 |
| `statOffsets/LearningRateFactor` | 0.4% (1/223) | 数值 | 0.2 |
| `statOffsets/MeleeDodgeChanceIndoorsDarkOffset` | 0.4% (1/223) | 数值 | 0.1 |
| `statOffsets/MeleeDodgeChanceIndoorsLitOffset` | 0.4% (1/223) | 数值 | -0.1 |
| `statOffsets/MeleeDodgeChanceOutdoorsDarkOffset` | 0.4% (1/223) | 数值 | 0.1 |
| `statOffsets/MeleeDodgeChanceOutdoorsLitOffset` | 0.4% (1/223) | 数值 | -0.1 |
| `statOffsets/MeleeHitChanceIndoorsDarkOffset` | 0.4% (1/223) | 数值 | 0.1 |
| `statOffsets/MeleeHitChanceIndoorsLitOffset` | 0.4% (1/223) | 数值 | -0.1 |
| `statOffsets/MeleeHitChanceOutdoorsDarkOffset` | 0.4% (1/223) | 数值 | 0.1 |
| `statOffsets/MeleeHitChanceOutdoorsLitOffset` | 0.4% (1/223) | 数值 | -0.1 |
| `statOffsets/MiningYield` | 0.4% (1/223) | 数值 | 0.1 |
| `statOffsets/PruningSpeed` | 0.4% (1/223) | 数值 | 0.25 |
| `statOffsets/PsychicRitualQualityOffset` | 0.9% (2/223) | 数值 | -0.1 / 0.1 |
| `statOffsets/ShootingAccuracyIndoorsDarkOffset` | 0.4% (1/223) | 数值 | 0.25 |
| `statOffsets/ShootingAccuracyIndoorsLitOffset` | 0.4% (1/223) | 数值 | -0.2 |
| `statOffsets/ShootingAccuracyOutdoorsDarkOffset` | 0.4% (1/223) | 数值 | 0.25 |
| `statOffsets/ShootingAccuracyOutdoorsLitOffset` | 0.4% (1/223) | 数值 | -0.2 |
| `statOffsets/WorkSpeedGlobal` | 1.4% (3/223) | 数值 | -0.08 / -0.16 |
| `statOffsets/WorkSpeedGlobalOffsetMech` | 0.4% (1/223) | 数值 | 0.2 |
| `takeNameFrom` | 1.4% (3/223) | 文本 | Funeral / Trial |
| `tipLabelOverride` | 0.9% (2/223) | 文本 | Prisoner/slave gladiator duel / Public execution |
| `useChoicesFromBuildingDefs` | 2.2% (5/223) | 布尔 | true |
| `useCooldownFromAbilityGroupDef` | 1.4% (3/223) | 文本 | Leader / Moralist |
| `useRepeatPenalty` | 2.2% (5/223) | 布尔 | false |
| `usesIdeoVisualEffects` | 1.8% (4/223) | 布尔 | false |
| `visible` | 6.3% (14/223) | 布尔 | false / true |
| `warnPlayerOnDesignateChopTree` | 1.4% (3/223) | 布尔 | true |
| `warnPlayerOnDesignateMine` | 1.4% (3/223) | 布尔 | true |
| `willingToConstructOtherIdeoBuildables` | 1.4% (3/223) | 布尔 | true |
| `workerClass` | 2.7% (6/223) | 文本 | PreceptWorker_Animal / PreceptWorker_Apparel / PreceptWorker_Building |

## 四、原版 defName 一览（共 223 个，列出前 60）

```text
`Funeral`                         `TrialPrisoner`                   `TrialMentalState`                ``                              
`Classic_DrumParty`               `Classic_DanceParty`              `Execution_DontCare`              `Proselytizing_Occasionally`    
`Proselytizing_Sometimes`         `Proselytizing_Frequently`        `Research_Normal`                 `FuneralNoCorpse`               
`Festival`                        `DateRitualConsumable`            `VoidStudy_VeryInefficient`       `VoidStudy_Inefficient`         
`VoidStudy_Efficient`             `VoidStudy_VeryEfficient`         `MechanoidLabor_Enhanced`         `Comfort_Ignored`               
`MarriageName_Random`             `Slavery_Acceptable`              `ThroneSpeech`                    `Cannibalism_Acceptable`        
`Nudity_Male_NoRules`             `Nudity_Female_NoRules`           `Research_ExtremelySlow`          `Research_VerySlow`             
`Research_Slow`                   `Research_Fast`                   `Research_VeryFast`               `Trial`                         
`SpouseCount_Male_Unlimited`      `SpouseCount_Female_Unlimited`    `Biosculpting_Accelerated`        `Inhumanizing_Required`         
`Slavery_Classic`                 `Bonding_Disapproved`             `Research_None`                   ``                              
`BioSculpter_Despised`            `Lovin_Free`                      `Blind_Psysense`                  `MiningYield_High`              
``                                `NeuralSupercharge_Preferred`     `NutrientPasteEating_Disgusting`  `AnimalConnection_Strong`       
`SlabBed_Preferred`               `Lovin_FreeApproved`              `Nudity_Female_UncoveredGroinDisapproved`  `Nudity_Male_UncoveredGroinOrChestDisapproved`
`OrganUse_Acceptable`             `LeaderSpeech`                    `RoleChange`                      `RoughLiving_Welcomed`          
`SleepAccelerator_Preferred`      `AgeReversal_Demanded`            `ChildLabor_Disapproved`          `NutrientPasteEating_DontMind`  
```

_余下 163 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
