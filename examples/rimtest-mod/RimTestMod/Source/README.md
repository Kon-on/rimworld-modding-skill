# RimTestMod —— 1.7 C# 编译现实记录（README）

> // AI 辅助生成
> 本文记录的是**在本机 RimWorld 1.7 实测得到的事实**，不是从 1.6 文档抄来的。
> 凡是没实测过的，本文一律标注「**未核实**」，不写成结论。
> 编写者：Line B（C# 编译线）。上游规格：`examples/rimtest-mod/_SPEC.md` 第 6 节。

---

## 0. 一句话结论

**1.7 上可以用这套工具链真正编译出 mod DLL**：`dotnet SDK 10.0.401` + `TargetFramework=net10.0` +
引用游戏根目录的 `Assembly-CSharp.dll` / `UnityStubs.dll` / `RimWorld.dll`（**全部 `Private=false`**），
产物落在本 mod 自己的 `Assemblies/`（`examples/rimtest-mod/RimTestMod/Assemblies/`）。两条编译路径（SDK / 裸 csc）都已跑通，见 §5。

**但 hjson/XML 时代的 C# 文档几乎全错**：UnityEngine 的具体类型在 1.7 已换成 `UnityStubs.dll` 兼容层，
1.6 的 `UnityEngine.CoreModule.dll`、`.NET Framework 4.7.2`、`RimWorldWin64_Data/Managed/` 三样东西**在这台机器上全部不存在**。
冲突清单见 §8。

---

## 1. 产物与本次真实构建结果

| 程序集 | 文件 | 字节 | 程序集版本 | SHA256 前 16 位 |
|---|---|---|---|---|
| 主程序集 | `Assemblies/RimTestMod.dll` | **11,776 B** | 1.0.0.0 | `C716008693023578` |
| 补丁程序集 | `Assemblies/RimTestMod.Patches.dll` | **12,800 B** | 1.0.0.0 | `D41381E1B5393BB1` |

最终一次运行的原始输出（默认路径 `dotnet build`）：

```
== 6. 摘要
名称                字节 版本
----                ---- ----
RimTestMod         11776 1.0.0.0
RimTestMod.Patches 12800 1.0.0.0
  [OK]   构建结束：全部检查通过
EXITCODE=0

已成功生成。  0 个警告  0 个错误      (RimTestMod)
已成功生成。  0 个警告  0 个错误      (RimTestMod.Patches)
```

> `Assemblies/` 里**只有这两个 .dll**。没有游戏 DLL、没有 `0Harmony.dll`、没有 `.deps.json`
> （`<GenerateDependencyFile>false</GenerateDependencyFile>` 压掉后者）。build.ps1 第 5 段会**反向检查**这一点，混进禁止清单里的 DLL 直接判失败。

### 产物真实依赖面（用 `System.Reflection.Metadata` 读 AssemblyRef 表，不是猜的）

| 产物 | AssemblyRef 表实际内容 |
|---|---|
| `RimTestMod.dll` | `System.Runtime`, `Assembly-CSharp` |
| `RimTestMod.Patches.dll` | `System.Runtime`, `Assembly-CSharp`, `UnityStubs`, `0Harmony`, `RimTestMod` |

**这张表就是「主程序集不依赖 Harmony 也能加载」的证据**：`RimTestMod.dll` 的依赖表里没有 `0Harmony`，
也没有 `UnityStubs`。即使 Harmony mod 没装、或 Harmony 与 Waylith 不兼容，主程序集照样能被游戏加载。

> **副产品发现**：两个 csproj 都引用了 `RimWorld.dll`，但两个产物的 AssemblyRef 表里**都没有它** ——
> Roslyn 会省略「引了但一个类型都没用到」的程序集引用。所以 AssemblyRef 表可以拿来精确刻画真实依赖面，
> 比 csproj 的 `<Reference>` 列表更可信。

---

## 2. 目标框架：为什么是 `net10.0`

