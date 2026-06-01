---
name: rimworld-modding
version: 0.721.0-alpha
description: >
  Comprehensive guide for RimWorld mod developers. Use when users want to create or modify
  RimWorld mods (weapons, buildings, items, plants, factions, events), work with XML Defs
  (ThingDef, RecipeDef), write C# mod code or Harmony patches, debug mod errors, or publish
  to Steam Workshop. Covers environment setup through publishing. 环世界模组制作全流程指南。
tags:
  - rimworld
  - modding
  - game-development
  - csharp
  - harmony
  - xml
  - steam-workshop
  - ai-generated
dependencies:
  rimworld-source:
    type: mcp
    url: https://mcp.rimsage.com/mcp
    required: false
    fallback: local-grep
---

# RimWorld Mod 制作指南

## ⚙️ 前置依赖：RimSage MCP

### 依赖声明

| 项目 | 值 |
|------|-----|
| **依赖名称** | RimSage（`rimworld-source`） |
| **协议** | MCP over HTTP |
| **必需工具** | `search_rimworld_source`、`get_def_details`、`read_rimworld_file` |
| **配置方式** | `.mcp.json`（项目级）或 `claude mcp add`（全局） |
| **首次索引** | 30-60 分钟，之后毫秒级 |

> ⚠️ RimSage 是**外部运行时依赖**——本 Skill 不捆绑、不内置 MCP 服务器。

### 初始化检测（每个会话开始时执行）

在开始任何 mod 制作工作前，先检测 MCP 可用性：

```
检测流程：
  try MCP ping
    ├─ ✅ 可用 → 使用 MCP 工具验证所有 Def 结构
    ├─ ❌ 不可用 → 询问用户：
    │     A. 帮我配置  → 创建 .mcp.json（参考 .mcp.json.example）
    │     B. 稍后再说  → 降级为本地 grep 模式（功能受限）
    │     C. 不用 MCP  → 永久降级，只用 grep
    └─ ⏱️ 超时 → 降级为本地 grep，提示用户检查 MCP 服务状态
```

### 优雅降级：MCP 不可用时的回退

| 原本用 MCP 做的事 | 降级方案 |
|------------------|---------|
| `get_def_details("xxx")` | `grep -r 'defName="xxx"' <RW>/Data/Core/Defs/` + Read 对应文件 |
| `search_rimworld_source("xxx")` | `grep -r "xxx" <RW>/Data/Core/Defs/` |
| `read_rimworld_file("path")` | Read 工具直接读本地文件 |
| 查继承链 | `grep -r 'ParentName="Xxx"' <RW>/Data/Core/Defs/'` 递归追溯 |

> **降级模式限制**：grep 只能做字面匹配，无法像 MCP 那样理解语义。"查哪些武器用了 extraMeleeDamages" 这种查询在降级模式中需要手动遍历文件。

### MCP 不可用时的错误信息

当调用 MCP 工具失败时，区分原因：

| 错误现象 | 可能原因 | 告诉用户 |
|---------|---------|---------|
| `mcp__rimworld-source` 工具不存在 | MCP 未配置或未批准 | "RimSage MCP 未连接——运行 `claude mcp add rimworld-source --transport http https://mcp.rimsage.com/mcp` 或在项目目录创建 `.mcp.json`（参考 `.mcp.json.example`）" |
| 工具调用超时 | MCP 服务未启动或网络问题 | "RimSage 服务无响应——检查 `https://mcp.rimsage.com/mcp` 是否可达，或降级为本地 grep 模式" |
| 工具返回空结果 | 索引未完成或查询不匹配 | "未找到匹配结果。可能原因：1) 索引还未完成（首次需 30-60 分钟）2) 查询关键词不对——试试更通用的词" |

### RimSage 三件套：何时用哪个

| 你要做的事 | 用这个工具 | 示例查询 |
|-----------|-----------|---------|
| 查某个 Def 的完整定义和继承链 | `get_def_details` | `get_def_details("MeleeWeapon_Gladius")` |
| 找"XX 是怎么实现的" | `search_rimworld_source` | `"melee weapon extraMeleeDamages example"` |
| 读某个源文件全文 | `read_rimworld_file` | `Data/Core/Defs/.../BaseWeapons.xml` |

### 典型查询模式

