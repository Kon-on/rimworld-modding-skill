# MonolithLevelDef

- **所属线**：世界线
- **原版实例数**：7
- **字段路径数**：43
- **资料片**：Anomaly
- **原版出处**：`Anomaly/Defs/Misc/MonolithLevels.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<MonolithLevelDef>
    <defName>Disrupted</defName>
    <level>6</level>
    <monolithLabel>collapsed monolith</monolithLabel>
    <monolithDescription>The remnants of the monolith which linked our world to the void lie broken. The twisted patterns that once writhed across its surface are now motionless. You can study the broken stones to gain further knowledge of the void phenomena.</monolithDescription>
    <graphicIndex>5</graphicIndex>
    <advanceThroughActivation>false</advanceThroughActivation>
    <postEndgame>true</postEndgame>
    <anomalyThreatTier>0</anomalyThreatTier>
    <useInactiveAnomalyThreatFraction>true</useInactiveAnomalyThreatFraction>
    <monolithStudyCategory>Advanced</monolithStudyCategory>
    <desiredHarbingerTreeCount>0</desiredHarbingerTreeCount>
    <anomalyMentalBreakChance>0</anomalyMentalBreakChance>
    <uiIconPath>Things/Building/VoidMonolith/Icons/VoidMonolith_F_MenuIcon</uiIconPath>
  </MonolithLevelDef>
```

