# RimWorld Mod 制作 Skill 实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 创建 rimworld-modding skill，让零基础用户通过 Claude Code 自然语言交互完成 RimWorld mod 全流程开发。

**Architecture:** SKILL.md 作为轻量总调度器（关键词意图路由），references/ 为按需加载的知识模块，templates/ 为可复制代码模板，workflows/ 为分步任务引导。遵循渐进式加载，每次最多 2-3 个子文件。

**Tech Stack:** Markdown（SKILL.md + 子文件）、XML（RimWorld Def 模板）、C#（Harmony/Mod 模板）

**Skill 安装路径:** `~/.claude/skills/rimworld-modding\`

---

## 文件结构总览

```
~/.claude/skills/rimworld-modding\
├── SKILL.md                        # Phase 1 — 总调度器
├── references/
│   ├── 01-environment.md           # Phase 1
│   ├── 02-project-structure.md     # Phase 1
│   ├── 03-xml-defs.md              # Phase 1（核心，最长）
│   ├── 04-xml-patching.md          # Phase 2
│   ├── 05-csharp-basics.md         # Phase 2
│   ├── 06-harmony.md               # Phase 1
│   ├── 07-assets.md                # Phase 2
│   ├── 08-debugging.md             # Phase 1
│   ├── 09-workshop.md              # Phase 2
│   └── 10-api-reference.md         # Phase 2
├── templates/
│   ├── weapon-melee.xml            # Phase 1
│   ├── weapon-ranged.xml           # Phase 1
│   ├── harmony-patch.cs            # Phase 1
│   ├── building.xml                # Phase 2
│   ├── recipe.xml                  # Phase 2
│   └── thingcomp.cs                # Phase 2
└── workflows/
    ├── new-mod.md                  # Phase 1
    ├── debug-crash.md              # Phase 1
    ├── add-item.md                 # Phase 2
    ├── add-building.md             # Phase 2
    └── patch-vanilla.md            # Phase 2
```

---

## Phase 1: MVP — 核心可用

> MVP 覆盖：SKILL.md 总调度器 + 5 个核心 reference + 3 个高频模板 + 2 个工作流。完成后用户即可进行最基础的 mod 创建、武器添加、Harmony 补丁和调试。

---

### Task 1: 创建 skill 目录结构

**Files:**
- Create: `~/.claude/skills/rimworld-modding\`
- Create: `~/.claude/skills/rimworld-modding\references\`
- Create: `~/.claude/skills/rimworld-modding\templates\`
- Create: `~/.claude/skills/rimworld-modding\workflows\`

- [ ] **Step 1: 创建目录**

```bash
mkdir -p "$HOME/.claude/skills/rimworld-modding/references"
mkdir -p "$HOME/.claude/skills/rimworld-modding/templates"
mkdir -p "$HOME/.claude/skills/rimworld-modding/workflows"
```

- [ ] **Step 2: 验证目录存在**

```bash
ls -la "$HOME/.claude/skills/rimworld-modding/"
```

Expected: 显示 references/ templates/ workflows/ 三个子目录。

---

### Task 2: 编写 SKILL.md（总调度器）

**Files:**
- Create: `~/.claude/skills/rimworld-modding\SKILL.md`

- [ ] **Step 1: 写入 SKILL.md**

文件内容如下（约 150 行）：

```markdown
---
name: rimworld-modding
description: |
  RimWorld mod 制作全流程指南——覆盖环境搭建、XML Def 系统、C# 开发、Harmony 补丁、
  资源制作和 Steam Workshop 发布。适用于零基础到进阶的 RimWorld 1.6 mod 开发者。
  
  触发词：RimWorld, 环世界, rimworld, RW, mod, Mod, 模组, Def, XML, ThingDef, 
  Harmony, Patch, 补丁, 武器, 建筑, 物品, 生物, 植物, 派系, 事件, 
  Steam Workshop, 创意工坊, C#, DLL, 编译
---

# RimWorld Mod 制作指南

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
| 📦 **发布到 Steam Workshop** | `references/09-workshop.md` |
| 📖 **查询 API/类/方法** | `references/10-api-reference.md`（建议先接入 RimSage MCP） |

## 核心原则

### 1. 命名规范
- **前缀**：所有 defName 和 C# 类名使用唯一前缀（如 `SR_`），避免 mod 冲突
- **namespace**：`YourModPrefix.ModName`
- **packageId**：`yourname.modname`（全小写，无空格）

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

### 4. 学习策略
- **先查速查表**：`references/10-api-reference.md` 覆盖高频 API
- **再看源码**：优先使用 RimSage MCP 搜索 RimWorld 源码
- **模仿原版**：`RimWorld/Data/Core/Defs/` 中的原版 Def 是最好的参考

## 外部工具协作

### RimSage MCP（推荐——实时源码搜索）

当需要查询 RimWorld 源码时：

1. 先查看 `references/10-api-reference.md` 速查表
2. 若速查表无结果，使用 RimSage MCP：
   ```
   claude mcp add rimworld-source --transport http https://mcp.rimsage.com/mcp
   ```
3. 用英文关键词调用 `search_rimworld_source` 工具

### dnSpy（离线——反编译 Assembly-CSharp.dll）

无网络或不想用 MCP 时，用 dnSpy 打开 `<RimWorld>/RimWorldWin64_Data/Managed/Assembly-CSharp.dll`，搜索类名/方法名。

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

### 代码模板 (templates/)
- `templates/weapon-melee.xml` — 近战武器 Def
- `templates/weapon-ranged.xml` — 远程武器 Def
- `templates/harmony-patch.cs` — Harmony 补丁骨架
- `templates/building.xml` — 建筑 Def（Phase 2）
- `templates/recipe.xml` — 配方 Def（Phase 2）
- `templates/thingcomp.cs` — ThingComp 骨架（Phase 2）

### 工作流 (workflows/)
- `workflows/new-mod.md` — 从零创建 mod
- `workflows/debug-crash.md` — 崩溃排查
- `workflows/add-item.md` — 添加物品（Phase 2）
- `workflows/add-building.md` — 添加建筑（Phase 2）
- `workflows/patch-vanilla.md` — 修改原版（Phase 2）
```

- [ ] **Step 2: 验证文件**

```bash
wc -l "$HOME/.claude/skills/rimworld-modding/SKILL.md"
```

Expected: ~140-160 行。

---

### Task 3: 编写 references/01-environment.md（环境搭建）

**Files:**
- Create: `~/.claude/skills/rimworld-modding\references\01-environment.md`

- [ ] **Step 1: 写入文件**

```markdown
# 01 — 环境搭建

> **适用版本**: RimWorld 1.6 | **最后更新**: 2026-05-31

## 概述

RimWorld mod 开发需要以下工具链。根据你要做的 mod 类型选择安装：

| Mod 类型 | 必需工具 |
|----------|---------|
| 纯 XML（物品/建筑/配方） | 文本编辑器（VS Code） + RimPy |
| C# + Harmony | Visual Studio 2022 / Rider + .NET Framework 4.7.2 |
| 资源制作 | GIMP / Paint.NET + Audacity |

## IDE 与编译器

### Visual Studio 2022（推荐）

