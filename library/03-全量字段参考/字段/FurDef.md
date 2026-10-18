# FurDef

- **所属线**：人物线
- **原版实例数**：1
- **字段路径数**：10
- **资料片**：Biotech
- **原版出处**：`Biotech/Defs/Misc/FurDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<FurDef>
    <defName>Furskin</defName>
    <noGraphic>true</noGraphic>
    <bodyTypeGraphicPaths>
      <Male>Things/Pawn/Humanlike/Bodies/FurCovered_Male</Male>
      <Female>Things/Pawn/Humanlike/Bodies/FurCovered_Female</Female>
      <Hulk>Things/Pawn/Humanlike/Bodies/FurCovered_Hulk</Hulk>
      <Fat>Things/Pawn/Humanlike/Bodies/FurCovered_Fat</Fat>
      <Thin>Things/Pawn/Humanlike/Bodies/FurCovered_Thin</Thin>
      <Child>Things/Pawn/Humanlike/Bodies/Naked_FurChild</Child>
      <Baby>Things/Pawn/Humanlike/Bodies/Naked_FurChild</Baby><!-- Always covered by swaddled graphic -->
    </bodyTypeGraphicPaths>
  </FurDef>
```

> 来自 `Biotech/Defs/Misc/FurDefs.xml`，defName = `Furskin`，XML 节点数 12（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
bodyTypeGraphicPaths                           [容器]
bodyTypeGraphicPaths/Baby                      [文本]  例：Things/Pawn/Humanlike/Bodies/Naked_FurChild
bodyTypeGraphicPaths/Child                     [文本]  例：Things/Pawn/Humanlike/Bodies/Naked_FurChild
bodyTypeGraphicPaths/Fat                       [文本]  例：Things/Pawn/Humanlike/Bodies/FurCovered_Fat
bodyTypeGraphicPaths/Female                    [文本]  例：Things/Pawn/Humanlike/Bodies/FurCovered_Female
bodyTypeGraphicPaths/Hulk                      [文本]  例：Things/Pawn/Humanlike/Bodies/FurCovered_Hulk
bodyTypeGraphicPaths/Male                      [文本]  例：Things/Pawn/Humanlike/Bodies/FurCovered_Male
bodyTypeGraphicPaths/Thin                      [文本]  例：Things/Pawn/Humanlike/Bodies/FurCovered_Thin
defName                                        [文本]  例：Furskin
noGraphic                                      [布尔]  例：true
```

## 三、全量字段表（10 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `bodyTypeGraphicPaths` | 100.0% (1/1) | 容器 |  |
| `bodyTypeGraphicPaths/Baby` | 100.0% (1/1) | 文本 | Things/Pawn/Humanlike/Bodies/Naked_FurChild |
| `bodyTypeGraphicPaths/Child` | 100.0% (1/1) | 文本 | Things/Pawn/Humanlike/Bodies/Naked_FurChild |
| `bodyTypeGraphicPaths/Fat` | 100.0% (1/1) | 文本 | Things/Pawn/Humanlike/Bodies/FurCovered_Fat |
| `bodyTypeGraphicPaths/Female` | 100.0% (1/1) | 文本 | Things/Pawn/Humanlike/Bodies/FurCovered_Female |
| `bodyTypeGraphicPaths/Hulk` | 100.0% (1/1) | 文本 | Things/Pawn/Humanlike/Bodies/FurCovered_Hulk |
| `bodyTypeGraphicPaths/Male` | 100.0% (1/1) | 文本 | Things/Pawn/Humanlike/Bodies/FurCovered_Male |
| `bodyTypeGraphicPaths/Thin` | 100.0% (1/1) | 文本 | Things/Pawn/Humanlike/Bodies/FurCovered_Thin |
| `defName` | 100.0% (1/1) | 文本 | Furskin |
| `noGraphic` | 100.0% (1/1) | 布尔 | true |

## 四、原版 defName 一览（共 1 个，列出前 60）

```text
`Furskin`                       
```
