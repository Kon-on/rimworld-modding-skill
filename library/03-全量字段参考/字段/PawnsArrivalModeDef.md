# PawnsArrivalModeDef

- **所属线**：世界线
- **原版实例数**：13
- **字段路径数**：24
- **资料片**：Anomaly、Core
- **原版出处**：`Core/Defs/Misc/PawnsArrivalModeDefs/PawnsArrivalModes.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<PawnsArrivalModeDef>
    <defName>EdgeWalkInDistributed</defName>
    <workerClass>PawnsArrivalModeWorker_EdgeWalkInDistributed</workerClass>
    <selectionWeightCurve>
      <points>
        <li>(0, 0)</li>
      </points>
    </selectionWeightCurve>
    <textEnemy>A group of {0} from {1} have arrived from every direction.</textEnemy>
    <textFriendly>A group of friendly {0} from {1} have arrived from every direction.</textFriendly>
    <textWillArrive>{0_pawnsPluralDef} will arrive on foot from every direction.</textWillArrive>
    <walkIn>true</walkIn>
  </PawnsArrivalModeDef>

  
```

> 来自 `Core/Defs/Misc/PawnsArrivalModeDefs/PawnsArrivalModes.xml`，defName = `EdgeWalkInDistributed`，XML 节点数 10（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：EdgeWalkIn / EdgeWalkInDarkness / EdgeWalkInDistributedGroups
selectionWeightCurve                           [容器]
selectionWeightCurve/points                    [容器]
selectionWeightCurve/points/li                 [文本]  例：(0, 1) / (300, 0) / (300, 1.0)
textEnemy                                      [文本]  例：A group of {0} from {1} have arrived from nearby. / A group of {0} from {1} have arrived nearby. / A group of {0} have arrived from nearby.
textWillArrive                                 [文本]  例：A horde of {0} shambling, rotting corpses are about to arrive. / {0_pawnsPluralDef} will arrive in transport pods. / {0_pawnsPluralDef} will arrive on foot, approaching from several angles at once.
workerClass                                    [文本]  例：PawnsArrivalModeWorker_EdgeWalkIn / PawnsArrivalModeWorker_EdgeWalkInDarkness / PawnsArrivalModeWorker_EdgeWalkInDistributedGroups
```

## 三、全量字段表（24 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (13/13) | 文本 | EdgeWalkIn / EdgeWalkInDarkness / EdgeWalkInDistributedGroups |
| `layerBlacklist` | 7.7% (1/13) | 容器 |  |
| `layerBlacklist/li` | 7.7% (1/13) | 文本 | Orbit |
| `layerWhitelist` | 46.2% (6/13) | 容器 |  |
| `layerWhitelist/li` | 84.6% (11/13) | 文本 | Orbit / Surface |
| `minSpaceSelectionWeight` | 30.8% (4/13) | 数值 | 0.1 |
| `minTechLevel` | 38.5% (5/13) | 文本 | Industrial |
| `pointsFactorCurve` | 46.2% (6/13) | 容器 |  |
| `pointsFactorCurve/points` | 46.2% (6/13) | 容器 |  |
| `pointsFactorCurve/points/li` | 61.5% (8/13) | 文本 | (0, 1) / 0, 0.5 / 0, 0.9 |
| `selectionWeightCurve` | 100.0% (13/13) | 容器 |  |
| `selectionWeightCurve/points` | 100.0% (13/13) | 容器 |  |
| `selectionWeightCurve/points/li` | 169.2% (22/13) | 文本 | (0, 1) / (300, 0) / (300, 1.0) |
| `selectionWeightCurvesPerFaction` | 15.4% (2/13) | 容器 |  |
| `selectionWeightCurvesPerFaction/li` | 15.4% (2/13) | 容器 |  |
| `selectionWeightCurvesPerFaction/li/faction` | 15.4% (2/13) | 文本 | Mechanoid |
| `selectionWeightCurvesPerFaction/li/selectionWeightPerPointsCurve` | 15.4% (2/13) | 容器 |  |
| `selectionWeightCurvesPerFaction/li/selectionWeightPerPointsCurve/points` | 15.4% (2/13) | 容器 |  |
| `selectionWeightCurvesPerFaction/li/selectionWeightPerPointsCurve/points/li` | 30.8% (4/13) | 文本 | (1000, 1.3) / (300, 0) |
| `textEnemy` | 100.0% (13/13) | 文本 | A group of {0} from {1} have arrived from nearby. / A group of {0} from {1} have arrived nearby. / A group of  |
| `textFriendly` | 76.9% (10/13) | 文本 | A group of friendly {0} from {1} have arrived in transport pods nearby. / A group of friendly {0} from {1} hav |
| `textWillArrive` | 100.0% (13/13) | 文本 | A horde of {0} shambling, rotting corpses are about to arrive. / {0_pawnsPluralDef} will arrive in transport p |
| `walkIn` | 46.2% (6/13) | 布尔 | true |
| `workerClass` | 100.0% (13/13) | 文本 | PawnsArrivalModeWorker_EdgeWalkIn / PawnsArrivalModeWorker_EdgeWalkInDarkness / PawnsArrivalModeWorker_EdgeWal |

## 四、原版 defName 一览（共 13 个，列出前 60）

```text
`EdgeWalkInDistributed`           `EdgeWalkInHateChanters`          `EdgeWalkIn`                      `EmergeFromWater`               
`EdgeWalkInDistributedGroups`     `EdgeWalkInDarkness`              `MechClusterDrop`                 `SpecificDropDebug`             
`EdgeDrop`                        `EdgeWalkInGroups`                `EdgeDropGroups`                  `CenterDrop`                    
`RandomDrop`                    
```
