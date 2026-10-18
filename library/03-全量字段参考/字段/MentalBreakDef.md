# MentalBreakDef

- **所属线**：人物线
- **原版实例数**：34
- **字段路径数**：16
- **资料片**：Anomaly、Biotech、Core、Ideology、Royalty
- **原版出处**：`Anomaly/Defs/MentalStateDefs/MentalStates_Mood.xml`、`Core/Defs/MentalStateDefs/MentalStates_Mood.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<MentalBreakDef Name="BaseAnomalyMentalBreak" Abstract="True">
    <anomalousBreak>true</anomalousBreak>
    <baseCommonality>1</baseCommonality>
  </MentalBreakDef>

  
```

> 来自 `Anomaly/Defs/MentalStateDefs/MentalStates_Mood.xml`，defName = ``，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：DarkVisions / EntityKiller / EntityLiberator
intensity                                      [文本]  例：Extreme / Major / Minor
mentalState                                    [文本]  例：DarkVisions / EntityKiller / EntityLiberator
```

## 三、全量字段表（16 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `anomalousBreak` | 2.9% (1/34) | 布尔 | true |
| `baseCommonality` | 76.5% (26/34) | 数值 | 0 / 0.5 / 0.75 |
| `commonalityFactorPerPopulationCurve` | 8.8% (3/34) | 容器 |  |
| `commonalityFactorPerPopulationCurve/points` | 8.8% (3/34) | 容器 |  |
| `commonalityFactorPerPopulationCurve/points/li` | 17.6% (6/34) | 文本 | (12, 1) / (2, 0.1) / (7, 0) |
| `defName` | 97.1% (33/34) | 文本 | DarkVisions / EntityKiller / EntityLiberator |
| `intensity` | 97.1% (33/34) | 文本 | Extreme / Major / Minor |
| `label` | 32.4% (11/34) | 文本 | dark visions / entity liberator / entity slayer |
| `layerWhitelist` | 2.9% (1/34) | 容器 |  |
| `layerWhitelist/li` | 2.9% (1/34) | 文本 | Surface |
| `mentalState` | 91.2% (31/34) | 文本 | DarkVisions / EntityKiller / EntityLiberator |
| `questLodgersCanDo` | 2.9% (1/34) | 布尔 | false |
| `requiredGene` | 2.9% (1/34) | 文本 | FireTerror |
| `requiredPrecept` | 2.9% (1/34) | 文本 | Inhumanizing_Required |
| `requiredTrait` | 2.9% (1/34) | 文本 | Pyromaniac |
| `workerClass` | 20.6% (7/34) | 文本 | MentalBreakWorker_BingingDrug / MentalBreakWorker_Catatonic / MentalBreakWorker_FireTerror |

## 四、原版 defName 一览（共 34 个，列出前 60）

```text
``                                `Binging_DrugMajor`               `DarkVisions`                     `InsaneRamblings`               
`EntityKiller`                    `EntityLiberator`                 `TerrifyingHallucinations`        `Berserk`                       
`Jailbreaker`                     `Slaughterer`                     `Wander_Psychotic`                `Tantrum`                       
`TargetedTantrum`                 `BedroomTantrum`                  `SadisticRage`                    `CorpseObsession`               
`Binging_Food`                    `Wander_Sad`                      `Wander_OwnRoom`                  `InsultingSpree`                
`TargetedInsultingSpree`          `Rebellion`                       `WildDecree`                      `BerserkShort`                  
`CubeSculpting`                   `FireStartingSpree`               `Binging_DrugExtreme`             `Catatonic`                     
`IdeoChange`                      `FireTerror`                      `HumanityBreak`                   `MurderousRage`                 
`RunWild`                         `GiveUpExit`                    
```
