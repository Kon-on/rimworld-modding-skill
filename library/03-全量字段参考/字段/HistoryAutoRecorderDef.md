# HistoryAutoRecorderDef

- **所属线**：系统线
- **原版实例数**：11
- **字段路径数**：6
- **资料片**：Core
- **原版出处**：`Core/Defs/Misc/HistoryAutoRecording/HistoryAutoRecorders.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<HistoryAutoRecorderDef>
    <defName>Wealth_Total</defName>
    <label>wealth (total)</label>
    <graphColor>(1, 1, 0, 1)</graphColor>
    <recordTicksFrequency>30000</recordTicksFrequency>
    <workerClass>HistoryAutoRecorderWorker_WealthTotal</workerClass>
    <valueFormat>${0}</valueFormat>
  </HistoryAutoRecorderDef>

  
```

> 来自 `Core/Defs/Misc/HistoryAutoRecording/HistoryAutoRecorders.xml`，defName = `Wealth_Total`，XML 节点数 7（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Wealth_Buildings / Wealth_Items / Wealth_Pawns
graphColor                                     [文本]  例：(0.3, 0.6, 0.48, 1) / (0.5, 0.7, 0, 1) / (0.91, 0.68, 0, 1)
label                                          [文本]  例：wealth (buildings) / wealth (creatures) / wealth (items)
recordTicksFrequency                           [数值]  例：30000 / 60000
valueFormat                                    [文本]  例：${0} / {0} / {0} days
workerClass                                    [文本]  例：HistoryAutoRecorderWorker_WealthBuildings / HistoryAutoRecorderWorker_WealthItems / HistoryAutoRecorderWorker_WealthPawns
```

## 三、全量字段表（6 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (11/11) | 文本 | Wealth_Buildings / Wealth_Items / Wealth_Pawns |
| `graphColor` | 100.0% (11/11) | 文本 | (0.3, 0.6, 0.48, 1) / (0.5, 0.7, 0, 1) / (0.91, 0.68, 0, 1) |
| `label` | 100.0% (11/11) | 文本 | wealth (buildings) / wealth (creatures) / wealth (items) |
| `recordTicksFrequency` | 100.0% (11/11) | 数值 | 30000 / 60000 |
| `valueFormat` | 100.0% (11/11) | 文本 | ${0} / {0} / {0} days |
| `workerClass` | 100.0% (11/11) | 文本 | HistoryAutoRecorderWorker_WealthBuildings / HistoryAutoRecorderWorker_WealthItems / HistoryAutoRecorderWorker_ |

## 四、原版 defName 一览（共 11 个，列出前 60）

```text
`Wealth_Total`                    `Wealth_Items`                    `Wealth_Buildings`                `Wealth_Pawns`                  
`FreeColonists`                   `Prisoners`                       `ColonistMood`                    `Adaptation`                    
`ThreatPoints`                    `PopAdaptation`                   `PopIntent`                     
```
