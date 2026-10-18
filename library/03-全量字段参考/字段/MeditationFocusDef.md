# MeditationFocusDef

- **所属线**：理念线
- **原版实例数**：7
- **字段路径数**：11
- **资料片**：Anomaly、Core
- **原版出处**：`Anomaly/Defs/MeditationFocusDefs/MeditationFocusDefs.xml`、`Core/Defs/MeditationFocusDefs/MeditationFocuses.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<MeditationFocusDef>
    <defName>Void</defName>
    <label>void</label>
  </MeditationFocusDef>
```

> 来自 `Anomaly/Defs/MeditationFocusDefs/MeditationFocusDefs.xml`，defName = `Void`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Artistic / Dignified / Natural
label                                          [文本]  例：artistic / dignified / natural
```

## 三、全量字段表（11 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (7/7) | 文本 | Artistic / Dignified / Natural |
| `incompatibleBackstoriesAny` | 14.3% (1/7) | 容器 |  |
| `incompatibleBackstoriesAny/li` | 14.3% (1/7) | 容器 |  |
| `incompatibleBackstoriesAny/li/categoryName` | 14.3% (1/7) | 文本 | Tribal |
| `incompatibleBackstoriesAny/li/slot` | 14.3% (1/7) | 文本 | Childhood |
| `label` | 100.0% (7/7) | 文本 | artistic / dignified / natural |
| `requiredBackstoriesAny` | 14.3% (1/7) | 容器 |  |
| `requiredBackstoriesAny/li` | 42.9% (3/7) | 容器 |  |
| `requiredBackstoriesAny/li/categoryName` | 42.9% (3/7) | 文本 | AdultTribal / ChildTribal / Tribal |
| `requiredBackstoriesAny/li/slot` | 42.9% (3/7) | 文本 | Childhood |
| `requiresRoyalTitle` | 14.3% (1/7) | 布尔 | True |

## 四、原版 defName 一览（共 7 个，列出前 60）

```text
`Void`                            `Morbid`                          `Minimal`                         `Flame`                         
`Dignified`                       `Artistic`                        `Natural`                       
```
