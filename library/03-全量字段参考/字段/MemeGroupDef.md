# MemeGroupDef

- **所属线**：理念线
- **原版实例数**：7
- **字段路径数**：5
- **资料片**：Ideology
- **原版出处**：`Ideology/Defs/MemeDefs/Memes_Structures_Basic.xml`、`Ideology/Defs/MemeDefs/Memes_Individualism.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<MemeGroupDef>
    <defName>Theist_Embodied</defName>
    <drawOffset>(0.62, 0)</drawOffset>
  </MemeGroupDef>

  
```

> 来自 `Ideology/Defs/MemeDefs/Memes_Structures_Basic.xml`，defName = `Theist_Embodied`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：GenderSupremacy / GroupRelation / Individualism
drawOffset                                     [文本]  例：(0.05, 0.46) / (0.09, 0.23) / (0.3, 0)
```

## 三、全量字段表（5 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (7/7) | 文本 | GenderSupremacy / GroupRelation / Individualism |
| `drawOffset` | 100.0% (7/7) | 文本 | (0.05, 0.46) / (0.09, 0.23) / (0.3, 0) |
| `maxRows` | 71.4% (5/7) | 数值 | 1 / 2 |
| `renderOrder` | 42.9% (3/7) | 数值 | 1000 / 1900 / 2000 |
| `renderWithGap` | 14.3% (1/7) | 布尔 | true |

## 四、原版 defName 一览（共 7 个，列出前 60）

```text
`Theist_Embodied`                 `Theist_Abstract`                 `GroupRelation`                   `Individualism`                 
`GenderSupremacy`                 `Primacy`                         `Misc`                          
```
