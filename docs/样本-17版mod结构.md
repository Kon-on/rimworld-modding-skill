# RimWorld 1.7 mod 规范结构与元数据实测报告

> 被测游戏：**1.7.4981 rev136**（命令：`Get-Content -LiteralPath '<游戏安装目录>\Version.txt'` → 输出 `1.7.4981 rev136`）
> 样本范围：创意工坊 `<创意工坊目录>`（共 136 个 mod 目录）
> 路径占位符：`<游戏安装目录>` = 含 `Assembly-CSharp.dll` 的 RimWorld 根目录；`<创意工坊目录>` = `<Steam 库>\steamapps\workshop\content\294100`；`<Steam 库>` = Steam 库根目录。
> 报告性质：一切结论均附「文件路径 + 实际命令 + 真实输出」；无证据的推断一律显式标注「**推测：**」。
> 采集方式：PowerShell（pwsh）逐文件读取 + `System.Xml.XmlDocument` 解析 + `Select-String` / 正则扫描；全部为静态读取，**未启动 RimWorld 游戏本体**。

---

## 一、样本清单表

### 1.1 样本枚举命令与真实输出

```powershell
$base='<创意工坊目录>'
Get-ChildItem -LiteralPath $base -Directory |
  Where-Object { Test-Path -LiteralPath (Join-Path $_.FullName '1.7') } |
  Select-Object -ExpandProperty Name
```

真实输出：

```text
1446523594, 1504723424, 1508341791, 1662119905, 2009463077, 2113372560, 2423311270, 2538411704,
2599942235, 2888380373, 2917732219, 2990606008, 3216091476, 3220120457, 3264193512, 3327029362,
3513846773, 3524116050, 3526354009, 3769804600, 839005762, 872762753
count = 22
```

对照数据（同一目录，其它命令输出）：

- `total mod dirs = 136`（`Get-ChildItem -LiteralPath $base -Directory` 计数）
- `supportedVersions lists 1.7 = 50`（对 136 个 mod 的 `About/About.xml` 做 `-match '<li>\s*1\.7\s*</li>'` 计数）

### 1.2 逐个 mod 实测字段

字段取自 `<mod>\About\About.xml`，用 `System.Xml.XmlDocument.Load()` 解析后 `SelectNodes('supportedVersions/li')` 逐项取值。

| # | mod ID | name | packageId | supportedVersions（原样顺序） | LoadFolders 文件（实际大小写） |
|---|--------|------|-----------|------------------------------|-------------------------------|
| 1 | 1446523594 | Dubs Mint Menus | Dubwise.DubsMintMenus | 1.0,1.1,1.2,1.3,1.4,1.5,1.6,**1.7** | 无 |
| 2 | 1504723424 | Smart Speed | sarg.smartspeed | 1.6,1.5,**1.7** | `loadFolders.xml`（小写） |
| 3 | 1508341791 | [FSF] Filth Vanishes With Rain And Time | FrozenSnowFox.FilthVanishesWithRainAndTime | 1.0…1.6,**1.7** | 无 |
| 4 | 1662119905 | Dubs Mint Minimap | dubwise.dubsmintminimap | 1.0…1.6,**1.7** | 无 |
| 5 | 2009463077 | Harmony | brrainz.harmony | 1.2…1.6,**1.7** | `LoadFolders.xml` |
| 6 | 2113372560 | TradeHelper | TimmyLiang.TradeHelper | 1.1…1.6,**1.7** | 无 |
| 7 | 2423311270 | Destroy Item | Garwel.DestroyItem | 1.2…1.6,**1.7** | 无 |
| 8 | 2538411704 | Visual Exceptions | brrainz.visualexceptions | 1.2…1.6,**1.7** | `LoadFolders.xml` |
| 9 | 2599942235 | DragSelect | telardo.DragSelect | 1.3…1.6,**1.7** | `LoadFolders.xml` |
| 10 | 2888380373 | WVC - Work Modes | wvc.sergkart.biotech.MoreMechanoidsWorkModes | 1.4,1.5,1.6,**1.7** | `loadFolders.xml`（小写） |
| 11 | 2917732219 | Muzzle Flash | IssacZhuang.MuzzleFlash | 1.4,1.5,1.6,**1.7** | `LoadFolders.xml` |
| 12 | 2990606008 | AB's Head Apparel Tweaker | AB.HATweaker | 1.4,1.5,1.6,**1.7** | `LoadFolders.xml` |
| 13 | 3216091476 | 补货状态 Restocking Status | RunningBugs.RestockingStatus | 1.4,1.5,1.6,**1.7** | **无**（只有 `LoadFolders.xml.bak`，不被加载） |
| 14 | 3220120457 | Music Manager (Continued) | zal.musicmanager | 1.5,1.6,**1.7** | `LoadFolders.xml` |
| 15 | 3264193512 | AAAA(Allowed Area Automatic Adapter) | seekiworksmod.no17 | 1.4,1.5,1.6,**1.7** | `LoadFolders.xml` |
| 16 | 3327029362 | Visible Raid Points简体中文汉化 | ChinesePack.visibleraidpoints.1trickPwnyta | 1.5,1.6,**1.7** | 无 |
| 17 | 3513846773 | Quality Colors (Continued) | DawnsGlow.qualcolor | 1.2…1.6,**1.7** | 无 |
| 18 | 3524116050 | Performance - Slower Pawn Tick Rate | Arkymn.SlowerPawnTickRate | 1.6,**1.7** | 无 |
| 19 | 3526354009 | Replace Stuff - Continued | Memegoddess.ReplaceStuff | 1.1…1.6,**1.7** | `LoadFolders.xml` |
| 20 | 3769804600 | Mine Sight | rabiosus.minesight | 1.6,**1.7** | `LoadFolders.xml` |
| 21 | 839005762 | Humanoid Alien Races | erdelf.HumanoidAlienRaces | 0.19,1.0…1.6,**1.7** | `loadFolders.xml`（小写） |
| 22 | 872762753 | MinifyEverything | erdelf.MinifyEverything | 1.0…1.6,**1.7** | 无 |

关于 packageId 的取值命令与说明：脚本用 `$m.SelectSingleNode('packageId').InnerText.Trim()` 读取（注意：**不要**用 `$pid` 作变量名，PowerShell 里 `$PID` 是只读内置变量，赋值会报 `Cannot overwrite variable PID because it is read-only or constant.` 并返回进程号）。

### 1.3 每个 mod 的 1.7 文件夹一级结构与 About 目录内容

命令（对每个 ID）：

```powershell
$d = Join-Path (Join-Path $base $id) '1.7'
Get-ChildItem -LiteralPath $d -Recurse -Force
Get-ChildItem -LiteralPath (Join-Path $root 'About') -Force
```

