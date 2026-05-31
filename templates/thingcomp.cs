// ThingComp 模板
// 替换 <YourNamespace> 和 <YourPrefix> 为实际值
// 使用方法：
//   1. 重命名 CompProperties_xxx 和 Comp_xxx 为你的类名
//   2. 在 CompProperties 中添加自定义数据字段
//   3. 在 ThingComp 中实现行为逻辑
//   4. 在 XML Def 的 <comps> 中引用 CompProperties_xxx

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
    }
}
