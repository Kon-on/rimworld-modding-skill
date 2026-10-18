# SongDef

- **所属线**：表现线
- **原版实例数**：76
- **字段路径数**：10
- **资料片**：Anomaly、Core、Ideology、Odyssey、Royalty
- **原版出处**：`Core/Defs/Misc/SongDefs/Songs_Gameplay.xml`、`Royalty/Defs/SongDefs/Songs_Gameplay.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<SongDef>
    <clipPath>Songs/Relax/Noodles_Mirage/Noodle_Mirage_b</clipPath>
  </SongDef>

  
```

> 来自 `Core/Defs/Misc/SongDefs/Songs_Gameplay.xml`，defName = ``，XML 节点数 2（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
clipPath                                       [文本]  例：Songs/Horror_Relax/A_Twisted_Path / Songs/Horror_Relax/Abandoned_By_The_Light / Songs/Horror_Relax/Blood_Rain_Falling
```

## 三、全量字段表（10 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `allowedSeasons` | 1.3% (1/76) | 容器 |  |
| `allowedSeasons/li` | 1.3% (1/76) | 文本 | Winter |
| `allowedTimeOfDay` | 15.8% (12/76) | 文本 | Day / Night |
| `clipPath` | 100.0% (76/76) | 文本 | Songs/Horror_Relax/A_Twisted_Path / Songs/Horror_Relax/Abandoned_By_The_Light / Songs/Horror_Relax/Blood_Rain_ |
| `commonality` | 25.0% (19/76) | 数值 | 0 / 2.0 |
| `defName` | 30.3% (23/76) | 文本 | A_Twisted_Path / Abandoned_By_The_Light / Blood_Rain_Falling |
| `minRoyalTitle` | 1.3% (1/76) | 文本 | Baron |
| `playOnMap` | 6.6% (5/76) | 布尔 | false |
| `tense` | 7.9% (6/76) | 布尔 | true |
| `volume` | 75.0% (57/76) | 数值 | 0.65 / 0.9 / 1.00 |

## 四、原版 defName 一览（共 76 个，列出前 60）

```text
``                                ``                                ``                                ``                              
``                                ``                                ``                                ``                              
``                                ``                                ``                                ``                              
``                                ``                                ``                                ``                              
``                                ``                                ``                                ``                              
``                                ``                                ``                                ``                              
``                                ``                                ``                                ``                              
``                                ``                                ``                                ``                              
``                                ``                                ``                                ``                              
``                                ``                                ``                                ``                              
``                                ``                                ``                                ``                              
``                                ``                                ``                                ``                              
``                                ``                                ``                                `OdysseyCreditsSong`            
``                                `Abandoned_By_The_Light`          `Blood_Rain_Falling`              `Shamblers_Blues`               
`A_Twisted_Path`                  `Have_They_Come_For_Us`           `Is_It_Truly_Alive`               `They_See_You`                  
```

_余下 16 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
