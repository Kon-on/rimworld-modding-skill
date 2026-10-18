# LayoutDef

- **所属线**：世界线
- **原版实例数**：1
- **字段路径数**：25
- **资料片**：Anomaly
- **原版出处**：`Anomaly/Defs/LayoutDefs/Layouts_Misc.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<LayoutDef>
    <defName>Labyrinth</defName>
    <workerClass>LayoutWorker_Labyrinth</workerClass>
    <canHaveMultipleLayoutsInRoom>true</canHaveMultipleLayoutsInRoom>
    <multipleLayoutRoomChance>0.15</multipleLayoutRoomChance>
    <noRoof>true</noRoof>
    <roomDefs>
      <LabyrinthObelisk/>
      <LabyrinthEmpty>0.15</LabyrinthEmpty>
      <LabyrinthEndlessPit>0.1</LabyrinthEndlessPit>
      <LabyrinthFloorEtchings>0.15</LabyrinthFloorEtchings>
      <LabyrinthDeadBody>0.05</LabyrinthDeadBody>
      <LabyrinthCorpseRoom>0.01</LabyrinthCorpseRoom>
      <LabyrinthStatueDeadlife>0.025</LabyrinthStatueDeadlife>
      <LabyrinthStatueTeleporter>0.025</LabyrinthStatueTeleporter>
      <LabyrinthSleepingFleshbeast>0.05</LabyrinthSleepingFleshbeast>
      <LabyrinthAbandonedCamp>0.02</LabyrinthAbandonedCamp>
      <LabyrinthAnimalCorpses>0.01</LabyrinthAnimalCorpses>
      <LabyrinthHarbinger>0.01</LabyrinthHarbinger>
      <LabyrinthTrees>0.03</LabyrinthTrees>
      <LabyrinthAnimals>0.0075</LabyrinthAnimals>
      <LabyrinthGrayBox>0.05</LabyrinthGrayBox>
      <LabyrinthLargeGrayBox>0.025</LabyrinthLargeGrayBox>
      <LabyrinthLargeEmptyGrayBox>0.025</LabyrinthLargeEmptyGrayBox>
      <LabyrinthFloorRamblings>0.05</LabyrinthFloorRamblings>
      <LabyrinthChildRoom MayRequire="Ludeon.RimWorld.Biotech">0.01</LabyrinthChildRoom>
    </roomDefs>
  </LayoutDef>
  
```

> 来自 `Anomaly/Defs/LayoutDefs/Layouts_Misc.xml`，defName = `Labyrinth`，XML 节点数 26（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
canHaveMultipleLayoutsInRoom                   [布尔]  例：true
defName                                        [文本]  例：Labyrinth
multipleLayoutRoomChance                       [数值]  例：0.15
noRoof                                         [布尔]  例：true
roomDefs                                       [容器]
roomDefs/LabyrinthAbandonedCamp                [数值]  例：0.02
roomDefs/LabyrinthAnimalCorpses                [数值]  例：0.01
roomDefs/LabyrinthAnimals                      [数值]  例：0.0075
roomDefs/LabyrinthChildRoom                    [数值]  例：0.01
roomDefs/LabyrinthCorpseRoom                   [数值]  例：0.01
roomDefs/LabyrinthDeadBody                     [数值]  例：0.05
roomDefs/LabyrinthEmpty                        [数值]  例：0.15
roomDefs/LabyrinthEndlessPit                   [数值]  例：0.1
roomDefs/LabyrinthFloorEtchings                [数值]  例：0.15
roomDefs/LabyrinthFloorRamblings               [数值]  例：0.05
roomDefs/LabyrinthGrayBox                      [数值]  例：0.05
roomDefs/LabyrinthHarbinger                    [数值]  例：0.01
roomDefs/LabyrinthLargeEmptyGrayBox            [数值]  例：0.025
roomDefs/LabyrinthLargeGrayBox                 [数值]  例：0.025
roomDefs/LabyrinthObelisk                      [容器]
roomDefs/LabyrinthSleepingFleshbeast           [数值]  例：0.05
roomDefs/LabyrinthStatueDeadlife               [数值]  例：0.025
roomDefs/LabyrinthStatueTeleporter             [数值]  例：0.025
roomDefs/LabyrinthTrees                        [数值]  例：0.03
workerClass                                    [文本]  例：LayoutWorker_Labyrinth
```

## 三、全量字段表（25 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `canHaveMultipleLayoutsInRoom` | 100.0% (1/1) | 布尔 | true |
| `defName` | 100.0% (1/1) | 文本 | Labyrinth |
| `multipleLayoutRoomChance` | 100.0% (1/1) | 数值 | 0.15 |
| `noRoof` | 100.0% (1/1) | 布尔 | true |
| `roomDefs` | 100.0% (1/1) | 容器 |  |
| `roomDefs/LabyrinthAbandonedCamp` | 100.0% (1/1) | 数值 | 0.02 |
| `roomDefs/LabyrinthAnimalCorpses` | 100.0% (1/1) | 数值 | 0.01 |
| `roomDefs/LabyrinthAnimals` | 100.0% (1/1) | 数值 | 0.0075 |
| `roomDefs/LabyrinthChildRoom` | 100.0% (1/1) | 数值 | 0.01 |
| `roomDefs/LabyrinthCorpseRoom` | 100.0% (1/1) | 数值 | 0.01 |
| `roomDefs/LabyrinthDeadBody` | 100.0% (1/1) | 数值 | 0.05 |
| `roomDefs/LabyrinthEmpty` | 100.0% (1/1) | 数值 | 0.15 |
| `roomDefs/LabyrinthEndlessPit` | 100.0% (1/1) | 数值 | 0.1 |
| `roomDefs/LabyrinthFloorEtchings` | 100.0% (1/1) | 数值 | 0.15 |
| `roomDefs/LabyrinthFloorRamblings` | 100.0% (1/1) | 数值 | 0.05 |
| `roomDefs/LabyrinthGrayBox` | 100.0% (1/1) | 数值 | 0.05 |
| `roomDefs/LabyrinthHarbinger` | 100.0% (1/1) | 数值 | 0.01 |
| `roomDefs/LabyrinthLargeEmptyGrayBox` | 100.0% (1/1) | 数值 | 0.025 |
| `roomDefs/LabyrinthLargeGrayBox` | 100.0% (1/1) | 数值 | 0.025 |
| `roomDefs/LabyrinthObelisk` | 100.0% (1/1) | 容器 |  |
| `roomDefs/LabyrinthSleepingFleshbeast` | 100.0% (1/1) | 数值 | 0.05 |
| `roomDefs/LabyrinthStatueDeadlife` | 100.0% (1/1) | 数值 | 0.025 |
| `roomDefs/LabyrinthStatueTeleporter` | 100.0% (1/1) | 数值 | 0.025 |
| `roomDefs/LabyrinthTrees` | 100.0% (1/1) | 数值 | 0.03 |
| `workerClass` | 100.0% (1/1) | 文本 | LayoutWorker_Labyrinth |

## 四、原版 defName 一览（共 1 个，列出前 60）

```text
`Labyrinth`                     
```
