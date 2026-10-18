# 02 — Mod 项目结构

> **适用版本**: RimWorld 1.7（实测 1.7.4981 rev136） | **最后更新**: 2026-10-18
>
> 目录结构与 About.xml 的**形状**从 1.6 到 1.7 没有变化，变的只是版本号写什么：现在写 `1.7`。
> 1.7 的实际变化都在运行时（引擎 Waylith、net10.0、DLL 在游戏安装根）——见 `references/01-environment.md`。


## 目录

- [标准目录树](#标准目录树)
- [About.xml 详解](#aboutxml-详解)
- [命名规范](#命名规范)
- [LoadFolders.xml（条件加载）](#loadfoldersxml条件加载)
- [快速检查清单](#快速检查清单)

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
├── 1.7/                     # 版本特定资源（用 LoadFolders 分开给不同游戏版本时才有这个目录）
│   └── Defs/
└── LoadFolders.xml          # 按版本/DLC 条件加载（可选）
```

## About.xml 详解

```xml
<?xml version="1.0" encoding="utf-8"?>
<ModMetaData>
  <!-- 内部 ID，全小写无空格，全局唯一——用户自行填写 -->
  <packageId>你的用户名.你的mod名</packageId>

  <!-- 显示名称（Steam Workshop 和 Mod 列表显示）——用户自行填写 -->
  <name>你的 Mod 名称</name>

  <!-- 作者名——用户自行填写自己的 Steam/GitHub 用户名或昵称 -->
  <author>在此填写你的名字</author>

  <!-- 游戏版本：写当前目标版本；同时支持多个版本就多写几个 li（顺序无关） -->
  <supportedVersions>
    <li>1.7</li>
  </supportedVersions>

  <!-- Mod 依赖（可选） -->
  <modDependencies>
    <!-- 必须依赖 Harmony -->
    <li>
      <packageId>brrainz.harmony</packageId>
      <displayName>Harmony</displayName>
    </li>
  </modDependencies>

  <!-- 依赖的 DLC（可选）：v 标签写游戏版本号 -->
  <modDependenciesByVersion>
    <v1.7>
      <li>
        <packageId>ludeon.rimworld.biotech</packageId>
        <displayName>Biotech</displayName>
      </li>
    </v1.7>
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
// 用户根据自己选择的前缀自行确定
namespace <你的前缀>.<你的Mod名>
{
    // 例如：如果你的前缀是 RCS_，Mod 名为 RainbowCatSword
    // namespace RCS.RainbowCatSword
}
```

### 文件命名

- XML Def 文件：`Category_SubCategory.xml`（如 `Items_Weapons.xml`, `Buildings_Production.xml`）
- Patch 文件：`Patch_Target_TargetName.xml`（如 `Patch_Vanilla_MeleeWeapons.xml`）

## 本地化（Languages 目录）

文本分两类，存放位置不同：

| 类型 | 原文写在哪 | 翻译写在哪 |
|------|-----------|-----------|
| Def 字段（label / description / 武器名…） | 你的 Def XML | `Languages/<语言>/DefInjected/<DefType>/<任意文件名>.xml` |
| C# 代码里的界面文字 | `"SR_Key".Translate()` | `Languages/<语言>/Keyed/<任意文件名>.xml` |

```
YourMod/
├── Defs/
│   └── ThingDefs_Misc/Weapons/PlasmaDagger.xml        # 英文原文
└── Languages/
    ├── English/
    │   └── DefInjected/ThingDef/Weapons.xml
    └── ChineseSimplified (简体中文)/
        ├── DefInjected/ThingDef/Weapons.xml
        └── Keyed/SR_Strings.xml
```

### DefInjected：key 必须带 Def 类型前缀

```xml
<?xml version="1.0" encoding="utf-8"?>
<LanguageData>
  <ThingDef.SR_Weapon_PlasmaDagger.label>等离子匕首</ThingDef.SR_Weapon_PlasmaDagger.label>
  <ThingDef.SR_Weapon_PlasmaDagger.description>一把刃口被等离子场包裹的匕首。</ThingDef.SR_Weapon_PlasmaDagger.description>
</LanguageData>
```

- key = `<DefType>.<defName>.<字段路径>`，文件名与目录内文件数量随意。
- 字段是列表时用数字索引：`<ThingDef.SR_Gun_IonRifle.verbs.0.label>`。
- 没翻译的字段回退到 Def 里的原文——所以 Def 里要写能读的英文原文，不要写占位符。
- **defName 是 key 的一部分**：一旦有翻译，改 defName 会让所有既有翻译失效（见本文「命名规范」）。

### Keyed：C# 字符串

```xml
<LanguageData>
  <SR_DamageAbsorbed>已吸收 {0} 点伤害</SR_DamageAbsorbed>
</LanguageData>
```

- 代码里 `"SR_DamageAbsorbed".Translate(amount)`；缺 key 时显示 key 原文，不会崩。
- 占位符可以调整语序，**不能增删个数**：调用方传 1 个参数，翻译里只能有 `{0}`。

### 落地检查

1. 语言目录名照原版抄：先看 `<RimWorld>/Data/Core/Languages/` 里目录怎么写的（如 `ChineseSimplified (简体中文)`），名字不对不会出现在 Options → Language 列表里。
2. 切语言后**重启游戏**才生效；label 变了才算通。
3. 没生效就看日志，翻译相关的报错会点名文件与 key。
4. 只做中文的 mod 可以直接把中文写进 Def——省事，但其他语言玩家会看到中文，且以后补翻译要回头动 Def。
5. 批量导出/导入翻译用社区工具 RimTrans，导出后仍要人工核对占位符个数与换行。

> ⚠️ 待核验：mod 一般不需要 `LanguageInfo.xml`（语言元数据/字体走原版），本模板未覆盖自定义语言的情况；要自定义语言或字体时，对照原版 `Data/Core/Languages/` 里的同名文件再写。

## LoadFolders.xml（条件加载）

当需要按 DLC 或版本加载不同 Def 时：

```xml
<?xml version="1.0" encoding="utf-8"?>
<loadFolders>
  <v1.7>
    <li>1.7</li>                                              <!-- 相对 mod 根目录的子目录 -->
    <li IfModActive="ludeon.rimworld.biotech">1.7/Biotech</li> <!-- 只有启用 Biotech 才加载 -->
  </v1.7>
</loadFolders>
```

要点：
- `<v1.7>` 里的条目是**相对 mod 根目录的路径**；如果 mod 所有内容都在根目录（最常见），写 `<v1.7><li>/</li></v1.7>`。
- 想同时支持多个版本，就并列写多个版本块（`<v1.6>…</v1.6>` + `<v1.7>…</v1.7>`）。
- 不写 LoadFolders.xml 时，游戏默认加载 mod 根目录（以及约定的版本目录），小 mod 完全可以不写。
- 本仓库的实测样例（44 文件测试 mod）用的就是最简形：`examples/rimtest-mod/RimTestMod/LoadFolders.xml`。

## 快速检查清单

- [ ] About.xml 中 `packageId` 全局唯一
- [ ] `supportedVersions` 包含 `1.7`
- [ ] 所有 defName 带唯一前缀
- [ ] 目录结构符合标准（About/ Defs/ Patches/ Assemblies/ Textures/）
