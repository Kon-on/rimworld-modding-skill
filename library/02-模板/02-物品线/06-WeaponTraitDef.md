# WeaponTraitDef

## 用途

WeaponTraitDef 是"武器词条"：给武器加属性偏移（`statOffsets`）、属性乘算（`statFactors`）、手持时给持有者的加成（`equippedStatOffsets`）、附加 Hediff（`equippedHediffs`）、击杀/绑定相关思维（`killThought` / `bondedThought`）甚至借用能力（`abilityProps`）。原版 62 个实例，其中 6 条字段达到 ≥90%（`commonality`、`defName`、`label`、`description`、`exclusionTags/li`、`traitAdjectives/li`），可视为必填。它靠 `weaponCategory` 限定只出现在某类武器上，取值来自 WeaponCategoryDef（16 个）。与 ThingDef（武器）、WeaponCategoryDef、HediffDef、ThoughtDef、AbilityDef 联动；原版实例见 `Royalty/Defs/WeaponTraitDefs/WeaponTraitDefs.xml` 与 `Odyssey/Defs/WeaponTraitDefs/WeaponTraitDefs.xml`。

## 模板

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Defs>

  <!-- 抽象基类：把 weaponCategory 定死，子词条只出现在该类武器上（原版 BladelinkBase 的写法） -->
  <WeaponTraitDef Name="EXAMPLE_BaseGunTrait" Abstract="True">
    <weaponCategory>Gun</weaponCategory>
  </WeaponTraitDef>

  <!-- 一个完整词条 -->
  <WeaponTraitDef ParentName="EXAMPLE_BaseGunTrait">
    <defName>EXAMPLE_Honed</defName>
    <label>精磨</label>
    <description>这把武器的部件被精细打磨过：远距离更准，但更贵。</description>
    <!-- 出现权重：98.4% 的原版词条都写；原版取值 0.5 / 0.75 / 1 -->
    <commonality>1</commonality>
    <!-- 互斥标签：同标签的词条不会同时出现在一把武器上（每个 li 一个标签） -->
    <exclusionTags>
      <li>EXAMPLE_BarrelWork</li>
      <li>EXAMPLE_SightsWork</li>
    </exclusionTags>
    <!-- 形容词：出现在武器名里（原版 nimble / quick / quickload） -->
    <traitAdjectives>
      <li>honed</li>
      <li>tuned</li>
    </traitAdjectives>
    <!-- statOffsets = 加算（可正可负） -->
    <statOffsets>
      <MarketValue>35</MarketValue>
      <Beauty>2</Beauty>
    </statOffsets>
    <!-- statFactors = 乘算（1.2 = +20%） -->
    <statFactors>
      <AccuracyLong>1.2</AccuracyLong>
      <AccuracyMedium>1.1</AccuracyMedium>
    </statFactors>
    <!-- 市价直接增减（单位：银） -->
    <marketValueOffset>300</marketValueOffset>
    <!-- 手持时给持有者的加成（StatDef 名做元素名） -->
    <equippedStatOffsets>
      <PsychicSensitivity>0.2</PsychicSensitivity>
    </equippedStatOffsets>
    <!-- 手持时附加的 Hediff（写 HediffDef 的 defName） -->
    <equippedHediffs>
      <li>EXAMPLE_TraitFocus</li>
    </equippedHediffs>
  </WeaponTraitDef>

