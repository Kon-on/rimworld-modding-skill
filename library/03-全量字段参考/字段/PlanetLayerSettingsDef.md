# PlanetLayerSettingsDef

- **所属线**：世界线
- **原版实例数**：2
- **字段路径数**：9
- **资料片**：Core、Odyssey
- **原版出处**：`Core/Defs/Misc/WorldLayerSettingsDefs/PlanetLayerSettings.xml`、`Odyssey/Defs/WorldLayerSettingsDefs/PlanetLayerSettings.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<PlanetLayerSettingsDef>
    <defName>Surface</defName>
    <label>Default surface</label>
    <settings>
      <radius>100</radius>
      <subdivisions>10</subdivisions>
      <useSurfaceViewAngle>true</useSurfaceViewAngle>
    </settings>
  </PlanetLayerSettingsDef>
  
```

> 来自 `Core/Defs/Misc/WorldLayerSettingsDefs/PlanetLayerSettings.xml`，defName = `Surface`，XML 节点数 7（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Orbit / Surface
label                                          [文本]  例：Default orbit / Default surface
settings                                       [容器]
settings/radius                                [数值]  例：100 / 130
settings/subdivisions                          [数值]  例：10 / 5
settings/useSurfaceViewAngle                   [布尔]  例：true
```

## 三、全量字段表（9 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (2/2) | 文本 | Orbit / Surface |
| `label` | 100.0% (2/2) | 文本 | Default orbit / Default surface |
| `settings` | 100.0% (2/2) | 容器 |  |
| `settings/backgroundWorldCameraOffset` | 50.0% (1/2) | 数值 | 160 |
| `settings/backgroundWorldCameraParallaxDistancePer100Cells` | 50.0% (1/2) | 数值 | 2.5 |
| `settings/extraCameraAltitude` | 50.0% (1/2) | 数值 | 300 |
| `settings/radius` | 100.0% (2/2) | 数值 | 100 / 130 |
| `settings/subdivisions` | 100.0% (2/2) | 数值 | 10 / 5 |
| `settings/useSurfaceViewAngle` | 100.0% (2/2) | 布尔 | true |

## 四、原版 defName 一览（共 2 个，列出前 60）

```text
`Surface`                         `Orbit`                         
```
