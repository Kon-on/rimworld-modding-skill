# 03 — XML Def 系统

> **适用版本**: RimWorld 1.6 | **最后更新**: 2026-05-31

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
  <techLevel>Ultratech</techLevel>             <!-- Neolithic/Medieval/Industrial/Spacer/Ultratech -->
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
      <WorkToBuild>5000</WorkToBuild>               <!-- 建造工作量 -->
    </statBases>
  </ThingDef>
```

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
    <techLevel>Ultratech</techLevel>

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
**最重要的原则：先查原版！** 使用 RimSage MCP 或直接到 `RimWorld/Data/Core/Defs/` 中搜索类似 Def，模仿原版的写法。
