# RoomPartDef

- **所属线**：世界线
- **原版实例数**：12
- **字段路径数**：2
- **资料片**：Odyssey
- **原版出处**：`Odyssey/Defs/RoomPartDefs/RoomParts_Common.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<RoomPartDef>
    <defName>InsectHive</defName>
    <workerClass>RoomPart_InsectHive</workerClass>
  </RoomPartDef>

  
```

> 来自 `Odyssey/Defs/RoomPartDefs/RoomParts_Common.xml`，defName = `InsectHive`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Breached / DormantThreatCluster / Gore
workerClass                                    [文本]  例：RoomPart_Breached / RoomPart_DormantThreatCluster / RoomPart_Gore
```

## 三、全量字段表（2 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (12/12) | 文本 | Breached / DormantThreatCluster / Gore |
| `workerClass` | 100.0% (12/12) | 文本 | RoomPart_Breached / RoomPart_DormantThreatCluster / RoomPart_Gore |

## 四、原版 defName 一览（共 12 个，列出前 60）

```text
`InsectHive`                      `Breached`                        `Gore`                            `DormantInsectCluster`          
`DormantMechCluster`              `Corpse`                          `CenterSpace`                     `AncientEngine`                 
`SentryDrone`                     `AncientWeaponStorage`            `ConnectConduits`                 `DormantThreatCluster`          
```
