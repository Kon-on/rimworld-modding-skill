# ThoughtDef

## 用途
ThoughtDef 定义一条**想法**：心情加成/惩罚（`baseMoodEffect`）或对某个特定小人的看法（`baseOpinionOffset`），是心情系统与人际关系的原子单位。它的分支由 `thoughtClass` 决定：记忆型（`Thought_Memory`，会随时间消失）、社交记忆型（`Thought_MemorySocial`，针对某个人的记忆）、情境型（`Thought_Situational`，由 `workerClass` 持续重算）。
它与 TraitDef（`nullifyingTraits` / `requiredTraits`）、HediffDef（`nullifyingHediffs` / `requiredHediffs` / `hediff`）、GeneDef（`nullifyingGenes` / `requiredGenes`）以及 Ideology 的 precept（`nullifyingPrecepts`）联动，用来让同一个事件对不同的人产生不同后果。原版共 933 个实例、65 条字段路径。

## 模板
```xml
<?xml version="1.0" encoding="utf-8" ?>
<Defs>

  <!-- 记忆型：会持续 durationDays 天，可按 stackLimit 叠加 -->
  <ThoughtDef>
    <defName>EXAMPLE_AteRation</defName>

    <durationDays>2</durationDays>                        <!-- 持续天数；情境型不写它 -->
    <stackLimit>3</stackLimit>                            <!-- 最多叠 3 层 -->
    <stackedEffectMultiplier>0.5</stackedEffectMultiplier><!-- 每多叠一层效果乘 0.5 -->
    <showBubble>true</showBubble>                         <!-- 头顶显示气泡（5.7% 的实例写） -->
    <icon>Things/Mote/ThoughtSymbol/SleepZ</icon>

    <!-- 有这些特质的人不受该想法影响 -->
    <nullifyingTraits>
      <li>Ascetic</li>
    </nullifyingTraits>
    <nullifyingHediffs>
      <li>DetoxifierLung</li>
    </nullifyingHediffs>

    <stages>
      <li>
        <label>ate a ration</label>                       <!-- 137.0%：label 永远写在 stages/li 里 -->
        <description>It wasn't good, but at least it was warm.</description>
        <baseMoodEffect>2</baseMoodEffect>                <!-- 心情修正：正数=好心情 -->
      </li>
    </stages>
  </ThoughtDef>

  <!-- 社交记忆型：影响对"某个人"的看法，而不是自己的心情 -->
  <ThoughtDef>
    <defName>EXAMPLE_HelpedMeOut</defName>
    <thoughtClass>Thought_MemorySocial</thoughtClass>
    <durationDays>10</durationDays>
    <stackLimitForSameOtherPawn>1</stackLimitForSameOtherPawn>

    <stages>
      <li>
        <label>helped me out</label>
        <labelSocial>helped out</labelSocial>
        <description>They helped me when I needed it.</description>
        <baseOpinionOffset>10</baseOpinionOffset>         <!-- 好感修正：正数=更喜欢对方 -->
      </li>
    </stages>
  </ThoughtDef>

  <!--
    情境型（Thought_Situational）：效果由 C# 的 ThoughtWorker 每段时间重新计算，
    必须写 workerClass，且通常不写 durationDays。示范（未启用）：

    <ThoughtDef>
      <defName>EXAMPLE_SituationSample</defName>
      <workerClass>ThoughtWorker_NeedFood</workerClass>   （类名必须真实存在，原版样例 ThoughtWorker_NeedFood）
      <validWhileDespawned>true</validWhileDespawned>
      <developmentalStageFilter>Baby, Child, Adult</developmentalStageFilter>
      <stages>
        <li><label>a</label><description>a</description><baseMoodEffect>-6</baseMoodEffect></li>
        <li><label>b</label><description>b</description><baseMoodEffect>-12</baseMoodEffect></li>
      </stages>
    </ThoughtDef>

    其它可选字段（示范）：
    <thoughtClass>Thought_Memory</thoughtClass>              记忆型默认类
    <requiredTraits><li>Cannibal</li></requiredTraits>       只有这些特质的人才有该想法
    <requiredGenes><li>Mood_Pessimist</li></requiredGenes>
    <requiredTraitsDegree>-1</requiredTraitsDegree>          特质等级要求
    <nullifyingPrecepts><li MayRequire="Ludeon.RimWorld.Ideology">RoughLiving_Welcomed</li></nullifyingPrecepts>
    <nullifyingGenes><li>ToxResist_Total</li></nullifyingGenes>
    <nullifyingTraitDegrees><PsychicSensitivity>2</PsychicSensitivity></nullifyingTraitDegrees>
    <doNotApplyToQuestLodgers>true</doNotApplyToQuestLodgers>
    <minExpectation>Moderate</minExpectation>                期望门槛（值 High/Low/Moderate）
    <effectMultiplyingStat>PsychicSensitivity</effectMultiplyingStat>
    <socialTargetDevelopmentalStageFilter>Child, Adult</socialTargetDevelopmentalStageFilter>
    <nextThought>NewColonyHope</nextThought>                 到期后替换成另一条想法
    <taleDef>HealedMe</taleDef>                              触发传说
    <gender>Female</gender> / <hediff>Inhumanized</hediff> / <gameCondition>Aurora</gameCondition>
    <invert>true</invert> / <lerpMoodToZero>true</lerpMoodToZero>
  -->

</Defs>
```

