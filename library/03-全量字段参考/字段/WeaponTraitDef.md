# WeaponTraitDef

- **所属线**：物品线
- **原版实例数**：62
- **字段路径数**：55
- **资料片**：Odyssey、Royalty
- **原版出处**：`Royalty/Defs/WeaponTraitDefs/WeaponTraitDefs.xml`、`Odyssey/Defs/WeaponTraitDefs/WeaponTraitDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<WeaponTraitDef Name="BladelinkBase" Abstract="True">
    <weaponCategory>BladeLink</weaponCategory>
  </WeaponTraitDef>
  
  
```

> 来自 `Royalty/Defs/WeaponTraitDefs/WeaponTraitDefs.xml`，defName = ``，XML 节点数 2（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
commonality                                    [数值]  例：0.5 / 0.75 / 1
defName                                        [文本]  例：AimAssistance / CustomGrip / QuickReload
description                                    [文本]  例：This weapon contains a customized grip that handles recoil better, improving acc / This weapon contains a rudimentary aim assistant computer which helps track targ / This weapon has a quick release-and-replace mechanism that makes it faster to re
exclusionTags/li                               [文本]  例：AmmoType / Barrel / Color
label                                          [文本]  例：aim assistance / custom grip / pistol brace
traitAdjectives/li                             [文本]  例：nimble / quick / quickload
```

## 三、全量字段表（55 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `abilityProps` | 9.7% (6/62) | 容器 |  |
| `abilityProps/abilityDef` | 9.7% (6/62) | 文本 | EMPPulse / LaunchEMPShell / LaunchFragGrenade |
| `abilityProps/ammoCountPerCharge` | 8.1% (5/62) | 数值 | 10 / 15 / 25 |
| `abilityProps/ammoDef` | 8.1% (5/62) | 文本 | Bioferrite / Chemfuel / Steel |
| `abilityProps/baseReloadTicks` | 8.1% (5/62) | 数值 | 60 |
| `abilityProps/chargeNoun` | 8.1% (5/62) | 文本 | burner charge / grenade / shell |
| `abilityProps/maxCharges` | 8.1% (5/62) | 数值 | 1 / 2 |
| `abilityProps/soundReload` | 8.1% (5/62) | 文本 | Standard_Reload |
| `additionalStoppingPower` | 1.6% (1/62) | 数值 | 2 |
| `bondedHediffs` | 1.6% (1/62) | 容器 |  |
| `bondedHediffs/li` | 1.6% (1/62) | 文本 | HungerMaker |
| `bondedThought` | 6.5% (4/62) | 文本 | BondedThoughtCalm / BondedThoughtKind / BondedThoughtMuttering |
| `burstShotCountMultiplier` | 1.6% (1/62) | 数值 | 1.5 |
| `burstShotSpeedMultiplier` | 1.6% (1/62) | 数值 | 2 |
| `canGenerateAlone` | 12.9% (8/62) | 布尔 | false |
| `commonality` | 98.4% (61/62) | 数值 | 0.5 / 0.75 / 1 |
| `damageDefOverride` | 8.1% (5/62) | 文本 | Bullet_TraitIncendiary / Bullet_TraitTox / Nerve |
| `defName` | 98.4% (61/62) | 文本 | AimAssistance / CustomGrip / QuickReload |
| `description` | 98.4% (61/62) | 文本 | This weapon contains a customized grip that handles recoil better, improving acc / This weapon contains a rudi |
| `equippedHediffs` | 4.8% (3/62) | 容器 |  |
| `equippedHediffs/li` | 4.8% (3/62) | 文本 | NeuralHeatRecoveryGain / NoPain / SpeedBoost |
| `equippedStatOffsets` | 8.1% (5/62) | 容器 |  |
| `equippedStatOffsets/MeditationFocusGain` | 1.6% (1/62) | 数值 | 0.1 |
| `equippedStatOffsets/PsychicSensitivity` | 6.5% (4/62) | 数值 | -0.15 / -0.30 / 0.2 |
| `exclusionTags` | 74.2% (46/62) | 容器 |  |
| `exclusionTags/li` | 98.4% (61/62) | 文本 | AmmoType / Barrel / Color |
| `extraDamages` | 1.6% (1/62) | 容器 |  |
| `extraDamages/li` | 1.6% (1/62) | 容器 |  |
| `extraDamages/li/amount` | 1.6% (1/62) | 数值 | 4 |
| `extraDamages/li/def` | 1.6% (1/62) | 文本 | EMP |
| `forcedColor` | 11.3% (7/62) | 文本 | UniqueWeapon_EMP / UniqueWeapon_Fire / UniqueWeapon_Gold |
| `ignoresAccuracyMaluses` | 1.6% (1/62) | 布尔 | true |
| `killThought` | 3.2% (2/62) | 文本 | OnKill_BadThought / OnKill_GoodThought |
| `label` | 98.4% (61/62) | 文本 | aim assistance / custom grip / pistol brace |
| `marketValueOffset` | 22.6% (14/62) | 数值 | -1000 / -500 / 300 |
| `neverBond` | 1.6% (1/62) | 布尔 | true |
| `statFactors` | 24.2% (15/62) | 容器 |  |
| `statFactors/AccuracyLong` | 11.3% (7/62) | 数值 | 0.8 / 0.9 / 1.2 |
| `statFactors/AccuracyMedium` | 11.3% (7/62) | 数值 | 0.8 / 0.9 / 0.95 |
| `statFactors/AccuracyShort` | 9.7% (6/62) | 数值 | 0.8 / 0.9 / 1.1 |
| `statFactors/AccuracyTouch` | 9.7% (6/62) | 数值 | 0.8 / 0.9 / 1.1 |
| `statFactors/MarketValue` | 8.1% (5/62) | 数值 | 0.8 / 0.85 / 1.4 |
| `statFactors/Mass` | 1.6% (1/62) | 数值 | 0.75 |
| `statFactors/RangedWeapon_Cooldown` | 3.2% (2/62) | 数值 | 0.8 / 1.5 |
| `statOffsets` | 66.1% (41/62) | 容器 |  |
| `statOffsets/Beauty` | 8.1% (5/62) | 数值 | -4 / 2 / 20 |
| `statOffsets/MarketValue` | 58.1% (36/62) | 数值 | 15 / 35 / 50 |
| `statOffsets/RangedWeapon_ArmorPenetrationMultiplier` | 9.7% (6/62) | 数值 | -0.25 / 0.15 / 0.2 |
| `statOffsets/RangedWeapon_DamageMultiplier` | 14.5% (9/62) | 数值 | -0.1 / 0.2 / 0.3 |
| `statOffsets/RangedWeapon_RangeMultiplier` | 9.7% (6/62) | 数值 | 0.1 / 0.15 / 0.2 |
| `statOffsets/RangedWeapon_WarmupMultiplier` | 6.5% (4/62) | 数值 | -0.2 / -0.25 / 0.2 |
| `traitAdjectives` | 67.7% (42/62) | 容器 |  |
| `traitAdjectives/li` | 214.5% (133/62) | 文本 | nimble / quick / quickload |
| `weaponCategory` | 69.3% (43/62) | 文本 | BulletFiring / Gun / PelletFiring |
| `workerClass` | 3.2% (2/62) | 文本 | WeaponTraitWorker_Jealous / WeaponTraitWorker_PsyfocusOnKill |

## 四、原版 defName 一览（共 62 个，列出前 60）

```text
``                                `PsyfocusMeditationBonus`         `NoPain`                          `SpeedBoost`                    
`HungerMaker`                     `NeuralHeatRecoveryGain`          `NeverBond`                       `PsychicSensitivityUpMajor`     
`PsychicSensitivityUpMinor`       `PsychicSensitivityDownMinor`     `PsychicSensitivityDownMajor`     `OnKill_PsyfocusGain`           
`OnKill_ThoughtGood`              `OnKill_ThoughtBad`               `NeedKill`                        `Jealous`                       
`ThoughtKind`                     `ThoughtCalm`                     `ThoughtMuttering`                `ThoughtWailing`                
`ReinforcedLimbs`                 `ExtendedMagazine`                `ChargeCapacitor`                 `RapidFire`                     
`BroadheadArrows`                 `ExtendedBarrel`                  `PrecisionScope`                  `RangefinderScope`              
`ShortenedBarrel`                 `FrequencyAmplifier`              `ParalyticArrows`                 `LightweightArrows`             
`EMPPulser`                       `QuickReload`                     `PiercingRounds`                  `ShoddySights`                  
`Lightweight`                     `HollowPointRounds`               `PiercingArrows`                  `ImprovedSights`                
`OversizedRounds`                 `Ornamental`                      `Ugly`                            `Cumbersome`                    
`JadeInlay`                       `CustomGrip`                      `StabilizerBrace`                 `ToxPellets`                    
`GoldInlay`                       `ToxRounds`                       `AimAssistance`                   `PulseCharger`                  
`BirdshotPellets`                 `IncendiaryRounds`                `IncendiaryPellets`               `GrenadeLauncher`               
`EMPRounds`                       `HighPowerRounds`                 `EMPLauncher`                     `SmokeLauncher`                 
```

_余下 2 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