**因为游戏自己就是 net10.0，mod 必须跟它一致。**

读 `E:\SteamLibrary\steamapps\common\RimWorld\RimWorld.runtimeconfig.json` 得到的原文事实：

```
"tfm": "net10.0",
"includedFrameworks": [ { "name": "Microsoft.NETCore.App", "version": "10.0.13-waylithclr.dev" } ]
"configProperties": {
   "WaylithClr.AssemblyNameRedirects": "UnityEngine*=UnityStubs;Unity.Newtonsoft.Json=;Unity.*=UnityStubs;Assembly-CSharp-firstpass=UnityStubs",
   "WaylithClr.JitPatchableAssemblies": "Assembly-CSharp",
   "WaylithClr.LaxAssemblyBinding": true,
   "WaylithClr.SkipAccessChecks": true
}
```

要点：
- 1.7 的运行时不是 Mono，也不是 .NET Framework，而是 **WaylithCLR（`10.0.13-waylithclr.dev`）**。
- `WaylithClr.AssemblyNameRedirects` 那行说明：**任何名为 `UnityEngine*` 的程序集都会被重定向到 `UnityStubs`**。
  这就是「不要引用 `UnityEngine.CoreModule.dll`」的根本原因 —— 那个文件本来也不存在。
- `WaylithClr.LaxAssemblyBinding=true` 是我们能容忍下面那条 CS1701 警告的底气（见 §4 坑 3）。

**目标框架契约：`<TargetFramework>net10.0</TargetFramework>`，本机 SDK `10.0.401`，运行时 `Microsoft.NETCore.App 10.0.2 / 10.0.12`。**
（引用框架用的是 `C:\Program Files\dotnet\packs\Microsoft.NETCore.App.Ref\10.0.12\ref\net10.0`。）

---

## 3. 引用了哪些 DLL，为什么

| 引用 | 路径 | 谁需要 | 为什么 |
|---|---|---|---|
| `Assembly-CSharp.dll` | 游戏根目录 | 主程序集 + 补丁 | **所有 `Verse.*` / `RimWorld.*` 游戏类型都在这里面**。注意它同时在 `RimWorld.dll` 里放了一小部分类型，见 §4 坑 1 |
| `UnityStubs.dll` | 游戏根目录 | 只有补丁程序集 | 1.7 的 Unity 兼容层（935 类型 / 7471 方法）。补丁里用到 `UnityEngine.Vector3`（`Projectile.ExactPosition`）所以才引 |
| `RimWorld.dll` | 游戏根目录 | 两个都引了，但**都没实际用到** | 保险起见引上；产物 AssemblyRef 里没有它（Roslyn 省略） |
| `0Harmony.dll` | **创意工坊 Harmony mod**：`E:\SteamLibrary\steamapps\workshop\content\294100\2009463077\1.7\Assemblies\0Harmony.dll` | 只有补丁程序集 | 游戏本体**不带** Harmony，只有装了 Harmony mod 才有 |

### 硬约束遵守情况

- ❌ **不引用也不复制任何 `UnityEngine.*.dll`** —— 因为游戏根目录下一个都没有（`Get-ChildItem *UnityEngine*` 零命中）。
- ✅ **不把游戏 DLL 复制进 `Assemblies/`**：所有 `<Reference>` 都带 `<Private>false</Private>`，编译期只读引用。
- ✅ **不复制 `0Harmony.dll`**（虽然用户允许作为 MIT 例外）：Harmony mod 自己会提供，重复打包会触发
  `HarmonyMod` 的 *"Another Harmony library was loaded before the Harmony mod could."* 告警并降级。
  build.ps1 只在编译期引用它。
- ✅ **没有改动游戏安装目录任何文件**：build.ps1 全程只 `Get-ChildItem` / `Test-Path` 游戏目录和工坊目录，写操作只落在本 mod 目录（`examples/rimtest-mod/RimTestMod/`）的 `Assemblies/` 与 `obj/build/` 下。

