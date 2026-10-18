# JobDef

## 用途

「一个具体行为」的定义——去搬运、去躺下休息、去攻击。它是 XML 与 C# 的分界线：`driverClass` 指向真正执行行为的 JobDriver 子类，XML 只负责这个行为的文案与调度属性（可不可以被打断、要不要拿武器、娱乐属性等）。

JobDef 自己不会发生：必须有东西去「派」它——`WorkGiverDef` 的 giverClass 在扫描后创建 Job、ThinkTree 的决策节点、`AbilityDef`、`JoyGiverDef`、`DutyDef` 或 C# 组件。反过来，一个 WorkGiverDef 若没有可用的 JobDef，也无法产生行为。原版 1.7 共 321 个大写 `JobDef` 实例 + 6 个小写 `jobDef` 历史遗留实例，33 条字段路径。

## 模板

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Defs>

  <!-- 搬运类行为：直接复用原版 JobDriver_HaulToCell（Core/Defs/JobDefs/Jobs_Work.xml 在用） -->
  <JobDef>
    <defName>EXAMPLE_HaulAlloyToCell</defName>

    <!-- 真正执行行为的 C# 类，必须是 JobDriver 的子类 -->
    <driverClass>JobDriver_HaulToCell</driverClass>

    <!-- 小人头顶的状态文字。TargetA / TargetB / TargetC 会被替换成 job 的目标 -->
    <reportString>hauling TargetA.</reportString>

    <!-- 睡觉/吃饭时能否被挂起（原版 25/321 写它） -->
    <suspendable>false</suspendable>

    <!-- 允许被「顺路顺便做」的合并前缀（原版 167/321 写它） -->
    <allowOpportunisticPrefix>true</allowOpportunisticPrefix>
  </JobDef>

  <!-- 休息类行为：复用原版 JobDriver_LayDown（Core/Defs/JobDefs/Jobs_Misc.xml 在用） -->
  <JobDef>
    <defName>EXAMPLE_LayDownAtAlloyBench</defName>
    <driverClass>JobDriver_LayDown</driverClass>
    <reportString>resting at the alloy bench.</reportString>

    <!-- 玩家不需要打断它：受到伤害时也不逃（原版 Steal / Kidnap 就是 Never） -->
    <casualInterruptible>false</casualInterruptible>
    <checkOverrideOnDamage>Never</checkOverrideOnDamage>
  </JobDef>

  <!-- 历史遗留写法：原版确实存在 6 处小写 <jobDef> 根元素（Biotech Jobs_Learning.xml 5 处、
       Core Jobs_Misc.xml 的 TriggerObject），游戏能正常加载。新 mod 请一律写大写 <JobDef>。
  <jobDef>
    <defName>EXAMPLE_LegacyForm</defName>
    <driverClass>JobDriver_UseItem</driverClass>
    <reportString>triggering TargetA.</reportString>
  </jobDef>
  -->

