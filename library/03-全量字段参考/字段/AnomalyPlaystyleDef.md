# AnomalyPlaystyleDef

- **所属线**：世界线
- **原版实例数**：3
- **字段路径数**：9
- **资料片**：Anomaly
- **原版出处**：`Anomaly/Defs/AnomalyPlaystyles/AnomalyPlaystyles.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<AnomalyPlaystyleDef>
    <defName>Standard</defName>
    <label>standard with monolith</label>
    <description>The standard Anomaly experience. Anomaly threats are linked to the activation of the void monolith.</description>
  </AnomalyPlaystyleDef>
  
  
```

> 来自 `Anomaly/Defs/AnomalyPlaystyles/AnomalyPlaystyles.xml`，defName = `Standard`，XML 节点数 4（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：AmbientHorror / Disabled / Standard
description                                    [文本]  例：Anomaly threats do not occur. Good if you don't want to interact with most Anoma / The monolith does not appear. Any Anomaly threat can occur, but Anomaly threats  / The standard Anomaly experience. Anomaly threats are linked to the activation of
label                                          [文本]  例：ambient horror / anomaly incidents disabled / standard with monolith
```

## 三、全量字段表（9 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `alwaysShowCodex` | 33.3% (1/3) | 布尔 | true |
| `defName` | 100.0% (3/3) | 文本 | AmbientHorror / Disabled / Standard |
| `description` | 100.0% (3/3) | 文本 | Anomaly threats do not occur. Good if you don't want to interact with most Anoma / The monolith does not appea |
| `displayStudyFactorSlider` | 33.3% (1/3) | 布尔 | false |
| `displayThreatFractionSliders` | 66.7% (2/3) | 布尔 | false |
| `enableAnomalyContent` | 33.3% (1/3) | 布尔 | false |
| `generateMonolith` | 66.7% (2/3) | 布尔 | false |
| `label` | 100.0% (3/3) | 文本 | ambient horror / anomaly incidents disabled / standard with monolith |
| `overrideThreatFraction` | 33.3% (1/3) | 布尔 | true |

## 四、原版 defName 一览（共 3 个，列出前 60）

```text
`Standard`                        `AmbientHorror`                   `Disabled`                      
```
