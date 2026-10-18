# PrisonerInteractionModeDef

- **所属线**：系统线
- **原版实例数**：12
- **字段路径数**：14
- **资料片**：Anomaly、Biotech、Core、Ideology
- **原版出处**：`Core/Defs/Misc/PrisonerInteractionModeDefs/PrisonerInteractionMode.xml`、`Ideology/Defs/PrisonerInteractionModeDefs/PrisonerInteractionMode.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<PrisonerInteractionModeDef>
    <defName>MaintainOnly</defName>
    <label>maintain only</label>
    <listOrder>0</listOrder>
    <description>Just feed the prisoner and provide for their basic needs, without attempting any other interaction.</description>
  </PrisonerInteractionModeDef>

  
```

> 来自 `Core/Defs/Misc/PrisonerInteractionModeDefs/PrisonerInteractionMode.xml`，defName = `MaintainOnly`，XML 节点数 5（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Bloodfeed / HemogenFarm / Interrogate
description                                    [文本]  例：An operation to extract hemogen packs will be automatically queued on this priso / Researchers interact with them to gain knowledge. / Wardens will interrogate the prisoner and watch their reactions to try to determ
label                                          [文本]  例：bloodfeed / hemogen farm / interrogate
listOrder                                      [数值]  例：0 / 25 / 26
```

## 三、全量字段表（14 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `allowInClassicIdeoMode` | 8.3% (1/12) | 布尔 | false |
| `allowOnWildMan` | 33.3% (4/12) | 布尔 | False / false |
| `defName` | 100.0% (12/12) | 文本 | Bloodfeed / HemogenFarm / Interrogate |
| `description` | 100.0% (12/12) | 文本 | An operation to extract hemogen packs will be automatically queued on this priso / Researchers interact with t |
| `hideIfGrayFleshNotAppeared` | 8.3% (1/12) | 布尔 | true |
| `hideIfNoBloodfeeders` | 8.3% (1/12) | 布尔 | true |
| `hideIfNotRecruitable` | 16.7% (2/12) | 布尔 | true |
| `hideIfNotStudiableAsPrisoner` | 8.3% (1/12) | 布尔 | true |
| `hideOnHemogenicPawns` | 16.7% (2/12) | 布尔 | true |
| `isChildInteraction` | 16.7% (2/12) | 布尔 | true |
| `isNonExclusiveInteraction` | 16.7% (2/12) | 布尔 | true |
| `label` | 100.0% (12/12) | 文本 | bloodfeed / hemogen farm / interrogate |
| `listOrder` | 100.0% (12/12) | 数值 | 0 / 25 / 26 |
| `mustBeAwake` | 25.0% (3/12) | 布尔 | false |

## 四、原版 defName 一览（共 12 个，列出前 60）

```text
`MaintainOnly`                    `Release`                         `Study`                           `Interrogate`                   
`Execution`                       `Enslave`                         `Convert`                         `AttemptRecruit`                
`ReduceWill`                      `HemogenFarm`                     `ReduceResistance`                `Bloodfeed`                     
```
