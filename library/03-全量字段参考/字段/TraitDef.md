# TraitDef

- **所属线**：人物线
- **原版实例数**：51
- **字段路径数**：122
- **资料片**：Anomaly、Biotech、Core
- **原版出处**：`Anomaly/Defs/TraitDefs/Traits.xml`、`Core/Defs/TraitDefs/Traits_Singular.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<TraitDef>
    <defName>PerfectMemory</defName>
    <commonality>0</commonality>
    <degreeDatas>
      <li>
        <label>perfect memory</label>
        <description>{PAWN_nameDef} has outstanding memory, both in terms of retaining information but also muscle memory. {PAWN_possessive} skills will never decay.</description>
      </li>
    </degreeDatas>
  </TraitDef>
  
  
```

> 来自 `Anomaly/Defs/TraitDefs/Traits.xml`，defName = `PerfectMemory`，XML 节点数 7（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：BodyMastery / Joyous / Occultist
degreeDatas                                    [容器]
degreeDatas/li                                 [容器]
degreeDatas/li/description                     [文本]  例：{PAWN_nameDef} doesn't have basic needs like eating, sleeping, or comfort. {PAWN / {PAWN_nameDef} has deep knowledge of the twisted patterns of dark psychic energy / {PAWN_nameDef} has outstanding memory, both in terms of retaining information bu
degreeDatas/li/label                           [文本]  例：body mastery / joyous / occultist
```

## 三、全量字段表（122 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `allowOnHostileSpawn` | 2.0% (1/51) | 布尔 | false |
| `commonality` | 76.5% (39/51) | 数值 | 0 / 0.5 / 0.7 |
| `commonalityFemale` | 3.9% (2/51) | 数值 | 0.3 / 1.7 |
| `conflictingPassions` | 2.0% (1/51) | 容器 |  |
| `conflictingPassions/li` | 2.0% (1/51) | 文本 | Shooting |
| `conflictingTraits` | 25.5% (13/51) | 容器 |  |
| `conflictingTraits/li` | 41.2% (21/51) | 文本 | Abrasive / Nerves / Psychopath |
| `defName` | 100.0% (51/51) | 文本 | BodyMastery / Joyous / Occultist |
| `degreeDatas` | 100.0% (51/51) | 容器 |  |
| `degreeDatas/li` | 143.1% (73/51) | 容器 |  |
| `degreeDatas/li/allowedMeditationFocusTypes` | 21.6% (11/51) | 容器 |  |
| `degreeDatas/li/allowedMeditationFocusTypes/li` | 21.6% (11/51) | 文本 | Flame / Minimal / Morbid |
| `degreeDatas/li/degree` | 62.7% (32/51) | 数值 | -1 / -2 / 1 |
| `degreeDatas/li/description` | 143.1% (73/51) | 文本 | {PAWN_nameDef} doesn't have basic needs like eating, sleeping, or comfort. {PAWN / {PAWN_nameDef} has deep kno |
| `degreeDatas/li/disablesNeeds` | 3.9% (2/51) | 容器 |  |
| `degreeDatas/li/disablesNeeds/li` | 7.8% (4/51) | 文本 | Comfort / Food / Outdoors |
| `degreeDatas/li/disallowedInspirations` | 3.9% (2/51) | 容器 |  |
| `degreeDatas/li/disallowedInspirations/li` | 3.9% (2/51) | 文本 | Frenzy_Go / Frenzy_Shoot |
| `degreeDatas/li/disallowedMeditationFocusTypes` | 3.9% (2/51) | 容器 |  |
| `degreeDatas/li/disallowedMeditationFocusTypes/li` | 3.9% (2/51) | 文本 | Artistic |
| `degreeDatas/li/disallowedMentalStates` | 2.0% (1/51) | 容器 |  |
| `degreeDatas/li/disallowedMentalStates/li` | 3.9% (2/51) | 文本 | Binging_DrugExtreme / Binging_DrugMajor |
| `degreeDatas/li/disallowedThoughts` | 2.0% (1/51) | 容器 |  |
| `degreeDatas/li/disallowedThoughts/li` | 3.9% (2/51) | 文本 | EntityInRoom / ImprisonedWithEntity |
| `degreeDatas/li/disallowedThoughtsFromIngestion` | 2.0% (1/51) | 容器 |  |
| `degreeDatas/li/disallowedThoughtsFromIngestion/li` | 2.0% (1/51) | 容器 |  |
| `degreeDatas/li/disallowedThoughtsFromIngestion/li/meatSource` | 2.0% (1/51) | 文本 | Humanlike |
| `degreeDatas/li/disallowedThoughtsFromIngestion/li/thoughts` | 2.0% (1/51) | 容器 |  |
| `degreeDatas/li/disallowedThoughtsFromIngestion/li/thoughts/li` | 5.9% (3/51) | 文本 | AteHumanlikeMeatAsIngredient / AteHumanlikeMeatDirect / AteRawFood |
| `degreeDatas/li/enablesNeeds` | 2.0% (1/51) | 容器 |  |
| `degreeDatas/li/enablesNeeds/li` | 2.0% (1/51) | 文本 | Indoors |
| `degreeDatas/li/extraThoughtsFromIngestion` | 2.0% (1/51) | 容器 |  |
| `degreeDatas/li/extraThoughtsFromIngestion/li` | 2.0% (1/51) | 容器 |  |
| `degreeDatas/li/extraThoughtsFromIngestion/li/meatSource` | 2.0% (1/51) | 文本 | Humanlike |
| `degreeDatas/li/extraThoughtsFromIngestion/li/thoughtsAsIngredient` | 2.0% (1/51) | 容器 |  |
| `degreeDatas/li/extraThoughtsFromIngestion/li/thoughtsAsIngredient/li` | 2.0% (1/51) | 文本 | AteHumanlikeMeatAsIngredientCannibal |
| `degreeDatas/li/extraThoughtsFromIngestion/li/thoughtsDirect` | 2.0% (1/51) | 容器 |  |
| `degreeDatas/li/extraThoughtsFromIngestion/li/thoughtsDirect/li` | 2.0% (1/51) | 文本 | AteHumanlikeMeatDirectCannibal |
| `degreeDatas/li/hungerRateFactor` | 2.0% (1/51) | 数值 | 1.5 |
| `degreeDatas/li/label` | 143.1% (73/51) | 文本 | body mastery / joyous / occultist |
| `degreeDatas/li/marketValueFactorOffset` | 13.7% (7/51) | 数值 | -0.1 / -0.10 / -0.15 |
| `degreeDatas/li/mentalBreakInspirationGainChance` | 2.0% (1/51) | 数值 | 0.5 |
| `degreeDatas/li/mentalBreakInspirationGainReasonText` | 2.0% (1/51) | 文本 | As a suffering tortured artist, [PAWN_nameIndef] has experienced an inspiration. |
| `degreeDatas/li/mentalBreakInspirationGainSet` | 2.0% (1/51) | 容器 |  |
| `degreeDatas/li/mentalBreakInspirationGainSet/li` | 2.0% (1/51) | 文本 | Inspired_Creativity |
| `degreeDatas/li/possessions` | 33.3% (17/51) | 容器 |  |
| `degreeDatas/li/possessions/Apparel_PsychicFoilHelmet` | 3.9% (2/51) | 容器 |  |
| `degreeDatas/li/possessions/Chemfuel` | 2.0% (1/51) | 文本 | 10~20 |
| `degreeDatas/li/possessions/Dye` | 2.0% (1/51) | 文本 | 10~20 |
| `degreeDatas/li/possessions/Gold` | 2.0% (1/51) | 文本 | 10~20 |
| `degreeDatas/li/possessions/Gun_Autopistol` | 2.0% (1/51) | 容器 |  |
| `degreeDatas/li/possessions/Gun_BoltActionRifle` | 2.0% (1/51) | 容器 |  |
| `degreeDatas/li/possessions/Heart` | 2.0% (1/51) | 容器 |  |
| `degreeDatas/li/possessions/MealFine` | 2.0% (1/51) | 文本 | 1~3 |
| `degreeDatas/li/possessions/Meat_Human` | 2.0% (1/51) | 文本 | 30~60 |
| `degreeDatas/li/possessions/MedicineIndustrial` | 2.0% (1/51) | 文本 | 2~5 |
| `degreeDatas/li/possessions/MeleeWeapon_Axe` | 2.0% (1/51) | 容器 |  |
| `degreeDatas/li/possessions/MeleeWeapon_Knife` | 2.0% (1/51) | 容器 |  |
| `degreeDatas/li/possessions/MeleeWeapon_LongSword` | 2.0% (1/51) | 容器 |  |
| `degreeDatas/li/possessions/Penoxycyline` | 2.0% (1/51) | 文本 | 5~10 |
| `degreeDatas/li/possessions/RawFungus` | 2.0% (1/51) | 文本 | 30~60 |
| `degreeDatas/li/possessions/Schematic` | 2.0% (1/51) | 容器 |  |
| `degreeDatas/li/possessions/Skull` | 2.0% (1/51) | 容器 |  |
| `degreeDatas/li/possessions/TextBook` | 2.0% (1/51) | 容器 |  |
| `degreeDatas/li/possessions/WakeUp` | 2.0% (1/51) | 文本 | 5~10 |
| `degreeDatas/li/possessions/Weapon_GrenadeMolotov` | 2.0% (1/51) | 容器 |  |
| `degreeDatas/li/randomDiseaseMtbDays` | 2.0% (1/51) | 数值 | 30 |
| `degreeDatas/li/randomMentalState` | 5.9% (3/51) | 文本 | Binging_Food / EntityLiberator / FireStartingSpree |
| `degreeDatas/li/randomMentalStateMtbDaysMoodCurve` | 5.9% (3/51) | 容器 |  |
| `degreeDatas/li/randomMentalStateMtbDaysMoodCurve/points` | 5.9% (3/51) | 容器 |  |
| `degreeDatas/li/randomMentalStateMtbDaysMoodCurve/points/li` | 5.9% (3/51) | 文本 | (0, 50) / (0, 60) |
| `degreeDatas/li/renderNodeProperties` | 2.0% (1/51) | 容器 |  |
| `degreeDatas/li/renderNodeProperties/li` | 3.9% (2/51) | 容器 |  |
| `degreeDatas/li/renderNodeProperties/li/anchorTag` | 3.9% (2/51) | 文本 | LeftEye / RightEye |
| `degreeDatas/li/renderNodeProperties/li/drawData` | 3.9% (2/51) | 容器 |  |
| `degreeDatas/li/renderNodeProperties/li/drawData/dataWest` | 2.0% (1/51) | 容器 |  |
| `degreeDatas/li/renderNodeProperties/li/drawData/dataWest/flip` | 2.0% (1/51) | 布尔 | false |
| `degreeDatas/li/renderNodeProperties/li/drawData/defaultData` | 3.9% (2/51) | 容器 |  |
| `degreeDatas/li/renderNodeProperties/li/drawData/defaultData/flip` | 2.0% (1/51) | 布尔 | true |
| `degreeDatas/li/renderNodeProperties/li/drawData/defaultData/layer` | 3.9% (2/51) | 数值 | 54 |
| `degreeDatas/li/renderNodeProperties/li/drawData/defaultData/offset` | 3.9% (2/51) | 文本 | (0, 0, -0.25) |
| `degreeDatas/li/renderNodeProperties/li/drawSize` | 3.9% (2/51) | 数值 | 0.2 |
| `degreeDatas/li/renderNodeProperties/li/parentTagDef` | 3.9% (2/51) | 文本 | Head |
| `degreeDatas/li/renderNodeProperties/li/rotDrawMode` | 3.9% (2/51) | 文本 | Fresh, Rotting |
| `degreeDatas/li/renderNodeProperties/li/side` | 3.9% (2/51) | 文本 | Left / Right |
| `degreeDatas/li/renderNodeProperties/li/texPath` | 3.9% (2/51) | 文本 | Things/Pawn/Humanlike/HeadAttachments/GrayEyes/Male/GrayEyes_Male |
| `degreeDatas/li/renderNodeProperties/li/texPathFemale` | 3.9% (2/51) | 文本 | Things/Pawn/Humanlike/HeadAttachments/GrayEyes/Female/GrayEyes_Female |
| `degreeDatas/li/skillGains` | 5.9% (3/51) | 容器 |  |
| `degreeDatas/li/skillGains/Cooking` | 2.0% (1/51) | 数值 | 4 |
| `degreeDatas/li/skillGains/Medicine` | 2.0% (1/51) | 数值 | 4 |
| `degreeDatas/li/skillGains/Melee` | 2.0% (1/51) | 数值 | 4 |
| `degreeDatas/li/skillGains/Shooting` | 2.0% (1/51) | 数值 | -10 |
| `degreeDatas/li/socialFightChanceFactor` | 2.0% (1/51) | 数值 | 4 |
| `degreeDatas/li/statFactors` | 27.5% (14/51) | 容器 |  |
| `degreeDatas/li/statFactors/CertaintyLossFactor` | 21.6% (11/51) | 数值 | 0.25 / 0.5 / 2 |
| `degreeDatas/li/statFactors/IncomingDamageFactor` | 3.9% (2/51) | 数值 | 0.5 / 1.15 |
| `degreeDatas/li/statFactors/PawnTrapSpringChance` | 2.0% (1/51) | 数值 | 0.1 |
| `degreeDatas/li/statOffsets` | 62.7% (32/51) | 容器 |  |
| `degreeDatas/li/statOffsets/AimingDelayFactor` | 3.9% (2/51) | 数值 | -0.5 / 0.25 |
| `degreeDatas/li/statOffsets/EntityStudyRate` | 2.0% (1/51) | 数值 | 0.5 |
| `degreeDatas/li/statOffsets/GlobalLearningFactor` | 5.9% (3/51) | 数值 | -0.75 / 0.75 |
| `degreeDatas/li/statOffsets/ImmunityGainSpeed` | 2.0% (1/51) | 数值 | 0.30 |
| `degreeDatas/li/statOffsets/MeleeDodgeChance` | 2.0% (1/51) | 数值 | 15 |
| `degreeDatas/li/statOffsets/MeleeHitChance` | 2.0% (1/51) | 数值 | 4 |
| `degreeDatas/li/statOffsets/MentalBreakThreshold` | 13.7% (7/51) | 数值 | -0.09 / 0.08 / 0.12 |
| `degreeDatas/li/statOffsets/MoveSpeed` | 5.9% (3/51) | 数值 | -0.2 / 0.2 / 0.4 |
| `degreeDatas/li/statOffsets/PainShockThreshold` | 2.0% (1/51) | 数值 | -0.50 |
| `degreeDatas/li/statOffsets/PawnBeauty` | 7.8% (4/51) | 数值 | -1 / -2 / 1 |
| `degreeDatas/li/statOffsets/PsychicSensitivity` | 7.8% (4/51) | 数值 | -0.5 / -1 / 0.4 |
| `degreeDatas/li/statOffsets/RestRateMultiplier` | 2.0% (1/51) | 数值 | 0.50 |
| `degreeDatas/li/statOffsets/ShootingAccuracyPawn` | 3.9% (2/51) | 数值 | -5 / 5 |
| `degreeDatas/li/statOffsets/StudyEfficiency` | 2.0% (1/51) | 数值 | 1 |
| `degreeDatas/li/statOffsets/WorkSpeedGlobal` | 11.8% (6/51) | 数值 | -0.20 / -0.35 / 0.20 |
| `degreeDatas/li/theOnlyAllowedMentalBreaks` | 5.9% (3/51) | 容器 |  |
| `degreeDatas/li/theOnlyAllowedMentalBreaks/li` | 5.9% (3/51) | 文本 | Binging_Food / EntityLiberator / FireStartingSpree |
| `disabledWorkTags` | 2.0% (1/51) | 文本 | Firefighting |
| `exclusionTags` | 13.7% (7/51) | 容器 |  |
| `exclusionTags/li` | 13.7% (7/51) | 文本 | SexualOrientation / SlowFastLearner / Toughness |
| `forcedPassions` | 2.0% (1/51) | 容器 |  |
| `forcedPassions/li` | 2.0% (1/51) | 文本 | Artistic |
| `requiredWorkTags` | 9.8% (5/51) | 容器 |  |
| `requiredWorkTags/li` | 9.8% (5/51) | 文本 | Intellectual / Social / Violent |

## 四、原版 defName 一览（共 51 个，列出前 60）

```text
`PerfectMemory`                   `Joyous`                          `Recluse`                         `Nudist`                        
`GreatMemory`                     `AnnoyingVoice`                   `CreepyBreathing`                 `DislikesMen`                   
`DislikesWomen`                   `QuickSleeper`                    `Disturbing`                      `NightOwl`                      
`Gay`                             `Bisexual`                        `Asexual`                         `Transhumanist`                 
`BodyPurist`                      `Occultist`                       `Nimble`                          `Delicate`                      
`Abrasive`                        `Masochist`                       `Greedy`                          `Jealous`                       
`Tough`                           `Kind`                            `FastLearner`                     `Psychopath`                    
`SlowLearner`                     `Bloodlust`                       `Wimp`                            `Undergrounder`                 
`Ascetic`                         `TorturedArtist`                  `TooSmart`                        `Neurotic`                      
`Immunity`                        `VoidFascination`                 `Pyromaniac`                      `Gourmand`                      
`NaturalMood`                     `DrugDesire`                      `Brawler`                         `SpeedOffset`                   
`Cannibal`                        `ShootingAccuracy`                `Industriousness`                 `Beauty`                        
`PsychicSensitivity`              `Nerves`                          `BodyMastery`                   
```
