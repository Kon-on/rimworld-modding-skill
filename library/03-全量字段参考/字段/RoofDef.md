# RoofDef

- **所属线**：世界线
- **原版实例数**：4
- **字段路径数**：8
- **资料片**：Anomaly、Core
- **原版出处**：`Core/Defs/Misc/RoofDefs/Roofs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<RoofDef>
    <defName>RoofConstructed</defName>
    <label>constructed roof</label>
    <isThickRoof>false</isThickRoof>
    <filthLeaving>Filth_RubbleBuilding</filthLeaving>
    <soundPunchThrough>PunchThroughRoofMetal</soundPunchThrough>
  </RoofDef>


  
```

> 来自 `Core/Defs/Misc/RoofDefs/Roofs.xml`，defName = `RoofConstructed`，XML 节点数 6（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：RoofConstructed / RoofRockThick / RoofRockThin
filthLeaving                                   [文本]  例：Filth_RubbleBuilding / Filth_RubbleRock
isThickRoof                                    [布尔]  例：false / true
label                                          [文本]  例：constructed roof / overhead mountain / rock roof (thin)
```

## 三、全量字段表（8 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `canCollapse` | 25.0% (1/4) | 布尔 | false |
| `collapseLeavingThingDef` | 25.0% (1/4) | 文本 | CollapsedRocks |
| `defName` | 100.0% (4/4) | 文本 | RoofConstructed / RoofRockThick / RoofRockThin |
| `filthLeaving` | 100.0% (4/4) | 文本 | Filth_RubbleBuilding / Filth_RubbleRock |
| `isNatural` | 75.0% (3/4) | 布尔 | true |
| `isThickRoof` | 100.0% (4/4) | 布尔 | false / true |
| `label` | 100.0% (4/4) | 文本 | constructed roof / overhead mountain / rock roof (thin) |
| `soundPunchThrough` | 50.0% (2/4) | 文本 | PunchThroughRoofMetal / Roof_Collapse |

## 四、原版 defName 一览（共 4 个，列出前 60）

```text
`RoofConstructed`                 `VoidmetalRoof`                   `RoofRockThin`                    `RoofRockThick`                 
```
