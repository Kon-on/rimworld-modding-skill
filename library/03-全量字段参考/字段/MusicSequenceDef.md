# MusicSequenceDef

- **所属线**：表现线
- **原版实例数**：8
- **字段路径数**：16
- **资料片**：Anomaly、Odyssey
- **原版出处**：`Anomaly/Defs/Misc/Music/Music_Sequences.xml`、`Odyssey/Defs/Misc/Music/Music_Sequences.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<MusicSequenceDef>
    <defName>MetalHell</defName>
    <canBeInterrupted>false</canBeInterrupted>
    <loop>true</loop>
    <fadeoutLastSongDuration>2</fadeoutLastSongDuration>
    <song>MetalHell_Ambience</song>
    <overrideVolume>0.6</overrideVolume>
  </MusicSequenceDef>

  
```

> 来自 `Anomaly/Defs/Misc/Music/Music_Sequences.xml`，defName = `MetalHell`，XML 节点数 7（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：HorrorCombat / HorrorMonolithAdvanced / HorrorRelax
songs/li                                       [文本]  例：A_Twisted_Path / Abandoned_By_The_Light / Blood_Rain_Falling
```

## 三、全量字段表（16 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `canBeInterrupted` | 62.5% (5/8) | 布尔 | false |
| `defName` | 100.0% (8/8) | 文本 | HorrorCombat / HorrorMonolithAdvanced / HorrorRelax |
| `endOnNoDanger` | 25.0% (2/8) | 布尔 | true |
| `fadeInDuration` | 12.5% (1/8) | 数值 | 4 |
| `fadeoutLastSongDuration` | 75.0% (6/8) | 数值 | 2 / 4 / 5 |
| `loop` | 87.5% (7/8) | 布尔 | true |
| `loopDelayRange` | 62.5% (5/8) | 文本 | 1~2 / 5~10 |
| `loopFadeout` | 12.5% (1/8) | 布尔 | true |
| `minTimeToPlay` | 62.5% (5/8) | 数值 | 30 |
| `overrideFadeout` | 12.5% (1/8) | 数值 | 4 |
| `overrideVolume` | 12.5% (1/8) | 数值 | 0.6 |
| `pausedVolumeFactor` | 37.5% (3/8) | 数值 | 0.5 |
| `song` | 25.0% (2/8) | 文本 | Corpse_Attack / MetalHell_Ambience |
| `songs` | 75.0% (6/8) | 容器 |  |
| `songs/li` | 225.0% (18/8) | 文本 | A_Twisted_Path / Abandoned_By_The_Light / Blood_Rain_Falling |
| `useTransitionForLifetime` | 12.5% (1/8) | 布尔 | false |

## 四、原版 defName 一览（共 8 个，列出前 60）

```text
`MetalHell`                       `HorrorTension`                   `HorrorMonolithAdvanced`          `HorrorRelax`                   
`OrbitalRelax`                    `CorpseAttack`                    `OrbitalCombat`                   `HorrorCombat`                  
```
