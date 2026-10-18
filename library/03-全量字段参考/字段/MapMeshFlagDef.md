# MapMeshFlagDef

- **所属线**：系统线
- **原版实例数**：15
- **字段路径数**：1
- **资料片**：Biotech、Core、Odyssey
- **原版出处**：`Biotech/Defs/MapMeshFlagDefs/MapMeshFlagDefs.xml`、`Core/Defs/MapMeshFlagDefs/MapMeshFlagDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<MapMeshFlagDef>
    <defName>Pollution</defName>
  </MapMeshFlagDef>
```

> 来自 `Biotech/Defs/MapMeshFlagDefs/MapMeshFlagDefs.xml`，defName = `Pollution`，XML 节点数 2（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：FogOfWar / None / Pollution
```

## 三、全量字段表（1 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (15/15) | 文本 | FogOfWar / None / Pollution |

## 四、原版 defName 一览（共 15 个，列出前 60）

```text
`Pollution`                       `None`                            `Things`                          `FogOfWar`                      
`Buildings`                       `GroundGlow`                      `Terrain`                         `Roofs`                         
`Snow`                            `Zone`                            `Plan`                            `PowerGrid`                     
`BuildingsDamage`                 `Gas`                             `Sand`                          
```
