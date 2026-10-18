# ThingDef

## 用途

ThingDef 是物品、建筑、动物、投射物等一切"实体"的通用定义类型（原版 2054 个实例、2699 条字段路径，**没有任何单条路径出现率达到 90%**，字段完全按需组合）。武器是它的一个分支：远程武器用 `verbs`（`verbClass` = Verb_Shoot + `defaultProjectile`）发射弹丸，近战武器用 `tools`（`capacities` + `power` + `cooldownTime`）在接触攻击时生效；而命中率与射击间隔写在顶层 `statBases`（AccuracyTouch/Short/Medium/Long、RangedWeapon_Cooldown），**不在 verbs 里**。制造入口是 `recipeMaker`（在制造台生成配方），材料用 `costList`（固定清单）或 `costStuffCount` + `stuffCategories`（可替换材料）。它与弹丸 ThingDef、RecipeDef、WeaponTraitDef、DamageDef、WeaponClassDef、ToolCapacityDef、StuffCategoryDef 联动。

## 模板

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Defs>

  <!-- ================= 1) 弹丸：被下面那把枪的 defaultProjectile 引用 ================= -->
  <!-- ParentName="BaseBullet" 是 Core/Defs/ThingDefs_Misc/Weapons/BaseWeapons.xml 里的抽象 Def，
       它已提供 category=Projectile、thingClass=Bullet、tickerType=Normal、altitudeLayer=Projectile、
       useHitPoints=False、neverMultiSelect=True、graphicData.shaderType=Transparent。 -->
  <ThingDef ParentName="BaseBullet">
    <defName>EXAMPLE_Bullet_Coilgun</defName>
    <label>coilgun slug</label>
    <graphicData>
      <texPath>Things/Projectile/Bullet_Small</texPath>
      <graphicClass>Graphic_Single</graphicClass>
    </graphicData>
    <projectile>
      <damageDef>Bullet</damageDef>
      <damageAmountBase>16</damageAmountBase>
      <stoppingPower>1.5</stoppingPower>
      <speed>70</speed>
    </projectile>
  </ThingDef>

  <!-- ================= 2) 远程武器 ================= -->
  <!-- ParentName="BaseHumanMakeableGun" 提供：thingClass=ThingWithComps、category=Item、
       weaponClasses(Ranged)、thingCategories(WeaponsRanged)、weaponTags(Gun)、tradeTags(WeaponRanged)、
       comps(CompEquippable/CompQuality/Art/Biocodable)、recipeMaker(TableMachining/UnfinishedGun)。 -->
  <ThingDef ParentName="BaseHumanMakeableGun">
    <defName>EXAMPLE_Gun_Coilgun</defName>
    <label>coilgun</label>
    <description>一把示例线圈枪，用于演示远程武器的字段布局。</description>
    <possessionCount>1</possessionCount>
    <graphicData>
      <texPath>Things/Item/Equipment/WeaponRanged/AssaultRifle</texPath>
      <graphicClass>Graphic_Single</graphicClass>
    </graphicData>
    <uiIconScale>1.4</uiIconScale>
    <soundInteract>Interact_Rifle</soundInteract>
    <techLevel>Industrial</techLevel>
    <!-- 命中率必须写在 statBases：四档距离各一个 0~1 的系数 -->
    <statBases>
      <WorkToMake>36000</WorkToMake>
      <Mass>3.2</Mass>
      <AccuracyTouch>0.65</AccuracyTouch>
      <AccuracyShort>0.75</AccuracyShort>
      <AccuracyMedium>0.68</AccuracyMedium>
      <AccuracyLong>0.50</AccuracyLong>
      <RangedWeapon_Cooldown>1.9</RangedWeapon_Cooldown>
    </statBases>
    <!-- 固定材料清单：子元素名就是物价的 defName -->
    <costList>
      <Steel>60</Steel>
      <ComponentIndustrial>6</ComponentIndustrial>
    </costList>
    <!-- 武器分类（WeaponClassDef 的 10 个取值之一），不要和 weaponTags 混用 -->
    <weaponClasses>
      <li>Ranged</li>
    </weaponClasses>
    <!-- 松散标签：给 AI 配装/生成器/贸易筛选用 -->
    <weaponTags>
      <li>Gun</li>
      <li>IndustrialGunAdvanced</li>
    </weaponTags>
    <verbs>
      <li>
        <verbClass>Verb_Shoot</verbClass>
        <hasStandardCommand>true</hasStandardCommand>
        <defaultProjectile>EXAMPLE_Bullet_Coilgun</defaultProjectile>
        <warmupTime>0.9</warmupTime>
        <range>27.9</range>
        <burstShotCount>3</burstShotCount>
        <ticksBetweenBurstShots>8</ticksBetweenBurstShots>
        <soundCast>Shot_AssaultRifle</soundCast>
        <soundCastTail>GunTail_Medium</soundCastTail>
        <muzzleFlashScale>9</muzzleFlashScale>
      </li>
    </verbs>
    <!-- 枪托/枪管砸人的近战工具：远程武器原版也都带 tools -->
    <tools>
      <li>
        <label>stock</label>
        <capacities>
          <li>Blunt</li>
        </capacities>
        <power>9</power>
        <cooldownTime>2</cooldownTime>
      </li>
      <li>
        <label>barrel</label>
        <capacities>
          <li>Blunt</li>
          <li>Poke</li>
        </capacities>
        <power>9</power>
        <cooldownTime>2</cooldownTime>
      </li>
    </tools>
    <recipeMaker>
      <workSpeedStat>GeneralLaborSpeed</workSpeedStat>
      <workSkill>Crafting</workSkill>
      <effectWorking>Smith</effectWorking>
      <soundWorking>Recipe_Smith</soundWorking>
      <recipeUsers>
        <li>TableMachining</li>
      </recipeUsers>
      <unfinishedThingDef>UnfinishedGun</unfinishedThingDef>
      <researchPrerequisite>Gunsmithing</researchPrerequisite>
      <skillRequirements>
        <Crafting>6</Crafting>
      </skillRequirements>
      <displayPriority>415</displayPriority>
    </recipeMaker>
  </ThingDef>

  <!-- ================= 3) 近战武器（用可选材料制造） ================= -->
  <!-- ParentName="BaseMeleeWeapon_Sharp_Quality" 额外提供：weaponClasses(Melee+MeleePiercer)、
       thingCategories(WeaponsMelee)、comps(CompQuality + CompProperties_Art)、
       recipeMaker(ElectricSmithy/FueledSmithy + UnfinishedWeapon)、defaultIngredientFilter。 -->
  <ThingDef ParentName="BaseMeleeWeapon_Sharp_Quality">
    <defName>EXAMPLE_Melee_Testblade</defName>
    <label>test blade</label>
    <description>一把示例长刃，用于演示近战武器的 tools 三段式。</description>
    <possessionCount>1</possessionCount>
    <graphicData>
      <texPath>Things/Item/Equipment/WeaponMelee/LongSword</texPath>
      <graphicClass>Graphic_Single</graphicClass>
    </graphicData>
    <uiIconScale>1.2</uiIconScale>
    <techLevel>Medieval</techLevel>
    <!-- 可选材料路线：数量 + 允许的材料类别（StuffCategoryDef 的 6 个取值） -->
    <costStuffCount>50</costStuffCount>
    <stuffCategories>
      <li>Metallic</li>
      <li>Woody</li>
    </stuffCategories>
    <statBases>
      <WorkToMake>12000</WorkToMake>
      <Mass>1.8</Mass>
    </statBases>
    <equippedAngleOffset>-65</equippedAngleOffset>
    <weaponClasses>
      <li>Melee</li>
    </weaponClasses>
    <weaponTags>
      <li>MedievalMeleeAdvanced</li>
    </weaponTags>
    <!-- 每个工具都要同时给 capacities / power / cooldownTime -->
    <tools>
      <li>
        <label>handle</label>
        <capacities>
          <li>Blunt</li>
        </capacities>
        <power>9</power>
        <cooldownTime>2</cooldownTime>
      </li>
      <li>
        <label>point</label>
        <capacities>
          <li>Stab</li>
        </capacities>
        <power>17</power>
        <cooldownTime>2.6</cooldownTime>
      </li>
      <li>
        <label>edge</label>
        <capacities>
          <li>Cut</li>
        </capacities>
        <power>18</power>
        <cooldownTime>2.6</cooldownTime>
      </li>
    </tools>
    <recipeMaker>
      <researchPrerequisite>LongBlades</researchPrerequisite>
      <skillRequirements>
        <Crafting>5</Crafting>
      </skillRequirements>
      <displayPriority>420</displayPriority>
    </recipeMaker>
  </ThingDef>

