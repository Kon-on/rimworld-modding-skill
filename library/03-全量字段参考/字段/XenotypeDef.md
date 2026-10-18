# XenotypeDef

- **所属线**：人物线
- **原版实例数**：12
- **字段路径数**：27
- **资料片**：Biotech、Odyssey
- **原版出处**：`Biotech/Defs/GeneDefs/XenotypeDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<XenotypeDef>
    <defName>Baseliner</defName>
    <label>baseliner</label>
    <description>A naturally-evolved human with no major significant genetic modifications.</description>
    <iconPath>UI/Icons/Xenotypes/Baseliner</iconPath>
    <displayPriority>1000</displayPriority>
    <factionlessGenerationWeight>40</factionlessGenerationWeight>
  </XenotypeDef>

  
```

> 来自 `Biotech/Defs/GeneDefs/XenotypeDefs.xml`，defName = `Baseliner`，XML 节点数 7（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Baseliner / Dirtmole / Genie
description                                    [文本]  例：A naturally-evolved human with no major significant genetic modifications. / Designed to be engineers, genies' delicate bones and natural aptitude with machi / Hussars are engineered soldiers. They fight aggressively and with precision, hea
descriptionShort                               [文本]  例：Designed to be engineers, genies have natural aptitude with machines, and are em / Hussars are engineered soldiers. They fight aggressively and with precision, hea / Sanguophages are ageless, deathless super-humans powered by archotech-created ar
genes                                          [容器]
genes/li                                       [文本]  例：AptitudeRemarkable_Mining / DarkVision / Eyes_Gray
iconPath                                       [文本]  例：UI/Icons/Xenotypes/Baseliner / UI/Icons/Xenotypes/Dirtmole / UI/Icons/Xenotypes/Genie
label                                          [文本]  例：baseliner / dirtmole / genie
```

## 三、全量字段表（27 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `canGenerateAsCombatant` | 8.3% (1/12) | 布尔 | false |
| `chanceToUseNameMaker` | 41.7% (5/12) | 数值 | 0.75 / 1 |
| `combatPowerFactor` | 50.0% (6/12) | 数值 | 1.2 / 1.5 / 1.6 |
| `defName` | 100.0% (12/12) | 文本 | Baseliner / Dirtmole / Genie |
| `description` | 100.0% (12/12) | 文本 | A naturally-evolved human with no major significant genetic modifications. / Designed to be engineers, genies' |
| `descriptionShort` | 91.7% (11/12) | 文本 | Designed to be engineers, genies have natural aptitude with machines, and are em / Hussars are engineered sold |
| `displayPriority` | 16.7% (2/12) | 数值 | -1000 / 1000 |
| `doubleXenotypeChances` | 8.3% (1/12) | 容器 |  |
| `doubleXenotypeChances/Dirtmole` | 8.3% (1/12) | 数值 | 0.02 |
| `doubleXenotypeChances/Impid` | 8.3% (1/12) | 数值 | 0.02 |
| `doubleXenotypeChances/Neanderthal` | 8.3% (1/12) | 数值 | 0.02 |
| `doubleXenotypeChances/Pigskin` | 8.3% (1/12) | 数值 | 0.02 |
| `doubleXenotypeChances/Waster` | 8.3% (1/12) | 数值 | 0.02 |
| `doubleXenotypeChances/Yttakin` | 8.3% (1/12) | 数值 | 0.02 |
| `factionlessGenerationWeight` | 16.7% (2/12) | 数值 | 0 / 40 |
| `forbiddenWeaponClasses` | 8.3% (1/12) | 容器 |  |
| `forbiddenWeaponClasses/li` | 8.3% (1/12) | 文本 | LongShots |
| `generateWithXenogermReplicatingHediffChance` | 8.3% (1/12) | 数值 | 0.5 |
| `genes` | 91.7% (11/12) | 容器 |  |
| `genes/li` | 1500.0% (180/12) | 文本 | AptitudeRemarkable_Mining / DarkVision / Eyes_Gray |
| `iconPath` | 100.0% (12/12) | 文本 | UI/Icons/Xenotypes/Baseliner / UI/Icons/Xenotypes/Dirtmole / UI/Icons/Xenotypes/Genie |
| `inheritable` | 50.0% (6/12) | 布尔 | true |
| `label` | 100.0% (12/12) | 文本 | baseliner / dirtmole / genie |
| `nameMaker` | 41.7% (5/12) | 文本 | NamerPersonDirtmole_Male / NamerPersonImpid / NamerPersonPigskin |
| `nameMakerFemale` | 8.3% (1/12) | 文本 | NamerPersonDirtmole_Female |
| `soundDefOnImplant` | 8.3% (1/12) | 文本 | PawnBecameSanguophage |
| `xenogermReplicatingDurationLeftDaysRange` | 8.3% (1/12) | 文本 | 0.1~140 |

## 四、原版 defName 一览（共 12 个，列出前 60）

```text
`Baseliner`                       `Genie`                           `Starjack`                        `Dirtmole`                      
`Waster`                          `Pigskin`                         `Neanderthal`                     `Hussar`                        
`Yttakin`                         `Impid`                           `Highmate`                        `Sanguophage`                   
```
