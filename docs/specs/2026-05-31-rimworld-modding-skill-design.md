# RimWorld Mod 制作 Skill 设计文档

**日期**: 2026-05-31  
**状态**: 待审阅  
**版本**: v1.0

---

## 1. 项目动机

### 1.1 问题

RimWorld mod 制作涉及多个独立技术领域（XML Def、C#、Harmony、资源制作、Steam 发布），学习曲线陡峭。新手常陷入以下困境：

- 不知道该从哪里开始
- 中文教程分散（贴吧、CSDN、灰机 wiki），缺乏系统性
- 英文官方文档虽然全面，但信息量大且语言有门槛
- 没有 AI 辅助的 mod 开发工作流

### 1.2 已有方案分析

| 方案 | 类型 | 局限 |
|------|------|------|
| RimSage / RimWorld Coding RAG | MCP 源码搜索 | 解决"查代码"，不解决"怎么做" |
| RimWorld Wiki Tutorials | 英文文档 | 语言门槛，不嵌入 AI 工作流 |
| 中文灰机 wiki | 中文文档 | 不完整，版本滞后 |
| RimWorld Mod Template | 项目脚手架 | 只解决环境搭建，不覆盖开发全流程 |

**我们的 Skill 填补的空白**：一个嵌入 Claude Code 的、中文主导的、全流程覆盖的 RimWorld mod 制作指南 + 开发辅助系统。

---

## 2. 目标与范围

### 2.1 核心目标

让用户（零基础）能在 Claude Code 中，通过自然语言交互完成 RimWorld mod 的全流程开发。

### 2.2 范围

**覆盖：**
- 环境搭建（IDE、.NET SDK、dnSpy 反编译、RimSage MCP 接入）
- Mod 项目结构
- XML Def 系统（物品、建筑、植物、生物、派系、事件等）
- XML PatchOperations（修改原版/其他 mod）
- C# Mod 开发（Mod 类、Settings、ExposeData、ThingComp、GameComponent）
- Harmony 补丁（Prefix/Postfix/Transpiler）
- 资源制作（纹理 PNG/Mask、音效）
- Steam Workshop 发布
- 调试与排错

**不覆盖：**
- RimWorld 源码本身的详细 API 文档（交给 MCP 工具）
- Unity 底层知识（Shader、AssetBundle 等高级内容，作为进阶留给后续版本）
- 具体 mod 创意设计（那是用户的领域）

### 2.3 目标版本

RimWorld 1.6，主体代码基于 1.6 API。

---

## 3. 架构设计

### 3.1 整体架构

```
用户输入 (自然语言)
       │
       ▼
┌─────────────┐
│  SKILL.md   │  ← 总调度器：识别意图 → 路由到子文件
│  (总索引)    │     内置快速决策树 + 关键词触发表
└──────┬──────┘
       │
       ├── 路由到 references/  (知识查询)
       │      ├── 01-environment.md
       │      ├── 02-project-structure.md
       │      ├── 03-xml-defs.md
       │      ├── 04-xml-patching.md
       │      ├── 05-csharp-basics.md
       │      ├── 06-harmony.md
       │      ├── 07-assets.md
       │      ├── 08-debugging.md
       │      ├── 09-workshop.md
       │      └── 10-api-reference.md
       │
       ├── 路由到 templates/  (代码生成)
       │      ├── mod-root/
       │      ├── weapon-melee.xml
       │      ├── weapon-ranged.xml
       │      ├── building.xml
       │      ├── recipe.xml
       │      ├── research.xml
       │      ├── apparel.xml
       │      ├── plant.xml
       │      ├── harmony-patch.cs
       │      └── thingcomp.cs
       │
       └── 路由到 workflows/ (任务引导)
              ├── new-mod.md
              ├── add-item.md
              ├── add-building.md
              ├── patch-vanilla.md
              └── debug-crash.md
```

### 3.2 触发机制

SKILL.md 的 description 字段包含关键词白名单，在用户消息匹配时激活：

**触发关键词：**
- RimWorld / 环世界 / rimworld / RW
- mod / Mod / 模组 / 模块
- Def / XML Def / ThingDef / RecipeDef
- Harmony / Patch / 补丁
- 武器 / 建筑 / 物品 / 生物 / 植物 / 派系 / 事件
- Steam Workshop / 创意工坊

### 3.3 意图路由（SKILL.md 核心逻辑）

