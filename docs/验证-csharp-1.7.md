# RimWorld 1.7 下 C# mod 与 Harmony 补丁可行性验证报告

- 验证对象：RimWorld 1.7.4981 rev136（E:\SteamLibrary\steamapps\common\RimWorld\Version.txt 内容为 `1.7.4981 rev136`）
- 创意工坊 mod 目录：E:\SteamLibrary\steamapps\workshop\content\294100（136 个 mod）
- 验证方式：**纯静态分析**（PE/CLI 元数据解析 + IL 反编译式读取 + 原生字符串搜索），**未启动 RimWorld 本体**（任务硬性要求）
- 结论标注约定：凡没有直接证据的推断一律以「推测：」开头；有证据的行给出「文件路径 + 实际命令 + 真实输出」
- 本报告只写入本文件，工作区其它文件未被修改

---

## 一、结论摘要

| 问题 | 结论 | 关键证据强度 |
| --- | --- | --- |
| 1. 1.7 还能用 Harmony 吗 | **能。** 游戏本体不再内置 Harmony（根目录 `*Harmony*` 递归 0 命中），但 Harmony mod（2009463077）提供 1.7 专用 `1.7\Assemblies\0Harmony.dll`（程序集 3.0.0.0，net10.0，自带 MonoMod.Core 原生 detour 引擎）。游戏本体甚至主动反射读取 Harmony 补丁信息用于内置 Profiler 界面 | 强（配置 + IL + 交叉引用） |
| 2. UnityStubs.dll 是什么 | **UnityEngine 的真兼容层（不是空的占位桩）。** 935 个类型 / 7471 个方法定义，全库只有 1 个类型含 P/Invoke、0 个类型含 InternalCall；几乎所有类型都是真托管实现（转发到 Waylith 引擎）。**只有 257 个方法**在「未实现」时调用 `UnityStubs.Internal.StubWarner::LogStub`——即**记一条警告并返回默认值/空操作，而不是抛异常** | 极强（全库扫描统计 + 逐条 IL） |
| 3. 是否有可用的 1.7 C# mod 范本 | **有 20 个。** 136 个 mod 中 22 个含 `1.7` 目录，其中 20 个在 1.7 下带 DLL；主流做法是 `1.7\Assemblies\*.dll` + `TargetFramework=net10.0` + 引用 `Assembly-CSharp 1.7.xxxx` 与 `UnityStubs 1.0.0.0` | 强（文件清单 + 元数据表） |
| 4. modder 入口类型是否还在 | **全部仍在：** `Verse.Mod`、`Verse.ModContentPack`、`Verse.ModAssemblyHandler`、`Verse.ModSettings`、`RimWorld.DefOf`、`Verse.DefModExtension`、`Verse.ThingComp`/`Verse.CompProperties`、`Verse.HediffComp`。`HarmonyLib` 在 Assembly-CSharp 里 **0 个类型**（它本来就住在 mod 的 0Harmony.dll 里，游戏只在 Profiler 里按字符串反射用它） | 强（类型清单 + IL） |
| 5. 1.7 写 C# mod | **最小可行做法**：`1.7\Assemblies\YourMod.dll`（net10.0，引用 Assembly-CSharp.dll + UnityStubs.dll + 0Harmony.dll）+ `About\About.xml`（supportedVersions 含 1.7）+ `LoadFolders.xml` 的 `<v1.7>` 或直接依赖版本目录自动探测 | 强 |

补充结论（全部有下文证据）：

1. **1.7 的运行时是自研栈**：`WaylithClr`（自研 CoreCLR 分支，`Microsoft.NETCore.App 10.0.13-waylithclr.dev`）+ Waylith 引擎 + Brutal.* 原生绑定。根目录**没有任何 UnityEngine*.dll**，UnityEngine 的 API 面由 `UnityStubs.dll` 提供，并通过 `WaylithClr.AssemblyNameRedirects` 把 `UnityEngine*=` 与 `Assembly-CSharp-firstpass=` 重定向到 UnityStubs。
2. **mod 程序集加载机制与 1.6 相同**：`Verse.ModAssemblyHandler::ReloadAll` 仍然对 mod 的 `Assemblies/` 目录逐个 `System.Reflection.Assembly::LoadFrom`，随后 `AssemblyIsUsable` 调 `assembly.GetTypes()`；**任何类型解析失败都会让这个 DLL 被整体拒绝**并打印 `"Loader exceptions:"`。
3. **版本目录解析有两套路径**：有 `LoadFolders.xml` 时按 `<v1.7>` 节点（支持 `IfModActive` / `IfModActiveAll` / `IfModNotActive` 属性）；**没有 `LoadFolders.xml` 时游戏仍会自动加载与当前版本同名的目录**（`Path.Combine(RootDir, CurrentVersionStringWithoutBuild)`，实测 `CurrentVersionStringWithoutBuild == "1.7"`），并追加 `Common` 目录与 mod 根目录。
4. **Harmony 3.0 与 Waylith 互不认识**：0Harmony.dll 的 29 个程序集引用**全部是 System.***，没有 UnityEngine / Assembly-CSharp / Waylith**；其补丁手段是 MonoMod.Core 的**原生 detour**（VirtualProtect/FlushInstructionCache 改写方法入口机器码，含 Iced.Intel x86 编解码器与 Mono.Cecil）。WaylithClr 侧则提供 `JitPatchableAssemblies="Assembly-CSharp"` 的方法级 patchpoint 白名单。
5. **Harmony 是否真能打上补丁，本任务无法实测**（禁止启动游戏）——见「四、无法确认的未知项」，存在两个已知风险点（MonoMod 的 JIT 版本探测、内联/JIT 优化）。

---

## 二、逐项证据

### 2.0 环境复核（先坐实用户给的既有事实）

命令：

    $g = "E:\SteamLibrary\steamapps\common\RimWorld"
    Get-Content -LiteralPath "$g\Version.txt"
    Get-ChildItem -LiteralPath $g -Recurse -File -Filter "*Harmony*"
    Get-ChildItem -LiteralPath $g -Recurse -File -Filter "UnityEngine*.dll"
    Get-ChildItem -LiteralPath $g -Recurse -File -Filter "clrjit*.dll"
    Get-ChildItem -LiteralPath $g -Recurse -File -Filter "*Waylith*"

真实输出（摘要）：

    Version.txt -> 1.7.4981 rev136
    *Harmony*       -> 0 hits
    UnityEngine*.dll -> 0 hits
    clrjit*.dll     -> 1 hits : clrjit.dll
    *Waylith*       -> 5 hits : Waylith.AssetBake.dll / Waylith.dll / Waylith.UnityCompat.dll / Waylith.VideoDecode.dll / waylithaudio.dll

游戏根目录关键文件（`Get-ChildItem -File`，仅列相关项，字节数）：

    Assembly-CSharp.dll 15632384     RimWorld.dll 284672          RimWorld.exe 198656
    UnityStubs.dll 961536            Waylith.dll 1538048          Waylith.UnityCompat.dll 51712
    Waylith.AssetBake.dll 72192      Waylith.VideoDecode.dll 217088
    coreclr.dll 9719808              clrjit.dll 3393536           System.Private.CoreLib.dll 16089088
    hostfxr.dll 740352               hostpolicy.dll 732672        netstandard.dll 90624   mscorlib.dll 49152
    Brutal.Vulkan.dll 1433088        Brutal.ImGui.dll 476672      Brutal.Core.*  (Collections/Common/Logging/Maths/Memory/Numerics/Package/Strings)
    com.rlabrecque.steamworks.net.dll 417280                     AssetsTools.NET.dll 196096
    RimWorld.runtimeconfig.json 1519  RimWorld.deps.json 75282    ModUpdating.txt 17464
    Data\ (Core / Royalty / Ideology / Biotech / Anomaly / Odyssey)   Mods\ (空，0 项)

程序集元数据（命令 `asmrefs.ps1 <dll>`，读 AssemblyDefinition + AssemblyRefs + TargetFrameworkAttribute）：

    DLL: E:\SteamLibrary\steamapps\common\RimWorld\Assembly-CSharp.dll
         name=Assembly-CSharp asmver=1.7.9786.4087
         refs(31): System.Runtime 10.0.0.0; UnityStubs 1.0.0.0; System.Collections 10.0.0.0; System.Threading 10.0.0.0;
                   System.Linq 10.0.0.0; System.Text.RegularExpressions 10.0.0.0; com.rlabrecque.steamworks.net 0.0.0.0;
                   Waylith 1.0.0.0; System.Xml.ReaderWriter 10.0.0.0; System.Linq.Expressions 10.0.0.0;
                   System.Collections.Concurrent 10.0.0.0; Brutal.Core.Logging 2026.9.0.0; System.Threading.Thread 10.0.0.0;
                   ... Waylith.AssetBake 1.0.0.0; ISharpZipLib 1.0.0.0; Brutal.Vulkan 2026.9.0.0; System.Console 10.0.0.0
         TargetFramework: .NETCoreApp,Version=v10.0

> 这说明：**游戏代码本身现在直接依赖 UnityStubs（Unity API 面）、Waylith（引擎）、Brutal.\*（原生绑定）**，而不是 UnityEngine.*。

`RimWorld.runtimeconfig.json` 全文（`Get-Content -Raw`）：

    {"runtimeOptions":{"tfm":"net10.0","includedFrameworks":[{"name":"Microsoft.NETCore.App","version":"10.0.13-waylithclr.dev"}],
    "configProperties":{
     "WaylithClr.AssemblyNameRedirects":"UnityEngine*=UnityStubs;Unity.Newtonsoft.Json=;Unity.*=UnityStubs;Assembly-CSharp-firstpass=UnityStubs",
     "WaylithClr.LaxAssemblyBinding":true,"WaylithClr.SkipAccessChecks":true,"WaylithClr.LaxDynamicMethodAttributes":true,
     "WaylithClr.AllowInitOnlyStaticWrites":true,"WaylithClr.LaxCallvirt":true,"WaylithClr.LaxAssemblyArchitecture":true,
     "WaylithClr.LaxTypeRefResolution":true,"WaylithClr.LaxMemberSignatures":true,"WaylithClr.DynamicMethodOwnerIsDeclaringType":true,
     "WaylithClr.CatchableAccessViolations":true,"WaylithClr.JitNoInlinePatchableIntoDynamicMethods":true,
     "WaylithClr.JitPatchableAssemblies":"Assembly-CSharp","WaylithClr.LaxInterfaceDispatch":true,
     "WaylithClr.IsolatedLoadsResolveByName":true,"WaylithClr.LaxPrivateFieldNames":true,"WaylithClr.MonoStringHashCode":true,
     "WaylithClr.MonoFloatFormatPrecision":true,"WaylithClr.LaxInheritedFieldRefs":true,"WaylithClr.MissingAssemblyTypeLoadException":true,
     "System.Reflection.Metadata.MetadataUpdater.IsSupported":false,
     "System.Runtime.Serialization.EnableUnsafeBinaryFormatterSerialization":true}}}

