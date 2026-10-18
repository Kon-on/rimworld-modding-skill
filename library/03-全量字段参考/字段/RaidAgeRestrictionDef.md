# RaidAgeRestrictionDef

- **所属线**：世界线
- **原版实例数**：1
- **字段路径数**：8
- **资料片**：Biotech
- **原版出处**：`Biotech/Defs/Storyteller/RaidAgeRestrictions.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<RaidAgeRestrictionDef>
    <defName>Children</defName>
    <developmentStage>Child</developmentStage>
    <threatPointsFactor>1.2</threatPointsFactor>
    <earliestDay>15</earliestDay>
    <ageRange>9~12</ageRange>
    <chance>0.025</chance>
    <arrivalTextExtra>All the {PAWNSPLURAL} appear to be children!</arrivalTextExtra>
    <workerClass>RaidAgeRestrictionWorker_Children</workerClass>
  </RaidAgeRestrictionDef>
```

> 来自 `Biotech/Defs/Storyteller/RaidAgeRestrictions.xml`，defName = `Children`，XML 节点数 9（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
ageRange                                       [文本]  例：9~12
arrivalTextExtra                               [文本]  例：All the {PAWNSPLURAL} appear to be children!
chance                                         [数值]  例：0.025
defName                                        [文本]  例：Children
developmentStage                               [文本]  例：Child
earliestDay                                    [数值]  例：15
threatPointsFactor                             [数值]  例：1.2
workerClass                                    [文本]  例：RaidAgeRestrictionWorker_Children
```

## 三、全量字段表（8 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `ageRange` | 100.0% (1/1) | 文本 | 9~12 |
| `arrivalTextExtra` | 100.0% (1/1) | 文本 | All the {PAWNSPLURAL} appear to be children! |
| `chance` | 100.0% (1/1) | 数值 | 0.025 |
| `defName` | 100.0% (1/1) | 文本 | Children |
| `developmentStage` | 100.0% (1/1) | 文本 | Child |
| `earliestDay` | 100.0% (1/1) | 数值 | 15 |
| `threatPointsFactor` | 100.0% (1/1) | 数值 | 1.2 |
| `workerClass` | 100.0% (1/1) | 文本 | RaidAgeRestrictionWorker_Children |

## 四、原版 defName 一览（共 1 个，列出前 60）

```text
`Children`                      
```