1. 下载 [Visual Studio 2022 Community](https://visualstudio.microsoft.com/vs/community/)
2. 安装时勾选 **".NET 桌面开发"** 工作负载
3. 确保 `.NET Framework 4.7.2 SDK` 被选中

### JetBrains Rider

轻量级替代方案，对反编译支持更好，启动更快。

### VS Code

适合 XML 和纹理编辑。安装扩展：
- **XML** (Red Hat)
- **C#** (Microsoft) — 仅语法高亮

## 引用 DLL

编译 C# Mod 需要引用以下 DLL，位于 `<RimWorld 安装目录>/RimWorldWin64_Data/Managed/`：

| DLL | 用途 |
|-----|------|
| `Assembly-CSharp.dll` | RimWorld 全部游戏代码 |
| `UnityEngine.dll` | Unity 引擎核心 |
| `UnityEngine.CoreModule.dll` | Unity 核心模块 |
| `UnityEngine.IMGUIModule.dll` | UI 相关 |

如需 Harmony，从 Steam Workshop 的 Harmony mod 中获取 `0Harmony.dll`，路径：
```
<RimWorld>/Mods/workshop-2009463077/Current/Assemblies/0Harmony.dll
```

## 源码查阅

### dnSpy（离线反编译）

1. 下载 [dnSpy](https://github.com/dnSpy/dnSpy/releases)
2. 打开 `<RimWorld>/RimWorldWin64_Data/Managed/Assembly-CSharp.dll`
3. 在左侧树中浏览命名空间和类
4. 右键某个方法 → Analyze 查看调用链

### RimSage MCP（AI 辅助搜索——推荐）

一键接入 Claude Code：

```bash
claude mcp add rimworld-source --transport http https://mcp.rimsage.com/mcp
```

接入后可使用 `search_rimworld_source` 用自然语言搜索 RimWorld 源码。

## 辅助工具

| 工具 | 用途 | 链接 |
|------|------|------|
| **RimPy** | Mod 管理 + Def 预览 | [GitHub](https://github.com/rimpy-custom/RimPy) |
| **RimSort** | Mod 排序与依赖管理 | [GitHub](https://github.com/RimSort/RimSort) |
| **RimWorld Mod Template** | VS 项目模板（含 CI/CD） | [GitHub](https://github.com/truemogician/RimWorld-Mod-Template) |

## 快速检查清单

- [ ] IDE 已安装，能创建 .NET Framework 4.7.2 项目
- [ ] 已找到并复制引用 DLL 路径
- [ ] dnSpy 或 RimSage 能正常查看 Assembly-CSharp.dll 内容
- [ ] Mod 输出目录已就绪（`<RimWorld>/Mods/`）
```

- [ ] **Step 2: 验证文件**

```bash
wc -l "$HOME/.claude/skills/rimworld-modding/references/01-environment.md"
```

Expected: ~100 行。

---

### Task 4: 编写 references/02-project-structure.md（项目结构）

**Files:**
- Create: `~/.claude/skills/rimworld-modding\references\02-project-structure.md`

- [ ] **Step 1: 写入文件**

```markdown
# 02 — Mod 项目结构

> **适用版本**: RimWorld 1.6 | **最后更新**: 2026-05-31

## 标准目录树

```
YourModName/
├── About/
│   ├── About.xml            # Mod 元信息（必需）
│   └── Preview.png          # Steam Workshop 预览图（推荐，640×360）
├── Defs/                    # XML 数据定义
│   ├── ThingDefs/
│   │   ├── Items_Weapons.xml
│   │   └── Buildings_Production.xml
│   ├── RecipeDefs/
│   ├── ResearchDefs/
│   └── ...
├── Patches/                 # XML PatchOperations（修改原版/其他 mod）
│   ├── Patch_Vanilla_Weapons.xml
│   └── ...
├── Assemblies/              # 编译后的 C# DLL（仅 C# mod 需要）
│   └── YourModName.dll
├── Textures/                # 纹理资源
│   ├── Things/
│   │   ├── Item/
│   │   └── Building/
│   └── UI/
├── Sounds/                  # 音效资源
├── Languages/               # 本地化（可选）
│   └── English/
│       └── Keyed/
│           └── Strings.xml
├── 1.6/                     # 版本特定资源（1.6+）
│   └── Defs/
└── LoadFolders.xml          # 按版本/DLC 条件加载（可选）
```

## About.xml 详解

```xml
<?xml version="1.0" encoding="utf-8"?>
<ModMetaData>
  <!-- 内部 ID，全小写无空格，全局唯一 -->
  <packageId>yourname.yourmodname</packageId>

  <!-- 显示名称（Steam Workshop 和 Mod 列表显示） -->
  <name>Your Mod Name</name>

  <!-- 作者名 -->
  <author>Your Name</author>

  <!-- 游戏版本：1.6 -->
  <supportedVersions>
    <li>1.6</li>
  </supportedVersions>

  <!-- Mod 依赖（可选） -->
  <modDependencies>
    <!-- 必须依赖 Harmony -->
    <li>
      <packageId>brrainz.harmony</packageId>
      <displayName>Harmony</displayName>
    </li>
  </modDependencies>

  <!-- 依赖的 DLC（可选） -->
  <modDependenciesByVersion>
    <v1.6>
      <li>
        <packageId>ludeon.rimworld.biotech</packageId>
        <displayName>Biotech</displayName>
      </li>
    </v1.6>
  </modDependenciesByVersion>

  <!-- 描述文本（Steam Workshop 显示） -->
  <description>Your mod description here.</description>
</ModMetaData>
```

## 命名规范

### defName 命名

```
<前缀>_<功能>_<名称>
例: SR_Weapon_PlasmaSword, SR_Building_ArcFurnace
```

- **前缀**：2-4 字符，你的 mod 专属（如 `SR_`）
- **功能分类**：Weapon, Building, Apparel, Recipe, Research, Hediff 等
- **名称**：PascalCase 英文

### C# 命名空间

```csharp
namespace SR.YourModName
{
    // ...
}
```

### 文件命名

- XML Def 文件：`Category_SubCategory.xml`（如 `Items_Weapons.xml`, `Buildings_Production.xml`）
- Patch 文件：`Patch_Target_TargetName.xml`（如 `Patch_Vanilla_MeleeWeapons.xml`）

## LoadFolders.xml（条件加载）

当需要按 DLC 或版本加载不同 Def 时：

```xml
<?xml version="1.0" encoding="utf-8"?>
<loadFolders>
  <v1.6>
    <li>1.6</li>
    <li IfModActive="ludeon.rimworld.biotech">1.6/Biotech</li>
  </v1.6>
</loadFolders>
```

## 快速检查清单

- [ ] About.xml 中 `packageId` 全局唯一
- [ ] `supportedVersions` 包含 `1.6`
- [ ] 所有 defName 带唯一前缀
- [ ] 目录结构符合标准（About/ Defs/ Patches/ Assemblies/ Textures/）
```

- [ ] **Step 2: 验证**

```bash
wc -l "$HOME/.claude/skills/rimworld-modding/references/02-project-structure.md"
```

---

### Task 5: 编写 references/03-xml-defs.md（XML Def 系统——核心模块）

**Files:**
- Create: `~/.claude/skills/rimworld-modding\references\03-xml-defs.md`

- [ ] **Step 1: 写入文件**

这是最长的核心模块。内容结构如下，写入完整 Markdown 文件：

```markdown
# 03 — XML Def 系统

> **适用版本**: RimWorld 1.6 | **最后更新**: 2026-05-31

## 什么是 Def？

Def（Definition）是 RimWorld 的数据定义系统。游戏中的所有内容——武器、建筑、植物、生物、派系、事件——都是通过 XML 文件中的 `Def` 定义的。

**核心理念**：XML 定义"数据是什么"，C# 代码定义"行为怎么做"。大部分内容型 mod 只需要 XML。

## Def 类型速查表

| Def 类型 | 用途 | 文件通常位置 |
|----------|------|-------------|
| `ThingDef` | 物品、建筑、植物、生物 | `Defs/ThingDefs/` |
| `RecipeDef` | 工作台配方 | `Defs/RecipeDefs/` |
| `ResearchDef` | 科技树节点 | `Defs/ResearchDefs/` |
| `HediffDef` | 健康状态/效果 | `Defs/HediffDefs/` |
| `TraitDef` | 角色特质 | `Defs/TraitDefs/` |
| `FactionDef` | 派系定义 | `Defs/FactionDefs/` |
| `IncidentDef` | 随机事件 | `Defs/IncidentDefs/` |
| `SoundDef` | 音效 | `Defs/SoundDefs/` |
| `DamageDef` | 伤害类型 | `Defs/DamageDefs/` |
| `JobDef` | 工作类型 | `Defs/JobDefs/` |
| `ThoughtDef` | 想法/心情 | `Defs/ThoughtDefs/` |
| `TerrainDef` | 地形 | `Defs/TerrainDefs/` |
| `WeatherDef` | 天气 | `Defs/WeatherDefs/` |

## ThingDef 详解

`ThingDef` 是最常用的 Def 类型，覆盖物品、建筑、植物等。

### 关键标签

#### 基础信息
```xml
<ThingDef ParentName="BaseWeapon">  <!-- 继承 BaseWeapon 的默认属性 -->
  <defName>SR_PlasmaSword</defName>    <!-- 唯一 ID -->
  <label>plasma sword</label>          <!-- 游戏内显示名 -->
  <description>A sword made of superheated plasma.</description>
  <category>Item</category>            <!-- Item | Building | Plant | Pawn -->
```

#### 物品分类
```xml
  <thingCategories>
    <li>WeaponsMelee</li>              <!-- 所属分类，决定在哪个库存区显示 -->
  </thingCategories>
```

#### 市场价值
```xml
  <statBases>
    <MarketValue>500</MarketValue>     <!-- 基础市场价值（银） -->
    <Mass>2.5</Mass>                   <!-- 重量（kg） -->
    <MaxHitPoints>150</MaxHitPoints>   <!-- 耐久度 -->
    <Flammability>0</Flammability>     <!-- 可燃性（0-1） -->
  </statBases>
```

#### 制作成本
```xml
  <costList>
    <Plasteel>60</Plasteel>            <!-- 所需材料数量 -->
    <ComponentIndustrial>3</ComponentIndustrial>
  </costList>
```

#### 战斗属性（武器）
```xml
  <weaponTags>
    <li>SR_Plasma</li>
  </weaponTags>
  <tools>
    <li>
      <label>edge</label>              <!-- 攻击部位标签 -->
      <capacities>
        <li>Cut</li>                   <!-- 伤害类型：Cut/Blunt/Stab -->
        <li>Stab</li>
      </capacities>
      <power>20</power>                <!-- 基础伤害 -->
      <cooldownTime>1.5</cooldownTime> <!-- 冷却时间（秒） -->
    </li>
  </tools>
```

#### 组件系统（Comps）
```xml
  <comps>
    <!-- 可装备 -->
    <li Class="CompProperties_Equippable">
      <slotGroup>Weapon</slotGroup>
    </li>
    <!-- 可制作（需要研究前置） -->
    <li Class="CompProperties_CompUsable">
      <useLabel>Equip</useLabel>
    </li>
  </comps>
```

#### 贴图
```xml
  <graphicData>
    <texPath>Things/Item/SR_PlasmaSword</texPath>    <!-- 贴图路径：Textures/ 下 -->
    <graphicClass>Graphic_Single</graphicClass>      <!-- 单张贴图 -->
    <shaderType>CutoutComplex</shaderType>           <!-- 着色器类型 -->
  </graphicData>
```

#### 建筑特殊标签
```xml
  <ThingDef ParentName="BuildingBase">
    <defName>SR_ArcFurnace</defName>
    <category>Building</category>
    <size>(3,2)</size>               <!-- 占地面积（宽, 高） -->
    <designationCategory>Production</designationCategory> <!-- 建造菜单分类 -->
    <passability>Impassable</passability>           <!-- 通过性 -->
    <fillPercent>0.85</fillPercent>                 <!-- 贴图填充率 -->
    <terrainAffordanceNeeded>Heavy</terrainAffordanceNeeded> <!-- 地形要求 -->
    <statBases>
      <WorkToBuild>5000</WorkToBuild>               <!-- 建造工作量 -->
    </statBases>
  </ThingDef>
```

## ParentName 继承机制

RimWorld 使用 `ParentName` 实现 Def 继承，减少重复代码。

**原版继承链示例：**
```
BaseWeapon → BaseMeleeWeapon → 你的武器
BaseWeapon → BaseRangedWeapon → 你的枪
BaseBuilding → BuildingBase → 你的建筑
```

**查看继承定义**：在 `RimWorld/Data/Core/Defs/ThingDefs/` 中搜索 `ParentName="BaseMeleeWeapon"` 查看其定义。

## MayRequire / MayRequireAnyOf（条件加载）

按 DLC 存在性决定是否加载 Def：

```xml
<!-- 仅 Biotech 激活时加载 -->
<ThingDef MayRequire="ludeon.rimworld.biotech" ParentName="BaseWeapon">
  ...
</ThingDef>

<!-- Biotech 或 Ideology 任一激活时加载 -->
<ThingDef MayRequireAnyOf="ludeon.rimworld.biotech, ludeon.rimworld.ideology">
  ...
</ThingDef>
```

## 完整示例：等离子长剑

```xml
<?xml version="1.0" encoding="utf-8"?>
<Defs>
  <!-- 一把自定义近战武器：等离子长剑 -->
  <ThingDef ParentName="BaseMeleeWeapon">
    <defName>SR_PlasmaSword</defName>
    <label>plasma sword</label>
    <description>A high-tech blade that cuts through armor with superheated plasma.</description>

    <category>Item</category>
    <thingCategories>
      <li>WeaponsMelee</li>
    </thingCategories>

    <statBases>
      <MarketValue>800</MarketValue>
      <Mass>2.0</Mass>
      <MaxHitPoints>200</MaxHitPoints>
      <Flammability>0</Flammability>
      <DeteriorationRate>0.5</DeteriorationRate>
    </statBases>

    <costList>
      <Plasteel>50</Plasteel>
      <ComponentSpacer>2</ComponentSpacer>
    </costList>

    <weaponTags>
      <li>SR_Plasma</li>
    </weaponTags>

    <tools>
      <li>
        <label>edge</label>
        <capacities>
          <li>Cut</li>
          <li>Stab</li>
        </capacities>
        <power>22</power>
        <cooldownTime>1.3</cooldownTime>
        <armorPenetration>0.35</armorPenetration>
      </li>
    </tools>

    <comps>
      <li Class="CompProperties_Equippable">
        <slotGroup>Weapon</slotGroup>
      </li>
    </comps>

    <graphicData>
      <texPath>Things/Item/SR_PlasmaSword</texPath>
      <graphicClass>Graphic_Single</graphicClass>
      <shaderType>CutoutComplex</shaderType>
    </graphicData>

    <!-- 关联配方（见 RecipeDef） -->
    <recipeMaker>
      <researchPrerequisite>SR_PlasmaForging</researchPrerequisite>
      <skillRequirements>
        <Crafting>8</Crafting>
      </skillRequirements>
      <workAmount>12000</workAmount>
    </recipeMaker>
  </ThingDef>
</Defs>
```

## 常见问题

### Q: 我的物品在游戏中不显示？
1. 检查 `texPath` 是否正确指向 `Textures/` 下的路径（不含 `Textures/` 前缀）
2. 确保贴图是 PNG 格式
3. 检查 `graphicClass` 是否匹配（单张贴图用 `Graphic_Single`）

### Q: defName 冲突怎么办？
始终使用你的专属前缀。如果仍然冲突，检查其他 mod 是否用了相同前缀。

### Q: 如何找到某个标签有哪些合法值？
在 `RimWorld/Data/Core/Defs/` 中搜索类似 Def，查看原版的写法。
```

- [ ] **Step 2: 验证**

```bash
wc -l "$HOME/.claude/skills/rimworld-modding/references/03-xml-defs.md"
```

Expected: 此文件较长，约 200-250 行。

---

### Task 6: 编写 references/06-harmony.md（Harmony 补丁）

**Files:**
- Create: `~/.claude/skills/rimworld-modding\references\06-harmony.md`

- [ ] **Step 1: 写入文件**

```markdown
# 06 — Harmony 补丁

> **适用版本**: RimWorld 1.6（Harmony 2.x） | **最后更新**: 2026-05-31

## 概述

Harmony 是 RimWorld mod 社区的标准代码补丁库。它让你**在运行时**修改原版代码或其它 mod 的行为，而不需要修改原始 DLL 文件——避免了 mod 之间的冲突。

**使用场景**：
- 修改某个方法的返回值
- 在某个方法执行前后插入自己的逻辑
- 完全替换某个方法的实现
- 修改 AI 行为、战斗计算、生成逻辑等

## 基础架构

### 入口类

```csharp
using Verse;
using HarmonyLib;
using System.Reflection;

namespace SR.YourModName
{
    [StaticConstructorOnStartup]  // 游戏启动时自动执行静态构造函数
    public static class HarmonyPatches
    {
        private static readonly Harmony instance;

        static HarmonyPatches()
        {
            instance = new Harmony("SR.YourModName");
            instance.PatchAll(Assembly.GetExecutingAssembly());
            Log.Message("SR.YourModName: Harmony patches applied.");
        }
    }
}
```

**关键点**：
- `[StaticConstructorOnStartup]` 确保在游戏加载后、主菜单显示前执行
- `"SR.YourModName"` 是 Harmony ID，**必须全局唯一**
- `PatchAll()` 自动扫描当前程序集中所有带 `[HarmonyPatch]` 特性的类

## 三种补丁类型

### 1. Prefix（前置拦截——最常用）

在原始方法执行**之前**运行。可以：
- 修改传入参数（通过 `ref`）
- 阻止原始方法执行（返回 `false`）
- 提前设置返回值

```csharp
[HarmonyPatch(typeof(Pawn), "Kill")]
public static class Patch_Pawn_Kill
{
    [HarmonyPrefix]
    public static bool Prefix(Pawn __instance, DamageInfo? dinfo, ref Hediff exactCulprit)
    {
        // 阻止特定 Pawn 被杀死
        if (__instance.def.defName == "SR_Immortal")
        {
            return false;  // 返回 false = 跳过原始方法
        }
        return true;  // 返回 true = 继续执行原始方法
    }
}
```

### 2. Postfix（后置拦截）

在原始方法执行**之后**运行。可以：
- 读取/修改返回值（通过 `ref __result`）
- 读取 `__state`（Prefix 传来的数据）

```csharp
[HarmonyPatch(typeof(Thing), "TakeDamage")]
public static class Patch_Thing_TakeDamage
{
    [HarmonyPostfix]
    public static void Postfix(Thing __instance, ref DamageInfo dinfo)
    {
        // 记录所有受到伤害的对象和伤害值
        Log.Message($"{__instance.Label} took {dinfo.Amount} damage from {dinfo.Instigator}");
    }
}
```

### 3. Transpiler（IL 级别修改——高级）

直接修改方法的 IL 中间码。除非你非常了解 IL，否则优先使用 Prefix/Postfix 组合。

```csharp
[HarmonyPatch(typeof(TargetClass), "TargetMethod")]
public static class Patch_Transpiler
{
    [HarmonyTranspiler]
    public static IEnumerable<CodeInstruction> Transpiler(IEnumerable<CodeInstruction> instructions)
    {
        // 修改 IL 指令序列
        // 高级用法，新手可跳过
        return instructions;
    }
}
```

## 特殊参数

Harmony 通过**参数名**自动注入以下值：

| 参数名 | 类型 | 说明 | 用于 |
|--------|------|------|------|
| `__instance` | 原始类的类型 | 调用方法的实例（静态方法为 null） | Prefix/Postfix |
| `__result` | 原始返回类型（加 `ref`） | 原始方法的返回值，可修改 | Postfix（读/写）, Prefix（提前设值） |
| `__state` | 任意类型 | Prefix 传给 Postfix 的桥梁 | Prefix（赋值）+ Postfix（读取） |
| `___paramName` | 参数类型（加 `ref`） | 原始方法的参数（三个下划线前缀） | Prefix（修改参数值） |

## 常见实战模式

### 模式 1：修改配方产出

```csharp
[HarmonyPatch(typeof(GenRecipe), "PostProcessProduct")]
public static class Patch_GenRecipe_PostProcessProduct
{
    [HarmonyPostfix]
    public static void Postfix(ref Thing product, RecipeDef recipeDef, Pawn worker)
    {
        // 如果制作者是 SR_ 特殊角色，产出品质提升
        if (worker?.def.defName == "SR_MasterCrafter")
        {
            if (product.TryGetComp<CompQuality>() is CompQuality qc)
            {
                qc.SetQuality(QualityCategory.Legendary, ArtGenerationContext.Outsider);
            }
        }
    }
}
```

### 模式 2：修改 AI 行为

```csharp
[HarmonyPatch(typeof(JobGiver_Work), "TryIssueJobPackage")]
public static class Patch_JobGiver_Work
{
    [HarmonyPrefix]
    public static bool Prefix(Pawn pawn, ref ThinkResult __result)
    {
        // 如果是 SR_ 特殊角色，禁止自动工作
        if (pawn.def.defName == "SR_LazyPawn" && Rand.Value < 0.5f)
        {
            __result = ThinkResult.NoJob;
            return false;
        }
        return true;
    }
}
```

### 模式 3：拦截事件触发

```csharp
[HarmonyPatch(typeof(IncidentWorker_Raid), "TryExecuteWorker")]
public static class Patch_Raid
{
    [HarmonyPrefix]
    public static bool Prefix(IncidentParms parms)
    {
        // 如果 mod 设置中禁用了袭击，阻止事件
        if (ModSettings_SR.disableRaids)
        {
            return false;
        }
        return true;
    }
}
```

## Harmony ID 冲突

如果两个 mod 同时 patch 同一个方法且使用相同的 Harmony ID 前缀，可能冲突。

**解决**：确保你的 `new Harmony("ID")` 中的 ID 与 packageId 类似（如 `yourname.modname`）。

## 调试 Harmony 补丁

1. 在 Prefix/Postfix 开头添加 `Log.Message()` 确认补丁被调用
2. 开启 RimWorld Dev Mode → 查看控制台输出
3. 检查 `Player.log`（路径见 `references/08-debugging.md`）

## 与 XML Patch 的对比

| | XML PatchOperations | Harmony |
|------|------|------|
| 修改数据 | ✅ | 不适用 |
| 修改行为/逻辑 | ❌ | ✅ |
| 冲突风险 | 低 | 中（同方法多 patch） |
| 学习难度 | 低 | 中高 |
| 需要编译 | 不需要 | 需要 |
```

- [ ] **Step 2: 验证**

```bash
wc -l "$HOME/.claude/skills/rimworld-modding/references/06-harmony.md"
```

---

### Task 7: 编写 references/08-debugging.md（调试与排错）

**Files:**
- Create: `~/.claude/skills/rimworld-modding\references\08-debugging.md`

- [ ] **Step 1: 写入文件**

```markdown
# 08 — 调试与排错

> **适用版本**: RimWorld 1.6 | **最后更新**: 2026-05-31

## 开发者模式

### 启用方式
1. 游戏主菜单 → **选项（Options）**
2. 勾选 **"开发者模式（Development Mode）"**
3. 屏幕顶部出现一排开发工具按钮

### 常用开发工具
- **Open Debug Actions Menu**（⚙️ 图标）→ 最常用的工具集
  - `Spawn Thing` — 直接生成物品测试
  - `Execute Incident` — 触发任意事件
  - `Apply Damage` — 对选中对象施加伤害
  - `Give Hediff` — 施加健康效果
- **Open Debug Log** — 查看实时日志
- **God Mode** — 无敌模式 + 免费建造

## 日志文件

### Player.log 位置

| 系统 | 路径 |
|------|------|
| Windows | `%USERPROFILE%\AppData\LocalLow\Ludeon Studios\RimWorld by Ludeon Studios\Player.log` |
| Linux | `~/.config/unity3d/Ludeon Studios/RimWorld by Ludeon Studios/Player.log` |
| macOS | `~/Library/Logs/Ludeon Studios/RimWorld by Ludeon Studios/Player.log` |

### 日志解读

```
[SR.YourModName] Harmony patches applied.     ← 你的 mod 正常启动
Could not resolve cross-reference to ...      ← XML Def 引用错误
NullReferenceException: Object reference not set  ← C# 空引用错误
```

### 输出自定义日志

```csharp
// 信息级别
Log.Message($"SR: Processing {thing.Label}");

// 警告级别（黄色）
Log.Warning($"SR: Missing texture for {thing.def.defName}");

// 错误级别（红色）
Log.Error($"SR: Failed to load {thing.def.defName}, reason: {ex.Message}");
```

## 常见错误速查

### 🔴 红字错误（游戏内弹窗）

| 错误信息 | 可能原因 | 解决方法 |
|----------|---------|---------|
| `Could not resolve cross-reference to ...` | defName 拼写错误或目标 Def 不存在 | 检查 XML 中的 defName 引用，确认目标 Def 已加载 |
| `Could not find type ...` | C# 类名错误或 DLL 未加载 | 检查 XML 中的 `Class=` 属性，确认 DLL 在 Assemblies/ 中 |
| `XML error: unexpected token` | XML 语法错误（标签未闭合） | 用 XML 验证器检查文件格式 |
| `Duplicate defName: ...` | 两个 Def 使用了相同的 defName | 确保你的前缀是唯一的 |

### ⬜ 白窗/灰窗（游戏加载时卡住）

1. **最近安装的 mod 冲突**——二分法排查：禁用一半 mod，逐步缩小范围
2. **XML 解析错误**——检查最后修改的 XML 文件是否有标签未闭合
3. **DLL 依赖缺失**——确认所有引用的 DLL 都已正确打包

### ❌ NullReferenceException

最常见的 C# 错误。原因：访问了为 `null` 的对象。

```csharp
// ❌ 危险写法
Pawn pawn = Find.AnyThing<Pawn>();
pawn.health.AddHediff(someHediff);  // pawn 可能为 null

// ✅ 安全写法
Pawn pawn = Find.AnyThing<Pawn>();
if (pawn != null)
{
    pawn.health.AddHediff(someHediff);
}
// 或使用模式匹配
if (Find.AnyThing<Pawn>() is Pawn pawn)
{
    pawn.health.AddHediff(someHediff);
}
```

## 隔离测试流程

当怀疑是 mod 冲突时：

1. 只加载你的 mod + Harmony + Core
2. 确认问题是否复现
   - **不复现** → mod 冲突，二分法找出冲突 mod
   - **复现** → 你的 mod 有 bug，进入下一步
3. 查看 Player.log，搜索你的 mod 前缀
4. 在可疑代码处加入 `Log.Message()` 输出变量值
5. 逐步缩小问题范围

## 开发中快速重载

- 修改 XML → 不需要重启游戏，在主菜单点击 **"Reset Mods"** 或直接开始新游戏
- 修改 C# 代码 → 必须重新编译 + 重启游戏
- 修改纹理 → 直接替换文件，游戏可能缓存需要重启

## 常见问题 FAQ

### Q: 为什么我的 mod 在 Mod 列表中不显示？
检查 About.xml 是否语法正确，`packageId` 是否与其他 mod 重复。

### Q: 开发模式下物品怎么生成？
Open Debug Actions Menu → Spawn Thing → 搜索你的物品 defName → 点击生成。

### Q: Harmony 补丁没有生效？
1. 确认 `[StaticConstructorOnStartup]` 类被正确调用（检查 Log.Message 输出）
2. 确认 patch 类的访问修饰符是 `public static`
3. 确认补丁所在的 DLL 在 Assemblies/ 中
```

- [ ] **Step 2: 验证**

```bash
wc -l "$HOME/.claude/skills/rimworld-modding/references/08-debugging.md"
```

---

### Task 8: 编写模板文件（3 个）

**Files:**
- Create: `~/.claude/skills/rimworld-modding\templates\weapon-melee.xml`
- Create: `~/.claude/skills/rimworld-modding\templates\weapon-ranged.xml`
- Create: `~/.claude/skills/rimworld-modding\templates\harmony-patch.cs`

- [ ] **Step 1: 写入 templates/weapon-melee.xml**

```xml
<?xml version="1.0" encoding="utf-8"?>
<!--
  近战武器模板
  替换所有 <Your...> 占位符为你的实际值
  前缀 <YourPrefix> 示例：SR → SR_Weapon_PlasmaSword
-->
<Defs>
  <ThingDef ParentName="BaseMeleeWeapon">
    <defName><YourPrefix>_Weapon_<YourName></defName>
    <label><your weapon label></label>
    <description><your weapon description></description>

    <thingCategories>
      <li>WeaponsMelee</li>
    </thingCategories>

    <statBases>
      <MarketValue>200</MarketValue>           <!-- 基础市场价值（银） -->
      <Mass>2.0</Mass>                          <!-- 重量（kg） -->
      <MaxHitPoints>150</MaxHitPoints>          <!-- 耐久度 -->
      <Flammability>0</Flammability>
    </statBases>

    <costList>
      <Steel>40</Steel>                         <!-- 制作所需材料 -->
    </costList>

    <weaponTags>
      <li><YourPrefix>_<YourTag></li>           <!-- 武器标签，用于文化/角色偏好 -->
    </weaponTags>

    <tools>
      <li>
        <label>edge</label>
        <capacities>
          <li>Cut</li>                          <!-- 伤害类型: Cut/Blunt/Stab/Poke -->
        </capacities>
        <power>15</power>                       <!-- 基础伤害值 -->
        <cooldownTime>1.6</cooldownTime>        <!-- 攻击冷却（秒） -->
        <armorPenetration>0.15</armorPenetration> <!-- 护甲穿透（0-1） -->
      </li>
    </tools>

    <comps>
      <li Class="CompProperties_Equippable">
        <slotGroup>Weapon</slotGroup>
      </li>
    </comps>

    <graphicData>
      <texPath>Things/Item/<YourPrefix>_<YourTexture></texPath>
      <graphicClass>Graphic_Single</graphicClass>
      <shaderType>CutoutComplex</shaderType>
    </graphicData>

    <recipeMaker>
      <workAmount>6000</workAmount>             <!-- 制作所需工作量 -->
    </recipeMaker>
  </ThingDef>
</Defs>
```

- [ ] **Step 2: 写入 templates/weapon-ranged.xml**

```xml
<?xml version="1.0" encoding="utf-8"?>
<!--
  远程武器模板
  替换所有 <Your...> 占位符为你的实际值
-->
<Defs>
  <ThingDef ParentName="BaseRangedWeapon">
    <defName><YourPrefix>_Gun_<YourName></defName>
    <label><your gun label></label>
    <description><your gun description></description>

    <thingCategories>
      <li>WeaponsRanged</li>
    </thingCategories>

    <statBases>
      <MarketValue>300</MarketValue>
      <Mass>3.0</Mass>
      <MaxHitPoints>120</MaxHitPoints>
      <Flammability>0.5</Flammability>
      <AccuracyTouch>0.75</AccuracyTouch>
      <AccuracyShort>0.85</AccuracyShort>
      <AccuracyMedium>0.70</AccuracyMedium>
      <AccuracyLong>0.50</AccuracyLong>
    </statBases>

    <costList>
      <Steel>60</Steel>
      <ComponentIndustrial>2</ComponentIndustrial>
    </costList>

    <weaponTags>
      <li><YourPrefix>_<YourTag></li>
    </weaponTags>

    <!-- 远程特有属性 -->
    <verbClass>Verb_Shoot</verbClass>
    <rangedWeapon_Cooldown>1.2</rangedWeapon_Cooldown>   <!-- 两次射击间隔（秒） -->
    <rangedWeapon_WarmupTime>1.0</rangedWeapon_WarmupTime> <!-- 瞄准时间（秒） -->
    <rangedWeapon_Range>25</rangedWeapon_Range>            <!-- 射程（格） -->

    <comps>
      <li Class="CompProperties_Equippable">
        <slotGroup>Weapon</slotGroup>
      </li>
      <!-- 需要弹药（可选） -->
      <!--
      <li Class="CompProperties_Reloadable">
        <ammoDef><YourPrefix>_Bullet</ammoDef>
        <maxCharges>6</maxCharges>
      </li>
      -->
    </comps>

    <graphicData>
      <texPath>Things/Item/<YourPrefix>_<YourTexture></texPath>
      <graphicClass>Graphic_Single</graphicClass>
      <shaderType>CutoutComplex</shaderType>
    </graphicData>

    <recipeMaker>
      <workAmount>8000</workAmount>
    </recipeMaker>
  </ThingDef>
</Defs>
```

- [ ] **Step 3: 写入 templates/harmony-patch.cs**

```csharp
// Harmony 补丁模板
// 替换 <YourNamespace> 和 <YourModID> 为你的实际值
// 使用方法：
//   1. 替换 TargetClass 为目标类名（用 dnSpy 或 RimSage 查找）
//   2. 替换 TargetMethod 为目标方法名
//   3. 根据需要选择 Prefix / Postfix / Transpiler
//   4. 实现你的 patch 逻辑

using Verse;
using HarmonyLib;
using System.Reflection;

namespace <YourNamespace>
{
    /// <summary>
    /// Harmony 补丁入口——游戏启动时自动加载所有补丁
    /// </summary>
    [StaticConstructorOnStartup]
    public static class HarmonyPatches
    {
        private static readonly Harmony instance;

        static HarmonyPatches()
        {
            // Harmony ID 必须全局唯一，建议使用 packageId 格式
            instance = new Harmony("<YourModID>");
            instance.PatchAll(Assembly.GetExecutingAssembly());
            Log.Message("<YourModID>: All Harmony patches applied successfully.");
        }
    }

    /// <summary>
    /// 示例：对 TargetClass.TargetMethod 进行 Prefix 拦截
    /// </summary>
    // [HarmonyPatch(typeof(TargetClass), "TargetMethod")]
    public static class Patch_TargetClass_TargetMethod
    {
        /// <summary>
        /// Prefix：在原方法执行前运行
        /// 返回 false = 跳过原方法
        /// 返回 true  = 继续执行原方法
        /// </summary>
        [HarmonyPrefix]
        public static bool Prefix(/* 原始参数列表 */)
        {
            // TODO: 在此编写前置逻辑

            return true;  // 允许原方法继续执行
        }

        /// <summary>
        /// Postfix：在原方法执行后运行
        /// 可以读取和修改 __result（原方法的返回值）
        /// </summary>
        // [HarmonyPostfix]
        // public static void Postfix(/* 原始参数列表 */, ref <ReturnType> __result)
        // {
        //     // TODO: 在此编写后置逻辑
        // }

        /// <summary>
        /// Transpiler：直接修改 IL 代码（高级用法）
        /// </summary>
        // [HarmonyTranspiler]
        // public static IEnumerable<CodeInstruction> Transpiler(IEnumerable<CodeInstruction> instructions)
        // {
        //     // TODO: 在此编写 IL 修改逻辑
        //     return instructions;
        // }
    }
}
```

- [ ] **Step 4: 验证所有模板文件**

```bash
ls -la "$HOME/.claude/skills/rimworld-modding/templates/"
```

Expected: weapon-melee.xml, weapon-ranged.xml, harmony-patch.cs 三个文件均存在。

---

### Task 9: 编写 workflows/new-mod.md（新建 mod 工作流）

**Files:**
- Create: `~/.claude/skills/rimworld-modding\workflows\new-mod.md`

- [ ] **Step 1: 写入文件**

```markdown
# 工作流：从零创建一个新 Mod

> 适用：第一次做 RimWorld mod，或开始一个全新项目

## 概述

按以下步骤操作，你将得到一个可被游戏加载的基本 mod 骨架。

## 步骤

### 第 1 步：确定 Mod 信息

在开始之前，确定以下内容：

| 项目 | 示例 | 说明 |
|------|------|------|
| Mod 名称 | My Awesome Mod | 游戏内显示名称 |
| packageId | yourname.awesomemod | 全小写无空格，全局唯一 |
| 前缀 | AWE_ | 2-4 字符，用于 defName |
| 作者 | Your Name | |
| 目标版本 | 1.6 | |
| namespace | AWE.MyAwesomeMod | C# 命名空间 |

### 第 2 步：创建目录结构

在 `<RimWorld 安装目录>/Mods/` 下创建 mod 文件夹：

```
<YourModName>/
├── About/
├── Defs/
│   └── ThingDefs/
├── Patches/
├── Textures/
│   └── Things/
│       └── Item/
└── Languages/
    └── English/
        └── Keyed/
```

### 第 3 步：编写 About.xml

在 `About/` 目录下创建 `About.xml`（详见 `references/02-project-structure.md`）。

### 第 4 步：创建第一个 Def

在 `Defs/ThingDefs/` 下创建你的第一个 XML 文件。

- 如果做**武器**：参考 `templates/weapon-melee.xml` 或 `templates/weapon-ranged.xml`
- 如果做**建筑**：参考 `references/03-xml-defs.md` 中建筑部分
- 详细 Def 系统参考：`references/03-xml-defs.md`

### 第 5 步：（可选）添加贴图

- 格式：PNG
- 路径：`Textures/Things/Item/<YourTexture>.png`
- 武器推荐尺寸：128×128 或 256×256
- 在 Def 的 `<texPath>` 中引用时去掉 `Textures/` 前缀和 `.png` 后缀

### 第 6 步：测试

1. 启动 RimWorld
2. Mod 列表中找到你的 mod → 勾选启用
3. 开始新游戏（或加载存档）
4. 启用 Developer Mode（`references/08-debugging.md`）
5. Open Debug Actions Menu → Spawn Thing → 搜索你的物品 defName
6. 确认物品正常显示和工作

### 第 7 步：（可选）添加 C# 代码

如果 mod 需要 C# 逻辑：

1. 创建 VS 项目（Class Library, .NET Framework 4.7.2）
2. 引用必要 DLL（`references/01-environment.md`）
3. 编写代码（参考 `references/05-csharp-basics.md`）
4. 编译后将 DLL 复制到 `Assemblies/` 目录
5. 重启游戏测试

### 第 8 步：（可选）发布到 Workshop

详见 `references/09-workshop.md`。

## 检查清单

- [ ] About.xml 填写完整且语法正确
- [ ] 目录结构符合标准
- [ ] 至少有一个 Def（物品/建筑）
- [ ] 在开发者模式下成功生成并看到你的物品
- [ ] defName 使用唯一前缀，无冲突
```

- [ ] **Step 2: 验证**

```bash
wc -l "$HOME/.claude/skills/rimworld-modding/workflows/new-mod.md"
```

---

### Task 10: 编写 workflows/debug-crash.md（调试工作流）

**Files:**
- Create: `~/.claude/skills/rimworld-modding\workflows\debug-crash.md`

- [ ] **Step 1: 写入文件**

```markdown
# 工作流：排查崩溃/报错

> 适用：mod 加载时报错、游戏中出现红字/白窗、游戏崩溃

## 快速决策树

```
游戏/Mod 出现问题
│
├─ 游戏加载时卡住/白窗？
│   ├─ 关闭所有 mod，只开你的 → 正常？ → mod 冲突，二分法排查
│   └─ 只开你的也卡住 → XML 语法错误 → 用 XML 验证器检查
│
├─ 弹出红字错误？
│   ├─ "Could not resolve cross-reference" → 检查 defName 引用
│   ├─ "Could not find type" → 检查 Class= 属性 / DLL 是否正确加载
│   ├─ "Duplicate defName" → 改前缀，确保全局唯一
│   └─ NullReferenceException → 查看日志堆栈，定位具体行
│
├─ Mod 列表中看不到你的 mod？
│   └─ 检查 About.xml 语法 + packageId 是否重复
│
└─ 游戏中行为异常（但不报错）？
    ├─ 在可疑代码中加入 Log.Message() 输出变量值
    ├─ 用开发者模式手动测试每个功能
    └─ 检查 Harmony 补丁是否成功加载（看日志中你的 Log.Message）
```

## 二分法排查 Mod 冲突

1. 禁用所有 mod，只留 Core + Harmony + 你的 mod
2. **问题消失？** → 是 mod 冲突
3. 启用一半 mod，测试
4. 反复二分，直到找到冲突 mod
5. 查看冲突 mod 是否 patch 了相同的类/方法

## 常用调试命令（开发者控制台）

在开发者模式下按 `` ` ``（反引号）打开开发者控制台：

| 命令 | 作用 |
|------|------|
| `list defs ThingDef` | 列出所有 ThingDef |
| `list defs <YourPrefix>` | 列出你的 mod 的 Def |
| `spawn <defName>` | 生成指定物品 |

## 获取帮助时应该提供的信息

在贴吧/论坛/Discord 求助时，附上以下内容有助于快速定位问题：

1. **Player.log** 完整内容（使用 Pastebin 等工具上传）
2. **你的 mod 的 About.xml**
3. **出错相关代码**（XML 片段或 C# 代码）
4. **其他已加载 mod 列表**
5. **复现步骤**：做了什么操作触发了问题？
```

- [ ] **Step 2: 验证**

```bash
wc -l "$HOME/.claude/skills/rimworld-modding/workflows/debug-crash.md"
```

---

### Task 11: Phase 1 完成验证

- [ ] **Step 1: 检查所有 Phase 1 文件存在**

```bash
echo "=== 检查文件结构 ===" && \
find "$HOME/.claude/skills/rimworld-modding" -type f | sort && \
echo "=== 总文件数 ===" && \
find "$HOME/.claude/skills/rimworld-modding" -type f | wc -l && \
echo "=== 总行数 ===" && \
find "$HOME/.claude/skills/rimworld-modding" -type f -exec wc -l {} + | tail -1
```

Expected: 11 个文件（1 SKILL.md + 5 references + 3 templates + 2 workflows），总计约 1500-2000 行。

- [ ] **Step 2: 手动验证 SKILL.md 触发机制**（在 Claude Code 中测试）

在 Claude Code 中输入以下测试语句，确认 skill 被触发：
- "我要做一个 RimWorld mod"
- "帮我加一把环世界武器"
- "怎么用 Harmony 改 RimWorld 的方法"

Expected: skill 被加载，显示 SKILL.md 的快速导航内容。

---

## Phase 2: 完整覆盖

> Phase 2 补充剩余 5 个 reference、3 个 template、3 个 workflow，并执行 TDD 压力测试。

---

### Task 12: references/04-xml-patching.md（XML PatchOperations）

**Files:**
- Create: `~/.claude/skills/rimworld-modding\references\04-xml-patching.md`

- [ ] **Step 1: 写入**

内容覆盖：
- XPath 选择器语法（`/Defs`, `[defName="xxx"]`, `/li[1]` 等）
- 5 种 Patch 操作：`PatchOperationAdd`, `PatchOperationRemove`, `PatchOperationReplace`, `PatchOperationSet`, `PatchOperationInsert`
- 条件补丁：`PatchOperationConditional`
- 按名查找：`PatchOperationFindMod`
- 3 个实战示例：修改原版武器伤害、给原版工作台添加配方、替换原版建筑贴图
- 每个示例包含 `<Operation>` 标签完整代码

---

### Task 13: references/05-csharp-basics.md（C# Mod 开发）

**Files:**
- Create: `~/.claude/skills/rimworld-modding\references\05-csharp-basics.md`

- [ ] **Step 1: 写入**

内容覆盖：
- Mod 类继承 `Verse.Mod` + Settings
- ExposeData 实现存档兼容
- ThingComp 系统、CompProperties
- GameComponent / MapComponent / WorldComponent
- DefModExtension 自定义 Def 扩展字段
- 完整实例：一个带开关的 Mod + 存储自定义设置

---

### Task 14: references/07-assets.md（资源制作）

**Files:**
- Create: `~/.claude/skills/rimworld-modding\references\07-assets.md`

- [ ] **Step 1: 写入**

内容覆盖：
- 纹理格式（PNG, 推荐分辨率表）
- Mask 图层（用于染色和装备覆盖）
- 音效格式（WAV/OGG）与 SoundDef
- 路径约定
- 工具推荐：GIMP/Paint.NET（纹理）、Audacity（音效）

---

### Task 15: references/09-workshop.md（发布）

**Files:**
- Create: `~/.claude/skills/rimworld-modding\references\09-workshop.md`

- [ ] **Step 1: 写入**

内容覆盖：
- 准备上传（目录结构检查、About.xml 审查、Preview.png 640×360）
- Steam Workshop 上传流程（游戏内直接上传）
- 版本管理（语义化版本 `major.minor.patch`）
- Mod 描述最佳实践
- 兼容性声明格式
- 更新 changelog 格式

---

### Task 16: references/10-api-reference.md（API 速查）

**Files:**
- Create: `~/.claude/skills/rimworld-modding\references\10-api-reference.md`

- [ ] **Step 1: 写入**

内容覆盖：
- 常用命名空间：`Verse`, `RimWorld`, `RimWorld.Planet`
- 高频类速查：`Thing`, `Pawn`, `Map`, `Find`, `GenSpawn`, `GenRecipe`, `ThingDef`, `RecipeDef`
- 高频方法速查表（按用途分类：生成、查询、战斗、UI）
- 1.5→1.6 关键 API 变化（标注 "1.6 WIP"）
- 与 RimSage MCP 的分工说明

---

### Task 17: 补充模板文件

**Files:**
- Create: `~/.claude/skills/rimworld-modding\templates\building.xml`
- Create: `~/.claude/skills/rimworld-modding\templates\recipe.xml`
- Create: `~/.claude/skills/rimworld-modding\templates\thingcomp.cs`

- [ ] **Step 1: 写入 building.xml** — 建筑 Def 模板（含占地面积、建筑菜单分类、地形要求）
- [ ] **Step 2: 写入 recipe.xml** — 配方 Def 模板（含原料、产出、技能要求、研究前置）
- [ ] **Step 3: 写入 thingcomp.cs** — ThingComp 骨架模板（含 CompProperties、Tick 处理、ExposeData）

---

### Task 18: 补充工作流文件

**Files:**
- Create: `~/.claude/skills/rimworld-modding\workflows\add-item.md`
- Create: `~/.claude/skills/rimworld-modding\workflows\add-building.md`
- Create: `~/.claude/skills/rimworld-modding\workflows\patch-vanilla.md`

- [ ] **Step 1: 写入 add-item.md** — 添加物品的完整步骤（Def → 贴图 → 配方 → 测试）
- [ ] **Step 2: 写入 add-building.md** — 添加建筑的完整步骤
- [ ] **Step 3: 写入 patch-vanilla.md** — 修改原版的分步指南（XML Patch + Harmony 两种方式）

---

### Task 19: TDD 压力测试

**Files:**
- Create: `d:\WORK\docs\superpowers\plans\rimworld-modding-skill-test-results.md`

- [ ] **Step 1: 基线测试（RED）——无 Skill 时 subagent 表现**

对每个压力场景，用 subagent（不带 rimworld-modding skill）测试：

**场景 1**: "帮我创建一个新的 RimWorld mod 项目"
- 评估是否给出正确的目录结构、About.xml 模板、Def 示例
- 记录遗漏和错误

**场景 2**: "我想添加一把自定义近战武器，类似长剑但伤害更高"
- 评估是否给出完整可用的 ThingDef

**场景 3**: "如何用 Harmony 拦截 Pawn.Kill 方法，让某个角色不会死亡"
- 评估是否给出正确的 [StaticConstructorOnStartup] + HarmonyPrefix 代码

**场景 4**: "我的 mod 报红字 Could not resolve cross-reference 怎么排查"
- 评估是否给出正确的调试流程

**场景 5**: "如何把我的 mod 发布到 Steam Workshop"
- 评估是否给出完整发布步骤

每个场景记录：
- ❌ 错误/遗漏
- ✅ 正确的部分
- 📝 改进建议

- [ ] **Step 2: 安装 Skill 后测试（GREEN）**

在 subagent 中加载 rimworld-modding skill，重新运行 5 个场景，对比：
- 所有 ❌ 是否修复
- 输出是否更完整/准确
- 是否出现了新的错误

- [ ] **Step 3: 重构循环**

根据 GREEN 阶段发现的遗漏：
1. 补充 references/ 中缺失的知识点
2. 优化 SKILL.md 的意图路由
3. 重新验证 → 直到 5 个场景全部通过

- [ ] **Step 4: 记录测试结果**

在 `d:\WORK\docs\superpowers\plans\rimworld-modding-skill-test-results.md` 中记录每个场景的 RED/GREEN 对比。

---

### Task 20: 最终验证

- [ ] **Step 1: 完整文件清单确认**

```bash
echo "=== rimworld-modding Skill 完整文件清单 ===" && \
find "$HOME/.claude/skills/rimworld-modding" -type f | sort && \
echo "" && \
echo "=== 各目录文件数 ===" && \
echo "references: $(find $HOME/.claude/skills/rimworld-modding/references -type f | wc -l)" && \
echo "templates: $(find $HOME/.claude/skills/rimworld-modding/templates -type f | wc -l)" && \
echo "workflows: $(find $HOME/.claude/skills/rimworld-modding/workflows -type f | wc -l)" && \
echo "" && \
echo "=== 总行数 ===" && \
find "$HOME/.claude/skills/rimworld-modding" -type f -exec wc -l {} + | tail -1
```

Expected:
- 总文件数：21（1 SKILL.md + 10 references + 6 templates + 5 workflows）- 准确来说是 22 个文件，算上 SKILL.md
- references: 10
- templates: 6
- workflows: 5
- 总行数：约 3000-4000

但等等，我们的 template 列表只有 6 个（weapon-melee.xml, weapon-ranged.xml, harmony-patch.cs, building.xml, recipe.xml, thingcomp.cs），加上 workflows 5 个，references 10 个，SKILL.md 1 个 = 22 个文件。

- [ ] **Step 2: 上下文效率检查**

确认 SKILL.md 约 150 行，每个 reference 文件 < 300 行，确保 SKILL.md + 子文件 < 3000 行。

```bash
for f in $(find "$HOME/.claude/skills/rimworld-modding/references" -type f); do
  echo "$(wc -l < "$f") $f"
done
```

- [ ] **Step 3: 最终确认**

确认所有 Step 中的 TODO 占位符（如 `<YourNamespace>` 和 `<YourModID>`）是有意保留的模板占位符，而非未完成内容。
```

- [ ] **Step 2: 验证文件行数**

```bash
wc -l "d:\WORK\docs\superpowers\plans\2026-05-31-rimworld-modding-skill-plan.md"
```

Expected: ~400-600 行（包含 Phase 1 完整内容和 Phase 2 概要）。

---

## 附录：Phase 2 任务概要

> Phase 2 任务给出概要描述和文件路径。详细步骤（代码块、命令）在 Phase 1 完成后执行时补充。

### Task 12: references/04-xml-patching.md
**文件**: `~/.claude/skills/rimworld-modding\references\04-xml-patching.md`
**内容**: XPath 选择器语法、5 种 Patch 操作（Add/Remove/Replace/Set/Insert）、条件补丁、3 个实战示例（修改原版武器伤害、添加配方到原版工作台、替换建筑贴图）。每个示例用完整 `<Operation>` 标签。

### Task 13: references/05-csharp-basics.md
**文件**: `~/.claude/skills/rimworld-modding\references\05-csharp-basics.md`
**内容**: Mod 类 + Settings、ExposeData、ThingComp 系统、GameComponent/MapComponent/WorldComponent、DefModExtension、完整 Mod 示例代码。

### Task 14: references/07-assets.md
**文件**: `~/.claude/skills/rimworld-modding\references\07-assets.md`
**内容**: 纹理格式（PNG/尺寸）、Mask 图层、音效格式与 SoundDef、路径约定、工具推荐。

### Task 15: references/09-workshop.md
**文件**: `~/.claude/skills/rimworld-modding\references\09-workshop.md`
**内容**: 上传准备、Steam Workshop 流程、版本管理、描述最佳实践、兼容性声明、changelog 格式。

### Task 16: references/10-api-reference.md
**文件**: `~/.claude/skills/rimworld-modding\references\10-api-reference.md`
**内容**: 常用命名空间/类/方法速查表、1.5→1.6 变化、与 RimSage 分工说明。

### Task 17: 补充模板（3 个）
**文件**: `templates/building.xml`, `templates/recipe.xml`, `templates/thingcomp.cs`
**内容**: 建筑 Def 模板、配方 Def 模板、ThingComp 骨架。

### Task 18: 补充工作流（3 个）
**文件**: `workflows/add-item.md`, `workflows/add-building.md`, `workflows/patch-vanilla.md`
**内容**: 添加物品、添加建筑、修改原版的分步指南。

### Task 19: TDD 压力测试
**文件**: `d:\WORK\docs\superpowers\plans\rimworld-modding-skill-test-results.md`
**内容**: 5 个压力场景的 RED→GREEN→REFACTOR 测试记录。

### Task 20: 最终验证
确认 22 个文件齐全、行数合理、上下文效率合规。
