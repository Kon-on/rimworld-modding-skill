// AI 辅助生成 | 目标平台 RimWorld 1.7.4981 rev136 (net10.0)
// ---------------------------------------------------------------------------
// 补丁 ID: Demo.RimTestMod.Patches.ProjectileLaunchPatch
//
// 目标方法真实签名（由 System.Reflection 从游戏根目录 Assembly-CSharp.dll 读出，
// 不是凭记忆写的；同一签名也原样写在本文件常量 TargetSignature 里）：
//   public virtual System.Void Verse.Projectile.Launch(
//       Verse.Thing launcher,
//       UnityEngine.Vector3 origin,
//       Verse.LocalTargetInfo usedTarget,
//       Verse.LocalTargetInfo intendedTarget,
//       Verse.ProjectileHitFlags hitFlags,
//       System.Boolean preventFriendlyFire,
//       Verse.Thing equipment,
//       Verse.ThingDef targetCoverDef)
// 参数名与默认值也是从元数据读出的：preventFriendlyFire 默认值 False。
// Projectile 的 namespace 是 Verse，不是 RimWorld（RimWorld 下没有 Projectile 类型）。
//
// 这里刻意引用 UnityEngine.Vector3（经 UnityStubs.dll 提供），以证明 1.7 的
// 「Unity 只剩存根」不会挡住补丁程序集的编译与签名绑定。
// ---------------------------------------------------------------------------
using System;
using HarmonyLib;
using UnityEngine;
using Verse;

namespace Demo.RimTestMod.Patches
{
    internal static class ProjectileLaunchPatch
    {
        /// <summary>人读补丁 ID（Harmony 3.0 的 HarmonyMethod 没有 id 字段，只有 category）。</summary>
        public const string PatchId = "Demo.RimTestMod.Patches.ProjectileLaunchPatch";

        /// <summary>目标方法签名原文（元数据核验结果）。</summary>
        public const string TargetSignature =
            "public virtual System.Void Verse.Projectile.Launch(Verse.Thing launcher, UnityEngine.Vector3 origin, Verse.LocalTargetInfo usedTarget, Verse.LocalTargetInfo intendedTarget, Verse.ProjectileHitFlags hitFlags, System.Boolean preventFriendlyFire, Verse.Thing equipment, Verse.ThingDef targetCoverDef)";

        /// <summary>
        /// Postfix。参数只取用得到的原参数（launcher / usedTarget / intendedTarget），
        /// 没有声明 origin / hitFlags / equipment / targetCoverDef —— 少取参数不会影响补丁绑定，
        /// 少一个参数就少一份绑定失败的风险。
        /// </summary>
        internal static void Postfix(Projectile __instance, Thing launcher, LocalTargetInfo usedTarget, LocalTargetInfo intendedTarget)
        {
            try
            {
                if (!PatchCommon.IsDmDef(__instance))
                {
                    return;
                }
                Log.Message("[RimTestMod.Patches] Projectile.Launch 补丁命中："
                            + __instance.def.defName
                            + " 由 " + (launcher != null ? launcher.LabelShortCap : "(无发射者)")
                            + " 发射 → used=" + usedTarget.ToString()
                            + " intended=" + intendedTarget.ToString()
                            + " 伤害=" + __instance.DamageAmount
                            + " 命中点=" + __instance.ExactPosition.ToString());
            }
            catch (Exception ex)
            {
                Log.Error("[RimTestMod.Patches] ProjectileLaunchPatch.Postfix 抛异常：" + ex);
            }
        }
    }
}
