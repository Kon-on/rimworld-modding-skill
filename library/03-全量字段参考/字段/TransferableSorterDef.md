# TransferableSorterDef

- **所属线**：表现线
- **原版实例数**：7
- **字段路径数**：3
- **资料片**：Core
- **原版出处**：`Core/Defs/Misc/TradeDialogSorterDefs/TransferableSorters.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<TransferableSorterDef>
    <defName>None</defName>
    <label>none</label>
    <comparerClass>TransferableComparer_None</comparerClass>
  </TransferableSorterDef>
  
  
```

> 来自 `Core/Defs/Misc/TradeDialogSorterDefs/TransferableSorters.xml`，defName = `None`，XML 节点数 4（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
comparerClass                                  [文本]  例：TransferableComparer_Category / TransferableComparer_MarketValue / TransferableComparer_Name
defName                                        [文本]  例：Category / MarketValue / Name
label                                          [文本]  例：category / market value / name
```

## 三、全量字段表（3 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `comparerClass` | 100.0% (7/7) | 文本 | TransferableComparer_Category / TransferableComparer_MarketValue / TransferableComparer_Name |
| `defName` | 100.0% (7/7) | 文本 | Category / MarketValue / Name |
| `label` | 100.0% (7/7) | 文本 | category / market value / name |

## 四、原版 defName 一览（共 7 个，列出前 60）

```text
`None`                            `Name`                            `MarketValue`                     `Category`                      
`Quality`                         `Mass`                            `HitPointsPercentage`           
```