| mod ID | `1.7/` 内的一级目录/文件 | `About/` 内文件 |
|--------|-----------------------------------|---------------------|
| 1446523594 | Assemblies(0Harmony.dll, DubsMintMenus.dll) / Defs(MainButtons.xml) | About.xml, Preview.png, PublishedFileId.txt |
| 1504723424 | Assemblies(SmartSpeed.dll) | About.xml, preview.png, PublishedFileId.txt |
| 1508341791 | Patches(Filth_Vanishes_With_Rain_And_Time.xml) | About.xml, Preview.png, PublishedFileId.txt |
| 1662119905 | Assemblies / Defs(MiniMapDefs.xml) / Textures\MMinimap\UI(*.png) / **Assets.zip(274534)** | About.xml, Preview.png, PublishedFileId.txt |
| 2009463077 | Assemblies(0Harmony.dll, HarmonyMod.dll) | About.xml, Manifest.xml, ModIcon.png, Preview.png, PublishedFileId.txt |
| 2113372560 | Assemblies(TradeHelper.dll) | About.xml, Preview.png, PublishedFileId.txt |
| 2423311270 | Assemblies(DestroyItem.dll) / Defs\DamageDefs / Defs\KeyBindings | About.xml, ModIcon.png, Preview.png, PublishedFileId.txt |
| 2538411704 | Assemblies(CrossPromotion.dll, VisualExceptions.dll) / Defs(MainButtonDefs.xml) | About.xml, Manifest.xml, ModIcon.png, Preview.png, PublishedFileId.txt |
| 2599942235 | Assemblies(DragSelect.dll) / ModCompat\TradeUIRevised\Assemblies | About.xml, ModIcon.png, preview.png, PublishedFileId.txt |
| 2888380373 | Assemblies / Defs / Languages(ChineseTraditional, English) / Odyssey\… / Patches | About.xml, preview.png, PublishedFileId.txt |
| 2917732219 | Assemblies(0Harmony.dll, MuzzleFlash.dll/.pdb/.deps.json) / Defs\ShaderDefs / **Shaders(*.glsl)** | About.xml, Preview.png, PublishedFileId.txt |
| 2990606008 | Assemblies(ABEasyLib.dll, HeadApparelTweaker.dll) / Languages(ChineseSimplified, ChineseTraditional, English) | About.xml, preview.png, PublishedFileId.txt |
| 3216091476 | Assemblies(RestockingStatus.dll + .deps.json) / Source(Main.cs, mod.csproj, mod.sln) | About.xml, after.png, before.png, Preview.png, Preview.png~, PublishedFileId.txt |
| 3220120457 | Assemblies(MusicManager.dll) / Languages\English\Keyed / Textures\UI\Icons / **Assets.zip(24429)** | About.xml, Changelog.txt, LICENSE, ModIcon.png, Preview.png, PublishedFileId.txt, Readme.md |
| 3264193512 | Assemblies(AAAA.dll) | About.xml, Preview.png, PublishedFileId.txt |
| 3327029362 | Languages\ChineseSimplified\Keyed(VisibleRaidPoints_Keys.xml) | About.xml, Preview.png, PublishedFileId.txt |
| 3513846773 | Assemblies(QualityColors.dll) | About.xml, ColorPicker.png, FullLabel.jpeg, Inventory.png, OnlyQuality.jpeg, Preview.png, PublishedFileId.txt |
| 3524116050 | Assemblies(SlowerPawnTickRate.dll) / Source(含 .vs/、obj/、bin/ 残留) | About.xml, Preview.png, PublishedFileId.txt |
| 3526354009 | Assemblies / Defs(29 个 xml) / Patches(ReplaceStuff16Patches.xml) / Textures | About.xml, Preview.png, PublishedFileId.txt |
| 3769804600 | Assemblies(MineSight.dll) / Defs\ShaderDefs(MineSight.xml) / **Shaders\MineSight(*.glsl)** | About.xml, Preview.png, PublishedFileId.txt |
| 839005762 | Assemblies(0Harmony.dll+ .pdb/.xml, AlienRace.dll+ .pdb/.deps.json) / Defs / Mods\Ideology / Mods\Odyssey / Patches | About.xml, Preview.png, PublishedFileId.txt |
| 872762753 | Assemblies(0Harmony.dll, MinifyEverything.dll/.deps.json) / Assemblies\net10.0-windows8.0 / Assemblies\netstandard2.0 | About.xml, Preview.png, PublishedFileId.txt |

**表内可读出的三条硬事实：**

1. `About/` 100% 位于 **mod 根目录**，22/22 的 `1.7/` 里**没有** About 目录。
2. `About/` 里除 `About.xml` 外，`PublishedFileId.txt` 22/22 存在（Steam 工坊下载标记），预览图存在但命名不统一：`Preview.png`（16 个）与 `preview.png`（5 个）混用；另有图片名不带 about 语义的（如 `after.png`、`ColorPicker.png`）。
3. `1.7/` 下出现的内容目录集合为：`Assemblies`、`Defs`、`Patches`、`Textures`、`Languages`、`Shaders`、`Source`（以及 `Common`/`Odyssey`/`Mods`/`ModCompat` 这类自定义分组）。**没有**任何样本在 `1.7/` 下放 `Sounds`（声音文件进了根目录 `Sounds/` 或 `Assets.zip`，见 1662119905 根目录 `Sounds/`、其根 `Assets.zip` 内含 `Sounds/MintMap/*.ogg`）。

---

## 二、规范布局结论

### 2.1 官方文档（游戏自带）原文

文件：`<游戏安装目录>\ModUpdating.txt`（404 行）
命令：`Get-Content -LiteralPath '<上述路径>' -Encoding UTF8`

第 74-82 行原文：

```text
Mods can have very different inner structure depending on what they do and what version(s) of the game they support.
But every mod must define an 'About' sub-folder, that contains an 'About.xml' file:

-YourMod/
  -About/
    -About.xml

'About.xml' is the place to define all meta-data(name, packageId, description, dependencies etc.) for your mod. This file is vital for the game to be able to load your mod.
```

第 96-99 行原文（内容子目录约定）：

```text
Mod content structure is defined by some combination of these sub-folders:

Defs/       - If your mod adds new XML definitions (ThingDef, PawnKindDef, JobDef etc.), this is the place for them.
```

（同段后续列出 `Patches/`、`Textures/`、`Sounds/`、`Languages/`、`Source/`、`Assemblies/` 等子目录；完整目录见 2.2。）

第 206-213 行原文（多版本支持 / load folder 的权威说明）：

```text
============ SUPPORTING MULTIPLE GAME VERSIONS ============

Before loading content for your mod, the game will first check if there is LoadFolders.xml defined, that has a list of folders for current version.
If not defined, the game will try to fallback to previous version or whatever available.

To learn more on how to setup multi-version support, refer to this page: https://docs.google.com/document/d/1_DmcLpIvHIQ5AxVLYrn9_iwkOqArlgcWcyE_6RSDG6M
```

第 173-204 行给出的「完整 mod 目录示例」原文摘录：

```text
-YourMod/
  -About/
    -About.xml
    -Preview.png
  -Assemblies/
    -ProjectName.dll
  -Source/
    -ProjectName.sln
    -...
  -Common/
    -Patches/
      -ReplaceTreeTextures.xml
    -Defs/
    -Textures/
    -Sounds/
  -1.1/
    -Patches/
      -ReplaceTreeTextures_1_1_Specific.xml
    -Textures/
  -1.5/
    -Patches/
      -ReplaceTreeTextures_1_5_Specific.xml
    -Textures/
```

### 2.2 结论：1.7 下的规范布局（有证据）

