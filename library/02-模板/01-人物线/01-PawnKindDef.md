# PawnKindDef

## 用途
PawnKindDef 描述「某一个派系下的某一种具体的人或动物」：它用 `race` 把 ThingDef（身体/种族）和 FactionDef 绑在一起，并决定这个个体出生时穿什么、带什么武器、有多强的战斗力。袭击队、商队、访客、任务人物在世界里「具体是谁」都由它决定。
它与 ThingDef（`race`，以及 `apparelRequired`/`techHediffsRequired` 里引用的衣物与植入体）、FactionDef（`defaultFactionDef`）、TraitDef（`disallowedTraits` / `forcedTraits`）联动；角色的属性上限仍由 `race` 指向的 ThingDef 决定，PawnKindDef 只负责"这一份"的装备与点数。原版共 333 个实例、277 条字段路径。

## 模板
```xml
<?xml version="1.0" encoding="utf-8" ?>
<Defs>

  <!-- 抽象模板：Name + Abstract="True" 定义可复用基类，下面的子 def 用 ParentName 继承 -->
  <PawnKindDef Name="EXAMPLE_GunnerBase" Abstract="True">
    <race>Human</race>                                    <!-- 必需：ThingDef 的 defName -->
    <defaultFactionDef>Pirate</defaultFactionDef>         <!-- 默认归属的 FactionDef -->
    <itemQuality>Normal</itemQuality>                     <!-- 生成装备的品质 -->
    <gearHealthRange>0.7~2.3</gearHealthRange>            <!-- 装备耐久比例，文本"最小~最大" -->
    <chemicalAddictionChance>0.1</chemicalAddictionChance>
    <combatEnhancingDrugsChance>0.15</combatEnhancingDrugsChance>
    <combatEnhancingDrugsCount>0~2</combatEnhancingDrugsCount>
    <biocodeWeaponChance>0.1</biocodeWeaponChance>
    <backstoryCryptosleepCommonality>0.08</backstoryCryptosleepCommonality>
    <maxGenerationAge>65</maxGenerationAge>
  </PawnKindDef>

  <PawnKindDef ParentName="EXAMPLE_GunnerBase">
    <defName>EXAMPLE_MercenaryGunner</defName>
    <label>example gunner</label>
    <labelPlural>example gunners</labelPlural>
    <combatPower>85</combatPower>                         <!-- 袭击点数换算的核心数值 -->

    <!-- 服装：apparelTags 用"服装标签(Tag)"筛选，apparelMoney 是预算区间 -->
    <apparelTags>
      <li>IndustrialBasic</li>
    </apparelTags>
    <apparelMoney>1000~1500</apparelMoney>
    <apparelAllowHeadgearChance>0.5</apparelAllowHeadgearChance>
    <!-- apparelRequired 里写的是具体 Apparel ThingDef 的 defName（不是 Tag） -->
    <apparelRequired>
      <li>Apparel_FlakVest</li>
    </apparelRequired>

    <!-- 武器：weaponTags 同样是标签筛选，weaponMoney 是预算 -->
    <weaponTags>
      <li>Gun</li>
    </weaponTags>
    <weaponMoney>330~650</weaponMoney>

    <!-- 植入体：chance 决定是否生成，money 决定档次，tags 决定类型 -->
    <techHediffsChance>0.15</techHediffsChance>
    <techHediffsMoney>700~1200</techHediffsMoney>
    <techHediffsTags>
      <li>Simple</li>
      <li>Advanced</li>
    </techHediffsTags>

    <disallowedTraits>
      <li>Brawler</li>
    </disallowedTraits>

    <!-- 随身物品：skipChance 是"整包不生成"的概率，subOptionsChooseOne 是候选之一 -->
    <inventoryOptions>
      <skipChance>0.9</skipChance>
      <subOptionsChooseOne>
        <li>
          <thingDef>MedicineIndustrial</thingDef>
          <countRange>1</countRange>
        </li>
      </subOptionsChooseOne>
    </inventoryOptions>

    <!-- 技能保底：生成时把该技能的随机区间抬到 4~14 -->
    <skills>
      <li>
        <skill>Shooting</skill>
        <range>4~14</range>
      </li>
    </skills>

    <canBeSapper>true</canBeSapper>
    <isGoodBreacher>true</isGoodBreacher>
    <initialResistanceRange>6~10</initialResistanceRange>
    <initialWillRange>2~4</initialWillRange>
  </PawnKindDef>

  <!--
    动物/机械体专用字段（下列仅示范，未启用；改用真实 race 时才写）：
    <wildGroupSize>3~6</wildGroupSize>            野生成群规模
    <ecoSystemWeight>0.20</ecoSystemWeight>       生态生成权重
    <lifeStages>...</lifeStages>                  各成长阶段的贴图（人形生物不用）
    <labelMale> / <labelFemale> / <labelFemalePlural>   性别称谓
    <forcedTraits><Undergrounder>0</Undergrounder></forcedTraits>  键=TraitDef名，值=degree
    <xenotypeSet><xenotypeChances><Hussar>0.03</Hussar></xenotypeChances></xenotypeSet>
  -->

</Defs>
```

