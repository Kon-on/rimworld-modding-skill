# GoodwillSituationDef

- **所属线**：世界线
- **原版实例数**：39
- **字段路径数**：8
- **资料片**：Core、Ideology
- **原版出处**：`Core/Defs/Goodwill/GoodwillSituations_Misc.xml`、`Ideology/Defs/Goodwill/GoodwillSituations_MemeCompatibility.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<GoodwillSituationDef>
    <defName>PermanentEnemy</defName>
    <label>permanently hostile</label>
    <workerClass>GoodwillSituationWorker_PermanentEnemy</workerClass>
  </GoodwillSituationDef>

  
```

> 来自 `Core/Defs/Goodwill/GoodwillSituations_Misc.xml`，defName = `PermanentEnemy`，XML 节点数 4（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：AttackingSettlement / NaturalEnemy / PermanentEnemy
label                                          [文本]  例：attacking settlement / both follow {0_name} / natural enemy
naturalGoodwillOffset                          [数值]  例：-10 / -20 / -30
workerClass                                    [文本]  例：GoodwillSituationWorker_AttackingSettlement / GoodwillSituationWorker_NaturalEnemy / GoodwillSituationWorker_PermanentEnemy
```

## 三、全量字段表（8 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (39/39) | 文本 | AttackingSettlement / NaturalEnemy / PermanentEnemy |
| `ignoreIllegalLabelCharacterConfigError` | 2.6% (1/39) | 布尔 | true |
| `label` | 100.0% (39/39) | 文本 | attacking settlement / both follow {0_name} / natural enemy |
| `meme` | 89.7% (35/39) | 文本 | AnimalPersonhood / FleshPurity / PainIsVirtue |
| `naturalGoodwillOffset` | 92.3% (36/39) | 数值 | -10 / -20 / -30 |
| `otherMeme` | 79.5% (31/39) | 文本 | AnimalPersonhood / FleshPurity / PainIsVirtue |
| `versusAll` | 10.3% (4/39) | 布尔 | true |
| `workerClass` | 100.0% (39/39) | 文本 | GoodwillSituationWorker_AttackingSettlement / GoodwillSituationWorker_NaturalEnemy / GoodwillSituationWorker_P |

## 四、原版 defName 一览（共 39 个，列出前 60）

```text
`PermanentEnemy`                  `NaturalEnemy`                    `AttackingSettlement`             `SameIdeo`                      
`AnimalPersonhood_AnimalPersonhood`  `Transhumanist_Transhumanist`     `FleshPurity_FleshPurity`         `PainIsVirtue_PainIsVirtue`     
`Cannibal_Cannibal`               `HumanPrimacy_HumanPrimacy`       `NaturePrimacy_NaturePrimacy`     `Individualist_Individualist`   
`Collectivist_Collectivist`       `MaleSupremacy_MaleSupremacy`     `FemaleSupremacy_FemaleSupremacy`  `Nudism_Nudism`                 
`HighLife_HighLife`               `Cannibal_FleshPurity`            `Cannibal_PainIsVirtue`           `HumanPrimacy_Transhumanist`    
`HumanPrimacy_FleshPurity`        `NaturePrimacy_AnimalPersonhood`  `Guilty_All`                      `FleshPurity_Transhumanist`     
`NaturePrimacy_Transhumanist`     `HumanPrimacy_AnimalPersonhood`   `Individualist_Cannibal`          `Individualist_Proselytizer`    
`Collectivist_Individualist`      `MaleSupremacy_Individualist`     `FemaleSupremacy_Individualist`   `Rancher_AnimalPersonhood`      
`NaturePrimacy_HumanPrimacy`      `FemaleSupremacy_MaleSupremacy`   `HighLife_FleshPurity`            `Rancher_NaturePrimacy`         
`Supremacist_All`                 `Raider_All`                      `Loyalist_All`                  
```
