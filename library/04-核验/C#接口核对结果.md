# C# 接口核对结果（07-CSharp 六份模板的机器核对）

> 本文件回答一个问题：**07-CSharp 里的每一行 C# 代码，用到的类型和成员在 1.7 里真的存在吗？签名对得上吗？**
> 核对方式不是"看文档"，而是**反射读取游戏目录里的 DLL 元数据**（不加载、不执行游戏代码）。
> 结论先说：**类型与成员 0 处不存在、0 处签名不符**；核对过程中改了模板 1 处代码 + 5 处数字/命名空间表述。

## 1. 核对对象

| 文件 | 路径 | 版本 / 规模 |
|---|---|---|
| 游戏主程序集 | `E:\SteamLibrary\steamapps\common\RimWorld\Assembly-CSharp.dll` | 程序集版本 **1.7.9786.4087**、**16,221** 个类型 |
| Unity 兼容层 | `E:\SteamLibrary\steamapps\common\RimWorld\UnityStubs.dll` | **934** 个类型 / **6,653** 个方法（DeclaredOnly 口径） |
| Harmony | `E:\SteamLibrary\steamapps\workshop\content\294100\2009463077\1.7\Assemblies\0Harmony.dll` | **3.0.0.0**、2,326 个类型（来自创意工坊 mod **2009463077**） |

被核对的模板：`02-模板/07-CSharp/` 下的 6 份（01-Mod入口与DefModExtension、02-ThingComp与HediffComp、03-JobDriver与WorkGiver、04-Harmony补丁、05-自定义Def类、06-UnityStubs兼容层与失效API），以及配套附录 `07-附录-UnityStubs失效成员清单.md`。

## 2. 核对方法（可复现）

1. `docs/_api_dump.ps1` —— 用 `[System.Reflection.Assembly]::LoadFrom` 载入三个 DLL（**只反射、不执行**），导出全部类型与成员（含每个类型沿 BaseType 链最多 8 层的继承展开）到 `docs/csharp-api.json`（1,056,446 字节）。
   - 要点：`GetTypes()` 可能抛 `ReflectionTypeLoadException`，需 catch 后取 `Exception.Types`。
   - **踩过的坑**：不要给 pwsh 注册 `AppDomain.AssemblyResolve` 处理器 —— 它会递归解析卫星程序集并爆栈（实测堆栈：`InternalGetSatelliteAssembly` → `ResourceManager.GetString` → `ModuleCmdletBase.LoadModule`）。直接 `LoadFrom` 三个 DLL 即可。
2. `docs/_member_search.ps1` —— 按方法名（`CanReserve`、`Reserve`、`IsForbidden`、`FailOnDespawnedNullOrForbidden`、`WithProgressBar`、`GetNamed`、`Kill` …）全局搜索，结果 `docs/_member_search.out.txt`（37,261 字节）。
3. `docs/_api_check3.ps1` —— 逐个精确签名核对，含**参数是否可选**（IsOptional / DefaultValue），结果 `docs/_api_check2.out.txt`、`docs/_api_check3.out.txt`。
4. `docs/_stub_scan.ps1` —— 扫描 `UnityStubs.dll` 每个方法体的 IL，找出对 `UnityStubs.Internal.StubWarner::LogStub`（MetadataToken **100663905**，小端字节 97,2,0,6）的调用点 → `docs/unitystubs-stubs.txt`；再由 `docs/_dump_us_signatures.ps1` 展开同名重载 → `docs/unitystubs-stub-signatures.txt`。
   - **坑**：含 IL 字节扫描循环的 .ps1 会被 Windows Defender / AMSI 判定为恶意脚本并拦截（"This script contains malicious content and has been blocked by your antivirus software"），随后该文件变成「被占用 / Access denied」，读不了也跑不了。**含此类循环的脚本要一次成型，或改用纯反射脚本。**

## 3. 核对结果：六份模板的用到的类型全部存在

| 模板 | 用到的关键类型 | 结论 |
|---|---|---|
| 01-Mod入口与DefModExtension | `Verse.Mod`、`Verse.ModSettings`、`Verse.Scribe_Values`、`Verse.DefModExtension` | 全部存在，签名一致；`SettingsCategory()` 确认是**方法**（不是属性） |
| 02-ThingComp与HediffComp | `Verse.CompProperties`、`Verse.ThingComp`、`Verse.HediffComp`、`Verse.Hediff`、`Verse.Pawn_HealthTracker` | 全部存在；`parent.pawn.health.RemoveHediff(parent)` 三段链路全部核对通过 |
| 03-JobDriver与WorkGiver | `RimWorld.WorkGiver_Scanner`、`Verse.AI.ReservationUtility`、`RimWorld.ForbidUtility`、`Verse.AI.Toil*`、`Verse.JobMaker` | 全部存在；**改了 1 处**（见下） |
| 04-Harmony补丁 | `HarmonyLib.Harmony`、`HarmonyPatch` 系列、`Verse.Pawn.Kill`、`Verse.StaticConstructorOnStartup` | 全部存在；`nameof(Pawn.Kill)` **无歧义**（Pawn 上只有 1 个 Kill 重载） |
| 05-自定义Def类 | `Verse.Def`、`Verse.DefDatabase<T>`、`RimWorld.DefOf` | 全部存在；**`[DefOf]` 的真实类型是 `RimWorld.DefOf`，不存在 `DefOfAttribute`** |
| 06-UnityStubs兼容层与失效API | `UnityStubs.Internal.StubWarner` 等 | 存在；**改了 5 处数字/命名空间**（见下） |