### 第三方库来源与许可证（按要求标注）

```
0Harmony.dll
  来源  : E:\SteamLibrary\steamapps\workshop\content\294100\2009463077\1.7\Assemblies\0Harmony.dll
  归属  : Harmony mod（packageId brrainz.harmony，作者 Andreas Pardeike，modVersion 3.0.1.0）
  程序集: 0Harmony v3.0.0.0，大小 2,532,864 B
  许可证: MIT License, Copyright (c) 2017 Andreas Pardeike
  用途  : 仅编译期引用（-r: / <Reference Private=false>）；本 mod 的 Assemblies/ 中不包含该文件
```

---

## 4. 完整命令 + 踩到的坑

### 4.1 日常构建（推荐）

```powershell
# 在仓库根执行（脚本用 $PSScriptRoot 自己定位 mod 目录）；默认 dotnet SDK 路径
& 'examples\rimtest-mod\RimTestMod\Source\build.ps1'

# 备选：裸 Roslyn csc.dll（不用 MSBuild / 不生成 csproj）
& 'examples\rimtest-mod\RimTestMod\Source\build.ps1' -UseCsc

# 自定义游戏/工坊目录
& '...\build.ps1' -GameDir 'D:\Steam\...\RimWorld' -HarmonyDir 'D:\...\2009463077\1.7\Assemblies'
```

脚本自带 6 段：①依赖校验 → ②清目录 → ③编译 → ④产物核验（AssemblyRef）→ ⑤**反向检查**（Assemblies 里不许有游戏 DLL / 0Harmony.dll）→ ⑥摘要。
任一检查失败累加计数，最后 `exit 1`（实测过：第一次就是 `EXITCODE=1`，修完才 `EXITCODE=0`）。

### 4.2 摊开来讲的话，这两条路径实际执行的命令

**路径 A（默认，`dotnet build`）** —— 脚本自动生成两个临时 csproj 到 mod 的 `obj/build/proj/`（`examples/rimtest-mod/RimTestMod/obj/build/proj/`）：

```powershell
dotnet build 'examples\rimtest-mod\RimTestMod\obj\build\proj\RimTestMod.csproj'         -c Release
dotnet build 'examples\rimtest-mod\RimTestMod\obj\build\proj\RimTestMod.Patches.csproj' -c Release
```

**路径 B（`-UseCsc`，不依赖 MSBuild）**：

```powershell
dotnet exec "C:\Program Files\dotnet\sdk\10.0.401\Roslyn\bincore\csc.dll" "@<obj/build/csc-RimTestMod.rsp>"
dotnet exec "C:\Program Files\dotnet\sdk\10.0.401\Roslyn\bincore\csc.dll" "@<obj/build/csc-RimTestMod.Patches.rsp>"
```

响应文件由脚本生成，形状是（`-refDlls` 会把 ref pack 下 167 个 DLL 全量 `-r:` 进去）：

```
-nologo
-nostdlib+
-target:library
-langversion:latest
-optimize+
-deterministic+
-platform:anycpu
-debug-
-warn:4
-out:"examples\rimtest-mod\RimTestMod\Assemblies\RimTestMod.Patches.dll"
-r:"C:\Program Files\dotnet\packs\Microsoft.NETCore.App.Ref\10.0.12\ref\net10.0\System.Runtime.dll"
...（ref pack 全部 167 个）
-r:"E:\SteamLibrary\steamapps\common\RimWorld\Assembly-CSharp.dll"
-r:"E:\SteamLibrary\steamapps\common\RimWorld\UnityStubs.dll"
-r:"...\2009463077\1.7\Assemblies\0Harmony.dll"
-r:"examples\rimtest-mod\RimTestMod\Assemblies\RimTestMod.dll"
"examples\rimtest-mod\RimTestMod\Source\Patches\PatchCommon.cs"   ...（补丁源文件）
"examples\rimtest-mod\RimTestMod\obj\build\AssemblyInfo.RimTestMod.Patches.cs"   （脚本生成的版本号，见坑 4）
```

