# BeardDef

- **所属线**：人物线
- **原版实例数**：42
- **字段路径数**：11
- **资料片**：Biotech、Core
- **原版出处**：`Biotech/Defs/BeardDefs/BeardDefs.xml`、`Core/Defs/BeardDefs/BeardDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<BeardDef ParentName="FurskinBeardBase">
    <defName>FurskinCurlyMoustache</defName>
    <label>curly moustache</label>
    <texPath>Things/Pawn/Humanlike/Beards/BeardFurskinCurlyMoustache</texPath>
  </BeardDef>

  
```

> 来自 `Biotech/Defs/BeardDefs/BeardDefs.xml`，defName = `FurskinCurlyMoustache`，XML 节点数 4（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：BeardFurskinKnots / BeardFurskinMegabraid / BeardFurskinMonkey
label                                          [文本]  例：curly moustache / knots / megabraid
styleTags/li                                   [文本]  例：BeardPunk / BeardShort / Furskin
texPath                                        [文本]  例：Things/Pawn/Humanlike/Beards/BeardFurskinCurlyMoustache / Things/Pawn/Humanlike/Beards/BeardFurskinKnots / Things/Pawn/Humanlike/Beards/BeardFurskinMegabraid
```

## 三、全量字段表（11 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `category` | 76.2% (32/42) | 文本 | Furskin / Minimal / Punk |
| `defName` | 97.6% (41/42) | 文本 | BeardFurskinKnots / BeardFurskinMegabraid / BeardFurskinMonkey |
| `label` | 97.6% (41/42) | 文本 | curly moustache / knots / megabraid |
| `noGraphic` | 2.4% (1/42) | 布尔 | true |
| `offsetNarrowEast` | 9.5% (4/42) | 文本 | (-0.01,0,0.03) / (-0.04,0,0) / (-0.05,0,0) |
| `offsetNarrowSouth` | 7.1% (3/42) | 文本 | (0,0,0.02) / (0,0,0.05) |
| `requiredGene` | 2.4% (1/42) | 文本 | Furskin |
| `styleGender` | 71.4% (30/42) | 文本 | Male |
| `styleTags` | 76.2% (32/42) | 容器 |  |
| `styleTags/li` | 159.5% (67/42) | 文本 | BeardPunk / BeardShort / Furskin |
| `texPath` | 95.2% (40/42) | 文本 | Things/Pawn/Humanlike/Beards/BeardFurskinCurlyMoustache / Things/Pawn/Humanlike/Beards/BeardFurskinKnots / Thi |

## 四、原版 defName 一览（共 42 个，列出前 60）

```text
`FurskinCurlyMoustache`           `BeardFurskinKnots`               `BeardFurskinMegabraid`           `BeardFurskinMonkey`            
`BeardFurskinMoustache`           `BeardFurskinScruffy`             `BeardFurskinSenile`              `BeardFurskinSideChops`         
`BeardFurskinSideTufts`           `BeardFurskinStrongChops`         ``                                `NoBeard`                       
`French`                          `Full`                            `Classy`                          `MuttonChops`                   
`SideWhiskers`                    `Anchor`                          `Norse`                           `Circle`                        
`Curtain`                         `StacheAndChops`                  `Fork`                            `Braided`                       
`Lincoln`                         `Machete`                         `Moustache`                       `OldDutch`                      
`VanDyke`                         `Bushy`                           `Boxed`                           `BeardCurly`                    
`Ducktail`                        `LongDutch`                       `TriBraid`                        `Seer`                          
`SoulPatch`                       `Urist`                           `Wizard`                          `Goatee`                        
`Stubble`                         `BushyStyled`                   
```
