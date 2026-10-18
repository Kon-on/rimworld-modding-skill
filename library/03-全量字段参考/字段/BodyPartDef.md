# BodyPartDef

- **所属线**：人物线
- **原版实例数**：147
- **字段路径数**：29
- **资料片**：Anomaly、Biotech、Core、Odyssey
- **原版出处**：`Anomaly/Defs/Bodies/Bodies_Entities.xml`、`Core/Defs/Bodies/BodyParts_Animal.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<BodyPartDef ParentName="MetalHorrorBase">
    <defName>MetalhorrorHead</defName>
    <label>head</label>
    <hitPoints>30</hitPoints>
  </BodyPartDef>

  
```

> 来自 `Anomaly/Defs/Bodies/Bodies_Entities.xml`，defName = `MetalhorrorHead`，XML 节点数 4（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：NociosphereCore / NociosphereShell / NoctolClaw
hitPoints                                      [数值]  例：10 / 1250 / 2500
label                                          [文本]  例：claw / core / shell
tags/li                                        [文本]  例：BloodPumpingSource / ConsciousnessSource / ManipulationLimbCore
```

## 三、全量字段表（29 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `alive` | 34.7% (51/147) | 布尔 | false |
| `beautyRelated` | 4.1% (6/147) | 布尔 | true |
| `bleedRate` | 49.0% (72/147) | 数值 | 0 / 0.3 / 2 |
| `canBeVacuumBurnt` | 2.7% (4/147) | 布尔 | false |
| `canScarify` | 5.4% (8/147) | 布尔 | true |
| `canSuggestAmputation` | 6.1% (9/147) | 布尔 | false |
| `conceptual` | 0.7% (1/147) | 布尔 | true |
| `defName` | 95.9% (141/147) | 文本 | NociosphereCore / NociosphereShell / NoctolClaw |
| `delicate` | 2.0% (3/147) | 布尔 | true |
| `destroyableByDamage` | 3.4% (5/147) | 布尔 | false |
| `executionPartPriority` | 7.5% (11/147) | 数值 | 1000 / 400 / 500 |
| `forceAlwaysRemovable` | 0.7% (1/147) | 布尔 | true |
| `frostbiteVulnerability` | 28.6% (42/147) | 数值 | 0.1 / 10 / 5 |
| `hitChanceFactors` | 0.7% (1/147) | 容器 |  |
| `hitChanceFactors/li` | 0.7% (1/147) | 容器 |  |
| `hitChanceFactors/li/key` | 0.7% (1/147) | 文本 | Blunt |
| `hitChanceFactors/li/value` | 0.7% (1/147) | 数值 | 0 |
| `hitPoints` | 93.2% (137/147) | 数值 | 10 / 1250 / 2500 |
| `label` | 95.2% (140/147) | 文本 | claw / core / shell |
| `labelShort` | 4.1% (6/147) | 文本 | body ring / claw |
| `pawnGeneratorCanAmputate` | 4.8% (7/147) | 布尔 | true |
| `permanentInjuryChanceFactor` | 52.4% (77/147) | 数值 | 0 / 15 / 6 |
| `removeRecipeLabelOverride` | 0.7% (1/147) | 文本 | remove |
| `skinCovered` | 71.4% (105/147) | 布尔 | false / true |
| `socketed` | 1.4% (2/147) | 布尔 | true |
| `solid` | 43.5% (64/147) | 布尔 | false / true |
| `spawnThingOnRemoved` | 2.7% (4/147) | 文本 | Heart / Kidney / Liver |
| `tags` | 60.5% (89/147) | 容器 |  |
| `tags/li` | 95.9% (141/147) | 文本 | BloodPumpingSource / ConsciousnessSource / ManipulationLimbCore |

## 四、原版 defName 一览（共 147 个，列出前 60）

```text
`MetalhorrorHead`                 `MechanicalWarqueenBodyFirstRing`  `MechanicalWarqueenBodySecondRing`  `MechanicalWarqueenBodyThirdRing`
`MechanicalWarqueenBodyFourthRing`  `MechanicalWarqueenBodyFifthRing`  `MechanicalDiabolusBodyFirstRing`  `MechanicalDiabolusBodySecondRing`
`MechanicalDiabolusBodyThirdRing`  `MechanicalDiabolusBodyFourthRing`  `MechanicalDiabolusBodyFifthRing`  `MechanicalDiabolusBodySixthRing`
`MechanicalTermiteBodyFirstRing`  `MechanicalTermiteBodySecondRing`  `MechanicalTermiteBodyThirdRing`  `Waist`                         
`MechanicalThoraxCanManipulate`   `MechanicalCentipedeBodyFirstRing`  `MechanicalCentipedeBodySecondRing`  `MechanicalCentipedeBodyThirdRing`
`MechanicalCentipedeBodyFourthRing`  `MechanicalCentipedeBodyFifthRing`  `MechanicalCentipedeBodySixthRing`  `MetalhorrorBlade`              
`Jowl`                            ``                                `MetalhorrorTorso`                `MetalhorrorEye`                
`MetalhorrorShoulder`             `MetalhorrorArm`                  `MetalhorrorLeg`                  `MetalhorrorFoot`               
`SpineLauncher_Gorehulk`          `Body`                            `InsectNostril`                   `Tail`                          
`Hump`                            `RearClaw`                        `MetalhorrorBrain`                `FleshbeastHead`                
`FleshbeastLeg`                   `InsectHead`                      `SnakeHead`                       `FrontClaw`                     
`Stomach`                         `Gills`                           `NoctolClaw`                      `MetalhorrorCore`               
`FleshClub_Gorehulk`              `Fin`                             `MovingBodyFleshbeast`            `Tentacle`                      
`FleshbeastSpike`                 `SnakeBody`                       `Trunk`                           `Paw`                           
`Leg`                             `Torso`                           `Shoulder`                        `Lung`                          
```

_余下 87 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
