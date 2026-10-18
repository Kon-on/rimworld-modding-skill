# ResearchTabDef

- **所属线**：系统线
- **原版实例数**：2
- **字段路径数**：7
- **资料片**：Anomaly、Core
- **原版出处**：`Core/Defs/ResearchProjectDefs/ResearchTabs.xml`、`Anomaly/Defs/ResearchTabDefs/ResearchTabs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<ResearchTabDef>
    <defName>Main</defName>
    <label>Main</label>
    <generalTitle>Main research projects</generalTitle>
    <generalDescription>Unlock new technologies by researching at a research bench. You can only have one active project at a time.</generalDescription>
  </ResearchTabDef>
```

> 来自 `Core/Defs/ResearchProjectDefs/ResearchTabs.xml`，defName = `Main`，XML 节点数 5（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Anomaly / Main
generalDescription                             [文本]  例：Unlock new technologies by researching at a research bench. You can only have on / Unlock void-related technologies by studying unnatural entities.\n\nYou can have
generalTitle                                   [文本]  例：Anomaly research projects / Main research projects
label                                          [文本]  例：Main / anomaly
```

## 三、全量字段表（7 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (2/2) | 文本 | Anomaly / Main |
| `generalDescription` | 100.0% (2/2) | 文本 | Unlock new technologies by researching at a research bench. You can only have on / Unlock void-related technol |
| `generalTitle` | 100.0% (2/2) | 文本 | Anomaly research projects / Main research projects |
| `label` | 100.0% (2/2) | 文本 | Main / anomaly |
| `minMonolithLevelVisible` | 50.0% (1/2) | 数值 | 1 |
| `tutorTag` | 50.0% (1/2) | 文本 | Research-Tab-Anomaly |
| `visibleByDefault` | 50.0% (1/2) | 布尔 | false |

## 四、原版 defName 一览（共 2 个，列出前 60）

```text
`Main`                            `Anomaly`                       
```
