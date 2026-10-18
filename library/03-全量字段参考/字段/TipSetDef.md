# TipSetDef

- **所属线**：系统线
- **原版实例数**：6
- **字段路径数**：3
- **资料片**：Anomaly、Biotech、Core、Ideology、Odyssey、Royalty
- **原版出处**：`Anomaly/Defs/TipSetDefs/Tips.xml`、`Biotech/Defs/TipSetDefs/Tips.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<TipSetDef>
    <defName>AnomalyTips</defName>
    <tips>

      <li TKey="AbductionPsychicRitual">The skip abduction psychic ritual prioritizes nearby enemies, letting you abduct raiders on your map.</li>
      <li TKey="BrainwipeUnwaveringlyLoyal">Have an unwaveringly loyal prisoner? The brainwipe psychic ritual will make them recruitable.</li>
      <li TKey="AdvancedProjectRollover">Want to finish a basic Anomaly research project faster? Advanced entities will contribute to your current basic research project if you don't have an active advanced project.</li>

    </tips>
  </TipSetDef>
```

> 来自 `Anomaly/Defs/TipSetDefs/Tips.xml`，defName = `AnomalyTips`，XML 节点数 6（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：AnomalyTips / BiotechTips / GameplayTips
tips                                           [容器]
tips/li                                        [文本]  例：Have an unwaveringly loyal prisoner? The brainwipe psychic ritual will make them / Mechanitors can summon powerful mechs. Fight them yourself - or draw them into y / The skip abduction psychic ritual prioritizes nearby enemies, letting you abduct
```

## 三、全量字段表（3 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (6/6) | 文本 | AnomalyTips / BiotechTips / GameplayTips |
| `tips` | 100.0% (6/6) | 容器 |  |
| `tips/li` | 2116.7% (127/6) | 文本 | Have an unwaveringly loyal prisoner? The brainwipe psychic ritual will make them / Mechanitors can summon powe |

## 四、原版 defName 一览（共 6 个，列出前 60）

```text
`AnomalyTips`                     `IdeoligionTips`                  `OdysseyTips`                     `BiotechTips`                   
`RoyaltyTips`                     `GameplayTips`                  
```
