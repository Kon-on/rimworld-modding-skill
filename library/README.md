# RimWorld 1.7 代码模板集

> **一句话**：把环世界 **1.7.4981 rev136**（本机安装版）里**实际存在的** 254 种 Def 类型、13,329 条字段路径、38 份可照着写的模板（另附 1 份 C# 失效清单数据附录），全部从游戏本体数据里提取出来，**每条字段都能对照原版 XML 核验**。
>
> 不依赖任何外部资料、不依赖 MCP、不联网查文档——**唯一事实来源就是 E:\SteamLibrary\steamapps\common\RimWorld\Data**。

## 30 秒速览

| 项目 | 数值 |
|---|---|
| 游戏版本 | 1.7.4981 rev136（`Version.txt`） |
| 资料片 | Core、Royalty、Ideology、Biotech、Anomaly、Odyssey |
| Def 类型 | **254 种** |
| Def XML 文件 | 1,560 个 |
| Def 实例 | 14,070 个 |
| 字段路径 | **13,329 条**（含出现率与样例值） |
| 唯一 defName | 11,710 个 |
| 手写模板 | **38 份**（32 份 XML + 6 份 C#），07-CSharp 另附 1 份《UnityStubs 失效成员清单》数据附录 |
| 机械核验结果 | **1,829** 条元素路径逐条判定，**1,800 条对照原版证实**，1 条待验证（原版从不使用的 `modExtensions`），0 条属于错误类型 |
| C# 接口核对 | 6 份 C# 模板用到的类型/成员/参数逐条比对 3 个 DLL：**0 处不存在、0 处签名不符**（1 处编译不过的问题已修） |

## 目录结构与用法

```
RimWorld-1.7-代码模板集/
├── 01-梳理报告/          # 先看这里：代码形态梳理 + 1.6→1.7 迁移指南
├── 02-模板/              # 照着写：分 7 条线的 38 份模板
│   ├── 01-人物线/  7 份   PawnKindDef、BackstoryDef、TraitDef、GeneDef、HediffDef、ThoughtDef、AbilityDef
│   ├── 02-物品线/  7 份   ThingDef（武器/衣物/建筑/动物）、RecipeDef、WeaponTraitDef、SpecialThingFilterDef
│   ├── 03-世界线/  6 份   FactionDef、IncidentDef、WeatherDef、BiomeDef、TerrainDef、WorldObjectDef
│   ├── 04-理念线/  4 份   PreceptDef、MemeDef、RitualPatternDef、IdeoIconDef
│   ├── 05-表现线/  4 份   SoundDef、FleckDef、EffecterDef、PawnRenderTreeDef
│   ├── 06-系统线/  4 份   ResearchProjectDef、WorkTypeDef、WorkGiverDef、JobDef
│   └── 07-CSharp/  7 份   Mod 入口、ThingComp/HediffComp、JobDriver/WorkGiver、Harmony、自定义 Def 类、UnityStubs、附录：UnityStubs 失效成员清单（254 条）
├── 03-全量字段参考/       # 查字段：254 种全量字段表 + 字段总表.csv（13,329 行）
│   ├── 00-字段索引.md
│   ├── 字段/<DefType>.md  × 254
│   └── 字段总表.csv
└── 04-核验/              # 查证据：核验结果.md/.csv（XML 字段 1,829 条逐条判定）+ C#接口核对结果.md
```

### 三条使用路径

1. **要写一个新 mod** → 进 `02-模板/<对应线>/`，找最接近的类型，把模板里的 `EXAMPLE_*` 改成自己的名字，按「字段说明」表增删字段。
2. **要确认某个字段到底存不存在 / 怎么写** → 进 `03-全量字段参考/字段/<DefType>.md`，看「出现率」一列：**≥90% 就是事实上的必填**，0% 附近的写法要警惕。也可直接搜 `字段总表.csv`。
3. **要把 1.6 的 mod 迁到 1.7** → 直接看 `01-梳理报告/1.6到1.7迁移指南.md` 的 A/B/C 三张表。

## 事实来源与可复现性

所有内容均由脚本从游戏本体提取，**不启动游戏、不反编译全部方法体**，命令可复跑：

```powershell
# 1) 提取 254 种 Def 的字段 schema（产出 docs/def-schema.json）
python docs/extract_def_schema.py

# 2) 提取每个类型的最小/中位真实范例（产出 docs/def-examples.json）
python docs/extract_def_examples.py

# 3) 生成 03-全量字段参考 下全部文件
python docs/build_tier_b.py

# 4) 把 02-模板 里所有 XML 元素路径对照 schema 核验（产出 04-核验/*）
#    脚本在 docs\ 下（它会按自身位置推算仓库根目录，必须原地运行）
python docs/verify_templates.py
```

> 本机 Python 用 DSH 捆绑版：`...\office-runtime\primary-runtime\dependencies\python\python.exe`（自带 lxml）。

## 核验结果怎么读

