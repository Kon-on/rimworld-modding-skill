> ✅ **核对状态：本页用到的类型与成员签名，已用反射对 1.7 游戏目录里的 DLL 逐条核对（0 处不存在、0 处签名不符；命令与原始输出见 `04-核验/C#接口核对结果.md`）；运行期行为未实机验证。**
>
> 核对目标（本机实测）：`Assembly-CSharp.dll` 版本 **1.7.9786.4087**、**16,221** 个类型；`UnityStubs.dll` **934** 个类型 / **6,653** 个方法，其中 **254** 个方法是 stub（分布在 88 个类型，清单见 `07-附录-UnityStubs失效成员清单.md`）；`0Harmony.dll` **3.0.0.0**（2,326 个类型，来自创意工坊 mod 2009463077）。
>
> 1.7 环境要点：目标框架 **net10.0**；**UnityEngine.\* 由 UnityStubs.dll 提供**（真兼容层，stub 只记警告并返回默认值、**不抛异常**）；**Harmony 不在游戏内**，须声明依赖 mod 2009463077 或自带 0Harmony.dll。
>
> csproj 要点：`<TargetFramework>net10.0</TargetFramework>`；引用游戏根目录的 `Assembly-CSharp.dll` 与 `UnityStubs.dll`（Private=false）；**不要引用 `UnityEngine.*.dll`**（1.7 已无这些文件）；依赖的第三方 DLL 必须一起放进 `Assemblies\`（否则整个 DLL 会被拒载并打印 "Loader exceptions:"）。


# JobDriver 与 WorkGiver

## 用途

让小人**做一件新事情**需要两个类：**WorkGiver**（扫描地图，找到该干的事，生成 Job）与 **JobDriver**（把 Job 拆成一串可执行的小步骤 Toil）。

XML 侧对应 `WorkGiverDef`（挂到工作类型）与 `JobDef`（声明行为）。

**典型用途**：做新工作、做新自动化行为。

## 代码

```csharp
using System.Collections.Generic;
using RimWorld;    // WorkGiver_Scanner、ForbidUtility(IsForbidden) 都在这里
using Verse;
using Verse.AI;    // ReservationUtility / ToilFailConditions / ToilEffects 在这里

namespace ExampleMod
{
    // ---------- WorkGiver：找活 ----------
    public class WorkGiver_ExampleForge : WorkGiver_Scanner
    {
        public override ThingRequest PotentialWorkThingRequest =>
            ThingRequest.ForDef(ThingDef.Named("EXAMPLE_Workbench"));

        public override PathEndMode PathEndMode => PathEndMode.InteractionCell;

        public override bool HasJobOnThing(Pawn pawn, Thing t, bool forced = false)
        {
            if (!pawn.CanReserve(t)) return false;
            if (t.IsForbidden(pawn)) return false;
            return true;
        }

        public override Job JobOnThing(Pawn pawn, Thing t, bool forced = false)
        {
            return JobMaker.MakeJob(JobDef.Named("EXAMPLE_CraftAtForge"), t);
        }
    }

    // ---------- JobDriver：干活 ----------
    public class JobDriver_ExampleCraft : JobDriver
    {
        private const TargetIndex BenchInd = TargetIndex.A;

        public override bool TryMakePreToilReservations(bool errorOnFailed)
            => pawn.Reserve(job.targetA, job, 1, -1, null, errorOnFailed);

        protected override IEnumerable<Toil> MakeNewToils()
        {
            this.FailOnDespawnedNullOrForbidden(BenchInd);

            // 1. 走到工作台
            yield return Toils_Goto.GotoThing(BenchInd, PathEndMode.InteractionCell);

            // 2. 原地工作若干 Tick
            Toil work = ToilMaker.MakeToil("ExampleCraft");
            work.tickAction = () => { /* 每个 Tick 的工作内容 */ };
            work.defaultCompleteMode = ToilCompleteMode.Delay;
            work.defaultDuration = 600;
            work.WithProgressBar(BenchInd, () => 1f - (float)ticksLeftThisToil / 600);
            yield return work;
        }
    }
}
```

配合的 XML：

```xml
<WorkGiverDef>
  <defName>EXAMPLE_DoForgeBills</defName>
  <label>锻造</label>
  <gerund>正在锻造</gerund>
  <verb>锻造</verb>
  <giverClass>ExampleMod.WorkGiver_ExampleForge</giverClass>
  <workType>EXAMPLE_Forge</workType>
  <priorityInType>300</priorityInType>
</WorkGiverDef>

<JobDef>
  <defName>EXAMPLE_CraftAtForge</defName>
  <driverClass>ExampleMod.JobDriver_ExampleCraft</driverClass>
  <reportString>正在锻造。</reportString>
</JobDef>
```

## 常见坑

- **WorkGiver 与 JobDriver 是配套的**：只有 WorkGiver 没有 Driver，小人会一直想做但做不出来。
- **`PotentialWorkThingRequest` 决定扫描成本**：写成 `ThingRequest.ForGroup` 这种宽泛条件会让性能明显下降。
- **每个 Toil 都要考虑失败处理**（`FailOnDespawnedNullOrForbidden` 等），否则目标消失时小人会卡住。
- **`TryMakePreToilReservations` 返回 false 时工作会被放弃**，预约失败必须正确返回。
- **`using RimWorld;` 不能省**：`WorkGiver_Scanner` 在 `RimWorld` 命名空间（不是 `Verse.AI`）；`t.IsForbidden(pawn)` 是 `RimWorld.ForbidUtility` 上的扩展方法。
- **XML 里的 `giverClass` / `driverClass` 要写命名空间全名**。

## 核验

本页用到的每个类型与成员，都已用反射对 1.7 的 DLL 逐条核对（原始输出见 `04-核验/C#接口核对结果.md`）。核对过程中改了模板三处，都是"编译不过"级别的真问题：

