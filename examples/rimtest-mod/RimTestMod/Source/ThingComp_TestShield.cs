// AI 辅助生成 | 目标平台 RimWorld 1.7.4981 rev136 (net10.0)
// ---------------------------------------------------------------------------
// Demo.RimTestMod.ThingComp_TestShield —— 吸收伤害到容量耗尽，之后按时间恢复。
//
// 【为什么这个文件一行 UnityEngine 都不引用】
//   1.7 已经移除 Unity：游戏根目录没有任何 UnityEngine*.dll，
//   RimWorld.runtimeconfig.json 里 WaylithClr.AssemblyNameRedirects =
//   "UnityEngine*=UnityStubs;..."，UnityEngine 只剩 UnityStubs.dll 存根。
//   本 comp 只做纯计算，所以全程用 System.Math / 基元类型，主程序集因此
//   只依赖 Assembly-CSharp.dll，加载面最小。
//
// 【1.7 实测契约】（用 System.Reflection 读 Assembly-CSharp.dll，非凭记忆）
//   TYPE public class Verse.ThingComp : System.Object
//     FIELD  public Verse.ThingWithComps parent
//     FIELD  public Verse.CompProperties props
//     METHOD public virtual System.Void Initialize(Verse.CompProperties props)
//     METHOD public virtual System.Void PostExposeData()
//     METHOD public virtual System.Void CompTick()
//     METHOD public virtual System.String CompInspectStringExtra()
//     METHOD public virtual System.Collections.Generic.IEnumerable<Verse.Gizmo> CompGetGizmosExtra()
//     METHOD public virtual System.Void PostSpawnSetup(System.Boolean respawningAfterLoad)
//     METHOD public virtual System.Void PostPreApplyDamage(ref Verse.DamageInfo dinfo, out System.Boolean absorbed)
//   TYPE public struct Verse.DamageInfo
//     PROP   System.Single Amount { get; }        <-- 只读！改值只能调 SetAmount(float)
//     METHOD public System.Void SetAmount(System.Single newAmount)
//   TYPE public static class Verse.Scribe_Values
//     METHOD public static System.Void Look<T>(ref T value, System.String label, T defaultValue, System.Boolean forceSave = False)
//   TYPE public static class Verse.Translator
//     METHOD public static ext Verse.TaggedString Translate(System.String key)
//     METHOD public static ext System.String Translate(System.String key, System.Object[] args)
// ---------------------------------------------------------------------------
using System;
using System.Collections.Generic;
using RimWorld;
using Verse;

namespace Demo.RimTestMod
{
    /// <summary>
    /// 测试用护盾：先扣护盾点数，护盾扣光才伤到本体；脱战后按 rechargeIntervalTicks 逐点恢复。
    /// </summary>
    public class ThingComp_TestShield : ThingComp
    {
        /// <summary>本地化 Keyed 键（Languages\&lt;语言&gt;\Keyed\DM_Keys.xml）。</summary>
        public const string KeyInspect = "DM_TestShield_Inspect";

        /// <summary>护盾破盾时的提示键。</summary>
        public const string KeyDepleted = "DM_TestShield_Depleted";

        /// <summary>补满护盾的 gizmo 标签键。</summary>
        public const string KeyGizmoLabel = "DM_TestShield_GizmoRefillLabel";

        /// <summary>补满护盾的 gizmo 描述键。</summary>
        public const string KeyGizmoDesc = "DM_TestShield_GizmoRefillDesc";

        // -1 是「存档里没有这个字段」的哨兵值：读档后由 EnsureInitialized 补成满容量。
        // 用哨兵而不是直接把默认值写成 shieldCapacity，是为了区分「存档里明确存了 0」。
        private int shieldPoints = -1;
        private int ticksSinceAbsorb;
        private int totalAbsorbed;
        private int lastAbsorbTick = -1;
        private bool everDepleted;

        public CompProperties_TestShield ShieldProps
        {
            get { return props as CompProperties_TestShield; }
        }

        /// <summary>护盾容量；props 未就绪（读档早期）时返回 0，不抛异常。</summary>
        public int ShieldCapacity
        {
            get
            {
                CompProperties_TestShield p = ShieldProps;
                return p != null ? p.shieldCapacity : 0;
            }
        }

        /// <summary>当前护盾值（对外只读视图，负数当 0）。</summary>
        public int ShieldPoints
        {
            get { return shieldPoints < 0 ? 0 : shieldPoints; }
        }

        /// <summary>累计吸收掉的伤害量，仅用于测试观察。</summary>
        public int TotalAbsorbed
        {
            get { return totalAbsorbed; }
        }

        /// <summary>护盾是否还在挡伤害。</summary>
        public bool ShieldIsUp
        {
            get { return ShieldPoints > 0; }
        }

        /// <summary>护盾百分比 0..1，给 UI 用。</summary>
        public float ShieldPercent
        {
            get
            {
                int cap = ShieldCapacity;
                if (cap <= 0)
                {
                    return 0f;
                }
                return (float)ShieldPoints / (float)cap;
            }
        }

        // -------------------------------------------------------------------
        // 生命周期
        // -------------------------------------------------------------------

        public override void Initialize(CompProperties props)
        {
            base.Initialize(props);
            EnsureInitialized();
        }

        public override void PostSpawnSetup(bool respawningAfterLoad)
        {
            base.PostSpawnSetup(respawningAfterLoad);
            EnsureInitialized();
        }

        /// <summary>把未初始化的护盾补成满容量，并夹到 [0, capacity]。</summary>
        private void EnsureInitialized()
        {
            int cap = ShieldCapacity;
            if (shieldPoints < 0)
            {
                shieldPoints = cap;
            }
            if (cap > 0 && shieldPoints > cap)
            {
                shieldPoints = cap;
            }
        }

