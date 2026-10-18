# WeatherDef

## 用途

WeatherDef 定义一种天气：地面降雨/降雪速率、移动与射击惩罚、天空四时段配色、环境音、覆盖层（雨丝、雾）与随机天气事件（闪电）。它由 BiomeDef 的 `baseWeatherCommonalities` 决定在某个生物群系里出现的相对频率，由 GameConditionDef 或 IncidentDef 改变或强制。改天气的配比要去 BiomeDef，改天气本身的样子才写它。

## 模板

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Defs>

  <!-- 一场带闪电的雷雨：结构照抄原版 RainyThunderstorm，换皮换数值即可。
       注意 overlayClasses / eventMakers.eventClass 填的是 C# 类名（本体 Assembly-CSharp.dll），
       纯 XML mod 只能复用原版已有的类。 -->
  <WeatherDef>
    <defName>EXAMPLE_SaltStorm</defName>
    <label>salt storm</label>
    <description>咸腥的暴雨裹着闪电压过海面。闪电会点燃地面，好在雨很快就把它浇灭；射击精度和移动速度都会下降。</description>

    <isBad>true</isBad>
    <favorability>Bad</favorability>
    <perceivePriority>2</perceivePriority>

    <!-- 只在 0~999℃ 的温度区间内出现 -->
    <temperatureRange>0~999</temperatureRange>
    <rainRate>1</rainRate>
    <windSpeedFactor>1.5</windSpeedFactor>
    <windSpeedOffset>1.25</windSpeedOffset>
    <accuracyMultiplier>0.8</accuracyMultiplier>
    <moveSpeedMultiplier>0.8</moveSpeedMultiplier>

    <!-- 会在小人身上留下的心情来源（ThoughtDef） -->
    <weatherThought>SoakingWet</weatherThought>

    <!-- 环境音（SoundDef） -->
    <ambientSounds>
      <li>Ambient_Wind_Storm</li>
      <li>Ambient_Rain</li>
    </ambientSounds>

    <!-- 天气持续时间范围，单位 tick（15000 tick ≈ 6 小时） -->
    <durationRange>15000~40000</durationRange>

    <!-- 随机天气事件：平均 1200 tick 一次闪电（类名来自本体程序集） -->
    <eventMakers>
      <li>
        <averageInterval>1200</averageInterval>
        <eventClass>WeatherEvent_LightningFlash</eventClass>
      </li>
      <li>
        <averageInterval>1200</averageInterval>
        <eventClass>WeatherEvent_LightningStrike</eventClass>
      </li>
    </eventMakers>

    <!-- 视觉覆盖层（C# 类名） -->
    <overlayClasses>
      <li>WeatherOverlay_Rain</li>
    </overlayClasses>

    <!-- 降雨量 → 该天气出现频率：这里是线性增长，雨越多越常来 -->
    <commonalityRainfallFactor>
      <points>
        <li>(0, 0)</li>
        <li>(1300, 1)</li>
        <li>(4000, 2.0)</li>
      </points>
    </commonalityRainfallFactor>

    <!-- 天空配色：四个时段各一组，值域 0~1 -->
    <skyColorsDay>
      <sky>(0.8,0.8,0.8)</sky>
      <shadow>(0.92,0.92,0.92)</shadow>
      <overlay>(0.7,0.7,0.7)</overlay>
      <saturation>0.9</saturation>
    </skyColorsDay>
    <skyColorsDusk>
      <sky>(1,1,1)</sky>
      <shadow>(0.92,0.92,0.92)</shadow>
      <overlay>(0.6,0.6,0.6)</overlay>
      <saturation>0.9</saturation>
    </skyColorsDusk>
    <skyColorsNightEdge>
      <sky>(0.35,0.40,0.45)</sky>
      <shadow>(0.92,0.92,0.92)</shadow>
      <overlay>(0.5,0.5,0.5)</overlay>
      <saturation>0.9</saturation>
    </skyColorsNightEdge>
    <skyColorsNightMid>
      <sky>(0.35,0.40,0.45)</sky>
      <shadow>(0.92,0.92,0.92)</shadow>
      <overlay>(0.5,0.5,0.5)</overlay>
      <saturation>0.9</saturation>
    </skyColorsNightMid>
  </WeatherDef>

