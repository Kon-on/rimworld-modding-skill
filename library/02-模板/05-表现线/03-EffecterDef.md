# EffecterDef

## 用途

EffecterDef 描述一套「触发式/持续式视觉+声音特效组合」：谁在什么位置喷什么 fleck、播什么声音、晃不晃屏。它自己不含任何贴图或音频，而是把 FleckDef、Mote（ThingDef）、SoundDef 按子效果器（subEffecter）拼装起来，由 C# 代码（`EffecterDefOf.X` 或 `Effecter.Make...`）在运行时按 defName 引用。

改一个 EffecterDef 就能同时调整一次爆炸的尘土、声音和镜头抖动，所以它是表现层里最常用、也最容易写错的一类 Def：`children/li` 下 40 多个字段的同名项分别挂在「顶层 Effecter」和「单个子效果器」两个不同层级上。

## 模板

四条覆盖了绝大多数写法：单子效果器喷洒、抽象基类+继承、嵌套子效果器+间歇音、吸附挂点。所有 fleckDef / moteDef / soundDef 都用了原版真实存在的名字（`DustPuff`、`DustPuffThick`、`FlashPowerCell`、`Mote_PowerCellBurning`、`Mote_Clipboard`、`GroundCrackHuge`、`BurningPowerCell_Start/Loop`、`Emergence_Quake`、`PokerChips`），整份文件可直接丢进 `Defs/` 加载。

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Defs>

  <!-- ============ ① 最简骨架：一个按概率喷洒 fleck 的子效果器 ============ -->
  <EffecterDef>
    <defName>EXAMPLE_DustSpray</defName>
    <children>
      <li>
        <!-- 必写：子效果器类名，决定这个 li 怎么工作 -->
        <subEffecterClass>SubEffecter_SprayerChance</subEffecterClass>
        <fleckDef>DustPuff</fleckDef>
        <!-- 每 tick 触发的概率 -->
        <chancePerTick>0.07</chancePerTick>
        <burstCount>1</burstCount>
        <!-- 生成点散布半径 -->
        <positionRadius>0.2</positionRadius>
        <scale>0.9~1.3</scale>
        <rotationRate>-60~60</rotationRate>
        <speed>0.6~1.8</speed>
        <spawnLocType>OnSource</spawnLocType>
        <fleckUsesAngleForVelocity>true</fleckUsesAngleForVelocity>
        <angle>0~360</angle>
        <positionOffset>(0, 0, 0)</positionOffset>
      </li>
    </children>
  </EffecterDef>

  <!-- ============ ② 抽象基类 + 继承；同一 def 内混用 moteDef 与 Sustainer 循环音 ============ -->
  <EffecterDef Name="EXAMPLE_BurningBase" Abstract="True">
    <children>
      <li>
        <subEffecterClass>SubEffecter_SprayerContinuous</subEffecterClass>
        <!-- moteDef 走 Mote（ThingDef）路线，与 fleckDef 二选一 -->
        <moteDef>Mote_PowerCellBurning</moteDef>
        <!-- 连续型：每隔这么多 tick 生成一个 -->
        <ticksBetweenMotes>50</ticksBetweenMotes>
        <positionRadius>0.15</positionRadius>
        <scale>0.9~1.1</scale>
        <angle>0</angle>
        <rotation>-15~15</rotation>
        <positionOffset>(0, 0, 0.4)</positionOffset>
        <spawnLocType>OnSource</spawnLocType>
      </li>
    </children>
  </EffecterDef>

  <EffecterDef ParentName="EXAMPLE_BurningBase">
    <defName>EXAMPLE_BurningCell</defName>
    <!-- 顶层字段：整个 Effecter 维持 120 tick -->
    <maintainTicks>120</maintainTicks>
    <children>
      <li>
        <subEffecterClass>SubEffecter_SprayerContinuous</subEffecterClass>
        <fleckDef>FlashPowerCell</fleckDef>
        <ticksBetweenMotes>15</ticksBetweenMotes>
        <positionRadius>0.2</positionRadius>
        <scale>4~5</scale>
        <angle>0</angle>
        <rotation>0~360</rotation>
        <positionOffset>(0, 0, 0.35)</positionOffset>
        <spawnLocType>OnSource</spawnLocType>
      </li>
      <li>
        <!-- 触发时播一次音 -->
        <subEffecterClass>SubEffecter_SoundTriggered</subEffecterClass>
        <soundDef>BurningPowerCell_Start</soundDef>
        <spawnLocType>OnTarget</spawnLocType>
      </li>
      <li>
        <!-- 持续循环音（sustainer） -->
        <subEffecterClass>SubEffecter_Sustainer</subEffecterClass>
        <soundDef>BurningPowerCell_Loop</soundDef>
        <spawnLocType>OnTarget</spawnLocType>
      </li>
    </children>
  </EffecterDef>

  <!-- ============ ③ 嵌套子效果器 + 间歇音 + 顶层调控字段 ============ -->
  <EffecterDef>
    <defName>EXAMPLE_NestedQuake</defName>
    <maintainTicks>130</maintainTicks>
    <randomWeight>1</randomWeight>
    <children>
      <li>
        <!-- GroupedChance 下再挂 children，用同一时机同步多个子效果器 -->
        <subEffecterClass>SubEffecter_GroupedChance</subEffecterClass>
        <chancePerTick>.01</chancePerTick>
        <chancePeriodTicks>20</chancePeriodTicks>
        <children>
          <li>
            <subEffecterClass>SubEffecter_CameraShakeSingle</subEffecterClass>
            <cameraShake>.1~.3</cameraShake>
            <distanceAttenuationScale>1</distanceAttenuationScale>
            <distanceAttenuationMax>30</distanceAttenuationMax>
            <soundDef>Emergence_Quake</soundDef>
          </li>
          <li>
            <subEffecterClass>SubEffecter_SprayerTriggered</subEffecterClass>
            <fleckDef>DustPuffThick</fleckDef>
            <initialDelayTicks>0</initialDelayTicks>
            <burstCount>2~4</burstCount>
            <spawnLocType>OnSource</spawnLocType>
            <positionRadius>4</positionRadius>
            <scale>1.5~3</scale>
            <rotation>0</rotation>
            <rotationRate>-60~60</rotationRate>
            <absoluteAngle>False</absoluteAngle>
            <positionOffset>(0, 0, 0)</positionOffset>
            <angle>0~360</angle>
            <fleckUsesAngleForVelocity>True</fleckUsesAngleForVelocity>
            <speed>.6~.75</speed>
            <makeMoteOnSubtrigger>true</makeMoteOnSubtrigger>
          </li>
        </children>
      </li>
      <li>
        <subEffecterClass>SubEffecter_SprayerTriggered</subEffecterClass>
        <moteDef>GroundCrackHuge</moteDef>
        <destroyMoteOnCleanup>true</destroyMoteOnCleanup>
        <burstCount>1</burstCount>
        <color>(1, 1, 1, .65)</color>
        <spawnLocType>OnSource</spawnLocType>
        <scale>6</scale>
        <rotation>0~360</rotation>
        <rotationRate>0</rotationRate>
        <absoluteAngle>True</absoluteAngle>
        <positionOffset>(0, 0, 0)</positionOffset>
        <angle>0</angle>
        <fleckUsesAngleForVelocity>False</fleckUsesAngleForVelocity>
        <speed>0</speed>
      </li>
      <li>
        <!-- 随机间隔播放的音效 -->
        <subEffecterClass>SubEffecter_SoundIntermittent</subEffecterClass>
        <soundDef>PokerChips</soundDef>
        <intermittentSoundInterval>
          <min>750</min>
          <max>4300</max>
        </intermittentSoundInterval>
      </li>
    </children>
  </EffecterDef>

  <!-- ============ ④ 吸附在生成者身上 + 按朝向偏移 + 顶层 offsetMode/offsetTowardsTarget ============ -->
  <EffecterDef>
    <defName>EXAMPLE_AttachedOverlay</defName>
    <!-- 顶层：不要跟随生成点（fleck 自身已锚定好位置） -->
    <offsetMode>Free</offsetMode>
    <offsetTowardsTarget>0.25~0.25</offsetTowardsTarget>
    <positionRadius>0.1</positionRadius>
    <children>
      <li>
        <subEffecterClass>SubEffecter_SprayerTriggered</subEffecterClass>
        <spawnLocType>OnSource</spawnLocType>
        <maxMoteCount>1</maxMoteCount>
        <destroyMoteOnCleanup>True</destroyMoteOnCleanup>
        <positionOffset>(0, 0, .5)</positionOffset>
        <moteDef>Mote_Clipboard</moteDef>
        <angle>0</angle>
        <rotation>0</rotation>
        <absoluteAngle>True</absoluteAngle>
        <attachToSpawnThing>true</attachToSpawnThing>
        <useTargetAInitialRotation>true</useTargetAInitialRotation>
        <!-- 四个朝向各一个偏移，面朝南时抬高一格 -->
        <perRotationOffsets>
          <li>(0, 0, 0)</li>
          <li>(0, 0, 0)</li>
          <li>(0, 1, 0)</li>
          <li>(0, 0, 0)</li>
        </perRotationOffsets>
      </li>
      <li>
        <subEffecterClass>SubEffecter_SprayerContinuous</subEffecterClass>
        <fleckDef>DustPuff</fleckDef>
        <scale>.6</scale>
        <positionLerpFactor>.5</positionLerpFactor>
        <burstCount>1</burstCount>
        <ticksBetweenMotes>45</ticksBetweenMotes>
        <spawnLocType>BetweenPositions</spawnLocType>
        <absoluteAngle>True</absoluteAngle>
        <positionRadius>0</positionRadius>
        <positionRadiusMin>0</positionRadiusMin>
        <angle>0</angle>
        <speed>0.7~1</speed>
        <rotation>-20~20</rotation>
        <fleckUsesAngleForVelocity>True</fleckUsesAngleForVelocity>
      </li>
    </children>
  </EffecterDef>