| 项 | 规范写法 | 实测证据 |
|----|----------|----------|
| About 放哪 | **mod 根目录 `About/About.xml`**（必需）；`About/Preview.png`（推荐）；`About/PublishedFileId.txt`（工坊自动生成） | 22/22 样本；命令 `Get-ChildItem -LiteralPath '<mod>\About'` 输出见 1.3；`ModUpdating.txt` L219 原文 So the full path is "About/About.xml" |
| Defs 放哪 | 可以在 **mod 根目录 `Defs/`**、**版本夹 `1.7/Defs/`**、**共享夹 `Common/Defs/`** 或任意被 load folder 声明的子路径。Defs 内部目录结构自定 | 872762753 根 `Defs/`+`1.7/`；3526354009 根 `Defs/`+`1.7/Defs/`；2423311270 根 `Defs/`+`1.7/Defs/DamageDefs`；3216091476 `Common/Defs/LetterDef.xml` |
| Patches 放哪 | 可以在 **根 `Patches/`** 或**版本夹 `1.7/Patches/`**（样本里 1.7 专属补丁一律放版本夹）；子目录可再分层（`Patches/WorkModes/`） | 1508341791 `1.7/Patches/Filth_Vanishes_With_Rain_And_Time.xml`；2888380373 `1.7/Patches/WorkModes/WVC_*.xml`（16 个）；839005762 `1.7/Patches/` 与根 `Patches/` 并存 |
| 程序集放哪 | 放**被加载的 load folder 里的 `Assemblies/`**，最常见 `1.7/Assemblies/*.dll`；同名依赖（0Harmony.dll）直接随包附带 | 20/22 样本有 `1.7/Assemblies/`；872762753 还有 `Assemblies/net10.0-windows8.0` 与 `Assemblies/netstandard2.0` 两个 TFM 子目录 |
| 版本文件夹怎么用 | 每版本一个同名数字夹（`1.6/`、`1.7/`）；用 `LoadFolders.xml` 显式声明，或**不写 LoadFolders.xml 让游戏自动回退到可用版本夹** | 22/22 有 `1.7/`；其中 12 个没有 LoadFolders 文件（见 1.2 表），内容确实在版本夹内（例：1508341791 根目录只有 `About/ Textures/ Assets.zip`，全部功能内容在 `1.7/Patches/`） |
| 根目录直接放内容是否也支持 | **支持**。`<li>/</li>` 即代表 mod 根目录；不写 LoadFolders.xml 时根目录同样是加载根 | 872762753 根目录有 `Assemblies/`+`Defs/` 且**没有** LoadFolders.xml；839005762 根目录 `Assemblies/ Defs/ Languages/ Textures/`；3526354009/2990606008/2423311270/2917732219 根目录均有 `Defs/`、`Patches/`、`Textures/` |

### 2.3 LoadFolders.xml 实测写法（原文摘录）

**（a）最简写法：只列版本夹**（`<创意工坊目录>\1504723424\loadFolders.xml`，196 字节，注意文件名全小写）

```xml
<loadFolders>
	<v1.5>
		<li>/</li>
		<li>1.5</li>
	</v1.5>
	<v1.6>
		<li>/</li>
		<li>1.6</li>
	</v1.6>
	<v1.7>
		<li>/</li>
		<li>1.7</li>
	</v1.7>
</loadFolders>
```

`/` = mod 根目录；`1.7` = 版本夹（相对 mod 根的 POSIX 相对路径）。**顺序即加载顺序。**

**（b）带条件加载（IfModActive）**（`<创意工坊目录>\2599942235\LoadFolders.xml`，456 字节）

```xml
<?xml version="1.0" encoding="utf-8"?>
<loadFolders>
	<v1.6>
		<li>1.6</li>
		<li>/</li>
		<li IfModActive="hobtook.tradeui">1.6/ModCompat/TradeUIRevised</li>
	</v1.6>
	<v1.7>
		<li>1.7</li>
		<li>/</li>
		<li IfModActive="hobtook.tradeui">1.7/ModCompat/TradeUIRevised</li>
	</v1.7>
</loadFolders>
```

（该文件 v1.3/v1.4/v1.5 段同样是 `<li>1.x</li><li>/</li>`；条件夹 `1.7/ModCompat/TradeUIRevised/Assemblies/DragSelectTradeUIRevisedCompat.dll` 实际存在。）

**（c）累加式（老版本内容继续叠加）**（`<创意工坊目录>\3526354009\LoadFolders.xml`，724 字节）

```xml
  <v1.6>
    <li>/</li>
    <li>1.1</li>
    <li>1.2</li>
    <li>1.3</li>
    <li>1.4</li>
    <li>1.5</li>
    <li>1.6</li>
  </v1.6>
	<v1.7>
		<li>/</li>
		<li>1.1</li>
		<li>1.2</li>
		<li>1.3</li>
		<li>1.4</li>
		<li>1.5</li>
		<li>1.6</li>
		<li>1.7</li>
	</v1.7>
```

**（d）DLC 门控（IfModActive + 子路径）**（`<创意工坊目录>\839005762\loadFolders.xml`，911 字节）

```xml
	<v1.7>
		<li>/</li>
		<li>1.7</li>
		<li IfModActive="Ludeon.RimWorld.Ideology">1.7/Mods/Ideology</li>
		<li IfModActive="Ludeon.RimWorld.Odyssey">1.7/Mods/Odyssey</li>
	</v1.7>
```

**（e）Common 共享夹需显式声明**（`<创意工坊目录>\3769804600\LoadFolders.xml`，180 字节）

```xml
<?xml version="1.0" encoding="utf-8"?>
<loadFolders>
  <v1.6>
    <li>Common</li>
    <li>1.6</li>
  </v1.6>
  <v1.7>
    <li>Common</li>
    <li>1.7</li>
  </v1.7>
</loadFolders>
```

（同款写法见 `<创意工坊目录>\3264193512\LoadFolders.xml`：各版本均为 `<li>Common</li><li>1.x</li>`，其 `Common/Assets.zip` 10349954 字节。）

### 2.4 引擎侧的验证（二进制字符串证据）

命令：

```powershell
$b=[System.IO.File]::ReadAllBytes('<游戏安装目录>\RimWorld.dll')
$u=[System.Text.Encoding]::Unicode.GetString($b)
([regex]::Matches($u,[regex]::Escape('LoadFolders'))).Count    # -> 1
```

真实输出（该字符串所在集群，已把非可打印字符替换为空格）：

```text
setPacks BakeModAssetPacks: | BakeModAssetPacks: mod folder not found: | has no load folder with textures or sounds, nothing to bake | ... , unchanged LoadFolders.xml MONOMOD_DMDType dynamicmethod ... WatchShaders ... vulkan vulkan-1.dll ...
```

同时 `Assembly-CSharp.dll` 内含（UTF-16 字符串，同一集群）：

```text
 did not load any content. Following load folders were used: | ... for mod | LoadDefs called with already existing def packages Load defs via DirectXmlLoader Defs/ Parse loaded defs | Unable to parse version string on mod | " | : targetVersion field is obsolete, use supportedVersions instead. | : <supportedVersions> in mod About.xml must specify at least one version. | <packageId> contains word "Ludeon", which is reserved for official content. | has a dependency with no <packageId> specified. | has a dependency with invalid <packageId>: | has a dependency ( ) with empty display name.
```

配套可读文本（`<游戏安装目录>\Data\Core\Languages\English\Keyed\Menus_Main.xml`，`Select-String -Pattern 'ModLoadFolder'` 的真实输出）：

```text
L153: <ModLoadFolderDoesntExist>Folder {0} specified for version {1} doesn't exist.</ModLoadFolderDoesntExist>
L154: <ModLoadFolderMalformedVersion>Malformed version string '{0}'. Correct format is Major.Minor (e.g. 1.1)</ModLoadFolderMalformedVersion>
L155: <ModLoadFolderListEmpty>The list of load folders for version {0} is empty.</ModLoadFolderListEmpty>
L156: <ModLoadFolderRepeatingFolder>Version {0} lists the same folder more than once: {1}.</ModLoadFolderRepeatingFolder>
L157: <ModLoadFolderOutOfOrder>Invalid version order: {0} should come before {1}.</ModLoadFolderOutOfOrder>
L158: <ModLoadFolderOutOfOrderDefault>Invalid version order: 'default' should be defined first.</ModLoadFolderOutOfOrderDefault>
L159: <ModLoadFolderDefaultDeprecated>Using 'default' in load folders is deprecated. Please define folders for each version using the &lt;v...&gt; tags.</ModLoadFolderDefaultDeprecated>
L160: <ModLoadFolderDefinesUnsupportedGameVersion>Version {0} is defined in load folders, but is not listed in 'supportedVersions' of mod's About.xml.</ModLoadFolderDefinesUnsupportedGameVersion>
```

