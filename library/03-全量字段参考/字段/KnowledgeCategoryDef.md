# KnowledgeCategoryDef

- **所属线**：人物线
- **原版实例数**：2
- **字段路径数**：5
- **资料片**：Anomaly
- **原版出处**：`Anomaly/Defs/KnowledgeCategoryDefs/KnowledgeCategories.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<KnowledgeCategoryDef>
    <defName>Basic</defName>
    <label>basic</label>
    <color>(1, 1, 1, 1)</color>
    <texPath>UI/AnomalyResearchCategoryMarkers/AnomalyResearchCategory_Basic</texPath>
  </KnowledgeCategoryDef>

  
```

> 来自 `Anomaly/Defs/KnowledgeCategoryDefs/KnowledgeCategories.xml`，defName = `Basic`，XML 节点数 5（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
color                                          [文本]  例：(1, 1, 1, 1)
defName                                        [文本]  例：Advanced / Basic
label                                          [文本]  例：advanced / basic
texPath                                        [文本]  例：UI/AnomalyResearchCategoryMarkers/AnomalyResearchCategory_Advanced / UI/AnomalyResearchCategoryMarkers/AnomalyResearchCategory_Basic
```

## 三、全量字段表（5 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `color` | 100.0% (2/2) | 文本 | (1, 1, 1, 1) |
| `defName` | 100.0% (2/2) | 文本 | Advanced / Basic |
| `label` | 100.0% (2/2) | 文本 | advanced / basic |
| `overflowCategory` | 50.0% (1/2) | 文本 | Basic |
| `texPath` | 100.0% (2/2) | 文本 | UI/AnomalyResearchCategoryMarkers/AnomalyResearchCategory_Advanced / UI/AnomalyResearchCategoryMarkers/Anomaly |

## 四、原版 defName 一览（共 2 个，列出前 60）

```text
`Basic`                           `Advanced`                      
```
