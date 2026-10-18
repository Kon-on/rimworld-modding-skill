# MusicTransitionDef

- **所属线**：表现线
- **原版实例数**：9
- **字段路径数**：6
- **资料片**：Anomaly、Odyssey
- **原版出处**：`Anomaly/Defs/Misc/Music/Music_Transitions.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<MusicTransitionDef>
    <defName>HorrorMonolithAdvanced</defName>
    <workerType>HorrorMonolithAdvancedTransition</workerType>
    <sequence>HorrorMonolithAdvanced</sequence>
    <priority>175</priority>
  </MusicTransitionDef>
  
  
```

> 来自 `Anomaly/Defs/Misc/Music/Music_Transitions.xml`，defName = `HorrorMonolithAdvanced`，XML 节点数 5（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：HorrorCombat / HorrorMonolithAdvanced / HorrorRelax
priority                                       [数值]  例：100 / 150 / 175
sequence                                       [文本]  例：HorrorCombat / HorrorMonolithAdvanced / HorrorRelax
workerType                                     [文本]  例：HorrorCombatTransition / HorrorMonolithAdvancedTransition / HorrorRelaxTransition
```

## 三、全量字段表（6 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `dangerRequirement` | 66.7% (6/9) | 文本 | RequiresDanger / RequiresNoDanger |
| `defName` | 100.0% (9/9) | 文本 | HorrorCombat / HorrorMonolithAdvanced / HorrorRelax |
| `overridesInterruptions` | 22.2% (2/9) | 布尔 | true |
| `priority` | 100.0% (9/9) | 数值 | 100 / 150 / 175 |
| `sequence` | 100.0% (9/9) | 文本 | HorrorCombat / HorrorMonolithAdvanced / HorrorRelax |
| `workerType` | 100.0% (9/9) | 文本 | HorrorCombatTransition / HorrorMonolithAdvancedTransition / HorrorRelaxTransition |

## 四、原版 defName 一览（共 9 个，列出前 60）

```text
`HorrorMonolithAdvanced`          `HorrorRelax`                     `HorrorTension`                   `HorrorCombat`                  
`CorpseAttack`                    `MetalHell`                       `OrbitalRelax`                    `OrbitalCombat`                 
`Mechhive`                      
```
