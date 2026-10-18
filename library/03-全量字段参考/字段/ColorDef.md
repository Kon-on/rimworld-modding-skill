# ColorDef

- **所属线**：表现线
- **原版实例数**：140
- **字段路径数**：7
- **资料片**：Core、Ideology、Odyssey
- **原版出处**：`Core/Defs/ColorDefs/ColorDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<ColorDef Name="StructureColorBase" Abstract="True">
    <colorType>Structure</colorType>
  </ColorDef>



  
```

> 来自 `Core/Defs/ColorDefs/ColorDefs.xml`，defName = ``，XML 节点数 2（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
color                                          [文本]  例：(118, 49, 57) / (132, 84, 72) / (138, 51, 36)
defName                                        [文本]  例：Structure_Auburn / Structure_Red / Structure_RedSubtle
```

## 三、全量字段表（7 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `color` | 96.4% (135/140) | 文本 | (118, 49, 57) / (132, 84, 72) / (138, 51, 36) |
| `colorType` | 3.6% (5/140) | 文本 | Hair / Ideo / Planning |
| `defName` | 96.4% (135/140) | 文本 | Structure_Auburn / Structure_Red / Structure_RedSubtle |
| `displayInStylingStationUI` | 8.6% (12/140) | 布尔 | false |
| `displayOrder` | 45.0% (63/140) | 数值 | 0 / 10 / 20 |
| `label` | 83.6% (117/140) | 文本 | auburn / red / scarlet |
| `randomlyPickable` | 3.6% (5/140) | 布尔 | false |

## 四、原版 defName 一览（共 140 个，列出前 60）

```text
``                                ``                                ``                                ``                              
`PitchBlack`                      `DarkBlack`                       `MidBlack`                        `DarkReddish`                   
`DarkSaturatedReddish`            `DarkBrown`                       `ReddishBrown`                    `SandyBlonde`                   
`Blonde`                          ``                                `PlanGray`                        `PlanRed`                       
`PlanOrange`                      `PlanYellow`                      `PlanGreen`                       `PlanCyan`                      
`PlanBlue`                        `PlanPurple`                      `PlanPink`                        `LightGrey`                     
`Grey`                            `DarkGrey`                        `Black`                           `LightRed`                      
`Red`                             `DarkRed`                         `LightOrange`                     `Orange`                        
`DarkOrange`                      `LightOlive`                      `Olive`                           `DarkOlive`                     
`LightGreen`                      `Green`                           `DarkGreen`                       `LightTeal`                     
`Teal`                            `DarkTeal`                        `LightBlue`                       `Blue`                          
`DarkBlue`                        `LightSapphire`                   `Sapphire`                        `DarkSapphire`                  
`LightMauve`                      `Mauve`                           `DarkMauve`                       `LightPurple`                   
`Purple`                          `DarkPurple`                      `LightPink`                       `Pink`                          
`DarkPink`                        `UniqueWeapon_Red`                `UniqueWeapon_MutedRed`           `UniqueWeapon_Purple`           
```

_余下 80 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
