# RoomPart_CrateDef

- **所属线**：世界线
- **原版实例数**：2
- **字段路径数**：3
- **资料片**：Odyssey
- **原版出处**：`Odyssey/Defs/RoomPartDefs/RoomParts_Common.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<RoomPart_CrateDef>
    <defName>HermetricCrate_LowValue</defName>
    <crateDef>AncientHermeticCrate</crateDef>
    <thingSetMaker>MapGen_ScarlandsHermeticCrate</thingSetMaker>
  </RoomPart_CrateDef>

  
```

> 来自 `Odyssey/Defs/RoomPartDefs/RoomParts_Common.xml`，defName = `HermetricCrate_LowValue`，XML 节点数 4（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
crateDef                                       [文本]  例：AncientHermeticCrate
defName                                        [文本]  例：HermetricCrate_HighValue / HermetricCrate_LowValue
thingSetMaker                                  [文本]  例：MapGen_HighValueCrate / MapGen_ScarlandsHermeticCrate
```

## 三、全量字段表（3 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `crateDef` | 100.0% (2/2) | 文本 | AncientHermeticCrate |
| `defName` | 100.0% (2/2) | 文本 | HermetricCrate_HighValue / HermetricCrate_LowValue |
| `thingSetMaker` | 100.0% (2/2) | 文本 | MapGen_HighValueCrate / MapGen_ScarlandsHermeticCrate |

## 四、原版 defName 一览（共 2 个，列出前 60）

```text
`HermetricCrate_LowValue`         `HermetricCrate_HighValue`      
```
