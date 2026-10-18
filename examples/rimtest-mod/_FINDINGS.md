# 技能缺陷账本（测试 mod 暴露的「文档 vs 1.7 现实」冲突）

> 由端到端测试过程中各线汇报汇总，最终用于修正 rimworld-modding 技能。每条都要能落到具体文件与行。

## 来源：线 C（贴图）— 2026-10-18

### F1 技能头部版本陈述过时（高）
- SKILL.md 头部 compatibility 仍写 **RimWorld 1.6 / Unity 2022.3.35 / .NET Framework 4.7.2+**。
- 实测：RimWorld **1.7.4981 rev136**；Unity **已被移除**（全盘无 UnityEngine*.dll，WaylithClr 把 UnityEngine* 重定向到 UnityStubs 存根）；`RimWorld.runtimeconfig.json` → tfm **net10.0**。
- 动作：SKILL.md frontmatter 与正文版本陈述 1.7 化；references/01-environment.md 同步。

### F2 原版贴图核验路径在 1.7 失效（高）
- 技能文档隐含「去 `Data\Core\Textures\...` 看原版贴图」。实测 **1.7 的 Data\Core 下没有 Textures 目录**（只有 About / Defs / Languages / Shaders）。
- 原版贴图全部打包在游戏根 **Assets.zip**（358,892,126 B）内，前缀 `Resources/Textures/...`，命名规则是「原文件名 + 再追加 `.dds`」（例：`AssaultRifle.png.dds`、`FlakJacket_male_south.psd.dds`），用 **Zstd（ZIP method 93）** 压缩。
- 后果：`python zipfile` 直接报 `That compression method is not supported`；Python 3.12 的 zlib **不支持 zstd**。可行路径：**Node 24 的 `zlib.zstdDecompressSync`** + 手写 ZIP 中央目录解析（本测试的实际做法），再用 Pillow 读 BC3/DXT5。
- 动作：技能里凡「查原版贴图」的步骤都要改写；补一节 1.7 资源解析（Assets.zip + .png.dds 命名 + Zstd 解包）。

### F3 贴图尺寸建议三套数值互相矛盾（中）
- `references/07-assets.md` 建议 1×1 建筑 = **256×256**；本测试规格定 128×128；原版对应物 `CraftingSpot`（1×1 生产建筑）实测 **64×64**。
- 动作：07-assets.md 的尺寸表要以 1.7 原版实测值重写，并说明「texPath 尺寸不强制，但与原版同量级更稳」。

### F4 原版没有 `Things/Item/Equipment/Apparel/` 这个目录（中）
- 实测 1.7 原版 `Things/Item/Equipment/` 下只有 `Special`、`WeaponMelee`、`WeaponRanged`。
- 原版服装物品图标一律在 `Things/Pawn/Humanlike/Apparel/<Name>/<Name>`（同一目录兼作物品图标与穿戴图）。
- 技术上自定义 texPath 可用（本测试即如此），但技能文档应给出原版惯例写法，避免学习者写出非惯例结构。

### F5 原版穿戴贴图按体型分文件，技能未提（中）
- 原版 `FlakJacket` 目录 16 个条目全是 `_male_/_female_/_thin_/_fat_/_hulk_` × 四向，**没有裸的 `FlakJacket_south`**。
- 只做一套通用四向图时，靠 `ApparelGraphicRecordGetter` 在缺失体型文件时回退到基础路径生效 ⇒ 所有体型共用一张、外观无差异（测试 mod 可接受）。
- 动作：07-assets.md 补「体型后缀规则」一节，讲清「一套通用图」与「逐体型图」的差别与代价。

### F6 武器贴图方向误解（中）
- 常见误解「武器要画成 45° 斜的」（线 C 首版即如此，已返工）。
- 实测原版 `Gladius.png.dds` bbox(0,50,128,71)（水平薄带）、`AssaultRifle.png.dds` bbox(0,49,128,98)（水平横跨全宽）⇒ **武器贴图画成水平**，斜置是 PawnRenderer 运行时旋转。
- 动作：07-assets.md 明确写这条，并加一句「不要在 XML/C# 里给武器加旋转设置」。

