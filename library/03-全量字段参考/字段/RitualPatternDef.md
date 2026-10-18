# RitualPatternDef

- **所属线**：理念线
- **原版实例数**：31
- **字段路径数**：34
- **资料片**：Biotech、Core、Ideology、Odyssey、Royalty
- **原版出处**：`Core/Defs/PreceptDefs/RitualPatternDefs/RitualPatterns.xml`、`Ideology/Defs/PreceptDefs/RitualPatternDefs/RitualPatterns.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<RitualPatternDef Abstract="True" Name="SpeechPatternBase">
    <ritualOutcomeEffect>AttendedSpeech</ritualOutcomeEffect>
  </RitualPatternDef>
  
```

> 来自 `Core/Defs/PreceptDefs/RitualPatternDefs/RitualPatterns.xml`，defName = ``，XML 节点数 2（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

_该类型没有出现率≥90% 的字段（字段高度自由）。_

## 三、全量字段表（34 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `allowOtherInstances` | 3.2% (1/31) | 布尔 | true |
| `alwaysStartAnytime` | 29.0% (9/31) | 布尔 | true |
| `beginRitualOverride` | 6.5% (2/31) | 文本 | gather for {0} / launch... |
| `cancelIconPathOverride` | 3.2% (1/31) | 文本 | UI/Commands/CancelLaunchGravship |
| `canMergeGizmosFromDifferentIdeos` | 6.5% (2/31) | 布尔 | false |
| `canStartAnytime` | 22.6% (7/31) | 布尔 | true |
| `defName` | 87.1% (27/31) | 文本 | ChildBirth / FuneralNoCorpse / FuneralStandard |
| `descOverride` | 29.0% (9/31) | 文本 | A dance party with drums. Participants will gather, socialize, play drums, and d / A dance party with loud mus |
| `iconPathOverride` | 38.7% (12/31) | 文本 | UI/Icons/Rituals/RitualAnimalSacrifice / UI/Icons/Rituals/RitualFestival / UI/Icons/Rituals/RitualPrisonerSacr |
| `ignoreConsumableBuildingRequirement` | 3.2% (1/31) | 布尔 | true |
| `ignoreExtremeTemperatures` | 3.2% (1/31) | 布尔 | true |
| `layerBlacklist` | 3.2% (1/31) | 容器 |  |
| `layerBlacklist/li` | 3.2% (1/31) | 文本 | Orbit |
| `maxTechLevel` | 3.2% (1/31) | 文本 | Neolithic |
| `mergeGizmosForObligations` | 6.5% (2/31) | 布尔 | true |
| `minTechLevel` | 3.2% (1/31) | 文本 | Industrial |
| `nameMaker` | 16.1% (5/31) | 文本 | NamerRitualFestival / NamerRitualFuneral / NamerRitualGladiatorDuel |
| `patternGroupTag` | 29.0% (9/31) | 容器/文本 | BlindingCeremony / CelebratedDate / RitualBuildingConsumer |
| `playsIdeoMusic` | 25.8% (8/31) | 布尔 | false |
| `ritualBehavior` | 87.1% (27/31) | 文本 | ChildBirth / DateRitual / Funeral |
| `ritualExpectedDesc` | 9.7% (3/31) | 文本 | Every year on {DATE}, {MEMBERS} can have a special celebration. / You can hold a {IDEOLIGION_adjective} funera |
| `ritualExpectedDescNoAdjective` | 6.5% (2/31) | 文本 | You can hold a funeral for {PAWN_nameDef} even though the body was lost. / You can hold a funeral for {PAWN_na |
| `ritualExplanation` | 3.2% (1/31) | 文本 | In case of success, their certainty will be reduced or they will convert immedia |
| `ritualObligationTargetFilter` | 71.0% (22/31) | 文本 | AnyEmptyGrave / ChildBirth / GauranlenTree |
| `ritualObligationTriggers` | 16.1% (5/31) | 容器 |  |
| `ritualObligationTriggers/li` | 16.1% (5/31) | 容器 |  |
| `ritualObligationTriggers/li/mustBePlayerIdeo` | 16.1% (5/31) | 布尔 | true |
| `ritualOnlyForIdeoMembers` | 29.0% (9/31) | 布尔 | false / true |
| `ritualOutcomeEffect` | 83.9% (26/31) | 文本 | AttendedFuneral / AttendedFuneralNoCorpse / AttendedSpeech |
| `ritualTargetFilter` | 19.4% (6/31) | 文本 | AltarIdeogramOrRitualSpot / AltarOrRitualSpot / IdeoBuildingOrRitualSpot |
| `shortDescOverride` | 29.0% (9/31) | 文本 | animal sacrifice / dance party / drum party |
| `showIdeoIconsInDialog` | 3.2% (1/31) | 布尔 | false |
| `tags` | 29.0% (9/31) | 容器 |  |
| `tags/li` | 25.8% (8/31) | 文本 | CelebratedDate / Consumable / Sacrifice |

## 四、原版 defName 一览（共 31 个，列出前 60）

```text
``                                `TrialPrisoner`                   `TrialMentalState`                ``                              
``                                `Trial`                           ``                                `ThroneSpeech`                  
`SacrificePrisoner`               `SacrificeAnimal`                 `LeaderSpeech`                    `BurnCircle`                    
`SmokeCircle`                     `FeastCannibal`                   `RoleChange`                      `Conversion`                    
`CelebrationTree`                 `Execution`                       `AnimaTreeLinking`                `ChildBirth`                    
`FuneralNoCorpse`                 `TreeConnection`                  `FuneralStandard`                 `GladiatorDuel`                 
`CelebrationPartyDanceTech`       `CelebrationPartyDanceDrum`       `CelebrationSkyLanterns`          `ScarificationCeremony`         
`BlindingCeremony`                `GravshipLaunch`                  `CelebrationPartyChat`          
```
