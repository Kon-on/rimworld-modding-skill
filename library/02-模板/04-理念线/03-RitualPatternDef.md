# RitualPatternDef

## 用途

RitualPatternDef 描述「一场仪式长什么样、什么时候能办、办完结算什么」：它是理念仪式的外观与规则外壳，本身不带玩家可见的戒律条目。原版把一类仪式的通用部分抽成 `Abstract="True"` 的基类（如 Core 的 `SpeechPatternBase`），再让具体仪式 `ParentName` 继承覆写。它必须被某个 PreceptDef 通过 `ritualPatternBase` 引用才会真正出现在游戏里——光写一个 RitualPatternDef 而不写配套戒律，等于写了一个没人调用的空壳。

## 模板

整份文件可另存为 `EXAMPLE_RitualPatterns.xml` 丢进 `Defs/`。里面引用的 `LeaderSpeech`、`AttendedSpeech`、`DateRitual`、`CelebratedDate`、`SpeechPatternBase`、`UI/Icons/Rituals/RitualFestival` 都是原版真实存在的名字，保证可直接加载；`EXAMPLE_HarvestFestival` 与配套戒律 `EXAMPLE_HarvestFestivalPrecept` 演示了两者的绑定关系。

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Defs>

  <!-- ============ ① 最小可用：一个随时可办、无需义务目标的仪式 ============ -->
  <RitualPatternDef>
    <defName>EXAMPLE_SkyRite</defName>
    <!-- ritualBehavior 指向已有的 RitualBehaviorDef；原版实际用过的值有 ChildBirth / DateRitual / Funeral / TreeConnection / LeaderSpeech / Conversion 等，不要自造 -->
    <ritualBehavior>LeaderSpeech</ritualBehavior>
    <!-- ritualOutcomeEffect 指向已有的 RitualOutcomeEffectDef；原版用过的值有 AttendedSpeech / AttendedFuneral / AttendedFuneralNoCorpse / CelebratedDate / Conversion 等 -->
    <ritualOutcomeEffect>AttendedSpeech</ritualOutcomeEffect>
    <!-- 义务目标筛选器：什么时候/在哪里能办；下面这个表示“任何理念建筑或仪式点” -->
    <ritualObligationTargetFilter>AnyIdeoBuildingOrRitualSpot</ritualObligationTargetFilter>
    <!-- 实际执行时选目标用的筛选器；原版其它取值：AltarOrRitualSpot / AltarIdeogramOrRitualSpot / UsableThrone -->
    <ritualTargetFilter>IdeoBuildingOrRitualSpot</ritualTargetFilter>
    <alwaysStartAnytime>true</alwaysStartAnytime>
    <ritualOnlyForIdeoMembers>false</ritualOnlyForIdeoMembers>
    <canMergeGizmosFromDifferentIdeos>false</canMergeGizmosFromDifferentIdeos>
    <!-- 仪式命名规则包；原版仪式只用到 NamerRitualFuneral / NamerRitualFestival / NamerRitualSacrifice / NamerRitualGladiatorDuel / NamerRitualMutilation -->
    <nameMaker>NamerRitualFestival</nameMaker>
    <patternGroupTag>EXAMPLE_SkyRite</patternGroupTag>
    <shortDescOverride>sky rite</shortDescOverride>
    <descOverride>Everyone gathers under the open sky while the leader speaks of the worlds beyond.</descOverride>
    <iconPathOverride>UI/Icons/Rituals/RitualFestival</iconPathOverride>
    <!-- 支持 {DATE} {MEMBERS} {IDEOLIGION_adjective} {PAWN_nameDef} 等占位符（见原版样例） -->
    <ritualExpectedDesc>You can hold a {IDEOLIGION_adjective} sky rite with {MEMBERS}.</ritualExpectedDesc>
    <ritualExpectedDescNoAdjective>You can hold a sky rite with {MEMBERS}.</ritualExpectedDescNoAdjective>
    <ritualExplanation>Speaking of the sky strengthens the community's resolve.</ritualExplanation>
    <playsIdeoMusic>true</playsIdeoMusic>
    <!-- 技术等级门槛，值为 TechLevel 文本：Neolithic / Medieval / Industrial / Spacer 等 -->
    <minTechLevel>Neolithic</minTechLevel>
    <!-- 地图层黑名单：在轨道层上不提供此仪式；MayRequire 保证只有装了对应资料片时才解析这个值 -->
    <layerBlacklist>
      <li MayRequire="Ludeon.RimWorld.Odyssey">Orbit</li>
    </layerBlacklist>
  </RitualPatternDef>

  <!-- ============ ② 义务型节日：由日期触发 + 带标签，继承 Core 的抽象基类 ============ -->
  <RitualPatternDef ParentName="SpeechPatternBase">
    <defName>EXAMPLE_HarvestFestival</defName>
    <ritualBehavior>DateRitual</ritualBehavior>
    <ritualOutcomeEffect>CelebratedDate</ritualOutcomeEffect>
    <ritualObligationTargetFilter>GatheringSpotOrAltar</ritualObligationTargetFilter>
    <ritualTargetFilter>AltarOrRitualSpot</ritualTargetFilter>
    <!-- 义务触发器：每个 li 必须带 Class 属性。原版 Class 全集只有 5 个：
         RitualObligationTrigger_MemberDiedProperties / _MemberCorpseDestroyedProperties /
         _DateProperties / _ScarificationProperties / _BlindingProperties -->
    <ritualObligationTriggers>
      <li Class="RitualObligationTrigger_DateProperties">
        <mustBePlayerIdeo>true</mustBePlayerIdeo>
      </li>
    </ritualObligationTriggers>
    <!-- 标签：可被 MemeDef 的 replaceRitualsWithTags 等按标签整体引用。
         原版全部取值只有 8 个：TreeConnection / CelebratedDate / Sacrifice / Consumable / Mutilation /
         ScarificationCeremony / BlindingCeremony / Execution。
         Inherit 属性表示是否继承父 def 的标签；<tags Inherit="False"> 可清空继承（原版 CelebrationConsumable 的写法）。 -->
    <tags Inherit="False">
      <li>CelebratedDate</li>
    </tags>
    <patternGroupTag>CelebratedDate</patternGroupTag>
    <canStartAnytime>true</canStartAnytime>
    <ritualOnlyForIdeoMembers>false</ritualOnlyForIdeoMembers>
    <playsIdeoMusic>false</playsIdeoMusic>
    <shortDescOverride>harvest festival</shortDescOverride>
    <descOverride>Once a year the community gathers to celebrate another turn of the seasons.</descOverride>
    <ritualExpectedDesc>Every year on {DATE}, {MEMBERS} can hold a harvest festival.</ritualExpectedDesc>
    <maxTechLevel>Industrial</maxTechLevel>
  </RitualPatternDef>

  <!-- ============ ③ 配套戒律：RitualPatternDef 必须被 PreceptDef.ritualPatternBase 引用才会生效 ============ -->
  <PreceptDef>
    <defName>EXAMPLE_HarvestFestivalPrecept</defName>
    <label>harvest festival</label>
    <description>A yearly gathering to mark the turning of the seasons.</description>
    <issue>Ritual</issue>
    <impact>Medium</impact>
    <iconPath>UI/Icons/Rituals/RitualFestival</iconPath>
    <preceptClass>Precept_Ritual</preceptClass>
    <!-- 这里填上面那个 RitualPatternDef 的 defName，两者由此绑定 -->
    <ritualPatternBase>EXAMPLE_HarvestFestival</ritualPatternBase>
    <countsTowardsPreceptLimit>false</countsTowardsPreceptLimit>
  </PreceptDef>

