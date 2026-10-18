# RecipeDef

## 用途

RecipeDef 描述"在某个台子上把输入变成输出"：`ingredients`（输入，每项含 `count` 与 `filter`）、`products`（产物，子元素名就是产物的 defName）、`workAmount`（工作量）。制造类配方用 `recipeUsers` 指明在哪座台子上可用（或反过来由建筑 ThingDef 的 `recipeMaker` 声明），`fixedIngredientFilter` 决定清单里哪些材料可选，`specialProducts` 用于"产出由输入决定"的配方（屠宰、切石）。手术类配方则改用 `addsHediff` / `removesHediff` + `appliedOnFixedBodyParts`。它与 ThingDef（输入/产物/台子）、HediffDef、StatDef（`workSpeedStat`、`efficiencyStat`）、SpecialThingFilterDef 联动。

**先纠正一个印象**：RecipeDef 的字段表统计偏向手术类（212 个实例里 32.6% 有 `addsHediff`），但字段名对制造类完全通用；制造类实例见 `Core/Defs/RecipeDefs/Recipes_Production.xml`。全类型只有 3 条字段达到 ≥90%：`ingredients/li`、`ingredients/li/count`、`ingredients/li/filter`。

## 模板

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Defs>

  <!-- ================= 1) 制造类配方：输入固定材料，产出固定产物 ================= -->
  <RecipeDef>
    <defName>EXAMPLE_Make_Coilgun</defName>
    <label>制造线圈枪</label>
    <description>把钢铁和组件组装成一把线圈枪。</description>
    <jobString>正在制造线圈枪。</jobString>
    <workSpeedStat>GeneralLaborSpeed</workSpeedStat>
    <workSkill>Crafting</workSkill>
    <effectWorking>Smith</effectWorking>
    <soundWorking>Recipe_Machining</soundWorking>
    <!-- 工作量：非手术类配方的核心数值 -->
    <workAmount>5000</workAmount>
    <!-- 制造中的半成品（可省；原版枪械用 UnfinishedGun） -->
    <unfinishedThingDef>UnfinishedGun</unfinishedThingDef>
    <!-- 输入：li 包一层，里面是 filter + count -->
    <ingredients>
      <li>
        <filter>
          <thingDefs>
            <li>Steel</li>
          </thingDefs>
        </filter>
        <count>12</count>
      </li>
      <li>
        <filter>
          <thingDefs>
            <li>ComponentIndustrial</li>
          </thingDefs>
        </filter>
        <count>2</count>
      </li>
    </ingredients>
    <!-- 清单里可选的输入（写死，不让玩家换材料） -->
    <fixedIngredientFilter>
      <thingDefs>
        <li>Steel</li>
        <li>ComponentIndustrial</li>
      </thingDefs>
    </fixedIngredientFilter>
    <!-- 产物：元素名 = 产物 ThingDef 的 defName，值是数量 -->
    <products>
      <EXAMPLE_Gun_Coilgun>1</EXAMPLE_Gun_Coilgun>
    </products>
    <skillRequirements>
      <Crafting>6</Crafting>
    </skillRequirements>
    <researchPrerequisite>Gunsmithing</researchPrerequisite>
    <displayPriority>420</displayPriority>
    <!-- 在哪些台子上可用（ThingDef defName） -->
    <recipeUsers>
      <li>TableMachining</li>
      <li>CraftingSpot</li>
    </recipeUsers>
  </RecipeDef>

  <!-- ================= 2) 屠宰类配方：产物由输入决定 ================= -->
  <RecipeDef>
    <defName>EXAMPLE_ButcherCorpseAnimal</defName>
    <label>屠宰动物尸体</label>
    <description>把动物尸体分解成肉与皮。</description>
    <jobString>正在屠宰。</jobString>
    <workAmount>450</workAmount>
    <workSpeedStat>GeneralLaborSpeed</workSpeedStat>
    <workSkill>Cooking</workSkill>
    <effectWorking>ButcherFlesh</effectWorking>
    <soundWorking>Recipe_ButcherCorpseFlesh</soundWorking>
    <!-- 输入开始腐烂时打断工作 -->
    <interruptIfIngredientIsRotting>true</interruptIfIngredientIsRotting>
    <!-- 计数器类名决定"左侧列表按什么归类" -->
    <workerCounterClass>RecipeWorkerCounter_ButcherAnimals</workerCounterClass>
    <ingredients>
      <li>
        <filter>
          <categories>
            <li>Corpses</li>
          </categories>
        </filter>
        <count>1</count>
      </li>
    </ingredients>
    <!-- specialProducts：产物是"按输入算出来的"，不能写 products -->
    <specialProducts>
      <li>Butchery</li>
    </specialProducts>
    <fixedIngredientFilter>
      <categories>
        <li>Corpses</li>
      </categories>
      <disallowedCategories>
        <li>CorpsesMechanoid</li>
      </disallowedCategories>
      <specialFiltersToDisallow>
        <li>AllowRotten</li>
      </specialFiltersToDisallow>
    </fixedIngredientFilter>
    <defaultIngredientFilter>
      <categories>
        <li>CorpsesAnimal</li>
      </categories>
    </defaultIngredientFilter>
  </RecipeDef>

