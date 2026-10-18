# StatDef

- **所属线**：系统线
- **原版实例数**：256
- **字段路径数**：164
- **资料片**：Anomaly、Biotech、Core、Ideology、Odyssey、Royalty
- **原版出处**：`Biotech/Defs/Stats/Stats_Pawns_General.xml`、`Ideology/Defs/StatDefs/Stats_Basics_Special.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<StatDef ParentName="MechanitorStatBase">
    <defName>MechBandwidth</defName>
    <label>mech bandwidth</label>
    <description>How much bandwidth a mechanitor has. More bandwidth allows a mechanitor to produce and control more mechs at the same time.\n\nLosing bandwidth means losing control of mechs, leaving them without an overseer. Such mechs can eventually become feral if not re-dominated.</description>
  </StatDef>

  
```

> 来自 `Biotech/Defs/Stats/Stats_Pawns_General.xml`，defName = `MechBandwidth`，XML 节点数 4（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：ColdContainmentBonus / ContainmentStrength / EntityStudyRate
description                                    [文本]  例：How securely this can contain an entity. This is improved by stronger walls and  / The containment strength needed to contain this entity properly. An entity in a  / The rate at which this person generates knowledge from studying unnatural entiti
label                                          [文本]  例：cold containment bonus / containment strength / entity study rate
```

## 三、全量字段表（164 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `alwaysHide` | 4.7% (12/256) | 布尔 | true |
| `applyFactorsIfNegative` | 1.2% (3/256) | 布尔 | false |
| `cacheable` | 5.9% (15/256) | 布尔 | true |
| `capacityFactors` | 16.4% (42/256) | 容器 |  |
| `capacityFactors/li` | 31.6% (81/256) | 容器 |  |
| `capacityFactors/li/allowedDefect` | 5.9% (15/256) | 数值 | 0.05 / 0.20 |
| `capacityFactors/li/capacity` | 31.6% (81/256) | 文本 | Breathing / Manipulation / Metabolism |
| `capacityFactors/li/max` | 18.4% (47/256) | 数值 | 1 / 1.1 / 1.2 |
| `capacityFactors/li/weight` | 31.6% (81/256) | 数值 | 0.3 / 0.5 / 0.95 |
| `capacityOffsets` | 1.9% (5/256) | 容器 |  |
| `capacityOffsets/li` | 3.9% (10/256) | 容器 |  |
| `capacityOffsets/li/capacity` | 3.9% (10/256) | 文本 | Manipulation / Moving / Sight |
| `capacityOffsets/li/max` | 3.1% (8/256) | 数值 | 1 / 1.4 / 1.5 |
| `capacityOffsets/li/scale` | 3.9% (10/256) | 数值 | -0.5 / 12 / 18 |
| `category` | 80.5% (206/256) | 文本 | Building / Containment / PawnWork |
| `defaultBaseValue` | 80.5% (206/256) | 数值 | 0 / 0.065 / 1 |
| `defName` | 95.3% (244/256) | 文本 | ColdContainmentBonus / ContainmentStrength / EntityStudyRate |
| `description` | 93.0% (238/256) | 文本 | How securely this can contain an entity. This is improved by stronger walls and  / The containment strength ne |
| `disableIfSkillDisabled` | 1.2% (3/256) | 文本 | Crafting / Social |
| `displayMaxWhenAboveOrEqual` | 0.4% (1/256) | 布尔 | true |
| `displayPriorityInCategory` | 80.1% (205/256) | 数值 | 209 / 210 / 211 |
| `finalizeEquippedStatOffset` | 1.2% (3/256) | 布尔 | false |
| `forInformationOnly` | 1.9% (5/256) | 布尔 | true |
| `formatString` | 8.2% (21/256) | 文本 | {0} per hour / {0} s / {0}/s |
| `formatStringUnfinalized` | 0.8% (2/256) | 文本 | {0} / day / {0} per day |
| `hideAtValue` | 26.2% (67/256) | 数值 | 0 / 1 / 1.0 |
| `hideInClassicMode` | 0.4% (1/256) | 布尔 | true |
| `label` | 95.3% (244/256) | 文本 | cold containment bonus / containment strength / entity study rate |
| `labelForFullStatList` | 6.2% (16/256) | 文本 | Armor - Blunt (armor stat) / Armor - Heat (armor stat) / Armor - Sharp (armor stat) |
| `maxValue` | 9.4% (24/256) | 数值 | 0.50 / 1000 / 2 |
| `minifiedThingInherits` | 1.2% (3/256) | 布尔 | true |
| `minValue` | 71.1% (182/256) | 数值 | 0 / 0.001 / 0.25 |
| `neverDisabled` | 3.5% (9/256) | 布尔 | true |
| `noSkillOffset` | 1.9% (5/256) | 数值 | 0 / 20 / 4 |
| `offsetLabel` | 0.4% (1/256) | 文本 | containment offset |
| `overridesHideStats` | 0.8% (2/256) | 布尔 | true |
| `parts` | 25.4% (65/256) | 容器 |  |
| `parts/li` | 48.4% (124/256) | 容器 |  |
| `parts/li/apparelStat` | 2.7% (7/256) | 文本 | Insulation_Cold / Insulation_Heat / PsychicSensitivityFactor |
| `parts/li/applyToNegativeValues` | 0.8% (2/256) | 布尔 | true |
| `parts/li/curve` | 4.7% (12/256) | 容器 |  |
| `parts/li/curve/points` | 4.7% (12/256) | 容器 |  |
| `parts/li/curve/points/li` | 14.8% (38/256) | 文本 | (12,0.98) / (13,1) / (3,0.5) |
| `parts/li/curve/points/li/loc` | 0.8% (2/256) | 容器 |  |
| `parts/li/curve/points/li/loc/x` | 0.8% (2/256) | 数值 | 0 / 1 |
| `parts/li/curve/points/li/loc/y` | 0.8% (2/256) | 数值 | 0.4 / 1 |
| `parts/li/customLabel` | 2.3% (6/256) | 文本 | Reading bonus / Room cleanliness |
| `parts/li/factor` | 3.1% (8/256) | 数值 | 0.66 / 0.75 / 1.1 |
| `parts/li/factorAwful` | 7.0% (18/256) | 数值 | 0.6 / 0.60 / 0.8 |
| `parts/li/factorExcellent` | 7.0% (18/256) | 数值 | 1.1 / 1.2 / 1.30 |
| `parts/li/factorExhausted` | 0.4% (1/256) | 数值 | 0.8 |
| `parts/li/factorFromGlowCurve` | 1.6% (4/256) | 容器 |  |
| `parts/li/factorFromGlowCurve/points` | 1.6% (4/256) | 容器 |  |
| `parts/li/factorFromGlowCurve/points/li` | 3.1% (8/256) | 文本 | (0,0.75) / (0,0.80) / (0.30,1.00) |
| `parts/li/factorGood` | 7.0% (18/256) | 数值 | 1.05 / 1.1 / 1.15 |
| `parts/li/factorIndoors` | 1.2% (3/256) | 数值 | 1 / 1.00 |
| `parts/li/factorLegendary` | 7.0% (18/256) | 数值 | 1.3 / 1.8 / 1.80 |
| `parts/li/factorMasterwork` | 7.0% (18/256) | 数值 | 1.2 / 1.45 / 1.5 |
| `parts/li/factorNormal` | 7.0% (18/256) | 数值 | 0.83 / 1 / 1.00 |
| `parts/li/factorOffsetOutdoors` | 0.4% (1/256) | 数值 | 0.5 |
| `parts/li/factorOffsetUnroofed` | 0.4% (1/256) | 数值 | 0.5 |
| `parts/li/factorOutdoors` | 1.2% (3/256) | 数值 | 0.75 / 0.85 |
| `parts/li/factorPoor` | 7.0% (18/256) | 数值 | 0.8 / 0.80 / 0.9 |
| `parts/li/factorStarving` | 0.4% (1/256) | 数值 | 0.7 |
| `parts/li/factorTired` | 0.4% (1/256) | 数值 | 0.96 |
| `parts/li/factorUrgentlyHungry` | 0.4% (1/256) | 数值 | 0.9 |
| `parts/li/factorVeryTired` | 0.4% (1/256) | 数值 | 0.92 |
| `parts/li/femaleFertilityAgeFactor` | 0.4% (1/256) | 容器 |  |
| `parts/li/femaleFertilityAgeFactor/points` | 0.4% (1/256) | 容器 |  |
| `parts/li/femaleFertilityAgeFactor/points/li` | 2.7% (7/256) | 文本 | (14, 0) / (20, 1) / (28, 1) |
| `parts/li/humanlikeOnly` | 4.3% (11/256) | 布尔 | true |
| `parts/li/ignoreIfIncapableOfSight` | 1.6% (4/256) | 布尔 | true |
| `parts/li/ignoreIfPrefersDarkness` | 1.6% (4/256) | 布尔 | true |
| `parts/li/includeWeapon` | 1.6% (4/256) | 布尔 | true |
| `parts/li/label` | 0.4% (1/256) | 文本 | Offset from mechanitor |
| `parts/li/maleFertilityAgeFactor` | 0.4% (1/256) | 容器 |  |
| `parts/li/maleFertilityAgeFactor/points` | 0.4% (1/256) | 容器 |  |
| `parts/li/maleFertilityAgeFactor/points/li` | 1.6% (4/256) | 文本 | (14, 0) / (18, 1) / (50, 1) |
| `parts/li/maxGainExcellent` | 0.4% (1/256) | 数值 | 1000 |
| `parts/li/maxGainGood` | 0.4% (1/256) | 数值 | 500 |
| `parts/li/maxGainLegendary` | 0.4% (1/256) | 数值 | 3000 |
| `parts/li/maxGainMasterwork` | 0.4% (1/256) | 数值 | 2000 |
| `parts/li/multiplier` | 1.9% (5/256) | 数值 | 1.5 / 2 / 3 |
| `parts/li/multiplierStat` | 1.9% (5/256) | 文本 | StuffEffectMultiplierArmor / StuffEffectMultiplierInsulation_Cold / StuffEffectMultiplierInsulation_Heat |
| `parts/li/offset` | 1.2% (3/256) | 数值 | 0.02 / 40 / 7 |
| `parts/li/offsetAwful` | 0.4% (1/256) | 数值 | 3 |
| `parts/li/offsetExcellent` | 0.4% (1/256) | 数值 | 20 |
| `parts/li/offsetGood` | 0.4% (1/256) | 数值 | 15 |
| `parts/li/offsetLegendary` | 0.4% (1/256) | 数值 | 40 |
| `parts/li/offsetMasterwork` | 0.4% (1/256) | 数值 | 30 |
| `parts/li/offsetNormal` | 0.4% (1/256) | 数值 | 10 |
| `parts/li/offsetOccupied` | 0.4% (1/256) | 数值 | 25 |
| `parts/li/offsetPoor` | 0.4% (1/256) | 数值 | 6 |
| `parts/li/pawnOnly` | 0.4% (1/256) | 布尔 | true |
| `parts/li/priority` | 1.9% (5/256) | 数值 | 100 |
| `parts/li/protectedByEdificeFactor` | 0.4% (1/256) | 数值 | 0 |
| `parts/li/radius` | 0.4% (1/256) | 数值 | 27.9 |
| `parts/li/roomStat` | 2.3% (6/256) | 文本 | AssemblySpeedFactor / ReadingBonus / ResearchSpeedFactor |
| `parts/li/stat` | 0.8% (2/256) | 文本 | ImmunityGainSpeedFactor / WorkSpeedGlobalOffsetMech |
| `parts/li/stuffPowerStat` | 1.9% (5/256) | 文本 | StuffPower_Armor_Blunt / StuffPower_Armor_Heat / StuffPower_Armor_Sharp |
| `parts/li/subtract` | 0.8% (2/256) | 布尔 | true |
| `parts/li/thingDefs` | 1.2% (3/256) | 容器 |  |
| `parts/li/thingDefs/li` | 1.2% (3/256) | 文本 | GibbetCage / SculptureTerror / Wastepack |
| `parts/li/trainableDef` | 0.8% (2/256) | 文本 | Dig |
| `parts/li/useBiologicalYears` | 3.1% (8/256) | 布尔 | true |
| `postProcessCurve` | 3.1% (8/256) | 容器 |  |
| `postProcessCurve/points` | 3.1% (8/256) | 容器 |  |
| `postProcessCurve/points/li` | 19.9% (51/256) | 文本 | (-10, 0.10) / (-20, 0.05) / (0.0, 0.50) |
| `postProcessStatFactors` | 1.2% (3/256) | 容器 |  |
| `postProcessStatFactors/li` | 1.2% (3/256) | 文本 | BandwidthCost / ShootingAccuracyChildFactor / WorkSpeedGlobal |
| `roundToFiveOver` | 1.9% (5/256) | 数值 | 100 / 200 / 300 |
| `roundValue` | 1.9% (5/256) | 布尔 | true |
| `scenarioRandomizable` | 16.4% (42/256) | 布尔 | true |
| `showDevelopmentalStageFilter` | 5.1% (13/256) | 文本 | Adult / Child / Child, Adult |
| `showIfHediffsPresent` | 0.8% (2/256) | 容器 |  |
| `showIfHediffsPresent/li` | 0.8% (2/256) | 文本 | PsychicAmplifier |
| `showIfModsLoaded` | 3.9% (10/256) | 容器 |  |
| `showIfModsLoaded/li` | 3.9% (10/256) | 文本 | ludeon.rimworld.royalty |
| `showIfModsLoadedAny` | 2.3% (6/256) | 容器 |  |
| `showIfModsLoadedAny/li` | 3.9% (10/256) | 文本 | ludeon.rimworld.biotech / ludeon.rimworld.royalty |
| `showIfUndefined` | 26.6% (68/256) | 布尔 | false / true |
| `showNonAbstract` | 0.4% (1/256) | 布尔 | true |
| `showOnAnimals` | 15.2% (39/256) | 布尔 | false / true |
| `showOnDefaultValue` | 3.5% (9/256) | 布尔 | false / true |
| `showOnDrones` | 11.7% (30/256) | 布尔 | false |
| `showOnEntities` | 5.5% (14/256) | 布尔 | false |
| `showOnHumanlikes` | 1.6% (4/256) | 布尔 | false / true |
| `showOnMechanoids` | 12.9% (33/256) | 布尔 | false / true |
| `showOnNonPowerPlants` | 0.4% (1/256) | 布尔 | false |
| `showOnNonWildManHumanlikes` | 0.4% (1/256) | 布尔 | false |
| `showOnNonWorkTables` | 0.8% (2/256) | 布尔 | false |
| `showOnPawnKind` | 1.2% (3/256) | 容器 |  |
| `showOnPawnKind/li` | 1.2% (3/256) | 文本 | Mech_Agrihand / Mech_Cleansweeper / Mech_Constructoid |
| `showOnPawns` | 5.5% (14/256) | 布尔 | false |
| `showOnPlayerMechanoids` | 0.8% (2/256) | 布尔 | true |
| `showOnSlavesOnly` | 0.4% (1/256) | 布尔 | true |
| `showOnUnhaulables` | 0.4% (1/256) | 布尔 | false |
| `showOnUntradeables` | 0.8% (2/256) | 布尔 | false |
| `showZeroBaseValue` | 0.8% (2/256) | 布尔 | false / true |
| `skillNeedFactors` | 16.4% (42/256) | 容器 |  |
| `skillNeedFactors/li` | 16.8% (43/256) | 容器 |  |
| `skillNeedFactors/li/baseValue` | 12.9% (33/256) | 数值 | 0.4 / 0.6 / 0.75 |
| `skillNeedFactors/li/bonusPerLevel` | 12.9% (33/256) | 数值 | 0.015 / 0.025 / 0.075 |
| `skillNeedFactors/li/curve` | 0.4% (1/256) | 容器 |  |
| `skillNeedFactors/li/curve/points` | 0.4% (1/256) | 容器 |  |
| `skillNeedFactors/li/curve/points/li` | 1.2% (3/256) | 文本 | (0, 1) / (10, 2) / (20, 3.5) |
| `skillNeedFactors/li/required` | 0.8% (2/256) | 布尔 | false |
| `skillNeedFactors/li/skill` | 16.8% (43/256) | 文本 | Animals / Crafting / Mining |
| `skillNeedFactors/li/valuesPerLevel` | 3.5% (9/256) | 容器 |  |
| `skillNeedFactors/li/valuesPerLevel/li` | 73.4% (188/256) | 数值 | 0.6 / 0.7 / 0.8 |
| `skillNeedOffsets` | 2.7% (7/256) | 容器 |  |
| `skillNeedOffsets/li` | 3.1% (8/256) | 容器 |  |
| `skillNeedOffsets/li/baseValue` | 3.1% (8/256) | 数值 | -0.015 / 0 / 0.2 |
| `skillNeedOffsets/li/bonusPerLevel` | 3.1% (8/256) | 数值 | -0.025 / 0.0075 / 0.09 |
| `skillNeedOffsets/li/required` | 0.8% (2/256) | 布尔 | false |
| `skillNeedOffsets/li/skill` | 3.1% (8/256) | 文本 | Intellectual / Melee / Shooting |
| `statFactors` | 7.8% (20/256) | 容器 |  |
| `statFactors/li` | 7.8% (20/256) | 文本 | Ability_EntropyGain / PlantHarvestYield / PsychicSensitivity |
| `supressDisabledError` | 0.8% (2/256) | 布尔 | true |
| `toStringNumberSense` | 0.4% (1/256) | 文本 | Offset |
| `toStringStyle` | 78.1% (200/256) | 文本 | FloatOne / Integer / PercentOne |
| `toStringStyleUnfinalized` | 2.3% (6/256) | 文本 | FloatOne |
| `valueIfMissing` | 0.8% (2/256) | 数值 | 0.4 / 0.8 |
| `workerClass` | 10.5% (27/256) | 文本 | StatWorker_ColdContainmentBonus / StatWorker_ContainmentStrength / StatWorker_Mechanitor |

## 四、原版 defName 一览（共 256 个，列出前 60）

```text
`MechBandwidth`                   `MechControlGroups`               `MarketValueIgnoreHp`             `BeautyOutdoors`                
`ShootingAccuracyOutdoorsDarkOffset`  `ShootingAccuracyOutdoorsLitOffset`  `ShootingAccuracyIndoorsDarkOffset`  `ShootingAccuracyIndoorsLitOffset`
`MeleeHitChanceOutdoorsDarkOffset`  `MeleeHitChanceOutdoorsLitOffset`  `MeleeHitChanceIndoorsDarkOffset`  `MeleeHitChanceIndoorsLitOffset`
`MeleeDodgeChanceOutdoorsDarkOffset`  `MeleeDodgeChanceOutdoorsLitOffset`  `MeleeDodgeChanceIndoorsDarkOffset`  `MeleeDodgeChanceIndoorsLitOffset`
`MechRemoteRepairDistance`        `MechRemoteShieldDistance`        `MechRemoteShieldEnergy`          `ShootingAccuracyFactor_Touch`  
`ShootingAccuracyFactor_Short`    `ShootingAccuracyFactor_Medium`   `ShootingAccuracyFactor_Long`     ``                              
`AccuracyTouch`                   `AccuracyShort`                   `AccuracyMedium`                  `AccuracyLong`                  
``                                `ResearchSpeed`                   ``                                `PsychicRitualQuality`          
`PsychicRitualQualityOffset`      `BandwidthCost`                   `StuffEffectMultiplierArmor`      `StuffEffectMultiplierInsulation_Cold`
`StuffEffectMultiplierInsulation_Heat`  ``                                `BedHungerRateFactor`             `PawnBeauty`                    
`SubstructureSupport`             `ColdContainmentBonus`            `HemogenGainFactor`               `Ability_GoodwillImpact`        
`FilthMultiplier`                 `CleaningTimeFactor`              `DoorOpenSpeed`                   `EMPResistance`                 
`FlightCooldown`                  `GravshipRange`                   `EntityStudyRate`                 `BabyPlayGainFactor`            
`BirthRitualQualityOffset`        ``                                `ControlTakingTime`               `MechEnergyUsageFactor`         
`MechEnergyLossPerHP`             `Ability_Range`                   `Ability_EffectRadius`            `CaravanBonusSpeedFactor`       
```

_余下 196 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
