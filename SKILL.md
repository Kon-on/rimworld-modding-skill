---
name: rimworld-modding
license: MIT
compatibility: RimWorld 1.7（实测 1.7.4981 rev136；引擎已换成 Waylith、目标框架 net10.0、Unity 不再需要）。核对 Def 需要可读的原版文件（游戏目录 Data/Core/Defs）或 RimSage MCP；两者都没有时只能产出「待验证草稿」。维护脚本需 Node 18+。
metadata:
  version: "1.2.0"
  repository: https://github.com/Kon-on/rimworld-modding-skill
description: |
  当用户制作 RimWorld（环世界）1.7 的 mod 时使用——新建 mod 项目、写 XML Def（武器／建筑／
  物品／服装／植物等）、C# 与 Harmony 补丁、编译 DLL、排查红字与崩溃、发布 Steam 创意工坊。
  
  触发词：RimWorld、环世界、rimworld、RW、mod、模组、Def、XML、ThingDef、Harmony、Patch、补丁、
  武器、建筑、物品、生物、植物、派系、事件、创意工坊、Workshop、C#、DLL、编译。
---

# RimWorld Mod 制作指南

## 🧠 核心决策：何时调 MCP，何时直接用模板

**三层决策——每次接收 mod 制作请求时，按以下优先级判断：**

```
用户请求
  │
  ├─ ① 有模板？ ─── 武器/服装/建筑/资源/配方/Harmony/ThingComp
  │     └─ ✅ 直接用模板生成，不调 MCP（注释头标「已验证」的免核验；标「待核验」的先走降级路径核对）
  │
  ├─ ② 报错/调试？ ─── 红字/白窗/崩溃/NullReferenceException
  │     └─ 🔍 调 MCP 查错误原因、搜索类似问题（MCP 不可用则 grep）
  │
  └─ ③ 无模板的新类型？ ─── 植物/生物/派系/事件/地形/Hediff/研究...
        └─ 📡 调 MCP 查原版 Def 结构 → 模仿写出 Def → 存储为新模板
```

> **先检索，再决策**：本仓库自带 RimWorld 1.7 模板库 `library/`（39 份模板 + 254 张字段表 + 1.3 万行字段总表，含 Steam 各 DLC），一行命令就能查，比下面这张速查表全得多：
>
> ```bash
> node scripts/find-template.mjs 武器                  # 关键词找模板与字段
> node scripts/find-template.mjs --def ThingDef        # 该 Def 类型的模板 + ≥90% 必填字段
> node scripts/find-template.mjs --field verbClass     # 字段路径、出现率、原版样例值
> ```
>
> 命中模板 → 走 ①（用它生成，是否免核验仍按注释头标注）；命中字段表 → 拿出现率核对字段名与路径，**别凭记忆写**；
> 脚本退出码 2（模板库不在本机）→ 走 ③ 调 MCP。下方对照表只是常用速查，模板库才是全集。

### 模板 ↔ Def 类型对照表

<!-- INDEX:TABLE:START -->
| 用户需求 | 对应模板 | MCP？ |
|----------|---------|:----:|
| 近战武器 | `assets/templates/weapon-melee.xml` | ❌ 免 |
| 远程武器 | `assets/templates/weapon-ranged.xml` | ❌ 免 |
| 服装/护甲/头饰 | `assets/templates/apparel.xml` | ❌ 免 |
| 原材料/建筑材料 | `assets/templates/resource-stuff.xml` | ❌ 免 |
| 建筑/工作台 | `assets/templates/building.xml` | ❌ 免 |
| 制作配方 | `assets/templates/recipe.xml` | ❌ 免 |
| 植物（观赏/作物） | `assets/templates/plant.xml` | ❌ 免 |
| Harmony 补丁 | `assets/templates/harmony-patch.cs` | ❌ 免 |
| C# ThingComp | `assets/templates/thingcomp.cs` | ❌ 免 |
| 修改原版（XML） | `references/04-xml-patching.md` | ❌ 免 |
| **生物 / 派系 / 事件 / 地形** | **无模板** | 📡 MCP |
| **地形 / Hediff / 研究 / 工作** | **无模板** | 📡 MCP |
| 任何**错误排查** | `references/08-debugging.md` | 🔍 MCP |
| 批量需求清单格式 | `assets/templates/requirements-template.md` | ❌ 免 |
<!-- INDEX:TABLE:END -->

