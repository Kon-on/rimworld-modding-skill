# 05 — C# Mod 开发基础

> **适用版本**: RimWorld 1.6 | **最后更新**: 2026-05-31


## 目录

- [概述](#概述)
- [Mod 类——入口点](#mod类入口点)
- [Mod Settings——可配置选项](#modsettings可配置选项)
- [ExposeData——存档兼容](#exposedata存档兼容)
- [ThingComp——给物品添加自定义组件](#thingcomp给物品添加自定义组件)
- [GameComponent / MapComponent / WorldComponent](#gamecomponentmapcomponentworldcomponent)
- [DefModExtension——自定义 Def 扩展字段](#defmodextension自定义def扩展字段)
- [编译与引用](#编译与引用)
- [常见问题](#常见问题)

## 概述

当 XML Def 无法满足需求时（如自定义行为、复杂逻辑、数据持久化），需要编写 C# 代码。

## Mod 类——入口点

```csharp
using Verse;
using UnityEngine;

// 用户根据自己选择的前缀和 Mod 名自行确定命名空间
namespace <你的前缀>.<你的Mod名>
{
    public class <你的Mod名>Mod : Mod
    {
        public static ModSettings_<你的前缀> settings;

        public <你的Mod名>Mod(ModContentPack content) : base(content)
        {
            settings = GetSettings<ModSettings_<你的前缀>>();
        }

        public override void DoSettingsWindowContents(Rect inRect)
        {
            base.DoSettingsWindowContents(inRect);
            settings.DoWindowContents(inRect);
        }

        public override string SettingsCategory()
        {
            return "你的 Mod 名称";  // 用户自行填写
        }
    }
}
```

## Mod Settings——可配置选项

```csharp
using Verse;
using UnityEngine;

// 用户根据自己选择的前缀自行确定命名空间
namespace <你的前缀>.<你的Mod名>
{
    public class ModSettings_<你的前缀> : ModSettings
    {
        public bool enableFeature = true;
        public float damageMultiplier = 1.5f;
        public int maxItems = 100;

        public void DoWindowContents(Rect inRect)
        {
            Listing_Standard listing = new Listing_Standard();
            listing.Begin(inRect);

            listing.CheckboxLabeled("Enable Feature", ref enableFeature);
            damageMultiplier = listing.Slider(damageMultiplier, 0.5f, 5f);
            listing.Gap();

            listing.Label($"Max Items: {maxItems}");
            maxItems = (int)listing.Slider(maxItems, 10, 1000);

            listing.End();
        }

        public override void ExposeData()
        {
            base.ExposeData();
            Scribe_Values.Look(ref enableFeature, "enableFeature", true);
            Scribe_Values.Look(ref damageMultiplier, "damageMultiplier", 1.5f);
            Scribe_Values.Look(ref maxItems, "maxItems", 100);
        }
    }
}
```

**关键点**：
- `ExposeData()` 中的字符串 key（如 `"enableFeature"`）用于存档读写
- 默认值必须在 `Scribe_Values.Look()` 中与 `ExposeData` 保持一致
- 所有可序列化的字段都要在 `ExposeData()` 中处理

## ExposeData——存档兼容

自定义类需要保存数据时必须实现：

```csharp
using Verse;

public class CustomTracker : IExposable
{
    public int counter;
    public Pawn trackedPawn;

    public void ExposeData()
    {
        Scribe_Values.Look(ref counter, "counter", 0);
        Scribe_References.Look(ref trackedPawn, "trackedPawn");
    }
}
```

**Scribe 方法速查**：

| 方法 | 用途 |
|------|------|
| `Scribe_Values.Look(ref val, key, default)` | 基本类型（int, float, bool, string） |
| `Scribe_References.Look(ref ref, key)` | Thing/Pawn 引用 |
| `Scribe_Defs.Look(ref def, key)` | Def 引用（ThingDef, RecipeDef 等） |
| `Scribe_Collections.Look(ref list, key, mode)` | 列表/集合 |
| `Scribe_Deep.Look(ref obj, key, ...)` | 嵌套 IExposable 对象 |

## ThingComp——给物品添加自定义组件

ThingComp 是最常用的扩展机制，用于给任意 Thing 添加自定义行为。

### CompProperties（数据定义）

```csharp
using Verse;

public class CompProperties_CustomBattery : CompProperties
{
    public float storedEnergy = 100f;
    public float efficiency = 0.9f;

    public CompProperties_CustomBattery()
    {
        compClass = typeof(CompCustomBattery);
    }
}
```

### ThingComp（行为实现）

```csharp
using Verse;

public class CompCustomBattery : ThingComp
{
    public CompProperties_CustomBattery Props => (CompProperties_CustomBattery)props;

    private float currentEnergy;

    public override void PostSpawnSetup(bool respawningAfterLoad)
    {
        base.PostSpawnSetup(respawningAfterLoad);
        if (!respawningAfterLoad)
        {
            currentEnergy = Props.storedEnergy;
        }
    }

    public override void CompTick()
    {
        base.CompTick();
        // 每 tick 执行的自定义逻辑
        // 注意：CompTick 每帧调用，避免重型操作
    }

    public override void PostExposeData()
    {
        base.PostExposeData();
        Scribe_Values.Look(ref currentEnergy, "currentEnergy", 0f);
    }

    public void DrainEnergy(float amount)
    {
        currentEnergy -= amount * Props.efficiency;
        if (currentEnergy < 0) currentEnergy = 0;
    }
}
```

### XML 中使用

```xml
<ThingDef ParentName="BuildingBase">
  <defName>SR_CustomBattery</defName>
  ...
  <comps>
    <li Class="CompProperties_CustomBattery">
      <storedEnergy>500</storedEnergy>
      <efficiency>0.95</efficiency>
    </li>
  </comps>
</ThingDef>
```

## GameComponent / MapComponent / WorldComponent

三种组件用于不同层级的数据管理：

| 组件 | 作用域 | 生命周期 | 用途 |
|------|--------|---------|------|
| `GameComponent` | 全局 | 游戏启动→退出 | 全局数据、事件监听 |
| `MapComponent` | 单张地图 | 地图加载→卸载 | 地图级数据 |
| `WorldComponent` | 世界 | 世界生成→退出 | 世界级数据（大地图） |

```csharp
// GameComponent 示例
[StaticConstructorOnStartup]
public class GameComponent_SR : GameComponent
{
    public static int totalItemsCrafted;

    public GameComponent_SR(Game game) { }

    public override void ExposeData()
    {
        base.ExposeData();
        Scribe_Values.Look(ref totalItemsCrafted, "totalItemsCrafted", 0);
    }
}
```

## DefModExtension——自定义 Def 扩展字段

当需要在 Def 中添加自定义数据字段时，使用 DefModExtension：

```csharp
using Verse;

public class DefModExtension_CustomWeapon : DefModExtension
{
    public float plasmaDamageBonus = 1.2f;
    public bool ignoresShield = true;
    public string customEffect = "PlasmaBurn";
}
```

XML 中使用：

```xml
<ThingDef ParentName="BaseMeleeWeapon">
  <defName>SR_PlasmaSword</defName>
  ...
  <modExtensions>
    <li Class="DefModExtension_CustomWeapon">
      <plasmaDamageBonus>1.5</plasmaDamageBonus>
      <ignoresShield>true</ignoresShield>
      <customEffect>PlasmaBurn</customEffect>
    </li>
  </modExtensions>
</ThingDef>
```

C# 中读取：

```csharp
var ext = weaponDef.GetModExtension<DefModExtension_CustomWeapon>();
if (ext?.ignoresShield == true)
{
    // 处理护盾穿透
}
```

## 编译与引用

1. 创建 **Class Library (.NET Framework 4.7.2)** 项目
2. 引用 DLL（见 `references/01-environment.md`）
3. 编译输出 DLL → 复制到 `Assemblies/`
4. 重启游戏加载

## 常见问题

### Q: ExposeData 没生效？
检查 key 字符串是否拼写正确，默认值是否与首次初始化一致。

### Q: ThingComp 不工作？
确认 `compClass` 指向正确的类，确认 XML 中 `Class=` 使用 `CompProperties_xxx` 类。

### Q: 编译报错找不到 Verse/RimWorld 类型？
确认引用了正确的 `Assembly-CSharp.dll` 路径。
