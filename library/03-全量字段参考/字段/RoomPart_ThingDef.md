# RoomPart_ThingDef

- **所属线**：世界线
- **原版实例数**：6
- **字段路径数**：3
- **资料片**：Odyssey
- **原版出处**：`Odyssey/Defs/RoomPartDefs/RoomParts_Common.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<RoomPart_ThingDef>
    <defName>CornerArmoredTurret</defName>
    <workerClass>RoomPart_CornerThing</workerClass>
    <thingDef>Turret_AncientArmoredTurret</thingDef>
  </RoomPart_ThingDef>

  
```

> 来自 `Odyssey/Defs/RoomPartDefs/RoomParts_Common.xml`，defName = `CornerArmoredTurret`，XML 节点数 4（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：CornerArmoredTurret / CornerMechPylon / CornerMiniTurret
thingDef                                       [文本]  例：HunterDroneTrap / MechPylon / Turret_AncientArmoredTurret
workerClass                                    [文本]  例：RoomPart_CornerThing / RoomPart_FillPadding
```

## 三、全量字段表（3 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (6/6) | 文本 | CornerArmoredTurret / CornerMechPylon / CornerMiniTurret |
| `thingDef` | 100.0% (6/6) | 文本 | HunterDroneTrap / MechPylon / Turret_AncientArmoredTurret |
| `workerClass` | 100.0% (6/6) | 文本 | RoomPart_CornerThing / RoomPart_FillPadding |

## 四、原版 defName 一览（共 6 个，列出前 60）

```text
`CornerArmoredTurret`             `CornerMechPylon`                 `CornerMiniTurret`                `HunterDrone`                   
`WaspDrone`                       `ExplosiveCrate`                
```
