# PreceptDef

## 用途

PreceptDef 是 **Ideology（理念）系统的“戒律/信条”定义**：一条戒律 = 理念里可勾选的一个立场（吃人=可接受、裸体=可憎、奴隶制=被认可……）。只要你写 `<issue>` 就把它挂进某个议题（issue）里，游戏会自动把它按议题分组、塞进理念编辑界面的候选列表。

戒律本身通常**没有任何逻辑**——实际效果全部由 `<comps>` 里的一串 `PreceptComp_*` 承担（加心情、记事件、禁止某事、触发精神崩坏……），戒律的“仪式玩法”则靠 `preceptClass=Precept_Ritual` + `ritualPatternBase` 外包给 RitualPatternDef。因此 PreceptDef 几乎总是与 **IssueDef**（议题标牌）、**ThoughtDef**（`comps/li/thought` 引用的心情）、**MemeDef**（`requiredMemes` / `conflictingMemes` 联动）、**RitualPatternDef**（仪式外形）成组出现。

## 模板

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Defs>

  <!-- ================================================================  
       ① 新议题（可选）
       要发明一个新的 <issue> 字符串，就得先给它一块标牌（IssueDef）。
       原版把 IssueDef 和 PreceptDef 写在同一个文件里：
         Biotech/Defs/PreceptDefs/Precepts_Bloodfeeders.xml
       
       只声明、暂时没有 PreceptDef 挂上去也没关系：它是惰性的，不会报错。
       ================================================================ -->
  <IssueDef>
    <defName>EXAMPLE_Stargazing</defName>
    <label>stargazing</label>
    <!-- 图标直接借原版贴图；删掉这一行只会显示空白图标，不会报错 -->
    <iconPath>UI/Issues/Inhumanizing</iconPath>
  </IssueDef>

  <!-- ================================================================  
       ② 普通戒律：效果全靠 <comps>
       本例复用原版议题 Nudity_Male 与原版 ThoughtDef，复制即可加载生效。
       ================================================================ -->
  <PreceptDef>
    <defName>EXAMPLE_Nudity_Male_FaceCoveredDisapproved</defName>
    <label>face covered</label>
    <description>Men should not cover their faces. Hiding the face hides one from other people, and that is shameful.</description>

    <!-- 必写：议题。写自定义议题就填 EXAMPLE_Stargazing（需先写上面的 IssueDef） -->
    <issue>Nudity_Male</issue>
    <!-- 必写：Low / Medium / High -->
    <impact>Medium</impact>

    <iconPath>UI/Icons/Rituals/RitualFestival</iconPath>
    <!-- 同一议题内的排序，越小越靠前 -->
    <displayOrderInIssue>40</displayOrderInIssue>
    <!-- 同一强度档内的排序 -->
    <displayOrderInImpact>200</displayOrderInImpact>
    <!-- 随机生成时的权重 -->
    <selectionWeight>1.0</selectionWeight>
    <!-- 0 = 新建理念时不默认勾选这条 -->
    <defaultSelectionWeight>0</defaultSelectionWeight>
    <!-- 是否占用理念的戒律数量上限 -->
    <countsTowardsPreceptLimit>true</countsTowardsPreceptLimit>
    <!-- 经典模式（无 DLC）也生效 -->
    <classic>true</classic>

    <!-- 核心：一条戒律可以挂多个 comp，每个 comp 自己带所需字段 -->
    <comps>
      <li Class="PreceptComp_SituationalThought">
        <thought>FaceCovered_Disapproved_Male</thought>
      </li>
      <li Class="PreceptComp_KnowsMemoryThought">
        <eventDef>AteHumanMeatDirect</eventDef>
        <thought>AteRawHumanlikeMeat</thought>
        <displayDescription>false</displayDescription>
      </li>
    </comps>
  </PreceptDef>

  <!-- 换成自定义议题时，还要自己定义 comps 里引用的 ThoughtDef，
       否则加载日志会报 Could not find ThoughtDef named ...；
       原版把 IssueDef + PreceptDef + ThoughtDef 放在同一个文件里，
       可照抄 Anomaly/Defs/PreceptDefs/Precepts_Inhumanizing.xml 的结构。
       
       自造议题的写法就是把上面的 <issue> 换成：
         <issue>EXAMPLE_Stargazing</issue>
  -->

  <!-- ================================================================  
       ③ 仪式戒律：preceptClass + ritualPatternBase
       preceptClass=Precept_Ritual 时，仪式的具体流程交给 RitualPatternDef。
       本例指向原版 CelebrationPartyChat（可解析、可直接加载）；
       你自己的仪式应指向本包的 RitualPatternDef，见 03-RitualPatternDef.md。
       ================================================================ -->
  <PreceptDef>
    <defName>EXAMPLE_MyParty</defName>
    <label>my party</label>
    <description>A regular gathering where everyone celebrates together.</description>
    <issue>Ritual</issue>
    <impact>Medium</impact>
    <iconPath>UI/Icons/Rituals/RitualFestival</iconPath>
    <preceptClass>Precept_Ritual</preceptClass>
    <ritualPatternBase>CelebrationPartyChat</ritualPatternBase>
    <allowDuplicates>false</allowDuplicates>
    <countsTowardsPreceptLimit>false</countsTowardsPreceptLimit>
    <selectionWeight>1.0</selectionWeight>
    <displayOrderInImpact>200</displayOrderInImpact>
    <displayOrderInIssue>60</displayOrderInIssue>
    <receivesExpectationsQualityOffset>true</receivesExpectationsQualityOffset>
    <skipOpportunityLettersBeforeDay>0</skipOpportunityLettersBeforeDay>
    <ignoreLimitsInEditMode>false</ignoreLimitsInEditMode>
  </PreceptDef>

