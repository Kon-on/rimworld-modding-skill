# TransportShipDef

- **所属线**：世界线
- **原版实例数**：4
- **字段路径数**：8
- **资料片**：Biotech、Odyssey、Royalty
- **原版出处**：`Biotech/Defs/TransportShipDefs/TransportShipDefs.xml`、`Odyssey/Defs/ThingDefs_Buildings/Buildings_Misc.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<TransportShipDef>
    <defName>Ship_ShuttleCrashing</defName>
    <label>crashed shuttle</label>
    <shipThing>ShuttleCrashed_Exitable</shipThing>
    <arrivingSkyfaller>ShuttleCrashing</arrivingSkyfaller>
  </TransportShipDef>

  
```

> 来自 `Biotech/Defs/TransportShipDefs/TransportShipDefs.xml`，defName = `Ship_ShuttleCrashing`，XML 节点数 5（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
arrivingSkyfaller                              [文本]  例：PassengerShuttleIncoming / ShuttleCrashing / ShuttleCrashing_Mechanitor
defName                                        [文本]  例：Ship_PassengerShuttle / Ship_Shuttle / Ship_ShuttleCrashing
label                                          [文本]  例：crashed mechanitor ship / crashed shuttle / passenger shuttle
shipThing                                      [文本]  例：PassengerShuttle / Shuttle / ShuttleCrashed_Exitable
```

## 三、全量字段表（8 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `arrivingSkyfaller` | 100.0% (4/4) | 文本 | PassengerShuttleIncoming / ShuttleCrashing / ShuttleCrashing_Mechanitor |
| `defName` | 100.0% (4/4) | 文本 | Ship_PassengerShuttle / Ship_Shuttle / Ship_ShuttleCrashing |
| `label` | 100.0% (4/4) | 文本 | crashed mechanitor ship / crashed shuttle / passenger shuttle |
| `leavingSkyfaller` | 50.0% (2/4) | 文本 | PassengerShuttleLeaving / ShuttleLeaving |
| `maxLaunchDistance` | 25.0% (1/4) | 数值 | 70 |
| `playerShuttle` | 25.0% (1/4) | 布尔 | true |
| `shipThing` | 100.0% (4/4) | 文本 | PassengerShuttle / Shuttle / ShuttleCrashed_Exitable |
| `worldObject` | 50.0% (2/4) | 文本 | PassengerShuttle / TravelingShuttle |

## 四、原版 defName 一览（共 4 个，列出前 60）

```text
`Ship_ShuttleCrashing`            `Ship_ShuttleCrashing_Mechanitor`  `Ship_PassengerShuttle`           `Ship_Shuttle`                  
```