</Defs>
```

## 字段说明

出现率来自 `03-全量字段参考/字段/RecipeDef.md`（分母 212）。

| 字段 | 出现率 | 值类型 | 说明 |
|---|---|---|---|
| `defName` | 88.7% (188/212) | 文本 | 配方唯一名。 |
| `label` | 88.7% (188/212) | 文本 | 清单里显示的名字。 |
| `description` | 88.7% (188/212) | 文本 | 悬浮说明。 |
| `jobString` | 75.0% (159/212) | 文本 | 小人工作时的状态文字（"Butchering."）。 |
| `ingredients` | 71.2% (151/212) | 容器 | 输入总容器。 |
| `ingredients/li` | 100.0% (212/212) | 容器 | **必写**：每个输入项一层 li。 |
| `ingredients/li/count` | 99.5% (211/212) | 数值 | **必写**：数量（0.25 / 1 / 2）。 |
| `ingredients/li/filter` | 100.0% (212/212) | 容器 | **必写**：该输入允许什么。 |
| `ingredients/li/filter/thingDefs` | 71.7% (152/212) | 容器 | 白名单：按具体物价。 |
| `ingredients/li/filter/thingDefs/li` | 72.2% (153/212) | 文本 | 物价 defName（Steel / Medicine …）。 |
| `ingredients/li/filter/categories` | 28.8% (61/212) | 容器 | 白名单：按 ThingCategoryDef。 |
| `ingredients/li/filter/categories/li` | 35.9% (76/212) | 文本 | 分类名（AnimalProductRaw / Corpses / Medicine）。 |
| `ingredients/li/filter/customSummary` | 7.1% (15/212) | 文本 | 自定义摘要文字（feedstock / greens / protein）。 |
| `ingredients/li/filter/disallowedCategories` | 0.5% (1/212) | 容器 | 黑名单：按分类排除。 |
| `ingredients/li/filter/disallowedThingDefs` | 0.9% (2/212) | 容器 | 黑名单：按物价排除（`li` 1.9%）。 |
| `products` | 26.9% (57/212) | 容器 | 产物容器；子元素名 = 产物 defName（如 `products/ComponentIndustrial` 0.5%）。 |
| `specialProducts` | 2.8% (6/212) | 容器 | 特殊产物标记（`li`：Butchery / Smelted / StoneBlocks）。 |
| `workAmount` | 25.5% (54/212) | 数值 | 工作量（1200 / 2000 / 450）。 |
| `workSpeedStat` | 17.0% (36/212) | 文本 | 受哪个速度属性影响（CookSpeed / DrugCookingSpeed / GeneralLaborSpeed）。 |
| `workSkill` | 8.0% (17/212) | 文本 | 受哪个技能影响（Cooking / Crafting / Medicine）。 |
| `effectWorking` | 16.0% (34/212) | 文本 | 工作特效（ButcherFlesh / Cook / CutStone）。 |
| `soundWorking` | 17.0% (36/212) | 文本 | 工作音效（Recipe_Brewing / Recipe_Machining）。 |
| `efficiencyStat` | 0.9% (2/212) | 文本 | 产出效率属性（ButcheryFleshEfficiency）。 |
| `skillRequirements` | 13.7% (29/212) | 容器 | 技能要求容器。 |
| `skillRequirements/Crafting` | 1.4% (3/212) | 数值 | 最低制作技能（8）。 |
| `skillRequirements/Cooking` | 2.8% (6/212) | 数值 | 最低烹饪技能。 |
| `skillRequirements/Medicine` | 8.0% (17/212) | 数值 | 最低医疗技能（3 / 4 / 5，手术类）。 |
| `recipeUsers` | 2.8% (6/212) | 容器 | 可用台子容器（也可由建筑 ThingDef 的 recipeMaker 反推）。 |
| `recipeUsers/li` | 4.2% (9/212) | 文本 | 台子的 ThingDef 名（ElectricTailoringBench / CraftingSpot / Human）。 |
| `researchPrerequisite` | 9.9% (21/212) | 文本 | 前置研究（单个）。 |
| `researchPrerequisites` | 0.5% (1/212) | 容器 | 前置研究（多个，`li` 0.9%）。 |
| `displayPriority` | 14.6% (31/212) | 数值 | 清单排序（100 / 1430 / 1431）。 |
| `fixedIngredientFilter` | 59.9% (127/212) | 容器 | 清单中"可选的输入"白名单。 |
| `fixedIngredientFilter/thingDefs/li` | 50.9% (108/212) | 文本 | 具体可选物价。 |
| `fixedIngredientFilter/categories/li` | 18.4% (39/212) | 文本 | 可选分类（Corpses / FoodRaw）。 |
| `fixedIngredientFilter/disallowedCategories` | 7.1% (15/212) | 容器 | 从可选里排除的分类。 |
| `fixedIngredientFilter/specialFiltersToDisallow` | 3.8% (8/212) | 容器 | 禁用的特殊过滤项（AllowRotten）。 |
| `fixedIngredientFilter/disallowDoesntProduceMeat` | 0.5% (1/212) | 布尔 | 禁掉"不出肉"的尸体。 |
| `defaultIngredientFilter` | 7.1% (15/212) | 容器 | 打开清单时的默认筛选。 |
| `defaultIngredientFilter/disallowedThingDefs/li` | 10.8% (23/212) | 文本 | 默认排除的物价（Apparel_ShieldBelt / InsectJelly）。 |
| `forceHiddenSpecialFilters` | 2.8% (6/212) | 容器 | 强制隐藏的过滤项（`li` 6.6%：AllowFresh）。 |
| `unfinishedThingDef` | 1.4% (3/212) | 文本 | 制造中半成品（UnfinishedComponent / UnfinishedGun）。 |
| `workerCounterClass` | 0.9% (2/212) | 文本 | 清单左侧计数逻辑（RecipeWorkerCounter_ButcherAnimals / _MakeStoneBlocks）。 |
| `workerClass` | 13.2% (28/212) | 文本 | 自定义配方逻辑（Recipe_AddHediff / Recipe_ExtractHemogen）。 |
| `targetCountAdjustment` | 1.4% (3/212) | 数值 | 一次做多少个（1 / 20 / 50）。 |
| `workSkillLearnFactor` | 1.4% (3/212) | 数值 | 技能学习系数（原版切石写 0 = 不涨技能）。 |
| `allowMixingIngredients` | 7.5% (16/212) | 布尔 | 允许同类材料混用。 |
| `ingredientValueGetterClass` | 6.6% (14/212) | 文本 | 输入价值换算器（IngredientValueGetter_Nutrition）。 |
| `requiredGiverWorkType` | 4.2% (9/212) | 文本 | 需要的工作类型（Cooking / Hauling）。 |
| `isViolation` | 6.6% (14/212) | 布尔 | 是否算违规（意识形态相关）。 |
| `uiIconThing` | 4.2% (9/212) | 文本 | 用某件物品的图标（HemogenPack / HumanOvum）。 |
| `uiIconPath` | 0.9% (2/212) | 文本 | 自定义图标路径。 |
| `descriptionHyperlinks` | 51.9% (110/212) | 容器 | 说明里的超链接（`ThingDef` 51.9%、`HediffDef` 37.3%）。 |
| `interruptIfIngredientIsRotting` | 0.5% (1/212) | 布尔 | 输入开始腐烂时打断。 |
| `smeltingWorkAmount` | 0.5% (1/212) | 数值 | 熔炼工作量（1600）。 |
| `dontShowIfAnyIngredientMissing` | 0.5% (1/212) | 布尔 | 缺料时隐藏该配方。 |
| `ignoreIngredientCountTakeEntireStacks` | 0.5% (1/212) | 布尔 | 无视数量直接整堆取用。 |
| `addsHediff` | 32.6% (69/212) | 文本 | **手术类**：植入的 HediffDef（AdrenalHeart）。 |
| `removesHediff` | 14.6% (31/212) | 文本 | **手术类**：移除的 HediffDef（Carcinoma / Painstopper）。 |
| `appliedOnFixedBodyParts` | 30.2% (64/212) | 容器 | 固定作用部位（`li`：Heart / Lung / Spine）。 |
| `appliedOnFixedBodyPartGroups` | 0.9% (2/212) | 容器 | 固定作用部位组（`li`：MiddleFingers / Teeth）。 |
| `targetsBodyPart` | 7.5% (16/212) | 布尔 | 是否由玩家选部位（原版多写 false）。 |
| `anesthetize` | 5.2% (11/212) | 布尔 | 是否麻醉。 |
| `hideBodyPartNames` | 7.1% (15/212) | 布尔 | 隐藏部位名。 |
| `surgerySuccessChanceFactor` | 3.3% (7/212) | 数值 | 手术成功率系数（1.2 / 1.5 / 2）。 |
| `deathOnFailedSurgeryChance` | 4.7% (10/212) | 数值 | 失败致死概率（0 / 0.02 / 0.1）。 |
| `surgeryOutcomeEffect` | 6.6% (14/212) | 文本 | 结果特效（SurgeryOutcomeBase / SurgeryOutcomeMinorFailure）。 |
| `addsHediffOnFailure` | 1.9% (4/212) | 文本 | 失败时附加的 Hediff（Sterilized）。 |
| `successfullyRemovedHediffMessage` | 4.7% (10/212) | 文本 | 成功提示（含 {0}/{1} 占位符）。 |
| `incompatibleWithHediffTags` | 3.3% (7/212) | 容器 | 与哪些 Hediff 标签互斥。 |
| `genderPrerequisite` | 2.4% (5/212) | 文本 | 性别前提（Female / Male）。 |
| `minAllowedAge` | 1.4% (3/212) | 数值 | 最低年龄（13 / 16）。 |
| `developmentalStageFilter` | 1.4% (3/212) | 文本 | 发育阶段（Child, Adult）。 |
| `mutantPrerequisite` | 2.8% (6/212) | 容器 | 需要的变异（`li`：Ghoul）。 |
| `gestationCycles` | 3.3% (7/212) | 数值 | 妊娠周期数（1 / 12 / 4）。 |
| `formingTicks` | 0.9% (2/212) | 数值 | 成型 tick（120000 / 30000）。 |
| `mechanitorOnlyRecipe` | 0.5% (1/212) | 布尔 | 仅机械师可用。 |
| `mechResurrection` | 0.5% (1/212) | 布尔 | 机械复活配方。 |

## 常见坑

1. **`ingredients/li` 是必写层级**：`ingredients` 本身只有 71.2%（151/212），但 `ingredients/li` 与 `ingredients/li/filter` 都是 100.0%，`ingredients/li/count` 99.5%（211/212）。把 `filter`/`count` 直接写在 `ingredients` 下不会被识别——包括原版里唯一"没写 count"的那个配方，说明 count 事实上也是必填。
2. **`products` 的子元素名必须是产物 defName**：写法是 `<products><产物defName>数量</产物defName></products>`（如原版 `<ComponentIndustrial>1</ComponentIndustrial>`）。写成 `<li><thingDef>…</thingDef><count>…</count></li>` 是**错误结构**（字段表里 `products` 下只有"按 defName 记名"的子路径与 `products/li`，没有 thingDef/count 子路径）。
3. **"产出由输入决定"要用 `specialProducts`，不能写 `products`**：屠宰（Butchery）、熔炼（Smelted）、切石（StoneBlocks）都走 `specialProducts`（2.8%，6/212），见 `Core/Defs/RecipeDefs/Recipes_Butchery.xml:37` 与 `Recipes_Production.xml:35`。
4. **`recipeUsers` 与建筑上的 `recipeMaker` 是两条入口**：RecipeDef 里写 `recipeUsers` 只有 2.8%（6/212），原版大量制造类配方是靠产物 ThingDef 的 `recipeMaker/recipeUsers`（6.1%，125/2054）挂到台子上的。两个都不给，配方不会出现在任何清单里（**推测**）。
5. **手术类与制造类的关键字段不通用**：制造类看 `products`/`workAmount`，手术类看 `addsHediff`/`removesHediff`/`appliedOnFixedBodyParts`；给制造配方写 `targetsBodyPart` 之类不会有任何效果（**推测**）。
6. **`workAmount` 只是基础值**：实际耗时还受 `workSpeedStat`（17.0%）与 `efficiencyStat`（0.9%）影响；只改 `workAmount` 看不出速度差异（**推测**）。

## 核验

- **逐字段对照**：上表出现率取自 `03-全量字段参考/字段/RecipeDef.md`（分母 212），可用机器可读版复核：
  `Select-String -Path '03-全量字段参考\字段总表.csv' -Pattern ',RecipeDef,ingredients/li/count,'`。
- **结构照抄原版**（路径相对 `<游戏安装目录>\Data\`）：
  - `Core/Defs/RecipeDefs/Recipes_Production.xml`：MakeStoneBlocksBase（第 4 行，workAmount/workSpeedStat/recipeUsers 写法）、Make_StoneBlocksAny（第 18 行，ingredients+fixedIngredientFilter+specialProducts 三件套）、Make_ComponentIndustrial（第 356 行，`products` 的正确写法 `<ComponentIndustrial>1</ComponentIndustrial>`）。
  - `Core/Defs/RecipeDefs/Recipes_Butchery.xml`：ButcherCorpseFlesh（第 4 行，specialProducts + fixedIngredientFilter + forceHiddenSpecialFilters + workerCounterClass）。
- **字段表出处说明**：`RecipeDef.md` 的"原版出处"记为 `Core/Defs/HediffDefs/BodyParts/Hediffs_BodyParts_Base.xml` 与 `..._Prosthetic.xml`（手术类配方与 HediffDef 写在一起），因此 `addsHediff` 一类手术字段占比很高；制造类字段请对照 `Core/Defs/RecipeDefs/*.xml`。
- **Def 级属性说明**：`ParentName` / `Abstract` / `Name` 不在字段表内，属 Def 框架属性（本模板未使用继承，全部字段显式写出，便于逐条核对）。
- **待验证项**：常见坑第 4、5、6 条的行为后果为**推测**（静态比对 Def 得出，未启动游戏实测）；所写字段路径本身均来自字段表，可保证存在。
