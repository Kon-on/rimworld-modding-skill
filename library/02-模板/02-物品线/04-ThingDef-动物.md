# ThingDef

## 用途

动物也是 ThingDef，全部生物学参数都挂在 `race` 节点下：`race/body` 指向 BodyDef 决定身体结构，`race/baseBodySize` / `baseHealthScale` / `baseHungerRate` 决定体型、血量与食量，`race/lifeStageAges` 定义幼年到成年的成长阶段并给每个阶段配叫声/受伤/死亡音效。攻击方式用 `tools`（`capacities` + `linkedBodyPartsGroup` 绑定部位），可驯化程度与产物由 `race/trainability`、`race/leatherDef` 与 `statBases/LeatherAmount` / `Wildness` 决定。要让动物真的出现在地图上，还必须写一个同名的 PawnKindDef（用 `race` 指回本 ThingDef、用 `lifeStages` 提供各阶段贴图）。它与 PawnKindDef、BodyDef、LifeStageDef、TrainableDef、ThingCategoryDef（Animals）、FilthDef 联动。

**先纠正两个常见误写**：不存在顶层 `bodyDef`（真实路径是 `race/body`，5.7%，116/2054）；也不存在顶层 `lifeStageAges`（真实路径是 `race/lifeStageAges`，7.1%，146/2054）。

