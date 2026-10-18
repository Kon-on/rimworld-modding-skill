# GeneTemplateDef

- **所属线**：人物线
- **原版实例数**：9
- **字段路径数**：22
- **资料片**：Biotech
- **原版出处**：`Biotech/Defs/GeneDefs/GeneTemplateDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<GeneTemplateDef Name="GeneAptitudeBase" Abstract="True">
    <geneClass>Gene</geneClass>
    <ignoreIllegalLabelCharacterConfigError>true</ignoreIllegalLabelCharacterConfigError>
    <exclusionTagPrefix>Aptitude</exclusionTagPrefix>
    <geneTemplateType>Skill</geneTemplateType>
    <displayCategory>Aptitudes</displayCategory>
    <selectionWeight>0.2</selectionWeight>
  </GeneTemplateDef>

  
```

> 来自 `Biotech/Defs/GeneDefs/GeneTemplateDefs.xml`，defName = ``，XML 节点数 7（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

_该类型没有出现率≥90% 的字段（字段高度自由）。_

## 三、全量字段表（22 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `addictionChanceFactor` | 33.3% (3/9) | 数值 | 0 / 0.5 |
| `aptitudeOffset` | 44.4% (4/9) | 数值 | -4 / -8 / 4 |
| `biostatCpx` | 77.8% (7/9) | 数值 | 1 / 2 |
| `biostatMet` | 77.8% (7/9) | 数值 | -1 / -3 / 1 |
| `chemicalBiostatOverrides` | 33.3% (3/9) | 容器 |  |
| `chemicalBiostatOverrides/li` | 66.7% (6/9) | 容器 |  |
| `chemicalBiostatOverrides/li/biostatMet` | 66.7% (6/9) | 数值 | -1 / -3 / 3 |
| `chemicalBiostatOverrides/li/chemical` | 66.7% (6/9) | 文本 | Alcohol / Smokeleaf |
| `defName` | 77.8% (7/9) | 文本 | AptitudePoor / AptitudeRemarkable / AptitudeStrong |
| `description` | 77.8% (7/9) | 文本 | The carrier's aptitude in {0} is increased by 4. Aptitude acts like an offset on / The carrier's aptitude in { |
| `displayCategory` | 22.2% (2/9) | 文本 | Aptitudes / Drugs |
| `displayOrderOffset` | 77.8% (7/9) | 数值 | 0 / 10 / 20 |
| `exclusionTagPrefix` | 22.2% (2/9) | 文本 | Addiction / Aptitude |
| `geneClass` | 33.3% (3/9) | 文本 | Gene / Gene_ChemicalDependency |
| `geneTemplateType` | 22.2% (2/9) | 文本 | Chemical / Skill |
| `iconPath` | 77.8% (7/9) | 文本 | UI/Icons/Genes/Skills/{0}/Poor / UI/Icons/Genes/Skills/{0}/Remarkable / UI/Icons/Genes/Skills/{0}/Strong |
| `ignoreIllegalLabelCharacterConfigError` | 22.2% (2/9) | 布尔 | true |
| `label` | 77.8% (7/9) | 文本 | awful {0} / great {0} / poor {0} |
| `labelShortAdj` | 33.3% (3/9) | 文本 | {0}-dependent / {0}-impervious / {0}-resistant |
| `minAgeActive` | 11.1% (1/9) | 数值 | 13 |
| `passionModType` | 22.2% (2/9) | 文本 | AddOneLevel / DropAll |
| `selectionWeight` | 22.2% (2/9) | 数值 | 0.2 / 0.25 |

## 四、原版 defName 一览（共 9 个，列出前 60）

```text
``                                ``                                `AptitudePoor`                    `AptitudeStrong`                
`AptitudeTerrible`                `AptitudeRemarkable`              `AddictionResistant`              `AddictionImmune`               
`ChemicalDependency`            
```
