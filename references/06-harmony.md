# 06 — Harmony 补丁

> **适用版本**: RimWorld 1.7（实测 1.7.4981 rev136 + Harmony 3.0） | **最后更新**: 2026-10-18
>
> ⚠️ 1.7 有三件事和 1.6 教程不一样：**游戏不自带 0Harmony**、**Harmony 升到 3.0（没有 `patchId` 了）**、
> **目标框架是 net10.0**。先看下面的「1.7 上的 Harmony」再抄代码。


## 目录

- [概述](#概述)
- [基础架构](#基础架构)
- [三种补丁类型](#三种补丁类型)
- [特殊参数](#特殊参数)
- [常见实战模式](#常见实战模式)
- [Harmony ID 冲突](#harmonyid冲突)
- [调试 Harmony 补丁](#调试harmony补丁)
- [与 XML Patch 的对比](#与xmlpatch的对比)

## 概述

Harmony 是 RimWorld mod 社区的标准代码补丁库。它让你**在运行时**修改原版代码或其它 mod 的行为，而不需要修改原始 DLL 文件——避免了 mod 之间的冲突。

**使用场景**：
- 修改某个方法的返回值
- 在某个方法执行前后插入自己的逻辑
- 完全替换某个方法的实现
- 修改 AI 行为、战斗计算、生成逻辑等

## 1.7 上的 Harmony（先看这个）

| 事项 | 1.6 及更早 | **1.7 实测** |
|---|---|---|
| 0Harmony.dll 从哪来 | 玩家 mod 列表里的 Harmony mod | **一样**，但游戏本体不再自带：本机只有创意工坊 `...\workshop\content\294100\2009463077\1.7\Assemblies\0Harmony.dll`（约 2.5 MB） |
| About.xml 依赖 | 常写 `<modDependencies>` 指向 Harmony | **必须写**，否则玩家漏装时你的补丁会静默失效 |
| 编译期引用 | 引用 0Harmony.dll | 一样：**只作编译期引用，绝不复制进 `Assemblies/`**（游戏侧由 Harmony mod 提供） |
| 补丁 ID | `Patch(..., id)` / `HarmonyMethod.id` | **Harmony 3.0 没有 `id` 字段了**。用唯一的 Harmony 实例 ID + 补丁类名，自己维护 `const string PatchId` 常量写日志 |
| 目标框架漂移 | .NET Framework 4.7.2 | 游戏是 **net10.0**，0Harmony 的编译目标是 net8 —— 本机实测能编译能在启动时加载，**但运行时是否全场景正常未验证**（我们只在启动阶段验证了补丁登记成功） |

### 推荐：bootstrap 模式（1.7 实测写法）

1.6 教程爱用 `PatchAll()`，它省事但有一个致命缺点：**一个补丁目标找不到就会抛异常，整条初始化链断掉**。
1.7 上更稳的做法是逐条 `AccessTools.Method` 取目标、取不到就 `Log.Error` 后继续：

```csharp
[StaticConstructorOnStartup]
public static class MyMod_PatchBootstrap
{
    private const string HarmonyId = "<你的packageId>.patches";
    private const string Tag = "[MyMod.Patches] ";

    static MyMod_PatchBootstrap()
    {
        try { Apply(); }
        catch (Exception e) { Log.Error(Tag + "补丁引导失败：" + e); }   // 只报错，不拖垮其他程序集
    }

    [MethodImpl(MethodImplOptions.NoInlining)]   // 隔离 HarmonyLib 类型：缺 0Harmony 时只红字，不丢整个 DLL
    private static void Apply()
    {
        var harmony = new Harmony(HarmonyId);
        int ok = 0, fail = 0;
        Patch(harmony, AccessTools.Method(typeof(Projectile), "Impact",
              new[] { typeof(Thing), typeof(bool) }), "MyMod.ProjectileImpact", ref ok, ref fail);
        Log.Message($"{Tag}补丁引导结束：成功 {ok} / 失败 {fail} / Harmony 自报 {harmony.GetPatchedMethods().Count()}");
    }

    [MethodImpl(MethodImplOptions.NoInlining)]
    private static void Patch(Harmony h, MethodBase target, string patchId, ref int ok, ref int fail)
    {
        if (target == null) { Log.Error($"{Tag}找不到目标方法，跳过 {patchId}"); fail++; return; }
        h.Patch(target, prefix: null, postfix: new HarmonyMethod(/* 你的 Postfix */));
        Log.Message($"{Tag}已打补丁 {patchId} → {target.DeclaringType?.Name}.{target.Name}");
        ok++;
    }
}
```

2. **补丁放独立程序集**：主逻辑一个 DLL（`MyMod.dll`），补丁一个 DLL（`MyMod.Patches.dll`）。
   好处是玩家没装 Harmony 时只有补丁 DLL 报错，主 mod 的物品/Def 照常可用。
   本仓库的 44 文件测试 mod 就是这么分的，可直接对照源码：
   `examples/rimtest-mod/RimTestMod/Source/Patches/RimTestMod_PatchBootstrap.cs`、
   `examples/rimtest-mod/RimTestMod/Source/build.ps1`（含 `0Harmony` 只引用不复制、产物目录禁止出现游戏 DLL 的校验）。

## 基础架构

### 入口类


```csharp
using Verse;
using HarmonyLib;
using System.Reflection;

// 用户自行替换命名空间和 Harmony ID
namespace <你的前缀>.<你的Mod名>
{
    [StaticConstructorOnStartup]
    public static class HarmonyPatches
    {
        private static readonly Harmony instance;

        static HarmonyPatches()
        {
            // Harmony ID 必须由用户根据 packageId 自行填写，确保全局唯一
            instance = new Harmony("<你的packageId>");
            instance.PatchAll(Assembly.GetExecutingAssembly());
            Log.Message("<你的packageId>: Harmony patches applied.");
        }
    }
}
```

**关键点**：
- `[StaticConstructorOnStartup]` 确保在游戏加载后、主菜单显示前执行
- `"<你的packageId>"` 是 Harmony ID，**必须全局唯一，由用户自行填写**（与 About.xml 中的 packageId 保持一致）
- `PatchAll()` 自动扫描当前程序集中所有带 `[HarmonyPatch]` 特性的类
- ⚠️ 上面是最小示例。1.7 上更推荐下面的 bootstrap 模式：目标方法找不到时只报红字，不会因一个补丁失败而中断整个程序集

## 三种补丁类型

### 1. Prefix（前置拦截——最常用）

在原始方法执行**之前**运行。可以：
- 修改传入参数（通过 `ref`）
- 阻止原始方法执行（返回 `false`）
- 提前设置返回值

```csharp
[HarmonyPatch(typeof(Pawn), "Kill")]
public static class Patch_Pawn_Kill
{
    [HarmonyPrefix]
    public static bool Prefix(Pawn __instance, DamageInfo? dinfo, ref Hediff exactCulprit)
    {
        // 阻止特定 Pawn 被杀死
        if (__instance.def.defName == "SR_Immortal")
        {
            return false;  // 返回 false = 跳过原始方法
        }
        return true;  // 返回 true = 继续执行原始方法
    }
}
```

### 2. Postfix（后置拦截）

在原始方法执行**之后**运行。可以：
- 读取/修改返回值（通过 `ref __result`）
- 读取 `__state`（Prefix 传来的数据）

```csharp
[HarmonyPatch(typeof(Thing), "TakeDamage")]
public static class Patch_Thing_TakeDamage
{
    [HarmonyPostfix]
    public static void Postfix(Thing __instance, ref DamageInfo dinfo)
    {
        // 记录所有受到伤害的对象和伤害值
        Log.Message($"{__instance.Label} took {dinfo.Amount} damage from {dinfo.Instigator}");
    }
}
```

### 3. Transpiler（IL 级别修改——高级）

直接修改方法的 IL 中间码。除非你非常了解 IL，否则优先使用 Prefix/Postfix 组合。

```csharp
[HarmonyPatch(typeof(TargetClass), "TargetMethod")]
public static class Patch_Transpiler
{
    [HarmonyTranspiler]
    public static IEnumerable<CodeInstruction> Transpiler(IEnumerable<CodeInstruction> instructions)
    {
        // 修改 IL 指令序列
        // 高级用法，新手可跳过
        return instructions;
    }
}
```

## 特殊参数

Harmony 通过**参数名**自动注入以下值：

| 参数名 | 类型 | 说明 | 用于 |
|--------|------|------|------|
| `__instance` | 原始类的类型 | 调用方法的实例（静态方法为 null） | Prefix/Postfix |
| `__result` | 原始返回类型（加 `ref`） | 原始方法的返回值，可修改 | Postfix（读/写）, Prefix（提前设值） |
| `__state` | 任意类型 | Prefix 传给 Postfix 的桥梁 | Prefix（赋值）+ Postfix（读取） |
| `___paramName` | 参数类型（加 `ref`） | 原始方法的参数（三个下划线前缀） | Prefix（修改参数值） |

## 常见实战模式

### 模式 1：修改配方产出

```csharp
[HarmonyPatch(typeof(GenRecipe), "PostProcessProduct")]
public static class Patch_GenRecipe_PostProcessProduct
{
    [HarmonyPostfix]
    public static void Postfix(ref Thing product, RecipeDef recipeDef, Pawn worker)
    {
        // 如果制作者是 SR_ 特殊角色，产出品质提升
        if (worker?.def.defName == "SR_MasterCrafter")
        {
            if (product.TryGetComp<CompQuality>() is CompQuality qc)
            {
                qc.SetQuality(QualityCategory.Legendary, ArtGenerationContext.Outsider);
            }
        }
    }
}
```

### 模式 2：修改 AI 行为

```csharp
[HarmonyPatch(typeof(JobGiver_Work), "TryIssueJobPackage")]
public static class Patch_JobGiver_Work
{
    [HarmonyPrefix]
    public static bool Prefix(Pawn pawn, ref ThinkResult __result)
    {
        // 如果是 SR_ 特殊角色，禁止自动工作
        if (pawn.def.defName == "SR_LazyPawn" && Rand.Value < 0.5f)
        {
            __result = ThinkResult.NoJob;
            return false;
        }
        return true;
    }
}
```

### 模式 3：拦截事件触发

```csharp
[HarmonyPatch(typeof(IncidentWorker_Raid), "TryExecuteWorker")]
public static class Patch_Raid
{
    [HarmonyPrefix]
    public static bool Prefix(IncidentParms parms)
    {
        // 如果 mod 设置中禁用了袭击，阻止事件
        if (ModSettings_SR.disableRaids)
        {
            return false;
        }
        return true;
    }
}
```

## Harmony ID 冲突

如果两个 mod 同时 patch 同一个方法且使用相同的 Harmony ID 前缀，可能冲突。

**解决**：确保你的 `new Harmony("ID")` 中的 ID 与 packageId 类似（如 `yourname.modname`）。

## 调试 Harmony 补丁

1. 在 Prefix/Postfix 开头添加 `Log.Message()` 确认补丁被调用
2. 开启 RimWorld Dev Mode → 查看控制台输出
3. 检查 `Player.log`（路径见 `references/08-debugging.md`）

## 与 XML Patch 的对比

| | XML PatchOperations | Harmony |
|------|------|------|
| 修改数据 | ✅ | 不适用 |
| 修改行为/逻辑 | ❌ | ✅ |
| 冲突风险 | 低 | 中（同方法多 patch） |
| 学习难度 | 低 | 中高 |
| 需要编译 | 不需要 | 需要 |