</Defs>
```

## 字段说明

出现率来自 `03-全量字段参考/字段/ThingDef.md` 的全量字段表（分母 2054 个 ThingDef 实例）。

| 字段 | 出现率 | 值类型 | 说明 |
|---|---|---|---|
| `verbs` | 3.9% (80/2054) | 容器 | 开火行为列表，一个武器可写多条（切换射击模式）。 |
| `verbs/li/verbClass` | 3.9% (80/2054) | 文本 | 原版一律 `Verb_Shoot`；80 条 verbs 实例全都写了它。 |
| `verbs/li/defaultProjectile` | 3.0% (61/2054) | 文本 | 弹丸 ThingDef 的 defName，远程武器的核心字段。 |
| `verbs/li/range` | 3.6% (74/2054) | 数值 | 射程（格）；原版样例 19.9 / 22.9 / 23.9，突击步枪 30.9。 |
| `verbs/li/warmupTime` | 3.5% (73/2054) | 数值 | 举枪时间（秒）；原版样例 0 / 0.5 / 1.0。 |
| `verbs/li/minRange` | 0.5% (10/2054) | 数值 | 最小射程，炮塔/迫击炮类使用。 |
| `verbs/li/burstShotCount` | 2.2% (46/2054) | 数值 | 一次扳机的点射发数，原版 1 / 2 / 20。 |
| `verbs/li/ticksBetweenBurstShots` | 1.3% (26/2054) | 数值 | 点射内两发间隔 tick（60 tick = 1 秒），原版 2 / 4 / 10。 |
| `verbs/li/forcedMissRadius` | 1.0% (20/2054) | 数值 | 强制散布半径，霰弹/散射武器用；原版 0.1 / 1.9 / 3。 |
| `verbs/li/muzzleFlashScale` | 2.4% (49/2054) | 数值 | 枪口火光大小，原版 6 / 14 / 16。 |
| `verbs/li/soundCast` | 3.5% (71/2054) | 文本 | 开火音效（SoundDef）。 |
| `verbs/li/soundCastTail` | 2.3% (47/2054) | 文本 | 尾音，原版 GunTail_Light / GunTail_Medium / GunTail_Heavy。 |
| `verbs/li/hasStandardCommand` | 3.3% (68/2054) | 布尔 | 是否在征召条上出现"开火"命令。 |
| `verbs/li/onlyManualCast` | 1.1% (22/2054) | 布尔 | true 时 AI 不会主动使用（手雷、救命道具）。 |
| `verbs/li/requireLineOfSight` | 0.3% (6/2054) | 布尔 | 是否需要视线。 |
| `verbs/li/targetParams` | 1.7% (34/2054) | 容器 | 瞄准参数容器，让武器可以打地面。 |
| `verbs/li/targetParams/canTargetLocations` | 1.4% (29/2054) | 布尔 | 允许瞄准"格子"（手雷/迫击炮必写）。 |
| `verbs/li/targetParams/canTargetBuildings` | 0.6% (12/2054) | 布尔 | 允许瞄准建筑。 |
| `tools` | 8.9% (183/2054) | 容器 | 近战攻击工具列表；武器、动物都用它。 |
| `tools/li/power` | 24.2% (498/2054) | 数值 | 该工具每次命中的伤害。 |
| `tools/li/cooldownTime` | 24.2% (498/2054) | 数值 | 该工具冷却（秒）。 |
| `tools/li/capacities` | 24.2% (498/2054) | 容器 | 伤害类型容器。 |
| `tools/li/capacities/li` | 28.3% (581/2054) | 文本 | 取值来自 ToolCapacityDef（Blunt/Cut/Stab/Poke/Bite/…共 13 个）。 |
| `tools/li/label` | 21.0% (431/2054) | 文本 | 部位名（handle/barrel/head），战斗日志显示用。 |
| `tools/li/labelNoLocation` | 7.3% (151/2054) | 文本 | 无位置前缀的部位名（blade/claw）。 |
| `tools/li/labelUsedInLogging` | 0.3% (6/2054) | 布尔 | false 时该工具不写进战斗日志。 |
| `tools/li/linkedBodyPartsGroup` | 19.0% (390/2054) | 文本 | 绑定部位组（Teeth/HeadAttackTool/LeftBlade），动物与异形用。 |
| `tools/li/chanceFactor` | 8.7% (178/2054) | 数值 | 该工具被选中的概率权重。 |
| `tools/li/ensureLinkedBodyPartsGroupAlwaysUsable` | 5.9% (122/2054) | 布尔 | 保证绑定的部位组始终可用。 |
| `tools/li/armorPenetration` | 0.4% (8/2054) | 数值 | 该工具的穿甲。 |
| `tools/li/extraMeleeDamages` | 0.3% (7/2054) | 容器 | 附加伤害：`li/def`（EMP/Flame/Stun）+ `li/amount` + `li/chance`。 |
| `statBases/AccuracyTouch` | 2.0% (41/2054) | 数值 | 贴身档命中率。**在 statBases 里，不在 verbs。** |
| `statBases/AccuracyShort` | 2.0% (41/2054) | 数值 | 近距档命中率。 |
| `statBases/AccuracyMedium` | 2.0% (41/2054) | 数值 | 中距档命中率。 |
| `statBases/AccuracyLong` | 2.1% (43/2054) | 数值 | 远距档命中率。 |
| `statBases/RangedWeapon_Cooldown` | 2.5% (52/2054) | 数值 | 两次射击的间隔秒数。 |
| `statBases/WorkToMake` | 8.1% (167/2054) | 数值 | 制造工作量，与 recipeMaker 共同决定制造时间。 |
| `statBases/Mass` | 23.9% (490/2054) | 数值 | 质量（kg），影响负重与搬运。 |
| `costList` | 17.0% (350/2054) | 容器 | 固定材料清单，子元素名 = 物价 defName。 |
| `costList/Steel` | 10.0% (206/2054) | 数值 | 钢铁用量，原版 15 / 25 / 150。 |
| `costList/ComponentIndustrial` | 8.4% (173/2054) | 数值 | 工业组件用量，原版 1 / 2 / 4。 |
| `costStuffCount` | 8.4% (172/2054) | 数值 | 用可选材料制造时的材料数量，必须配 `stuffCategories`。 |
| `stuffCategories` | 8.2% (168/2054) | 容器 | 允许的材料类别容器。 |
| `stuffCategories/li` | 15.2% (313/2054) | 文本 | 取值来自 StuffCategoryDef（Fabric/Leathery/Metallic/Woody/Stony/Bioferrite）。 |
| `weaponClasses` | 3.1% (63/2054) | 容器 | 武器大类容器。 |
| `weaponClasses/li` | 4.2% (86/2054) | 文本 | 取值来自 WeaponClassDef（Melee/Ranged/RangedLight/RangedHeavy/LongShots/ShortShots/MeleePiercer/MeleeBlunt/Neolithic/Ultratech）。 |
| `weaponTags` | 3.1% (63/2054) | 容器 | 松散标签容器。 |
| `weaponTags/li` | 4.2% (86/2054) | 文本 | Gun/AssaultRifle/IndustrialGunAdvanced/MedievalMeleeDecent 等。 |
| `projectile` | 3.8% (78/2054) | 容器 | 弹丸 Def 上的飞行参数节点。 |
| `projectile/damageDef` | 3.3% (67/2054) | 文本 | 伤害类型 DamageDef（Bullet 等）。 |
| `projectile/damageAmountBase` | 2.3% (48/2054) | 数值 | 基础伤害，原版 7 / 12 / 18。 |
| `projectile/stoppingPower` | 1.0% (21/2054) | 数值 | 硬直强度，原版 1 / 1.5 / 2.5。 |
| `projectile/speed` | 3.4% (70/2054) | 数值 | 飞行速度，原版 25 / 55 / 75。 |
| `recipeMaker` | 11.9% (245/2054) | 容器 | 在 ThingDef 上内嵌配方，制造菜单里就能做这件装备。 |
| `recipeMaker/recipeUsers` | 4.6% (94/2054) | 容器 | 允许制造的台子；原版 CraftingSpot / ElectricSmithy / BioferriteShaper。 |
| `recipeMaker/recipeUsers/li` | 6.1% (125/2054) | 文本 | 台子的 ThingDef defName。 |
| `recipeMaker/researchPrerequisite` | 8.1% (167/2054) | 容器/文本 | 前置研究项目。 |
| `recipeMaker/skillRequirements` | 4.4% (90/2054) | 容器 | 技能要求容器。 |
| `recipeMaker/skillRequirements/Crafting` | 4.3% (88/2054) | 数值 | 最低制作技能，原版 3 / 4 / 6。 |
| `recipeMaker/displayPriority` | 7.3% (151/2054) | 数值 | 制造菜单排序，原版 110 / 140 / 150。 |
| `recipeMaker/unfinishedThingDef` | 3.1% (64/2054) | 文本 | 制造中的半成品（UnfinishedGun / UnfinishedWeapon）。 |
| `recipeMaker/workSkill` | 3.0% (62/2054) | 文本 | 受哪个技能影响（Crafting）。 |
| `recipeMaker/workSpeedStat` | 2.9% (60/2054) | 文本 | 受哪个速度属性影响（GeneralLaborSpeed）。 |
| `recipeMaker/effectWorking` | 2.6% (53/2054) | 文本 | 工作特效（Smith / Cook / Sculpt）。 |
| `recipeMaker/soundWorking` | 2.8% (57/2054) | 文本 | 工作音效（Recipe_Smith / Recipe_Machining）。 |
| `uiIconScale` | 7.3% (150/2054) | 数值 | 图标缩放。 |
| `equippedAngleOffset` | 1.1% (23/2054) | 数值 | 手持贴图的旋转角。 |
| `possessionCount` | 5.1% (105/2054) | 数值 | 生成时一件占用的数量，武器原版都写 1。 |
| `techLevel` | 6.1% (126/2054) | 文本 | Neolithic / Medieval / Industrial / Spacer / Archotech。 |
| `tradeTags` / `tradeTags/li` | 11.4% (234/2054) / 14.1% (290/2054) | 容器 / 文本 | 贸易分类（WeaponRanged / WeaponMelee）。 |
| `thingSetMakerTags/li` | 7.3% (150/2054) | 文本 | 战利品生成标签（RewardStandardQualitySuper）。 |
| `smeltable` | 2.1% (44/2054) | 布尔 | 能否被熔炼回收。 |
| `comps` / `comps/li` / `comps/li/compClass` | 33.3% (684) / 76.1% (1564) / 13.8% (284) | 容器 / 容器 / 文本 | 组件；字段表只收录子元素路径，不收录 `Class="..."` 属性。 |

## 常见坑

1. **命中率写进 `verbs` 会静默失效**：字段表 `verbs/li/*` 下没有任何 Accuracy 路径，真实路径是 `statBases/AccuracyTouch|AccuracyShort|AccuracyMedium|AccuracyLong`（各 2.0–2.1%）。原版每把枪都写在 statBases，见 `Core/Defs/ThingDefs_Misc/Weapons/RangedIndustrial.xml:30`（Gun_Revolver）。
2. **近战伤害不能写 `verbs`**：只有 `tools/li/power` + `tools/li/cooldownTime`（两者出现数完全相同：24.2%，498/2054，说明原版每个工具两件都写）。只写其中一个不会按预期出伤害（**推测**，未在游戏内实测）。
3. **`capacities` 只能填 ToolCapacityDef 的 13 个 defName**：Blunt / Cut / Stab / Poke / Bite / Scratch / ToxicBite / ScratchToxic / KickMaterialInEyes / Demolish / DemolishDoors / PorcupineBite / PorcupineScratch（依据 `Core/Defs/ToolCapacityDefs/ToolCapacity.xml` 与 `Biotech/Defs/ToolCapacityDefs/ToolCapacityDefs.xml`）。填不存在的值不会加载成功（**推测**）。
4. **`weaponClasses` 和 `weaponTags` 不是同义词**：`weaponClasses` 只能填 WeaponClassDef 的 10 个值，决定武器行为分类；`weaponTags` 是松散标签，写错只影响 AI 配装/贸易（**推测**）。原版常成对出现，如 Gun_AssaultRifle 同时写 `weaponClasses`（继承 Ranged）与 `weaponTags`（IndustrialGunAdvanced/AssaultRifle）。
5. **`costStuffCount` 必须配 `stuffCategories`**：原版用 `costStuffCount` 的武器都同时给材料类别（MeleeMedieval.xml 的 Mace：costStuffCount 50 + Metallic/Woody），否则材料选择列表为空、制造菜单里做不出来（**推测**）。`costList` 与 `costStuffCount` 是两条路线，同时写会让需求叠加（**推测**）。
6. **远程武器不带 `defaultProjectile` 等于空枪**：字段表该路径 3.0%（61/2054），而原版每一把射弹武器都有（RangedIndustrial.xml 全篇）；漏写会导致开火时找不到弹丸（**推测**，未实测）。

## 核验

- **逐字段对照**：上表每条出现率都取自 `03-全量字段参考/字段/ThingDef.md` 的"全量字段表"，分母 2054。可用机器可读版复核：
  `Select-String -Path '03-全量字段参考\字段总表.csv' -Pattern ',ThingDef,verbs/li/range,'`（列顺序 line,defType,path,present,instances,ratio,kind,samples,sourceFile）。
- **结构照抄原版**（原版路径均相对 `<游戏安装目录>\Data\`）：
  - `Core/Defs/ThingDefs_Misc/Weapons/BaseWeapons.xml`：BaseWeapon（第 4 行起）、BaseGun、BaseGunWithQuality、BaseMakeableGun、BaseHumanMakeableGun、BaseBullet、BaseMeleeWeapon / _Sharp / _Blunt / _Sharp_Quality 抽象链——本模板三个 `ParentName` 都指向这里的抽象 Def。
  - `Core/Defs/ThingDefs_Misc/Weapons/RangedIndustrial.xml`：Bullet_Revolver（第 7 行）、Gun_Revolver（第 20 行）、Gun_AssaultRifle（第 946 行）——本项目标 `projectile` 与 `verbs` 的写法来源。
  - `Core/Defs/ThingDefs_Misc/Weapons/MeleeMedieval.xml`：MeleeWeapon_Mace（第 5 行）、MeleeWeapon_LongSword（第 121 行）——近战 `tools` 与 `costStuffCount`+`stuffCategories` 来源。
- **取值枚举来源**：`Core/Defs/WeaponClassDefs/WeaponClassDefs.xml`（10 个）、`Core/Defs/ToolCapacityDefs/ToolCapacity.xml` + `Biotech/Defs/ToolCapacityDefs/ToolCapacityDefs.xml`（13 个）、`Core/Defs/Misc/StuffCategoryDefs/StuffCategories.xml`（6 个）——分别对应 `03-全量字段参考/字段/WeaponClassDef.md`、`ToolCapacityDef.md`、`StuffCategoryDef.md`。
- **Def 级属性说明**：`ParentName` / `Abstract` / `Name` / `MayRequire` 不是字段表收录的字段路径，属 Def 框架属性，本模板按原版 BaseWeapons.xml 的用法照抄。
- **comps 未自造**：本模板不自己写 `<li Class="...">`，全部沿用 BaseWeapons.xml 已定义的 comps，避免自创 Class 值（字段表只收录 `comps/li/compClass` 一类子元素路径，不收录 `Class` 属性）。
