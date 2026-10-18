# SkillDef

- **所属线**：人物线
- **原版实例数**：12
- **字段路径数**：12
- **资料片**：Core
- **原版出处**：`Core/Defs/SkillDefs/Skills.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<SkillDef>
    <defName>Crafting</defName>
    <description>Crafting general items including weapons, components, and refined resources.</description>
    <skillLabel>crafting</skillLabel>
    <listOrder>50</listOrder>
    <lessonInteraction MayRequire="Ludeon.RimWorld.Biotech">LessonCrafting</lessonInteraction>
    <generalRules>
      <rulesStrings>
        <li>subject-&gt;crafting</li>
        <li>subject-&gt;assembly</li>
        <li>subject-&gt;manufacturing</li>
        <li>subject-&gt;handcrafting</li>
        <li>subject-&gt;fabrication</li>
        <li>subject-&gt;production</li>
        <li>subject-&gt;craftsmanship</li>
        <li>subject-&gt;machining</li>
        <li>subject-&gt;artisanry</li>
      </rulesStrings>
    </generalRules>
  </SkillDef>

  
```

> 来自 `Core/Defs/SkillDefs/Skills.xml`，defName = `Crafting`，XML 节点数 17（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Construction / Melee / Mining
description                                    [文本]  例：Constructing and deconstructing structures and furniture. / Digging tunnels and extracting buried resources. / Melee combat, both armed and unarmed.
generalRules                                   [容器]
generalRules/rulesStrings                      [容器]
generalRules/rulesStrings/li                   [文本]  例：subject->aiming / subject->guns / subject->shooting
lessonInteraction                              [文本]  例：LessonConstruction / LessonMelee / LessonMining
listOrder                                      [数值]  例：100 / 110 / 120
skillLabel                                     [文本]  例：construction / melee / mining
```

## 三、全量字段表（12 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (12/12) | 文本 | Construction / Melee / Mining |
| `description` | 100.0% (12/12) | 文本 | Constructing and deconstructing structures and furniture. / Digging tunnels and extracting buried resources. / |
| `disablingWorkTags` | 16.7% (2/12) | 文本 | Violent |
| `generalRules` | 100.0% (12/12) | 容器 |  |
| `generalRules/rulesStrings` | 100.0% (12/12) | 容器 |  |
| `generalRules/rulesStrings/li` | 1466.7% (176/12) | 文本 | subject->aiming / subject->guns / subject->shooting |
| `lessonInteraction` | 100.0% (12/12) | 文本 | LessonConstruction / LessonMelee / LessonMining |
| `listOrder` | 100.0% (12/12) | 数值 | 100 / 110 / 120 |
| `neverDisabledBasedOnWorkTypes` | 16.7% (2/12) | 布尔 | true |
| `pawnCreatorSummaryVisible` | 66.7% (8/12) | 布尔 | true |
| `skillLabel` | 100.0% (12/12) | 文本 | construction / melee / mining |
| `usuallyDefinedInBackstories` | 8.3% (1/12) | 布尔 | false |

## 四、原版 defName 一览（共 12 个，列出前 60）

```text
`Crafting`                        `Construction`                    `Artistic`                        `Animals`                       
`Melee`                           `Mining`                          `Cooking`                         `Social`                        
`Plants`                          `Shooting`                        `Medicine`                        `Intellectual`                  
```
