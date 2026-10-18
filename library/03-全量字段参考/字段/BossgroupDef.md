# BossgroupDef

- **所属线**：世界线
- **原版实例数**：4
- **字段路径数**：27
- **资料片**：Biotech
- **原版出处**：`Biotech/Defs/BossgroupDefs/Bossgroups.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<BossgroupDef Abstract="True" Name="BaseBossgroup">
    <quest>Bossgroup</quest>
    <repeatWaveStartIndex>2</repeatWaveStartIndex>
  </BossgroupDef>

  
```

> 来自 `Biotech/Defs/BossgroupDefs/Bossgroups.xml`，defName = ``，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
waves/li                                       [容器]
waves/li/bossApparel                           [容器]
waves/li/bossApparel/li                        [容器]
waves/li/bossApparel/li/thing                  [文本]  例：Apparel_HeavyShield
waves/li/bossCount                             [数值]  例：1 / 2 / 3
waves/li/escorts                               [容器]
waves/li/escorts/Mech_CentipedeBlaster         [数值]  例：2 / 4 / 8
waves/li/escorts/Mech_CentipedeBurner          [数值]  例：2 / 3 / 4
waves/li/escorts/Mech_CentipedeGunner          [数值]  例：3 / 4 / 5
waves/li/escorts/Mech_Centurion                [数值]  例：1
waves/li/escorts/Mech_Diabolus                 [数值]  例：1 / 2 / 3
waves/li/escorts/Mech_Lancer                   [数值]  例：10 / 4 / 5
waves/li/escorts/Mech_Militor                  [数值]  例：10 / 15 / 4
waves/li/escorts/Mech_Pikeman                  [数值]  例：2 / 5 / 8
waves/li/escorts/Mech_Scyther                  [数值]  例：14 / 2 / 5
waves/li/escorts/Mech_Tesseron                 [数值]  例：1 / 10 / 2
waves/li/escorts/Mech_Tunneler                 [数值]  例：1 / 2 / 3
```

## 三、全量字段表（27 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `boss` | 75.0% (3/4) | 文本 | Apocriton / Diabolus / Warqueen |
| `defName` | 75.0% (3/4) | 文本 | Apocriton / Diabolus / Warqueen |
| `leaderDescription` | 75.0% (3/4) | 文本 | The {LEADERKIND_label} has a built-in mech gestator and is capable of deploying  / The {LEADERKIND_label} is a |
| `quest` | 25.0% (1/4) | 文本 | Bossgroup |
| `repeatWaveStartIndex` | 25.0% (1/4) | 数值 | 2 |
| `rewardDef` | 75.0% (3/4) | 文本 | NanostructuringChip / PowerfocusChip / SignalChip |
| `waves` | 75.0% (3/4) | 容器 |  |
| `waves/li` | 600.0% (24/4) | 容器 |  |
| `waves/li/bossApparel` | 525.0% (21/4) | 容器 |  |
| `waves/li/bossApparel/li` | 525.0% (21/4) | 容器 |  |
| `waves/li/bossApparel/li/thing` | 525.0% (21/4) | 文本 | Apparel_HeavyShield |
| `waves/li/bossCount` | 600.0% (24/4) | 数值 | 1 / 2 / 3 |
| `waves/li/escorts` | 600.0% (24/4) | 容器 |  |
| `waves/li/escorts/Mech_CentipedeBlaster` | 100.0% (4/4) | 数值 | 2 / 4 / 8 |
| `waves/li/escorts/Mech_CentipedeBurner` | 150.0% (6/4) | 数值 | 2 / 3 / 4 |
| `waves/li/escorts/Mech_CentipedeGunner` | 100.0% (4/4) | 数值 | 3 / 4 / 5 |
| `waves/li/escorts/Mech_Centurion` | 175.0% (7/4) | 数值 | 1 |
| `waves/li/escorts/Mech_Diabolus` | 125.0% (5/4) | 数值 | 1 / 2 / 3 |
| `waves/li/escorts/Mech_Lancer` | 125.0% (5/4) | 数值 | 10 / 4 / 5 |
| `waves/li/escorts/Mech_Legionary` | 75.0% (3/4) | 数值 | 3 |
| `waves/li/escorts/Mech_Militor` | 450.0% (18/4) | 数值 | 10 / 15 / 4 |
| `waves/li/escorts/Mech_Pikeman` | 150.0% (6/4) | 数值 | 2 / 5 / 8 |
| `waves/li/escorts/Mech_Scorcher` | 25.0% (1/4) | 数值 | 18 |
| `waves/li/escorts/Mech_Scyther` | 225.0% (9/4) | 数值 | 14 / 2 / 5 |
| `waves/li/escorts/Mech_Tesseron` | 100.0% (4/4) | 数值 | 1 / 10 / 2 |
| `waves/li/escorts/Mech_Tunneler` | 100.0% (4/4) | 数值 | 1 / 2 / 3 |
| `waves/li/escorts/Mech_Warqueen` | 50.0% (2/4) | 数值 | 1 |

## 四、原版 defName 一览（共 4 个，列出前 60）

```text
``                                `Diabolus`                        `Warqueen`                        `Apocriton`                     
```