## 模板

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Defs>

  <!-- ================= 1) 动物 ThingDef ================= -->
  <!-- ParentName="AnimalThingBase"（Core/Defs/ThingDefs_Races/Races_Animal_Base.xml）提供：
       category=Pawn、thingClass=Pawn、thinkTreeMain=Animal、renderTree=Animal、hasGenders、
       thingCategories(Animals)、recipes(宰杀/安乐死等)、compAttachBase 等。 -->
  <ThingDef ParentName="AnimalThingBase">
    <defName>EXAMPLE_Animal_Stonebacks</defName>
    <label>石甲兽</label>
    <description>一只示例动物：食草、可驯化、产普通皮革。</description>
    <devNote>示例：仿 Hare 的最小动物定义</devNote>
    <statBases>
      <MoveSpeed>5.0</MoveSpeed>
      <MarketValue>180</MarketValue>
      <ComfyTemperatureMin>-15</ComfyTemperatureMin>
      <ComfyTemperatureMax>40</ComfyTemperatureMax>
      <Wildness>0.55</Wildness>
      <LeatherAmount>60</LeatherAmount>
      <ToxicResistance>0.5</ToxicResistance>
    </statBases>
    <!-- 攻击工具：capacities 用 ToolCapacityDef 的取值，linkedBodyPartsGroup 绑 BodyPartGroupDef -->
    <tools>
      <li>
        <capacities>
          <li>Bite</li>
        </capacities>
        <power>12</power>
        <cooldownTime>2</cooldownTime>
        <linkedBodyPartsGroup>Teeth</linkedBodyPartsGroup>
      </li>
      <li>
        <label>head</label>
        <capacities>
          <li>Blunt</li>
        </capacities>
        <power>7</power>
        <cooldownTime>2</cooldownTime>
        <linkedBodyPartsGroup>HeadAttackTool</linkedBodyPartsGroup>
        <ensureLinkedBodyPartsGroupAlwaysUsable>true</ensureLinkedBodyPartsGroupAlwaysUsable>
        <chanceFactor>0.2</chanceFactor>
      </li>
    </tools>
    <race>
      <body>QuadrupedAnimalWithPawsAndTail</body>
      <!-- 体型/血量/食量：三者共同决定成体大小 -->
      <baseBodySize>0.8</baseBodySize>
      <baseHealthScale>0.9</baseHealthScale>
      <baseHungerRate>0.28</baseHungerRate>
      <foodType>VegetarianRoughAnimal</foodType>
      <leatherDef>Leather_Plain</leatherDef>
      <trainability>Intermediate</trainability>
      <petness>0.3</petness>
      <lifeExpectancy>12</lifeExpectancy>
      <gestationPeriodDays>10</gestationPeriodDays>
      <mateMtbHours>8</mateMtbHours>
      <nuzzleMtbHours>24</nuzzleMtbHours>
      <roamMtbDays>3</roamMtbDays>
      <herdAnimal>true</herdAnimal>
      <!-- 幼年/青年/成体三阶段；音效挂在"成年"那一档上 -->
      <lifeStageAges>
        <li>
          <def>AnimalBaby</def>
          <minAge>0</minAge>
        </li>
        <li>
          <def>AnimalJuvenile</def>
          <minAge>0.1</minAge>
        </li>
        <li>
          <def>AnimalAdult</def>
          <minAge>0.3</minAge>
          <soundWounded>Pawn_Melee_SmallScratch_HitPawn</soundWounded>
          <soundDeath>Pawn_Hare_Death</soundDeath>
          <!-- 叫声与愤怒声同样只写在"成年"这一档上，race 直属节点没有 soundCall/soundAngry -->
          <soundCall>Pawn_Hare_Call</soundCall>
          <soundAngry>Pawn_Hare_Angry</soundAngry>
        </li>
      </lifeStageAges>
      <!-- 每胎数量曲线：points/li 的写法是 "(x, y)" -->
      <litterSizeCurve>
        <points>
          <li>(1.0, 0)</li>
          <li>(1.5, 1)</li>
          <li>(2.0, 1)</li>
          <li>(2.5, 0)</li>
        </points>
      </litterSizeCurve>
      <soundEating>Rodent_Eat</soundEating>
      <soundMeleeHitPawn>Pawn_Melee_SmallScratch_HitPawn</soundMeleeHitPawn>
      <soundMeleeHitBuilding>Pawn_Melee_SmallScratch_HitBuilding</soundMeleeHitBuilding>
      <soundMeleeMiss>Pawn_Melee_SmallScratch_Miss</soundMeleeMiss>
    </race>
    <thingCategories>
      <li>Animals</li>
    </thingCategories>
    <tradeTags>
      <li>AnimalCommon</li>
    </tradeTags>
  </ThingDef>

  <!-- ================= 2) 配套 PawnKindDef（没有它动物不会自然刷新） ================= -->
  <!-- ParentName="AnimalKindBase"（Races_Animal_Base.xml）提供野生动物的通用设置。 -->
  <PawnKindDef ParentName="AnimalKindBase">
    <defName>EXAMPLE_Animal_Stonebacks</defName>
    <label>石甲兽</label>
    <!-- race 必须填上面那个 ThingDef 的 defName -->
    <race>EXAMPLE_Animal_Stonebacks</race>
    <combatPower>90</combatPower>
    <ecoSystemWeight>0.4</ecoSystemWeight>
    <!-- lifeStages 按"幼年 → 青年 → 成体"顺序，每档给贴图 -->
    <lifeStages>
      <li>
        <bodyGraphicData>
          <texPath>Things/Pawn/Animal/Hare/Hare</texPath>
          <drawSize>0.7</drawSize>
          <color>(130,127,106)</color>
        </bodyGraphicData>
        <dessicatedBodyGraphicData>
          <texPath>Things/Pawn/Animal/Hare/Dessicated_Hare</texPath>
          <drawSize>0.7</drawSize>
        </dessicatedBodyGraphicData>
      </li>
      <li>
        <bodyGraphicData>
          <texPath>Things/Pawn/Animal/Hare/Hare</texPath>
          <drawSize>1.0</drawSize>
          <color>(130,127,106)</color>
        </bodyGraphicData>
        <dessicatedBodyGraphicData>
          <texPath>Things/Pawn/Animal/Hare/Dessicated_Hare</texPath>
          <drawSize>1.0</drawSize>
        </dessicatedBodyGraphicData>
      </li>
      <li>
        <bodyGraphicData>
          <texPath>Things/Pawn/Animal/Hare/Hare</texPath>
          <drawSize>1.3</drawSize>
          <color>(130,127,106)</color>
        </bodyGraphicData>
        <dessicatedBodyGraphicData>
          <texPath>Things/Pawn/Animal/Hare/Dessicated_Hare</texPath>
          <drawSize>1.3</drawSize>
        </dessicatedBodyGraphicData>
      </li>
    </lifeStages>
  </PawnKindDef>

