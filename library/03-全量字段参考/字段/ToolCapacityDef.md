# ToolCapacityDef

- **所属线**：物品线
- **原版实例数**：13
- **字段路径数**：2
- **资料片**：Biotech、Core、Odyssey
- **原版出处**：`Biotech/Defs/ToolCapacityDefs/ToolCapacityDefs.xml`、`Core/Defs/ToolCapacityDefs/ToolCapacity.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<ToolCapacityDef>
    <defName>DemolishDoors</defName>
    <label>demolish doors</label>
  </ToolCapacityDef>
```

> 来自 `Biotech/Defs/ToolCapacityDefs/ToolCapacityDefs.xml`，defName = `DemolishDoors`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Blunt / Cut / DemolishDoors
label                                          [文本]  例：blunt / cut / demolish doors
```

## 三、全量字段表（2 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (13/13) | 文本 | Blunt / Cut / DemolishDoors |
| `label` | 100.0% (13/13) | 文本 | blunt / cut / demolish doors |

## 四、原版 defName 一览（共 13 个，列出前 60）

```text
`DemolishDoors`                   `Stab`                            `Cut`                             `Blunt`                         
`Scratch`                         `Poke`                            `Bite`                            `ToxicBite`                     
`ScratchToxic`                    `KickMaterialInEyes`              `Demolish`                        `PorcupineBite`                 
`PorcupineScratch`              
```
