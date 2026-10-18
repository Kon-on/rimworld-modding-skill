# WorldObjectDef

## 用途

WorldObjectDef 定义星球视图上的"物件"：据点、商队、坠毁飞船、地标、临时营地、飞船残骸、任务地点等。它决定这个东西**在地图上怎么画**（`texture` / `expandingIcon*`）、**是不是一张可进入的地图**（`worldObjectClass` + `mapGenerator` + `canHaveMap`）、**能发生哪些事件**（`IncidentTargetTags`）、以及**带哪些行为组件**（`comps`）。它与 IncidentDef 的 `targetTags` 成对出现：WorldObjectDef 声明"我提供哪些标签"，IncidentDef 声明"我要在哪些标签上发生"。

> 本类型是少见的高自由度 Def：字段参考里**没有出现率 ≥90% 的字段**（实例只有 38 个，字段 36 条），所以下面模板给的是"能跑起来的最小组合"，而不是"照抄率最高的写法"。

## 模板

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Defs>

  <!-- 一个自定义世界物件：地图上可见、可进入、能被事件选中的遗迹营地。
       worldObjectClass 是 C# 类名（本体 Assembly-CSharp.dll），这里复用原版 Site，
       所以它天然具备"进入后生成地图、可被任务/事件指向"的行为。 -->
  <WorldObjectDef ParentName="StaticWorldObjectBase">
    <defName>EXAMPLE_WeatheredOutpost</defName>
    <label>weathered outpost</label>
    <description>一座被风沙埋了半截的旧哨所。塔楼还立着，但里面早就没人了。</description>

    <!-- C# 类名：决定这个物件的行为（原版值：Site / Caravan / Settlement / AbandonedSettlement ...） -->
    <worldObjectClass>Site</worldObjectClass>

    <!-- 星球视图上的绘制 -->
    <texture>World/WorldObjects/Camp</texture>
    <expandingIcon>true</expandingIcon>
    <expandingIconTexture>World/WorldObjects/Expanding/Camp</expandingIconTexture>
    <expandingIconPriority>85</expandingIconPriority>
    <expandMore>true</expandMore>

    <!-- 可被玩家当临时据点使用 -->
    <isTempIncidentMapOwner>true</isTempIncidentMapOwner>
    <canBePlayerHome>true</canBePlayerHome>

    <!-- 进入后生成的地图尺寸（长, 高, 宽 三元组写法，原版样例 (200, 1, 200)） -->
    <overrideMapSize>(200, 1, 200)</overrideMapSize>

    <!-- 提供哪些事件标签：IncidentDef 的 targetTags 要靠它才落得下来 -->
    <IncidentTargetTags>
      <li>Map_Misc</li>
    </IncidentTargetTags>

    <!-- 行为组件：Class 是 C# 类名 -->
    <comps>
      <li Class="WorldObjectCompProperties_Timeout" />
      <li Class="WorldObjectCompProperties_FormCaravan" />
      <li Class="WorldObjectCompProperties_TimedDetectionRaids" />
    </comps>
  </WorldObjectDef>

