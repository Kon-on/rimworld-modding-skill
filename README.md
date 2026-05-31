# RimWorld Modding Skill

Claude Code agent skill for RimWorld mod development. Covers the full mod creation workflow — from environment setup to Steam Workshop publishing.

## Features

- **Full coverage**: XML Defs, C# modding, Harmony patching, assets, debugging, Workshop publishing
- **Chinese-first**: Teaching content in Chinese, code/XML in English
- **Vanilla-verified**: Every Def pattern validated against RimWorld 1.6 base game files
- **RimSage MCP integration**: Real-time source code search for verifying Def structures
- **Test-first pipeline**: Test version → developer verification → formalize → optional publish
- **Templates**: Ready-to-use XML templates for weapons (melee/ranged), buildings, recipes, ThingComp, and Harmony patches

## Structure

```
rimworld-modding-skill/
├── SKILL.md                 # Main dispatcher + intent routing
├── references/              # Knowledge base (10 files)
│   ├── 01-environment.md    # IDE, .NET, dnSpy, MCP setup
│   ├── 02-project-structure.md
│   ├── 03-xml-defs.md       # Core: ThingDef, RecipeDef, etc.
│   ├── 04-xml-patching.md   # XPath PatchOperations
│   ├── 05-csharp-basics.md
│   ├── 06-harmony.md
│   ├── 07-assets.md
│   ├── 08-debugging.md
│   ├── 09-workshop.md
│   └── 10-api-reference.md
├── templates/               # Code templates (6 files)
│   ├── weapon-melee.xml
│   ├── weapon-ranged.xml
│   ├── building.xml
│   ├── recipe.xml
│   ├── harmony-patch.cs
│   └── thingcomp.cs
├── workflows/               # Task workflows (6 files)
│   ├── new-mod.md            # Test-first creation
│   ├── formalize-mod.md      # Test→formal→publish
│   ├── add-item.md
│   ├── add-building.md
│   ├── patch-vanilla.md
│   └── debug-crash.md
└── docs/                    # Design docs
    ├── specs/                # Specification
    └── plans/                # Implementation plan
```

## Installation

Copy the skill directory to your Claude Code skills folder:

```
cp -r rimworld-modding-skill ~/.claude/skills/rimworld-modding/
```

Or install via the skills marketplace (coming soon).

## Requirements

- RimWorld 1.6
- [RimSage MCP](https://mcp.rimsage.com/mcp) (recommended for source code search)
- .mcp.json configured for the `rimworld-source` MCP server

## License

MIT
