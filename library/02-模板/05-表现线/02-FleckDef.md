# FleckDef

## 用途

FleckDef 描述一个「飞溅物」：尘土、血花、火花、水花、法术光效这类不入格、无实体、播完即消失的视觉特效。它由 EffecterDef 的 `fleckDef` 字段（或代码里的 `FleckMaker`）按 defName 引用并生成，是表现层最常用的一类 Def。一个 FleckDef 只描述「长什么样、活多久、怎么动」，不描述「什么时候生成」，所以它必须和 EffecterDef 或代码配合才会出现在游戏里。

## 模板

三条覆盖了全部常见形态：单图、随机多图+缩放曲线、继承基类。贴图路径都填了原版真实存在的 Core 资源（`Things/Mote/FeedbackGoto`、`Things/Mote/GroundSplash/*`），保证整份文件可直接加载。

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Defs>

  <!-- ============ ① 最简单图 fleck：graphicData + 生命周期三段时间 ============ -->
  <FleckDef>
    <defName>EXAMPLE_DustSpurt</defName>
    <!-- 绘制层级：决定会不会被墙/屋顶挡住。原版常用 LowPlant / Terrain / MoteLow / MoteOverhead / MetaOverlays -->
    <altitudeLayer>MoteOverhead</altitudeLayer>
    <!-- 三段时间：淡入 -> 完全实心 -> 淡出（单位：秒） -->
    <fadeInTime>0.1</fadeInTime>
    <solidTime>0.5</solidTime>
    <fadeOutTime>0.35</fadeOutTime>
    <!-- 每秒缩放增量，负数表示逐渐缩小 -->
    <growthRate>-0.3</growthRate>
    <graphicData>
      <!-- 贴图路径不带前导斜杠、不含扩展名 -->
      <texPath>Things/Mote/FeedbackGoto</texPath>
      <shaderType>Mote</shaderType>
      <graphicClass>Graphic_FleckPulse</graphicClass>
      <!-- 可以是单个数，也可以是 (宽,高) -->
      <drawSize>(1,1)</drawSize>
      <!-- (r, g, b, a)：可以是 0~1 小数，也可以是 0~255 整数 -->
      <color>(0.53, 0.69, 0.74, 0.5)</color>
      <renderInstanced>true</renderInstanced>
    </graphicData>
  </FleckDef>

  <!-- ============ ② 随机多图 + 缩放曲线 + 抛物弧 ============ -->
  <FleckDef>
    <defName>EXAMPLE_WaterSpray</defName>
    <altitudeLayer>MoteOverhead</altitudeLayer>
    <!-- randomGraphics 与 graphicData 二选一：这里给两套贴图，生成时随机挑一个 -->
    <randomGraphics>
      <li>
        <graphicClass>Graphic_FleckPulse</graphicClass>
        <shaderType>Mote</shaderType>
        <texPath>Things/Mote/GroundSplash/GroundSplashA</texPath>
        <drawSize>(1,1)</drawSize>
        <color>(0.53, 0.69, 0.74, .5)</color>
        <renderInstanced>false</renderInstanced>
      </li>
      <li>
        <graphicClass>Graphic_FleckPulse</graphicClass>
        <shaderType>Mote</shaderType>
        <texPath>Things/Mote/GroundSplash/GroundSplashB</texPath>
        <drawSize>(1,1)</drawSize>
        <color>(0.53, 0.69, 0.74, .5)</color>
        <renderInstanced>false</renderInstanced>
      </li>
    </randomGraphics>
    <fadeInTime>0</fadeInTime>
    <solidTime>0.3</solidTime>
    <fadeOutTime>0.35</fadeOutTime>
    <growthRate>1</growthRate>
    <!-- 抛物线弧：archHeight 是弧顶高度，archDuration 是飞行时长；两者都可写 min~max -->
    <archHeight>0</archHeight>
    <archDuration>0.5</archDuration>
    <!-- 缩放锚点，不写则以自身中心缩放 -->
    <scalingAnchor>(.5, .2, 0)</scalingAnchor>
    <unattachedDrawOffset>(0, 0, 0)</unattachedDrawOffset>
    <!-- scalers 用曲线驱动某个轴的缩放；axisMask 里 1 表示生效 -->
    <scalers>
      <li>
        <scaleAmt>1</scaleAmt>
        <scaleTime>.65</scaleTime>
        <axisMask>(1, 0, 0)</axisMask>
        <curve>
          <points>
            <li>(0,0.5)</li>
            <li>(0.25,0.7)</li>
            <li>(0.5,0.85)</li>
            <li>(0.75,0.95)</li>
            <li>(1,1)</li>
          </points>
        </curve>
      </li>
    </scalers>
    <!-- 落地时的声音：填另一个 SoundDef 的 defName -->
    <landSound>StoneImpact</landSound>
  </FleckDef>

  <!-- ============ ③ 继承基类：抽象 def 放公共参数，子 def 只覆写差异 ============ -->
  <FleckDef Name="EXAMPLE_FeedbackBase" Abstract="True">
    <altitudeLayer>MetaOverlays</altitudeLayer>
    <!-- realTime=true 表示暂停时也继续播放，UI 反馈类特效常用 -->
    <realTime>true</realTime>
    <solidTime>0.25</solidTime>
    <fadeOutTime>0.15</fadeOutTime>
    <growthRate>-0.3</growthRate>
    <graphicData>
      <drawSize>1.25</drawSize>
    </graphicData>
  </FleckDef>

  <FleckDef ParentName="EXAMPLE_FeedbackBase">
    <defName>EXAMPLE_GotoFeedback</defName>
    <!-- 只覆写贴图，其余全部继承上面的抽象 def -->
    <graphicData>
      <texPath>Things/Mote/FeedbackGoto</texPath>
    </graphicData>
  </FleckDef>

