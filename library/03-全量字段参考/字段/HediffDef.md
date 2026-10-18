# HediffDef

- **所属线**：人物线
- **原版实例数**：344
- **字段路径数**：475
- **资料片**：Anomaly、Biotech、Core、Ideology、Odyssey、Royalty
- **原版出处**：`Anomaly/Defs/HediffDefs/Hediffs_BodyParts_Prosthetic.xml`、`Ideology/Defs/HediffDefs/Hediffs_Casts.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<HediffDef Name="AddedMutationBase" ParentName="AddedBodyPartBase" Abstract="True">
    <organicAddedBodypart>true</organicAddedBodypart>
  </HediffDef>
  
  
```

> 来自 `Anomaly/Defs/HediffDefs/Hediffs_BodyParts_Prosthetic.xml`，defName = ``，XML 节点数 2（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
comps/li                                       [容器]
defName                                        [文本]  例：FleshWhip / FleshmassLung / FleshmassStomach
description                                    [文本]  例：A cancerous mass of semi-sentient flesh. The harsh acid it produces is painful,  / A cancerous mass of semi-sentient flesh. The tissue constantly regrows and repla / A fleshy, muscled tentacle resembling a partial transformation into a fleshbeast
label                                          [文本]  例：flesh tentacle / flesh whip / fleshmass lung
stages/li                                      [容器]
stages/li/capMods/li                           [容器]
stages/li/capMods/li/capacity                  [文本]  例：Consciousness / Manipulation / Moving
```

## 三、全量字段表（475 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `abilities` | 1.2% (4/344) | 容器 |  |
| `abilities/li` | 1.2% (4/344) | 文本 | CorrosiveSpray / GhoulFrenzy / MetalbloodInjection |
| `addedPartProps` | 12.5% (43/344) | 容器 |  |
| `addedPartProps/betterThanNatural` | 4.9% (17/344) | 布尔 | true |
| `addedPartProps/isGoodWeapon` | 0.3% (1/344) | 布尔 | true |
| `addedPartProps/partEfficiency` | 8.4% (29/344) | 数值 | 0.85 / 1.1 / 1.20 |
| `addedPartProps/solid` | 11.9% (41/344) | 布尔 | true |
| `allowedMeditationFocusTypes` | 0.3% (1/344) | 容器 |  |
| `allowedMeditationFocusTypes/li` | 0.3% (1/344) | 文本 | Void |
| `allowMothballIfLowPriorityWorldPawn` | 0.9% (3/344) | 布尔 | true |
| `alwaysShowSeverity` | 2.9% (10/344) | 布尔 | true |
| `aptitudes` | 0.3% (1/344) | 容器 |  |
| `aptitudes/Animals` | 0.3% (1/344) | 数值 | -12 |
| `aptitudes/Artistic` | 0.3% (1/344) | 数值 | -12 |
| `aptitudes/Social` | 0.3% (1/344) | 数值 | -12 |
| `battleStateLabel` | 1.5% (5/344) | 文本 | blind |
| `blocksSleeping` | 0.6% (2/344) | 布尔 | true |
| `canAffectBionicOrImplant` | 0.3% (1/344) | 布尔 | false |
| `canApplyDodChanceForCapacityChanges` | 1.5% (5/344) | 布尔 | true |
| `chanceToCauseNoPain` | 0.3% (1/344) | 数值 | 0.3 |
| `chemicalNeed` | 2.0% (7/344) | 文本 | Chemical_Alcohol / Chemical_Ambrosia / Chemical_GoJuice |
| `chronic` | 0.3% (1/344) | 布尔 | true |
| `clearsEgo` | 0.3% (1/344) | 布尔 | true |
| `comps` | 62.8% (216/344) | 容器 |  |
| `comps/li` | 100.9% (347/344) | 容器 |  |
| `comps/li/abilityDefs` | 0.9% (3/344) | 容器 |  |
| `comps/li/abilityDefs/li` | 0.9% (3/344) | 文本 | RemoteRepair / RemoteShield / VoidTerror |
| `comps/li/activatedMinimum` | 0.3% (1/344) | 数值 | 0.15 |
| `comps/li/activityMultiplier` | 0.3% (1/344) | 容器 |  |
| `comps/li/activityMultiplier/points` | 0.3% (1/344) | 容器 |  |
| `comps/li/activityMultiplier/points/li` | 0.6% (2/344) | 文本 | (0.1, 0.2) / (0.9, 1) |
| `comps/li/atSeverity` | 0.3% (1/344) | 数值 | 1 |
| `comps/li/baseTendDurationHours` | 4.4% (15/344) | 数值 | 168 / 18 / 48 |
| `comps/li/canUseDecimalsShortForm` | 0.6% (2/344) | 布尔 | true |
| `comps/li/chance` | 0.3% (1/344) | 数值 | 0.01 |
| `comps/li/chemical` | 2.0% (7/344) | 文本 | Alcohol / Ambrosia / GoJuice |
| `comps/li/compClass` | 2.0% (7/344) | 文本 | HediffComp_DisappearsAndKills_Shambler / HediffComp_DisappearsPausable_LethalInjuries / HediffComp_PregnantHum |
| `comps/li/createHediff` | 1.5% (5/344) | 文本 | BrainShock |
| `comps/li/customMote` | 0.9% (3/344) | 文本 | Mote_CombatCommandLinkLine / Mote_WorkCommandLinkLine |
| `comps/li/damageDefIncoming` | 2.3% (8/344) | 文本 | EMP |
| `comps/li/damageType` | 0.3% (1/344) | 文本 | Decayed |
| `comps/li/decayPerDayPercentageLevelCurve` | 0.3% (1/344) | 容器 |  |
| `comps/li/decayPerDayPercentageLevelCurve/points` | 0.3% (1/344) | 容器 |  |
| `comps/li/decayPerDayPercentageLevelCurve/points/li` | 0.9% (3/344) | 文本 | (12, 0.15) / (20, 0.25) / (4, 0.05) |
| `comps/li/densityStages` | 0.3% (1/344) | 容器 |  |
| `comps/li/densityStages/li` | 0.9% (3/344) | 数值 | 0.2 / 0.5 / 1 |
| `comps/li/disappearsAfterGiving` | 0.3% (1/344) | 布尔 | true |
| `comps/li/disappearsAfterTicks` | 13.4% (46/344) | 数值/文本 | 360~640 / 50 / 60000 |
| `comps/li/disappearsAfterTicks/max` | 0.3% (1/344) | 数值 | 60000 |
| `comps/li/disappearsAfterTicks/min` | 0.3% (1/344) | 数值 | 60000 |
| `comps/li/disappearsAtTotalTendQuality` | 0.6% (2/344) | 数值 | 3 |
| `comps/li/discoverLetterLabel` | 0.3% (1/344) | 文本 | Overdose: {0} |
| `comps/li/discoverLetterText` | 0.3% (1/344) | 文本 | {0} is overdosing! |
| `comps/li/endMentalStateOnCure` | 0.3% (1/344) | 布尔 | false |
| `comps/li/entropyTransferAmount` | 0.3% (1/344) | 数值 | 0.5 |
| `comps/li/exposureStatFactor` | 0.3% (1/344) | 文本 | ToxicEnvironmentResistance |
| `comps/li/fadeDurationTicks` | 0.3% (1/344) | 数值 | 60 |
| `comps/li/filth` | 0.3% (1/344) | 文本 | Filth_Slime |
| `comps/li/fleck` | 0.3% (1/344) | 文本 | AcidCloud |
| `comps/li/forced` | 0.3% (1/344) | 布尔 | true |
| `comps/li/fullChargeAmount` | 0.3% (1/344) | 数值 | 0.125 |
| `comps/li/gasType` | 0.6% (2/344) | 文本 | RotStink / ToxGas |
| `comps/li/healAmount` | 1.5% (5/344) | 数值 | 0.02 / 0.05 / 0.1 |
| `comps/li/hediff` | 1.7% (6/344) | 文本 | CombatCommandBuff / FarmingCommandBuff / MarksmanCommandBuff |
| `comps/li/hediffDef` | 0.6% (2/344) | 文本 | LungRot / Scaria |
| `comps/li/hediffs` | 2.3% (8/344) | 容器 |  |
| `comps/li/hediffs/li` | 2.9% (10/344) | 文本 | CrumbledMind / CrumblingMind / OrganDecay |
| `comps/li/hediffs/li/countRange` | 0.6% (2/344) | 文本 | 3~5 |
| `comps/li/hediffs/li/hediff` | 1.5% (5/344) | 文本 | CrumbledMind / CrumblingMind / OrganDecay |
| `comps/li/hediffs/li/partsToAffect` | 0.6% (2/344) | 容器 |  |
| `comps/li/hediffs/li/partsToAffect/li` | 1.7% (6/344) | 文本 | Heart / Kidney / Lung |
| `comps/li/hediffs/li/severityRange` | 0.6% (2/344) | 文本 | 0.02~0.15 |
| `comps/li/hidden` | 0.3% (1/344) | 布尔 | true |
| `comps/li/hideMoteWhenNotDrafted` | 1.7% (6/344) | 布尔 | true |
| `comps/li/humanMentalState` | 0.3% (1/344) | 文本 | Berserk |
| `comps/li/immunityPerDayNotSick` | 2.3% (8/344) | 数值 | -0.02 / -0.06 / -0.40 |
| `comps/li/immunityPerDaySick` | 2.3% (8/344) | 数值 | .1 / 0.2388 / 0.2614 |
| `comps/li/infectionChance` | 3.2% (11/344) | 数值 | 0.05 / 0.15 / 0.20 |
| `comps/li/initialCharge` | 0.3% (1/344) | 数值 | 0.125 |
| `comps/li/injuryCount` | 0.3% (1/344) | 文本 | 3~6 |
| `comps/li/injuryCreatedOnDeath` | 0.3% (1/344) | 文本 | ChemicalBurn |
| `comps/li/instantlyPermanentLabel` | 0.9% (3/344) | 文本 | permanent beam injury / permanent energy bolt wound / permanent gunshot injury |
| `comps/li/interval` | 0.3% (1/344) | 数值 | 60 |
| `comps/li/intervalTicks` | 0.6% (2/344) | 数值 | 60 / 60000 |
| `comps/li/labelInBrackets` | 0.3% (1/344) | 文本 | milk fullness {CHARGEFACTOR_percentage} |
| `comps/li/labelSolidTendedWell` | 5.5% (19/344) | 文本 | set / tended / treated |
| `comps/li/labelTendedWell` | 5.5% (19/344) | 文本 | bandaged / set / treated |
| `comps/li/labelTendedWellInner` | 5.5% (19/344) | 文本 | dressed / sutured / tended |
| `comps/li/letterDef` | 0.6% (2/344) | 文本 | NeutralEvent / ThreatBig |
| `comps/li/letterDesc` | 1.2% (4/344) | 文本 | {PAWN_nameDef} can no longer hide {PAWN_possessive} crippling condition. The dup / {PAWN_nameDef} can no longe |
| `comps/li/letterLabel` | 3.2% (11/344) | 文本 | Crumbling mind: {PAWN_nameDef} / Fleshmass operation / Organ decay: {PAWN_nameDef} |
| `comps/li/letterText` | 2.0% (7/344) | 文本 | Attempting to remove {PAWN_nameDef}'s flesh whip has caused the twisting mass of / Attempting to remove {PAWN_ |
| `comps/li/letterType` | 0.3% (1/344) | 文本 | HumanPregnancy |
| `comps/li/lovinMTBFactor` | 0.3% (1/344) | 数值 | 0.5 |
| `comps/li/manuallyTriggered` | 0.6% (2/344) | 布尔 | true |
| `comps/li/maxDistance` | 1.2% (4/344) | 数值 | 10 / 30 |
| `comps/li/mechanitorFactor` | 0.3% (1/344) | 数值 | 2 |
| `comps/li/message` | 1.7% (6/344) | 文本 | The unnatural corpse is moving faster! / {0_nameDef} is now suffering from duplicate sickness. / {0} is no lon |
| `comps/li/messageOnDisappear` | 0.3% (1/344) | 文本 | {PAWN_nameDef}'s genes have finished regrowing. |
| `comps/li/messageOnNonZeroSeverity` | 0.3% (1/344) | 布尔 | false |
| `comps/li/messageText` | 0.3% (1/344) | 文本 | {PAWN_labelShort}'s {1} was destroyed by organ decay. |
| `comps/li/messageType` | 1.2% (4/344) | 文本 | NeutralEvent / PositiveEvent / SilentInput |
| `comps/li/minAge` | 0.3% (1/344) | 数值 | 13 |
| `comps/li/minChargeToActivate` | 0.3% (1/344) | 数值 | 0.031 |
| `comps/li/minSeverity` | 0.6% (2/344) | 数值 | 0.5 / 1 |
| `comps/li/mote` | 1.7% (6/344) | 文本 | Mote_CombatCommand / Mote_WorkCommand |
| `comps/li/moteCount` | 0.3% (1/344) | 数值 | 6 |
| `comps/li/moteOffsetRange` | 0.3% (1/344) | 文本 | 0.25~0.75 |
| `comps/li/mtbCheckDuration` | 0.3% (1/344) | 数值 | 600 |
| `comps/li/mtbDaysToCauseMentalState` | 0.3% (1/344) | 数值 | 0.04 |
| `comps/li/mtbHours` | 0.3% (1/344) | 数值 | 4 |
| `comps/li/mtbOverRotGasExposureCurve` | 0.3% (1/344) | 容器 |  |
| `comps/li/mtbOverRotGasExposureCurve/points` | 0.3% (1/344) | 容器 |  |
| `comps/li/mtbOverRotGasExposureCurve/points/li` | 0.6% (2/344) | 文本 | (0.5, 8) / (1, 0.5) |
| `comps/li/notifyMessage` | 0.6% (2/344) | 文本 | {PAWN_labelShort}'s infant illness went from {1} to {2}. / {PAWN_labelShort}'s labor went from {1} to {2}. |
| `comps/li/onlyIfNoMechanitorDied` | 0.3% (1/344) | 布尔 | true |
| `comps/li/onlyMessageForColonistsOrPrisoners` | 0.6% (2/344) | 布尔 | true |
| `comps/li/overrideLetterDesc` | 0.3% (1/344) | 文本 | {PAWN_nameDef} can no longer control {PAWN_possessive} anger. Too many of {PAWN_ |
| `comps/li/overrideLetterLabel` | 0.3% (1/344) | 文本 | Cube rage: {PAWN_nameDef} |
| `comps/li/painDistance` | 0.3% (1/344) | 数值 | 5.9 |
| `comps/li/permanentLabel` | 6.1% (21/344) | 文本 | old energy bolt wound / permanent psychic scarring / psychic scarring |
| `comps/li/phases` | 0.3% (1/344) | 容器 |  |
| `comps/li/phases/li` | 1.2% (4/344) | 容器 |  |
| `comps/li/phases/li/descriptionExtra` | 1.2% (4/344) | 文本 | that are life threatening without exceptional medical care and glitterworld medi / that are life threatening w |
| `comps/li/phases/li/labelPrefix` | 1.2% (4/344) | 文本 | bad / common / grave |
| `comps/li/phases/li/severityPerDay` | 1.2% (4/344) | 数值 | -0.25 / 0.1 / 0.3 |
| `comps/li/pollutedSeverity` | 0.3% (1/344) | 数值 | 0.0333 |
| `comps/li/preventLetterIfPreviouslyDetected` | 0.3% (1/344) | 布尔 | true |
| `comps/li/range` | 2.0% (7/344) | 数值 | 30 / 9.9 |
| `comps/li/recoverFromDisruptedTicks` | 0.3% (1/344) | 数值 | 90 |
| `comps/li/removeOnTriggered` | 0.3% (1/344) | 布尔 | true |
| `comps/li/requiredMentalState` | 0.3% (1/344) | 文本 | BerserkTrance |
| `comps/li/requireLinkOnOtherPawn` | 1.5% (5/344) | 布尔 | false |
| `comps/li/sendLetterWhenDiscovered` | 0.6% (2/344) | 布尔 | true |
| `comps/li/severity` | 0.3% (1/344) | 数值 | 0.2 |
| `comps/li/severityGasDensityFactor` | 0.3% (1/344) | 数值 | 0.04 |
| `comps/li/severityIndices` | 0.3% (1/344) | 文本 | 3~5 |
| `comps/li/severityNotExposed` | 0.3% (1/344) | 数值 | -0.00020 |
| `comps/li/severityPerDay` | 11.6% (40/344) | 数值 | -0.1 / 0.1 / 0.33 |
| `comps/li/severityPerDayGrowing` | 0.3% (1/344) | 数值 | 0.003 |
| `comps/li/severityPerDayGrowingRandomFactor` | 0.3% (1/344) | 文本 | 0.45~1.65 |
| `comps/li/severityPerDayImmune` | 2.3% (8/344) | 数值 | -0.333 / -0.4947 / -0.70 |
| `comps/li/severityPerDayNotImmune` | 3.5% (12/344) | 数值 | -0.08 / 0.0007 / 0.003 |
| `comps/li/severityPerDayNotImmuneRandomFactor` | 0.3% (1/344) | 文本 | 0.5~3 |
| `comps/li/severityPerDayRange` | 1.7% (6/344) | 文本 | 0.0166~0.0334 / 0.05~0.1 / 0.3~0.5 |
| `comps/li/severityPerDayRemission` | 0.3% (1/344) | 数值 | -0.002 |
| `comps/li/severityPerDayRemissionRandomFactor` | 0.3% (1/344) | 文本 | 0.7~1.5 |
| `comps/li/severityPerDayTended` | 3.8% (13/344) | 数值 | -.35 / -0.0027 / -0.8 |
| `comps/li/severityPerHourEmpty` | 0.3% (1/344) | 数值 | 0.05 |
| `comps/li/severityPerHourHemogen` | 0.3% (1/344) | 数值 | -0.1 |
| `comps/li/severityPerSecondRange` | 0.6% (2/344) | 数值/文本 | 0.0111 / 0.1~0.15 |
| `comps/li/severityPerSecondUnexposed` | 0.3% (1/344) | 数值 | -0.1 |
| `comps/li/showDaysToRecover` | 2.3% (8/344) | 布尔 | true |
| `comps/li/showHoursToRecover` | 4.7% (16/344) | 布尔 | true |
| `comps/li/showRemainingTime` | 16.6% (57/344) | 布尔 | True / false / true |
| `comps/li/showTendQuality` | 0.3% (1/344) | 布尔 | false |
| `comps/li/singleWanderDurationTicks` | 0.3% (1/344) | 数值 | 180 |
| `comps/li/sound` | 0.3% (1/344) | 文本 | DeathAcidifier |
| `comps/li/stages` | 0.3% (1/344) | 文本 | 2~ |
| `comps/li/stateEffecter` | 1.7% (6/344) | 文本 | GhoulFrenzy / LaborEarly / RageSpeedState |
| `comps/li/surgicalDetectionDesc` | 1.7% (6/344) | 文本 | {PAWN_nameDef} is showing early signs of a severe condition which will cause the / {PAWN_nameDef} is showing e |
| `comps/li/targetingParameters` | 1.7% (6/344) | 容器 |  |
| `comps/li/targetingParameters/canTargetAnimals` | 1.7% (6/344) | 布尔 | false |
| `comps/li/targetingParameters/canTargetBuildings` | 1.7% (6/344) | 布尔 | false |
| `comps/li/targetingParameters/canTargetMechs` | 1.7% (6/344) | 布尔 | false |
| `comps/li/targetingParameters/onlyTargetColonists` | 1.7% (6/344) | 布尔 | true |
| `comps/li/tendAllAtOnce` | 0.3% (1/344) | 布尔 | true |
| `comps/li/tendOverlapHours` | 0.3% (1/344) | 数值 | 6 |
| `comps/li/thought` | 0.9% (3/344) | 文本 | BlissLobotomy / Catharsis / PsychicHarmonization |
| `comps/li/thoughtDefs` | 0.3% (1/344) | 容器 |  |
| `comps/li/thoughtDefs/li` | 1.2% (4/344) | 文本 | PregnancyMood_Collapse / PregnancyMood_Down / PregnancyMood_High |
| `comps/li/ticks` | 0.6% (2/344) | 数值 | 600 |
| `comps/li/ticksToFullCharge` | 0.3% (1/344) | 数值 | 15000 |
| `comps/li/ticksToRandomize` | 0.6% (2/344) | 文本 | 5000~15000 / 60000~180000 |
| `comps/li/tools` | 3.5% (12/344) | 容器 |  |
| `comps/li/tools/li` | 3.5% (12/344) | 容器 |  |
| `comps/li/tools/li/alwaysTreatAsWeapon` | 2.3% (8/344) | 布尔 | false / true |
| `comps/li/tools/li/armorPenetration` | 1.2% (4/344) | 数值 | 0.15 / 0.38 / 0.6 |
| `comps/li/tools/li/capacities` | 3.5% (12/344) | 容器 |  |
| `comps/li/tools/li/capacities/li` | 3.5% (12/344) | 文本 | Blunt / Cut / Scratch |
| `comps/li/tools/li/cooldownTime` | 3.5% (12/344) | 数值 | 1.5 / 2 / 2.6 |
| `comps/li/tools/li/label` | 3.5% (12/344) | 文本 | blade / claw / drill |
| `comps/li/tools/li/power` | 3.5% (12/344) | 数值 | 12 / 14 / 20.5 |
| `comps/li/tools/li/soundMeleeHit` | 2.6% (9/344) | 文本 | MeleeHit_BionicPunch / MeleeHit_DrillArm / MeleeHit_FieldHand |
| `comps/li/tools/li/soundMeleeMiss` | 2.6% (9/344) | 文本 | MeleeMiss_BionicPunch / MeleeMiss_DrillArm / MeleeMiss_FieldHand |
| `comps/li/unpollutedSeverity` | 0.3% (1/344) | 数值 | -0.003 |
| `comps/li/visibleToPlayer` | 0.6% (2/344) | 布尔 | false / true |
| `comps/li/vomit` | 0.9% (3/344) | 布尔 | true |
| `comps/li/wanderMtbHours` | 0.3% (1/344) | 数值 | 0.05 |
| `comps/li/wanderRadius` | 0.3% (1/344) | 数值 | 3 |
| `countsAsAddedPartOrImplant` | 0.3% (1/344) | 布尔 | true |
| `cureAllAtOnceIfCuredByItem` | 1.2% (4/344) | 布尔 | true |
| `debugLabelExtra` | 4.1% (14/344) | 文本 | accelerated / animal / creepjoiner |
| `defaultInstallPart` | 1.7% (6/344) | 文本 | Brain / Lung / Shoulder |
| `defaultLabelColor` | 14.0% (48/344) | 文本 | (0.5, 0.5, 0.5) / (0.6, 0.6, 1.0) / (0.7, 1.0, 0.7) |
| `defName` | 93.9% (323/344) | 文本 | FleshWhip / FleshmassLung / FleshmassStomach |
| `deprioritizeHealing` | 0.6% (2/344) | 布尔 | true |
| `description` | 92.7% (319/344) | 文本 | A cancerous mass of semi-sentient flesh. The harsh acid it produces is painful,  / A cancerous mass of semi-se |
| `descriptionHyperlinks` | 17.7% (61/344) | 容器 |  |
| `descriptionHyperlinks/HediffDef` | 0.9% (3/344) | 文本 | LungRot / PsychicBreakdown / PsychicShock |
| `descriptionHyperlinks/ThingDef` | 17.4% (60/344) | 文本 | ControlSublink / DetoxifierKidney / DetoxifierLung |
| `descriptionShort` | 4.1% (14/344) | 文本 | A bionic implant that allows direct control of mechanoids. Can only be removed a / An implant which allows the |
| `displayWound` | 2.0% (7/344) | 布尔 | false / true |
| `duplicationAllowed` | 4.1% (14/344) | 布尔 | false |
| `everCurableByItem` | 9.3% (32/344) | 布尔 | false |
| `extraTooltip` | 0.3% (1/344) | 文本 | Lasts until the next deathrest. |
| `forceRemoveOnResurrection` | 0.9% (3/344) | 布尔 | true |
| `forceRenderTreeRecache` | 0.6% (2/344) | 布尔 | true |
| `givesInfectionPathways` | 0.3% (1/344) | 容器 |  |
| `givesInfectionPathways/li` | 0.3% (1/344) | 文本 | RevenantHypnotized |
| `hairColorOverride` | 0.3% (1/344) | 文本 | (250, 250, 250) |
| `hediffClass` | 46.2% (159/344) | 文本 | HediffWithComps / Hediff_DeathRefusal / Hediff_DeathRefusal_CreepJoiner |
| `hediffGivers` | 1.7% (6/344) | 容器 |  |
| `hediffGivers/li` | 2.3% (8/344) | 容器 |  |
| `hediffGivers/li/countToAffect` | 0.6% (2/344) | 数值 | 1 / 2 |
| `hediffGivers/li/hediff` | 2.3% (8/344) | 文本 | Carcinoma / ChemicalDamageModerate / ChemicalDamageSevere |
| `hediffGivers/li/mtbDays` | 0.3% (1/344) | 数值 | 120 |
| `hediffGivers/li/partsToAffect` | 2.3% (8/344) | 容器 |  |
| `hediffGivers/li/partsToAffect/li` | 2.3% (8/344) | 文本 | Brain / Kidney / Liver |
| `hediffGivers/li/severityToMtbDaysCurve` | 2.0% (7/344) | 容器 |  |
| `hediffGivers/li/severityToMtbDaysCurve/points` | 2.0% (7/344) | 容器 |  |
| `hediffGivers/li/severityToMtbDaysCurve/points/li` | 6.1% (21/344) | 文本 | (0.45, 99999) / (0.5, 180) / (0.5, 60) |
| `initialSeverity` | 16.3% (56/344) | 数值 | 0 / 0.0 / 0.001 |
| `injuryProps` | 8.1% (28/344) | 容器 |  |
| `injuryProps/alwaysUseDestroyedLabel` | 1.5% (5/344) | 布尔 | true |
| `injuryProps/averagePainPerSeverityPermanent` | 6.1% (21/344) | 数值 | 0.00625 / 0.075 |
| `injuryProps/bleedRate` | 3.8% (13/344) | 数值 | 0.01 / 0.03 / 0.06 |
| `injuryProps/canMerge` | 5.5% (19/344) | 布尔 | false / true |
| `injuryProps/destroyedLabel` | 6.7% (23/344) | 文本 | Blasted off / Destroyed / Digested |
| `injuryProps/destroyedOutLabel` | 3.8% (13/344) | 文本 | Blasted out / Burned out / Burned out (chemical) |
| `injuryProps/painPerSeverity` | 5.8% (20/344) | 数值 | 0.01 / 0.0125 / 0.01875 |
| `injuryProps/useRemovedLabel` | 0.3% (1/344) | 布尔 | true |
| `inspectString` | 0.3% (1/344) | 文本 | Scaria infected. |
| `isBad` | 23.5% (81/344) | 布尔 | false / true |
| `isInfection` | 0.3% (1/344) | 布尔 | true |
| `keepOnBodyPartRestoration` | 3.5% (12/344) | 布尔 | True / true |
| `label` | 92.2% (317/344) | 文本 | flesh tentacle / flesh whip / fleshmass lung |
| `labelNoun` | 34.0% (117/344) | 文本 | a flesh tentacle / a flesh whip / a fleshmass lung |
| `labelNounPretty` | 1.5% (5/344) | 文本 | decayed {1} / digested {1} / missing a {1} |
| `lethalSeverity` | 7.0% (24/344) | 数值 | 0.0 / 1 / 1.0 |
| `levelIsQuantity` | 1.5% (5/344) | 布尔 | true |
| `makesAlert` | 0.3% (1/344) | 布尔 | false |
| `makesSickThought` | 5.8% (20/344) | 布尔 | false / true |
| `maxSeverity` | 14.2% (49/344) | 数值 | 1 / 1.0 / 3 |
| `minSeverity` | 4.1% (14/344) | 数值 | 0 / 0.001 |
| `onlyLifeThreateningTo` | 0.3% (1/344) | 容器 |  |
| `onlyLifeThreateningTo/li` | 0.3% (1/344) | 文本 | Heart |
| `organicAddedBodypart` | 0.3% (1/344) | 布尔 | true |
| `possiblePathways` | 0.3% (1/344) | 容器 |  |
| `possiblePathways/EntityAttacked` | 0.3% (1/344) | 文本 | Implanted through {SOURCEKIND_label} attack |
| `possiblePathways/PrearrivalGeneric` | 0.3% (1/344) | 文本 | Implanted before arrival at your colony |
| `possiblePathways/RevenantHypnotized` | 0.3% (1/344) | 文本 | Implanted by revenant during hypnosis |
| `pregnant` | 1.2% (4/344) | 布尔 | true |
| `preventsCrawling` | 0.9% (3/344) | 布尔 | true |
| `preventsDeath` | 0.3% (1/344) | 布尔 | true |
| `preventsLungRot` | 0.6% (2/344) | 布尔 | true |
| `preventsPregnancy` | 1.5% (5/344) | 布尔 | true |
| `priceImpact` | 3.5% (12/344) | 布尔 | false / true |
| `priceOffset` | 0.3% (1/344) | 数值 | -110 |
| `recordDownedTale` | 0.6% (2/344) | 布尔 | false |
| `removeOnDeathrestStart` | 0.3% (1/344) | 布尔 | true |
| `removeOnQuestLodgers` | 0.3% (1/344) | 布尔 | true |
| `removeOnRedressChanceByDaysCurve` | 0.9% (3/344) | 容器 |  |
| `removeOnRedressChanceByDaysCurve/points` | 0.9% (3/344) | 容器 |  |
| `removeOnRedressChanceByDaysCurve/points/li` | 3.2% (11/344) | 文本 | (0, 0) / (10, 0) / (2, 0) |
| `removeOnRedressIfNotOfKind` | 0.3% (1/344) | 容器 |  |
| `removeOnRedressIfNotOfKind/li` | 0.6% (2/344) | 文本 | Mechanitor / Mechanitor_Basic |
| `removeWithTags` | 0.3% (1/344) | 容器 |  |
| `removeWithTags/li` | 0.3% (1/344) | 文本 | ReversibleSterilized |
| `renderNodeProperties` | 2.6% (9/344) | 容器 |  |
| `renderNodeProperties/li` | 3.8% (13/344) | 容器 |  |
| `renderNodeProperties/li/anchorTag` | 0.6% (2/344) | 文本 | LeftEye / RightEye |
| `renderNodeProperties/li/baseLayer` | 2.0% (7/344) | 数值 | 20 / 60 / 65 |
| `renderNodeProperties/li/colorType` | 0.6% (2/344) | 文本 | Skin |
| `renderNodeProperties/li/debugLabel` | 2.0% (7/344) | 文本 | Ghoul plates / Ghoul spikes / Scaria sores |
| `renderNodeProperties/li/drawData` | 1.7% (6/344) | 容器 |  |
| `renderNodeProperties/li/drawData/bodyTypeScales` | 0.6% (2/344) | 容器 |  |
| `renderNodeProperties/li/drawData/bodyTypeScales/Fat` | 0.6% (2/344) | 数值 | 1.4 |
| `renderNodeProperties/li/drawData/bodyTypeScales/Hulk` | 0.6% (2/344) | 数值 | 1.2 |
| `renderNodeProperties/li/drawData/bodyTypeScales/Thin` | 0.6% (2/344) | 数值 | 0.8 |
| `renderNodeProperties/li/drawData/childScale` | 0.6% (2/344) | 数值 | 0.7 |
| `renderNodeProperties/li/drawData/dataEast` | 0.6% (2/344) | 容器 |  |
| `renderNodeProperties/li/drawData/dataEast/flip` | 0.6% (2/344) | 布尔 | true |
| `renderNodeProperties/li/drawData/dataEast/rotationOffset` | 0.6% (2/344) | 数值 | 270 |
| `renderNodeProperties/li/drawData/dataNorth` | 0.6% (2/344) | 容器 |  |
| `renderNodeProperties/li/drawData/dataNorth/flip` | 0.6% (2/344) | 布尔 | true |
| `renderNodeProperties/li/drawData/dataNorth/layer` | 0.6% (2/344) | 数值 | 0 |
| `renderNodeProperties/li/drawData/dataNorth/rotationOffset` | 0.6% (2/344) | 数值 | 310 |
| `renderNodeProperties/li/drawData/dataSouth` | 0.6% (2/344) | 容器 |  |
| `renderNodeProperties/li/drawData/dataSouth/rotationOffset` | 0.6% (2/344) | 数值 | 220 |
| `renderNodeProperties/li/drawData/dataWest` | 1.5% (5/344) | 容器 |  |
| `renderNodeProperties/li/drawData/dataWest/flip` | 0.9% (3/344) | 布尔 | false / true |
| `renderNodeProperties/li/drawData/dataWest/rotationOffset` | 0.6% (2/344) | 数值 | 270 |
| `renderNodeProperties/li/drawData/defaultData` | 1.7% (6/344) | 容器 |  |
| `renderNodeProperties/li/drawData/defaultData/flip` | 0.3% (1/344) | 布尔 | true |
| `renderNodeProperties/li/drawData/defaultData/layer` | 1.7% (6/344) | 数值 | 49 / 54 / 56 |
| `renderNodeProperties/li/drawData/defaultData/offset` | 1.2% (4/344) | 文本 | (0, 0, -0.25) |
| `renderNodeProperties/li/drawData/scaleOffsetByBodySize` | 0.6% (2/344) | 布尔 | true |
| `renderNodeProperties/li/drawData/useBodyPartAnchor` | 0.6% (2/344) | 布尔 | true |
| `renderNodeProperties/li/drawSize` | 1.7% (6/344) | 数值 | 0.15 / 0.2 / 1.3 |
| `renderNodeProperties/li/durationTicksRange` | 0.6% (2/344) | 文本 | 10~35 |
| `renderNodeProperties/li/flipGraphic` | 0.3% (1/344) | 布尔 | true |
| `renderNodeProperties/li/nextSpasmTicksRange` | 0.6% (2/344) | 文本 | 10~50 |
| `renderNodeProperties/li/nodeClass` | 0.6% (2/344) | 文本 | PawnRenderNode_AnimalPart |
| `renderNodeProperties/li/overlayLayer` | 1.2% (4/344) | 文本 | Body |
| `renderNodeProperties/li/overrideMeshSize` | 0.6% (2/344) | 数值 | 1 |
| `renderNodeProperties/li/parentTagDef` | 1.7% (6/344) | 文本 | Body / Head |
| `renderNodeProperties/li/pawnType` | 1.2% (4/344) | 文本 | HumanlikeOnly / NonHumanlikeOnly |
| `renderNodeProperties/li/rotationRange` | 0.6% (2/344) | 文本 | -30~30 |
| `renderNodeProperties/li/rotDrawMode` | 1.2% (4/344) | 文本 | Fresh, Rotting |
| `renderNodeProperties/li/side` | 0.6% (2/344) | 文本 | Left / Right |
| `renderNodeProperties/li/texPath` | 1.2% (4/344) | 文本 | Things/Pawn/Humanlike/HeadAttachments/GrayEyes/Male/GrayEyes_Male / Things/Pawn/Wounds/ArchotechEye / Things/P |
| `renderNodeProperties/li/texPathFemale` | 0.6% (2/344) | 文本 | Things/Pawn/Humanlike/HeadAttachments/GrayEyes/Female/GrayEyes_Female |
| `renderNodeProperties/li/texPaths` | 1.5% (5/344) | 容器 |  |
| `renderNodeProperties/li/texPaths/li` | 7.3% (25/344) | 文本 | Things/Pawn/Humanlike/BodyAttachments/FleshWhipLimb/FleshWhipLimbA / Things/Pawn/Humanlike/BodyAttachments/Ten |
| `renderNodeProperties/li/texSeed` | 0.9% (3/344) | 数值 | 1 / 2 |
| `renderNodeProperties/li/useRottenColor` | 0.6% (2/344) | 布尔 | true |
| `renderNodeProperties/li/useSkinShader` | 0.6% (2/344) | 布尔 | true |
| `renderNodeProperties/li/workerClass` | 2.6% (9/344) | 文本 | PawnRenderNodeWorker_AttachmentBody / PawnRenderNodeWorker_HediffEye / PawnRenderNodeWorker_OverlayScaria |
| `reportStringOverrides` | 0.3% (1/344) | 容器 |  |
| `reportStringOverrides/li` | 1.7% (6/344) | 容器 |  |
| `reportStringOverrides/li/jobDef` | 1.7% (6/344) | 文本 | Meditate / MeditatePray / Pray |
| `reportStringOverrides/li/reportString` | 1.7% (6/344) | 文本 | Asleep, dreaming about the cube. / Meditating on the cube. / Praying for the cube. |
| `scenarioCanAdd` | 6.1% (21/344) | 布尔 | false / true |
| `showGizmosOnCorpse` | 0.3% (1/344) | 布尔 | true |
| `skinColorTint` | 0.3% (1/344) | 文本 | (0.37, 0.15, 0.1) |
| `skinColorTintStrength` | 0.3% (1/344) | 数值 | 0.4 |
| `skinShader` | 0.3% (1/344) | 文本 | Metalblood |
| `spawnThingOnRemoved` | 16.9% (58/344) | 文本 | AdrenalHeart / CorrosiveHeart / DetoxifierLung |
| `stages` | 67.7% (233/344) | 容器 |  |
| `stages/li` | 124.1% (427/344) | 容器 |  |
| `stages/li/allowedMentalBreakIntensities` | 0.6% (2/344) | 容器 |  |
| `stages/li/allowedMentalBreakIntensities/li` | 0.9% (3/344) | 文本 | Major / Minor |
| `stages/li/becomeVisible` | 7.0% (24/344) | 布尔 | false / true |
| `stages/li/blocksInspirations` | 0.3% (1/344) | 布尔 | true |
| `stages/li/blocksMentalBreaks` | 0.3% (1/344) | 布尔 | true |
| `stages/li/blocksSleeping` | 0.3% (1/344) | 布尔 | true |
| `stages/li/capacityFactorEffectMultiplier` | 0.6% (2/344) | 文本 | PsychicSensitivity |
| `stages/li/capMods` | 57.0% (196/344) | 容器 |  |
| `stages/li/capMods/li` | 98.8% (340/344) | 容器 |  |
| `stages/li/capMods/li/capacity` | 98.8% (340/344) | 文本 | Consciousness / Manipulation / Moving |
| `stages/li/capMods/li/offset` | 61.6% (212/344) | 数值 | -0.05 / -0.1 / -0.15 |
| `stages/li/capMods/li/postFactor` | 22.4% (77/344) | 数值 | 0.6 / 0.75 / 0.9 |
| `stages/li/capMods/li/setMax` | 14.5% (50/344) | 数值 | 0.1 / 0.5 / 0.8 |
| `stages/li/capMods/li/setMaxCurveEvaluateStat` | 0.3% (1/344) | 文本 | PsychicSensitivity |
| `stages/li/capMods/li/setMaxCurveOverride` | 0.3% (1/344) | 容器 |  |
| `stages/li/capMods/li/setMaxCurveOverride/points` | 0.3% (1/344) | 容器 |  |
| `stages/li/capMods/li/setMaxCurveOverride/points/li` | 0.6% (2/344) | 文本 | 0, 1 / 1, 0.5 |
| `stages/li/damageFactors` | 0.3% (1/344) | 容器 |  |
| `stages/li/damageFactors/Burn` | 0.3% (1/344) | 数值 | 4 |
| `stages/li/damageFactors/Flame` | 0.3% (1/344) | 数值 | 4 |
| `stages/li/deathMtbDays` | 0.6% (2/344) | 数值 | 10 / 3.0 |
| `stages/li/destroyPart` | 0.3% (1/344) | 布尔 | true |
| `stages/li/disabledWorkTags` | 0.6% (2/344) | 容器 |  |
| `stages/li/disabledWorkTags/li` | 1.7% (6/344) | 文本 | Caring / Intellectual / ManualDumb |
| `stages/li/disablesNeeds` | 0.9% (3/344) | 容器 |  |
| `stages/li/disablesNeeds/li` | 1.5% (5/344) | 文本 | Beauty / Comfort / Outdoors |
| `stages/li/extraTooltip` | 0.6% (2/344) | 文本 | This person feels separated from their bonded individual. / This person's bonded individual is nearby. |
| `stages/li/fertilityFactor` | 0.3% (1/344) | 数值 | 0.05 |
| `stages/li/foodPoisoningChanceFactor` | 1.2% (4/344) | 数值 | 0 / 0.5 |
| `stages/li/forgetMemoryThoughtMtbDays` | 1.5% (5/344) | 数值 | 1.0 / 2 / 4 |
| `stages/li/hediffGivers` | 4.4% (15/344) | 容器 |  |
| `stages/li/hediffGivers/li` | 5.5% (19/344) | 容器 |  |
| `stages/li/hediffGivers/li/allowOnBeggars` | 1.5% (5/344) | 布尔 | false |
| `stages/li/hediffGivers/li/allowOnLodgers` | 1.5% (5/344) | 布尔 | false |
| `stages/li/hediffGivers/li/allowOnQuestReservedPawns` | 1.5% (5/344) | 布尔 | false |
| `stages/li/hediffGivers/li/allowOnQuestRewardPawns` | 1.5% (5/344) | 布尔 | false |
| `stages/li/hediffGivers/li/canAffectAnyLivePart` | 0.9% (3/344) | 布尔 | true |
| `stages/li/hediffGivers/li/hediff` | 5.5% (19/344) | 文本 | Carcinoma / ChemicalDamageModerate / Dementia |
| `stages/li/hediffGivers/li/mtbDays` | 4.1% (14/344) | 数值 | 10 / 120 / 13 |
| `stages/li/hediffGivers/li/mtbHours` | 1.2% (4/344) | 数值 | 2 |
| `stages/li/hediffGivers/li/partsToAffect` | 3.2% (11/344) | 容器 |  |
| `stages/li/hediffGivers/li/partsToAffect/li` | 3.2% (11/344) | 文本 | Brain / Heart |
| `stages/li/hediffGivers/li/severityAmount` | 1.2% (4/344) | 数值 | 2 / 4 / 6 |
| `stages/li/hungerRateFactor` | 1.2% (4/344) | 数值 | 0.1 / 0.25 / 0.75 |
| `stages/li/hungerRateFactorOffset` | 5.2% (18/344) | 数值 | 0.1 / 0.15 / 0.3 |
| `stages/li/label` | 62.2% (214/344) | 文本 | acute / impossible / lingering |
| `stages/li/lifeThreatening` | 7.0% (24/344) | 布尔 | true |
| `stages/li/makeImmuneTo` | 1.7% (6/344) | 容器 |  |
| `stages/li/makeImmuneTo/li` | 2.3% (8/344) | 文本 | GutWorms / Malaria / Plague |
| `stages/li/mentalBreakMtbDays` | 2.0% (7/344) | 数值 | 0.25 / 0.5 / 3 |
| `stages/li/mentalStateGivers` | 3.8% (13/344) | 容器 |  |
| `stages/li/mentalStateGivers/li` | 4.9% (17/344) | 容器 |  |
| `stages/li/mentalStateGivers/li/mentalState` | 4.9% (17/344) | 文本 | Berserk / Binging_DrugExtreme / Binging_DrugMajor |
| `stages/li/mentalStateGivers/li/mtbDays` | 4.9% (17/344) | 数值 | 0.4 / 10 / 40 |
| `stages/li/minSeverity` | 59.6% (205/344) | 数值 | 0 / 0.5 / 0.8 |
| `stages/li/mtbDeathDestroysBrain` | 0.3% (1/344) | 布尔 | true |
| `stages/li/multiplyStatChangesBySeverity` | 0.9% (3/344) | 布尔 | true |
| `stages/li/naturalHealingFactor` | 0.6% (2/344) | 数值 | 0 / 1.5 |
| `stages/li/opinionOfOthersFactor` | 0.6% (2/344) | 数值 | 0 |
| `stages/li/overrideLabel` | 0.9% (3/344) | 文本 | deficiency coma / psychic bond / psychic bond distance |
| `stages/li/overrideMoodBase` | 0.3% (1/344) | 数值 | 0.9 |
| `stages/li/painFactor` | 6.7% (23/344) | 数值 | 0 / 0.1 / 0.3 |
| `stages/li/painOffset` | 26.7% (92/344) | 数值 | 0.05 / 0.06 / 0.08 |
| `stages/li/partEfficiencyOffset` | 10.5% (36/344) | 数值 | -0.15 / -0.20 / -0.5 |
| `stages/li/partIgnoreMissingHP` | 0.3% (1/344) | 布尔 | true |
| `stages/li/pctAllThoughtNullification` | 0.3% (1/344) | 数值 | 1 |
| `stages/li/pctConditionalThoughtsNullified` | 0.9% (3/344) | 数值 | 0.15 / 0.33 / 0.5 |
| `stages/li/regeneration` | 1.2% (4/344) | 数值 | 100 / 30000 / 350 |
| `stages/li/showRegenerationStat` | 0.3% (1/344) | 布尔 | false |
| `stages/li/socialFightChanceFactor` | 3.2% (11/344) | 数值 | 1.5 / 2.5 / 4.0 |
| `stages/li/statFactors` | 15.7% (54/344) | 容器 |  |
| `stages/li/statFactors/Fertility` | 0.3% (1/344) | 数值 | 0 |
| `stages/li/statFactors/Flammability` | 0.6% (2/344) | 数值 | 0 |
| `stages/li/statFactors/ImmunityGainSpeed` | 0.3% (1/344) | 数值 | 2 |
| `stages/li/statFactors/IncomingDamageFactor` | 2.3% (8/344) | 数值 | 0.2 / 0.5 |
| `stages/li/statFactors/InjuryHealingFactor` | 0.3% (1/344) | 数值 | 2 |
| `stages/li/statFactors/JoyFallRateFactor` | 0.3% (1/344) | 数值 | 0.5 |
| `stages/li/statFactors/MaxNutrition` | 0.3% (1/344) | 数值 | 2 |
| `stages/li/statFactors/MeleeCooldownFactor` | 0.6% (2/344) | 数值 | 0.7 / 1.5 |
| `stages/li/statFactors/MeleeDamageFactor` | 2.0% (7/344) | 数值 | 1.1 / 1.25 / 1.375 |
| `stages/li/statFactors/MoveSpeed` | 4.7% (16/344) | 数值 | 0.5 / 0.8 / 1.2 |
| `stages/li/statFactors/PsychicEntropyGain` | 0.3% (1/344) | 数值 | 0.5 |
| `stages/li/statFactors/PsychicEntropyMax` | 1.7% (6/344) | 数值 | 1.6667 / 2.0 / 2.3334 |
| `stages/li/statFactors/PsychicEntropyRecoveryRate` | 1.7% (6/344) | 数值 | 1.25 / 1.375 / 1.5 |
| `stages/li/statFactors/PsychicSensitivity` | 1.5% (5/344) | 数值 | 0 / 1.25 / 2 |
| `stages/li/statFactors/RestFallRateFactor` | 2.9% (10/344) | 数值 | 0 / 0.15 / 0.6 |
| `stages/li/statFactors/StaggerDurationFactor` | 0.3% (1/344) | 数值 | 0 |
| `stages/li/statFactors/StudyEfficiency` | 0.6% (2/344) | 数值 | 1.25 / 2 |
| `stages/li/statFactors/WorkSpeedGlobal` | 1.5% (5/344) | 数值 | 0.8 / 0.9 / 1.5 |
| `stages/li/statOffsetEffectMultiplier` | 0.3% (1/344) | 文本 | PsychicSensitivity |
| `stages/li/statOffsets` | 30.5% (105/344) | 容器 |  |
| `stages/li/statOffsets/AimingDelayFactor` | 0.3% (1/344) | 数值 | -0.4 |
| `stages/li/statOffsets/ArmorRating_Blunt` | 0.9% (3/344) | 数值 | 0.1 / 0.2 / 0.3 |
| `stages/li/statOffsets/ArmorRating_Heat` | 0.9% (3/344) | 数值 | 0.3 / 0.4 / 0.5 |
| `stages/li/statOffsets/ArmorRating_Sharp` | 0.9% (3/344) | 数值 | 0.35 / 0.52 / 0.70 |
| `stages/li/statOffsets/ComfyTemperatureMax` | 0.6% (2/344) | 数值 | 30 / 40 |
| `stages/li/statOffsets/ComfyTemperatureMin` | 1.2% (4/344) | 数值 | -16 / -26 / -40 |
| `stages/li/statOffsets/ConstructionSpeed` | 0.3% (1/344) | 数值 | 0.4 |
| `stages/li/statOffsets/CookSpeed` | 0.3% (1/344) | 数值 | 5 |
| `stages/li/statOffsets/DeepDrillingSpeed` | 0.3% (1/344) | 数值 | 0.7 |
| `stages/li/statOffsets/GeneralLaborSpeed` | 0.3% (1/344) | 数值 | 0.2 |
| `stages/li/statOffsets/GlobalLearningFactor` | 0.9% (3/344) | 数值 | -0.5 / 0.2 / 0.25 |
| `stages/li/statOffsets/HemogenGainFactor` | 0.3% (1/344) | 数值 | 0.25 |
| `stages/li/statOffsets/ImmunityGainSpeed` | 0.6% (2/344) | 数值 | 0.08 / 0.25 |
| `stages/li/statOffsets/InjuryHealingFactor` | 0.3% (1/344) | 数值 | 0.25 |
| `stages/li/statOffsets/MechBandwidth` | 0.3% (1/344) | 数值 | 6 |
| `stages/li/statOffsets/MechControlGroups` | 2.0% (7/344) | 数值 | 2 / 4 / 5 |
| `stages/li/statOffsets/MechFormingSpeed` | 1.7% (6/344) | 数值 | 1 / 1.33 / 1.66 |
| `stages/li/statOffsets/MechRemoteRepairDistance` | 0.9% (3/344) | 数值 | 13.9 / 19.9 / 7.9 |
| `stages/li/statOffsets/MechRemoteShieldDistance` | 0.9% (3/344) | 数值 | 13.9 / 19.9 / 7.9 |
| `stages/li/statOffsets/MechRemoteShieldEnergy` | 0.9% (3/344) | 数值 | 150 / 225 / 75 |
| `stages/li/statOffsets/MechRepairSpeed` | 1.7% (6/344) | 数值 | 1 / 1.33 / 1.66 |
| `stages/li/statOffsets/MeditationFocusGain` | 0.6% (2/344) | 数值 | 0.05 / 0.2 |
| `stages/li/statOffsets/MeleeCooldownFactor` | 0.9% (3/344) | 数值 | 1.25 / 1.5 / 2 |
| `stages/li/statOffsets/MeleeDodgeChance` | 0.3% (1/344) | 数值 | 8 |
| `stages/li/statOffsets/MeleeHitChance` | 0.6% (2/344) | 数值 | 3 / 8 |
| `stages/li/statOffsets/MentalBreakThreshold` | 2.3% (8/344) | 数值 | 0.02 / 0.04 / 0.08 |
| `stages/li/statOffsets/MinimumContainmentStrength` | 0.6% (2/344) | 数值 | 25 / 35 |
| `stages/li/statOffsets/MiningSpeed` | 0.6% (2/344) | 数值 | 0.4 / 1.60 |
| `stages/li/statOffsets/MoveSpeed` | 2.3% (8/344) | 数值 | -0.2 / -0.25 / -0.7 |
| `stages/li/statOffsets/NegotiationAbility` | 0.3% (1/344) | 数值 | 0.50 |
| `stages/li/statOffsets/PainShockThreshold` | 0.3% (1/344) | 数值 | 10 |
| `stages/li/statOffsets/PawnBeauty` | 1.7% (6/344) | 数值 | -1 / -2 / 1 |
| `stages/li/statOffsets/PilotingAbility` | 0.3% (1/344) | 数值 | 0.45 |
| `stages/li/statOffsets/PlantWorkSpeed` | 0.6% (2/344) | 数值 | 0.4 / 1.60 |
| `stages/li/statOffsets/PsychicEntropyRecoveryRate` | 0.6% (2/344) | 数值 | 0.05 / 0.15 |
| `stages/li/statOffsets/PsychicSensitivity` | 1.7% (6/344) | 数值 | -1 / 0.05 / 0.1 |
| `stages/li/statOffsets/ResearchSpeed` | 0.6% (2/344) | 数值 | 0.2 / 0.3 |
| `stages/li/statOffsets/RestFallRateFactor` | 4.1% (14/344) | 数值 | -0.9 / 0.3 / 0.7 |
| `stages/li/statOffsets/ShootingAccuracyPawn` | 0.6% (2/344) | 数值 | 3 / 4 |
| `stages/li/statOffsets/ToxicEnvironmentResistance` | 0.6% (2/344) | 数值 | 0.3 / 0.6 |
| `stages/li/statOffsets/ToxicResistance` | 0.6% (2/344) | 数值 | 0.5 / 1 |
| `stages/li/statOffsets/TradePriceImprovement` | 0.3% (1/344) | 数值 | 0.10 |
| `stages/li/statOffsets/Wildness` | 0.3% (1/344) | 数值 | -0.25 |
| `stages/li/statOffsets/WorkSpeedGlobal` | 2.3% (8/344) | 数值 | -0.5 / 0.2 / 0.3 |
| `stages/li/statOffsets/WorkSpeedGlobalOffsetMech` | 1.7% (6/344) | 数值 | 0.18 / 0.24 / 0.30 |
| `stages/li/tale` | 0.3% (1/344) | 文本 | Drunk |
| `stages/li/totalBleedFactor` | 0.3% (1/344) | 数值 | 0.5 |
| `stages/li/vomitMtbDays` | 10.8% (37/344) | 数值 | 0.075 / 0.5 / 0.75 |
| `tags` | 2.3% (8/344) | 容器 |  |
| `tags/li` | 2.3% (8/344) | 文本 | ArmorGland / OvumExtracted / ReversibleSterilized |
| `taleOnVisible` | 1.2% (4/344) | 文本 | HeatstrokeRevealed / HypothermiaRevealed / ToxicityRevealed |
| `targetPrefix` | 0.3% (1/344) | 文本 | for |
| `tendable` | 6.7% (23/344) | 布尔 | false / true |

## 四、原版 defName 一览（共 344 个，列出前 60）

```text
``                                ``                                ``                                ``                              
`DeathRefusalCreepJoiner`         ``                                `BandNode`                        `PsychicBondTorn`               
`OrganDecay`                      ``                                `DeathRefusal`                    `OrganDecayCreepjoiner`         
`Stillborn`                       `Vasectomy`                       `ImplantedIUD`                    `TubalLigation`                 
`SelfShutdown`                    ``                                ``                                ``                              
`ChemicalDamageModerate`          `RevenantVertebrae`               `DEV_Unburnable`                  `Blindness`                     
`HearingLoss`                     `ChemicalDamageSevere`            `LoveEnhancer`                    `PsychicAnesthesia`             
`Joyfuzz`                         `DarknessExposure`                `AmbrosiaTolerance`               `Denture`                       
`Cataract`                        `ResearchCommandBuff`             `FarmingCommandBuff`              `MiningCommandBuff`             
`PsilocapTolerance`               `PsychicLove`                     `NoPain`                          `HungerMaker`                   
`CorrosiveHeart`                  ``                                `PsychicallyDead`                 `VatGrowing`                    
``                                `PegLeg`                          `WoodenHand`                      `WoodenFoot`                    
`CochlearImplant`                 ``                                `MarksmanCommandBuff`             `ProductionCommandBuff`         
`NeuralHeatRecoveryGain`          `AwokenHypnosis`                  `Digested`                        `HemogenAmplified`              
`GlucosoidRush`                   `BionicSpine`                     `BionicTongue`                    `SimpleProstheticLeg`           
```

_余下 284 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
