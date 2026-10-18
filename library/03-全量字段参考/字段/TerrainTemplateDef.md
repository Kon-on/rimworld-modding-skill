# TerrainTemplateDef

- **所属线**：世界线
- **原版实例数**：5
- **字段路径数**：24
- **资料片**：Core、Ideology、Royalty
- **原版出处**：`Ideology/Defs/TerrainDefs/Terrain_Floors.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<TerrainTemplateDef ParentName="IdeoCarpetTemplateBase">
    <defName>Carpet_Morbid</defName>
    <label>morbid carpet ({0})</label>
    <description>Fine carpet in a morbid style.</description>
    <texturePath>Terrain/Surfaces/MorbidCarpet</texturePath>
    <designatorDropdown>Floor_Morbid_Carpet</designatorDropdown>
    <dominantStyleCategory>Morbid</dominantStyleCategory>
  </TerrainTemplateDef>


  
```

> 来自 `Ideology/Defs/TerrainDefs/Terrain_Floors.xml`，defName = `Carpet_Morbid`，XML 节点数 7（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
tags/li                                        [文本]  例：FineFloor / Floor
```

## 三、全量字段表（24 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `burnedDef` | 60.0% (3/5) | 文本 | BurnedCarpet |
| `canGenerateDefaultDesignator` | 20.0% (1/5) | 布尔 | false |
| `constructionSkillPrerequisite` | 40.0% (2/5) | 数值 | 6 |
| `costList` | 60.0% (3/5) | 容器 |  |
| `costList/Cloth` | 60.0% (3/5) | 数值 | 35 / 7 |
| `defName` | 80.0% (4/5) | 文本 | Carpet / CarpetFine / Carpet_Morbid |
| `description` | 80.0% (4/5) | 文本 | Fine carpet in a morbid style. / Fine carpet with a hexagonal pattern for that ultra-technological look. / Lux |
| `designatorDropdown` | 80.0% (4/5) | 文本 | Floor_Carpet / Floor_Carpet_Fine / Floor_Morbid_Carpet |
| `dominantStyleCategory` | 40.0% (2/5) | 文本 | Morbid / Techist |
| `ignoreIllegalLabelCharacterConfigError` | 60.0% (3/5) | 布尔 | true |
| `label` | 80.0% (4/5) | 文本 | carpet ({0}) / fine carpet ({0}) / hex carpet ({0}) |
| `renderPrecedenceStart` | 60.0% (3/5) | 数值 | 200 / 220 |
| `researchPrerequisites` | 60.0% (3/5) | 容器 |  |
| `researchPrerequisites/li` | 60.0% (3/5) | 文本 | CarpetMaking |
| `statBases` | 60.0% (3/5) | 容器 |  |
| `statBases/Beauty` | 60.0% (3/5) | 数值 | 2 / 4 |
| `statBases/CleaningTimeFactor` | 60.0% (3/5) | 数值 | 2 |
| `statBases/Flammability` | 60.0% (3/5) | 数值 | 0.32 |
| `statBases/StyleDominance` | 20.0% (1/5) | 数值 | 1 |
| `statBases/WorkToBuild` | 60.0% (3/5) | 数值 | 4000 / 800 |
| `tags` | 60.0% (3/5) | 容器 |  |
| `tags/li` | 100.0% (5/5) | 文本 | FineFloor / Floor |
| `texturePath` | 80.0% (4/5) | 文本 | Terrain/Surfaces/Carpet / Terrain/Surfaces/CarpetFine / Terrain/Surfaces/HexCarpet |
| `uiOrder` | 60.0% (3/5) | 数值 | 2100 / 2110 / 2115 |

## 四、原版 defName 一览（共 5 个，列出前 60）

```text
`Carpet_Morbid`                   `Carpet_Transhumanist`            ``                                `Carpet`                        
`CarpetFine`                    
```
