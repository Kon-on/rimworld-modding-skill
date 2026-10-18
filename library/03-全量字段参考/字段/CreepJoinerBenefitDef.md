# CreepJoinerBenefitDef

- **所属线**：世界线
- **原版实例数**：10
- **字段路径数**：29
- **资料片**：Anomaly
- **原版出处**：`Anomaly/Defs/CreepjoinerDefs/Benefits.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<CreepJoinerBenefitDef>
    <defName>Occultist</defName>
    <label>occultist</label>
    <letterExtra>{PAWN_pronoun} is deeply knowledgeable of all things related to the void. {PAWN_pronoun} can study unnatural phenomena faster than others and will also teach others when {PAWN_pronoun} gets the chance.</letterExtra>
    <traits>
      <Occultist/>
    </traits>
  </CreepJoinerBenefitDef>
  
  
```

> 来自 `Anomaly/Defs/CreepjoinerDefs/Benefits.xml`，defName = `Occultist`，XML 节点数 6（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Occultist / PerfectHuman / ShamblerOverlord
label                                          [文本]  例：occultist / perfect human / shambler overlord
letterExtra                                    [文本]  例：{PAWN_nameDef} is skilled in everything to an unnatural degree. Regardless of th / {PAWN_nameDef}'s body is riddled with corrupt archites. {PAWN_pronoun} can relea / {PAWN_pronoun} is deeply knowledgeable of all things related to the void. {PAWN_
```

## 三、全量字段表（29 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `abilities` | 50.0% (5/10) | 容器 |  |
| `abilities/li` | 50.0% (5/10) | 文本 | ReleaseDeadlifeDust / ShapeFlesh / TransmuteSteel |
| `defName` | 100.0% (10/10) | 文本 | Occultist / PerfectHuman / ShamblerOverlord |
| `excludes` | 10.0% (1/10) | 容器 |  |
| `excludes/li` | 10.0% (1/10) | 文本 | Disturbing |
| `hediffs` | 10.0% (1/10) | 容器 |  |
| `hediffs/li` | 10.0% (1/10) | 文本 | DeathRefusalCreepJoiner |
| `label` | 100.0% (10/10) | 文本 | occultist / perfect human / shambler overlord |
| `letterExtra` | 100.0% (10/10) | 文本 | {PAWN_nameDef} is skilled in everything to an unnatural degree. Regardless of th / {PAWN_nameDef}'s body is ri |
| `skills` | 10.0% (1/10) | 容器 |  |
| `skills/Animals` | 10.0% (1/10) | 文本 | 14~18 |
| `skills/Artistic` | 10.0% (1/10) | 文本 | 14~18 |
| `skills/Construction` | 10.0% (1/10) | 文本 | 14~18 |
| `skills/Cooking` | 10.0% (1/10) | 文本 | 14~18 |
| `skills/Crafting` | 10.0% (1/10) | 文本 | 14~18 |
| `skills/Intellectual` | 10.0% (1/10) | 文本 | 14~18 |
| `skills/Medicine` | 10.0% (1/10) | 文本 | 14~18 |
| `skills/Melee` | 10.0% (1/10) | 文本 | 14~18 |
| `skills/Mining` | 10.0% (1/10) | 文本 | 14~18 |
| `skills/Plants` | 10.0% (1/10) | 文本 | 14~18 |
| `skills/Shooting` | 10.0% (1/10) | 文本 | 14~18 |
| `skills/Social` | 10.0% (1/10) | 文本 | 14~18 |
| `traits` | 40.0% (4/10) | 容器 |  |
| `traits/BodyMastery` | 10.0% (1/10) | 容器 |  |
| `traits/Industriousness` | 10.0% (1/10) | 数值 | 2 |
| `traits/Joyous` | 10.0% (1/10) | 容器 |  |
| `traits/Occultist` | 10.0% (1/10) | 容器 |  |
| `traits/PerfectMemory` | 10.0% (1/10) | 容器 |  |
| `weight` | 10.0% (1/10) | 数值 | 0.5 |

## 四、原版 defName 一览（共 10 个，列出前 60）

```text
`Occultist`                       `ShamblerOverlord`                `Fleshcrafter`                    `Alchemist`                     
`DeathRefusal`                    `BodyMastery`                     `PsychicButcher`                  `UnnaturalHealing`              
`Joybringer`                      `PerfectHuman`                  
```
