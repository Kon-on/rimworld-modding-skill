# AbilityDef

- **所属线**：人物线
- **原版实例数**：107
- **字段路径数**：260
- **资料片**：Anomaly、Biotech、Core、Ideology、Odyssey、Royalty
- **原版出处**：`Royalty/Defs/AbilityDefs/Abilities.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<AbilityDef Name="PsycastBaseSkip" ParentName="PsycastBase" Abstract="True">
    <category>Skip</category>
  </AbilityDef>
  
  
```

> 来自 `Royalty/Defs/AbilityDefs/Abilities.xml`，defName = ``，XML 节点数 2（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
comps/li                                       [容器]
defName                                        [文本]  例：ConsumeLeap_Devourer / SpikeLaunch_Fingerspike / SpikeLaunch_Toughspike
label                                          [文本]  例：consume leap / entity skip / spike launch
```

## 三、全量字段表（260 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `abilityClass` | 0.9% (1/107) | 文本 | Psycast |
| `ai_IsIncendiary` | 3.7% (4/107) | 布尔 | true |
| `ai_IsOffensive` | 2.8% (3/107) | 布尔 | true |
| `ai_SearchAOEForTargets` | 1.9% (2/107) | 布尔 | true |
| `aiCanUse` | 18.7% (20/107) | 布尔 | true |
| `canUseAoeToGetTargets` | 10.3% (11/107) | 布尔 | False / false / true |
| `casterMustBeCapableOfViolence` | 58.9% (63/107) | 布尔 | false |
| `category` | 9.3% (10/107) | 文本 | Psychic / Sanguophage / Skip |
| `charges` | 3.7% (4/107) | 数值 | 2 / 3 / 5 |
| `comps` | 86.9% (93/107) | 容器 |  |
| `comps/li` | 143.0% (153/107) | 容器 |  |
| `comps/li/allowedForChild` | 1.9% (2/107) | 布尔 | false |
| `comps/li/allowOnBuildings` | 0.9% (1/107) | 布尔 | False |
| `comps/li/applicableToMechs` | 3.7% (4/107) | 布尔 | False |
| `comps/li/appliedEffecterDef` | 0.9% (1/107) | 文本 | MechResurrected |
| `comps/li/applyGoodwillImpactToLodgers` | 4.7% (5/107) | 布尔 | False |
| `comps/li/barrelOffsetDistance` | 1.9% (2/107) | 数值 | 6 |
| `comps/li/baseCertaintyGain` | 0.9% (1/107) | 数值 | 0.2 |
| `comps/li/bloodFilthToSpawnRange` | 0.9% (1/107) | 数值 | 1 |
| `comps/li/canApplyToAsleep` | 0.9% (1/107) | 布尔 | true |
| `comps/li/canApplyToMentallyBroken` | 0.9% (1/107) | 布尔 | True |
| `comps/li/canApplyToUnconscious` | 1.9% (2/107) | 布尔 | true |
| `comps/li/canHitFilledCells` | 2.8% (3/107) | 布尔 | true |
| `comps/li/canTargetBaby` | 1.9% (2/107) | 布尔 | False |
| `comps/li/canTargetBosses` | 1.9% (2/107) | 布尔 | false |
| `comps/li/capacity` | 2.8% (3/107) | 文本 | Eating / Manipulation / Talking |
| `comps/li/casterEffect` | 0.9% (1/107) | 文本 | AnimalWarcall_Cast |
| `comps/li/cellsToFill` | 0.9% (1/107) | 数值 | 15 |
| `comps/li/chanceFromHearingCurve` | 1.9% (2/107) | 容器 |  |
| `comps/li/chanceFromHearingCurve/points` | 1.9% (2/107) | 容器 |  |
| `comps/li/chanceFromHearingCurve/points/li` | 3.7% (4/107) | 文本 | (0.0, 0.0) / (0.8, 1.0) / (1.0, 0.75) |
| `comps/li/chunkCount` | 0.9% (1/107) | 数值 | 5 |
| `comps/li/clamorRadius` | 10.3% (11/107) | 数值 | 10 / 15 / 25 |
| `comps/li/clamorType` | 10.3% (11/107) | 文本 | Ability |
| `comps/li/compClass` | 39.2% (42/107) | 文本 | CompAbilityEffect_GiveHediff / CompAbilityEffect_GiveHediffPsychic / CompAbilityEffect_GiveMentalState |
| `comps/li/coneSizeDegrees` | 1.9% (2/107) | 数值 | 12 / 7.2 |
| `comps/li/convertPowerFactor` | 0.9% (1/107) | 数值 | 2 |
| `comps/li/costs` | 0.9% (1/107) | 容器 |  |
| `comps/li/costs/li` | 2.8% (3/107) | 容器 |  |
| `comps/li/costs/li/cost` | 2.8% (3/107) | 数值 | 1 / 3 / 5 |
| `comps/li/costs/li/weightClass` | 2.8% (3/107) | 文本 | Heavy / Light / Medium |
| `comps/li/damageDef` | 0.9% (1/107) | 文本 | EMP |
| `comps/li/damAmount` | 1.9% (2/107) | 数值 | 12 / 16 |
| `comps/li/destClamorRadius` | 2.8% (3/107) | 数值 | 10 |
| `comps/li/destClamorType` | 2.8% (3/107) | 文本 | Ability |
| `comps/li/destination` | 5.6% (6/107) | 文本 | Caster / RandomInRange / Selected |
| `comps/li/durationMultiplier` | 9.3% (10/107) | 文本 | PsychicSensitivity |
| `comps/li/durationSecondsOverride` | 2.8% (3/107) | 文本 | 2000~4000 / 20~30 |
| `comps/li/effecterDef` | 10.3% (11/107) | 文本 | AgonyPulseExplosion / BurnerUsed / Fire_Spew |
| `comps/li/elementRatios` | 0.9% (1/107) | 容器 |  |
| `comps/li/elementRatios/li` | 1.9% (2/107) | 容器 |  |
| `comps/li/elementRatios/li/ratio` | 1.9% (2/107) | 数值 | 1 / 15 |
| `comps/li/elementRatios/li/sourceStuff` | 1.9% (2/107) | 文本 | ChunkSlagSteel / Steel |
| `comps/li/exceptions` | 0.9% (1/107) | 容器 |  |
| `comps/li/exceptions/li` | 0.9% (1/107) | 文本 | Jailbreaker |
| `comps/li/excludeNPCFactions` | 0.9% (1/107) | 布尔 | true |
| `comps/li/explosionRadius` | 0.9% (1/107) | 数值 | 4.9 |
| `comps/li/failedMessage` | 0.9% (1/107) | 文本 | Must target steel, steel slag chunks, steel buildings, or steel items. |
| `comps/li/failedThoughtInitiator` | 0.9% (1/107) | 文本 | FailedConvertAbilityInitiator |
| `comps/li/failedThoughtRecipient` | 1.9% (2/107) | 文本 | CounselFailed / FailedConvertAbilityRecipient |
| `comps/li/failMessage` | 1.9% (2/107) | 文本 | {INITIATOR_labelShort} botched the attempt to counsel {RECIPIENT_labelShort}. {R / {INITIATOR_labelShort} fail |
| `comps/li/filthDef` | 2.8% (3/107) | 文本 | Filth_Ash / Filth_FlammableBile |
| `comps/li/firefoamRadius` | 0.9% (1/107) | 数值 | 3.5 |
| `comps/li/fleckDef` | 19.6% (21/107) | 文本 | BloodSplash / PsycastPsychicEffect / PsycastPsychicLine |
| `comps/li/fleckDefs` | 3.7% (4/107) | 容器 |  |
| `comps/li/fleckDefs/li` | 7.5% (8/107) | 文本 | PsycastSkipInnerExit / PsycastSkipOuterRingExit |
| `comps/li/forced` | 0.9% (1/107) | 布尔 | true |
| `comps/li/gasType` | 0.9% (1/107) | 文本 | DeadlifeDust |
| `comps/li/goodwillImpact` | 14.0% (15/107) | 数值 | -15 / -25 / -5 |
| `comps/li/goodwillImpactForBerserk` | 0.9% (1/107) | 数值 | -75 |
| `comps/li/goodwillImpactForNeuroquake` | 0.9% (1/107) | 数值 | -10 |
| `comps/li/hediffDef` | 24.3% (26/107) | 文本 | AgonyPulse / GhoulFrenzy / Metalblood |
| `comps/li/hemogenCost` | 3.7% (4/107) | 数值 | 0.05 / 0.2 / 0.90 |
| `comps/li/hemogenGain` | 0.9% (1/107) | 数值 | 0.2 |
| `comps/li/ignoreSelf` | 0.9% (1/107) | 布尔 | true |
| `comps/li/interactionDef` | 6.5% (7/107) | 文本 | PreachHealth / WordOfJoy / WordOfTrust |
| `comps/li/jobDef` | 0.9% (1/107) | 文本 | GotoMindControlled |
| `comps/li/lifespanNoise` | 1.9% (2/107) | 数值 | 40 |
| `comps/li/lineWidthEnd` | 2.8% (3/107) | 数值 | 3 / 5 |
| `comps/li/maintainForTicks` | 3.7% (4/107) | 数值 | 60 |
| `comps/li/maintainTicks` | 1.9% (2/107) | 数值 | 20 |
| `comps/li/maxBodySize` | 1.9% (2/107) | 数值 | 10 / 2.5 |
| `comps/li/maxCorpseAgeTicks` | 0.9% (1/107) | 数值 | 3600 |
| `comps/li/mentalStateRadius` | 0.9% (1/107) | 数值 | 60 |
| `comps/li/moteDef` | 1.9% (2/107) | 文本 | Mote_IncineratorBurst |
| `comps/li/numCellsToHit` | 4.7% (5/107) | 数值 | 18 / 9 |
| `comps/li/numPods` | 0.9% (1/107) | 文本 | 2~3 |
| `comps/li/numStreams` | 1.9% (2/107) | 数值 | 15 |
| `comps/li/offset` | 0.9% (1/107) | 数值 | -12 |
| `comps/li/onlyApplyToSelf` | 9.3% (10/107) | 布尔 | True |
| `comps/li/onlyBrain` | 11.2% (12/107) | 布尔 | True / true |
| `comps/li/opinionThoughtDefToGiveTarget` | 0.9% (1/107) | 文本 | FedOn_Social |
| `comps/li/outcomeItems` | 0.9% (1/107) | 容器 |  |
| `comps/li/outcomeItems/li` | 4.7% (5/107) | 文本 | Bioferrite / Gold / Plasteel |
| `comps/li/outcomeStuff` | 0.9% (1/107) | 容器 |  |
| `comps/li/outcomeStuff/li` | 3.7% (4/107) | 文本 | Bioferrite / Gold / Plasteel |
| `comps/li/pattern` | 0.9% (1/107) | 容器 |  |
| `comps/li/pattern/li` | 4.7% (5/107) | 文本 | (-1, 0) / (0, 0) / (0, 1) |
| `comps/li/points` | 0.9% (1/107) | 文本 | 750~1250 |
| `comps/li/preCastTicks` | 3.7% (4/107) | 数值 | 5 |
| `comps/li/projectileDef` | 10.3% (11/107) | 文本 | PiercingSpine / Proj_Acid / Proj_CorrosiveFluid |
| `comps/li/psychic` | 15.9% (17/107) | 布尔 | False / True |
| `comps/li/psyfocusCostForExtreme` | 0.9% (1/107) | 数值 | 0.7 |
| `comps/li/psyfocusCostForMajor` | 0.9% (1/107) | 数值 | 0.5 |
| `comps/li/psyfocusCostForMinor` | 0.9% (1/107) | 数值 | 0.3 |
| `comps/li/radius` | 0.9% (1/107) | 数值 | 5.9 |
| `comps/li/randomRange` | 1.9% (2/107) | 文本 | 6.9~24.9 |
| `comps/li/range` | 6.5% (7/107) | 数值 | -1 / 11 / 13 |
| `comps/li/rangeNoise` | 1.9% (2/107) | 数值 | .4 |
| `comps/li/replaceExisting` | 11.2% (12/107) | 布尔 | true |
| `comps/li/requiresLineOfSight` | 2.8% (3/107) | 布尔 | True / false |
| `comps/li/resistanceGain` | 0.9% (1/107) | 数值 | 1 |
| `comps/li/ritualDef` | 3.7% (4/107) | 文本 | Conversion / LeaderSpeech / ThroneSpeech |
| `comps/li/ritualDefForMentalState` | 0.9% (1/107) | 文本 | TrialMentalState |
| `comps/li/ritualDefForPrisoner` | 0.9% (1/107) | 文本 | TrialPrisoner |
| `comps/li/scale` | 3.7% (4/107) | 数值 | 0.42 / 1.55 |
| `comps/li/scatterRadius` | 0.9% (1/107) | 数值 | 2.9 |
| `comps/li/screenShakeIntensity` | 2.8% (3/107) | 数值 | 0.5 / 1.0 / 2 |
| `comps/li/severity` | 0.9% (1/107) | 数值 | 0 |
| `comps/li/sizeReductionDistanceThreshold` | 1.9% (2/107) | 数值 | 8 |
| `comps/li/smokeRadius` | 1.9% (2/107) | 数值 | 3.5 |
| `comps/li/sound` | 12.2% (13/107) | 文本 | MoralistAbility_Resolve / PreachHealth_Resolve / PsycastWallraise |
| `comps/li/soundFemale` | 0.9% (1/107) | 文本 | BerserkTrance_Resolve_Female |
| `comps/li/soundMale` | 0.9% (1/107) | 文本 | BerserkTrance_Resolve_Male |
| `comps/li/sprayEffecter` | 4.7% (5/107) | 文本 | AcidSpray_Directional / FoamSpray_Directional |
| `comps/li/stateDef` | 6.5% (7/107) | 文本 | BerserkTrance / BerserkWarcall / TerrifyingHallucinations |
| `comps/li/stateDefForMechs` | 1.9% (2/107) | 文本 | BerserkMechanoid |
| `comps/li/stunTicks` | 3.7% (4/107) | 文本 | 18~60 / 70~120 |
| `comps/li/successMessage` | 3.7% (4/107) | 文本 | {INITIATOR_labelShort} has converted {RECIPIENT_labelShort} to {IDEO}. / {INITIATOR_labelShort} has reassured  |
| `comps/li/successMessageNoNegativeThought` | 0.9% (1/107) | 文本 | {INITIATOR_labelShort} successfully counselled {RECIPIENT_labelShort}, increasin |
| `comps/li/targetEffect` | 0.9% (1/107) | 文本 | AnimalWarcall_CastOnTarget |
| `comps/li/targetReceivesEntropy` | 0.9% (1/107) | 布尔 | False |
| `comps/li/targetRoleId` | 1.9% (2/107) | 文本 | convertee / convict |
| `comps/li/tendQualityRange` | 0.9% (1/107) | 文本 | 0.4~0.8 |
| `comps/li/thingDef` | 1.9% (2/107) | 文本 | BulletShieldPsychic / SolarPinhole |
| `comps/li/thoughtDefToGiveTarget` | 0.9% (1/107) | 文本 | FedOn |
| `comps/li/workTags` | 3.7% (4/107) | 容器 |  |
| `comps/li/workTags/li` | 3.7% (4/107) | 文本 | Social |
| `comps/li/worldRangeTiles` | 0.9% (1/107) | 数值 | 4 |
| `confirmationDialogText` | 0.9% (1/107) | 文本 | If you use neuroquake, everyone in this region will feel the neuroquake echo, yo |
| `cooldownPerCharge` | 1.9% (2/107) | 布尔 | true |
| `cooldownTicksRange` | 39.2% (42/107) | 数值/文本 | 120 / 130 / 180~480 |
| `defName` | 92.5% (99/107) | 文本 | ConsumeLeap_Devourer / SpikeLaunch_Fingerspike / SpikeLaunch_Toughspike |
| `description` | 89.7% (96/107) | 文本 | Launch a bone spike at a target. / Launch a keratin spine at a target to do damage. / Leap onto a target and b |
| `disableGizmoWhileUndrafted` | 25.2% (27/107) | 布尔 | False / false / true |
| `displayGizmoWhileUndrafted` | 25.2% (27/107) | 布尔 | True / false / true |
| `displayOrder` | 13.1% (14/107) | 数值 | 100 / 300 / 400 |
| `emissionInterval` | 0.9% (1/107) | 数值 | 60 |
| `emittedFleck` | 0.9% (1/107) | 文本 | PreachHealth |
| `gizmoClass` | 2.8% (3/107) | 文本 | Command_Ability / Command_AbilitySpeech / Command_AbilityTrial |
| `groupAbility` | 2.8% (3/107) | 布尔 | true |
| `groupDef` | 11.2% (12/107) | 文本 | Leader / Moralist / MultiRole |
| `hasExternallyHandledCooldown` | 0.9% (1/107) | 布尔 | true |
| `hostile` | 29.9% (32/107) | 布尔 | false |
| `hotKey` | 40.2% (43/107) | 文本 | Misc1 / Misc12 / Misc3 |
| `iconPath` | 82.2% (88/107) | 文本 | UI/Abilities/ShapeFlesh / UI/Abilities/Slaughter / UI/Abilities/TransmuteSteel |
| `jobDef` | 19.6% (21/107) | 文本 | CastAbilityOnThingMelee / CastAbilityOnThingWithoutWeapon / CastAbilityOnThingWithoutWeaponInterruptible |
| `label` | 90.6% (97/107) | 文本 | consume leap / entity skip / spike launch |
| `level` | 27.1% (29/107) | 数值 | 1 / 2 / 3 |
| `moteOffsetAmountTowardsTarget` | 4.7% (5/107) | 数值 | 0.5 |
| `overrideGroupCooldown` | 1.9% (2/107) | 布尔 | True |
| `requiredMemes` | 0.9% (1/107) | 容器 |  |
| `requiredMemes/li` | 0.9% (1/107) | 文本 | Proselytizer |
| `sendMessageOnCooldownComplete` | 14.0% (15/107) | 布尔 | true |
| `showCastingProgressBar` | 1.9% (2/107) | 布尔 | True / true |
| `showGizmoOnWorldView` | 0.9% (1/107) | 布尔 | True |
| `showOnCharacterCard` | 1.9% (2/107) | 布尔 | false |
| `showPsycastEffects` | 21.5% (23/107) | 布尔 | False / false |
| `showWhenDrafted` | 11.2% (12/107) | 布尔 | false |
| `statBases` | 42.1% (45/107) | 容器 |  |
| `statBases/Ability_Duration` | 28.0% (30/107) | 数值 | 0 / 15 / 40 |
| `statBases/Ability_EffectRadius` | 17.8% (19/107) | 数值 | 0 / 2.9 / 5 |
| `statBases/Ability_EntropyGain` | 19.6% (21/107) | 数值 | 0 / 12 / 20 |
| `statBases/Ability_PsyfocusCost` | 26.2% (28/107) | 数值 | 0.01 / 0.02 / 0.03 |
| `stunTargetWhileCasting` | 16.8% (18/107) | 布尔 | True / true |
| `targetRequired` | 16.8% (18/107) | 布尔 | False / True / false |
| `targetWorldCell` | 0.9% (1/107) | 布尔 | True |
| `uiOrder` | 8.4% (9/107) | 数值 | 1 / 2 / 3 |
| `useAverageTargetPositionForWarmupEffecter` | 1.9% (2/107) | 布尔 | true |
| `verbProperties` | 88.8% (95/107) | 容器 |  |
| `verbProperties/accuracyLong` | 1.9% (2/107) | 数值 | 0.6 |
| `verbProperties/accuracyMedium` | 1.9% (2/107) | 数值 | 0.7 |
| `verbProperties/accuracyShort` | 1.9% (2/107) | 数值 | 0.8 |
| `verbProperties/accuracyTouch` | 1.9% (2/107) | 数值 | 0.9 |
| `verbProperties/ai_IsBuildingDestroyer` | 0.9% (1/107) | 布尔 | true |
| `verbProperties/ai_IsWeapon` | 4.7% (5/107) | 布尔 | false |
| `verbProperties/ai_ProjectileLaunchingIgnoresMeleeThreats` | 1.9% (2/107) | 布尔 | true |
| `verbProperties/aimingChargeMote` | 0.9% (1/107) | 文本 | Mote_FleshmelterBolt_Charge |
| `verbProperties/aimingChargeMoteOffset` | 0.9% (1/107) | 数值 | 1.07 |
| `verbProperties/aimingLineMote` | 0.9% (1/107) | 文本 | Mote_FleshmelterBolt_Aim |
| `verbProperties/aimingLineMoteFixedLength` | 0.9% (1/107) | 数值 | 15.9 |
| `verbProperties/aimingTargetMote` | 0.9% (1/107) | 文本 | Mote_FleshmelterBolt_Target |
| `verbProperties/beamTargetsGround` | 0.9% (1/107) | 布尔 | true |
| `verbProperties/burstShotCount` | 1.9% (2/107) | 数值 | 1 / 12 |
| `verbProperties/defaultProjectile` | 5.6% (6/107) | 文本 | Bullet_Heatspike / Spike_Fingerspike / Spike_Toughspike |
| `verbProperties/drawAimPie` | 29.9% (32/107) | 布尔 | False / false / true |
| `verbProperties/drawHighlightWithLineOfSight` | 1.9% (2/107) | 布尔 | true |
| `verbProperties/flammabilityAttachFireChanceCurve` | 1.9% (2/107) | 容器 |  |
| `verbProperties/flammabilityAttachFireChanceCurve/points` | 1.9% (2/107) | 容器 |  |
| `verbProperties/flammabilityAttachFireChanceCurve/points/li` | 3.7% (4/107) | 文本 | (0.2, 0) / (1, 1) |
| `verbProperties/flightEffecterDef` | 0.9% (1/107) | 文本 | JumpMechFlightEffect |
| `verbProperties/flyWithCarriedThing` | 1.9% (2/107) | 布尔 | false / true |
| `verbProperties/forcedMissRadius` | 2.8% (3/107) | 数值 | 1.9 |
| `verbProperties/forceNormalTimeSpeed` | 1.9% (2/107) | 布尔 | false |
| `verbProperties/label` | 4.7% (5/107) | 文本 | consume leap / jump / release deadlife dust |
| `verbProperties/minRange` | 1.9% (2/107) | 数值 | 5.9 / 6 |
| `verbProperties/mouseTargetingText` | 0.9% (1/107) | 文本 | Choose an animal to call |
| `verbProperties/muzzleFlashScale` | 1.9% (2/107) | 数值 | 9 |
| `verbProperties/nonInterruptingSelfCast` | 2.8% (3/107) | 布尔 | true |
| `verbProperties/onlyManualCast` | 0.9% (1/107) | 布尔 | True |
| `verbProperties/range` | 77.6% (83/107) | 数值 | 17.9 / 3.9 / 5.9 |
| `verbProperties/rangedFireRulepack` | 0.9% (1/107) | 文本 | Combat_RangedFire_Thrown |
| `verbProperties/rangeStat` | 1.9% (2/107) | 文本 | MechRemoteRepairDistance / MechRemoteShieldDistance |
| `verbProperties/requireLineOfSight` | 22.4% (24/107) | 布尔 | False / True / false |
| `verbProperties/soundAiming` | 0.9% (1/107) | 文本 | FleshmelterBolt_Charging |
| `verbProperties/soundCast` | 29.0% (31/107) | 容器/文本 | Ability_SpineLaunch / Gorehulk_Spine_Launch / Heatspikes_Shot |
| `verbProperties/soundCastTail` | 3.7% (4/107) | 文本 | GunTail_Medium / Heatspikes_Tail |
| `verbProperties/soundLanding` | 3.7% (4/107) | 文本 | JumpMechLand / Longjump_Land / Pawn_Devourer_Land |
| `verbProperties/stunTargetOnCastStart` | 0.9% (1/107) | 布尔 | true |
| `verbProperties/targetable` | 3.7% (4/107) | 布尔 | false |
| `verbProperties/targetParams` | 78.5% (84/107) | 容器 |  |
| `verbProperties/targetParams/canTargetAnimals` | 31.8% (34/107) | 布尔 | False / True / false |
| `verbProperties/targetParams/canTargetBloodfeeders` | 1.9% (2/107) | 布尔 | false / true |
| `verbProperties/targetParams/canTargetBuildings` | 30.8% (33/107) | 布尔 | False / false / true |
| `verbProperties/targetParams/canTargetCorpses` | 2.8% (3/107) | 布尔 | true |
| `verbProperties/targetParams/canTargetEntities` | 4.7% (5/107) | 布尔 | False |
| `verbProperties/targetParams/canTargetHumans` | 11.2% (12/107) | 布尔 | False / false / true |
| `verbProperties/targetParams/canTargetItems` | 2.8% (3/107) | 布尔 | True / true |
| `verbProperties/targetParams/canTargetLocations` | 29.0% (31/107) | 布尔 | True / false / true |
| `verbProperties/targetParams/canTargetMechs` | 20.6% (22/107) | 布尔 | False / false / true |
| `verbProperties/targetParams/canTargetPawns` | 19.6% (21/107) | 布尔 | False / false / true |
| `verbProperties/targetParams/canTargetPlants` | 0.9% (1/107) | 布尔 | true |
| `verbProperties/targetParams/canTargetSelf` | 37.4% (40/107) | 布尔 | True / false / true |
| `verbProperties/targetParams/canTargetSubhumans` | 13.1% (14/107) | 布尔 | False / false |
| `verbProperties/targetParams/mapObjectTargetsMustBeAutoAttackable` | 1.9% (2/107) | 布尔 | False / false |
| `verbProperties/targetParams/neverTargetHostileFaction` | 6.5% (7/107) | 布尔 | True |
| `verbProperties/targetParams/neverTargetIncapacitated` | 4.7% (5/107) | 布尔 | True / true |
| `verbProperties/targetParams/onlyRepairableMechs` | 0.9% (1/107) | 布尔 | true |
| `verbProperties/targetParams/onlyTargetColonists` | 2.8% (3/107) | 布尔 | True / true |
| `verbProperties/targetParams/onlyTargetColonistsOrPrisonersOrSlaves` | 0.9% (1/107) | 布尔 | true |
| `verbProperties/targetParams/onlyTargetColonistsOrPrisonersOrSlavesAllowMinorMentalBreaks` | 0.9% (1/107) | 布尔 | true |
| `verbProperties/targetParams/onlyTargetCorpses` | 0.9% (1/107) | 布尔 | true |
| `verbProperties/targetParams/onlyTargetPrisonersOfColony` | 0.9% (1/107) | 布尔 | True |
| `verbProperties/targetParams/thingCategory` | 1.9% (2/107) | 文本 | Item |
| `verbProperties/ticksBetweenBurstShots` | 0.9% (1/107) | 数值 | 6 |
| `verbProperties/useableInPocketMaps` | 1.9% (2/107) | 布尔 | false |
| `verbProperties/useableInVacuum` | 0.9% (1/107) | 布尔 | false |
| `verbProperties/verbClass` | 54.2% (58/107) | 文本 | Verb_AbilityShoot / Verb_CastAbility / Verb_CastAbilityConsumeLeap |
| `verbProperties/violent` | 2.8% (3/107) | 布尔 | false |
| `verbProperties/warmupEffecter` | 2.8% (3/107) | 文本 | AnimalWarcall_Warmup / Fire_Burst_Warmup / JumpMechWarmupEffect |
| `verbProperties/warmupTime` | 78.5% (84/107) | 数值 | 0 / 0.25 / 0.5 |
| `waitForJobEnd` | 0.9% (1/107) | 布尔 | true |
| `warmupEffecter` | 9.3% (10/107) | 文本 | Bloodfeed_Warmup / HoraxianAbilityCasting / HoraxianSpellDark_Warmup |
| `warmupMote` | 7.5% (8/107) | 文本 | Mote_CoagulateStencil / Mote_HoraxSmallSpellWarmup / Mote_ResurrectAbility |
| `warmupMoteSocialSymbol` | 13.1% (14/107) | 文本 | Things/Mote/SpeechSymbols/Convert / UI/Abilities/CombatCommand / UI/Abilities/PreachHealth |
| `warmupPreEndSound` | 0.9% (1/107) | 文本 | Psycast_Neuroquake_CastEnd |
| `warmupPreEndSoundSeconds` | 0.9% (1/107) | 数值 | 5 |
| `warmupSound` | 12.2% (13/107) | 文本 | AnomalyAbilityWarmup / MoralistAbility_Warmup / PreachHealth_Warmup |
| `warmupStartSound` | 15.9% (17/107) | 文本 | AcidSpray_Warmup / Bloodfeed_Cast / Coagulate_Cast |
| `writeCombatLog` | 21.5% (23/107) | 布尔 | True / true |

## 四、原版 defName 一览（共 107 个，列出前 60）

```text
``                                `UnnaturalCorpseSkip`             `SpikeLaunch_Toughspike`          `SpikeLaunch_Fingerspike`       
``                                `SpineLaunch_Gorehulk`            ``                                `WarTrumpet`                    
`ThrumboRoar`                     `LeaderSpeech`                    `Speech`                          `MarksmanCommand`               
``                                ``                                `ResearchCommand`                 `FarmingCommand`                
`ProductionCommand`               `MiningCommand`                   `LaunchFragGrenade`               `LaunchEMPShell`                
`LaunchSmokeShell`                `PiercingSpine`                   `LaunchIncendiaryShell`           `WordOfInspiration`             
`CallMechanoids`                  `CallDropPods`                    `EMPPulse`                        ``                              
`LongjumpMechLauncher`            `WordOfTrust`                     `ConsumeLeap_Devourer`            `CorrosiveSpray`                
`SmokepopMech`                    `BerserkTrance`                   `DeactivateMechanoid`             `Heatspikes`                    
`AcidSpray`                       `FoamSpray`                       `Trial`                           `ReimplantXenogerm`             
`FireSpew`                        `LongjumpMech`                    `ConversionRitual`                `SludgeSpew`                    
`WordOfLove`                      `Farskip`                         `FireBurst`                       `FirefoampopMech`               
`PsychicSlaughter`                `Longjump`                        `EggSpew`                         `Stun`                          
`Burden`                          `EntropyDump`                     `Chunkskip`                       `ReleaseDeadlifeDust`           
`Focus`                           `Invisibility`                    `Flashstorm`                      `BulletShield`                  
```

_余下 47 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
