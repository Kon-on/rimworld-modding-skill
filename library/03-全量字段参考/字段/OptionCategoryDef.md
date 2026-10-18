# OptionCategoryDef

- **所属线**：系统线
- **原版实例数**：8
- **字段路径数**：4
- **资料片**：Core
- **原版出处**：`Core/Defs/Misc/OptionCategoryDefs/OptionCategories.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<OptionCategoryDef>
    <defName>General</defName>
    <label>general</label>
    <texPath>UI/Icons/Options/OptionsGeneral</texPath>
  </OptionCategoryDef>
  
  
```

> 来自 `Core/Defs/Misc/OptionCategoryDefs/OptionCategories.xml`，defName = `General`，XML 节点数 4（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Audio / Gameplay / General
label                                          [文本]  例：audio / gameplay / general
texPath                                        [文本]  例：UI/Icons/Options/OptionsAudio / UI/Icons/Options/OptionsGameplay / UI/Icons/Options/OptionsGeneral
```

## 三、全量字段表（4 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (8/8) | 文本 | Audio / Gameplay / General |
| `isDev` | 12.5% (1/8) | 布尔 | true |
| `label` | 100.0% (8/8) | 文本 | audio / gameplay / general |
| `texPath` | 100.0% (8/8) | 文本 | UI/Icons/Options/OptionsAudio / UI/Icons/Options/OptionsGameplay / UI/Icons/Options/OptionsGeneral |

## 四、原版 defName 一览（共 8 个，列出前 60）

```text
`General`                         `Graphics`                        `Audio`                           `Gameplay`                      
`Interface`                       `Controls`                        `Mods`                            `Dev`                           
```
