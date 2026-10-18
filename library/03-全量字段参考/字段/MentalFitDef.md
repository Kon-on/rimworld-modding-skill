# MentalFitDef

- **所属线**：人物线
- **原版实例数**：2
- **字段路径数**：7
- **资料片**：Biotech
- **原版出处**：`Biotech/Defs/MentalStateDefs/MentalStates_BabyFits.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<MentalFitDef>
    <defName>Crying</defName>
    <label>crying</label>
    <mentalState>Crying</mentalState>
    <developmentalStageFilter>Baby</developmentalStageFilter>
    <mtbDaysMoodCurve>
      <points>
        <li>(0, .083)</li>
        <li>(0.25, .166)</li>
        <li>(0.50, 1)</li>
        <li>(0.75, 4)</li>
        <li>(1.00, 8)</li>
      </points>
    </mtbDaysMoodCurve>
  </MentalFitDef>

  
```

> 来自 `Biotech/Defs/MentalStateDefs/MentalStates_BabyFits.xml`，defName = `Crying`，XML 节点数 12（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Crying / Giggling
developmentalStageFilter                       [文本]  例：Baby
label                                          [文本]  例：crying / giggling
mentalState                                    [文本]  例：Crying / Giggling
mtbDaysMoodCurve                               [容器]
mtbDaysMoodCurve/points                        [容器]
mtbDaysMoodCurve/points/li                     [文本]  例：(0, .083) / (0.25, .166) / (0.50, 1)
```

## 三、全量字段表（7 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (2/2) | 文本 | Crying / Giggling |
| `developmentalStageFilter` | 100.0% (2/2) | 文本 | Baby |
| `label` | 100.0% (2/2) | 文本 | crying / giggling |
| `mentalState` | 100.0% (2/2) | 文本 | Crying / Giggling |
| `mtbDaysMoodCurve` | 100.0% (2/2) | 容器 |  |
| `mtbDaysMoodCurve/points` | 100.0% (2/2) | 容器 |  |
| `mtbDaysMoodCurve/points/li` | 500.0% (10/2) | 文本 | (0, .083) / (0.25, .166) / (0.50, 1) |

## 四、原版 defName 一览（共 2 个，列出前 60）

```text
`Crying`                          `Giggling`                      
```
