# DamageDef

- **所属线**：物品线
- **原版实例数**：53
- **字段路径数**：83
- **资料片**：Anomaly、Biotech、Core、Odyssey
- **原版出处**：`Anomaly/Defs/DamageDefs/Damages_Misc.xml`、`Core/Defs/DamageDefs/Damages_Medical.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<DamageDef ParentName="Vaporize">
    <defName>NociosphereVaporize</defName>
    <soundExplosion>FleshmelterBolt_Blast</soundExplosion>
  </DamageDef>
  
```

> 来自 `Anomaly/Defs/DamageDefs/Damages_Misc.xml`，defName = `NociosphereVaporize`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Digested / ElectricalBurn / EnergyBolt
```

## 三、全量字段表（83 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `additionalHediffs` | 7.5% (4/53) | 容器 |  |
| `additionalHediffs/li` | 7.5% (4/53) | 容器 |  |
| `additionalHediffs/li/hediff` | 7.5% (4/53) | 文本 | ToxicBuildup |
| `additionalHediffs/li/inverseStatScaling` | 7.5% (4/53) | 布尔 | true |
| `additionalHediffs/li/severityPerDamageDealt` | 7.5% (4/53) | 数值 | 0.0065 / 0.015 |
| `additionalHediffs/li/victimSeverityScaling` | 7.5% (4/53) | 文本 | ToxicResistance |
| `additionalHediffs/li/victimSeverityScalingByInvBodySize` | 7.5% (4/53) | 布尔 | true |
| `additionalHediffsThisPart` | 3.8% (2/53) | 容器 |  |
| `additionalHediffsThisPart/li` | 3.8% (2/53) | 文本 | PorcupineQuill |
| `applyAdditionalHediffsIfHuntingForFood` | 9.4% (5/53) | 布尔 | false / true |
| `armorCategory` | 35.9% (19/53) | 容器/文本 | Blunt / Heat / Sharp |
| `bluntInnerHitChance` | 1.9% (1/53) | 数值 | 0.4 |
| `bluntInnerHitDamageFractionToAdd` | 1.9% (1/53) | 文本 | 0.2~0.35 |
| `bluntInnerHitDamageFractionToConvert` | 1.9% (1/53) | 文本 | 0.1~0.2 |
| `bluntStunChancePerDamagePctOfCorePartToBodyCurve` | 1.9% (1/53) | 容器 |  |
| `bluntStunChancePerDamagePctOfCorePartToBodyCurve/points` | 1.9% (1/53) | 容器 |  |
| `bluntStunChancePerDamagePctOfCorePartToBodyCurve/points/li` | 3.8% (2/53) | 文本 | (0.4, 0) / (0.9, 0.15) |
| `bluntStunChancePerDamagePctOfCorePartToHeadCurve` | 1.9% (1/53) | 容器 |  |
| `bluntStunChancePerDamagePctOfCorePartToHeadCurve/points` | 1.9% (1/53) | 容器 |  |
| `bluntStunChancePerDamagePctOfCorePartToHeadCurve/points/li` | 3.8% (2/53) | 文本 | (0.04, 0.20) / (0.5, 1) |
| `bluntStunDuration` | 1.9% (1/53) | 数值 | 2.0 |
| `buildingDamageFactor` | 3.8% (2/53) | 数值 | 1.5 / 10 |
| `buildingDamageFactorImpassable` | 11.3% (6/53) | 数值 | 0.4 / 0.75 / 15 |
| `buildingDamageFactorPassable` | 9.4% (5/53) | 数值 | 0.2 / 2 / 5 |
| `canInterruptJobs` | 17.0% (9/53) | 布尔 | false |
| `canUseDeflectMetalEffect` | 3.8% (2/53) | 布尔 | false |
| `causeStun` | 7.5% (4/53) | 布尔 | true |
| `combatLogRules` | 18.9% (10/53) | 文本 | Damage_Extinguish / Damage_Flame / Damage_MechBandShockwave |
| `consideredHelpful` | 1.9% (1/53) | 布尔 | true |
| `constantStunDurationTicks` | 1.9% (1/53) | 数值 | 1200 |
| `corpseDamageFactor` | 3.8% (2/53) | 数值 | 0.1 / 0.5 |
| `cutCleaveBonus` | 1.9% (1/53) | 数值 | 1.4 |
| `cutExtraTargetsCurve` | 1.9% (1/53) | 容器 |  |
| `cutExtraTargetsCurve/points` | 1.9% (1/53) | 容器 |  |
| `cutExtraTargetsCurve/points/li` | 7.5% (4/53) | 文本 | 0, 0 / 0.6, 1 / 0.9, 2 |
| `damageEffecter` | 5.7% (3/53) | 文本 | Impact_Toxic |
| `deathMessage` | 52.8% (28/53) | 文本 | {0} died from being digested. / {0} has been killed by a psychic attack. / {0} has been killed by an energy bo |
| `defaultArmorPenetration` | 13.2% (7/53) | 数值 | 0 / 0.10 / 1 |
| `defaultDamage` | 24.5% (13/53) | 数值 | 0 / 10 / 50 |
| `defaultStoppingPower` | 5.7% (3/53) | 数值 | 0.5 / 1.5 / 2.0 |
| `defName` | 98.1% (52/53) | 文本 | Digested / ElectricalBurn / EnergyBolt |
| `execution` | 1.9% (1/53) | 布尔 | true |
| `explosionAffectOutsidePartsOnly` | 3.8% (2/53) | 布尔 | false |
| `explosionCellEffecter` | 1.9% (1/53) | 文本 | MechBandElectricityArc |
| `explosionCellEffecterChance` | 1.9% (1/53) | 数值 | 0.1 |
| `explosionCellEffecterMaxRadius` | 1.9% (1/53) | 数值 | 10 |
| `explosionCellFleck` | 18.9% (10/53) | 文本 | BlastDry / BlastExtinguisher / BlastFlame |
| `explosionCenterEffecter` | 1.9% (1/53) | 文本 | BlastMechBandShockwave |
| `explosionColorCenter` | 9.4% (5/53) | 文本 | (0.26, 0.51, 0.97) / (0.73, 0.93, 0.96) / (1, 0.5, 0.3) |
| `explosionColorEdge` | 18.9% (10/53) | 文本 | (0.26, 0.51, 0.97) / (0.706, 0.839, 0.09, 0.05) / (1, 1, 0.7) |
| `explosionHeatEnergyPerCell` | 5.7% (3/53) | 数值 | 15 / 20 / 5 |
| `explosionInteriorFleck` | 1.9% (1/53) | 文本 | ElectricalSpark |
| `explosionSnowMeltAmount` | 3.8% (2/53) | 数值 | 0 |
| `expolosionPropagationSpeed` | 1.9% (1/53) | 数值 | 0.3 |
| `externalViolence` | 35.9% (19/53) | 布尔 | false / true |
| `externalViolenceForMechanoids` | 3.8% (2/53) | 布尔 | true |
| `harmAllLayersUntilOutside` | 28.3% (15/53) | 布尔 | false / true |
| `harmsHealth` | 13.2% (7/53) | 布尔 | false |
| `hasForcefulImpact` | 13.2% (7/53) | 布尔 | false / true |
| `hediff` | 50.9% (27/53) | 文本 | Digested / ElectricalBurn / EnergyBolt |
| `hediffSkin` | 9.4% (5/53) | 文本 | Bruise / Cut / ExecutionCut |
| `hediffSolid` | 22.6% (12/53) | 文本 | Crack / PsychicInjurySolid |
| `igniteCellChance` | 1.9% (1/53) | 数值 | 1 |
| `igniteChanceByTargetFlammability` | 3.8% (2/53) | 容器 |  |
| `igniteChanceByTargetFlammability/points` | 3.8% (2/53) | 容器 |  |
| `igniteChanceByTargetFlammability/points/li` | 7.5% (4/53) | 文本 | (0, 0) / (1, 0.3) / (1, 1) |
| `ignoreShields` | 1.9% (1/53) | 布尔 | true |
| `impactSoundType` | 41.5% (22/53) | 容器/文本 | Bullet / Electric / MechBandShockwave |
| `isExplosive` | 3.8% (2/53) | 布尔 | true |
| `isRanged` | 9.4% (5/53) | 布尔 | true |
| `label` | 84.9% (45/53) | 文本 | digestion / electrical burn / energy bolt |
| `makesAnimalsFlee` | 11.3% (6/53) | 布尔 | true |
| `makesBlood` | 17.0% (9/53) | 布尔 | false |
| `minDamageToFragment` | 9.4% (5/53) | 数值 | 1 / 15 |
| `overkillPctToDestroyPart` | 22.6% (12/53) | 文本 | 0.4~1.0 / 0~0.1 / 0~0.7 |
| `plantDamageFactor` | 7.5% (4/53) | 数值 | 10 / 2 / 4 |
| `scaleDamageToBuildingsBasedOnFlammability` | 5.7% (3/53) | 布尔 | false / true |
| `scratchSplitPercentage` | 1.9% (1/53) | 数值 | 0.67 |
| `soundExplosion` | 22.6% (12/53) | 文本 | Explosion_Flame / Explosion_MechBandShockwave / Explosion_Smoke |
| `stabChanceOfForcedInternal` | 5.7% (3/53) | 数值 | 0.4 / 0.6 |
| `stunAdaptationTicks` | 3.8% (2/53) | 数值 | 2200 / 240 |
| `stunResistStat` | 1.9% (1/53) | 文本 | EMPResistance |
| `workerClass` | 58.5% (31/53) | 文本 | DamageWorker_AddInjury / DamageWorker_Flame / DamageWorker_Frostbite |

## 四、原版 defName 一览（共 53 个，列出前 60）

```text
`NociosphereVaporize`             `Mining`                          `ArrowHighVelocity`               ``                              
`BeamBypassShields`               `Burn`                            `Poke`                            `Demolish`                      
`BombSuper`                       `Nerve`                           `NerveStun`                       `MiningBomb`                    
`Digested`                        `Deterioration`                   `Rotting`                         `Decayed`                       
`PorcupineBite`                   `PorcupineScratch`                `AcidBurn`                        `Bullet_TraitIncendiary`        
`Psychic`                         `Frostbite`                       `VacuumBurn`                      `ElectricalBurn`                
`DeadlifeDust`                    `ToxGas`                          `SurgicalCut`                     `Smoke`                         
`Stun`                            `BulletToxic`                     `TornadoScratch`                  `ExecutionCut`                  
`Stab`                            `Bite`                            `Bullet_TraitTox`                 `Crush`                         
`Scratch`                         `ScratchToxic`                    `ToxicBite`                       `Bullet`                        
`Extinguish`                      `RangedStab`                      `Arrow`                           `Beam`                          
`EMP`                             `EnergyBolt`                      `MechBandShockwave`               `Cut`                           
`Flame`                           `Thump`                           `Vaporize`                        `Blunt`                         
`Bomb`                          
```
