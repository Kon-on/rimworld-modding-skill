---
name: rimworld-modding
description: |
  RimWorld mod 制作全流程指南——覆盖环境搭建、XML Def 系统、C# 开发、Harmony 补丁、
  资源制作和 Steam Workshop 发布。适用于零基础到进阶的 RimWorld 1.6 mod 开发者。
  跨平台支持 Claude Code / TRAE / Copilot CLI / Codex / Gemini CLI / Cursor 等主流 AI 编程工具。
  
  触发词：RimWorld, 环世界, rimworld, RW, mod, Mod, 模组, Def, XML, ThingDef, 
  Harmony, Patch, 补丁, 武器, 建筑, 物品, 生物, 植物, 派系, 事件, 
  Steam Workshop, 创意工坊, C#, DLL, 编译
---

# RimWorld Mod 制作指南

## 🧠 核心决策：何时调 MCP，何时直接用模板

**三层决策——每次接收 mod 制作请求时，按以下优先级判断：**

```
用户请求
  │
  ├─ ① 有模板？ ─── 武器/服装/建筑/资源/配方/Harmony/ThingComp
  │     └─ ✅ 直接用模板生成，不调 MCP（模板已验证过原版结构）
  │
  ├─ ② 报错/调试？ ─── 红字/白窗/崩溃/NullReferenceException
  │     └─ 🔍 调 MCP 查错误原因、搜索类似问题（MCP 不可用则 grep）
  │
  └─ ③ 无模板的新类型？ ─── 植物/生物/派系/事件/地形/Hediff/研究...
        └─ 📡 调 MCP 查原版 Def 结构 → 模仿写出 Def → 存储为新模板
```

### 模板 ↔ Def 类型对照表

| 用户需求 | 对应模板 | MCP？ |
|----------|---------|:----:|
| 近战武器 | `templates/weapon-melee.xml` | ❌ 免 |
| 远程武器 | `templates/weapon-ranged.xml` | ❌ 免 |
| 服装/护甲/头饰 | `templates/apparel.xml` | ❌ 免 |
| 原材料/建筑材料 | `templates/resource-stuff.xml` | ❌ 免 |
| 建筑/工作台 | `templates/building.xml` | ❌ 免 |
| 制作配方 | `templates/recipe.xml` | ❌ 免 |
| Harmony 补丁 | `templates/harmony-patch.cs` | ❌ 免 |
| C# ThingComp | `templates/thingcomp.cs` | ❌ 免 |
| 修改原版（XML） | `references/04-xml-patching.md` | ❌ 免 |
| **植物 / 生物 / 派系 / 事件** | **无模板** | 📡 MCP |
| **地形 / Hediff / 研究 / 工作** | **无模板** | 📡 MCP |
| 任何**错误排查** | `references/08-debugging.md` | 🔍 MCP |

---

## ⚙️ RimSage MCP 配置

> 如果还没有配置，参考 `.mcp.json.example` 创建项目级配置，或运行平台对应的 MCP 添加命令。
> 首次索引需 30-60 分钟。详见 `references/11-platform-adaptation.md`。

**MCP 不可用时**：降级为本地 `grep` 搜索 `RimWorld/Data/Core/Defs/`。

### MCP 三件套（仅在上表标明 📡 或 🔍 时使用）

| 场景 | 用这个工具 | 示例 |
|------|-----------|------|
| 无模板 → 查原版 Def 结构 | `get_def_details` | `get_def_details("Plant_TreeOak")` |
| 无模板 → 搜索实现模式 | `search_rimworld_source` | `"plant def wild cluster"` |
| 报错 → 查错误原因 | `search_rimworld_source` | `"NullReferenceException food"` |

### 新类型模板创建流程（场景 ③）

```
用户要求无模板类型
  → ① MCP 查原版类似 Def（get_def_details + search_rimworld_source）
  → ② 写出完整可用的 Def（带中文注释，遵循下方"模板格式规范"）
  → ③ Write 模板到文件系统（绝对路径，不能用对话中输出代替）
  → ④ 更新 SKILL.md 两处列表（见下方"存储与更新清单"）
  → ✅ 下次同类型请求直接免 MCP
```

**📋 存储与更新清单（每次创建新模板后必须逐项完成）：**