**要点**：`AssemblyNameRedirects` 把三个名字前缀重定向到 `UnityStubs`（`Unity.Newtonsoft.Json=` 是空目标 = 直接移除该引用）；`JitPatchableAssemblies` 只列了 `Assembly-CSharp`（**mod 自己的程序集不在白名单里**）。

  真实字符串证据（从 `coreclr.dll` 原生搜索，命令 `[IlAsm]::RawAsciiSearch/RawUtf16Search`）：

    ASCII 符号  : ?JitPatchableAssemblies@EEConfig@@QEBAPEB_WXZ
                  ?JitNoInlinePatchableIntoDynamicMethods@EEConfig@@QEBA_NXZ
    UTF-16 串   : WaylithClr.JitPatchableAssemblies        (@0x558C3E)
                  WaylithClr.JitNoInlinePatchableIntoDynamicMethods (@0x558CEC)
    ASCII 串    : Jit_Patchpoint: patchpoint (0x%p) TRANSITION unexpected context IP 0x%p
                  PatchpointOptimizationPolicy: patchpoint (0x%p) OSR method creation failed, ...
                  JitPatchpointWorker: failed to restore patchpoint info for Method=0x%pM
                  JIT_Patchpoint / JIT_PatchpointForced / GetPatchpointInfo@CEEJitInfo / PerPatchpointInfo

且：`coreclr.dll` 中 `"Detour"`/`"Harmony"`/`"MonoMod"` 三个串 **0 命中**；`Waylith.dll` 中 `"Patchable"`/`"Detour"`/`"RuntimePatch"` 均 0 命中。
→ **WaylithClr 内置的是通用「方法级 patchpoint / 可重定向入口 + 可打补丁程序集白名单」，不是 Harmony 专用支持。**

---

### 2.1 问题 1：Harmony 在 1.7 如何工作

#### (1) mod 2009463077 的 1.7 子目录文件清单

命令：`Get-ChildItem -LiteralPath "E:\SteamLibrary\steamapps\workshop\content\294100\2009463077" -Recurse -File`

    LICENSE 1073 | LoadFolders.xml 335 | README.md 1145
    About\About.xml 445 | About\Manifest.xml 480 | About\ModIcon.png 5605 | About\Preview.png 100538 | About\PublishedFileId.txt 10
    1.4\Assemblies\{0Harmony.dll 931840, HarmonyMod.dll 5120}
    1.5\Assemblies\{0Harmony.dll 2195456, HarmonyMod.dll 12288}
    1.6\Assemblies\{0Harmony.dll 2485248, HarmonyMod.dll 17920}
    1.7\Assemblies\{0Harmony.dll 2532864, HarmonyMod.dll 15872}      <-- 1.7 下就这两个文件

`About\About.xml`：`name=Harmony, author=Andreas Pardeike, packageId=brrainz.harmony, modVersion=3.0.1.0`，supportedVersions 为 `1.2,1.3,1.4,1.5,1.6,1.7`。
`LoadFolders.xml`（原文）：

    <loadFolders>
      <v1.5><li>/</li><li>1.5</li></v1.5>
      <v1.6><li>/</li><li>1.6</li></v1.6>
      <v1.7><li>/</li><li>1.7</li></v1.7>
    </loadFolders>

#### (2) 版本号（命令：`[System.Reflection.AssemblyName]::GetAssemblyName(path)` 与 `$fi.VersionInfo`）

| 文件 | AssemblyVersion | ProductVersion | 大小 |
| --- | --- | --- | --- |
| …\2009463077\1.7\Assemblies\0Harmony.dll | **3.0.0.0** | 3.0.0.0-rc.3+3c0e32cd3fd20e4ae27c47cb8c888844766f9f1a | 2532864 |
| …\2009463077\1.7\Assemblies\HarmonyMod.dll | **3.0.1.0** | 3.0.1.0 | 15872 |
| …\2009463077\1.6\Assemblies\0Harmony.dll | 2.4.3.0 | 2.4.3.0+b79f2f1a… | 2485248 |
| …\RimWorld\Assembly-CSharp.dll | 1.7.9786.4087 | 1.7.9786.4087+81e14e7a… | 15632384 |

  `1.7\Assemblies\0Harmony.dll` 的 TargetFramework 为 **.NETCoreApp,Version=v10.0**，29 个引用全部是 `System.** 10.0.0.0`（少量 8.0.0.0 与 `netstandard 2.0.0.0`）。

#### (3) HarmonyMod.dll 的作用（IL 实证）

类型清单（`[IlDump]::TypeNames + Summarize`）：

    <Module>, HarmonyMod.ExceptionTools, HarmonyMod.LogLocation, HarmonyMod.Main,
    HarmonyMod.VersionControl_DrawInfoInCorner_Patch, HarmonyMod.StackTrace_ToString_Patch,
    HarmonyMod.Log_ResetMessageCount_Patch, HarmonyMod.Settings（: Verse.ModSettings）, 若干编译器生成类

- `HarmonyMod.Main::.ctor(Verse.ModContentPack)` 的 IL 里 `call Verse.Mod::.ctor(Verse.ModContentPack)` → **HarmonyMod 就是一个标准 `Verse.Mod` 子类**（游戏 Mod 体系内的一员）。
- **`HarmonyMod.Main::.cctor()`（il=581，ops=196）是关键**，其中字符串与调用：

      ldstr "0Harmony" / "Lib.Harmony" / "HarmonyLib" / "0Harmony.dll"
      ldstr "Could not read version of our 0Harmony.dll from disk: "
      ldstr "HARMONY LOADING PROBLEM\n\nAnother Harmony library was loaded before the Harmony mod could.\n"
      ldstr "Their version: " / "\nOur version: "
      ldstr "This means that your Harmony version is now downgraded to "
      ldstr " regardless of what the Harmony mod provides. "
      ldstr "You need to update or remove that other loader/mod. The other Harmony was loaded from: "
      ldstr "data-[0-9A-F]{16}"      (正则，用于从加载路径里剥掉动态程序集后缀)
      ldstr "…loaded from memory and not via a file path. This often hints to preloaders like Doorstop or similar."
      ldstr "net.pardeike.rimworld.lib.harmony"
      ldstr "Lib.Harmony could not be initialized: "
      calls: Assembly::GetExecutingAssembly → AppDomain::get_CurrentDomain → AppDomain::GetAssemblies()
             → LINQ Single(...) 找名为 "0Harmony"/"Lib.Harmony" 的程序集 → 比较版本（Version::op_GreaterThan）
             → new HarmonyLib.Harmony::.ctor(String)  (id = "net.pardeike.rimworld.lib.harmony")
             → HarmonyLib.Harmony::PatchAll(System.Reflection.Assembly)
             → Verse.Log::Message / Warning / Error

  → **HarmonyMod 的职责就是：加载/校验 0Harmony 库 + 对 HarmonyMod.dll 自己执行 `Harmony.PatchAll` + 提供 UI 与设置。**
- `HarmonyMod.LogLocation::Initialize()`（il=141）里出现 `"HARMONY_LOG_FILE"`、`"HARMONY_NO_LOG"`、`"Logs"`、`"harmony.log.txt"`，并调用 **`Waylith.Runtime.WaylithRuntime::get_Current` → `WaylithRuntime::get_App` → `WaylithAppState::get_LogDataPath`** → `Path::Combine` → `Directory::CreateDirectory` → `Environment::SetEnvironmentVariable`。**即 Harmony 自己也在用 Waylith 的运行时 API 拿日志目录。**
- `HarmonyMod.VersionControl_DrawInfoInCorner_Patch::Postfix()`（il=180）使用 `Verse.Text::set_Font(Verse.GameFont)`、**`UnityEngine.Color::get_white()`**、`Verse.ColorExtension::ToTransparent`、**`UnityEngine.GUI::set_color`**、`Verse.Text::CalcSize`、**`UnityEngine.Rect::.ctor`**、`Verse.Widgets::Label`、**`Verse.Mouse::IsOver`**、`Verse.TooltipHandler::TipRegion`、`Verse.Find::get_WindowStack`、`new Verse.Dialog_MessageBox`、`Verse.WindowStack::Add` —— **这些 UnityEngine.* 类型全部来自 UnityStubs**（见 2.2），说明 Harmony 的 UI 补丁在 1.7 的兼容层上照常写。
- `HarmonyMod.StackTrace_ToString_Patch::TargetMethod()` 使用 `HarmonyLib.AccessTools::GetDeclaredMethods(System.Type)`，Postfix 调 `HarmonyMod.ExceptionTools::EnhanceStackTrace`，内部再用 `Harmony::GetOriginalMethodFromStackframe`、`Harmony::GetPatchInfo`、`PatchProcessor::GetSortedPatchMethods`、`Patch::GetMethod`。

#### (4) 能否对 Assembly-CSharp 打补丁 —— 判定与依据

依据 A（配置层面）：`WaylithClr.JitPatchableAssemblies = "Assembly-CSharp"` —— 游戏把 **Assembly-CSharp 显式列为「可以打补丁」的程序集**（`coreclr.dll` 里 `EEConfig::JitPatchableAssemblies` 有对应访问器与 `JIT_Patchpoint*` 机制）。mod 自己的 DLL 不在白名单里，因此**从白名单角度，最容易/最被支持的目标恰恰是 Assembly-CSharp**。