### 坑 1【最重要】命名空间 ≠ 程序集：`RimWorld.MessageTypeDefOf` 其实住在 `Assembly-CSharp.dll` 里

第一次编译 exit 1，唯一错误：

```
ThingComp_TestShield.cs(220,75): error CS0103: 当前上下文中不存在名称"MessageTypeDefOf"
```

我原以为「`RimWorld.` 前缀的类型在 `RimWorld.dll`，`Verse.` 前缀的在 `Assembly-CSharp.dll`」——**这个直觉是错的**。
用自建探针（`SigProbe one GAME RimWorld.MessageTypeDefOf`，`GAME` = `Assembly-CSharp.dll`）实测：
`MessageTypeDefOf` 就在 **Assembly-CSharp 里面**，是 `public static class`，字段 `NeutralEvent` 等。
修法：`using RimWorld;` 即可，**不需要额外引用**。

顺带实测到 `Verse.Messages` 的真实重载（1.6 教程里的写法对不上）：

```
METHOD public static System.Void Messages::Message(System.String text, Verse.MessageTypeDef def, System.Boolean historical = True)
METHOD public static System.Void Messages::Message(System.String text, Verse.LookTargets lookTargets, Verse.MessageTypeDef def, System.Boolean historical = True)
METHOD public static System.Void Messages::Message(System.String text, Verse.LookTargets lookTargets, Verse.MessageTypeDef def, RimWorld.Quest quest, System.Boolean historical)
METHOD public static System.Void Messages::Message(Verse.Message msg, System.Boolean historical)
```

注意第二参是 **`LookTargets` 不是 `Thing`**（靠 `LookTargets` 的 `op_Implicit(Verse.Thing)` 隐式转换接住）。
最终代码：
`Messages.Message(KeyDepleted.Translate(), new LookTargets(parent), MessageTypeDefOf.NeutralEvent, false);`

### 坑 2 `csc` 的 `-version`

想给产物设版本号 `1.0.0.0`，往 csc 命令行加了 `-version:1.0.0.0`，结果：

```
    5.9.0-1.26423.113 (e34a38d2ae1fc26406a317517196e55c68ff83ab)
[OK]   csc RimTestMod.dll 退出码 0        <-- 退出码 0，但什么产物都没有
```

**`csc -version` 的语义是「打印编译器版本然后退出」，不是「设置程序集版本」。**
（顺带：这条也证伪了它是个「程序集版本开关」。）
修法：脚本生成临时 `AssemblyInfo.<程序集名>.cs` 一起编，里面放 `[assembly: AssemblyVersion("1.0.0.0")]` ——
这正是 SDK 路径 `dotnet build` 自动生成 AssemblyInfo 所做的事。修完两条路径的产物版本都是 1.0.0.0。

### 坑 3 CS1701：`0Harmony` 是针对 .NET 8 引用框架编译的

csc 路径下编补丁程序集时报：

```
warning CS1701: 假定"0Harmony"使用的程序集引用"System.Runtime, Version=8.0.0.0, Culture=neutral,
PublicKeyToken=b03f5f7f11d50a3a"与"System.Runtime"的标识"System.Runtime, Version=10.0.0.0,
Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"匹配，您可能需要提供运行时策略
```

即 **`0Harmony.dll` 3.0 是拿 .NET 8 的引用框架编的，而游戏跑的是 .NET 10**。
这是个**警告不是错误**（编译照样通过），且游戏的 `WaylithClr.LaxAssemblyBinding=true` 正是为这种版本漂移准备的。
SDK 路径没报这条（MSBuild 的引用解析会规范化），**两条路径对同一个源文件给出不同警告数**，这是正常现象。
**未核实**：这条版本漂移在运行时会不会真的出问题（本任务禁止启动游戏，无法验证）。

