> ✅ **核对状态：本页用到的类型与成员签名，已用反射对 1.7 游戏目录里的 DLL 逐条核对（0 处不存在、0 处签名不符；命令与原始输出见 `04-核验/C#接口核对结果.md`）；运行期行为未实机验证。**
>
> 核对目标（本机实测）：`Assembly-CSharp.dll` 版本 **1.7.9786.4087**、**16,221** 个类型；`UnityStubs.dll` **934** 个类型 / **6,653** 个方法，其中 **254** 个方法是 stub（分布在 88 个类型，清单见 `07-附录-UnityStubs失效成员清单.md`）；`0Harmony.dll` **3.0.0.0**（2,326 个类型，来自创意工坊 mod 2009463077）。
>
> 1.7 环境要点：目标框架 **net10.0**；**UnityEngine.\* 由 UnityStubs.dll 提供**（真兼容层，stub 只记警告并返回默认值、**不抛异常**）；**Harmony 不在游戏内**，须声明依赖 mod 2009463077 或自带 0Harmony.dll。
>
> csproj 要点：`<TargetFramework>net10.0</TargetFramework>`；引用游戏根目录的 `Assembly-CSharp.dll` 与 `UnityStubs.dll`（Private=false）；**不要引用 `UnityEngine.*.dll`**（1.7 已无这些文件）；依赖的第三方 DLL 必须一起放进 `Assemblies\`（否则整个 DLL 会被拒载并打印 "Loader exceptions:"）。

# Harmony 补丁

## 用途

**Harmony 用来在不改原版代码的前提下修改已有方法的行为**（前缀、后缀、替换）。1.7 里它**不再随游戏内置**。

**典型用途**：改原版数值、在方法前后插入逻辑、绕过一个判断。

## 1.7 的关键差异

| 项 | 1.6 | 1.7 |
|---|---|---|
| Harmony 来源 | 随游戏/其他 mod 提供 | **独立创意工坊 mod 2009463077** |
| 0Harmony.dll 版本 | 2.4.3（net472） | **3.0.0.0-rc.3（net10.0）** |
| HarmonyMod.dll | 2.4.2 | 3.0.1.0 |
| 引用方式（样本 csproj） | Lib.Harmony 2.3.1.1 | **Lib.Harmony 3.0.0-rc.2** |

以上四行来自实测样本（mod 2009463077 与 3216091476 的 csproj 逐行对比）。

## 代码

```csharp
using HarmonyLib;
using Verse;

namespace ExampleMod
{
    [StaticConstructorOnStartup]
    public static class HarmonyBootstrap
    {
        static HarmonyBootstrap()
        {
            var harmony = new Harmony("examplemod.patches");
            harmony.PatchAll();
            Log.Message("[ExampleMod] Harmony 补丁已装载。");
        }
    }

    // 前缀：返回 false 可跳过原方法
    [HarmonyPatch(typeof(Pawn), nameof(Pawn.Kill))]
    public static class Patch_Pawn_Kill
    {
        [HarmonyPrefix]
        public static bool Prefix(Pawn __instance)
        {
            if (__instance == null) return true;
            // 返回 false = 不执行原方法
            return true;
        }
    }

    // 后缀：在原方法之后执行，可读 __result
    [HarmonyPatch(typeof(Pawn), nameof(Pawn.Kill))]
    public static class Patch_Pawn_Kill_Post
    {
        [HarmonyPostfix]
        public static void Postfix(Pawn __instance, ref DamageInfo? dinfo) { }
    }
}
```

mod 的 About.xml 里声明依赖：

```xml
<modDependencies>
  <li>
    <packageId>brrainz.harmony</packageId>
    <displayName>Harmony</displayName>
    <steamWorkshopUrl>steam://url/CommunityFilePage/2009463077</steamWorkshopUrl>
  </li>
