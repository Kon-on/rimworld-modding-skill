# BodyPartTagDef

- **所属线**：人物线
- **原版实例数**：25
- **字段路径数**：2
- **资料片**：Core
- **原版出处**：`Core/Defs/Misc/BodyPartTagDefs/BodyPartTagDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<BodyPartTagDef>
    <defName>BreathingSourceCage</defName>
  </BodyPartTagDef>

  
```

> 来自 `Core/Defs/Misc/BodyPartTagDefs/BodyPartTagDefs.xml`，defName = `BreathingSourceCage`，XML 节点数 2（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：BloodFiltrationKidney / BloodFiltrationLiver / BloodFiltrationSource
```

## 三、全量字段表（2 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (25/25) | 文本 | BloodFiltrationKidney / BloodFiltrationLiver / BloodFiltrationSource |
| `vital` | 32.0% (8/25) | 布尔 | true |

## 四、原版 defName 一览（共 25 个，列出前 60）

```text
`BreathingSourceCage`             `EatingSource`                    `EatingPathway`                   `Tongue`                        
`HearingSource`                   `ManipulationLimbCore`            `ManipulationLimbSegment`         `ManipulationLimbDigit`         
`MovingLimbCore`                  `MovingLimbSegment`               `MovingLimbDigit`                 `Pelvis`                        
`SightSource`                     `Spine`                           `TalkingSource`                   `TalkingPathway`                
`Mirrored`                        `BloodFiltrationSource`           `BloodFiltrationLiver`            `BloodFiltrationKidney`         
`BloodPumpingSource`              `BreathingSource`                 `BreathingPathway`                `ConsciousnessSource`           
`MetabolismSource`              
```