---

## ⚙️ RimSage MCP 配置

> 如果还没有配置，参考 `.mcp.json.example` 创建项目级配置，或运行平台对应的 MCP 添加命令。
> 首次索引需 30-60 分钟。详见 `references/11-platform-adaptation.md`。

**MCP 不可用时**：按「核验源降级路径」（见下方「外部工具协作」）逐级回退：本地 grep → 请用户给路径 → 待验证草稿。**永远不要凭记忆猜字段名或枚举值。**

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

**📋 存储与更新清单（每次创建新模板后必须逐项完成——第 1 步和第 4 步最容易漏）：**

| # | 操作 | 工具 | 目标位置 |
|---|------|------|---------|
| 1 | 写入模板文件（必须落盘，在对话里输出不算完成） | `Write` | `assets/templates/<新类型>.xml`（或 `.cs`） |
| 2 | 加入「模板 ↔ Def 类型对照表」 | `Edit` | SKILL.md 的 `<!-- INDEX:TABLE -->` 区块内——新增一行，标记 `❌ 免` |
| 3 | 加入「子文件索引 → 代码模板」 | `Edit` | SKILL.md 的 `<!-- INDEX:TEMPLATES -->` 区块内——新增条目 |
| 4 | 跑校验脚本 | `Bash` | `node scripts/check-index.mjs` 必须通过 |

> 只生成 Def 不落盘、或落盘不更新索引，下次同类请求依旧重复调 MCP——**生成新模板 = 落盘 + 更新两处索引 + 校验通过**。

**📐 模板格式规范（Write 模板文件时必须遵守）：**

1. `<?xml version="1.0" encoding="utf-8"?>` 开头（XML 模板）
2. 注释块（`<!-- ... -->`）包含（前两项由 `scripts/check-index.mjs` 机器校验，缺一即失败）：
   - `验证状态：已验证（对照 <原版文件>）` 或 `验证状态：待核验（需核对 <字段／文件>）`
   - `AI 辅助生成`
   - 模板类型名称
   - 原版参考路径（哪个原版 XML 文件）
   - ParentName 继承链（完整层级）
   - 关键设计决策说明
3. 所有用户自定义值使用 `{{YourXxx}}` 占位符（如 `{{YourPrefix}}_Thing_{{YourName}}`）——**不要写成尖括号形式**：模板文件本身必须能被 XML 解析器解析，`<YourPrefix>` 会让整个模板不是合法 XML，
4. 关键字段附带中文行内注释（含可选值列表/合法范围）
5. 文件末尾保留一个空行

**💡 模板示例参考**：打开任意现有模板（如 `assets/templates/weapon-melee.xml`）查看注释头和占位符风格，新模板应与之保持一致。

---

## 🧠 学习系统

每次加载此 Skill 时，必须先读取 `learnings/errors.txt` 中的历史错误记录，
并在后续工作中避免重复犯错。

排查完错误并修复后，必须将关键教训总结为一句话追加到 `learnings/errors.txt`。
格式：`YYYY-MM-DD | <类别> | <一句话总结>`

| 类别 | 适用场景 |
|------|---------|
| XML | ThingDef/RecipeDef/Def 属性写错、枚举值错误、ParentName 错误 |
| C# | 编译错误、空引用、类型错误、DLL 加载问题 |
| Harmony | Patch ID 冲突、补丁未生效、Prefix/Postfix 签名错误 |
| Path | 文件路径错误、资源缺失、加载顺序问题 |
| Other | 上述类别之外的错误 |

