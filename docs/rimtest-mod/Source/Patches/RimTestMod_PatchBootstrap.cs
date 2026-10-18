// AI 辅助生成 | 目标平台 RimWorld 1.7.4981 rev136 (net10.0)
// ---------------------------------------------------------------------------
// RimTestMod.Patches 的引导入口。
//
// 为什么不用 Harmony.PatchAll：
//   PatchAll 要求补丁类挂 [HarmonyPatch] 特性，目标方法签名写在特性里；
//   一旦签名对不上，PatchAll 会直接抛异常，整个引导中断。这里改成
//   AccessTools.Method 逐条取目标、逐条 Patch，取不到就 Log.Error 后继续，
//   这样「某个目标方法在本版本改名」不会连带废掉其他补丁。
//
// 为什么套 [MethodImpl(MethodImplOptions.NoInlining)]：
//   本类是 0Harmony 的使用方，如果不隔离，JIT 编译外层方法时就要解析
//   HarmonyLib 类型；万一 Harmony mod 没启用，异常会发生在 catch 之外。
//   放进单独不内联的方法里，缺 0Harmony 时异常一定落在 try/catch 内，游戏
//   只会看到一条红色错误日志，不会因为缺依赖而丢整个 DLL。
//
// 关于「补丁 ID」：Harmony 3.0 的 HarmonyMethod 里【没有】id 字段（2.x 的补丁 ID
// 概念被 category/switch 机制取代，实测字段表：method / methodName / declaringType /
// argumentTypes / priority / category / debug / before / after / methodType /
// infixOuterBody / innerMethod / innerTarget / nonVirtualDelegate /
// uncheckedReferenceBinding / reversePatchType）。所以这里用
// 「唯一 Harmony 实例 ID + 唯一补丁类名 + 每个补丁类自带 public const string PatchId」
// 来表达补丁身份。没有设置 category：category 与 switch 挂钩，可能影响补丁默认是否
// 生效，在不能启动游戏的验证环境里无法证实，故不用。
// ---------------------------------------------------------------------------
using System;
using System.Collections.Generic;
using System.Reflection;
using System.Runtime.CompilerServices;
using HarmonyLib;
using Verse;

namespace Demo.RimTestMod.Patches
{
    [StaticConstructorOnStartup]
    public static class RimTestMod_PatchBootstrap
    {
        public const string HarmonyId = "test.rimtestmod.patches";

        private const string Tag = "[RimTestMod.Patches] ";

        /// <summary>实际打上去的补丁数量，供外部（含测试 mod 的其它部分）查证。</summary>
        public static int AppliedCount { get; private set; }

        /// <summary>失败条数。</summary>
        public static int FailedCount { get; private set; }

        /// <summary>一行状态，供调试面板显示。</summary>
        public static string Status { get; private set; } = "尚未运行";

        static RimTestMod_PatchBootstrap()
        {
            try
            {
                Run();
            }
            catch (Exception ex)
            {
                Status = "引导失败：" + ex.GetType().Name;
                FailedCount = -1;
                Log.Error(Tag + "Harmony 引导失败，补丁未生效（Harmony mod 是否启用 / 是否为本版本？）：" + ex);
            }
        }

        [MethodImpl(MethodImplOptions.NoInlining)]
        private static void Run()
        {
            Assembly harmonyAsm = typeof(Harmony).Assembly;
            AssemblyName harmonyName = harmonyAsm.GetName();
            Log.Message(Tag + "0Harmony = " + harmonyName.Name + " v" + harmonyName.Version
                        + " 文件 " + SafeLocation(harmonyAsm));

            Harmony harmony = new Harmony(HarmonyId);

            // ---- 1) Verse.Projectile.Launch —— 8 参数重载（故意带 UnityEngine.Vector3） ----
            Type[] launchArgs = new Type[]
            {
                typeof(Thing), typeof(UnityEngine.Vector3), typeof(LocalTargetInfo), typeof(LocalTargetInfo),
                typeof(ProjectileHitFlags), typeof(bool), typeof(Thing), typeof(ThingDef)
            };
            MethodInfo launchTarget = AccessTools.Method(typeof(Projectile), "Launch", launchArgs, null);
            Apply(harmony, ProjectileLaunchPatch.PatchId, launchTarget,
                  null, AccessTools.Method(typeof(ProjectileLaunchPatch), "Postfix", null, null));

            // ---- 2) Verse.Projectile.Impact —— protected virtual ----
            Type[] impactArgs = new Type[] { typeof(Thing), typeof(bool) };
            MethodInfo impactTarget = AccessTools.Method(typeof(Projectile), "Impact", impactArgs, null);
            Apply(harmony, ProjectileImpactPatch.PatchId, impactTarget,
                  null, AccessTools.Method(typeof(ProjectileImpactPatch), "Postfix", null, null));

            // ---- 3) Verse.Thing.TakeDamage —— 非 virtual，Prefix 记血量 ----
            Type[] takeDamageArgs = new Type[] { typeof(DamageInfo) };
            MethodInfo takeDamageTarget = AccessTools.Method(typeof(Thing), "TakeDamage", takeDamageArgs, null);
            Apply(harmony, ThingTakeDamagePatch.PatchId, takeDamageTarget,
                  AccessTools.Method(typeof(ThingTakeDamagePatch), "Prefix", null, null),
                  AccessTools.Method(typeof(ThingTakeDamagePatch), "Postfix", null, null));

            int reported = 0;
            foreach (MethodBase mb in harmony.GetPatchedMethods())
            {
                reported++;
                Log.Message(Tag + "Harmony 自报已修补：" + PatchCommon.Describe(mb));
            }

            Status = "成功 " + AppliedCount + " / 失败 " + FailedCount + " / Harmony 自报 " + reported;
            Log.Message(Tag + "补丁引导结束：" + Status);
        }

        private static void Apply(Harmony harmony, string patchId, MethodInfo target, MethodInfo prefix, MethodInfo postfix)
        {
            if (target == null)
            {
                FailedCount++;
                Log.Error(Tag + "找不到补丁目标，已跳过 " + patchId
                          + "；请用程序集元数据核对目标签名是否随版本变化。");
                return;
            }
            if (prefix == null && postfix == null)
            {
                FailedCount++;
                Log.Error(Tag + "补丁方法反射失败，已跳过 " + patchId + "（补丁类可能没编译进程序集）。");
                return;
            }
            try
            {
                HarmonyMethod pre = prefix != null ? new HarmonyMethod(prefix) : null;
                HarmonyMethod post = postfix != null ? new HarmonyMethod(postfix) : null;
                if (pre != null)
                {
                    pre.priority = Priority.Normal;
                }
                if (post != null)
                {
                    post.priority = Priority.Normal;
                }
                // 显式转型 + 位置实参：绕开 Harmony 里可能存在的同名 string 重载带来的歧义。
                harmony.Patch((MethodBase)target, (HarmonyMethod)pre, (HarmonyMethod)post,
                              (HarmonyMethod)null, (HarmonyMethod)null);
                AppliedCount++;
                Log.Message(Tag + "已打补丁 " + patchId + " → " + PatchCommon.Describe(target));
            }
            catch (Exception ex)
            {
                FailedCount++;
                Log.Error(Tag + "补丁失败 " + patchId + " → " + PatchCommon.Describe(target) + "：" + ex);
            }
        }

        private static string SafeLocation(Assembly asm)
        {
            try
            {
                return asm.Location;
            }
            catch (Exception)
            {
                return "(内存程序集，无路径)";
            }
        }
    }
}
