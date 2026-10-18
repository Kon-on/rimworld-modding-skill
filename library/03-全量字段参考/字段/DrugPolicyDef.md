# DrugPolicyDef

- **所属线**：系统线
- **原版实例数**：4
- **字段路径数**：10
- **资料片**：Core
- **原版出处**：`Core/Defs/DrugPolicyDefs/DrugPolicyDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<DrugPolicyDef>
    <defName>NoDrugs</defName>
    <label>no drugs</label>
  </DrugPolicyDef>

  
```

> 来自 `Core/Defs/DrugPolicyDefs/DrugPolicyDefs.xml`，defName = `NoDrugs`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：NoDrugs / OneDrinkPerDay / SocialDrugs
entries/li                                     [容器]
entries/li/allowedForJoy                       [布尔]  例：true
entries/li/drug                                [文本]  例：Beer / SmokeleafJoint
label                                          [文本]  例：no drugs / one drink per day / social drugs
```

## 三、全量字段表（10 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `allowPleasureDrugs` | 25.0% (1/4) | 布尔 | true |
| `defName` | 100.0% (4/4) | 文本 | NoDrugs / OneDrinkPerDay / SocialDrugs |
| `entries` | 50.0% (2/4) | 容器 |  |
| `entries/li` | 100.0% (4/4) | 容器 |  |
| `entries/li/allowedForJoy` | 100.0% (4/4) | 布尔 | true |
| `entries/li/allowScheduled` | 25.0% (1/4) | 布尔 | true |
| `entries/li/daysFrequency` | 25.0% (1/4) | 数值 | 1 |
| `entries/li/drug` | 100.0% (4/4) | 文本 | Beer / SmokeleafJoint |
| `entries/li/takeToInventory` | 25.0% (1/4) | 数值 | 1 |
| `label` | 100.0% (4/4) | 文本 | no drugs / one drink per day / social drugs |

## 四、原版 defName 一览（共 4 个，列出前 60）

```text
`NoDrugs`                         `Unrestricted`                    `SocialDrugs`                     `OneDrinkPerDay`                
```
