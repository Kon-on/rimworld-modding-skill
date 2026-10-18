# KeyBindingDef

- **所属线**：系统线
- **原版实例数**：66
- **字段路径数**：10
- **资料片**：Core
- **原版出处**：`Core/Defs/Misc/KeyBindings/KeyBindings.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<KeyBindingDef Name="GameMapKeyBinding" Abstract="true">
    <category>GameMapCamera</category>
  </KeyBindingDef>

  
```

> 来自 `Core/Defs/Misc/KeyBindings/KeyBindings.xml`，defName = ``，XML 节点数 2（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

_该类型没有出现率≥90% 的字段（字段高度自由）。_

## 三、全量字段表（10 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `category` | 13.6% (9/66) | 文本 | Game / GameMapCamera / SelectionMisc |
| `defaultKeyCodeA` | 89.4% (59/66) | 文本 | A / D / S |
| `defaultKeyCodeB` | 15.2% (10/66) | 文本 | DownArrow / LeftArrow / RightArrow |
| `defName` | 89.4% (59/66) | 文本 | MapDolly_Down / MapDolly_Left / MapDolly_Right |
| `devModeOnly` | 13.6% (9/66) | 布尔 | true |
| `extraConflictTags` | 3.0% (2/66) | 容器 |  |
| `extraConflictTags/li` | 3.0% (2/66) | 文本 | ModifierIncrement |
| `ignoreConflictsWith` | 6.1% (4/66) | 容器 |  |
| `ignoreConflictsWith/li` | 12.1% (8/66) | 文本 | Designator_NextDrawStyle / Designator_PreviousDrawStyle / Designator_RotateLeft |
| `label` | 89.4% (59/66) | 文本 | dolly down / dolly left / dolly right |

## 四、原版 defName 一览（共 66 个，列出前 60）

```text
``                                ``                                ``                                ``                              
``                                ``                                ``                                `MapZoom_In`                    
`MapZoom_Out`                     `Accept`                          `Cancel`                          `TakeScreenshot`                
`ToggleScreenshotMode`            `SelectNextInCell`                `TogglePause`                     `TimeSpeed_Normal`              
`TimeSpeed_Fast`                  `TimeSpeed_Superfast`             `TimeSpeed_Slower`                `TimeSpeed_Faster`              
`PreviousColonist`                `NextColonist`                    `ToggleRoomStatsDisplay`          `ToggleBeautyDisplay`           
`OpenMapSearch`                   `Misc1`                           `Misc2`                           `Misc3`                         
`Misc4`                           `Misc5`                           `Misc6`                           `Misc7`                         
`Misc8`                           `Misc9`                           `Misc10`                          `Misc11`                        
`Misc12`                          `Command_TogglePower`             `Command_ItemForbid`              `Command_ColonistDraft`         
`Designator_Cancel`               `Designator_Deconstruct`          `Dev_ToggleDebugLog`              `MapDolly_Up`                   
`MapDolly_Down`                   `MapDolly_Left`                   `MapDolly_Right`                  `TimeSpeed_Ultrafast`           
`ShowCellInspector`               `Designator_ShapeSnap`            `QueueOrder`                      `Dev_TickOnce`                  
`Dev_ToggleGodMode`               `Dev_ToggleDebugActionsMenu`      `Dev_ToggleDebugLogMenu`          `Dev_ToggleDebugInspector`      
`Dev_ToggleDebugSettingsMenu`     `Dev_ToggleDevPalette`            `ShowEyedropper`                  `Dev_ChangeSelectedDebugAction` 
```

_余下 6 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
