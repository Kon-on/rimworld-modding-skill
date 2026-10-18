// Harmony 补丁模板（RimWorld 1.7 + Harmony 3.0）
// 验证状态：已验证（1.7.4981 rev136 真机编译 + 启动时补丁登记实测；0Harmony 来自创意工坊
//            Harmony mod 2009463077 的 1.7/Assemblies/0Harmony.dll，仅编译期引用、不随包分发。
//            可对照的完整实现：examples/rimtest-mod/RimTestMod/Source/Patches/）
// AI 辅助生成
// 替换 <YourNamespace> 和 <YourModID> 为你的实际值
//
// 1.7 关键差异（1.6 教程在这里几乎全错）：
//   1. 游戏本体**不自带** 0Harmony.dll —— About.xml 里必须声明依赖 Harmony mod，否则玩家漏装时补丁静默失效
//   2. Harmony 升到 **3.0**：HarmonyMethod 没有 id 字段了，PatchAll 之外没有"补丁 ID"概念
//      → 用唯一的 Harmony 实例 ID + 自己的 PatchId 常量写日志
//   3. 目标框架 net10.0；引用 Assembly-CSharp.dll / RimWorld.dll / UnityStubs.dll（都在游戏安装根目录）
//   4. 推荐"逐条取目标 + 取不到只报错"的 bootstrap 写法：一个补丁目标找不到，不会拖垮整条初始化链
//   5. 补丁建议放**独立程序集**（MyMod.Patches.dll）：缺 Harmony 时只有补丁报红字，主 mod 照常可用

using Verse;
using HarmonyLib;
using System;
using System.Linq;
using System.Reflection;
using System.Runtime.CompilerServices;

namespace <YourNamespace>
{
    /// <summary>
    /// 补丁入口——游戏启动时（主菜单出现前）执行一次。
    /// </summary>
    [StaticConstructorOnStartup]
    public static class <YourModID>_PatchBootstrap
    {
        // Harmony 实例 ID：全局唯一，建议用 packageId 派生
        private const string HarmonyId = "<YourModID>.patches";
        // 日志前缀，方便在 Player.log 里过滤
        private const string Tag = "[<YourModID>.Patches] ";

        static <YourModID>_PatchBootstrap()
        {
            try
            {
                Apply();
            }
            catch (Exception e)
            {
                // 只报错：不要把异常抛到外层，否则可能连带影响同程序集的其他内容
                Log.Error(Tag + "补丁引导失败：" + e);
            }
        }

        /// <summary>
        /// NoInlining 的作用：把 HarmonyLib 类型的解析推迟到方法被调用时。
        /// 玩家没装 Harmony 时，JIT 只在调用这一句时报错，而不是在加载整个程序集时炸掉。
        /// </summary>
        [MethodImpl(MethodImplOptions.NoInlining)]
        private static void Apply()
        {
            var harmony = new Harmony(HarmonyId);
            int ok = 0, failed = 0;

            // ── 逐条登记补丁：目标签名写全（参数类型必须精确，否则 AccessTools 取不到） ──
            Patch(harmony,
                AccessTools.Method(typeof(Projectile), "Impact", new[] { typeof(Thing), typeof(bool) }),
                "Patch_Projectile_Impact", Patch_Projectile_Impact.Postfix, ref ok, ref failed);

            // 取不到目标就跳过，不抛异常
            Log.Message($"{Tag}补丁引导结束：成功 {ok} / 失败 {failed} / Harmony 自报 {harmony.GetPatchedMethods().Count()}");
        }

        [MethodImpl(MethodImplOptions.NoInlining)]
        private static void Patch(Harmony harmony, MethodBase target, string patchId,
                                  MethodInfo postfix, ref int ok, ref int failed)
        {
            if (target == null)
            {
                Log.Error($"{Tag}目标方法不存在，跳过 {patchId}（游戏版本变了？用 dnSpy 核对签名）");
                failed++;
                return;
            }

            harmony.Patch(target, prefix: null, postfix: new HarmonyMethod(postfix));
            Log.Message($"{Tag}已打补丁 {patchId} → {target.DeclaringType?.Name}.{target.Name}");
            ok++;
        }
    }

    /// <summary>
    /// 示例补丁：Projectile.Impact(Thing hitThing, bool blockedByShield)
    /// Postfix 可以读到 __instance 与原始参数；要改返回值就加 ref __result。
    /// </summary>
    public static class Patch_Projectile_Impact
    {
        // 只对自己 mod 的东西打日志，避免刷屏
        private static bool IsOurs(Thing t) => t?.def?.defName?.StartsWith("<YourPrefix>_") == true;

        public static void Postfix(Projectile __instance, Thing hitThing, bool blockedByShield)
        {
            if (!IsOurs(__instance) && !IsOurs(hitThing)) return;
            Log.Message($"{Tag}Impact：{__instance.def.defName} 命中 {hitThing?.LabelShortCap} blockedByShield={blockedByShield}");
        }
    }

    /// <summary>
    /// Prefix / Transpiler 的骨架（按需启用）。
    /// Prefix 返回 false = 跳过原方法；返回 true = 继续执行。
    /// </summary>
    // public static class Patch_SomeType_SomeMethod
    // {
    //     [HarmonyPrefix]
    //     public static bool Prefix(/* 原始参数列表（类型必须与方法签名一致） */)
    //     {
    //         return true;
    //     }
    //
    //     [HarmonyTranspiler]
    //     public static IEnumerable<CodeInstruction> Transpiler(IEnumerable<CodeInstruction> instructions)
    //     {
    //         return instructions;   // 高级用法：直接改 IL
    //     }
    // }
}
