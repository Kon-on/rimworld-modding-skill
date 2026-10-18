# GauranlenTreeModeDef

- **所属线**：理念线
- **原版实例数**：7
- **字段路径数**：11
- **资料片**：Ideology
- **原版出处**：`Ideology/Defs/GauranlenTreeModDefs/GauranlenTreeModeDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<GauranlenTreeModeDef>
    <defName>Carrier</defName>
    <label>carrier</label>
    <description>A dryad caste specialized in carrying items. Under human influence, it can help haul things where they need to go.</description>
    <pawnKindDef>Dryad_Carrier</pawnKindDef>
    <drawPosition>(0, 0)</drawPosition>
    <displayedStats>
      <li>MaxHitPoints</li>
      <li>MoveSpeed</li>
      <li>CarryingCapacity</li>
    </displayedStats>
    <hyperlinks>
      <ThingDef>Dryad_Carrier</ThingDef>
    </hyperlinks>
  </GauranlenTreeModeDef>

  
```

> 来自 `Ideology/Defs/GauranlenTreeModDefs/GauranlenTreeModeDefs.xml`，defName = `Carrier`，XML 节点数 12（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Barkskin / Carrier / Clawer
description                                    [文本]  例：A dryad caste specialized in absorbing hits during combat. Barkskin dryads are c / A dryad caste specialized in aggression and damage-dealing attacks. The clawer d / A dryad caste specialized in carrying items. Under human influence, it can help 
displayedStats                                 [容器]
displayedStats/li                              [文本]  例：ArmorRating_Blunt / CarryingCapacity / MaxHitPoints
drawPosition                                   [文本]  例：(0, 0) / (0, 0.1665) / (0, 0.333)
hyperlinks                                     [容器]
hyperlinks/ThingDef                            [文本]  例：Dryad_Barkskin / Dryad_Carrier / Dryad_Clawer
label                                          [文本]  例：barkskin / carrier / clawer
pawnKindDef                                    [文本]  例：Dryad_Barkskin / Dryad_Carrier / Dryad_Clawer
```

## 三、全量字段表（11 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (7/7) | 文本 | Barkskin / Carrier / Clawer |
| `description` | 100.0% (7/7) | 文本 | A dryad caste specialized in absorbing hits during combat. Barkskin dryads are c / A dryad caste specialized i |
| `displayedStats` | 100.0% (7/7) | 容器 |  |
| `displayedStats/li` | 271.4% (19/7) | 文本 | ArmorRating_Blunt / CarryingCapacity / MaxHitPoints |
| `drawPosition` | 100.0% (7/7) | 文本 | (0, 0) / (0, 0.1665) / (0, 0.333) |
| `hyperlinks` | 100.0% (7/7) | 容器 |  |
| `hyperlinks/ThingDef` | 157.1% (11/7) | 文本 | Dryad_Barkskin / Dryad_Carrier / Dryad_Clawer |
| `label` | 100.0% (7/7) | 文本 | barkskin / carrier / clawer |
| `pawnKindDef` | 100.0% (7/7) | 文本 | Dryad_Barkskin / Dryad_Carrier / Dryad_Clawer |
| `requiredMemes` | 14.3% (1/7) | 容器 |  |
| `requiredMemes/li` | 14.3% (1/7) | 文本 | TreeConnection |

## 四、原版 defName 一览（共 7 个，列出前 60）

```text
`Carrier`                         `Woodmaker`                       `Medicinemaker`                   `Berrymaker`                    
`Clawer`                          `Barkskin`                        `Gaumaker`                      
```
