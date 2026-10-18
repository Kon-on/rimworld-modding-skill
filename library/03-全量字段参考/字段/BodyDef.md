# BodyDef

- **所属线**：人物线
- **原版实例数**：48
- **字段路径数**：61
- **资料片**：Anomaly、Biotech、Core、Odyssey
- **原版出处**：`Anomaly/Defs/Bodies/Bodies_Entities.xml`、`Core/Defs/Bodies/Bodies_Animal_Bird.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<BodyDef>
    <defName>FleshmassNucleus</defName>
    <label>fleshmass nucleus</label>
    <corePart>
      <def>FleshmassNucleusCore</def>
      <height>Middle</height>
      <depth>Outside</depth>
      <groups>
        <li>Torso</li>
      </groups>
    </corePart>
  </BodyDef>

  
```

> 来自 `Anomaly/Defs/Bodies/Bodies_Entities.xml`，defName = `FleshmassNucleus`，XML 节点数 9（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
corePart                                       [容器]
corePart/def                                   [文本]  例：Body / FleshmassNucleusCore / MetalhorrorTorso
corePart/depth                                 [文本]  例：Outside
corePart/height                                [文本]  例：Middle
corePart/parts                                 [容器]
corePart/parts/li                              [容器]
corePart/parts/li/coverage                     [数值]  例：0.03 / 0.07 / 0.2
corePart/parts/li/customLabel                  [文本]  例：front left leg / front right leg / rear left leg
corePart/parts/li/def                          [文本]  例：Kidney / Leg / Liver
corePart/parts/li/depth                        [文本]  例：Inside / Outside
corePart/parts/li/groups                       [容器]
corePart/parts/li/groups/li                    [文本]  例：Legs / Neck / Shoulders
corePart/parts/li/height                       [文本]  例：Bottom / Middle / Top
corePart/parts/li/parts                        [容器]
corePart/parts/li/parts/li                     [容器]
corePart/parts/li/parts/li/coverage            [数值]  例：0.1 / 0.15 / 0.75
corePart/parts/li/parts/li/customLabel         [文本]  例：front left claw / front right claw / rear left claw
corePart/parts/li/parts/li/def                 [文本]  例：Head / MetalhorrorArm / MetalhorrorFoot
corePart/parts/li/parts/li/groups              [容器]
corePart/parts/li/parts/li/groups/li           [文本]  例：Feet / FrontLeftClaw / FrontRightClaw
corePart/parts/li/parts/li/parts               [容器]
corePart/parts/li/parts/li/parts/li            [容器]
corePart/parts/li/parts/li/parts/li/coverage   [数值]  例：0.08 / 0.10 / 0.12
corePart/parts/li/parts/li/parts/li/customLabel [文本]  例：left ear / left eye / right ear
corePart/parts/li/parts/li/parts/li/def        [文本]  例：AnimalJaw / Ear / Eye
corePart/parts/li/parts/li/parts/li/depth      [文本]  例：Inside
corePart/parts/li/parts/li/parts/li/groups     [容器]
corePart/parts/li/parts/li/parts/li/groups/li  [文本]  例：Feet / LeftBlade / RightBlade
corePart/parts/li/parts/li/parts/li/parts/li   [容器]
corePart/parts/li/parts/li/parts/li/parts/li/coverage [数值]  例：0.6 / 0.7 / 0.70
corePart/parts/li/parts/li/parts/li/parts/li/def [文本]  例：Brain / MechanicalDiabolusBodyFifthRing / MechanicalWarqueenBodyFifthRing
corePart/parts/li/parts/li/parts/li/parts/li/groups [容器]
corePart/parts/li/parts/li/parts/li/parts/li/groups/li [文本]  例：Eyes / FullHead / TuskAttackTool
defName                                        [文本]  例：FleshmassNucleus / Metalhorror / Nociosphere
label                                          [文本]  例：fleshmass nucleus / metalhorror / nociosphere
```

## 三、全量字段表（61 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `corePart` | 100.0% (48/48) | 容器 |  |
| `corePart/def` | 100.0% (48/48) | 文本 | Body / FleshmassNucleusCore / MetalhorrorTorso |
| `corePart/depth` | 100.0% (48/48) | 文本 | Outside |
| `corePart/groups` | 31.2% (15/48) | 容器 |  |
| `corePart/groups/li` | 31.2% (15/48) | 文本 | Torso |
| `corePart/height` | 100.0% (48/48) | 文本 | Middle |
| `corePart/parts` | 97.9% (47/48) | 容器 |  |
| `corePart/parts/li` | 995.8% (478/48) | 容器 |  |
| `corePart/parts/li/coverage` | 995.8% (478/48) | 数值 | 0.03 / 0.07 / 0.2 |
| `corePart/parts/li/customLabel` | 535.4% (257/48) | 文本 | front left leg / front right leg / rear left leg |
| `corePart/parts/li/def` | 995.8% (478/48) | 文本 | Kidney / Leg / Liver |
| `corePart/parts/li/depth` | 547.9% (263/48) | 文本 | Inside / Outside |
| `corePart/parts/li/flipGraphic` | 4.2% (2/48) | 布尔 | true |
| `corePart/parts/li/groups` | 227.1% (109/48) | 容器 |  |
| `corePart/parts/li/groups/li` | 235.4% (113/48) | 文本 | Legs / Neck / Shoulders |
| `corePart/parts/li/height` | 364.6% (175/48) | 文本 | Bottom / Middle / Top |
| `corePart/parts/li/parts` | 316.7% (152/48) | 容器 |  |
| `corePart/parts/li/parts/li` | 493.8% (237/48) | 容器 |  |
| `corePart/parts/li/parts/li/coverage` | 493.8% (237/48) | 数值 | 0.1 / 0.15 / 0.75 |
| `corePart/parts/li/parts/li/customLabel` | 352.1% (169/48) | 文本 | front left claw / front right claw / rear left claw |
| `corePart/parts/li/parts/li/def` | 493.8% (237/48) | 文本 | Head / MetalhorrorArm / MetalhorrorFoot |
| `corePart/parts/li/parts/li/depth` | 77.1% (37/48) | 文本 | Inside / Outside |
| `corePart/parts/li/parts/li/flipGraphic` | 6.2% (3/48) | 布尔 | true |
| `corePart/parts/li/parts/li/groups` | 233.3% (112/48) | 容器 |  |
| `corePart/parts/li/parts/li/groups/li` | 291.7% (140/48) | 文本 | Feet / FrontLeftClaw / FrontRightClaw |
| `corePart/parts/li/parts/li/height` | 8.3% (4/48) | 文本 | Top |
| `corePart/parts/li/parts/li/parts` | 122.9% (59/48) | 容器 |  |
| `corePart/parts/li/parts/li/parts/li` | 531.2% (255/48) | 容器 |  |
| `corePart/parts/li/parts/li/parts/li/coverage` | 531.2% (255/48) | 数值 | 0.08 / 0.10 / 0.12 |
| `corePart/parts/li/parts/li/parts/li/customLabel` | 347.9% (167/48) | 文本 | left ear / left eye / right ear |
| `corePart/parts/li/parts/li/parts/li/def` | 531.2% (255/48) | 文本 | AnimalJaw / Ear / Eye |
| `corePart/parts/li/parts/li/parts/li/depth` | 91.7% (44/48) | 文本 | Inside |
| `corePart/parts/li/parts/li/parts/li/flipGraphic` | 6.2% (3/48) | 布尔 | true |
| `corePart/parts/li/parts/li/parts/li/groups` | 160.4% (77/48) | 容器 |  |
| `corePart/parts/li/parts/li/parts/li/groups/li` | 218.8% (105/48) | 文本 | Feet / LeftBlade / RightBlade |
| `corePart/parts/li/parts/li/parts/li/height` | 20.8% (10/48) | 文本 | Bottom |
| `corePart/parts/li/parts/li/parts/li/parts` | 70.8% (34/48) | 容器 |  |
| `corePart/parts/li/parts/li/parts/li/parts/li` | 135.4% (65/48) | 容器 |  |
| `corePart/parts/li/parts/li/parts/li/parts/li/coverage` | 135.4% (65/48) | 数值 | 0.6 / 0.7 / 0.70 |
| `corePart/parts/li/parts/li/parts/li/parts/li/customLabel` | 83.3% (40/48) | 文本 | left tusk / right index finger / right thumb |
| `corePart/parts/li/parts/li/parts/li/parts/li/def` | 135.4% (65/48) | 文本 | Brain / MechanicalDiabolusBodyFifthRing / MechanicalWarqueenBodyFifthRing |
| `corePart/parts/li/parts/li/parts/li/parts/li/depth` | 31.2% (15/48) | 文本 | Inside |
| `corePart/parts/li/parts/li/parts/li/parts/li/groups` | 97.9% (47/48) | 容器 |  |
| `corePart/parts/li/parts/li/parts/li/parts/li/groups/li` | 156.2% (75/48) | 文本 | Eyes / FullHead / TuskAttackTool |
| `corePart/parts/li/parts/li/parts/li/parts/li/parts` | 6.2% (3/48) | 容器 |  |
| `corePart/parts/li/parts/li/parts/li/parts/li/parts/li` | 8.3% (4/48) | 容器 |  |
| `corePart/parts/li/parts/li/parts/li/parts/li/parts/li/coverage` | 8.3% (4/48) | 数值 | 0.05 / 0.5 |
| `corePart/parts/li/parts/li/parts/li/parts/li/parts/li/def` | 8.3% (4/48) | 文本 | FluidReprocessor / MechanicalCentipedeBodySixthRing / MechanicalDiabolusBodySixthRing |
| `corePart/parts/li/parts/li/parts/li/parts/li/parts/li/depth` | 4.2% (2/48) | 文本 | Inside |
| `corePart/parts/li/parts/li/parts/li/parts/li/parts/li/height` | 2.1% (1/48) | 文本 | Middle |
| `corePart/parts/li/parts/li/parts/li/parts/li/parts/li/parts` | 2.1% (1/48) | 容器 |  |
| `corePart/parts/li/parts/li/parts/li/parts/li/parts/li/parts/li` | 2.1% (1/48) | 容器 |  |
| `corePart/parts/li/parts/li/parts/li/parts/li/parts/li/parts/li/coverage` | 2.1% (1/48) | 数值 | 0.05 |
| `corePart/parts/li/parts/li/parts/li/parts/li/parts/li/parts/li/def` | 2.1% (1/48) | 文本 | FluidReprocessor |
| `corePart/parts/li/parts/li/parts/li/parts/li/parts/li/parts/li/depth` | 2.1% (1/48) | 文本 | Inside |
| `corePart/parts/li/parts/li/parts/li/visibleHediffRots` | 4.2% (2/48) | 容器 |  |
| `corePart/parts/li/parts/li/parts/li/visibleHediffRots/li` | 8.3% (4/48) | 文本 | East / South / West |
| `corePart/parts/li/parts/li/parts/li/woundAnchorTag` | 8.3% (4/48) | 文本 | LeftEye / RightEye |
| `corePart/parts/li/woundAnchorTag` | 16.7% (8/48) | 文本 | LeftLeg / LeftShoulder / RightLeg |
| `defName` | 100.0% (48/48) | 文本 | FleshmassNucleus / Metalhorror / Nociosphere |
| `label` | 100.0% (48/48) | 文本 | fleshmass nucleus / metalhorror / nociosphere |

## 四、原版 defName 一览（共 48 个，列出前 60）

```text
`FleshmassNucleus`                `Nociosphere`                     `Drone`                           `DroneWithThreeLegs`            
`DroneWithTreads`                 `MechanicalTermite`               `Snail`                           `Mech_Light`                    
`MechanicalCentipede`             `Snake`                           `Mech_Warqueen`                   `Mech_Agrihand`                 
`Mech_Diabolus`                   `Larva`                           `BeetleLike`                      `Devourer`                      
`TurtleLike`                      `Scorcher`                        `Apocriton`                       `BeetleLikeWithClaw`            
`Pikeman`                         `Crab`                            `Cyclops`                         `Metalhorror`                   
`Bird`                            `Mech_Centurion`                  `Mech_Tunneler`                   `Bulbfreak`                     
`Dreadmeld`                       `Pinniped`                        `Noctol`                          `QuadrupedAnimalWithPaws`       
`QuadrupedAnimalWithHooves`       `QuadrupedAnimalWithPawsAndTail`  `QuadrupedAnimalWithHoovesAndHump`  `PinnipedWithTusks`             
`QuadrupedAnimalWithHoovesAndHorn`  `QuadrupedAnimalWithHoovesAndTusks`  `QuadrupedAnimalWithHoovesTusksAndTrunk`  `Fingerspike`                   
`Toughspike`                      `Lancer`                          `Trispike`                        `Scyther`                       
`QuadrupedAnimalWithClawsTailAndJowl`  `Monkey`                          `Gorehulk`                        `Human`                         
```
