# StructureStructureLayoutDef

- **所属线**：世界线
- **原版实例数**：1
- **字段路径数**：11
- **资料片**：Odyssey
- **原版出处**：`Odyssey/Defs/LayoutDefs/Layouts_OrbitalPlatform.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<StructureStructureLayoutDef Name="OrbitalPlatformBase" Abstract="True">
    <workerClass>LayoutWorker_OrbitalPlatform</workerClass>
    <canHaveMultipleLayoutsInRoom>true</canHaveMultipleLayoutsInRoom>
    <corridorShapes>AsymmetricCross, H, Cross, T</corridorShapes>
    <terrainDef>OrbitalPlatform</terrainDef>
    <defaultAffordanceTerrainDef>OrbitalPlatform</defaultAffordanceTerrainDef>
    <doorStuffDef>Steel</doorStuffDef>
    <wallDef>OrbitalAncientFortifiedWall</wallDef>
    <exteriorDoorDef>AncientBlastDoor</exteriorDoorDef>
    <roomToExteriorDoorRatio>0.15</roomToExteriorDoorRatio>
    <surroundingScatterRange>2~6</surroundingScatterRange>
    <surroundingTerrainDef>OrbitalPlatform</surroundingTerrainDef>
  </StructureStructureLayoutDef>
  
  
```

> 来自 `Odyssey/Defs/LayoutDefs/Layouts_OrbitalPlatform.xml`，defName = ``，XML 节点数 12（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
canHaveMultipleLayoutsInRoom                   [布尔]  例：true
corridorShapes                                 [文本]  例：AsymmetricCross, H, Cross, T
defaultAffordanceTerrainDef                    [文本]  例：OrbitalPlatform
doorStuffDef                                   [文本]  例：Steel
exteriorDoorDef                                [文本]  例：AncientBlastDoor
roomToExteriorDoorRatio                        [数值]  例：0.15
surroundingScatterRange                        [文本]  例：2~6
surroundingTerrainDef                          [文本]  例：OrbitalPlatform
terrainDef                                     [文本]  例：OrbitalPlatform
wallDef                                        [文本]  例：OrbitalAncientFortifiedWall
workerClass                                    [文本]  例：LayoutWorker_OrbitalPlatform
```

## 三、全量字段表（11 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `canHaveMultipleLayoutsInRoom` | 100.0% (1/1) | 布尔 | true |
| `corridorShapes` | 100.0% (1/1) | 文本 | AsymmetricCross, H, Cross, T |
| `defaultAffordanceTerrainDef` | 100.0% (1/1) | 文本 | OrbitalPlatform |
| `doorStuffDef` | 100.0% (1/1) | 文本 | Steel |
| `exteriorDoorDef` | 100.0% (1/1) | 文本 | AncientBlastDoor |
| `roomToExteriorDoorRatio` | 100.0% (1/1) | 数值 | 0.15 |
| `surroundingScatterRange` | 100.0% (1/1) | 文本 | 2~6 |
| `surroundingTerrainDef` | 100.0% (1/1) | 文本 | OrbitalPlatform |
| `terrainDef` | 100.0% (1/1) | 文本 | OrbitalPlatform |
| `wallDef` | 100.0% (1/1) | 文本 | OrbitalAncientFortifiedWall |
| `workerClass` | 100.0% (1/1) | 文本 | LayoutWorker_OrbitalPlatform |

## 四、原版 defName 一览（共 1 个，列出前 60）

```text
``                              
```
