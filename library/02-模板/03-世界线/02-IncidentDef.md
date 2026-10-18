# IncidentDef

## 用途

IncidentDef 是"事件"的定义：故事叙述者按 `baseChance` / `mtbDaysByBiome` 等权重抽取它，满足 `targetTags`、`earliestDay`、`minRefireDays` 等条件后交给 `workerClass` 执行。它上接 IncidentCategoryDef（分类）、IncidentTargetTagDef（可发生地点），下联 GameConditionDef（天气/环境条件）、LetterDef（信件）、TaleDef（编年史）、QuestScriptDef（任务）、PawnKindDef（指定兵种）。想做"每 N 天来一次的事"，先看是不是用现成 worker 就能拼出来。

## 模板

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Defs>

  <!-- ① 环境条件型事件：复用原版 worker，不需要写 C#。
       它在玩家地图上挂一个 GameConditionDef，持续 durationDays 天后结束。 -->
  <IncidentDef>
    <defName>EXAMPLE_ToxicBloom</defName>
    <label>toxic bloom</label>
    <category>Misc</category>

    <!-- 能发生的地点标签（IncidentTargetTagDef；要与 WorldObjectDef.IncidentTargetTags 对得上） -->
    <targetTags>
      <li>Map_PlayerHome</li>
    </targetTags>

    <!-- workerClass 是 C# 类名（Assembly-CSharp.dll），不是 defName -->
    <workerClass>IncidentWorker_MakeGameCondition</workerClass>
    <gameCondition>ToxicFallout</gameCondition>

    <!-- 来信内容 -->
    <letterLabel>Toxic bloom</letterLabel>
    <letterDef>ThreatSmall</letterDef>
    <letterText>一股刺鼻的孢子云正在从海岸方向涌来，暴露在外的人和动物都会中毒。</letterText>

    <!-- 抽取权重与门槛 -->
    <baseChance>0.12</baseChance>
    <earliestDay>60</earliestDay>
    <minRefireDays>90</minRefireDays>
    <durationDays>2.5~10.5</durationDays>

    <!-- 玩家在世界创建界面关掉"极端天气"时，本事件一并禁用 -->
    <disabledWhen>
      <extremeWeatherIncidentsDisabled>true</extremeWeatherIncidentsDisabled>
    </disabledWhen>

    <tale>ToxicFallout</tale>
    <canOccurOnAllPlanetLayers>true</canOccurOnAllPlanetLayers>
  </IncidentDef>

  <!-- ② 只对商队生效的事件：用 mtbDaysByBiome 按生物群系给出"平均间隔天数" -->
  <IncidentDef>
    <defName>EXAMPLE_CaravanPowwow</defName>
    <label>caravan powwow</label>
    <category>Misc</category>
    <targetTags>
      <li>Caravan</li>
      <li>Map_TempIncident</li>
    </targetTags>
    <workerClass>IncidentWorker_CaravanMeeting</workerClass>
    <minRefireDays>0.17</minRefireDays>
    <tale>CaravanMeeting</tale>
    <mtbDaysByBiome>
      <TemperateForest>10</TemperateForest>
      <BorealForest>10</BorealForest>
      <AridShrubland>10</AridShrubland>
      <TropicalRainforest>10</TropicalRainforest>
      <Desert>15</Desert>
      <Tundra>15</Tundra>
      <TropicalSwamp>15</TropicalSwamp>
      <TemperateSwamp>15</TemperateSwamp>
      <ColdBog>25</ColdBog>
      <ExtremeDesert>25</ExtremeDesert>
      <IceSheet>35</IceSheet>
      <SeaIce>80</SeaIce>
    </mtbDaysByBiome>
  </IncidentDef>

