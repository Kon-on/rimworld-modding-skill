# ThoughtDef

- **所属线**：人物线
- **原版实例数**：933
- **字段路径数**：65
- **资料片**：Anomaly、Biotech、Core、Ideology、Odyssey、Royalty
- **原版出处**：`Ideology/Defs/PreceptDefs/Precepts_Charity.xml`、`Ideology/Defs/ThoughtDefs/Thoughts_Ritual_Quality.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<ThoughtDef Abstract="True" Name="CharityBase">
    <durationDays>8</durationDays>
  </ThoughtDef>

  
```

> 来自 `Ideology/Defs/PreceptDefs/Precepts_Charity.xml`，defName = ``，XML 节点数 2（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Inhumanizing_Required_Human / InvolvedInPsychicRitual_Abhorrent / InvolvedInPsychicRitual_Social_Abhorrent
stages                                         [容器]
stages/li                                      [容器]
stages/li/baseMoodEffect                       [数值]  例：-12 / -2 / -4
stages/li/description                          [文本]  例：I have touched the filthy psychic power below space. I am disgusted with myself. / I'm ashamed of my humanity. I want to embrace the void but I fear it. / To use such filthy rituals shows we are among the most base of creatures. We hav
stages/li/label                                [文本]  例：human shame / involved in psychic ritual / no psychic rituals
```

## 三、全量字段表（65 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 98.8% (922/933) | 文本 | Inhumanizing_Required_Human / InvolvedInPsychicRitual_Abhorrent / InvolvedInPsychicRitual_Social_Abhorrent |
| `developmentalStageFilter` | 14.1% (132/933) | 文本 | Adult / Baby / Baby, Child, Adult |
| `doNotApplyToQuestLodgers` | 11.4% (106/933) | 布尔 | true |
| `durationDays` | 50.9% (475/933) | 数值 | 1 / 2 / 20 |
| `effectMultiplyingStat` | 1.2% (11/933) | 文本 | PsychicSensitivity |
| `effectMultiplyingStatCurve` | 0.2% (2/933) | 容器 |  |
| `effectMultiplyingStatCurve/points` | 0.2% (2/933) | 容器 |  |
| `effectMultiplyingStatCurve/points/li` | 0.9% (8/933) | 文本 | 0, 0 / 1, 1 / 1.5, 1.5 |
| `gameCondition` | 0.3% (3/933) | 文本 | Aurora / BioluminescentSpores / UnnaturalDarkness |
| `gender` | 2.6% (24/933) | 文本 | Female / Male |
| `hediff` | 4.2% (39/933) | 文本 | FleshWhip / Inhumanized / PleasurePulse |
| `icon` | 3.9% (36/933) | 文本 | Things/Mote/Childcare/BabyCrying/BabyCryingIcon / Things/Mote/Childcare/BabyGiggling/BabyGigglingIcon / Things |
| `ignoreSubhumans` | 0.3% (3/933) | 布尔 | false |
| `invert` | 0.2% (2/933) | 布尔 | true |
| `label` | 0.1% (1/933) | 文本 | Leader of different ideoligion |
| `labelInBracketsExtraForHediff` | 0.4% (4/933) | 文本 | collapse / down / high |
| `lerpMoodToZero` | 0.1% (1/933) | 布尔 | true |
| `maxCumulatedOpinionOffset` | 0.2% (2/933) | 数值 | 10 / 36 |
| `minExpectation` | 1.0% (9/933) | 文本 | High / Low / Moderate |
| `minExpectationForNegativeThought` | 0.5% (5/933) | 文本 | Low |
| `neverNullifyIfAnyTrait` | 0.1% (1/933) | 容器 |  |
| `neverNullifyIfAnyTrait/li` | 0.1% (1/933) | 文本 | Wimp |
| `nextThought` | 0.1% (1/933) | 文本 | NewColonyHope |
| `nullifiedIfNotColonist` | 0.8% (7/933) | 布尔 | true |
| `nullifyingGenes` | 1.5% (14/933) | 容器 |  |
| `nullifyingGenes/li` | 1.9% (18/933) | 文本 | Hemogenic / ToxResist_Total / ToxicEnvironmentResistance_Total |
| `nullifyingHediffs` | 12.7% (118/933) | 容器 |  |
| `nullifyingHediffs/li` | 12.8% (119/933) | 文本 | DetoxifierLung / FleshmassLung / Inhumanized |
| `nullifyingOwnTales` | 0.2% (2/933) | 容器 |  |
| `nullifyingOwnTales/li` | 0.4% (4/933) | 文本 | AteRawHumanlikeMeat / ButcheredHumanlikeCorpse |
| `nullifyingPrecepts` | 2.1% (20/933) | 容器 |  |
| `nullifyingPrecepts/li` | 4.2% (39/933) | 文本 | Bloodfeeders_Revered / BodyMod_Approved / Cannibalism_Acceptable |
| `nullifyingTraitDegrees` | 1.4% (13/933) | 容器 |  |
| `nullifyingTraitDegrees/DrugDesire` | 2.7% (25/933) | 数值 | -1 / 1 / 2 |
| `nullifyingTraits` | 17.2% (160/933) | 容器 |  |
| `nullifyingTraits/li` | 25.0% (233/933) | 文本 | Ascetic / Disturbing / Psychopath |
| `producesMemoryThought` | 0.2% (2/933) | 文本 | AnyBodyPartButGroinCovered_Disapproved_Memory / AnyBodyPartCovered_Disapproved_Memory |
| `replaceThoughts` | 0.2% (2/933) | 容器 |  |
| `replaceThoughts/li` | 0.2% (2/933) | 文本 | AteFineMeal / AteLavishMeal |
| `requiredGenes` | 0.8% (7/933) | 容器 |  |
| `requiredGenes/li` | 0.8% (7/933) | 文本 | Mood_Depressive / Mood_Optimist / Mood_Pessimist |
| `requiredHediffs` | 0.2% (2/933) | 容器 |  |
| `requiredHediffs/li` | 0.2% (2/933) | 文本 | CubeInterest / Inhumanized |
| `requiredTraits` | 4.0% (37/933) | 容器 |  |
| `requiredTraits/li` | 4.1% (38/933) | 文本 | Bloodlust / Cannibal / Recluse |
| `requiredTraitsDegree` | 0.9% (8/933) | 数值 | -1 / -2 / 1 |
| `showBubble` | 5.7% (53/933) | 布尔 | true |
| `socialTargetDevelopmentalStageFilter` | 1.5% (14/933) | 文本 | Baby / Baby, Child, Adult / Child, Adult |
| `stackedEffectMultiplier` | 8.4% (78/933) | 数值 | 0.75 / 0.8 / 0.9 |
| `stackLimit` | 39.3% (367/933) | 数值 | 1 / 100 / 2 |
| `stackLimitForSameOtherPawn` | 13.7% (128/933) | 数值 | 1 / 10 / 3 |
| `stages` | 97.5% (910/933) | 容器 |  |
| `stages/li` | 141.6% (1321/933) | 容器 |  |
| `stages/li/baseMoodEffect` | 115.1% (1074/933) | 数值 | -12 / -2 / -4 |
| `stages/li/baseOpinionOffset` | 22.0% (205/933) | 数值 | -10 / -20 / -30 |
| `stages/li/description` | 115.8% (1080/933) | 文本 | I have touched the filthy psychic power below space. I am disgusted with myself. / I'm ashamed of my humanity. |
| `stages/li/label` | 137.0% (1278/933) | 文本 | human shame / involved in psychic ritual / no psychic rituals |
| `stages/li/labelSocial` | 0.3% (3/933) | 文本 | gave away my bonded animal / sold my loved one |
| `stages/li/visible` | 1.4% (13/933) | 布尔 | false |
| `stagesStack` | 0.1% (1/933) | 布尔 | true |
| `taleDef` | 0.9% (8/933) | 文本 | DefeatedHostileFactionLeader / HealedMe / KilledChild |
| `thoughtClass` | 44.6% (416/933) | 文本 | Thought_Memory / Thought_MemorySocial / Thought_Situational |
| `thoughtToMake` | 1.1% (10/933) | 文本 | ForcedMeToTakeDrugsMood / InsultedMood / KindWordsMood |
| `validWhileDespawned` | 18.9% (176/933) | 布尔 | true |
| `workerClass` | 35.3% (329/933) | 文本 | ThoughtWorker_Hediff / ThoughtWorker_Precept_NoPsychicRituals / ThoughtWorker_Precept_NonImhumanized |

## 四、原版 defName 一览（共 933 个，列出前 60）

```text
``                                ``                                `AnyBodyPartCovered_Disapproved_Female`  `AnyBodyPartCovered_Disapproved_Social_Female`
`AnyBodyPartButGroinCovered_Disapproved_Female`  `AnyBodyPartButGroinCovered_Disapproved_Social_Female`  `GroinUncovered_Disapproved_Female`  `GroinUncovered_Disapproved_Social_Female`
`GroinOrChestUncovered_Disapproved_Female`  `GroinOrChestUncovered_Disapproved_Social_Female`  `GroinChestOrHairUncovered_Disapproved_Female`  `GroinChestOrHairUncovered_Disapproved_Social_Female`
`GroinChestHairOrFaceUncovered_Disapproved_Female`  `GroinChestHairOrFaceUncovered_Disapproved_Social_Female`  ``                                ``                              
``                                ``                                ``                                ``                              
`WasTaught`                       `GaveLesson`                      ``                                `MyBirthMotherDied`             
`MyBirthMotherLost`               `MySonDied`                       `MyDaughterDied`                  `MyHusbandDied`                 
`MyWifeDied`                      `MyFianceDied`                    `MyFianceeDied`                   `MyLoverDied`                   
`MyBrotherDied`                   `MySisterDied`                    `MyGrandchildDied`                `MyFatherDied`                  
`MyMotherDied`                    `MyNieceDied`                     `MyNephewDied`                    `MyHalfSiblingDied`             
`MyAuntDied`                      `MyUncleDied`                     `MyGrandparentDied`               `MyCousinDied`                  
`MyKinDied`                       `MySonLost`                       `MyDaughterLost`                  `MyHusbandLost`                 
`MyWifeLost`                      `MyFianceLost`                    `MyFianceeLost`                   `MyLoverLost`                   
`MyBrotherLost`                   `MySisterLost`                    `MyGrandchildLost`                `MyFatherLost`                  
`MyMotherLost`                    `MyNieceLost`                     `MyNephewLost`                    `MyHalfSiblingLost`             
```

_余下 873 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
