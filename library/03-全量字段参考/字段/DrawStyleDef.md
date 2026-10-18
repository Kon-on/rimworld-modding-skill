# DrawStyleDef

- **所属线**：表现线
- **原版实例数**：6
- **字段路径数**：8
- **资料片**：Core
- **原版出处**：`Core/Defs/DrawStyleDefs/DrawStyles.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<DrawStyleDef>
    <defName>AngledLine</defName>
    <label>angled line</label>
    <uiIconPath>UI/Widgets/DrawStyles/AngledLine</uiIconPath>
    <drawStyleType>DrawStyle_AngledLine</drawStyleType>
  </DrawStyleDef>
  
  
```

> 来自 `Core/Defs/DrawStyleDefs/DrawStyles.xml`，defName = `AngledLine`，XML 节点数 5（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：AngledLine / EmptyRectangle / FilledRectangle
drawStyleType                                  [文本]  例：DrawStyle_AngledLine / DrawStyle_EmptyRectangle / DrawStyle_FilledRectangle
label                                          [文本]  例：angled line / empty rectangle / filled rectangle
uiIconPath                                     [文本]  例：UI/Widgets/DrawStyles/AngledLine / UI/Widgets/DrawStyles/RectangleEmpty / UI/Widgets/DrawStyles/RectangleFilled
```

## 三、全量字段表（8 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `canSnap` | 16.7% (1/6) | 布尔 | false |
| `defName` | 100.0% (6/6) | 文本 | AngledLine / EmptyRectangle / FilledRectangle |
| `drawArea` | 16.7% (1/6) | 布尔 | false |
| `drawOutline` | 66.7% (4/6) | 布尔 | true |
| `drawShortSideMeasurement` | 16.7% (1/6) | 布尔 | false |
| `drawStyleType` | 100.0% (6/6) | 文本 | DrawStyle_AngledLine / DrawStyle_EmptyRectangle / DrawStyle_FilledRectangle |
| `label` | 100.0% (6/6) | 文本 | angled line / empty rectangle / filled rectangle |
| `uiIconPath` | 100.0% (6/6) | 文本 | UI/Widgets/DrawStyles/AngledLine / UI/Widgets/DrawStyles/RectangleEmpty / UI/Widgets/DrawStyles/RectangleFille |

## 四、原版 defName 一览（共 6 个，列出前 60）

```text
`AngledLine`                      `FilledRectangle`                 `EmptyRectangle`                  `FilledOval`                    
`EmptyOval`                       `Line`                          
```