| # | 操作 | 工具 | 目标位置 |
|---|------|------|---------|
| 1 | 写入模板文件 | `Write` | `templates/<新类型>.xml`（或用 `.cs` 后缀） |
| 2 | 添加到"模板 ↔ Def 类型对照表" | `Edit` | SKILL.md 顶部表格——新增一行，标记 `❌ 免` |
| 3 | 添加到"子文件索引 → 代码模板" | `Edit` | SKILL.md 底部 `templates/` 列表——新增条目 |

**📐 模板格式规范（Write 模板文件时必须遵守）：**

1. `<?xml version="1.0" encoding="utf-8"?>` 开头（XML 模板）
2. 注释块（`<!-- ... -->`）包含：
   - 模板类型名称 + 验证状态
   - 原版参考路径（哪个原版 XML 文件）
   - ParentName 继承链（完整层级）
   - 关键设计决策说明
3. 所有用户自定义值使用 `<YourXxx>` 占位符（如 `<YourPrefix>_Thing_<YourName>`）
4. 关键字段附带中文行内注释（含可选值列表/合法范围）
5. 文件末尾保留一个空行

**💡 模板示例参考**：打开任意现有模板（如 `templates/weapon-melee.xml`）查看注释头和占位符风格，新模板应与之保持一致。

---

## 核心工作流：测试版先行（Test → Verify → Formalize）

**所有 mod 生成后，默认先生成测试版本。开发者确认无 bug 后，再正规化并可选发布。**

```
用户需求 → 生成测试版 Mod → 开发者进游戏测试
                              ├─ 有 bug → 修复 → 重新测试
                              └─ 确认无误 → 正规化 → 可选：上传 Steam
```

> **测试版 vs 正规版**：测试版快速迭代验证；正规版清理命名、补全 About.xml、准备发布。

## 快速导航

根据你的需求，我会自动加载对应的参考文档和模板。

### 我想...
| 需求 | 加载内容 |
|------|---------|
| 🆕 **新建一个 mod 项目** | `workflows/new-mod.md` + `references/02-project-structure.md` |
| ⚔️ **添加武器/物品/建筑/服装/植物** | `references/03-xml-defs.md` + 对应 `templates/*.xml` |
| 🔧 **修改原版机制/打补丁** | `references/04-xml-patching.md`（XML）/ `references/06-harmony.md`（C#） |
| 💻 **编写 C# 代码/DLL** | `references/05-csharp-basics.md` |
| 🎵 **用 Harmony 拦截方法** | `references/06-harmony.md` + `templates/harmony-patch.cs` |
| 🖼️ **添加纹理/音效资源** | `references/07-assets.md` |
| 🐛 **排查报错/崩溃/红字** | `references/08-debugging.md` |
| ✅ **测试通过，正规化 mod** | `workflows/formalize-mod.md` |
| 📦 **发布到 Steam Workshop** | `references/09-workshop.md` |
| 📖 **查询 API/类/方法** | `references/10-api-reference.md`（建议先接入 RimSage MCP） |
| 🔄 **适配其他 AI 平台** | `references/11-platform-adaptation.md`（Copilot/Codex/Gemini 等工具映射） |

## 核心原则

### 1. 命名规范
- **前缀**：所有 defName 和 C# 类名使用唯一前缀（**由用户自行选择**，如 `RCS_`、`AWE_` 等），避免 mod 冲突
- **namespace**：`你的前缀.Mod名`（由用户根据前缀确定）
- **packageId**：`你的用户名.mod名`（全小写，无空格，**用户自行填写**，如 `steamid.modname`）
- **作者名**：所有 `<author>`、作者字段**必须由用户自行填写**，AI 不预设作者信息

### 2. 版本注意
- **目标版本**：RimWorld 1.6
- **Unity 版本**：2022.3.35
- **.NET Framework**：4.7.2+
- 每个 reference 文件顶部标注适用版本和最后更新日期

### 3. 安全实践
- 始终在 `[StaticConstructorOnStartup]` 中初始化 Harmony
- Harmony patch 方法使用唯一的 patch ID
- ExposeData 中正确保存/加载自定义数据
- 避免在构造函数中做重型操作
- 优先使用 PatchOperations 而非直接修改原版文件

### 4. ⚖️ 法律边界——什么能做，什么不能

**Ludeon Studios 积极支持 mod 制作**——官方 Wiki 有完整 modding 教程，Steam Workshop 是官方集成渠道。但以下底线不可越过：

