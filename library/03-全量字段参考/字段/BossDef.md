# BossDef

- **所属线**：世界线
- **原版实例数**：3
- **字段路径数**：3
- **资料片**：Biotech
- **原版出处**：`Biotech/Defs/BossgroupDefs/Bossgroups.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<BossDef>
    <defName>Diabolus</defName>
    <kindDef>Mech_Diabolus</kindDef>
    <appearAfterTicks>7200000</appearAfterTicks><!-- 2 years -->
  </BossDef>

  
```

> 来自 `Biotech/Defs/BossgroupDefs/Bossgroups.xml`，defName = `Diabolus`，XML 节点数 5（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
appearAfterTicks                               [数值]  例：14400000 / 21600000 / 7200000
defName                                        [文本]  例：Apocriton / Diabolus / Warqueen
kindDef                                        [文本]  例：Mech_Apocriton / Mech_Diabolus / Mech_Warqueen
```

## 三、全量字段表（3 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `appearAfterTicks` | 100.0% (3/3) | 数值 | 14400000 / 21600000 / 7200000 |
| `defName` | 100.0% (3/3) | 文本 | Apocriton / Diabolus / Warqueen |
| `kindDef` | 100.0% (3/3) | 文本 | Mech_Apocriton / Mech_Diabolus / Mech_Warqueen |

## 四、原版 defName 一览（共 3 个，列出前 60）

```text
`Diabolus`                        `Warqueen`                        `Apocriton`                     
```
