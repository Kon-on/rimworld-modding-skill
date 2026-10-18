# PawnGroupKindDef

- **所属线**：世界线
- **原版实例数**：20
- **字段路径数**：2
- **资料片**：Anomaly、Core、Ideology
- **原版出处**：`Anomaly/Defs/PawnGroupKindDefs/PawnGroupKinds.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<PawnGroupKindDef>
    <defName>Shamblers</defName>
    <workerClass>PawnGroupKindWorker_Shamblers</workerClass>
  </PawnGroupKindDef>
  
  
```

> 来自 `Anomaly/Defs/PawnGroupKindDefs/PawnGroupKinds.xml`，defName = `Shamblers`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Fleshbeasts / FleshbeastsWithDreadmeld / Shamblers
workerClass                                    [文本]  例：PawnGroupKindWorker_Normal / PawnGroupKindWorker_Shamblers / PawnGroupKindWorker_Trader
```

## 三、全量字段表（2 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (20/20) | 文本 | Fleshbeasts / FleshbeastsWithDreadmeld / Shamblers |
| `workerClass` | 100.0% (20/20) | 文本 | PawnGroupKindWorker_Normal / PawnGroupKindWorker_Shamblers / PawnGroupKindWorker_Trader |

## 四、原版 defName 一览（共 20 个，列出前 60）

```text
`Shamblers`                       `Fleshbeasts`                     `FleshbeastsWithDreadmeld`        `Sightstealers`                 
`Metalhorrors`                    `PsychicRitualSiege`              `Gorehulks`                       `Devourers`                     
`Noctols`                         `SightstealersNoctols`            `Chimeras`                        `Combat`                        
`Trader`                          `Peaceful`                        `Settlement`                      `Settlement_RangedOnly`         
`Miners`                          `Hunters`                         `Loggers`                         `Farmers`                       
```
