// ThingComp 模板（RimWorld 1.7）
// 验证状态：已验证（生命周期方法名对照原版 1.7 ThingComp：PostSpawnSetup / CompTick /
//            PostExposeData / CompInspectStringExtra / CompGetGizmosExtra；本模板所依据的
//            同类实现已在 1.7.4981 上真机编译为 DLL——见
//            examples/rimtest-mod/RimTestMod/Source/ThingComp_TestShield.cs）
// AI 辅助生成
// 替换 <YourNamespace> 和 <YourPrefix> 为实际值
// 使用方法：
//   1. 重命名 CompProperties_xxx 和 Comp_xxx 为你的类名
//   2. 在 CompProperties 中添加自定义数据字段
//   3. 在 ThingComp 中实现行为逻辑
//   4. 在 XML Def 的 <comps> 中引用 CompProperties_xxx
//
// 1.7 注意：
//   · 目标框架 net10.0，引用游戏安装根目录的 Assembly-CSharp.dll（见 references/01-environment.md）
//   · 存读档覆写的是 PostExposeData()，不是 ExposeData()——本模板已如此
//   · Scribe_Values.Look 的 key 字符串**不要改名**（改了就等于老存档读不到这些字段）
//   · 只在需要高响应时才用 CompTick()；能低频就用 CompTickRare() / CompTickLong()

using Verse;

namespace <YourNamespace>
{
    /// <summary>
    /// CompProperties：在 XML 中定义的数据字段
    /// 每个 CompProperties 类必须在 XML 中用 Class="CompProperties_xxx" 引用
    /// </summary>
    public class CompProperties_<YourPrefix>Custom : CompProperties
    {
        // 自定义数据字段——可在 XML 中配置
        public float customValue = 1.0f;
        public int tickInterval = 60;  // 每 60 ticks 执行一次（约 1 秒）
        public bool enableOnSpawn = true;

        public CompProperties_<YourPrefix>Custom()
        {
            // 必须设置为对应的 ThingComp 类
            compClass = typeof(Comp<YourPrefix>Custom);
        }
    }

    /// <summary>
    /// ThingComp：实现运行时行为
    /// </summary>
    public class Comp<YourPrefix>Custom : ThingComp
    {
        // 便捷的属性访问器
        public CompProperties_<YourPrefix>Custom Props => (CompProperties_<YourPrefix>Custom)props;

        // 内部状态
        private int tickCounter;
        private bool isActive;

        /// <summary>
        /// 生成后的初始化
        /// </summary>
        public override void PostSpawnSetup(bool respawningAfterLoad)
        {
            base.PostSpawnSetup(respawningAfterLoad);

            if (!respawningAfterLoad && Props.enableOnSpawn)
            {
                isActive = true;
            }
        }

        /// <summary>
        /// 每 tick 执行（仅当需要高响应性时使用）
        /// 大多数情况用 CompTickRare 或 CompTickLong 更好
        /// </summary>
        public override void CompTick()
        {
            base.CompTick();

            if (!isActive || !parent.Spawned) return;

            tickCounter++;
            if (tickCounter >= Props.tickInterval)
            {
                tickCounter = 0;
                DoTickAction();
            }
        }

        /// <summary>
        /// 按 tickInterval 间隔执行的自定义逻辑
        /// </summary>
        private void DoTickAction()
        {
            // TODO: 在此编写周期性逻辑
            // 示例：消耗电池能量
            // var battery = parent.GetComp<CompPowerBattery>();
            // battery?.DrawPower(Props.customValue);
        }

        /// <summary>
        /// 存档/读档
        /// </summary>
        public override void PostExposeData()
        {
            base.PostExposeData();
            Scribe_Values.Look(ref tickCounter, "tickCounter", 0);
            Scribe_Values.Look(ref isActive, "isActive", false);
        }

        /// <summary>
        /// 获取调试检查字符串（在开发者模式中显示）
        /// </summary>
        public override string CompInspectStringExtra()
        {
            if (!isActive) return "Inactive";
            return $"Active | Custom Value: {Props.customValue:F1} | Ticks: {tickCounter}/{Props.tickInterval}";
        }

        /// <summary>
        /// 给物品加命令按钮（可选）。
        /// 1.7 实测：Command_Action 在 Verse 命名空间（不是 RimWorld）。
        /// 图片可用 TexCommand.ForbidOff 等原版图标，或用 ContentFinder&lt;Texture2D&gt;.Get("UI/Commands/Xxx")。
        /// </summary>
        // public override IEnumerable<Gizmo> CompGetGizmosExtra()
        // {
        //     foreach (var g in base.CompGetGizmosExtra()) yield return g;
        //     yield return new Command_Action
        //     {
        //         defaultLabel = "Do something",
        //         defaultDesc = "Testing only.",
        //         icon = TexCommand.ForbidOff,
        //         action = () => { isActive = !isActive; }
        //     };
        // }
    }
}
