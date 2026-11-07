# RimWorld Modding Skill

> 给 AI 编码代理用的 RimWorld 1.7 mod 制作技能：环境搭建、XML Def、C# 与 Harmony 补丁、贴图、调试、Steam Workshop 发布的全流程，附带经原版实测校准的模板库与可机械校验的索引。

**兼容** Claude Code · OpenAI Codex · Gemini CLI · GitHub Copilot CLI · TRAE · DSH · Cursor / Windsurf（降级）

**版本** 1.2.0 · **许可** MIT · [变更记录](CHANGELOG.md)

---

## 目录

- [能做什么](#能做什么)
- [安装](#安装)
- [使用](#使用)
- [仓库内容](#仓库内容)
- [工作原理](#工作原理)
- [已知限制](#已知限制)
- [维护](#维护)
- [致谢与许可](#致谢与许可)

## 能做什么

| 你要做的事 | 技能会给你 | 出处 |
|---|---|---|
| 做一个武器 / 服装 / 建筑 / 植物 / 材料 | 可直接改用的 XML Def 模板 | [assets/templates](assets/templates) |
| 改原版机制 | XML PatchOperation 写法 + 节点语义坑 | [references/04-xml-patching.md](references/04-xml-patching.md) |
| 写 C# 组件、存读档 | ThingComp 模板与 Scribe 写法 | [references/05-csharp-basics.md](references/05-csharp-basics.md) |
| 拦截游戏方法 | Harmony 3.0 bootstrap 完整代码 | [references/06-harmony.md](references/06-harmony.md) |
| 出贴图、配朝向 | 尺寸 / 朝向 / 命名约定与 Graphic 类型选择 | [references/07-assets.md](references/07-assets.md) |
| 游戏报红字 | 日志定位、常见报错速查 | [references/08-debugging.md](references/08-debugging.md) |
| 发布到创意工坊 | 元数据、版本声明、合规要求 | [references/09-workshop.md](references/09-workshop.md) |
| 一次做多个物品 | 需求清单 → 批量产出流程 | [references/workflows/batch-process.md](references/workflows/batch-process.md) |

没有 RimSage MCP、甚至本机没装游戏也能用：技能会按降级规则标注 **「⚠️ 待验证草稿」**——这是设计，不是失败。

## 安装

克隆到本地：

```bash
git clone https://github.com/Kon-on/rimworld-modding-skill.git
```

然后把整个目录复制到对应代理的技能目录（下表），或直接让代理读 [SKILL.md](SKILL.md)。

| 平台 | 技能目录 |
|---|---|
| **Claude Code** | `~/.claude/skills/rimworld-modding/` |
| **OpenAI Codex** | `~/.codex/skills/rimworld-modding/` |
| **Gemini CLI** | `~/.gemini/skills/rimworld-modding/` |
| **GitHub Copilot CLI** | `~/.copilot/skills/rimworld-modding/` |
| **TRAE** | `~/.trae/skills/rimworld-modding/` |
| **DSH** | `~/.dsh/skills/rimworld-modding/` 或 `<项目>/.dsh/skills/` |
| **Cursor / Windsurf** | 不支持技能目录，手动引用 [references](references) 与 [assets/templates](assets/templates) |

```bash
# 以 Claude Code 为例，其他平台换个目标目录即可
cp -r rimworld-modding-skill ~/.claude/skills/rimworld-modding/
```

**可选依赖**：按 Def 名反查原版数据需要 RimSage MCP。把 [.mcp.json.example](.mcp.json.example) 复制为 `.mcp.json`，重启代理后批准连接。各平台工具映射见 [references/11-platform-adaptation.md](references/11-platform-adaptation.md)。

**环境要求**：RimWorld 1.7（引擎 Waylith / net10.0）。只有改本仓库、跑校验脚本时才需要 Node 18+。

## 使用

装好后直接说需求，技能默认走「测试版先行」：先生成可加载的测试版 → 你进游戏验证 → 通过后正规化 → 再决定是否发布。

```text
用 rimworld-modding 技能，做一个等离子匕首：伤害 18，冷却 1.2 秒
```

```text
给这个 mod 加一件防弹背心，锐器防护 40%，保暖 8
```

```text
游戏启动报红字「Could not resolve cross-reference」，帮我定位一下
```

更完整的流程见 [references/workflows/new-mod.md](references/workflows/new-mod.md)（从零到可加载）与 [references/workflows/formalize-mod.md](references/workflows/formalize-mod.md)（测试通过后正规化）。

## 仓库内容

```
rimworld-modding-skill/
├── SKILL.md                     # 技能入口：三层决策、命名规范、标注要求、索引（唯一必需文件）
├── README.md                    # 本文件
├── CHANGELOG.md                 # 版本变更记录
├── LICENSE                      # MIT
├── .mcp.json.example            # RimSage MCP 配置模板
├── references/                  # 11 篇知识参考（环境 / 结构 / XML / 补丁 / C# / Harmony / 资源 / 调试 / 发布 / API / 跨平台）
│   └── workflows/               # 7 个工作流（新建、正规化、加物品、加建筑、批量、打补丁、查崩溃）
├── assets/templates/            # 10 个起步模板（8 个 XML/C# + 需求清单模板）
├── library/                     # 1.7 模板库（301 文件）：39 份实测模板、254 张字段表、字段总表
└── scripts/                     # 零依赖 Node 脚本：check-index / xml-lint / find-template
```

## 工作原理

**三层决策**：① 有模板 → 直接用，免核验；② 撞到报错 → 查原版 / 查 MCP；③ 没有模板 → 查原版 → 写 Def → 回填模板库并更新索引。

**核验源降级**：① 本仓库 1.7 模板库（`node scripts/find-template.mjs 武器` / `--def ThingDef` / `--field verbClass`）→ ② 本机原版 `Data/` 里 grep 真实出现次数 → ③ RimSage MCP 或 dnSpy 读程序集。三层都不可用时输出「⚠️ 待验证草稿」，不猜。

**模板库**（[library](library)）：[01-梳理报告](library/01-梳理报告) 记录 1.7 代码形态与 1.6 → 1.7 迁移；[02-模板](library/02-模板) 是 39 份按线分组的模板；[03-全量字段参考](library/03-全量字段参考) 是 254 张字段表 + 字段总表；[04-核验](library/04-核验) 是模板库自身的核验结果。

## 已知限制

- **Harmony 兼容性**：Harmony 3.0（按 net8 编译）跑在 net10.0 游戏上，目前只验证到「编译通过 + 补丁登记成功」，长时间、多场景未验证。
- **语言目录标识**：`legacyFolderName` 的实际取值无法静态确定，文档同时给出 `ChineseSimplified` 与 `ChineseSimplified (简体中文)` 两种写法。
- **实测环境**：Windows + RimWorld 1.7.4981 rev136；Linux / macOS 未验证。

## 维护

改完本仓库任何文件，先跑：

```bash
node scripts/check-index.mjs --strict   # 路径引用 / 索引覆盖率 / 模板标注 / XML 良构性
```

SKILL.md 里的「模板 ↔ Def 类型对照表」与「子文件索引」是手写索引，目录一改名就会静默漂移。机械约束交给脚本，人只负责内容。

## 致谢与许可

感谢 **[RimSage](https://mcp.rimsage.com/mcp)**（MIT 协议开源）——排查报错、创建新类型模板时靠它快速定位原版参照。

MIT，见 [LICENSE](LICENSE)。本项目的代码、文档与模板由 AI 生成并经人工审查，请自行验证后再用于正式发布。

---

## English

An AI-agent skill for **RimWorld 1.7** mod development: XML Defs, C#, Harmony patching, textures, debugging, and Steam Workshop publishing — plus a locally extracted 1.7 template library (301 files: 39 templates, 254 field tables) and mechanical index checks.

- **Install**: copy the repo into your agent's skills directory (Claude Code: `~/.claude/skills/rimworld-modding/`, Codex / Gemini CLI / Copilot CLI / TRAE / DSH use their own paths).
- **Use**: point your agent at [SKILL.md](SKILL.md); it defaults to "test version first → verify → formalize → optionally publish".
- **Optional dependency**: [RimSage MCP](https://mcp.rimsage.com/mcp) — copy [.mcp.json.example](.mcp.json.example) to `.mcp.json`. Without it, output is explicitly marked as unverified draft.
- **Verify**: `node scripts/check-index.mjs --strict`.
- **License**: MIT. AI-generated with human review — verify everything yourself.
