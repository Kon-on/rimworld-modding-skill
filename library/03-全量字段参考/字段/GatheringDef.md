# GatheringDef

- **所属线**：理念线
- **原版实例数**：3
- **字段路径数**：14
- **资料片**：Core、Royalty
- **原版出处**：`Core/Defs/GatheringDefs/Gatherings.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<GatheringDef>
    <defName>MarriageCeremony</defName>
    <label>marriage ceremony</label>
    <respectTimetable>false</respectTimetable>
    <workerClass>GatheringWorker_MarriageCeremony</workerClass>
  </GatheringDef>
```

> 来自 `Core/Defs/GatheringDefs/Gatherings.xml`，defName = `MarriageCeremony`，XML 节点数 5（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Concert / MarriageCeremony / Party
label                                          [文本]  例：concert / marriage ceremony / party
requiredTitleAny/li                            [文本]  例：Baron / Count / Knight
workerClass                                    [文本]  例：GatheringWorker_Concert / GatheringWorker_MarriageCeremony / GatheringWorker_Party
```

## 三、全量字段表（14 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `calledOffMessage` | 66.7% (2/3) | 文本 | The concert has been cancelled. / The party has been called off. |
| `defName` | 100.0% (3/3) | 文本 | Concert / MarriageCeremony / Party |
| `duty` | 66.7% (2/3) | 文本 | Concert / Party |
| `finishedMessage` | 66.7% (2/3) | 文本 | The concert has concluded. / The party has finished. |
| `gatherSpotDefs` | 33.3% (1/3) | 容器 |  |
| `gatherSpotDefs/li` | 33.3% (1/3) | 文本 | PartySpot |
| `label` | 100.0% (3/3) | 文本 | concert / marriage ceremony / party |
| `letterText` | 66.7% (2/3) | 文本 | {ORGANIZER_labelShort} is holding a concert! Everyone who goes will gain recreat / {ORGANIZER_labelShort} is t |
| `letterTitle` | 66.7% (2/3) | 文本 | Concert / Party |
| `randomSelectionWeight` | 66.7% (2/3) | 数值 | 1 |
| `requiredTitleAny` | 33.3% (1/3) | 容器 |  |
| `requiredTitleAny/li` | 133.3% (4/3) | 文本 | Baron / Count / Knight |
| `respectTimetable` | 33.3% (1/3) | 布尔 | false |
| `workerClass` | 100.0% (3/3) | 文本 | GatheringWorker_Concert / GatheringWorker_MarriageCeremony / GatheringWorker_Party |

## 四、原版 defName 一览（共 3 个，列出前 60）

```text
`MarriageCeremony`                `Party`                           `Concert`                       
```
