# StyleItemCategoryDef

- **所属线**：物品线
- **原版实例数**：12
- **字段路径数**：2
- **资料片**：Anomaly、Biotech、Core
- **原版出处**：`Anomaly/Defs/HairDefs/HairsCultist.xml`、`Core/Defs/Misc/HairDefs/StyleItemCategoryDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<StyleItemCategoryDef>
    <defName>Cultist</defName>
    <label>cultist</label>
  </StyleItemCategoryDef>

  
```

> 来自 `Anomaly/Defs/HairDefs/HairsCultist.xml`，defName = `Cultist`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Cultist / Furskin / Minimal
label                                          [文本]  例：cultist / furskin / minimal
```

## 三、全量字段表（2 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (12/12) | 文本 | Cultist / Furskin / Minimal |
| `label` | 100.0% (12/12) | 文本 | cultist / furskin / minimal |

## 四、原版 defName 一览（共 12 个，列出前 60）

```text
`Cultist`                         `Furskin`                         `Minimal`                         `Tribal`                        
`Cannibal`                        `Punk`                            `Urban`                           `Rural`                         
`Royal`                           `Soldier`                         `Moustache`                       `Misc`                          
```
