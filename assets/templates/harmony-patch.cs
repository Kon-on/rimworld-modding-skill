// Harmony 补丁模板
// AI 辅助生成
// 替换 <YourNamespace> 和 <YourModID> 为你的实际值
// 使用方法：
//   1. 替换 TargetClass 为目标类名（用 dnSpy 或 RimSage 查找）
//   2. 替换 TargetMethod 为目标方法名
//   3. 根据需要选择 Prefix / Postfix / Transpiler
//   4. 实现你的 patch 逻辑

using Verse;
using HarmonyLib;
using System.Reflection;

namespace <YourNamespace>
{
    /// <summary>
    /// Harmony 补丁入口——游戏启动时自动加载所有补丁
    /// </summary>
    [StaticConstructorOnStartup]
    public static class HarmonyPatches
    {
        private static readonly Harmony instance;

        static HarmonyPatches()
        {
            // Harmony ID 必须全局唯一，建议使用 packageId 格式
            instance = new Harmony("<YourModID>");
            instance.PatchAll(Assembly.GetExecutingAssembly());
            Log.Message("<YourModID>: All Harmony patches applied successfully.");
        }
    }

    /// <summary>
    /// 示例：对 TargetClass.TargetMethod 进行 Prefix 拦截
    /// </summary>
    // [HarmonyPatch(typeof(TargetClass), "TargetMethod")]
    public static class Patch_TargetClass_TargetMethod
    {
        /// <summary>
        /// Prefix：在原方法执行前运行
        /// 返回 false = 跳过原方法
        /// 返回 true  = 继续执行原方法
        /// </summary>
        [HarmonyPrefix]
        public static bool Prefix(/* 原始参数列表 */)
        {
            // TODO: 在此编写前置逻辑

            return true;  // 允许原方法继续执行
        }

        /// <summary>
        /// Postfix：在原方法执行后运行
        /// 可以读取和修改 __result（原方法的返回值）
        /// </summary>
        // [HarmonyPostfix]
        // public static void Postfix(/* 原始参数列表 */, ref <ReturnType> __result)
        // {
        //     // TODO: 在此编写后置逻辑
        // }

        /// <summary>
        /// Transpiler：直接修改 IL 代码（高级用法）
        /// </summary>
        // [HarmonyTranspiler]
        // public static IEnumerable<CodeInstruction> Transpiler(IEnumerable<CodeInstruction> instructions)
        // {
        //     // TODO: 在此编写 IL 修改逻辑
        //     return instructions;
        // }
    }
}
