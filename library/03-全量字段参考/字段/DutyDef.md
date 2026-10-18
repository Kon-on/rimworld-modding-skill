# DutyDef

- **所属线**：系统线
- **原版实例数**：108
- **字段路径数**：120
- **资料片**：Anomaly、Biotech、Core、Ideology、Odyssey、Royalty
- **原版出处**：`Anomaly/Defs/DutyDefs/Duties_PsychicRituals.xml`、`Core/Defs/DutyDefs/Duties_Misc.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<DutyDef>
    <defName>Invoke</defName>
    <thinkNode Class="JobGiver_StandAndStare"/>
  </DutyDef>

  
```

> 来自 `Anomaly/Defs/DutyDefs/Duties_PsychicRituals.xml`，defName = `Invoke`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Goto_NoZeroLengthPaths / PerformHateChant / ShamblerSwarm
thinkNode                                      [容器]
thinkNode/subNodes                             [容器]
thinkNode/subNodes/li                          [容器]
```

## 三、全量字段表（120 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `alwaysShowWeapon` | 15.7% (17/108) | 布尔 | true |
| `constantThinkNode` | 5.6% (6/108) | 容器 |  |
| `constantThinkNode/subNodes` | 5.6% (6/108) | 容器 |  |
| `constantThinkNode/subNodes/li` | 5.6% (6/108) | 容器 |  |
| `constantThinkNode/subNodes/li/pickUpUtilityItems` | 1.8% (2/108) | 布尔 | true |
| `constantThinkNode/subNodes/li/preferBuildingDestroyers` | 0.9% (1/108) | 布尔 | true |
| `constantThinkNode/tagToGive` | 1.8% (2/108) | 文本 | Escaping |
| `defName` | 100.0% (108/108) | 文本 | Goto_NoZeroLengthPaths / PerformHateChant / ShamblerSwarm |
| `drawBodyOverride` | 0.9% (1/108) | 布尔 | true |
| `forceFaceUpPosture` | 0.9% (1/108) | 布尔 | true |
| `hook` | 30.6% (33/108) | 文本 | HighPriority / MediumPriority |
| `label` | 4.6% (5/108) | 文本 | concert / dance party / party |
| `ritualSpectateTarget` | 5.6% (6/108) | 布尔 | true |
| `socialModeMax` | 24.1% (26/108) | 文本 | Off |
| `thinkNode` | 100.0% (108/108) | 容器 |  |
| `thinkNode/allowZeroLengthPaths` | 0.9% (1/108) | 布尔 | true |
| `thinkNode/canFlyOutOfMap` | 1.8% (2/108) | 布尔 | false |
| `thinkNode/defaultLocomotion` | 1.8% (2/108) | 文本 | Walk |
| `thinkNode/exactCell` | 1.8% (2/108) | 布尔 | true |
| `thinkNode/subNodes` | 92.6% (100/108) | 容器 |  |
| `thinkNode/subNodes/li` | 261.1% (282/108) | 容器 |  |
| `thinkNode/subNodes/li/ability` | 1.8% (2/108) | 文本 | ConsumeLeap_Devourer / SpineLaunch_Gorehulk |
| `thinkNode/subNodes/li/addArrivalTagIfInvalidTarget` | 0.9% (1/108) | 布尔 | true |
| `thinkNode/subNodes/li/addArrivalTagIfNoBedAvailable` | 0.9% (1/108) | 布尔 | true |
| `thinkNode/subNodes/li/addArrivalTagIfTargetIsDead` | 1.8% (2/108) | 布尔 | true |
| `thinkNode/subNodes/li/allowTurrets` | 2.8% (3/108) | 布尔 | true |
| `thinkNode/subNodes/li/allowUnroofed` | 0.9% (1/108) | 布尔 | false |
| `thinkNode/subNodes/li/allowZeroLengthPaths` | 0.9% (1/108) | 布尔 | true |
| `thinkNode/subNodes/li/attackAllInert` | 7.4% (8/108) | 布尔 | true |
| `thinkNode/subNodes/li/canBashDoors` | 0.9% (1/108) | 布尔 | false |
| `thinkNode/subNodes/li/canFlyOutOfMap` | 2.8% (3/108) | 布尔 | false |
| `thinkNode/subNodes/li/canMineNonMineables` | 2.8% (3/108) | 布尔 | false |
| `thinkNode/subNodes/li/chance` | 0.9% (1/108) | 数值 | 0.05 |
| `thinkNode/subNodes/li/chaseTarget` | 1.8% (2/108) | 布尔 | false |
| `thinkNode/subNodes/li/count` | 1.8% (2/108) | 数值 | 4 |
| `thinkNode/subNodes/li/def` | 1.8% (2/108) | 文本 | WoodLog |
| `thinkNode/subNodes/li/defaultLocomotion` | 6.5% (7/108) | 文本 | Jog / Walk |
| `thinkNode/subNodes/li/desiredRadius` | 3.7% (4/108) | 数值 | 5 / 6 |
| `thinkNode/subNodes/li/destinationFocusIndex` | 1.8% (2/108) | 数值 | 2 / 3 |
| `thinkNode/subNodes/li/enemyDistToFleeRange` | 0.9% (1/108) | 文本 | 2.9~7.9 |
| `thinkNode/subNodes/li/exactCell` | 15.7% (17/108) | 布尔 | true |
| `thinkNode/subNodes/li/expireOnNearbyEnemy` | 3.7% (4/108) | 布尔 | true |
| `thinkNode/subNodes/li/expiryInterval` | 0.9% (1/108) | 数值 | 120 |
| `thinkNode/subNodes/li/fleeDistRange` | 0.9% (1/108) | 文本 | 13.5~20 |
| `thinkNode/subNodes/li/forceCanDig` | 0.9% (1/108) | 布尔 | true |
| `thinkNode/subNodes/li/forceCanDigIfAnyHostileActiveThreat` | 0.9% (1/108) | 布尔 | true |
| `thinkNode/subNodes/li/forceCanDigIfCantReachMapEdge` | 1.8% (2/108) | 布尔 | true |
| `thinkNode/subNodes/li/ignoreNonCombatants` | 2.8% (3/108) | 布尔 | true |
| `thinkNode/subNodes/li/invert` | 0.9% (1/108) | 布尔 | true |
| `thinkNode/subNodes/li/jobDef` | 0.9% (1/108) | 文本 | LayDown |
| `thinkNode/subNodes/li/jobMaxDuration` | 4.6% (5/108) | 数值 | 120 / 200 / 500 |
| `thinkNode/subNodes/li/locomotionUrgency` | 24.1% (26/108) | 文本 | Amble / Jog |
| `thinkNode/subNodes/li/locomotionUrgencyOutsideRadius` | 6.5% (7/108) | 文本 | Sprint / Walk |
| `thinkNode/subNodes/li/lookDirection` | 0.9% (1/108) | 文本 | NorthWest |
| `thinkNode/subNodes/li/maxDanger` | 2.8% (3/108) | 文本 | Deadly / Some |
| `thinkNode/subNodes/li/maxDistance` | 0.9% (1/108) | 数值 | 2.9 |
| `thinkNode/subNodes/li/maxDistFromPoint` | 2.8% (3/108) | 数值 | 25 / 50 |
| `thinkNode/subNodes/li/maxDistToDutyTarget` | 0.9% (1/108) | 数值 | 12 |
| `thinkNode/subNodes/li/maxDistToSquadFlag` | 5.6% (6/108) | 数值 | 16 |
| `thinkNode/subNodes/li/min` | 0.9% (1/108) | 数值 | 0.7 |
| `thinkNode/subNodes/li/minCategory` | 2.8% (3/108) | 文本 | UrgentlyHungry / VeryTired |
| `thinkNode/subNodes/li/minDistanceToOtherReservedCell` | 0.9% (1/108) | 数值 | 3 |
| `thinkNode/subNodes/li/mtbHours` | 0.9% (1/108) | 数值 | 2.5 |
| `thinkNode/subNodes/li/needLOSToAcquireNonPawnTargets` | 7.4% (8/108) | 布尔 | true |
| `thinkNode/subNodes/li/onlyIfDamagingState` | 0.9% (1/108) | 布尔 | true |
| `thinkNode/subNodes/li/onlyIfInDanger` | 3.7% (4/108) | 布尔 | true |
| `thinkNode/subNodes/li/overrideExpiryInterval` | 2.8% (3/108) | 数值 | 60 |
| `thinkNode/subNodes/li/ritualTagOnArrival` | 8.3% (9/108) | 文本 | Arrived |
| `thinkNode/subNodes/li/skipIfCantTargetNow` | 0.9% (1/108) | 布尔 | false |
| `thinkNode/subNodes/li/skipIfTargetCanReach` | 0.9% (1/108) | 布尔 | true |
| `thinkNode/subNodes/li/subNodes` | 40.7% (44/108) | 容器 |  |
| `thinkNode/subNodes/li/subNodes/li` | 61.1% (66/108) | 容器 |  |
| `thinkNode/subNodes/li/subNodes/li/chance` | 11.1% (12/108) | 数值 | 0.05 / 0.1 / 0.35 |
| `thinkNode/subNodes/li/subNodes/li/desiredRadius` | 1.8% (2/108) | 数值 | 6 |
| `thinkNode/subNodes/li/subNodes/li/exactCell` | 0.9% (1/108) | 布尔 | true |
| `thinkNode/subNodes/li/subNodes/li/expiryInterval` | 0.9% (1/108) | 数值 | 120 |
| `thinkNode/subNodes/li/subNodes/li/faceSpectatorsIfPossible` | 1.8% (2/108) | 布尔 | true |
| `thinkNode/subNodes/li/subNodes/li/hediff` | 0.9% (1/108) | 文本 | SmokeleafHigh |
| `thinkNode/subNodes/li/subNodes/li/ignoreOtherReservations` | 0.9% (1/108) | 布尔 | true |
| `thinkNode/subNodes/li/subNodes/li/locomotionUrgency` | 2.8% (3/108) | 文本 | Jog |
| `thinkNode/subNodes/li/subNodes/li/maintainFacing` | 0.9% (1/108) | 布尔 | true |
| `thinkNode/subNodes/li/subNodes/li/minCategory` | 2.8% (3/108) | 文本 | Hungry / Starving / VeryTired |
| `thinkNode/subNodes/li/subNodes/li/needLOSToAcquireNonPawnTargets` | 2.8% (3/108) | 布尔 | true |
| `thinkNode/subNodes/li/subNodes/li/severityRange` | 0.9% (1/108) | 文本 | 0.4~0.6 |
| `thinkNode/subNodes/li/subNodes/li/showSpeechBubbles` | 1.8% (2/108) | 布尔 | false |
| `thinkNode/subNodes/li/subNodes/li/soundDefFemale` | 6.5% (7/108) | 文本 | Speech_Funeral_Female / Speech_Ideoligious_Female / Speech_Leader_Female |
| `thinkNode/subNodes/li/subNodes/li/soundDefMale` | 6.5% (7/108) | 文本 | Speech_Funeral_Male / Speech_Ideoligious_Male / Speech_Leader_Male |
| `thinkNode/subNodes/li/subNodes/li/subNodes` | 15.7% (17/108) | 容器 |  |
| `thinkNode/subNodes/li/subNodes/li/subNodes/li` | 17.6% (19/108) | 容器 |  |
| `thinkNode/subNodes/li/subNodes/li/subNodes/li/desiredRadius` | 0.9% (1/108) | 数值 | 8 |
| `thinkNode/subNodes/li/subNodes/li/subNodes/li/needLOSToAcquireNonPawnTargets` | 0.9% (1/108) | 布尔 | true |
| `thinkNode/subNodes/li/subNodes/li/subNodes/li/subNodes` | 0.9% (1/108) | 容器 |  |
| `thinkNode/subNodes/li/subNodes/li/subNodes/li/subNodes/li` | 0.9% (1/108) | 容器 |  |
| `thinkNode/subNodes/li/subNodes/li/subNodes/li/targetAcquireRadius` | 0.9% (1/108) | 数值 | 15 |
| `thinkNode/subNodes/li/subNodes/li/subNodes/li/targetKeepRadius` | 0.9% (1/108) | 数值 | 18 |
| `thinkNode/subNodes/li/subNodes/li/subNodes/li/ticksRange` | 3.7% (4/108) | 数值/文本 | 350~750 / 480 |
| `thinkNode/subNodes/li/subNodes/li/targetAcquireRadius` | 2.8% (3/108) | 数值 | 12 / 14 / 65 |
| `thinkNode/subNodes/li/subNodes/li/targetKeepRadius` | 2.8% (3/108) | 数值 | 15 / 17 / 72 |
| `thinkNode/subNodes/li/subNodes/li/ticks` | 1.8% (2/108) | 数值 | 50 / 60 |
| `thinkNode/subNodes/li/subNodes/li/ticksBetweenWandersRange` | 3.7% (4/108) | 数值/文本 | 50 / 50~250 |
| `thinkNode/subNodes/li/subNodes/li/ticksRange` | 0.9% (1/108) | 文本 | 350~750 |
| `thinkNode/subNodes/li/subNodes/li/treeDef` | 6.5% (7/108) | 文本 | MainColonistBehaviorCore / SatisfyBasicNeeds / SatisfyBasicNeedsAndWork |
| `thinkNode/subNodes/li/subNodes/li/useBed` | 1.8% (2/108) | 布尔 | true |
| `thinkNode/subNodes/li/subNodes/li/wanderRadius` | 2.8% (3/108) | 数值 | 12 / 3 / 5 |
| `thinkNode/subNodes/li/subNodes/li/workTags` | 0.9% (1/108) | 容器 |  |
| `thinkNode/subNodes/li/subNodes/li/workTags/li` | 0.9% (1/108) | 文本 | Violent |
| `thinkNode/subNodes/li/tag` | 1.8% (2/108) | 文本 | carry / goto |
| `thinkNode/subNodes/li/tagToGive` | 2.8% (3/108) | 文本 | SatisfyingNeeds / WaitingForOthersToFinishGatheringItems |
| `thinkNode/subNodes/li/targetAcquireRadius` | 28.7% (31/108) | 数值 | 12 / 20 / 35 |
| `thinkNode/subNodes/li/targetKeepRadius` | 25.9% (28/108) | 数值 | 15 / 30 / 40 |
| `thinkNode/subNodes/li/thresholdTicks` | 0.9% (1/108) | 数值 | 600 |
| `thinkNode/subNodes/li/ticks` | 5.6% (6/108) | 数值 | 60 |
| `thinkNode/subNodes/li/ticksBetweenWandersRange` | 4.6% (5/108) | 文本 | 50~250 / 600~1200 |
| `thinkNode/subNodes/li/treeDef` | 13.9% (15/108) | 文本 | Abilities_Aggressive / SatisfyBasicNeeds / SatisfyVeryUrgentNeeds |
| `thinkNode/subNodes/li/wanderOnArrival` | 2.8% (3/108) | 布尔 | false |
| `thinkNode/subNodes/li/wanderRadius` | 13.0% (14/108) | 数值 | 12 / 3 / 5 |
| `thinkNode/subNodes/li/workTags` | 1.8% (2/108) | 容器 |  |
| `thinkNode/subNodes/li/workTags/li` | 1.8% (2/108) | 文本 | Violent |
| `thinkNode/tag` | 1.8% (2/108) | 文本 | goto |
| `thinkNode/tagToGive` | 1.8% (2/108) | 文本 | Escaping |

## 四、原版 defName 一览（共 108 个，列出前 60）

```text
`Invoke`                          `PsychicRitualDance`              `WaitForRitualParticipants`       `GatherOfferingsForPsychicRitual`
`PerformHateChant`                `Goto_NoZeroLengthPaths`          `ChimeraStalkFlee`                `Idle`                          
`ExitMapRandom`                   `ExitMapBest`                     `EnterTransporter`                `Bestow`                        
`Goto`                            `IdleNoInteraction`               `WanderClose_NoNeeds`             `EatAtCannibalPlatter`          
`StandOnCell`                     `GoToValidSubstructure`           `LinkWithAnimaTree`               `ChimeraStalkWander`            
`KeepLyingDown`                   `SpectateCircle`                  `SpectateSocial`                  `LayDownAwake`                  
`Pilgrims_Spectate`               `Sacrifice`                       `Scarify`                         `Blind`                         
`SpectateDirectionSociallyActive`  `DropWeapon`                      `Spectate`                        `TravelOrLeave`                 
`EnterTransporterAndDefendSelf`   `PlayTargetInstrument`            `LinkWithAnimaTreeSecondary`      `KeepLyingDownForBirth`         
`Kidnap`                          `Steal`                           `SleepForever`                    `DeliverPawnToCell`             
`Duel`                            `ChimeraAttack`                   `TakeWoundedGuest`                `DefendHiveAggressively`        
`ExitMapNearDutyTarget`           `WanderClose`                     `DeliverPawnToAltar`              `SightstealerSwarm`             
`DefendFleshmassHeart`            `VoidAwakeningWander`             `TravelOrWait`                    `ExitMapBestAndDefendSelf`      
`PrepareCaravan_GatherDownedPawns`  `Follow`                          `HuntEnemiesIndividual`           `ArriveToCell`                  
`ShamblerSwarm`                   `SightstealerAssault`             `AssaultThing`                    `Warqueen`                      
```

_余下 48 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
