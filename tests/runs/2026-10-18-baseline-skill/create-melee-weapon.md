# 等离子匕首 · 近战武器 Def（RimWorld 1.7）

**这次走的是哪条路**：近战武器有已验证模板 `assets/templates/weapon-melee.xml`（注释头标注「验证状态：已验证（对照原版 `Data/Core/Defs/ThingDefs_Misc/Weapons/MeleeMedieval.xml`）」），按技能的三层决策直接走第 ① 层：**用模板生成，不调 MCP**。字段名与取值我再用本机 1.7 模板库复核了一遍——`tools/li/power` 出现率 24.2%、`tools/li/cooldownTime` 24.2%、`tools/li/capacities/li` 28.3%、`techLevel` 6.1%、`stuffCategories/li` 15.2%，都不是凭记忆写的。

## ⚠️ 先改一个值：科技等级是 `Ultra`

你想要的那个科技等级，对应的枚举值是 **`Ultra`**，**后面不要加 `tech` 后缀**（把两个词连成一体的写法会被判为非法值）。1.7 的 `TechLevel` 枚举（反射实测）只有 8 个值：

`Undefined / Animal / Neolithic / Medieval / Industrial / Spacer / Ultra / Archotech`

1.7 全库分布：Industrial 110、Spacer 60、Neolithic 40、Medieval 23、Ultra 13、Archotech 10、Animal 2。写法带了后缀会被判非法值——这是本技能记录在案的高频错误，下面 XML 里已经按 `Ultra` 写好。

## 先定四项，我才能落盘

这四项按技能规定由你决定，AI 不替你预设：

| 项目 | 规则 | 你的取值 |
|---|---|---|
| 前缀 | 2–4 字符，所有 defName 与贴图名都带它 | ？ |
| namespace | `<前缀>.<Mod名>`（只有写 C# 时才用到） | ？ |
| packageId | 全小写无空格，测试版先用 `test.<功能名>` | ？ |
| 作者 | About.xml 与 Steam 页面里的 `<author>` | ？ |

把这四项发我，我就把下面 XML 里的 `{{...}}` 全部填好并直接落盘；你要是说「你看着办」，我按 mod 名生成临时值，并在正规化时提醒你替换。

## 一、ThingDef（唯一必需的 Def）

