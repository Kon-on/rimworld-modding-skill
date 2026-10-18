# DesignationCategoryDef

- **所属线**：系统线
- **原版实例数**：16
- **字段路径数**：10
- **资料片**：Anomaly、Biotech、Core、Ideology、Odyssey
- **原版出处**：`Core/Defs/Misc/Designations/DesignationCategories.xml`、`Odyssey/Defs/DesignationCategoryDefs/DesignationCategories.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<DesignationCategoryDef>
    <defName>Production</defName>
    <label>production</label>
    <order>600</order>
    <specialDesignatorClasses>
      <li>Designator_Cancel</li>
      <li>Designator_Deconstruct</li>
    </specialDesignatorClasses>
  </DesignationCategoryDef>

  
```

> 来自 `Core/Defs/Misc/Designations/DesignationCategories.xml`，defName = `Production`，XML 节点数 7（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Anomaly / Biotech / Orders
label                                          [文本]  例：anomaly / biotech / orders
order                                          [数值]  例：11 / 12 / 800
specialDesignatorClasses                       [容器]
specialDesignatorClasses/li                    [文本]  例：Designator_Cancel / Designator_Deconstruct / Designator_Mine
```

## 三、全量字段表（10 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (16/16) | 文本 | Anomaly / Biotech / Orders |
| `label` | 100.0% (16/16) | 文本 | anomaly / biotech / orders |
| `minMonolithLevel` | 6.2% (1/16) | 数值 | 1 |
| `order` | 100.0% (16/16) | 数值 | 11 / 12 / 800 |
| `preferredColumn` | 12.5% (2/16) | 数值 | 1 |
| `researchPrerequisites` | 18.8% (3/16) | 容器 |  |
| `researchPrerequisites/li` | 18.8% (3/16) | 文本 | Electricity / ShipBasics |
| `showPowerGrid` | 6.2% (1/16) | 布尔 | true |
| `specialDesignatorClasses` | 100.0% (16/16) | 容器 |  |
| `specialDesignatorClasses/li` | 456.2% (73/16) | 文本 | Designator_Cancel / Designator_Deconstruct / Designator_Mine |

## 四、原版 defName 一览（共 16 个，列出前 60）

```text
`Production`                      `Furniture`                       `Security`                        `Misc`                          
`Joy`                             `Temperature`                     `Anomaly`                         `Ideology`                      
`Odyssey`                         `Structure`                       `Ship`                            `Biotech`                       
`Power`                           `Floors`                          `Zone`                            `Orders`                        
```
