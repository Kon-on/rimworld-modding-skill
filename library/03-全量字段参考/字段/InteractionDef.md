# InteractionDef

- **所属线**：人物线
- **原版实例数**：68
- **字段路径数**：17
- **资料片**：Anomaly、Biotech、Core、Ideology、Royalty
- **原版出处**：`Ideology/Defs/InteractionDefs/Interactions_Social.xml`、`Core/Defs/InteractionDefs/Interactions_Animal.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<InteractionDef>
    <defName>Counsel_Failure</defName>
    <label>failed counsel</label>
    <symbol>UI/Abilities/Counsel</symbol>
    <logRulesInitiator>
      <rulesStrings>
        <li>r_logentry-&gt;[INITIATOR_nameDef] tried to counsel [RECIPIENT_nameDef], but botched the attempt and made things worse.</li>
      </rulesStrings>
    </logRulesInitiator>
  </InteractionDef>

  
```

> 来自 `Ideology/Defs/InteractionDefs/Interactions_Social.xml`，defName = `Counsel_Failure`，XML 节点数 7（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：CreepyWords / DisturbingChat / InhumanRambling
label                                          [文本]  例：creepy words / inhuman rambling / occult teaching
logRulesInitiator                              [容器]
logRulesInitiator/include/li                   [文本]  例：DarkDialogue / LessonInteractionCommonSituations / LessonInteractionHowTo
logRulesInitiator/rulesStrings                 [容器]
logRulesInitiator/rulesStrings/li              [文本]  例：r_logentry->[INITIATOR_nameDef] [disturbed] [RECIPIENT_nameDef] by [talkingAbout / r_logentry->[INITIATOR_nameDef] [rambled] [darkSpeechAdverb] about [subjectInsan / r_logentry->[INITIATOR_nameDef] [rambled] about [subjectInsane].
symbol                                         [文本]  例：Things/Mote/SpeechSymbols/CreepyWords / Things/Mote/SpeechSymbols/InhumanRambling / Things/Mote/SpeechSymbols/Interrogation
```

## 三、全量字段表（17 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (68/68) | 文本 | CreepyWords / DisturbingChat / InhumanRambling |
| `ignoreTimeSinceLastInteraction` | 55.9% (38/68) | 布尔 | True |
| `initiatorThought` | 2.9% (2/68) | 文本 | Chitchat / DeepTalk |
| `initiatorXpGainAmount` | 16.2% (11/68) | 数值 | 230 / 45 / 70 |
| `initiatorXpGainSkill` | 16.2% (11/68) | 文本 | Animals / Social |
| `interactionMote` | 1.5% (1/68) | 文本 | Mote_Thought |
| `label` | 100.0% (68/68) | 文本 | creepy words / inhuman rambling / occult teaching |
| `logRulesInitiator` | 100.0% (68/68) | 容器 |  |
| `logRulesInitiator/include` | 50.0% (34/68) | 容器 |  |
| `logRulesInitiator/include/li` | 97.1% (66/68) | 文本 | DarkDialogue / LessonInteractionCommonSituations / LessonInteractionHowTo |
| `logRulesInitiator/rulesStrings` | 100.0% (68/68) | 容器 |  |
| `logRulesInitiator/rulesStrings/li` | 1483.8% (1009/68) | 文本 | r_logentry->[INITIATOR_nameDef] [disturbed] [RECIPIENT_nameDef] by [talkingAbout / r_logentry->[INITIATOR_name |
| `recipientThought` | 11.8% (8/68) | 文本 | Chitchat / DeepTalk / RapportBuilt |
| `socialFightBaseChance` | 2.9% (2/68) | 数值 | 0.005 / 0.04 |
| `symbol` | 97.1% (66/68) | 文本 | Things/Mote/SpeechSymbols/CreepyWords / Things/Mote/SpeechSymbols/InhumanRambling / Things/Mote/SpeechSymbols/ |
| `symbolSource` | 4.4% (3/68) | 文本 | InitiatorFaction / InitiatorIdeo |
| `workerClass` | 58.8% (40/68) | 文本 | InteractionWorker / InteractionWorker_InhumanRambling / InteractionWorker_InterrogateIdentity |

## 四、原版 defName 一览（共 68 个，列出前 60）

```text
`Counsel_Failure`                 `Convert_Success`                 `Convert_Failure`                 `Reassure`                      
`LessonGeneric`                   `ConvertIdeoAttempt`              `WorkDrive`                       `WordOfTrust`                   
`WordOfJoy`                       `WordOfLove`                      `WordOfSerenity`                  `WordOfInspiration`             
`MarriageProposal`                `PreachHealth`                    `CreepyWords`                     `Breakup`                       
`EnslaveAttempt`                  `Suppress`                        `InhumanRambling`                 `PrisonerStudyAnomaly`          
`RecruitAttempt`                  `Counsel_Success`                 `OccultTeaching`                  `SparkSlaveRebellion`           
`Trial_Defend`                    `ReleaseToWild`                   `SparkJailbreak`                  `TrainAttempt`                  
`LessonSocial`                    `Speech_DateRitual`               `Speech_Execution`                `LessonIntellectual`            
`Speech_Funeral`                  `Speech_TreeConnection`           `TameAttempt`                     `Trial_Accuse`                  
`Speech_Blinding`                 `KindWords`                       `Speech_Duel`                     `Speech_Conversion`             
`DeepTalk`                        `LessonShooting`                  `Slight`                          `LessonArtistic`                
`Speech_Scarification`            `Speech_RemoveRole`               `LessonConstruction`              `LessonPlants`                  
`AnimalChat`                      `Chitchat`                        `Speech_Sacrifice`                `LessonCooking`                 
`Nuzzle`                          `LessonMining`                    `Speech_AcceptRole`               `LessonMelee`                   
`LessonCrafting`                  `Insult`                          `LessonAnimals`                   `BabyPlay`                      
```

_余下 8 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