#### ✅ 完全合法——放心做

| 行为 | 依据 |
|------|------|
| 编写原创 XML Def | RimWorld 公开数据接口 |
| 用原版 ParentName 继承 | 等同于调用公开 API |
| 模仿原版 Def 结构 | 等同于参考 API 文档 |
| 用 dnSpy / MCP 查原版代码 | mod 社区标准做法（官方 Wiki C# 教程第一页就教你用 dnSpy） |
| 发布原创 mod 到 Steam Workshop | 官方支持的发布渠道 |

#### ❌ 绝对禁止

| 行为 | 原因 |
|------|------|
| **复制原版 C# 源码到你的 mod** | 侵犯 Ludeon 版权 |
| **打包原版 DLL（Assembly-CSharp.dll 等）到你的 mod** | 侵犯版权 |
| **复制其他 mod 的代码/资产/贴图** | 侵犯原作者权利 |
| **使用第三方 IP（宝可梦、星战、漫威等）的角色/名称/资产** | 商标/版权侵权 |
| **使用 AI 生成的、明显抄袭第三方 IP 的贴图** | 版权风险 |

#### ⚠️ 灰色地带（允许但有风险）

| 行为 | 建议 |
|------|------|
| 受其他游戏**启发**的武器/物品（如彩虹喵喵剑 ≈ Meowmere） | ✅ 合法——灵感不侵权，名称/设计要是原创的 |
| 反编译查看原版方法签名 | ✅ 行业惯例——只查 API，不抄实现 |
| 参考原版数值（如 Gladius 伤害=16）来平衡你的武器 | ✅ 参考值范围，不直接复制 |

**核心原则：你的 mod 可以模仿原版结构和 API 用法，但代码和资产必须是原创的。不确定时，问开发者确认。**

### 4. 学习策略
- **先查速查表**：`references/10-api-reference.md` 覆盖高频 API
- **再看源码**：优先使用 RimSage MCP 搜索 RimWorld 源码
- **模仿原版**：`RimWorld/Data/Core/Defs/` 中的原版 Def 是最好的参考。**优先使用 RimSage MCP 直接查询原版结构**，避免凭记忆猜测 ParentName 或字段名。

### 5. ⚠️ 三层决策详解

#### ① 有模板 → 直接用，不调 MCP

模板内的字段名、枚举值、ParentName 继承链、Comps 配置均已在编写时对照原版验证。直接使用模板生成，仅替换 `<Your...>` 占位符即可。**模板是经过验证的，无须重复验证。**

```
用户: "生成一把近战等离子剑"
→ 加载 templates/weapon-melee.xml
→ 填入用户指定的伤害/冷却/材质/科技等级
→ 直接输出 Def + 贴图路径 + 配方配置
→ 不调 MCP
```

#### ② 报错/调试 → 调 MCP 查原因

当用户报告游戏内错误（红字、白窗、崩溃、异常行为）时，用 MCP 搜索错误信息、查看相关方法源码，找出根本原因。

```
用户: "我的 mod 报 NullReferenceException at Pawn.Tick"
→ search_rimworld_source("Pawn Tick")
→ 查相关方法签名和调用链
→ 定位问题代码 → 给出修复方案
```

**MCP 不可用时**：用 grep 搜原版 Defs 目录 + dnSpy 反编译 C#。

#### ③ 无模板的新类型 → MCP 查 → 写 → ⚠️ 存模板

遇到模板未覆盖的 Def 类型（如植物、生物、派系等），**完整流程如下**：

```
用户: "帮我添加一种新植物"
→ ① 查对照表，确认当前无 plants.xml 模板
→ ② MCP: get_def_details("Plant_TreeOak") → 了解原版 Def 结构（字段名、继承、Comps）
→ ③ MCP: search_rimworld_source("plant def wild") → 确认关键字段的用法模式
→ ④ 根据原版结构写出完整 Def + 中文注释（遵循模板格式规范）
→ ⑤ ⚠️ Write 到 templates/plant.xml（skill 的 templates/ 目录下）
        （必须用 Write 工具写入文件系统，不能在对话中输出就算完！）
→ ⑥ Edit SKILL.md 对照表：添加 `| 植物 | templates/plant.xml | ❌ 免 |`
→ ⑦ Edit SKILL.md 索引：添加 `- templates/plant.xml — 植物 Def`
→ ✅ 完成——下次遇到植物请求直接免 MCP，加载模板即可
```

