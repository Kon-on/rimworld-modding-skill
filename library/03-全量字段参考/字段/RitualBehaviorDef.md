# RitualBehaviorDef

- **所属线**：理念线
- **原版实例数**：27
- **字段路径数**：123
- **资料片**：Biotech、Ideology、Odyssey、Royalty
- **原版出处**：`Ideology/Defs/Rituals/Ritual_Behaviors.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<RitualBehaviorDef ParentName="DateRitualBehavior">
    <defName>BurnCircle</defName>
    <durationTicks>5000</durationTicks>
    <roles Inherit="False"/>
    <spectatorsLabel>Participants</spectatorsLabel>
    <spectatorGerund>participate</spectatorGerund>
    <stages Inherit="False">
      <li>
        <defaultDuty>SpectateSocial</defaultDuty>
        <endTriggers>
          <li Class="StageEndTrigger_DurationPercentage">
            <percentage>1</percentage>
          </li>
        </endTriggers>
      </li>
    </stages>
  </RitualBehaviorDef>

  
```

> 来自 `Ideology/Defs/Rituals/Ritual_Behaviors.xml`，defName = `BurnCircle`，XML 节点数 12（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：ChildBirth / DateRitual / Funeral
roles                                          [容器]
roles/li                                       [容器]
roles/li/countsAsParticipant                   [布尔]  例：False / false
roles/li/id                                    [文本]  例：doctor / leader / moralist
roles/li/label                                 [文本]  例：convict / doctor / mother
roles/li/maxCount                              [数值]  例：1
roles/li/required                              [布尔]  例：True / true
stages                                         [容器]
stages/li                                      [容器]
stages/li/defaultDuty                          [文本]  例：Party / PartyDance / Spectate
stages/li/endTriggers                          [容器]
stages/li/endTriggers/li                       [容器]
stages/li/endTriggers/li/percentage            [数值]  例：0.3 / 0.6 / 0.7
stages/li/endTriggers/li/roleIds/li            [文本]  例：convict / doctor / leader
stages/li/failTriggers/li                      [容器]
stages/li/failTriggers/li/desc                 [文本]  例：Convicted prisoner is not reachable. / Prisoner is not reachable. / escort asleep
stages/li/roleBehaviors                        [容器]
stages/li/roleBehaviors/li                     [容器]
stages/li/roleBehaviors/li/customPositions     [容器]
stages/li/roleBehaviors/li/customPositions/li  [容器]
stages/li/roleBehaviors/li/dutyDef             [文本]  例：ArriveToCell / Idle / KeepLyingDown
stages/li/roleBehaviors/li/roleId              [文本]  例：doctor / leader / moralist
```

## 三、全量字段表（123 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `cancellationTriggers` | 3.7% (1/27) | 容器 |  |
| `cancellationTriggers/li` | 3.7% (1/27) | 容器 |  |
| `cancellationTriggers/li/roleId` | 3.7% (1/27) | 文本 | target |
| `defName` | 96.3% (26/27) | 文本 | ChildBirth / DateRitual / Funeral |
| `displayCompletedMessage` | 3.7% (1/27) | 布尔 | false |
| `durationTicks` | 81.5% (22/27) | 数值 | -1 / 5000 / 6250 |
| `letterText` | 7.4% (2/27) | 文本 | {ORGANIZER_labelShort} is giving a speech from the throne.
\nIf all goes well, l / {SPEAKER_labelShort} is giv |
| `letterTitle` | 7.4% (2/27) | 文本 | Speech from the throne / {RITUAL_labelCap} |
| `maxEnhancerDistance` | 3.7% (1/27) | 数值 | 12 |
| `preceptRequirements` | 7.4% (2/27) | 容器 |  |
| `preceptRequirements/li` | 7.4% (2/27) | 容器 |  |
| `roles` | 100.0% (27/27) | 容器 |  |
| `roles/li` | 122.2% (33/27) | 容器 |  |
| `roles/li/addToLord` | 3.7% (1/27) | 布尔 | false |
| `roles/li/allowChild` | 63.0% (17/27) | 布尔 | false |
| `roles/li/allowDowned` | 11.1% (3/27) | 布尔 | true |
| `roles/li/allowKeepLayingDown` | 3.7% (1/27) | 布尔 | true |
| `roles/li/allowNonAggroMentalState` | 3.7% (1/27) | 布尔 | true |
| `roles/li/allowOtherIdeos` | 3.7% (1/27) | 布尔 | True |
| `roles/li/blocksSocialInteraction` | 14.8% (4/27) | 布尔 | true |
| `roles/li/categoryLabel` | 14.8% (4/27) | 文本 | duelist escorts / duelists |
| `roles/li/countsAsParticipant` | 107.4% (29/27) | 布尔 | False / false |
| `roles/li/customChildDisallowMessage` | 7.4% (2/27) | 文本 | Only adults can connect to the Gauranlen tree. / Only adults can link with an anima tree. |
| `roles/li/defaultForSelectedColonist` | 11.1% (3/27) | 布尔 | true |
| `roles/li/endJobOnRitualCleanup` | 7.4% (2/27) | 布尔 | false |
| `roles/li/id` | 122.2% (33/27) | 文本 | doctor / leader / moralist |
| `roles/li/ignoreBleeding` | 37.0% (10/27) | 布尔 | true |
| `roles/li/label` | 122.2% (33/27) | 文本 | convict / doctor / mother |
| `roles/li/maxCount` | 122.2% (33/27) | 数值 | 1 |
| `roles/li/mergeId` | 14.8% (4/27) | 文本 | duelist / escorte |
| `roles/li/minBodySize` | 3.7% (1/27) | 数值 | 0.75 |
| `roles/li/missingDesc` | 48.1% (13/27) | 文本 | a prisoner / an animal with body size of at least 0.8 / non-downed colonists capable of hauling |
| `roles/li/mustBeAbleToReachTarget` | 40.7% (11/27) | 布尔 | True |
| `roles/li/mustBeCapableToFight` | 7.4% (2/27) | 布尔 | true |
| `roles/li/noCandidatesGizmoDesc` | 3.7% (1/27) | 文本 | Need a colonist with the natural meditation focus type who is below maximum psyl |
| `roles/li/precept` | 40.7% (11/27) | 文本 | IdeoRole_Leader / IdeoRole_Moralist |
| `roles/li/removeFromAssignmentsOnDeath` | 11.1% (3/27) | 布尔 | false |
| `roles/li/required` | 107.4% (29/27) | 布尔 | True / true |
| `roles/li/requiredWorkType` | 7.4% (2/27) | 文本 | Doctor / PlantCutting |
| `roles/li/substitutable` | 25.9% (7/27) | 布尔 | True / true |
| `roles/li/tag` | 40.7% (11/27) | 文本 | Leader / Moralist |
| `roles/li/usedSkill` | 11.1% (3/27) | 文本 | Intellectual / Medicine |
| `roles/li/usedStat` | 7.4% (2/27) | 文本 | PilotingAbility |
| `soundDefsPerEnhancerCount` | 3.7% (1/27) | 容器 |  |
| `soundDefsPerEnhancerCount/li` | 25.9% (7/27) | 文本 | DanceParty_NoMusic / Drum_Music_1 / Drum_Music_2 |
| `spectatorFilter` | 7.4% (2/27) | 容器 |  |
| `spectatorFilter/description` | 7.4% (2/27) | 文本 | Must have natural focus type. / Spectators must be willing to watch the execution. |
| `spectatorGerund` | 48.1% (13/27) | 文本 | crew / participate / spectate |
| `spectatorsIgnoreBleeding` | 3.7% (1/27) | 布尔 | true |
| `spectatorsLabel` | 48.1% (13/27) | 文本 | Crew / Participants / Spectators |
| `stages` | 96.3% (26/27) | 容器 |  |
| `stages/li` | 229.6% (62/27) | 容器 |  |
| `stages/li/allowedSpectateSidesOverride` | 22.2% (6/27) | 文本 | Horizontal / Vertical |
| `stages/li/defaultDuty` | 229.6% (62/27) | 文本 | Party / PartyDance / Spectate |
| `stages/li/endTriggers` | 229.6% (62/27) | 容器 |  |
| `stages/li/endTriggers/li` | 237.0% (64/27) | 容器 |  |
| `stages/li/endTriggers/li/clearTag` | 18.5% (5/27) | 布尔 | true |
| `stages/li/endTriggers/li/countsTowardsProgress` | 3.7% (1/27) | 布尔 | true |
| `stages/li/endTriggers/li/percentage` | 125.9% (34/27) | 数值 | 0.3 / 0.6 / 0.7 |
| `stages/li/endTriggers/li/roleId` | 22.2% (6/27) | 文本 | animal / mother / prisoner |
| `stages/li/endTriggers/li/roleIds` | 70.4% (19/27) | 容器 |  |
| `stages/li/endTriggers/li/roleIds/li` | 96.3% (26/27) | 文本 | convict / doctor / leader |
| `stages/li/essential` | 37.0% (10/27) | 布尔 | True |
| `stages/li/failTriggers` | 44.4% (12/27) | 容器 |  |
| `stages/li/failTriggers/li` | 92.6% (25/27) | 容器 |  |
| `stages/li/failTriggers/li/allowanceTicks` | 7.4% (2/27) | 数值 | 1000 |
| `stages/li/failTriggers/li/desc` | 92.6% (25/27) | 文本 | Convicted prisoner is not reachable. / Prisoner is not reachable. / escort asleep |
| `stages/li/failTriggers/li/onlyIfTargetIsOfDef` | 22.2% (6/27) | 文本 | Campfire / LightBall |
| `stages/li/failTriggers/li/pawnId` | 40.7% (11/27) | 文本 | animal / leader / moralist |
| `stages/li/failTriggers/li/takeeId` | 29.6% (8/27) | 文本 | animal / convict / duelist1 |
| `stages/li/failTriggers/li/takerId` | 29.6% (8/27) | 文本 | doer / escorte1 / leader |
| `stages/li/failTriggers/li/thingDef` | 3.7% (1/27) | 文本 | Drum |
| `stages/li/highlightRolePawns` | 7.4% (2/27) | 容器 |  |
| `stages/li/highlightRolePawns/li` | 14.8% (4/27) | 文本 | convict / leader |
| `stages/li/ignoreDurationToFinishAfterStage` | 3.7% (1/27) | 布尔 | true |
| `stages/li/interruptedAction` | 3.7% (1/27) | 容器 |  |
| `stages/li/interruptedAction/count` | 3.7% (1/27) | 数值 | 4 |
| `stages/li/interruptedAction/def` | 3.7% (1/27) | 文本 | WoodLog |
| `stages/li/pawnLeaveAction` | 3.7% (1/27) | 容器 |  |
| `stages/li/pawnLeaveAction/count` | 3.7% (1/27) | 数值 | 4 |
| `stages/li/pawnLeaveAction/def` | 3.7% (1/27) | 文本 | WoodLog |
| `stages/li/postAction` | 22.2% (6/27) | 容器 |  |
| `stages/li/postAction/messageTypeDef` | 3.7% (1/27) | 文本 | NeutralEvent |
| `stages/li/postAction/roleId` | 14.8% (4/27) | 文本 | doctor / doer |
| `stages/li/postAction/sound` | 3.7% (1/27) | 文本 | GladiatorDuel_Start |
| `stages/li/postAction/tag` | 14.8% (4/27) | 文本 | Arrived |
| `stages/li/postAction/text` | 3.7% (1/27) | 文本 | {0}: The speech is over, and the party is beginning. |
| `stages/li/preAction` | 7.4% (2/27) | 容器 |  |
| `stages/li/preAction/roleIds` | 7.4% (2/27) | 容器 |  |
| `stages/li/preAction/roleIds/li` | 11.1% (3/27) | 文本 | duelist1 / duelist2 / target |
| `stages/li/preAction/stunDurationTicks` | 3.7% (1/27) | 数值 | 300 |
| `stages/li/roleBehaviors` | 192.6% (52/27) | 容器 |  |
| `stages/li/roleBehaviors/li` | 366.7% (99/27) | 容器 |  |
| `stages/li/roleBehaviors/li/customPositions` | 174.1% (47/27) | 容器 |  |
| `stages/li/roleBehaviors/li/customPositions/li` | 214.8% (58/27) | 容器 |  |
| `stages/li/roleBehaviors/li/customPositions/li/distFromTarget` | 7.4% (2/27) | 数值 | 2 |
| `stages/li/roleBehaviors/li/customPositions/li/distRange` | 18.5% (5/27) | 文本 | 1~3 / 3~3 |
| `stages/li/roleBehaviors/li/customPositions/li/duelistIndex` | 7.4% (2/27) | 数值 | 0 / 1 |
| `stages/li/roleBehaviors/li/customPositions/li/faceThing` | 18.5% (5/27) | 布尔 | true |
| `stages/li/roleBehaviors/li/customPositions/li/facing` | 40.7% (11/27) | 文本 | South / West |
| `stages/li/roleBehaviors/li/customPositions/li/highlight` | 3.7% (1/27) | 布尔 | true |
| `stages/li/roleBehaviors/li/customPositions/li/maxDistanceToFocus` | 40.7% (11/27) | 数值 | 5 |
| `stages/li/roleBehaviors/li/customPositions/li/offset` | 18.5% (5/27) | 文本 | (-1,0,0) |
| `stages/li/roleBehaviors/li/customPositions/li/preferredCellSearchPattern` | 11.1% (3/27) | 容器 |  |
| `stages/li/roleBehaviors/li/customPositions/li/preferredRotation` | 18.5% (5/27) | 文本 | North |
| `stages/li/roleBehaviors/li/dutyDef` | 366.7% (99/27) | 文本 | ArriveToCell / Idle / KeepLyingDown |
| `stages/li/roleBehaviors/li/jobReportOverride` | 11.1% (3/27) | 文本 | delivering baby / giving birth |
| `stages/li/roleBehaviors/li/roleId` | 366.7% (99/27) | 文本 | doctor / leader / moralist |
| `stages/li/roleBehaviors/li/speakerInteraction` | 59.3% (16/27) | 文本 | Speech_DateRitual / Speech_Funeral / Speech_Leader |
| `stages/li/showProgressBar` | 18.5% (5/27) | 布尔 | false |
| `stages/li/spectateDistanceOverride` | 55.6% (15/27) | 数值/文本 | 1 / 3~4 / 5~7 |
| `stages/li/spectatorsRequired` | 22.2% (6/27) | 布尔 | true |
| `stages/li/targetId` | 14.8% (4/27) | 文本 | convertee / mother / target |
| `stages/li/targets` | 22.2% (6/27) | 容器 |  |
| `stages/li/targets/li` | 29.6% (8/27) | 容器 |  |
| `stages/li/targets/li/pawnId` | 29.6% (8/27) | 文本 | doer / escorte1 / escorte2 |
| `stages/li/targets/li/targetId` | 29.6% (8/27) | 文本 | duelist1 / duelist2 / target |
| `stages/li/tickActionMaker` | 3.7% (1/27) | 容器 |  |
| `stages/li/tickActionMaker/preliminaryTicks` | 3.7% (1/27) | 文本 | 0~90 |
| `stages/li/tickActionMaker/woodCost` | 3.7% (1/27) | 数值 | 4 |
| `stages/li/visualEffectDef` | 33.3% (9/27) | 文本 | Funeral / SacrificeAnimal / SacrificePrisoner |
| `useVisualEffectsFromRoleIdIdeo` | 7.4% (2/27) | 文本 | connector / executioner |
| `workerClass` | 63.0% (17/27) | 文本 | RitualBehaviorWorker_ChildBirth / RitualBehaviorWorker_Funeral / RitualBehaviorWorker_Speech |

## 四、原版 defName 一览（共 27 个，列出前 60）

```text
`BurnCircle`                      `SmokeCircle`                     `FeastCannibal`                   ``                              
`CelebrationTree`                 `ThroneSpeech`                    `DancePartyTech`                  `CelebrationSkyLanterns`        
`Funeral`                         `TreeConnection`                  `AnimaTreeLinking`                `LeaderSpeech`                  
`CelebrationPartyDanceDrum`       `RoleChange`                      `TrialMentalState`                `DateRitual`                    
`GravshipLaunch`                  `Conversion`                      `TrialPrisoner`                   `Trial`                         
`SacrificeAnimal`                 `SacrificePrisoner`               `Execution`                       `ChildBirth`                    
`ScarificationCeremony`           `BlindingCeremony`                `GladiatorDuel`                 
```