## 字段说明
| 字段 | 出现率 | 值类型 | 说明 |
|---|---|---|---|
| `defName` | 85.6% (285/333) | 文本 | 唯一 ID，其他 Def 用它引用本兵种 |
| `label` | 76.3% (254/333) | 文本 | 单数显示名；复数另用 `labelPlural`（12.3% (41/333)） |
| `combatPower` | 65.5% (218/333) | 数值 | 袭击点数换算的核心数值，样例 300 / 70 / 80 |
| `race` | 55.9% (186/333) | 文本 | 指向 ThingDef；多数实例从 ParentName 继承 |
| `lifeStages` | 46.9% (156/333) | 容器 | 各阶段 bodyGraphicData（贴图/尺寸），动物与机械体用 |
| `apparelTags/li` | 45.6% (152/333) | 文本 | 服装**标签**筛选；本体 `apparelTags` 17.7% (59/333) |
| `weaponTags/li` | 36.3% (121/333) | 文本 | 武器**标签**筛选，样例 `Gun`、`MedievalMeleeDecent` |
| `initialResistanceRange` | 30.9% (103/333) | 文本 | 招募抵抗值区间，如 `13~21` |
| `techHediffsTags/li` | 29.1% (97/333) | 文本 | 植入体标签；本体 15.6% (52/333) |
| `weaponTags` | 28.2% (94/333) | 容器 | 标签列表容器 |
| `ecoSystemWeight` | 27.0% (90/333) | 数值 | 生态生成权重（动物） |
| `apparelMoney` | 22.8% (76/333) | 数值/文本 | 服装预算区间，如 `400~1000` |
| `weaponMoney` | 21.3% (71/333) | 数值/文本 | 武器预算区间 |
| `techHediffsMoney` | 21.3% (71/333) | 数值/文本 | 植入体预算区间 |
| `initialWillRange` | 20.1% (67/333) | 数值/文本 | 初始意志（招募难度） |
| `defaultFactionDef` | 19.8% (66/333) | 容器/文本 | 默认派系 |
| `techHediffsChance` | 17.7% (59/333) | 数值 | 生成植入体的概率 |
| `apparelRequired/li` | 16.5% (55/333) | 文本 | **Apparel 的 defName**（不是标签）；本体 10.8% (36/333) |
| `apparelAllowHeadgearChance` | 15.3% (51/333) | 数值 | 允许戴头部装备的概率 |
| `gearHealthRange` | 13.5% (45/333) | 文本 | 装备耐久比例区间 |
| `labelPlural` | 12.3% (41/333) | 文本 | 复数显示名 |
| `itemQuality` | 10.5% (35/333) | 文本 | 装备品质，样例 `Awful` / `Good` / `Normal` |
| `wildGroupSize` | 10.5% (35/333) | 文本 | 野生成群规模 |
| `xenotypeSet/xenotypeChances` | 9.0% (30/333) | 容器 | 各 xenotype 概率，键为 XenotypeDef 名 |
| `backstoryCryptosleepCommonality` | 7.8% (26/333) | 数值 | 冷冻睡眠背景比例 |
| `disallowedTraits/li` | 7.8% (26/333) | 文本 | 禁止出现的特质；本体 6.9% (23/333) |
| `chemicalAddictionChance` | 7.2% (24/333) | 数值 | 成瘾品成瘾概率 |
| `isFighter` | 6.9% (23/333) | 布尔 | 是否作为战斗单位 |
| `inventoryOptions/subOptionsChooseOne/li/thingDef` | 6.0% (20/333) | 文本 | 随身物品候选 |
| `inventoryOptions/subOptionsChooseOne/li/countRange` | 6.0% (20/333) | 数值/文本 | 随身物品数量 |
| `useFactionXenotypes` | 5.4% (18/333) | 布尔 | 是否跟随派系 xenotype |
| `inventoryOptions/skipChance` | 4.8% (16/333) | 数值 | 不生成随身物品的概率 |
| `skills/li/skill` / `skills/li/range` | 各 4.8% (16/333) | 文本 | 技能名与保底区间 |
| `combatEnhancingDrugsChance` | 4.8% (16/333) | 数值 | 携带战斗药物概率 |
| `maxGenerationAge` | 4.8% (16/333) | 数值 | 生成年龄上限 |
| `invNutrition` | 4.5% (15/333) | 数值 | 随身食物营养值 |
| `biocodeWeaponChance` | 3.9% (13/333) | 数值 | 生物绑定武器概率 |
| `startingHediffs/li/def` | 3.9% (13/333) | 文本 | 初始 hediff；本体 2.7% (9/333) |
| `combatEnhancingDrugsCount` | 3.6% (12/333) | 文本 | 战斗药物数量区间 |
| `canBeSapper` | 3.6% (12/333) | 布尔 | 可作为工兵 |
| `techHediffsRequired/li` | 3.0% (10/333) | 文本 | 必须安装的植入体 defName；本体 2.4% (8/333) |
| `titleRequired` | 2.7% (9/333) | 文本 | 需要的爵位（Royalty） |
| `factionLeader` | 1.8% (6/333) | 布尔 | 是否为派系领袖 |
| `isGoodBreacher` | 1.5% (5/333) | 布尔 | 是否擅长拆墙 |

