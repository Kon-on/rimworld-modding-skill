# LandingOutcomeDef

- **所属线**：世界线
- **原版实例数**：4
- **字段路径数**：6
- **资料片**：Odyssey
- **原版出处**：`Odyssey/Defs/Misc/LandingOutcomes.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<LandingOutcomeDef>
    <defName>MinorGravshipCrash</defName>
    <letterLabel>minor gravship crash</letterLabel>
    <letterText>While landing {GRAVSHIP}, {PILOT_nameDef} accidentally disengaged the grav engine too early, causing the gravship to free-fall for several feet. Some buildings on the gravship have sustained light damage from the crash.</letterText>
    <letterDef>NegativeEvent</letterDef>
    <workerClass>LandingOutcomeWorker_MinorGravshipCrash</workerClass>
    <weight>1</weight>
  </LandingOutcomeDef>

  
```

> 来自 `Odyssey/Defs/Misc/LandingOutcomes.xml`，defName = `MinorGravshipCrash`，XML 节点数 7（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：GravNausea / MinorGravshipCrash / OverheatedGravEngine
letterDef                                      [文本]  例：NegativeEvent
letterLabel                                    [文本]  例：grav nausea / minor gravship crash / overheated grav engine
letterText                                     [文本]  例：While landing {GRAVSHIP}, {PILOT_nameDef} accidentally disengaged the grav engin / While landing {GRAVSHIP}, {PILOT_nameDef} over-engaged the grav engine, causing  / While landing {GRAVSHIP}, {PILOT_nameDef} overheated the ship's thrusters, fryin
weight                                         [数值]  例：1
workerClass                                    [文本]  例：LandingOutcomeWorker_GravNausea / LandingOutcomeWorker_MinorGravshipCrash / LandingOutcomeWorker_OverheatedGravEngine
```

## 三、全量字段表（6 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (4/4) | 文本 | GravNausea / MinorGravshipCrash / OverheatedGravEngine |
| `letterDef` | 100.0% (4/4) | 文本 | NegativeEvent |
| `letterLabel` | 100.0% (4/4) | 文本 | grav nausea / minor gravship crash / overheated grav engine |
| `letterText` | 100.0% (4/4) | 文本 | While landing {GRAVSHIP}, {PILOT_nameDef} accidentally disengaged the grav engin / While landing {GRAVSHIP}, { |
| `weight` | 100.0% (4/4) | 数值 | 1 |
| `workerClass` | 100.0% (4/4) | 文本 | LandingOutcomeWorker_GravNausea / LandingOutcomeWorker_MinorGravshipCrash / LandingOutcomeWorker_OverheatedGra |

## 四、原版 defName 一览（共 4 个，列出前 60）

```text
`MinorGravshipCrash`              `ThrusterBreakdown`               `OverheatedGravEngine`            `GravNausea`                    
```
