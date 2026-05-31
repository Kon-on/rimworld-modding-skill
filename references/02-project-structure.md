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
  <!-- 内部 ID，全小写无空格，全局唯一——用户自行填写 -->
  <packageId>你的用户名.你的mod名</packageId>

  <!-- 显示名称（Steam Workshop 和 Mod 列表显示）——用户自行填写 -->
  <name>你的 Mod 名称</name>

  <!-- 作者名——用户自行填写自己的 Steam/GitHub 用户名或昵称 -->
  <author>在此填写你的名字</author>

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