</Defs>
```

## 字段说明

出现率来自 `03-全量字段参考/字段/ThingDef.md`（分母 2054）；PawnKindDef 部分来自 `字段/PawnKindDef.md`（分母 333）。

| 字段 | 出现率 | 值类型 | 说明 |
|---|---|---|---|
| `race` | 8.6% (176/2054) | 容器 | 生物参数总节点，动物必写。 |
| `race/body` | 5.7% (116/2054) | 文本 | BodyDef 名（Human / QuadrupedAnimalWithPawsAndTail …）。**不叫 bodyDef。** |
| `race/baseBodySize` | 6.1% (125/2054) | 数值 | 基础体型（0.8 / 1 / 2），决定体积与承重。 |
| `race/baseHealthScale` | 6.3% (129/2054) | 数值 | 血量系数（0.6 / 0.75 / 1.5）。 |
| `race/baseHungerRate` | 4.5% (92/2054) | 数值 | 食量（0.2 / 0.28 / 0.35）。 |
| `race/foodType` | 4.9% (101/2054) | 文本 | OmnivoreAnimal / OvivoreAnimal / CarnivoreAnimal / None。 |
| `race/leatherDef` | 3.8% (77/2054) | 文本 | 屠宰产出皮革 Def（Leather_Bear）。 |
| `race/meatLabel` | 0.6% (12/2054) | 文本 | 肉的显示名（bear meat）。 |
| `race/useMeatFrom` | 1.3% (26/2054) | 文本 | 复用另一动物的肉（Hare）。 |
| `race/specificMeatDef` | 0.3% (6/2054) | 文本 | 指定特殊肉（Meat_Twisted）。 |
| `race/trainability` | 4.2% (87/2054) | 文本 | None / Intermediate / Advanced。 |
| `race/petness` | 1.5% (31/2054) | 数值 | 被当作宠物的倾向（0.3 / 0.50）。 |
| `race/lifeExpectancy` | 5.4% (110/2054) | 数值 | 寿命年数（8 / 100 / 250）。 |
| `race/lifeStageAges` | 7.1% (146/2054) | 容器 | 成长阶段容器。**顶层不存在同名路径。** |
| `race/lifeStageAges/li/def` | 17.3% (355/2054) | 文本 | LifeStageDef 名（AnimalBaby / AnimalJuvenile / AnimalAdult）。 |
| `race/lifeStageAges/li/minAge` | 16.1% (331/2054) | 数值 | 该阶段的起始年龄（年），原版 0 / 0.016667 / 0.05。 |
| `race/lifeStageAges/li/soundCall` | 7.8% (161/2054) | 文本 | 该阶段的叫声。 |
| `race/lifeStageAges/li/soundAngry` | 4.9% (101/2054) | 文本 | 愤怒声。 |
| `race/lifeStageAges/li/soundWounded` | 7.9% (163/2054) | 文本 | 受伤声。 |
| `race/lifeStageAges/li/soundDeath` | 7.4% (153/2054) | 文本 | 死亡声。 |
| `race/lifeStageAges/li/soundAttack` | 0.1% (3/2054) | 文本 | 攻击声（少见）。 |
| `race/litterSizeCurve` | 1.7% (35/2054) | 容器 | 每胎数量曲线。 |
| `race/litterSizeCurve/points/li` | 7.2% (149/2054) | 文本 | 形如 `(1.5, 1)` 的点。 |
| `race/gestationPeriodDays` | 3.4% (70/2054) | 数值 | 妊娠天数（5.61 / 10 / 12）。 |
| `race/mateMtbHours` | 0.7% (14/2054) | 数值 | 平均交配间隔小时（8）。 |
| `race/nuzzleMtbHours` | 0.5% (10/2054) | 数值 | 平均蹭人间隔小时（12 / 24 / 48）。 |
| `race/roamMtbDays` | 1.6% (32/2054) | 数值 | 平均漫游间隔天（2 / 3 / 5）。 |
| `race/herdAnimal` | 2.1% (44/2054) | 布尔 | 是否成群行动。 |
| `race/predator` | 0.5% (10/2054) | 布尔 | 是否捕食者。 |
| `race/packAnimal` | 0.4% (9/2054) | 布尔 | 能否作为驮兽。 |
| `race/manhunterOnDamageChance` | 2.0% (42/2054) | 数值 | 受伤后变疯的概率（0.1 / 0.5）。 |
| `race/manhunterOnTameFailChance` | 1.5% (31/2054) | 数值 | 驯服失败变疯概率（0.10 / 0.2 / 0.30）。 |
| `race/specialTrainables` | 1.4% (28/2054) | 容器 | 额外训练项（`li` 1.4%：AttackTarget / Comfort / Dig）。 |
| `race/hasGenders` | 0.6% (12/2054) | 布尔 | 是否有性别。 |
| `race/forceGender` | 0.1% (1/2054) | 文本 | 强制性别。 |
| `race/nameGenerator` / `race/nameGeneratorFemale` | 0.1% (3/2054) / 0.1% (1/2054) | 文本 | 命名器。 |
| `race/animalType` | 0.3% (7/2054) | 文本 | Canine / Dryad 等特殊分类。 |
| `race/soundEating` | 3.9% (81/2054) | 文本 | 进食音效。 |
| `race/soundMeleeHitPawn` | 4.4% (91/2054) | 文本 | 近战命中活体音效。 |
| `race/soundMeleeHitBuilding` | 4.4% (91/2054) | 文本 | 近战命中建筑音效。 |
| `race/soundMeleeMiss` | 4.4% (91/2054) | 文本 | 近战落空音效。 |
| `race/soundMeleeDodge` | 0.4% (9/2054) | 文本 | 闪避音效。 |
| `race/soundCallIntervalRange` | 0.3% (6/2054) | 文本 | 叫声间隔区间，形如 `1000~2000`。 |
| `race/thinkTreeMain` / `race/thinkTreeConstant` | 1.0% (20/2054) / 0.9% (19/2054) | 文本 | 思考树（Animal / AnimalConstant），改 AI 行为时用。 |
| `race/renderTree` | 0.6% (12/2054) | 文本 | 渲染树（Animal / Misc）。 |
| `race/bloodDef` / `race/bloodSmearDef` | 0.6% (12/2054) / 0.1% (3/2054) | 文本 | 出血/擦血污物 Def（Filth_Blood）。 |
| `race/hediffGiverSets/li` | 0.6% (12/2054) | 文本 | 疾病集合（OrganicStandard）。 |
| `race/headPosPerRotation/li` | 19.3% (396/2054) | 文本 | 各朝向的头部偏移，形如 `(0.19, 0, 0)`。 |
| `race/canCrossBreedWith` / `race/crossAggroWith` | 0.1% (2/2054) | 容器 | 杂交/敌对关系（`li` 为 ThingDef 名）。 |
| `race/detritusLeavings` | 0.6% (13/2054) | 容器 | 定期掉落的杂物（`li` 1.8%，36/2054）。 |
| `race/waterCellCost` / `race/waterSeeker` | 0.7% (15/2054) / 0.6% (13/2054) | 数值 / 布尔 | 涉水代价与是否找水（Odyssey）。 |
| `race/canFishForFood` | 0.4% (8/2054) | 布尔 | 是否会捕鱼。 |
| `race/disableIgniteVerb` / `race/alwaysAwake` / `race/needsRest` | 0.4% (9) / 0.1% (2) / 0.6% (12) | 布尔 | 行为开关。 |
| `race/maxPreyBodySize` | 0.5% (11/2054) | 数值 | 可捕食的最大体型。 |
| `race/hasCorpse` / `race/isImmuneToInfections` / `race/canReleaseToWild` | 0.3% (7) / 0.3% (6) / 0.1% (1) | 布尔 | 尸体与免疫相关开关。 |
| `race/canBecomeShambler` | 0.4% (8/2054) | 布尔 | 能否变成蹒跚者（Anomaly）。 |
| `race/deathAction` + `/workerClass` | 0.3% (7/2054) / 0.2% (4/2054) | 容器 / 文本 | 死亡时触发的 worker。 |
| `statBases/MoveSpeed` | 6.7% (137/2054) | 数值 | 移动速度（格/秒）。 |
| `statBases/Wildness` | 4.8% (98/2054) | 数值 | 野性（0 / 0.8 / 0.85），越高越难驯。 |
| `statBases/LeatherAmount` | 1.0% (21/2054) | 数值 | 屠宰产皮量。 |
| `statBases/ToxicResistance` | 1.0% (21/2054) | 数值 | 毒抗（动物基类给 0.5）。 |
| `statBases/MarketValue` | 17.5% (359/2054) | 数值 | 市价。 |
| `statBases/ComfyTemperatureMin` / `statBases/ComfyTemperatureMax` | 5.5% (113) / 2.4% (49) | 数值 | 舒适温度区间边界。 |
| `tools/li/power` / `tools/li/cooldownTime` | 24.2% (498/2054) | 数值 | 该攻击工具的伤害与冷却。 |
| `tools/li/capacities/li` | 28.3% (581/2054) | 文本 | ToolCapacityDef 取值（Bite / Blunt / Scratch / Cut …）。 |
| `tools/li/linkedBodyPartsGroup` | 19.0% (390/2054) | 文本 | 绑定的 BodyPartGroupDef（Teeth / HeadAttackTool）。 |
| `tools/li/chanceFactor` | 8.7% (178/2054) | 数值 | 该工具被选中的权重。 |
| `tools/li/ensureLinkedBodyPartsGroupAlwaysUsable` | 5.9% (122/2054) | 布尔 | 保证绑定的部位组始终可用。 |
| `thingCategories/li` | 12.4% (255/2054) | 文本 | 分类（Animals 由 AnimalThingBase 提供）。 |
| `tradeTags/li` | 14.1% (290/2054) | 文本 | 贸易标签（AnimalCommon）。 |
| `devNote` | 2.6% (53/2054) | 文本 | 开发者备注（squirrel-1），不影响逻辑。 |
| **PawnKindDef** `race` | 55.9% (186/333) | 文本 | 指回动物 ThingDef 的 defName。 |
| **PawnKindDef** `lifeStages/li/bodyGraphicData/texPath` | 117.4% (391/333) | 文本 | 各阶段贴图（一个 def 多档 → 超过 100%）。 |
| **PawnKindDef** `lifeStages/li/bodyGraphicData/drawSize` | 117.4% (391/333) | 数值 | 各阶段贴图尺寸。 |
| **PawnKindDef** `lifeStages/li/bodyGraphicData/color` | 33.6% (112/333) | 文本 | 贴图着色 (130,127,106)。 |
| **PawnKindDef** `lifeStages/li/dessicatedBodyGraphicData/texPath` | 99.4% (331/333) | 文本 | 干尸贴图。 |
| **PawnKindDef** `combatPower` | 65.5% (218/333) | 数值 | 战斗点数（影响袭击规模与自保）。 |
| **PawnKindDef** `ecoSystemWeight` | 27.0% (90/333) | 数值 | 生态权重（0.20 / 0.22 / 0.5），影响自然生成密度。 |

## 常见坑

1. **`bodyDef` 是错的，要写 `race/body`**：字段表无顶层 `bodyDef`（0 命中），原版写法见 `Core/Defs/ThingDefs_Races/Races_Animal_Hares.xml:26`（BaseHare 的 `<race><body>QuadrupedAnimalWithPawsAndTail</body>`）。
2. **`lifeStageAges` 必须包在 `race` 里**：顶层 `lifeStageAges` 不存在；正确路径 `race/lifeStageAges`（7.1%，146/2054），子项 `li/def` 与 `li/minAge` 分别是阶段 Def 名和起始年龄。
3. **只有 ThingDef 不会让动物刷出来**：原版每只动物都配一个同名 PawnKindDef（`Races_Animal_Hares.xml:103` 的 Hare），其中 `race` 指回 ThingDef、`lifeStages` 提供贴图。`race` 写错或漏写，游戏里选不到这个动物（**推测**）。
4. **`lifeStages` 的档数要与 `race/lifeStageAges` 对齐**：Hare 是 3 档（Baby/Juvenile/Adult）对应 3 条 `lifeStages/li`。数量不匹配会导致某阶段没贴图（**推测**，原版 391 条 lifeStages/li ≈ 3 档 × 130 只动物）。
5. **音效挂在 `lifeStageAges/li` 上而不是顶层**：`soundCall/soundAngry/soundWounded/soundDeath` 都出现在 `race/lifeStageAges/li/*` 下（各 4.9%–7.9%），且原版只写在成年那一档（见 Hares 的 AnimalAdult）。写在别处不会报错但不生效（**推测**）。
6. **`tools` 的伤害类型来自 ToolCapacityDef**：Bite/Blunt/Cut/Scratch/Poke/Stab 等 13 个取值（依据 `Core/Defs/ToolCapacityDefs/ToolCapacity.xml` 与 `Biotech/Defs/ToolCapacityDefs/ToolCapacityDefs.xml`）；`linkedBodyPartsGroup` 则必须填 BodyPartGroupDef 的 defName，否则攻击不会绑定到具体部位（**推测**）。

## 核验

- **逐字段对照**：ThingDef 部分取自 `03-全量字段参考/字段/ThingDef.md`（分母 2054），PawnKindDef 部分取自 `03-全量字段参考/字段/PawnKindDef.md`（分母 333）。可用机器可读版复核：
  `Select-String -Path '03-全量字段参考\字段总表.csv' -Pattern ',ThingDef,race/lifeStageAges/li/minAge,'` 与 `-Pattern ',PawnKindDef,lifeStages/li/bodyGraphicData/texPath,'`。
- **负面结论的核验方式**：`bodyDef`、顶层 `lifeStageAges` 在字段表与 `docs/def-schema.json` 中均 0 命中，故本文件明确改写成 `race/body`、`race/lifeStageAges`。
- **结构照抄原版**（路径相对 `<游戏安装目录>\Data\`）：
  - `Core/Defs/ThingDefs_Races/Races_Animal_Hares.xml`：BaseHare（第 4 行，race 全部字段的来源）、Hare ThingDef（第 88 行）、PawnKindDef HareBase（第 81 行）、PawnKindDef Hare（第 103 行，lifeStages 三档写法）。
  - `Core/Defs/ThingDefs_Races/Races_Animal_Base.xml`：BasePawn 与 AnimalThingBase（第 4 行起，第 104 行结束）——本模板 `ParentName` 来源，提供 category=Pawn、thinkTree、thingCategories(Animals)、recipes 等。
  - `Core/Defs/BodyDefs/...`（body 取值）、`Core/Defs/LifeStageDefs/LifeStages.xml`（AnimalBaby / AnimalJuvenile / AnimalAdult）、`Core/Defs/BodyPartGroupDefs/...`（Teeth / HeadAttackTool）。
- **Def 级属性说明**：`ParentName` / `Abstract` / `Name` 不是字段表收录的字段路径，属 Def 框架属性。
- **待验证项**：常见坑第 3、4、5、6 条的后果描述为静态比对得出的**推测**，未在本机启动游戏实测；字段路径本身均来自字段表，可保证存在。
