# StorytellerDef

- **所属线**：世界线
- **原版实例数**：5
- **字段路径数**：104
- **资料片**：Core
- **原版出处**：`Core/Defs/Storyteller/Storytellers.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<StorytellerDef ParentName="BaseStoryteller">
    <defName>Tutor</defName>
    <label>Tutor Hidden</label>
    <populationIntentFactorFromPopCurve>
      <points>
        <li>0, 0</li>
      </points>
    </populationIntentFactorFromPopCurve>
    <listVisible>false</listVisible>
    <listOrder>1000</listOrder>
    <tutorialMode>true</tutorialMode>
    <disableAdaptiveTraining>true</disableAdaptiveTraining>
    <disableAlerts>true</disableAlerts>
    <disablePermadeath>true</disablePermadeath>
    <forcedDifficulty>Easy</forcedDifficulty>
    <comps Inherit="False"/>
  </StorytellerDef>
```

> 来自 `Core/Defs/Storyteller/Storytellers.xml`，defName = `Tutor`，XML 节点数 14（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
adaptDaysGrowthRateCurve/points/li             [文本]  例：(-0.01,  3) / (-30,    3) / (-30.01, 6)
adaptDaysLossFromColonistViolentlyDownedByPopulation/points/li [文本]  例：(1,  8) / (11, 5) / (2,  6)
comps                                          [容器]
comps/li                                       [容器]
comps/li/acceptFractionByDaysPassedCurve       [容器]
comps/li/acceptFractionByDaysPassedCurve/points [容器]
comps/li/acceptFractionByDaysPassedCurve/points/li [文本]  例：(15, 1) / (8, 0)
comps/li/allowedTargetTags                     [容器]
comps/li/allowedTargetTags/li                  [文本]  例：Map_Misc / Map_PlayerHome / Map_TempIncident
comps/li/applyCaravanVisibility                [布尔]  例：true
comps/li/baseIncidentsPerYear                  [数值]  例：2 / 4 / 5
comps/li/category                              [文本]  例：GiveQuest / Misc / ThreatBig
comps/li/enableIfAnyModActive                  [容器]
comps/li/enableIfAnyModActive/li               [文本]  例：Ludeon.RimWorld.Anomaly / Ludeon.RimWorld.Biotech / Ludeon.RimWorld.Ideology
comps/li/incident                              [文本]  例：GiveQuest_AncientComplex_Mechanitor / GiveQuest_ReliquaryPilgrims / PoluxTreeSpawn
comps/li/minDaysPassed                         [数值]  例：20 / 30 / 35
comps/li/minSpacingDays                        [数值]  例：20 / 3 / 30
comps/li/mtbDays                               [数值]  例：15 / 4 / 4.8
comps/li/numIncidentsRange                     [数值/文本]  例：0.2~1 / 1 / 1~2
comps/li/offDays                               [数值]  例：0 / 15 / 6.0
comps/li/onDays                                [数值]  例：15 / 40 / 60
pointsFactorFromAdaptDays/points/li            [文本]  例：(  0, 0.80) / ( 30, 1.00) / ( 60, 1.20)
populationIntentFactorFromPopCurve/points/li   [文本]  例：0,  8.0 / 1,  2.0 / 4,  1.0
```

## 三、全量字段表（104 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `adaptDaysGameStartGraceDays` | 20.0% (1/5) | 数值 | 30 |
| `adaptDaysGrowthRateCurve` | 20.0% (1/5) | 容器 |  |
| `adaptDaysGrowthRateCurve/points` | 20.0% (1/5) | 容器 |  |
| `adaptDaysGrowthRateCurve/points/li` | 160.0% (8/5) | 文本 | (-0.01,  3) / (-30,    3) / (-30.01, 6) |
| `adaptDaysLossFromColonistLostByPostPopulation` | 20.0% (1/5) | 容器 |  |
| `adaptDaysLossFromColonistLostByPostPopulation/points` | 20.0% (1/5) | 容器 |  |
| `adaptDaysLossFromColonistLostByPostPopulation/points/li` | 60.0% (3/5) | 文本 | ( 0, 30) / (11, 30) / (20, 20) |
| `adaptDaysLossFromColonistViolentlyDownedByPopulation` | 20.0% (1/5) | 容器 |  |
| `adaptDaysLossFromColonistViolentlyDownedByPopulation/points` | 20.0% (1/5) | 容器 |  |
| `adaptDaysLossFromColonistViolentlyDownedByPopulation/points/li` | 100.0% (5/5) | 文本 | (1,  8) / (11, 5) / (2,  6) |
| `adaptDaysMax` | 20.0% (1/5) | 数值 | 100 |
| `adaptDaysMin` | 20.0% (1/5) | 数值 | -60 |
| `comps` | 100.0% (5/5) | 容器 |  |
| `comps/li` | 1420.0% (71/5) | 容器 |  |
| `comps/li/acceptFractionByDaysPassedCurve` | 120.0% (6/5) | 容器 |  |
| `comps/li/acceptFractionByDaysPassedCurve/points` | 120.0% (6/5) | 容器 |  |
| `comps/li/acceptFractionByDaysPassedCurve/points/li` | 240.0% (12/5) | 文本 | (15, 1) / (8, 0) |
| `comps/li/acceptPercentFactorPerThreatPointsCurve` | 40.0% (2/5) | 容器 |  |
| `comps/li/acceptPercentFactorPerThreatPointsCurve/points` | 40.0% (2/5) | 容器 |  |
| `comps/li/acceptPercentFactorPerThreatPointsCurve/points/li` | 80.0% (4/5) | 文本 | (2800, 0) / (800, 1) |
| `comps/li/allowedTargetTags` | 960.0% (48/5) | 容器 |  |
| `comps/li/allowedTargetTags/li` | 1240.0% (62/5) | 文本 | Map_Misc / Map_PlayerHome / Map_TempIncident |
| `comps/li/applyCaravanVisibility` | 120.0% (6/5) | 布尔 | true |
| `comps/li/baseIncidentsPerYear` | 200.0% (10/5) | 数值 | 2 / 4 / 5 |
| `comps/li/baseMtbDaysPerDrill` | 20.0% (1/5) | 数值 | 20 |
| `comps/li/blockedByQueuedOrActiveQuests` | 20.0% (1/5) | 容器 |  |
| `comps/li/blockedByQueuedOrActiveQuests/li` | 40.0% (2/5) | 文本 | MechanitorShip / OpportunitySite_AncientComplex_Mechanitor |
| `comps/li/category` | 620.0% (31/5) | 文本 | GiveQuest / Misc / ThreatBig |
| `comps/li/categoryWeights` | 20.0% (1/5) | 容器 |  |
| `comps/li/categoryWeights/FactionArrival` | 20.0% (1/5) | 数值 | 2.4 |
| `comps/li/categoryWeights/Misc` | 20.0% (1/5) | 数值 | 3.5 |
| `comps/li/categoryWeights/OrbitalVisitor` | 20.0% (1/5) | 数值 | 1.1 |
| `comps/li/categoryWeights/ShipChunkDrop` | 20.0% (1/5) | 数值 | 0.22 |
| `comps/li/categoryWeights/ThreatBig` | 20.0% (1/5) | 数值 | 1.4 |
| `comps/li/categoryWeights/ThreatSmall` | 20.0% (1/5) | 数值 | 0.6 |
| `comps/li/countdownFactorAnyConnectors` | 20.0% (1/5) | 数值 | 2 |
| `comps/li/daysBetweenPodSpawns` | 20.0% (1/5) | 数值 | 60 |
| `comps/li/delayTicks` | 80.0% (4/5) | 数值 | 120 / 180 |
| `comps/li/disableIfAnyModActive` | 60.0% (3/5) | 容器 |  |
| `comps/li/disableIfAnyModActive/li` | 60.0% (3/5) | 文本 | Ludeon.RimWorld.Royalty |
| `comps/li/disallowedTargetTags` | 40.0% (2/5) | 容器 |  |
| `comps/li/disallowedTargetTags/li` | 40.0% (2/5) | 文本 | Map_RaidBeacon |
| `comps/li/enableIfAnyModActive` | 320.0% (16/5) | 容器 |  |
| `comps/li/enableIfAnyModActive/li` | 320.0% (16/5) | 文本 | Ludeon.RimWorld.Anomaly / Ludeon.RimWorld.Biotech / Ludeon.RimWorld.Ideology |
| `comps/li/existingMechanitorOrMechlinkMTBFactor` | 20.0% (1/5) | 数值 | 4 |
| `comps/li/fireAfterDaysPassed` | 80.0% (4/5) | 数值 | 20 / 26 / 6 |
| `comps/li/forceRaidEnemyBeforeDaysPassed` | 40.0% (2/5) | 数值 | 20 |
| `comps/li/fullAlliesOnly` | 60.0% (3/5) | 布尔 | true |
| `comps/li/incident` | 580.0% (29/5) | 文本 | GiveQuest_AncientComplex_Mechanitor / GiveQuest_ReliquaryPilgrims / PoluxTreeSpawn |
| `comps/li/lastFireMaxMTBThreshold` | 20.0% (1/5) | 数值 | 2 |
| `comps/li/lastFireMinMTBThreshold` | 20.0% (1/5) | 数值 | 0.5 |
| `comps/li/maxThreatBigIntervalDays` | 20.0% (1/5) | 数值 | 13 |
| `comps/li/minColonistCount` | 20.0% (1/5) | 数值 | 3 |
| `comps/li/minColonyWealth` | 20.0% (1/5) | 数值 | 150000 |
| `comps/li/minDanger` | 60.0% (3/5) | 文本 | High |
| `comps/li/minDaysPassed` | 540.0% (27/5) | 数值 | 20 / 30 / 35 |
| `comps/li/minIncChancePopulationIntentFactor` | 20.0% (1/5) | 数值 | 0.2 |
| `comps/li/minSpacingDays` | 400.0% (20/5) | 数值 | 20 / 3 / 30 |
| `comps/li/minWealth` | 20.0% (1/5) | 数值 | 20000 |
| `comps/li/mtbDays` | 160.0% (8/5) | 数值 | 15 / 4 / 4.8 |
| `comps/li/numIncidentsRange` | 340.0% (17/5) | 数值/文本 | 0.2~1 / 1 / 1~2 |
| `comps/li/offDays` | 220.0% (11/5) | 数值 | 0 / 15 / 6.0 |
| `comps/li/onDays` | 340.0% (17/5) | 数值 | 15 / 40 / 60 |
| `comps/li/parms` | 60.0% (3/5) | 容器 |  |
| `comps/li/parms/allowedThreats` | 60.0% (3/5) | 文本 | Raids |
| `comps/li/parms/minSpacingDays` | 60.0% (3/5) | 数值 | 0.04 |
| `comps/li/parms/minThreatPoints` | 60.0% (3/5) | 数值 | 500 |
| `comps/li/parms/numIncidentsRange` | 60.0% (3/5) | 文本 | 1~2 |
| `comps/li/parms/offDays` | 60.0% (3/5) | 数值 | 0.5 |
| `comps/li/parms/onDays` | 60.0% (3/5) | 数值 | 1.0 |
| `comps/li/questDef` | 20.0% (1/5) | 文本 | MechanoidSignal |
| `comps/li/questIncident` | 20.0% (1/5) | 文本 | GiveQuest_MechanoidSignal |
| `comps/li/randomPointsFactorRange` | 20.0% (1/5) | 文本 | 0.5~1.5 |
| `comps/li/refireEveryDays` | 20.0% (1/5) | 数值 | 22 |
| `comps/li/skipIfColonistHasMinTitle` | 20.0% (1/5) | 文本 | Yeoman |
| `comps/li/skipIfOnExtremeBiome` | 40.0% (2/5) | 布尔 | true |
| `comps/li/skipThreatBigIfRaidBeacon` | 20.0% (1/5) | 布尔 | true |
| `comps/li/spaceMinSpacingDays` | 20.0% (1/5) | 数值 | 2 |
| `comps/li/spaceMtbDayFactor` | 20.0% (1/5) | 数值 | 2 |
| `comps/li/thing` | 20.0% (1/5) | 文本 | Wastepack |
| `defName` | 80.0% (4/5) | 文本 | Cassandra / Phoebe / Randy |
| `description` | 60.0% (3/5) | 文本 | Cassandra creates story events on a classic increasing curve of challenge and te / Phoebe gives lots of time b |
| `disableAdaptiveTraining` | 20.0% (1/5) | 布尔 | true |
| `disableAlerts` | 20.0% (1/5) | 布尔 | true |
| `disablePermadeath` | 20.0% (1/5) | 布尔 | true |
| `forcedDifficulty` | 20.0% (1/5) | 文本 | Easy |
| `label` | 80.0% (4/5) | 文本 | Cassandra Classic / Phoebe Chillax / Randy Random |
| `listOrder` | 80.0% (4/5) | 数值 | 1000 / 20 / 30 |
| `listVisible` | 20.0% (1/5) | 布尔 | false |
| `pointsFactorFromAdaptDays` | 20.0% (1/5) | 容器 |  |
| `pointsFactorFromAdaptDays/points` | 20.0% (1/5) | 容器 |  |
| `pointsFactorFromAdaptDays/points/li` | 120.0% (6/5) | 文本 | (  0, 0.80) / ( 30, 1.00) / ( 60, 1.20) |
| `pointsFactorFromDaysPassed` | 20.0% (1/5) | 容器 |  |
| `pointsFactorFromDaysPassed/points` | 20.0% (1/5) | 容器 |  |
| `pointsFactorFromDaysPassed/points/li` | 40.0% (2/5) | 文本 | (10, 0.70) / (40, 1.00) |
| `populationIntentFactorFromPopAdaptDaysCurve` | 20.0% (1/5) | 容器 |  |
| `populationIntentFactorFromPopAdaptDaysCurve/points` | 20.0% (1/5) | 容器 |  |
| `populationIntentFactorFromPopAdaptDaysCurve/points/li` | 40.0% (2/5) | 文本 | ( 0, 0) / ( 8, 1) |
| `populationIntentFactorFromPopCurve` | 40.0% (2/5) | 容器 |  |
| `populationIntentFactorFromPopCurve/points` | 40.0% (2/5) | 容器 |  |
| `populationIntentFactorFromPopCurve/points/li` | 140.0% (7/5) | 文本 | 0,  8.0 / 1,  2.0 / 4,  1.0 |
| `portraitLarge` | 60.0% (3/5) | 文本 | UI/HeroArt/Storytellers/CassandraClassic / UI/HeroArt/Storytellers/PhoebeFriendly / UI/HeroArt/Storytellers/Ra |
| `portraitTiny` | 60.0% (3/5) | 文本 | UI/HeroArt/Storytellers/CassandraClassicTiny / UI/HeroArt/Storytellers/PhoebeFriendlyTiny / UI/HeroArt/Storyte |
| `tutorialMode` | 20.0% (1/5) | 布尔 | true |

## 四、原版 defName 一览（共 5 个，列出前 60）

```text
`Tutor`                           `Randy`                           `Phoebe`                          `Cassandra`                     
``                              
```