### 坑 4 PowerShell 函数的输出流会把退出码带坏

脚本里 `Invoke-Csc` 一开始写成：
```powershell
& dotnet exec $cscDll "@$rsp"
return $LASTEXITCODE
```
结果 `$c1` 不是 `0`，而是**一个数组**：`['warning CS2023: ...', 0]` —— 因为原生命令的 stdout 落进了函数的输出流，
PowerShell 会把「所有输出」+「return 的值」拼成数组一起返回。报错信息于是变成
`退出码 warning CS2023: /noconfig 选项是在响应文件中指定的，因此被忽略 0`（**编译其实是成功的，脚本误判**）。
修法：`& dotnet exec $cscDll "@$rsp" 2>&1 | ForEach-Object { Write-Host "    $_" }` 之后再 `return $LASTEXITCODE`。

### 坑 5 其它小坑（一次性记录）

- `-noconfig` 放进响应文件里会被 csc 吐槽 `CS2023: /noconfig 选项是在响应文件中指定的，因此被忽略` —— 已删除。
- `<BaseIntermediateOutputPath>` 手改会触发 `MSB3539` 警告 —— 已删除，改用默认 `obj/`。
- `dotnet build` 默认会在输出目录生成 `.deps.json` —— 加 `<GenerateDependencyFile>false</GenerateDependencyFile>` 压掉，保证 `Assemblies/` 里只有 .dll。
- `<EnableDefaultCompileItems>false</EnableDefaultCompileItems>` + 显式 `<Compile Include>`：避免 SDK 默认 glob 去吃 `obj/` 下的临时文件。
- 写本脚本自身时的一个教训：脚本里**全程不用 PowerShell 反引号转义**（改用字符串拼接和 `[char]10`），
  否则嵌套引号层级太深极易写错。

---

## 5. 补丁目标签名（**从 `Assembly-CSharp.dll` 元数据反射读出的原文，逐字粘贴**）

探针 `docs/_lineB-tools/SigProbe`（自建，net10.0 控制台程序，`System.Reflection` + `AssemblyLoadContext.Default.Resolving`），
调用形式 `SigProbe one GAME <类型全名>`，`GAME` 解析到 `E:\SteamLibrary\steamapps\common\RimWorld\Assembly-CSharp.dll`。
以下是探针输出的**原样**行（默认值也保留）：

```
TYPE public class Verse.Projectile : Verse.ThingWithComps
  METHOD public System.Void Launch(Verse.Thing launcher, Verse.LocalTargetInfo usedTarget, Verse.LocalTargetInfo intendedTarget, Verse.ProjectileHitFlags hitFlags, System.Boolean preventFriendlyFire = False, Verse.Thing equipment)
  METHOD public virtual System.Void Launch(Verse.Thing launcher, UnityEngine.Vector3 origin, Verse.LocalTargetInfo usedTarget, Verse.LocalTargetInfo intendedTarget, Verse.ProjectileHitFlags hitFlags, System.Boolean preventFriendlyFire = False, Verse.Thing equipment, Verse.ThingDef targetCoverDef)
  METHOD protected virtual System.Void Impact(Verse.Thing hitThing, System.Boolean blockedByShield = False)
  METHOD protected virtual System.Void ImpactSomething()
  FIELD  protected System.Int32 ticksToImpact
  PROP   Verse.Thing Launcher { get; }
  PROP   UnityEngine.Vector3 ExactPosition { get; }

TYPE public class Verse.Thing : Verse.Entity
  METHOD public Verse.DamageWorker+DamageResult TakeDamage(Verse.DamageInfo dinfo)
```

补丁实际打的目标（`RimTestMod_PatchBootstrap` 里逐条 `AccessTools.Method` 取，取不到就 `Log.Error` 并继续，不整体失败）：

