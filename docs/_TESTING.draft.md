# 完整测试 Mod — 测试指导书（草稿，待线 A/B 回填）

> 草稿位置：docs/_TESTING.draft.md。线 A（XML）/ 线 B（C#）完成后并入 `examples/rimtest-mod/`（当时的 `成果/环世界-完整测试mod`）并回填文件清单与 defName 表。

## 0. 这份测试在验证什么

用 rimworld-modding 技能从零做一个 mod，把技能的六条核心能力各跑一遍，看哪条在 RimWorld 1.7 现实环境下走不通：

| 线 | 验证目标 | 对应技能机制 | 状态 |
|----|----------|--------------|:----:|
| A | 6 个 XML Def（近战/远程/服装/材料/建筑/配方）+ 本地化 | 走 assets/templates/ 模板，免查 MCP | 进行中 |
| B | C# ThingComp + Harmony 补丁，真实编译 | references/05、06 + assets/templates/thingcomp.cs、harmony-patch.cs | 进行中 |
| C | 9 张原创贴图 + Preview.png | references/07-assets.md | ✅ 已完成 |
| D | 无模板新类型（植物）全流程：查原版 → 写 Def → 回写模板 → 更新索引 | SKILL.md「场景③」五行闭环 | ✅ 已完成（assets/templates/plant.xml） |
| E | XML PatchOperations 改原版 | references/04-xml-patching.md | 进行中 |
| F | 静态核验（不启动游戏） | 本测试新增工具 docs/verify-testmod.mjs | ✅ 已可用 |

## 1. 本机环境事实（实测，2026-10-18）

- 游戏：RimWorld **1.7.4981 rev136**，安装目录 `E:\SteamLibrary\steamapps\common\RimWorld`
- 目标框架：**net10.0**（`RimWorld.runtimeconfig.json` 的 includedFrameworks = Microsoft.NETCore.App 10.0.13-waylithclr.dev）
- 引擎：Unity **已移除**；全盘无 `UnityEngine*.dll`，`WaylithClr.AssemblyNameRedirects` 把 UnityEngine* 重定向到 UnityStubs
- 程序集位置：`Assembly-CSharp.dll`、`RimWorld.dll` 等**全在安装根目录**；`RimWorldWin64_Data/Managed/` 已不存在
- Harmony：游戏**不再自带** `0Harmony.dll`，用 Harmony 的 mod 必须自带一份（放在自己版本的 `Assemblies/`）
- 贴图：纯 `Textures/*.png` 在 1.7 仍可用；另有新的 `Assets.zip` 形态（内部条目形如 `Textures/x/y.png.dds`）

## 2. 安装（开发者模式）

