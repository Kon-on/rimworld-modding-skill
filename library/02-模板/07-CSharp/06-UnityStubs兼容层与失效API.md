> ✅ **核对状态：本页用到的类型与成员签名，已用反射对 1.7 游戏目录里的 DLL 逐条核对（0 处不存在、0 处签名不符；命令与原始输出见 `04-核验/C#接口核对结果.md`）；运行期行为未实机验证。**
>
> 核对目标（本机实测）：`Assembly-CSharp.dll` 版本 **1.7.9786.4087**、**16,221** 个类型；`UnityStubs.dll` **934** 个类型 / **6,653** 个方法，其中 **254** 个方法是 stub（分布在 88 个类型，清单见 `07-附录-UnityStubs失效成员清单.md`）；`0Harmony.dll` **3.0.0.0**（2,326 个类型，来自创意工坊 mod 2009463077）。
>
> 1.7 环境要点：目标框架 **net10.0**；**UnityEngine.\* 由 UnityStubs.dll 提供**（真兼容层，stub 只记警告并返回默认值、**不抛异常**）；**Harmony 不在游戏内**，须声明依赖 mod 2009463077 或自带 0Harmony.dll。
>
> csproj 要点：`<TargetFramework>net10.0</TargetFramework>`；引用游戏根目录的 `Assembly-CSharp.dll` 与 `UnityStubs.dll`（Private=false）；**不要引用 `UnityEngine.*.dll`**（1.7 已无这些文件）；依赖的第三方 DLL 必须一起放进 `Assemblies\`（否则整个 DLL 会被拒载并打印 "Loader exceptions:"）。

# UnityStubs 兼容层与 1.7 失效 API 清单

## 用途

**1.7 的 UnityEngine 已经不是真的 Unity 了**：游戏换成自研 Waylith 引擎后，原来的 `UnityEngine.*` 由 **UnityStubs.dll** 顶替（运行时通过 `WaylithClr.AssemblyNameRedirects = "UnityEngine*=UnityStubs"` 重定向）。

**好消息**：UnityStubs 是**真兼容层**，不是空壳——实测 **934 个类型 / 6,653 个方法**（口径：Public + NonPublic + Instance + Static + DeclaredOnly）。**绝大多数 Unity API 照常能用**，旧代码往往不改就能编过。

**坏消息**：其中 **254 个方法体（分布在 88 个类型里）**会调用 `UnityStubs.Internal.StubWarner.LogStub`，也就是**没有实现**——调用时只记一条警告然后返回默认值/空操作（**不抛异常**，所以函数不会崩，但也不会有效果，这是最容易被忽略的坑）。数字按方法体里的实际调用点统计；更早一版报告口径为 257，差异来自重载计数方式。

本文件的工作：**告诉你哪些 API 还能用、哪些已经废了、废了该换什么。**

## 不能用了或不可靠的 API（会静默失效）

| 类别 | 具体成员 | 现状 |
|---|---|---|
| 输入 | `Input.GetAxis`、`Input.GetTouch` | stub（返回 0/空）。`UnityEngine.Input` 共 **37** 个方法，其中 **2 个** stub、**35 个正常**（原稿「其余 37 个正常」是口径错误）；新版 InputSystem 另有一批 stub（`InputActionAsset` 13 处，`Mouse`/`Pointer`/`InputActionMap` 各 3 处） |
| 时间 | `Time.timeScale` 赋值 | stub；且 `get_timeScale` 被硬编码为恒返回 1（改不了游戏速度） |
| 图形 | `Graphics.DrawTexture`、`Graphics.ExecuteCommandBuffer` | stub |
| 图形 | `Material.SetTexture` | stub（其他 Material 方法正常） |
| 资源 | `Resources.GetBuiltinResource` | stub |
| 网格 | `Mesh.Optimize`、`Mesh.SetIndices` | stub |
| 截图 | `ScreenCapture.CaptureScreenshot` | stub |
| 对象 | `UnityEngine.Object.hideFlags` | stub |
| 计算着色器 | `ComputeShader` 大部分成员 | 12 个方法 stub |
| 命令缓冲 | **`UnityEngine.Rendering.CommandBuffer`**（原稿漏了命名空间） | 30 处 stub 调用点，该类基本不可用 |
| 剔除/性能 | `CullingGroup`（**11** 处调用点 / 18 个方法）、`Unity.Profiling.ProfilerRecorder`（7）、**`UnityEngine.Profiling.Profiler`**（6） | stub，应改用 `Waylith.Profiling.*`；注意 `Profiler` 的完整命名空间是 **UnityEngine.Profiling**（原稿漏了 `Engine.`） |
| 相机/UI | `Camera` 6 个成员、`UnityEngine.UI`、TMP、Video、InputSystem | 部分成员 stub，整块不建议新写 |

> 上表是**按类型分组的高频项**；**完整 254 条清单**见 `07-附录-UnityStubs失效成员清单.md`（按类型分组，另附 288 条展开签名）。提取原理：扫描 `UnityStubs.dll` 每个方法体里对 `UnityStubs.Internal.StubWarner::LogStub` 的调用点（脚本 `docs/_stub_scan.ps1`）。

## 还完全可用的 API（可放心写）

实测 stub 密度（方法数按 `DeclaredOnly` 口径，全部为本机反射复测）：

| 类型 | 方法数 | stub | 可用性 |
|---|---|---|---|
| `Mathf` | 64 | 0 | 完整 |
| `Transform` | 60 | 0 | 完整 |
| `Vector3` / `Vector2` | 55 / 53 | 0 | 完整 |
| `Rect` / `Color` / `Color32` | 44 / 44 / 11 | 0 | 完整 |
| `GameObject` | 30 | 0 | 完整 |
| `MonoBehaviour` | 4 | 0 | 完整（协程走 `UnityEngine.CoroutineScheduler`） |
| `GUI` | 156 | 0 | 完整 |
| `Screen` | 15 | 0 | 完整（转发 `Waylith.EngineWindow`） |
| `Application` / `Debug` | 37 / 24 | 0 | 完整 |
| `Mesh` | 176 | 2 | 基本可用（避开 `Optimize`/`SetIndices`） |
| `Graphics` | 99 | 3 | 基本可用（避开 `DrawTexture`/`ExecuteCommandBuffer`） |
| `Material` | 141 | 1 | 基本可用（避开 `SetTexture`） |
| `Texture2D` | 83 | 2 | 基本可用 |
| `Shader` | 75 | 4 | 基本可用（避开 `GetGlobalTexture` 等） |
| `Camera` | 90 | 6 | 部分失效 |
| `RenderTexture` | 51 | 3 | 部分失效 |
| `Resources` | 20 | 1 | 避开 `GetBuiltinResource` |
| `CullingGroup` / `ComputeShader` | 18 / 12 | 11 / 12 | 基本不可用 |

> 原稿这里的括号数字（`Vector3`(57)、`Mathf`(65)、`Texture2D`(91) …）是**含继承成员**的口径，本表统一改成 `DeclaredOnly` 口径，数值会小幅差异。

## 1.7 里新写的代码应该怎么做

```csharp
// 1) 直接用 UnityEngine.* 是可以的（会被重定向到 UnityStubs）
using UnityEngine;

