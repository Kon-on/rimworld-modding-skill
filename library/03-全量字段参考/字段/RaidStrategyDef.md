# RaidStrategyDef

- **所属线**：世界线
- **原版实例数**：12
- **字段路径数**：25
- **资料片**：Anomaly、Core
- **原版出处**：`Core/Defs/Storyteller/RaidStrategies_Basic.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<RaidStrategyDef ParentName="ImmediateAttack">
    <defName>ImmediateAttackFriendly</defName>
    <workerClass>RaidStrategyWorker_ImmediateAttackFriendly</workerClass>
    <pawnsCanBringFood>True</pawnsCanBringFood>
  </RaidStrategyDef>

  
```

> 来自 `Core/Defs/Storyteller/RaidStrategies_Basic.xml`，defName = `ImmediateAttackFriendly`，XML 节点数 4（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
arriveModes/li                                 [文本]  例：CenterDrop / EdgeDrop / EdgeWalkIn
defName                                        [文本]  例：ImmediateAttack / ImmediateAttackFriendly / PsychicRitualSiege
pointsFactorCurve/points/li                    [文本]  例：(0, 0.7) / (0, 1) / (5000, 0.5)
selectionWeightPerPointsCurve/points/li        [文本]  例：(0, 0) / (0, 1) / (0,0)
workerClass                                    [文本]  例：RaidStrategyWorker_ImmediateAttack / RaidStrategyWorker_ImmediateAttackFriendly / RaidStrategyWorker_PsychicRitualSiege
```

## 三、全量字段表（25 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `arrivalTextEnemy` | 83.3% (10/12) | 文本 | Some unnatural force is animating these lifeless corpses. They are intent on att / They are attacking immediat |
| `arrivalTextFriendly` | 50.0% (6/12) | 文本 | It looks like they want to use siege tactics to help you. / They are moving in to help you immediately. / They |
| `arriveModes` | 75.0% (9/12) | 容器 |  |
| `arriveModes/li` | 225.0% (27/12) | 文本 | CenterDrop / EdgeDrop / EdgeWalkIn |
| `defName` | 91.7% (11/12) | 文本 | ImmediateAttack / ImmediateAttackFriendly / PsychicRitualSiege |
| `layerWhitelist` | 8.3% (1/12) | 容器 |  |
| `layerWhitelist/li` | 8.3% (1/12) | 文本 | Surface |
| `letterLabelEnemy` | 75.0% (9/12) | 文本 | Raid / Raid: Horax cultists / Shambler assault |
| `letterLabelFriendly` | 50.0% (6/12) | 文本 | Friendlies |
| `minPawns` | 16.7% (2/12) | 数值 | 2 / 4 |
| `pawnsCanBringFood` | 16.7% (2/12) | 布尔 | True / true |
| `pointsFactorCurve` | 75.0% (9/12) | 容器 |  |
| `pointsFactorCurve/points` | 75.0% (9/12) | 容器 |  |
| `pointsFactorCurve/points/li` | 116.7% (14/12) | 文本 | (0, 0.7) / (0, 1) / (5000, 0.5) |
| `raidLootValueFactor` | 8.3% (1/12) | 数值 | 0 |
| `selectionWeightCurvesPerFaction` | 33.3% (4/12) | 容器 |  |
| `selectionWeightCurvesPerFaction/li` | 33.3% (4/12) | 容器 |  |
| `selectionWeightCurvesPerFaction/li/faction` | 33.3% (4/12) | 文本 | Mechanoid |
| `selectionWeightCurvesPerFaction/li/selectionWeightPerPointsCurve` | 33.3% (4/12) | 容器 |  |
| `selectionWeightCurvesPerFaction/li/selectionWeightPerPointsCurve/points` | 33.3% (4/12) | 容器 |  |
| `selectionWeightCurvesPerFaction/li/selectionWeightPerPointsCurve/points/li` | 50.0% (6/12) | 文本 | (0, 0) / (0, 1) / (1000, 0.25) |
| `selectionWeightPerPointsCurve` | 75.0% (9/12) | 容器 |  |
| `selectionWeightPerPointsCurve/points` | 75.0% (9/12) | 容器 |  |
| `selectionWeightPerPointsCurve/points/li` | 108.3% (13/12) | 文本 | (0, 0) / (0, 1) / (0,0) |
| `workerClass` | 91.7% (11/12) | 文本 | RaidStrategyWorker_ImmediateAttack / RaidStrategyWorker_ImmediateAttackFriendly / RaidStrategyWorker_PsychicRi |

## 四、原版 defName 一览（共 12 个，列出前 60）

```text
`ImmediateAttackFriendly`         `ImmediateAttackBreaching`        `ImmediateAttackBreachingSmart`   `ShamblerAssault`               
`PsychicRitualSiege`              `ImmediateAttackSappers`          `ImmediateAttackSmart`            `EmergeFromWater`               
`Siege`                           ``                                `StageThenAttack`                 `ImmediateAttack`               
```
