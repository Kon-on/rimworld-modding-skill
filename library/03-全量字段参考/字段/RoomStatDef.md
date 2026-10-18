# RoomStatDef

- **所属线**：世界线
- **原版实例数**：13
- **字段路径数**：15
- **资料片**：Biotech、Core、Ideology
- **原版出处**：`Core/Defs/Rooms/RoomStats.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<RoomStatDef>
    <defName>ReadingBonus</defName>
    <label>reading bonus</label>
    <workerClass>RoomStatWorker_ReadingBonus</workerClass>
    <roomlessScore>1</roomlessScore>
    <updatePriority>0</updatePriority>
    <isHidden>true</isHidden>
  </RoomStatDef>
  
  
```

> 来自 `Core/Defs/Rooms/RoomStats.xml`，defName = `ReadingBonus`，XML 节点数 7（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
curve/points/li                                [文本]  例：( 0.0, 1.00 ) / ( 1.0, 1.15 ) / (-2.5, 0.85 )
defName                                        [文本]  例：AssemblySpeedFactor / Impressiveness / Space
label                                          [文本]  例：impressiveness / space / wealth
roomlessScore                                  [数值]  例：0 / 0.75 / 1
scoreStages/li                                 [容器]
scoreStages/li/label                           [文本]  例：extremely impressive / unbelievably impressive / very impressive
scoreStages/li/minScore                        [数值]  例：120 / 170 / 240
updatePriority                                 [数值]  例：0 / 1 / 2
workerClass                                    [文本]  例：RoomStatWorker_FromStatByCurve / RoomStatWorker_Impressiveness / RoomStatWorker_Space
```

## 三、全量字段表（15 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `curve` | 53.8% (7/13) | 容器 |  |
| `curve/points` | 53.8% (7/13) | 容器 |  |
| `curve/points/li` | 192.3% (25/13) | 文本 | ( 0.0, 1.00 ) / ( 1.0, 1.15 ) / (-2.5, 0.85 ) |
| `defName` | 100.0% (13/13) | 文本 | AssemblySpeedFactor / Impressiveness / Space |
| `displayRounded` | 23.1% (3/13) | 布尔 | true |
| `inputStat` | 53.8% (7/13) | 文本 | Cleanliness / Impressiveness |
| `isHidden` | 61.5% (8/13) | 布尔 | true |
| `label` | 100.0% (13/13) | 文本 | impressiveness / space / wealth |
| `roomlessScore` | 100.0% (13/13) | 数值 | 0 / 0.75 / 1 |
| `scoreStages` | 38.5% (5/13) | 容器 |  |
| `scoreStages/li` | 300.0% (39/13) | 容器 |  |
| `scoreStages/li/label` | 300.0% (39/13) | 文本 | extremely impressive / unbelievably impressive / very impressive |
| `scoreStages/li/minScore` | 261.5% (34/13) | 数值 | 120 / 170 / 240 |
| `updatePriority` | 100.0% (13/13) | 数值 | 0 / 1 / 2 |
| `workerClass` | 100.0% (13/13) | 文本 | RoomStatWorker_FromStatByCurve / RoomStatWorker_Impressiveness / RoomStatWorker_Space |

## 四、原版 defName 一览（共 13 个，列出前 60）

```text
`ReadingBonus`                    `GraveVisitingJoyGainFactor`      `FoodPoisonChance`                `AssemblySpeedFactor`           
`InfectionChanceFactor`           `SurgerySuccessChanceCleanlinessFactor`  `ResearchSpeedFactor`             `BiosculpterPodSpeedFactor`     
`Cleanliness`                     `Space`                           `Beauty`                          `Wealth`                        
`Impressiveness`                
```
