# RoadDef

- **所属线**：世界线
- **原版实例数**：5
- **字段路径数**：25
- **资料片**：Core
- **原版出处**：`Core/Defs/RoadDefs/RoadDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<RoadDef>
    <defName>DirtPath</defName>
    <label>dirt path</label>
    <priority>10</priority>
    <movementCostMultiplier>0.5</movementCostMultiplier>
    <tilesPerSegment>15</tilesPerSegment>
    <pathingMode>Avoid</pathingMode>
    <roadGenSteps>
      <li Class="RoadDefGenStep_Place">
        <chancePerPositionCurve>
          <points>
            <li>(1.1, 1)</li>
            <li>(1.1, 0)</li>
          </points>
        </chancePerPositionCurve>
        <place>Bridge</place>
        <antialiasingMultiplier>0</antialiasingMultiplier>
        <onlyIfOriginAllows>true</onlyIfOriginAllows> <!-- only if bridge also at the center -->
      </li>
      <li Class="RoadDefGenStep_Place">
        <chancePerPositionCurve>
          <points>
            <li>(0, 0.9)</li>
            <li>(0.6, 0.8)</li>
            <li>(0.8, 0)</li>
          </points>
        </chancePerPositionCurve>
        <place>PackedDirt</place>
      </li>
    </roadGenSteps>
    <distortionFrequency>0.5</distortionFrequency>
    <distortionIntensity>0.2</distortionIntensity>
    <worldRenderSteps>
      <li>
        <layer>Outline</layer>
        <width>0.35</width>
      </li>
      <li>
        <layer>Dirt</layer>
        <width>0.2</width>
      </li>
    </worldRenderSteps>
    <worldTransitionGroup>Dirt</worldTransitionGroup>
  </RoadDef>
  
  
```

> 来自 `Core/Defs/RoadDefs/RoadDefs.xml`，defName = `DirtPath`，XML 节点数 34（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：AncientAsphaltRoad / DirtPath / DirtRoad
label                                          [文本]  例：ancient asphalt road / dirt path / dirt road
movementCostMultiplier                         [数值]  例：0.5
pathingMode                                    [文本]  例：Avoid / Bulldoze
priority                                       [数值]  例：10 / 20 / 30
roadGenSteps                                   [容器]
roadGenSteps/li                                [容器]
roadGenSteps/li/antialiasingMultiplier         [数值]  例：0
roadGenSteps/li/chancePerPositionCurve         [容器]
roadGenSteps/li/chancePerPositionCurve/points  [容器]
roadGenSteps/li/chancePerPositionCurve/points/li [文本]  例：(0, 0.9) / (0.6, 0.8) / (0.8, 0)
roadGenSteps/li/onlyIfOriginAllows             [布尔]  例：true
roadGenSteps/li/place                          [文本]  例：AncientLamppost / Bridge / FlagstoneSandstone
roadGenSteps/li/suppressOnTerrainTag           [文本]  例：Water
tilesPerSegment                                [数值]  例：100 / 15 / 25
worldRenderSteps                               [容器]
worldRenderSteps/li                            [容器]
worldRenderSteps/li/layer                      [文本]  例：Asphalt / Dirt / Outline
worldRenderSteps/li/width                      [数值]  例：0.2 / 0.35 / 0.4
worldTransitionGroup                           [文本]  例：Asphalt / Dirt / Stone
```

## 三、全量字段表（25 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `ancientOnly` | 40.0% (2/5) | 布尔 | true |
| `defName` | 100.0% (5/5) | 文本 | AncientAsphaltRoad / DirtPath / DirtRoad |
| `distortionFrequency` | 60.0% (3/5) | 数值 | 0.2 / 0.5 |
| `distortionIntensity` | 60.0% (3/5) | 数值 | 0.10 / 0.2 |
| `label` | 100.0% (5/5) | 文本 | ancient asphalt road / dirt path / dirt road |
| `movementCostMultiplier` | 100.0% (5/5) | 数值 | 0.5 |
| `pathingMode` | 100.0% (5/5) | 文本 | Avoid / Bulldoze |
| `priority` | 100.0% (5/5) | 数值 | 10 / 20 / 30 |
| `roadGenSteps` | 100.0% (5/5) | 容器 |  |
| `roadGenSteps/li` | 340.0% (17/5) | 容器 |  |
| `roadGenSteps/li/antialiasingMultiplier` | 120.0% (6/5) | 数值 | 0 |
| `roadGenSteps/li/chancePerPositionCurve` | 340.0% (17/5) | 容器 |  |
| `roadGenSteps/li/chancePerPositionCurve/points` | 340.0% (17/5) | 容器 |  |
| `roadGenSteps/li/chancePerPositionCurve/points/li` | 1000.0% (50/5) | 文本 | (0, 0.9) / (0.6, 0.8) / (0.8, 0) |
| `roadGenSteps/li/onlyIfOriginAllows` | 100.0% (5/5) | 布尔 | true |
| `roadGenSteps/li/periodicSpacing` | 40.0% (2/5) | 数值 | 12 / 8 |
| `roadGenSteps/li/place` | 320.0% (16/5) | 文本 | AncientLamppost / Bridge / FlagstoneSandstone |
| `roadGenSteps/li/proximitySpacing` | 40.0% (2/5) | 数值 | 4 |
| `roadGenSteps/li/suppressOnTerrainTag` | 120.0% (6/5) | 文本 | Water |
| `tilesPerSegment` | 100.0% (5/5) | 数值 | 100 / 15 / 25 |
| `worldRenderSteps` | 100.0% (5/5) | 容器 |  |
| `worldRenderSteps/li` | 240.0% (12/5) | 容器 |  |
| `worldRenderSteps/li/layer` | 240.0% (12/5) | 文本 | Asphalt / Dirt / Outline |
| `worldRenderSteps/li/width` | 240.0% (12/5) | 数值 | 0.2 / 0.35 / 0.4 |
| `worldTransitionGroup` | 100.0% (5/5) | 文本 | Asphalt / Dirt / Stone |

## 四、原版 defName 一览（共 5 个，列出前 60）

```text
`DirtPath`                        `DirtRoad`                        `StoneRoad`                       `AncientAsphaltRoad`            
`AncientAsphaltHighway`         
```
