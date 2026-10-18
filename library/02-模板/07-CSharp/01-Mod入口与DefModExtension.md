> ✅ **核对状态：本页用到的类型与成员签名，已用反射对 1.7 游戏目录里的 DLL 逐条核对（0 处不存在、0 处签名不符；命令与原始输出见 `04-核验/C#接口核对结果.md`）；运行期行为未实机验证。**
>
> 核对目标（本机实测）：`Assembly-CSharp.dll` 版本 **1.7.9786.4087**、**16,221** 个类型；`UnityStubs.dll` **934** 个类型 / **6,653** 个方法，其中 **254** 个方法是 stub（分布在 88 个类型，清单见 `07-附录-UnityStubs失效成员清单.md`）；`0Harmony.dll` **3.0.0.0**（2,326 个类型，来自创意工坊 mod 2009463077）。
>
> 1.7 环境要点：目标框架 **net10.0**；**UnityEngine.\* 由 UnityStubs.dll 提供**（真兼容层，stub 只记警告并返回默认值、**不抛异常**）；**Harmony 不在游戏内**，须声明依赖 mod 2009463077 或自带 0Harmony.dll。
>
> csproj 要点：`<TargetFramework>net10.0</TargetFramework>`；引用游戏根目录的 `Assembly-CSharp.dll` 与 `UnityStubs.dll`（Private=false）；**不要引用 `UnityEngine.*.dll`**（1.7 已无这些文件）；依赖的第三方 DLL 必须一起放进 `Assemblies\`（否则整个 DLL 会被拒载并打印 "Loader exceptions:"）。

# Mod 入口与 DefModExtension

## 用途

一个 C# mod 的最小骨架：**Mod 子类**（mod 设置与初始化）、**ModSettings**（存玩家配置）、**DefModExtension**（往已有 Def 上挂自定义数据，不必继承）。

DefModExtension 是 1.7 里最推荐的扩展方式：它让**纯数据**挂在原版 Def 上，其他 mod 也能读到。

## 代码

```csharp
using Verse;

namespace ExampleMod
{
    // 1. mod 入口：RimWorld 会扫描程序集里所有 Verse.Mod 的非抽象子类
    public class ExampleMod : Mod
    {
        public static ExampleModSettings Settings;

        public ExampleMod(ModContentPack content) : base(content)
        {
            Settings = GetSettings<ExampleModSettings>();
        }

        public override string SettingsCategory() => "示例 Mod";
    }

    // 2. 设置：存盘与读盘由 Scribe 完成
    public class ExampleModSettings : ModSettings
    {
        public float multiplier = 2f;

        public override void ExposeData()
        {
            Scribe_Values.Look(ref multiplier, "multiplier", 2f);
        }
    }

    // 3. DefModExtension：给原版/自己的 Def 附加数据
    public class DefModExtension_Example : DefModExtension
    {
        public float multiplier = 2f;
        public string customLabel;
    }
}
```

对应的 XML 用法（可以挂在任意 Def 上）：

```xml
<ThingDef ParentName="BaseGun">
  <defName>EXAMPLE_Rifle</defName>
  <modExtensions>
    <li Class="ExampleMod.DefModExtension_Example">
      <multiplier>3.5</multiplier>
      <customLabel>特殊型号</customLabel>
    </li>
  </modExtensions>
</ThingDef>
```

## 常见坑

- **`Class` 属性要写完整命名空间**（如 `ExampleMod.DefModExtension_Example`），只写类名会找不到。
- **1.7 里 Harmony 是外部 mod**：程序集用到 Harmony 时，mod 必须依赖 2009463077，或自己随包带 0Harmony.dll。
- **不要再用 Unity 时代的多线程/协程/渲染 API**：UnityEngine.\* 现在由 UnityStubs 顶替，行为不等价（待验证）。
- **建议把 DLL 编到 net10.0**：虽然 WaylithClr 开了 LaxAssemblyBinding 等宽松开关、旧框架程序集仍可能加载，但样本里 16/22 个 1.7 mod 都重编到了 net10.0。
- **`JitPatchableAssemblies = Assembly-CSharp` 只针对游戏本体**，你自己的程序集不在这个列表里。

## 核验

本页用到的每个类型与成员，都已用反射对 1.7 的 DLL 逐条核对（原始输出见 `04-核验/C#接口核对结果.md`）：

| 本页用到 | 1.7 实际签名（机器核对） |
|---|---|
| `Verse.Mod` 构造函数 | `public Mod(ModContentPack content)` |
| `Verse.Mod.GetSettings<T>` | `public T GetSettings<T>()` |
| `Verse.Mod.SettingsCategory` | `public virtual string SettingsCategory()` —— **是方法不是属性**，模板的 `override` 写法正确 |
| `Verse.Mod.DoSettingsWindowContents` | `public virtual void DoSettingsWindowContents(Rect inRect)` —— 画设置窗体的入口是它；`SettingsCategory` 只返回标题 |
| `Verse.Mod.Content` | `public ModContentPack Content { get; }`（同名的 `intContent` 是内部字段，别用） |
| `Verse.ModSettings.ExposeData` | `public virtual void ExposeData()` |
| `Verse.Scribe_Values.Look<T>` | `public static void Look<T>(ref T value, string label, T defaultValue = 默认, bool forceSave = true)` —— 后两参可省，模板的 3 参调用命中 |
| `Verse.DefModExtension` | `class DefModExtension : System.Object`（无参构造） |
| `Verse.Def.modExtensions` | `public List<DefModExtension> modExtensions` —— **是字段**，XML 的 `<modExtensions><li Class="...">` 就是填它 |

**结论**：0 处不存在、0 处签名不符。保留的未知项只有运行期行为（`Mod` 子类的实例化时机、`GetSettings` 的回调链路），需实机验证。

其他依据：环境事实来自 `RimWorld.runtimeconfig.json` 与安装根目录二进制（实测）；编译目标参考样本 mod `...\294100\3216091476\1.7\Source\mod.csproj`（net472→net10.0、Krafs.Rimworld.Ref 1.6.4488-beta→1.7.4977-alpha.1）。
