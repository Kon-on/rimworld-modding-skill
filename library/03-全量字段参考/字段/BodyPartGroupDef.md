# BodyPartGroupDef

- **所属线**：人物线
- **原版实例数**：48
- **字段路径数**：4
- **资料片**：Anomaly、Biotech、Core、Odyssey
- **原版出处**：`Biotech/Defs/Bodies/BodyPartGroups.xml`、`Core/Defs/Bodies/BodyPartGroups.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<BodyPartGroupDef>
    <defName>BulbTurret</defName>
    <label>bulb turret</label>
  </BodyPartGroupDef>
```

> 来自 `Biotech/Defs/Bodies/BodyPartGroups.xml`，defName = `BulbTurret`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：FrontLeftClaw / FrontRightClaw / LeftSpike
label                                          [文本]  例：front left claw / front right claw / left spike
```

## 三、全量字段表（4 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (48/48) | 文本 | FrontLeftClaw / FrontRightClaw / LeftSpike |
| `label` | 100.0% (48/48) | 文本 | front left claw / front right claw / left spike |
| `labelShort` | 47.9% (23/48) | 文本 | claw / fin / flesh club |
| `listOrder` | 52.1% (25/48) | 数值 | 77 / 78 / 79 |

## 四、原版 defName 一览（共 48 个，列出前 60）

```text
`BulbTurret`                      `HeadAttackTool`                  `TuskAttackTool`                  `HornAttackTool`                
`HeadClaw`                        `TurtleBeakAttackTool`            `Beak`                            `FrontLeftClaw`                 
`FrontRightClaw`                  `FirstTentacle`                   `SecondTentacle`                  `ThirdTentacle`                 
`FourthTentacle`                  `FifthTentacle`                   `RightFleshClub`                  `LeftFleshClub`                 
`LeftFin`                         `RightFin`                        `LeftPowerClaw`                   `RightPowerClaw`                
`Torso`                           `UpperHead`                       `FullHead`                        `Eyes`                          
`Teeth`                           `Mouth`                           `Neck`                            `Arms`                          
`Shoulders`                       `Hands`                           `Waist`                           `Legs`                          
`Feet`                            `FrontLeftPaw`                    `FrontRightPaw`                   `FrontLeftLeg`                  
`FrontRightLeg`                   `FrontLeftClaws`                  `FrontRightClaws`                 `LeftBlade`                     
`RightBlade`                      `LeftSpike`                       `RightSpike`                      `MiddleSpike`                   
`LeftHand`                        `RightHand`                       `MiddleFingers`                   `SpikedShellAttackTool`         
```
