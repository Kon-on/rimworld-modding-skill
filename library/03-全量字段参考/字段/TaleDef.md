# TaleDef

- **所属线**：世界线
- **原版实例数**：101
- **字段路径数**：21
- **资料片**：Anomaly、Biotech、Core、Odyssey、Royalty
- **原版出处**：`Core/Defs/TaleDefs/Tales_NoPawn.xml`、`Core/Defs/TaleDefs/Tales_Incident.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<TaleDef>
    <defName>MajorThreat</defName>
    <taleClass>Tale</taleClass>
    <type>PermanentHistorical</type>
    <usableForArt>false</usableForArt>
    <historyGraphColor>(0.8, 0.45, 0.45)</historyGraphColor>
  </TaleDef>
  
  
```

> 来自 `Core/Defs/TaleDefs/Tales_NoPawn.xml`，defName = `MajorThreat`，XML 节点数 6（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
baseInterest                                   [数值]  例：1 / 20 / 3.5
defName                                        [文本]  例：DeathPall / HealedMe / MutatedMyArm
label                                          [文本]  例：death pall / healed me / mutated my arm
rulePack                                       [容器]
rulePack/rulesStrings                          [容器]
rulePack/rulesStrings/li                       [文本]  例：image->[STUDIER_nameFull] carefully examining [ENTITY_nameDef] [circumstance_gro / image->[STUDIER_nameFull] conducting experiments, seeking to understand the secr / image->[STUDIER_nameFull] striving to comprehend the nature of [ENTITY_nameDef] 
taleClass                                      [文本]  例：Tale_DoublePawn / Tale_DoublePawnKilledBy / Tale_SinglePawn
type                                           [文本]  例：Expirable / PermanentHistorical / Volatile
```

## 三、全量字段表（21 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `baseInterest` | 91.1% (92/101) | 数值 | 1 / 20 / 3.5 |
| `colonistOnly` | 1.0% (1/101) | 布尔 | false |
| `defName` | 100.0% (101/101) | 文本 | DeathPall / HealedMe / MutatedMyArm |
| `defSymbol` | 20.8% (21/101) | 文本 | CAPACITY / MATERIAL / TRAINABLE |
| `defType` | 5.9% (6/101) | 文本 | HediffDef / PawnCapacityDef / SkillDef |
| `expireDays` | 9.9% (10/101) | 数值 | 20 / 50 / 60 |
| `firstPawnSymbol` | 39.6% (40/101) | 文本 | CAPTURER / HEALER / KILLER |
| `historyGraphColor` | 3.0% (3/101) | 文本 | (0.46, 0.98, 0.97) / (0.8, 0.45, 0.45) / (1,1,1) |
| `ignoreChance` | 4.0% (4/101) | 数值 | 0.5 |
| `label` | 98.0% (99/101) | 文本 | death pall / healed me / mutated my arm |
| `maxPerPawn` | 9.9% (10/101) | 数值 | 1 / 2 |
| `rulePack` | 91.1% (92/101) | 容器 |  |
| `rulePack/include` | 2.0% (2/101) | 容器 |  |
| `rulePack/include/li` | 2.0% (2/101) | 文本 | Gathering_Concert |
| `rulePack/rulesStrings` | 91.1% (92/101) | 容器 |  |
| `rulePack/rulesStrings/li` | 1749.5% (1767/101) | 文本 | image->[STUDIER_nameFull] carefully examining [ENTITY_nameDef] [circumstance_gro / image->[STUDIER_nameFull] c |
| `secondPawnSymbol` | 38.6% (39/101) | 文本 | CHILD / ENTITY / HEALED |
| `taleClass` | 100.0% (101/101) | 文本 | Tale_DoublePawn / Tale_DoublePawnKilledBy / Tale_SinglePawn |
| `type` | 100.0% (101/101) | 文本 | Expirable / PermanentHistorical / Volatile |
| `usableForArt` | 8.9% (9/101) | 布尔 | false |
| `usableWithChildren` | 2.0% (2/101) | 布尔 | false |

## 四、原版 defName 一览（共 101 个，列出前 60）

```text
`MajorThreat`                     `TileSettled`                     `ButcheredHumanlikeCorpse`        `HealedMe`                      
`MutatedMyArm`                    `KilledChild`                     `KilledColonist`                  `KilledColonyAnimal`            
`DefeatedHostileFactionLeader`    `ClosedTheVoid`                   `EmbracedTheVoid`                 `HeldConcert`                   
`DeathPall`                       `ReadBook`                        `UnnaturalDarkness`               `PerformedPsychicRitual`        
`NoxiousHaze`                     `BondedWithAnimal`                `CollapseDodged`                  `AttendedConcert`               
`StudiedEntity`                   `Meditated`                       `BuiltSnowman`                    `StruckMineable`                
`FinishedResearchProject`         `Hunted`                          `TradedWith`                      `Exhausted`                     
`Eclipse`                         `Prayed`                          `EnteredCryptosleep`              `DidSurgery`                    
`Breakup`                         `VolcanicWinter`                  `CompletedLongConstructionProject`  `CompletedLongCraftingProject`  
`CaravanFormed`                   `CaravanAssaultSuccessful`        `Recruited`                       `TamedAnimal`                   
`BecameLover`                     `Marriage`                        `CaravanAmbushedByManhunter`      `AttendedParty`                 
`PutIntoCryptosleep`              `IncreasedMenagerie`              `CaravanRemoteMining`             `HypothermiaRevealed`           
`GaveBirth`                       `ToxicFallout`                    `Aurora`                          `MinedValuable`                 
`Stripped`                        `GainedMasterSkillWithoutPassion`  `Vomited`                         `HeatstrokeRevealed`            
`CaravanAmbushedByHumanlike`      `MentalStateGaveUp`               `CaravanFled`                     `Flashstorm`                    
```

_余下 41 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
