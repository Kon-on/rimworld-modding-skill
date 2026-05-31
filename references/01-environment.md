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

### ⭐ RimSage MCP（AI 辅助搜索——强烈推荐）

**这是最重要的开发工具。** 能让你用自然语言搜索 RimWorld 源码，实时验证 Def 结构、API 用法。

#### 安装方式

**方式 A：项目级配置（推荐）**

参考本 Skill 目录下的 `.mcp.json.example`，复制为 `.mcp.json` 放到项目根目录。

**方式 B：全局配置**

```bash
claude mcp add rimworld-source --transport http https://mcp.rimsage.com/mcp
```

> 首次索引需 30-60 分钟，之后查询速度在毫秒级。

#### 可用工具

| 工具 | 用途 |
|------|------|
| `search_rimworld_source` | 自然语言搜索 C# 源码和 XML Def |
| `get_def_details` | 获取 Def 的完整定义和继承关系 |
| `read_rimworld_file` | 读取指定源文件全文 |

#### 验证 MCP 是否正常

在 Claude Code 中尝试调用 MCP 工具。如果工具列表中看不到 `mcp__rimworld-source__*`，说明未连接——检查：
1. `.mcp.json` 是否存在且格式正确
2. Claude Code 是否已批准该 MCP 连接（右下角弹窗）
3. `https://mcp.rimsage.com/mcp` 是否可达

#### MCP 不可用时的替代方案

降级为本地搜索：
```bash
grep -r "关键词" "<RimWorld>/Data/Core/Defs/"
```
或用 dnSpy 反编译 `Assembly-CSharp.dll`（见下方）。

### dnSpy（离线反编译——备选）

当没有网络或不想用 MCP 时的替代方案：

1. 下载 [dnSpy](https://github.com/dnSpy/dnSpy/releases)
2. 打开 `<RimWorld>/RimWorldWin64_Data/Managed/Assembly-CSharp.dll`
3. 在左侧树中浏览命名空间和类
4. 右键某个方法 → Analyze 查看调用链

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
