// AI 辅助生成 | 目标平台 RimWorld 1.7.4981 rev136 (net10.0)
// Patches 子程序集 Demo.RimTestMod.Patches 的公共小工具。
using System;
using System.Reflection;
using Verse;

namespace Demo.RimTestMod.Patches
{
    internal static class PatchCommon
    {
        /// <summary>只对 DM_ 前缀的 def 记日志，否则整个游戏的子弹/伤害都会刷屏。</summary>
        internal static bool IsDmDef(Thing t)
        {
            if (t == null || t.def == null)
            {
                return false;
            }
            string n = t.def.defName;
            return n != null && n.StartsWith("DM_", StringComparison.Ordinal);
        }

        /// <summary>把反射拿到的 MethodBase 还原成一行可读签名，写进日志便于核对。</summary>
        internal static string Describe(MethodBase m)
        {
            if (m == null)
            {
                return "(null)";
            }
            try
            {
                ParameterInfo[] ps = m.GetParameters();
                string[] parts = new string[ps.Length];
                for (int i = 0; i < ps.Length; i++)
                {
                    parts[i] = ps[i].ParameterType.FullName + " " + ps[i].Name;
                }
                string ret = (m is MethodInfo mi && mi.ReturnType != null) ? mi.ReturnType.FullName + " " : "";
                return ret + (m.DeclaringType != null ? m.DeclaringType.FullName : "?") + "." + m.Name + "(" + string.Join(", ", parts) + ")";
            }
            catch (Exception ex)
            {
                return m.Name + " <签名读取失败: " + ex.GetType().Name + ">";
            }
        }

        internal static string SafeLog(string tag, string body)
        {
            return tag + body;
        }
    }
}