> **⚠️ 关键提醒：步骤⑤（Write 文件）和⑥⑦（更新 SKILL.md）最容易遗漏！**
> 如果只生成了 Def 但没有写入文件系统，下次同类请求时模板仍然不存在，又会重复 MCP 查询。
> **生成新模板 = 写入文件 + 更新 SKILL.md，缺一不可。**

**反面教材（RainbowCatSword 犯过的错）**：
- ❌ `techLevel` 凭记忆写 `Ultratech` → 实际是 `Ultra`（如果先用模板就不会错）
- ❌ `extraMeleeDamages` 凭记忆加 `Class="DamageWorker_AddInjury"` → 模板已标明不需要 Class

**教训：有模板就不用 MCP——模板就是为了消灭凭记忆猜测。无模板才调 MCP——查出来、写下来、存下来。**

## 外部工具协作

### 优先级

```
① 有模板 → 直接用模板 → 不调任何外部工具
② 无模板 → MCP > grep > dnSpy
③ 有错误 → MCP > grep > dnSpy
```

### RimSage MCP（有模板时跳过，无模板或报错时第一选择）

详见顶部"核心决策"章节。

### grep（MCP 不可用时的兜底）

```bash
# 搜索字段的所有用法
grep -r "extraMeleeDamages" "D:/steam/steamapps/common/RimWorld/Data/Core/Defs/" | head -10

# 搜索 ParentName 定义
grep -r 'Name="BaseMeleeWeapon"' "D:/steam/steamapps/common/RimWorld/Data/Core/Defs/"

# 搜索所有 techLevel 取值
grep -rh "techLevel" "D:/steam/steamapps/common/RimWorld/Data/Core/Defs/" | sort -u | head -20
```

### dnSpy（第三选择——反编译 C# 源码）

无网络时用 dnSpy 打开 `<RimWorld>/RimWorldWin64_Data/Managed/Assembly-CSharp.dll`。

## 资源链接

- [RimWorld Wiki Modding Tutorials](https://rimworldwiki.com/wiki/Modding_Tutorials)
- [RimWorld 中文维基](https://rimworld.huijiwiki.com)
- [Harmony 官方文档](https://github.com/pardeike/Harmony/wiki)
- [RimWorld Mod Template (VS)](https://github.com/truemogician/RimWorld-Mod-Template)
- [RimSearcher MCP](https://github.com/kearril/RimSearcher)

## 子文件索引

### 知识参考 (references/)
1. `references/01-environment.md` — 环境搭建
2. `references/02-project-structure.md` — Mod 项目结构
3. `references/03-xml-defs.md` — XML Def 系统
4. `references/04-xml-patching.md` — XML PatchOperations
5. `references/05-csharp-basics.md` — C# Mod 开发
6. `references/06-harmony.md` — Harmony 补丁
7. `references/07-assets.md` — 资源制作
8. `references/08-debugging.md` — 调试与排错
9. `references/09-workshop.md` — Steam Workshop 发布
10. `references/10-api-reference.md` — API 速查表
11. `references/11-platform-adaptation.md` — 跨平台适配（TRAE/Copilot/Codex/Gemini 工具映射）

### 代码模板 (templates/)
- `templates/weapon-melee.xml` — 近战武器 Def
- `templates/weapon-ranged.xml` — 远程武器 Def
- `templates/harmony-patch.cs` — Harmony 补丁骨架
- `templates/building.xml` — 建筑 Def（Phase 2）
- `templates/recipe.xml` — 配方 Def（Phase 2）
- `templates/thingcomp.cs` — ThingComp 骨架
- `templates/apparel.xml` — 服装/护甲 Def（含衣物、护甲、头饰注释）
- `templates/resource-stuff.xml` — 原材料/建筑材料 Def（含 stuffProps 完整注释）

### 工作流 (workflows/)
- `workflows/new-mod.md` — 从零创建 mod（测试版先行）
- `workflows/formalize-mod.md` — 测试通过后正规化 + 可选发布
- `workflows/debug-crash.md` — 崩溃排查
- `workflows/add-item.md` — 添加物品
- `workflows/add-building.md` — 添加建筑
- `workflows/patch-vanilla.md` — 修改原版
