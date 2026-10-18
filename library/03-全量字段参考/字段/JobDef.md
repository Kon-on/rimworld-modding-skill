# JobDef

- **所属线**：系统线
- **原版实例数**：321
- **字段路径数**：33
- **资料片**：Anomaly、Biotech、Core、Ideology、Odyssey、Royalty
- **原版出处**：`Biotech/Defs/JobDefs/Jobs_Play.xml`、`Core/Defs/JobDefs/Jobs_Work.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<JobDef Abstract="True" Name="BabyPlay">
    <reportString>playing with TargetA.</reportString>
  </JobDef>

  
```

> 来自 `Biotech/Defs/JobDefs/Jobs_Play.xml`，defName = ``，XML 节点数 2（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：RevenantAttack / RevenantEscape / RevenantSleep
driverClass                                    [文本]  例：JobDriver_RevenantAttack / JobDriver_RevenantEscape / JobDriver_RevenantSleep
reportString                                   [文本]  例：escaping / hibernating / stalking TargetA.
```

## 三、全量字段表（33 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `abilityCasting` | 0.6% (2/321) | 布尔 | true |
| `allowOpportunisticPrefix` | 52.0% (167/321) | 布尔 | false / true |
| `alwaysShowReport` | 0.6% (2/321) | 布尔 | true |
| `alwaysShowWeapon` | 4.0% (13/321) | 布尔 | true |
| `carryThingAfterJob` | 8.4% (27/321) | 布尔 | true |
| `casualInterruptible` | 22.7% (73/321) | 布尔 | false / true |
| `checkOverrideOnDamage` | 4.0% (13/321) | 文本 | Never / OnlyIfInstigatorNotJobTarget |
| `collideWithPawns` | 2.5% (8/321) | 布尔 | true |
| `containerReservationLayer` | 0.3% (1/321) | 文本 | Empty |
| `defName` | 99.7% (320/321) | 文本 | RevenantAttack / RevenantEscape / RevenantSleep |
| `displayAsAreaInFloatMenu` | 0.6% (2/321) | 布尔 | false |
| `driverClass` | 99.1% (318/321) | 文本 | JobDriver_RevenantAttack / JobDriver_RevenantEscape / JobDriver_RevenantSleep |
| `dropThingBeforeJob` | 6.5% (21/321) | 布尔 | false |
| `forceCompleteBeforeNextJob` | 0.6% (2/321) | 布尔 | false / true |
| `ifFlyingKeepFlying` | 0.6% (2/321) | 布尔 | true |
| `isCrawlingIfDowned` | 4.0% (13/321) | 布尔 | false |
| `isIdle` | 1.6% (5/321) | 布尔 | true |
| `joyDuration` | 7.2% (23/321) | 数值 | 2000 / 3000 / 4000 |
| `joyKind` | 6.9% (22/321) | 文本 | Gaming_Cerebral / Gaming_Dexterity / Meditative |
| `joyMaxParticipants` | 2.8% (9/321) | 数值 | 2 / 3 / 4 |
| `joySkill` | 2.5% (8/321) | 文本 | Artistic / Intellectual / Shooting |
| `joyXpPerTick` | 2.5% (8/321) | 数值 | 0.0015 / 0.002 / 0.003 |
| `makeTargetPrisoner` | 1.6% (5/321) | 布尔 | true |
| `neverFleeFromEnemies` | 0.3% (1/321) | 布尔 | true |
| `neverShowWeapon` | 7.5% (24/321) | 布尔 | true |
| `overrideFlyChance` | 3.1% (10/321) | 数值 | 1 |
| `playerInterruptible` | 1.9% (6/321) | 布尔 | false |
| `reportString` | 94.4% (303/321) | 文本 | escaping / hibernating / stalking TargetA. |
| `sleepCanInterrupt` | 0.6% (2/321) | 布尔 | false |
| `suspendable` | 7.8% (25/321) | 布尔 | false |
| `taleOnCompletion` | 4.7% (15/321) | 文本 | BuiltSnowman / Meditated / Prayed |
| `tryStartFlying` | 3.7% (12/321) | 布尔 | true |
| `waitAfterArriving` | 0.3% (1/321) | 数值 | 2000 |

## 四、原版 defName 一览（共 321 个，列出前 60）

```text
``                                `RemoveMechlink`                  `CastAbilityOnThingWithoutWeaponInterruptible`  `PlayStatic`                    
`PlayWalking`                     `PlayToys`                        `RevenantWander`                  `RevenantEscape`                
`RevenantSleep`                   `TransferBetweenEntityHolders`    `InvestigateMonolith`             `ActivateMonolith`              
`ChimeraSwitchToAttackMode`       `FillIn`                          `CarryToMomAfterBirth`            `Skydreaming`                   
`NatureRunning`                   `MechCharge`                      `HaulMechToCharger`               `RepairMech`                    
`ControlMech`                     `DisassembleMech`                 `PrisonerBloodfeed`               `Deathrest`                     
`CastAbilityOnThingWithoutWeapon`  `ReleaseMechs`                    `TryRomance`                      `HaulToAtomizer`                
`IdleWhileDespawned`              `Wait_SafeTemperature`            `TradeWithPawn`                   `DismissTrader`                 
`InstallImplant`                  `Insult`                          `HaulCorpseToPublicPlace`         `InducePrisonerToEscape`        
`OfferHelp`                       `EmptyThingContainer`             `InteractThing`                   `FillIn`                        
`Dance`                           `GotoAndBeSociallyActive`         `EatAtCannibalPlatter`            `InduceSlaveToRebel`            
`GiveToPawn`                      `OpenStylingStationDialog`        `UseStylingStation`               `UseStylingStationAutomatic`    
`ExtractRelic`                    `InstallRelic`                    `GetNeuralSupercharge`            `DyeHair`                       
`CreateAndEnterCocoon`            `CreateAndEnterHealingPod`        `ReturnToGauranlenTree`           `MergeIntoGaumakerPod`          
`ChangeTreeMode`                  `SelfDetonate`                    `InspectGravEngine`               `PilotConsole`                  
```

_余下 261 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
