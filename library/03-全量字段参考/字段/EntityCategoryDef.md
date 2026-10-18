# EntityCategoryDef

- **所属线**：世界线
- **原版实例数**：3
- **字段路径数**：3
- **资料片**：Anomaly
- **原版出处**：`Anomaly/Defs/EntityCategoryDefs/EntityCategories.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<EntityCategoryDef>
    <defName>Basic</defName>
    <label>basic</label>
    <listOrder>0</listOrder>
  </EntityCategoryDef>

  
```

> 来自 `Anomaly/Defs/EntityCategoryDefs/EntityCategories.xml`，defName = `Basic`，XML 节点数 4（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Advanced / Basic / Ultimate
label                                          [文本]  例：advanced / basic / ultimate
listOrder                                      [数值]  例：0 / 1 / 2
```

## 三、全量字段表（3 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (3/3) | 文本 | Advanced / Basic / Ultimate |
| `label` | 100.0% (3/3) | 文本 | advanced / basic / ultimate |
| `listOrder` | 100.0% (3/3) | 数值 | 0 / 1 / 2 |

## 四、原版 defName 一览（共 3 个，列出前 60）

```text
`Basic`                           `Advanced`                        `Ultimate`                      
```