依据 B（游戏本体主动消费 Harmony）：Assembly-CSharp 中唯一引用 `HarmonyLib.Harmony` 字符串的方法是
**`Verse.ProfilerUI.Dialog_ProfilerAssemblies::HarmonyPatchLines`（il=550）**，其 IL 序列：

    ldstr "HarmonyLib.Harmony" → Verse.GenTypes::GetTypeInAnyAssembly
      → Type::GetMethod("GetAllPatchedMethods", 24) / Type::GetMethod("GetPatchInfo", 24)   (24 = BindingFlags)
      → GetAllPatchedMethods() → castclass MethodBase → GetPatchInfo(method)
      → 取成员名 "Prefixes" / "Postfixes" / "Finalizers" → 每项取 "PatchMethod" (MethodInfo)
      → patch.DeclaringType.FullName，拼成 "Assembly-CSharp!Verse.X::Y" 形式
      → catch: Verse.Log::Warning("Could not list harmony patches for the profiler: " + ex.Message)

即 **1.7 的游戏本体主动按字符串反射调用 Harmony 的 API 来展示补丁列表**——Harmony 是被官方预期存在的。

依据 C（同一 Profiler 把 Harmony 排除在插桩之外）：`Verse.ProfilerUI.ProfilerPrefs::Load`（il=124）里 `ldstr "0Harmony" / "MonoMod.*" / "Mono.Cecil*"`，经 `ProfilerPrefs::get_FilePath`（`"Profiler.xml"`）→ `Verse.DirectXmlLoader::ItemFromXmlFile` → `ProfilerPrefsData::instrumentationTargets` / `ProfilerPrefs::DefaultTargets` → **`Waylith.Profiling.Instrumentation.ProfilerInstrumentation::set_ExcludedAssemblies`**。同一条大字符串里还有 `"Assembly-CSharp!Verse.*::*"`、`"Assembly-CSharp!RimWorld.*::*"`（插桩过滤器语法）。→ 官方明确把 0Harmony/MonoMod/Mono.Cecil 从帧插桩里排除，避免与 Harmony 的代码改写互相干扰。

依据 D（Harmony 的实现路线）：`0Harmony.dll`（1.7）

    - 引用：全部 System.* 10.0.0.0（29 个）——**无 UnityEngine / Assembly-CSharp / Waylith 引用**
    - 类型统计：含 "MonoMod" 582 个类型、"Detour" 23 个、"HarmonyLib.Harmony" 44、"AccessTools" 33；"Waylith"、"Patchpoint" 均 **0**
    - 命名空间规模：Mono.Cecil 198 / HarmonyLib 118 / Mono.Cecil.Cil 68 / Iced.Intel.DecoderInternal 310 /
      Iced.Intel 58（x86 机器码编解码）/ MonoMod.Utils 42 / MonoMod.Core.Platforms 27 / MonoMod.Core 9 /
      Microsoft.Cci.Pdb 215 / Mono.CompilerServices.SymbolWriter 22
    - 关键 UTF-16 串："VirtualQuery failed: "、"ProtectRW"/"ProtectRWX"、"FlushInstructionCache"、
      "Creating simple detour 0x{} => 0x{}"、"Applying native detour from {} to {}"、
      "Cannot create alternate entry point for native detour"、
      "Could not disable inlining of method {}; detours may not be reliable"、
      "This means that the method has been detoured twice. Detour cleanup will fail."、
      "JIT version does not match expected JIT version! expected: {}, got: {}"、
      "guid == ExpectedJitVersion"、"Error while setting up the ICorJitInfo wrapper: "、
      "Provided value for MonoMod.JitPath switch '{}' does not look like a ClrJIT path"、"clrjit"、"coreclr"

**判定：Harmony 3.0（随 mod 提供）在 1.7 下是「自带 MonoMod.Core 原生 detour 的独立补丁引擎」，它对 Assembly-CSharp 打补丁在机制上是可行的（游戏把 Assembly-CSharp 列为可打补丁程序集，且游戏本体就消费 Harmony 的补丁表）。**
**但「补丁是否真的生效」无法在本任务内实测**（禁止启动游戏）：MonoMod.Core 有一条依赖 CoreCLR 内部 JIT 版本/guid 的探测路径（`"JIT version does not match expected JIT version!"`），而 WaylithClr 是自研 CLR（版本串 `10.0.13-waylithclr.dev`），该路径可能失配；**推测：**其 native detour 主路径不依赖该探测，因此常规 Prefix/Postfix 补丁大概率可用，但需要一次实际运行验证（见第四节）。

---

### 2.2 问题 2：UnityStubs.dll 是什么

文件：`E:\SteamLibrary\steamapps\common\RimWorld\UnityStubs.dll`（961536 字节）

#### (1) 规模与性质

    TargetFramework : .NETCoreApp,Version=v10.0
    类型定义        : 935 个
    MethodDef       : 7471 个
    AssemblyRefs    : 33 个（Waylith.UnityCompat 1.0.0.0 / Waylith 1.0.0.0 / Waylith.AssetBake /
                      Waylith.VideoDecode / System.Numerics.Vectors / AssetsTools.NET / AssetsTools.NET.Texture /
                      Brutal.Core.Logging 2026.9.0.0 / Brutal.Vulkan / Brutal.Glfw / Brutal.Core.Numerics /
                      Fmod5Sharp 3.1.0.0 / Microsoft.Extensions.Logging.Abstractions / System.Net.Http 等）

命名空间规模（`[IlAsm]::NamespaceStats`）：

    UnityEngine 286 | UnityEngine.Rendering 32 | UnityEngine.InputSystem 21 | UnityEngine.UI 17 | UnityEngine.Bindings 16
    UnityEngine.Networking 14 | UnityEngine.Events 10 | UnityEngine.Pool 10 | InputSystem.LowLevel 9 | PlayerLoop 7
    InputSystem.Controls 7 | UnityEngine.Video 6 | EventSystems 5 | TextCore 4 | TextCore.LowLevel 4 | Unity.Jobs 4
    Experimental.Rendering 4 | Scripting 4 | SceneManagement 3 | Internal 3 | Audio 3 | Assertions 3 | Profiling 2 …
    另有自制命名空间：UnityStubs.Gui（IGuiBackend/GuiBackend/ITextMeshProBackend/TextMeshProBackend/GuiVertex/TmpFontMetrics）、
    UnityStubs.Rendering（ICameraTextureRenderer/CameraTextureRenderer/CameraViewFactory/IScreenCaptureBackend/ScreenCaptureBackend）、
    UnityStubs.Internal.*（AssetBundleReader/AssetRegistry/FontFaceReader/LineRendererDriver/MeshRaycastBvh/MeshRendererDriver/
    ParticleSystemDriver/ShaderArrays/SmolV/SpirvModule/StubWarner/TextureST/WebTransfer…）、UnityStubs.ContentPacks / ModAssetPacks

**是真实现还是占位？——全库统计结论：**

