// AI 辅助生成 | 目标平台 RimWorld 1.7.4981 rev136 (net10.0)
// ---------------------------------------------------------------------------
// 补丁 ID: Demo.RimTestMod.Patches.ThingTakeDamagePatch
//
// 目标方法真实签名（System.Reflection 读出）：
//   public Verse.DamageWorker+DamageResult Verse.Thing.TakeDamage(Verse.DamageInfo dinfo)
//   非 virtual、公开、返回嵌套类型 DamageWorker.DamageResult。
// 这里刻意【不声明】__result —— 返回值 DamageResult 是 class 还是 struct 没实测，
// 声明错了会让 Prefix/Postfix 直接绑定失败；本补丁只需要看伤害前后的血量。
//
// 本补丁还演示了跨程序集调用：RimTestMod.Patches.dll 引用 RimTestMod.dll 的
// Demo.RimTestMod.ThingComp_TestShield 与 Verse.ThingCompUtility 扩展方法。
// ---------------------------------------------------------------------------
using System;
using HarmonyLib;
using Verse;

namespace Demo.RimTestMod.Patches
{
    internal static class ThingTakeDamagePatch
    {
        public const string PatchId = "Demo.RimTestMod.Patches.ThingTakeDamagePatch";

        public const string TargetSignature =
            "public Verse.DamageWorker+DamageResult Verse.Thing.TakeDamage(Verse.DamageInfo dinfo)";

        /// <summary>进 TakeDamage 之前把血量存进 __state（-1 表示不关心 / 无需记录）。</summary>
        internal static void Prefix(Thing __instance, ref int __state)
        {
            __state = -1;
            try
            {
                if (__instance == null)
                {
                    return;
                }
                __state = __instance.HitPoints;
            }
            catch (Exception ex)
            {
                Log.Error("[RimTestMod.Patches] ThingTakeDamagePatch.Prefix 抛异常：" + ex);
            }
        }

        internal static void Postfix(Thing __instance, DamageInfo dinfo, int __state)
        {
            try
            {
                if (__instance == null || __state < 0)
                {
                    return;
                }
                bool related = PatchCommon.IsDmDef(__instance) || HasTestShield(__instance);
                if (!related)
                {
                    return; // 全游戏伤害都记日志会刷屏，只记与测试 mod 相关的那部分
                }
                Log.Message("[RimTestMod.Patches] Thing.TakeDamage 补丁命中："
                            + (__instance.def != null ? __instance.def.defName : "(null)")
                            + " 血量 " + __state + " → " + __instance.HitPoints
                            + " 伤害=" + dinfo.Amount
                            + " 类型=" + (dinfo.Def != null ? dinfo.Def.defName : "(null)"));
            }
            catch (Exception ex)
            {
                Log.Error("[RimTestMod.Patches] ThingTakeDamagePatch.Postfix 抛异常：" + ex);
            }
        }

        private static bool HasTestShield(Thing t)
        {
            try
            {
                return ThingCompUtility.TryGetComp<Demo.RimTestMod.ThingComp_TestShield>(t) != null;
            }
            catch (Exception)
            {
                return false;
            }
        }
    }
}
