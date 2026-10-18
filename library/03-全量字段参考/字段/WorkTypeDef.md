# WorkTypeDef

- **所属线**：系统线
- **原版实例数**：22
- **字段路径数**：14
- **资料片**：Anomaly、Biotech、Core
- **原版出处**：`Core/Defs/WorkTypeDefs/WorkTypes.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<WorkTypeDef>
    <defName>Patient</defName>
    <labelShort>patient</labelShort>
    <pawnLabel>Patient</pawnLabel>
    <gerundLabel>patienting</gerundLabel>
    <description>Go to a medical bed for treatment if you have an immediately life-threatening health condition.</description>
    <verb>Become patient</verb>
    <naturalPriority>1350</naturalPriority>
    <alwaysStartActive>true</alwaysStartActive>
  </WorkTypeDef>

  
```

> 来自 `Core/Defs/WorkTypeDefs/WorkTypes.xml`，defName = `Patient`，XML 节点数 9（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Childcare / DarkStudy / Firefighter
description                                    [文本]  例：Care for a baby or child of the colony. / Extinguish fires in the colony. / Go to a medical bed for treatment if you have an immediately life-threatening he
gerundLabel                                    [文本]  例：caring / firefighting / patienting
labelShort                                     [文本]  例：childcare / dark study / firefight
naturalPriority                                [数值]  例：1175 / 1350 / 1400
pawnLabel                                      [文本]  例：Childcarer / Firefighter / Patient
verb                                           [文本]  例：Become patient / Care / Extinguish
workTags                                       [容器]
workTags/li                                    [文本]  例：AllWork / Commoner / Intellectual
```

## 三、全量字段表（14 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `alwaysStartActive` | 31.8% (7/22) | 布尔 | true |
| `defName` | 100.0% (22/22) | 文本 | Childcare / DarkStudy / Firefighter |
| `description` | 100.0% (22/22) | 文本 | Care for a baby or child of the colony. / Extinguish fires in the colony. / Go to a medical bed for treatment  |
| `disabledForSlaves` | 22.7% (5/22) | 布尔 | true |
| `gerundLabel` | 100.0% (22/22) | 文本 | caring / firefighting / patienting |
| `labelShort` | 100.0% (22/22) | 文本 | childcare / dark study / firefight |
| `naturalPriority` | 100.0% (22/22) | 数值 | 1175 / 1350 / 1400 |
| `pawnLabel` | 100.0% (22/22) | 文本 | Childcarer / Firefighter / Patient |
| `relevantSkills` | 72.7% (16/22) | 容器 |  |
| `relevantSkills/li` | 77.3% (17/22) | 文本 | Animals / Intellectual / Medicine |
| `requireCapableColonist` | 45.5% (10/22) | 布尔 | true |
| `verb` | 100.0% (22/22) | 文本 | Become patient / Care / Extinguish |
| `workTags` | 90.9% (20/22) | 容器 |  |
| `workTags/li` | 318.2% (70/22) | 文本 | AllWork / Commoner / Intellectual |

## 四、原版 defName 一览（共 22 个，列出前 60）

```text
`Patient`                         `PatientBedRest`                  `BasicWorker`                     `Firefighter`                   
`Doctor`                          `Handling`                        `DarkStudy`                       `Warden`                        
`Cooking`                         `Smithing`                        `Tailoring`                       `Art`                           
`Hauling`                         `Cleaning`                        `Research`                        `Childcare`                     
`Construction`                    `Growing`                         `Mining`                          `PlantCutting`                  
`Crafting`                        `Hunting`                       
```