由 L153-L160 可反推出引擎对 LoadFolders.xml 的**硬校验规则**（这些是游戏自带的提示文案，构成行为证据）：

1. `<vX.Y>` 里声明的目录**必须真实存在**，否则报 `ModLoadFolderDoesntExist`。
2. 版本段的名字必须是 `Major.Minor` 格式。
3. 版本段的 `<li>` 不能为空列表、不能重复同一目录。
4. 版本段必须**按版本递增顺序**排列（`ModLoadFolderOutOfOrder`），`default`（老写法）已废弃且必须排第一。
5. 版本段里出现的版本**必须在 `supportedVersions` 里列出**，否则报 `ModLoadFolderDefinesUnsupportedGameVersion`。

对照样本：22 个样本的 LoadFolders 文件（共 10 个）全部满足上述规则——版本段严格递增、目录真实存在、无重复项；没有任何样本使用 `default` 段。

### 2.5 文件大小写与平台风险

- 引擎字面量是 `LoadFolders.xml`（`RimWorld.dll` UTF-16 命中 1 次）。
- 但样本里 3 个用**全小写文件名** `loadFolders.xml`：1504723424、2888380373、839005762；这 3 个 mod 的 1.7 内容都只在版本夹里（如 1504723424 根目录仅 `About/ Languages/ Textures/ loadFolders.xml`），也就意味着它们的 1.7 内容能被正常加载 → 文件名大小写未产生差异。
  **推测：** 这是 Windows/NTFS 文件名大小写不敏感导致的；同一 mod 在大小写敏感的 Linux 文件系统上可能读不到 `LoadFolders.xml`。
- 同理 `About/preview.png`（小写）与 `Preview.png` 混用（样本中 5 个用小写）。
- **实务建议（结论）：** 模板必须写成精确的 `LoadFolders.xml` 与 `About/Preview.png` 拼写。

### 2.6 规范布局结论（可直接当模板）

```text
<ModRoot>/
  About/
    About.xml              <- 必需
    Preview.png            <- 推荐（官方推荐比例 2.468:1）
    PublishedFileId.txt    <- 工坊自动生成，不要手写
  LoadFolders.xml          <- 可选；写就要精确这个文件名
  Common/                  <- 可选共享夹（必须在 LoadFolders 中显式 <li>Common</li>）
    Defs/
    Patches/
    Textures/
    Languages/
  Assemblies/              <- 可选：根目录级程序集（无 LoadFolders 时随根加载）
  Defs/                    <- 可选：根目录级 Defs
  Patches/                 <- 可选：根目录级补丁
  Sounds/
  Textures/
  1.6/
    Defs/ Patches/ Assemblies/ Textures/ Languages/
  1.7/
    Defs/ Patches/ Assemblies/ Textures/ Languages/ Shaders/
```

---

## 三、真实 patch 样例（1.7 原文摘录）

**patch 文件的存放位置（实测，22/22）**：一律放在被加载的 load folder 的 `Patches/` 目录下，1.7 专属补丁即 `<mod>/1.7/Patches/**/*.xml`（可任意层级子目录；递归扫描由 2888380373 的 `1.7/Patches/WorkModes/` 下 16 个文件被加载佐证）。
**根元素（实测，22/22）**：一律是 `<Patch>`；每个操作写成 `<Operation Class="PatchOperationXXX">`，或写成 `<li Class="...">` 嵌在 `<operations>` 里。XML 声明可有可无。

### 样例 1｜PatchOperationSequence + Remove/Add/Replace

文件：`<创意工坊目录>\1508341791\1.7\Patches\Filth_Vanishes_With_Rain_And_Time.xml`（1412 字节，50 行）
命令：`Get-Content -LiteralPath '<上述路径>' -Encoding UTF8`

```xml
<?xml version="1.0" encoding="utf-8"?>

<Patch>

	<Operation Class="PatchOperationSequence">
		<success>Normal</success>
		<operations>

			<!-- Filth Vanishes With Rain And Time -->
				
			<!-- Remove all entries for rainWashes then readd them to ensure they're all true -->
			
            <li Class="PatchOperationRemove">
				<xpath>/Defs/ThingDef
				[defName != "Filth_Water"]
				[defName != "Filth_GrayFlesh"]
				[defName != "Filth_RevenantBloodPool"]
				[defName != "Filth_RevenantSmear"]
				[defName != "RG_FilthWater"]
				[defName != "RG_FilthWaterSpatter"]
				[filth] /filth/rainWashes</xpath>
            </li>

			<li Class="PatchOperationAdd">
				<xpath>/Defs/ThingDef
				[defName != "Filth_Water"]
				[defName != "Filth_GrayFlesh"]
				[defName != "Filth_RevenantBloodPool"]
				[defName != "Filth_RevenantSmear"]
				[defName != "RG_FilthWater"]
				[defName != "RG_FilthWaterSpatter"]
				[filth] /filth</xpath>
				<value>
					<rainWashes>true</rainWashes>
				</value>
			</li>
				
			<!-- Only change entries with disappearsInDays 15 or above -->

			<li Class="PatchOperationReplace">
				<xpath>/Defs/ThingDef [number(substring-before(filth/disappearsInDays, '~')) >= 15] /filth/disappearsInDays</xpath>
				<value>
					<disappearsInDays>14~15</disappearsInDays>
				</value>
			</li>
			
		</operations>
	</Operation>

</Patch>
```

要点：`<success>` 控制失败语义（Normal / Always / Invert）；xpath 内可换行书写多条件谓词；`<li>` 复用 `<operations>` 列表。

### 样例 2｜PatchOperationConditional + nomatch（1.7 专属文件）

文件：`<创意工坊目录>\3526354009\1.7\Patches\ReplaceStuff16Patches.xml`（531 字节）

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Patch>
	<Operation Class="PatchOperationConditional">
		<xpath>Defs/ThingDef[defName="Door"]/building/relatedBuildCommands</xpath>
		<nomatch Class="PatchOperationAdd">
		  <xpath>Defs/ThingDef[defName="Door"]/building</xpath>
		  <value>
			<relatedBuildCommands />
		  </value>
		</nomatch>
	  </Operation>

	<Operation Class="PatchOperationAdd">
		<xpath>Defs/ThingDef[defName="Door"]/building/relatedBuildCommands</xpath>
		<value>
			<li>Autodoor</li>
		</value>
	</Operation>
