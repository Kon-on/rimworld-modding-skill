# ChemicalDef

- **所属线**：物品线
- **原版实例数**：8
- **字段路径数**：18
- **资料片**：Core、Odyssey
- **原版出处**：`Core/Defs/Drugs/GoJuice.xml`、`Core/Defs/Drugs/Ambrosia.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<ChemicalDef>
    <defName>GoJuice</defName>
    <label>go-juice</label>
    <addictionHediff>GoJuiceAddiction</addictionHediff>
    <geneOverdoseChanceFactorResist>0.5</geneOverdoseChanceFactorResist>
    <geneOverdoseChanceFactorImmune>0</geneOverdoseChanceFactorImmune>
  </ChemicalDef>
  
  
```

> 来自 `Core/Defs/Drugs/GoJuice.xml`，defName = `GoJuice`，XML 节点数 6（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Alcohol / Ambrosia / GoJuice
label                                          [文本]  例：alcohol / ambrosia / go-juice
```

## 三、全量字段表（18 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `addictionHediff` | 87.5% (7/8) | 文本 | AlcoholAddiction / AmbrosiaAddiction / GoJuiceAddiction |
| `canBeAddicted` | 12.5% (1/8) | 布尔 | false |
| `canBinge` | 12.5% (1/8) | 布尔 | false |
| `defName` | 100.0% (8/8) | 文本 | Alcohol / Ambrosia / GoJuice |
| `geneOverdoseChanceFactorImmune` | 37.5% (3/8) | 数值 | 0 |
| `geneOverdoseChanceFactorResist` | 37.5% (3/8) | 数值 | 0.5 |
| `generateAddictionGenes` | 37.5% (3/8) | 布尔 | false |
| `geneToleranceBuildupFactorImmune` | 37.5% (3/8) | 数值 | 0 |
| `geneToleranceBuildupFactorResist` | 37.5% (3/8) | 数值 | 0.5 |
| `label` | 100.0% (8/8) | 文本 | alcohol / ambrosia / go-juice |
| `onGeneratedAddictedEvents` | 25.0% (2/8) | 容器 |  |
| `onGeneratedAddictedEvents/li` | 25.0% (2/8) | 容器 |  |
| `onGeneratedAddictedEvents/li/chance` | 25.0% (2/8) | 数值 | 0.15 |
| `onGeneratedAddictedEvents/li/hediff` | 25.0% (2/8) | 文本 | ChemicalDamageSevere / Cirrhosis |
| `onGeneratedAddictedEvents/li/partsToAffect` | 25.0% (2/8) | 容器 |  |
| `onGeneratedAddictedEvents/li/partsToAffect/li` | 25.0% (2/8) | 文本 | Kidney / Liver |
| `onGeneratedAddictedToleranceChance` | 50.0% (4/8) | 数值 | 0.8 |
| `toleranceHediff` | 62.5% (5/8) | 文本 | AlcoholTolerance / AmbrosiaTolerance / PsychiteTolerance |

## 四、原版 defName 一览（共 8 个，列出前 60）

```text
`GoJuice`                         `Luciferium`                      `WakeUp`                          `Psilocap`                      
`Ambrosia`                        `Smokeleaf`                       `Alcohol`                         `Psychite`                      
```