- 对 935 个类型逐个统计 `internalcall` / `pinvoke`：**只有 1 个类型含 P/Invoke（`UnityEngine.ImageConversion`，1 个），0 个类型含 InternalCall**，其余全是纯托管 IL。
- 对全库扫描 `UnityStubs.Internal.StubWarner::LogStub` 的调用（`[IlStub]::Scan`）：**命中 257 个方法，涉及 88 个类型**。
- StubWarner 的语义（由 `UnityEngine.Time::set_timeScale` 的 IL 直接可见）：

      ldstr "timeScale"
      ldstr "D:\Workspaces\rimworld-builds\RimWorldWaylith\UnityStubs\Time.cs"
      ldc.i4.s 36
      call UnityStubs.Internal.StubWarner::LogStub
      ret

  → **「没实现」的 API 不是 throw，而是调用 `LogStub(API名, 源码文件, 行号)` 记一条警告后返回默认值/空操作。**（源码路径顺带暴露了官方开发树 `D:\Workspaces\rimworld-builds\RimWorldWaylith\UnityStubs\`。）

#### (2) 用户点名类型的确认（方法数 / IL 字节 / 是否 stub）

命令：`[IlClass]::Classify($g\UnityStubs.dll, $w, "", "", 0)` + 对 stubwarner.txt 按类型计票。

| 类型 | 方法数 | IL 字节 | 调用 Waylith | Stub 数 | 判定 |
| --- | --- | --- | --- | --- | --- |
| UnityEngine.Vector3 | 57 | 3037 | 0 | **0** | 纯值类型真实现 |
| UnityEngine.Vector2 | 54 | 1617 | 0 | **0** | 真实现 |
| UnityEngine.Vector4 | 40 | 1120 | 0 | **0** | 真实现 |
| UnityEngine.Vector2Int | 22 | — | 0 | **0** | 真实现 |
| UnityEngine.Color | 46 | 1602 | 7 | **0** | 真实现 |
| UnityEngine.Color32 | 12 | 560 | 5 | **0** | 真实现 |
| UnityEngine.Rect | 47 | 1668 | 0 | **0** | 真实现 |
| UnityEngine.RectOffset | 17 | 389 | 0 | **0** | 真实现 |
| UnityEngine.Mathf | 65 | 1655 | 0 | **0** | 真实现 |
| UnityEngine.Texture2D | 91 | 6423 | 116 | 2 | 真实现（仅 2 处边缘 stub） |
| UnityEngine.Material | 146 | 6153 | 114 | **1**（SetTexture） | 真实现 |
| UnityEngine.Shader | 77 | 2000 | 36 | 4 | 真实现 |
| UnityEngine.Time | 16 | 339 | 21 | **1**（set_timeScale） | 真实现（timeScale 只读） |
| UnityEngine.Input | 39 | 3261 | 0 | **2**（GetAxis、GetTouch） | 其余 37 个方法非 stub |
| UnityEngine.Transform | 61 | 1513 | 23 | **0** | 真实现 |
| UnityEngine.GameObject | 35 | 3237 | 59 | **0** | 真实现 |
| UnityEngine.MonoBehaviour | 5 | 54 | 0 | **0** | 真实现（协程走 `UnityEngine.CoroutineScheduler`） |
| UnityEngine.GUI | 158 | 14557 | 6 | **0** | 真实现 |
| UnityEngine.GUIStyle | 82 | 4395 | 0 | **0** | 真实现 |
| UnityEngine.GUIContent / GUISkin | 17 / 44 | 476 / 2097 | 0 / 18 | 0 / 0 | 真实现 |
| UnityEngine.Screen | 16 | 629 | 35 | **0** | 真实现（全部转发 Waylith.EngineWindow） |
| UnityEngine.Application | 39 | 1566 | 67 | **0** | 真实现 |
| UnityEngine.SystemInfo | 28 | 533 | 4 | **0** | 真实现 |
| UnityEngine.Resources | 22 | 1590 | 28 | **1**（GetBuiltinResource） | 真实现 |
| UnityEngine.Font | 28 | 1700 | 3 | 0 | 真实现 |
| UnityEngine.Debug | 25 | 630 | 0 | **0** | 真实现 |
| UnityEngine.Event | 38 | 631 | 0 | 0 | 真实现 |
| UnityEngine.KeyCode | 0（枚举） | 0 | 0 | 0 | 真实现 |
| UnityEngine.LayerMask / Physics / Random | 14 / 12 / 18 | 443 / 335 / 508 | 0 | 0 | 真实现 |
| UnityEngine.Mesh | 178 | 12116 | 232 | **2**（Optimize、SetIndices） | 真实现 |
| UnityEngine.Camera | 92 | 3669 | 1 | 6（立体/CommandBuffer 类） | 真实现 |
| UnityEngine.Sprite / TextAsset | 26 / 6 | 428 / 273 | 0 / 1 | 0 / 0 | 真实现 |
| UnityEngine.AudioClip / AudioSource | 22 / 67 | 1538 / 3023 | 27 / 50 | 2 / 2 | 真实现（音频后端 Fmod5Sharp/MiniAudio） |
| UnityEngine.Coroutine | 1 | 7 | 0 | 0 | 真实现（句柄） |
| UnityEngine.ScriptableObject | 4 | 109 | 0 | 0 | 真实现 |
| UnityEngine.Quaternion / Matrix4x4 / Bounds / Ray | 31 / 42 / 27 / 8 | 2088 / 3684 / 1021 / 136 | 0 | 0 | 真实现 |
| UnityEngine.Graphics | 101 | 6500 | 73 | 3（DrawTexture/ExecuteCommandBuffer×2） | 真实现 |
| UnityEngine.RenderTexture | 60 | 2181 | 27 | 3 | 真实现 |
| UnityEngine.Texture | 40 | 842 | 25 | 0 | 真实现 |
| UnityEngine.MaterialPropertyBlock | 69 | 3386 | 16 | 0 | 真实现 |
| UnityEngine.JsonUtility | 4 | — | — | 0 | 真实现 |

**典型 IL 佐证（真实现，不是占位）：**

`UnityEngine.Time`（`[IlDump2]::Dump($g\UnityStubs.dll, $w, "UnityEngine.Time", $true, "")`）：

    get_deltaTime: call Waylith.UnityCompat.UnityRuntime::get_Current / dup / brtrue.s / pop / ldc.r4 0 / ret
                   ... call UnityRuntime::get_Time / callvirt UnityTimeState::get_DeltaTime
                   / call UnityEngine.Time::get_maximumDeltaTime / call System.Math::Min / ret
    get_time / get_realtimeSinceStartup / get_unscaledDeltaTime / get_unscaledTime: 转发到 UnityTimeState::*
    get_smoothDeltaTime: 纯托管（按帧做 0.2 系数平滑）
    get_timeScale:  ldc.r4 1; ret        <-- 硬编码常量 1
    set_timeScale:  LogStub("timeScale", "...\UnityStubs\Time.cs", 36)

`UnityEngine.MonoBehaviour`：

    set_useGUILayout: ret（空）
    StartCoroutine(IEnumerator) → UnityEngine.CoroutineScheduler::Start(IEnumerator) → newobj Coroutine
    StopCoroutine / StopAllCoroutines → CoroutineScheduler::Stop / StopAll
    .ctor → UnityEngine.Behaviour::.ctor

`UnityEngine.Screen`：`get_width` → `Waylith.UnityCompat.UnityRuntime::get_Screen::get_Width`（无运行时则回退 1280/720、dpi 96）；
`get_fullScreen` → `Waylith.EngineWindow::get_FullScreen`；`SetResolution` → `Waylith.EngineWindow::SetResolution`；`get_resolutions` 遍历 `Waylith.EngineWindow::get_AvailableResolutions`。

`UnityEngine.Texture2D`：`LoadImage(byte[])` → `LoadEncodedImage`；`SetPixelData` 走 `Waylith.Rendering.TexturePixelData::{get_MipCount,get_Format,EnsureWritableMipLevel,get_Levels}`（仅在需要解码的 mip 路径才 LogStub）。

#### (3) 257 个 stub 的分布（`stubwarner.txt`，共 258 行，末行 `TOTAL_MATCHING_METHODS: 257`）

    UnityEngine.Rendering.CommandBuffer 30 | UnityEngine.InputSystem.InputActionAsset 13 | UnityEngine.ComputeShader 12
    UnityEngine.CullingGroup 12 | UnityEditor.UnityStats 8 | Unity.Profiling.ProfilerRecorder 7 | UnityEngine.Camera 6
    UnityEngine.UI.MaskableGraphic 6 | UnityEngine.Profiling.Profiler 6 | UnityEngine.Video.VideoPlayer 5 | UnityEngine.Hash 5
    UnityEngine.GL 5 | UnityEngine.Experimental.Rendering.RayTracingAccelerationStructure 5 | UnityEngine.TouchScreenKeyboard 5
    UnityEngine.GraphicsBuffer 4 | UnityEngine.Texture 4 | UnityEngine.QualitySettings 4 | UnityEngine.UI.Graphic 4
    UnityEditor.EditorWindow 4 | TextCore.LowLevel.FontEngine 4 | UnityEngine.Shader 4 | SceneManagement.SceneManager 4
    Display 3 | ParticleSystem 3 | Touch 3 | SkinnedMeshRenderer 3 | RenderTexture 3 | Graphics 3 | TestTools.LogAssert 3
    其余 1~2 处：Animator / AudioClip / AudioSource / AudioSettings / AudioFilterBehaviour / LineRenderer / Mesh /
    ParticleSystemRenderer / ScreenCapture / InputSystem / Jobs.IJobParallelForTransformExtensions / Input / Texture2D /
    RectTransform / Texture2DArray / Texture3D / Time / Scripting.GarbageCollector / AnimationClip / Resources / Renderer /
    RaycastHit / Object / Motion / Material / LowLevel.PlayerLoop / Jobs.TransformAccessArray / CustomYieldInstruction /
    RuntimeAnimatorController / TrailRenderer

**与 modder 直接相关的 stub（清单）：**

    UnityEngine.Time::set_timeScale                     （get_timeScale 恒为 1）
    UnityEngine.Input::GetAxis / GetTouch               （GetAxis 的 ldstr: "Horizontal" "Vertical" "Mouse X" "Mouse Y" "Mouse ScrollWheel"）
    UnityEngine.Material::SetTexture
    UnityEngine.Object::set_hideFlags
    UnityEngine.Texture2D::SetPixelData（仅 mip 解码路径）/ PackTextures
    UnityEngine.Shader::GetGlobalTexture / GetPropertyName / GetPropertyType / GetPropertyRangeLimits
    UnityEngine.Resources::GetBuiltinResource           （ldstr ".ttf"）
    UnityEngine.Graphics::DrawTexture / ExecuteCommandBuffer / ExecuteCommandBufferAsync
    UnityEngine.Camera::get_stereoEnabled / get_stereoActiveEye / AddCommandBuffer / AddCommandBufferAsync /
                        GetStereoProjectionMatrix / GetStereoViewMatrix
    UnityEngine.Mesh::Optimize / SetIndices
    UnityEngine.ScreenCapture::CaptureScreenshot / WarnIfSuperSized
    UnityEngine.RenderTexture::GetNativeDepthBufferPtr / DiscardContents×2
    UnityEngine.AudioClip::get_isFinite / get_isRealtime ; AudioSource::PlayClipAtPoint / ApplySpatialState ;
    AudioSettings::Reset ; AudioFilterBehaviour::Push
    Unity.Profiling.ProfilerRecorder::{Start,StartNew,Stop,Dispose,get_Valid,get_CurrentValue,get_LastValue} ;
    Unity.Profiling.Memory.MemoryProfiler::TakeSnapshot ; Unity.Collections.NativeSortExtension::Sort
    UnityEngine.ComputeShader::*（整套）; UnityEngine.CullingGroup::*（几乎整套）; UnityEngine.Rendering.CommandBuffer::*（30 处）
    TMPro.TMP_FontAsset::CreateFontAsset ; UnityStandardAssets.ImageEffects.PostEffectsBase::DrawBorder

#### (4) Assembly-CSharp 实际用到的 UnityEngine 类型

命令：`[IlAsm]::TypeRefs($g\Assembly-CSharp.dll, $w, "UnityStubs")` → **173 条 typeRef**（完整列表，按文件顺序）：

    UnityEngine.GUIStyle, Rect, TextAnchor, Vector2, Vector3, Event, Coroutine, MonoBehaviour,
    Unity.Jobs.IJob, JobHandle, IJobFor, IJobParallelFor,
    UnityEngine.Jobs.IJobParallelForTransform, TransformAccess, TransformAccessArray,
    Unity.Collections.LowLevel.Unsafe.NativeDisableUnsafePtrRestrictionAttribute, Unity.Collections.Allocator,
    Unity.Collections.LowLevel.Unsafe.UnsafeUtility, UnityEngine.Keyframe, WrapMode, AnimationCurve, Vector4, Texture2D,
    Color, Matrix4x4, Color32, Unity.Collections.NativeArray<T>, NativeList<T>, NativeBitArray,
    Unity.Collections.LowLevel.Unsafe.UnsafeList<T>, UnsafeBitArray, NativeContainerAttribute, WriteAccessRequiredAttribute,
    UnityEngine.Bounds, Camera, Unity.Burst.BurstCompileAttribute, Unity.Mathematics.int3, float3, UnityEngine.Quaternion,
    UnityEngine.TextAsset, KeyCode, EventType, Rendering.RenderQueue, Ray, RuntimePlatform, Material, LogType,
    AsyncOperation, Shader, MaterialPropertyBlock, GameObject, RenderTexture, AudioClip, RenderTextureFormat,
    SceneManagement.Scene, UnityStandardAssets.ImageEffects.ColorCorrectionCurves, Resolution, RefreshRate, SystemLanguage,
    Mesh, Unity.Collections.ReadOnlyAttribute, NativeDisableParallelForRestrictionAttribute, UnityEngine.Object,
    UnityEngine.AssetBundle, TextureFormat, Unity.Collections.NativeReference<T>, UnityEngine.Graphics, Texture, FilterMode,
    JetBrains.Annotations.CanBeNullAttribute, UnityEngine.Font, GUIContent, EventModifiers, Vector2Int, FullScreenMode,
    UnityEngine.GUI, Unity.Profiling.ProfilerRecorder, UnityEngine.RaycastHit, TextEditor, Gradient, GradientColorKey,
    GradientAlphaKey, UnityStubs.Gui.IGuiBackend, UnityEngine.RectOffset, Unity.Collections.NativeSetThreadIndexAttribute,
    UnityEngine.AudioReverbPreset, AudioReverbFilter, AudioSource, Behaviour, AudioLowPassFilter, AudioHighPassFilter,
    AudioEchoFilter, AudioRolloffMode, JetBrains.Annotations.UsedImplicitlyAttribute, UnityEngine.Transform,
    Unity.Profiling.ProfilerMarker, TMPro.TMP_FontAsset, UnityEngine.TextMesh, TMPro.TextMeshPro, TMP_TextInfo,
    TMP_CharacterInfo, UnityEngine.MeshCollider, Mathf, Time, Unity.Jobs.IJobExtensions, IJobForExtensions,
    IJobParallelForExtensions, UnityEngine.Jobs.IJobParallelForTransformExtensions, UnityEngine.GL, ScaleMode, Input,
    GUIUtility, UnityEngine.Profiling.Profiler, Resources, Unity.Collections.LowLevel.Unsafe.NativeArrayUnsafeUtility,
    NativeListUnsafeUtility, NativeArrayOptions, AllocatorManager, Unity.Mathematics.math, UnityEngine.Screen,
    Application, Unity.Jobs.LowLevel.Unsafe.JobsUtility, UnityEngine.SystemInfo, Waylith.UnityCompat.UnityRuntime,
    Waylith.UnityCompat.UnityAppState, UnityEngine.Debug, ILogger, StackTraceUtility, SceneManagement.SceneManager,
    UnityEngine.LayerMask, Component, RenderingPath, CameraClearFlags, UnityStubs.ImportDefaults, TextureWrapMode,
    UnityEngine.Analytics.PerformanceReporting, UnityStubs.Gui.GuiBackend, Rendering.ShadowCastingMode,
    UnityStubs.ContentPacks, Unity.Collections.NativeListExtensions, UnityEngine.ImageConversion, RenderTextureReadWrite,
    Experimental.Rendering.GraphicsFormat, TextureCreationFlags, ColorUtility, GUISkin, GUIStyleState, GUISettings,
    FocusType, Unity.Profiling.ProfilerCategory, ProfilerRecorderOptions, UnityEngine.PrimitiveType, Physics, Cursor,
    CursorMode, AudioListener, ScreenCapture, UnityStubs.ModAssetPacks, FontStyle, AudioDistortionFilter,
    AudioChorusFilter, RenderBuffer, TMPro.TMP_Text, TextAlignment, MeshRenderer, Renderer, UnityEngine.UI.Graphic,
    TMPro.TMP_MeshInfo, TMP_VertexDataUpdateFlags, UnityEngine.Collider, WaitForSeconds, WaitUntil, Random

分组统计（对 173 条按命名空间）：

    Unity.Collections 19 | Unity.Jobs 8 | UnityEngine.Jobs 4 | Unity.Profiling 4 | Unity.Mathematics 3 |
    JetBrains.Annotations 2 | UnityStubs.Gui 2 | UnityEngine.SceneManagement 2 | UnityEngine.Rendering 2 |
    UnityEngine.Experimental 2 | Waylith.UnityCompat 2 | UnityEngine.* 单个各 1（约 120 条）

→ 注意两点：
1. **Unity.Jobs / Unity.Collections / Unity.Profiling / Unity.Mathematics / Unity.Burst 的 API 也由 UnityStubs.dll 提供**（不是 Waylith）。
2. 游戏代码**直接引用 Waylith.UnityCompat.UnityRuntime / UnityAppState**（用来判断引擎是否就绪），并引用 `UnityStubs.Gui.*` / `UnityStubs.ContentPacks` / `UnityStubs.ModAssetPacks` / `UnityStubs.ImportDefaults` 等内部类型。

#### (5) 游戏代码现在用什么替代（Waylith 栈）

`Assembly-CSharp.dll` 对各程序集的 typeRef 计数：

    UnityStubs 173 | Waylith 58 | Waylith.AssetBake 1 | Brutal.Core.Logging 5 | Brutal.Vulkan 2 |
    com.rlabrecque.steamworks.net 35 | ISharpZipLib 2 | System.Runtime 225 | System.Private.CoreLib 0

`Waylith.dll` 命名空间规模（`[IlAsm]::NamespaceStats`）：

    Waylith.Rendering 186 | Waylith.Math 33 | Waylith.Profiling 26 | Waylith.Graphics 26 | Waylith.Graphics.Meshes 26 |
    Waylith.Rendering.Compute 13 | Waylith 12 | Waylith.Input 10 | Waylith.Assets 10 | Waylith.Diagnostics 9 |
    Waylith.Audio 8 | Waylith.Runtime 7 | Waylith.Jobs 7 | Waylith.Utils 6 | Waylith.Profiling.Instrumentation 6 |
    Waylith.PlatformSpecific 6 | Waylith.Logging 5 | Waylith.Hardware 5 | Waylith.Collections 4 | Waylith.CLI 4 |
    Waylith.Rendering.PostFx 3 | Waylith.Rendering.Culling 2 | Waylith.Audio.MiniAudio 2 | (global) 449

游戏自身用到的一部分 Waylith 类型（`[IlAsm]::TypeRefs($g\Assembly-CSharp.dll,$w,"Waylith")` 前 45 条）：

    Waylith.Rendering.RenderQueueValue / ShaderProgramDefinition / Shader / ShaderHotReloader / ShaderWarmupPlan /
      ShaderKeywordContribution / Texture2D / BcEncodeTarget / LoadedTextureData / TextureSwizzle / GpuTextureAllocation /
      TexturePixelData / GpuTextureService / ITextureCacheSource / TextureCompressionSettings / Mipmapper / ShaderRegistry /
      PipelineState / ShaderSourceLoader / MaterialLayout / ShaderVertexInputLayout / PrecompiledShaderStages /
      ShaderPrewarmer / ShaderVariantEnumerator / AssetPrefetcher / LoadedTextureFormat / Texture
    Waylith.AssetBake.ContentBakeResult
    Waylith.Profiling.FrameProfiler / ProfilerLabelId / ZoneChunk / ZoneNode / RuntimePauseReason / ProfilerPathTable /
      ThreadTimeline / ProfilerWindowRequest / ProfilerWindowResult / PathAccumulator / VramProfiler
    Waylith.Diagnostics.ProcessMemorySnapshot / MemoryReportSection / MemoryReportItem
    Waylith.Graphics.GpuMemorySummary / GpuDescription        Waylith.Logging.VerboseLog

`Waylith.UnityCompat.dll`（51712 字节）提供 Unity 风格的运行时桥：命名空间 `Waylith.UnityCompat`，类型含
`UnityRuntime`（13 个方法，Classify 行：`Waylith.UnityCompat.UnityRuntime | base=System.Object [System.Runtime] | methods=13 | internalcall=0 | pinvoke=0 | ilbytes=409 | callsWaylith=49 | callsUnity=4#throws=0`）、`UnityWorld`（102 方法）、`UnityFrame`、`UnityUtils`、`UnityCompatDiagnostics`、`UnityWorld/{UnityObjectState,UnityGameObjectState,UnityComponentState,UnityBehaviourState,UnityTransformState}`、`UnityWorld/UnityMessageType`、`UnityWorld/UnityResourceEntry` 等。

