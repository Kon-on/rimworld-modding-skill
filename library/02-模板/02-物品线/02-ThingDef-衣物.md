# ThingDef

## 用途

衣物是 ThingDef 的一支：`thingClass` 为 `Apparel`（原版由 ApparelNoQualityBase / ApparelBase 提供），装备部位与穿层由 `apparel` 节点决定——`apparel/layers` 决定它和别的衣物谁穿在外面（取值来自 ApparelLayerDef 的 6 个：OnSkin / Middle / Shell / Belt / Overhead / EyeCover），`apparel/bodyPartGroups` 决定保护与保温的身体部位，`apparel/wornGraphicPath` 决定穿上后的贴图。保暖与护甲数值写在 `statBases`（Insulation_Cold/Heat、ArmorRating_Sharp/Blunt/Heat、StuffEffectMultiplier*），穿着时给穿戴者的属性加成写在顶层 `equippedStatOffsets`。制造走 `recipeMaker`（裁剪台），材料用 `costStuffCount` + `stuffCategories`（可换布料/皮革）或 `costList`。它和 StuffCategoryDef、材料 ThingDef 的 `stuffProps`、SpecialThingFilterDef（死人衣物/童装过滤）联动。

**先纠正一个常见误写**：字段表里不存在 `apBodyPartGroups` 或顶层 `bodyPartGroups`，真实路径是 `apparel/bodyPartGroups`（4.6%，95/2054）与 `apparel/bodyPartGroups/li`（8.7%，178/2054）。

