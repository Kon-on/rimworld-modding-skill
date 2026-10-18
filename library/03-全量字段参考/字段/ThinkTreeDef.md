# ThinkTreeDef

- **所属线**：系统线
- **原版实例数**：61
- **字段路径数**：157
- **资料片**：Anomaly、Biotech、Core、Ideology、Odyssey
- **原版出处**：`Anomaly/Defs/ThinkTreeDefs/Chimera.xml`、`Anomaly/Defs/ThinkTreeDefs/Ghoul.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<ThinkTreeDef>
    <defName>ChimeraConstant</defName>
    <thinkRoot Class="ThinkNode_Priority">
      <subNodes>
        <!-- Despawned -->
        <li Class="ThinkNode_Subtree">
          <treeDef>Despawned</treeDef>
        </li>
      </subNodes>
    </thinkRoot>
  </ThinkTreeDef>
  
```

> 来自 `Anomaly/Defs/ThinkTreeDefs/Chimera.xml`，defName = `ChimeraConstant`，XML 节点数 7（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：AwokenCorpse / AwokenCorpseConstant / Chimera
thinkRoot                                      [容器]
thinkRoot/subNodes                             [容器]
thinkRoot/subNodes/li                          [容器]
thinkRoot/subNodes/li/subNodes                 [容器]
thinkRoot/subNodes/li/subNodes/li              [容器]
thinkRoot/subNodes/li/subNodes/li/subNodes     [容器]
thinkRoot/subNodes/li/subNodes/li/subNodes/li  [容器]
thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes [容器]
thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li [容器]
thinkRoot/subNodes/li/treeDef                  [文本]  例：BurningResponse / Despawned / Downed
```

## 三、全量字段表（157 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (61/61) | 文本 | AwokenCorpse / AwokenCorpseConstant / Chimera |
| `thinkRoot` | 100.0% (61/61) | 容器 |  |
| `thinkRoot/invert` | 1.6% (1/61) | 布尔 | true |
| `thinkRoot/subNodes` | 100.0% (61/61) | 容器 |  |
| `thinkRoot/subNodes/li` | 562.3% (343/61) | 容器 |  |
| `thinkRoot/subNodes/li/ability` | 3.3% (2/61) | 文本 | ConsumeLeap_Devourer / SpineLaunch_Gorehulk |
| `thinkRoot/subNodes/li/allowFlyOutInstead` | 1.6% (1/61) | 布尔 | true |
| `thinkRoot/subNodes/li/allowTurrets` | 3.3% (2/61) | 布尔 | true |
| `thinkRoot/subNodes/li/dutyHook` | 1.6% (1/61) | 文本 | HighPriority |
| `thinkRoot/subNodes/li/enemyDistToFleeRange` | 1.6% (1/61) | 文本 | 2.9~7.9 |
| `thinkRoot/subNodes/li/fleeDistRange` | 1.6% (1/61) | 文本 | 13.5~20 |
| `thinkRoot/subNodes/li/inBedOnly` | 1.6% (1/61) | 布尔 | true |
| `thinkRoot/subNodes/li/insertTag` | 34.4% (21/61) | 文本 | Devourer_PreMain / Devourer_PreWander / Fleshbeast_PreMain |
| `thinkRoot/subNodes/li/invert` | 19.7% (12/61) | 布尔 | true |
| `thinkRoot/subNodes/li/leaveJoinableLordIfIssuesJob` | 3.3% (2/61) | 布尔 | true |
| `thinkRoot/subNodes/li/maxDanger` | 8.2% (5/61) | 文本 | Deadly |
| `thinkRoot/subNodes/li/maxDistance` | 3.3% (2/61) | 数值 | 2.9 |
| `thinkRoot/subNodes/li/maxRadius` | 1.6% (1/61) | 数值 | 15 |
| `thinkRoot/subNodes/li/mtbDays` | 3.3% (2/61) | 数值 | 60 |
| `thinkRoot/subNodes/li/mtbHours` | 1.6% (1/61) | 数值 | 10 |
| `thinkRoot/subNodes/li/needLOSToAcquireNonPawnTargets` | 1.6% (1/61) | 布尔 | true |
| `thinkRoot/subNodes/li/pawnKind` | 3.3% (2/61) | 文本 | WildMan |
| `thinkRoot/subNodes/li/requiresInjury` | 1.6% (1/61) | 布尔 | false |
| `thinkRoot/subNodes/li/skipIfCantTargetNow` | 1.6% (1/61) | 布尔 | false |
| `thinkRoot/subNodes/li/state` | 44.3% (27/61) | 文本 | Attack / Escape / Sleep |
| `thinkRoot/subNodes/li/stateClass` | 4.9% (3/61) | 文本 | MentalState_InsultingSpree / MentalState_Manhunter / MentalState_Tantrum |
| `thinkRoot/subNodes/li/states` | 4.9% (3/61) | 容器 |  |
| `thinkRoot/subNodes/li/states/li` | 14.8% (9/61) | 文本 | Binging_DrugExtreme / Binging_DrugMajor / HumanityBreak |
| `thinkRoot/subNodes/li/subNodes` | 252.5% (154/61) | 容器 |  |
| `thinkRoot/subNodes/li/subNodes/li` | 480.3% (293/61) | 容器 |  |
| `thinkRoot/subNodes/li/subNodes/li/ability` | 4.9% (3/61) | 文本 | AnimalWarcall / Longjump / LongjumpMechLauncher |
| `thinkRoot/subNodes/li/subNodes/li/attackAllInert` | 1.6% (1/61) | 布尔 | true |
| `thinkRoot/subNodes/li/subNodes/li/canBash` | 1.6% (1/61) | 布尔 | true |
| `thinkRoot/subNodes/li/subNodes/li/canBashDoors` | 1.6% (1/61) | 布尔 | true |
| `thinkRoot/subNodes/li/subNodes/li/chaseTarget` | 1.6% (1/61) | 布尔 | true |
| `thinkRoot/subNodes/li/subNodes/li/defaultLocomotion` | 4.9% (3/61) | 文本 | Walk |
| `thinkRoot/subNodes/li/subNodes/li/dutyHook` | 1.6% (1/61) | 文本 | MediumPriority |
| `thinkRoot/subNodes/li/subNodes/li/emergency` | 1.6% (1/61) | 布尔 | true |
| `thinkRoot/subNodes/li/subNodes/li/expireOnNearbyEnemy` | 1.6% (1/61) | 布尔 | true |
| `thinkRoot/subNodes/li/subNodes/li/forceCanDig` | 1.6% (1/61) | 布尔 | true |
| `thinkRoot/subNodes/li/subNodes/li/humanlikesOnly` | 1.6% (1/61) | 布尔 | true |
| `thinkRoot/subNodes/li/subNodes/li/ignoreForbidden` | 1.6% (1/61) | 布尔 | true |
| `thinkRoot/subNodes/li/subNodes/li/inBedOnly` | 13.1% (8/61) | 布尔 | true |
| `thinkRoot/subNodes/li/subNodes/li/invert` | 6.6% (4/61) | 布尔 | true |
| `thinkRoot/subNodes/li/subNodes/li/leaveJoinableLordIfIssuesJob` | 8.2% (5/61) | 布尔 | true |
| `thinkRoot/subNodes/li/subNodes/li/locomotionUrgency` | 4.9% (3/61) | 文本 | Jog |
| `thinkRoot/subNodes/li/subNodes/li/maxDanger` | 27.9% (17/61) | 文本 | Deadly / Some |
| `thinkRoot/subNodes/li/subNodes/li/maxDistToSquadFlag` | 1.6% (1/61) | 数值 | 8 |
| `thinkRoot/subNodes/li/subNodes/li/minCategory` | 3.3% (2/61) | 文本 | UrgentlyHungry / VeryTired |
| `thinkRoot/subNodes/li/subNodes/li/minIntelligence` | 1.6% (1/61) | 文本 | ToolUser |
| `thinkRoot/subNodes/li/subNodes/li/minPriority` | 3.3% (2/61) | 数值 | 0.5 |
| `thinkRoot/subNodes/li/subNodes/li/mode` | 3.3% (2/61) | 文本 | Attack / Patrol |
| `thinkRoot/subNodes/li/subNodes/li/mtbDays` | 3.3% (2/61) | 数值 | 60 |
| `thinkRoot/subNodes/li/subNodes/li/mtbHours` | 4.9% (3/61) | 数值 | 1 / 1.5 |
| `thinkRoot/subNodes/li/subNodes/li/need` | 1.6% (1/61) | 文本 | Food |
| `thinkRoot/subNodes/li/subNodes/li/pawnKind` | 1.6% (1/61) | 文本 | Dryad_Gaumaker |
| `thinkRoot/subNodes/li/subNodes/li/subNodes` | 190.2% (116/61) | 容器 |  |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li` | 293.4% (179/61) | 容器 |  |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/ability` | 3.3% (2/61) | 文本 | ResurrectionMech / SmokepopMech |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/chance` | 1.6% (1/61) | 数值 | 0.5 |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/defaultLocomotion` | 14.8% (9/61) | 文本 | Amble / Jog / Walk |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/expiryInterval` | 1.6% (1/61) | 数值 | 560 |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/forceScanWholeMap` | 1.6% (1/61) | 布尔 | true |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/interval` | 1.6% (1/61) | 数值 | 65 |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/invert` | 4.9% (3/61) | 布尔 | true |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/jobDef` | 3.3% (2/61) | 文本 | BeatFire / Rescue |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/jobMaxDuration` | 1.6% (1/61) | 数值 | 1200 |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/leaveJoinableLordIfIssuesJob` | 6.6% (4/61) | 布尔 | true |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/locomotionUrgency` | 3.3% (2/61) | 文本 | Amble / Jog |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/maxAttackDistance` | 1.6% (1/61) | 数值 | 65 |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/maxDanger` | 29.5% (18/61) | 文本 | Deadly / None / Some |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/maxLevelPercentage` | 36.1% (22/61) | 数值 | 0.05 / 0.15 |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/min` | 3.3% (2/61) | 数值 | 0.7 |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/minCategory` | 1.6% (1/61) | 文本 | UrgentlyHungry |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/need` | 1.6% (1/61) | 文本 | Joy |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/needLOSToAcquireNonPawnTargets` | 1.6% (1/61) | 布尔 | true |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/requiredCapacities` | 4.9% (3/61) | 容器 |  |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/requiredCapacities/li` | 4.9% (3/61) | 文本 | Manipulation |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes` | 106.6% (65/61) | 容器 |  |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li` | 159.0% (97/61) | 容器 |  |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/ability` | 8.2% (5/61) | 文本 | AnimalWarcall / LongjumpMech / LongjumpMechLauncher |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/abilityDef` | 1.6% (1/61) | 文本 | ResurrectionMech |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/chance` | 3.3% (2/61) | 数值 | 0.1 |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/defaultLocomotion` | 6.6% (4/61) | 文本 | Walk |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/emergency` | 1.6% (1/61) | 布尔 | true |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/expiryInterval` | 6.6% (4/61) | 数值 | 120 / 500 / 560 |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/forced` | 1.6% (1/61) | 布尔 | true |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/invert` | 1.6% (1/61) | 布尔 | true |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/leaveJoinableLordIfIssuesJob` | 1.6% (1/61) | 布尔 | true |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/locomotionUrgency` | 1.6% (1/61) | 文本 | Amble |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/maxDanger` | 13.1% (8/61) | 文本 | Deadly / None |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/maxDistToSquadFlag` | 1.6% (1/61) | 数值 | 8 |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/maxLevelPercentage` | 3.3% (2/61) | 数值 | 0.05 / 0.15 |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/minCategory` | 6.6% (4/61) | 文本 | Starving / Tired / UrgentlyHungry |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/mtbDays` | 3.3% (2/61) | 数值 | 60 |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/radius` | 3.3% (2/61) | 数值 | 75 |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes` | 36.1% (22/61) | 容器 |  |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes/li` | 49.2% (30/61) | 容器 |  |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes/li/ability` | 1.6% (1/61) | 文本 | ResurrectionMech |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes/li/attackMeleeThreatEvenIfNotHostile` | 4.9% (3/61) | 布尔 | true |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes/li/defaultLocomotion` | 1.6% (1/61) | 文本 | Sprint |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes/li/expiryInterval` | 3.3% (2/61) | 数值 | 500 |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes/li/failIfCantJoinOrCreateCaravan` | 1.6% (1/61) | 布尔 | true |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes/li/invert` | 1.6% (1/61) | 布尔 | true |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes/li/maxDanger` | 3.3% (2/61) | 文本 | None |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes/li/maxThreatDistance` | 1.6% (1/61) | 数值 | 2 |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes/li/maxTicksAgo` | 1.6% (1/61) | 数值 | 120 |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes/li/minCloseTargets` | 1.6% (1/61) | 数值 | 2 |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes` | 18.0% (11/61) | 容器 |  |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes/li` | 19.7% (12/61) | 容器 |  |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes/li/ability` | 3.3% (2/61) | 文本 | Longjump / SmokepopMech |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes/li/defaultLocomotion` | 3.3% (2/61) | 文本 | Walk |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes/li/locomotionUrgency` | 1.6% (1/61) | 文本 | Jog |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes/li/maxDanger` | 3.3% (2/61) | 文本 | Deadly |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes/li/minCategory` | 1.6% (1/61) | 文本 | Tired |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes/li/reportStringOverride` | 1.6% (1/61) | 文本 | Patrolling. |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes` | 1.6% (1/61) | 容器 |  |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes/li` | 1.6% (1/61) | 容器 |  |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes/li/ability` | 1.6% (1/61) | 文本 | LongjumpMech |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes/li/thresholdTicks` | 1.6% (1/61) | 数值 | 120 |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes/li/tagToGive` | 9.8% (6/61) | 文本 | Misc / MiscWork / TrainedAnimalBehavior |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes/li/targetAcquireRadius` | 1.6% (1/61) | 数值 | 65 |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes/li/targetKeepRadius` | 1.6% (1/61) | 数值 | 72 |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes/li/thresholdPercent` | 1.6% (1/61) | 数值 | 0.25 |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/subNodes/li/ticksBetweenWandersRange` | 3.3% (2/61) | 文本 | 120~240 |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/tagToGive` | 1.6% (1/61) | 文本 | Escaping |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/targetIndex` | 1.6% (1/61) | 文本 | B |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/thresholdTicks` | 3.3% (2/61) | 数值 | 120 / 600 |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/ticksBetweenWandersRange` | 11.5% (7/61) | 文本 | 120~240 / 125~200 |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/trainable` | 4.9% (3/61) | 文本 | Haul |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/subNodes/li/treeDef` | 3.3% (2/61) | 文本 | DigOutIfCannotReachMapEdge |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/tagToGive` | 26.2% (16/61) | 文本 | Idle / Misc / RestingForMedicalReasons |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/targetAcquireRadius` | 1.6% (1/61) | 数值 | 65 |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/targetKeepRadius` | 1.6% (1/61) | 数值 | 72 |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/threshold` | 1.6% (1/61) | 数值 | 0.9 |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/thresholdPercent` | 1.6% (1/61) | 数值 | 0.25 |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/ticksBetweenWandersRange` | 9.8% (6/61) | 文本 | 120~240 / 125~200 |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/trainable` | 8.2% (5/61) | 文本 | Obedience / Rescue |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/treeDef` | 3.3% (2/61) | 文本 | Downed / LordDuty |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/urgentOnly` | 1.6% (1/61) | 布尔 | true |
| `thinkRoot/subNodes/li/subNodes/li/subNodes/li/workMode` | 6.6% (4/61) | 文本 | Escort / Recharge / SelfShutdown |
| `thinkRoot/subNodes/li/subNodes/li/tagToGive` | 67.2% (41/61) | 文本 | DraftedOrder / Idle / Misc |
| `thinkRoot/subNodes/li/subNodes/li/targetAcquireRadius` | 9.8% (6/61) | 数值 | 30 / 65 |
| `thinkRoot/subNodes/li/subNodes/li/targetKeepRadius` | 9.8% (6/61) | 数值 | 35 / 72 |
| `thinkRoot/subNodes/li/subNodes/li/threshold` | 1.6% (1/61) | 数值 | 0.6 |
| `thinkRoot/subNodes/li/subNodes/li/ticksBetweenWandersRange` | 9.8% (6/61) | 文本 | 120~240 / 180~720 |
| `thinkRoot/subNodes/li/subNodes/li/trainable` | 6.6% (4/61) | 文本 | Dig / Forage |
| `thinkRoot/subNodes/li/subNodes/li/treeDef` | 39.3% (24/61) | 文本 | JoinAutoJoinableCaravan / LeaveIfStarving / LeaveIfWrongSeason |
| `thinkRoot/subNodes/li/subNodes/li/wanderRadius` | 3.3% (2/61) | 数值 | 12 / 6 |
| `thinkRoot/subNodes/li/tagToGive` | 18.0% (11/61) | 文本 | Idle / Misc / SatisfyingNeeds |
| `thinkRoot/subNodes/li/targetAcquireRadius` | 11.5% (7/61) | 数值 | 20 / 30 / 65 |
| `thinkRoot/subNodes/li/targetKeepRadius` | 11.5% (7/61) | 数值 | 30 / 35 / 72 |
| `thinkRoot/subNodes/li/ticksBetweenWandersRange` | 8.2% (5/61) | 文本 | 120~240 / 60~120 |
| `thinkRoot/subNodes/li/treeDef` | 154.1% (94/61) | 文本 | BurningResponse / Despawned / Downed |
| `thinkRoot/subNodes/li/waitInSafeTemp` | 1.6% (1/61) | 布尔 | false |
| `thinkRoot/subNodes/li/wanderRadius` | 1.6% (1/61) | 数值 | 5 |
| `thinkRoot/tagToGive` | 18.0% (11/61) | 文本 | InMentalState / Misc / SatisfyingNeeds |

