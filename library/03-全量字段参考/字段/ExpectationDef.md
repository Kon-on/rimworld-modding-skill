# ExpectationDef

- **所属线**：理念线
- **原版实例数**：10
- **字段路径数**：9
- **资料片**：Core、Ideology
- **原版出处**：`Core/Defs/Misc/ExpectationDefs/Expectations.xml`、`Ideology/Defs/Misc/ExpectationDefs/Expectations.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<ExpectationDef>
    <defName>Noble</defName>
    <label>noble</label>
    <order>8</order>
    <thoughtStage>6</thoughtStage>
    <joyKindsNeeded>6</joyKindsNeeded>
    <joyToleranceDropPerDay>0.07</joyToleranceDropPerDay>
  </ExpectationDef>

  
```

> 来自 `Core/Defs/Misc/ExpectationDefs/Expectations.xml`，defName = `Noble`，XML 节点数 7（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：ExtremelyLow / Low / Moderate
joyKindsNeeded                                 [数值]  例：2 / 3 / 4
joyToleranceDropPerDay                         [数值]  例：0.10 / 0.11 / 0.13
label                                          [文本]  例：extremely low / low / moderate
order                                          [数值]  例：0 / 1 / 2
thoughtStage                                   [数值]  例：2 / 3 / 4
```

## 三、全量字段表（9 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (10/10) | 文本 | ExtremelyLow / Low / Moderate |
| `forRoles` | 20.0% (2/10) | 布尔 | True |
| `joyKindsNeeded` | 100.0% (10/10) | 数值 | 2 / 3 / 4 |
| `joyToleranceDropPerDay` | 100.0% (10/10) | 数值 | 0.10 / 0.11 / 0.13 |
| `label` | 100.0% (10/10) | 文本 | extremely low / low / moderate |
| `maxMapWealth` | 60.0% (6/10) | 数值 | 15000 / 182000 / 31000 |
| `order` | 100.0% (10/10) | 数值 | 0 / 1 / 2 |
| `ritualQualityOffset` | 30.0% (3/10) | 数值 | 0.15 / 0.3 / 0.5 |
| `thoughtStage` | 100.0% (10/10) | 数值 | 2 / 3 / 4 |

## 四、原版 defName 一览（共 10 个，列出前 60）

```text
`Noble`                           `Royal`                           `Moderate`                        `High`                          
`SkyHigh`                         `RoleElite`                       `RoleSupreme`                     `ExtremelyLow`                  
`VeryLow`                         `Low`                           
```
