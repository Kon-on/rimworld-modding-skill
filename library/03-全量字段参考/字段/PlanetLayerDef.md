# PlanetLayerDef

- **所属线**：世界线
- **原版实例数**：3
- **字段路径数**：35
- **资料片**：Core、Odyssey
- **原版出处**：`Odyssey/Defs/PlanetLayerDefs/PlanetLayers.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<PlanetLayerDef ParentName="OrbitLayer">
    <defName>Orbit</defName>
    <label>orbit</label>
    <viewGizmoTooltip>View locations that are orbiting the planet.</viewGizmoTooltip>
    <elevationString>200km</elevationString>
    <defaultBiome>Orbit</defaultBiome>
    <rangeDistanceFactor>20</rangeDistanceFactor>
  </PlanetLayerDef>
  
  
```

> 来自 `Odyssey/Defs/PlanetLayerDefs/PlanetLayers.xml`，defName = `Orbit`，XML 节点数 7（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
elevationString                                [文本]  例：200km / {0}m
viewAngleSettlementsFactorCurve/points/li      [文本]  例：(0, 1) / (0.3, 1) / (0.5, 0.75)
worldDrawLayers/li                             [文本]  例：WorldDrawLayer_CurrentMapTile / WorldDrawLayer_MouseTile / WorldDrawLayer_SelectedTile
worldGenSteps/li                               [文本]  例：Lakes / Mutators / Rivers
worldTabs/li                                   [文本]  例：WITab_Orbit / WITab_Planet / WITab_Terrain
```

## 三、全量字段表（35 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `alwaysRaycastable` | 33.3% (1/3) | 布尔 | false |
| `backgroundBiome` | 33.3% (1/3) | 文本 | Ocean |
| `canFormCaravans` | 33.3% (1/3) | 布尔 | false |
| `defaultBiome` | 66.7% (2/3) | 文本 | Orbit / Space |
| `defaultMapWorldObject` | 33.3% (1/3) | 文本 | Space |
| `defName` | 66.7% (2/3) | 文本 | Orbit / Surface |
| `destroyedSettlementWorldObjectDef` | 33.3% (1/3) | 文本 | DestroyedSpaceSettlement |
| `elevationString` | 100.0% (3/3) | 文本 | 200km / {0}m |
| `gerundLabel` | 66.7% (2/3) | 文本 | in / on the |
| `ignoreNoBuildArea` | 33.3% (1/3) | 布尔 | true |
| `isSpace` | 33.3% (1/3) | 布尔 | true |
| `label` | 66.7% (2/3) | 文本 | orbit / planet |
| `layerType` | 66.7% (2/3) | 文本 | OrbitLayer / SurfaceLayer |
| `lineWidthFactor` | 33.3% (1/3) | 数值 | 7.5 |
| `obstructsExpandingIcons` | 33.3% (1/3) | 布尔 | false |
| `onlyAllowWhitelistedArrivalModes` | 33.3% (1/3) | 布尔 | true |
| `onlyAllowWhitelistedArrivals` | 33.3% (1/3) | 布尔 | true |
| `onlyAllowWhitelistedGameConditions` | 33.3% (1/3) | 布尔 | true |
| `onlyAllowWhitelistedIncidents` | 33.3% (1/3) | 布尔 | true |
| `raidPointsFactor` | 33.3% (1/3) | 数值 | 0.85 |
| `rangeDistanceFactor` | 33.3% (1/3) | 数值 | 20 |
| `settlementsPer100kTiles` | 33.3% (1/3) | 文本 | 1000~1000 |
| `settlementWorldObjectDef` | 33.3% (1/3) | 文本 | SpaceSettlement |
| `tileType` | 33.3% (1/3) | 文本 | SurfaceTile |
| `viewAngleSettlementsFactorCurve` | 33.3% (1/3) | 容器 |  |
| `viewAngleSettlementsFactorCurve/points` | 33.3% (1/3) | 容器 |  |
| `viewAngleSettlementsFactorCurve/points/li` | 133.3% (4/3) | 文本 | (0, 1) / (0.3, 1) / (0.5, 0.75) |
| `viewGizmoTexPath` | 66.7% (2/3) | 文本 | UI/Commands/ViewOrbit / UI/Commands/ViewPlanet |
| `viewGizmoTooltip` | 66.7% (2/3) | 文本 | View locations that are on the surface. / View locations that are orbiting the planet. |
| `worldDrawLayers` | 66.7% (2/3) | 容器 |  |
| `worldDrawLayers/li` | 600.0% (18/3) | 文本 | WorldDrawLayer_CurrentMapTile / WorldDrawLayer_MouseTile / WorldDrawLayer_SelectedTile |
| `worldGenSteps` | 66.7% (2/3) | 容器 |  |
| `worldGenSteps/li` | 433.3% (13/3) | 文本 | Lakes / Mutators / Rivers |
| `worldTabs` | 66.7% (2/3) | 容器 |  |
| `worldTabs/li` | 133.3% (4/3) | 文本 | WITab_Orbit / WITab_Planet / WITab_Terrain |

## 四、原版 defName 一览（共 3 个，列出前 60）

```text
`Orbit`                           ``                                `Surface`                       
```