## 四、原版 defName 一览（共 61 个，列出前 60）

```text
`ChimeraConstant`                 `FleshmassNucleusConstant`        `NociosphereConstant`             `RevenantConstant`              
`HumanlikeBabyConstant`           `LordDutyConstant`                `HumanlikeBaby`                   `Despawned`                     
`DigOutIfCannotReachMapEdge`      `SatisfyBasicNeeds`               `AwokenCorpseConstant`            `DevourerConstant`              
`FleshbeastConstant`              `FleshmassNucleus`                `GorehulkConstant`                `MetalhorrorConstant`           
`NoctolConstant`                  `ShamblerConstant`                `SightstealerConstant`            `BurningResponse`               
`SatisfyBasicNeedsAndWork`        `SatisfyVeryUrgentNeeds`          `WaspDroneConstant`               `LeaveIfWrongSeason`            
`HunterDroneConstant`             `Abilities_Aggressive`            `Downed`                          `LeaveIfStarving`               
`RopedPawn`                       `Chimera`                         `GhoulConstant`                   `Sightstealer`                  
`WarUrchinConstant`               `AnimalConstant`                  `InsectConstant`                  `Nociosphere`                   
`SentryDroneConstant`             `Abilities_Escape`                `LordDuty`                        `MainWildManBehaviorCore`       
`Revenant`                        `MainColonistBehaviorCore`        `AwokenCorpse`                    `HumanlikeConstant`             
`JoinAutoJoinableCaravan`         `Drone`                           `Shambler`                        `Devourer`                      
`Gorehulk`                        `Noctol`                          `Metalhorror`                     `MentalStateCritical`           
`Fleshbeast`                      `MechConstant`                    `Ghoul`                           `Dryad`                         
`Mechanoid`                       `Animal`                          `Insect`                          `Humanlike`                     
```

_余下 1 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