</Defs>
```

## 字段说明

全量 33 条路径（出现率 = 该路径在原版 321 个大写实例中的出现比例，直接取自字段参考）。

| 字段 | 出现率 | 值类型 | 说明 |
|---|---|---|---|
| `defName` | 99.7% (320/321) | 文本 | Def 唯一 ID；缺的 1 个是 Biotech 的 Abstract 基类 BabyPlay |
| `driverClass` | 99.1% (318/321) | 文本 | C# JobDriver 类名，例：JobDriver_Wait / JobDriver_TakeToBed |
| `reportString` | 94.4% (303/321) | 文本 | 头顶状态文字，占位符 TargetA/TargetB/TargetC |
| `allowOpportunisticPrefix` | 52.0% (167/321) | 布尔 | 允许顺路合并执行 |
| `casualInterruptible` | 22.7% (73/321) | 布尔 | 可被日常事务打断 |
| `carryThingAfterJob` | 8.4% (27/321) | 布尔 | 做完后继续拿着东西 |
| `suspendable` | 7.8% (25/321) | 布尔 | 睡觉/吃饭时可否挂起 |
| `neverShowWeapon` | 7.5% (24/321) | 布尔 | 不显示武器 |
| `joyDuration` | 7.2% (23/321) | 数值 | 娱乐时长，例：2000 / 3000 |
| `joyKind` | 6.9% (22/321) | 文本 | 娱乐种类，取值来自 JoyKindDef |
| `dropThingBeforeJob` | 6.5% (21/321) | 布尔 | 开工前放下手持物 |
| `taleOnCompletion` | 4.7% (15/321) | 文本 | 完成时记录的 TaleDef，例：BuiltSnowman |
| `alwaysShowWeapon` | 4.0% (13/321) | 布尔 | 总是显示武器 |
| `checkOverrideOnDamage` | 4.0% (13/321) | 文本 | 受伤时的重判策略，例：Never / OnlyIfInstigatorNotJobTarget |
| `isCrawlingIfDowned` | 4.0% (13/321) | 布尔 | 倒地后爬行执行 |
| `tryStartFlying` | 3.7% (12/321) | 布尔 | 尝试飞行前往 |
| `overrideFlyChance` | 3.1% (10/321) | 数值 | 强制飞行概率，例：1 |
| `joyMaxParticipants` | 2.8% (9/321) | 数值 | 娱乐最大参与人数，例：2 / 3 / 4 |
| `collideWithPawns` | 2.5% (8/321) | 布尔 | 与其它小人碰撞 |
| `joySkill` | 2.5% (8/321) | 文本 | 娱乐同时练的技能，例：Artistic / Intellectual |
| `joyXpPerTick` | 2.5% (8/321) | 数值 | 娱乐技能经验，例：0.0015 / 0.002 |
| `playerInterruptible` | 1.9% (6/321) | 布尔 | 玩家可否打断 |
| `isIdle` | 1.6% (5/321) | 布尔 | 属于发呆行为 |
| `makeTargetPrisoner` | 1.6% (5/321) | 布尔 | 把目标变成囚犯 |
| `forceCompleteBeforeNextJob` | 0.6% (2/321) | 布尔 | 必须做完才能接下一个活 |
| `abilityCasting` | 0.6% (2/321) | 布尔 | 属于技能施放 |
| `alwaysShowReport` | 0.6% (2/321) | 布尔 | 总是显示报告文本 |
| `displayAsAreaInFloatMenu` | 0.6% (2/321) | 布尔 | 在右键菜单里以区域形式显示 |
| `ifFlyingKeepFlying` | 0.6% (2/321) | 布尔 | 飞行途中保持飞行 |
| `sleepCanInterrupt` | 0.6% (2/321) | 布尔 | 睡眠可打断 |
| `containerReservationLayer` | 0.3% (1/321) | 文本 | 容器预定层，原文样例 Empty |
| `neverFleeFromEnemies` | 0.3% (1/321) | 布尔 | 遇敌不逃 |
| `waitAfterArriving` | 0.3% (1/321) | 数值 | 到达后等待时长，原文样例 2000 |

## 常见坑

1. **`driverClass` 实质必填。** 原版 318/321 都写；未写的只有 2 个（Biotech/Defs/JobDefs/Jobs_Misc.xml 的 CastAbilityOnThingWithoutWeapon 与 CastAbilityOnThingWithoutWeaponInterruptible），它们为何仍能加载未核实（待验证），不要照抄。做一个全新行为必须自己写 JobDriver 子类；只想复用现成行为时，原版最通用的类是 JobDriver_Wait（被 5 个 JobDef 复用）。
2. **`reportString` 可以省略（17/321 未写），但省了小人头顶就没有状态文字。** 占位符原版只用到 TargetA（388 次）、TargetB（42 次）、TargetC（8 次）；唯一例外是 Anomaly/Defs/JobDefs/Jobs_Misc.xml 的 BuildCubeSculpture 用 `{0}`（"building a {0} sculpture."）——{0} 需要 C# 侧提供参数，照抄很可能取不到值（推测）。
3. **小写 `<jobDef>` 是历史遗留且确实存在：原版共 6 处**（Biotech/Defs/JobDefs/Jobs_Learning.xml 第 16/22/28/34/40 行的 Radiotalking、Floordrawing、Workwatching、Lessontaking、Lessongiving；Core/Defs/JobDefs/Jobs_Misc.xml:467 的 TriggerObject）。它们能随原版正常加载，说明 Def 类型名的匹配不区分大小写（待验证：未反编译核实）。注意：用 grep 会搜到 60 多处小写 jobDef，其中绝大多数是 AbilityDef、ThinkTreeDef、HediffDef、JoyGiverDef、BabyPlayDef、LearningDesireDef、DutyDef、QuestScriptDef 里的子元素引用，不是根 Def——别误判。新 mod 一律写 `<JobDef>`。
4. **`suspendable` 与 `casualInterruptible` 可以同时写。** 原版有 5 个实例同时写了二者（CastAbilityOnThingUninterruptible、Vomit、Lovin、GotoMindControlled、TendPatient），不必二选一。
5. **JobDef 只是定义，没人派它就不会发生。** 需要 WorkGiverDef（giverClass 扫描后创建 Job）、ThinkTreeDef、AbilityDef、JoyGiverDef、DutyDef 或 C# 组件来触发。只写一个 JobDef，游戏里不会出现任何新行为。
6. **同类型同名 defName 不会硬崩，但会互相覆盖。** 原版 FillIn 在 Core/Defs/JobDefs/Jobs_Work.xml:298 与 Anomaly/Defs/JobDefs/Jobs_Work.xml:22 各有一份、内容一致，游戏正常加载（覆盖/合并的确切语义待验证）；自己的两个 JobDef 撞名会让其中一个的字段被另一个覆盖（推测）。
7. **`joyKind`/`joyDuration`/`joySkill`/`joyXpPerTick`/`joyMaxParticipants` 只对娱乐类 Job 有意义**（原版各约 8~23 个实例）。`joyKind` 的取值来自 JoyKindDef：Meditative、Chemical、Gaming_Dexterity、Gaming_Cerebral、Television、Telescope、HighCulture、Social、Gluttonous、Reading。

## 核验

本模板逐字段对照的原版位置（相对 <游戏安装目录>\Data\）：

| 模板里的写法 | 原版依据 |
|---|---|
| `driverClass JobDriver_HaulToCell` + `reportString` + `suspendable` + `allowOpportunisticPrefix` | Core/Defs/JobDefs/Jobs_Work.xml（HaulToCell：JobDriver_HaulToCell、reportString "hauling TargetA."、suspendable false、allowOpportunisticPrefix true；FillIn 在该文件 :298 用 JobDriver_FillIn） |
| `driverClass JobDriver_LayDown` + `casualInterruptible` + `checkOverrideOnDamage` | Core/Defs/JobDefs/Jobs_Misc.xml（JobDriver_LayDown 被 2 个 JobDef 复用）；Jobs_Work.xml（Steal 与 Kidnap 写 casualInterruptible false + checkOverrideOnDamage Never；Rescue 写 carryThingAfterJob true + dropThingBeforeJob false） |
| 同时写 `suspendable` 与 `casualInterruptible` | Core/Defs/JobDefs/Jobs_Misc.xml（CastAbilityOnThingUninterruptible、Vomit、Lovin、GotoMindControlled）与 Jobs_Work.xml（TendPatient） |
| 小写 `jobDef` 历史写法 | Biotech/Defs/JobDefs/Jobs_Learning.xml:16/22/28/34/40（Radiotalking、Floordrawing、Workwatching、Lessontaking、Lessongiving）；Core/Defs/JobDefs/Jobs_Misc.xml:467（TriggerObject）。字段参考：library/03-全量字段参考/字段/jobDef_variant.md（6 实例 / 4 路径） |
| 缺 `driverClass` / `reportString` 的原版实例 | Biotech/Defs/JobDefs/Jobs_Misc.xml（CastAbilityOnThingWithoutWeapon、CastAbilityOnThingWithoutWeaponInterruptible）；Biotech/Defs/JobDefs/Jobs_Play.xml（Abstract BabyPlay 只写 reportString） |
| 各字段出现率 | library/03-全量字段参考/字段/JobDef.md（321 实例 / 33 路径），由 docs/def-schema.json 实测生成 |
