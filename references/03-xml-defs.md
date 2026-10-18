# 03 — XML Def 系统

> **适用版本**: RimWorld 1.7（实测 1.7.4981 rev136） | **最后更新**: 2026-10-18


## 目录

- [什么是 Def？](#什么是def)
- [1.6 → 1.7 字段变更速查（先看这个）](#16--17-字段变更速查先看这个)
- [Def 类型速查表](#def类型速查表)
- [ThingDef 详解](#thingdef详解)
- [远程武器（1.7 真实结构）](#远程武器17-真实结构)
- [配方 RecipeDef（1.7 真实结构）](#配方-recipedef17-真实结构)
- [服装 Apparel（1.7 真实结构）](#服装-apparel17-真实结构)
- [ParentName 继承机制](#parentname继承机制)
- [MayRequire / MayRequireAnyOf（条件加载）](#mayrequiremayrequireanyof条件加载)
- [完整示例：彩虹喵喵剑](#完整示例彩虹喵喵剑)
- [常见问题](#常见问题)

## 什么是 Def？

Def（Definition）是 RimWorld 的数据定义系统。游戏中的所有内容——武器、建筑、植物、生物、派系、事件——都是通过 XML 文件中的 `Def` 定义的。

**核心理念**：XML 定义"数据是什么"，C# 代码定义"行为怎么做"。大部分内容型 mod 只需要 XML。

**⚠️ 每个 Def 在生成前，先查原版：**

| 你要写的 Def | RimSage 查询 |
|-------------|-------------|
| 近战武器 | `get_def_details("MeleeWeapon_Gladius")` |
| 远程武器 | `get_def_details("Gun_Revolver")` |
| 建筑 | `get_def_details("FueledSmithy")` |
| 服装 | `get_def_details("Apparel_CowboyHat")` |
| 植物 | `get_def_details("PlantRose")` |
| 配方 | `search_rimworld_source("RecipeDef")` |

## 1.6 → 1.7 字段变更速查（先看这个）

网上教程与旧模板里下面这些写法在 1.7 **全部无效或会报错**。写之前先对照这张表（括号内为原版 1.7 全库实测次数，证据见 `examples/rimtest-mod/_FINDINGS.md`）：

| 你要写的东西 | 1.6 及更早（❌ 无效） | 1.7 正确写法（✅） |
|--------------|----------------------|-------------------|
| 远程武器冷却 | 顶层 `<rangedWeapon_Cooldown>` | `statBases/RangedWeapon_Cooldown` |
| 射程 / 预热 / 弹丸 / 音效 | 顶层 `<range>` `<warmupTime>` `<verbClass>` | `verbs/li/range`、`verbs/li/warmupTime`、`verbs/li/defaultProjectile`、`verbs/li/soundCast` |
| 连发 | 顶层 `burstShotCount` | `verbs/li/burstShotCount` + `verbs/li/ticksBetweenBurstShots`（不写 = 单发） |
| 命中率 | — | `statBases/AccuracyTouch\|Short\|Medium\|Long` |
| 配方产物 | `<products><li><thingDef>…</thingDef><count>…</count></li></products>` | `<products><产物defName>数量</产物defName></products>`（字典写法，原版 50 个 products 块全是此形态） |
| 材料决定的产物 | 无需额外字段（以为） | 手写配方必须加 `<productHasIngredientStuff>true</productHasIngredientStuff>` |
| 服装覆盖部位 | `apBodyPartGroups` 或顶层 `bodyPartGroups` | `apparel/bodyPartGroups/li`（4.6% / 8.7%，值 Torso、Neck、FullHead） |
| 服装穿搭标签 | 以为是 `ApparelTagDef` 的引用 | **没有 ApparelTagDef 这个类型**；`apparel/tags/li` 是自由字符串（IndustrialBasic、Soldier…） |
| 建造工作量 | 顶层 `workToBuild` | `statBases/WorkToBuild`（14.5%） |
| 制造工作量（物品） | — | `statBases/WorkToMake`（8.1%）或 RecipeDef 的 `workAmount` |
| 脏污 | `filthAffordance`（1.7 无此路径） | `statBases/FilthRate`（走过掉污）或顶层 `filthLeaving`（离开留污） |
| 工作台 | 只写 `ParentName="BenchBase"` | 还需 `thingClass=Building_WorkTable` + `inspectorTabs/li=ITab_Bills`（否则没有「账单」页） |
| 单贴图随机化 | `Graphic_Random`（单文件会报 `No textures found at path`） | 单张图用 `Graphic_Single`；要随机必须把 texPath 做成目录并放多张图 |
| 补丁操作 | `PatchOperationSet`（1.7 无此类型） | Replace / Add / Insert / Remove / `PatchOperationAttributeSet` 等（详见 `04-xml-patching.md`） |

## Def 类型速查表

| Def 类型 | 用途 | 文件通常位置 |
|----------|------|-------------|
| `ThingDef` | 物品、建筑、植物、生物 | `Defs/ThingDefs/` |
| `RecipeDef` | 工作台配方 | `Defs/RecipeDefs/` |
| `ResearchDef` | 科技树节点 | `Defs/ResearchDefs/` |
| `HediffDef` | 健康状态/效果 | `Defs/HediffDefs/` |
| `TraitDef` | 角色特质 | `Defs/TraitDefs/` |
| `FactionDef` | 派系定义 | `Defs/FactionDefs/` |
| `IncidentDef` | 随机事件 | `Defs/IncidentDefs/` |
| `SoundDef` | 音效 | `Defs/SoundDefs/` |
| `DamageDef` | 伤害类型 | `Defs/DamageDefs/` |
| `JobDef` | 工作类型 | `Defs/JobDefs/` |
| `ThoughtDef` | 想法/心情 | `Defs/ThoughtDefs/` |
| `TerrainDef` | 地形 | `Defs/TerrainDefs/` |
| `WeatherDef` | 天气 | `Defs/WeatherDefs/` |

## ThingDef 详解

`ThingDef` 是最常用的 Def 类型，覆盖物品、建筑、植物等。

### 关键标签

#### 基础信息
```xml
<ThingDef ParentName="BaseMeleeWeapon_Sharp_Quality">
  <!-- ParentName 继承链：BaseWeapon → BaseMeleeWeapon → BaseMeleeWeapon_Sharp → BaseMeleeWeapon_Sharp_Quality -->
  <!-- ⚠️ 不同武器类型使用不同的 ParentName，详见下方"ParentName 继承机制" -->
  <defName>RCS_Weapon_PlasmaSword</defName>    <!-- 唯一 ID -->
  <label>plasma sword</label>                  <!-- 游戏内显示名 -->
  <description>A sword made of superheated plasma.</description>
  <possessionCount>1</possessionCount>         <!-- 可持有个数 -->
  <techLevel>Ultra</techLevel>                 <!-- 合法值见下：Animal/Neolithic/Medieval/Industrial/Spacer/Ultra/Archotech -->
  <!-- ⚠️ 合法枚举（反射 RimWorld.TechLevel 实测）：Undefined / Animal / Neolithic / Medieval / Industrial / Spacer / Ultra / Archotech -->
  <!-- ⚠️ 是 Ultra，不是 Ultratech。1.7 全库分布：Industrial 110、Spacer 60、Neolithic 40、Medieval 23、Ultra 13、Archotech 10、Animal 2 -->
```

#### 物品分类
```xml
  <thingCategories>
    <li>WeaponsMelee</li>              <!-- 所属分类，决定在哪个库存区显示 -->
  </thingCategories>
```

#### 市场价值
```xml
  <statBases>
    <MarketValue>500</MarketValue>     <!-- 基础市场价值（银） -->
    <Mass>2.5</Mass>                   <!-- 重量（kg） -->
    <MaxHitPoints>150</MaxHitPoints>   <!-- 耐久度 -->
    <Flammability>0</Flammability>     <!-- 可燃性（0-1） -->
  </statBases>
```

#### 材料成本（武器/装备用 stuff 系统）

```xml
  <!-- ⚠️ 武器和装备使用 stuff 材料系统，而非 costList -->
  <!-- costStuffCount = 所需材料单位数 -->
  <costStuffCount>50</costStuffCount>
  <stuffCategories>                 <!-- 允许的材料种类 -->
    <li>Metallic</li>               <!-- 金属类（钢、玻璃钢、铀等） -->
    <!-- <li>Woody</li> -->         <!-- 木质类 -->
    <!-- <li>Stony</li> -->         <!-- 石质类 -->
  </stuffCategories>
```

#### 材料成本（建筑用 costList）

```xml
  <!-- ⚠️ costList 用于建筑等有固定材料需求的 Def -->
  <costList>
    <Steel>100</Steel>              <!-- 所需材料 ThingDef defName -->
    <ComponentIndustrial>3</ComponentIndustrial>
  </costList>
```

#### 战斗属性（武器）
```xml
  <weaponTags>
    <li>SR_Plasma</li>
  </weaponTags>
  <tools>
    <li>
      <label>edge</label>              <!-- 攻击部位标签 -->
      <capacities>
        <li>Cut</li>                   <!-- 伤害类型：Cut/Blunt/Stab -->
        <li>Stab</li>
      </capacities>
      <power>20</power>                <!-- 基础伤害 -->
      <cooldownTime>1.5</cooldownTime> <!-- 冷却时间（秒） -->
    </li>
  </tools>
```

#### 组件系统（Comps）

```xml
  <!-- ⚠️ BaseWeapon 已内置 CompEquippable、CompForbiddable、CompStyleable -->
  <!-- 无需在 <comps> 中重复添加！仅在需要额外组件时添加： -->
  <comps>
    <!-- 品质系统（如果用 BaseMeleeWeapon_Sharp_Quality 父类则已继承） -->
    <!-- <li><compClass>CompQuality</compClass></li> -->
    <!-- 艺术品系统（Quality 父类已继承） -->
    <!-- <li Class="CompProperties_Art">...</li> -->
    <!-- 可摧毁（建筑用） -->
    <!-- <li Class="CompProperties_Breakdownable" /> -->
  </comps>
```

#### 贴图
```xml
  <graphicData>
    <texPath>Things/Item/SR_PlasmaSword</texPath>    <!-- 贴图路径：Textures/ 下 -->
    <graphicClass>Graphic_Single</graphicClass>      <!-- 单张贴图 -->
    <shaderType>CutoutComplex</shaderType>           <!-- 着色器类型 -->
  </graphicData>
```

#### 建筑特殊标签
```xml
  <ThingDef ParentName="BuildingBase">
    <defName>SR_ArcFurnace</defName>
    <category>Building</category>
    <size>(3,2)</size>               <!-- 占地面积（宽, 高） -->
    <designationCategory>Production</designationCategory> <!-- 建造菜单分类 -->
    <passability>Impassable</passability>           <!-- 通过性 -->
    <fillPercent>0.85</fillPercent>                 <!-- 贴图填充率 -->
    <terrainAffordanceNeeded>Heavy</terrainAffordanceNeeded> <!-- 地形要求 -->
    <statBases>
      <WorkToBuild>5000</WorkToBuild>               <!-- 建造工作量（不是 workToBuild） -->
    </statBases>
  </ThingDef>
```

> `statBases/WorkToBuild`（14.5%）是**建造**它要花的工；`statBases/WorkToMake`（8.1%）是**在里面制作**东西要花的工。两者混用会导致"瞬间建好"或"永远建不完"。

#### 工作台（BenchBase 系）必须补齐的四项

```xml
<ThingDef ParentName="BenchBase">
  <defName>SR_TestBench</defName>
  <thingClass>Building_WorkTable</thingClass>        <!-- ❗不写就没有配方逻辑（原版 17 处用法） -->
  <inspectorTabs>
    <li>ITab_Bills</li>                              <!-- ❗不写就没有「账单」页（原版 23 处用法） -->
  </inspectorTabs>
  <recipes>
    <li>SR_Recipe_PlasmaSword</li>                   <!-- 也可以反过来由 RecipeDef.recipeUsers 指向本台 -->
  </recipes>
  <comps>
    <li Class="CompProperties_AffectedByFacilities"> <!-- 被工具柜等设施加成（原版 25 处用法） -->
      <linkableFacilities>
        <li>ToolCabinet</li>
      </linkableFacilities>
    </li>
  </comps>
</ThingDef>
```

> 自动配方机制：建筑的 `<recipes>` 与 RecipeDef 的 `recipeUsers` 指向同一个配方**不会**出现重复账单——`ThingDef.AllRecipes` 是两者并集并用 `List.Contains` 去重。

## ParentName 继承机制

RimWorld 使用 `ParentName` 实现 Def 继承，减少重复代码。

**⚠️ 生成 Def 前，务必先查看原版父类定义！** 在 `<RimWorld>/Data/Core/Defs/ThingDefs_Misc/Weapons/BaseWeapons.xml` 中查看完整继承链。

**原版武器继承链：**
```
BaseWeapon（Abstract：thingClass, category, CompEquippable, CompForbiddable, CompStyleable）
├── BaseMeleeWeapon（Abstract：thingCategories WeaponsMelee, recipeMaker, tradeTags）
│   ├── BaseMeleeWeapon_Sharp（Abstract：weaponClasses MeleePiercer）
│   │   └── BaseMeleeWeapon_Sharp_Quality（Abstract：CompQuality + CompArt）
│   │       └── 👈 你的锋利近战武器用这个 ParentName
│   └── BaseMeleeWeapon_Blunt
└── BaseGun（Abstract：thingCategories WeaponsRanged）
    └── BaseGunWithQuality
        └── BaseMakeableGun（Abstract：recipeMaker）
            └── BaseHumanMakeableGun（Abstract：weaponTags + Biocodable）
                └── 👈 你的远程武器用这个 ParentName
```

**原版建筑继承链：**
```
BaseBuilding → BuildingBase → 你的建筑
```

**原版武器继承链里的关键事实**：`BaseMeleeWeapon` 虽然自带 `recipeMaker`，但原版近战武器（Gladius、LongSword、Mace）**各自重写了 recipeMaker**。想让武器进"锻造台 + 研究前置"体系，就要在自己的 Def 里写 `recipeMaker`（例：Gladius 的 `researchPrerequisite Smithing` + `skillRequirements/Crafting 3` + `displayPriority 410`）。

## 远程武器（1.7 真实结构）

```xml
<ThingDef ParentName="BaseBullet">
  <defName>SR_Projectile_IonRifle</defName>
  <graphicData>
    <texPath>Things/Projectile/SR_IonRifleBullet</texPath>
    <graphicClass>Graphic_Single</graphicClass>
  </graphicData>
  <projectile>
    <damageDef>Bullet</damageDef>
    <damageAmountBase>15</damageAmountBase>   <!-- 单发伤害 -->
    <stoppingPower>1.5</stoppingPower>
    <speed>60</speed>
  </projectile>
</ThingDef>

<ThingDef ParentName="BaseHumanMakeableGun">
  <defName>SR_Weapon_IonRifle</defName>
  <label>ion rifle</label>
  <techLevel>Spacer</techLevel>
  <statBases>
    <WorkToMake>25000</WorkToMake>
    <Mass>3.6</Mass>
    <AccuracyTouch>0.55</AccuracyTouch>       <!-- 四种距离命中率 -->
    <AccuracyShort>0.68</AccuracyShort>
    <AccuracyMedium>0.60</AccuracyMedium>
    <AccuracyLong>0.50</AccuracyLong>
    <RangedWeapon_Cooldown>1.8</RangedWeapon_Cooldown>  <!-- ❗冷却在这里，不在顶层 -->
  </statBases>
  <costList>                                  <!-- 远程武器用固定材料（近战/装备才用 costStuffCount） -->
    <Plasteel>40</Plasteel>
    <Steel>20</Steel>
    <ComponentIndustrial>6</ComponentIndustrial>
  </costList>
  <verbs>
    <li>
      <verbClass>Verb_Shoot</verbClass>
      <hasStandardCommand>true</hasStandardCommand>
      <defaultProjectile>SR_Projectile_IonRifle</defaultProjectile>
      <warmupTime>0.8</warmupTime>            <!-- 预热（秒） -->
      <range>30</range>                       <!-- 射程 -->
      <soundCast>Shot_ChargeRifle</soundCast> <!-- 音效 Def 名，先到原版 SoundDefs 里挑 -->
      <soundCastTail>GunTail_Medium</soundCastTail>
      <muzzleFlashScale>9</muzzleFlashScale>
    </li>
  </verbs>
</ThingDef>
```

- **不写 `recipeMaker`** → 继承 `BaseMakeableGun` 的（机械加工台 + Gunsmithing 研究 + UnfinishedGun），这是最省事的做法。
- 要连发：在 `verbs/li` 里加 `burstShotCount` 与 `ticksBetweenBurstShots`（原版电荷步枪是 3 发 / 12 tick）。
- 参考原版全文：`Data/Core/Defs/ThingDefs_Misc/Weapons/RangedSpacer.xml`（Gun_ChargeRifle）、`RangedIndustrial.xml`（Gun_Revolver）。

## 配方 RecipeDef（1.7 真实结构）

```xml
<RecipeDef>
  <defName>SR_Recipe_PlasmaSword</defName>
  <label>make plasma sword</label>
  <description>把材料锻造成等离子剑。</description>
  <jobString>正在锻造等离子剑。</jobString>
  <workAmount>8000</workAmount>                  <!-- 工作量（配 workSpeedStat 决定工时） -->
  <ingredients>
    <li>
      <filter>
        <categories><li>Metallic</li></categories>   <!-- 也可是 <thingDefs><li>Steel</li></thingDefs> -->
      </filter>
      <count>50</count>
    </li>
  </ingredients>
  <products>
    <SR_Weapon_PlasmaSword>1</SR_Weapon_PlasmaSword>  <!-- ❗字典写法：子元素名 = 产物 defName，值 = 数量 -->
  </products>
  <productHasIngredientStuff>true</productHasIngredientStuff>  <!-- 产物继承输入材料时必须写 -->
  <recipeUsers>
    <li>SR_TestBench</li>                              <!-- 在哪座台子上可用 -->
  </recipeUsers>
  <unfinishedThingDef>UnfinishedWeapon</unfinishedThingDef>    <!-- 半成品（可选） -->
</RecipeDef>
```

- 用 `costStuffCount` 类配方（产物材料由玩家选的材料决定）时，`productHasIngredientStuff` 必须显式写 `true`——该字段存在于代码里但原版 XML 0 处使用（那类配方由 `RecipeDefGenerator` 在代码中生成并自动处理）。
- `fixedIngredientFilter` / `defaultIngredientFilter` 用来限定或排除材料（例：`defaultIngredientFilter/disallowedThingDefs/li` 排除 Gold、Jade）。
- 配方名与描述要本地化：`Languages/<语言>/DefInjected/RecipeDef/*.xml` 写 `<SR_Recipe_PlasmaSword.label>…</SR_Recipe_PlasmaSword.label>` 与 `.jobString`。

## 服装 Apparel（1.7 真实结构）

```xml
<ThingDef ParentName="ApparelMakeableBase">
  <defName>SR_Apparel_TestVest</defName>
  <techLevel>Industrial</techLevel>
  <costStuffCount>60</costStuffCount>              <!-- 服装用 stuff 系统 -->
  <stuffCategories>
    <li>Fabric</li><li>Leathery</li><li>Metallic</li>
  </stuffCategories>
  <statBases>
    <WorkToMake>9000</WorkToMake>
    <Mass>4</Mass>
    <MaxHitPoints>200</MaxHitPoints>
    <StuffEffectMultiplierArmor>0.35</StuffEffectMultiplierArmor> <!-- 材料护甲系数 -->
    <ArmorRating_Sharp>1.00</ArmorRating_Sharp>
    <ArmorRating_Blunt>0.36</ArmorRating_Blunt>
    <ArmorRating_Heat>0.27</ArmorRating_Heat>
    <Insulation_Cold>1</Insulation_Cold>
    <EquipDelay>5</EquipDelay>
  </statBases>
  <thingCategories><li>ApparelArmor</li></thingCategories>
  <apparel>
    <bodyPartGroups>                                 <!-- ❗只在 apparel 节点里；没有 apBodyPartGroups -->
      <li>Torso</li>
      <li>Neck</li>
    </bodyPartGroups>
    <wornGraphicPath>Things/Pawn/Humanlike/Apparel/SR_TestVest/SR_TestVest</wornGraphicPath>
    <layers><li>Middle</li></layers>
    <tags><li>IndustrialBasic</li></tags>            <!-- 自由字符串，没有 ApparelTagDef -->
    <defaultOutfitTags><li>Soldier</li></defaultOutfitTags>
  </apparel>
</ThingDef>
```

- 穿戴贴图是**按方向分文件**放在 `wornGraphicPath` 指向的目录下（`…​_east / _north / _south / _west.png`）；原版部分装备还进一步按体型分（`_male_ / _female_ / _thin_ / _fat_ / _hulk_` 等）。只放一张总图不会生效。
- 物品图标另走 `graphicData/texPath`（原版惯例：`Things/Item/Equipment/Apparel/<Name>`）。
- `apparel/wornGraphicPath`（字符串，原版 104 处）与 `apparel/wornGraphicPaths`（列表，2 处）并存，常规用前者。

**查看继承定义**：在 `RimWorld/Data/Core/Defs/ThingDefs_Misc/Weapons/BaseWeapons.xml` 中搜索 `ParentName="BaseMeleeWeapon"` 查看其定义。

## MayRequire / MayRequireAnyOf（条件加载）

按 DLC 存在性决定是否加载 Def：

```xml
<!-- 仅 Biotech 激活时加载 -->
<ThingDef MayRequire="ludeon.rimworld.biotech" ParentName="BaseWeapon">
  ...
</ThingDef>

<!-- Biotech 或 Ideology 任一激活时加载 -->
<ThingDef MayRequireAnyOf="ludeon.rimworld.biotech, ludeon.rimworld.ideology">
  ...
</ThingDef>
```

## 完整示例：彩虹喵喵剑

> 以下是一个经过**实际验证**可用的近战武器 Def。基于原版 `BaseMeleeWeapon_Sharp_Quality` 父类。

```xml
<?xml version="1.0" encoding="utf-8"?>
<Defs>
  <ThingDef ParentName="BaseMeleeWeapon_Sharp_Quality">
    <defName>RCS_Weapon_RainbowCatSword</defName>
    <label>rainbow cat sword</label>
    <description>A shimmering blade infused with the power of rainbow cats.</description>

    <possessionCount>1</possessionCount>
    <techLevel>Ultra</techLevel>

    <!-- stuff 材料系统：需要 60 单位金属材料 -->
    <costStuffCount>60</costStuffCount>
    <stuffCategories>
      <li>Metallic</li>
    </stuffCategories>

    <statBases>
      <WorkToMake>12000</WorkToMake>
      <Mass>1.8</Mass>
      <MaxHitPoints>200</MaxHitPoints>
      <Flammability>0</Flammability>
      <DeteriorationRate>0.3</DeteriorationRate>
    </statBases>

    <equippedAngleOffset>-55</equippedAngleOffset>

    <weaponTags>
      <li>RCS_Rainbow</li>
    </weaponTags>

    <tools>
      <li>
        <label>edge</label>
        <capacities>
          <li>Cut</li>
          <li>Stab</li>
        </capacities>
        <power>18</power>
        <cooldownTime>1.3</cooldownTime>
        <armorPenetration>0.25</armorPenetration>
      </li>
    </tools>

    <graphicData>
      <texPath>Things/Item/RCS_RainbowCatSword</texPath>
      <graphicClass>Graphic_Single</graphicClass>
      <shaderType>CutoutComplex</shaderType>
    </graphicData>

    <recipeMaker>
      <researchPrerequisite>Smithing</researchPrerequisite>
      <skillRequirements>
        <Crafting>6</Crafting>
      </skillRequirements>
      <workAmount>10000</workAmount>
    </recipeMaker>
  </ThingDef>
</Defs>
```

**关键点说明：**
- `ParentName="BaseMeleeWeapon_Sharp_Quality"` 已继承 `thingCategories`、`CompEquippable`、`CompQuality`、`CompArt`、默认 `recipeMaker` 等
- `costStuffCount` + `stuffCategories` 替代 `costList`——玩家可用任意金属材料制作
- `possessionCount` 和 `techLevel` 是必需的
- 子元素标签会**合并**父类定义（如 `recipeMaker` 中只需写你覆盖的部分）

## 常见问题

### Q: 我的物品在游戏中不显示？
1. 检查 `texPath` 是否正确指向 `Textures/` 下的路径（不含 `Textures/` 前缀）
2. 确保贴图是 PNG 格式
3. 检查 `graphicClass` 是否匹配（单张贴图用 `Graphic_Single`）

### Q: defName 冲突怎么办？
始终使用你的专属前缀。如果仍然冲突，检查其他 mod 是否用了相同前缀。

### Q: 如何找到某个标签有哪些合法值？
**最重要的原则：先查原版！** 三条路（任一条可用即可，不必都具备）：
1. 本仓库自带 1.7 模板库：`node scripts/find-template.mjs --field 字段名`（会给出出现率、取值例与原版出处）
2. 本机原版数据：`grep -rn "字段名" "<RimWorld>/Data/"`（1560 个 XML）
3. RimSage MCP / dnSpy

都没有 → 明确标注「⚠️ 待验证草稿」并列出待核验字段，不要把猜测写成结论。

### Q: 贴图路径写对了，游戏里却是紫块 / 日志说 `No textures found at path`？
1. 单张贴图必须 `Graphic_Single`；用 `Graphic_Random` / `Graphic_Collection` 时 texPath 必须是**目录**且目录里有多张图，否则该 graphicClass 初始化失败。
2. 文件名大小写与 `texPath` 必须逐字一致（Linux/macOS 上大小写敏感）。
3. 贴图尺寸与朝向要照抄同类原版物品（武器图标是**水平**的，不要预先旋转 45°；详见 `07-assets.md`）。

### Q: 启动日志报 `Could not find parent` / 我的 Def 完全没加载？
1. `ParentName` 拼写与**该 Def 是否 Abstract**（抽象父类不能直接被游戏当作正经 Def 用，但可以被继承）。
2. `LoadFolders.xml` 是否覆盖了当前版本目录（见 `02-project-structure.md`）。
3. `MayRequire` 引用了玩家没装的 DLC → 该 Def 被整条跳过。
4. 更完整的排查链见 `08-debugging.md`。
