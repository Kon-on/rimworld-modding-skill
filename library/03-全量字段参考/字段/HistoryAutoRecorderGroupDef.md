# HistoryAutoRecorderGroupDef

- **所属线**：系统线
- **原版实例数**：4
- **字段路径数**：9
- **资料片**：Core
- **原版出处**：`Core/Defs/Misc/HistoryAutoRecording/HistoryAutoRecorderGroups.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<HistoryAutoRecorderGroupDef>
    <defName>Population</defName>
    <label>population</label>
    <integersOnly>true</integersOnly>
    <historyAutoRecorderDefs>
      <li>FreeColonists</li>
      <li>Prisoners</li>
    </historyAutoRecorderDefs>
  </HistoryAutoRecorderGroupDef>

  
```

> 来自 `Core/Defs/Misc/HistoryAutoRecording/HistoryAutoRecorderGroups.xml`，defName = `Population`，XML 节点数 7（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：ColonistMood / Debug / Population
historyAutoRecorderDefs                        [容器]
historyAutoRecorderDefs/li                     [文本]  例：Wealth_Buildings / Wealth_Items / Wealth_Pawns
label                                          [文本]  例：colonist mood / debug / population
```

## 三、全量字段表（9 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (4/4) | 文本 | ColonistMood / Debug / Population |
| `devModeOnly` | 25.0% (1/4) | 布尔 | true |
| `fixedScale` | 25.0% (1/4) | 文本 | (0, 100) |
| `historyAutoRecorderDefs` | 100.0% (4/4) | 容器 |  |
| `historyAutoRecorderDefs/li` | 275.0% (11/4) | 文本 | Wealth_Buildings / Wealth_Items / Wealth_Pawns |
| `integersOnly` | 25.0% (1/4) | 布尔 | true |
| `label` | 100.0% (4/4) | 文本 | colonist mood / debug / population |
| `onlyPositiveValues` | 25.0% (1/4) | 布尔 | false |
| `useFixedScale` | 25.0% (1/4) | 布尔 | true |

## 四、原版 defName 一览（共 4 个，列出前 60）

```text
`Population`                      `ColonistMood`                    `Wealth`                          `Debug`                         
```
