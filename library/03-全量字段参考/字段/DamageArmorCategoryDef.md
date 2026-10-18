# DamageArmorCategoryDef

- **所属线**：物品线
- **原版实例数**：3
- **字段路径数**：3
- **资料片**：Core
- **原版出处**：`Core/Defs/Misc/DamageArmorCategoryDef/DamageArmorCategoryDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<DamageArmorCategoryDef>
    <defName>Heat</defName>
    <armorRatingStat>ArmorRating_Heat</armorRatingStat>
  </DamageArmorCategoryDef>
```

> 来自 `Core/Defs/Misc/DamageArmorCategoryDef/DamageArmorCategoryDefs.xml`，defName = `Heat`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
armorRatingStat                                [文本]  例：ArmorRating_Blunt / ArmorRating_Heat / ArmorRating_Sharp
defName                                        [文本]  例：Blunt / Heat / Sharp
```

## 三、全量字段表（3 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `armorRatingStat` | 100.0% (3/3) | 文本 | ArmorRating_Blunt / ArmorRating_Heat / ArmorRating_Sharp |
| `defName` | 100.0% (3/3) | 文本 | Blunt / Heat / Sharp |
| `multStat` | 66.7% (2/3) | 文本 | BluntDamageMultiplier / SharpDamageMultiplier |

## 四、原版 defName 一览（共 3 个，列出前 60）

```text
`Heat`                            `Sharp`                           `Blunt`                         
```
