# 离子步枪（Ion Rifle）—— RimWorld 1.7 远程武器

按技能的三层决策，这个需求落在 **①「有模板」**：远程武器有现成模板 `assets/templates/weapon-ranged.xml`，注释头标的是「验证状态：已验证（对照原版 1.7 全库）」——所以**直接套模板生成，不调 MCP、不凭记忆写字段**。

## 一、先说清这几个数值写在哪（1.7 结构，最常踩的坑）

**一把远程武器 = 两个 ThingDef：弹丸 + 枪本体。** 伤害定义在**弹丸**上，不在枪上，两者用 `defaultProjectile` 接起来。

| 你要的 | 1.7 里写在哪 |
|---|---|
| 伤害 15 | 弹丸 Def 的 `projectile/damageAmountBase`（写在枪上不生效） |
| 射程 30 | `verbs/li/range` |
| 射击间隔 | `statBases/RangedWeapon_Cooldown` |
| 预热（瞄准）时间 | `verbs/li/warmupTime` |
| 命中率 4 档 | `statBases` 里的 `AccuracyTouch / AccuracyShort / AccuracyMedium / AccuracyLong` |
| 连发还是单发 | `verbs/li` 里加 `burstShotCount` + `ticksBetweenBurstShots`（不写 = 单发） |

> ⚠️ 1.6 及更早的写法在 1.7 **全部失效**，老教程、老模板都别照抄：顶层 `rangedWeapon_Range`、`rangedWeapon_WarmupTime`、`rangedWeapon_Cooldown` 以及顶层 `verbClass` 这四个路径，原版 1.7 全库已经不存在。写了**不报错但完全不生效**，是最难排查的一类问题。

## 二、开工前，4 个值需要你定（技能规定：这四项 AI 不替你编）

| # | 需要你给 | 例子 |
|---|---|---|
| 1 | 前缀 prefix | `ABC` → Def 名就是 `ABC_Weapon_IonRifle` |
| 2 | namespace | `ABC.IonRifleMod` |
| 3 | packageId | 全小写、无空格，如 `yourname.ionrifle`（测试版建议带 `test.` 前缀） |
| 4 | 作者名 | About.xml 的 `<author>` |

下面 Def 里所有 `{{YourPrefix}}` 都替换成第 1 项的值（**没替换完就进游戏会报错**）。
把这 4 个值发我，我直接把整包填好给你（Def + About.xml + 贴图清单 + 中文汉化）。

## 三、武器 Def