</Defs>
```

## 字段说明

| 字段 | 出现率 | 值类型 | 说明 |
|---|---|---|---|
| `defName` | 94.2% (131/139) | 文本 | 唯一标识 |
| `label` | 93.5% (130/139) | 文本 | 内部名（全小写），玩家看不到 |
| `workerClass` | 79.9% (111/139) | 文本 | C# 类名：决定这个事件真正干什么 |
| `category` | 74.1% (103/139) | 文本 | IncidentCategoryDef defName（原版：Misc / ThreatBig / Special 等） |
| `targetTags` / `targetTags/li` | 72.7% (101/139) / 85.6% (119/139) | 容器 / 文本 | 可发生地点标签（IncidentTargetTagDef） |
| `baseChance` | 72.7% (101/139) | 数值 | 抽取基础权重（原版样例 0.2 / 0.5 / 0.75 / 1.0 / 7.4） |
| `minRefireDays` | 36.7% (51/139) | 数值 | 触发后多少天内不再触发；可为小数（原版 `CaravanMeeting` 用 0.17） |
| `letterLabel` | 54.0% (75/139) | 文本 | 信件标题 |
| `letterDef` | 36.7% (51/139) | 文本 | LetterDef defName（ThreatBig / ThreatSmall / PositiveEvent / NeutralEvent） |
| `letterText` | 28.8% (40/139) | 文本 | 信件正文 |
| `earliestDay` | 19.4% (27/139) | 数值 | 开局第几天之后才可能出现（原版样例 15 / 30 / 45 / 60） |
| `durationDays` | 12.2% (17/139) | 文本 | 持续天数，`min~max`（原版样例 `1~3`、`2.5~10.5`） |
| `gameCondition` | 12.2% (17/139) | 文本 | GameConditionDef defName：挂到地图上的环境条件 |
| `tale` | 18.0% (25/139) | 文本 | TaleDef defName：会写进编年史 |
| `pointsScaleable` | 19.4% (27/139) | 布尔 | 强度是否随袭击点数缩放 |
| `minThreatPoints` | 12.2% (17/139) | 数值 | 最低袭击点数门槛（原版样例 200 / 250 / 300） |
| `disabledWhen/extremeWeatherIncidentsDisabled` | 6.5% (9/139) | 布尔 | 玩家关掉极端天气时一并禁用 |
| `mtbDaysByBiome/<BiomeDef>` | 2.9% (4/139) | 数值 | 按生物群系给平均间隔天数 |
| `allowedBiomes/li` / `disallowedBiomes/li` | 15.1% (21/139) / 1.4% (2/139) | 文本 | 白/黑名单生物群系（BiomeDef defName） |
| `requireColonistsPresent` | 11.5% (16/139) | 布尔 | 是否有殖民者在地图上才可能发生 |
| `pointsScaleable` | 19.4% (27/139) | 布尔 | 见上 |
| `canOccurOnAllPlanetLayers` | 9.3% (13/139) | 布尔 | 是否在所有星球层（地表/轨道等）都可能发生 |
| `hidden` | 2.9% (4/139) | 布尔 | 不出现在调试/列表 UI |
| `ignoreRecentSelectionWeighting` | 2.2% (3/139) | 布尔 | 不受"最近抽过"的降权影响（原版 `RaidEnemy` 用 true） |
| `questScriptDef` | 17.3% (24/139) | 文本 | QuestScriptDef defName：转成任务 |
| `pawnKind` | 2.2% (3/139) | 文本 | 指定刷出的 PawnKindDef |
| `refireCheckTags/li` | 3.6% (5/139) | 文本 | 与其它事件的互斥/冷却标签 |
| `minAnomalyThreatLevel` | 20.9% (29/139) | 数值 | Anomaly：异常威胁等级门槛 |
| `diseaseIncident` | 9.3% (13/139) | 文本 | 疾病事件的 IncidentDef（原版样例 Flu / Malaria / Plague） |

## 常见坑

1. **`workerClass` 是 C# 类名，不是 defName，也不是随便起的字符串。** 纯 XML 的 mod 只能复用原版已有的 worker：本次在本体 `Assembly-CSharp.dll` 中实测存在 96 个 `IncidentWorker_*` 类，例如 `IncidentWorker_MakeGameCondition`、`IncidentWorker_ResourcePodCrash`、`IncidentWorker_CaravanMeeting`、`IncidentWorker_MeteoriteImpact`、`IncidentWorker_ShortCircuit`。要写自己的逻辑必须编译程序集。
2. **`category` 必须命中 IncidentCategoryDef。** 原版共 13 个（见 `Core/Defs/Misc/IncidentCategoryDefs/IncidentCategoryDefs.xml`）：`Special`、`Misc`、`ThreatSmall`、`ThreatBig`、`FactionArrival`、`OrbitalVisitor`、`ShipChunkDrop`、`DiseaseHuman`、`DiseaseAnimal`、`AllyAssistance`、`EndGame_ShipEscape`、`GiveQuest`、`DeepDrillInfestation`。写错或留空的具体表现【待验证】：未启动游戏实测。
3. **`targetTags` 要和 WorldObjectDef 的 `IncidentTargetTags` 对得上**（例如地图上发生的事件用 `Map_PlayerHome`／`Map_Misc`，商队用 `Caravan`，临时地图用 `Map_TempIncident`）。对不上的后果不是报错而是"永远不触发"，很难查；原版对应关系见 `06-WorldObjectDef.md`。
4. **`baseChance` 与 `mtbDaysByBiome` 是两套抽取模型。** 原版 `CaravanMeeting` 只给 `mtbDaysByBiome` 而不写 `baseChance`；两者同时写会不会叠加【待验证】——本次没有启动游戏做权重实验。用法上建议二选一。
5. **`gameCondition` / `durationDays` 需要配套的 worker 才生效**（原版 `ToxicFallout`、`VolcanicWinter` 都用 `IncidentWorker_MakeGameCondition`）。把它们挂到别的 worker 上不会报错，但也不会有你期待的效果【推测】。
6. **`gameCondition` 是 GameConditionDef 的 defName，不是 WeatherDef。** 想要"某种天气"应该改 BiomeDef 的 `baseWeatherCommonalities`（见 `04-BiomeDef.md`），或让事件去挂 GameConditionDef。
7. **`letterText` 里不要写未经转义的 XML 特殊字符**，段落分隔用 `\n`（原版大量使用，例如 `Anomaly/Defs/Storyteller/Incidents_Map_Misc.xml`）。

## 核验

- **字段合法性**：逐条对照 `library/03-全量字段参考/字段/IncidentDef.md` 的「全量字段表（70 条路径）」，模板中所有元素名均能在表中找到。
- **原版写法依据**（相对 `E:\SteamLibrary\steamapps\common\RimWorld\Data\`）：
  - `Core/Defs/Storyteller/Incidents_Map_Misc.xml`：`ToxicFallout`（category / targetTags / workerClass / gameCondition / letterLabel / letterDef / baseChance / earliestDay / minRefireDays / disabledWhen / durationDays / tale 的完整真实写法）、`ShortCircuit`、`ResourcePodCrash`、`PsychicSoothe`。
  - `Core/Defs/Storyteller/Incidents_Caravan_All.xml`：`CaravanMeeting`（`mtbDaysByBiome` 的 12 个生物群系键与取值）。
  - `Core/Defs/Storyteller/Incidents_Map_Threats.xml`：`RaidEnemy`（`pointsScaleable`、`ignoreRecentSelectionWeighting`）。
  - `Anomaly/Defs/Storyteller/Incidents_Map_Misc.xml`：`DeathPall`（`minAnomalyThreatLevel`、`ParentName="AnomalyIncidentBase"`）。
- **跨 Def 引用**：`IncidentWorker_MakeGameCondition` / `IncidentWorker_CaravanMeeting` 已在本体 `Assembly-CSharp.dll` 中命中；`GameConditionDef ToxicFallout`、`TaleDef ToxicFallout`、`TaleDef CaravanMeeting`、`LetterDef ThreatSmall`、`IncidentCategoryDef Misc`、`IncidentTargetTagDef Map_PlayerHome / Caravan / Map_TempIncident` 均已在本体 `Data/**/Defs/**` 中核验存在（扫描全部原版 XML 建立类型索引后比对）。
- **生物群系键**：`TemperateForest` … `SeaIce` 这 12 个键均为原版 BiomeDef defName（对照 `Core/Defs/BiomeDefs/*.xml`）。
