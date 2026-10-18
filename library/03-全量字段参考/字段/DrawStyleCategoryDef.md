# DrawStyleCategoryDef

- **所属线**：表现线
- **原版实例数**：19
- **字段路径数**：3
- **资料片**：Core
- **原版出处**：`Core/Defs/DrawStyleCategoryDefs/DrawStyleCategories.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<DrawStyleCategoryDef ParentName="Default1D">
    <defName>Walls</defName>
  </DrawStyleCategoryDef>

  
```

> 来自 `Core/Defs/DrawStyleCategoryDefs/DrawStyleCategories.xml`，defName = `Walls`，XML 节点数 2（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Default1D / Default2D / Fill2D
```

## 三、全量字段表（3 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (19/19) | 文本 | Default1D / Default2D / Fill2D |
| `styles` | 21.1% (4/19) | 容器 |  |
| `styles/li` | 68.4% (13/19) | 文本 | EmptyOval / EmptyRectangle / FilledOval |

## 四、原版 defName 一览（共 19 个，列出前 60）

```text
`Walls`                           `Conduits`                        `Defenses`                        `Zones`                         
`Areas`                           `Orders`                          `Mine`                            `Paint`                         
`Plans`                           `RemovePlans`                     `RemoveZones`                     `Foundations`                   
`Floors`                          `Cancel`                          `Plants`                          `FilledRectangle`               
`Fill2D`                          `Default1D`                       `Default2D`                     
```