```
IF 用户提到"新建/创建/开始 + mod/项目"
   → 加载 workflows/new-mod.md
   → 加载 references/02-project-structure.md
   → 生成 mod-root/ 模板

ELSE IF 用户提到"物品/武器/建筑/服装/植物/配方/研究"
   → 加载 references/03-xml-defs.md 对应章节
   → 加载对应 template/*.xml
   → 提供交互式填写引导

ELSE IF 用户提到"修改原版/打补丁/覆盖/调整 + 机制/属性/行为"
   → 加载 references/04-xml-patching.md
   → 如果是 C# 层面 → 加载 references/06-harmony.md

ELSE IF 用户提到"Harmony/拦截/Prefix/Postfix/Transpiler"
   → 加载 references/06-harmony.md
   → 加载 templates/harmony-patch.cs

ELSE IF 用户提到"C#/代码/脚本/DLL/编译/组件"
   → 加载 references/05-csharp-basics.md

ELSE IF 用户提到"纹理/贴图/图片/音效/资源"
   → 加载 references/07-assets.md

ELSE IF 用户提到"报错/崩溃/调试/日志/白窗/红字"
   → 加载 references/08-debugging.md

ELSE IF 用户提到"发布/上传/创意工坊/Steam"
   → 加载 references/09-workshop.md

ELSE IF 用户提到"API/查询/源码/类/方法"
   → 引导用户使用 RimSage MCP 进行源码搜索
   → 加载 references/10-api-reference.md

ELSE
   → 给出分类引导，询问用户具体需求
```

### 3.4 子文件加载策略

遵循**渐进式加载**原则：