## 字段说明
| 字段 | 出现率 | 值类型 | 说明 |
|---|---|---|---|
| `defName` | 98.8% (922/933) | 文本 | 唯一 ID |
| `stages` | 97.5% (910/933) | 容器 | 阶段列表容器 |
| `stages/li` | 141.6% (1321/933) | 容器 | 阶段条目（>100% 表示一条定义可有多段） |
| `stages/li/label` | 137.0% (1278/933) | 文本 | 阶段名，样例 `human shame` |
| `stages/li/description` | 115.8% (1080/933) | 文本 | 阶段描述 |
| `stages/li/baseMoodEffect` | 115.1% (1074/933) | 数值 | 心情修正，样例 -12 / -2 / -4 |
| `durationDays` | 50.9% (475/933) | 数值 | 持续天数，样例 1 / 2 / 20 |
| `thoughtClass` | 44.6% (416/933) | 文本 | 实现类，样例 Thought_Memory / Thought_MemorySocial / Thought_Situational |
| `stackLimit` | 39.3% (367/933) | 数值 | 最大叠加层数，样例 1 / 2 / 100 |
| `workerClass` | 35.3% (329/933) | 文本 | 情境型的判定实现，样例 ThoughtWorker_Hediff |
| `stages/li/baseOpinionOffset` | 22.0% (205/933) | 数值 | 好感修正，样例 -10 / -20 / -30 |
| `validWhileDespawned` | 18.9% (176/933) | 布尔 | 离图期间是否继续生效 |
| `nullifyingTraits` | 17.2% (160/933) | 容器 | 抵消该想法的特质 |
| `nullifyingTraits/li` | 25.0% (233/933) | 文本 | 样例 Ascetic / Psychopath |
| `nullifyingHediffs/li` | 12.8% (119/933) | 文本 | 样例 DetoxifierLung / Inhumanized；本体 12.7% (118/933) |
| `developmentalStageFilter` | 14.1% (132/933) | 文本 | 生效年龄段，样例 `Adult` / `Baby, Child, Adult` |
| `stackLimitForSameOtherPawn` | 13.7% (128/933) | 数值 | 对同一个人的叠加上限 |
| `doNotApplyToQuestLodgers` | 11.4% (106/933) | 布尔 | 任务访客不适用 |
| `stackedEffectMultiplier` | 8.4% (78/933) | 数值 | 叠加衰减系数，样例 0.75 / 0.9 |
| `showBubble` | 5.7% (53/933) | 布尔 | 是否头顶气泡 |
| `hediff` | 4.2% (39/933) | 文本 | 关联 hediff，样例 FleshWhip / Inhumanized |
| `requiredTraits/li` | 4.1% (38/933) | 文本 | 需要特质；本体 4.0% (37/933) |
| `icon` | 3.9% (36/933) | 文本 | 图标路径 |
| `nullifyingPrecepts/li` | 4.2% (39/933) | 文本 | 抵消该想法的信条 |
| `nullifyingGenes/li` | 1.9% (18/933) | 文本 | 抵消该想法的基因 |
| `socialTargetDevelopmentalStageFilter` | 1.5% (14/933) | 文本 | 社交对象年龄段过滤 |
| `stages/li/visible` | 1.4% (13/933) | 布尔 | 阶段是否可见 |
| `nullifyingTraitDegrees` | 1.4% (13/933) | 容器 | 按特质等级抵消，键=特质名 |
| `effectMultiplyingStat` | 1.2% (11/933) | 文本 | 放大效果的能力值，样例 PsychicSensitivity |
| `thoughtToMake` | 1.1% (10/933) | 文本 | 替换成另一条想法 |
| `minExpectation` | 1.0% (9/933) | 文本 | 期望门槛，样例 High / Low / Moderate |
| `taleDef` | 0.9% (8/933) | 文本 | 触发传说，样例 HealedMe |
| `requiredTraitsDegree` | 0.9% (8/933) | 数值 | 特质等级要求 |
| `nullifiedIfNotColonist` | 0.8% (7/933) | 布尔 | 非殖民者则失效 |
| `requiredGenes/li` | 0.8% (7/933) | 文本 | 需要基因 |
| `minExpectationForNegativeThought` | 0.5% (5/933) | 文本 | 负面想法的期望门槛 |
| `stages/li/labelSocial` | 0.3% (3/933) | 文本 | 社交版本的显示名 |
| `gender` | 2.6% (24/933) | 文本 | 性别限定 |
| `nullifyingOwnTales` | 0.2% (2/933) | 容器 | 抵消特定传说 |
| `maxCumulatedOpinionOffset` | 0.2% (2/933) | 数值 | 好感累计上限 |
| `replaceThoughts` | 0.2% (2/933) | 容器 | 替换其它想法 |
| `producesMemoryThought` | 0.2% (2/933) | 文本 | 情境想法转成记忆想法 |
| `invert` | 0.2% (2/933) | 布尔 | 反转 | 
| `nextThought` | 0.1% (1/933) | 文本 | 到期后接续的想法，样例 NewColonyHope |
| `lerpMoodToZero` | 0.1% (1/933) | 布尔 | 心情向 0 插值 |
| `neverNullifyIfAnyTrait` | 0.1% (1/933) | 容器 | 例外特质 |
| `gameCondition` | 0.3% (3/933) | 文本 | 关联天气/环境条件，样例 Aurora |
| `ignoreSubhumans` | 0.3% (3/933) | 布尔 | 忽略亚人 |

