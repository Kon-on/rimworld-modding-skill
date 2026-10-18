# 环世界完整测试 Mod —— 共享规格（唯一契约，所有人必须遵守）

## 0. 这是什么
用 skills 仓库（<REPO_ROOT>，技能名 rimworld-modding）从零做出的一个 RimWorld mod，
目的是端到端完整测试该技能：XML Def 模板路径、无模板新类型路径、C# ThingComp、Harmony 补丁、
XML PatchOperations、贴图资源、本地化、静态核验。

## 1. 已定的命名四要素（由用户授权「看着办，给临时值」）
- 统一前缀：DM_
- C# namespace：Demo.RimTestMod
- packageId：test.rimtestmod
- 作者：占位符（发布前必须替换）
- mod 显示名：完整测试 Mod (Test)
- mod 工作目录：<REPO_ROOT>\docs\rimtest-mod

## 2. 本机 1.7 平台现实（已实测，写代码/写 XML 必须按这个来）
- 游戏：E:\SteamLibrary\steamapps\common\RimWorld，Version.txt = 1.7.4981 rev136
- 运行时：.NET 10（RimWorld.runtimeconfig.json → tfm net10.0；Microsoft.NETCore.App 10.0.13-waylithclr.dev）
- Unity 已被移除：全盘无 UnityEngine*.dll；runtimeconfig 里 WaylithClr.AssemblyNameRedirects = "UnityEngine*=UnityStubs;...;Assembly-CSharp-firstpass=UnityStubs"，UnityEngine 只剩存根（UnityStubs）。**不要写依赖 UnityEngine 具体成员的代码**。
- 游戏 DLL 在安装根目录：Assembly-CSharp.dll（14.91 MB）、RimWorld.dll、mscorlib.dll、netstandard.dll、System.*.dll、coreclr.dll、hostfxr.dll
- 旧文档里的 <RimWorld>\RimWorldWin64_Data\Managed\ **不存在**
- 游戏本体**不自带** 0Harmony.dll（全盘搜不到 *armony*）
- 原版数据：Data\{Core,Anomaly,Biotech,Ideology,Odyssey,Royalty}\**\*.xml
- 贴图：纯 Textures\ 目录在 1.7 仍可用（至少 4 个支持 1.7 的创意工坊 mod 这么用）；1.7 另有 Assets.zip 打包形态，本次不用
- 工具链：dotnet SDK 10.0.401（C:\Program Files\dotnet\sdk）；C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe

## 3. 核验源（写任何字段前必须核对，禁止凭记忆）
- 1.7 字段与模板库（首选，来自本机 1.7.4981 实测提取）：<REPO_ROOT>\library\
  - 02-模板/ 下按线分的模板（含最小真实范例）
  - 03-全量字段参考\字段总表.csv（全量字段 + 出现率）与 03-全量字段参考\字段\<DefType>.md
  - 检索命令：node "<REPO_ROOT>\scripts\find-template.mjs" --def ThingDef；--field <字段名>；--list
- 原版游戏数据（最终权威）：E:\SteamLibrary\steamapps\common\RimWorld\Data\**\*.xml
- 技能自带模板（1.6 时代，可能过时，仅作起点）：<REPO_ROOT>\assets\templates\

## 4. 文件清单与归属（文件级互斥，谁也别碰别人的文件）

### 线 A = XML（subagent 负责）
- Defs\ThingDefs\Weapons_Melee.xml → DM_Weapon_PlasmaDagger（近战武器，来自 weapon-melee.xml）
- Defs\ThingDefs\Weapons_Ranged.xml → DM_Weapon_IonRifle + 子弹 DM_Projectile_IonRifle（来自 weapon-ranged.xml）
- Defs\ThingDefs\Apparel.xml → DM_Apparel_TestVest（来自 apparel.xml，必须带 ThingComp，见第 6 节）
- Defs\ThingDefs\Items_Resources.xml → DM_Stuff_TestAlloy（材料，来自 resource-stuff.xml）
- Defs\ThingDefs\Buildings.xml → DM_Building_TestBench（来自 building.xml）
- Defs\RecipeDefs\Recipes.xml → DM_Recipe_PlasmaDagger、DM_Recipe_IonRifle（来自 recipe.xml）
- Patches\Patch_Vanilla_Weapons.xml → PatchOperations 改原版（至少用 2 种不同 Operation，例如 PatchOperationAdd + PatchOperationReplace/PatchOperationInsert）
- Languages\<照原版目录名抄>\DefInjected\ThingDef\DM_Weapons.xml 与 Keyed\DM_Keys.xml（本地化分支）

### 线 B = C#（subagent 负责）
- Source\*.cs（ThingComp，无 Harmony 依赖）
- Source\Patches\*.cs（Harmony 补丁，单独程序集）
- Source\build.ps1（可复现编译脚本）
- Assemblies\RimTestMod.dll、Assemblies\RimTestMod.Patches.dll
- Source\README.md（把 1.7 编译现实写清楚：命令、参数、引用哪些 DLL、结论）