</Defs>
```

## 字段说明

> EffecterDef 共 285 个实例、82 条路径。下表把 82 条**全部列全**。注意 `children/li/*` 的出现率会超过 100%（如 `subEffecterClass` 241.1%），因为一个 def 平均有 2.4 个子效果器。

| 字段 | 出现率 | 值类型 | 说明 |
| --- | --- | --- | --- |
| `children` | 100.0% (285/285) | 容器 | 子效果器容器。EffecterDef 100% 都有它（285/285）；`children/li` 平均一个 def 出现 2.4 次（687/285）。 |
| `children/li` | 241.1% (687/285) | 容器 | 一个子效果器配置，必须带 `subEffecterClass` 决定行为，其余字段由该类读取。 |
| `children/li/absoluteAngle` | 26.7% (76/285) | 布尔 | `angle` 是绝对方位(true)还是相对源→目标方向(false)，样例 True/False。 |
| `children/li/airTime` | 3.2% (9/285) | 数值/文本 | 飞行时间，可写单值或范围（`0.08~0.16`、`0.75`）。 |
| `children/li/angle` | 70.5% (201/285) | 数值/文本 | 喷射方向角，可写单值或范围（`0~360`、`-30~30`、`180`）。是否影响速度方向取决于 `fleckUsesAngleForVelocity`（推测）。 |
| `children/li/attachPoint` | 0.7% (2/285) | 文本 | 吸附到具名挂点，全库唯一取值 `Exhaust`（AtmosphericHeaterAmbience）。 |
| `children/li/attachToSpawnThing` | 12.6% (36/285) | 布尔 | 是否把生成物吸附到生成点（例如挂在施法者身上），样例 true。 |
| `children/li/avoidLastPositionRadius` | 1.4% (4/285) | 数值 | 避免与上一次位置过近的半径，如 0.3、1、2。 |
| `children/li/burstCount` | 129.5% (369/285) | 数值/文本 | 一次触发产生几个，可写单值或 `min~max`（`1~4`、`8~8`、`5~10`）。 |
| `children/li/cameraShake` | 3.2% (9/285) | 数值 | 镜头晃动强度（CameraShake 系），如 `..2` 类的 `.2`、`.25`、`.5`、`1`。 |
| `children/li/chancePerTick` | 60.7% (173/285) | 数值 | 每 tick 触发概率（SprayerChance 系），如 0.07、0.05、0.7、.01。 |
| `children/li/chancePeriodTicks` | 26.0% (74/285) | 数值 | 概率判定的间隔 tick（如 15、20、30）。 |
| `children/li/children` | 2.1% (6/285) | 容器 | 嵌套子效果器容器（如 SubEffecter_GroupedChance 下再挂多个子效果器）。 |
| `children/li/children/li` | 7.7% (22/285) | 容器 | 嵌套子效果器条目，字段集与 `children/li` 相同。 |
| `children/li/children/li/absoluteAngle` | 5.6% (16/285) | 布尔 | （嵌套层）`angle` 是绝对方位(true)还是相对源→目标方向(false)，样例 True/False。 |
| `children/li/children/li/angle` | 6.0% (17/285) | 数值/文本 | （嵌套层）喷射方向角，可写单值或范围（`0~360`、`-30~30`、`180`）。是否影响速度方向取决于 `fleckUsesAngleForVelocity`（推测）。 |
| `children/li/children/li/avoidLastPositionRadius` | 3.5% (10/285) | 数值 | （嵌套层）避免与上一次位置过近的半径，如 0.3、1、2。 |
| `children/li/children/li/burstCount` | 6.3% (18/285) | 数值/文本 | （嵌套层）一次触发产生几个，可写单值或 `min~max`（`1~4`、`8~8`、`5~10`）。 |
| `children/li/children/li/cameraShake` | 0.7% (2/285) | 文本 | （嵌套层）镜头晃动强度（CameraShake 系），如 `..2` 类的 `.2`、`.25`、`.5`、`1`。 |
| `children/li/children/li/chancePerTick` | 3.9% (11/285) | 数值 | （嵌套层）每 tick 触发概率（SprayerChance 系），如 0.07、0.05、0.7、.01。 |
| `children/li/children/li/chancePeriodTicks` | 1.8% (5/285) | 数值 | （嵌套层）概率判定的间隔 tick（如 15、20、30）。 |
| `children/li/children/li/color` | 1.8% (5/285) | 文本 | （嵌套层）生成物叠加色 `(r, g, b, a)`，如 `(1, 1, 1, .75)`、`(1, 0, 0, .25)`。 |
| `children/li/children/li/distanceAttenuationMax` | 1.4% (4/285) | 数值 | （嵌套层）震屏的距离衰减上限（世界格），如 10、30、100。 |
| `children/li/children/li/distanceAttenuationScale` | 1.4% (4/285) | 数值 | （嵌套层）震屏的距离衰减系数，如 .5、1。 |
| `children/li/children/li/fleckDef` | 6.3% (18/285) | 文本 | （嵌套层）要生成的 FleckDef 的 defName（Sprayer 系子效果器用）。原版样例：DustPuff、DustPuffThick、GroundCrack、ThrownDebris、SparkFlash。 |
| `children/li/children/li/fleckUsesAngleForVelocity` | 5.3% (15/285) | 布尔 | （嵌套层）是否让 `angle` 决定速度方向（47.0% 使用），样例 true/True/False。 |
| `children/li/children/li/initialDelayTicks` | 4.9% (14/285) | 数值 | （嵌套层）延迟多少 tick 才开始（如 550、660、710）。 |
| `children/li/children/li/makeMoteOnSubtrigger` | 5.3% (15/285) | 布尔 | （嵌套层）子弹触发时是否补生成 Mote，样例 true。 |
| `children/li/children/li/positionOffset` | 6.3% (18/285) | 文本 | （嵌套层）额外坐标偏移 `(x, y, z)`，如 `(0, 0, 0.4)`、`(-.5, 0, -.5)`。 |
| `children/li/children/li/positionRadius` | 6.3% (18/285) | 数值 | （嵌套层）**顶层字段**（与 `children/li/positionRadius` 不是一回事）。整个 Effecter 的生成点散布半径，全库 8/285。 |
| `children/li/children/li/positionRadiusMin` | 4.9% (14/285) | 数值 | （嵌套层）散布半径下限，与 `positionRadius` 组成环带（如 0、2、3、4.2）。 |
| `children/li/children/li/randomWeight` | 0.4% (1/285) | 数值 | **顶层字段**。多个 Effecter 随机挑选时的权重（.3、1），全库仅 3 例。 |
| `children/li/children/li/rotation` | 6.3% (18/285) | 数值/文本 | （嵌套层）初始旋转角，可写单值或范围（`0`、`-150~150`、`0~360`、`-20~20`）。 |
| `children/li/children/li/rotationRate` | 6.3% (18/285) | 数值/文本 | （嵌套层）每秒旋转速率，可写单值或范围（`0`、`-60~60`、`-200~200`、`100~200`）。 |
| `children/li/children/li/scale` | 7.0% (20/285) | 数值/文本 | （嵌套层）生成物缩放，可写单值或范围：`6`、`2~5`、`.15~.25`、`20`。 |
| `children/li/children/li/soundDef` | 0.7% (2/285) | 文本 | （嵌套层）该子效果器播放的 SoundDef defName（Sound*/Sustainer/CameraShakeSingle 系），样例 Emergence_Quake、BurningPowerCell_Loop、PokerChips。 |
| `children/li/children/li/spawnLocType` | 6.3% (18/285) | 文本 | （嵌套层）生成位置来源。原版样例：OnSource、OnTarget、BetweenPositions、RandomDrawPosOnTarget。 |
| `children/li/children/li/speed` | 6.3% (18/285) | 数值/文本 | （嵌套层）初速度，可写单值或范围（`0`、`0.6~1.8`、`9~15`、`5~20`）。 |
| `children/li/children/li/subEffecterClass` | 7.7% (22/285) | 文本 | （嵌套层）**必写**。子效果器类名，全库只出现 15 个（见「核验」表）：SubEffecter_SprayerTriggered(260)、SubEffecter_SprayerChance(173)、SubEffecter_SprayerContinuous(85)、SubEffecter_SoundTriggered(64)、SubEffecter_SprayerTriggeredDelayed(48)、SubEffecter_Sustainer(44)、SubEffecter_CameraShakeSingle(10)、SubEffecter_InteractSymbol(9)、SubEffecter_GroupedChance(5)、SubEffecter_CameraShakeChance(4)、SubEffecter_SprayerTriggeredChance(2)、SubEffecter_DrifterEmoteChance(2)、SubEffecter_ProgressBar(2)、SubEffecter_Random(1)、SubEffecter_SoundIntermittent(1)。 |
| `children/li/color` | 14.4% (41/285) | 文本 | 生成物叠加色 `(r, g, b, a)`，如 `(1, 1, 1, .75)`、`(1, 0, 0, .25)`。 |
| `children/li/destroyMoteOnCleanup` | 3.2% (9/285) | 布尔 | 子效果器销毁时是否连带销毁它生成的 Mote，样例 True/true。 |
| `children/li/distanceAttenuationMax` | 1.4% (4/285) | 数值 | 震屏的距离衰减上限（世界格），如 10、30、100。 |
| `children/li/distanceAttenuationScale` | 2.8% (8/285) | 数值 | 震屏的距离衰减系数，如 .5、1。 |
| `children/li/fleckDef` | 139.3% (397/285) | 文本 | 要生成的 FleckDef 的 defName（Sprayer 系子效果器用）。原版样例：DustPuff、DustPuffThick、GroundCrack、ThrownDebris、SparkFlash。 |
| `children/li/fleckUsesAngleForVelocity` | 47.0% (134/285) | 布尔 | 是否让 `angle` 决定速度方向（47.0% 使用），样例 true/True/False。 |
| `children/li/initialDelayTicks` | 25.6% (73/285) | 数值 | 延迟多少 tick 才开始（如 550、660、710）。 |
| `children/li/intermittentSoundInterval` | 0.4% (1/285) | 容器 | 间歇音间隔容器（配合 SubEffecter_SoundIntermittent）。 |
| `children/li/intermittentSoundInterval/max` | 0.4% (1/285) | 数值 | 最大间隔 tick（原版 PlayPoker 用 4300）。 |
| `children/li/intermittentSoundInterval/min` | 0.4% (1/285) | 数值 | 最小间隔 tick（原版 PlayPoker 用 750）。 |
| `children/li/lifespanMaxTicks` | 5.6% (16/285) | 数值 | 该子效果器最长存活 tick 数（如 1、8、240、440）。 |
| `children/li/makeMoteOnSubtrigger` | 1.4% (4/285) | 布尔 | 子弹触发时是否补生成 Mote，样例 true。 |
| `children/li/maxMoteCount` | 4.2% (12/285) | 数值 | 同时存在的 Mote 上限（1、3、8、14），常与 `destroyMoteOnCleanup` 连用。 |
| `children/li/moteDef` | 57.9% (165/285) | 文本 | 要生成的 Mote（ThingDef）的 defName，与 `fleckDef` 并列的另一条路。Mote 是有寿命的实体，可被 `destroyMoteOnCleanup` 清理。样例 Mote_PowerCellBurning、Mote_Clipboard、Mote_MeatExplosionMist、GroundCrackHuge。 |
| `children/li/orbitOrigin` | 2.8% (8/285) | 布尔 | 是否绕原点（生成点）公转，样例 true。 |
| `children/li/orbitSnapStrength` | 2.8% (8/285) | 数值 | 公转吸附强度，如 .8、1.0。 |
| `children/li/orbitSpeed` | 0.7% (2/285) | 文本 | 公转速度，可写范围（`-5~-1`、`-6~-1`）。 |
| `children/li/perRotationOffsets` | 1.8% (5/285) | 容器 | 按朝向给出的偏移列表容器（4 个 li 对应四个朝向），常与 `attachToSpawnThing`+`useTargetAInitialRotation` 连用。 |
| `children/li/perRotationOffsets/li` | 7.0% (20/285) | 文本 | 单个朝向上的偏移，文本 `(x, y, z)`，如 `(0, 1, 0)`（面朝南时抬高一格）。 |
| `children/li/positionDimensions` | 2.1% (6/285) | 文本 | 多点采样用的长方体尺寸 `(x, y, z)`，如 `(0.32, 0, 0.2)`、`(4.5, 0, 1.7)`。 |
| `children/li/positionLerpFactor` | 20.7% (59/285) | 数值 | 位置跟随插值系数（0~1，越大跟得越紧），如 .3、.5、.75。 |
| `children/li/positionOffset` | 52.6% (150/285) | 文本 | 额外坐标偏移 `(x, y, z)`，如 `(0, 0, 0.4)`、`(-.5, 0, -.5)`。 |
| `children/li/positionRadius` | 124.2% (354/285) | 数值 | 生成点的随机散布半径，高频主字段（124.2%），如 0.15、0.2、1、4。 |
| `children/li/positionRadiusMin` | 32.6% (93/285) | 数值 | 散布半径下限，与 `positionRadius` 组成环带（如 0、2、3、4.2）。 |
| `children/li/rotateTowardsTargetCenter` | 8.4% (24/285) | 布尔 | 是否朝目标中心旋转，样例 True/true。 |
| `children/li/rotation` | 82.5% (235/285) | 数值/文本 | 初始旋转角，可写单值或范围（`0`、`-150~150`、`0~360`、`-20~20`）。 |
| `children/li/rotationRate` | 55.4% (158/285) | 数值/文本 | 每秒旋转速率，可写单值或范围（`0`、`-60~60`、`-200~200`、`100~200`）。 |
| `children/li/scale` | 150.2% (428/285) | 数值/文本 | 生成物缩放，可写单值或范围：`6`、`2~5`、`.15~.25`、`20`。 |
| `children/li/soundDef` | 41.8% (119/285) | 文本 | 该子效果器播放的 SoundDef defName（Sound*/Sustainer/CameraShakeSingle 系），样例 Emergence_Quake、BurningPowerCell_Loop、PokerChips。 |
| `children/li/spawnLocType` | 177.5% (506/285) | 文本 | 生成位置来源。原版样例：OnSource、OnTarget、BetweenPositions、RandomDrawPosOnTarget。 |
| `children/li/speed` | 110.5% (315/285) | 数值/文本 | 初速度，可写单值或范围（`0`、`0.6~1.8`、`9~15`、`5~20`）。 |
| `children/li/subEffecterClass` | 241.1% (687/285) | 文本 | **必写**。子效果器类名，全库只出现 15 个（见「核验」表）：SubEffecter_SprayerTriggered(260)、SubEffecter_SprayerChance(173)、SubEffecter_SprayerContinuous(85)、SubEffecter_SoundTriggered(64)、SubEffecter_SprayerTriggeredDelayed(48)、SubEffecter_Sustainer(44)、SubEffecter_CameraShakeSingle(10)、SubEffecter_InteractSymbol(9)、SubEffecter_GroupedChance(5)、SubEffecter_CameraShakeChance(4)、SubEffecter_SprayerTriggeredChance(2)、SubEffecter_DrifterEmoteChance(2)、SubEffecter_ProgressBar(2)、SubEffecter_Random(1)、SubEffecter_SoundIntermittent(1)。 |
| `children/li/ticksBeforeSustainerStart` | 1.4% (4/285) | 数值 | 循环音开始前的等待 tick（35、120、600）。 |
| `children/li/ticksBetweenMotes` | 30.5% (87/285) | 数值 | 连续型子效果器两次生成之间的 tick 数（如 2、15、30、50）。 |
| `children/li/useTargetABodyAngle` | 0.4% (1/285) | 布尔 | 是否用目标 A 的身体朝向角（全库仅 1 例，样例 true）。 |
| `children/li/useTargetAInitialRotation` | 3.5% (10/285) | 布尔 | 是否用目标 A 的初始朝向，样例 true。 |
| `children/li/useTargetBInitialRotation` | 1.8% (5/285) | 布尔 | 是否用目标 B 的初始朝向，样例 true。 |
| `defName` | 99.3% (283/285) | 文本 | 必填。全局唯一 ID；代码（如 `EffecterDefOf.X`）与其它 Def 都按它引用。 |
| `maintainTicks` | 8.1% (23/285) | 数值 | **顶层字段**（写在 `</children>` 之后或 defName 之后）。该 Effecter 维持的 tick 数：120、130、60、720。 |
| `offsetMode` | 0.7% (2/285) | 文本 | **顶层字段**。全库唯一取值 `Free`。原版注释：不要让特效跟随生成点，因为 fleck 自身已锚定好位置，跟随反而会引入错误偏移。 |
| `offsetTowardsTarget` | 2.8% (8/285) | 文本 | **顶层字段**。整体朝目标方向的偏移量，可写单值或范围（`0.25~0.25`、`0.31~0.31`）。 |
| `positionRadius` | 2.8% (8/285) | 数值 | **顶层字段**（与 `children/li/positionRadius` 不是一回事）。整个 Effecter 的生成点散布半径，全库 8/285。 |
| `randomWeight` | 1.1% (3/285) | 数值 | **顶层字段**。多个 Effecter 随机挑选时的权重（.3、1），全库仅 3 例。 |

