# SoundDef

## 用途

SoundDef 是 RimWorld 里所有声音的注册表：枪声、环境音、UI 点击音、持续型音效（sustainer）都由它定义，其它 Def 通过 `soundCastDef`、`soundDef`、`sustainStartSound` 之类的字段按 defName 引用它。一个 SoundDef 的结构固定是「一个父级 + `subSounds` 列表 + 每段声音自己的 `grains`（音频来源）与音量/音高/距离范围」，其中 `grains` 只有两种玩法：单文件（`AudioGrain_Clip`）或整个文件夹随机（`AudioGrain_Folder`）。1.7 起它还支持 `paramMappings`，可以把运行时参数（如拖动时长、环境音量、地下深度）映射到音量或音高上。

## 模板

下面四条覆盖了 SoundDef 的全部常见形态。**注意 `clipPath`/`clipFolderPath` 都是相对游戏 `Sounds/` 目录、不带扩展名的路径**：模板里故意填了原版真实存在的音频（`Interact/CrateOpeningStarted`、`Misc/Shuttle/Boarding`、`UI/Designate/DragBuilding`），这样文件可直接加载且不报找不到音频；换成你自己的音效时把这几行改掉即可。

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Defs>

  <!-- ============ ① 最常见：单文件一次性音效（oneshot） ============ -->
  <SoundDef>
    <defName>EXAMPLE_CrateCreak</defName>
    <!-- context 只有两个合法值：MapOnly / WorldOnly -->
    <context>MapOnly</context>
    <subSounds>
      <li>
        <grains>
          <!-- 必须带 Class；AudioGrain_Clip = 播单个文件 -->
          <li Class="AudioGrain_Clip">
            <!-- 相对 Sounds/ 目录，不带扩展名 -->
            <clipPath>Interact/CrateOpeningStarted</clipPath>
          </li>
        </grains>
        <!-- 距离衰减：25 格内满音量，到 50 格衰减为 0 -->
        <distRange>25~50</distRange>
        <!-- 音量可以写范围（min~max），也可以只写一个数 -->
        <volumeRange>14</volumeRange>
      </li>
    </subSounds>
  </SoundDef>

  <!-- ============ ② 文件夹随机音：一次配好一组音效，加载时随机挑一个 ============ -->
  <SoundDef>
    <defName>EXAMPLE_GateOpen</defName>
    <context>MapOnly</context>
    <maxSimultaneous>1</maxSimultaneous>
    <subSounds>
      <li>
        <grains>
          <li Class="AudioGrain_Folder">
            <!-- 指向 Sounds/ 下的一个文件夹；文件夹里所有音频会被随机使用 -->
            <clipFolderPath>Misc/Shuttle/Boarding</clipFolderPath>
          </li>
        </grains>
        <volumeRange>30</volumeRange>
        <pitchRange>0.9~1.1</pitchRange>
        <repeatMode>NeverTwice</repeatMode>
        <randomStartPoint>true</randomStartPoint>
        <startDelayRange>0~0.25</startDelayRange>
        <muteWhenPaused>true</muteWhenPaused>
      </li>
    </subSounds>
  </SoundDef>

  <!-- ============ ③ 持续音（sustainer）：顶层 sustain=true + 子音效循环 ============ -->
  <SoundDef>
    <defName>EXAMPLE_DragHum</defName>
    <context>MapOnly</context>
    <!-- 顶层 sustain 声明“本 SoundDef 是一个持续型音效”，由代码发动/停止 -->
    <sustain>True</sustain>
    <maxSimultaneous>1</maxSimultaneous>
    <priorityMode>PrioritizeNearest</priorityMode>
    <!-- 起音指向的是另一个 SoundDef 的 defName，不是音频路径 -->
    <sustainStartSound>Designate_DragBuilding_Start</sustainStartSound>
    <sustainStopSound>GeothermalPlant_Ambience_Stop</sustainStopSound>
    <sustainFadeoutTime>0.25</sustainFadeoutTime>
    <subSounds>
      <li>
        <!-- 只有镜头看得到时才播，适合 UI 长音 -->
        <onCamera>True</onCamera>
        <grains>
          <li Class="AudioGrain_Clip">
            <clipPath>UI/Designate/DragBuilding</clipPath>
          </li>
        </grains>
        <volumeRange>14.17647~8.294118</volumeRange>
        <pitchRange>0.7973334~0.7973334</pitchRange>
        <!-- subSounds 一级的 sustainLoop 才是“这一段循环播放” -->
        <sustainLoop>True</sustainLoop>
        <sustainLoopDurationRange>5~5</sustainLoopDurationRange>
        <sustainIntervalRange>3~8</sustainIntervalRange>
        <sustainAttack>0.5</sustainAttack>
        <sustainRelease>0.5</sustainRelease>
      </li>
    </subSounds>
  </SoundDef>

  <!-- ============ ④ 参数映射：把运行时参数接到音量/音高上（1.7 新玩法） ============ -->
  <SoundDef>
    <defName>EXAMPLE_ParamMappedHum</defName>
    <context>MapOnly</context>
    <sustain>True</sustain>
    <maxSimultaneous>1</maxSimultaneous>
    <subSounds>
      <li>
        <onCamera>True</onCamera>
        <grains>
          <li Class="AudioGrain_Clip">
            <clipPath>UI/Designate/DragBuilding</clipPath>
          </li>
        </grains>
        <volumeRange>14</volumeRange>
        <paramMappings>
          <li>
            <!-- 输入端必须带 Class；取值见字段说明里的 9 种 SoundParamSource_* -->
            <inParam Class="SoundParamSource_External">
              <inParamName>TimeSinceDrag</inParamName>
              <defaultValue>1</defaultValue>
            </inParam>
            <!-- 输出端也必须带 Class；空元素写法照抄原版 -->
            <outParam Class="SoundParamTarget_Volume" />
            <paramUpdateMode>Constant</paramUpdateMode>
            <!-- 曲线点用 loc/x、loc/y 两个数描述一点；至少两点才有斜率 -->
            <curve>
              <points>
                <li>
                  <loc>
                    <x>0.001351357</x>
                    <y>0.9981133</y>
                  </loc>
                </li>
                <li>
                  <loc>
                    <x>1</x>
                    <y>0</y>
                  </loc>
                </li>
              </points>
            </curve>
          </li>
        </paramMappings>
      </li>
    </subSounds>
  </SoundDef>

