# SurgeryOutcomeEffectDef

- **所属线**：人物线
- **原版实例数**：3
- **字段路径数**：24
- **资料片**：Biotech、Core
- **原版出处**：`Core/Defs/RecipeDefs/SurgeryOutcomeEffectDefs.xml`、`Biotech/Defs/RecipeDefs/SurgeryOutcomeEffectDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<SurgeryOutcomeEffectDef ParentName="SurgeryOutcomeBase">
    <defName>SurgeryOutcomeMinorFailure</defName>
    <outcomes Inherit="False">
      <li Class="SurgeryOutcomeSuccess"/>
      <li Class="SurgeryOutcome_Failure">
        <failure>true</failure>
        <totalDamage>20</totalDamage>
        <applyEffectsToPart>true</applyEffectsToPart>
        <letterLabel>Surgery failed on {PATIENT_labelShort}</letterLabel>
        <letterText>{SURGEON_labelShort} has failed in a minor way while operating on {PATIENT_labelShort} ({RECIPE_label}).</letterText>
      </li>
    </outcomes>
  </SurgeryOutcomeEffectDef>
```

> 来自 `Core/Defs/RecipeDefs/SurgeryOutcomeEffectDefs.xml`，defName = `SurgeryOutcomeMinorFailure`，XML 节点数 10（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
comps/li                                       [容器]
comps/li/curve                                 [容器]
comps/li/curve/points                          [容器]
comps/li/curve/points/li                       [文本]  例：(0, 1) / (20, 0.6) / (20, 1)
defName                                        [文本]  例：ImplantXenogerm / SurgeryOutcomeBase / SurgeryOutcomeMinorFailure
outcomes                                       [容器]
outcomes/li                                    [容器]
outcomes/li/applyEffectsToPart                 [布尔]  例：false / true
outcomes/li/applyToRecipes/li                  [文本]  例：ImplantIUD / RemoveIUD / ReverseVasectomy
outcomes/li/chance                             [数值]  例：0.03 / 0.05 / 0.45
outcomes/li/failure                            [布尔]  例：false / true
outcomes/li/letterLabel                        [文本]  例：Surgery failed on {PATIENT_labelShort} / Surgery failed on {PATIENT_labelShort}: Sterilized
outcomes/li/letterText                         [文本]  例：{SURGEON_labelShort} has failed catastrophically while operating on {PATIENT_lab / {SURGEON_labelShort} has failed in a minor way while operating on {PATIENT_label / {SURGEON_labelShort} has failed in a ridiculous way while operating on {PATIENT_
outcomes/li/totalDamage                        [数值]  例：10 / 20 / 65
```

## 三、全量字段表（24 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `comps` | 66.7% (2/3) | 容器 |  |
| `comps/li` | 400.0% (12/3) | 容器 |  |
| `comps/li/curve` | 133.3% (4/3) | 容器 |  |
| `comps/li/curve/points` | 133.3% (4/3) | 容器 |  |
| `comps/li/curve/points/li` | 333.3% (10/3) | 文本 | (0, 1) / (20, 0.6) / (20, 1) |
| `comps/li/factor` | 66.7% (2/3) | 数值 | 2 |
| `comps/li/inspirationDef` | 66.7% (2/3) | 文本 | Inspired_Surgery |
| `comps/li/range` | 33.3% (1/3) | 文本 | 0~0.98 |
| `defName` | 100.0% (3/3) | 文本 | ImplantXenogerm / SurgeryOutcomeBase / SurgeryOutcomeMinorFailure |
| `outcomes` | 100.0% (3/3) | 容器 |  |
| `outcomes/li` | 333.3% (10/3) | 容器 |  |
| `outcomes/li/applyEffectsToPart` | 266.7% (8/3) | 布尔 | false / true |
| `outcomes/li/applyToRecipes` | 66.7% (2/3) | 容器 |  |
| `outcomes/li/applyToRecipes/li` | 133.3% (4/3) | 文本 | ImplantIUD / RemoveIUD / ReverseVasectomy |
| `outcomes/li/chance` | 200.0% (6/3) | 数值 | 0.03 / 0.05 / 0.45 |
| `outcomes/li/failedHediff` | 66.7% (2/3) | 文本 | Sterilized |
| `outcomes/li/failure` | 266.7% (8/3) | 布尔 | false / true |
| `outcomes/li/hediff` | 33.3% (1/3) | 文本 | XenogerminationComa |
| `outcomes/li/letterLabel` | 233.3% (7/3) | 文本 | Surgery failed on {PATIENT_labelShort} / Surgery failed on {PATIENT_labelShort}: Sterilized |
| `outcomes/li/letterText` | 233.3% (7/3) | 文本 | {SURGEON_labelShort} has failed catastrophically while operating on {PATIENT_lab / {SURGEON_labelShort} has fa |
| `outcomes/li/qualityToDurationDaysCurve` | 33.3% (1/3) | 容器 |  |
| `outcomes/li/qualityToDurationDaysCurve/points` | 33.3% (1/3) | 容器 |  |
| `outcomes/li/qualityToDurationDaysCurve/points/li` | 66.7% (2/3) | 文本 | (0, 3) / (1, 1) |
| `outcomes/li/totalDamage` | 200.0% (6/3) | 数值 | 10 / 20 / 65 |

## 四、原版 defName 一览（共 3 个，列出前 60）

```text
`SurgeryOutcomeMinorFailure`      `ImplantXenogerm`                 `SurgeryOutcomeBase`            
```