| 补丁 | 目标方法签名（原文） | 我们挂的 |
|---|---|---|
| `ProjectileLaunchPatch` | `public virtual System.Void Verse.Projectile::Launch(Verse.Thing, UnityEngine.Vector3, Verse.LocalTargetInfo, Verse.LocalTargetInfo, Verse.ProjectileHitFlags, System.Boolean, Verse.Thing, Verse.ThingDef)` | Postfix |
| `ProjectileImpactPatch` | `protected virtual System.Void Verse.Projectile::Impact(Verse.Thing, System.Boolean)` | Postfix |
| `ThingTakeDamagePatch` | `public Verse.DamageWorker+DamageResult Verse.Thing::TakeDamage(Verse.DamageInfo)` | Prefix(+Postfix) |

### Harmony 侧实测的 API（来自 `0Harmony.dll` 3.0，同样是探针输出原文）

```
TYPE public class HarmonyLib.Harmony : System.Object
  CTOR   public .ctor(System.String id)
  METHOD public System.Reflection.MethodInfo Patch(System.Reflection.MethodBase original, HarmonyLib.HarmonyMethod prefix, HarmonyLib.HarmonyMethod postfix, HarmonyLib.HarmonyMethod transpiler, HarmonyLib.HarmonyMethod finalizer)
  METHOD public System.Void PatchAll()  /  PatchAll(System.Reflection.Assembly assembly)
  METHOD public System.Collections.Generic.IEnumerable<System.Reflection.MethodBase> GetPatchedMethods()
TYPE public class HarmonyLib.HarmonyMethod
  FIELD  public MethodInfo method ; public string methodName ; public Type declaringType ; public Type[] argumentTypes
         public int priority ; public string category ; public string[] before ; public string[] after
  CTOR   public .ctor(System.Reflection.MethodInfo method)
         public .ctor(System.Reflection.MethodInfo method, int priority = -1, string[] before, string[] after, System.Nullable<bool> debug)
```

**重要差异（Harmony 2.x → 3.0）**：`HarmonyMethod` **没有 `patchId` 字段**，`Harmony.Patch()` **也没有补丁 ID 参数**。
Harmony 3.0 用 `category` + `SetSwitch/ClearSwitch` 取代了 2.x 的「补丁 ID」概念。

> **规格 §6 要求「补丁 ID 必须唯一」的落地方式**：因为 3.0 没有 ID 机制，我们改用
> ①唯一的 `Harmony` 实例 ID `test.rimtestmod.patches`；②每个补丁类的唯一全名（如 `Demo.RimTestMod.Patches.ProjectileLaunchPatch`）；
> ③每个补丁类里声明 `public const string PatchId`，值就是它自己的全名，供日志/人读排查。
> **我们刻意没有使用 `HarmonyMethod.category`** —— category 和 switch 机制的默认生效语义在**禁止启动游戏**的前提下无法验证，不敢用。

**技术选择**：`RimTestMod_PatchBootstrap` 用 `AccessTools.Method` **逐条手工 Patch**，不用 `PatchAll` ——
`PatchAll` 一个签名对不上就整体抛异常，逐条打则「哪条成功哪条失败」都能 `Log.Message` 出来，且失败的不拖累成功的。
整个 `Run()` 包在 `try/catch` 里 + `[MethodImpl(MethodImplOptions.NoInlining)]` 隔离，
这样即使 `0Harmony.dll` 缺失导致 `HarmonyLib.*` 类型无法解析，也只是这个补丁程序集报错，不会连环炸到主程序集。

---

## 6. XML 侧交接（不属本文件清单，写给 XML 线的同事）

C# 侧已经就绪，XML 侧要按下面这条**精确契约**接线，否则组件不会被实例化：

```xml
<li Class="Demo.RimTestMod.CompProperties_TestShield">
  <shieldCapacity>50</shieldCapacity>
</li>
```

