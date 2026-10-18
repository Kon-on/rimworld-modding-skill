# 完整测试 Mod —— 测试指导书

**这是给测试者（你）的手册。照着第 3 节逐项点，把结果记回每张表的「结果」列。**

| 项 | 值 |
|---|---|
| mod 显示名 | 完整测试 Mod (Test) |
| packageId | `test.rimtestmod`（测试版前缀；正式发布前须按技能「测试版先行」流程正规化） |
| 目标版本 | RimWorld **1.7**（本机 Steam 版 `1.7.4981 rev136`） |
| 已安装位置 | `E:\SteamLibrary\steamapps\common\RimWorld\Mods\RimTestMod\` |
| 交付副本 | [RimTestMod](RimTestMod)（44 个文件；逐文件 sha256 见 [文件清单-sha256.txt](文件清单-sha256.txt)） |
| 静态核验报告 | [核验报告.md](核验报告.md) 与机器可读的 [核验报告.json](核验报告.json) |
| 文档定稿时间 | 2026-10-18 |
| 作者字段 | **占位符「（待填：作者名）」——发布前必须替换** |

---

## 0. 这个 mod 在测什么

用 rimworld-modding 技能从零做一个 mod，把技能的每条分支在 1.7 上真跑一遍，看哪条走不通。

| 线 | 内容 | 对应技能机制 | 静态状态 | 运行时状态 |
|---|---|---|:--:|:--:|
| A | 6 类 XML Def（近战 / 远程 / 服装 / 材料 / 建筑 / 配方）+ 中文本地化 | 直接套 `assets/templates/` 模板，不查外部资料 | ✅ | 待测（3.1） |
| B | C# ThingComp（护盾）+ 3 个 Harmony 补丁，真实编译出 2 个 DLL | `references/05-csharp-basics.md`、`06-harmony.md` + `thingcomp.cs`/`harmony-patch.cs` 模板 | ✅ 编译 0 警告 0 错误 | 待测（3.3） |
| C | 12 张原创 PNG（4 个物品图标 + 穿戴四向 + 台面 + 材料 + 植物 + 弹丸 + Preview） | `references/07-assets.md` | ✅ 已出图、尺寸/格式自检 12/12 | 待测（3.1 各项的眼睛观察） |
| D | 无模板新类型（植物）：查原版 → 写 Def → 回写模板 → 更新索引 | SKILL.md「场景 ③」五行闭环 | ✅（已产出 `assets/templates/plant.xml`） | 待测（3.2） |
| E | 3 个 PatchOperation 改原版左轮 | `references/04-xml-patching.md` | ✅ | 待测（3.4） |
| F | 静态核验器（8 类检查，不开游戏） | 本次测试新增 `docs/verify-testmod.mjs` | ✅ 0 错 4 警（4 条都是预期良性，见 4.2） | — |

---

## 1. 本机环境事实（实测，不是抄文档）

- 游戏：RimWorld **1.7.4981 rev136**，`E:\SteamLibrary\steamapps\common\RimWorld`
- 目标框架：**net10.0**（`RimWorld.runtimeconfig.json` 里 includedFrameworks = Microsoft.NETCore.App 10.0.13-waylithclr.dev）
- 引擎：**Unity 已被移除**；全盘没有 `UnityEngine*.dll`，`WaylithClr.AssemblyNameRedirects` 把 UnityEngine\* 重定向到 UnityStubs
- 程序集位置：`Assembly-CSharp.dll`、`RimWorld.dll` 等**全在安装根目录**；老文档说的 `RimWorldWin64_Data/Managed/` **已不存在**
- Harmony：游戏**不再自带** `0Harmony.dll`，用 Harmony 的 mod 必须自己带一份（本机工坊 Harmony：`…\workshop\content\294100\2009463077\1.7\Assemblies\0Harmony.dll`）
- 贴图：纯 `Textures/*.png` 在 1.7 仍然可用；另有新的 `Assets.zip` 形态（内部条目形如 `Textures/x/y.png.dds`，Zstd 压缩）

---

## 2. 安装与启动

### 2.1 先决定要不要测 Harmony 补丁

本 mod 的两个 DLL 里，`RimTestMod.dll`（护盾 comp）**不依赖** Harmony；`RimTestMod.Patches.dll`（3 个补丁）依赖工坊 Harmony mod 提供的 `0Harmony.dll`，且**没有**把 0Harmony.dll 打进 `Assemblies/`。

- 想测 C2 / C3 的补丁部分 → 模组列表里**同时启用 Harmony**，并让它排在本 mod 前面（自动排序通常就是这个结果）。
- 只想测 XML / 贴图 / 护盾 → 可以不启用 Harmony。此时 `RimTestMod.Patches.dll` 加载会报红字，这是**预期现象**，正好用来验证「一个补丁程序集挂掉不该拖垮主 mod」。

### 2.2 步骤

1. mod 已经装好：`<RimWorld>\Mods\RimTestMod\`。（换机器时把 [RimTestMod](RimTestMod) 整个目录复制进 `Mods\`。）
2. 启动游戏 → 选项 → 模组 → 勾选「完整测试 Mod (Test)」；（测补丁的话同时勾 Harmony）。
3. 选项 → 开发者模式 → 打开；再把日志窗口打开（`~` 键 / 屏幕左上「日志」按钮），勾上自动打开。
4. 新建殖民地：任意剧本，建议 Temperate forest（要测野生植物 X8，别用极端地形）。

### 2.3 30 秒上手（最快看到东西）

开发者模式 → 顶栏「Debug actions」→ `Spawn thing` → 搜索框敲 **`test`** 或 **`plasma`**、`ion`、`alloy`、`bloom` → 依次生成等离子匕首、离子步枪、测试护盾背心、测试合金、测试花，再点 `Spawn building` 放一个测试装配台。

---

## 3. 逐项测试

> 结果列如实填：**通过 / 不通过 / 未测**。不通过时把现象原文（红字全文、defName、报错行）记下来——那才是这次测试最有价值的产出。

### 3.1 线 A：XML Def 与本地化

| # | 测试项 | 操作 | 预期（精确值） | 结果 |
|---|---|---|---|:--:|
| X1 | 近战武器「等离子匕首」 | 生成 `DM_Weapon_PlasmaDagger` | 能搜到；图标是青色匕首（128×128，**水平**朝向，不歪）；信息面板「近战攻击」= 刃 **18 伤害 / 1.2 秒**、柄 9 / 2 秒；生成时带品质标签；中文名「等离子匕首（测试）」 | |
| X1b | 材料影响（可选） | 用**测试合金**造一把匕首（或生成时选材料） | 刃伤害变成 **18 × 1.1 ≈ 19.8**（合金 `SharpDamageMultiplier` 1.1）；用钢则为 18 | |
| X2 | 远程武器「离子步枪」 | 生成 `DM_Weapon_IonRifle`，让小人装备后开火 | 图标青色步枪；信息面板：射程 **30 格**、伤害 **15**（Bullet 类型）、预热 0.8 秒、冷却 1.8 秒、**单发**；开火有枪口闪光与音效；弹丸贴图正确（不是紫块） | |
| X3 | 服装「测试护盾背心」 | 生成 `DM_Apparel_TestVest`，给小人穿上 | 能装备（躯干+颈部 / Middle 层）；四个朝向外观都正确；信息面板出现护盾行；有「补满测试护盾」按钮 | |
| X4 | 材料「测试合金」 | 生成 `DM_Stuff_TestAlloy` | 能搜到、能堆叠、能当**建造材料**（Metallic）；颜色青蓝 (56,216,232)；用它建的墙 HP ×1.6、建造工作量 ×1.8、美观 ×1.2、**不可燃** | |
| X5 | 建筑「测试装配台」 | 建造菜单 → **生产** 分类 | 出现「测试装配台」，造价 **钢 100 + 工业组件 3**，建造工作量 2000，**无研究前置**；1×1、可放、有互动格（小人站下方格）；选中后出现**「账单」标签页**；靠近工具柜时有设施连线 | |
| X6 | 两条配方 | 打开测试装配台 → 账单 → 添加 | 列表出现「制造等离子匕首（测试）」与「制造离子步枪（测试）」；技能需求 Crafting **3 / 4**；材料 = 金属类 ×50 / 钢 20+白金 40+工业组件 6；产物正确；**匕首产物继承你选的金属材料** | |
| L1 | 中文本地化 | 游戏语言设为「简体中文（中国）」，看上述物品的面板 | 名称/描述是中文（不是 `test shield vest`）；护盾行是「测试护盾：50/50（累计吸收 0 点伤害）」 | |
| L2 | 语言目录形态（重要实验） | ① 当前状态（两种目录名同时存在）看是否中文；② 把 `Languages\ChineseSimplified (简体中文)\` **移入回收站** → 重开游戏 → 再确认；③ 复原 | ①②都应显示中文。若只有 ① 显示、② 变英文，说明本机只认带括号名；反向则只认短名。**这一步决定技能该怎么写语言目录规范** | |

### 3.2 线 D：无模板新类型（植物）

| # | 测试项 | 操作 | 预期 | 结果 |
|---|---|---|---|:--:|
| X7 | 观赏植物「测试花」 | 生成 `DM_Plant_TestBloom`，或种植菜单 | 能生成/能种；**1.5 天**成熟；光照 ≥0.3 才长；成熟后有美观度；可割除；**日志无** `No textures found at path` / `Collection cannot init` | |
| X8 | 野生生成 | 新开地图后到处看看 | 地图上应有野生测试花（`wildOrder` 1） | |

### 3.3 线 B：C# 与 Harmony

| # | 测试项 | 操作 | 预期（精确值） | 结果 |
|---|---|---|---|:--:|
| C1 | 护盾 ThingComp 生效 | 给小人穿背心，然后挨打（或开发者工具 `Damage thing`） | 无 `Could not find type` 红字；面板显示「测试护盾：50/50（累计吸收 N 点伤害）」；受击时**护盾先吸收**、数字下降；耗尽时飘字「测试护盾被打破了！」；再受击才掉血 | |
| C1b | 恢复与 Gizmo | 等一会儿，点「补满测试护盾」 | 护盾随时间自动回复；按钮点了立刻回满 50 | |
| C2 | 3 个 Harmony 补丁生效 | ① 用离子步枪打一枪 → ② 用开发者工具伤害测试装配台 → ③ 看日志 | ① 出现两行（`Projectile.Launch` / `Projectile.Impact`，含 `DM_Projectile_IonRifle`、伤害 15）；② 出现一行 `Thing.TakeDamage 补丁命中：DM_Building_TestBench 血量 <前> → <后> 伤害=<n> 类型=<Def>`；③ 无 Harmony 异常栈 | |
| C3 | 程序集加载 | 看日志窗口头部 | 启用 Harmony 时应有：`[RimTestMod.Patches] 0Harmony = …`、3 行 `已打补丁 …`、若干行 `Harmony 自报已修补：…`、一行 `补丁引导结束：成功 3 / 失败 0 / Harmony 自报 3`；未启用 Harmony 时只有一条红字，**主 mod 的 XML 与护盾仍工作** | |
| S1 | 存档 / 读档 | 让护盾掉一点（别回满）→ 存档 → 读档 | 护盾点数与累计吸收值**保持读档前的值**（不会回满）；无读档报错 | |

### 3.4 线 E：原版补丁

| # | 测试项 | 操作 | 预期 | 结果 |
|---|---|---|---|:--:|
| P1 | 三个操作都打到原版左轮 `Gun_Revolver` | 生成一把左轮，看信息面板 | ① 远程冷却 **1.6 → 1.4 秒**；② 近战攻击列表**最前面**多一条「枪托」Blunt 9 / 2 秒（原版自带的是 grip/barrel）；③ `weaponTags` 里多了 `DM_Patch_TestTag`（游戏内不可见，用开发者工具的 def 检查器看，看不到就标「未测」） | |

---

## 4. 静态核验（不用开游戏，可随时复现）

### 4.1 怎么跑

```powershell
node docs/verify-testmod.mjs --mod "examples\rimtest-mod\RimTestMod" --out "examples\rimtest-mod\核验报告.json"
```

检查 8 类问题：XML 良构 / defName 唯一且带前缀 / ParentName 与 defName 引用可解析 / texPath 贴图存在 / 字段路径对照 1.7 字段总表 / 枚举值 / Patch 结构与 xpath / XML 里引用的自定义 C# 类型在 DLL 中存在。有 error 时退出码 1。

### 4.2 本次结果（对**交付副本**跑，2026-10-18）

| 检查 | 结果 |
|---|---|
| [1] XML 良构 | 19 个文件解析，**0 失败** |
| [2] Def | 9 个（含 2 条配方），defName 唯一、全部 `DM_` 前缀 |
| [3] 原版索引 | 1560 个 XML / 12415 个 defName+Name |
| [4] texPath | 8 处引用，**缺失 0 处** |
| [5] 字段路径 | 241 处，字段表未收录 4 处（见下） |
| [7] Patch | 1 个文件，用到 PatchOperationReplace / Add / Insert |
| [8] DLL 与自定义类型 | 2 个 DLL 存在；XML 引用的自定义类型命中 |
| 合计 | **错误 0 项，警告 4 项，退出码 0** |

4 条警告都是**预期良性**：

1. `productHasIngredientStuff` —— 字段真实存在于 DLL 元数据，但原版 XML 0 处使用（`costStuffCount` 类配方由代码生成器自动处理），所以字段表里没有它；
2. `products/DM_Weapon_PlasmaDagger`、3. `products/DM_Weapon_IonRifle` —— 1.7 的 `products` 是「**子元素名 = 产物 defName**、元素值 = 数量」的字典写法，字段表无法预先枚举任意 defName；
4. `comps/li/shieldCapacity` —— 本 mod 自定义 comp 的属性，字段表只收原版字段。

---

## 5. 失败现象 → 排查路径

| 现象 | 首先做什么 |
|---|---|
| 搜不到 defName | 确认 XML 在 `Defs/` 下且良构（先跑 4.1 的核验器）；确认 `LoadFolders.xml` 里 `<v1.7><li>/</li></v1.7>`；确认 mod 已勾选 |
| 红字 `Could not find parent` | ParentName 写错或原版改名 —— 用原版 XML 的 `<ThingDef Name="…">`（抽象 def 用 `Name`）核对，7 个父 Def 分别是 `BaseMeleeWeapon_Sharp_Quality`、`BaseBullet`、`BaseHumanMakeableGun`、`ApparelMakeableBase`、`ResourceBase`、`BenchBase`、`PlantBase` |
| 贴图空白 / 紫块 | texPath 与 `Textures/` 下相对路径不一致（不带扩展名、大小写敏感）；穿在身上的贴图走 `apparel/wornGraphicPath`，按体型分文件（`_male_/_female_/_thin_/_fat_/_hulk_`），本 mod 只提供不分体型的一套 |
| 植物报 `No textures found at path` | `Graphic_Random`（和 `Graphic_Collection` 系）要求 texPath 是**目录**、目录下有多张贴图；单张平铺 PNG 必须用 `Graphic_Single` |
| C# 类型找不到 | `Assemblies/` 里有 DLL；XML 里 `Class` 写的是**全名**（`Demo.RimTestMod.CompProperties_TestShield`）；目标框架 net10.0 |
| Harmony 报错 / 补丁没装 | 需要工坊 Harmony mod 提供 `0Harmony.dll` 并排在前面；日志里对照 `补丁引导结束：成功 N / 失败 M`，失败 0 但补丁不生效就看目标签名是否随版本变了 |
| 启动即崩 | 先禁用本 mod 确认游戏本体正常，再逐条启用（XML → 主 DLL → Harmony 补丁） |

---

## 6. 本次测试已经暴露的技能缺陷（静态阶段已确认）

> 完整账本在 `examples\rimtest-mod\_FINDINGS.md`；下面是与 1.6 老文档冲突、且本次已在 1.7 上取到证据的部分。
>
> **状态更新（2026-10-18）**：下表 15 条已全部回改进技能本体，随 **技能 1.2.0** 发布（见 `CHANGELOG.md` 的 1.2.0 节、
> `learnings/errors.txt` 的 2026-10-18 记录）。本节保留为"当时发现了什么"的证据；如果你现在读技能文档，看到的应该已是修正后的 1.7 写法。

| # | 技能里怎么写的（1.6） | 1.7 现实（证据） |
|---|---|---|
| 1 | 目标版本 1.6、Unity 2022.3.35、.NET Framework 4.7.2 | 1.7 是 net10.0 + UnityStubs（`RimWorld.runtimeconfig.json`、全盘无 `UnityEngine*.dll`） |
| 2 | 游戏 DLL 在 `RimWorldWin64_Data/Managed/` | 1.7 **没有**这个目录，DLL 在安装根目录 |
| 3 | 原版贴图在 `Data/Core/Textures`，可直接读 PNG | 1.7 原版贴图在安装根目录的 `Assets.zip` 内（条目名 = 原名 + `.dds`，Zstd 压缩） |
| 4 | 近战武器 `techLevel` 没有 `Ultratech` | 枚举是 `Undefined/Animal/Neolithic/Medieval/Industrial/Spacer/Ultra/Archotech`——用户想说的「Ultratech」对应 **`Ultra`**；另需注意字段表漏了 `Ultra` 与 `Animal` |
| 5 | 远程武器顶层写 `rangedWeapon_Cooldown` / `warmupTime` / `range` / `verbClass` | 1.7 **全部无效**：冷却在 `statBases/RangedWeapon_Cooldown`，射程/预热/弹丸在 `verbs/li` 里 |
| 6 | 配方产物写 `<products><li><thingDef>…</thingDef><count>…</count></li></products>` | 1.7 是字典写法：`<products><产物defName>数量</产物defName></products>`（原版 50 个 `products` 块全是这个形态） |
| 7 | 建筑模板缺 `thingClass` / `inspectorTabs`，且提到 `filthAffordance` | 工作台必须 `thingClass=Building_WorkTable` + `inspectorTabs/li=ITab_Bills`；`filthAffordance` 在 1.7 不存在 |
| 8 | 服装用 `apBodyPartGroups` / 顶层 `bodyPartGroups` | 1.7 只有 `apparel/bodyPartGroups/li` |
| 9 | 服装 `tags` 引用 `ApparelTagDef` | 1.7 **没有** `ApparelTagDef` 这个类型，`tags`/`defaultOutfitTags` 是自由字符串列表 |
| 10 | 服装贴图用 `wornGraphicPath` | 1.7 是单值 `wornGraphicPath`（原版 13 处）与列表 `wornGraphicPaths` 并存，需按需选 |
| 11 | 补丁操作写 `PatchOperationSet` | 1.7 **不存在**该类型；节点名是 `<Operation>`，具体类型由 `Class` 属性决定 |
| 12 | （文档未提 `PatchOperationInsert` 的语义） | 它把 `value` 插成**匹配节点的兄弟节点**，所以 xpath 必须指向列表里的已有节点（`/tools/li[1]`），指向容器 `/tools` 会插错位置 → 运行时字段错误 |
| 13 | （文档未提） | `Graphic_Random` 需要目录形态贴图，单图必须 `Graphic_Single` |
| 14 | （文档未提） | 手写的「材料决定」配方必须显式写 `productHasIngredientStuff=true`，否则产物不继承输入材料 |
| 15 | 语言目录名未规定 | 本机 136 个工坊 mod：短名 `ChineseSimplified` 43 个、带括号 `ChineseSimplified (简体中文)` 18 个，两种都无 `LanguageInfo.xml`，1.7 下两种都在用 → 规范应写明「目录名 = 语言身份」并给出两种合法写法 |

**运行时段可能还会暴露新问题**（例如补丁运行时是否真生效、`0Harmony` 版本兼容、植物野生生成、穿戴贴图体型），请把第 3 节的结果贴回来，我再回填第 6 节。

---

## 7. 尚未核实的事项（诚实清单）

- 全部结论来自 **本机 DLL 元数据反射 + 原版 Data 全库比对**，没有启动过游戏。
- `legacyFolderName` 的取值无法静态确定（`Assembly-CSharp.dll` 里只读不写），所以「短名目录一定被认」靠的是 136 个工坊 mod 的群体证据 + L2 实验，而不是官方文档。
- `DamageResult` 是 class 还是 struct 未实测，因此 `Thing.TakeDamage` 的补丁**故意不声明** `__result`。
- `0Harmony.dll`（工坊版，引用框架 net8）与 1.7 的 net10.0 运行时之间是否有漂移，未验证。
- `<order>Prepend</order>` 的子元素写法合法（字段+枚举双重反射确认），但原版 14 个补丁文件里没有先例。
- 测试护盾背心的**物品图标**路径（`Things/Item/Equipment/Apparel/DM_TestVest`）没有照抄原版 FlakVest 的写法（原版图标直接复用穿戴贴图目录），属于刻意的探路；若游戏里图标不显示，这是第一嫌疑。
- 两条配方**故意不写研究前置**（测试可达性优先），不等于技能推荐这么做。

---

## 8. AI 声明与法律边界

- 本 mod 的 XML / C# / 贴图全部由 AI 辅助生成；`About.xml` 描述末尾与每个 `Source/*.cs` 文件头都带 `[AI 辅助生成]` 标注。
- 贴图为纯几何矢量原创绘制（脚本 `Source/make-textures.py` 可重跑复现），未使用任何第三方 IP 素材。
- 未复制原版 C# 源码、未打包原版 DLL；编译时仅从工坊 Harmony 引用 `0Harmony.dll`，成品里不含它。
- `author` 是占位符，**发布到创意工坊前必须由你替换**，并遵守技能里的法律边界章节。

---

## 9. 卸载与回退

1. 关闭游戏。
2. 把 `<RimWorld>\Mods\RimTestMod\` 整个目录**移入回收站**（不要永久删除）。
3. 启动游戏，确认模组列表里已无本 mod。
4. 存档里若已放置本 mod 的物件，读档会提示缺 Def，属预期；删掉那些物件或换回未使用本 mod 的存档即可。
