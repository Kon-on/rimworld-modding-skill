# 01 — 环境搭建

> **适用版本**: RimWorld 1.7（实测 1.7.4981 rev136） | **最后更新**: 2026-10-18

## 概述

RimWorld mod 开发需要以下工具链。根据你要做的 mod 类型选择安装：

| Mod 类型 | 必需工具 |
|----------|---------|
| 纯 XML（物品/建筑/配方） | 文本编辑器（VS Code） + RimPy |
| C# + Harmony | .NET SDK 10（`dotnet` 命令）+ 任意编辑器 |
| 资源制作 | GIMP / Paint.NET + Audacity |

> **1.7 起不再需要 Unity**：游戏引擎已换掉 Unity 运行时，Unity 类型由随游戏发布的兼容层提供（见下节）。

> **路径写法**：本技能与全仓库文档统一用占位符——`<游戏安装目录>`（游戏根目录，含 `Assembly-CSharp.dll`）、`<创意工坊目录>`（`<Steam 库>\steamapps\workshop\content\294100`）、`<仓库根>`（本仓库检出目录）；配套脚本用环境变量 `RIMWORLD_DIR` / `HARMONY_DIR`，未设置时按 Steam 注册表与库清单自动探测。

## 1.7 的环境变化（与 1.6 及更早版本的差异）

从 1.6 升级到 1.7 后，网上绝大多数教程与旧模板里的这几件事**已经全错**，先记住现实：

| 项目 | 1.6 及更早 | **1.7 实测** |
|------|-----------|-------------|
| 引擎 | Unity 2022.3.x，随游戏带 Unity 运行库 | 引擎已替换；Unity 类型由安装根目录的 `UnityStubs.dll` 等兼容程序集提供 |
| 游戏程序集位置 | `RimWorldWin64_Data/Managed/` | **安装根目录**（`RimWorldWin64_Data` 目录已不存在） |
| 目标框架 | .NET Framework 4.7.2 | **.NET 10（`net10.0`）** |
| 核心素材 | `Data/Core/Textures/` 散装文件 | **`Assets.zip`**（安装根目录，约 342 MB，Zstd 压缩） |
| Harmony | 部分整合包自带 | **游戏不自带**，必须由 Harmony mod（创意工坊 2009463077）提供 |
| 原版数据 | `Data/` | `Data/` 仍是散装 XML，可直接 grep（只有贴图/音频进了 Assets.zip） |

判断版本：读 `<RimWorld>` 安装根目录的 `Version.txt`（例：`1.7.4981 rev136`）。

## IDE 与编译器

### .NET SDK 10（必需）

```bash
dotnet --version    # 应为 10.x 或更高
```

编译 RimWorld mod 的程序集**不需要** Visual Studio：一个 .csproj + `dotnet build` 即可（见下节）。

### Visual Studio 2022 / Rider（可选）

需要 C# 智能提示与调试时安装，但要在安装器里勾选 **.NET 10 SDK**——默认的「.NET 桌面开发」工作负载带的仍是 .NET Framework，**编不出 1.7 的 mod**。

### VS Code

适合 XML 和纹理编辑。安装扩展：**XML** (Red Hat)、**C#** (Microsoft)。

## 引用 DLL

编译 C# Mod 需要引用以下程序集，**位于游戏安装根目录**：

| DLL | 用途 |
|-----|------|
| `Assembly-CSharp.dll` | RimWorld 全部游戏代码（约 15.6 MB） |
| `RimWorld.dll` | 程序集入口 / 版本信息 |
| `UnityStubs.dll` | Unity 类型兼容层（`UnityEngine.Vector3`、`Color` 等都来自这里） |

> ⚠️ 旧教程里的 `UnityEngine.dll`、`UnityEngine.CoreModule.dll`、`UnityEngine.IMGUIModule.dll` 在 1.7 安装目录**不存在**，照着找会白费时间。

### 编译方式 A：临时 csproj + dotnet build（推荐）

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net10.0</TargetFramework>
    <AssemblyName>你的Mod名</AssemblyName>
    <Nullable>disable</Nullable>
    <LangVersion>latest</LangVersion>
    <AppendTargetFrameworkToOutputPath>false</AppendTargetFrameworkToOutputPath>
  </PropertyGroup>
  <ItemGroup>
    <Reference Include="Assembly-CSharp"><HintPath>$(RimWorldDir)/Assembly-CSharp.dll</HintPath></Reference>
    <Reference Include="RimWorld"><HintPath>$(RimWorldDir)/RimWorld.dll</HintPath></Reference>
    <Reference Include="UnityStubs"><HintPath>$(RimWorldDir)/UnityStubs.dll</HintPath></Reference>
  </ItemGroup>