> 来自 `Anomaly/Defs/Misc/MonolithLevels.xml`，defName = `Disrupted`，XML 节点数 14（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
advanceThroughActivation                       [布尔]  例：false / true
anomalyMentalBreakChance                       [数值]  例：0.05 / 0.2 / 0.4
anomalyThreatTier                              [数值]  例：0 / 1 / 2
attachments/li                                 [容器]
attachments/li/def                             [文本]  例：VoidMonolithAttachmentBottomLeft / VoidMonolithAttachmentBottomRight / VoidMonolithAttachmentLeft
attachments/li/graphicIndex                    [数值]  例：0 / 1 / 2
attachments/li/offset                          [文本]  例：(-1, -2) / (-2, 0) / (1, -2)
defName                                        [文本]  例：Inactive / Stirring / VoidAwakened
desiredHarbingerTreeCount                      [数值]  例：0 / 3 / 6
graphicIndex                                   [数值]  例：0 / 1 / 2
level                                          [数值]  例：0 / 1 / 2
monolithLabel                                  [文本]  例：collapsed monolith / fallen monolith / void monolith
```

## 三、全量字段表（43 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `activatableLetterLabel` | 28.6% (2/7) | 文本 | Attuning the monolith / Awakening the monolith |
| `activatableLetterText` | 28.6% (2/7) | 文本 | You now have enough knowledge of dark phenomena to fully awaken the void monolit / You now have sufficient kno |
| `activatedLetterText` | 42.9% (3/7) | 文本 | As the monolith twisted and changed, {PAWN_nameDef} was overcome with a horrifyi / Attuning the monolith cause |
| `activatedSound` | 57.1% (4/7) | 文本 | VoidMonolith_ActivatedL0L1 / VoidMonolith_ActivatedL1L2 / VoidMonolith_ActivatedL2L3 |
| `activateFloatMenuText` | 42.9% (3/7) | 文本 | attune {0} / awaken {0} / investigate {0} |
| `activateGizmoDescription` | 42.9% (3/7) | 文本 | Send a colonist to attune the monolith.\n\nThis will attract new and more danger / Send a colonist to investig |
| `activateGizmoText` | 42.9% (3/7) | 文本 | attune / awaken / investigate |
| `activateQuestText` | 42.9% (3/7) | 文本 | Send a colonist to attune the monolith. / Send a colonist to awaken the monolith. / Send a colonist to investi |
| `activateSound` | 42.9% (3/7) | 文本 | VoidMonolith_ActivateL0L1 / VoidMonolith_ActivateL1L2 / VoidMonolith_ActivateL2L3 |
| `advanceThroughActivation` | 100.0% (7/7) | 布尔 | false / true |
| `anomalyMentalBreakChance` | 100.0% (7/7) | 数值 | 0.05 / 0.2 / 0.4 |
| `anomalyThreatFractionFactor` | 42.9% (3/7) | 数值 | 1.5 |
| `anomalyThreatTier` | 100.0% (7/7) | 数值 | 0 / 1 / 2 |
| `attachments` | 71.4% (5/7) | 容器 |  |
| `attachments/li` | 314.3% (22/7) | 容器 |  |
| `attachments/li/def` | 314.3% (22/7) | 文本 | VoidMonolithAttachmentBottomLeft / VoidMonolithAttachmentBottomRight / VoidMonolithAttachmentLeft |
| `attachments/li/graphicIndex` | 314.3% (22/7) | 数值 | 0 / 1 / 2 |
| `attachments/li/offset` | 314.3% (22/7) | 文本 | (-1, -2) / (-2, 0) / (1, -2) |
| `defName` | 100.0% (7/7) | 文本 | Inactive / Stirring / VoidAwakened |
| `desiredHarbingerTreeCount` | 100.0% (7/7) | 数值 | 0 / 3 / 6 |
| `entityCatagoryCompletionRequired` | 28.6% (2/7) | 文本 | Advanced / Basic |
| `entityCountCompletionRequired` | 28.6% (2/7) | 数值 | 12 / 7 |
| `extraQuestDescription` | 57.1% (4/7) | 文本 | The monolith is a conduit to the void where a dark superintelligence processes e / The void has awoken. The ga |
| `graphicIndex` | 100.0% (7/7) | 数值 | 0 / 1 / 2 |
| `incidentsOnReached` | 28.6% (2/7) | 容器 |  |
| `incidentsOnReached/li` | 28.6% (2/7) | 文本 | PitGate / SightstealerArrival |
| `level` | 100.0% (7/7) | 数值 | 0 / 1 / 2 |
| `levelInspectText` | 85.7% (6/7) | 文本 | Level 1: Intermittent psychic humming / Level 2: Pulsing with psychic energy / Level 3: Awakening |
| `monolithCanBeActivatedText` | 42.9% (3/7) | 文本 | Can be attuned now. / Can be awakened now. / Can be investigated now. |
| `monolithDescription` | 14.3% (1/7) | 文本 | The remnants of the monolith which linked our world to the void lie broken. The  |
| `monolithGlowRadiusOverride` | 28.6% (2/7) | 数值 | 20 / 24 |
| `monolithGlows` | 42.9% (3/7) | 布尔 | true |
| `monolithLabel` | 100.0% (7/7) | 文本 | collapsed monolith / fallen monolith / void monolith |
| `monolithStudyCategory` | 85.7% (6/7) | 文本 | Advanced / Basic |
| `pawnSentToActivateMessage` | 42.9% (3/7) | 文本 | {PAWN_nameDef} has been sent to attune the monolith. / {PAWN_nameDef} has been sent to awaken the monolith. /  |
| `postEndgame` | 28.6% (2/7) | 布尔 | true |
| `sizeIncludingAttachments` | 71.4% (5/7) | 文本 | (5, 3) / (5, 5) |
| `triggersGrayPall` | 28.6% (2/7) | 布尔 | true |
| `uiIconPath` | 85.7% (6/7) | 文本 | Things/Building/VoidMonolith/Icons/VoidMonolith_A_MenuIcon / Things/Building/VoidMonolith/Icons/VoidMonolith_B |
| `unreachableDuringConditions` | 14.3% (1/7) | 容器 |  |
| `unreachableDuringConditions/li` | 14.3% (1/7) | 文本 | UnnaturalDarkness |
| `useActiveAnomalyThreatFraction` | 71.4% (5/7) | 布尔 | true |
| `useInactiveAnomalyThreatFraction` | 28.6% (2/7) | 布尔 | true |

## 四、原版 defName 一览（共 7 个，列出前 60）

```text
`Disrupted`                       `Inactive`                        `Embraced`                        `Stirring`                      
`Gleaming`                        `VoidAwakened`                    `Waking`                        
```
