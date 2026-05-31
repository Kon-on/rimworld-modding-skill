# 06 — Harmony 补丁

> **适用版本**: RimWorld 1.6（Harmony 2.x） | **最后更新**: 2026-05-31

## 概述

Harmony 是 RimWorld mod 社区的标准代码补丁库。它让你**在运行时**修改原版代码或其它 mod 的行为，而不需要修改原始 DLL 文件——避免了 mod 之间的冲突。

**使用场景**：
- 修改某个方法的返回值
- 在某个方法执行前后插入自己的逻辑
- 完全替换某个方法的实现
- 修改 AI 行为、战斗计算、生成逻辑等

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