落盘位置：`你的mod/Defs/ThingDefs/Weapons_Ranged.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<Defs>

  <!-- ================= 1) 弹丸：伤害 15 定义在这里 ================= -->
  <!-- ParentName="BaseBullet" 是原版 BaseWeapons.xml 里的抽象 Def，已提供：
       category=Projectile、thingClass=Bullet、altitudeLayer=Projectile、
       useHitPoints=False、neverMultiSelect=True、graphicData.shaderType=Transparent
       —— 这些都不用重复写。 -->
  <ThingDef ParentName="BaseBullet">
    <defName>{{YourPrefix}}_Projectile_IonRifle</defName>
    <label>ion bolt</label>
    <graphicData>
      <!-- 指向单个贴图文件；Graphic_Single 才是单文件写法 -->
      <texPath>Things/Projectile/{{YourPrefix}}_IonRifleBullet</texPath>
      <graphicClass>Graphic_Single</graphicClass>
    </graphicData>
    <projectile>
      <damageDef>Bullet</damageDef>                 <!-- 原版可选：Bullet / Arrow / Beam / Bomb… -->
      <damageAmountBase>15</damageAmountBase>       <!-- ★ 伤害 15 -->
      <stoppingPower>1.5</stoppingPower>            <!-- 穿透力 -->
      <speed>60</speed>                             <!-- 弹丸飞行速度 -->
    </projectile>
  </ThingDef>

  <!-- ================= 2) 枪本体 ================= -->
  <!-- ParentName="BaseHumanMakeableGun" 继承链：BaseWeapon → BaseGun → BaseGunWithQuality
       → BaseMakeableGun → BaseHumanMakeableGun，已经免费给你：
         thingClass=ThingWithComps、category=Item、thingCategories=WeaponsRanged、
         weaponTags=Gun、tradeTags=WeaponRanged、comps(CompEquippable/Quality/Art/Biocodable)、
         recipeMaker(机械加工台 TableMachining + Gunsmithing 研究 + UnfinishedGun)
       —— 所以下面不需要再写这些东西。 -->
  <ThingDef ParentName="BaseHumanMakeableGun">
    <defName>{{YourPrefix}}_Weapon_IonRifle</defName>
    <label>ion rifle</label>
    <description>A spacer-tech rifle that fires superheated ion bolts. Effective at long range, but its capacitor needs a moment to recharge between shots.</description>
    <techLevel>Spacer</techLevel>          <!-- 合法值：Animal/Neolithic/Medieval/Industrial/Spacer/Ultra/Archotech -->
    <possessionCount>1</possessionCount>

    <graphicData>
      <texPath>Things/Item/Equipment/WeaponRanged/{{YourPrefix}}_IonRifle</texPath>
      <graphicClass>Graphic_Single</graphicClass>
    </graphicData>
    <uiIconScale>1.15</uiIconScale>        <!-- 图标缩放（原版电荷步枪约 1.15、左轮 1.4） -->

    <soundInteract>Interact_Rifle</soundInteract>   <!-- 拾取/选中音效，必须是真实存在的 SoundDef -->

    <statBases>
      <WorkToMake>25000</WorkToMake>       <!-- 制作工作量 -->
      <Mass>3.6</Mass>                     <!-- 重量 kg -->
      <AccuracyTouch>0.55</AccuracyTouch>  <!-- 四种距离命中率，0~1 -->
      <AccuracyShort>0.68</AccuracyShort>
      <AccuracyMedium>0.60</AccuracyMedium>
      <AccuracyLong>0.50</AccuracyLong>
      <RangedWeapon_Cooldown>1.8</RangedWeapon_Cooldown>  <!-- ★ 两次射击间隔（秒） -->
    </statBases>

    <weaponClasses>
      <li>RangedLight</li>                 <!-- 原版取值：RangedLight / RangedHeavy / RangedSpacer… -->
    </weaponClasses>
    <weaponTags>
      <li>SpacerGun</li>                   <!-- 列表是「追加」语义，父级的 Gun 仍在，不会丢 -->
    </weaponTags>
    <thingSetMakerTags>
      <li>RewardStandardQualitySuper</li>  <!-- 让它能作为任务奖励出现；不想要可整段删掉 -->
    </thingSetMakerTags>

    <!-- 材料：子元素名 = 物价的 defName（固定清单写法，原版枪械都是这么写的） -->
    <costList>
      <Plasteel>40</Plasteel>
      <Steel>20</Steel>
      <ComponentIndustrial>6</ComponentIndustrial>
    </costList>

    <verbs>
      <li>
        <verbClass>Verb_Shoot</verbClass>              <!-- 远程射击动词 -->
        <hasStandardCommand>true</hasStandardCommand>  <!-- 允许玩家手动强制开火 -->
        <defaultProjectile>{{YourPrefix}}_Projectile_IonRifle</defaultProjectile>  <!-- 接上面的弹丸 -->
        <warmupTime>0.8</warmupTime>                   <!-- 瞄准/预热（秒） -->
        <range>30</range>                              <!-- ★ 射程 30 格 -->
        <soundCast>Shot_ChargeRifle</soundCast>        <!-- 开火音效（原版 SoundDef） -->
        <soundCastTail>GunTail_Medium</soundCastTail>  <!-- 尾音：GunTail_Light / GunTail_Medium / GunTail_Heavy -->
        <muzzleFlashScale>9</muzzleFlashScale>
        <!-- 想做三连发，就在这一行下面加：
             <burstShotCount>3</burstShotCount>
             <ticksBetweenBurstShots>8</ticksBetweenBurstShots>
             不写这两个就是单发。 -->
      </li>
    </verbs>

    <!-- 原版远程武器都带近战 tools：被贴脸时用枪托/枪管砸人，不做就是纯白板 -->
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
  </ThingDef>

</Defs>
```

## 四、贴图（2 张，缺了是紫块 / 红字）

| 文件 | 建议尺寸 | 用途 |
|---|---|---|
| `Textures/Things/Item/Equipment/WeaponRanged/{{YourPrefix}}_IonRifle.png` | 128×128 | 枪的图标/手持贴图 |
| `Textures/Things/Projectile/{{YourPrefix}}_IonRifleBullet.png` | 32×32 | 弹丸 |