### F7 技能缺 Assets.zip 层（高，与 F2 同源）
- 技能全文没有 Assets.zip 这一层，也没有 `.png.dds` 命名规则。1.7 的 mod 也可以自带 Assets.zip（实测工坊 mod 条目形如 `Textures/Mint/UI/Accuracy.png.dds`），但纯 `Textures/*.png` 仍可用（至少 4 个支持 1.7 的工坊 mod 这么用）。

### 线 C 的实测参照值（供技能文档 1.7 化时引用）
- `FlakJacket.psd.dds` 128×128 bbox(0,4,128,127)；`Gladius.png.dds` 128×128 bbox(0,50,128,71)；`AssaultRifle.png.dds` 128×128 bbox(0,49,128,98)
- `Naked_Male_south` 躯干 x38..89 / y40..107（肩线 y≈44、下摆 y≈104）；`Naked_Male_east` 侧视 x42..89
- `FlakJacket_male_south` 中段不透明 x33..93；`CraftingSpot.psd.dds` 64×64；`Steel_a.psd.dds` 64×64 bbox(0,18,64,48)；`Bullet_Small.psd.dds` 64×64 bbox(0,10,64,64)；`RoseA.psd.dds` 64×64
- 结论：穿戴贴图 128 画布、躯干占 x≈34..94 窄中段；图标类 64×64。