1. **SKILL.md** 始终加载（轻量索引，<200 行）
2. **references/** 仅在匹配时按需加载（每次 1-2 个文件）
3. **templates/** 在被请求生成代码时加载
4. **workflows/** 在任务匹配时加载

每次对话最多加载 2-3 个子文件，避免上下文污染。

---

## 4. 各模块详细说明

### 4.1 SKILL.md（总调度器）~150 行

- YAML frontmatter（name, description + 触发关键词）
- 快速决策树（意图 → 模块映射表）
- 核心原则（命名规范、版本注意、安全实践）
- 与外部工具的协作指引（RimSage MCP 调用时机）

### 4.2 references/01-environment.md — 环境搭建

- Visual Studio 2022 / VS Code + .NET Framework 4.7.2 配置
- RimWorld 本体引用 DLL 路径
- dnSpy 反编译 Assembly-CSharp.dll 查看源码
- RimSage MCP 安装与接入 Claude Code
- RimPy / RimSort 辅助工具

### 4.3 references/02-project-structure.md — 项目结构

- 标准目录树（About/ Defs/ Assemblies/ Textures/ Sounds/ Patches/ Languages/ 1.6/）
- About.xml 字段详解（name, author, packageId, supportedVersions, modDependencies）
- LoadFolders.xml（按版本/DLC 条件加载）
- 命名规范（前缀、namespace、defName）

### 4.4 references/03-xml-defs.md — XML Def 系统（核心模块，最长）

- Def 体系概览与常见 Def 类型表
- 各 Def 详解：ThingDef（物品/建筑/植物）、RecipeDef、ResearchDef、HediffDef、TraitDef、FactionDef、IncidentDef 等
- 关键标签参考（statBases, costList, thingCategories, comps, etc.）
- ParentName 继承机制
- MayRequire/MayRequireAnyOf 条件加载
- 完整示例（武器、建筑、植物各一个）

### 4.5 references/04-xml-patching.md — XML PatchOperations

- Patch 文件结构与 XPath 选择器
- 操作类型：add, remove, replace, set, insert
- 实战示例：修改原版武器伤害、添加配方到原版工作台、替换建筑贴图

### 4.6 references/05-csharp-basics.md — C# Mod 开发

- Mod 类（继承 Verse.Mod）
- Mod Settings（窗口化配置）
- ThingComp 系统
- GameComponent / MapComponent / WorldComponent
- ExposeData（存档兼容）
- DefModExtension（自定义 Def 扩展字段）

### 4.7 references/06-harmony.md — Harmony 补丁

- 基础概念与 [StaticConstructorOnStartup] 入口
- Prefix（前置拦截）— 修改参数、跳过原方法、替换返回值
- Postfix（后置拦截）— 修改结果
- Transpiler（IL 级修改）— 高级用法简要介绍
- __instance / __result / __state 等特殊参数
- 常见模式（替换配方产出、修改 AI 行为、拦截事件）

### 4.8 references/07-assets.md — 资源制作

- 纹理格式规范（PNG, 推荐分辨率）
- Mask 图层的使用
- 音效格式（WAV/OGG）
- 路径约定（Textures/Things/, Sounds/）
- 简单工具推荐（GIMP, Paint.NET, Audacity）

### 4.9 references/08-debugging.md — 调试与排错

- 开发者模式启用与常用操作
- Player.log 日志位置与解读
- 常见错误速查（红字/白窗/NullReferenceException/XML 解析错误）
- 二分法排查 mod 冲突
- 隔离测试技巧

### 4.10 references/09-workshop.md — 发布

- Steam Workshop 上传流程
- 版本号管理与更新
- Mod 描述与预览图最佳实践
- 兼容性声明（DLC、其他 mod）

### 4.11 references/10-api-reference.md — API 速查

- 常用类/方法速查表（Verse, RimWorld 命名空间）
- Def 字段索引（按功能分类）
- 版本差异备注（1.5 → 1.6 关键变化）
- 与 RimSage MCP 的分工：速查表用于高频场景，MCP 用于深度查询

### 4.12 templates/ — 模板文件

每个模板包含：
- 完整可工作的 XML/C# 代码
- 中文注释标注关键字段
- 占位符 `<YourModName>`, `<YourPrefix>` 供替换

### 4.13 workflows/ — 工作流

- **new-mod.md**：从零到发布的一步步清单
- **add-item.md**：添加物品的完整代码+步骤
- **add-building.md**：添加建筑的完整代码+步骤
- **patch-vanilla.md**：修改原版内容的操作指南
- **debug-crash.md**：崩溃排查决策树

---

## 5. 语言规范

- **教学说明、注释、工作流指引**：中文
- **代码、XML 标签名、C# 类名/方法名、文件名**：英文
- **Def 名称示例**：英文，带中文注释说明其用途

示例：
```xml
<!-- 一把自定义近战武器：等离子长剑 -->
<ThingDef ParentName="BaseMeleeWeapon">
  <defName>SR_PlasmaSword</defName>
  <label>plasma sword</label>  <!-- 游戏中显示的名称 -->
  ...
</ThingDef>
```

---

## 6. 与外部工具协作

### 6.1 RimSage MCP（推荐）

当用户需要查询 RimWorld 源码时（如 "Thing 类的 Destroy 方法怎么写的"），Skill 应：

1. 先查自己的 `references/10-api-reference.md` 速查表
2. 如果速查表没有，引导用户调用 RimSage MCP：
   ```
   claude mcp add rimworld-source --transport http https://mcp.rimsage.com/mcp
   ```
3. 帮用户用英文关键词调用 `search_rimworld_source` 等工具

### 6.2 dnSpy / ILSpy

当没有网络或不想用 MCP 时，引导用户用 dnSpy 反编译本地 `Assembly-CSharp.dll`。

---

## 7. 测试策略

遵循 writing-skills 的 TDD 流程：

1. **编写压力场景**（subagent 扮演零基础用户，请求执行典型任务）
2. **基线测试（RED）**：无 skill 时，subagent 是否输出错误/不完整的指导
3. **安装 skill（GREEN）**：验证 subagent 输出正确、完整的指导
4. **重构（REFACTOR）**：发现遗漏场景 → 补充 → 重新验证

初始压力场景（最小可验证集）：
1. "帮我创建一个新的 RimWorld mod 项目"
2. "我想添加一把自定义近战武器"
3. "如何用 Harmony 拦截游戏的某个方法"
4. "我的 mod 报红字错误怎么排查"
5. "如何把我的 mod 发布到 Steam Workshop"

---

## 8. 非功能需求

- **上下文效率**：SKILL.md + 任一子文件 < 3000 行，确保不溢出上下文
- **维护性**：模块独立，新增知识点只需添加/修改对应 reference 文件
- **可扩展性**：后续可新增 references/11-dlc-specific.md、references/12-performance.md 等
- **版本追踪**：每个 reference 文件顶部注明适用 RimWorld 版本和最后更新日期

---

## 9. 风险与缓解

| 风险 | 缓解 |
|------|------|
| RimWorld 1.6 API 尚未完全稳定 | API 速查表标注"WIP 1.6"，后续增量更新 |
| 中文社区资料可能过时 | 优先参考官方 Wiki，中文资料做交叉验证 |
| 模板可能因版本更新失效 | 模板包含版本标签，定期审查 |
| MCP 工具接口变化 | SKILL.md 中的 MCP 指引保持通用，不硬编码 |

---

## 10. 交付计划

该 Skill 分为两个阶段：

**Phase 1 — 核心可用（MVP）**
- SKILL.md 总调度器
- 5 个核心 reference：环境、项目结构、XML Def、Harmony、调试
- 3 个高频 template：武器近战/远程、Harmony 补丁
- 2 个工作流：new-mod、debug-crash

**Phase 2 — 完整覆盖**
- 剩余 reference 文件
- 剩余 template 文件
- 剩余 workflow 文件
- TDD 压力测试
