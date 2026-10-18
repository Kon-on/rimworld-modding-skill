# DesignatorDropdownGroupDef

- **所属线**：系统线
- **原版实例数**：13
- **字段路径数**：5
- **资料片**：Core、Ideology
- **原版出处**：`Core/Defs/Misc/DesignatorDropdownGroupDef/DesignatorDropdownGroupDef.xml`、`Ideology/Defs/TerrainDefs/Terrain_Floors.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<DesignatorDropdownGroupDef>
    <defName>Floor_Tile</defName>
    <label>tile</label>
  </DesignatorDropdownGroupDef>

  
```

> 来自 `Core/Defs/Misc/DesignatorDropdownGroupDef/DesignatorDropdownGroupDef.xml`，defName = `Floor_Tile`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Floor_Carpet / Floor_Carpet_Fine / Floor_Tile
label                                          [文本]  例：carpet / fine carpet / fine tile
```

## 三、全量字段表（5 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (13/13) | 文本 | Floor_Carpet / Floor_Carpet_Fine / Floor_Tile |
| `iconSource` | 38.5% (5/13) | 文本 | Placed |
| `includeEyeDropperTool` | 30.8% (4/13) | 布尔 | true |
| `label` | 100.0% (13/13) | 文本 | carpet / fine carpet / fine tile |
| `useGridMenu` | 30.8% (4/13) | 布尔 | true |

## 四、原版 defName 一览（共 13 个，列出前 60）

```text
`Floor_Tile`                      `Floor_Tile_Fine`                 `Floor_Tile_Metal`                `Floor_Flagstone`               
`StandingLampColored`             `Floor_Morbid_Stone`              `Floor_Spikecore_Tile`            `Floor_Totemic_Tile`            
`Floor_MindbendCarpet`            `Floor_Carpet`                    `Floor_Carpet_Fine`               `Floor_Morbid_Carpet`           
`Floor_Transhumanist_Carpet`    
```