- 类名必须是 `Demo.RimTestMod.CompProperties_TestShield`（`public int shieldCapacity = 50` 是规格 §6 的契约字段名，逐字一致）。
- 组件类 `Demo.RimTestMod.ThingComp_TestShield : Verse.ThingComp` 由属性类的无参构造自动绑定（`compClass = typeof(...)`），XML 里不用再写。
- **⚠️ 需要 XML 线补 4 个 Keyed 本地化键**（C# 里已经写好键名，缺了游戏里会直接显示键名原文）：
  `DM_TestShield_Inspect`（含 `{0}/{1}/{2}` 三个占位）、`DM_TestShield_Depleted`、`DM_TestShield_GizmoRefillLabel`、`DM_TestShield_GizmoRefillDesc`。

### 组件行为（`_SPEC.md` §6 契约的实现口径）

- 吸收伤害：`PostPreApplyDamage(ref DamageInfo dinfo, out bool absorbed)` —— 实测 1.7 签名与 1.6 相同。
  吸收量 = `Ceiling(dinfo.Amount)` 与剩余护盾点取小；**完全吸收**时 `dinfo.SetAmount(0f)` 且 `absorbed = true`；
  **部分吸收**时只把 `dinfo.Amount` 减到剩余值（`Verse.DamageInfo` 是 struct、`Amount` 是**只读属性**，
  唯一改值途径是 `dinfo.SetAmount(float)` —— 1.6 教程里常见的 `dinfo.Amount = x` 在 1.7 编不过）。
- 恢复：`CompTick()` 里每 `rechargeIntervalTicks`（默认 120 tick = 2 秒）回 `rechargeAmount`（默认 5）点，夹在 `shieldCapacity` 上限。
- 存读：`PostExposeData()` 用 `Scribe_Values.Look`，键名带 `DM_` 前缀（`DM_ShieldPoints` 等 5 个）。
  **默认值给 `-1` 而不是「满护盾」**：读档时 `props` 可能还没接上，`ShieldCapacity` 会返回 0，
  拿它当默认值会把老存档的护盾静默清零；`-1` 作为「存档里没这个字段」的哨兵，在 `PostSpawnSetup`/`PostLoadInit` 时补满。
- **零 UnityEngine 依赖**：主程序集里一个 `UnityEngine` 类型都没用（护盾计算只用 `System.Math`），
  这是「主程序集加载面最小」的一部分，也被 §1 的 AssemblyRef 表证实。

---

## 7. 未核实 / 已知风险（如实列出）

1. **补丁在运行时是否真的生效 —— 未核实。** 本任务明令禁止启动游戏，因此只做到「编译通过 + 目标签名元数据核对无误 + 产物依赖面正确」。
2. **Harmony 3.0 与 WaylithCLR 的运行时兼容性 —— 未核实。** 上游验证报告（`docs/验证-csharp-1.7.md`）的判断是
   「Harmony 3.0 内含 MonoMod.Core 原生 detour，理论可用，但两者互不认识，未实测」。
3. **`0Harmony` 的 .NET 8 → 10 版本漂移（CS1701）会不会在运行时出问题 —— 未核实**（见 §4 坑 3）。
4. **`DamageWorker.DamageResult` 是 class 还是 struct —— 未实测**，所以 `ThingTakeDamagePatch` 刻意**不声明 `__result`**，
   避免补丁绑定因类型推断失败。这属于主动规避，不是遗漏。
5. **游戏在 1.7 下的实际启动行为、def 加载结果 —— 未核实**（decided by 其它线的负责人）。

---

## 8. 「模板/文档 vs 1.7 现实」冲突点（本线实测，供汇总）