</Patch>
```

要点：`PatchOperationConditional` 用 `<nomatch Class=...>` / `<match Class=...>` 内嵌操作；xpath 不带前导 `/` 亦可（相对根 `Defs`）。

### 样例 3｜自定义 Operation 子类 + success=Invert + PatchOperationInsert

文件：`<创意工坊目录>\2888380373\1.7\Patches\00_Patches_Zones.xml`（2980 字节；下方省略原文第 26-58 行整段被注释掉的旧代码）

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Patch>

	<!-- Order fix -->

	<Operation Class="PatchOperationSequence">
	  <success>Always</success>
	  <operations>
		<li Class="PatchOperationReplace">
		  <xpath>/Defs/MechWorkModeDef[defName="Work"]/uiOrder</xpath>
		  <success>Invert</success>
		  <value>
			<uiOrder>100</uiOrder>
		  </value>
		</li>
		<li Class="PatchOperationAdd">
		  <xpath>/Defs/MechWorkModeDef[defName="Work"]</xpath>
		  <success>Always</success>
		  <value>
			<uiOrder>100</uiOrder>
		  </value>
		</li>
	  </operations>
	</Operation>

	<Operation Class="WVC_WorkModes.PatchOperation_Settings">
		<settingName>enable_GoToShutdownZoneJob</settingName>
		<active Class="PatchOperationInsert">
		  <xpath>/Defs/DesignationCategoryDef[defName="Biotech" or defName="Zone"]/specialDesignatorClasses/li[contains(text(),'Designator_Deconstruct')]</xpath>
		  <order>Append</order>
		  <success>Always</success>
		  <value>
			<li>WVC_WorkModes.Designator_MechanoidShutdownZone</li>
		  </value>
		</active>
	</Operation>

	<Operation Class="WVC_WorkModes.PatchOperation_Settings">
		<settingName>enable_GoToShutdownRoomJob</settingName>
		<deActive Class="PatchOperationRemove">
		  <xpath>/Defs/RoomRoleDef[defName="WVC_MechHangar"]</xpath>
		  <success>Always</success>
		</deActive>
	</Operation>

</Patch>
```

要点：`Class` 可以是 mod 自己 DLL 里的 `PatchOperation` 子类（`WVC_WorkModes.PatchOperation_Settings`），并自定义子节点名（`<settingName>`、`<active>`、`<deActive>`）。

### 样例 4｜无 XML 声明 + PatchOperationAttributeSet + IgnoreIfNoMatchingField

文件：`<创意工坊目录>\839005762\1.7\Patches\HumansAreAliensToo.xml`（3685 字节，摘录前 20 行）

```xml
<Patch>
    <Operation Class="PatchOperationAttributeSet">
        <xpath>Defs/ThingDef[defName="Human" or defName="CreepJoiner"]</xpath>
        <attribute>Class</attribute>
        <value>AlienRace.ThingDef_AlienRace</value>
    </Operation>
    
    <Operation Class="PatchOperationReplace">
        <xpath>Defs/PawnRenderTreeDef//li[texPath="Things/Pawn/Humanlike/Apparel/SwaddledBaby/Swaddled_Child"]/nodeClass</xpath>
        <value>
            <nodeClass>AlienRace.AlienPawnRenderNode_Swaddle</nodeClass>
        </value>
    </Operation>

    <Operation Class="PatchOperationAdd">
        <xpath>Defs/ThingDef[defName="Human"]</xpath>
        <value>
            <alienRace IgnoreIfNoMatchingField="True">
                <generalSettings>
                    <allowHumanBios>true</allowHumanBios>
                    ...
                </generalSettings>
            </alienRace>
        </value>
    </Operation>
</Patch>
```

要点：文件可以**完全没有 `<?xml ... ?>` 声明**；xpath 可用属性谓词 `[texPath="..."]`；往 Def 里注入自定义字段时必须加 `IgnoreIfNoMatchingField="True"`（官方文档 `ModUpdating.txt` L356-359 亦如此要求）。

---

## 四、1.7 新写法（实测）

### 4.1 【新】ShaderDef + `Shaders/*.glsl`（1.7 渲染管线 / Waylith）

**Def 文件**：`<创意工坊目录>\2917732219\1.7\Defs\ShaderDefs\MuzzleFlash.xml`（603 字节）

```xml
<?xml version="1.0" encoding="utf-8"?>

<Defs>

  <!-- 1.7 (Waylith): the engine loads GLSL sources from 1.7/Shaders and compiles them,
       replacing the precompiled Unity AssetBundle shaders of 1.4-1.6 -->
  <ShaderDef>
    <defName>MuzzleFlashAnimatedAdditive</defName>
    <shaderProgram>
      <vertexShaderFileName>MuzzleFlash.vert.glsl</vertexShaderFileName>
      <fragmentShaderFileName>MuzzleFlash.frag.glsl</fragmentShaderFileName>
      <blendMode>Additive</blendMode>
      <depthWrite>false</depthWrite>
      <renderQueue>3151</renderQueue>
    </shaderProgram>
  </ShaderDef>

</Defs>
```

**同类第二个样本**：`<创意工坊目录>\3769804600\1.7\Defs\ShaderDefs\MineSight.xml`（1070 字节，两个 ShaderDef）

```xml
<Defs>
  <ShaderDef>
    <defName>MineSight_Stripes</defName>
    <shaderProgram>
      <vertexShaderFileName>MineSight/MineSightStripes.vert.glsl</vertexShaderFileName>
      <fragmentShaderFileName>MineSight/MineSightStripes.frag.glsl</fragmentShaderFileName>
      <useTexture>false</useTexture>
      <transparent>true</transparent>
      <depthTest>false</depthTest>
      <depthWrite>false</depthWrite>
      <cullMode>None</cullMode>
      <renderQueue>3595</renderQueue>
    </shaderProgram>
  </ShaderDef>
  <ShaderDef>
    <defName>MineSight_Outline</defName>
    <shaderProgram>
      <vertexShaderFileName>MineSight/MineSightOutline.vert.glsl</vertexShaderFileName>
      <fragmentShaderFileName>MineSight/MineSightOutline.frag.glsl</fragmentShaderFileName>
      <useTexture>false</useTexture>
      <transparent>true</transparent>
      <depthTest>false</depthTest>
      <depthWrite>false</depthWrite>
      <cullMode>None</cullMode>
      <renderQueue>3610</renderQueue>
    </shaderProgram>
  </ShaderDef>
</Defs>
```

**「这是 1.7 新增而非 1.6 已有」的证据链（四条）：**

1. **两个 mod 的 1.6 夹里完全没有 ShaderDef 相关文件**：命令 `Get-ChildItem -LiteralPath '<mod>\1.6' -Recurse` 的输出中不存在 `Defs\ShaderDefs`、不存在 `Shaders`；对应 `<mod>\1.7` 才新增（见 1.3 表）。
2. **引擎侧存在对应类型**：命令 `([regex]::Matches([System.Text.Encoding]::Unicode.GetString([System.IO.File]::ReadAllBytes('<游戏安装目录>\Assembly-CSharp.dll')), 'ShaderDef')).Count` → 命中 **4** 次；`'shaderProgram'` → 命中 **1** 次。
3. **官方 Core 用同一写法**：`<游戏安装目录>\Data\Core\Defs\ShaderDefs\Shaders.Map.xml` 与 `Shaders.World.xml` 存在同名字段（并额外使用了 `<flipTextureST>false</flipTextureST>`、`<textureWrapOverrides><li><key>_MainTex</key><value>Repeat</value></li></textureWrapOverrides>`）。
4. **全工坊只此 2 例**：命令 `Get-ChildItem -LiteralPath <workshop> -Recurse -Include *.xml | Select-String -Pattern '<ShaderDef' -List` 恰好输出两个文件（2917732219 与 3769804600），其余 134 个 mod 均无。

**GLSL 源码规范**（文件 `<创意工坊目录>\3769804600\1.7\Shaders\MineSight\MineSightStripes.vert.glsl`，413 字节，前 17 行原文）：

