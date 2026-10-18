# HediffGiverSetDef

- **所属线**：人物线
- **原版实例数**：4
- **字段路径数**：24
- **资料片**：Anomaly、Core
- **原版出处**：`Anomaly/Defs/HediffGiverSetDefs/HediffGiverSetDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<HediffGiverSetDef>
    <defName>AnomalyEntity</defName>
    <hediffGivers>
      <li Class="HediffGiver_Bleeding">
        <hediff>BloodLoss</hediff>
      </li>
    </hediffGivers>
  </HediffGiverSetDef>
```

> 来自 `Anomaly/Defs/HediffGiverSetDefs/HediffGiverSetDefs.xml`，defName = `AnomalyEntity`，XML 节点数 5（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：AnomalyEntity / Fleshbeast / Human
hediffGivers                                   [容器]
hediffGivers/li                                [容器]
hediffGivers/li/ageFractionChanceCurve         [容器]
hediffGivers/li/ageFractionChanceCurve/points  [容器]
hediffGivers/li/ageFractionChanceCurve/points/li [文本]  例：(0.25, 0) / (0.3, 0.001) / (0.5, 0.00145)
hediffGivers/li/hediff                         [文本]  例：BloodLoss / HeartArteryBlockage / Heatstroke
hediffGivers/li/partsToAffect                  [容器]
hediffGivers/li/partsToAffect/li               [文本]  例：Brain / Ear / Heart
```

## 三、全量字段表（24 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (4/4) | 文本 | AnomalyEntity / Fleshbeast / Human |
| `hediffGivers` | 100.0% (4/4) | 容器 |  |
| `hediffGivers/li` | 525.0% (21/4) | 容器 |  |
| `hediffGivers/li/ageFractionChanceCurve` | 225.0% (9/4) | 容器 |  |
| `hediffGivers/li/ageFractionChanceCurve/points` | 225.0% (9/4) | 容器 |  |
| `hediffGivers/li/ageFractionChanceCurve/points/li` | 850.0% (34/4) | 文本 | (0.25, 0) / (0.3, 0.001) / (0.5, 0.00145) |
| `hediffGivers/li/ageFractionMtbDaysCurve` | 25.0% (1/4) | 容器 |  |
| `hediffGivers/li/ageFractionMtbDaysCurve/points` | 25.0% (1/4) | 容器 |  |
| `hediffGivers/li/ageFractionMtbDaysCurve/points/li` | 75.0% (3/4) | 文本 | (0.6, 9999999) / (0.8, 2500) / (1, 300) |
| `hediffGivers/li/allowOnBeggars` | 50.0% (2/4) | 布尔 | false |
| `hediffGivers/li/allowOnLodgers` | 50.0% (2/4) | 布尔 | false |
| `hediffGivers/li/allowOnQuestReservedPawns` | 50.0% (2/4) | 布尔 | false |
| `hediffGivers/li/allowOnQuestRewardPawns` | 50.0% (2/4) | 布尔 | false |
| `hediffGivers/li/averageSeverityPerDayBeforeGeneration` | 75.0% (3/4) | 数值 | 0.00025 / 0.0005 / 0.001 |
| `hediffGivers/li/canAffectAnyLivePart` | 25.0% (1/4) | 布尔 | true |
| `hediffGivers/li/chancePerDamagePct` | 25.0% (1/4) | 数值 | 0.12 |
| `hediffGivers/li/countToAffect` | 75.0% (3/4) | 数值 | 2 |
| `hediffGivers/li/hediff` | 475.0% (19/4) | 文本 | BloodLoss / HeartArteryBlockage / Heatstroke |
| `hediffGivers/li/hediffInsectoid` | 50.0% (2/4) | 文本 | HypothermicSlowdown |
| `hediffGivers/li/letter` | 25.0% (1/4) | 文本 | [PAWN_nameDef]'s brain injury has caused [PAWN_objective] to develop strange sav |
| `hediffGivers/li/letterLabel` | 25.0% (1/4) | 文本 | Trauma savant |
| `hediffGivers/li/minPlayerPopulation` | 25.0% (1/4) | 数值 | 2 |
| `hediffGivers/li/partsToAffect` | 250.0% (10/4) | 容器 |  |
| `hediffGivers/li/partsToAffect/li` | 250.0% (10/4) | 文本 | Brain / Ear / Heart |

## 四、原版 defName 一览（共 4 个，列出前 60）

```text
`AnomalyEntity`                   `Human`                           `Fleshbeast`                      `OrganicStandard`               
```