</Defs>
```

## 字段说明

> 注意：本 DefType **没有任何出现率 ≥90% 的字段**。原版 31 个实例里最高的三项也只有 87.1%，所以「写少了」是常态——字段出现率低不代表可以不写，而是说明每个仪式的写法差异很大。深层嵌套路径的出现率会按「同一 def 内出现多次」累加，可能超过 100%。

| 字段 | 出现率 | 值类型 | 说明 |
| --- | --- | --- | --- |
| `defName` | 87.1% (27/31) | 文本 | 必填。全局唯一 ID；PreceptDef 的 `ritualPatternBase` 就是填这个值。 |
| `ritualBehavior` | 87.1% (27/31) | 文本 | **最关键的字段**。指向已有的 RitualBehaviorDef（原版样例：ChildBirth、DateRitual、Funeral、TreeConnection、LeaderSpeech、Conversion），决定仪式执行时跑哪套行为逻辑。 |
| `ritualOutcomeEffect` | 83.9% (26/31) | 文本 | 指向已有的 RitualOutcomeEffectDef（原版样例：AttendedSpeech、AttendedFuneral、AttendedFuneralNoCorpse、CelebratedDate、Conversion），决定仪式成功/失败后结算什么。 |
| `ritualObligationTargetFilter` | 71.0% (22/31) | 文本 | 「何时可以办」的目标筛选器（原版样例：AnyEmptyGrave、GraveWithTargetsCorpse、GauranlenTree、AnyIdeoBuildingOrRitualSpot、RitualSpotOrAltar、GatheringSpotOrAltar、ChristmasTree）。 |
| `ritualTargetFilter` | 19.4% (6/31) | 文本 | 仪式执行时选目标用的筛选器（原版样例：IdeoBuildingOrRitualSpot、AltarOrRitualSpot、AltarIdeogramOrRitualSpot、UsableThrone）。 |
| `ritualObligationTriggers/li` | 16.1% (5/31) | 容器 | 义务触发器列表，**每个 li 必须带 Class 属性**。原版 Class 全集只有 5 个：`RitualObligationTrigger_MemberDiedProperties`、`RitualObligationTrigger_MemberCorpseDestroyedProperties`、`RitualObligationTrigger_DateProperties`、`RitualObligationTrigger_ScarificationProperties`、`RitualObligationTrigger_BlindingProperties`。（元素可用属性：Class） |
| `ritualObligationTriggers/li/mustBePlayerIdeo` | 16.1% (5/31) | 布尔 | 该触发器是否只对玩家理念生效。 |
| `alwaysStartAnytime` | 29.0% (9/31) | 布尔 | 是否永远可以随时开始（不受日期/义务限制）。 |
| `canStartAnytime` | 22.6% (7/31) | 布尔 | 是否允许任何时候手动开始。 |
| `ritualOnlyForIdeoMembers` | 29.0% (9/31) | 布尔 | 是否只允许理念成员参加。 |
| `ritualExpectedDesc` | 9.7% (3/31) | 文本 | 在 UI/提示里预告该仪式的文案，支持 `{DATE}`、`{MEMBERS}`、`{IDEOLIGION_adjective}`、`{PAWN_nameDef}` 等占位符（占位符清单见原版样例）。 |
| `ritualExpectedDescNoAdjective` | 6.5% (2/31) | 文本 | 同上但不带理念形容词的版本。 |
| `ritualExplanation` | 3.2% (1/31) | 文本 | 仪式用途说明（原版 Conversion 用它解释「成功后对方信念会下降或被转化」）。 |
| `shortDescOverride` | 29.0% (9/31) | 文本 | 覆盖简短描述（如 animal sacrifice、dance party）。 |
| `descOverride` | 29.0% (9/31) | 文本 | 覆盖完整描述文本。 |
| `iconPathOverride` | 38.7% (12/31) | 文本 | 覆盖仪式图标贴图路径（如 UI/Icons/Rituals/TreeConnection）。 |
| `nameMaker` | 16.1% (5/31) | 文本 | 仪式取名规则包 defName（原版仪式用到的只有：NamerRitualFuneral、NamerRitualFestival、NamerRitualSacrifice、NamerRitualGladiatorDuel、NamerRitualMutilation）。 |
| `patternGroupTag` | 29.0% (9/31) | 容器/文本 | 模式分组标签，用来把同类仪式归到一组（GUI 合并/分组用）。 |
| `tags/li` | 25.8% (8/31) | 文本 | 标签，用于被 MemeDef 的 `replaceRitualsWithTags` 等按标签引用。原版全部取值只有 8 个：TreeConnection、CelebratedDate、Sacrifice、Consumable、Mutilation、ScarificationCeremony、BlindingCeremony、Execution。 |
| `tags` | 29.0% (9/31) | 容器 | 标签容器。**可带 `Inherit` 属性**，抽象基类写 `<tags Inherit="False">` 可清空从父 def 继承来的标签（原版 CelebrationConsumable 就是这种写法）。（元素可用属性：Inherit） |
| `playsIdeoMusic` | 25.8% (8/31) | 布尔 | 仪式时是否播放理念音乐。 |
| `minTechLevel` | 3.2% (1/31) | 文本 | 最低技术等级（文本，如 Neolithic / Industrial）。 |
| `maxTechLevel` | 3.2% (1/31) | 文本 | 最高技术等级，用于让仪式只在低技术阶段出现。 |
| `layerBlacklist/li` | 3.2% (1/31) | 文本 | 黑名单地图层（如 `Orbit`），该层上不提供此仪式。元素可用 `MayRequire` 属性标注资料片依赖。（元素可用属性：MayRequire） |
| `layerBlacklist` | 3.2% (1/31) | 容器 | 黑名单容器。 |
| `ignoreConsumableBuildingRequirement` | 3.2% (1/31) | 布尔 | 为 true 时忽略消耗型建筑的要求（如不需要圣诞树就能办）。 |
| `ignoreExtremeTemperatures` | 3.2% (1/31) | 布尔 | 为 true 时不受极端温度影响。 |
| `allowOtherInstances` | 3.2% (1/31) | 布尔 | 是否允许同时存在其它实例。 |
| `beginRitualOverride` | 6.5% (2/31) | 文本 | 覆盖「开始仪式」按钮的文字，可带 `{0}` 占位符。 |
| `cancelIconPathOverride` | 3.2% (1/31) | 文本 | 覆盖取消图标的贴图路径。 |
| `showIdeoIconsInDialog` | 3.2% (1/31) | 布尔 | 是否在对话框里显示理念图标。 |
| `canMergeGizmosFromDifferentIdeos` | 6.5% (2/31) | 布尔 | 不同理念的同类仪式 gizmo 是否合并。 |
| `mergeGizmosForObligations` | 6.5% (2/31) | 布尔 | 义务型仪式的 gizmo 是否合并显示。 |

## 常见坑

1. **没有配套戒律**：RitualPatternDef 只是「外壳」，必须被某个 PreceptDef 的 `ritualPatternBase` 引用（同时 `issue` 写 `Ritual`、`preceptClass` 写 `Precept_Ritual`）才会在游戏里出现；只写 pattern 不会报错，但玩家永远看不到这个仪式。
2. **漏写 `ritualOutcomeEffect`**：原版 83.9% 的 pattern 都写了它。它是仪式结算的唯一入口，缺省时仪式结束后没有任何结果（推测：结算找不到效果对象，可能直接走默认空实现）。
3. **`ritualBehavior` 自造类名**：它必须指向已有的 RitualBehaviorDef（ChildBirth / DateRitual / Funeral / TreeConnection / LeaderSpeech / Conversion 等）。写一个不存在的名字，仪式按钮会出现但点了没有行为（推测：行为对象为 null）。
4. **`ritualObligationTriggers/li` 忘了 `Class` 属性**：原版 5 个用例全部带 Class（`RitualObligationTrigger_DateProperties` 等），没有 Class 的 li 无法实例化出触发器（推测），日期/死亡/致盲类义务就永远不会触发。另外 `mustBePlayerIdeo` 决定该义务是否只对玩家理念生效，原版一律显式写 `true`。
5. **`<tags>` 的 Inherit 没写**：用 `ParentName` 继承抽象基类时，父 def 的标签会一并继承。原版 `CelebrationConsumable` 用 `<tags Inherit="False">` 显式清空；如果你只想加自己的标签又不想继承父 def 的，就必须写 `Inherit="False"`。
6. **技术等级门槛写反**：`minTechLevel`/`maxTechLevel` 是 TechLevel 文本（Neolithic / Medieval / Industrial / Spacer 等），用 `maxTechLevel=Neolithic` 表示「只有部落阶段才有」。写错会导致仪式在该文明阶段静默消失。
7. **`ritualExpectedDesc` 的占位符**：原版样例里出现过 `{DATE}`、`{MEMBERS}`、`{IDEOLIGION_adjective}`、`{PAWN_nameDef}`，但**占位符全集未穷举（待验证）**——不确定的占位符不要写，宁可用纯文本。

## 核验

- **字段说明表**：全部 33 行路径逐条从 `<REPO_ROOT>\docs\def-schema.json` 的 `defTypes.RitualPatternDef`（31 个实例、34 条路径）提取，写入前用脚本断言路径存在（0 缺失）；出现率数字与 `03-全量字段参考\字段\RitualPatternDef.md` 一致。
- **① 骨架**逐字对照 `Ideology/Defs/PreceptDefs/RitualPatternDefs/RitualPatterns.xml` 的 `LeaderSpeech`（ritualBehavior/ritualObligationTargetFilter/ritualTargetFilter/alwaysStartAnytime/ritualOnlyForIdeoMembers/canMergeGizmosFromDifferentIdeos）与 `Conversion`（ritualOutcomeEffect/ritualExplanation）。
- **② 义务型**对照同文件 `CelebrationPartyChat`（ritualObligationTriggers + `Class="RitualObligationTrigger_DateProperties"` + mustBePlayerIdeo、tags/li=CelebratedDate、patternGroupTag=CelebratedDate、ritualBehavior=DateRitual、ritualOutcomeEffect=CelebratedDate）与 `CelebrationTree`（iconPathOverride、descOverride、shortDescOverride、ignoreConsumableBuildingRequirement）。
- **`tags` 的 `Inherit` 属性与 `Inherit="False"` 用法**：取自同文件 `CelebrationConsumable`（Abstract 且 `<tags Inherit="False">`）。
- **父 def 继承写法**：`Core/Defs/PreceptDefs/RitualPatternDefs/RitualPatterns.xml` 只有 1 个块（`RitualPatternDef Abstract="True" Name="SpeechPatternBase"` + `ritualOutcomeEffect=AttendedSpeech`），本模板 ② 的 `ParentName="SpeechPatternBase"` 即指向它。
- **取值全集**（写进常见坑的硬数字）均由全库扫描确认：`tags/li` 8 个取值、`ritualObligationTriggers` 的 Class 5 个取值、仪式 `nameMaker` 5 个取值、`layerBlacklist/li` 的 `MayRequire` 属性用法取自 `CelebrationSkyLanterns`。
- **③ 联动**：`ritualPatternBase` 的取值来自 `Ideology/Defs/PreceptDefs/Precepts_Ritual.xml` 的 `FuneralBase`（`issue=Ritual`、`preceptClass=Precept_Ritual`、`ritualPatternBase=FuneralStandard`）。
- 未启动游戏加载验证；元素名、属性名、取值均来自上述原版文件与字段表。
