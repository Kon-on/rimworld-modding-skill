# HairDef

- **所属线**：人物线
- **原版实例数**：82
- **字段路径数**：9
- **资料片**：Anomaly、Core、Royalty
- **原版出处**：`Anomaly/Defs/HairDefs/HairsCultist.xml`、`Core/Defs/Misc/HairDefs/HairsGeneral.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<HairDef Name="CultistHairBase" Abstract="True">
    <category>Cultist</category>
    <styleTags>
      <li>Cultist</li>
    </styleTags>
  </HairDef>

  
```

> 来自 `Anomaly/Defs/HairDefs/HairsCultist.xml`，defName = ``，XML 节点数 4（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：DoubleTuft / LargeTuft / LongMess
label                                          [文本]  例：double tuft / large tuft / long mess
styleGender                                    [文本]  例：Any / Female / Male
styleTags/li                                   [文本]  例：Cultist / Ghoul / HairShort
texPath                                        [文本]  例：Things/Pawn/Humanlike/Hairs/DoubleTuft / Things/Pawn/Humanlike/Hairs/LargeTuft / Things/Pawn/Humanlike/Hairs/LongMess
```

## 三、全量字段表（9 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `category` | 76.8% (63/82) | 文本 | Cultist / Rural / Soldier |
| `defName` | 97.6% (80/82) | 文本 | DoubleTuft / LargeTuft / LongMess |
| `label` | 97.6% (80/82) | 文本 | double tuft / large tuft / long mess |
| `noGraphic` | 1.2% (1/82) | 布尔 | true |
| `requiredMutant` | 1.2% (1/82) | 文本 | Ghoul |
| `styleGender` | 90.2% (74/82) | 文本 | Any / Female / Male |
| `styleTags` | 78.0% (64/82) | 容器 |  |
| `styleTags/li` | 165.9% (136/82) | 文本 | Cultist / Ghoul / HairShort |
| `texPath` | 96.3% (79/82) | 文本 | Things/Pawn/Humanlike/Hairs/DoubleTuft / Things/Pawn/Humanlike/Hairs/LargeTuft / Things/Pawn/Humanlike/Hairs/L |

## 四、原版 defName 一览（共 82 个，列出前 60）

```text
``                                `Ghoul_Furious`                   `Ghoul_Hungry`                    `Ghoul_Ravenous`                
`Ghoul_Twisted`                   `Ghoul_Vengeful`                  `Ghoul_Warped`                    `Ghoul_Wicked`                  
`DoubleTuft`                      `LargeTuft`                       `LongMess`                        `LongOily`                      
`Parted`                          `PatchyShave`                     `RoughShave`                      `ShavedMohawk`                  
`ShortCut`                        `SideCut`                         `SideSpikes`                      ``                              
`Lackland`                        `Revolt`                          `Pigtails`                        `Afro`                          
`Bob`                             `Burgundy`                        `Troubadour`                      `GreasySwoop`                   
`Cleopatra`                       `Firestarter`                     `Junkie`                          `ShaveTopBraid`                 
`Keeper`                          `Primal`                          `Artist`                          `Mary`                          
`Princess`                        `Scatman`                         `Cute`                            `Decent`                        
`FancyBun`                        `Mop`                             `Wavy`                            `Frozen`                        
`Bowlcut`                         `Bravo`                           `Recruit`                         `Scrapper`                      
`Rookie`                          `Spikes`                          `Warden`                          `Locks`                         
`Savage`                          `Sticky`                          `Bald`                            `Topdog`                        
`Elisabeth`                       `Lisa`                            `Henry`                           `Richard`                       
```

_余下 22 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