1. 把 `examples\rimtest-mod\RimTestMod\`（或直接引用 `<RimWorld>\Mods\RimTestMod\`）放进 RimWorld 的 `Mods` 目录。
2. 启动游戏 → 选项 → 模组 → 勾选「完整测试 Mod (Test)」→ 自动排序/手动置底。
3. 开启开发者模式（选项 → 开发者模式 → 打开），并在日志窗口勾选自动打开。
4. 新建一个殖民地（任意剧本，建议 Temperate forest）用于观察。

## 3. 逐项测试

> 结果列请如实填：通过 / 不通过 / 未测。不通过的按第 5 节排查，并把现象原文（红字、Def 名、报错行）记下来。

### 3.1 XML Def 六项（线 A）

| # | 测试项 | 操作 | 预期 | 结果 |
|---|--------|------|------|:----:|
| X1 | 近战武器「等离子匕首」 | Dev Mode → Spawn thing → 搜 `DM_Weapon_PlasmaDagger` | 能搜到、能生成、贴图为匕首外观、信息面板显示伤害/冷却 | |
| X2 | 远程武器「离子步枪」 | 同上搜 `DM_Weapon_IonRifle` | 能搜到、装备后能射击、弹道贴图正确 | |
| X3 | 服装「测试防护背心」 | 同上搜 `DM_Apparel_TestVest` | 能搜到、装备后外观正确（四个朝向） | |
| X4 | 材料「测试合金」 | 同上搜 `DM_Stuff_TestAlloy` | 能搜到、可堆叠、可作建筑/武器材料 | |
| X5 | 建筑「测试工作台」 | Dev Mode → Spawn building 或建造菜单 | 能搜到、可放置、有工作台 gfx | |
| X6 | 配方 | 打开对应工作台的制作清单 | 配方出现、材料消耗正确、产出正确物品 | |
| L1 | 中文本地化 | 上述任一项的信息面板 | label/description 显示**中文**而非 defName | |

### 3.2 植物（场景③ 新类型，线 D）

| # | 测试项 | 操作 | 预期 | 结果 |
|---|--------|------|------|:----:|
| X7 | 观赏植物「测试花」 | Dev Mode → Spawn thing → `DM_Plant_TestBloom`；或种植菜单 → 观赏 | 能搜到/能种、会生长、成熟后给美观度、割除不掉落多余物品 | |
| X8 | 野生生成 | 新开地图后搜地图上的野生测试花 | 若配置了 wildOrder，应有野生个体 | |

### 3.3 C# 与 Harmony（线 B）

| # | 测试项 | 操作 | 预期 | 结果 |
|---|--------|------|------|:----:|
| C1 | ThingComp 护盾 | 给小人穿上测试防护背心，看信息面板/受击 | Comp 被加载（无 `Could not find type` 红字），护盾值 50 生效 | |
| C2 | Harmony 补丁 | 触发被补丁的目标行为 | 补丁生效（行为/数值按补丁设计改变），日志无 Harmony 异常 | |
| C3 | 程序集加载 | 打开日志窗口看头部 | 无「Could not load assembly」「找不到 0Harmony」类错误 | |

### 3.4 原版补丁（线 E）

| # | 测试项 | 操作 | 预期 | 结果 |
|---|--------|------|------|:----:|
| P1 | PatchOperation 生效 | 按补丁目标查看对应原版 Def 的实际数值（信息面板/制作台） | 数值按补丁改变，且**未破坏**原版其他内容 | |

## 4. 静态核验（不用启动游戏，可先跑）

```powershell
node docs/verify-testmod.mjs
```

检查 8 类问题：XML 良构、defName 唯一且带前缀、ParentName/defName 引用可解析、texPath 贴图存在、字段路径对照 1.7 全量字段总表、枚举值（techLevel / plant.purpose）、Patch 结构与 xpath、XML 引用的自定义 C# 类型在 DLL 中存在。报告写入 `examples/rimtest-mod/核验报告.json`（本文档成稿时的旧路径 `docs/verify-report.json` 已随重复工作副本一并移除），有 error 时退出码 1。

**最近一次结果（贴图线完成后）**：XML 4 个文件良构；Def 1 个；原版索引 1560 个 XML / 12415 个 defName+Name；texPath 引用 1 处 **缺失 0 处**；字段路径 24 处**全部命中 1.7 字段表**；错误 0 项、警告 0 项。

## 5. 失败现象 → 排查路径

| 现象 | 首先做什么 |
|------|-----------|
| 搜不到 defName | 走技能三层决策 ③：先查 `Data/Core/Defs` 同名 Def 对照字段；确认 XML 在第一层目录的 `Defs/` 下且良构（`verify-testmod.mjs` 会先说 XML 是否良构） |
| 红字 `Could not find parent` | ParentName 写错或原版已改名 —— 用原版 XML 的 `<ThingDef Name="...">` 属性与元素名核对 |
| 贴图空白/紫块 | texPath 与 `Textures/` 下相对路径不一致（不带扩展名）；大小写敏感 |
| C# 类型找不到 | 确认 `Assemblies/` 里有编译产物、namespace 与 XML 里写的完全一致、目标框架 net10.0 |
| Harmony 报错 | 1.7 需自带 `0Harmony.dll`；补丁 ID 唯一；目标方法签名必须用 dnSpy/元数据核对 |
| 启动即崩 | 先禁用本 mod 启动，确认游戏本体正常，再逐条启用 |

## 6. 本测试暴露的技能缺陷（1.6 → 1.7）

待测试跑完后统一回填：技能里写「目标版本 1.6 / 引用 DLL 在 RimWorldWin64_Data/Managed / .NET Framework 4.7.2 / Harmony 从 workshop-2009463077 取」等陈述与本机 1.7 现实的冲突清单，以及修正结果。

## 7. AI 声明与法律边界

- 本 mod 全部 XML/C#/贴图由 AI 辅助生成；`About.xml` description 末尾、`Source/*.cs` 文件头均已标注 `[AI 辅助生成]`。
- 贴图为纯几何矢量原创绘制，未使用任何第三方 IP 素材；未复制原版 C# 源码、未打包原版 DLL。
- 作者字段为占位符「（待填：作者名）」，发布前必须替换。

## 8. 卸载与回退

1. 关闭游戏；把 `Mods\RimTestMod\` 整个目录移入回收站（不要永久删除）。
2. 启动游戏确认模组列表已无本 mod；存档中若已放置本 mod 的物品，读档会留空引用提示，属预期。
