# 11 — 跨平台适配

> **适用版本**: RimWorld 1.6 | **最后更新**: 2026-06-01

## 支持的 AI 编程平台

本 Skill 设计为平台中立——RimWorld modding 知识不依赖特定 AI 工具。以下为各平台使用指南。

### Claude Code（原生平台）

**Skill 安装**：
```
cp -r rimworld-modding-skill ~/.claude/skills/rimworld-modding/
```

**MCP 配置**（二选一）：
```bash
# 方案 A：项目级配置（推荐）
# 在项目根目录创建 .mcp.json（参考 .mcp.json.example）

# 方案 B：全局配置
claude mcp add rimworld-source --transport http https://mcp.rimsage.com/mcp
```

**关键工具**：`Read`, `Write`, `Edit`, `Bash`, `Grep`, `Glob`, `Skill`

---

### GitHub Copilot CLI

**Skill 安装**：
```
mkdir -p ~/.copilot/skills/rimworld-modding/
cp -r rimworld-modding-skill/* ~/.copilot/skills/rimworld-modding/
```

**MCP 配置**：Copilot 支持 `.mcp.json` 文件。将 `.mcp.json.example` 复制为 `.mcp.json` 并修改。

**工具映射**：

| 本 Skill 中的操作 | Copilot 工具 |
|------------------|-------------|
| 读取文件 | `view` |
| 创建/写入文件 | `create` |
| 编辑文件 | `edit` |
| 搜索文件内容 | `grep` |
| 按文件名搜索 | `glob` |
| 运行命令 | `bash` |
| 同时执行多个独立任务 | 多个 `task` 调用 |
| 任务跟踪 | `sql` with `todos` table |
| 加载 Skill | `skill` |

---

### OpenAI Codex

**Skill 安装**：Codex 支持 natively load skills。将文件复制到 `~/.codex/skills/rimworld-modding/`。

**MCP 配置**：Codex 支持 `.mcp.json`。

**工具映射**：

| 本 Skill 中的操作 | Codex 工具 |
|------------------|-----------|
| 文件操作 | 原生文件工具 |
| 终端命令 | 原生 shell 工具 |
| 并行子任务 | `spawn_agent` + `wait_agent` |
| 任务跟踪 | `update_plan` |
| 加载 Skill | 原生 skill 加载 |

> 需在 `~/.codex/config.toml` 中启用 `[features].multi_agent = true`。

---

### Gemini CLI

**Skill 安装**：Gemini CLI 自动加载 `~/.gemini/skills/` 下的 skills。

**MCP 配置**：Gemini 支持 MCP（需在配置中声明）。

---

### TRAE（字节跳动 AI IDE）

**Skill 安装**：
```
mkdir -p ~/.trae/skills/rimworld-modding/
cp -r rimworld-modding-skill/* ~/.trae/skills/rimworld-modding/
```

> TRAE 原生支持 `SKILL.md` 格式，Skill 放入 `.trae/skills/` 后自动识别。

**MCP 配置**：

TRAE 支持 `.mcp.json`（项目级）和 `.trae/mcp.json`（项目级）。将 `.mcp.json.example` 复制为 `.mcp.json` 即可。

```bash
cp .mcp.json.example .mcp.json
```

也可在 TRAE 设置 → MCP 中手动添加 HTTP 类型的 MCP Server，URL 填 `https://mcp.rimsage.com/mcp`。

**工具映射**：

| 本 Skill 中的操作 | TRAE 工具 |
|------------------|----------|
| 读取文件 | `Read` / 文件读取 |
| 创建/写入文件 | `Write` / 文件写入 |
| 编辑文件 | `Edit` / 文件编辑 |
| 搜索文件内容 | `Grep` / 内容搜索 |
| 按文件名搜索 | `Glob` / 文件搜索 |
| 运行命令 | `Bash` / 终端 |
| 并行子任务 | `Agent`（Subagent） |
| 加载 Skill | 原生 SKILL.md 自动加载 |

> **注意**：TRAE 的中国版和国际版功能可能略有差异，建议更新到最新版本以获得完整的 Agent + MCP 支持。

---

### Cursor / Windsurf / 其他 IDE 插件

这些 IDE 插件通常不支持 MCP。使用以下降级方案：

| 原本用 MCP 做的事 | 降级方案 |
|------------------|---------|
| 搜索 RimWorld 源码 | 在 IDE 中全局搜索 `<RimWorld>/Data/Core/Defs/` |
| 查看 Def 结构 | 直接打开原版 XML 文件阅读 |
| 查找类/方法定义 | 用 dnSpy 反编译 `Assembly-CSharp.dll` |

**使用方式**：将 Skill 的 `references/` 和 `templates/` 作为知识库引用，手动复制对应模板。

---

## 通用 MCP 配置（所有平台）

`.mcp.json` 是 MCP 的跨平台标准配置格式。本 Skill 的 `.mcp.json.example` 可用于任何支持 MCP 的平台：

```json
{
  "mcpServers": {
    "rimworld-source": {
      "transport": "http",
      "url": "https://mcp.rimsage.com/mcp"
    }
  }
}
```

## 无 MCP 时的回退方案

所有平台均支持的最基本工作流：

1. **查原版 Def**：用文件搜索工具在 `<RimWorld>/Data/Core/Defs/` 中搜索
2. **模仿结构**：找到类似的原版 Def，复制其 XML 结构
3. **对照模板**：使用 `templates/` 中的模板文件
4. **阅读文档**：参考 `references/` 中的说明

```bash
# 通用 grep 搜索（所有平台适用）
grep -r "techLevel" "<RimWorld>/Data/Core/Defs/" | head -20
grep -r 'ParentName="BaseMeleeWeapon"' "<RimWorld>/Data/Core/Defs/"
```
