// AI 辅助生成 | 目标平台 RimWorld 1.7.4981 rev136 (net10.0)
// ---------------------------------------------------------------------------
// 补丁 ID: Demo.RimTestMod.Patches.ProjectileImpactPatch
//
// 目标方法真实签名（System.Reflection 读出）：
//   protected virtual System.Void Verse.Projectile.Impact(Verse.Thing hitThing, System.Boolean blockedByShield)
//   hitThing 无默认值，blockedByShield 默认值 False = 该方法带可选参数。
// 注意 Impact 是 protected：HarmonyLib.AccessTools.Method 默认用 BindingFlags.all，
// 能拿到非公开方法，所以不需要手写 bindingFlags。
// ---------------------------------------------------------------------------
using System;
using HarmonyLib;
using Verse;

namespace Demo.RimTestMod.Patches
{
    internal static class ProjectileImpactPatch
    {
        public const string PatchId = "Demo.RimTestMod.Patches.ProjectileImpactPatch";

        public const string TargetSignature =
            "protected virtual System.Void Verse.Projectile.Impact(Verse.Thing hitThing, System.Boolean blockedByShield)";

        internal static void Postfix(Projectile __instance, Thing hitThing, bool blockedByShield)
        {
            try
            {
                if (!PatchCommon.IsDmDef(__instance))
                {
                    return;
                }
                Log.Message("[RimTestMod.Patches] Projectile.Impact 补丁命中："
                            + __instance.def.defName
                            + " 命中 " + (hitThing != null ? hitThing.LabelShortCap : "(地面/无目标)")
                            + " blockedByShield=" + blockedByShield
                            + " 伤害=" + __instance.DamageAmount
                            + " 伤害类型=" + (__instance.DamageDef != null ? __instance.DamageDef.defName : "(null)"));
            }
            catch (Exception ex)
            {
                Log.Error("[RimTestMod.Patches] ProjectileImpactPatch.Postfix 抛异常：" + ex);
            }
        }
    }
}
