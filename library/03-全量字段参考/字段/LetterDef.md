# LetterDef

- **所属线**：系统线
- **原版实例数**：27
- **字段路径数**：8
- **资料片**：Anomaly、Biotech、Core、Ideology
- **原版出处**：`Anomaly/Defs/Misc/LetterDefs/CustomChoiceLetters.xml`、`Core/Defs/Misc/LetterDefs/CustomNotificationLetters.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<LetterDef ParentName="CustomChoiceLetterBase">
    <defName>AcceptCreepJoiner</defName>
    <letterClass>ChoiceLetter_AcceptCreepJoiner</letterClass>
  </LetterDef>
  
  
```

> 来自 `Anomaly/Defs/Misc/LetterDefs/CustomChoiceLetters.xml`，defName = `AcceptCreepJoiner`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：AcceptCreepJoiner / BabyBirth / BabyToChild
```

## 三、全量字段表（8 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `arriveSound` | 48.1% (13/27) | 文本 | BabyBecomesChild / ChildBirthday / HumanPregnancy |
| `bounce` | 7.4% (2/27) | 布尔 | true |
| `color` | 33.3% (9/27) | 文本 | (120, 176, 216) / (175, 176, 185) / (204, 196, 135) |
| `defName` | 96.3% (26/27) | 文本 | AcceptCreepJoiner / BabyBirth / BabyToChild |
| `flashColor` | 25.9% (7/27) | 文本 | (106, 179, 231) / (210, 198, 106) / (255, 155, 95) |
| `flashInterval` | 29.6% (8/27) | 数值 | -1 / 40 / 6 |
| `letterClass` | 63.0% (17/27) | 文本 | ChoiceLetter_AcceptCreepJoiner / ChoiceLetter_BabyBirth / ChoiceLetter_BabyToChild |
| `pauseMode` | 7.4% (2/27) | 文本 | AnyThreat / MajorThreat |

## 四、原版 defName 一览（共 27 个，列出前 60）

```text
`AcceptCreepJoiner`               `EntityDiscovered`                `BabyBirth`                       `Bossgroup`                     
`HumanPregnancy`                  `RansomDemand`                    `ChoosePawn`                      `AcceptVisitors`                
`AcceptJoiner`                    `BetrayVisitors`                  `GameEnded`                       `Death`                         
`NewQuest`                        `NewQuest_ThreatBig`              `RelicHuntInstallationFound`      `BabyToChild`                   
`ChildBirthday`                   `ChildToAdult`                    ``                                `BundleLetter`                  
`RitualOutcomePositive`           `RitualOutcomeNegative`           `NegativeEvent`                   `NeutralEvent`                  
`PositiveEvent`                   `ThreatBig`                       `ThreatSmall`                   
```