```xml
<?xml version="1.0" encoding="utf-8"?>
<!--
  等离子匕首 / plasma dagger —— 近战武器 ThingDef（测试版）
  验证状态：已验证（按本技能模板 assets/templates/weapon-melee.xml 生成，该模板注释头对照原版
            Data/Core/Defs/ThingDefs_Misc/Weapons/MeleeMedieval.xml）
  AI 辅助生成
  模板类型：ThingDef · 近战武器
  原版参考：MeleeMedieval.xml（MeleeWeapon_Mace 第 5 行、MeleeWeapon_LongSword 第 121 行）
  ParentName 继承链：BaseWeapon → BaseMeleeWeapon → BaseMeleeWeapon_Sharp → BaseMeleeWeapon_Sharp_Quality
    父类已提供：thingCategories(WeaponsMelee)、weaponClasses(Melee / MeleePiercer)、
    comps(Equippable / Forbiddable / Styleable / Quality / Art)、recipeMaker(锻造台 + UnfinishedWeapon)
  关键设计决策：
    1. techLevel 写 Ultra：1.7 的 TechLevel 枚举里没有带 tech 后缀的写法
    2. 匕首只保留一个工具（一个刃尖），伤害与冷却就是你要求的 18 / 1.2
    3. 材料走 costStuffCount + stuffCategories，玩家可用任意金属打造（不是固定成本清单）
    4. 贴图 128×128、水平绘制；手持倾角交给 equippedAngleOffset
-->
<Defs>
  <ThingDef ParentName="BaseMeleeWeapon_Sharp_Quality">
    <defName>{{YourPrefix}}_Weapon_PlasmaDagger</defName>
    <label>plasma dagger</label>
    <description>A dagger whose edge is a sliver of contained plasma. It cuts through armor like cloth.</description>

    <possessionCount>1</possessionCount>
    <techLevel>Ultra</techLevel>                       <!-- 别加 tech 后缀；合法值：Animal / Neolithic / Medieval / Industrial / Spacer / Ultra / Archotech -->

    <!-- 材料成本：40 单位任意金属（钢、玻璃钢、铀……），由玩家选材 -->
    <costStuffCount>40</costStuffCount>
    <stuffCategories>
      <li>Metallic</li>                                <!-- StuffCategoryDef 取值：Metallic / Woody / Stony / Fabric / Leathery / Bioferrite -->
    </stuffCategories>

    <statBases>
      <WorkToMake>9000</WorkToMake>                    <!-- 制作工作量（tick）；60 tick = 1 秒 -->
      <Mass>1.2</Mass>                                 <!-- 重量 kg，匕首比长剑轻 -->
      <MaxHitPoints>180</MaxHitPoints>                 <!-- 耐久度 -->
      <Flammability>0</Flammability>                   <!-- 可燃性 0~1，等离子武器不该被烧掉 -->
    </statBases>

    <equippedAngleOffset>-55</equippedAngleOffset>      <!-- 手持贴图倾角；原版近战常见 -55 ~ -65 -->

    <weaponTags>
      <li>{{YourPrefix}}_PlasmaMelee</li>            <!-- 松散标签，供 AI 配装/贸易筛选，可自定义 -->
    </weaponTags>

    <!-- 战斗数值：匕首只有一个攻击面 -->
    <tools>
      <li>
        <label>point</label>                           <!-- 战斗日志里显示的部位名 -->
        <capacities>
          <li>Stab</li>                                <!-- ToolCapacityDef 合法值：Blunt / Cut / Stab / Poke / …；想偏切割可改 Cut，或与 Stab 并列 -->
        </capacities>
        <power>18</power>                              <!-- ★ 基础伤害 = 18 -->
        <cooldownTime>1.2</cooldownTime>               <!-- ★ 攻击冷却（秒）= 1.2 -->
        <armorPenetration>0.3</armorPenetration>       <!-- 穿甲 0~1；原版仅 8 处使用（0.4%），嫌强就删掉或降到 0.15 -->

        <!-- 可选：等离子灼烧，要用就取消注释。字段路径已核对（额外伤害/li/def、amount、chance），原版仅 7 处使用，
             样例 def 为 EMP / Flame / Stun，chance 样例 0.5 / 0.7；原版没有可逐字对照的近战武器实例，属按字段表写出的写法。
        <extraMeleeDamages>
          <li>
            <def>Flame</def>
            <amount>6</amount>
            <chance>0.5</chance>
          </li>
        </extraMeleeDamages>
        -->
      </li>
    </tools>

    <graphicData>
      <texPath>Things/Item/Equipment/WeaponMelee/{{YourPrefix}}_PlasmaDagger</texPath>
      <graphicClass>Graphic_Single</graphicClass>       <!-- 单张图必须 Graphic_Single；Graphic_Random 会报 No textures found at path -->
      <shaderType>CutoutComplex</shaderType>
    </graphicData>
    <uiIconScale>1.2</uiIconScale>                      <!-- 图标缩放，>1 放大 -->

    <recipeMaker>
      <researchPrerequisite>Smithing</researchPrerequisite>  <!-- 已验证存在的原版研究；想做后期武器就换成你自己的 ResearchProjectDef defName -->
      <skillRequirements>
        <Crafting>8</Crafting>                          <!-- 最低制作技能 0~20 -->
      </skillRequirements>
      <workAmount>9000</workAmount>                     <!-- 与 statBases/WorkToMake 保持一致 -->
      <displayPriority>420</displayPriority>            <!-- 制造菜单里的排序 -->
    </recipeMaker>
  </ThingDef>
</Defs>
```

## 二、你给的三项参数分别落在哪

| 你的要求 | 写进哪个字段 | 本次取值 | 说明 |
|---|---|---|---|
| 近战武器 | `ParentName="BaseMeleeWeapon_Sharp_Quality"` | — | 已继承武器分类、Comps、品质、默认锻造台，不需要重复写 |
| 伤害 18 | `tools/li/power` | 18 | 近战伤害只认这里；写成远程的 `verbs` 不会生效 |
| 冷却 1.2 秒 | `tools/li/cooldownTime` | 1.2 | 与 `power` 必须成对写（原版 498 处工具两条都写） |
| 科技等级（你要的那档） | `techLevel` | `Ultra` | 枚举里只有 Ultra，没有带 tech 后缀的写法 |

顺带一个强度参照：18 ÷ 1.2 ≈ **15 伤害/秒**；模板库记录的原版长剑（MeleeMedieval.xml 的长刃）是 power 18 / cooldownTime 2.6 ≈ 6.9 每秒——你这把是 Ultra 级的快刀。觉得太强，最省事的旋钮就是 `cooldownTime`（调到 1.6 就接近 Spacer 级手感）。

## 三、目录结构与贴图

