# IdeoStoryPatternDef

- **所属线**：理念线
- **原版实例数**：6
- **字段路径数**：10
- **资料片**：Ideology
- **原版出处**：`Ideology/Defs/RulePackDefs/RulePacks_Ideo_Description.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<IdeoStoryPatternDef>
    <defName>IdeologicalFounder</defName>
    <segments>
      <li>setup</li>
      <li>story</li>
      <li>story</li>
    </segments>
    <rules>
      <include>
        <li>IdeoDescriptionGlobal</li>
      </include>
      <rulesStrings>
        <!-- final fallbacks -->
        <li>story(priority=-999)-&gt;</li> <!-- allow zero or more stories -->

        <!-- generic setup -->
        <li>setup-&gt;In a broken world, [founderName] saw all that was wrong and created our movement.</li>
        <li>setup-&gt;Struck by the wrongness of the world, [founderName] studied history and philosophy and discovered the new truth that guides us.</li>
        <li>setup-&gt;One day while working, [founderName] was struck by a great epiphany. [founder_pronoun] dropped [founder_possessive] tools and began spreading [founder_possessive] word among the other workers.</li>
        <li>setup-&gt;[founderName] sat on a park bench for twenty years as [founder_pronoun] contemplated our world. With [founder_possessive] insight, [founder_pronoun] wrote our founding book.</li>

        <!-- low-priority generic stories -->
        <li>story(uses=1,priority=-10)-&gt;The [memberNamePlural] would not have understood the true nature of [memeConcept] without [founderName]'s teachings.</li>
        <li>story(uses=1,priority=-10)-&gt;[founderName]'s speech at a [ritualName] inspired many to lead a [memeAdjective] life.</li>
        <li>story(uses=1,priority=-10)-&gt;None could surpass [founderName]'s understanding of [memeConcept], and [founder_pronoun] was appointed the first [leaderTitle] of the [memberNamePlural].</li>
        <li>story(uses=1,priority=-10)-&gt;[founderName] carried a [relic0_thingDef_label] named [relic0_name] with [founder_objective] everywhere to remind people to live a [memeAdjective] life.</li>
      </rulesStrings>
    </rules>
  </IdeoStoryPatternDef>

  
```

> 来自 `Ideology/Defs/RulePackDefs/RulePacks_Ideo_Description.xml`，defName = `IdeologicalFounder`，XML 节点数 23（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：IdeologicalFounder / IdeologicalLesson / TheistFounder
rules                                          [容器]
rules/include                                  [容器]
rules/include/li                               [文本]  例：IdeoDescriptionGlobal
rules/rulesStrings                             [容器]
rules/rulesStrings/li                          [文本]  例：creation->For an eternity, there was a world of [Color] [materialOrigin], until  / creation->In an old universe of strife, [deity0_name] whipped up great fire that / creation->[deity0_name] gave birth to humans in a grand accident, and looked upo
segments                                       [容器]
segments/li                                    [文本]  例：conflict / creation / episode
```

## 三、全量字段表（10 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (6/6) | 文本 | IdeologicalFounder / IdeologicalLesson / TheistFounder |
| `noCapitalizeFirstSentence` | 16.7% (1/6) | 容器 |  |
| `noCapitalizeFirstSentence/li` | 16.7% (1/6) | 文本 | lesson |
| `rules` | 100.0% (6/6) | 容器 |  |
| `rules/include` | 100.0% (6/6) | 容器 |  |
| `rules/include/li` | 100.0% (6/6) | 文本 | IdeoDescriptionGlobal |
| `rules/rulesStrings` | 100.0% (6/6) | 容器 |  |
| `rules/rulesStrings/li` | 2366.7% (142/6) | 文本 | creation->For an eternity, there was a world of [Color] [materialOrigin], until  / creation->In an old univers |
| `segments` | 100.0% (6/6) | 容器 |  |
| `segments/li` | 316.7% (19/6) | 文本 | conflict / creation / episode |

## 四、原版 defName 一览（共 6 个，列出前 60）

```text
`IdeologicalFounder`              `AnimistDescription`              `ArchistDescription`              `TheistMyth`                    
`TheistFounder`                   `IdeologicalLesson`             
```
