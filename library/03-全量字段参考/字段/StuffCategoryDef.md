# StuffCategoryDef

- **所属线**：物品线
- **原版实例数**：6
- **字段路径数**：6
- **资料片**：Anomaly、Core
- **原版出处**：`Core/Defs/Misc/StuffCategoryDefs/StuffCategories.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<StuffCategoryDef>
    <defName>Fabric</defName>
    <label>fabric</label>
    <noun>fabric</noun>
    <destroySoundSmall>BuildingDestroyed_Soft_Small</destroySoundSmall>
    <destroySoundMedium>BuildingDestroyed_Soft_Medium</destroySoundMedium>
  </StuffCategoryDef>

  
```

> 来自 `Core/Defs/Misc/StuffCategoryDefs/StuffCategories.xml`，defName = `Fabric`，XML 节点数 6（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Bioferrite / Metallic / Stony
destroySoundMedium                             [文本]  例：BuildingDestroyed_Metal_Medium / BuildingDestroyed_Soft_Medium / BuildingDestroyed_Stone_Medium
destroySoundSmall                              [文本]  例：BuildingDestroyed_Metal_Small / BuildingDestroyed_Soft_Small / BuildingDestroyed_Stone_Small
label                                          [文本]  例：bioferrite / metallic / stony
noun                                           [文本]  例：bioferrite / metal / stone
```

## 三、全量字段表（6 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (6/6) | 文本 | Bioferrite / Metallic / Stony |
| `destroySoundLarge` | 66.7% (4/6) | 文本 | BuildingDestroyed_Metal_Big / BuildingDestroyed_Stone_Big / BuildingDestroyed_Wood_Big |
| `destroySoundMedium` | 100.0% (6/6) | 文本 | BuildingDestroyed_Metal_Medium / BuildingDestroyed_Soft_Medium / BuildingDestroyed_Stone_Medium |
| `destroySoundSmall` | 100.0% (6/6) | 文本 | BuildingDestroyed_Metal_Small / BuildingDestroyed_Soft_Small / BuildingDestroyed_Stone_Small |
| `label` | 100.0% (6/6) | 文本 | bioferrite / metallic / stony |
| `noun` | 100.0% (6/6) | 文本 | bioferrite / metal / stone |

## 四、原版 defName 一览（共 6 个，列出前 60）

```text
`Fabric`                          `Leathery`                        `Bioferrite`                      `Metallic`                      
`Woody`                           `Stony`                         
```