```
<RimWorld 安装目录>/Mods/PlasmaDaggerTest/
├── About/
│   └── About.xml                                   # 见第四节
├── Defs/
│   └── ThingDefs/Weapons_PlasmaDagger.xml           # 上面那段 XML
├── Textures/
│   └── Things/Item/Equipment/WeaponMelee/{{YourPrefix}}_PlasmaDagger.png
└── Languages/                                       # 可选，见第六节
    └── ChineseSimplified/DefInjected/ThingDef/Weapons_PlasmaDagger.xml
```

**贴图要求**：PNG，**128×128**（原版武器图标就是这个尺寸），内容**水平放置**——原版武器贴图一律水平绘制，游戏里的倾角由 `equippedAngleOffset` 控制，预先旋转 45° 会转两次。texPath 不写 `Textures/` 前缀、不写 `.png` 后缀，大小写必须与文件名逐字一致（Linux/macOS 上敏感）。贴图必须原创，不要用第三方 IP 的素材。

## 四、About.xml（测试版）

```xml
<?xml version="1.0" encoding="utf-8"?>
<ModMetaData>
  <packageId>test.{{YourModName}}</packageId>        <!-- 测试版带 test. 前缀，正规化时去掉 -->
  <name>Plasma Dagger (Test)</name>                  <!-- 测试版命名，方便快速迭代 -->
  <author>{{YourAuthor}}</author>
  <supportedVersions>
    <li>1.7</li>                                     <!-- 目标版本 RimWorld 1.7 -->
  </supportedVersions>
  <description>一把以约束等离子为刃的近战匕首：伤害 18，冷却 1.2 秒，Ultra 级科技。
测试版：正式发布前需按「测试版先行」流程正规化。

[AI 辅助生成]</description>
</ModMetaData>
```

## 五、进游戏怎么测（测试版先行）

1. 把 `PlasmaDaggerTest/` 放进 RimWorld 的 `Mods/` 目录，启动游戏，在 Mod 列表里勾选它。
2. 开开发者模式（选项 → 开发者模式）→ 顶栏 Debug Actions → **Spawn Thing** → 搜你的 defName。
3. 逐项确认：贴图正常显示（不是紫块）/ 日志无红字 / 装备后在角色面板确认伤害 18、冷却 1.2 / 战斗日志里的部位名是 `point`。
4. 制造链路验证：研究完 Smithing 后到锻造台看配方（制造台由父类 recipeMaker 提供）；配方若没出现，再在 `recipeMaker` 里显式补 `<recipeUsers><li>ElectricSmithy</li></recipeUsers>`。
5. 结果反馈给我：没问题就说「可以正规化」，我按正规化流程清理 packageId、补全 About.xml、替换正式贴图；有红字就把日志贴给我。

## 六、可选增强（要哪个说一声）

- **等离子灼烧**：给工具加额外伤害，示意代码已注释在上面的 XML 里（`def` / `amount` / `chance` 三个字段都在 1.7 字段表里）。加完先跑一次确认无红字再保留。
- **中文名**：`Languages/ChineseSimplified/DefInjected/ThingDef/Weapons_PlasmaDagger.xml`，元素名用 `你的defName.label` 这种形式（注意：大括号不是合法的 XML 名称字符，所以不能把 `{{YourPrefix}}` 直接写进元素名）：

```xml
<?xml version="1.0" encoding="utf-8"?>
<LanguageData>
  <!-- 把 YOURDEFNAME 换成你最终的 defName，例如 ABC_Weapon_PlasmaDagger -->
  <YOURDEFNAME.label>等离子匕首</YOURDEFNAME.label>
  <YOURDEFNAME.description>以约束等离子为刃的匕首，切甲如布。</YOURDEFNAME.description>
</LanguageData>
```

  1.7 里语言目录名用短名 `ChineseSimplified` 或带括号的 `ChineseSimplified (简体中文)` 都能加载，两个都放可以做兜底。
- **做成后期科技**：把 `researchPrerequisite` 换成你自己新建的 `ResearchProjectDef`，别用原版中期研究。

## 落盘时我会做的事

拿到你的前缀 / namespace / packageId / 作者后，我会：填好全部占位符 → 在 `<RimWorld>/Mods/PlasmaDaggerTest/` 下落 `About/About.xml` 与 `Defs/ThingDefs/Weapons_PlasmaDagger.xml` → 生成一张 128×128 的原创占位贴图（正式贴图建议你自己画）→ 把测试步骤再给你一遍。发布到创意工坊要等测试通过正规化之后，且 Steam 页面描述里也要标注「本 Mod 部分内容由 AI 辅助生成」。
