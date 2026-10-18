# RitualObligationTargetFilterDef

- **所属线**：理念线
- **原版实例数**：21
- **字段路径数**：9
- **资料片**：Biotech、Ideology、Odyssey、Royalty
- **原版出处**：`Biotech/Defs/Rituals/Ritual_Targets.xml`、`Ideology/Defs/Rituals/Ritual_Targets.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<RitualObligationTargetFilterDef>
    <defName>ChildBirth</defName>
    <workerClass>RitualObligationTargetWorker_ChildBirth</workerClass>
  </RitualObligationTargetFilterDef>
```

> 来自 `Biotech/Defs/Rituals/Ritual_Targets.xml`，defName = `ChildBirth`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：AnyEmptyGrave / ChildBirth / GatheringSpot
workerClass                                    [文本]  例：RitualObligationTargetWorker_AnyEmptyGrave / RitualObligationTargetWorker_AnyGatherSpot / RitualObligationTargetWorker_ChildBirth
```

## 三、全量字段表（9 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (21/21) | 文本 | AnyEmptyGrave / ChildBirth / GatheringSpot |
| `maxDrumDistance` | 4.8% (1/21) | 数值 | 12 |
| `maxSpeakerDistance` | 4.8% (1/21) | 数值 | 12 |
| `minUnroofedCells` | 4.8% (1/21) | 数值 | 25 |
| `thingDefs` | 28.6% (6/21) | 容器 |  |
| `thingDefs/li` | 52.4% (11/21) | 文本 | Campfire / ChristmasTree / LightBall |
| `unroofedCellSearchRadius` | 4.8% (1/21) | 数值 | 12 |
| `woodPerParticipant` | 4.8% (1/21) | 数值 | 4 |
| `workerClass` | 100.0% (21/21) | 文本 | RitualObligationTargetWorker_AnyEmptyGrave / RitualObligationTargetWorker_AnyGatherSpot / RitualObligationTarg |

## 四、原版 defName 一览（共 21 个，列出前 60）

```text
`ChildBirth`                      `GraveWithTargetsCorpse`          `AnyEmptyGrave`                   `GatheringSpot`                 
`GatheringSpotOrAltar`            `RitualSpotOrAltar`               `AnyRitualSpot`                   `AnyIdeoBuildingOrRitualSpot`   
`RitualSpotIdeogramOrAltar`       `RitualSpotOrAltar_Scarification`  `RitualSpotOrAltar_Blinding`      `GauranlenTree`                 
`GravshipLaunch`                  `AnimaTree`                       `ChristmasTree`                   `FeastCannibal`                 
`CampfireSkylanterns`             `SmokeCircle`                     `LightBall`                       `RitualSpotOrCampfireParty`     
`BurnTargets`                   
```
