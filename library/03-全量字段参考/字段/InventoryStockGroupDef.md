# InventoryStockGroupDef

- **所属线**：物品线
- **原版实例数**：1
- **字段路径数**：4
- **资料片**：Core
- **原版出处**：`Core/Defs/Misc/InventoryStockGroupDefs/InventoryStockGroups.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<InventoryStockGroupDef>
    <defName>Medicine</defName>
    <thingDefs>
      <li>MedicineHerbal</li>
      <li>MedicineIndustrial</li>
      <li>MedicineUltratech</li>
    </thingDefs>
    <defaultThingDef>MedicineIndustrial</defaultThingDef>
  </InventoryStockGroupDef>
```

> 来自 `Core/Defs/Misc/InventoryStockGroupDefs/InventoryStockGroups.xml`，defName = `Medicine`，XML 节点数 7（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defaultThingDef                                [文本]  例：MedicineIndustrial
defName                                        [文本]  例：Medicine
thingDefs                                      [容器]
thingDefs/li                                   [文本]  例：MedicineHerbal / MedicineIndustrial / MedicineUltratech
```

## 三、全量字段表（4 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defaultThingDef` | 100.0% (1/1) | 文本 | MedicineIndustrial |
| `defName` | 100.0% (1/1) | 文本 | Medicine |
| `thingDefs` | 100.0% (1/1) | 容器 |  |
| `thingDefs/li` | 300.0% (3/1) | 文本 | MedicineHerbal / MedicineIndustrial / MedicineUltratech |

## 四、原版 defName 一览（共 1 个，列出前 60）

```text
`Medicine`                      
```
