# CreepJoinerAggressiveDef

- **所属线**：世界线
- **原版实例数**：3
- **字段路径数**：11
- **资料片**：Anomaly
- **原版出处**：`Anomaly/Defs/CreepjoinerDefs/Aggressive.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<CreepJoinerAggressiveDef>
    <defName>Assault</defName>
    <label>basic assault</label>
    <weight>3</weight>
    <workerType>CreepJoinerWorker_AggressionBasic</workerType>
    <hasMessage>true</hasMessage>
    <message>{PAWN_nameDef} has become hostile!</message>
  </CreepJoinerAggressiveDef>
  
  
```

> 来自 `Anomaly/Defs/CreepjoinerDefs/Aggressive.xml`，defName = `Assault`，XML 节点数 7（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Assault / FleshbeastEmergence / SightstealerAttack
label                                          [文本]  例：basic assault / fleshbeast emergence / sightstealer attack
weight                                         [数值]  例：1 / 3
workerType                                     [文本]  例：CreepJoinerWorker_AggressionBasic / CreepJoinerWorker_FleshbeastEmergence / CreepJoinerWorker_SightstealerAttack
```

## 三、全量字段表（11 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (3/3) | 文本 | Assault / FleshbeastEmergence / SightstealerAttack |
| `hasLetter` | 66.7% (2/3) | 布尔 | true |
| `hasMessage` | 33.3% (1/3) | 布尔 | true |
| `label` | 100.0% (3/3) | 文本 | basic assault / fleshbeast emergence / sightstealer attack |
| `letterDef` | 66.7% (2/3) | 文本 | ThreatBig |
| `letterDesc` | 66.7% (2/3) | 文本 | {PAWN_nameDef} has let out a twisted half-human scream.\n\nIn the distance, you  / {PAWN_nameDef} has transfor |
| `letterLabel` | 66.7% (2/3) | 文本 | {PAWN_nameDef} transformed / {PAWN_nameDef}'s howl |
| `message` | 33.3% (1/3) | 文本 | {PAWN_nameDef} has become hostile! |
| `minCombatPoints` | 33.3% (1/3) | 数值 | 150 |
| `weight` | 100.0% (3/3) | 数值 | 1 / 3 |
| `workerType` | 100.0% (3/3) | 文本 | CreepJoinerWorker_AggressionBasic / CreepJoinerWorker_FleshbeastEmergence / CreepJoinerWorker_SightstealerAtta |

## 四、原版 defName 一览（共 3 个，列出前 60）

```text
`Assault`                         `SightstealerAttack`              `FleshbeastEmergence`           
```
