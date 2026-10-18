# CreepjoinerRejectionDef

- **所属线**：世界线
- **原版实例数**：2
- **字段路径数**：8
- **资料片**：Anomaly
- **原版出处**：`Anomaly/Defs/CreepjoinerDefs/Rejections.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<CreepjoinerRejectionDef>
    <defName>Departure</defName>
    <label>departure</label>
    <weight>1</weight>
    <hasLetter>true</hasLetter>
    <letterLabel>{PAWN_nameDef} departure</letterLabel>
    <letterDesc>{PAWN_nameDef} is disappointed by the way that you have treated {PAWN_objective}. {PAWN_pronoun} has decided to leave.</letterDesc>
    <letterDef>NeutralEvent</letterDef>
    <workerType>CreepJoinerWorker_DoDepart</workerType>
  </CreepjoinerRejectionDef>
  
  
```

> 来自 `Anomaly/Defs/CreepjoinerDefs/Rejections.xml`，defName = `Departure`，XML 节点数 9（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：AggressiveRejection / Departure
hasLetter                                      [布尔]  例：true
label                                          [文本]  例：aggressive / departure
letterDef                                      [文本]  例：NeutralEvent / ThreatBig
letterDesc                                     [文本]  例：Upon being rejected, {PAWN_nameDef} flew into a murderous rage and began to atta / {PAWN_nameDef} is disappointed by the way that you have treated {PAWN_objective}
letterLabel                                    [文本]  例：{PAWN_nameDef} departure / {PAWN_nameDef} hostile
weight                                         [数值]  例：1
workerType                                     [文本]  例：CreepJoinerWorker_DoAggressive / CreepJoinerWorker_DoDepart
```

## 三、全量字段表（8 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (2/2) | 文本 | AggressiveRejection / Departure |
| `hasLetter` | 100.0% (2/2) | 布尔 | true |
| `label` | 100.0% (2/2) | 文本 | aggressive / departure |
| `letterDef` | 100.0% (2/2) | 文本 | NeutralEvent / ThreatBig |
| `letterDesc` | 100.0% (2/2) | 文本 | Upon being rejected, {PAWN_nameDef} flew into a murderous rage and began to atta / {PAWN_nameDef} is disappoin |
| `letterLabel` | 100.0% (2/2) | 文本 | {PAWN_nameDef} departure / {PAWN_nameDef} hostile |
| `weight` | 100.0% (2/2) | 数值 | 1 |
| `workerType` | 100.0% (2/2) | 文本 | CreepJoinerWorker_DoAggressive / CreepJoinerWorker_DoDepart |

## 四、原版 defName 一览（共 2 个，列出前 60）

```text
`Departure`                       `AggressiveRejection`           
```
