# 变更记录

格式参考 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)；版本号遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

## 1.2.0 — 2026-10-18

这次改动只为一件事：**把整个技能从 1.6 校准到 1.7**。证据不是猜的——用这个技能真机做成了一个环世界 1.7 测试 mod（含 8 类 XML Def、ThingComp、3 个 Harmony 补丁、12 张原创贴图、本地化），过程中撞到的每一处「文档与 1.7 现实不一致」都记下来，再逐条回改技能本体。

### 变更（1.6 → 1.7 校准）

- SKILL.md：`compatibility` / `description` / "版本注意" / dnSpy 段落全部改 1.7（引擎 Waylith、框架 net10.0、程序集在游戏安装根目录）。
- `references/01-environment.md` **全量重写**：1.7 环境变化表、.NET SDK 10、安装根的三个引用 DLL、两种编译方式（临时 csproj / csc + 引用程序集）、Harmony 来源与三条规则、PowerShell 元数据探针、核验源三层降级、快速检查清单。
- `references/03-xml-defs.md`：新增「1.6 → 1.7 字段变更速查」，以及远程武器、配方、服装三节 **1.7 真实结构**；techLevel 补全枚举（含 `Ultra`/`Animal`）；工作台"四件套"；`AllRecipes` 去重机制。
- `references/04-xml-patching.md`：新增「节点名与 Class 属性」「1.7 可用的补丁操作全清单」；`PatchOperationSet` 已不存在（否则用 `PatchOperationAttributeSet`）；`Insert` 的兄弟节点语义坑；"调试 Patch" 重写。
- `references/05-csharp-basics.md`：新增「1.7 API 差异速查（实测）」（`dinfo.SetAmount`、`LookTargets`、`Verse.Command_Action`、`Verse.MessageTypeDefOf`、`UnityStubs`、Harmony 3.0）。
- `references/06-harmony.md`：新增「1.7 上的 Harmony」与 **bootstrap 模式**完整代码（逐条取目标、失败只报错、不拖垮程序集）。
- `references/07-assets.md` **全量重写**：原版贴图改在安装根 `Assets.zip`（内部 `.dds`，Zstd）、按原版实测的尺寸与朝向表、穿戴贴图的朝向/体型后缀、"Graphic_Single vs Graphic_Random"。
- `references/02 / 08 / 09 / 10 / 11`：版本陈述与 `LoadFolders`/`supportedVersions` 示例改 1.7；`10` 的"1.5 → 1.6 待复核"整节换成 **"1.6 → 1.7 关键变化（已实测）"**。
- `assets/templates/`：武器（远程）、配方、建筑、服装、植物模板修正；`harmony-patch.cs` 按 Harmony 3.0 重写；`thingcomp.cs` 升级；模板注释头的验证状态按实际证据升级为「已验证」。
- `references/workflows/`：new-mod、formalize-mod 的目标版本与 `supportedVersions` 改 1.7。

### 修复（原文写错、在 1.7 上会直接踩坑的地方）

- 远程武器模板：顶层的 `rangedWeapon_Cooldown`/`WarmupTime`/`range`/`verbClass` 在 1.7 **全部无效** → 正确写法是 `statBases/RangedWeapon_Cooldown` + `verbs/li` 内各字段。
- 配方模板：`products` 写成 `<li><thingDef>/<count></li>` 是错的 → 1.7 是字典写法 `<products><产物defName>数量</产物defName></products>`；`workSpeedStat` 用的 `CraftingSpeed` **这个 StatDef 在 1.7 里不存在**（改 `GeneralLaborSpeed`）。
- 建筑模板：缺 `thingClass=Building_WorkTable` 与 `inspectorTabs/li=ITab_Bills`；文件里出现**两个 `<comps>` 节点**（已合并为一个列表容器）；`Mass` 的用途注释写错（拆毁返还是由 `costList` 决定）。
- 服装模板：techLevel 枚举缺 `Ultra`/`Animal`；`wornGraphicPath` 未说明方向与体型后缀；未说明 1.7 没有 `ApparelTagDef`。
- 植物模板：`Graphic_Random` 配单文件贴图会报 `No textures found at path …`/`Collection cannot init`（`Graphic_Collection` 初始化失败）→ 改 `Graphic_Single`。