</Defs>
```

## 字段说明

| 字段 | 出现率 | 值类型 | 说明 |
|---|---|---|---|
| `defName` | 86.8% (33/38) | 文本 | 唯一标识 |
| `label` | 89.5% (34/38) | 文本 | 显示名（原版全小写） |
| `description` | 57.9% (22/38) | 文本 | 描述文本 |
| `worldObjectClass` | 68.4% (26/38) | 文本 | **C# 类名**，决定行为（原版样例 Caravan / Settlement / AbandonedSettlement） |
| `texture` | 44.7% (17/38) | 文本 | 主贴图路径 |
| `expandingIcon` | 42.1% (16/38) | 布尔 | 是否在地图上放大显示为图标 |
| `expandingIconTexture` | 47.4% (18/38) | 文本 | 放大图标贴图 |
| `expandingIconPriority` | 39.5% (15/38) | 数值 | 图标重叠时的优先级（原版样例 10 / 20 / 100） |
| `expandingIconDrawSize` / `expandingIconColor` / `expandingIconMaskTexture` / `expandingShader` | 18.4% / 10.5% / 2.6% / 2.6% | 数值/文本 | 图标尺寸、颜色、遮罩、着色器 |
| `expandMore` | 18.4% (7/38) | 布尔 | 是否参与"展开更多"聚合显示 |
| `useDynamicDrawer` | 15.8% (6/38) | 布尔 | 用动态绘制（移动中的物件，如商队） |
| `comps/li` | 76.3% (29/38) | 容器 | 行为组件列表，写法 `<li Class="…" />` |
| `IncidentTargetTags/li` | 26.3% (10/38) | 文本 | 提供的事件地点标签（原版样例 Caravan / Map_Misc / Map_PlayerHome） |
| `inspectorTabs/li` | 23.7% (9/38) | 文本 | **C# 类名**（WITab_*，原版样例 WITab_Terrain / WITab_Planet / WITab_Orbit） |
| `canBePlayerHome` | 21.1% (8/38) | 布尔 | 能否作为玩家据点 |
| `canHaveMap` | 10.5% (4/38) | 布尔 | 能否进入（原版样例 false） |
| `mapGenerator` | 31.6% (12/38) | 文本 | MapGeneratorDef defName（原版样例 EscapeShip / BasePlayer_SecondArchonexusCycle） |
| `nameMaker` | 7.9% (3/38) | 文本 | RulePackDef defName，生成物件名（原版样例 NamerWorldObject_AsteroidBasic） |
| `overrideMapSize` | 10.5% (4/38) | 文本 | 覆盖地图尺寸，`(长, 1, 宽)`（原版样例 (200, 1, 200)） |
| `isTempIncidentMapOwner` | 7.9% (3/38) | 布尔 | 是否是临时事件地图（事件用完即弃） |
| `treatAsPlayerHome` | 7.9% (3/38) | 布尔 | 是否被当作玩家据点对待 |
| `validLaunchTarget` | 7.9% (3/38) | 布尔 | 能否作为发射目标（原版样例 false） |
| `allowCaravanIncidentsWhichGenerateMap` | 10.5% (4/38) | 布尔 | 是否允许会生成地图的商队事件 |
| `fullyExpandedInSpace` | 13.2% (5/38) | 布尔 | 在太空中是否始终完全展开 |
| `saved` | 2.6% (1/38) | 布尔 | 是否存档（原版 `RoutePlannerWaypoint` 用 false） |
| `drawAltitudeOffset` | 2.6% (1/38) | 数值 | 绘制高度偏移（原版样例 0.01） |
| `neverMultiSelect` / `requiresSignalJammerToReach` / `canResizeToGravship` / `blockExitGridUntilBattleIsWon` | 2.6%~5.3% | 布尔 | 单实例开关 |

## 常见坑

1. **`worldObjectClass` 是 C# 类名，不是 defName**，而且本类型没有"纯 XML 也能干活"的通用类：填错会直接导致物件行为异常或报错。可复用的原版类包括 `Site`、`Caravan`、`Settlement`、`AbandonedSettlement`、`EscapeShip`、`Camp`、`TravellingTransporters`、`RoutePlannerWaypoint`、`PocketMapParent`、`PeaceTalks`、`CaravansBattlefield`。
2. **`comps` 的 `Class` 是结构化属性**（类似 `ParentName`），写法必须是 `<li Class="WorldObjectCompProperties_Timeout" />`。可用类实测有 14 个：`Abandon`、`DebugArena`、`DefeatAllEnemiesQuest`、`DownedRefugee`、`EnterCooldown`、`EscapeShip`、`FormCaravan`、`ItemStashContents`、`PrisonerWillingToJoin`、`TimedDetectionRaids`、`TimedForcedExit`、`TimedMakeFactionHostile`、`Timeout`、`TradeRequest`。
3. **`IncidentTargetTags` 要和 IncidentDef 的 `targetTags` 成对写。** 只在地图（`Map_PlayerHome`）发生的事件被指到一个世界物件上，或者物件没提供事件所需的标签，结果都是"事件永远不触发"而不是报错——这是排查事件不动时最容易漏的一环（对照 `02-IncidentDef.md`）。
4. **`inspectorTabs` 也是 C# 类名**（原版 `WITab_Terrain` / `WITab_Planet` / `WITab_Orbit` 来自 `StaticWorldObjectBase`；商队用 `WITab_Caravan_*` 系列）。本模板直接继承 `StaticWorldObjectBase` 拿到通用三个页签。
5. **`canHaveMap` 与 `worldObjectClass` 要匹配**：原版 `AbandonedSettlement` 用 `canHaveMap=false`（不可进入），`Site` 默认可进入。给一个默认要生成地图的类硬关掉 `canHaveMap` 会发生什么【待验证】，本次未启动游戏验证。
6. **`overrideMapSize` 是三元组文本** `(200, 1, 200)`，不是三个子元素；原版 `(200,1,200)` 与 `(200, 1, 200)` 两种写法都有。
7. **`nameMaker` 指向 RulePackDef**（不是"NameMakerDef"，本体没有这个 Def 类型），原版样例 `NamerWorldObject_AsteroidBasic` 定义在 `Odyssey/Defs/RulePackDefs/RulePacks_Namers_OrbitalLocations.xml`。

## 核验

- **字段合法性**：逐条对照 `library/03-全量字段参考/字段/WorldObjectDef.md` 的「全量字段表（36 条路径）」；该文件同时给出"没有出现率≥90% 的字段"这一结论，本模板据此明确标注为"最小可跑组合"。
- **原版写法依据**（相对 `E:\SteamLibrary\steamapps\common\RimWorld\Data\`）：
  - `Core/Defs/WorldObjectDefs/WorldObjects.xml`：`StaticWorldObjectBase`（父定义：三个 inspectorTabs）、`Site`（本模板骨架：worldObjectClass + expandingIcon + comps + IncidentTargetTags）、`Camp`（`overrideMapSize`、`isTempIncidentMapOwner`、`texture`、`expandingIconTexture` 的真实写法）、`Caravan`、`AttackedNonPlayerCaravan`、`RoutePlannerWaypoint`（`saved=false`、`drawAltitudeOffset`）、`Settlement`（`canBePlayerHome`、`comps`）。
  - `Odyssey/Defs/WorldObjectDefs/WorldObjects.xml`：`nameMaker` 用法与 `AsteroidMiningSite`。
  - `Royalty/Defs/WorldObjectDefs/WorldObjects.xml`、`Ideology/Defs/WorldObjectDefs/WorldObjects.xml`、`Core/Defs/Storyteller/Incidents_Caravan_All.xml`（内嵌 WorldObjectDef 的写法）。
- **类名核验**：`WorldObjectCompProperties_Timeout`、`WorldObjectCompProperties_FormCaravan`、`WorldObjectCompProperties_TimedDetectionRaids`、`WITab_Terrain`、`WITab_Planet`、`WITab_Orbit` 均已在本体 `Assembly-CSharp.dll` 中命中字符串。
- **跨 Def 引用**：`MapGeneratorDef EscapeShip` / `BasePlayer_SecondArchonexusCycle`、`RulePackDef NamerWorldObject_AsteroidBasic`、`IncidentTargetTagDef Map_Misc / Map_PlayerHome / Caravan / Map_TempIncident` 均已通过扫描本体 `Data/**/Defs/**/*.xml` 建立类型索引后比对通过。注意 `nameMaker` 的目标类型实测为 **RulePackDef**（schema 中不存在 NameMakerDef）。
- **贴图**：`World/WorldObjects/Camp`、`World/WorldObjects/Expanding/Camp` 已在本体 `Assets.zip` 中命中。
