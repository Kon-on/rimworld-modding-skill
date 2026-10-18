# MentalStateDef

- **所属线**：人物线
- **原版实例数**：49
- **字段路径数**：43
- **资料片**：Anomaly、Biotech、Core、Ideology、Odyssey
- **原版出处**：`Core/Defs/MentalStateDefs/MentalStates_Mood.xml`、`Biotech/Defs/MentalStateDefs/MentalStates_Special.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<MentalStateDef Abstract="True" Name="BaseMentalState">
    <minTicksBeforeRecovery>10000</minTicksBeforeRecovery>
    <recoveryMtbDays>0.3</recoveryMtbDays>
  </MentalStateDef>

  
```

> 来自 `Core/Defs/MentalStateDefs/MentalStates_Mood.xml`，defName = ``，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：DarkVisions / EntityKiller / EntityLiberator
```

## 三、全量字段表（43 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `allowBeatfire` | 32.6% (16/49) | 布尔 | true |
| `allowGuilty` | 2.0% (1/49) | 布尔 | false |
| `baseInspectLine` | 79.6% (39/49) | 文本 | Mental state: Dark visions / Mental state: Entity liberator / Mental state: Entity slayer |
| `beginLetter` | 65.3% (32/49) | 文本 | {0} has become suddenly allured by a captive entity and is convinced it must be  / {0} has snapped. {PAWN_pron |
| `beginLetterDef` | 42.9% (21/49) | 文本 | NegativeEvent / NeutralEvent / ThreatSmall |
| `beginLetterLabel` | 30.6% (15/49) | 文本 | cube obsession / dark visions / insane ramblings |
| `blockInteractionInitiationExcept` | 20.4% (10/49) | 容器 |  |
| `blockInteractionInitiationExcept/li` | 12.2% (6/49) | 文本 | Insult / Slight |
| `blockInteractionRecipientExcept` | 20.4% (10/49) | 容器 |  |
| `blockInteractionRecipientExcept/li` | 14.3% (7/49) | 文本 | Insult / Slight |
| `blockNormalThoughts` | 42.9% (21/49) | 布尔 | true |
| `blockRandomInteraction` | 20.4% (10/49) | 布尔 | true |
| `blocksDefendAndExpandHive` | 2.0% (1/49) | 布尔 | true |
| `category` | 69.4% (34/49) | 文本 | Aggro / Malicious / Misc |
| `colonistsOnly` | 28.6% (14/49) | 布尔 | true |
| `defName` | 93.9% (46/49) | 文本 | DarkVisions / EntityKiller / EntityLiberator |
| `downedCanDo` | 4.1% (2/49) | 布尔 | true |
| `drugCategory` | 4.1% (2/49) | 文本 | Hard / Social |
| `escapingPrisonersIgnore` | 18.4% (9/49) | 布尔 | true |
| `ignoreDrugPolicy` | 2.0% (1/49) | 布尔 | true |
| `inCaravanCanDo` | 36.7% (18/49) | 布尔 | false / true |
| `label` | 73.5% (36/49) | 文本 | dark visions / entity liberator / entity slayer |
| `maxTicksBeforeRecovery` | 57.1% (28/49) | 数值 | 12000 / 15000 / 45000 |
| `minTicksBeforeRecovery` | 71.4% (35/49) | 数值 | 10000 / 30000 / 40000 |
| `moodRecoveryThought` | 32.6% (16/49) | 文本 | Catharsis / VoidCatharsis |
| `nameColor` | 71.4% (35/49) | 文本 | (0.65, 0.9, 0.93) / (0.8,0.36,1) / (0.88,0.48,0.16) |
| `prisonersCanDo` | 14.3% (7/49) | 布尔 | false |
| `recoverFromCollapsingExhausted` | 12.2% (6/49) | 布尔 | false |
| `recoverFromDowned` | 10.2% (5/49) | 布尔 | false |
| `recoverFromSleep` | 51.0% (25/49) | 布尔 | false / true |
| `recoveryMessage` | 57.1% (28/49) | 容器/文本 | {0} is no longer freeing entities. / {0} is no longer slaughtering random entities. / {PAWN_nameDef} has stopp |
| `recoveryMtbDays` | 46.9% (23/49) | 数值 | 0.033 / 0.166 / 0.3 |
| `requiredCapacities` | 6.1% (3/49) | 容器 |  |
| `requiredCapacities/li` | 6.1% (3/49) | 文本 | Manipulation / Talking |
| `slavesCanDo` | 2.0% (1/49) | 布尔 | false |
| `slavesOnly` | 2.0% (1/49) | 布尔 | true |
| `stateClass` | 81.6% (40/49) | 文本 | MentalState_EntityKiller / MentalState_EntityLiberator / MentalState_HumanityBreak |
| `stateEffecter` | 16.3% (8/49) | 文本 | AnimalWarcallMentalState / BabyCrying / BabyGiggling |
| `stopsJobs` | 2.0% (1/49) | 布尔 | false |
| `tale` | 6.1% (3/49) | 文本 | MentalStateBerserk / MentalStateGaveUp |
| `ticksBetweenRamblingRange` | 6.1% (3/49) | 文本 | 1200~3600 / 600~1800 / 600~900 |
| `unspawnedNotInCaravanCanDo` | 4.1% (2/49) | 布尔 | true |
| `workerClass` | 34.7% (17/49) | 文本 | MentalStateWorker_BingingDrug / MentalStateWorker_EntityKiller / MentalStateWorker_EntityLiberator |

## 四、原版 defName 一览（共 49 个，列出前 60）

```text
``                                `BerserkPermanent`                `Binging_DrugMajor`               `Wander_Psychotic_Short`        
``                                `BerserkShort`                    `Crying`                          `Giggling`                      
`BedroomTantrum`                  `TargetedInsultingSpree`          `ManhunterPermanent`              `TargetedTantrum`               
`CocoonDisturbed`                 `SadisticRage`                    `Manhunter`                       `SocialFighting`                
`IdeoChange`                      `PanicFleeFire`                   `PanicFlee`                       `BerserkMechanoid`              
`Roaming`                         `Terror`                          `ManhunterBloodRain`              ``                              
`BerserkWarcall`                  `BerserkTrance`                   `CubeSculpting`                   `Rebellion`                     
`WanderConfused`                  `Binging_DrugExtreme`             `GiveUpExit`                      `Wander_Psychotic`              
`DarkVisions`                     `InsaneRamblings`                 `TerrifyingHallucinations`        `HumanityBreak`                 
`Jailbreaker`                     `EntityLiberator`                 `Binging_Food`                    `Wander_Sad`                    
`Wander_OwnRoom`                  `EntityKiller`                    `FireStartingSpree`               `Slaughterer`                   
`CorpseObsession`                 `MurderousRage`                   `Berserk`                         `Tantrum`                       
`InsultingSpree`                
```
