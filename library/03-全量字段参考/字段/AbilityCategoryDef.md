# AbilityCategoryDef

- **所属线**：人物线
- **原版实例数**：4
- **字段路径数**：2
- **资料片**：Biotech、Royalty
- **原版出处**：`Biotech/Defs/AbilityDefs/Abilities.xml`、`Royalty/Defs/AbilityDefs/AbilityCategories.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<AbilityCategoryDef>
    <defName>Sanguophage</defName>
    <displayOrder>1000</displayOrder>
  </AbilityCategoryDef>

  
```

> 来自 `Biotech/Defs/AbilityDefs/Abilities.xml`，defName = `Sanguophage`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Psychic / Sanguophage / Skip
displayOrder                                   [数值]  例：0 / 1 / 1000
```

## 三、全量字段表（2 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (4/4) | 文本 | Psychic / Sanguophage / Skip |
| `displayOrder` | 100.0% (4/4) | 数值 | 0 / 1 / 1000 |

## 四、原版 defName 一览（共 4 个，列出前 60）

```text
`Sanguophage`                     `WordOf`                          `Psychic`                         `Skip`                          
```
