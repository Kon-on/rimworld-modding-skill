# RimWorld Modding Skill · 环世界Mod制作技能

Claude Code 环世界 Mod 制作全流程技能——从环境搭建到 Steam Workshop 发布。
Claude Code agent skill for full-cycle RimWorld mod development.

---

## 功能特性

- **全流程覆盖**: XML Def、C#、Harmony 补丁、资源制作、调试、Workshop 发布
- **中英双语**: 教程用中文，代码/XML 用英文
- **原版验证**: 所有 Def 模式均对照 RimWorld 1.6 原版文件验证
- **RimSage MCP 集成**: 实时源码搜索，写 Def 前先查原版
- **测试版先行**: 测试版 → 验证 → 正规化 → 可选发布
- **代码模板**: 近战/远程武器、建筑、配方、ThingComp、Harmony 补丁

## 目录结构

```
rimworld-modding-skill/
├── SKILL.md                 # 总调度器 + 意图路由
├── references/              # 知识库（10 篇）
│   ├── 01-environment.md    # IDE、.NET、dnSpy、MCP 配置
│   ├── 02-project-structure.md
│   ├── 03-xml-defs.md       # 核心：ThingDef、RecipeDef 等
│   ├── 04-xml-patching.md   # XPath PatchOperations
│   ├── 05-csharp-basics.md
│   ├── 06-harmony.md
│   ├── 07-assets.md
│   ├── 08-debugging.md
│   ├── 09-workshop.md
│   └── 10-api-reference.md
├── templates/               # 代码模板（6 个）
│   ├── weapon-melee.xml
│   ├── weapon-ranged.xml
│   ├── building.xml
│   ├── recipe.xml
│   ├── harmony-patch.cs
│   └── thingcomp.cs
├── workflows/               # 工作流（6 个）
│   ├── new-mod.md            # 测试版先行创建
│   ├── formalize-mod.md      # 测试→正规化→发布
│   ├── add-item.md
│   ├── add-building.md
│   ├── patch-vanilla.md
│   └── debug-crash.md
└── docs/                    # 设计文档
    ├── specs/                # 设计规格
    └── plans/                # 实施计划
```

## 安装

复制到 Claude Code skills 目录：

```
cp -r rimworld-modding-skill ~/.claude/skills/rimworld-modding/
```

## 需求

- RimWorld 1.6
- [RimSage MCP](https://mcp.rimsage.com/mcp)（推荐，用于源码搜索）
- `.mcp.json` 配置 `rimworld-source` MCP 服务器

## 致谢

本项目依赖以下开源工具：

- **[RimSage](https://mcp.rimsage.com/mcp)**（MIT 协议）—— RimWorld 源码 AI 搜索 MCP 服务器，提供 `search_rimworld_source`、`get_def_details`、`read_rimworld_file` 工具，是本 Skill 验证 Def 结构的核心依赖。本项目基于 MIT 协议使用该组件。

> 感谢 RimSage 作者为 RimWorld mod 社区提供了如此强大的开发工具。

## 许可证

MIT

---

## Features (EN)

- **Full coverage**: XML Defs, C# modding, Harmony patching, assets, debugging, Workshop
- **Bilingual**: Chinese tutorials + English code/XML
- **Vanilla-verified**: All Def patterns validated against RimWorld 1.6 base game files
- **RimSage MCP**: Real-time source code search for verifying Def structures
- **Test-first pipeline**: Test version → verify → formalize → optional publish
- **Templates**: Ready-to-use XML/C# templates for weapons, buildings, recipes, ThingComp, Harmony

## Installation (EN)

```
cp -r rimworld-modding-skill ~/.claude/skills/rimworld-modding/
```

## Acknowledgments

This project depends on:

- **[RimSage](https://mcp.rimsage.com/mcp)** (MIT License) — AI-powered RimWorld source code search MCP server. Provides `search_rimworld_source`, `get_def_details`, and `read_rimworld_file`. Used under the MIT License.

> Thanks to the RimSage author for building such a powerful tool for the RimWorld modding community.

## License

MIT