// 2) 反射找 Unity 类型时，程序集名要写 "UnityStubs"（不是 "UnityEngine.CoreModule"）
var t = System.Type.GetType("UnityEngine.Vector3, UnityStubs");

// 3) 性能计时改走 Waylith
using Waylith.Profiling;   // 取代 Unity.Profiling.Profiler / ProfilerRecorder

// 4) 渲染/纹理处理：1.7 的样本 mod 已把 GPU 路径改成纯 CPU 实现
//    （删掉了 RenderTexture.GetTemporary / Graphics.Blit / Texture2D.ReadPixels，
//      改为 Color[] + GetPixelBilinear + SetPixels 手工合成）
```

## 常见坑

- **stub 是静默失效**：调回去默认值，不抛异常、日志里只有一条警告，很容易误判为"我的逻辑没生效"。
- **不要引用 `UnityEngine.*.dll`**：1.7 游戏目录里这些文件已经没有了，csproj 里要改成引用 `UnityStubs.dll`。
- **不要假设旧的 Unity 程序集名**：`UnityEngine.CoreModule`、`UnityEngine.IMGUIModule` 之类的反射字符串会失败（样本中有 mod 因此仍是 .NET Framework 4.8 + 引用 1.6 的 Assembly-CSharp，属于侥幸能加载）。
- **性能分析相关 API 全部换栈**：`Unity.Profiling` → `Waylith.Profiling`（`ProfilerInstrumentation.ExcludedAssemblies` 里官方已把 `0Harmony`/`MonoMod.*`/`Mono.Cecil*` 排除，说明官方在这套栈上做埋点）。
- **渲染管线不再吃 Unity 资产**：预编译的 AssetBundle Shader 失效，1.7 渲染自定义效果要写 ShaderDef + `.glsl`（见 1.6→1.7 迁移指南）。

## 核验

- `docs\验证-csharp-1.7.md`：UnityStubs.dll 元数据统计（口径为 935 类型 / 7471 MethodDef / 33 AssemblyRefs / net10.0）、stub 方法分布、`StubWarner::LogStub` 行为（记警告 + 返回默认值，不抛异常）、逐类型方法数与 IL 字节数
- 本轮独立复测产物：`docs\csharp-api.json`（三 DLL 全量类型/成员）、`docs\unitystubs-stubs.txt`（254 条 stub 调用点）、`docs\unitystubs-stub-signatures.txt`（288 条展开签名）
- 同一报告：Assembly-CSharp.dll 的 173 条 UnityStubs typeRef 明细（含 Unity.Collections 19、Unity.Jobs 8、Unity.Profiling 4）
- 游戏根目录 `RimWorld.runtimeconfig.json` 的 `AssemblyNameRedirects`