## 常见坑

1. **`children/li` 漏写 `subEffecterClass`**：原版 687 个 `children/li` 与 687 个 `subEffecterClass` 一一对应（覆盖率 100%），每个子效果器都必须由类名驱动。漏写时这个 li 无法实例化（具体报错形式**待验证**：原版没有可参照的漏写样例）。另外 `SubEffecter_*` 全库只有 15 个类名，写一个不存在的类名不会有任何效果（推测）。
2. **找不到 `levels` 字段**：本次点名的 `levels` 在 EffecterDef 的 82 条路径中**不存在**；进一步全库检索 254 个 DefType 也没有任何路径名含 `levels`。**结论：EffecterDef 没有「特效层级」概念（疑似不存在，待验证）**。分层靠两点：嵌套用 `children/li/children/li`，绘制高度由 fleckDef / moteDef 自己的 `altitudeLayer` 决定。
3. **`fleckDef`、`moteDef`、`soundDef` 三者混用**：`fleckDef` 生成 Fleck（无实体、自动消失），`moteDef` 生成 Mote（Thing，可被 `destroyMoteOnCleanup` 清理、可被 `maxMoteCount` 限流），`soundDef` 只服务于 Sound*/Sustainer/CameraShakeSingle 系。字段名写错不会报错，只是该子效果器什么都不显示（推测）。
4. **同名字段放错层级**：`positionRadius` 顶层只占 2.8% (8/285)，而 `children/li/positionRadius` 有 124.2%；`offsetTowardsTarget`、`offsetMode`、`randomWeight`、`maintainTicks` 都是**顶层**（写 `defName` 之后或 `</children>` 之后），写进 li 里无效（推测）。`perRotationOffsets` 反过来只属于 li。
5. **`angle` 与 `absoluteAngle` 的关系弄反**：`absoluteAngle=true` 时 `angle` 是绝对朝向，`false` 时是相对「源→目标」方向（推测，来自原版同一 def 内两种写法并存的观察：GroundCrack 用 True+`angle=0`，ThrownDebris 用 False+`angle=0~360`）。方向还受 `fleckUsesAngleForVelocity` 控制，想让 fleck 沿 `angle` 飞必须同时打开它。
6. **继承 `ParentName` 时 `<children>` 是追加还是覆盖，未做加载验证（待验证）**：原版 `Power_Cell_Burning`（`Core/Defs/Effects/Effecter_Misc.xml:360`）继承 `Power_Cell_Burning_Base` 时只写了自己的 3 个 li，父类的烟雾子效果器没重写——看起来是列表追加，但没有实测确认。本模板 ② 的写法在两种语义下都能正常加载。同理 `maintainTicks` 不写时持续型 Effecter 由谁回收也**待验证**（原版仅 8.1% 写它）。