</Defs>
```

## 字段说明

出现率来自 `03-全量字段参考/字段/WeaponTraitDef.md`（分母 62）。

| 字段 | 出现率 | 值类型 | 说明 |
|---|---|---|---|
| `defName` | 98.4% (61/62) | 文本 | 词条唯一名。 |
| `label` | 98.4% (61/62) | 文本 | 显示名（aim assistance / custom grip）。 |
| `description` | 98.4% (61/62) | 文本 | 说明文字。 |
| `commonality` | 98.4% (61/62) | 数值 | 出现权重，原版 0.5 / 0.75 / 1（不是百分比概率）。 |
| `exclusionTags` | 74.2% (46/62) | 容器 | 互斥标签容器。 |
| `exclusionTags/li` | 98.4% (61/62) | 文本 | 单个标签（AmmoType / Barrel / Color …）。 |
| `traitAdjectives` | 67.7% (42/62) | 容器 | 形容词容器。 |
| `traitAdjectives/li` | 214.5% (133/62) | 文本 | 单条形容词（nimble / quick / quickload）；>100% 表示一个 def 多个。 |
| `weaponCategory` | 69.3% (43/62) | 文本 | 限定武器类别，取值来自 WeaponCategoryDef（BulletFiring / Gun / PelletFiring / BladeLink …共 16 个）。 |
| `statOffsets` | 66.1% (41/62) | 容器 | 加算属性容器。 |
| `statOffsets/MarketValue` | 58.1% (36/62) | 数值 | 市价加算（15 / 35 / 50）。 |
| `statOffsets/Beauty` | 8.1% (5/62) | 数值 | 美观加算（-4 / 2 / 20）。 |
| `statOffsets/RangedWeapon_DamageMultiplier` | 14.5% (9/62) | 数值 | 伤害加算（-0.1 / 0.2 / 0.3）。 |
| `statOffsets/RangedWeapon_ArmorPenetrationMultiplier` | 9.7% (6/62) | 数值 | 穿甲加算（-0.25 / 0.15 / 0.2）。 |
| `statOffsets/RangedWeapon_RangeMultiplier` | 9.7% (6/62) | 数值 | 射程加算（0.1 / 0.15 / 0.2）。 |
| `statOffsets/RangedWeapon_WarmupMultiplier` | 6.5% (4/62) | 数值 | 举枪时间加算（-0.2 / 0.2）。 |
| `statFactors` | 24.2% (15/62) | 容器 | 乘算属性容器。 |
| `statFactors/AccuracyLong` | 11.3% (7/62) | 数值 | 远距命中乘算（0.8 / 0.9 / 1.2）。 |
| `statFactors/AccuracyMedium` | 11.3% (7/62) | 数值 | 中距命中乘算（0.8 / 0.9 / 0.95）。 |
| `statFactors/AccuracyShort` | 9.7% (6/62) | 数值 | 近距命中乘算。 |
| `statFactors/AccuracyTouch` | 9.7% (6/62) | 数值 | 贴身命中乘算。 |
| `statFactors/MarketValue` | 8.1% (5/62) | 数值 | 市价乘算（0.8 / 0.85 / 1.4）。 |
| `statFactors/Mass` | 1.6% (1/62) | 数值 | 质量乘算（0.75）。 |
| `statFactors/RangedWeapon_Cooldown` | 3.2% (2/62) | 数值 | 冷却乘算（0.8 / 1.5）。 |
| `marketValueOffset` | 22.6% (14/62) | 数值 | 市价加减（-1000 / -500 / 300）。 |
| `equippedStatOffsets` | 8.1% (5/62) | 容器 | 手持时给持有者的属性偏移。 |
| `equippedStatOffsets/PsychicSensitivity` | 6.5% (4/62) | 数值 | 心灵敏感度（-0.15 / -0.30 / 0.2）。 |
| `equippedStatOffsets/MeditationFocusGain` | 1.6% (1/62) | 数值 | 冥想专注收益（0.1）。 |
| `equippedHediffs` | 4.8% (3/62) | 容器 | 手持时附加 Hediff（`li`：NeuralHeatRecoveryGain / NoPain / SpeedBoost）。 |
| `abilityProps` | 9.7% (6/62) | 容器 | 给武器加"能力"（手雷/EMP 发射）。 |
| `abilityProps/abilityDef` | 9.7% (6/62) | 文本 | AbilityDef 名（EMPPulse / LaunchFragGrenade）。 |
| `abilityProps/ammoDef` | 8.1% (5/62) | 文本 | 弹药物价（Bioferrite / Chemfuel / Steel）。 |
| `abilityProps/ammoCountPerCharge` | 8.1% (5/62) | 数值 | 每次充能的弹药数（10 / 15 / 25）。 |
| `abilityProps/maxCharges` | 8.1% (5/62) | 数值 | 最大充能数（1 / 2）。 |
| `abilityProps/chargeNoun` | 8.1% (5/62) | 文本 | 充能单位名（burner charge / grenade / shell）。 |
| `abilityProps/baseReloadTicks` | 8.1% (5/62) | 数值 | 装填基础 tick（60）。 |
| `abilityProps/soundReload` | 8.1% (5/62) | 文本 | 装填音效（Standard_Reload）。 |
| `forcedColor` | 11.3% (7/62) | 文本 | 强制贴图配色（UniqueWeapon_EMP / UniqueWeapon_Gold）。 |
| `canGenerateAlone` | 12.9% (8/62) | 布尔 | 能否单独生成（原版都写 false）。 |
| `damageDefOverride` | 8.1% (5/62) | 文本 | 覆盖弹丸伤害类型（Bullet_TraitIncendiary / Nerve）。 |
| `bondedThought` | 6.5% (4/62) | 文本 | 绑定后的思维（BondedThoughtCalm / BondedThoughtKind）。 |
| `bondedHediffs` | 1.6% (1/62) | 容器 | 绑定后附加 Hediff（`li`：HungerMaker）。 |
| `killThought` | 3.2% (2/62) | 文本 | 击杀后思维（OnKill_BadThought / OnKill_GoodThought）。 |
| `neverBond` | 1.6% (1/62) | 布尔 | 永不与持有者绑定（true）。 |
| `ignoresAccuracyMaluses` | 1.6% (1/62) | 布尔 | 无视命中惩罚（true）。 |
| `additionalStoppingPower` | 1.6% (1/62) | 数值 | 附加硬直（2）。 |
| `burstShotCountMultiplier` | 1.6% (1/62) | 数值 | 点射发数乘算（1.5）。 |
| `burstShotSpeedMultiplier` | 1.6% (1/62) | 数值 | 点射速度乘算（2）。 |
| `workerClass` | 3.2% (2/62) | 文本 | 自定义逻辑（WeaponTraitWorker_Jealous / _PsyfocusOnKill）。 |
| `extraDamages` | 1.6% (1/62) | 容器 | 附加伤害：`li`（容器）→ `li/def`（EMP）+ `li/amount`（4）。 |

## 常见坑

1. **`commonality` 是权重不是概率**：原版取值只有 0.5 / 0.75 / 1（98.4% 的词条都写）。多个词条的相对权重决定谁更容易被抽到，写 0.5 不等于"50% 概率"（**推测**，取自原版取值分布）。
2. **`exclusionTags` 要成对写才互斥**：两个词条必须带同一个标签才互斥（`li` 98.4%，标签如 AmmoType / Barrel / Color）。只在一侧写标签不会互斥（**推测**）。
3. **`statOffsets` 是加算、`statFactors` 是乘算**：市价加算 `statOffsets/MarketValue`（58.1%，35/50/15）；命中乘算 `statFactors/AccuracyLong`（11.3%，0.8/0.9/1.2）。把 1.2 写进 `statOffsets` 会变成"+1.2 倍数值"而不是"+20%"（**推测**）。
4. **`abilityProps` 是成套字段**：`abilityDef`（9.7%）、`ammoDef`、`ammoCountPerCharge`、`maxCharges`、`chargeNoun`、`baseReloadTicks`、`soundReload`（各 8.1%）在原版总是同时出现；只写一半会导致能力没有弹药或没有充能（**推测**）。
5. **词条不会自动出现在普通武器上**：原版 62 个词条的 `weaponCategory` 集中在 BladeLink / Gun / BulletFiring 等类别（69.3% 写了它），说明词条靠武器类别匹配；新建的普通枪不会自带词条，需要代码侧或对应武器框架支持（**推测**，未查 C# 侧）。
6. **靠 `ParentName` 继承时 `weaponCategory` 只写一次**：原版 `BladelinkBase` 抽象 Def 里写 `<weaponCategory>BladeLink</weaponCategory>`，12 个子词条都不重复写。子 Def 里再写一次会覆盖父值（**推测**，属 Def 框架通用行为）。

## 核验

- **逐字段对照**：上表出现率取自 `03-全量字段参考/字段/WeaponTraitDef.md`（分母 62），可用机器可读版复核：
  `Select-String -Path '03-全量字段参考\字段总表.csv' -Pattern ',WeaponTraitDef,statFactors/AccuracyLong,'`。
- **结构照抄原版**（路径相对 `E:\SteamLibrary\steamapps\common\RimWorld\Data\`）：
  - `Royalty/Defs/WeaponTraitDefs/WeaponTraitDefs.xml`：BladelinkBase（第 6 行，`weaponCategory` 抽象基类写法）、PsychicSensitivityUpMajor（第 10 行，`commonality 0.75` + `equippedStatOffsets` + `exclusionTags`）、PsyfocusMeditationBonus（第 256 行，`marketValueOffset 500`）、NeverBond（第 369 行，`neverBond true`）、Jealous（第 380 行，`workerClass WeaponTraitWorker_Jealous`）。
  - `Odyssey/Defs/WeaponTraitDefs/WeaponTraitDefs.xml`：AimAssistance / CustomGrip / QuickReload / ExtendedMagazine / JadeInlay / GoldInlay 等词条与 `abilityProps` 用法。
  - `Odyssey/Defs/WeaponTraitDefs/WeaponCategoryDefs.xml`：`weaponCategory` 的 16 个合法取值（Ranged / BulletFiring / Bow / Rifle / Sighted / Scoped / Shotgun / BurstFire / LowStoppingPower / Gun / PelletFiring / PulseCharge / Pistol / BeamWeapon / Attachable / BladeLink），对应 `03-全量字段参考/字段/WeaponCategoryDef.md`。
- **Def 级属性说明**：`ParentName` / `Abstract` / `Name` 不在字段表内，属 Def 框架属性；本模板沿用原版"抽象基类定 weaponCategory、子词条只写差异"的写法。
- **待验证项**：常见坑 1–6 的因果描述均为**推测**（静态比对原版取值分布得出，未在游戏内实测，也未查反编译代码）；所有字段路径本身均可由字段表核实存在。
