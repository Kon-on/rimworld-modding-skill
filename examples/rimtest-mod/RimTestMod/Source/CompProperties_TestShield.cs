// AI 辅助生成 | 目标平台 RimWorld 1.7.4981 rev136 (net10.0)
// ---------------------------------------------------------------------------
// Demo.RimTestMod.CompProperties_TestShield
//   XML 侧写法（Defs\ThingDefs\Apparel.xml → DM_Apparel_TestVest）：
//     <li Class="Demo.RimTestMod.CompProperties_TestShield">
//       <shieldCapacity>50</shieldCapacity>
//     </li>
//   字段名 shieldCapacity 必须与本文件的公开字段名逐字一致（RimWorld 的 XML
//   加载器按字段名反射赋值，没有别名机制）。
//
// 1.7 实测契约（用 System.Reflection 读 Assembly-CSharp.dll 得到，非凭记忆）：
//   TYPE public class Verse.CompProperties : System.Object
//     FIELD  public System.Type compClass
//     CTOR   public .ctor()
//     METHOD public virtual System.Collections.Generic.IEnumerable<System.String>
//            ConfigErrors(Verse.ThingDef parentDef)
// ---------------------------------------------------------------------------
using System.Collections.Generic;
using Verse;

namespace Demo.RimTestMod
{
    /// <summary>测试用护盾的配置（对应 XML 的 comps 条目）。</summary>
    public class CompProperties_TestShield : CompProperties
    {
        /// <summary>护盾容量。契约字段名，XML 用 &lt;shieldCapacity&gt; 配置。</summary>
        public int shieldCapacity = 50;

        /// <summary>每恢复 1 点护盾需要经过的 tick 数（60 tick = 1 秒）。</summary>
        public int rechargeIntervalTicks = 120;

        /// <summary>每次恢复事件补多少点。</summary>
        public int rechargeAmount = 5;

        /// <summary>关掉后该 comp 完全不吸收伤害（便于做对照测试）。</summary>
        public bool absorbsDamage = true;

        /// <summary>低于此值的伤害不消耗护盾（避免鸡毛蒜皮的伤害把护盾刮没）。</summary>
        public float minimumAbsorbableDamage = 0.01f;

        public CompProperties_TestShield()
        {
            compClass = typeof(ThingComp_TestShield);
        }

        public override IEnumerable<string> ConfigErrors(ThingDef parentDef)
        {
            foreach (string e in base.ConfigErrors(parentDef))
            {
                yield return e;
            }
            if (shieldCapacity <= 0)
            {
                yield return "DM_CompProperties_TestShield: shieldCapacity 必须大于 0（当前 " + shieldCapacity + "）";
            }
            if (rechargeAmount < 0)
            {
                yield return "DM_CompProperties_TestShield: rechargeAmount 不能为负数（当前 " + rechargeAmount + "）";
            }
            if (rechargeAmount > 0 && rechargeIntervalTicks <= 0)
            {
                yield return "DM_CompProperties_TestShield: rechargeAmount > 0 时 rechargeIntervalTicks 必须大于 0";
            }
            if (rechargeAmount > shieldCapacity)
            {
                yield return "DM_CompProperties_TestShield: rechargeAmount 大于 shieldCapacity，单次恢复即满，疑似配置错误";
            }
        }
    }
}
