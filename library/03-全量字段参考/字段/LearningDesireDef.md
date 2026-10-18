# LearningDesireDef

- **所属线**：人物线
- **原版实例数**：7
- **字段路径数**：8
- **资料片**：Biotech
- **原版出处**：`Biotech/Defs/LearningDesireDefs/LearningDesires.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<LearningDesireDef>
    <defName>Skydreaming</defName>
    <label>sky dreaming</label>
    <description>Find a spot outside and watch the sky. Requires access to the outdoors.</description>
    <workerClass>LearningGiver_Skydreaming</workerClass>
    <iconPath>UI/Icons/Learning/Skydreaming</iconPath>
    <jobDef>Skydreaming</jobDef>
  </LearningDesireDef>

  
```

> 来自 `Biotech/Defs/LearningDesireDefs/LearningDesires.xml`，defName = `Skydreaming`，XML 节点数 7（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Floordrawing / NatureRunning / Radiotalking
description                                    [文本]  例：Chat with people over the radio. Requires a powered comms console. / Draw designs on the ground using chalk. A cleaner will eventually remove the dra / Explore the local outdoors. Requires access to the outdoors.
iconPath                                       [文本]  例：UI/Icons/Learning/FloorDrawing / UI/Icons/Learning/NatureRunning / UI/Icons/Learning/Radiotalking
jobDef                                         [文本]  例：Floordrawing / NatureRunning / Radiotalking
label                                          [文本]  例：floor drawing / nature running / radio talking
workerClass                                    [文本]  例：LearningGiver_Floordrawing / LearningGiver_NatureRunning / LearningGiver_Radiotalking
```

## 三、全量字段表（8 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (7/7) | 文本 | Floordrawing / NatureRunning / Radiotalking |
| `description` | 100.0% (7/7) | 文本 | Chat with people over the radio. Requires a powered comms console. / Draw designs on the ground using chalk. A |
| `iconPath` | 100.0% (7/7) | 文本 | UI/Icons/Learning/FloorDrawing / UI/Icons/Learning/NatureRunning / UI/Icons/Learning/Radiotalking |
| `jobDef` | 100.0% (7/7) | 文本 | Floordrawing / NatureRunning / Radiotalking |
| `label` | 100.0% (7/7) | 文本 | floor drawing / nature running / radio talking |
| `selectionWeight` | 14.3% (1/7) | 数值 | 2.5 |
| `workerClass` | 100.0% (7/7) | 文本 | LearningGiver_Floordrawing / LearningGiver_NatureRunning / LearningGiver_Radiotalking |
| `xpPerTick` | 28.6% (2/7) | 数值 | 0.16 / 0.25 |

## 四、原版 defName 一览（共 7 个，列出前 60）

```text
`Skydreaming`                     `Radiotalking`                    `Floordrawing`                    `NatureRunning`                 
`Reading`                         `Workwatching`                    `Lessontaking`                  
```