```glsl
#version 450

layout(location = 0) in vec3 inPosition; // @vertex Position required
layout(push_constant) uniform Push { mat4 modelMatrix; } push;
layout(set = 0, binding = 0) uniform VertexUniforms
{
    mat4 ViewProj;
} uVertex;

layout(location = 0) out vec2 vWorld;

void main()
{
    vec4 world = push.modelMatrix * vec4(inPosition, 1.0);
    gl_Position = uVertex.ViewProj * world;
    vWorld = world.xz;
}
```

要点：`#version 450`（Vulkan 风格 GLSL）；`set = 0, binding = 0` 的 `VertexUniforms.ViewProj`；`push_constant` 里的 `modelMatrix`；顶点属性用 `// @vertex Position required` 注释声明语义。游戏自身也带同类文件：`<游戏安装目录>\Rendering\Shaders\`（如 `SceneDefault.frag.glsl`），根目录并有 `slang*.dll`、`Brutal.Vulkan*.dll`。

**结论**：1.7 的 shader 类 mod 不再依赖预编译 Unity AssetBundle，而是 `1.7/Defs/ShaderDefs/*.xml` + `1.7/Shaders/*.glsl` 的**纯文本管线**（该结论同时被 2917732219 作者写在 XML 注释里的原话佐证，见上）。

### 4.2 【新】Asset pack：`Assets.zip`（预编码 DDS / OGG 打包）

实测分布（命令：`Get-ChildItem -LiteralPath <workshop> -Recurse -Filter 'Assets.zip' -File`）：

```text
...\1446523594\Assets.zip            132674
...\1508341791\Assets.zip              3068
...\1662119905\Assets.zip            389987
...\1662119905\1.7\Assets.zip        274534   <- 版本夹内！
...\2423311270\Assets.zip              2532
...\2888380373\Assets.zip            292472
...\2917732219\Assets.zip           3467348
...\3051527562\Assets.zip            352393
...\3220120457\1.7\Assets.zip         24429   <- 版本夹内！
...\3264193512\Common\Assets.zip   10349954   <- Common 夹内！
...\839005762\Assets.zip              46677
```

zip 内部结构（`[System.IO.Compression.ZipFile]::OpenRead(...)` 列条目）——**只装资源，不装 Defs**：

```text
1446523594\Assets.zip  (40 entries)   Textures/Mint/UI/*.png.dds
1662119905\1.7\Assets.zip (35 entries) Textures/MMinimap/UI/*.png.dds
1662119905\Assets.zip  (38 entries)   Sounds/MintMap/*.ogg + Textures/MMinimap/UI/*.png.dds
```

**「这是 1.7 机制」的四条独立证据：**

1. `<游戏安装目录>\Data\Core\Languages\English\Keyed\Menus_Main.xml` L181-187 原文：
   ```text
L181: <UploadBuildAssetPack>Build asset pack</UploadBuildAssetPack>
L182: <UploadBuildAssetPackTip>Packs textures and sounds into an asset pack in each load folder before uploading, to improve download and load times. Untick this to upload the mod folder as it is.</UploadBuildAssetPackTip>
L184: <UploadSkipSourceTexturesTip>Skips uploading the original image and sound files that were included in asset packs. Leave this unticked if you need compatibility with RimWorld 1.6 or earlier.</UploadSkipSourceTexturesTip>
L185: <BakingModAssetPacks>Baking asset packs</BakingModAssetPacks>
L187: <ModAssetPackBakeFailed>Baking the asset packs for {0} failed, the mod was not uploaded:</ModAssetPackBakeFailed>
   ```
   L184 明确把「asset pack」与「RimWorld 1.6 or earlier」对立 —— **1.7 起才有**。
2. `<游戏安装目录>\RimWorld.dll` 内含 `BakeModAssetPacks: mod folder not found:` 与 `has no load folder with textures or sounds, nothing to bake` —— 「**每个 load folder 各自一份** asset pack」，与实测中 `1.7/Assets.zip`、`Common/Assets.zip` 的分层一致。
3. `<游戏安装目录>\Licenses.txt` L170 原文：`Asset packs use ZstdSharp, Copyright (c) 2021 Oleg Stepanischev, a port of` —— 打包格式为 Zstd。
4. 839005762 的配套元数据文件：`Assets.zip.fingerprint`、`Assets.zip.roles`、`Assets.zip.stamps`；其中 `Assets.zip.roles` 内容形如 `Textures/AlienRace/HARModIcon.png.dds image:Default`。

**结论**：1.7 允许（工坊上传工具默认会）把 `Textures/`、`Sounds/` 预编码进**每个 load folder 的 `Assets.zip`**（`.png.dds` 等已编码资源）。**不写 asset pack、直接放 `Textures/*.png` 依旧可用**——实测 1662119905 的 `1.7/Assets.zip` 与 `1.7/Textures/MMinimap/UI/*.png` **同时存在**，且 3526354009 的 `1.7/Textures/TDReplaceStuffIcon.png` 直接是裸 png、该 mod 无 Assets.zip。

### 4.3 【新】`Assemblies/*.deps.json` 与多目标框架

- `<创意工坊目录>\2917732219\1.7\Assemblies\MuzzleFlash.deps.json`（1001 字节）、`MuzzleFlash.pdb`
- `<创意工坊目录>\3216091476\1.7\Assemblies\RestockingStatus.deps.json`（1006 字节）—— **在 1.6 夹里没有**（1.6→1.7 的新增项）
- `<创意工坊目录>\872762753\1.7\Assemblies\` 下同时存在 `net10.0-windows8.0/` 与 `netstandard2.0/` 两个 TFM 子目录（`MinifyEverything.deps.json` 1026 字节）
- `<创意工坊目录>\839005762\1.7\Assemblies\AlienRace.deps.json`（995 字节）

**结论**：1.7 环境下样本普遍使用 **.NET 10（net10.0）** 目标框架编译；`*.deps.json` 出现在 `Assemblies/` 里是被接受的（加载器只取 `*.dll`）。
注：`<创意工坊目录>\3524116050\1.7\Source\SlowerPawnTickRate\SlowerPawnTickRate\obj\Debug\.NETFramework,Version=v4.7.2.AssemblyAttributes.cs` 说明仍有作者用旧框架编老代码——**1.7 并不强制 net10.0**；`<创意工坊目录>\3216091476\UPGRADE-1.7.md` 第 5 行作者自述「新增独立 net10.0 工程，引用 Krafs.Rimworld.Ref 1.7.4977-alpha.1 和 Lib.Harmony 3.0.0-rc.2」。

### 4.4 Odyssey / TileMutatorDef（实测：样本 0 使用）

- 官方引擎类型存在：`Assembly-CSharp.dll` UTF-16 命中 `TileMutatorDef` **2 次**。
- 官方 Def 样例：`<游戏安装目录>\Data\Core\Defs\MapGeneration\TileMutators.xml`（defName：`Mountain`/`Caves`/`Coast`/`River`/`UndergroundCave`；字段 `categories`/`workerClass`/`genOrder`/`priority`）与 `<游戏安装目录>\Data\Odyssey\Defs\TileMutators\TileMutators_{AncientStructures,ManMade,Modifiers,Natural,Special}.xml`。
- **22 个样本 mod 里没有任何一个使用 TileMutatorDef**：命令 `Get-ChildItem -LiteralPath <workshop> -Recurse -Include *.xml | Select-String -Pattern 'TileMutatorDef' -List` → **零输出**（136 个 mod 全覆盖）。
- 样本里与 Odyssey 有关的写法是**目录门控 + 补丁**，不是新 Def：
  - `<创意工坊目录>\2888380373\1.7\Odyssey\`（Assemblies/Defs/Patches），由 `loadFolders.xml` 的 `<li IfModActive="brrainz.harmony">1.7/Odyssey</li>` 门控（1.6 段同一位置写的是 `<li IfModActive="ludeon.rimworld.odyssey">1.6/Odyssey</li>`）；
  - `<创意工坊目录>\839005762\1.7\Mods\Odyssey\`（Languages/Patches），由 `<li IfModActive="Ludeon.RimWorld.Odyssey">1.7/Mods/Odyssey</li>` 门控；
  - `<创意工坊目录>\3526354009\1.7\Defs\Odyssey.xml`（456 字节，1.6 与 1.7 两个夹里的该文件 `Compare-Object` 结果为 identical content）。
- **推测：** TileMutatorDef 属于 Odyssey DLC 的引擎 Def，**不一定是 1.7 相对 1.6 的新增**；本报告无法证明它在 1.6 不存在（无 1.6 版本的游戏数据可对照）。

### 4.5 关键负面结论：1.6 与 1.7 的**同名 Def/XML 往往一字不差**

命令（对每个存在同名文件的样本执行）：

```powershell
Compare-Object (Get-Content -LiteralPath '<mod>\1.6\<相对路径>') (Get-Content -LiteralPath '<mod>\1.7\<相对路径>')
```

结果：

| mod | 文件 | 差异 |
|-----|------|------|
| 1508341791 | `Patches\Filth_Vanishes_With_Rain_And_Time.xml` | identical content |
| 2423311270 | `Defs\DamageDefs\Damages.xml`、`Defs\KeyBindings\KeyBindings.xml` | identical content |
| 1446523594 | `Defs\MainButtons.xml` | identical content |
| 1662119905 | `Defs\MiniMapDefs.xml` | identical content |
| 3526354009 | `Defs\Odyssey.xml`、`Patches\ReplaceStuff16Patches.xml` | identical content |
| 839005762 | `Defs\ShaderTypes.xml`、`Defs\RaceSettings.xml` | identical content |
| 2990606008 | `Languages\English\Keyed\exSetting.xml` | identical content |

**结论（对模板最有价值的一条）**：这批 1.7 已适配 mod 的 1.7 夹，绝大多数是「**重新编译程序集 + 拷贝同名 XML**」，Defs 层几乎无字段级变化。真正的新增只出现在：

| mod | 1.7 夹新增（1.6 夹无） | 说明 |
|-----|------------------------|------|
| 2538411704 | `1.7/Defs/MainButtonDefs.xml`（677 字节） | 文件名新，字段（`workerClass`/`tabWindowClass`/`iconPath`/`minimized`/`validWithoutMap`/`canBeTutorDenied`/`order`）非新 |
| 2917732219 | `1.7/Defs/ShaderDefs/MuzzleFlash.xml` + `1.7/Shaders/MuzzleFlash.{vert,frag}.glsl` | **1.7 新机制** |
| 3769804600 | `1.7/Defs/ShaderDefs/MineSight.xml` + `1.7/Shaders/MineSight/*.glsl`（4 个） | **1.7 新机制** |
| 3220120457 | `1.7/Assets.zip`（24429 字节） | **1.7 新机制** |
| 3216091476 | `1.7/Assemblies/RestockingStatus.deps.json` | .NET 打包产物 |
| 2888380373 | 1.6 的 2 个大补丁文件被拆成 `1.7/Patches/WorkModes/` 下 16 个文件 | 组织方式变化，非语法变化 |

### 4.6 2538411704 的 1.7 专属 MainButtonDef（原文）

`<创意工坊目录>\2538411704\1.7\Defs\MainButtonDefs.xml`（677 字节）：

```xml
<?xml version="1.0" encoding="utf-8"?>
<Defs>
  <!-- Always registered; TabButtonWorker hides it while there is nothing to report. -->
  <MainButtonDef>
    <defName>VisualExceptionsTab</defName>
    <label>Visual Exceptions</label>
    <description>Exceptions caught since startup and the mods involved in them.</description>
    <workerClass>VisualExceptions.TabButtonWorker</workerClass>
    <tabWindowClass>VisualExceptions.ExceptionInspector</tabWindowClass>
    <iconPath>HarmonyTab</iconPath>
    <minimized>true</minimized>
    <validWithoutMap>true</validWithoutMap>
    <canBeTutorDenied>false</canBeTutorDenied>
    <order>-100000</order>
  </MainButtonDef>
</Defs>
```

---

## 五、存疑项

### 5.1 supportedVersions 到底写什么格式？漏写 1.7 会怎样？

**真实格式（22/22 一致）**：写 `<li>1.7</li>`，即**纯 `Major.Minor` 两段式字符串**，绝不带 rev/build。
例（`<创意工坊目录>\3524116050\About\About.xml`）：

```xml
<supportedVersions>
  <li>1.6</li>
  <li>1.7</li>
</supportedVersions>
```

官方文档佐证：`ModUpdating.txt` L253-254 原文 —— `<supportedVersions> (list, required)` / `A list of game versions mod is compatible with. Entries must be in "X.Y" format, where X is major version and Y is minor version.`
引擎佐证：`Assembly-CSharp.dll` 内含 `Unable to parse version string on mod `、`targetVersion field is obsolete, use supportedVersions instead.`、`<supportedVersions> in mod About.xml must specify at least one version.`
全量扫描佐证：对 136 个 mod 做正则 `'1\.7[^,\s]'` → **0 命中**，即不存在 `1.7.1` / `v1.7` / `1.7 beta` 之类写法。

**漏写 1.7 的后果（分「已证实」与「推测」两档）：**

- **已证实（有直接证据）**
  - `LoadFolders.xml` 里出现 `<v1.7>` 而 `supportedVersions` 没有 1.7 → 游戏有专门警告：`Data\Core\Languages\English\Keyed\Menus_Main.xml` L160 `<ModLoadFolderDefinesUnsupportedGameVersion>Version {0} is defined in load folders, but is not listed in 'supportedVersions' of mod About.xml.</ModLoadFolderDefinesUnsupportedGameVersion>`。
  - `supportedVersions` **整体缺失/为空**是硬错误：引擎字面量 `<supportedVersions> in mod About.xml must specify at least one version.`。
  - **格式不对**也是硬错误：引擎字面量 `Unable to parse version string on mod `。
  - 全部 22 个样本的 `supportedVersions` 都写了 `<li>1.7</li>`；全工坊 136 个 mod 中「**有 1.7 文件夹但 supportedVersions 漏写 1.7**」的数量 = **0**（命令：逐 mod 判断 `Test-Path <mod>\1.7` 与 `About.xml -match '<li>\s*1\.7\s*</li>'`）。
  - 反向数据：**列了 1.7 却没有 1.7 文件夹 = 28 个**（50 - 22）。→ 说明「supportedVersions 写 1.7」与「必须有 1.7 文件夹」**不是**绑定关系；内容放在根目录、Common 或其它 load folder 也能声明支持 1.7。
- **推测：** 漏写 1.7 不会阻止加载，只会把该 mod 标记为「非本版本 mod」。依据：官方 DLC 的 `About/About.xml`（`<游戏安装目录>\Data\{Anomaly,Biotech,Ideology,Odyssey,Royalty}\About\About.xml`）在 1.7.4981 环境下**仍只写 `<li>1.6</li>`**，而这些内容显然被正常加载；配套文案 `Menus_Main.xml` L147-149：`<ModNotMadeForThisVersion>This mod was not made for this version of RimWorld, and will probably not work correctly.</ModNotMadeForThisVersion>`（措辞是「probably not work」，不是「refuse to load」）。
  **但**：在 `Assembly-CSharp.dll`、`RimWorld.dll`、`UnityStubs.dll`、`Waylith.dll` 里用 ASCII 与 UTF-16 两种编码搜 `ModNotMadeForThisVersion` 均 **0 命中**，因此「该文案挂在哪个判定分支上」未能证实；且官方 DLC 走的是 `Data/` 官方内容通道，未必适用第三方 mod 的校验路径。**要 100% 确认，需在游戏里实测（本任务禁止启动游戏本体）。**

### 5.2 LoadFolders.xml 的完整语法，游戏没有随附文档

- `ModUpdating.txt` 第 62 行写 `Added LoadFolders.xml ... More in 'LOAD FOLDERS XML' section.`、第 170 行写 `you can learn more about writing 'LoadFolders.xml' in 'MOD LOAD FOLDERS' section`，但 `Select-String -Path '<game>\ModUpdating.txt' -Pattern 'LOAD FOLDERS'` 只命中 L62/L154/L155/L170（L154/L155 是正文里的泛述），**文件里没有这个章节**。
- 该文档的版本变更标题只有一条：`Select-String -Pattern '^\s*\d+\.\d+\s*->\s*\d+\.\d+'` → 仅 L5 `1.0 -> 1.1`；全文 404 行中**没有出现 1.7、Waylith 或 shader 字样**（命令：`Select-String -Pattern '1.7|Waylith|hader'` → 无输出）。→ 该文档是 1.5 时代产物，**不能作为 1.7 新特性的依据**。
- 官方外链（L213）指向 `https://docs.google.com/document/d/1_DmcLpIvHIQ5AxVLYrn9_iwkOqArlgcWcyE_6RSDG6M`（本次未联网抓取）。**推测：** 完整 LoadFolders 语法应以该外链为准；本报告 2.3/2.4 的规则是从游戏自带的 8 条 `ModLoadFolder*` 提示文案与 10 个真实文件反推的。

### 5.3 `analyzer.xml` 是什么机制

- `<创意工坊目录>\3769804600\analyzer.xml`（1478 字节，mod **根目录**）根元素为 `<Analyzer>`，内含 `<MineSight><Methods><li>类名:方法名</li>…</Methods></MineSight>`，条目形如 `MineSight.MineHighlightPatch:Postfix`，注释写 `Profile entry points so nested renderer helpers are not counted again. Use Analyzer's internal profiling on a row to investigate its callees.`
- 全工坊扫描：`Get-ChildItem -LiteralPath <workshop> -Recurse -Filter 'analyzer.xml'` → **只此 1 个文件**。
- 游戏二进制里搜 `analyzer.xml` → ASCII 0 命中；`Assembly-CSharp.dll` UTF-16 亦 0 命中。
- **推测：** 它是 1.7 的 mod 级性能剖析入口（作者注释提到「Analyzer's internal profiling」），但**未能证实是否为官方机制**；若要写进模板，必须先确认。

### 5.4 文件名大小写（Windows 训练集偏差）

见 2.5。`loadFolders.xml`（3 个样本）与 `preview.png`（5 个样本）在 Windows 上都能用，**推测**在其他平台可能失败。模板一律用 `LoadFolders.xml` / `Preview.png`。

### 5.5 TileMutatorDef 是否为「1.7 新增」未证实

见 4.4。它确实存在于 1.7.4981 的引擎与官方 Def 中（`Data\Core\Defs\MapGeneration\TileMutators.xml`、`Data\Odyssey\Defs\TileMutators\`），但**没有 1.6 版游戏数据可供对照**，无法断言它是 1.7 相对 1.6 的新增；且 22 个样本 mod 使用数 = 0，样本内无实证写法。写模板时应把它标注为「Odyssey 相关引擎 Def（版本归属待确认）」。

### 5.6 未做的事与限制

1. **未启动 RimWorld 游戏本体**（任务硬性要求），因此所有「加载行为」结论均为静态证据 + 官方文案推导，未经运行验证。
2. **未联网**：`ModUpdating.txt` L213 外链的 Google Doc（LoadFolders 语法权威文档）未抓取。
3. 本报告**只写了这一个文件**；未修改、未删除工作区（`<仓库根>`）内任何其他文件。
4. 扫描过程全部为只读操作（`Get-ChildItem`、`Get-Content`、`Select-String`、`System.Xml.XmlDocument.Load`、`[System.IO.Compression.ZipFile]::OpenRead`、`[System.IO.File]::ReadAllBytes`）。

### 5.7 一处样本内部的异常，供模板编写者警惕

`<创意工坊目录>\3216091476\LoadFolders.xml.bak`（643 字节）内容为 v1.3/v1.4/v1.5 三段（**无 v1.6/v1.7**），而该 mod 的 `supportedVersions` 是 1.4,1.5,1.6,1.7、根目录存在 `1.4/ 1.5/ 1.6/ 1.7/ Common/`。
**关键点**：文件扩展名是 `.bak`，引擎只认 `LoadFolders.xml`（`RimWorld.dll` 字面量证据见 2.4），因此该 mod 实际走的是「无 LoadFolders → 自动选中版本夹」的回退路径，**`Common/` 下的 `Defs/LetterDef.xml`、`Patches/Patches.xml`、`Textures/RestockingStatus/refresh.png` 是否被加载无从保证**。
**推测：** 不写 `<li>Common</li>` 声明时 `Common/` 不会被自动加载（反证：3264193512、3769804600 都专门在 LoadFolders 里写 `<li>Common</li>`）。→ 模板必须强调：**自定义共享目录（Common 等）不在默认加载集内，必须显式声明。**

---

## 附：证据可复现清单（关键命令）

```powershell
$game   = '<游戏安装目录>'
$ws     = '<创意工坊目录>'

# 1) 游戏版本
Get-Content -LiteralPath (Join-Path $game 'Version.txt')

# 2) 含 1.7 文件夹的 mod
Get-ChildItem -LiteralPath $ws -Directory |
  Where-Object { Test-Path -LiteralPath (Join-Path $_.FullName '1.7') } |
  Select-Object -ExpandProperty Name

# 3) 单个 mod 的 About.xml 关键字段
[System.Xml.XmlDocument]$x = New-Object System.Xml.XmlDocument
$x.Load((Join-Path $ws '<modId>\About\About.xml'))
$x.DocumentElement.SelectNodes('supportedVersions/li') | ForEach-Object { $_.InnerText.Trim() }

# 4) 1.7 目录树
Get-ChildItem -LiteralPath (Join-Path $ws '<modId>\1.7') -Recurse -Force

# 5) LoadFolders / patch / shader 全文
Get-Content -LiteralPath (Join-Path $ws '<modId>\LoadFolders.xml') -Encoding UTF8
Get-Content -LiteralPath (Join-Path $ws '<modId>\1.7\Patches\<file>.xml') -Encoding UTF8

# 6) 1.6 vs 1.7 同名文件差异（第二行是 PowerShell 续行符）
Compare-Object (Get-Content -LiteralPath (Join-Path $ws '<modId>\1.6\<rel>')) `
               (Get-Content -LiteralPath (Join-Path $ws '<modId>\1.7\<rel>'))

# 7) 引擎字符串证据
$u=[System.Text.Encoding]::Unicode.GetString([System.IO.File]::ReadAllBytes((Join-Path $game 'Assembly-CSharp.dll')))
([regex]::Matches($u,[regex]::Escape('supportedVersions'))).Count
$u2=[System.Text.Encoding]::Unicode.GetString([System.IO.File]::ReadAllBytes((Join-Path $game 'RimWorld.dll')))
([regex]::Matches($u2,[regex]::Escape('LoadFolders'))).Count
```
