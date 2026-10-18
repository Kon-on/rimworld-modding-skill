# NeedDef

- **所属线**：人物线
- **原版实例数**：25
- **字段路径数**：30
- **资料片**：Biotech、Core、Ideology、Royalty
- **原版出处**：`Core/Defs/Drugs/DrugBases.xml`、`Biotech/Defs/NeedDefs/Needs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<NeedDef Name="DrugAddictionNeedBase" Abstract="True">
    <onlyIfCausedByHediff>true</onlyIfCausedByHediff>
    <tutorHighlightTag>NeedAddiction</tutorHighlightTag>
    <showForCaravanMembers>true</showForCaravanMembers>
  </NeedDef>
  
```

> 来自 `Core/Defs/Drugs/DrugBases.xml`，defName = ``，XML 节点数 4（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Deathrest / KillThirst / Learning
label                                          [文本]  例：deathrest / kill satiety / learning
needClass                                      [文本]  例：Need_Deathrest / Need_KillThirst / Need_Learning
```

## 三、全量字段表（30 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `baseLevel` | 20.0% (5/25) | 数值 | 0 / 0.01 / 0.32 |
| `colonistAndPrisonersOnly` | 32.0% (8/25) | 布尔 | true |
| `colonistsOnly` | 8.0% (2/25) | 布尔 | true |
| `defName` | 96.0% (24/25) | 文本 | Deathrest / KillThirst / Learning |
| `description` | 88.0% (22/25) | 文本 | Babies need to be played with by adults. If they aren't played with, they will b / Children need new lessons a |
| `developmentalStageFilter` | 28.0% (7/25) | 文本 | Adult / Baby / Baby, Child, Adult |
| `fallPerDay` | 20.0% (5/25) | 数值 | 0 / 0.071 / 0.15 |
| `freezeInMentalState` | 4.0% (1/25) | 布尔 | true |
| `freezeWhileSleeping` | 32.0% (8/25) | 布尔 | true |
| `label` | 92.0% (23/25) | 文本 | deathrest / kill satiety / learning |
| `listPriority` | 84.0% (21/25) | 数值 | 10000 / 500 / 550 |
| `major` | 32.0% (8/25) | 布尔 | true |
| `minIntelligence` | 44.0% (11/25) | 文本 | Humanlike / ToolUser |
| `needClass` | 96.0% (24/25) | 文本 | Need_Deathrest / Need_KillThirst / Need_Learning |
| `neverOnPrisoner` | 4.0% (1/25) | 布尔 | true |
| `neverOnSlave` | 4.0% (1/25) | 布尔 | true |
| `nullifyingPrecepts` | 4.0% (1/25) | 容器 |  |
| `nullifyingPrecepts/li` | 4.0% (1/25) | 文本 | Comfort_Ignored |
| `onlyIfCausedByGene` | 12.0% (3/25) | 布尔 | true |
| `onlyIfCausedByHediff` | 8.0% (2/25) | 布尔 | true |
| `onlyIfCausedByIdeo` | 4.0% (1/25) | 布尔 | true |
| `onlyIfCausedByTrait` | 4.0% (1/25) | 布尔 | true |
| `playerMechsOnly` | 4.0% (1/25) | 布尔 | true |
| `seekerFallPerHour` | 16.0% (4/25) | 数值 | 0.04 / 0.08 / 0.90 |
| `seekerRisePerHour` | 16.0% (4/25) | 数值 | 0.12 / 0.32 / 0.60 |
| `showForCaravanMembers` | 20.0% (5/25) | 布尔 | true |
| `showOnNeedList` | 16.0% (4/25) | 布尔 | false / true |
| `showUnitTicks` | 4.0% (1/25) | 布尔 | true |
| `slavesOnly` | 4.0% (1/25) | 布尔 | true |
| `tutorHighlightTag` | 4.0% (1/25) | 文本 | NeedAddiction |

## 四、原版 defName 一览（共 25 个，列出前 60）

```text
``                                `Authority`                       `Chemical_Alcohol`                `Chemical_Ambrosia`             
`Chemical_Psychite`               `Chemical_Smokeleaf`              `Chemical_GoJuice`                `Chemical_WakeUp`               
`Chemical_Luciferium`             `Suppression`                     `KillThirst`                      `Learning`                      
`Play`                            `Rest`                            `Outdoors`                        `Deathrest`                     
`Food`                            `DrugDesire`                      `RoomSize`                        `MechEnergy`                    
`Beauty`                          `Comfort`                         `Indoors`                         `Joy`                           
`Mood`                          
```
