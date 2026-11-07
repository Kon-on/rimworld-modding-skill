# RimWorld Modding Skill

English · [简体中文](README.md)

> An AI-agent skill for **RimWorld 1.7** mod development: environment setup, XML Defs, C# and Harmony patches, textures, debugging, and Steam Workshop publishing — with a template library calibrated against the vanilla game and a mechanically checked index.

**Works with** Claude Code · OpenAI Codex · Gemini CLI · GitHub Copilot CLI · TRAE · DSH · Cursor / Windsurf (degraded)

**Version** 1.2.0 · **License** MIT · [Changelog](CHANGELOG.md)

---

## Contents

- [What it does](#what-it-does)
- [Install](#install)
- [Usage](#usage)
- [What's inside](#whats-inside)
- [How it works](#how-it-works)
- [Known limitations](#known-limitations)
- [Maintenance](#maintenance)
- [Credits and license](#credits-and-license)

## What it does

| You want to… | The skill gives you | Where |
|---|---|---|
| Build a weapon / apparel / building / plant / material | Ready-to-adapt XML Def templates | [assets/templates](assets/templates) |
| Patch vanilla mechanics | PatchOperation patterns and node-semantics pitfalls | [references/04-xml-patching.md](references/04-xml-patching.md) |
| Write C# comps and save data | ThingComp template and Scribe patterns | [references/05-csharp-basics.md](references/05-csharp-basics.md) |
| Intercept game methods | Complete Harmony 3.0 bootstrap code | [references/06-harmony.md](references/06-harmony.md) |
| Make textures with correct orientation | Size / orientation / naming rules and Graphic type selection | [references/07-assets.md](references/07-assets.md) |
| Read a red-error log | Log locations and a common-error lookup table | [references/08-debugging.md](references/08-debugging.md) |
| Publish to the Workshop | Metadata, version declarations, compliance | [references/09-workshop.md](references/09-workshop.md) |
| Produce many items at once | Requirements checklist → batch pipeline | [references/workflows/batch-process.md](references/workflows/batch-process.md) |

It works without RimSage MCP, and even without the game installed: output is then explicitly marked **"⚠️ unverified draft"** — that is by design, not a failure.

## Install

Clone the repository:

```bash
git clone https://github.com/Kon-on/rimworld-modding-skill.git
```

Then copy the whole directory into your agent's skills folder (table below), or simply point the agent at [SKILL.md](SKILL.md).

| Platform | Skills directory |
|---|---|
| **Claude Code** | `~/.claude/skills/rimworld-modding/` |
| **OpenAI Codex** | `~/.codex/skills/rimworld-modding/` |
| **Gemini CLI** | `~/.gemini/skills/rimworld-modding/` |
| **GitHub Copilot CLI** | `~/.copilot/skills/rimworld-modding/` |
| **TRAE** | `~/.trae/skills/rimworld-modding/` |
| **DSH** | `~/.dsh/skills/rimworld-modding/` or `<project>/.dsh/skills/` |
| **Cursor / Windsurf** | No skills folder; reference [references](references) and [assets/templates](assets/templates) manually |

```bash
# Claude Code example; swap the target directory for other platforms
cp -r rimworld-modding-skill ~/.claude/skills/rimworld-modding/
```

**Optional dependency**: looking up vanilla data by Def name needs RimSage MCP. Copy [.mcp.json.example](.mcp.json.example) to `.mcp.json`, restart the agent, then approve the connection. Per-platform tool mapping is in [references/11-platform-adaptation.md](references/11-platform-adaptation.md).

**Requirements**: RimWorld 1.7 (Waylith engine, net10.0). Node 18+ is only needed to modify this repository or run the check script.

## Usage

Just describe what you want. The skill defaults to **test version first**: generate a loadable test build → you verify in game → formalize → optionally publish.

```text
Use the rimworld-modding skill to make a plasma dagger: 18 damage, 1.2s cooldown
```

```text
Add a kevlar vest to this mod: 40% sharp armor, 8 insulation
```

```text
The game throws "Could not resolve cross-reference" on startup — help me track it down
```

Full flows: [references/workflows/new-mod.md](references/workflows/new-mod.md) (zero to loadable) and [references/workflows/formalize-mod.md](references/workflows/formalize-mod.md) (formalize after testing).

## What's inside

```
rimworld-modding-skill/
├── SKILL.md                     # Entry point: three-tier decision, naming rules, labeling, index (the only required file)
├── README.md                    # Chinese README
├── README.en.md                 # This file
├── CHANGELOG.md                 # Version history
├── LICENSE                      # MIT
├── .mcp.json.example            # RimSage MCP config template
├── references/                  # 11 knowledge documents (environment / structure / XML / patching / C# / Harmony / assets / debugging / publishing / API / platforms)
│   └── workflows/               # 7 workflows (new mod, formalize, add item, add building, batch, patch, debug crash)
├── assets/templates/            # 10 starter templates (8 XML/C# plus a requirements template)
├── library/                     # 1.7 template library (301 files): 39 verified templates, 254 field tables, field index
└── scripts/                     # Zero-dependency Node scripts: check-index / xml-lint / find-template
```

## How it works

**Three-tier decision**: (1) template exists → use it directly, no verification needed; (2) hit an error → check vanilla source or MCP; (3) no template → read vanilla source → write the Def → feed it back into the template library and update the index.

**Verification fallback**: (1) the bundled 1.7 template library (`node scripts/find-template.mjs weapon` / `--def ThingDef` / `--field verbClass`) → (2) grep real occurrence counts in your local `Data/` → (3) RimSage MCP or dnSpy on the assemblies. If all three are unavailable, the output is marked "⚠️ unverified draft" — it never guesses.

**Template library** ([library](library)): [01-梳理报告](library/01-梳理报告) records 1.7 code shape and the 1.6 → 1.7 migration; [02-模板](library/02-模板) holds 39 templates grouped by production line; [03-全量字段参考](library/03-全量字段参考) has 254 field tables plus a field index; [04-核验](library/04-核验) contains the library's own verification results.

## Known limitations

- **Harmony compatibility**: Harmony 3.0 (built against net8) runs on a net10.0 game; only "compiles + registers at startup" has been verified, not long sessions or edge cases.
- **Language folder identifier**: the actual value of `legacyFolderName` cannot be determined statically, so the docs give both `ChineseSimplified` and `ChineseSimplified (简体中文)`.
- **Verified environment**: Windows + RimWorld 1.7.4981 rev136; Linux and macOS untested.

## Maintenance

After changing anything in this repository, run:

```bash
node scripts/check-index.mjs --strict   # path references / index coverage / template markers / XML well-formedness
```

The template-to-Def table and the sub-file index inside SKILL.md are hand-written, so they drift silently whenever a directory is renamed. The script enforces the mechanical part; humans only maintain the content.

## Credits and license

Thanks to **[RimSage](https://mcp.rimsage.com/mcp)** (MIT) — locating vanilla references by hand would otherwise mean scrolling through thousands of lines of XML.

MIT, see [LICENSE](LICENSE). Code, docs, and templates were AI-generated with human review — verify everything yourself before publishing.