PNG 格式；路径要和 Def 里的 `texPath` 一一对应：`Textures/` 不出现在 texPath 里，texPath 里也不写 `.png` 扩展名。
（顺便避个坑：`Graphic_Random` 要求 texPath 指向**目录**且目录里有贴图，指向单文件会报 `No textures found at path`；单张图就用 `Graphic_Single`。）

## 五、制作入口 & 中文名

- **制作入口不用写**：没写 `recipeMaker` → 自动继承 `BaseMakeableGun` 的配方，即研究 `Gunsmithing` 后，**机械加工台**里出现「制造离子步枪」账单，材料就是上面 `costList` 那三样。想换工作台/研究，再在自己的 Def 里写 `<recipeMaker>` 覆盖。
- **中文名（可选但推荐）**：`Languages/ChineseSimplified/DefInjected/ThingDef/{{YourPrefix}}_Weapons.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<LanguageData>
  <{{YourPrefix}}_Weapon_IonRifle.label>离子步枪</{{YourPrefix}}_Weapon_IonRifle.label>
  <{{YourPrefix}}_Weapon_IonRifle.description>一种发射超热离子弹的太空时代步枪，射程远、单发威力足，但每次射击后电容需要短暂充能。</{{YourPrefix}}_Weapon_IonRifle.description>
  <{{YourPrefix}}_Projectile_IonRifle.label>离子弹</{{YourPrefix}}_Projectile_IonRifle.label>
</LanguageData>
```

> DefInjected 的键名就是 defName，所以 `{{YourPrefix}}` 也要全部替换掉、替换后才是合法 XML，别替换到一半就丢进游戏。
> 语言目录名用 `ChineseSimplified` 或 `ChineseSimplified (简体中文)` 都认（1.7 实测两者皆可），想稳可以两个目录都放一份。

## 六、测试（技能默认流程：测试版先行）

先出测试版 → 你进游戏确认没 bug → 再正规化（补 About.xml、清理命名、可选发 Steam）。测试步骤：

1. 把 mod 目录放进 `RimWorld/Mods/`，启动器里勾选启用；
2. 打开开发者模式，看**日志窗口**有没有红字（字段名写错、defName 重复都会在这里报）；
3. 开发者工具 → 生成物品，或直接搜索 `{{YourPrefix}}_Weapon_IonRifle`；
4. 让小人装备并开火。信息面板应显示：**射程 30 格 / 伤害 15（Bullet 类型）/ 预热 0.8 秒 / 冷却 1.8 秒 / 单发**；开火有枪口闪光和音效；弹丸贴图正常（不是紫块）。

有红字就把日志原文发我——按技能流程排查：**先看日志 → 再对照原版 → 最后才查自己写的字段**，不猜。

## 七、别忘 AI 标注（技能硬性要求）

`About/About.xml` 的 `<description>` 末尾加一行 `[AI 辅助生成]`，玩家在 Mod 列表里能看到；以后发 Steam Workshop 时，页面描述里也要写明。

## 八、这套写法凭什么能直接用

- 字段名、枚举值、ParentName 继承链来自 `assets/templates/weapon-ranged.xml`，该模板注释头标的就是「已验证（对照原版 1.7 全库）」——替换占位符即可，**免核验**；
- 对应的原版参考文件（想自己核对时看这几个）：
  - `Data/Core/Defs/ThingDefs_Misc/Weapons/BaseWeapons.xml` —— BaseBullet / BaseGun / BaseGunWithQuality / BaseMakeableGun / BaseHumanMakeableGun 抽象链；
  - `Data/Core/Defs/ThingDefs_Misc/Weapons/RangedIndustrial.xml` —— Gun_Revolver（工业枪的 `statBases` 命中率 + `RangedWeapon_Cooldown` + `verbs` 写法）；
  - `Data/Core/Defs/ThingDefs_Misc/Weapons/RangedSpacer.xml` —— Gun_ChargeRifle（Spacer 能源枪的 techLevel / weaponTags / tools / soundCast）；
- 音效名都取自原版真实 SoundDef：`Interact_Rifle`（ThingDef/soundInteract 的原版在用值）、`Shot_ChargeRifle`、`GunTail_Medium`（皆为原版在用值）。

需要我把上面这些直接落盘成一个可加载的测试版 mod 项目吗？给我那 4 个值（前缀 / namespace / packageId / 作者名）就行。
