# 10 — API 速查表

> **适用版本**: RimWorld 1.7（实测 1.7.4981 rev136） | **最后更新**: 2026-10-18 | **状态**: 草稿——高频类与方法清单未逐条对照正式版核实；**「1.6 → 1.7 关键变化」一节已实测**，其余以 dnSpy 反编译的 `Assembly-CSharp.dll`（游戏安装根）和 RimSage 查询为准


## 目录

- [概述](#概述)
- [常用命名空间](#常用命名空间)
- [高频类速查](#高频类速查)
- [高频方法速查（按用途）](#高频方法速查按用途)
- [1.6 → 1.7 关键变化（已实测）](#16--17-关键变化已实测)
- [学习资源](#学习资源)

## 概述

本文档提供高频 API 的快速参考——只是速查表。

> **速查表 vs MCP**：速查表用于快速回忆已知信息。遇到不确定的字段/枚举/结构时，不要猜——用 RimSage MCP 查：
> - `search_rimworld_source("你的查询")` — 自然语言搜索
> - `get_def_details("defName")` — 看完整 Def 定义 + 继承链
> - `read_rimworld_file("路径")` — 看源文件全文

### 速查表查不到？直接用 MCP

如果某个类/方法不在本文档中，不要翻更多文档——直接用 MCP 搜索。

| 我想知道 | MCP 查询 |
|---------|---------|
| Thing 类有哪些 public 方法 | `search_rimworld_source("Thing class methods")` |
| CompProperties 有哪些子类 | `search_rimworld_source("CompProperties class")` |
| DamageDef 有哪些 | `search_rimworld_source("DamageDef Burn Cut")` |
| 某个方法的完整签名 | `search_rimworld_source("方法名 DamageInfo")` |

## 常用命名空间

| 命名空间 | 内容 |
|---------|------|
| `Verse` | 核心系统（Thing, Pawn, Map, GenSpawn, Log） |
| `RimWorld` | 游戏逻辑（Recipe, Research, Incident, JobDriver） |
| `RimWorld.Planet` | 世界地图（World, Caravan, Settlement, Site） |
| `HarmonyLib` | Harmony 补丁库 |

## 高频类速查

### Verse.Thing（所有实体的基类）

| 成员 | 说明 |
|------|------|
| `thing.def` | 返回 ThingDef |
| `thing.Position` | 在地图上的位置（IntVec3） |
| `thing.Map` | 所在的地图 |
| `thing.Spawned` | 是否已在地图上生成 |
| `thing.Destroy(DestroyMode)` | 销毁对象 |
| `thing.HitPoints` | 当前耐久值 |
| `thing.GetComp<T>()` | 获取指定 ThingComp |

### Verse.Pawn（角色/生物）

| 成员 | 说明 |
|------|------|
| `pawn.health` | Pawn_HealthTracker |
| `pawn.health.AddHediff(HediffDef)` | 添加健康效果 |
| `pawn.needs` | Pawn_NeedsTracker |
| `pawn.story` | 背景故事（人类专有） |
| `pawn.equipment` | Pawn_EquipmentTracker |
| `pawn.apparel` | Pawn_ApparelTracker |
| `pawn.def.defName` | 获取 Pawn 的 Def 名称 |

### Verse.Map（地图）

| 成员 | 说明 |
|------|------|
| `map.thingGrid.ThingsAt(IntVec3)` | 获取某格所有 Thing |
| `map.listerThings` | 按类型索引的 Thing 列表 |
| `map.weatherManager` | 天气管理 |
| `map.mapPawns` | 地图上所有 Pawn |

### Verse.Find（全局查询）

| 成员 | 说明 |
|------|------|
| `Find.CurrentMap` | 当前玩家所在的地图 |
| `Find.AnyThing<T>()` | 查找地图上任意一个 T 类型对象 |
| `Find.World` | 世界对象 |
| `Find.FactionManager` | 派系管理 |
| `Find.ResearchManager` | 研究管理 |

### Verse.GenSpawn（生成工具）

| 方法 | 说明 |
|------|------|
| `GenSpawn.Spawn(ThingDef, IntVec3, Map)` | 在指定位置生成 Thing |
| `GenSpawn.Spawn(Thing, IntVec3, Map)` | 将已有 Thing 放置到地图上 |

### Verse.GenRecipe（配方工具）

| 方法 | 说明 |
|------|------|
| `GenRecipe.PostProcessProduct(Thing, RecipeDef, Pawn)` | 配方产出的后处理 |

### RimWorld.QualityUtility（品质工具）

| 方法 | 说明 |
|------|------|
| `QualityUtility.GenerateQualityCreatedByPawn(Pawn)` | 根据角色技能生成品质 |
| `QualityUtility.SendCraftNotification(Thing, Pawn)` | 发送制作通知 |

## 高频方法速查（按用途）

### 生成与放置
```csharp
Thing thing = ThingMaker.MakeThing(ThingDef.Named("SR_PlasmaSword"));
GenSpawn.Spawn(thing, Position, Map);

Pawn pawn = PawnGenerator.GeneratePawn(PawnKindDef.Named("SR_CustomPawn"), Faction.OfPlayer);
GenSpawn.Spawn(pawn, Position, Map);
```

### 查询
```csharp
// 查找地图上所有指定 Def 的 Thing
List<Thing> things = Map.listerThings.ThingsOfDef(ThingDef.Named("SR_PlasmaSword"));

// 查找范围内所有 Pawn
IEnumerable<Pawn> pawns = Map.mapPawns.AllPawnsSpawned.Where(p => p.Position.InHorDistOf(center, radius));
```

### 伤害与战斗
```csharp
DamageInfo dinfo = new DamageInfo(DamageDefOf.Cut, amount: 10, armorPenetration: 0.3f);
pawn.TakeDamage(dinfo);
```

### 日志
```csharp
Log.Message($"SR: Normal message");
Log.Warning($"SR: Warning - {variable}");
Log.Error($"SR: Error - {ex.Message}\n{ex.StackTrace}");
```

## 1.6 → 1.7 关键变化（已实测）

> ✅ 本节是**在本机 1.7.4981 rev136 上真机编译 + 元数据/DLL 反射核对**得到的，不是"待复核"。
> 完整证据与账本见 `examples/rimtest-mod/_FINDINGS.md`。

| 变化 | 说明（1.7 现实） |
|------|------|
| 引擎 | Unity 被自研 **Waylith** 替换；游戏根目录出现 `Waylith*.dll`、`UnityStubs.dll`，**不再有 `ReactUnity`/`UnityEngine.dll`/`RimWorldWin64_Data`** |
| 目标框架 | **net10.0**（1.6 的 .NET Framework 4.7.2 / Unity 2022.3.35 引用全部作废） |
| 引用 DLL | `Assembly-CSharp.dll` + `RimWorld.dll` + `UnityStubs.dll`，三个都在**安装根目录** |
| Harmony | 升到 **3.0**：`HarmonyMethod` 没有 `id` 字段了；游戏本体**不自带** 0Harmony（由创意工坊 Harmony mod 提供） |
| `DamageInfo` | `Amount` / `armorPenetration` 变**只读**，改用 `dinfo.SetAmount(x)` |
| `Messages.Message` | 第二参数是 `LookTargets`（`new LookTargets(thing)` 或 `LookTargets.Invalid`），末尾 `historical` 一般传 `false` |
| UI 类命名空间 | `Command_Action` 在 **`Verse`**（`RimWorld.Command_Action` 不存在）；`MessageTypeDefOf` 也在 `Verse`，位于 `Assembly-CSharp.dll` |
| `LoadFolders.xml` | 版本块写法不变，只是把 `<v1.6>` 换成 `<v1.7>`（详见 `references/02-project-structure.md`）；内容与 1.6 完全一致，1.7 没有强制新字段 |
| 原版资产 | 从散装 `Data/Core/Textures` 改为安装根 `Assets.zip`（内部为 `.dds`，Zstd 压缩）——只影响你**查看**原版贴图，不影响 mod 资源写法 |

**建议**：不在上表里的 API，引用前先在 `Assembly-CSharp.dll`（安装根，dnSpy 或 `Select-String -Encoding utf8`）确认一次。

## 学习资源

- **查看原版实现**：`RimWorld/Data/Core/Defs/` 中的 XML 和 dnSpy 反编译的 C#
- **RimSage MCP**：自然语言搜索源码
- **Harmony Wiki**：https://github.com/pardeike/Harmony/wiki
- **RimWorld Wiki**：https://rimworldwiki.com/wiki/Modding_Tutorials