## 4. 核对过程中改掉的 6 处

| # | 文件 | 原稿 | 核对结果 | 处理 |
|---|---|---|---|---|
| 1 | 03-JobDriver与WorkGiver | 只写 `using Verse.AI;` | `WorkGiver_Scanner` 的真实全名是 **`RimWorld.WorkGiver_Scanner`**（基类 `RimWorld.WorkGiver`）；`IsForbidden` 是 `RimWorld.ForbidUtility` 的扩展方法 | **代码补 `using RimWorld;`**（编译不过级别的问题） |
| 2 | 03 | 把 `FailOnDespawnedNullOrForbidden` / `WithProgressBar` 当普通方法 | 它们是 `Verse.AI` 下静态扩展类 `ToilFailConditions` / `ToilEffects` 的方法 | 确认 `using Verse.AI;` 已覆盖，无需改 |
| 3 | 03 | `GotoThing(ind, PathEndMode.InteractionCell)` 两参调用 | 真签名 `GotoThing(TargetIndex, PathEndMode, bool canGotoSpawnedParent = true)`，第三参有默认值 | 合法，无需改 |
| 4 | 06 | 「全部 935 个类型、7471 个方法」「257 个方法没实现」 | 实测 **934 类型 / 6,653 方法 / 254 个 stub 调用点（230 个唯一成员 / 88 个类型）**；差异是统计口径 | 全文改成实测口径并注明差异来源 |
| 5 | 06 | 「其余 37 个 Input 方法正常」 | 实测 `Input` 共 **37** 个方法，其中 **2 个 stub / 35 个正常** | 改为 35，并补 InputSystem 的 stub 分布 |
| 6 | 06 | `CommandBuffer`(30)、`CullingGroup`(12)、`Unity.Profiling.Profiler` | `UnityEngine.Rendering.CommandBuffer` 30 处调用点；`CullingGroup` **11** 处调用点（18 个方法）；`Profiler` 的完整命名空间是 **`UnityEngine.Profiling`** | 补全命名空间、修正数字、把可用性表的括号数字统一为 DeclaredOnly 口径 |

另有两处是**新增**而非修正：02 补记 1.7 新出现的 `CompTickInterval(int)` / `CompPostTickInterval(ref float, int)`；04 补上 4 条「为什么这次敢说 Harmony 能用」的静态证据链。

## 5. 已验证签名速查（模板里用到的全部）

