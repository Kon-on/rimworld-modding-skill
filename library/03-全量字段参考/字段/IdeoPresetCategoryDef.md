# IdeoPresetCategoryDef

- **所属线**：理念线
- **原版实例数**：6
- **字段路径数**：4
- **资料片**：Ideology
- **原版出处**：`Ideology/Defs/PreconfiguredIdeos/IdeoPresetDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<IdeoPresetCategoryDef>
    <defName>Classic</defName>
    <label>classic</label>
    <description>Classic RimWorld without the ideoligion system. Good for your first few games, or when you're not trying to do something specific. All Ideology expansion content remains active.</description>
    <groupLabel>Classic</groupLabel>
  </IdeoPresetCategoryDef>

  
```

> 来自 `Ideology/Defs/PreconfiguredIdeos/IdeoPresetDefs.xml`，defName = `Classic`，XML 节点数 5（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Classic / Fluid / Mild
description                                    [文本]  例：Begin with a simple ideoligion and develop it over time. / Classic RimWorld without the ideoligion system. Good for your first few games, o / Classic-like gameplay with small variations.
groupLabel                                     [文本]  例：Classic / Custom / Fluid
label                                          [文本]  例：classic / fluid / mild
```

## 三、全量字段表（4 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (6/6) | 文本 | Classic / Fluid / Mild |
| `description` | 100.0% (6/6) | 文本 | Begin with a simple ideoligion and develop it over time. / Classic RimWorld without the ideoligion system. Goo |
| `groupLabel` | 100.0% (6/6) | 文本 | Classic / Custom / Fluid |
| `label` | 100.0% (6/6) | 文本 | classic / fluid / mild |

## 四、原版 defName 一览（共 6 个，列出前 60）

```text
`Classic`                         `Fluid`                           `Mild`                            `Strong`                        
`Intense`                         `Custom`                        
```
