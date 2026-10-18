# ResearchProjectDef

## 用途

研究项目（科技）定义。写它来让一个新科技出现在「研究」界面的科技树上：由 `baseCost` 决定研究点花费，`researchViewX`/`researchViewY` 决定树上的坐标，`prerequisites` 与 `hiddenPrerequisites` 决定什么时候能开始研究，`requiredResearchBuilding` 与 `requiredResearchFacilities` 决定必须用哪个研究台和附加设施。

它本身不「给」任何东西——真正被解锁的内容挂在别的 Def 上，通过反向字段引用本 Def 的 defName：`ThingDef/researchPrerequisites`（原版出现率 7.35%，151/2054）、`ThingDef/recipeMaker/researchPrerequisite`（8.13%，167/2054）、`RecipeDef/researchPrerequisite`（9.91%，21/212）、`TerrainDef/researchPrerequisites`（7.3%，10/137）、`DesignationCategoryDef/researchPrerequisites`（18.8%，3/16）。

联动的 Def：`ResearchTabDef`（`tab` 的取值来源，原版只有 Main、Anomaly 两个）、`ResearchProjectTagDef`（`tags` 的取值来源，原版 5 个）、`ThingDef`（研究台 HiTechResearchBench、附加设施 MultiAnalyzer、科技图纸相关）。原版 1.7 共 168 个实例、43 条字段路径。

## 模板

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Defs>

  <!-- 普通研究项目：全部字段路径均取自原版 1.7 实有的路径 -->
  <ResearchProjectDef>
    <defName>EXAMPLE_AlienMetallurgy</defName>
    <label>alien metallurgy</label>
    <description>Unlock alloy smelting and the arc smelter.</description>

    <!-- 研究点花费。原版 114/168 写了它；Anomaly 的知识研究改用 knowledgeCost -->
    <baseCost>1500</baseCost>

    <!-- 科技等级：原版只出现过 Neolithic / Medieval / Industrial / Spacer / Ultra -->
    <techLevel>Industrial</techLevel>

    <!-- 显式前置科技：必须是 ResearchProjectDef 的 defName -->
    <prerequisites>
      <li>Smithing</li>
      <li>Electricity</li>
    </prerequisites>

    <!-- 隐藏前置：界面上不显示，但同样卡住进度。原版 33/168 使用 -->
    <hiddenPrerequisites>
      <li>Machining</li>
    </hiddenPrerequisites>

    <!-- 必须在该研究台研究（原版唯一取值就是它）；附加设施原版唯一取值 MultiAnalyzer -->
    <requiredResearchBuilding>HiTechResearchBench</requiredResearchBuilding>
    <requiredResearchFacilities>
      <li>MultiAnalyzer</li>
    </requiredResearchFacilities>

    <!-- 科技树坐标：X 越大越靠后（越晚解锁），Y 越大越靠上 -->
    <researchViewX>14.00</researchViewX>
    <researchViewY>4.00</researchViewY>

    <!-- 研究页签，必须匹配某个 ResearchTabDef 的 defName（原版：Main / Anomaly） -->
    <tab>Main</tab>

    <!-- 开局筛选标签，必须匹配某个 ResearchProjectTagDef 的 defName -->
    <tags>
      <li>ClassicStart</li>
    </tags>

    <!-- 研究进度叙述文本：li 以 subject-> / subject_story-> / subject_gerund-> 开头 -->
    <generalRules>
      <rulesStrings>
        <li>subject->alien metallurgy</li>
        <li>subject_story->reverse-engineered an alien alloy</li>
        <li>subject_gerund->studying alien alloys</li>
      </rulesStrings>
    </generalRules>
  </ResearchProjectDef>

  <!-- 科技图纸（techprint）变体：Royalty 的帝国科技就是这套写法 -->
  <ResearchProjectDef>
    <defName>EXAMPLE_EmpireAlloyPlating</defName>
    <label>empire alloy plating</label>
    <description>Unlock empire-derived alloy plating.</description>
    <baseCost>2000</baseCost>
    <techLevel>Spacer</techLevel>
    <prerequisites>
      <li>EXAMPLE_AlienMetallurgy</li>
    </prerequisites>
    <requiredResearchBuilding>HiTechResearchBench</requiredResearchBuilding>
    <researchViewX>16.00</researchViewX>
    <researchViewY>4.00</researchViewY>

    <!-- 科技图纸：需要买到/捡到 techprintCount 张图纸，市场价 techprintMarketValue -->
    <techprintCount>1</techprintCount>
    <techprintCommonality>1</techprintCommonality>
    <techprintMarketValue>1000</techprintMarketValue>

    <!-- 只有具备该派系类别的派系会持有这项科技（原版取值：Empire、Outlander） -->
    <heldByFactionCategoryTags>
      <li>Empire</li>
    </heldByFactionCategoryTags>

    <generalRules>
      <rulesStrings>
        <li>subject->empire alloy plating</li>
        <li>subject_gerund->studying empire alloys</li>
      </rulesStrings>
    </generalRules>
  </ResearchProjectDef>

