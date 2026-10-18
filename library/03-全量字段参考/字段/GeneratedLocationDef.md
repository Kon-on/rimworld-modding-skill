# GeneratedLocationDef

- **所属线**：世界线
- **原版实例数**：1
- **字段路径数**：6
- **资料片**：Odyssey
- **原版出处**：`Odyssey/Defs/GeneratedLocationDefs/GeneratedLocations.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<GeneratedLocationDef>
    <defName>Asteroids</defName>
    <worldObjectDef>AsteroidBasic</worldObjectDef>
    <layerDefs>
      <li>Orbit</li>
    </layerDefs>
    <preciousResources>
      <li>MineableGold</li>
      <li>MineableSilver</li>
      <li>MineableSteel</li>
      <li>MineableUranium</li>
      <li>MineablePlasteel</li>
      <li>MineableComponentsIndustrial</li>
      <li>MineableJade</li>
    </preciousResources>
  </GeneratedLocationDef>
  
```

> 来自 `Odyssey/Defs/GeneratedLocationDefs/GeneratedLocations.xml`，defName = `Asteroids`，XML 节点数 13（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Asteroids
layerDefs                                      [容器]
layerDefs/li                                   [文本]  例：Orbit
preciousResources                              [容器]
preciousResources/li                           [文本]  例：MineableGold / MineableSilver / MineableSteel
worldObjectDef                                 [文本]  例：AsteroidBasic
```

## 三、全量字段表（6 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (1/1) | 文本 | Asteroids |
| `layerDefs` | 100.0% (1/1) | 容器 |  |
| `layerDefs/li` | 100.0% (1/1) | 文本 | Orbit |
| `preciousResources` | 100.0% (1/1) | 容器 |  |
| `preciousResources/li` | 700.0% (7/1) | 文本 | MineableGold / MineableSilver / MineableSteel |
| `worldObjectDef` | 100.0% (1/1) | 文本 | AsteroidBasic |

## 四、原版 defName 一览（共 1 个，列出前 60）

```text
`Asteroids`                     
```
