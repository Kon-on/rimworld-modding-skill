# FeatureDef

- **所属线**：世界线
- **原版实例数**：25
- **字段路径数**：17
- **资料片**：Core、Odyssey
- **原版出处**：`Core/Defs/Misc/FeatureDefs/Features.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<FeatureDef>
    <defName>OuterOcean</defName>
    <workerClass>FeatureWorker_OuterOcean</workerClass>
    <order>150</order>
    <minSize>15</minSize>
    <nameMaker>NamerOcean</nameMaker>
  </FeatureDef>

  
```

> 来自 `Core/Defs/Misc/FeatureDefs/Features.xml`，defName = `OuterOcean`，XML 节点数 6（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
acceptableBiomes/li                            [文本]  例：AridShrubland / ColdBog / LavaField
defName                                        [文本]  例：Archipelago / Bay / Island
nameMaker                                      [文本]  例：NamerArchipelago / NamerBay / NamerIsland
order                                          [数值]  例：10 / 100 / 20
rootBiomes/li                                  [文本]  例：Desert / ExtremeDesert / Lake
workerClass                                    [文本]  例：FeatureWorker_Archipelago / FeatureWorker_Bay / FeatureWorker_Island
```

## 三、全量字段表（17 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `acceptableBiomes` | 40.0% (10/25) | 容器 |  |
| `acceptableBiomes/li` | 128.0% (32/25) | 文本 | AridShrubland / ColdBog / LavaField |
| `canTouchWorldEdge` | 8.0% (2/25) | 布尔 | false |
| `defName` | 100.0% (25/25) | 文本 | Archipelago / Bay / Island |
| `maxPassageWidth` | 4.0% (1/25) | 数值 | 12 |
| `maxPctOfWholeArea` | 4.0% (1/25) | 数值 | 0.5 |
| `maxRootGroupSize` | 4.0% (1/25) | 数值 | 75 |
| `maxSize` | 16.0% (4/25) | 数值 | 1500 / 350 / 400 |
| `maxSpaceBetweenRootGroups` | 4.0% (1/25) | 数值 | 1 |
| `minRootGroupsInCluster` | 4.0% (1/25) | 数值 | 1 |
| `minRootGroupSize` | 24.0% (6/25) | 数值 | 12 / 3 / 6 |
| `minSize` | 36.0% (9/25) | 数值 | 15 / 3 / 30 |
| `nameMaker` | 100.0% (25/25) | 文本 | NamerArchipelago / NamerBay / NamerIsland |
| `order` | 100.0% (25/25) | 数值 | 10 / 100 / 20 |
| `rootBiomes` | 76.0% (19/25) | 容器 |  |
| `rootBiomes/li` | 92.0% (23/25) | 文本 | Desert / ExtremeDesert / Lake |
| `workerClass` | 100.0% (25/25) | 文本 | FeatureWorker_Archipelago / FeatureWorker_Bay / FeatureWorker_Island |

## 四、原版 defName 一览（共 25 个，列出前 60）

```text
`OuterOcean`                      `Island`                          `Archipelago`                     `Peninsula`                     
`Grasslands`                      `Lake`                            `Ocean`                           `Scarlands`                     
`LavaField`                       `GlacialPlain`                    `Glowforest`                      `Bay`                           
`MountainRange`                   `OceanBay`                        `Sea`                             `Desert`                        
`TemperateSwamp`                  `TropicalSwamp`                   `ColdBog`                         `BorealForest`                  
`IceSheet`                        `TropicalRainforest`              `Tundra`                          `TemperateForest`               
`AridShrubland`                 
```
