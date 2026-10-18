# BillStoreModeDef

- **所属线**：系统线
- **原版实例数**：3
- **字段路径数**：4
- **资料片**：Core
- **原版出处**：`Core/Defs/Misc/BillDefs/BillStoreModeDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<BillStoreModeDef>
    <defName>DropOnFloor</defName>
    <label>drop on floor</label>
    <listOrder>0</listOrder>
  </BillStoreModeDef>

  
```

> 来自 `Core/Defs/Misc/BillDefs/BillStoreModeDefs.xml`，defName = `DropOnFloor`，XML 节点数 4（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：BestStockpile / DropOnFloor / SpecificStockpile
label                                          [文本]  例：drop on floor / take to best stockpile / take to {0}
listOrder                                      [数值]  例：0 / 10 / 20
```

## 三、全量字段表（4 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (3/3) | 文本 | BestStockpile / DropOnFloor / SpecificStockpile |
| `ignoreIllegalLabelCharacterConfigError` | 33.3% (1/3) | 布尔 | true |
| `label` | 100.0% (3/3) | 文本 | drop on floor / take to best stockpile / take to {0} |
| `listOrder` | 100.0% (3/3) | 数值 | 0 / 10 / 20 |

## 四、原版 defName 一览（共 3 个，列出前 60）

```text
`DropOnFloor`                     `BestStockpile`                   `SpecificStockpile`             
```