---

### 2.3 问题 3：实际可用的 1.7 C# mod 范本

命令：`Get-ChildItem -LiteralPath "E:\SteamLibrary\steamapps\workshop\content\294100" -Directory` 后对每个 mod 检查 `1.7` 目录、递归 DLL、`About\About.xml`、`LoadFolders.xml`。

**136 个 mod 中 22 个含 `1.7` 目录，其中 20 个在 1.7 下有 DLL**（2 个无 DLL）。带 DLL 清单：

| # | PublishedFileId | 名称 | 1.7 下的 DLL（相对 mod 根） |
| --- | --- | --- | --- |
| 1 | 3216091476 | 补货状态 Restocking Status | 1.7\Assemblies\RestockingStatus.dll (6144) |
| 2 | 3264193512 | AAAA (Allowed Area Automatic Adapter) | 1.7\Assemblies\AAAA.dll (78336) |
| 3 | 2990606008 | AB's Head Apparel Tweaker | 1.7\Assemblies\ABEasyLib.dll (20480), 1.7\Assemblies\HeadApparelTweaker.dll (59392) |
| 4 | 2423311270 | Destroy Item | 1.7\Assemblies\DestroyItem.dll (16384) |
| 5 | 2599942235 | DragSelect | 1.7\Assemblies\DragSelect.dll (10752), 1.7\ModCompat\TradeUIRevised\Assemblies\DragSelectTradeUIRevisedCompat.dll (8192) |
| 6 | 1446523594 | Dubs Mint Menus | 1.7\Assemblies\0Harmony.dll (2523136), 1.7\Assemblies\DubsMintMenus.dll (214016) |
| 7 | 1662119905 | Dubs Mint Minimap | 1.7\Assemblies\0Harmony.dll (2523136), 1.7\Assemblies\DubsMintMinimap.dll |
| 8 | 2009463077 | Harmony | 1.7\Assemblies\0Harmony.dll (2532864), 1.7\Assemblies\HarmonyMod.dll (15872) |
| 9 | 839005762 | Humanoid Alien Races | 1.7\Assemblies\0Harmony.dll (2356224), 1.7\Assemblies\AlienRace.dll (427008) |
| 10 | 3769804600 | Mine Sight | 1.7\Assemblies\MineSight.dll (56320) |
| 11 | 872762753 | MinifyEverything | 1.7\Assemblies\0Harmony.dll (2193920), 1.7\Assemblies\MinifyEverything.dll |
| 12 | 3220120457 | Music Manager (Continued) | 1.7\Assemblies\MusicManager.dll (55808) |
| 13 | 2917732219 | Muzzle Flash | 1.7\Assemblies\0Harmony.dll (2060800), 1.7\Assemblies\MuzzleFlash.dll (35328) |
| 14 | 3524116050 | Performance - Slower Pawn Tick Rate | 1.7\Assemblies\SlowerPawnTickRate.dll (14336)（另含 Source\…\obj\Debug 的同名副本） |
| 15 | 3513846773 | Quality Colors (Continued) | 1.7\Assemblies\QualityColors.dll (54784) |
| 16 | 3526354009 | Replace Stuff - Continued | 1.7\Assemblies\Replace_Stuff.dll (133632) |
| 17 | 1504723424 | Smart Speed | 1.7\Assemblies\SmartSpeed.dll (15872) |
| 18 | 2113372560 | TradeHelper | 1.7\Assemblies\TradeHelper.dll (17408) |
| 19 | 2538411704 | Visual Exceptions | 1.7\Assemblies\CrossPromotion.dll (60416), 1.7\Assemblies\VisualExceptions.dll (50688) |
| 20 | 2888380373 | WVC - Work Modes | 1.7\Assemblies\WVC_MoreMechanoidsWorkModes_Main.dll (67072), 1.7\Odyssey\Assemblies\WVC_WorkModes_Odyssey.dll (15872) |