</Defs>
```

## 字段说明

全量 43 条路径（出现率 = 该路径在原版 168 个实例中的出现比例）。

| 字段 | 出现率 | 值类型 | 说明 |
|---|---|---|---|
| `defName` | 97.6% (164/168) | 文本 | Def 唯一 ID；缺它的 4 个都是 Abstract 基类 |
| `label` | 97.6% (164/168) | 文本 | 研究界面显示名 |
| `description` | 97.6% (164/168) | 文本 | 研究界面说明文字 |
| `baseCost` | 67.9% (114/168) | 数值 | 研究点花费，原版取值 200~4000+ |
| `techLevel` | 67.3% (113/168) | 文本 | 原版取值 Industrial 71 / Spacer 19 / Medieval 12 / Neolithic 9 / Ultra 2 |
| `prerequisites` | 86.9% (146/168) | 容器 | 显式前置科技列表 |
| `prerequisites/li` | 102.4% (172/168) | 文本 | 一个 ResearchProjectDef 的 defName |
| `researchViewX` | 97.6% (164/168) | 数值 | 科技树坐标 X |
| `researchViewY` | 97.6% (164/168) | 数值 | 科技树坐标 Y |
| `generalRules` | 97.6% (164/168) | 容器 | 研究叙述规则容器 |
| `generalRules/rulesStrings` | 97.6% (164/168) | 容器 | 叙述字符串容器 |
| `generalRules/rulesStrings/li` | 578.6% (972/168) | 文本 | 形如 subject->…、subject_story->…、subject_gerund->… |
| `hiddenPrerequisites` | 19.6% (33/168) | 容器 | 隐藏前置：不显示但限制进度 |
| `hiddenPrerequisites/li` | 22.0% (37/168) | 文本 | 同上，ResearchProjectDef 的 defName |
| `requiredResearchBuilding` | 28.6% (48/168) | 文本 | 原版唯一取值 HiTechResearchBench |
| `requiredResearchFacilities` | 13.7% (23/168) | 容器 | 附加研究设施列表 |
| `requiredResearchFacilities/li` | 13.7% (23/168) | 文本 | 原版唯一取值 MultiAnalyzer |
| `tab` | 23.8% (40/168) | 文本 | 原版唯一取值 Anomaly（其余 128 个不写，落在 Main 页） |
| `knowledgeCategory` | 23.8% (40/168) | 文本 | 知识研究分类，原版 Basic 21 / Advanced 19 |
| `knowledgeCost` | 23.8% (40/168) | 数值 | 知识研究的花费，替代 baseCost，原版取值 5 / 10 / 20 |
| `tags` | 7.7% (13/168) | 容器 | 开局筛选标签列表 |
| `tags/li` | 8.3% (14/168) | 文本 | 原版取值 TribalStart / ClassicStart / ShipRelated |
| `techprintCount` | 1.8% (3/168) | 数值 | 需要多少张科技图纸，原版 1 / 2 |
| `techprintCommonality` | 1.8% (3/168) | 数值 | 图纸出现常见度，原版 1 / 2 / 3 |
| `techprintMarketValue` | 4.2% (7/168) | 数值 | 图纸市场价，原版 1000 / 1500 / 2000 |
| `heldByFactionCategoryTags` | 2.4% (4/168) | 容器 | 持有该科技的派系类别 |
| `heldByFactionCategoryTags/li` | 2.4% (4/168) | 文本 | 原版取值 Empire / Outlander |
| `requiredAnalyzed` | 2.4% (4/168) | 容器 | 必须先分析过的物品 |
| `requiredAnalyzed/li` | 2.4% (4/168) | 文本 | 原版取值 NanostructuringChip / PowerfocusChip / SignalChip |
| `discoveredLetterTitle` | 2.4% (4/168) | 文本 | 首次解锁时的信件标题 |
| `discoveredLetterText` | 2.4% (4/168) | 文本 | 首次解锁时的信件正文 |
| `discoveredLetterDisabledWhen` | 0.6% (1/168) | 容器 | 满足条件时不发解锁信件 |
| `discoveredLetterDisabledWhen/bigThreatsDisabled` | 0.6% (1/168) | 布尔 | 原文样例 true |
| `hideWhen` | 4.8% (8/168) | 容器 | 按游戏设置隐藏该项目 |
| `hideWhen/turretsDisabled` | 3.6% (6/168) | 布尔 | 关闭炮塔时隐藏 |
| `hideWhen/trapsDisabled` | 0.6% (1/168) | 布尔 | 关闭陷阱时隐藏 |
| `hideWhen/mortarsDisabled` | 0.6% (1/168) | 布尔 | 关闭迫击炮时隐藏 |
| `teachConcept` | 1.2% (2/168) | 文本 | 解锁时教学的概念 defName，原版 Fishing / VoidProvocation |
| `customUnlockTexts` | 0.6% (1/168) | 容器 | 自定义解锁提示文本 |
| `customUnlockTexts/li` | 0.6% (1/168) | 文本 | 原文样例 Fishing zone |
| `recalculatePower` | 0.6% (1/168) | 布尔 | 原文样例 true |
| `requireGravEngineInspected` | 0.6% (1/168) | 布尔 | 原文样例 true |
| `requiresMechanitor` | 0.6% (1/168) | 布尔 | 原文样例 true |

## 常见坑

1. **`baseCost` 不是必填，但省掉后要自己兜底。** 原版 54/168 没写：Anomaly 40 个改用 `knowledgeCost`；Royalty 12 个靠 `ParentName` 从基类继承（Royalty/Defs/ResearchProjectDefs/ResearchProjects_Implants.xml 的 :24/:51/:77/:103 都是 ParentName=BaseBodyPartEmpire_TierA，基类 baseCost 2000）；另有 3 个 Abstract 基类。既不写、也无可继承父 Def，就得到一个「不需要研究点」的项目——缺省值本身未反编译核实（待验证）。
2. **`prerequisites/li` 里写的是 ResearchProjectDef 的 defName，不是解锁物的 ThingDef 名。** 容易混是因为原版存在同名：`MultiAnalyzer` 既是 ThingDef，也是 ResearchProjectDef（Core/Defs/ResearchProjectDefs/ResearchProjects_4_MultiAnalyzer.xml:4），所以 "&lt;li&gt;MultiAnalyzer&lt;/li&gt;" 合法。若你写了一个没有同名研究项目的 ThingDef 名，前置不会生效（推测）。
3. **`tab` 必须匹配某个 `ResearchTabDef` 的 defName。** 原版只有 Main 与 Anomaly；除 Anomaly 那 40 个实例外，其余 128 个都不写 `tab` 且都出现在 Main 页（默认 Main，机理未反编译，待验证）。写一个不存在的页签名，项目在研究界面里会找不到（推测）。
4. **`researchViewX`/`researchViewY` 省略会让图标全部叠在原点。** 原版 164/168 都写。坐标相邻的项目要留间距，否则科技树图标重叠难以点选。
5. **`techLevel` 的自创或拼错值不会被纠正。** 原版只出现 Industrial(71) / Spacer(19) / Medieval(12) / Neolithic(9) / Ultra(2) 五个值；照抄其中之一的拼写最安全。
6. **只写研究项目不会解锁任何东西。** 解锁必须在目标 Def 上反向引用：ThingDef 用 `researchPrerequisites`（7.35%）或 `recipeMaker/researchPrerequisite`（8.13%，单值）/`recipeMaker/researchPrerequisites`（0.05%，列表），RecipeDef 用 `researchPrerequisite`（9.91%），TerrainDef 用 `researchPrerequisites`（7.3%），DesignationCategoryDef 用 `researchPrerequisites`（18.8%）。
7. **`generalRules/rulesStrings/li` 必须以 `subject->`、`subject_story->` 或 `subject_gerund->` 前缀开头。** 原版 972 条实例全部如此；原版唯一不写 `generalRules` 的 4 个实例都是 Abstract 基类，普通项目建议照写。

## 核验

本模板逐字段对照的原版位置（相对 <游戏安装目录>\Data\）：

| 模板里的写法 | 原版依据 |
|---|---|
| `baseCost` + `techLevel` + `prerequisites` + `hiddenPrerequisites` + `requiredResearchBuilding` + `researchViewX/Y` + `generalRules` | Core/Defs/ResearchProjectDefs/ResearchProjects_4_MultiAnalyzer.xml:4（MultiAnalyzer，baseCost 4000 / Industrial / hiddenPrerequisites Machining / viewX 14.00 / viewY 3.00） |
| `tags`、`researchViewX/Y` 的又一实例 | Core/Defs/ResearchProjectDefs/ResearchProjects_1.xml:6（PsychoidBrewing，baseCost 500 / Neolithic / TribalStart / viewX 2.00 / viewY 0.70） |
| `requiredResearchFacilities` + `prerequisites` 多值 | Ideology/Defs/ResearchProjectDefs/ResearchProjects_Misc.xml:3（Biosculpting 1500/Industrial/HiTechResearchBench）、:32（Bioregeneration 4000 + MultiAnalyzer） |
| `techprintCount`/`techprintCommonality`/`techprintMarketValue`/`heldByFactionCategoryTags` 与 `ParentName` 继承 | Royalty/Defs/ResearchProjectDefs/ResearchProjects_Implants.xml:4（Abstract TierA）、:13（TierB，techLevel Ultra）、:103（VenomSynthesis） |
| `tab` 的取值来源 | Core/Defs/ResearchProjectDefs/ResearchTabs.xml:6（ResearchTabDef Main；同文件注释说明如何新增页签并让项目的 tab 与之匹配）、Anomaly 侧的 Anomaly 页签 |
| 各字段出现率 | library/03-全量字段参考/字段/ResearchProjectDef.md（168 实例 / 43 路径），由 docs/def-schema.json 实测生成 |
