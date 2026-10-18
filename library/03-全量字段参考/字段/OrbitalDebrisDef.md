# OrbitalDebrisDef

- **所属线**：世界线
- **原版实例数**：3
- **字段路径数**：11
- **资料片**：Odyssey
- **原版出处**：`Odyssey/Defs/OrbitalDebrisDefs/OrbitalDebris.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<OrbitalDebrisDef>
    <defName>Asteroid</defName>
    <graphics>
      <li>
        <weighting>0.2</weighting>
        <order>1</order>
        <parallaxPer10Cells>0.2</parallaxPer10Cells>
        <graphicData>
          <texPath>World/Debris/Asteroid/Large</texPath>
          <graphicClass>Graphic_Random</graphicClass>
          <shaderType>OrbitalDebris</shaderType>
          <drawSize>14</drawSize>
        </graphicData>
      </li>
      <li>
        <weighting>0.5</weighting>
        <order>2</order>
        <parallaxPer10Cells>1</parallaxPer10Cells>
        <graphicData>
          <texPath>World/Debris/Asteroid/Medium</texPath>
          <graphicClass>Graphic_Random</graphicClass>
          <shaderType>OrbitalDebris</shaderType>
          <drawSize>6</drawSize>
        </graphicData>
      </li>
      <li>
        <weighting>1.0</weighting>
        <order>3</order>
        <parallaxPer10Cells>2</parallaxPer10Cells>
        <graphicData>
          <texPath>World/Debris/Asteroid/Small</texPath>
          <graphicClass>Graphic_Random</graphicClass>
          <shaderType>OrbitalDebris</shaderType>
          <drawSize>3</drawSize>
        </graphicData>
      </li>
    </graphics>
  </OrbitalDebrisDef>

  
```

> 来自 `Odyssey/Defs/OrbitalDebrisDefs/OrbitalDebris.xml`，defName = `Asteroid`，XML 节点数 30（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Asteroid / Manmade / Mechanoid
graphics                                       [容器]
graphics/li                                    [容器]
graphics/li/graphicData                        [容器]
graphics/li/graphicData/drawSize               [数值]  例：14 / 2 / 3
graphics/li/graphicData/graphicClass           [文本]  例：Graphic_Random
graphics/li/graphicData/shaderType             [文本]  例：OrbitalDebris
graphics/li/graphicData/texPath                [文本]  例：World/Debris/Asteroid/Large / World/Debris/Asteroid/Medium / World/Debris/Asteroid/Small
graphics/li/order                              [数值]  例：1 / 2 / 3
graphics/li/parallaxPer10Cells                 [数值]  例：0.2 / 1 / 2
graphics/li/weighting                          [数值]  例：0.2 / 0.5 / 0.75
```

## 三、全量字段表（11 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (3/3) | 文本 | Asteroid / Manmade / Mechanoid |
| `graphics` | 100.0% (3/3) | 容器 |  |
| `graphics/li` | 300.0% (9/3) | 容器 |  |
| `graphics/li/graphicData` | 300.0% (9/3) | 容器 |  |
| `graphics/li/graphicData/drawSize` | 300.0% (9/3) | 数值 | 14 / 2 / 3 |
| `graphics/li/graphicData/graphicClass` | 300.0% (9/3) | 文本 | Graphic_Random |
| `graphics/li/graphicData/shaderType` | 300.0% (9/3) | 文本 | OrbitalDebris |
| `graphics/li/graphicData/texPath` | 300.0% (9/3) | 文本 | World/Debris/Asteroid/Large / World/Debris/Asteroid/Medium / World/Debris/Asteroid/Small |
| `graphics/li/order` | 300.0% (9/3) | 数值 | 1 / 2 / 3 |
| `graphics/li/parallaxPer10Cells` | 300.0% (9/3) | 数值 | 0.2 / 1 / 2 |
| `graphics/li/weighting` | 300.0% (9/3) | 数值 | 0.2 / 0.5 / 0.75 |

## 四、原版 defName 一览（共 3 个，列出前 60）

```text
`Asteroid`                        `Manmade`                         `Mechanoid`                     
```