### 线 C = 贴图（subagent 负责）
必须逐字节对上下面的 texPath（文件放在 Textures\ 下，路径去掉 Textures\ 前缀与 .png 后缀就是 texPath）：
- Textures\Things\Item\Equipment\WeaponMelee\DM_PlasmaDagger.png（128x128）
- Textures\Things\Item\Equipment\WeaponRanged\DM_IonRifle.png（128x128）
- Textures\Things\Projectile\DM_IonRifleBullet.png（32x32）
- Textures\Things\Item\Equipment\Apparel\DM_TestVest.png（128x128，物品图标）
- Textures\Things\Pawn\Humanlike\Apparel\DM_TestVest\DM_TestVest_north.png / _south.png / _east.png / _west.png（各 128x128，穿戴外观）
- Textures\Things\Item\Resource\DM_TestAlloy.png（64x64）
- Textures\Things\Building\Production\DM_TestBench.png（128x128）
- Textures\Things\Plant\DM_TestBloom.png（64x64）
- About\Preview.png（640x360）
- 另出 Textures\_MANIFEST.md 或 _MANIFEST.json：文件名、尺寸、生成方式、sha256

### 线 L = Lead（我本人负责，别人不要碰）
- About\About.xml、LoadFolders.xml
- Defs\ThingDefs\Plants.xml（DM_Plant_TestBloom，走「无模板新类型」全流程）
- 静态核验脚本 docs\verify-testmod.mjs（或 .ps1）
- examples\rimtest-mod\ 的整套组装、TESTING.md、核验报告、装到游戏 Mods\RimTestMod\

## 5. texPath 契约（XML 与贴图必须一致，谁都不许自行改名）
| Def | texPath |
|---|---|
| DM_Weapon_PlasmaDagger | Things/Item/Equipment/WeaponMelee/DM_PlasmaDagger |
| DM_Weapon_IonRifle | Things/Item/Equipment/WeaponRanged/DM_IonRifle |
| DM_Projectile_IonRifle | Things/Projectile/DM_IonRifleBullet |
| DM_Apparel_TestVest | Things/Item/Equipment/Apparel/DM_TestVest |
| DM_Apparel_TestVest（穿戴） | Things/Pawn/Humanlike/Apparel/DM_TestVest/DM_TestVest |
| DM_Stuff_TestAlloy | Things/Item/Resource/DM_TestAlloy |
| DM_Building_TestBench | Things/Building/Production/DM_TestBench |
| DM_Plant_TestBloom | Things/Plant/DM_TestBloom |

## 6. C# 契约（XML 与 C# 必须一致）
- ThingComp 类：Demo.RimTestMod.ThingComp_TestShield（继承 Verse.ThingComp）
- 属性类：Demo.RimTestMod.CompProperties_TestShield（继承 Verse.CompProperties）
- 公开可配置字段：public int shieldCapacity = 50;（XML 里用 <shieldCapacity> 配）
- 行为：吸收伤害直到容量耗尽，之后按时间恢复；状态必须用 ExposeData 正确存档读档
- XML 侧写法：DM_Apparel_TestVest 的 <comps> 里放 <li Class="Demo.RimTestMod.CompProperties_TestShield"><shieldCapacity>50</shieldCapacity></li>
- Harmony 补丁必须放在独立程序集 RimTestMod.Patches.dll 里，这样 Harmony 缺失时主程序集仍能加载
- 补丁 ID 必须唯一（例如 Demo.RimTestMod.VerbShootPatch）；补丁目标方法签名必须先用程序集元数据核验存在，不能凭记忆

## 7. 硬约束（违反即返工）
1. 不修改游戏安装目录的任何文件（最终安装副本由 Lead 统一做，别人不许写 E:\SteamLibrary）
2. 不复制原版 C# 源码；不把游戏 DLL 打进 mod；不使用第三方 IP 素材
3. 不写 examples\ 目录（那是 Lead 的收尾动作）；不写 assets\templates\（模板回写是 Lead 的活）
4. defName 必须唯一且全部以 DM_ 开头；XML 文件末尾留一个空行
5. 字段与枚举必须核对 1.7 实测数据；核对不了的，必须在报告里明确写「未能核实」而不是含糊过去
6. Defs 目录下不要用 <版本号> 子目录（本次只支持 1.7，走 LoadFolders.xml）

## 8. 汇报格式（每个人都要给）
1. 我写了哪些文件（绝对路径，逐个列出）
2. 每个产物的核验来源（读了哪个原版文件 / 哪张字段表，得出什么结论）
3. 发现的问题与「模板/文档 vs 1.7 现实」的冲突点（这条最重要，技能缺陷清单要靠它）
4. 我没能核实或不确定的地方（如实说，不要编）

## 9. 实测补充（2026-10-17 追加，覆盖规格里含糊的地方）
- 语言目录名实测：Core\Languages 下只有 English；创意工坊 mod 一律用 Languages\ChineseSimplified（不带括注后缀）。本 mod 用 Languages\ChineseSimplified\。
- LoadFolders.xml 实测格式（1504723424 等支持 1.7 的 mod）：<v1.7><li>/</li><li>1.7</li></v1.7>。本 mod 只支持 1.7，写 <v1.7><li>/</li></v1.7>。
- 植物 Def 由 Lead 负责，文件为 Defs\ThingDefs\Plants.xml（DM_Plant_TestBloom），线 A 不要碰它，也不要碰 Languages\ChineseSimplified\DefInjected\ThingDef\DM_Plants.xml。
- 实测字段核对结论（ThingDef 共 2054 个实例）：plant/growDays 3.89%、plant/lifespanDaysPerGrowDays 0.63%、plant/sowWork 0.58%、plant/sowTags 1.56%、plant/purpose 1.02%、plant/visualSizeRange 3.31%、plant/topWindExposure 2.87%、plant/growMinGlow 0.78%、plant/dieIfLeafless 0.97%、plant/harvestTag 1.36%。1.7 还有一个新字段 plant/harvestYieldAffectedByDifficulty。