### 证据

- 每条结论都指向原版 1.7 文件行号或 DLL 反射结果。
- 可复跑：`node scripts/check-index.mjs --strict`。

### 已知问题

- **运行时验证尚未完成**：本机未启动游戏，游戏内测试项（语言目录加载、补丁日志、植物贴图、存档读档）待跑。静态检查通过 ≠ 运行时正确。
- Harmony 3.0（编译目标 net8）与游戏 net10.0 的运行时漂移只在"能编译 + 启动时登记成功"这一层验证过，全场景未验证。
- 沿用 1.1.0 的两条：部分评测断言字面量过严；缺无技能的 RED baseline。

## 1.1.0 — 2026-10-17

这次改动针对同一个根因：**靠人记着的约束一定会漂移**。手写索引会漂、没有可复现验证的知识会腐化、核验源缺失时人会开始凭记忆写字段名——三类问题都改成机械约束。

### 新增

- `scripts/check-index.mjs`：零依赖校验脚本。检查 skill 内路径引用是否存在、是否残留重构前的旧前缀、索引区块是否收录全部文件、模板注释头是否有验证状态与 AI 标注；`--strict`（警告即失败）、`--json`（CI）可用。
- 评测运行器、评测方法论与首次 baseline（4 条用例 / 24 条断言，23 通过）。
- `CHANGELOG.md`（本文件）。
- SKILL.md「核验源降级路径」：RimSage MCP → 本地 grep / dnSpy → 向用户索要游戏目录 → 「⚠️ 待验证草稿」，并规定草稿的四条硬要求（开头声明、列出待核对项、不得写入模板目录、提醒复核）。
- `references/02-project-structure.md`：「本地化（Languages 目录）」一节（DefInjected / Keyed / 落地检查）。
- `references/11-platform-adaptation.md`：DSH（DeepSeek Harness）平台一节与工具映射（含 Windows PowerShell 提示）。
- README：「维护与校验」一节，并记录同类现成工具（agentskills-ci、agent-skill-evals、lychee）作为可选增强。

### 变更

- frontmatter：`description` 改为触发条件前置（能力清单移到 README）；新增 `license`、`compatibility`、`metadata.version`、`metadata.repository`。
- SKILL.md 去重与重编号：「核心决策」与「三层决策详解」不再重复叙述同一套判断；命名规范压缩为 2 条并指向 `references/02-project-structure.md`。
- 模板注释头统一为 `验证状态：已验证（对照 <原版文件>）` / `验证状态：待核验（需核对 <字段／文件>）` + `AI 辅助生成`。武器、服装、原材料为「已验证」；建筑、配方、Harmony、ThingComp 按实际情况标为「待核验」。
- 核心决策树与「三层决策」①：区分「已验证」与「待核验」模板——后者必须先按降级路径核对再用。
- `references/10-api-reference.md`：状态从 WIP 改为「草稿」，并说明以反编译源码为准；「1.5 → 1.6 关键变化」标为待复核。
- README：补版本号、DSH 平台行与安装命令、目录树、需求（Node 18+ 与无核验源时的行为）。

### 修复

- 修复目录重构（2026-06-01，commit f08c44e）后残留的旧路径引用共 **47 处**：SKILL.md 37 处、README.md 1 处、`references/workflows/` 9 处。校验脚本第一次运行就把 workflows 里的 9 处也扫了出来——此前的人工审计只覆盖了 SKILL.md 与 README.md，说明人工审计本身也需要机械兜底。
- `references/11-platform-adaptation.md` 两处 `templates/` → `assets/templates/`。

### 已知问题

- 评测断言有三处字面量过严（属性写法 vs 元素写法、`not_contains` 会误伤正确的纠错文案）。未擅自修改断言——改测试迎合答案等于取消测试。
- 缺 RED baseline（无技能对照），当前分数还不能证明「技能确实改变了产出质量」；待跑。

## 1.0.0 — 2026-06-01

- 按 skill 发布惯例标准化目录：`templates/` → `assets/templates/`、`workflows/` → `references/workflows/`，评测用例目录独立，移除两份设计/计划文档。
- 首次发布：SKILL.md、11 篇参考文档、7 个工作流、9 个模板、错误学习记录与 4 条评测用例。