        // -------------------------------------------------------------------
        // 存档
        // -------------------------------------------------------------------

        public override void PostExposeData()
        {
            base.PostExposeData();
            // 默认值给 -1（哨兵）而不是 ShieldCapacity：读档时 props 可能还没接上，
            // 此时 ShieldCapacity 返回 0，若拿它当默认值会把老存档的护盾静默清零。
            Scribe_Values.Look(ref shieldPoints, "DM_ShieldPoints", -1);
            Scribe_Values.Look(ref ticksSinceAbsorb, "DM_ShieldTicksSinceAbsorb", 0);
            Scribe_Values.Look(ref totalAbsorbed, "DM_ShieldTotalAbsorbed", 0);
            Scribe_Values.Look(ref lastAbsorbTick, "DM_ShieldLastAbsorbTick", -1);
            Scribe_Values.Look(ref everDepleted, "DM_ShieldEverDepleted", false);

            if (Scribe.mode == LoadSaveMode.PostLoadInit)
            {
                EnsureInitialized();
            }
        }

        // -------------------------------------------------------------------
        // 吸收伤害
        // -------------------------------------------------------------------

        public override void PostPreApplyDamage(ref DamageInfo dinfo, out bool absorbed)
        {
            base.PostPreApplyDamage(ref dinfo, out absorbed);
            if (absorbed)
            {
                return; // 上游已经拦下这份伤害（例如别的护盾 comp）
            }

            CompProperties_TestShield p = ShieldProps;
            if (p == null || !p.absorbsDamage)
            {
                return;
            }

            EnsureInitialized();

            float amount = dinfo.Amount;
            if (amount <= 0f || amount < p.minimumAbsorbableDamage)
            {
                return;
            }

            // 不引用 UnityEngine.Mathf，纯 System 计算
            int wanted = (int)Math.Ceiling((double)amount);
            if (wanted <= 0)
            {
                return;
            }

            if (ShieldIsUp)
            {
                int absorbedNow = wanted < ShieldPoints ? wanted : ShieldPoints;
                shieldPoints -= absorbedNow;
                totalAbsorbed += absorbedNow;
                ticksSinceAbsorb = 0;
                lastAbsorbTick = (parent != null && parent.Map != null) ? Find.TickManager.TicksGame : -1;

                float remaining = amount - absorbedNow;
                if (remaining <= 0f)
                {
                    // 完全吸收：把伤害归零并告诉调用方「已被吸收」，原版就不会再走掉血逻辑
                    dinfo.SetAmount(0f);
                    absorbed = true;
                }
                else
                {
                    // 部分吸收：只削减伤害数值，剩下的照常打在本体上
                    dinfo.SetAmount(remaining);
                }

                if (!ShieldIsUp && !everDepleted)
                {
                    everDepleted = true;
                    // 1.7 实测签名（System.Reflection 读出）：
                    //   public static System.Void Verse.Messages.Message(System.String text,
                    //       Verse.LookTargets lookTargets, Verse.MessageTypeDef def, System.Boolean historical = True)
                    // 注意两点：
                    //   1) MessageTypeDefOf 的 namespace 是 RimWorld（RimWorld.dll），不是 Verse；
                    //   2) 第二个参数是 LookTargets 而不是 Thing，靠 op_Implicit(Thing) 隐式转过去。
                    if (Translator.CanTranslate(KeyDepleted))
                    {
                        Messages.Message(KeyDepleted.Translate(), new LookTargets(parent), MessageTypeDefOf.NeutralEvent, false);
                    }
                }
            }
        }

        // -------------------------------------------------------------------
        // 恢复
        // -------------------------------------------------------------------

        public override void CompTick()
        {
            base.CompTick();
            EnsureInitialized();

            CompProperties_TestShield p = ShieldProps;
            if (p == null || p.rechargeAmount <= 0)
            {
                return;
            }
            if (shieldPoints >= p.shieldCapacity)
            {
                ticksSinceAbsorb = 0;
                return;
            }

            ticksSinceAbsorb++;
            if (ticksSinceAbsorb < p.rechargeIntervalTicks)
            {
                return;
            }

            ticksSinceAbsorb = 0;
            shieldPoints += p.rechargeAmount;
            if (shieldPoints > p.shieldCapacity)
            {
                shieldPoints = p.shieldCapacity;
            }
        }

        // -------------------------------------------------------------------
        // 界面
        // -------------------------------------------------------------------

        public override string CompInspectStringExtra()
        {
            EnsureInitialized();
            return KeyInspect.Translate(ShieldPoints, ShieldCapacity, totalAbsorbed);
        }

        public override IEnumerable<Gizmo> CompGetGizmosExtra()
        {
            foreach (Gizmo g in base.CompGetGizmosExtra())
            {
                yield return g;
            }

            yield return new Command_Action
            {
                defaultLabel = KeyGizmoLabel.Translate(),
                defaultDesc = KeyGizmoDesc.Translate(),
                action = delegate
                {
                    Refill();
                    Log.Message("[RimTestMod] DM_Apparel_TestVest 护盾已被测试 gizmo 补满："
                                + ShieldPoints + "/" + ShieldCapacity);
                }
            };
        }

        /// <summary>把护盾补满（gizmo 与调试用）。</summary>
        public void Refill()
        {
            EnsureInitialized();
            shieldPoints = ShieldCapacity;
            ticksSinceAbsorb = 0;
        }

        /// <summary>把护盾清零（调试用）。</summary>
        public void Drain()
        {
            EnsureInitialized();
            shieldPoints = 0;
            ticksSinceAbsorb = 0;
        }
    }
}