## 常见坑
1. `label` / `description` / `baseMoodEffect` 都写在 **`stages/li` 内部**：原版出现率分别是 137.0% / 115.8% / 115.1%，而根级 `label` 只有 0.1% (1/933)。写错位置想法不会显示。
2. `baseMoodEffect`（影响自己心情）与 `baseOpinionOffset`（影响对他人的好感）是两套数值，社交想法用后者（22.0% 的实例写了 `stages/li/baseOpinionOffset`）。
3. `durationDays` 只有 50.9% 的实例写：情境型想法（`workerClass` 驱动）通常不写它，由 worker 每次重算决定是否存在。
4. 情境型必须配 `workerClass`（35.3% 的实例写了该字段，值形如 `ThoughtWorker_Hediff`）；`workerClass` 是 C# 类，写一个不存在的类名会加载失败。**只写 `thoughtClass` 而没有 worker 的情境想法不会自动触发。**【推测】
5. `nullifying*` 系列是"让这条想法失效"的白名单机制（traits / hediffs / precepts / genes / traitDegrees），原版 `Psychopath`、`Ascetic` 大量用于抵消社交与饮食类想法；要限定"只有某类人有"，则用 `requiredTraits` / `requiredGenes`。
6. `stackLimit` 要配合 `stackedEffectMultiplier` 才看得出叠减效果（原版样例 0.75 / 0.8 / 0.9）；跨人对同一目标的叠加另有 `stackLimitForSameOtherPawn`（13.7%）。

## 核验
- 记忆型写法逐行对照原版 `Core/Defs/ThoughtDefs/Thoughts_Memory_Misc.xml`：`AteWithoutTable`(:4-21) 给出 durationDays / stackLimit / `nullifyingTraits/Ascetic` / `nullifyingPrecepts`（含 `MayRequire="Ludeon.RimWorld.Ideology"` 的 `RoughLiving_Welcomed`）/ stages/li 的 label+description+baseMoodEffect(-3)；`SleepDisturbed`(:23-38) 给出 `icon`、`showBubble`、`stackedEffectMultiplier`、`developmentalStageFilter`；`NewColonyOptimism`(:40-52) 给出 `nextThought`。
- 情境型写法对照原版 `Core/Defs/ThoughtDefs/Thoughts_Situation_Needs.xml` 的 `NeedFood`(:4-9)：`workerClass` `ThoughtWorker_NeedFood` + `validWhileDespawned` + `developmentalStageFilter` + 多段 stages（每段只有 label/description/baseMoodEffect）。
- 出现率与样例值来自 `library/03-全量字段参考/字段/ThoughtDef.md`（933 个原版实例实测）。
- 其它可交叉核对文件：`Core/Defs/ThoughtDefs/Thoughts_Memory_Social.xml`（社交记忆）、`Thoughts_Memory_Eating.xml`（饮食类）、`Thoughts_Situation_Traits.xml`（特性相关）。