### 线 C 未核实项（如实记录）
- 穿戴背心与人物躯干的像素级对位（轮廓取 x34..94 / y42..106，比原版略宽 1px）未经真机肉眼验证。
- 未生成 `_m` 遮罩（规格未要求）。
- 未核实 1.7 对 texPath 解析是否有额外限制。
- About\Preview.png 是否随组装进 `examples\rimtest-mod\` 与 `Mods\RimTestMod\` 属 Lead 组装动作。
## 来源：线 B（C# / Harmony 编译）— 2026-10-18

### F8 技能「版本注意」三件套在 1.7 全为假（高）
- `.NET Framework 4.7.2+` → 实际 **net10.0**（`RimWorld.runtimeconfig.json` 的 tfm）。
- `Unity 2022.3.35` + `UnityEngine.CoreModule.dll` → 实际 **UnityStubs.dll 兼容层**，游戏根目录 `*UnityEngine*` **零命中**。
- `<RimWorld>\RimWorldWin64_Data\Managed\` → **目录不存在**，DLL 全在游戏根目录。
- `游戏自带 0Harmony` → **游戏本体不带**；需从 Harmony mod（工坊 2009463077）1.7\Assemblies\0Harmony.dll 取，自带旧版会触发 HarmonyMod 告警并降级。
- 动作：references/01-environment.md、references/05-csharp-basics.md、references/06-harmony.md 全面 1.7 化。

### F9 1.7 API 与技能/教程示例不符（高，逐条已实测）
- `dinfo.Amount = x` → **编不过**（只读）；唯一途径 `dinfo.SetAmount(float)`。
- `Messages.Message(text, thing, def)` → 第二参是 **LookTargets**，不是 Thing。
- `RimWorld.Command_Action` → **不存在**，正确类型是 `Verse.Command_Action`。
- 「`RimWorld.` 前缀的类型在 RimWorld.dll」→ **不成立**：`RimWorld.MessageTypeDefOf` 实际在 **Assembly-CSharp.dll**。
- Harmony **3.0**：`HarmonyMethod` **无 patchId**、`Patch()` 无 ID 参数，改用 category + switch；技能 harmony-patch.cs 模板里的 patchId 写法需改。
- `csc -version` = 打印编译器版本并退出，exit 0 但零产物（踩坑记录）。
- 动作：05-csharp-basics.md / 06-harmony.md 补「1.7 API 差异 + 如何用元数据探针核对签名而不是凭记忆」；harmony-patch.cs 模板同步。

### 线 B 的实测证据链（可复现）
- 自建元数据探针 docs\_lineB-tools\SigProbe（net10.0，真反射）逐条读 Assembly-CSharp.dll / 0Harmony.dll 真实签名。
- 产物 AssemblyRef 表：RimTestMod.dll → System.Runtime, Assembly-CSharp（**无 0Harmony、无 UnityStubs**，即「Harmony 缺失时主程序集仍能加载」的硬证据）；RimTestMod.Patches.dll → System.Runtime, Assembly-CSharp, UnityStubs, 0Harmony, RimTestMod。
- build.ps1 两条路径均 exit 0（dotnet SDK 10.0.401 默认路径产物 11,776 B / 12,800 B；`-UseCsc` 路径 11,264 B / 12,288 B）。
- Assemblies\ 反向检查：只有本 mod 两个 .dll，无游戏 DLL、无 0Harmony.dll、无 .deps.json。

### 线 B 未核实项（如实记录）
- 补丁运行时是否真生效（禁止启动游戏，只到「编译通过 + 目标签名元数据核对」）。
- 0Harmony 3.0 针对 .NET 8 引用框架编译（csc 路径报 CS1701），与 net10.0 运行时是否漂移未验证（游戏 LaxAssemblyBinding=true）。
- `DamageWorker.DamageResult` 是 class 还是 struct 未实测，故 ThingTakeDamagePatch 刻意不声明 `__result`。

### 跨线需求（线 A 未交付前由 Lead 兜底）
- 4 个 Keyed 键必须存在于 `Languages\ChineseSimplified\Keyed\`：`DM_TestShield_Inspect`（含 {0}/{1}/{2}）、`DM_TestShield_Depleted`、`DM_TestShield_GizmoRefillLabel`、`DM_TestShield_GizmoRefillDesc`；否则游戏内显示键名原文。
- `DM_Apparel_TestVest` 的 `<comps>` 必须写 `<li Class="Demo.RimTestMod.CompProperties_TestShield"><shieldCapacity>50</shieldCapacity></li>`。

## 来源：Lead 端到端核验（技能自身）— 2026-10-18

### F10 技能自带的 XML 模板全部不是合法 XML（P0，已修）
- 症状：`assets/templates/` 下 8 个 .xml 中 **7 个解析失败**（Python ElementTree 与 .NET XmlDocument 双向复现）。两类缺陷：
  1. 元素文本里写尖括号占位符：`<defName><YourPrefix>_Weapon_<YourName></defName>`（.NET 报 `The 'YourName' start tag on line 17 position 35 does not match the end tag of 'defName'`），`<label><your weapon label></label>` 同类；
  2. 注释体里出现 `-` 连字符 runs：`plant.xml` 的分隔线注释（.NET 报 `An XML comment cannot contain '--', and '-' cannot be the last character. Line 16, position 3`）。
- 后果：SKILL.md 承诺「有模板 → 直接用（免核验）」，但把模板原样拷进 mod 会让 RimWorld 加载 Def 直接失败——这条承诺在修复前是错的。
- 修复：占位符统一为 `{{YourXxx}}`（含 `<your weapon label>`→`{{YourWeaponLabel}}` 这类 CamelCase 转换）；注释里除上述两类形态外一律不动，`-` runs 换成等量 `=`。
- 机械化防复发（这是本条真正的产出）：新增 `scripts/xml-lint.mjs`（`xmlProblems(src)` 零依赖良构扫描）+ `tests/test-xml-lint.mjs`（12/12 通过，两个历史缺陷当固定样本）+ `check-index.mjs` 新增第 6 项校验「XML 模板必须良构」+ CI 新增 step「XML 模板良构性」。
- 约定（已写进 SKILL.md:116）：模板里的用户自定义值一律用 `{{YourXxx}}`，**不许写尖括号形式**。

## 来源：线 A（XML Def）交付后的 Lead 复核 + 端到端核验 — 2026-10-18

### F11 `techLevel` 合法值表缺 `Ultra` 与 `Animal`（中）
- 技能 `assets/templates/weapon-melee.xml` 与 `references/03-xml-defs.md` 的 techLevel 说明只纠正了「没有 Ultratech」，没给出完整枚举。
- 实测（反射 `Assembly-CSharp.dll` 的 `RimWorld.TechLevel`）：`Undefined / Animal / Neolithic / Medieval / Industrial / Spacer / Ultra / Archotech`。
- 原版 1.7 全库取值分布（含 DLC）：Industrial 110、Spacer 60、Neolithic 40、Medieval 23、**Ultra 13**、Archotech 10、**Animal 2**。
- 动作：03-xml-defs.md 写全枚举 + 分布；模板注释同步（Ultra 级近战武器即「等离子/单分子」那一档）。

### F12 远程武器「顶层 rangedWeapon_* / warmupTime / range / verbClass」在 1.7 全部无效（高）
- 1.6 模板写法（顶层 `<rangedWeapon_Cooldown>`、`<warmupTime>`、`<range>`、`<verbClass>`）在本版本不生效。
- 1.7 真实结构：冷却 = `statBases/RangedWeapon_Cooldown`；射程/预热/弹丸/音效 = `verbs/li{verbClass, warmupTime, range, defaultProjectile, soundCast, soundCastTail, muzzleFlashScale}`；命中率 = `statBases/AccuracyTouch|Short|Medium|Long`。
- 证据：`Core/Defs/ThingDefs_Misc/Weapons/RangedSpacer.xml:5`（Gun_ChargeRifle）与 `RangedIndustrial.xml:20`（Gun_Revolver）全文比对；字段表里顶层 `rangedWeapon_Cooldown` 命中率 0。
- 动作：重写 `assets/templates/weapon-ranged.xml`；03-xml-defs.md 的远程武器条目改结构。

### F13 配方产物是「字典写法」，1.6 模板的 `products/li/thingDef+count` 是错的（高）
- 1.7 正确形态：`<products><产物defName>数量</产物defName></products>`。
- 证据：原版 `Data` 全库 50 个含 `products` 的 RecipeDef 块全是这个形态（如 Anomaly `ExtractBioferrite` 的 `<Bioferrite>15</Bioferrite>`）；字段表里 `products/li/thingDef`、`products/li/count` 路径不存在。
- 附带：材料决定的产物（`costStuffCount` 类）手写配方必须显式写 `productHasIngredientStuff=true`，否则产物不继承输入材料（字段名存在于 DLL 元数据 UTF-8 名表偏移 12707852，但原版 XML 0 处使用——因为那类配方由 `RecipeDefGenerator` 在代码里生成）。
- 动作：重写 `assets/templates/recipe.xml`；03-xml-defs.md 配方条目改写 + 增加 `productHasIngredientStuff` 说明。

### F14 建筑模板缺工作台两件套，且提到的字段不存在（中）
- 1.7 工作台必须：`thingClass=Building_WorkTable`（原版 17 处用法）+ `inspectorTabs/li=ITab_Bills`（不然没有「账单」页）。
- `filthAffordance` 在 1.7 **不存在**；建筑工作量字段是 `statBases/WorkToBuild`（没有小写 `workToBuild`）；可被设施加成 = `comps/li Class="CompProperties_AffectedByFacilities"`（原版 25 处）+ `linkableFacilities/li`。
- **归属更正（复核时查实）**：`filthAffordance` 与 `apBodyPartGroups` 这两处"错字段"**不是技能正文写的**——技能 `references/03-xml-defs.md` 里 0 处出现这两个词。它们出自模板库 `library/02-模板/02-物品线/03-ThingDef-建筑.md:7,241,252` 与 `02-ThingDef-衣物.md:7,205,275`，而那份库恰恰是在"**先纠正常见误写**"（明确写着"字段表里不存在 filthAffordance / apBodyPartGroups / 顶层 bodyPartGroups"）。所以技能的缺口只是**没把这类负结论写进去**，不是写错了字段名。
- 动作：重写 `assets/templates/building.xml`。

### F15 服装字段：`apBodyPartGroups` / 顶层 `bodyPartGroups` / `ApparelTagDef` 三处都不成立（中）
- 1.7 只有 `apparel/bodyPartGroups/li`（Torso/Neck…）。
- **没有 `ApparelTagDef` 这个 Def 类型**：`apparel/tags`、`defaultOutfitTags` 是自由字符串列表（原版值例：IndustrialBasic、Soldier、Worker、BasicClothing）。
- `wornGraphicPath`（String）与 `wornGraphicPaths`（List）并存。**数字更正（复核时重数）**：1.7 字段表里 `apparel/wornGraphicPath` 5.1%（104/2054）为文本路径、`apparel/wornGraphicPaths` 0.1%（2/2054）为容器；原版 `Data` 全库 `<wornGraphicPath>` 标签 **131 处**（含 ThingStyleDefs 内的引用）。先前报告中"原版 13 处"是漏数。
- 动作：`assets/templates/apparel.xml` 与 03-xml-defs.md 服装条目修正。

### F16 补丁操作：`PatchOperationSet` 在 1.7 不存在；`PatchOperationInsert` 的 xpath 语义有坑（高）
- `references/04-xml-patching.md` 提到 `Verse.PatchOperationSet` —— 1.7 没有这个类型（只有 `PatchOperationAttributeSet`）。
- 补丁节点名是 `<Operation>`，具体类型由 **`Class` 属性**决定（`DirectXmlToObject.ClassTypeOf` 对字面量 "Class" 特判）。
- `PatchOperationInsert` 把 `value` 插成**匹配节点的兄弟节点**（`<order>Prepend/Append</order>` 决定前后），所以 xpath 必须指向列表里已存在的某个节点；本测试首版写 `/tools`（容器），运行时会变成把 `<li>` 插到 `<ThingDef>` 直接子级 ⇒ 字段错误。已改为 `/tools/li[1] + <order>Prepend</order>`。
- `PatchOperationAdd` 指向列表容器（`/weaponTags`）是正确的、也是原版惯例。
- `<recipeUsers Inherit="False">`（Gun_ChargeRifle）证明**列表节点默认是追加语义**，要整段替换必须 `Inherit="False"`。
- 动作：04-xml-patching.md 增加「1.7 补丁操作真实清单 + Insert 语义 + Inherit 语义」一节。

### F17 `Graphic_Random` / `Graphic_Collection` 需要目录形态贴图（中）
- 证据：`Assembly-CSharp.dll` 内含字符串 `Collection cannot init`（UTF-16 偏移 6949450）与 `No textures found at path`（偏移 6949474）；原版装饰植物 `Plant_Rose`/`Plant_Daylily` 用 `Graphic_Random` 且贴图是目录形态（`Things/Plant/Rose/*.png`）。
- 本测试的植物按 texPath 契约只有一张平铺 PNG ⇒ 已把 `graphicClass` 从 `Graphic_Random` 改成 `Graphic_Single`。
- 动作：07-assets.md 与 03-xml-defs.md 补「单图必须 Graphic_Single」这类对应关系。

### F18 语言目录名规范缺失（中，实测数据已取）
- 1.7 的 `Core/Languages` 下只有 English 是实体目录，其余 28 种是 `.tar`（`ChineseSimplified (简体中文).tar`），tar 内 LanguageInfo.xml 没有 `folderName` 字段 ⇒ **语言身份 = 目录名**。
- 本机 136 个创意工坊 mod 实测：短名 `ChineseSimplified` **43** 个、带括号 `ChineseSimplified (简体中文)` **18** 个；两种目录里都**没有** `LanguageInfo.xml`；声明支持 1.7 且用短名的至少 4 个（1446523594 / 1662119905 / 1701592470 / 2113372560）⇒ 两种写法都合法。
- 本测试的做法：两种目录同时提供、内容逐字相同，并让 TESTING.md 的 L2 实验判定本机实际加载哪一个。
- 动作：SKILL.md 与 references/02-project-structure.md 增加语言目录一节，写明「目录名 = 语言身份」「两种合法写法」「Keyed / DefInjected/<DefType>/ 结构」。

### F19 原版近战武器的 recipeMaker 各自独立（参考信息，非缺陷）
- `BaseMeleeWeapon` 给了默认 recipeMaker（电炉/燃油炉 + UnfinishedWeapon），但原版 Gladius/LongSword/Mace **各自重写** recipeMaker（例：Gladius 为 `researchPrerequisite Smithing` + `skillRequirements/Crafting 3` + `displayPriority 410`）。
- 含义：想让武器进「锻造台 + 研究前置」体系，要在自己的 Def 里写 recipeMaker，而不是指望继承。

### F20 自动配方与双入口去重（参考信息，非缺陷）
- `ThingDef/recipeMaker` 会由 `RimWorld.RecipeDefGenerator.DefsFromRecipeMakers` 生成对应 RecipeDef；`ThingDef.AllRecipes` = `<recipes>` ∪ `recipeUsers` 含本 def 的配方，并用 `List.Contains` 去重 ⇒ 建筑 `<recipes>` 与 RecipeDef `recipeUsers` 指向同一配方**不会**出现重复账单（本测试两条配方即双入口，可直接验证）。

## 来源：Lead 组装与交付 — 2026-10-18

### 交付物位置
- 交付副本：`examples\rimtest-mod\RimTestMod\`（44 文件 / 400,182 B，逐文件 sha256 见 `examples\rimtest-mod\文件清单-sha256.txt`）
- 测试指导书：`examples\rimtest-mod\TESTING.md`；静态核验报告：`examples\rimtest-mod\核验报告.md` + `核验报告.json`
- 已安装副本：`E:\SteamLibrary\steamapps\common\RimWorld\Mods\RimTestMod\`（除下条所述的 `Source/README.md` 外，与交付副本逐字节相同）
- ⚠️ 2026-10-18 路径修复：交付副本的 `Source/README.md` 修掉 10 处指向已移除工作副本的引用，该文件随之与已安装副本里那一份不再逐字节相同；两个 `.dll`、全部 Def/贴图/本地化未变，**不影响运行时测试**（游戏不读 `Source/README.md`）。用户已于 2026-10-18 决定不同步这一份，故两副本保持该 1 处文档差异。
- 静态核验（对交付副本跑）：19 XML 良构 0 失败 / 9 Def / texPath 8 处缺失 0 / 字段路径 241 处 4 处未收录（全部预期良性）/ 错误 0 警告 4；退出码 0。

### 组装期做的两处内容修正
- 两个语言目录（短名与带括号）内容统一为**逐字相同**的 4 个文件：`DefInjected/ThingDef/DM_Weapons.xml`（11 条）、`DefInjected/ThingDef/DM_Plants.xml`（2 条）、`DefInjected/RecipeDef/DM_Recipes.xml`（4 条）、`Keyed/DM_Keys.xml`（4 键）——原先带括号目录缺植物条目。
- `Plants.xml` 的 `graphicClass` 改 `Graphic_Single`（F17）。

### 仍未核实（运行时段才能答的问题）
- 补丁运行时是否真生效、`0Harmony`（net8 引用框架）与 net10.0 运行时是否漂移。
- 语言目录哪种形态在本机实际被加载（L2 实验）。
- 穿在身上四向贴图与人物躯干的对位、植物野生生成、图标路径 `Things/Item/Equipment/Apparel/` 是否被接受。


