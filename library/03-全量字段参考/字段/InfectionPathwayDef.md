# InfectionPathwayDef

- **所属线**：世界线
- **原版实例数**：3
- **字段路径数**：3
- **资料片**：Anomaly、Core
- **原版出处**：`Anomaly/Defs/InfectionPathwayDefs/InfectionPathwayDefs.xml`、`Core/Defs/InfectionPathwayDefs/InfectionPathwayDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<InfectionPathwayDef>
    <defName>RevenantHypnotized</defName>
    <label>revenant hypnotized</label>
  </InfectionPathwayDef>
  
```

> 来自 `Anomaly/Defs/InfectionPathwayDefs/InfectionPathwayDefs.xml`，defName = `RevenantHypnotized`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：EntityAttacked / PrearrivalGeneric / RevenantHypnotized
label                                          [文本]  例：entity attack / prearrival generic / revenant hypnotized
```

## 三、全量字段表（3 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (3/3) | 文本 | EntityAttacked / PrearrivalGeneric / RevenantHypnotized |
| `label` | 100.0% (3/3) | 文本 | entity attack / prearrival generic / revenant hypnotized |
| `pawnRequired` | 33.3% (1/3) | 布尔 | true |

## 四、原版 defName 一览（共 3 个，列出前 60）

```text
`RevenantHypnotized`              `PrearrivalGeneric`               `EntityAttacked`                
```