</Defs>
```

## 字段说明

| 字段 | 出现率 | 值类型 | 说明 |
|---|---|---|---|
| `defName` | 96.0% (24/25) | 文本 | 唯一标识；BiomeDef 的 `baseWeatherCommonalities` 用它当键 |
| `label` | 92.0% (23/25) | 文本 | 内部名（小写） |
| `description` | 88.0% (22/25) | 文本 | 描述文本 |
| `favorability` | 80.0% (20/25) | 文本 | `Good` / `Neutral` / `Bad`，影响观感与部分判定 |
| `perceivePriority` | 84.0% (21/25) | 数值 | 同时满足多天气时谁优先（原版样例 0 / 1 / 2） |
| `ambientSounds/li` | 96.0% (24/25) | 文本 | SoundDef defName，可多条 |
| `accuracyMultiplier` | 56.0% (14/25) | 数值 | 射击精度乘数（原版样例 0.5 / 0.7 / 0.75 / 0.8） |
| `moveSpeedMultiplier` | 40.0% (10/25) | 数值 | 移动速度乘数（原版样例 0.7 / 0.8 / 0.9） |
| `windSpeedFactor` | 60.0% (15/25) | 数值 | 风速乘数（原版样例 0.5 / 1.5） |
| `windSpeedOffset` | 20.0% (5/25) | 数值 | 风速加值（原版样例 1.25 / 1.5） |
| `rainRate` | 36.0% (9/25) | 数值 | 降雨强度（原版样例 1） |
| `snowRate` | 12.0% (3/25) | 数值 | 降雪强度（原版样例 0.8 / 1.2 / 1.5） |
| `sandRate` | 4.0% (1/25) | 数值 | 扬沙强度（原版样例 1.6） |
| `temperatureRange` | 40.0% (10/25) | 文本 | `min~max`，气温不在区间内则不会出现（原版样例 `0~100`、`0~999`） |
| `weatherThought` | 36.0% (9/25) | 文本 | ThoughtDef defName（原版样例 SoakingWet / DeathPall / GrayPall） |
| `overlayClasses/li` | 72.0% (18/25) | 文本 | **C# 类名**（原版样例 WeatherOverlay_Rain / WeatherOverlay_BloodFog） |
| `eventMakers/li/eventClass` | 16.0% (4/25) | 文本 | **C# 类名**（原版样例 WeatherEvent_LightningFlash / WeatherEvent_LightningStrike） |
| `eventMakers/li/averageInterval` | 16.0% (4/25) | 数值 | 平均间隔 tick（原版样例 1200） |
| `durationRange` | 12.0% (3/25) | 文本 | 持续 tick 范围（原版样例 `15000~40000`、`30000~90000`） |
| `letterDef` / `letterLabel` / `letterText` | 12.0% (3/25) | 文本 | 天气开始时发的信（LetterDef defName + 标题 + 正文） |
| `commonalityRainfallFactor/points/li` | 124.0% (31/25) | 文本 | 曲线点 `(降雨量, 频率)` |
| `skyColorsDay` 等四组 | 88.0% (22/25) | 容器 | 白天/黄昏/夜缘/子夜四时段配色 |
| `skyColorsDay/sky`、`shadow`、`overlay` | 88.0% (22/25) | 文本 | 三个颜色值，`(r,g,b)` 0~1 |
| `skyColorsDay/saturation` | 88.0% (22/25) | 数值 | 饱和度（原版样例 0.5 / 0.75 / 0.9 / 1.25） |
| `isBad` | 40.0% (10/25) | 布尔 | 是否算恶劣天气 |
| `repeatable` | 16.0% (4/25) | 布尔 | 是否可重复（原版 `Clear` 用 true） |
| `workerClass` | 4.0% (1/25) | 文本 | C# 类名，仅原版 `TorrentialRain`（`WeatherWorker_TorrentialRain`）使用 |
| `canOccurAsRandomForcedEvent` | 16.0% (4/25) | 布尔 | 是否可被随机强制触发（原版样例 false） |
| `preventsShuttleLaunch` | 12.0% (3/25) | 布尔 | 是否阻止穿梭机起飞 |
| `transitionTicksOverride` | 8.0% (2/25) | 数值 | 覆盖天气切换过渡时长（原版样例 600） |
| `maxGlow` / `doToxicBuildup` / `preventSkygaze` | 4.0% (1/25) | 数值/布尔 | 单实例字段（Anomaly 等专用） |

## 常见坑

1. **`overlayClasses` 与 `eventMakers.eventClass` 填的是 C# 类名，不是 Def 名。** 证据：`WeatherOverlay_Rain` 在全本体 XML 中只出现一次（`Core/Defs/WeatherDefs/Weathers.xml` 里 `Rain` 的 `overlayClasses`），从来没有被任何 Def 定义过；而它在本体 `Assembly-CSharp.dll` 中以类的形式存在（同类还有 `WeatherOverlay_SnowHard`、`WeatherOverlay_NoxiousHaze` 等 20 个，`WeatherEvent_LightningFlash` 等 3 个）。所以纯 XML 的 mod 只能用原版已有的覆盖层/事件类。
2. **只写 WeatherDef 不会让它在地图上出现。** 出现概率由 BiomeDef 的 `baseWeatherCommonalities/<WeatherDef>` 决定（见 `04-BiomeDef.md`）。
3. **四个时段配色建议全给。** `skyColorsDay` / `skyColorsDusk` / `skyColorsNightEdge` / `skyColorsNightMid` 的出现率同为 88.0%（22/25）。只给一部分会怎样【待验证】：本次未启动游戏对比渲染结果，但从原版一致性推断其余时段会退回默认色。
4. **`temperatureRange` 是 `min~max` 字符串**（`0~100`、`-999~-0.5`），不是两个子元素。写反了区间（min > max）不会报错但永不出现【推测】。
5. **`durationRange` 单位是 tick**（60 tick = 1 秒；原版 `15000~40000` 约 6~17 小时），不是天。写成天数会得到一场几乎瞬间结束的天气【推测：基于 tick 换算与 `PsychicSoothe` 用"天"的对比】。
6. **想替换原版某种天气（而不是新增）** 的原版做法是 `Inherit` 或同名覆盖；本模板采用新增 `EXAMPLE_` 前缀的独立天气，不影响原版 `Rain` / `RainyThunderstorm`。

## 核验

- **字段合法性**：逐条对照 `library/03-全量字段参考/字段/WeatherDef.md` 的「全量字段表（61 条路径）」。
- **原版写法依据**（相对 `<游戏安装目录>\Data\`）：
  - `Core/Defs/WeatherDefs/Weathers.xml`：`RainyThunderstorm`（本模板的主要骨架：isBad / temperatureRange / windSpeedFactor / windSpeedOffset / favorability / perceivePriority / weatherThought / accuracyMultiplier / rainRate / moveSpeedMultiplier / ambientSounds / durationRange / eventMakers / overlayClasses / commonalityRainfallFactor / 四组 skyColors）、`Rain`、`Clear`。
  - `Odyssey/Defs/WeatherDefs/Weathers.xml`：`TorrentialRain`（唯一使用 `workerClass` 的实例，以及 `letterDef`/`letterLabel`/`letterText` 的真实写法）。
  - `Anomaly/Defs/WeatherDefs/Weathers.xml`：`UnnaturalDarkness_Stage1`（该 DefType 的最小实例，且展示 `ParentName` 继承用法）。
- **类名核验**：`WeatherOverlay_Rain`、`WeatherEvent_LightningFlash`、`WeatherEvent_LightningStrike` 均已在本体 `<游戏安装目录>\Assembly-CSharp.dll` 中命中字符串。
- **跨 Def 引用**：`Ambient_Wind_Storm` / `Ambient_Rain` 为 SoundDef；`SoakingWet` 为 ThoughtDef——两者均已在本体 `Data/**/Defs/**` 中核验存在。