## 模板

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Defs>

  <!-- ============ 1) 可换材料的衣物 ============ -->
  <!-- ParentName="ApparelMakeableBase"（Core/Defs/ThingDefs_Misc/Apparel_Various.xml:45）提供：
       thingClass=Apparel、category=Item、drawerType=MapMeshOnly、useHitPoints、selectable、pathCost=14、
       altitudeLayer=Item、tickerType=Never、burnableByRecipe、smeltable、rotatable=false、
       comps(Forbiddable / CompColorable / CompQuality / Styleable)、
       recipeMaker(workSkill Crafting、Tailor 两座台、UnfinishedApparel、defaultIngredientFilter)、tradeTags(Clothing)。 -->
  <ThingDef ParentName="ApparelMakeableBase">
    <defName>EXAMPLE_Apparel_DustCoat</defName>
    <label>dust coat</label>
    <description>一件示例外套，用于演示衣物字段布局。</description>
    <possessionCount>1</possessionCount>
    <recipeMaker>
      <researchPrerequisite>ComplexClothing</researchPrerequisite>
      <displayPriority>216</displayPriority>
    </recipeMaker>
    <graphicData>
      <texPath>Things/Pawn/Humanlike/Apparel/Duster/Duster</texPath>
      <graphicClass>Graphic_Single</graphicClass>
      <drawSize>1.05</drawSize>
    </graphicData>
    <!-- 可选材料路线：数量 + 允许的材料类别（StuffCategoryDef 的 6 个取值） -->
    <costStuffCount>80</costStuffCount>
    <stuffCategories>
      <li>Fabric</li>
      <li>Leathery</li>
    </stuffCategories>
    <thingCategories>
      <li>ApparelMisc</li>
    </thingCategories>
    <!-- 保暖/护甲的"每材料一份"系数：实际值 = 材料 statBases 里的 StuffPower_* × 这里的系数 -->
    <statBases>
      <MaxHitPoints>200</MaxHitPoints>
      <WorkToMake>10000</WorkToMake>
      <Mass>2</Mass>
      <StuffEffectMultiplierArmor>0.3</StuffEffectMultiplierArmor>
      <StuffEffectMultiplierInsulation_Cold>0.60</StuffEffectMultiplierInsulation_Cold>
      <StuffEffectMultiplierInsulation_Heat>0.85</StuffEffectMultiplierInsulation_Heat>
      <EquipDelay>3</EquipDelay>
    </statBases>
    <!-- 穿着期间给穿戴者加属性偏移：元素名就是 StatDef 的 defName -->
    <equippedStatOffsets>
      <SlaveSuppressionOffset>-0.05</SlaveSuppressionOffset>
    </equippedStatOffsets>
    <apparel>
      <!-- 覆盖的身体部位组（BodyPartGroupDef） -->
      <bodyPartGroups>
        <li>Torso</li>
        <li>Neck</li>
        <li>Shoulders</li>
        <li>Arms</li>
        <li>Legs</li>
      </bodyPartGroups>
      <!-- 穿在身上的贴图目录（同目录下按朝向/性别/体型找变体文件） -->
      <wornGraphicPath>Things/Pawn/Humanlike/Apparel/Duster/Duster</wornGraphicPath>
      <!-- 穿层：ApparelLayerDef 的 6 个取值之一，决定与其它衣物的先后顺序 -->
      <layers>
        <li>Shell</li>
      </layers>
      <tags>
        <li>IndustrialAdvanced</li>
      </tags>
      <defaultOutfitTags>
        <li>Worker</li>
      </defaultOutfitTags>
      <canBeDesiredForIdeo>false</canBeDesiredForIdeo>
    </apparel>
    <tradeTags>
      <li>BasicClothing</li>
    </tradeTags>
  </ThingDef>

  <!-- ============ 2) 固定材料的护甲 ============ -->
  <!-- ParentName="ArmorMachineableBase"（Apparel_Various.xml:104）：绕开 costStuffCount，用 costList 定死材料，
       制造台是 TableMachining（机械加工台），半成品 UnfinishedArmor。 -->
  <ThingDef ParentName="ArmorMachineableBase">
    <defName>EXAMPLE_Apparel_PlateVest</defName>
    <label>plate vest</label>
    <description>一件示例护甲背心，只用固定材料制造。</description>
    <techLevel>Industrial</techLevel>
    <recipeMaker>
      <researchPrerequisite>FlakArmor</researchPrerequisite>
      <unfinishedThingDef>UnfinishedTechArmor</unfinishedThingDef>
      <skillRequirements>
        <Crafting>4</Crafting>
      </skillRequirements>
      <displayPriority>220</displayPriority>
    </recipeMaker>
    <graphicData>
      <texPath>Things/Pawn/Humanlike/Apparel/FlakVest/FlakVest</texPath>
      <graphicClass>Graphic_Single</graphicClass>
      <drawSize>0.90</drawSize>
    </graphicData>
    <!-- 不可换材料的护甲直接把护甲/保温写死（不写 StuffEffectMultiplier*） -->
    <statBases>
      <WorkToMake>9000</WorkToMake>
      <MaxHitPoints>200</MaxHitPoints>
      <Mass>4</Mass>
      <Flammability>0.6</Flammability>
      <ArmorRating_Sharp>1.00</ArmorRating_Sharp>
      <ArmorRating_Blunt>0.36</ArmorRating_Blunt>
      <ArmorRating_Heat>0.27</ArmorRating_Heat>
      <Insulation_Cold>1</Insulation_Cold>
      <EquipDelay>5</EquipDelay>
    </statBases>
    <equippedStatOffsets>
      <MoveSpeed>-0.12</MoveSpeed>
    </equippedStatOffsets>
    <thingCategories>
      <li>ApparelArmor</li>
    </thingCategories>
    <costList>
      <Cloth>30</Cloth>
      <Steel>60</Steel>
      <ComponentIndustrial>1</ComponentIndustrial>
    </costList>
    <apparel>
      <bodyPartGroups>
        <li>Torso</li>
        <li>Neck</li>
      </bodyPartGroups>
      <wornGraphicPath>Things/Pawn/Humanlike/Apparel/FlakVest/FlakVest</wornGraphicPath>
      <!-- Middle 层 = 穿在外衣里面、内衣外面 -->
      <layers>
        <li>Middle</li>
      </layers>
      <tags>
        <li>IndustrialMilitaryBasic</li>
      </tags>
      <defaultOutfitTags>
        <li>Soldier</li>
      </defaultOutfitTags>
    </apparel>
    <tradeTags>
      <li>Armor</li>
    </tradeTags>
  </ThingDef>

  <!-- ============ 3) 材料 Def：衣物 stuffCategories 能选到的东西 ============ -->
  <!-- ParentName="ResourceBase"（Core/Defs/ThingDefs_Items/Items_Resource_Base.xml:4）提供
       thingClass=ThingWithComps、category=Item、stackLimit=75、altitudeLayer=Item 等。 -->
  <ThingDef ParentName="ResourceBase">
    <defName>EXAMPLE_Stuff_Dustcloth</defName>
    <label>dustcloth</label>
    <description>一种示例材料；衣物把它的 StuffPower_* 乘上自己的 StuffEffectMultiplier*。</description>
    <graphicData>
      <texPath>Things/Item/Resource/Leather</texPath>
      <graphicClass>Graphic_StackCount</graphicClass>
      <color>(162,106,57)</color>
    </graphicData>
    <statBases>
      <MaxHitPoints>60</MaxHitPoints>
      <DeteriorationRate>2</DeteriorationRate>
      <Mass>0.03</Mass>
      <Flammability>1</Flammability>
      <MarketValue>2.1</MarketValue>
      <StuffPower_Armor_Sharp>0.81</StuffPower_Armor_Sharp>
      <StuffPower_Armor_Blunt>0.24</StuffPower_Armor_Blunt>
      <StuffPower_Armor_Heat>1.5</StuffPower_Armor_Heat>
      <StuffPower_Insulation_Cold>16</StuffPower_Insulation_Cold>
      <StuffPower_Insulation_Heat>16</StuffPower_Insulation_Heat>
    </statBases>
    <thingCategories>
      <li>Leathers</li>
    </thingCategories>
    <burnableByRecipe>true</burnableByRecipe>
    <stuffProps>
      <categories>
        <li>Leathery</li>
      </categories>
      <color>(162,106,57)</color>
      <commonality>1</commonality>
      <statFactors>
        <MaxHitPoints>1.3</MaxHitPoints>
      </statFactors>
      <canSuggestUseDefaultStuff>true</canSuggestUseDefaultStuff>
    </stuffProps>
  </ThingDef>

