# jobDef

- **所属线**：系统线
- **原版实例数**：6
- **字段路径数**：4
- **资料片**：Biotech、Core
- **原版出处**：`Biotech/Defs/JobDefs/Jobs_Learning.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<jobDef>
    <defName>Radiotalking</defName>
    <driverClass>JobDriver_RadioTalking</driverClass>
    <reportString>radiotalking.</reportString>
  </jobDef>

  
```

> 来自 `Biotech/Defs/JobDefs/Jobs_Learning.xml`，defName = `Radiotalking`，XML 节点数 4（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Floordrawing / Lessontaking / Radiotalking
driverClass                                    [文本]  例：JobDriver_Floordrawing / JobDriver_Lessontaking / JobDriver_RadioTalking
reportString                                   [文本]  例：floordrawing. / learning a lesson / radiotalking.
```

## 三、全量字段表（4 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `allowOpportunisticPrefix` | 16.7% (1/6) | 布尔 | true |
| `defName` | 100.0% (6/6) | 文本 | Floordrawing / Lessontaking / Radiotalking |
| `driverClass` | 100.0% (6/6) | 文本 | JobDriver_Floordrawing / JobDriver_Lessontaking / JobDriver_RadioTalking |
| `reportString` | 100.0% (6/6) | 文本 | floordrawing. / learning a lesson / radiotalking. |

## 四、原版 defName 一览（共 6 个，列出前 60）

```text
`Radiotalking`                    `Floordrawing`                    `Workwatching`                    `Lessontaking`                  
`Lessongiving`                    `TriggerObject`                 
```
