# HistoryEventDef

- **所属线**：世界线
- **原版实例数**：171
- **字段路径数**：2
- **资料片**：Anomaly、Biotech、Core、Ideology、Odyssey
- **原版出处**：`Anomaly/Defs/Misc/HistoryEventDefs.xml`、`Core/Defs/PreceptDefs/Precepts_Lovin.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<HistoryEventDef>
    <defName>GhoulInfusionPerformed</defName>
    <label>ghoul infusion performed</label>
  </HistoryEventDef>

  
```

> 来自 `Anomaly/Defs/Misc/HistoryEventDefs.xml`，defName = `GhoulInfusionPerformed`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：BecameMutant / DestroyedVoidMonolith / GhoulInfusionPerformed
label                                          [文本]  例：destroyed void monolith / ghoul infusion performed / psychic ritual performed
```

## 三、全量字段表（2 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (171/171) | 文本 | BecameMutant / DestroyedVoidMonolith / GhoulInfusionPerformed |
| `label` | 100.0% (171/171) | 文本 | destroyed void monolith / ghoul infusion performed / psychic ritual performed |

## 四、原版 defName 一览（共 171 个，列出前 60）

```text
`GhoulInfusionPerformed`          `BecameMutant`                    `DestroyedVoidMonolith`           `PsychicRitualPerformed`        
`InvolvedInPsychicRitual`         `WasPsychicRitualTarget`          `PollutedNearbySite`              `PollutedBase`                  
`ToxicWasteDumping`               `AbsorbedXenogerm`                `ExtractedHemogenPack`            `BloodfeederDied`               
`PropagateBloodfeederGene`        `BecomeNonPreferredXenotype`      `XenogermAbsorbed`                `GaveGift`                      
`Traded`                          `RequestedTrader`                 `RequestedOrbitalTrader`          `RequestedMilitaryAid`          
`PeaceTalksDisaster`              `PeaceTalksBackfire`              `PeaceTalksSuccess`               `PeaceTalksTriumph`             
`AttackedBuilding`                `ShuttleDestroyed`                `LaborersMissedShuttle`           `UsedHarmfulAbility`            
`UsedForbiddenThing`              `ReachNaturalGoodwill`            `RitualDone`                      `DebugGoodwill`                 
`UsedHarmfulItem`                 `AttackedMember`                  `MemberCrushed`                   `MemberNeutrallyDied`           
`MemberCaptured`                  `MemberKilled`                    `MemberSold`                      `MemberExitedMapHealthy`        
`FriendlyExitedMapTended`         `PerformedHarmfulSurgery`         `MemberStripped`                  `InnocentPrisonerDied`          
`GuiltyPrisonerDied`              `PrisonerDied`                    `QuestGoodwillReward`             `QuestPawnLost`                 
`QuestPawnArrested`               `ShuttleCommanderMissedShuttle`   `ShuttleGuardsMissedShuttle`      `MonumentConstructionExpired`   
`MonumentConstructionMapRemoved`  `FailedToKeepLodgersHappy`        `QuestPrisonerRecruited`          `QuestPrisonerEnslaved`         
`MemberMissedShuttle`             `MonumentDestroyed`               `AcceptedDeserter`                `SettlementProximity`           
```

_余下 111 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
