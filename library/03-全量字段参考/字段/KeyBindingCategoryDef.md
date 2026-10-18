# KeyBindingCategoryDef

- **所属线**：系统线
- **原版实例数**：9
- **字段路径数**：7
- **资料片**：Core
- **原版出处**：`Core/Defs/Misc/KeyBindings/KeyBindingCategories.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<KeyBindingCategoryDef>
    <defName>DebugMenu</defName>
    <label>debug menu</label>
    <description>Controls used in debug menus. Active in development mode only.</description>
    <checkForConflicts>
      <li>Development</li>
    </checkForConflicts>
  </KeyBindingCategoryDef>
```

> 来自 `Core/Defs/Misc/KeyBindings/KeyBindingCategories.xml`，defName = `DebugMenu`，XML 节点数 6（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
checkForConflicts                              [容器]
checkForConflicts/li                           [文本]  例：Development / Game / MainTabs
defName                                        [文本]  例：Game / GameMapCamera / SelectionMisc
description                                    [文本]  例：Colony mode controls that apply in most situations. / Controls for the camera. / Generic controls that are re-used by many items and objects throughout the game.
label                                          [文本]  例：camera / in-game global / misc
```

## 三、全量字段表（7 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `checkForConflicts` | 100.0% (9/9) | 容器 |  |
| `checkForConflicts/li` | 333.3% (30/9) | 文本 | Development / Game / MainTabs |
| `defName` | 100.0% (9/9) | 文本 | Game / GameMapCamera / SelectionMisc |
| `description` | 100.0% (9/9) | 文本 | Colony mode controls that apply in most situations. / Controls for the camera. / Generic controls that are re- |
| `isGameUniversal` | 33.3% (3/9) | 布尔 | true |
| `label` | 100.0% (9/9) | 文本 | camera / in-game global / misc |
| `selfConflicting` | 11.1% (1/9) | 布尔 | false |

## 四、原版 defName 一览（共 9 个，列出前 60）

```text
`DebugMenu`                       `Development`                     `Architect`                       `SelectionMisc`                 
`SelectionSpecial`                `GameMapCamera`                   `Game`                            `MainTabs`                      
`Modifiers`                     
```
