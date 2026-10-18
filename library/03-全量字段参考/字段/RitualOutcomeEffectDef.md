# RitualOutcomeEffectDef

- **所属线**：理念线
- **原版实例数**：31
- **字段路径数**：82
- **资料片**：Biotech、Core、Ideology、Odyssey、Royalty
- **原版出处**：`Ideology/Defs/Rituals/Ritual_Outcomes.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<RitualOutcomeEffectDef ParentName="DestroyConsumableBuilding">
    <defName>DestroyConsumableBuilding_ChristmasTree</defName>
    <effecter>VanishChristmasTree</effecter>
  </RitualOutcomeEffectDef>

  
```

> 来自 `Ideology/Defs/Rituals/Ritual_Outcomes.xml`，defName = `DestroyConsumableBuilding_ChristmasTree`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
comps/li                                       [容器]
comps/li/curve                                 [容器]
comps/li/curve/points                          [容器]
comps/li/curve/points/li                       [文本]  例：(0, 0.0) / 0,  0 / 0.6, 0.1
comps/li/label                                 [文本]  例：bed health effects / indoors / loved one present
outcomeChances/li                              [容器]
outcomeChances/li/chance                       [数值]  例：0.025 / 0.075 / 0.2
outcomeChances/li/description                  [文本]  例：The {0} was heartwarming. The speech was captivating and heartfelt, and everyone / {MOTHER_labelShort} gave birth to a baby. Unfortunately, the baby is sick. / {MOTHER_labelShort} gave birth to a healthy baby!
outcomeChances/li/label                        [文本]  例：Healthy / Inspirational / Sick
outcomeChances/li/memory                       [文本]  例：EncouragingSpeech / InspirationalSpeech / TerribleSpeech
outcomeChances/li/positivityIndex              [数值]  例：-1 / 0 / 1
```

## 三、全量字段表（82 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `allowAttachableOutcome` | 16.1% (5/31) | 布尔 | false |
| `allowOutcomeWithNoAttendance` | 6.5% (2/31) | 布尔 | true |
| `comps` | 83.9% (26/31) | 容器 |  |
| `comps/li` | 229.0% (71/31) | 容器 |  |
| `comps/li/allowAltars` | 16.1% (5/31) | 布尔 | true |
| `comps/li/autoApplyInClassicMode` | 3.2% (1/31) | 布尔 | true |
| `comps/li/autoPoweredNeedsToBeOn` | 3.2% (1/31) | 布尔 | true |
| `comps/li/curve` | 112.9% (35/31) | 容器 |  |
| `comps/li/curve/points` | 112.9% (35/31) | 容器 |  |
| `comps/li/curve/points/li` | 390.3% (121/31) | 文本 | (0, 0.0) / 0,  0 / 0.6, 0.1 |
| `comps/li/def` | 12.9% (4/31) | 文本 | Lectern |
| `comps/li/defs` | 9.7% (3/31) | 容器 |  |
| `comps/li/defs/li` | 9.7% (3/31) | 文本 | Campfire / Ideogram / LightBall |
| `comps/li/disableInClassicMode` | 6.5% (2/31) | 布尔 | true |
| `comps/li/expectedThingLabelTip` | 22.6% (7/31) | 文本 | a campfire / a lightball / an altar |
| `comps/li/facilityQualityOffsets` | 9.7% (3/31) | 容器 |  |
| `comps/li/facilityQualityOffsets/li` | 9.7% (3/31) | 容器 |  |
| `comps/li/facilityQualityOffsets/li/key` | 9.7% (3/31) | 文本 | LargeThruster / PilotSubpersonaCore / SmallThruster |
| `comps/li/facilityQualityOffsets/li/value` | 9.7% (3/31) | 数值 | 0.01 / 0.03 / 0.15 |
| `comps/li/label` | 196.8% (61/31) | 文本 | bed health effects / indoors / loved one present |
| `comps/li/labelAbstract` | 32.3% (10/31) | 文本 | Defendant's negotiation ability / doctor's medicine skill / mother's age |
| `comps/li/labelNotMet` | 3.2% (1/31) | 文本 | loved one absent |
| `comps/li/lovedOneOfRole` | 3.2% (1/31) | 文本 | mother |
| `comps/li/maxDistance` | 6.5% (2/31) | 数值 | 12 |
| `comps/li/maxHorDistFromTarget` | 12.9% (4/31) | 数值 | 5 |
| `comps/li/mustBeBed` | 3.2% (1/31) | 布尔 | true |
| `comps/li/offsetForSlave` | 3.2% (1/31) | 数值 | 0 |
| `comps/li/offsetPerExpectation` | 3.2% (1/31) | 容器 |  |
| `comps/li/offsetPerExpectation/ExtremelyLow` | 3.2% (1/31) | 数值 | 0.1 |
| `comps/li/offsetPerExpectation/High` | 3.2% (1/31) | 数值 | -0.2 |
| `comps/li/offsetPerExpectation/Low` | 3.2% (1/31) | 数值 | 0 |
| `comps/li/offsetPerExpectation/Moderate` | 3.2% (1/31) | 数值 | -0.1 |
| `comps/li/offsetPerExpectation/Noble` | 3.2% (1/31) | 数值 | -0.3 |
| `comps/li/offsetPerExpectation/RoleElite` | 3.2% (1/31) | 数值 | -0.3 |
| `comps/li/offsetPerExpectation/RoleSupreme` | 3.2% (1/31) | 数值 | -0.3 |
| `comps/li/offsetPerExpectation/Royal` | 3.2% (1/31) | 数值 | -0.3 |
| `comps/li/offsetPerExpectation/SkyHigh` | 3.2% (1/31) | 数值 | -0.3 |
| `comps/li/offsetPerExpectation/VeryLow` | 3.2% (1/31) | 数值 | 0.05 |
| `comps/li/qualityOffset` | 83.9% (26/31) | 数值 | 0.05 / 0.2 / 0.25 |
| `comps/li/roleId` | 54.8% (17/31) | 文本 | doctor / moralist / mother |
| `comps/li/scaledBy` | 9.7% (3/31) | 数值 | -0.25 / 0.25 |
| `comps/li/skillDef` | 3.2% (1/31) | 文本 | Medicine |
| `comps/li/statDef` | 48.4% (15/31) | 文本 | BirthRitualQualityOffset / Cleanliness / Impressiveness |
| `comps/li/tag` | 3.2% (1/31) | 文本 | LaunchedSkyLantern |
| `defName` | 87.1% (27/31) | 文本 | AttendedFuneral / AttendedFuneralNoCorpse / AttendedSpeech |
| `description` | 64.5% (20/31) | 文本 | All quality factors determine how healthy the mom and baby are going to be. / Depending on ritual quality, par |
| `effecter` | 9.7% (3/31) | 文本 | VanishBurnable / VanishBurnbong / VanishChristmasTree |
| `extraInfoLines` | 3.2% (1/31) | 容器 |  |
| `extraInfoLines/li` | 3.2% (1/31) | 文本 | Each participant will make a lantern out of 4 wood. |
| `extraOutcomeDescriptions` | 6.5% (2/31) | 容器 |  |
| `extraOutcomeDescriptions/li` | 9.7% (3/31) | 容器 |  |
| `extraOutcomeDescriptions/li/description` | 9.7% (3/31) | 文本 | Additionally, the mother will have a {0_percentage} chance to die during birth. / Additionally, there's a {0_p |
| `extraOutcomeDescriptions/li/qualityToValue` | 9.7% (3/31) | 文本 | GravshipUtility.LaunchCooldownFromQuality / GravshipUtility.NegativeLandingOutcomeFromQuality / PregnancyUtili |
| `extraPredictedOutcomeDescriptions` | 25.8% (8/31) | 容器 |  |
| `extraPredictedOutcomeDescriptions/li` | 32.3% (10/31) | 文本 | If the {0} is beautiful or unforgettable, the skylanterns might attract a group  / If the {0} is fun or unforg |
| `filthCountToSpawn` | 6.5% (2/31) | 文本 | 2~4 |
| `filthDefToSpawn` | 6.5% (2/31) | 文本 | Filth_Ash |
| `fleckDef` | 3.2% (1/31) | 文本 | BloodSplashLong |
| `fleckScaleRange` | 3.2% (1/31) | 文本 | 1~2.5 |
| `flecksPerCell` | 3.2% (1/31) | 数值 | 15 |
| `fleckVelocityAngle` | 3.2% (1/31) | 文本 | -55~55 |
| `fleckVelocitySpeed` | 3.2% (1/31) | 文本 | 0.1~1.5 |
| `givesDevelopmentPoints` | 12.9% (4/31) | 布尔 | false |
| `honorFromQuality` | 3.2% (1/31) | 容器 |  |
| `honorFromQuality/points` | 3.2% (1/31) | 容器 |  |
| `honorFromQuality/points/li` | 12.9% (4/31) | 文本 | (0,   0) / (0.3, 1) / (0.6, 2) |
| `maxQuality` | 3.2% (1/31) | 数值 | 0.9 |
| `minQuality` | 3.2% (1/31) | 数值 | 0.1 |
| `outcomeChances` | 51.6% (16/31) | 容器 |  |
| `outcomeChances/li` | 187.1% (58/31) | 容器 |  |
| `outcomeChances/li/chance` | 187.1% (58/31) | 数值 | 0.025 / 0.075 / 0.2 |
| `outcomeChances/li/description` | 161.3% (50/31) | 文本 | The {0} was heartwarming. The speech was captivating and heartfelt, and everyone / {MOTHER_labelShort} gave bi |
| `outcomeChances/li/ideoCertaintyOffset` | 12.9% (4/31) | 数值 | -0.3 / -1 / 0.12 |
| `outcomeChances/li/label` | 187.1% (58/31) | 文本 | Healthy / Inspirational / Sick |
| `outcomeChances/li/memory` | 158.1% (49/31) | 文本 | EncouragingSpeech / InspirationalSpeech / TerribleSpeech |
| `outcomeChances/li/positivityIndex` | 187.1% (58/31) | 数值 | -1 / 0 / 1 |
| `outcomeChances/li/potentialExtraOutcomeDesc` | 32.3% (10/31) | 文本 | Everyone felt refreshed after their trance-like dancing experience. Participants / The skylanterns lifted high |
| `outcomeChances/li/roleIdsNotGainingMemory` | 12.9% (4/31) | 容器 |  |
| `outcomeChances/li/roleIdsNotGainingMemory/li` | 12.9% (4/31) | 文本 | duelist |
| `startingQuality` | 3.2% (1/31) | 数值 | 0.5 |
| `warnOnLowQuality` | 6.5% (2/31) | 布尔 | false |
| `workerClass` | 67.7% (21/31) | 文本 | RitualOutcomeEffectWorker_ChildBirth / RitualOutcomeEffectWorker_Execution / RitualOutcomeEffectWorker_FromQua |

## 四、原版 defName 一览（共 31 个，列出前 60）

```text
`DestroyConsumableBuilding_ChristmasTree`  `CelebratedDate_Consumable`       `DestroyConsumableBuilding_Pyre`  `DestroyConsumableBuilding_Burnbong`
`DestroyConsumableBuilding`       ``                                `AttendedFuneral`                 `AttendedFuneralNoCorpse`       
`AnimaTreeLinking`                `TrialMentalState`                `ConnectToTree`                   `CelebrationPartyDanceDrum`     
`DestroyConsumableBuilding_CannibalPlatter`  `CelebrationPartyDanceTech`       `RoleChange`                      ``                              
``                                `Trial`                           `Execution`                       `CelebrationSkyLanterns`        
``                                `BestowingCeremony`               `CelebratedDate`                  `AttendedSpeech`                
`ScarificationCeremony`           `Sacrifice`                       `BlindingCeremony`                `GladiatorDuel`                 
`GravshipLaunch`                  `ChildBirth`                      `Conversion`                    
```