此文件仅在 rimworld-modding skill 上下文中读取，其他场景不读取。

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
| 🆕 **新建一个 mod 项目** | `references/workflows/new-mod.md` + `references/02-project-structure.md` |
| ⚔️ **添加武器/物品/建筑/服装/植物** | `references/03-xml-defs.md` + 对应 `assets/templates/*.xml` |
| 🔧 **修改原版机制/打补丁** | `references/04-xml-patching.md`（XML）/ `references/06-harmony.md`（C#） |
| 💻 **编写 C# 代码/DLL** | `references/05-csharp-basics.md` |
| 🎵 **用 Harmony 拦截方法** | `references/06-harmony.md` + `assets/templates/harmony-patch.cs` |
| 🖼️ **添加纹理/音效资源** | `references/07-assets.md` |
| 🐛 **排查报错/崩溃/红字** | `references/08-debugging.md` |
| 📖 **查看历史错误记录** | `learnings/errors.txt`（自动读取） |
| ✅ **测试通过，正规化 mod** | `references/workflows/formalize-mod.md` |
| 📦 **批量处理多个需求** | `references/workflows/batch-process.md` + `assets/templates/requirements-template.md` |
| 📦 **发布到 Steam Workshop** | `references/09-workshop.md` |
| 📖 **查询 API/类/方法** | `references/10-api-reference.md`（建议先接入 RimSage MCP） |
| 🔄 **适配其他 AI 平台** | `references/11-platform-adaptation.md`（Claude Code / Copilot / Codex / Gemini / TRAE / Cursor / DSH 工具映射） |

## 核心原则

### 1. 命名规范（唯一权威版在 `references/02-project-structure.md` → 命名规范）
- **四项全由用户决定，AI 不预设**：前缀（如 `RCS_`）、namespace（`你的前缀.Mod名`）、packageId（全小写无空格，如 `steamid.modname`）、作者名（所有 `<author>` 字段）
- 用户没给 → **先问，不要自己编一个**；只有用户明确说「你看着办」时才按其 mod 名生成临时值，并提醒发布前替换

### 2. 版本注意
- **目标版本**：RimWorld 1.7（本机实测 1.7.4981 rev136）
- **引擎**：Waylith（自研，1.7 起替换 Unity；游戏根目录的 `UnityStubs.dll` 提供兼容层）
- **.NET**：net10.0（不再用 .NET Framework 4.7.2；编译细节见 `references/01-environment.md`）
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

### 5. 学习策略
- **先查速查表**：`references/10-api-reference.md` 覆盖高频 API
- **再看源码**：优先使用 RimSage MCP 搜索 RimWorld 源码
- **模仿原版**：`RimWorld/Data/Core/Defs/` 中的原版 Def 是最好的参考。**优先使用 RimSage MCP 直接查询原版结构**，避免凭记忆猜测 ParentName 或字段名。

### 6. AI 生成标注
每次生成 mod 后，必须在以下位置标注 AI 辅助生成，确保玩家可发现且不影响游戏体验：

- **About.xml 的 `<description>` 末尾** — 添加一行 `[AI 辅助生成]`，玩家在 Mod 列表中查看信息时可见
- **Steam Workshop 页面描述** — 在描述开头或末尾标注"本 Mod 部分内容由 AI 辅助生成"
- **C# 代码文件头部注释**（如 Harmony 补丁）— 添加 `// AI 辅助生成`，开发者审查代码时可见
- 不在 label、defName、游戏内图标等影响实际游玩体验的位置标注

### 7. 三层决策详解（示例与反面教材）

#### ① 有模板 → 直接用，不调 MCP

标注为「验证状态：已验证」的模板，其字段名／枚举值／ParentName 继承链／Comps 均已对照原版核实，只需替换 `{{Your...}}` 占位符；标注为「待核验」的模板必须先按降级路径查一遍再用。

