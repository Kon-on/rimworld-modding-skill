# RimWorld 1.7 代码形态梳理

> 本文所有数字与结论均来自本机安装实测（RimWorld **1.7.4981 rev136**，路径 `<游戏安装目录>`），
> 可用配套脚本在 `docs/` 目录重新生成全部统计结果。凡属推断而非实测的内容，均已显式标注「推测」。

---

## 0. 一句话结论

1.7 **没有改 Def 的 XML 写法**，但**换了引擎和运行时**：Unity 被 Ludeon 自研的 Waylith 引擎顶替，Mono 被自研 CLR 顶替，
目标框架升到 **.NET 10（net10.0）**。对 mod 作者的实际影响集中在三点：**Harmony 改为外部 mod 提供**、
**UnityEngine.＊ API 只剩垫片**、**渲染管线改为 Vulkan + GLSL**。XML Def 与 PatchOperation 的写法基本不变。

---

## 1. 版本与安装事实

| 项目 | 实测值 |
|---|---|
| 版本 | 1.7.4981 rev136（`Version.txt`） |
| 官方内容 | Core、Royalty、Ideology、Biotech、Anomaly、Odyssey（6 个） |
| Def XML 文件数 | 1,560 |
| Def 实例数 | 14,070 |
| Def 类型数 | **254** |
| 安装根 `Mods/` | 空（0 项） |
| 创意工坊 mod | 136 个（appid 294100），其中 **22 个已含 1.7 文件夹** |
| 用户配置目录 | `AppData\LocalLow\Ludeon Studios\RimWorld by Ludeon Studios` |

---

## 2. 1.7 最大的变化：引擎换成 Waylith

### 2.1 证据

```json
tfm = "net10.0"
includedFrameworks = Microsoft.NETCore.App 10.0.13-waylithclr.dev
WaylithClr.AssemblyNameRedirects = "UnityEngine*=UnityStubs;Unity.Newtonsoft.Json=;
                                    Unity.*=UnityStubs;Assembly-CSharp-firstpass=UnityStubs"
WaylithClr.JitPatchableAssemblies = "Assembly-CSharp"
```

安装根目录出现了一批全新二进制：`Waylith.dll`、`Waylith.AssetBake.dll`、
`Waylith.UnityCompat.dll`、`Waylith.VideoDecode.dll`、`Brutal.Core/Vulkan/Gltf/ImGui.dll`、
`slang-compiler.dll`、`coreclr.dll`，以及新的 `vulkan/` 与 `Rendering/` 目录。
旧的 `RimWorld_Data/`、`UnityPlayer.dll` 已不存在；
`Readme.txt` 却仍在描述 Unity 时代的结构（**已过时，不可作为依据**）。

`Rendering/Shaders/` 下是 19 个 GLSL 源文件（`SceneDefault.frag.glsl`、
`SceneDefault.vert.glsl`、BC1/BC4/BC5/BC7 压缩 Compute、`MipmapDownsample`、`Nv12ToRgba`、
`PostFxComposite.frag.glsl` 等），说明渲染后端已是 Vulkan + Slang/GLSL，**不是** Unity 的 ShaderLab。

### 2.2 Unity 的位置：只剩垫片

`Assembly-CSharp.dll` 里 `Verse` 出现 755 次，`UnityEngine` 仅 **17 次**，
`MonoBehaviour` 仅 **1 次**。残留引用只剩 `UnityEngine.Profiling`（→ Waylith.Profiling）、
`UnityEngine.Jobs`（→ Unity.Jobs）、`UnityEngine.Rendering`（→ Waylith.Rendering）、
`SceneManagement`、`UI`、`Analytics` 等零星几处。
UnityEngine 的公开面由 **`UnityStubs.dll`** 顶替，它提供 36 个 `UnityEngine.＊` 命名空间占位。

> **对 mod 的含义（重要）**：任何依赖 `GameObject` / `Transform` / `Material` / `Shader` /
> `Texture2D` / `Time` / `Input` 等 Unity 运行时 API 的旧 mod 代码，在 1.7 上都不再可靠。
> 纯 Verse 命名空间（Def、Thing、Pawn、Map、Comp、Job）的代码不受影响。

### 2.3 但 Assembly-CSharp.dll 仍是标准托管程序集

实测：PE32（Magic = 0x10B），COR20 元数据目录存在（rva = 0x2008，size = 72），节区 `.text/.rsrc/.reloc` 齐全。
所以 **IL 元数据完整存在**，可以反编译、可以反射、也可以被 JIT 打补丁
（`WaylithClr.JitPatchableAssemblies = "Assembly-CSharp"` 明确允许）。这也是 Harmony 在 1.7 仍能工作的基础。

