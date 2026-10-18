> ✅ **核对状态：本页用到的类型与成员签名，已用反射对 1.7 游戏目录里的 DLL 逐条核对（0 处不存在、0 处签名不符；命令与原始输出见 `04-核验/C#接口核对结果.md`）；运行期行为未实机验证。**
>
> 核对目标（本机实测）：`Assembly-CSharp.dll` 版本 **1.7.9786.4087**、**16,221** 个类型；`UnityStubs.dll` **934** 个类型 / **6,653** 个方法，其中 **254** 个方法是 stub（分布在 88 个类型，清单见 `07-附录-UnityStubs失效成员清单.md`）；`0Harmony.dll` **3.0.0.0**（2,326 个类型，来自创意工坊 mod 2009463077）。
>
> 1.7 环境要点：目标框架 **net10.0**；**UnityEngine.\* 由 UnityStubs.dll 提供**（真兼容层，stub 只记警告并返回默认值、**不抛异常**）；**Harmony 不在游戏内**，须声明依赖 mod 2009463077 或自带 0Harmony.dll。
>
> csproj 要点：`<TargetFramework>net10.0</TargetFramework>`；引用游戏根目录的 `Assembly-CSharp.dll` 与 `UnityStubs.dll`（Private=false）；**不要引用 `UnityEngine.*.dll`**（1.7 已无这些文件）；依赖的第三方 DLL 必须一起放进 `Assemblies\`（否则整个 DLL 会被拒载并打印 "Loader exceptions:"）。


# ThingComp 与 HediffComp

## 用途

**Comp 是往已有物件上挂行为的标准方式**：不新建 Def 类，而是给任意 ThingDef / HediffDef / AbilityDef 挂一个组件。组件分两半：**Properties 类**（只放数据，XML 里写它）与 **Comp 类**（放逻辑）。

**典型用途**：给物品加「用一次就消耗」、给建筑加「自动发电」、给状态加「到时间自动消失」。

## 代码

```csharp
using Verse;

namespace ExampleMod
{
    // ---------- ThingComp ----------
    public class CompProperties_ExampleGlow : CompProperties
    {
        public float radius = 5f;
        public int tickInterval = 120;

        public CompProperties_ExampleGlow()
        {
            compClass = typeof(CompExampleGlow);
        }
    }

    public class CompExampleGlow : ThingComp
    {
        private int ticks;
        public CompProperties_ExampleGlow Props => (CompProperties_ExampleGlow)props;

        public override void CompTick()
        {
            ticks++;
            if (ticks < Props.tickInterval) return;
            ticks = 0;
            // 在这里做周期性逻辑
        }

        public override void PostExposeData()
        {
            base.PostExposeData();
            Scribe_Values.Look(ref ticks, "ticks", 0);
        }
    }

    // ---------- HediffComp ----------
    public class HediffCompProperties_ExampleFade : HediffCompProperties
    {
        public int ticksToDisappear = 60000;

        public HediffCompProperties_ExampleFade()
        {
            compClass = typeof(HediffCompExampleFade);
        }
    }

    public class HediffCompExampleFade : HediffComp
    {
        private int ticks;
        public HediffCompProperties_ExampleFade Props => (HediffCompProperties_ExampleFade)props;

        public override void CompPostTick(ref float severityAdjustment)
        {
            ticks++;
            if (ticks >= Props.ticksToDisappear) parent.pawn.health.RemoveHediff(parent);
        }

        public override void CompExposeData()
        {
            base.CompExposeData();
            Scribe_Values.Look(ref ticks, "ticks", 0);
        }
    }
}
```

对应的 XML：

```xml
<!-- ThingComp：写在任意 ThingDef 的 comps 里 -->
<comps>
  <li Class="ExampleMod.CompProperties_ExampleGlow">
    <radius>6</radius>
    <tickInterval>90</tickInterval>
  </li>
</comps>

<!-- HediffComp：写在 HediffDef 的 comps 里（需要 hediffClass 支持 comp） -->
<comps>
  <li Class="ExampleMod.HediffCompProperties_ExampleFade">
    <ticksToDisappear>30000</ticksToDisappear>
  </li>
</comps>
```

## 常见坑

- **Properties 的构造函数里必须设置 `compClass`**，否则 XML 里只能写数据、游戏不知道怎么实例化逻辑类。
- **XML 里写的是 Properties 类的完整名**（`CompProperties_ExampleGlow`），不是逻辑类名。
- **需要存盘的字段一律用 `Scribe_Values.Look` 写进 `PostExposeData` / `CompExposeData`**，否则读档后重置。
- **Hediff 要能用 comp，HediffDef 必须写 `hediffClass` 为 `HediffWithComps` 或其子类**。
- **每 Tick 的逻辑要自己控制频率**：comp 的 Tick 是每帧级调用，重逻辑必须按 `tickInterval` 节流，否则会明显掉帧。

## 核验

本页用到的每个类型与成员，都已用反射对 1.7 的 DLL 逐条核对（原始输出见 `04-核验/C#接口核对结果.md`）：

| 本页用到 | 1.7 实际签名（机器核对） |
|---|---|
| `Verse.CompProperties` | 只有 1 个字段：`public Type compClass` —— 所以构造函数里必须自己赋值 |
| `Verse.ThingComp` | 字段 `public CompProperties props`；方法 `public virtual void Initialize(CompProperties)`、`public virtual void CompTick()`、`public virtual void CompTickInterval(int delta)`、`public virtual void CompTickRare()`、`public virtual void CompTickLong()`、`public virtual void PostExposeData()` |
| `Verse.HediffComp` | 字段 `public HediffWithComps parent`、`public HediffCompProperties props`；方法 `public virtual void CompPostTick(ref float severityAdjustment)`、`public virtual void CompPostTickInterval(ref float, int delta)`、`public virtual void CompExposeData()` |
| `Verse.Hediff`（parent 的基类） | 字段 `public Pawn pawn`、`public float severityInt`；属性 `public float Severity { get; }` |
| `Verse.Pawn_HealthTracker.RemoveHediff` | `public void RemoveHediff(Hediff hediff)` |
| `Verse.Pawn.health` | 字段 `public Pawn_HealthTracker health` |

所以模板里的 `parent.pawn.health.RemoveHediff(parent)` 三段链路全部核对通过：`parent` 的静态类型就是 `HediffWithComps`（它的基类是 `Hediff`），可以传入 `RemoveHediff(Hediff)`。

**1.7 新发现**：Comp 家族多了 `CompTickInterval(int delta)` / `CompPostTickInterval(ref float, int delta)` 两个可按间隔调用的入口。模板仍用 `CompTick` + 自己计数（兼容性更好、行为最可预期），要做省性能的高频组件可以改走新入口。

**结论**：0 处不存在、0 处签名不符。保留的未知项是运行期行为（组件被实例化/回收的时机、`CompTickInterval` 的实际调用频率）——本页未实机验证。
