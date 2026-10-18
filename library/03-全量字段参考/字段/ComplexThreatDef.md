# ComplexThreatDef

- **所属线**：世界线
- **原版实例数**：11
- **字段路径数**：17
- **资料片**：Core、Ideology
- **原版出处**：`Core/Defs/ComplexThreatDefs/ComplexThreats_Misx.xml`、`Ideology/Defs/ComplexThreatDefs/ComplexThreats_Misc.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<ComplexThreatDef Abstract="True" Name="SleepingThreat" ParentName="DelayedThreat">
    <postSpawnPassiveThreatFactor>0.5</postSpawnPassiveThreatFactor>
    <spawnInOtherRoomChance>0.5</spawnInOtherRoomChance>
  </ComplexThreatDef>

  
```

> 来自 `Core/Defs/ComplexThreatDefs/ComplexThreats_Misx.xml`，defName = ``，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

_该类型没有出现率≥90% 的字段（字段高度自由）。_

## 三、全量字段表（17 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `allowPassive` | 18.2% (2/11) | 布尔 | false |
| `defName` | 81.8% (9/11) | 文本 | CryptosleepPods / MechDrop / SleepingInsects |
| `delayChance` | 9.1% (1/11) | 数值 | 0.25 |
| `delayTickOptions` | 9.1% (1/11) | 容器 |  |
| `delayTickOptions/li` | 72.7% (8/11) | 数值 | 10800 / 1800 / 3600 |
| `faction` | 18.2% (2/11) | 文本 | Insect / Mechanoid |
| `fallbackToRoomEnteredTrigger` | 9.1% (1/11) | 布尔 | false |
| `minPoints` | 27.3% (3/11) | 数值 | 100 / 200 |
| `postSpawnPassiveThreatFactor` | 27.3% (3/11) | 数值 | 0.1 / 0.25 / 0.5 |
| `signalActionAmbushType` | 18.2% (2/11) | 文本 | Mechanoids / Normal |
| `spawnAroundComplex` | 9.1% (1/11) | 布尔 | true |
| `spawnInOtherRoomChance` | 36.4% (4/11) | 数值 | 0.5 |
| `threatFactorOverDelayTicksCurve` | 9.1% (1/11) | 容器 |  |
| `threatFactorOverDelayTicksCurve/points` | 9.1% (1/11) | 容器 |  |
| `threatFactorOverDelayTicksCurve/points/li` | 27.3% (3/11) | 文本 | (0, 0) / (1800, 1.2) / (36000, 1.5) |
| `useDropPods` | 9.1% (1/11) | 布尔 | true |
| `workerClass` | 81.8% (9/11) | 文本 | ComplexThreatWorker_Ambush / ComplexThreatWorker_CryptosleepPods / ComplexThreatWorker_SleepingInsects |

## 四、原版 defName 一览（共 11 个，列出前 60）

```text
``                                `RaidTerminal`                    `SecurityCrate`                   `SleepingMechanoids`            
`SleepingInsects`                 `CryptosleepPods`                 `FuelNode`                        `MechDrop`                      
`Infestation`                     `Ambush`                          ``                              
```