</Defs>
```

## 字段说明

出现率来自 `03-全量字段参考/字段/ThingDef.md`（分母 2054）。

| 字段 | 出现率 | 值类型 | 说明 |
|---|---|---|---|
| `apparel` | 6.2% (128/2054) | 容器 | 衣物的核心节点，缺了它 `thingClass=Apparel` 也不知道穿哪儿。 |
| `apparel/layers` | 4.3% (89/2054) | 容器 | 穿层容器。 |
| `apparel/layers/li` | 4.7% (96/2054) | 文本 | 取值来自 ApparelLayerDef：OnSkin/Middle/Shell/Belt/Overhead/EyeCover。 |
| `apparel/bodyPartGroups` | 4.6% (95/2054) | 容器 | 覆盖部位容器。**不叫 apBodyPartGroups。** |
| `apparel/bodyPartGroups/li` | 8.7% (178/2054) | 文本 | BodyPartGroupDef 名（Torso/Neck/Shoulders/Arms/Legs/FullHead…）。 |
| `apparel/wornGraphicPath` | 5.1% (104/2054) | 文本 | 穿在身上的贴图路径（不是 graphicData.texPath）。 |
| `apparel/wornGraphicPaths` | 0.1% (2/2054) | 容器 | 多套穿着贴图的容器写法（`li` 0.3%，6/2054）。 |
| `apparel/tags` | 2.9% (59/2054) | 容器 | 衣物标签容器。 |
| `apparel/tags/li` | 3.9% (81/2054) | 文本 | IndustrialBasic / IndustrialAdvanced / IndustrialMilitaryBasic 等。 |
| `apparel/defaultOutfitTags` | 2.6% (53/2054) | 容器 | 默认服装方案标签。 |
| `apparel/defaultOutfitTags/li` | 3.9% (79/2054) | 文本 | Nudist / Soldier / Spacefarer / Worker。 |
| `apparel/countsAsClothingForNudity` | 2.4% (49/2054) | 布尔 | 是否算"穿了衣服"（防裸体心情处罚）。 |
| `apparel/careIfWornByCorpse` | 1.0% (20/2054) | 布尔 | 是否在意"死人身上扒下来的"。 |
| `apparel/careIfDamaged` | 1.0% (20/2054) | 布尔 | 是否在意磨损。 |
| `apparel/useWornGraphicMask` | 0.3% (6/2054) | 布尔 | 用遮罩图换色。 |
| `apparel/developmentalStageFilter` | 1.2% (24/2054) | 文本 | Child / "Child, Adult"，限定儿童或成人。 |
| `apparel/parentTagDef` | 0.5% (11/2054) | 文本 | 归类标签（ApparelBody / ApparelHead）。 |
| `apparel/canBeDesiredForIdeo` | 1.2% (25/2054) | 布尔 | 是否可能被意识形态信徒"想要"。 |
| `apparel/canBeGeneratedToSatisfyWarmth` | 1.2% (25/2054) | 布尔 | 是否会被随机生成用来满足保暖需求。 |
| `apparel/wearPerDay` | 1.0% (20/2054) | 数值 | 每天磨损量。 |
| `apparel/scoreOffset` | 1.1% (23/2054) | 数值 | 穿着评分偏移，影响 NPC 选择。 |
| `apparel/soundWear` / `apparel/soundRemove` | 0.2% (5/2054) | 文本 | 穿/脱音效（Wear_PowerArmor / Remove_PowerArmor）。 |
| `apparel/wornGraphicData` | 1.0% (20/2054) | 容器 | 穿着贴图的高级配置（朝向偏移/缩放、fat/thin/male/female 变体）。 |
| `apparel/wornGraphicData/renderUtilityAsPack` | 1.0% (20/2054) | 布尔 | 把装备渲染成背包。 |
| `stuffCategories` | 8.2% (168/2054) | 容器 | 允许的材料类别容器。 |
| `stuffCategories/li` | 15.2% (313/2054) | 文本 | Fabric / Leathery / Metallic / Woody / Stony / Bioferrite。 |
| `costStuffCount` | 8.4% (172/2054) | 数值 | 可选材料路线的材料数量（原版 20 / 25 / 70，外套 80）。 |
| `costList` | 17.0% (350/2054) | 容器 | 固定材料清单（与 costStuffCount 二选一）。 |
| `costList/Cloth` | 0.5% (10/2054) | 数值 | 布料用量，原版背心 30。 |
| `costList/Steel` | 10.0% (206/2054) | 数值 | 钢铁用量。 |
| `statBases/StuffEffectMultiplierArmor` | 2.3% (47/2054) | 数值 | 材料护甲系数（0.2 / 0.3 / 0.4）。 |
| `statBases/StuffEffectMultiplierInsulation_Cold` | 2.3% (48/2054) | 数值 | 材料保暖系数。 |
| `statBases/StuffEffectMultiplierInsulation_Heat` | 2.3% (48/2054) | 数值 | 材料隔热系数。 |
| `statBases/Insulation_Cold` | 1.1% (22/2054) | 数值 | 不可换材料衣物的固定保暖值。 |
| `statBases/Insulation_Heat` | 1.0% (21/2054) | 数值 | 固定隔热值。 |
| `statBases/ArmorRating_Sharp` | 2.6% (53/2054) | 数值 | 锐器护甲。 |
| `statBases/ArmorRating_Blunt` | 2.6% (53/2054) | 数值 | 钝器护甲。 |
| `statBases/ArmorRating_Heat` | 1.6% (32/2054) | 数值 | 热能护甲。 |
| `statBases/EquipDelay` | 4.5% (93/2054) | 数值 | 穿脱耗时（秒）。 |
| `statBases/MaxHitPoints` | 32.4% (665/2054) | 数值 | 耐久。 |
| `statBases/Flammability` | 22.2% (456/2054) | 数值 | 可燃性。 |
| `equippedStatOffsets` | 3.2% (66/2054) | 容器 | 穿着时的属性偏移，子元素名 = StatDef 名。 |
| `equippedStatOffsets/SlaveSuppressionOffset` | 1.3% (26/2054) | 数值 | 原版样例 -0.05 / -0.1 / -0.3。 |
| `equippedStatOffsets/MoveSpeed` | 0.5% (11/2054) | 数值 | 原版样例 -0.12 / -0.25 / -0.4。 |
| `equippedStatOffsets/PsychicEntropyRecoveryRate` | 0.6% (12/2054) | 数值 | 心灵熵恢复速率偏移。 |
| `equippedStatOffsets/VacuumResistance` | 0.6% (13/2054) | 数值 | 真空抗性（Odyssey）。 |
| `comps/li/compClass` | 13.8% (284/2054) | 文本 | 组件类名（CompColorable / CompQuality），原版也常用 `<li Class="CompProperties_X">` 属性写法。 |
| `colorGenerator` | 3.0% (62/2054) | 容器 | 随机配色器（原版用 `Class="ColorGenerator_Options"`）。 |
| `colorGenerator/options/li/weight` | 4.9% (100/2054) | 数值 | 配色权重（10 / 15 / 20）。 |
| `colorGenerator/options/li/only` | 4.4% (91/2054) | 文本 | 固定颜色，如 (0.33,0.33,0.33)。 |
| `colorGenerator/options/li/min` / `colorGenerator/options/li/max` | 1.3% (26/2054) / 1.3% (26/2054) | 文本 | 颜色区间。 |
| `stuffProps` | 2.8% (58/2054) | 容器 | **写在材料 Def 上**，让该材料可以被衣物/建筑选用。 |
| `stuffProps/categories` / `/li` | 0.8% (16/2054) / 0.9% (18/2054) | 容器 / 文本 | 该材料归属的 StuffCategory。 |
| `stuffProps/color` | 2.6% (54/2054) | 文本 | 材料色 (112,89,43)。 |
| `stuffProps/commonality` | 2.1% (44/2054) | 数值 | 材料在随机生成中的常见度。 |
| `stuffProps/stuffAdjective` | 0.4% (8/2054) | 文本 | 品质形容词（"木制的"）。 |
| `stuffProps/appearance` | 0.4% (9/2054) | 文本 | 外观风格（Metal / Planks / Bricks）。 |
| `stuffProps/constructEffect` | 0.5% (10/2054) | 文本 | 建造特效（ConstructMetal / ConstructWood）。 |
| `stuffProps/isAirtight` | 0.3% (6/2054) | 布尔 | 该材料做出来是否气密。 |
| `stuffProps/canSuggestUseDefaultStuff` | 0.6% (12/2054) | 布尔 | 是否允许系统推荐默认材料。 |
| `stuffProps/statFactors` | 2.2% (46/2054) | 容器 | 材料对成品属性的乘算（/Beauty、/MaxHitPoints、/Flammability、/WorkToBuild、/WorkToMake）。 |
| `stuffProps/statOffsets` | 0.4% (8/2054) | 容器 | 材料对成品属性的加算（/Beauty 0.3%、/WorkToBuild 0.1%）。 |
| `stuffProps/statFactorsQuality` | 0.1% (1/2054) | 容器 | 按品质分子的乘算（`li/{stat, awful…legendary}`）。 |
| `statBases/StuffPower_Armor_Sharp` | 1.8% (38/2054) | 数值 | 材料自身护甲输出，被衣物 StuffEffectMultiplierArmor 乘。 |
| `statBases/StuffPower_Insulation_Cold` | 2.2% (46/2054) | 数值 | 材料保暖输出（皮革 16）。 |
| `statBases/StuffPower_Insulation_Heat` | 2.1% (44/2054) | 数值 | 材料隔热输出。 |
| `statBases/LeatherAmount` | 1.0% (21/2054) | 数值 | 动物皮量（材料 Def 上）。 |
| `recipeMaker` / `recipeMaker/recipeUsers` | 11.9% (245/2054) / 4.6% (94/2054) | 容器 | 制造入口；衣物原版走 ElectricTailoringBench + HandTailoringBench。 |
| `recipeMaker/defaultIngredientFilter` | 0.5% (10/2054) | 容器 | 默认材料过滤，原版排除 Gold/Silver/Plasteel 等。 |
| `tradeTags/li` | 14.1% (290/2054) | 文本 | Clothing / BasicClothing / Armor。 |

## 常见坑

1. **`bodyPartGroups` 只能在 `apparel` 节点里**：字段表不存在 `apBodyPartGroups`，也不存在顶层 `bodyPartGroups`；真实路径是 `apparel/bodyPartGroups`（4.6%，95/2054）与 `apparel/bodyPartGroups/li`（8.7%，178/2054）。写错外层不会被识别。
2. **`wornGraphicPath` 与 `graphicData/texPath` 是两个东西**：前者是"穿在身上"的贴图目录（5.1%，104/2054），后者是掉在地上的物品贴图（68.2%）。只写 texPath 会导致穿上后没图（**推测**，未实测）。
3. **`stuffCategories` 与 `costList` 不要同时用**：原版服装分两条线——可换材料的（Apparel_Duster：costStuffCount 80 + Fabric/Leathery）与固定材料的（Apparel_FlakVest：costList）。同时写会让材料需求叠加（**推测**）。
4. **`StuffEffectMultiplier*` 只在可换材料的衣服上有意义**：真实数值来自材料 Def 的 `statBases/StuffPower_*`（皮革 StuffPower_Armor_Sharp 0.81、StuffPower_Insulation_Cold 16），乘这个系数得到成品值；不可换材料的衣服直接写 `ArmorRating_*` / `Insulation_*`（**推测**：机制描述依据原版两套 Def 的分工，未实测具体算式）。
5. **`apparel/layers` 只能填 ApparelLayerDef 的 6 个 defName**（OnSkin / Middle / Shell / Belt / Overhead / EyeCover）。同一层两件衣服会争位；层写错会导致衣物永远穿不上或被别的衣服挤掉（**推测**）。
6. **材料 Def 上忘写 `stuffProps` 就不会出现在材料选择列表里**：`stuffProps/categories` 决定它归属哪个 StuffCategory，而衣服用 `stuffCategories` 反选（依据 Core 的皮革 Def 与 Apparel_Duster 两处写法）。`stuffProps` 在 ThingDef 里只有 2.8%（58/2054），说明它只属于"材料"这一类 Def。
7. **`tags` 与 NPC 的配装逻辑挂钩**：原版用 `apparel/tags/li`（3.9%，81/2054）给衣物打 IndustrialMilitaryBasic 之类的标签，再由 PawnKindDef 侧的配装标签去选；自己发明标签而两侧不匹配，NPC 就不会穿（**推测**：字段表只收录衣物侧的 `apparel/tags/li`，PawnKindDef 侧字段未在本文件核对范围）。

## 核验

- **逐字段对照**：上表出现率取自 `03-全量字段参考/字段/ThingDef.md`（分母 2054），可用 `字段总表.csv` 复核，例如
  `Select-String -Path '03-全量字段参考\字段总表.csv' -Pattern ',ThingDef,apparel/bodyPartGroups,'`。
- **结构照抄原版**（路径相对 `E:\SteamLibrary\steamapps\common\RimWorld\Data\`）：
  - `Core/Defs/ThingDefs_Misc/Apparel_Various.xml`：ApparelNoQualityBase（第 4 行）、ApparelBase（第 36 行）、ApparelMakeableBase（第 45 行）、ArmorSmithableBase（第 76 行）、ArmorMachineableBase（第 104 行）、Apparel_Duster（第 454 行）、Apparel_FlakVest（第 705 行）——本模板两件衣物的字段与取值逐条对照这两件原版衣物。
  - `Core/Defs/ThingDefs_Misc/Apparel_Headgear.xml`：CowboyHat（第 40 行）、Apparel_SimpleHelmet（第 414 行）、Apparel_AdvancedHelmet（第 467 行）——头盔类的参照物。
  - `Core/Defs/ThingDefs_Items/Items_Resource_Base.xml`（ResourceBase，第 4 行）与 `Core/Defs/ThingDefs_Items/Items_Resource_Stuff_Leather.xml`（LeatherBase 第 4 行、Leather_Plain 第 44 行）——第 3 个 def（材料）的字段来源。
- **取值枚举来源**：`Core/Defs/Misc/ApparelLayerDefs/ApparelLayerDefs.xml`（6 个层）、`Core/Defs/Misc/StuffCategoryDefs/StuffCategories.xml`（6 个材料类别）、`Core/Defs/ThingCategoryDefs/ThingCategories.xml`（ApparelMisc / ApparelArmor / Leathers）——对应 `03-全量字段参考/字段/ApparelLayerDef.md`、`StuffCategoryDef.md`、`ThingCategoryDef.md`。
- **Def 级属性说明**：`ParentName` / `Abstract` / `Name` 不在字段表内，属 Def 框架属性，照抄原版 Apparel_Various.xml 的用法。
- **待验证项**：常见坑中标注"推测"的条目指机制层面的因果（游戏内实际表现）；字段路径本身 100% 来自字段表——即路径一定存在，但"不这么写会怎样"未在本机启动游戏实测。
