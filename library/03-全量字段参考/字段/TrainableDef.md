# TrainableDef

- **所属线**：人物线
- **原版实例数**：14
- **字段路径数**：16
- **资料片**：Core、Odyssey
- **原版出处**：`Odyssey/Defs/Misc/Trainables.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<TrainableDef>
    <defName>Comfort</defName>
    <label>comfort</label>
    <description>The animal will be more emotionally supportive. It will nuzzle more often, and make your colonists happier when it does so.</description>
    <listPriority>0</listPriority>
    <difficulty>200</difficulty>
    <steps>2</steps>
    <specialTrainable>true</specialTrainable>
  </TrainableDef>

  
```

> 来自 `Odyssey/Defs/Misc/Trainables.xml`，defName = `Comfort`，XML 节点数 8（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Haul / Obedience / Release
description                                    [文本]  例：The animal can be assigned a master whom it will follow and defend. / The animal can be released to attack distant targets instead of just guarding it / The animal will randomly haul items from time to time (though it can't be direct
difficulty                                     [数值]  例：100 / 200 / 300
label                                          [文本]  例：attack / guard / haul
listPriority                                   [数值]  例：1000 / 400 / 600
steps                                          [数值]  例：2 / 3 / 5
```

## 三、全量字段表（16 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defaultTrainable` | 35.7% (5/14) | 布尔 | true |
| `defName` | 100.0% (14/14) | 文本 | Haul / Obedience / Release |
| `description` | 100.0% (14/14) | 文本 | The animal can be assigned a master whom it will follow and defend. / The animal can be released to attack dis |
| `difficulty` | 100.0% (14/14) | 数值 | 100 / 200 / 300 |
| `enablesAbility` | 35.7% (5/14) | 文本 | EggSpew / SludgeSpew / TerrorRoar |
| `icon` | 35.7% (5/14) | 文本 | UI/Icons/Trainables/Haul / UI/Icons/Trainables/Obedience / UI/Icons/Trainables/Release |
| `label` | 100.0% (14/14) | 文本 | attack / guard / haul |
| `listPriority` | 100.0% (14/14) | 数值 | 1000 / 400 / 600 |
| `minBodySize` | 14.3% (2/14) | 数值 | 0.40 / 0.65 |
| `prerequisites` | 35.7% (5/14) | 容器 |  |
| `prerequisites/li` | 35.7% (5/14) | 文本 | Obedience / Release / Tameness |
| `requiredTrainability` | 35.7% (5/14) | 文本 | Advanced / Intermediate / None |
| `specialTrainable` | 64.3% (9/14) | 布尔 | true |
| `steps` | 100.0% (14/14) | 数值 | 2 / 3 / 5 |
| `tags` | 28.6% (4/14) | 容器 |  |
| `tags/li` | 35.7% (5/14) | 文本 | Basic / Combat / Help |

## 四、原版 defName 一览（共 14 个，列出前 60）

```text
`Comfort`                         `Forage`                          `Dig`                             `EggSpew`                       
`SludgeSpew`                      `TerrorRoar`                      `WarTrumpet`                      `ThrumboRoar`                   
`Tameness`                        `AttackTarget`                    `Obedience`                       `Release`                       
`Haul`                            `Rescue`                        
```