#### 推荐的 5 个范本（含其 DLL 的 TFM 与 AssemblyRefs 实测）

    #2 AAAA.dll           TargetFramework=.NETCoreApp,Version=v10.0 ; refs: Assembly-CSharp 1.7.9785.1822 ; 0Harmony 3.0.0.0
    #6 DubsMintMenus.dll  .NETCoreApp,Version=v10.0 ; refs: Assembly-CSharp 1.7.9781.31297 ; 0Harmony 3.0.0.0 ; (自带 1.7\Assemblies\0Harmony.dll)
    #9 AlienRace.dll      .NETCoreApp,Version=v10.0 ; refs: Assembly-CSharp 1.7.9784.3272 ; 0Harmony 2.3.6.0   ; (自带 1.7\Assemblies\0Harmony.dll 2356224)
    #10 MineSight.dll     .NETCoreApp,Version=v10.0 ; refs: Assembly-CSharp 1.7.9785.1822 ; 0Harmony 3.0.0.0 ; Waylith 1.0.0.0
    #16 Replace_Stuff.dll .NETCoreApp,Version=v10.0 ; refs: Assembly-CSharp 1.7.9784.3272 ; 0Harmony 2.4.2.0

全部 20 个 mod 的 DLL 都**引用了 Assembly-CSharp**（版本 1.7.9781.31297 / 1.7.9782.27799 / 1.7.9782.37458 / 1.7.9784.3272 / 1.7.9785.1822 / 1.7.9786.4087），绝大多数为 `.NETCoreApp,Version=v10.0`。

**是否自带 0Harmony.dll：**

- **自带**（6 个）：1446523594 Dubs Mint Menus、1662119905 Dubs Mint Minimap、2009463077 Harmony、839005762 HAR、872762753 MinifyEverything、2917732219 Muzzle Flash
- **不自带**（14 个）：3216091476、3264193512、2990606008、2423311270、2599942235、3769804600、3220120457、3524116050、3513846773、3526354009、1504723424、2113372560、2538411704、2888380373 —— 它们**引用了 0Harmony 却不打包**，因此必须依赖 brrainz.harmony 被同时启用。

**自带 0Harmony 的版本各不相同**：2.3.3.0（MuzzleFlash）/ 2.3.6.0（AlienRace）/ 2.4.1.0（HeadApparelTweaker）/ 2.4.2.0（Replace_Stuff、MusicManager）/ 2.4.3.0（SmartSpeed）/ 3.0.0.0（DubsMintMenus、QualityColors、DragSelect、AAAA、MineSight、RestockingStatus、VisualExceptions、HarmonyMod）—— 说明**编译期引用的 0Harmony 版本不需要等于 Harmony mod 提供的 3.0.1.0**。

**重要反例：仍按 .NET Framework 编译、却直接放进 1.7 目录的 DLL**

    #3 HeadApparelTweaker.dll : TargetFramework=.NETFramework,Version=v4.8
        refs: mscorlib 4.0.0.0 ; **Assembly-CSharp 1.6.9676.17735** ; 0Harmony 2.4.1.0 ;
              UnityEngine.CoreModule 0.0.0.0 ; UnityEngine.IMGUIModule ; UnityEngine.TextRenderingModule ;
              ABEasyLib ; AlienRace ; System.Core
    #4 DestroyItem.dll : .NETFramework,Version=v4.8 ; refs: mscorlib 4.0.0.0 ; Assembly-CSharp 1.7.9784.3272 ;
        UnityStubs 1.0.0.0 ; System.Core   （无 0Harmony）
    #18 TradeHelper.dll : .NETFramework,Version=v4.7.2 ; refs: mscorlib 4.0.0.0 ; Assembly-CSharp 1.7.9786.4087 ;
        UnityStubs ; 0Harmony 2.10.1.0 ; System.Core ; System 4.0.0.0

→ 这三个 DLL 引用的是 `UnityEngine.CoreModule` 这类在 1.7 已**不存在**的程序集，能加载只能依赖 `WaylithClr.AssemblyNameRedirects` 把 `UnityEngine*=` 重定向到 `UnityStubs`（`WaylithClr.LaxAssemblyBinding`/`LaxTypeRefResolution` 也开着）。
**推测：**这些是「1.6 时代 DLL 原样塞进 1.7 目录」的 mod（HeadApparelTweaker 甚至引用 Assembly-CSharp 1.6 版本号），能在 1.7 下加载**不等于**其 API 用法在 1.7 仍正确。

#### 1.7 目录的两种声明方式（实测）

`LoadFolders.xml` 原始文本按 `<v1.7>` 匹配（注意节点名里是**点**，不是 `v1_7`）：

    Harmony(2009463077)          v1.7 => <li>/</li> <li>1.7</li>
    AAAA(3264193512)             v1.7 => <li>Common</li> <li>1.7</li>
    Mine Sight(3769804600)       v1.7 => <li>Common</li> <li>1.7</li>
    AB's Head Apparel(2990606008) v1.7 => <li>/</li> <li>1.7</li>
    DragSelect(2599942235)       v1.7 => <li>1.7</li> <li>/</li> <li IfModActive="hobtook.tradeui">1.7/ModCompat/TradeUIRevised</li>
    Humanoid Alien Races(839005762) v1.7 => <li>/</li> <li>1.7</li>
        <li IfModActive="Ludeon.RimWorld.Ideology">1.7/Mods/Ideology</li>
        <li IfModActive="Ludeon.RimWorld.Odyssey">1.7/Mods/Odyssey</li>
    Replace Stuff(3526354009)    v1.7 => <li>/</li> <li>1.1</li> <li>1.2</li> <li>1.3</li> <li>1.4</li> <li>1.5</li> <li>1.6</li> <li>1.7</li>
    Visual Exceptions(2538411704) v1.7 => <li>/</li> <li>1.7</li>
    WVC - Work Modes(2888380373)  v1.7 => <li>/</li> <li>1.7</li> <li IfModActive="brrainz.harmony">1.7/Odyssey</li>
    Music Manager(3220120457)     v1.7 => <li>1.7</li>
    Smart Speed(1504723424)       v1.7 => <li>/</li> <li>1.7</li>

**没有 `LoadFolders.xml` 的 mod 也能用 1.7 目录**（例如 Quality Colors 3513846773 只有 `1.2…1.7` 目录 + `About` + `Languages`，Dubs Mint Menus 1446523594 同样没有）——原因是游戏在 `Verse.ModContentPack::InitLoadFolders` 里有自动探测（见 2.5）。

---

### 2.4 问题 4：modder 入口类型是否仍存在

命令：`[IlAsm]::TypeNames($g\Assembly-CSharp.dll, $w, "<过滤词>")` 与 `[IlDump2]::Dump(..., exactType, withIl, ...)`

    --- filter "RimWorld.DefOf"        -> 2 types
          RimWorld.DefOf : System.Attribute   [methods=1]
          RimWorld.DefOfHelper : System.Object [methods=4]
    --- filter "Verse.DefModExtension" -> 1 types
          Verse.DefModExtension : System.Object [methods=3]
    --- filter "Verse.ThingComp"       -> 3 types
          Verse.ThingComp : System.Object [methods=82]
          Verse.ThingCompUtility : System.Object [methods=5]
          Verse.ThingComp_VacuumAware : Verse.ThingComp [methods=4]      <-- 1.7 新增
    --- filter "Verse.HediffComp"      -> 153 types（家族完整）
          Verse.HediffCompProperties : System.Object [methods=4]
          Verse.HediffComp : System.Object [methods=33]
          Verse.HediffCompProperties_AttachPoints / Verse.HediffComp_AttachPoints / …（共 153 个，含 Verse.HediffComp_* 与 …Properties_*）
    --- filter "Verse.Mod"             -> 54 types（节选）
          Verse.Mod : System.Object [methods=6]
          Verse.ModContentPack : System.Object [methods=37]
          Verse.ModAssemblyHandler : System.Object [methods=3]
          Verse.ModSettings : System.Object [methods=5]
          Verse.ModLister [methods=40] / Verse.ModMetaData [methods=63] / Verse.ModSummaryWindow / Verse.ModContentHolder<T> …
    --- filter "Verse.CompProperties"  -> 10 types
          Verse.CompProperties : System.Object [methods=8] (+ CompProperties_AffectsSky / _HeatPusher / _Lifespan / …)
    --- filter "HarmonyLib"            -> 0 types

`Verse.Mod` 的完整 API（IL 实证）：

    TYPE Verse.Mod : System.Object
      FIELD modSettings (Private) / intContent (Private) ;  PROP Content
      METHOD get_Content il=7 → ldfld intContent ; ret
      METHOD .ctor(Verse.ModContentPack) il=14 → call Object::.ctor / stfld intContent
      METHOD GetSettings il=180 → 类型不符时报 Verse.Log::Error("Mod {0} attempted to read two different settings classes (was {1}, is now {2})")
                                 否则 Verse.LoadedModManager::ReadModSettings(Content.FolderName, GetType().Name) → ModSettings::set_Mod
      METHOD WriteSettings il=20 / DoSettingsWindowContents il=1（ret）/ SettingsCategory il=6（ldstr ""）

→ **`public class Main : Verse.Mod` 的写法在 1.7 完全成立（构造函数签名一致）。**