```
用户: "生成一把近战等离子剑"
→ 加载 assets/templates/weapon-melee.xml
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

**核验源不可用时**：按「核验源降级路径」逐级回退，绝不凭记忆猜字段名。

#### ③ 无模板的新类型 → MCP 查 → 写 → ⚠️ 存模板

遇到模板未覆盖的 Def 类型（如植物、生物、派系等），**完整流程如下**：

```
用户: "帮我添加一种新植物"
→ ① 查对照表，确认当前无 plants.xml 模板
→ ② MCP: get_def_details("Plant_TreeOak") → 了解原版 Def 结构（字段名、继承、Comps）
→ ③ MCP: search_rimworld_source("plant def wild") → 确认关键字段的用法模式
→ ④ 根据原版结构写出完整 Def + 中文注释（遵循模板格式规范）
→ ⑤⑥⑦ 落盘 + 更新两处索引 —— 细则见顶部「📋 存储与更新清单」，缺一不可
→ 🔧 收尾：`node scripts/check-index.mjs` 必须通过（索引漏了它会直接报错）
→ ✅ 完成——下次遇到植物请求直接免 MCP，加载模板即可
```

**反面教材（RainbowCatSword 犯过的错）**：
- ❌ `techLevel` 凭记忆写 `Ultratech` → 实际是 `Ultra`（如果先用模板就不会错）
- ❌ `extraMeleeDamages` 凭记忆加 `Class="DamageWorker_AddInjury"` → 模板已标明不需要 Class

**教训：有模板就不用 MCP——模板就是为了消灭凭记忆猜测。无模板才调 MCP——查出来、写下来、存下来。**

## 外部工具协作

### 优先级

```
① 有模板（已验证）→ 直接用模板 → 不调任何外部工具
② 无模板 → MCP > grep > dnSpy
③ 有错误 → MCP > grep > dnSpy
```

### 核验源降级路径（按顺序走完，一级都不能跳）

```
① RimSage MCP    —— 首选，直接查原版结构与源码
② 本地检索原版   —— grep `RimWorld/Data/Core/Defs/`；C# 用 dnSpy 反编译 Assembly-CSharp.dll
③ 向用户要路径   —— 「请把 RimWorld 安装目录（含 Data/Core/Defs）发我」；拿到后回到 ②
④ 都没有         —— 输出「⚠️ 待验证草稿」，不冒充已核验内容
```

**走到第 ④ 级（游戏未安装／拿不到原版文件）时必须这样做：**
1. 交付物开头写明：`⚠️ 待验证草稿——未对照原版核验，字段名与枚举值需你自行确认`；
2. 逐条列出**不确定的字段**，并注明"到哪个原版文件能核对"（如 `Defs/ThingDefs_Misc/Weapons/MeleeMedieval.xml`）；
3. **不得写入 `assets/templates/`**——模板目录只收已验证内容，否则下次会顶着"已验证"的名义传播错误；
4. 告诉用户：等能访问原版（装游戏／配 MCP／给路径）时回来复核，再存模板。

### RimSage MCP（有模板时跳过，无模板或报错时第一选择）

详见顶部"核心决策"章节。

### grep（MCP 不可用时的兜底）

> `<游戏安装目录>` 指游戏根目录（含 `Assembly-CSharp.dll` 的那一层）；换机器时替换成实际路径，脚本里则用环境变量 `RIMWORLD_DIR` / `HARMONY_DIR`，不要把本机路径写进交付物。

```bash
# 搜索字段的所有用法
grep -r "extraMeleeDamages" "<游戏安装目录>/Data/Core/Defs/" | head -10

# 搜索 ParentName 定义
grep -r 'Name="BaseMeleeWeapon"' "<游戏安装目录>/Data/Core/Defs/"

