# TattooDef

- **所属线**：人物线
- **原版实例数**：31
- **字段路径数**：10
- **资料片**：Core、Ideology
- **原版出处**：`Ideology/Defs/TattooDefs/TattooDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<TattooDef>
    <defName>Face_Tiger</defName>
    <label>tiger</label>
    <texPath>Things/Pawn/Humanlike/Tattoos/Face_Tiger/Face_Tiger</texPath>
    <tattooType>Face</tattooType>
    <category>Tribal</category>
    <styleTags>
      <li>TattooFaceTribal</li>
    </styleTags>
  </TattooDef>

  
```

> 来自 `Ideology/Defs/TattooDefs/TattooDefs.xml`，defName = `Face_Tiger`，XML 节点数 8（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
category                                       [文本]  例：Cannibal / Minimal / Punk
defName                                        [文本]  例：Face_Cobweb / Face_Tiger / NoTattoo_Body
label                                          [文本]  例：cobweb / eclipse / none
styleTags                                      [容器]
styleTags/li                                   [文本]  例：NoTattoo / TattooBodyTribal / TattooFacePunk
tattooType                                     [文本]  例：Body / Face
texPath                                        [文本]  例：Things/Mote/Transparent / Things/Pawn/Humanlike/Tattoos/Face_Cobweb/FaceTattooCobweb / Things/Pawn/Humanlike/Tattoos/Face_Eclipse/FaceTattooEclipse
```

## 三、全量字段表（10 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `category` | 100.0% (31/31) | 文本 | Cannibal / Minimal / Punk |
| `defName` | 100.0% (31/31) | 文本 | Face_Cobweb / Face_Tiger / NoTattoo_Body |
| `iconPath` | 9.7% (3/31) | 文本 | Things/Mote/Transparent / Things/Pawn/Humanlike/Tattoos/Body_Wings/TattooWings_north |
| `label` | 100.0% (31/31) | 文本 | cobweb / eclipse / none |
| `noGraphic` | 6.5% (2/31) | 布尔 | true |
| `styleTags` | 100.0% (31/31) | 容器 |  |
| `styleTags/li` | 100.0% (31/31) | 文本 | NoTattoo / TattooBodyTribal / TattooFacePunk |
| `tattooType` | 100.0% (31/31) | 文本 | Body / Face |
| `texPath` | 100.0% (31/31) | 文本 | Things/Mote/Transparent / Things/Pawn/Humanlike/Tattoos/Face_Cobweb/FaceTattooCobweb / Things/Pawn/Humanlike/T |
| `visibleNorth` | 25.8% (8/31) | 布尔 | false |

## 四、原版 defName 一览（共 31 个，列出前 60）

```text
`Face_Tiger`                      `Face_Eclipse`                    `Face_Line`                       `Body_Tiger`                    
`Body_Buttons`                    `Body_Rings`                      `Face_Love`                       `Face_Stars`                    
`Body_Heart`                      `Body_Cross`                      `Body_Jester`                     `Body_Moon`                     
`Body_Power`                      `Body_Royal`                      `Body_Skull`                      `Body_Scar`                     
`Body_Skeleton`                   `Body_Spike`                      `Body_Insect`                     `Body_Sun`                      
`Face_Cobweb`                     `Face_Oracle`                     `Face_Pantheon`                   `Face_Warpaint`                 
`Face_Worried`                    `Face_Tear`                       `Face_Headshot`                   `Body_Wings`                    
`Face_Spider`                     `NoTattoo_Face`                   `NoTattoo_Body`                 
```