`HarmonyLib` 在 Assembly-CSharp 里 0 个类型：游戏只在 `Verse.ProfilerUI.Dialog_ProfilerAssemblies::HarmonyPatchLines` 里用字符串 `"HarmonyLib.Harmony"` + `GenTypes::GetTypeInAnyAssembly` + 反射（见 2.1 依据 B）。真正的 HarmonyLib 类型在 mod 的 `0Harmony.dll` 里（HarmonyLib 命名空间 118 个类型）。

**顺带核实：`ModUpdating.txt`（17464 字节，404 行）只到 1.0→1.1 的内容**（`"1.0 -> 1.1"` 章节 + MOD FILE STRUCTURE / MOD METADATA / LOAD FOLDERS / SUPPORTING MULTIPLE GAME VERSIONS），**没有任何 1.7 / 引擎替换 / C# 相关说明**（对 `1.7|1.6 ->|Harmony|Unity|Assembly|C#|Waylith|net10|CoreLib` 的逐行 grep 只命中 3 处泛化描述与 steaWorkshopUrl）。→ 官方没有随 1.7 更新这份文档。

---

### 2.5 附：mod 程序集加载与「1.7 目录」解析的决定性 IL

#### (1) 程序集加载仍是从 `Assemblies/` 目录 `Assembly.LoadFrom`

`Verse.ModAssemblyHandler::ReloadAll`（il=230）：

    ldfld mod → ldstr "Assemblies/" → ModContentPack::GetAllFilesForModPreserveOrder
      → Enumerable::Select → 逐个 Assembly::LoadFrom(FileSystemInfo::get_FullName)
        （try/catch → Verse.Log::Error，插值串 "Exception loading {name}: {exc}"）
      → ModAssemblyHandler::AssemblyIsUsable(assembly) → true 时 GenTypes::ClearCache() → loadedAssemblies.Add

`Verse.ModAssemblyHandler::AssemblyIsUsable`（il=268）：第一步即 `assembly.GetTypes()`；抛 `ReflectionTypeLoadException` 时打印

    "ReflectionTypeLoadException getting types in assembly {asm.GetName().Name}: {ex}"
    （空行）"Loader exceptions:"
    每条 "   => {loaderException}"

并**返回 false**（其它异常同样返回 false）。

→ **任何一个类型解析失败（缺依赖程序集、签名不匹配），整个 DLL 都会被丢弃**；DLL 的所有依赖必须一并放进 `Assemblies/`。

#### (2) 版本目录解析（`Verse.ModContentPack::InitLoadFolders`，il=570）

    if (ModLister.GetModWithIdentifier(PackageId)?.loadFolders != null && DefinedVersions().Count > 0):
        folders = mod.LoadFoldersForVersion(VersionControl.CurrentVersionString)   // "1.7.4981 rev136"
        if folders.Count > 0 → AddFolders(folders); return
        version = DefinedVersions().Where(...).OrderByDescending(...).FirstOrDefault()
        if version 非空 → AddFolders(LoadFoldersForVersion(version)); return
        否则 → AddFolders(LoadFoldersForVersion("default"))
    if foldersToLoadDescendingOrder.Count == 0:
        dir = Path.Combine(RootDir, VersionControl.CurrentVersionStringWithoutBuild)   // 见下：实测 == "1.7"
        if Directory.Exists(dir) → add dir
        else → 枚举 RootDir 下所有可解析为版本的子目录，排序后**选择一个版本目录**加入（推测：取不超过当前版本的最高版本目录）
        Common = Path.Combine(RootDir, ModContentPack::CommonFolderName) ; if Directory.Exists → add
        add RootDir

配套证据：

- `RimWorld.VersionControl::.cctor`（il=377）里
  `versionStringWithoutBuild = version.Major + "." + version.Minor`（IL 里是 `Major.ToString() + "." + Minor.ToString()` 两次 `string::Concat`），
  `version` 由 `Assembly::GetExecutingAssembly().GetName().Version`（即 Assembly-CSharp 的 1.7.9786.4087 → Build=9786-4805=4981, Revision=4087*2/60=136）推得
  → **`CurrentVersionStringWithoutBuild` 的字面值就是 `"1.7"`**，与 `Version.txt` 的 `1.7.4981 rev136` 自洽。