`04-核验/核验结果.md` 把模板里 **1,829 条**元素路径逐条判定（CSV 共 1,830 行，多出的 1 行是新增附录文件「无 XML 代码块」的占位记录）：

| 判定 | 条数 | 含义 |
|---|---|---|
| 已证实 | 1,800 | 该路径在同名 Def 类型的原版全量字段表里存在（原版确实这么写） |
| 待验证 | 1 | `ThingDef/modExtensions`：全本体 0 次出现，该机制是 mod 专用的，无法用原版数据证实（核验确实抓到过 2 条真错误——`race/soundCall`、`race/soundAngry` 应写在 `race/lifeStageAges/li/` 下——已修正后复跑归零） |
| 自定义 | 1 | 位于 `Class="ExampleMod.*"` 的自定义组件子树内，本体当然没有 |
| 片段 | 20 | 不是以 `<Defs>` 为根的写法示意块（如单独的 `<comps>`），不做字段比对 |

同时 38 份模板全部通过结构一致性检查：**32 份 XML 模板**统一为「用途 / 模板 / 字段说明（字段｜出现率｜值类型｜说明）/ 常见坑 / 核验」，**6 份 C# 模板**统一为「用途 / 代码 / 常见坑 / 核验」（其中 `06-UnityStubs兼容层与失效API` 按「不能用了 / 还可用 / 新写法」三段组织，另有 `01-Mod入口` 含 1.7 关键差异小节）。

C# 模板另做了一轮**接口核对**（`04-核验/C#接口核对结果.md`）：用反射读完三个 DLL 的全部类型与成员 —— `Assembly-CSharp.dll`（版本 1.7.9786.4087 / 16,221 类型）、`UnityStubs.dll`（934 类型 / 6,653 方法）、`0Harmony.dll`（3.0.0.0 / 2,326 类型），把 6 份模板里用到的每个类型、方法、字段、参数（含默认值）逐条比对：**0 处类型/成员不存在、0 处签名不符**。过程中改掉 1 处「编译不过」级别的问题（`WorkGiver_Scanner` 实际在 `RimWorld` 命名空间，模板缺 `using RimWorld;`）和 5 处数字/命名空间表述。UnityStubs 的 **254 个 stub 调用点（230 个唯一成员 / 88 个类型）**完整清单见 `02-模板/07-CSharp/07-附录-UnityStubs失效成员清单.md`。

## 1.7 你必须知道的三个结论

1. **引擎换了，Def 体系没换**：1.7 把 Unity 换成了自研 **Waylith** 引擎（`RimWorld.runtimeconfig.json` 里 `tfm=net10.0`、`includedFrameworks=Microsoft.NETCore.App 10.0.13-waylithclr.dev`，`UnityEngine.*` 被重定向到 `UnityStubs`）。但 **Def XML 层没有观察到任何强制新字段**——7 组同时含 1.6/1.7 目录的 mod，两版同名 XML 逐字节相同。
2. **C# 要重编**：目标框架 net472 → **net10.0**，引用 `Assembly-CSharp.dll` + `UnityStubs.dll`（**不要引用 `UnityEngine.*.dll`，1.7 已无这些文件**）。
3. **Harmony 不在游戏里了**：改用独立创意工坊 mod **2009463077**（0Harmony 3.0.0.0-rc.3 / net10.0），About.xml 里要用 `<modDependencies>` 声明。

## 已知局限（如实说明）

| 项 | 状态 |
|---|---|
| C# 模板的运行期行为 | **未验证**。类型/成员存在性已逐条机器核对（见 `04-核验/C#接口核对结果.md`），但**没有启动游戏跑过**；Harmony 3.0 走 MonoMod 原生 detour，与自研 WaylithClr 的 JIT 探测是否兼容，只能实跑才知道 |
| 1.7 官方迁移文档 | **不存在**。游戏里的 `ModUpdating.txt` 只更新到 1.0→1.1，`Readme.txt` 还是旧的 `---_Data` 时代说明，**都不能当 1.7 依据** |
| 模板风格 | 38 份模板由多轮产出合并（部分为不同批次撰写），**正文措辞略有差异**，但小节结构统一、字段已 100% 机械核验 |
| 逻辑行为类结论 | 诸如「某字段越大越靠前」「未知字段是否报错」这类**运行期行为**，均已在原文标注「待验证 / 推测」 |
| 覆盖范围 | 手写模板覆盖 **38 个高频类型**；其余 216 种类型有一份**自动生成的字段参考 + 最小真实范例**（`03-全量字段参考`） |

## 怎么自己再核验一遍

1. 打开 `04-核验/核验结果.csv`，随便挑几行「已证实」的路径；
2. 到游戏本体 `Data\<资料片>\Defs` 里搜同名字段，看原版是否真的这么写；
3. 或者直接重跑 `python docs/verify_templates.py`（脚本在 `docs\`，按自身位置推算仓库根目录），结果应当完全一致（脚本只读游戏目录，不改任何文件）。