## 常见坑
1. 把衣物/植入体的 defName 塞进 `apparelTags`/`techHediffsTags` 会永远匹配不到——这两个字段收的是 ThingDef 里声明的**标签**；要指定具体物品请用 `apparelRequired` / `techHediffsRequired`（原版样例值分别是 `Apparel_Duster`、`DeathAcidifier`）。
2. 独立 def（不写 ParentName）必须自己写 `race`，否则加载后这个兵种无法生成。原版只有 55.9% 显式写 `race`，其余都从 `ParentName` 继承。【推测：漏写时报错文本未核实】
3. `combatPower` 直接参与袭击点数换算，填 0 或与实际装备不符会让袭击强度失真（原版 65.5% 都填了真实数值，样例 300 / 70 / 80）。
4. `inventoryOptions/skipChance` 是"整包都不生成"的概率，写 `1` 等于永远不刷药品；原版常用 0.9~0.95。
5. `lifeStages`、`ecoSystemWeight`、`wildGroupSize` 属于动物/机械体路线（原版出现率 46.9% / 27.0% / 10.5%）。【推测：人形兵种不读取这些字段】
6. 数值区间统一写成 `最小~最大` 的**文本**（如 `0.7~3.2`、`0~2`），原版样例值全部是这种形式。

## 核验
- 模板结构（抽象基类 + ParentName 继承 + 具体 def）与逐字段取值，对照原版 `Core/Defs/PawnKindDefs_Humanlikes/PawnKinds_Mercenary.xml`：`MercenaryBase`(:4-15) 给出 race `Human`/defaultFactionDef `Pirate`/itemQuality `Normal`/chemicalAddictionChance/biocodeWeaponChance/backstoryCryptosleepCommonality/maxGenerationAge/combatEnhancingDrugsChance/combatEnhancingDrugsCount；`GrenadierBase`(:19-51) 给出 gearHealthRange `0.7~2.3`/initialWillRange `1~3`/apparelTags/apparelMoney/weaponMoney/techHediffsChance/techHediffsMoney/techHediffsTags/disallowedTraits `Brawler`/inventoryOptions；`MercenaryGunnerBase`(:100-137) 给出 weaponTags `Gun`、apparelRequired 之外的 apparelMoney `1000~1500`、skills/li 的 `Shooting`+`4~14`；`Grenadier_Destructive`(:53-63) 与 `PirateBoss`(:305-312) 给出 combatPower/canBeSapper/isGoodBreacher/initialResistanceRange/factionLeader/labelPlural。
- 表格中的出现率、值类型、样例值全部来自 `library/03-全量字段参考/字段/PawnKindDef.md` 的「全量字段表」（该目录由本机 1.7.4981 rev136 实测 333 个原版实例提取）。
- 可交叉核对的其它原版文件：`Core/Defs/PawnKindDefs_Humanlikes/PawnKinds_Tribal.xml`、`PawnKinds_Pirate.xml`、`Core/Defs/PawnKindDefs/PawnKinds_Breach.xml`。
