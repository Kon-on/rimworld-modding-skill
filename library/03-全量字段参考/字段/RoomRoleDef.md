# RoomRoleDef

- **所属线**：世界线
- **原版实例数**：23
- **字段路径数**：6
- **资料片**：Anomaly、Biotech、Core、Ideology、Royalty
- **原版出处**：`Anomaly/Defs/Rooms/RoomRoles.xml`、`Core/Defs/Rooms/RoomRoles.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<RoomRoleDef>
    <defName>ContainmentCell</defName>
    <label>containment cell</label>
    <workerClass>RoomRoleWorker_ContainmentCell</workerClass>
  </RoomRoleDef>
  
  
```

> 来自 `Anomaly/Defs/Rooms/RoomRoles.xml`，defName = `ContainmentCell`，XML 节点数 4（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：CeremonialChamber / ContainmentCell / Nursery
label                                          [文本]  例：ceremonial chamber / containment cell / nursery
relatedStats/li                                [文本]  例：Beauty / Cleanliness / Space
workerClass                                    [文本]  例：RoomRoleWorker_CeremonialChamber / RoomRoleWorker_ContainmentCell / RoomRoleWorker_Nursery
```

## 三、全量字段表（6 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `avoidViewingArtIfUnowned` | 21.7% (5/23) | 布尔 | true |
| `defName` | 100.0% (23/23) | 文本 | CeremonialChamber / ContainmentCell / Nursery |
| `label` | 100.0% (23/23) | 文本 | ceremonial chamber / containment cell / nursery |
| `relatedStats` | 43.5% (10/23) | 容器 |  |
| `relatedStats/li` | 156.5% (36/23) | 文本 | Beauty / Cleanliness / Space |
| `workerClass` | 100.0% (23/23) | 文本 | RoomRoleWorker_CeremonialChamber / RoomRoleWorker_ContainmentCell / RoomRoleWorker_Nursery |

## 四、原版 defName 一览（共 23 个，列出前 60）

```text
`ContainmentCell`                 `CeremonialChamber`               `Nursery`                         `Playroom`                      
`Classroom`                       `DeathrestChamber`                `None`                            `Room`                          
`Workshop`                        `Storeroom`                       `Tomb`                            `Barn`                          
`WorshipRoom`                     `Laboratory`                      `Kitchen`                         `ThroneRoom`                    
`Hospital`                        `DiningRoom`                      `RecRoom`                         `Bedroom`                       
`PrisonCell`                      `Barracks`                        `PrisonBarracks`                
```