</modDependencies>
```

## 常见坑

- **1.7 必须自己解决 Harmony 依赖**：游戏目录里递归搜 `*Harmony*` 命中 0 个文件（实测），不能假设玩家环境已有。
- **Harmony 2.x 的补丁写法在 3.0 上不保证兼容**：样本 mod 都同步升到了 3.x，建议跟齐。
- **补丁 ID 要唯一**（`new Harmony("作者.mod")`），用默认 ID 会与其他 mod 冲突。
- **补丁方法签名必须与原方法严格匹配**，1.7 换了 CLR（Waylith CLR），模糊匹配的容错行为未知（待验证）。
- **不要试图补丁 UnityEngine.\* 类型**：它们现在来自 UnityStubs.dll 垫片，不是真实实现。

## 核验

本页用到的每个类型与成员，都已用反射对 1.7 的 DLL 逐条核对（原始输出见 `04-核验/C#接口核对结果.md`）：

| 本页用到 | 1.7 实际签名（机器核对） |
|---|---|
| `HarmonyLib.Harmony` 构造函数 | `public Harmony(string id)`（也有无参构造） |
| `HarmonyLib.Harmony.PatchAll` | `public void PatchAll()` / `public void PatchAll(Assembly assembly)` |
| `HarmonyLib.Harmony.Patch` | `public MethodInfo Patch(MethodBase original, HarmonyMethod prefix = null, HarmonyMethod postfix = null, HarmonyMethod transpiler = null, HarmonyMethod finalizer = null)` |
| 卸载/查询 | `UnpatchAll(string harmonyID = null)`、`Unpatch(MethodBase, HarmonyPatchType, string harmonyID = null)`、`GetAllPatchedMethods()`、`GetPatchInfo(MethodBase)`、`PatchCategory/CreateProcessor/CreateReversePatcher` 均在 |
| `HarmonyLib.HarmonyPatch` | 存在（基类 `HarmonyAttribute`）；`HarmonyPrefix`、`HarmonyPostfix`、`HarmonyMethod`、`HarmonyPatchAll` 也都在 |
| `Verse.Pawn.Kill` | **Pawn 上只有 1 个**：`public virtual void Kill(Nullable<DamageInfo> dinfo, Hediff exactCulprit = null)` → `nameof(Pawn.Kill)` **无歧义**；Postfix 里的 `ref DamageInfo? dinfo` 与参数名/类型都对得上（参数名必须与原名一致） |
| `StaticConstructorOnStartup` | `Verse.StaticConstructorOnStartup : System.Attribute`（在 `using Verse;` 下可用） |
| 程序集版本 | `0Harmony.dll` = **3.0.0.0**（2,326 个类型），不是 2.4.3 |

**为什么这次敢说「可以用」**（静态证据链，全部本机实测）：

1. `RimWorld.runtimeconfig.json` 里有 `WaylithClr.JitPatchableAssemblies = "Assembly-CSharp"` —— 官方把游戏主程序集标记为**可打 JIT 补丁**。
2. `coreclr.dll` 里能找到 `EEConfig::JitPatchableAssemblies` 访问器与 `JIT_Patchpoint*` 字符串 —— 自研 CLR 里确实保留了补丁点机制。
3. 游戏自己的 `Verse.ProfilerUI.Dialog_ProfilerAssemblies` 会反射调用 `HarmonyLib.Harmony.GetAllPatchedMethods` / `GetPatchInfo` —— 官方 UI 预期玩家装了 Harmony。
4. `0Harmony.dll` 自带 MonoMod 原生 detour 实现（net10.0），HarmonyMod.dll 本身就是一个 `Verse.Mod` 子类，其静态构造函数里 `new Harmony("net.pardeike.rimworld.lib.harmony")` + `PatchAll(自身)`。

**唯一保留的未知项（重要）**：补丁在运行中的 1.7 是否**真的生效**无法静态证实 —— MonoMod 的 detour 依赖 `clrjit`/`ICorJitInfo` 版本探测，而 1.7 用的 `WaylithClr 10.0.13-waylithclr.dev` 是自研 CLR。**首次实机加载务必看日志里有没有补丁失败信息**。

其他依据：Harmony 外置=游戏安装目录递归搜 `*Harmony*` 结果 0 条（实测）；mod 2009463077 的 1.6/1.7 两版 0Harmony.dll 与 HarmonyMod.dll 对比（实测）；样本 csproj `...\294100\3216091476\1.7\Source\mod.csproj`（Lib.Harmony 2.3.1.1→3.0.0-rc.2）。