</Project>
```

```bash
dotnet build 你的Mod.csproj -c Release -p:RimWorldDir="<游戏安装目录>"
```

### 编译方式 B：csc + 引用框架（不想用 SDK 项目文件时）

```powershell
# 引用框架：Microsoft.NETCore.App.Ref 的 ref/net10.0 目录
& "$refDir/csc.dll" ...   # 或用 dotnet exec 调用 csc.dll，附 /r: 指向游戏程序集
```

两种方式都要把产物输出到 `Assemblies/`，并且**不要把游戏 DLL 复制进去**。

### 硬约束：产物目录里只能有自己的 DLL

`Assemblies/` 里出现 `Assembly-CSharp.dll`、`RimWorld.dll`、`UnityStubs.dll`、`0Harmony.dll` 都会引发加载冲突或版权问题。构建脚本最后应加一道校验：只允许出现本 mod 自己的产物。

> 一份实测通过的完整构建脚本（双路径：`dotnet build` 与 `csc + ref pack`，含 6 段自检）见本仓库交付物 `examples/rimtest-mod/RimTestMod/Source/build.ps1`，可直接抄思路。

## Harmony（0Harmony.dll）

Harmony **不再随游戏分发**，来自创意工坊的 Harmony mod：

```
<Steam 库>/steamapps/workshop/content/294100/2009463077/1.7/Assemblies/0Harmony.dll
```

规则：
1. **只作编译期引用**，不要拷进自己 mod 的 `Assemblies/`（运行时由 Harmony mod 提供）。
2. 只给「补丁程序集」引用 Harmony；**主程序集不要引用 0Harmony**——这样玩家没装 Harmony 时，主 mod 仍能加载，只有补丁那部分报错。
3. 目标框架差异：Harmony 的 1.7 版可能基于较低版本编译，与 `net10.0` 运行时存在漂移风险（实测编译通过、运行时未验证）。

## 源码查阅

### dnSpy（离线反编译）

1. 下载 [dnSpy](https://github.com/dnSpy/dnSpy/releases)（或 dnSpyEx）
2. 打开 `<RimWorld>/Assembly-CSharp.dll`（**安装根目录**，不是 `RimWorldWin64_Data`）
3. 在左侧树中浏览命名空间和类；右键方法 → Analyze 查看调用链

### 元数据探针（没有 dnSpy 时的快速核对）

字符串路径等方法"是否存在"可以不反编译就确认：

```powershell
# 字段/类型名以 UTF-8 存在元数据字符串表里，直接搜二进制即可
Select-String -Path "<RimWorld>/Assembly-CSharp.dll" -Pattern "productHasIngredientStuff" -Encoding utf8
```

注意两类字符串编码不同：**类型/字段名多为 UTF-8**，而**部分运行时日志模板为 UTF-16**（搜不中时可换 `-Encoding unicode` 再试）。找到≠被使用：还要回原版 `Data/` 里数一数实际出现次数。

### ⭐ RimSage MCP（AI 辅助搜索）

能让你用自然语言搜索 RimWorld 源码，实时验证 Def 结构、API 用法。安装：参考本 Skill 目录下的 `.mcp.json.example`（复制为 `.mcp.json`），或

```bash
claude mcp add rimworld-source --transport http https://mcp.rimsage.com/mcp
```

常用工具：`search_rimworld_source`（自然语言搜源码与 Def）、`get_def_details`（Def 完整定义与继承）、`read_rimworld_file`（读指定文件）。

### 核验源优先级（三层降级，任何一层可用就不算"待验证草稿"）

| 优先级 | 核验源 | 命令 / 做法 |
|--------|--------|------------|
| ① | **本仓库自带 1.7 模板库** | `node scripts/find-template.mjs --def ThingDef` / `--field verbClass` |
| ② | **本机原版数据** | `grep -rn "关键词" "<RimWorld>/Data/"`（1560 个 XML，含 DLC） |
| ③ | RimSage MCP / dnSpy | 语义检索或反编译 |
| — | 以上都不可用 | 明确标注「⚠️ 待验证草稿」，并列出待核验字段清单；**不要**把猜测写成确定结论 |

## 辅助工具

| 工具 | 用途 | 链接 |
|------|------|------|
| **RimPy** | Mod 管理 + Def 预览 | [GitHub](https://github.com/rimpy-custom/RimPy) |
| **RimSort** | Mod 排序与依赖管理 | [GitHub](https://github.com/RimSort/RimSort) |

## 快速检查清单

- [ ] `dotnet --version` ≥ 10.x（编 C# 时）
- [ ] 已定位游戏安装根目录，能读到 `Version.txt` 与 `Assembly-CSharp.dll`
- [ ] 知道 `Data/` 可直接 grep；贴图/音频在 `Assets.zip`（要读需 Zstd 解压，见 `07-assets.md`）
- [ ] 装 Harmony 时知道 0Harmony.dll 只作编译引用、不进 `Assemblies/`
- [ ] 构建产物校验：`Assemblies/` 里只有本 mod 的 DLL
- [ ] Mod 输出目录已就绪（`<RimWorld>/Mods/<你的Mod>/`）