</Defs>
```

## 字段说明

> SoundDef 共 113 条路径、1233 个实例，下表收录全部常用项与模板用到的字段（深层嵌套路径按出现次数累加，可能超过 100%）。

| 字段 | 出现率 | 值类型 | 说明 |
| --- | --- | --- | --- |
| `defName` | 99.8% (1231/1233) | 文本 | 必填。全局唯一 ID；其它 def 引用声音时（如 ThingDef 的 soundCastDef）就是填这个值。 |
| `context` | 88.1% (1086/1233) | 文本 | 播放场景：原版只出现过 `MapOnly`（地图内）与 `WorldOnly`（世界地图）两个值，比例约 600:1。 |
| `subSounds` | 99.8% (1230/1233) | 容器 | **必填容器**，一段声音的播放参数都在这里；可以放多个 li，其中一个会被随机选中。 |
| `subSounds/li/grains` | 102.0% (1258/1233) | 容器 | 必填容器：真正要播的音频来源（clip 或 folder）放这里。 |
| `subSounds/li/grains/li` | 102.2% (1260/1233) | 容器 | 音频源条目。**必须带 `Class` 属性**；原版全库只用两种：`AudioGrain_Clip`（单文件）与 `AudioGrain_Folder`（整文件夹随机）。（元素可用属性：Class） |
| `subSounds/li/grains/li/clipPath` | 36.6% (451/1233) | 文本 | 单文件音频路径，相对于游戏 `Sounds/` 目录，**不带扩展名**（如 `Interact/CrateOpeningStarted`）。配合 `AudioGrain_Clip` 使用。 |
| `subSounds/li/grains/li/clipFolderPath` | 65.6% (809/1233) | 文本 | 文件夹音频路径，同样相对 `Sounds/`（如 `Misc/Shuttle/Boarding`），加载时随机挑一个文件。配合 `AudioGrain_Folder` 使用。 |
| `subSounds/li/grains/li/forceToMono` | 0.4% (5/1233) | 布尔 | 强制单声道。 |
| `subSounds/li/volumeRange` | 99.8% (1230/1233) | 数值/文本 | 音量范围，文本 `min~max`，也可以只写一个数（如 `14`、`25`）。**99.8% 的 SoundDef 都写了它**。 |
| `subSounds/li/pitchRange` | 55.4% (683/1233) | 数值/文本 | 音高范围，文本 `min~max`，如 `0.7973334~0.7973334`。 |
| `subSounds/li/distRange` | 50.4% (622/1233) | 文本 | 距离衰减范围，文本 `min~max`，如 `25~50`、`0~50.27907`。 |
| `subSounds/li/gameSpeedRange` | 2.4% (29/1233) | 数值/文本 | 允许播放的游戏速度范围（可写数字或 `min~max` 文本）。 |
| `subSounds/li/startDelayRange` | 0.9% (11/1233) | 数值/文本 | 播放前的随机延迟范围。 |
| `subSounds/li/muteWhenPaused` | 19.0% (234/1233) | 布尔 | 游戏暂停时是否静音。 |
| `subSounds/li/onCamera` | 15.2% (188/1233) | 布尔 | 是否只有镜头可见时才播（UI 音效常用 `True`）。 |
| `subSounds/li/name` | 1.7% (21/1233) | 容器/文本 | 子音效的名字（容器或文本）。用于在代码里按名索引子音效。 |
| `subSounds/li/repeatMode` | 7.3% (90/1233) | 文本 | 重复策略。原版取值只有 `NeverTwice`（43 次）与 `Any`（4 次）。 |
| `subSounds/li/randomStartPoint` | 0.7% (9/1233) | 布尔 | 是否从音频的随机位置开始播放。 |
| `subSounds/li/sustainLoop` | 40.4% (498/1233) | 布尔 | **`subSounds/li` 层级**的循环开关：true 表示这一段循环播放。原版 40.4% 的 SoundDef 写过它。 |
| `subSounds/li/sustainLoopDurationRange` | 1.3% (16/1233) | 数值/文本 | 每次循环的持续时长范围（如 `5~5`、`1~1`）。 |
| `subSounds/li/sustainIntervalRange` | 5.4% (67/1233) | 数值/文本 | 循环之间的间隔范围，可为负数（原版有 `-0.5~-0.5`）。 |
| `subSounds/li/sustainAttack` | 4.1% (51/1233) | 数值 | 渐入时间（秒）。 |
| `subSounds/li/sustainRelease` | 2.8% (35/1233) | 数值 | 渐出时间（秒）。 |
| `subSounds/li/sustainSkipFirstAttack` | 1.3% (16/1233) | 布尔 | 是否跳过第一次渐入。 |
| `subSounds/li/tempoAffectedByGameSpeed` | 4.7% (58/1233) | 布尔 | 是否随游戏速度改变播放速率。 |
| `sustain` | 20.3% (250/1233) | 布尔 | **顶层字段**（20.3%）：把这个 SoundDef 声明成一个可被长音调用/持续播放的 sustainer。注意它和 `subSounds/li/sustainLoop` 不是同一个东西。 |
| `sustainStartSound` | 1.5% (19/1233) | 文本 | 顶层：sustain 开始时要播的**另一个 SoundDef 的 defName**（不是音频路径）。 |
| `sustainStopSound` | 1.9% (23/1233) | 文本 | 顶层：sustain 结束时要播的另一个 SoundDef 的 defName。 |
| `sustainFadeoutStartSound` | 0.2% (2/1233) | 文本 | 顶层：开始淡出时附加播放的 SoundDef defName。 |
| `sustainFadeoutTime` | 1.5% (19/1233) | 数值 | 顶层：淡出时长（秒）。 |
| `maxSimultaneous` | 47.0% (580/1233) | 数值 | 同一时刻最多允许几个实例同时播放。 |
| `maxVoices` | 7.7% (95/1233) | 数值 | 最大声部数。 |
| `priorityMode` | 26.0% (320/1233) | 文本 | 多个实例竞争时的取舍策略：`PrioritizeExisting`（保留已有）或 `PrioritizeNearest`（保留最近的）。 |
| `slot` | 0.2% (2/1233) | 文本 | 音频槽位标记，全库只出现过 `Radio` 一个值（仅 2 个实例）。 |
| `subSounds/li/paramMappings/li` | 5.3% (65/1233) | 容器 | 1.7 的参数映射条目：把一个输入参数映射到一个输出属性（如「拖动时间 → 音量」）。 |
| `subSounds/li/paramMappings/li/inParam` | 5.3% (65/1233) | 容器 | 输入参数，**必须带 `Class` 属性**。原版全库只用过 9 种：`SoundParamSource_AmbientVolume`、`SoundParamSource_CameraAltitude`、`SoundParamSource_External`、`SoundParamSource_MusicPlayingFadeOut`、`SoundParamSource_TimeOfDay`、`SoundParamSource_OutdoorTemperature`、`SoundParamSource_Underground`、`SoundParamSource_AggregateSize`、`SoundParamSource_SourceAge`。（元素可用属性：Class） |
| `subSounds/li/paramMappings/li/inParam/inParamName` | 1.0% (12/1233) | 文本 | 输入参数名（文本）。`SoundParamSource_External` 时必须与代码里传入的名字一致（原版用例是 `TimeSinceDrag`）。 |
| `subSounds/li/paramMappings/li/inParam/defaultValue` | 1.0% (12/1233) | 数值 | 输入参数的默认值。 |
| `subSounds/li/paramMappings/li/inParam/timeType` | 0.1% (1/1233) | 文本 | 输入时间类型标记（原版仅 1 个实例使用）。 |
| `subSounds/li/paramMappings/li/outParam` | 5.3% (65/1233) | 容器 | 输出目标，**必须带 `Class` 属性**。原版全库只用过 5 种：`SoundParamTarget_Volume`、`SoundParamTarget_Pitch`、`SoundParamTarget_PropertyLowPass`、`SoundParamTarget_PropertyHighPass`、`SoundParamTarget_PropertyReverb`。（元素可用属性：Class） |
| `subSounds/li/paramMappings/li/outParam/filterProperty` | 0.2% (3/1233) | 文本 | 当输出目标是滤波器属性时，指定具体属性名。 |
| `subSounds/li/paramMappings/li/outParam/pitchType` | 0.1% (1/1233) | 文本 | 音高类型标记。 |
| `subSounds/li/paramMappings/li/paramUpdateMode` | 3.6% (45/1233) | 文本 | 参数刷新方式。全库只出现过 `Constant` 一个值。 |
| `subSounds/li/paramMappings/li/curve/points/li` | 9.7% (120/1233) | 文本 | 映射曲线上的一个采样点，用 `loc/x`、`loc/y` 两个数描述。 |
| `subSounds/li/paramMappings/li/curve/points/li/loc/x` | 9.4% (116/1233) | 数值 | 采样点的 X（输入值）。 |
| `subSounds/li/paramMappings/li/curve/points/li/loc/y` | 9.4% (116/1233) | 数值 | 采样点的 Y（输出值）。 |
| `subSounds/li/sustainIntervalFactorByAggregateSize/points/li/loc/x` | 0.2% (3/1233) | 数值 | 按聚集规模缩放循环间隔的曲线采样点 X。 |
| `subSounds/li/sustainIntervalFactorByAggregateSize/points/li/loc/y` | 0.2% (3/1233) | 数值 | 同上，采样点 Y。 |
| `subSounds/li/filters/li` | 0.6% (7/1233) | 容器 | 音频滤镜，**必须带 `Class` 属性**（全库仅 7 个实例使用）。（元素可用属性：Class） |
| `subSounds/li/filters/li/cutoffFrequency` | 0.3% (4/1233) | 数值 | 滤镜截止频率。 |
| `subSounds/li/filters/li/lowpassResonaceQ` | 0.2% (3/1233) | 数值 | 低通共振 Q 值（原版字段名就是这么拼的，注意没有第二个 s）。 |
| `subSounds/li/filters/li/wetMix` | 0.2% (2/1233) | 数值 | 湿声比例。 |
| `subSounds/li/filters/li/dryMix` | 0.2% (2/1233) | 数值 | 干声比例。 |
| `subSounds/li/filters/li/delay` | 0.2% (2/1233) | 数值 | 延迟时间。 |
| `subSounds/li/filters/li/decayRatio` | 0.2% (2/1233) | 数值 | 衰减比。 |
| `subSounds/li/filters/li/baseSetup` | 0.1% (1/1233) | 容器 | 混响基础参数容器（room / decayTime / reflectionsLevel 等 14 个数值字段，全库各仅 1 个实例使用）。 |
| `subSounds/li/canVacuumDampen` | 0.1% (1/1233) | 布尔 | 真空是否吸音（全库仅 1 个实例使用）。 |

## 常见坑

1. **把 `clipPath` 当成贴图路径写**：它是相对游戏 `Sounds/` 目录、**不带扩展名**的路径（如 `Interact/CrateOpeningStarted`），既不是 `Textures/` 下的贴图路径也不含 `.wav`。写错时不会崩，只是**静默无声**（推测：加载器找不到文件时记一条日志并跳过）。
2. **`grains/li` 漏写 `Class`**：原版全库只有 `AudioGrain_Clip` 与 `AudioGrain_Folder` 两种取值，且两者用的是**不同字段**——`AudioGrain_Clip` 配 `clipPath`，`AudioGrain_Folder` 配 `clipFolderPath`。填错类或写错字段名，声音不会出来（推测：该音频源无法被实例化）。
3. **`sustain` 与 `sustainLoop` 层级混淆**：`sustain` 是**顶层**字段（20.3%，声明这个 SoundDef 是持续音、由代码激活）；`sustainLoop` 是 **`subSounds/li` 一级**的字段（40.4%，声明这一段循环播放）。把 `sustainLoop` 写到顶层、或把 `sustain` 写进 `subSounds/li`，都不会生效且不报错（推测：解析器忽略未知路径）。
4. **`sustainStartSound` 填成音频路径**：`sustainStartSound` / `sustainStopSound` / `sustainFadeoutStartSound` 填的都是**另一个 SoundDef 的 defName**（原版示例里 `Designate_DragBuilding` 的起音指向 `Designate_DragBuilding_Start`）。填路径则解析不到 defName，起停音缺失。
5. **`paramMappings` 的 `inParam` / `outParam` 没有 `Class`**：这两者必须带 Class（`SoundParamSource_*` / `SoundParamTarget_*`）。全库输入只出现过 9 种、输出只出现过 5 种（见字段说明表），`paramUpdateMode` 只出现过 `Constant`；写错类名不报错但映射无效（推测）。
6. **`distRange`/`volumeRange` 写成中文波浪号或逗号**：范围一律用半角 `~` 连接（如 `25~50`），也允许只写单值（`14`、`25`）。写成 `25-50` 或 `25，50` 会解析失败（推测）。
7. **`context` 留空**：原版 88.1% 的 SoundDef 显式写了 `MapOnly` 或 `WorldOnly`（约 600:1）。原版确实存在完全不写 context 的 SoundDef（如 `Core/Defs/SoundDefs/UI_Oneshots_Designation.xml` 的 `Designate_DragBuilding_Start`），但其默认适用范围**未在本次核验中确认（待验证）**，建议显式写。

## 核验

- **字段说明表**：全部行取自 `<REPO_ROOT>\docs\def-schema.json` 的 `defTypes.SoundDef`（1233 个实例、113 条路径），脚本逐条断言路径存在（0 缺失）；出现率数字与 `03-全量字段参考\字段\SoundDef.md` 同源。
- **① oneshot**：逐字对照 `Core/Defs/SoundDefs/Building_Oneshots_Misc.xml` 的 `CrateOpeningStarted`（context=MapOnly、`grains/li Class="AudioGrain_Clip"`、clipPath=Interact/CrateOpeningStarted、distRange=25~50、volumeRange=14）。
- **② 文件夹随机音**：`AudioGrain_Folder` + `clipFolderPath` 写法对照 `Core/Defs/SoundDefs/Building_Oneshots_Misc.xml`（clipFolderPath=Misc/Shuttle/Boarding）与 `Anomaly/Defs/SoundDefs/Buildings_Misc.xml` 的 `PitGateOpen`（volumeRange=30）；`repeatMode`、`randomStartPoint`、`startDelayRange`、`muteWhenPaused`、`onCamera` 的用法取自 SoundDef 全量字段表（分别为 7.3%、0.7%、0.9%、19.0%、15.2%）。
- **③ sustainer**：顶层 `sustain` / `maxSimultaneous` / `priorityMode` / `sustainStartSound` / `sustainFadeoutTime` 与 `subSounds` 内的 `onCamera`、`pitchRange`、`sustainLoop` 结构逐字对照 `Core/Defs/SoundDefs/UI_Sustainers_Designation.xml` 的 `Designate_DragBuilding`；`sustainLoop`+`sustainAttack`/`sustainRelease`/`sustainLoopDurationRange` 组合对照 `Anomaly/Defs/SoundDefs/Pawn_Sustainers_Misc.xml` 的 `Pawn_SelfResurrection`；`sustainStopSound` 引用的 `GeothermalPlant_Ambience_Stop` 来自 `Core/Defs/SoundDefs/Building_Sustainers_Ambiences.xml`。
- **④ paramMappings**：整块（`inParam Class="SoundParamSource_External"` + `inParamName=TimeSinceDrag` + `defaultValue` + 空元素 `<outParam Class="SoundParamTarget_Volume" />` + `paramUpdateMode=Constant` + `curve/points/li/loc/x|y`）逐字对照 `Core/Defs/SoundDefs/UI_Sustainers_Designation.xml` 的 `Designate_DragBuilding`。
- **取值全集**（写进字段说明与常见坑的硬数字）：`AudioGrain_*` 只有 2 种、`SoundParamSource_*` 9 种、`SoundParamTarget_*` 5 种、`context` 值 `MapOnly/WorldOnly`、`repeatMode` 值 `NeverTwice/Any`、`paramUpdateMode` 值 `Constant`、`slot` 值 `Radio`，均由全库扫描确认；SoundDef 文件共 122 个（Core 35 个）。
- 未启动游戏加载验证；元素名、属性名与取值全部来自上述原版文件与字段表。