- `Verse.ModLoadFolders::LoadDataFromXmlCustom`（il=631）：子节点名先 `ToLower()`，若以 `"v"` 开头则 `Substring(1)`（所以 `<v1.7>` → 键 `"1.7"`），条目文本为 `/` 或 `\` 时按「mod 根目录」处理（`new Verse.LoadFolder("", …)`），并解析三种属性 **`IfModActive` / `IfModActiveAll` / `IfModNotActive`**（逗号分隔 packageId 列表）。
- `Verse.LoadFolder::get_ShouldLoad`（il=84）：依次判断 `requiredAnyOfPackageIds`（`ModLister::AnyModActiveNoSuffix`）、`requiredAllOfPackageIds`（`AllModsActiveNoSuffix`）、`disallowedAnyOfPackageIds`。
- `Verse.ModLoadFolders::GetIssueList` 的诊断键名（可用于排查 LoadFolders 写法）：`ModLoadFolderListEmpty` / `ModLoadFolderRepeatingFolder` / `ModLoadFolderMalformedVersion` / `ModLoadFolderDefaultDeprecated` / `ModLoadFolderOutOfOrder` / `ModLoadFolderDoesntExist` / `ModLoadFolderDefinesUnsupportedGameVersion`。

→ **结论：`LoadFolders.xml` 是可选的；即使不写，只要目录名恰好是 `1.7`（当前版本 major.minor），游戏也会自动加载它**（外加 `Common` 与 mod 根目录）。

---

### 2.6 复现用工具与产物

所有辅助工具都在临时目录 `C:\Users\<user>\AppData\Local\Temp\rw17\`（未写入工作区）：

| 工具 | 作用 |
| --- | --- |
| asmrefs.ps1 | 打印 DLL 的 AssemblyDefinition 名/版本 + 全部 AssemblyReferences + TargetFramework |
| IlDump.cs / IlClass.cs | 类型清单；每类型 methods/internalcall/pinvoke/ilbytes/callsWaylith/callsUnity 统计；成员与 IL dump |
| IlStub.cs | `Scan(path,w,callNeedle,typeFilter)`：列出调用指定成员的方法 + 其 ldstr 常量 |
| IlAsm.cs | `TypeRefs` / `TypeNames` / `NamespaceStats` / `RawUtf16Search` / `RawAsciiSearch` |
| IlDump2.cs | `Dump(path,w,exactType,withIl,methodFilter)`：单类型完整字段/属性/方法签名 + 逐条 IL |
| IlStr.cs | `FindString(path,w,needle,withCalls,withIl)`：找含指定 ldstr 的方法 |

产物：`C:\Users\<user>\AppData\Local\Temp\rw17\stubwarner.txt`（258 行，257 个 stub 方法）、`...\acsharp_unityrefs.txt`（173 条 UnityStubs typeRef）、`...\loadfolders.txt`。

常用命令骨架：

    Add-Type -Path "C:\Users\<user>\AppData\Local\Temp\rw17\IlDump2.cs"
    $sw = New-Object System.IO.StringWriter
    [IlDump2]::Dump("E:\SteamLibrary\steamapps\common\RimWorld\Assembly-CSharp.dll", $sw, "Verse.Mod", $true, "")
    $sw.ToString()

（注：PowerShell 中 System.Reflection.Metadata 的扩展方法不能直接调用，须写 `[System.Reflection.Metadata.PEReaderExtensions]::GetMetadataReader($pe)`。）

---

## 三、对 mod 模板的具体影响

### 3.1 推荐的 1.7 mod 目录结构

    YourMod/
      About/
        About.xml                 <-- supportedVersions 必须含 <li>1.7</li>
      LoadFolders.xml             <-- 可选但建议（见下）
      Common/                     <-- 可选，跨版本共享内容（游戏自动加载）
      Defs/ Patches/ Textures/ Languages/
      1.7/
        Assemblies/
          YourMod.dll
          （0Harmony.dll 一般不要打包，交给 Harmony mod）
        Defs/ Patches/ Textures/ …

`LoadFolders.xml`（多版本 + 条件加载的写法，与实测 mod 一致）：

    <loadFolders>
      <v1.6><li>/</li><li>1.6</li></v1.6>
      <v1.7><li>/</li><li>1.7</li></v1.7>
    </loadFolders>

条件加载：`<li IfModActive="brrainz.harmony">1.7/Odyssey</li>`、`IfModActiveAll`（全部启用才加载）、`IfModNotActive`（都不启用才加载）。

### 3.2 编译配置（csproj）要点

    <PropertyGroup>
      <TargetFramework>net10.0</TargetFramework>          <!-- 与 0Harmony/UnityStubs 一致：.NETCoreApp,Version=v10.0 -->
      <LangVersion>latest</LangVersion>
      <Nullable>disable</Nullable>                         <!-- 游戏程序集未启用可空注解 -->
      <EnableDefaultCompileItems>true</EnableDefaultCompileItems>
    </PropertyGroup>
    <ItemGroup>
      <!-- 全部是 Private=false 的参考程序集，编译 DLL 里不应复制它们 -->
      <Reference Include="Assembly-CSharp"><HintPath>E:\SteamLibrary\steamapps\common\RimWorld\Assembly-CSharp.dll</HintPath><Private>false</Private></Reference>
      <Reference Include="UnityStubs"><HintPath>E:\SteamLibrary\steamapps\common\RimWorld\UnityStubs.dll</HintPath><Private>false</Private></Reference>
      <Reference Include="0Harmony"><HintPath>E:\SteamLibrary\steamapps\workshop\content\294100\2009463077\1.7\Assemblies\0Harmony.dll</HintPath><Private>false</Private></Reference>
      <!-- 需要引擎能力时才引： -->
      <Reference Include="Waylith"><HintPath>E:\SteamLibrary\steamapps\common\RimWorld\Waylith.dll</HintPath><Private>false</Private></Reference>
    </ItemGroup>

**不要引用** `UnityEngine.CoreModule / UnityEngine.IMGUIModule / UnityEngine.TextRenderingModule` 等——1.7 已不存在这些文件（根目录 `UnityEngine*.dll` 递归 0 命中）。

### 3.3 代码模板

    // 入口：与 1.6 完全一致
    public class Main : Verse.Mod
    {
        public Main(Verse.ModContentPack content) : base(content)
        {
            var h = new HarmonyLib.Harmony("yourname.yourmod");
            h.PatchAll(System.Reflection.Assembly.GetExecutingAssembly());
        }
    }
    // 设置：Verse.ModSettings 未变（可通过 GetSettings<T>() 读取）

- 程序集级特性（`[StaticConstructorOnStartup]`、`[DefOf]`、`[HarmonyPatch]`、`[HotSwappableAttribute]`）仍可用（`RimWorld.DefOf` / `Verse.DefOfHelper` 存在）。
- `[HarmonyPatch]` 对 `Assembly-CSharp` 类型打补丁是白名单内目标（`WaylithClr.JitPatchableAssemblies="Assembly-CSharp"`）。
- 日志用 `Verse.Log`（HarmonyMod 自己在用）。
- 反射查找 Unity 类型时，程序集名是 `"UnityStubs"`，**不是** `"UnityEngine.CoreModule"`。

### 3.4 明确会失效 / 有坑的 1.6 写法

| 1.6 写法 | 1.7 状态 | 证据 |
| --- | --- | --- |
| 引用 `UnityEngine.*.dll` 并 `CopyLocal` | **失效**：这些程序集不存在；只能引用 `UnityStubs.dll`（旧 DLL 靠 `AssemblyNameRedirects` 侥幸加载） | 根目录 `UnityEngine*.dll` 0 命中；`AssemblyNameRedirects` |
| 反射 `Type.GetType("…, UnityEngine.CoreModule")` | **失效** → 改用 `", UnityStubs"` | 同上 |
| `Input.GetAxis` / `Input.GetTouch` | **stub**：记警告返回默认值（鼠标滚轮/摇杆/触摸读取拿不到值） | stubwarner.txt：`UnityEngine.Input::GetAxis‖"Horizontal" "Vertical" "Mouse X" "Mouse Y" "Mouse ScrollWheel"` |
| `Time.timeScale` 赋值 | **stub**；`get_timeScale` 硬编码返回 1 → 任何「加速/变速」逻辑必须换实现（1.7 有 `SmartSpeed`、`SlowerPawnTickRate` 之类 mod，说明有替代路径，具体 API 未确认） | Time.cs 行 36 LogStub；get_timeScale: `ldc.r4 1; ret` |
| `Material.SetTexture` | **stub** | stubwarner.txt |
| `UnityEngine.Object.hideFlags` 赋值 | **stub** | stubwarner.txt |
| `Graphics.DrawTexture` / `Graphics.ExecuteCommandBuffer(Async)` | **stub** | stubwarner.txt |
| `Resources.GetBuiltinResource<T>(…, ".ttf")` | **stub** | stubwarner.txt（ldstr ".ttf"） |
| `Mesh.Optimize` / `Mesh.SetIndices` | **stub** | stubwarner.txt |
| `ScreenCapture.CaptureScreenshot` | **stub** | stubwarner.txt |
| `Unity.Profiling.ProfilerRecorder` / `UnityEngine.Profiling.Profiler` 采样 | **stub** → 用 `Waylith.Profiling.*`（FrameProfiler / ProfilerLabelId / ThreadTimeline / VramProfiler…） | stubwarner.txt + Assembly-CSharp 的 Waylith typeRefs |
| `ComputeShader.*`、`CommandBuffer.*`、`CullingGroup.*`、`ParticleSystem` 高级路径、`TouchScreenKeyboard`、`UnityEngine.UI/TMP/Video/InputSystem` 大量成员 | **stub**（记警告） | stubwarner.txt TOP 统计 |
| `UnityEngine.SceneManagement.SceneManager` 覆盖/加载 API 的一部分（4 处）、`RenderTexture.DiscardContents`、`Camera.AddCommandBuffer` | **stub** | stubwarner.txt |
| 依赖旧 Unity 的 `Physics` 射线检测细节 | 类型是真实现，但是否与 Waylith 的物理/网格 BVH（`UnityStubs.Internal.MeshRaycastBvh`）语义一致 **未验证** | 见第四节 |
| 打包旧版 `0Harmony.dll`（2.x）且同时启用 Harmony mod | 会被 HarmonyMod 检测并输出告警（"Another Harmony library was loaded before the Harmony mod could." / "This means that your Harmony version is now downgraded to …"）；实测 1.7 下不同 mod 带了 2.3.3~3.0.0 多个版本，风险真实存在 | HarmonyMod.Main::.cctor IL 字符串 |
| 把依赖 DLL 放在 `Assemblies/` 之外或用 `Assembly.LoadFile` 自加载 | 若 `AssemblyIsUsable` 阶段 `GetTypes()` 抛异常，**整个 DLL 被拒**并报 `"Loader exceptions:"` | ModAssemblyHandler::AssemblyIsUsable IL |
| `.NET Framework 4.x` 目标 + `UnityEngine.*` 引用 | 加载可能成功（已有 3 个实例），但属于未受支持的组合；**建议改 net10.0** | HeadApparelTweaker / DestroyItem / TradeHelper 实测 |

### 3.5 兼容层「真实现」带来的好消息

以下 1.6 常见用法**在 1.7 下仍是真实现，可直接沿用**（方法数/stub 数见 2.2）：
`Vector2/Vector3/Vector4/Vector2Int/Color/Color32/Rect/RectOffset/Mathf/Quaternion/Matrix4x4/Bounds/Ray`（全部 0 stub）、
`GUI/GUIStyle/GUIContent/GUISkin/Event/KeyCode`（0 stub）、`Screen/Application/SystemInfo`（0 stub）、
`Texture2D/LoadImage`、`Material`（除 SetTexture）、`Shader`（除 4 个反射式属性查询）、`Transform/GameObject/Component/Behaviour/MonoBehaviour`（0 stub）、
`Debug/Log`、`Coroutine 协程（CoroutineScheduler）`、`JsonUtility`、`AnimationCurve`、`AudioClip/AudioSource` 基本播放。

---

## 四、无法确认的未知项

1. **Harmony 补丁在运行中的 1.7 是否真的生效（最高优先级未知项）**
   本任务禁止启动游戏，无法实测。已知风险：
   - MonoMod.Core 内含 `"JIT version does not match expected JIT version! expected: {}, got: {}"`、`"guid == ExpectedJitVersion"`、`"Error while setting up the ICorJitInfo wrapper: "`、`"Unknown .NET Core 3.x minor version"` 等探测代码，且 `0Harmony.dll` 对 Waylith 一无所知；
   - 但 `coreclr.dll` 提供 `JitPatchableAssemblies`/patchpoint 机制、游戏本体主动消费 Harmony 补丁信息、官方 Profiler 把 0Harmony/MonoMod/Cecil 排除在插桩外——三处都指向「Harmony 被官方预期可用」。
   **推测：**常规 Prefix/Postfix（native detour + 入口重定向）可用；需要一次真机验证（启动游戏、加载一个含 1.7 Harmony 补丁的 mod、看 Logs 与 `Verse.ProfilerUI` 的补丁列表）。**唯一稳妥的验证命令是实际运行游戏**，本轮未做。
2. **`WaylithClr.JitPatchableAssemblies` 白名单对 Harmony 是否必要**
   Harmony 3.0 走的是自己的原生 detour，**没有**引用 Waylith / 该配置；白名单可能是 WaylithClr 内部（热重载/OSR patchpoint）使用。**未确认**未列入白名单的程序集（例如 mod 自己的 DLL）能否被 Harmony 在自己身上打补丁——HarmonyMod 自身不在白名单里，但它对自己 `PatchAll`（只有 `HarmonyMod.VersionControl_DrawInfoInCorner_Patch` 等少数补丁）。**推测：**Harmony 自己打自己没问题，但「补丁目标是不是必须白名单内」需要实验。
3. **`JitNoInlinePatchableIntoDynamicMethods`/内联导致的补丁失效**
   0Harmony 里有 `"Could not disable inlining of method {}; detours may not be reliable"`。1.7 的 JIT 是自研实现，是否支持「禁止内联」的常规手段未验证。
4. **UnityStubs 的「实现质量」分层**
   257 个方法明确是 stub（记警告），但**其余 ~7200 个方法虽非 stub，也不代表行为与 Unity 完全一致**（例如 `Camera` 只调用了 1 次 Waylith、`Input` 0 次 Waylith 却非 stub，说明部分实现是纯托管状态机）。逐 API 的行为等价性无法静态判定。**建议**：把「UnityStubs 里非 stub」当作「可以尝试」，把关键路径放到游戏里冒烟测试。
5. **GUI/渲染的实际后端**
   `UnityStubs.Gui.IGuiBackend / GuiBackend / TextMeshProBackend` 存在，但由谁实现（Waylith? Brutal.ImGui?）、mod 自绘 UI 在 1.7 的显示效果如何，未验证。
6. **输入系统**：`Input.GetAxis/GetTouch` 是 stub；`Waylith.Input`（10 个类型）是否是可用的替代 API、`Input.GetKey*` 是否真能用，未验证。
7. **1.7 相对 1.6 的 Verse/RimWorld API 变更**：本轮只确认了入口类型存在（`Verse.Mod`/`ModContentPack`/`ModAssemblyHandler`/`DefOf`/`DefModExtension`/`ThingComp`/`HediffComp`），**没有做逐 API diff**。**建议**：直接以 1.7 的 `Assembly-CSharp.dll` 为参考程序集编译旧 mod 源码，让编译器把 API 变更全部暴露出来（这也是最省时的迁移方法）。
8. **非托管/反射类高级技巧**：`System.Reflection.Emit`、动态方法、`AccessTools` 的字段访问在 WaylithClr 上是否全部可用（配置里 `LaxPrivateFieldNames`/`SkipAccessChecks`/`DynamicMethodOwnerIsDeclaringType` 等开关开着，看起来是为兼容而设），未逐项验证。
9. **`ModUpdating.txt` 没有 1.7 内容**，官方是否另有迁移文档未在本地发现（本地只找到这一份，且只到 1.0→1.1）。
10. **`Data\Core` 之外的官方扩展目录（Royalty/Ideology/Biotech/Anomaly/Odyssey）在 1.7 的程序集组织**未展开检查（它们可能也含 DLL；本轮只确认 `Data\` 下 6 个目录与 `Mods\` 为空）。

---

### 附：本报告未能做到的事

- 未启动游戏，因此**所有「运行时行为」结论都是静态推断**（已逐条标注）。
- 未验证 Workshop 上 1.7 标记的 mod 是否**实际能跑**（只验证了它们的文件结构、目标框架与程序集引用）。
