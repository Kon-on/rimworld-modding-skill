# PitGateIncidentDef

- **所属线**：世界线
- **原版实例数**：1
- **字段路径数**：10
- **资料片**：Anomaly
- **原版出处**：`Anomaly/Defs/Misc/PitGateIncidentDefs/PitGateIncidentDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<PitGateIncidentDef>
    <defName>FleshbeastEmergence</defName>
    <label>fleshbeast emergence</label>
    <workerClass>PitGateIncidentWorker_Fleshbeast</workerClass>
    <baseChance>1</baseChance>
    <durationRangeTicks>600</durationRangeTicks> <!-- 10 seconds -->
    <usesThreatPoints>true</usesThreatPoints>
    <disableEnteringTicks>600</disableEnteringTicks> <!-- 10 seconds -->
    <disableEnteringReason>fleshbeasts are emerging</disableEnteringReason>
    <letterLabel>Fleshbeast emergence</letterLabel>
    <letterText>A horde of fleshbeasts is emerging from the pit gate. Get ready!</letterText>
  </PitGateIncidentDef>
```

> 来自 `Anomaly/Defs/Misc/PitGateIncidentDefs/PitGateIncidentDefs.xml`，defName = `FleshbeastEmergence`，XML 节点数 13（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
baseChance                                     [数值]  例：1
defName                                        [文本]  例：FleshbeastEmergence
disableEnteringReason                          [文本]  例：fleshbeasts are emerging
disableEnteringTicks                           [数值]  例：600
durationRangeTicks                             [数值]  例：600
label                                          [文本]  例：fleshbeast emergence
letterLabel                                    [文本]  例：Fleshbeast emergence
letterText                                     [文本]  例：A horde of fleshbeasts is emerging from the pit gate. Get ready!
usesThreatPoints                               [布尔]  例：true
workerClass                                    [文本]  例：PitGateIncidentWorker_Fleshbeast
```

## 三、全量字段表（10 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `baseChance` | 100.0% (1/1) | 数值 | 1 |
| `defName` | 100.0% (1/1) | 文本 | FleshbeastEmergence |
| `disableEnteringReason` | 100.0% (1/1) | 文本 | fleshbeasts are emerging |
| `disableEnteringTicks` | 100.0% (1/1) | 数值 | 600 |
| `durationRangeTicks` | 100.0% (1/1) | 数值 | 600 |
| `label` | 100.0% (1/1) | 文本 | fleshbeast emergence |
| `letterLabel` | 100.0% (1/1) | 文本 | Fleshbeast emergence |
| `letterText` | 100.0% (1/1) | 文本 | A horde of fleshbeasts is emerging from the pit gate. Get ready! |
| `usesThreatPoints` | 100.0% (1/1) | 布尔 | true |
| `workerClass` | 100.0% (1/1) | 文本 | PitGateIncidentWorker_Fleshbeast |

## 四、原版 defName 一览（共 1 个，列出前 60）

```text
`FleshbeastEmergence`           
```