| # | 1.6 时代的说法（`SKILL.md` / 模板 / 通行教程） | 1.7 本机实测现实 | 证据 |
|---|---|---|---|
| 1 | `TargetFramework` = `.NET Framework 4.7.2+` | **`net10.0`** | `RimWorld.runtimeconfig.json` 的 `"tfm": "net10.0"` |
| 2 | Unity 2022.3.35，引用 `UnityEngine.CoreModule.dll` 等 | **Unity 已换成 `UnityStubs.dll` 兼容层**；游戏根目录 `*UnityEngine*` **零命中** | `Get-ChildItem *UnityEngine*` 无结果；`WaylithClr.AssemblyNameRedirects=UnityEngine*=UnityStubs` |
| 3 | 游戏 DLL 在 `RimWorldWin64_Data\Managed\` | **该目录不存在**；DLL 全在游戏根目录 | `Test-Path RimWorldWin64_Data\Managed` = False |
| 4 | 「`Harmony` 随游戏一起来」/「mod 自带 0Harmony.dll」 | **游戏本体不带**；要从 Harmony mod 的 `1.7\Assemblies\` 取；**自带旧版会触发告警降级** | 游戏根目录 `*Harmony*` 零命中；工坊 mod 2009463077 |
| 5 | `dinfo.Amount = x` 改伤害 | **编不过**：`Amount` 只读，必须 `dinfo.SetAmount(x)` | `Verse.DamageInfo` 元数据：`PROP float Amount { get; }` + `METHOD SetAmount(float)` |
| 6 | `Messages.Message(text, thing, def)` | 第二参是 **`LookTargets`** 不是 `Thing` | `Verse.Messages` 元数据（§4 坑 1） |
| 7 | `RimWorld.Command_Action` | **不存在**；正确类型是 `Verse.Command_Action` | 类型全名探针未命中 `RimWorld.Command_Action` |
| 8 | 「`RimWorld.` 前缀的类型在 `RimWorld.dll`」 | **不一定**，`RimWorld.MessageTypeDefOf` 在 `Assembly-CSharp.dll` 里 | 探针 `one GAME RimWorld.MessageTypeDefOf` 命中（§4 坑 1） |
| 9 | Harmony 2.x 的「补丁 ID」 | Harmony **3.0**：`HarmonyMethod` 无 `patchId`，`Patch()` 无 ID 参数，改用 `category`+switch | `HarmonyLib.HarmonyMethod` 字段列表（§5） |
| 10 | `-version:1.0.0.0` 之类的 csc 版本开关 | **`csc -version` 是「打印版本并退出」**，会导致「exit 0 但零产物」 | 实测输出（§4 坑 2） |

---

## 9. 文件清单（本线交付）

| 文件 | 说明 |
|---|---|
| `Source/ThingComp_TestShield.cs` | 护盾组件（10.6 KB，零 UnityEngine 依赖） |
| `Source/CompProperties_TestShield.cs` | 组件属性 + `ConfigErrors` 校验（2.7 KB） |
| `Source/Patches/PatchCommon.cs` | `IsDmDef`（只对 `DM_` 前缀的 def 记日志，防刷屏）、`Describe(MethodBase)` |
| `Source/Patches/ProjectileLaunchPatch.cs` | 打 8 参 `Launch` 重载（含 `UnityEngine.Vector3`，证明 UnityStubs 引用路径可用） |
| `Source/Patches/ProjectileImpactPatch.cs` | 打 `protected virtual Impact`（证明 `AccessTools` 能取到 protected） |
| `Source/Patches/ThingTakeDamagePatch.cs` | 打 `Thing.TakeDamage`，跨程序集读主程序集的护盾组件 |
| `Source/Patches/RimTestMod_PatchBootstrap.cs` | `[StaticConstructorOnStartup]` 引导类，逐条补丁 + 全量日志 + 优雅降级 |
| `Source/build.ps1` | 可复现编译脚本（双路径，6 段校验，失败 exit 1） |
| `Source/README.md` | 本文 |
| `Assemblies/RimTestMod.dll` (11,776 B) / `Assemblies/RimTestMod.Patches.dll` (12,800 B) | 真实编译产物 |

**源文件头都带 `// AI 辅助生成` 标注**（`SKILL.md` 的 AI 标注要求）。
