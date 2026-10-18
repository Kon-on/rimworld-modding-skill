# InspirationDef

- **所属线**：人物线
- **原版实例数**：8
- **字段路径数**：34
- **资料片**：Core
- **原版出处**：`Core/Defs/InspirationDefs/Inspirations.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<InspirationDef>
    <defName>Frenzy_Work</defName>
    <label>work frenzy</label>
    <baseDurationDays>8</baseDurationDays>
    <beginLetter>[PAWN_pronoun] will work faster for the next 8 days.</beginLetter>
    <beginLetterDef>PositiveEvent</beginLetterDef>
    <endMessage>{0} is no longer inspired (work frenzy).</endMessage>
    <baseInspectLine>Inspired: Work frenzy</baseInspectLine>
    <requiredNonDisabledWorkTags>AllWork</requiredNonDisabledWorkTags>
    <minAge>10</minAge>
    <statFactors>
      <WorkSpeedGlobal>1.8</WorkSpeedGlobal>
    </statFactors>
  </InspirationDef>

  
```

> 来自 `Core/Defs/InspirationDefs/Inspirations.xml`，defName = `Frenzy_Work`，XML 节点数 12（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
baseDurationDays                               [数值]  例：8
baseInspectLine                                [文本]  例：Inspired: Go frenzy / Inspired: Inspired trade / Inspired: Shoot frenzy
beginLetter                                    [文本]  例：[PAWN_pronoun] will get a significant trade price bonus when closing [PAWN_posse / [PAWN_pronoun] will move faster for the next 8 days. / [PAWN_pronoun] will shoot more accurately for the next 8 days.
beginLetterDef                                 [文本]  例：PositiveEvent
defName                                        [文本]  例：Frenzy_Go / Frenzy_Shoot / Frenzy_Work
endMessage                                     [文本]  例：{0} is no longer inspired (go frenzy). / {0} is no longer inspired (inspired trade). / {0} is no longer inspired (shoot frenzy).
label                                          [文本]  例：go frenzy / inspired trade / shoot frenzy
```

## 三、全量字段表（34 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `allowedOnDownedPawns` | 12.5% (1/8) | 布尔 | false |
| `associatedSkills` | 75.0% (6/8) | 容器 |  |
| `associatedSkills/li` | 75.0% (6/8) | 文本 | Animals / Medicine / Shooting |
| `baseDurationDays` | 100.0% (8/8) | 数值 | 8 |
| `baseInspectLine` | 100.0% (8/8) | 文本 | Inspired: Go frenzy / Inspired: Inspired trade / Inspired: Shoot frenzy |
| `beginLetter` | 100.0% (8/8) | 文本 | [PAWN_pronoun] will get a significant trade price bonus when closing [PAWN_posse / [PAWN_pronoun] will move fa |
| `beginLetterDef` | 100.0% (8/8) | 文本 | PositiveEvent |
| `defName` | 100.0% (8/8) | 文本 | Frenzy_Go / Frenzy_Shoot / Frenzy_Work |
| `endMessage` | 100.0% (8/8) | 文本 | {0} is no longer inspired (go frenzy). / {0} is no longer inspired (inspired trade). / {0} is no longer inspir |
| `label` | 100.0% (8/8) | 文本 | go frenzy / inspired trade / shoot frenzy |
| `minAge` | 75.0% (6/8) | 数值 | 10 / 13 / 6 |
| `requiredAnyNonDisabledWorkType` | 12.5% (1/8) | 容器 |  |
| `requiredAnyNonDisabledWorkType/li` | 50.0% (4/8) | 文本 | Art / Construction / Smithing |
| `requiredAnySkill` | 12.5% (1/8) | 容器 |  |
| `requiredAnySkill/Artistic` | 12.5% (1/8) | 数值 | 3 |
| `requiredAnySkill/Construction` | 12.5% (1/8) | 数值 | 3 |
| `requiredAnySkill/Crafting` | 12.5% (1/8) | 数值 | 3 |
| `requiredCapacities` | 62.5% (5/8) | 容器 |  |
| `requiredCapacities/li` | 62.5% (5/8) | 文本 | Manipulation / Moving / Talking |
| `requiredNonDisabledStats` | 62.5% (5/8) | 容器 |  |
| `requiredNonDisabledStats/li` | 62.5% (5/8) | 文本 | NegotiationAbility / ShootingAccuracyPawn / TameAnimalChance |
| `requiredNonDisabledWorkTags` | 12.5% (1/8) | 文本 | AllWork |
| `requiredNonDisabledWorkTypes` | 37.5% (3/8) | 容器 |  |
| `requiredNonDisabledWorkTypes/li` | 37.5% (3/8) | 文本 | Doctor / Handling / Warden |
| `requiredSkills` | 50.0% (4/8) | 容器 |  |
| `requiredSkills/Animals` | 12.5% (1/8) | 数值 | 3 |
| `requiredSkills/Medicine` | 12.5% (1/8) | 数值 | 3 |
| `requiredSkills/Social` | 25.0% (2/8) | 数值 | 3 |
| `statFactors` | 25.0% (2/8) | 容器 |  |
| `statFactors/MoveSpeed` | 12.5% (1/8) | 数值 | 1.4 |
| `statFactors/WorkSpeedGlobal` | 12.5% (1/8) | 数值 | 1.8 |
| `statOffsets` | 25.0% (2/8) | 容器 |  |
| `statOffsets/ShootingAccuracyPawn` | 12.5% (1/8) | 数值 | 8 |
| `statOffsets/TradePriceImprovement` | 12.5% (1/8) | 数值 | 0.18 |

## 四、原版 defName 一览（共 8 个，列出前 60）

```text
`Frenzy_Work`                     `Frenzy_Go`                       `Frenzy_Shoot`                    `Inspired_Trade`                
`Inspired_Taming`                 `Inspired_Recruitment`            `Inspired_Surgery`                `Inspired_Creativity`           
```