**查继承链**：`get_def_details("BaseMeleeWeapon")` → 看 ParentName 链  
**查字段用法**：`search_rimworld_source("extraMeleeDamages Burn")`  
**验证枚举值**：`search_rimworld_source("techLevel Ultra")` → 确认是 "Ultra" 不是 "Ultratech"  
**对比相似物品**：`get_def_details("MeleeWeapon_Gladius")` → 模仿写新武器

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
| ✅ **测试通过，正规化 mod** | `references/workflows/formalize-mod.md` |
| 📦 **发布到 Steam Workshop** | `references/09-workshop.md` |
| 📖 **查询 API/类/方法** | `references/10-api-reference.md`（建议先接入 RimSage MCP） |

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

### 5. ⚠️ 铁律：写代码前必须验证（Validate First, Write Second）

**禁止凭记忆或猜测填写任何字段名、枚举值、类名或 XML 结构。每写一个 Def 前，必须先查原版。**

#### 验证三步

```
1. MCP 查（最快）：get_def_details("<原版类似物品>") 或 search_rimworld_source("<字段名> <关键词>")
2. grep 查（MCP 不可用时）：grep -r "字段名" "RimWorld/Data/Core/Defs/"
3. 读文件（以上都不行）：Read 对应的原版 Def 文件
```

#### 每种需求对应的查询

| 要写的内容 | MCP 方式（优先） | grep 兜底 |
|-----------|-----------------|----------|
| `techLevel` 枚举 | `search_rimworld_source("techLevel Neolithic Medieval Industrial")` | `grep -r "techLevel" Data/Core/Defs/ \| head -20` |
| `ParentName` | `get_def_details("<类似物品defName>")` 看继承链 | `grep -r 'Name="BaseXxx"' Data/Core/Defs/` |
| `Class=` 属性 | `search_rimworld_source("Class=\"CompProperties_Xxx\"")` | `grep -r 'Class="Xxx"' Data/Core/Defs/` |
| 嵌套结构如 extraMeleeDamages | `search_rimworld_source("extraMeleeDamages")` | `grep -r "extraMeleeDamages" Data/Core/` |
| 完整的 Def 参考 | `get_def_details("原版物品defName")` | Read 原版文件 |
| C# 方法签名 | `search_rimworld_source("方法名")` | dnSpy 反编译 |

#### 反面教材（RainbowCatSword 犯过的错）：
- ❌ `techLevel` 凭记忆写 `Ultratech` → 实际是 `Ultra`（一次 `search_rimworld_source("techLevel")` 就能发现）
- ❌ `extraMeleeDamages` 凭记忆加 `Class="DamageWorker_AddInjury"` → 实际不需要 Class

**教训：每个字段的值都是查出来的，不是想出来的。**

## 外部工具协作

### RimSage MCP（第一选择）

详见顶部"开始前"章节。如果 MCP 不可用：

### grep（第二选择——本地搜索）

```bash
# 搜索字段的所有用法（<RW> 替换为你的 RimWorld 安装目录）
grep -r "extraMeleeDamages" "<RW>/Data/Core/Defs/" | head -10

# 搜索 ParentName 定义
grep -r 'Name="BaseMeleeWeapon"' "<RW>/Data/Core/Defs/"

# 搜索所有 techLevel 取值
grep -rh "techLevel" "<RW>/Data/Core/Defs/" | sort -u | head -20
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

### 代码模板 (assets/templates/)
- `assets/templates/weapon-melee.xml` — 近战武器 Def
- `assets/templates/weapon-ranged.xml` — 远程武器 Def
- `assets/templates/harmony-patch.cs` — Harmony 补丁骨架
- `assets/templates/building.xml` — 建筑 Def
- `assets/templates/recipe.xml` — 配方 Def
- `assets/templates/thingcomp.cs` — ThingComp 骨架

### 工作流 (references/workflows/)
- `references/workflows/new-mod.md` — 从零创建 mod（测试版先行）
- `references/workflows/formalize-mod.md` — 测试通过后正规化 + 可选发布
- `references/workflows/debug-crash.md` — 崩溃排查
- `references/workflows/add-item.md` — 添加物品
- `references/workflows/add-building.md` — 添加建筑
- `references/workflows/patch-vanilla.md` — 修改原版