## 核验

- **字段说明表**：82 行全部取自 `<REPO_ROOT>\docs\def-schema.json` 的 `defTypes.EffecterDef`（285 个实例、82 条路径），脚本逐条断言路径存在（0 缺失、0 遗漏）；出现率与 `03-全量字段参考\字段\EffecterDef.md` 同源。
- **① 最简骨架**：`Core/Defs/Effects/Effecter_Construction.xml:104` 的 `RoofWork`（subEffecterClass=SubEffecter_SprayerChance、fleckDef=DustPuff、chancePerTick=0.07、scale=0.9~1.3、rotationRate=-60~60、speed=0.6~1.8），补入的 `spawnLocType`/`angle`/`positionOffset`/`fleckUsesAngleForVelocity` 取自同族样例 `Core/Defs/Effects/Effecter_Misc.xml:695` 的 `EmergencePointSustained8X8`。
- **② 抽象基类 + 继承 + moteDef/Sustainer**：`Core/Defs/Effects/Effecter_Misc.xml:333` 的 `<EffecterDef Name="Power_Cell_Burning_Base" Abstract="True">`（SubEffecter_SprayerContinuous + moteDef=Mote_PowerCellBurning + ticksBetweenMotes=50 + positionOffset=(0,0,0.4)）、`:360` 的 `Power_Cell_Burning`（ParentName 继承 + SubEffecter_SoundTriggered/SubEffecter_Sustainer + soundDef=BurningPowerCell_Start/Loop + `maintainTicks` 为顶层字段的写法见 `Anomaly/Defs/Effects/Effecter_Misc.xml:434` 的 TachycardiacArrest `maintainTicks=720`）；另一处 Abstract 写法见 `Biotech/Defs/Effects/Effecter_GivingBirth.xml:33`。
- **③ 嵌套 + 间歇音**：`Core/Defs/Effects/Effecter_Misc.xml:695` 的 `EmergencePointSustained8X8`（GroupedChance + chancePerTick .01 + chancePeriodTicks 20 + 嵌套 CameraShakeSingle{cameraShake .1~.3, distanceAttenuationScale, distanceAttenuationMax 30, soundDef Emergence_Quake} + 嵌套 SprayerTriggered 全字段），`intermittentSoundInterval` 的最小可用样例是 `Core/Defs/Effects/Effecter_Misc.xml:62` 的 `PlayPoker`（SubEffecter_SoundIntermittent + soundDef=PokerChips + min 750/max 4300）。
- **④ 吸附与顶层偏移**：`Anomaly/Defs/Effects/Effecter_Misc.xml:2608` 的 `StudyHoraxian`（attachToSpawnThing + useTargetAInitialRotation + perRotationOffsets 四个 li + maxMoteCount + destroyMoteOnCleanup + moteDef=Mote_Clipboard）、`Core/Defs/Effects/Effecter_Damage.xml:57`（顶层 `offsetTowardsTarget=0.25~0.25` 与顶层 `positionRadius=0.1` 紧跟在 `</children>` 之后）、`Anomaly/Defs/Effects/Effecter_Misc.xml` 的 `GhoulFrenzy`（顶层 `offsetMode=Free`）、`:641` 的 `UndercaveCeilingDebris`（顶层 `maintainTicks=130` + `randomWeight=1`）、`AtmosphericHeaterAmbience`（`attachPoint=Exhaust`，全库唯一）。
- **子效果器类名统计**：扫描 20 个 `Effecter_*.xml` 文件（覆盖 Core/Royalty/Ideology/Biotech/Anomaly/Odyssey 六个资料片的 `Defs/Effects/`）得到 15 个 `subEffecterClass` 取值，逐个数写入「常见坑」第 1 条的括号内。
- 未启动游戏加载验证；元素名、嵌套结构与取值全部来自上述原版文件与字段表。