### 2.4 Harmony 不再内置

递归搜索游戏安装目录，`＊Harmony＊` 命中 **0 个文件**。Harmony 现在是独立创意工坊 mod（**2009463077**），
其 1.7 目录内含 `0Harmony.dll` 与 `HarmonyMod.dll`。

> **对 mod 的含义**：1.7 的 C# mod 要么**自己带** `0Harmony.dll`，要么在 About.xml 里声明依赖 Harmony mod。
> 不能假设玩家环境里已有 Harmony 被游戏预加载。

---

## 3. Def 体系的实测规模

对 `Data/<资料片>/Defs` 下全部 XML 做逐元素路径统计（`docs/extract_def_schema.py`），得到：

| 指标 | 数值 |
|---|---|
| Def 类型 | 254 |
| Def 实例 | 14,070 |
| 字段路径（类型 × 路径累计） | 13,329 |
| 解析失败 | 0 |

### 3.1 按线分布

| 线 | 类型数 | 实例数 | 字段路径数 | 说明 |
|---|---:|---:|---:|---|
| 人物线 | 46 | 3,683 | 2,292 | Pawn、特性、基因、背景、Hediff、心情、技能、能力 |
| 物品线 | 18 | 2,603 | 3,072 | ThingDef 家族、配方、材料分类、武器特性、伤害 |
| 世界线 | 98 | 2,080 | 5,148 | 派系、事件、任务、地形、生物群系、世界物体、异常 |
| 理念线 | 23 | 701 | 772 | 戒律、信条、仪式、文化、图标 |
| 表现线 | 26 | 2,927 | 1,242 | 音效、Fleck、Effecter、材质、着色器、渲染树 |
| 系统线 | 43 | 2,076 | 803 | 研究、工作、Job、Stat、AI、规则包 |
| **合计** | **254** | **14,070** | **13,329** | |

> 世界线类型多但实例少：Anomaly 把 16 个通灵仪式各自做成一个 Def 子类
>（`PsychicRitualDef_BloodRain`、`_Brainwipe`、`_Chronophagy` …），每个通常只有 1 个实例。

### 3.2 规模最大的 12 个类型

| Def 类型 | 实例 | 字段路径 | 线 |
|---|---:|---:|---|
| ThingDef | 2,054 | 2,699 | 物品 |
| SoundDef | 1,233 | 113 | 表现 |
| ThoughtDef | 933 | 65 | 人物 |
| BackstoryDef | 845 | 132 | 人物 |
| HediffDef | 344 | 475 | 人物 |
| RulePackDef | 340 | 15 | 系统 |
| PawnKindDef | 333 | 277 | 人物 |
| FleckDef | 327 | 115 | 表现 |
| JobDef | 321 | 33 | 系统 |
| EffecterDef | 285 | 82 | 表现 |
| StatDef | 256 | 164 | 系统 |
| PreceptDef | 223 | 245 | 理念 |

### 3.3 资料片覆盖

| 资料片 | 出现的 Def 类型数 |
|---|---:|
| Core | 170 |
| Anomaly | 110 |
| Odyssey | 93 |
| Biotech | 91 |
| Ideology | 78 |
| Royalty | 57 |

其中 **50 种类型只在 Core 出现**，**137 种类型跨 2 个及以上资料片**。

---

## 4. 六条线怎么分

分类按 **modder 的心理模型** 划分，不按游戏内部命名空间：

- **人物线** — 想做一个新种族 / 新职业背景 / 新特性 / 新基因 / 新病，看这里。
- **物品线** — 想做一把枪 / 一件衣服 / 一栋建筑 / 一只动物 / 一个新配方，看这里。
- **世界线** — 想做一个新派系 / 新事件 / 新地形 / 新星球层，看这里。
- **理念线** — Ideology 资料片的戒律、信条、仪式体系。
- **表现线** — 音效、粒子、光效、材质、小人渲染树。做美术与特效的看这里。
- **系统线** — 研究、工作类型、Job、Stat、AI 思维树等底层系统。

每个类型属于哪条线，见 [全量字段索引](03-全量字段参考/00-字段索引.md)。

---

## 5. 1.7 上值得注意的几个具体现象

### 5.1 Def 类型名存在大小写容错（实测确认）

原版自己就有两处大小写不一致，而且**都能正常工作**：

| 位置 | 写法 | 实例数 |
|---|---|---|
| `Biotech/Defs/JobDefs/Jobs_Learning.xml` 第 16/22/28/34/40 行起 | 小写 `<jobDef>` | 5 |
| `Core/Defs/BackstoryDefs/Solid/Solid_Rare.xml` 第 4 行 | 大写 `<BackStoryDef Abstract="True" Name="Solid">` | 1 |

