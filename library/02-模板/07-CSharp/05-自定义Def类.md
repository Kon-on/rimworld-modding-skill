> ✅ **核对状态：本页用到的类型与成员签名，已用反射对 1.7 游戏目录里的 DLL 逐条核对（0 处不存在、0 处签名不符；命令与原始输出见 `04-核验/C#接口核对结果.md`）；运行期行为未实机验证。**
>
> 核对目标（本机实测）：`Assembly-CSharp.dll` 版本 **1.7.9786.4087**、**16,221** 个类型；`UnityStubs.dll` **934** 个类型 / **6,653** 个方法，其中 **254** 个方法是 stub（分布在 88 个类型，清单见 `07-附录-UnityStubs失效成员清单.md`）；`0Harmony.dll` **3.0.0.0**（2,326 个类型，来自创意工坊 mod 2009463077）。
>
> 1.7 环境要点：目标框架 **net10.0**；**UnityEngine.\* 由 UnityStubs.dll 提供**（真兼容层，stub 只记警告并返回默认值、**不抛异常**）；**Harmony 不在游戏内**，须声明依赖 mod 2009463077 或自带 0Harmony.dll。
>
> csproj 要点：`<TargetFramework>net10.0</TargetFramework>`；引用游戏根目录的 `Assembly-CSharp.dll` 与 `UnityStubs.dll`（Private=false）；**不要引用 `UnityEngine.*.dll`**（1.7 已无这些文件）；依赖的第三方 DLL 必须一起放进 `Assemblies\`（否则整个 DLL 会被拒载并打印 "Loader exceptions:"）。

# 自定义 Def 类

## 用途

当原版 Def 的字段不够用时，可以**继承一个 Def 类**并加字段。XML 里用类名当根元素即可。

**典型用途**：做一套别人也能引用的新数据 Def（例如自定义的任务定义、剧情节点）。

## 代码

```csharp
using System.Collections.Generic;
using Verse;

namespace ExampleMod
{
    // 1. 自定义 Def 类：继承 Verse.Def
    public class ExampleStoryDef : Def
    {
        public int weight = 1;
        public string narrativeKey;
        public List<string> involvedDefs;
    }

    // 2. DefOf：给常用 Def 一个静态引用，避免到处写字符串
    [DefOf]
    public static class ExampleDefOf
    {
        public static ExampleStoryDef EXAMPLE_FirstStory;
    }

    // 3. 使用时取 def
    public static class ExampleUsage
    {
        public static void Do()
        {
            var d = DefDatabase<ExampleStoryDef>.GetNamed("EXAMPLE_FirstStory");
            Log.Message(d.narrativeKey);
        }
    }
}
```

对应的 XML（**根元素名就是类名**）：

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Defs>

  <ExampleMod.ExampleStoryDef>
    <defName>EXAMPLE_FirstStory</defName>
    <label>第一个示例故事</label>
    <description>这是一段自定义 Def 的示例。</description>
    <weight>3</weight>
    <narrativeKey>first_story</narrativeKey>
    <involvedDefs>
      <li>EXAMPLE_Rifle</li>
    </involvedDefs>
  </ExampleMod.ExampleStoryDef>
</Defs>
```

## 常见坑

- **XML 根元素要写类的命名空间全名**（或依赖游戏用短名解析——两种写法的容错性未验证，建议写全名）。
- **`DefOf` 类里的字段名必须与 defName 完全一致**，RimWorld 会在静态构造时按名字注入；不一致会抛异常。
- **自定义 Def 也必须有自己的文件夹**（如 `Defs/ExampleStoryDefs/`），文件名不影响解析但目录要有。
- **字段类型要能被 Scribe 处理**：常见类型（int/float/string/bool/List<string>）没问题，自定义类需要自己写 `ExposeData`。
- **发布后改字段名会破坏玩家存档**：Def 的顺序与名字是存档的一部分，加字段可以、改名字要谨慎。

## 核验

本页用到的每个类型与成员，都已用反射对 1.7 的 DLL 逐条核对（原始输出见 `04-核验/C#接口核对结果.md`）：

| 本页用到 | 1.7 实际签名（机器核对） |
|---|---|
| `Verse.Def` | 基类 `Verse.Editable`；字段 `string defName`、`string label`、`string description`、`List<DefModExtension> modExtensions`、`ModContentPack modContentPack`、`ushort index`；属性 `TaggedString LabelCap { get; }` |
| `Verse.DefDatabase<T>.GetNamed` | `public static T GetNamed(string defName, bool errorOnFail = true)`（想不报错取用 `GetNamedSilentFail(string defName)`） |
| `[DefOf]` 的真实类型 | **`RimWorld.DefOf`（继承 `System.Attribute`）** —— 没有 `DefOfAttribute` 这个类，反射找 `DefOfAttribute` 会找不到；注入由 `RimWorld.DefOfHelper` 完成 |
| `Verse.DefModExtension` | `class DefModExtension : System.Object`，无参构造 |

**结论**：类型与签名 0 处不存在、0 处不符。

- 「Def 子类当 XML 根元素」是官方用法：254 种 Def 类型里大量是子类（如 `PsychicRitualDef_BloodRain`、`RoomPart_CrateDef`、`CreepJoiner*`），来自 03-全量字段参考。
- 保留的未知项：**小写/短名根元素能否解析**。原版本体里存在大小写不一致的真实案例（`Core\Defs\BackstoryDefs\Solid\Solid_Rare.xml` 用大写 `BackStoryDef`，`Biotech\Defs\JobDefs\Jobs_Learning.xml` 用小写 `jobDef` 根标签共 6 处），据此**推断** 1.7 的 Def 类型名解析不区分大小写，但未实机验证 —— 模板仍建议写类名全名。