# 搜索所有 techLevel 取值
grep -rh "techLevel" "<游戏安装目录>/Data/Core/Defs/" | sort -u | head -20
```

### dnSpy（第三选择——反编译 C# 源码）

无网络时用 dnSpy 打开游戏**安装根目录**的 `Assembly-CSharp.dll`（1.7 没有 `RimWorldWin64_Data/Managed/`，DLL 就在根目录；同目录还有 `RimWorld.dll`、`UnityStubs.dll`）。

## 资源链接

- [RimWorld Wiki Modding Tutorials](https://rimworldwiki.com/wiki/Modding_Tutorials)
- [RimWorld 中文维基](https://rimworld.huijiwiki.com)
- [Harmony 官方文档](https://github.com/pardeike/Harmony/wiki)
- [RimWorld Mod Template (VS)](https://github.com/truemogician/RimWorld-Mod-Template)
- [RimSearcher MCP](https://github.com/kearril/RimSearcher)

## 🔧 维护者工具（技能运行时用不到，改动本仓库时才用）

| 文件 | 作用 | 命令 |
|------|------|------|
| `scripts/check-index.mjs` | 机械校验：路径引用是否存在、两处索引是否收录全部文件、模板标注是否齐全 | `node scripts/check-index.mjs`（`--strict` 警告即失败，`--json` 供 CI） |
| `tests/run-evals.mjs` | 跑 `tests/evals.json` 的评测断言 / 校验用例结构 | `node tests/run-evals.mjs --validate` · `--prompts` · `--check-all <运行目录>` |
| `scripts/find-template.mjs` | 查本地 1.7 模板库：模板清单、某 Def 类型的模板与必填字段、某字段的路径与出现率 | `node scripts/find-template.mjs --list` · `--def ThingDef` · `--field verbClass`（`--json` 供机器读） |
| `tests/test-find-template.mjs` | 检索脚本的冒烟测试（库缺位时自动跳过） | `node tests/test-find-template.mjs` |
| `scripts/xml-lint.mjs` | 零依赖 XML 良构性扫描（标签配对、注释里的 `--`、占位符写进元素名）；被 check-index 与单测共用 | 经 `node tests/test-xml-lint.mjs` 调用 |
| `tests/test-xml-lint.mjs` | XML 模板良构性单测（含"占位符不能当元素名"这类反例） | `node tests/test-xml-lint.mjs` |
| `tests/README.md` | 评测方法论与 baseline 记录 | — |
| `.github/workflows/check.yml` | CI：每次提交自动跑索引校验、用例结构、检索脚本冒烟、XML 良构性 | 推到 GitHub 即生效 |
| `CHANGELOG.md` | 版本变更记录 | — |

> 改完本仓库任何文件，先跑 `node scripts/check-index.mjs` 再提交。

## 子文件索引

<!-- INDEX:REFERENCES:START -->
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
11. `references/11-platform-adaptation.md` — 跨平台适配（Claude Code / Copilot / Codex / Gemini / TRAE / Cursor / DSH 工具映射）
<!-- INDEX:REFERENCES:END -->

<!-- INDEX:TEMPLATES:START -->
### 代码模板 (assets/templates/)
- `assets/templates/weapon-melee.xml` — 近战武器 Def
- `assets/templates/weapon-ranged.xml` — 远程武器 Def
- `assets/templates/harmony-patch.cs` — Harmony 补丁骨架
- `assets/templates/building.xml` — 建筑 Def（Phase 2）
- `assets/templates/recipe.xml` — 配方 Def（Phase 2）
- `assets/templates/thingcomp.cs` — ThingComp 骨架
- `assets/templates/apparel.xml` — 服装/护甲 Def（含衣物、护甲、头饰注释）
- `assets/templates/resource-stuff.xml` — 原材料/建筑材料 Def（含 stuffProps 完整注释）
- `assets/templates/requirements-template.md` — 批量需求文件格式模板
- `assets/templates/plant.xml` — 植物 Def（观赏/作物两段，走「无模板新类型」流程产出）
<!-- INDEX:TEMPLATES:END -->

### 错误学习 (learnings/)
- `learnings/errors.txt` — 历史错误记录（每次加载 Skill 时自动读取）

<!-- INDEX:WORKFLOWS:START -->
### 工作流 (references/workflows/)
- `references/workflows/new-mod.md` — 从零创建 mod（测试版先行）
- `references/workflows/formalize-mod.md` — 测试通过后正规化 + 可选发布
- `references/workflows/debug-crash.md` — 崩溃排查
- `references/workflows/add-item.md` — 添加物品
- `references/workflows/add-building.md` — 添加建筑
- `references/workflows/batch-process.md` — 批量处理需求清单
- `references/workflows/patch-vanilla.md` — 修改原版
<!-- INDEX:WORKFLOWS:END -->