**为什么可以断定这是被容忍的、而不是失效的**：`Solid_Rare.xml` 里后续约 800 个背景故事全部写
`<BackstoryDef ParentName="Solid">`。如果第 4 行那个抽象父定义因大小写没被识别，
所有子定义都会因找不到父定义而报错 —— 而实测游戏正常加载。
Biotech 的 5 个小写 `<jobDef>`（Radiotalking、Floordrawing、Workwatching、Lessontaking、Lessongiving）
也都是游戏里真实存在的 Job。

> **建议**：能容忍 ≠ 应该写。**自己写 mod 一律用正确大小写**（`JobDef`、`BackstoryDef`）。
> 容错是 Ludeon 的兼容手段，未来版本可能收紧。

### 5.2 Anomaly 引入了一批 Def 子类型名

`PsychicRitualDef_＊`（16 个）、`RoomPart_＊Def`（4 个）、`CreepJoiner＊Def`（5 个）、
`BossDef`、`BossgroupDef`、`MonolithLevelDef`、`EntityCategoryDef` 等，
都是 **Def 子类**而非新机制。写它们的 XML 时，根元素名直接用这个子类名。

### 5.3 Odyssey 带来的新家族

`GravshipComponentTypeDef`、`PlanetLayerDef`、`PlanetLayerSettingsDef`、
`ScatterableDef`、`LandingOutcomeDef`、`NegativeFishingOutcomeDef`、
`OrbitalDebrisDef`、`TransportShipDef`、`ShipJobDef` —— 
围绕星球层 / 重力船 / 坠落的一组新 Def。

### 5.4 小人渲染改用 PawnRenderTreeDef

1.7 里 `PawnRenderTreeDef` 有 11 个实例、72 条字段路径，配合 `PawnRenderNodeTagDef`、
`AnimationDef`、`GraphicStateDef`、`RenderSkipFlagDef` 组成新的渲染描述体系。
做自定义小人外观时**优先查这几个类型**，不要直接套用 1.4 时代 `GraphicSet` 的写法
（后者在 1.7 的兼容状态标注为「推测」）。

---

## 6. 本次交付物怎么用

```text
RimWorld-1.7-代码模板集/
├── README.md            从这里开始
├── 01-梳理报告/          本文 + 254 类型总表
├── 02-模板/             手写精讲模板（人物/物品/世界/理念/表现/系统/C#）
├── 03-全量字段参考/      254 种类型的字段表 + 最小真实范例
└── 04-核验/             机器核验脚本与结果
```

两条路：

1. **我想照着做一个东西** → 去 `02-模板/`，找同类模板，改 defName 和数值。
2. **我要查某个字段到底存不存在** → 去 `03-全量字段参考/字段/<DefType>.md`，看全量字段表与出现率。

---

## 7. 怎么核验本文与模板

**字段级核验（可复现）**：`docs/extract_def_schema.py` 重新扫一遍本机 Def XML，产出 `def-schema.json`；
`docs/build_tier_b.py` 据此生成 254 份字段表。任何人重跑这两步都能得到同样的数字。

**模板级核验**：`04-核验/verify_templates.py` 把 `02-模板/` 下每个 XML 里的元素路径抽出来，
逐条比对 `def-schema.json` 中同类型的路径集合，输出「已证实 / 待验证」清单。

**出现率怎么读**：某字段在该类型原版实例中的出现比例。≥90% 基本必填；40–90% 常见可选；<10% 属于特例用法。
本数据集里出现率最低的路径也至少在原版真实出现过一次 —— 也就是说，字段表里没有凭空造出来的路径。

---

## 8. 局限与未验证项（如实说明）

| 项 | 状态 |
|---|---|
| Def XML 写法 | **实测确认**（14,070 个实例逐路径统计） |
| 引擎替换 / .NET 10 / Waylith CLR | **实测确认**（runtimeconfig.json + 安装目录二进制 + 着色器源码） |
| Harmony 外置 | **实测确认**（安装目录 0 命中；mod 2009463077 内含 0Harmony.dll） |
| Def 类型名大小写容错 | **由必要性推证**（见 5.1），未做运行时验证 |
| C# 模板中的具体 API 签名 | **标注「待验证」**，需反编译 `Assembly-CSharp.dll` 逐条确认 |
| 各 mod 的 1.7 迁移实际改法 | 由样本 mod 归纳，非官方文档 |
| `ModUpdating.txt` | **已过时**，最新小节仍是 1.0→1.1 |
| `Readme.txt` | **已过时**，仍在描述 Unity 时代的结构 |

---

*生成环境：RimWorld 1.7.4981 rev136 + 全部 6 个官方资料片；统计脚本位于 `docs/`，可复跑。*