```
// Verse.Mod（1.7.9786.4087 实测）
.ctor(ModContentPack content)
public T GetSettings<T>()
public virtual string SettingsCategory()          // 是方法
public virtual void DoSettingsWindowContents(Rect inRect)
public virtual void WriteSettings()
public ModContentPack Content { get; }

// Verse.ModSettings / Verse.Scribe_Values
public virtual void ExposeData()
public static void Look<T>(ref T value, string label, T defaultValue = default, bool forceSave = false)

// Comp 家族
CompProperties : 只有 1 个字段  public Type compClass
ThingComp      : public CompProperties props;  virtual Initialize(CompProperties) / CompTick() / CompTickInterval(int delta) / CompTickRare() / CompTickLong() / PostExposeData()
HediffComp     : public HediffWithComps parent; public HediffCompProperties props;
                 virtual CompPostTick(ref float severityAdjustment) / CompPostTickInterval(ref float, int delta) / CompExposeData()
Hediff         : public Pawn pawn; public float severityInt; public float Severity { get; }
Pawn           : public Pawn_HealthTracker health
Pawn_HealthTracker : public void RemoveHediff(Hediff hediff)

// 工作与 Job
RimWorld.WorkGiver_Scanner : ThingRequest PotentialWorkThingRequest { get; } / PathEndMode PathEndMode { get; }
                             bool HasJobOnThing(Pawn pawn, Thing t, bool forced = false)
                             Job JobOnThing(Pawn pawn, Thing t, bool forced = false)
Verse.AI.ReservationUtility (static 扩展)
   bool CanReserve(Pawn p, LocalTargetInfo target, int maxPawns = 1, int stackCount = -1, ReservationLayerDef layer = null, bool ignoreOtherReservations = false)
   bool Reserve(Pawn p, LocalTargetInfo target, Job job, int maxPawns = 1, int stackCount = -1, ReservationLayerDef layer = null, bool errorOnFailed = false, bool ignoreOtherReservations = false)
RimWorld.ForbidUtility (static 扩展) : bool IsForbidden(Thing, Pawn) / (IntVec3, Pawn) / (Thing, Faction)
Verse.AI.ToilFailConditions (static 扩展) : T FailOnDespawnedNullOrForbidden<T>(T f, TargetIndex ind) 等
Verse.AI.ToilEffects (static 扩展)        : Toil WithProgressBar(Toil, TargetIndex, Func<float>, bool = true, float = 0f, bool = false) 等
Verse.AI.Toils_Goto : GotoThing(TargetIndex, PathEndMode, bool canGotoSpawnedParent = true) / GotoThing(TargetIndex, IntVec3)
                      GotoCell(TargetIndex, PathEndMode) / GotoCell(IntVec3, PathEndMode) / Goto(TargetIndex, PathEndMode) / GotoBuild(TargetIndex)
Verse.AI.JobDriver  : public virtual abstract bool TryMakePreToilReservations(bool errorOnFailed)
                      nonpublic virtual abstract IEnumerable<Toil> MakeNewToils()     // 用 protected override
                      字段 Pawn pawn / Job job / int ticksLeftThisToil
Verse.AI.Toil       : 字段 Action tickAction / Action initAction / Action<T> tickIntervalAction
                      ToilCompleteMode defaultCompleteMode / int defaultDuration
Verse.ToilMaker     : static Toil MakeToil(string debugName)
Verse.JobMaker      : MakeJob() / (JobDef) / (JobDef, LocalTargetInfo) / (JobDef, LocalTargetInfo, LocalTargetInfo)
                      / (JobDef, LocalTargetInfo, LocalTargetInfo, LocalTargetInfo) / (JobDef, LocalTargetInfo, int, bool) / (JobDef, int, bool)
Verse.ThingRequest  : static ThingRequest ForDef(ThingDef singleDef)
Verse.ThingDef      : static ThingDef Named(string defName)
Verse.AI.Job        : 字段 LocalTargetInfo targetA
Verse.Pawn          : public virtual void Kill(Nullable<DamageInfo> dinfo, Hediff exactCulprit = null)   // 唯一重载

// Harmony（0Harmony 3.0.0.0）
HarmonyLib.Harmony  : .ctor(string id) / void PatchAll() / void PatchAll(Assembly)
                      MethodInfo Patch(MethodBase original, HarmonyMethod prefix = null, HarmonyMethod postfix = null, HarmonyMethod transpiler = null, HarmonyMethod finalizer = null)
                      void UnpatchAll(string harmonyID = null) / void Unpatch(MethodBase, HarmonyPatchType, string harmonyID = null)
                      IEnumerable<MethodBase> GetAllPatchedMethods() / HarmonyLib.PatchInfo GetPatchInfo(MethodBase)
HarmonyLib          : HarmonyPatch / HarmonyPrefix / HarmonyPostfix / HarmonyMethod / HarmonyPatchAll 均存在
Verse               : StaticConstructorOnStartup : Attribute

// Def 体系
Verse.Def           : 基类 Verse.Editable；字段 string defName / label / description / List<DefModExtension> modExtensions / ModContentPack modContentPack / ushort index
                      public TaggedString LabelCap { get; }
Verse.DefDatabase<T>: static T GetNamed(string defName, bool errorOnFail = true) / static T GetNamedSilentFail(string defName)
RimWorld.DefOf      : Attribute（**不存在 DefOfAttribute**）  /  RimWorld.DefOfHelper 负责注入
Verse.DefModExtension : class DefModExtension : System.Object
```

## 6. 还剩下什么没验证（诚实清单）

| 未验证项 | 为什么没验证 | 怎么验证 |
|---|---|---|
| Harmony 补丁在运行时是否真的生效 | 需要实机加载游戏；MonoMod 的 detour 依赖 `clrjit`/`ICorJitInfo` 版本探测，而 1.7 用自研 `WaylithClr 10.0.13-waylithclr.dev` | 装一个用 Harmony 的 mod，看日志里有没有补丁失败信息 |
| 自定义 Def 类 / Mod 类的实例化与 XML 解析行为 | 需要实机 | 用最小 mod 实测，看 `DefDatabase` 里有没有你的 defName，以及 `Loader exceptions` |
| Comp 组件的 tick 频率、Toil 中断条件触发时机 | 纯运行期行为 | 实机观察 + 日志打点 |
| stub 方法被调用时日志的确切文本 | 需要运行 | 调用一次 `Input.GetAxis` 后查日志 |

> 口语版：**"能不能编过、名字对不对"已经全部机器核对完（0 处不存在）；"运行起来是不是这个效果"必须实机跑一次。** 模板里所有 C# 都按这个标准标注。

## 7. 复跑

```powershell
# 1) 导出三份 DLL 的类型与成员快照（只反射、不执行）
pwsh -File "docs/_api_dump.ps1"        # -> docs/csharp-api.json
# 2) 精确核对签名
pwsh -File "docs/_api_check3.ps1"      # -> docs/_api_check2.out.txt / _api_check3.out.txt
# 3) 提取 UnityStubs 失效成员（注意：含 IL 扫描，可能被杀软拦截）
pwsh -File "docs/_stub_scan.ps1"       # -> docs/unitystubs-stubs.txt
pwsh -File "docs/_dump_us_signatures.ps1"  # -> docs/unitystubs-stub-signatures.txt
```
