# MapGeneratorDef

- **所属线**：世界线
- **原版实例数**：20
- **字段路径数**：24
- **资料片**：Anomaly、Core、Ideology、Odyssey
- **原版出处**：`Ideology/Defs/MapGeneration/BasePlayerMapGenerator.xml`、`Odyssey/Defs/MapGeneration/SpaceMapGenerator.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<MapGeneratorDef ParentName="Base_Player">
    <defName>BasePlayer_SecondArchonexusCycle</defName>
    <genSteps>
      <li>ArchonexusResearchBuildings_SecondCycle</li>
    </genSteps>
  </MapGeneratorDef>

  
```

> 来自 `Ideology/Defs/MapGeneration/BasePlayerMapGenerator.xml`，defName = `BasePlayer_SecondArchonexusCycle`，XML 节点数 4（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Base_Faction / Labyrinth / MetalHell
genSteps                                       [容器]
genSteps/li                                    [文本]  例：ElevationFertility / Labyrinth / MetalHell
```

## 三、全量字段表（24 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `customMapComponents` | 10.0% (2/20) | 容器 |  |
| `customMapComponents/li` | 10.0% (2/20) | 文本 | LabyrinthMapComponent / UndercaveMapComponent |
| `defaultUnderGridTerrain` | 5.0% (1/20) | 文本 | Space |
| `defeatRequiresCantReachUnfogged` | 5.0% (1/20) | 布尔 | false |
| `defName` | 95.0% (19/20) | 文本 | Base_Faction / Labyrinth / MetalHell |
| `disableCallAid` | 30.0% (6/20) | 布尔 | true |
| `disableMapClippers` | 5.0% (1/20) | 布尔 | true |
| `disableShadows` | 5.0% (1/20) | 布尔 | true |
| `forceCaves` | 10.0% (2/20) | 布尔 | true |
| `genSteps` | 95.0% (19/20) | 容器 |  |
| `genSteps/li` | 555.0% (111/20) | 文本 | ElevationFertility / Labyrinth / MetalHell |
| `ignoreAreaRevealedLetter` | 20.0% (4/20) | 布尔 | true |
| `isUnderground` | 20.0% (4/20) | 布尔 | true |
| `label` | 60.0% (12/20) | 文本 | ancient stockpile / labyrinth / metal hell |
| `pocketMapProperties` | 30.0% (6/20) | 容器 |  |
| `pocketMapProperties/biome` | 30.0% (6/20) | 文本 | Labyrinth / MetalHell / Undercave |
| `pocketMapProperties/canBeCleaned` | 5.0% (1/20) | 布尔 | true |
| `pocketMapProperties/canLaunchGravship` | 5.0% (1/20) | 布尔 | true |
| `pocketMapProperties/temperature` | 30.0% (6/20) | 数值 | -75 / 15 / 25 |
| `pocketMapProperties/tileMutators` | 10.0% (2/20) | 容器 |  |
| `pocketMapProperties/tileMutators/li` | 10.0% (2/20) | 文本 | UndergroundCave |
| `renderWorld` | 5.0% (1/20) | 布尔 | true |
| `roofDef` | 5.0% (1/20) | 文本 | VoidmetalRoof |
| `validScenarioMap` | 5.0% (1/20) | 布尔 | true |

## 四、原版 defName 一览（共 20 个，列出前 60）

```text
`BasePlayer_SecondArchonexusCycle`  `BasePlayer_ThirdArchonexusCycle`  `Encounter`                       `EscapeShip`                    
`Base_Faction`                    `SpacePocket`                     `SettlementPlatform`              `OrbitalRelay`                  
`Mechhive`                        `Asteroid`                        `OrbitalItemStash`                `Base_Player`                   
`MetalHell`                       `Space`                           `AsteroidBasic`                   `Labyrinth`                     
`AncientStockpile`                `InsectLair`                      ``                                `Undercave`                     
```