</Defs>
```

## 字段说明

> FleckDef 共 327 个实例、115 条路径。`scalers/li/curve/points/li` 这类深层路径的出现率会超过 100%（151.1%），因为一个 def 内可以出现多次。

| 字段 | 出现率 | 值类型 | 说明 |
| --- | --- | --- | --- |
| `defName` | 96.6% (316/327) | 文本 | 必填。全局唯一 ID；EffecterDef 的 `fleckDef`、ThingDef 的各种 fleck 字段都按它引用。 |
| `altitudeLayer` | 91.7% (300/327) | 文本 | **必写**。贴图绘制层级，原版样例：LowPlant、Terrain、MoteLow、MoteOverhead、MetaOverlays。层级决定它会不会被墙/屋顶遮挡。 |
| `solidTime` | 92.4% (302/327) | 数值 | **必写**。完全实心（不透明、不缩放）持续的时间秒数，原版样例 0.25 / 1 / 3 / 4 / 6。 |
| `fadeOutTime` | 91.7% (300/327) | 数值 | 淡出时长秒数，原版样例 0 / 0.15 / 0.35 / 0.65 / 1 / 2.5。 |
| `fadeInTime` | 78.9% (258/327) | 数值 | 淡入时长秒数，通常较短的 .04 / .1 / .25。 |
| `growthRate` | 44.6% (146/327) | 数值 | 每秒钟的缩放增长量，可为负（-3 表示迅速缩小），原版样例 -.16 / .08 / 1 / 2.0。 |
| `graphicData` | 87.5% (286/327) | 容器 | 图形定义容器（87.5% 的 FleckDef 用它）。与 `randomGraphics` 二选一：用 graphicData 是单图，用 randomGraphics 是随机多图。 |
| `graphicData/texPath` | 83.2% (272/327) | 文本 | 贴图路径，**不带前导斜杠、不含扩展名**（如 `Things/Mote/FeedbackGoto`）。 |
| `graphicData/shaderType` | 59.6% (195/327) | 文本 | 渲染用的 shader 名，原版样例：Mote、Transparent、MoteGlowPulse、MoteLargeDistortionWave、MoteMultiplyCircular、MoteMultiplyAddCircular、DarkHighlightRing。 |
| `graphicData/graphicClass` | 36.1% (118/327) | 文本 | 图形类，原版只有例：Graphic_Fleck、Graphic_FleckPulse、Graphic_FleckSplash。不写时用默认 Fleck 绘制类。 |
| `graphicData/drawSize` | 47.4% (155/327) | 数值/文本 | 绘制尺寸，可以是一个数（`1.25`）或 `(宽,高)` 文本（`(6, 6)`、`(1,1)`）。 |
| `graphicData/color` | 21.1% (69/327) | 文本 | 叠加颜色，(r, g, b, a)，四个分量都可以是 0~1 小数或 0~255 整数（原版两种写法都有）。 |
| `graphicData/renderInstanced` | 20.8% (68/327) | 布尔 | 是否用 GPU 实例化渲染（大量同类 fleck 时省性能）。 |
| `graphicData/renderQueue` | 1.2% (4/327) | 数值 | 自定义渲染队列号（原版样例 3181 / 3200 / 4000）。 |
| `graphicData/drawOffset` | 0.9% (3/327) | 文本 | 绘制偏移 (x, y, z)。 |
| `graphicData/borderMipMaps` | 0.3% (1/327) | 布尔 | 是否生成边界 mipmap。 |
| `graphicData/shaderParameters` | 34.9% (114/327) | 容器 | shader 参数容器。**子元素名就是参数名、大小写敏感**，例如 `_distortionIntensity`(9.8%) 与 `_DistortionIntensity`(3.1%) 是两个不同参数（原版同时存在）。共 60 个参数名。 |
| `graphicData/shaderParameters/_brightnessMultiplier` | 10.1% (33/327) | 数值 | 亮度倍率，原版样例 -20 / 0.0 / 1.15 / 5.15。 |
| `graphicData/shaderParameters/_Color` | 3.1% (10/327) | 文本 | shader 主颜色，(r,g,b,a)，原版样例 `(1, .2, .2, .2)`。 |
| `graphicData/shaderParameters/_Color2` | 7.3% (24/327) | 文本 | 第二颜色，配合 `_ColorLerp` 之类的参数使用。 |
| `graphicData/shaderParameters/_DistortionTex` | 10.7% (35/327) | 文本 | 扰动贴图路径（**这里带前导斜杠**，如 `/Things/Mote/PsycastNoise`），与 `_distortionIntensity` 配套。 |
| `graphicData/shaderParameters/_NoiseTex` | 7.3% (24/327) | 文本 | 噪声贴图路径，与 `_noiseIntensity` / `_ageToNoiseRatio` 配套。 |
| `randomGraphics/li` | 38.5% (126/327) | 容器 | 随机贴图列表：每个 li 是一套完整的图形配置，生成 fleck 时随机挑一个。 |
| `randomGraphics/li/texPath` | 38.5% (126/327) | 文本 | 该随机图标的贴图路径。 |
| `randomGraphics/li/shaderType` | 38.5% (126/327) | 文本 | 该随机图标的 shaderType。 |
| `randomGraphics/li/graphicClass` | 38.5% (126/327) | 文本 | 该随机图标的图形类（原版样例 Graphic_Fleck、Graphic_FleckPulse）。 |
| `randomGraphics/li/drawSize` | 32.1% (105/327) | 数值/文本 | 该随机图标的绘制尺寸。 |
| `randomGraphics/li/color` | 15.6% (51/327) | 文本 | 该随机图标的叠加颜色。 |
| `randomGraphics/li/renderInstanced` | 7.6% (25/327) | 布尔 | 该随机图标是否实例化渲染。 |
| `randomGraphics/li/shaderParameters` | 4.6% (15/327) | 容器 | 该随机图标的 shader 参数容器。 |
| `scalers/li` | 5.8% (19/327) | 容器 | 缩放曲线条目：按时间轴驱动某个轴的缩放。 |
| `scalers/li/scaleAmt` | 5.8% (19/327) | 数值/文本 | 缩放幅度，可写单值（1）或范围（`.8~1`、`1~4`）。 |
| `scalers/li/scaleTime` | 5.8% (19/327) | 数值/文本 | 缩放完成所需时间，可写单值或范围（`.2~6`、`2`）。 |
| `scalers/li/axisMask` | 2.1% (7/327) | 文本 | 作用轴掩码，(x, y, z) 只填 0/1，如 `(1, 0, 0)` 表示只影响横向。 |
| `scalers/li/curve/points/li` | 151.1% (494/327) | 文本 | 曲线采样点，写成 `(x,y)` 形式，如 `(0,0)`、`(1,1)`。原版单个 fleck 常带 26 个点。 |
| `scalingAnchor` | 0.6% (2/327) | 文本 | 缩放锚点，(x, y, z)，如 `(.5, .2, 0)`；不写时以自身中心缩放。 |
| `unattachedDrawOffset` | 1.5% (5/327) | 文本 | 未附着（自由飘散）时的绘制偏移，如 `(0, 0, 8)`。 |
| `altitudeLayerIncOffset` | 1.5% (5/327) | 数值 | 层级内额外提升的数值偏移（-0.5 / -1.5 / 13 等，全库仅 5 例）。 |
| `archHeight` | 3.4% (11/327) | 数值/文本 | 抛物线弧的顶点高度，可写单值或范围（`.75`、`1~2`、`12~16`）。常用于溅射/掉落物。 |
| `archDuration` | 3.1% (10/327) | 数值/文本 | 弧线飞行时长，可写单值或范围（`.5`、`0.9~1.5`）。 |
| `archCurve/points/li` | 71.6% (234/327) | 文本 | 自定义弧线曲线点，`(x,y)` 形式；不写时用默认抛物线。 |
| `speedPerTime` | 4.0% (13/327) | 数值/文本 | 每单位时间的移动速度，可写负值或范围（`-6~10`）。 |
| `acceleration` | 4.3% (14/327) | 文本 | 加速度向量，如 `(0, 0, 2)`。 |
| `fleckSystemClass` | 9.2% (30/327) | 文本 | 用哪个 fleck 系统类管理这类 fleck，原版样例：FleckSystemSplash、FleckSystemStatic、FleckSystemThrown。不写时用默认。 |
| `realTime` | 0.6% (2/327) | 布尔 | 是否使用真实时间（暂停时继续播放），Meta 层的 UI 反馈常用 `true`。 |
| `landSound` | 0.6% (2/327) | 文本 | 落地时播放的**另一个 SoundDef 的 defName**（如 StoneImpact）。 |
| `rotateTowardsMoveDirection` | 3.1% (10/327) | 布尔 | 是否朝移动方向旋转。 |
| `rotateTowardsMoveDirectionExtraAngle` | 0.9% (3/327) | 数值 | 在上面基础上额外旋转的角度（如 -90）。 |
| `useAttachLink` | 4.6% (15/327) | 布尔 | 是否把 fleck 绑定到附着点上。 |
| `attachedToHead` | 0.6% (2/327) | 布尔 | 是否附着在头部。 |
| `drawOffscreen` | 0.9% (3/327) | 布尔 | 离屏时是否也绘制。 |

## 常见坑

1. **`graphicData` 与 `randomGraphics` 同时写**：一个是单图、一个是随机多图，原版没有同时使用的例子；同时写时哪一边生效**未验证（待验证）**，请不要混用。
2. **`shaderParameters` 的参数名大小写写错**：子元素名即参数名且大小写敏感——全库同时存在 `_DistortionIntensity`(3.1%) 与 `_distortionIntensity`(9.8%)、`_NoiseIntensity` 与 `_noiseIntensity` 两组同名异写的独立参数（共 60 个参数名）。写成别的拼写不会报错，只会被当成一个未知参数（推测）。
3. **贴图路径加了前导斜杠**：`graphicData/texPath` 与 `randomGraphics/li/texPath` 都是**不带前导斜杠**的（`Things/Mote/...`），但 `shaderParameters` 里的贴图参数（`_DistortionTex`、`_NoiseTex`）原版写法**带**前导斜杠（`/Things/Mote/...`）。两处规范相反，最容易混。
4. **不给 `altitudeLayer`**：91.7% 的原版 fleck 都写了它。不写时层级取默认值，特效可能被墙体/屋顶遮挡或在错误的高度穿插（推测）。想让特效永远可见可用 `MetaOverlays`（原版 UI 反馈类 fleck 就放在这一层，并常配 `realTime=true`）。
5. **`solidTime` 给了 0**：`solidTime` 是「完全实心」的时长（92.4% 的 fleck 都写，常见 1/3/4/6）。如果它和 `fadeInTime`、`fadeOutTime` 都为 0，fleck 会在同一帧生成又消失，看起来「什么都没出现」。
6. **`scalers/li/curve/points` 里的点写成 `<li><x>0</x><y>0</y></li>`**：FleckDef 的曲线点是**文本形式的 `(x,y)`**（如 `(0,0)`、`(1,1)`），不是 SoundDef 里那种 `loc/x`、`loc/y` 子元素结构。写成后者会解析失败（推测）。
7. **`landSound` 填音频路径**：它填的是**另一个 SoundDef 的 defName**（原版样例 `StoneImpact`、`HorseshoeImpact`），不是 `Sounds/` 下的文件路径。

## 核验

- **字段说明表**：全部行取自 `<REPO_ROOT>\docs\def-schema.json` 的 `defTypes.FleckDef`（327 个实例、115 条路径），脚本逐条断言路径存在（0 缺失）；出现率与 `03-全量字段参考\字段\FleckDef.md` 同源。
- **① 单图形态**：`altitudeLayer`/`fadeInTime`/`solidTime`/`fadeOutTime`/`growthRate`/`graphicData{texPath,shaderType,drawSize,color}` 的组合逐字对照 `Anomaly/Defs/Effects/Fleck_Visual.xml`（`ParentName="FleckBase"` 的 `MonolithLevelChanged`）与 `Core/Defs/Effects/Fleck_Visual.xml`。
- **② 随机多图 + scalers + 弧线**：逐字对照 `Core/Defs/Effects/Fleck_Visual.xml` 的 `GroundWaterSplash`（randomGraphics/li 的 graphicClass/shaderType/texPath/drawSize/color、unattachedDrawOffset、archHeight、scalingAnchor、scalers/li 的 scaleAmt/scaleTime/axisMask/curve/points/li 文本曲线点）。
- **③ 抽象基类 + 继承**：逐字对照 `Core/Defs/Effects/Fleck_Meta.xml` 的 `FleckFeedbackBase`（`Name="FleckFeedbackBase" Abstract="True"` + altitudeLayer=MetaOverlays + realTime=true + solidTime=0.25 + fadeOutTime=0.15 + growthRate=-0.3 + graphicData/drawSize=1.25）与它的子 def `FeedbackGoto`（只覆写 graphicData/texPath）。
- **`shaderParameters` 大小写**：由 def-schema.json 中 `graphicData/shaderParameters/*` 的 60 个键名直接比对得出（存在 `_DistortionIntensity`/`_distortionIntensity`、`_NoiseIntensity`/`_noiseIntensity` 两组同名异写）。
- **取值样例**（altitudeLayer、graphicClass、shaderType、fleckSystemClass、solidTime、growthRate）均取自字段表的 `samples` 列，未做任何推测性补写。
- 未启动游戏加载验证；元素名、嵌套结构与取值全部来自上述原版文件与字段表。