</Defs>
```

## 字段说明

出现率直接抄自 `03-全量字段参考/字段/PreceptDef.md`（原版 223 个 PreceptDef 实例、245 条路径的统计值）。

| 字段 | 出现率 | 值类型 | 说明 |
|---|---|---|---|
| `defName` | 96.4% (215/223) | 文本 | 必填。全局唯一 ID，其他 Def 用这个名字引用本戒律。 |
| `label` | 93.7% (209/223) | 文本 | 戒律在界面上显示的短名（如 disapproved / respected）。 |
| `description` | 91.9% (205/223) | 文本 | 戒律的长描述，显示在戒律卡片上。可含 \n 换行。 |
| `issue` | 88.3% (197/223) | 文本 | **必写**。所属议题字符串。原版议题见各 `Precepts_*.xml`；自造议题需另写 `<IssueDef>`（见模板）。 |
| `impact` | 84.3% (188/223) | 文本 | **必写**。戒律强度，只有 `Low` / `Medium` / `High` 三种取值（原版样例仅此三种）。 |
| `preceptClass` | 10.8% (24/223) | 文本 | 自定义 C# 类（继承 `Precept`）。只有需要新玩法时写：`Precept_Ritual`、`Precept_Animal`、`Precept_Apparel`、`Precept_Xenotype` 等；不写则默认 `Precept`。 |
| `workerClass` | 2.7% (6/223) | 文本 | 自定义 `PreceptWorker`，负责生成候选/描述文本。写 `preceptClass` 时通常要配一个，例如 `PreceptWorker_Apparel`。 |
| `ritualPatternBase` | 9.4% (21/223) | 文本 | `preceptClass=Precept_Ritual` 时指向一个 RitualPatternDef 的 defName，决定这个仪式怎么举行。详见 `03-RitualPatternDef.md`。 |
| `iconPath` | 11.2% (25/223) | 文本 | 图标贴图路径（不含扩展名）。缺失只会显示空白图标，不会报错。 |
| `displayOrderInIssue` | 63.7% (142/223) | 数值 | 同一 issue 内的排序，越小越靠前（原版常见 0/10/20/30）。 |
| `displayOrderInImpact` | 55.6% (124/223) | 数值 | 同一 impact 内的排序（原版常见 -100/100）。 |
| `selectionWeight` | 5.8% (13/223) | 数值 | 被 AI/随机生成时抽中的权重（浮点）。 |
| `defaultSelectionWeight` | 15.2% (34/223) | 数值 | 玩家新建理念时该戒律的默认选中权重；设为 `0` 表示不默认选中（常见做法）。 |
| `countsTowardsPreceptLimit` | 10.3% (23/223) | 布尔 | 是否占用理念可选的戒律数量上限。仪式类的原版做法是 `false`。 |
| `allowDuplicates` | 3.1% (7/223) | 布尔 | 同一理念里是否允许重复出现同一条戒律。 |
| `canGenerateAsSpecialPrecept` | 4.5% (10/223) | 布尔 | 是否可作为“特殊戒律”在游戏中途生成（原版多为 `false`）。 |
| `ignoreLimitsInEditMode` | 3.1% (7/223) | 布尔 | 在理念编辑界面是否忽略冲突/上限限制。 |
| `classic` | 12.1% (27/223) | 布尔 | `true` 表示这是“经典模式”（无 Ideology DLC）也能用的戒律。 |
| `visible` | 6.3% (14/223) | 布尔 | `false` 时不在理念编辑界面列出（仅作为内部/隐藏戒律使用）。 |
| `receivesExpectationsQualityOffset` | 2.2% (5/223) | 布尔 | 仪式质量是否受期望值影响（原版葬礼类为 `true`）。 |
| `requiredMemes/li` | 29.1% (65/223) | 文本 | 只有拥有这些 Meme 的理念才会出现该戒律。可多条。 |
| `associatedMemes/li` | 52.0% (116/223) | 文本 | 与该戒律关联的 Meme（用于 UI 提示/联动）。 |
| `conflictingMemes/li` | 22.9% (51/223) | 文本 | 与这些 Meme 互斥；有冲突则不出现在候选里。 |
| `exclusionTags/li` | 10.3% (23/223) | 文本 | 互斥标签：带同一标签的戒律不会同时出现在一个理念里。 |
| `statFactors` | 8.1% (18/223) |  | 按 stat 乘算修正，形如 `<MeleeDamageFactor>1.5</MeleeDamageFactor>`。 |
| `statOffsets` | 6.3% (14/223) |  | 按 stat 加算修正。 |
| `grantedAbilities/li` | 7.6% (17/223) | 文本 | 该戒律直接授予的能力 defName。 |
| `roleApparelRequirements/li` | 13.9% (31/223) |  | 角色着装要求，含 `requirement/bodyPartGroupsMatchAny`、`requirement/requiredDefs`、`requirement/requiredTags`。 |
| `comps` | 67.7% (151/223) | 容器 | **核心**：戒律的实际效果由 comps 列表承担，见下方四行。 |
| `comps/li` | 233.6% (521/223) |  | 一条 `<li Class="PreceptComp_...">`。类名决定该条目需要哪些子字段。 |
| `comps/li/thought` | 196.9% (439/223) | 文本 | 该 comp 关联的 ThoughtDef（心情）。`PreceptComp_SituationalThought` 必填。 |
| `comps/li/eventDef` | 164.1% (366/223) | 文本 | 该 comp 监听的历史事件 defName（`PreceptComp_KnowsMemoryThought` / `SelfTookMemoryThought` / `DevelopmentPoints` 必填）。 |
| `comps/li/points` | 9.4% (21/223) | 数值 | `PreceptComp_DevelopmentPoints` 的加分值。 |
| `comps/li/removesThought` | 2.7% (6/223) | 文本 | 可选：触发后移除指定 Thought 记忆。 |
| `comps/li/gender` | 10.8% (24/223) | 文本 | 限定性别 `Male`/`Female`（ gendered 版 comp 用）。 |
| `comps/li/mentalBreakDef` | 0.4% (1/223) | 文本 | `PreceptComp_MentalBreak` 要触发的精神崩坏 defName。 |
| `comps/li/displayDescription` | 5.4% (12/223) | 布尔 | 该 comp 是否在 UI 描述里显示（默认 true，置 `false` 可隐藏重复项）。 |
| `comps/li/chance` | 1.8% (4/223) | 数值 | 该 comp 生效的概率（0–1）。 |
| `comps/li/description` | 53.4% (119/223) | 文本 | 该 comp 单独显示的描述文本（会覆盖 `{DESCRIPTION}` 占位）。 |
| `comps/li/eventLabel` | 3.6% (8/223) | 文本 | 历史事件在 UI 上的标签，如 blinded someone。 |
| `comps/li/onlyForNonSlaves` | 4.0% (9/223) | 布尔 | 只对非奴隶生效。 |
| `comps/li/tooltipShowMoodRange` | 5.4% (12/223) | 布尔 | 工具提示里是否显示心情区间。 |
| `comps/li/buildingDef` | 0.4% (1/223) | 文本 | `PreceptComp_*Building*` 类指向的建筑 defName。 |

> `comps/li` 内出现率最高的 Class 依次是：`PreceptComp_KnowsMemoryThought`(181)、`PreceptComp_SituationalThought`(154)、`PreceptComp_SelfTookMemoryThought`(96)、`PreceptComp_UnwillingToDo`(30)、`PreceptComp_DevelopmentPoints`(21)、`PreceptComp_UnwillingToDo_Gendered`(16)、`PreceptComp_UnwillingToDo_Chance`(4)、`PreceptComp_Apparel_DesiredStrong`(1)、`PreceptComp_Apparel_Desired`(1)、`PreceptComp_BedThought`(1)、`PreceptComp_UnwillingToDo_WithDef`(1)。

## 常见坑

1. **`issue` 拼错或没有对应 IssueDef**：戒律永远不会出现在理念编辑界面，日志里也不一定给明显报错。自造议题必须先写 `<IssueDef>`（模板 ①）。原版 76 个 `Precepts_*.xml` 里，IssueDef 与它的 PreceptDef 总在同一文件。
2. **`comps` 引用了不存在的 `thought` / `eventDef`**：加载时报 `Could not find ThoughtDef named ...` / `Could not find ... event`，该 comp 的效果静默失效，但戒律本身照样出现在界面上——最难查的一类问题。跟着原版配对抄最稳：`PreceptComp_SituationalThought` 只需 `thought`；`PreceptComp_KnowsMemoryThought` / `PreceptComp_SelfTookMemoryThought` 需要 `eventDef` + `thought`（可选 `removesThought`）；`PreceptComp_DevelopmentPoints` 需要 `eventDef` + `points`。
3. **`preceptClass=Precept_Ritual` 却没给 `ritualPatternBase`**：仪式无法开始（推测：原版所有 Ritual 类戒律都同时给了这两个字段，未找到反例）。反过来，普通戒律不要乱写 `preceptClass`，写错类名会在打开理念界面时抛异常。
4. **`impact` 不是数字**：原版 PreceptDef 的 `impact` 只有 `Low` / `Medium` / `High` 三个文本取值（`MemeDef` 的 `impact` 才是 0–3 的数字，别混）。
5. **`comps/li` 的属性顺序有约定**：原版大量写成 `<li MayRequire="Ludeon.RimWorld.Ideology" Class="PreceptComp_UnwillingToDo_Gendered">`（先 MayRequire 后 Class），`attrs` 记录就是 `["Class","MayRequire"]`。用 `MayRequire` 引用资料片内容，缺 DLC 时该条会被跳过而不是报错。
6. **由 `ParentName` 继承时列表会被继承**：原版 `Precepts_Ritual.xml` 的写法是抽象基类 `FuneralBase` 放公共字段，子 def 只写 `<defName>` / `<label>` / 差异字段（如 `FuneralNoCorpse` 只覆盖 `ritualPatternBase` 与 `takeNameFrom`）。父级的 `comps/li` 列表也会一起继承；要切断列表继承需显式 `Inherit="False"`（该属性在 RitualPatternDef 的 `<tags>` 上有原版用例 `CelebrationConsumable`，用在 `comps` 上**待验证**）。

## 核验

本模板每个元素都逐字对照过下列原版文件（相对 `RimWorld/Data/`）与字段参考，未使用任何字段表之外的路径：

- `Ideology/Defs/PreceptDefs/Precepts_Ritual.xml` — 抽象基类 `FuneralBase` 逐字段核对了 `issue` / `impact` / `iconPath` / `preceptClass` / `ritualPatternBase` / `allowDuplicates` / `countsTowardsPreceptLimit` / `selectionWeight` / `displayOrderInImpact` / `ignoreLimitsInEditMode` / `receivesExpectationsQualityOffset` / `skipOpportunityLettersBeforeDay` / `classic`；子 def `FuneralNoCorpse` 核对 `ParentName` 继承写法。
- `Ideology/Defs/PreceptDefs/Precepts_Nudity.xml` — 模板 ② 的 `issue`+`comps` 最小结构来自 `Nudity_Male_CoveringFaceDisapproved`（`PreceptComp_SituationalThought` + `thought`）。
- `Core/Defs/PreceptDefs/Precepts_Cannibalism.xml` — `PreceptComp_KnowsMemoryThought` 的 `eventDef`+`thought` 配对（`AteHumanMeatDirect`→`AteRawHumanlikeMeat`）逐字取自 `Cannibalism_Classic`。
- `Ideology/Defs/PreceptDefs/Precepts_Blindness.xml` — `defaultSelectionWeight` / `displayOrderInIssue` / `requiredMemes` / `PreceptComp_DevelopmentPoints` 写法（`Blindness_Respected`）。
- `Ideology/Defs/PreceptDefs/Precepts_Apparel.xml` — `preceptClass=Precept_Apparel` + `workerClass=PreceptWorker_Apparel` + `useChoicesFromBuildingDefs` 组合（`ApparelDesired_Strong_Subordinate`）。
- `Core/Defs/PreceptDefs/Precepts_SpouseCount.xml` — `comps/li` 的 `MayRequire`/`Class` 属性写法与 `gender`、`displayDescription`。
- `Anomaly/Defs/PreceptDefs/Precepts_Inhumanizing.xml` — `IssueDef` + `PreceptDef` + `ThoughtDef` 同文件范例，以及 `PreceptComp_MentalBreak` + `mentalBreakDef`。
- `Biotech/Defs/PreceptDefs/Precepts_Bloodfeeders.xml` — 第二个 IssueDef 范例。
- `Ideology/Defs/PreceptDefs/Precepts_Buildings.xml`（54–67 行） — `buildingRoomRequirements/li` 的 `RoomRequirement_Area` / `RoomRequirement_TerrainWithTags`（`tags/li` = Floor/FineFloor）/ `RoomRequirement_Impressiveness`。
- 出现率数字：`library/03-全量字段参考/字段/PreceptDef.md` 全量字段表（245 条），逐一复制，未改动。
- 机器可读来源：`docs/def-schema.json` 的 `defTypes.PreceptDef`（instances=223、pathCount=245、expansions=Core/Royalty/Ideology/Biotech/Anomaly/Odyssey）。
