# RitualTargetFilterDef

- **所属线**：理念线
- **原版实例数**：7
- **字段路径数**：4
- **资料片**：Ideology、Royalty
- **原版出处**：`Ideology/Defs/Rituals/Ritual_Targets.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<RitualTargetFilterDef>
    <defName>Altar</defName>
    <workerClass>RitualTargetFilter_IdeoBuilding</workerClass>
  </RitualTargetFilterDef>

  
```

> 来自 `Ideology/Defs/Rituals/Ritual_Targets.xml`，defName = `Altar`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Altar / AltarOrRitualSpot / IdeoBuilding
workerClass                                    [文本]  例：RitualTargetFilter_Altar / RitualTargetFilter_AltarOrIdeogram / RitualTargetFilter_IdeoBuilding
```

## 三、全量字段表（4 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (7/7) | 文本 | Altar / AltarOrRitualSpot / IdeoBuilding |
| `fallBackToGatherSpot` | 28.6% (2/7) | 布尔 | true |
| `fallbackToRitualSpot` | 28.6% (2/7) | 布尔 | true |
| `workerClass` | 100.0% (7/7) | 文本 | RitualTargetFilter_Altar / RitualTargetFilter_AltarOrIdeogram / RitualTargetFilter_IdeoBuilding |

## 四、原版 defName 一览（共 7 个，列出前 60）

```text
`Altar`                           `UsableThrone`                    `SelectedThing`                   `IdeoBuilding`                  
`IdeoBuildingOrRitualSpot`        `AltarOrRitualSpot`               `AltarIdeogramOrRitualSpot`     
```