| # | 原稿 | 核对结果 | 处理 |
|---|---|---|---|
| 1 | 只写 `using Verse.AI;` | `WorkGiver_Scanner` 的真实名称是 **`RimWorld.WorkGiver_Scanner`**（基类 `RimWorld.WorkGiver`，字段 `WorkGiverDef def`）；`IsForbidden` 是 `RimWorld.ForbidUtility` 的扩展方法 | 代码已补 **`using RimWorld;`** |
| 2 | 把 `FailOnDespawnedNullOrForbidden` / `WithProgressBar` 当普通方法 | 它们是 **`Verse.AI` 命名空间下 `ToilFailConditions` / `ToilEffects` 两个静态扩展类**的方法 | 命名空间已核实（`using Verse.AI;` 已覆盖），无需改代码 |
| 3 | `Toils_Goto.GotoThing(ind, PathEndMode.InteractionCell)`（2 参） | 真实签名 `GotoThing(TargetIndex ind, PathEndMode peMode, bool canGotoSpawnedParent = true)`，第三参**有默认值** | 合法，无需改 |

核对到的关键签名：

| 本页用到 | 1.7 实际签名（机器核对） |
|---|---|
| `RimWorld.WorkGiver_Scanner` | 属性 `ThingRequest PotentialWorkThingRequest`、`PathEndMode PathEndMode`；方法 `bool HasJobOnThing(Pawn pawn, Thing t, bool forced = false)`、`Job JobOnThing(Pawn pawn, Thing t, bool forced = false)`（还有 `MaxPathDanger`、`HasJobOnCell`、`JobOnCell`、`GetPriority`、`PotentialWorkThingsGlobal` 等，均为 `public virtual`） |
| `Verse.AI.ReservationUtility`（静态扩展） | `static bool CanReserve(Pawn p, LocalTargetInfo target, int maxPawns = 1, int stackCount = -1, ReservationLayerDef layer = null, bool ignoreOtherReservations = false)`；`static bool Reserve(Pawn p, LocalTargetInfo target, Job job, int maxPawns = 1, int stackCount = -1, ReservationLayerDef layer = null, bool errorOnFailed = false, bool ignoreOtherReservations = false)` |
| `RimWorld.ForbidUtility`（静态扩展） | `static bool IsForbidden(Thing t, Pawn pawn)`、`IsForbidden(IntVec3 c, Pawn pawn)`、`IsForbidden(Thing t, Faction faction)` |
| `Verse.AI.ToilFailConditions`（静态扩展） | `static T FailOnDespawnedNullOrForbidden<T>(T f, TargetIndex ind)`（同类还有 FailOnDespawnedOrNull / FailOnDestroyedOrNull / FailOnForbidden / FailOnDowned / FailOnMentalState …） |
| `Verse.AI.ToilEffects`（静态扩展） | `static Toil WithProgressBar(Toil toil, TargetIndex ind, Func<float> progressGetter, bool interpolateBetweenActorAndTarget = true, float offsetZ = 0f, bool alwaysShow = false)`；另有 `WithProgressBarToilDelay`、`WithEffect`、`PlaySoundAtStart/AtEnd` |
| `Verse.AI.Toils_Goto` | `GotoThing(TargetIndex ind, PathEndMode peMode, bool canGotoSpawnedParent = true)`、`GotoThing(TargetIndex ind, IntVec3 exactCell)`、`GotoCell(TargetIndex ind, PathEndMode peMode)`、`GotoCell(IntVec3 cell, PathEndMode peMode)`、`Goto(TargetIndex ind, PathEndMode peMode)`、`GotoBuild(TargetIndex ind)` |
| `Verse.AI.JobDriver` | `public virtual abstract bool TryMakePreToilReservations(bool errorOnFailed)`；`nonpublic virtual abstract IEnumerable<Toil> MakeNewToils()`（所以模板用 `protected override` 正确）；字段 `Pawn pawn`、`Job job`、`int ticksLeftThisToil` |
| `Verse.AI.Toil` | 字段 `Action tickAction`、`Action initAction`、`Action<T> tickIntervalAction`、`ToilCompleteMode defaultCompleteMode`、`int defaultDuration` |
| `Verse.ToilMaker` | `static Toil MakeToil(string debugName)` |
| `Verse.JobMaker` | 7 个重载：`MakeJob()`、`MakeJob(JobDef)`、`MakeJob(JobDef, LocalTargetInfo)`、`(JobDef, LocalTargetInfo, LocalTargetInfo)`、`(JobDef, LocalTargetInfo, LocalTargetInfo, LocalTargetInfo)`、`(JobDef, LocalTargetInfo, int expiryInterval, bool checkOverrideOnExpiry)`、`(JobDef, int, bool)` |
| `Verse.ThingRequest.ForDef` | `static ThingRequest ForDef(ThingDef singleDef)` |
| `Verse.ThingDef.Named` | `static ThingDef Named(string defName)` |
| `Verse.AI.Job.targetA` | 字段 `LocalTargetInfo targetA` |

**结论**：类型与签名 0 处不存在、0 处不符；上面 3 处模板问题中 1 处已修（`using RimWorld;`），另 2 处经核对确认原写法合法。保留的未知项是运行期行为（WorkGiver 扫描频率、Toil 中断条件的实际触发时机）——本页未实机验证。

其他依据：WorkGiverDef 的 `giverClass` 出现率 98%、JobDef 的 `driverClass` 出现率 99%（来自 03-全量字段参考）。
