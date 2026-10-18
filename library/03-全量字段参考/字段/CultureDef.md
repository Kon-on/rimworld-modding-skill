# CultureDef

- **所属线**：理念线
- **原版实例数**：5
- **字段路径数**：25
- **资料片**：Core、Royalty
- **原版出处**：`Core/Defs/CultureDefs/Cultures.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<CultureDef>
    <defName>Rustican</defName>
    <label>rustican</label>
    <description>A hardy industrial culture common among rimworld outlanders.</description>
    <ideoNameMaker MayRequire="Ludeon.RimWorld.Ideology">NamerIdeoRustican</ideoNameMaker>
    <deityNameMaker MayRequire="Ludeon.RimWorld.Ideology">NamerDeityRustican</deityNameMaker>
    <deityTypeMaker MayRequire="Ludeon.RimWorld.Ideology">DeityTypeMakerRustican</deityTypeMaker>
    <leaderTitleMaker MayRequire="Ludeon.RimWorld.Ideology">LeaderTitleMaker_Rustican</leaderTitleMaker>
    <festivalNameMaker MayRequire="Ludeon.RimWorld.Ideology">NamerFestivalRustican</festivalNameMaker>
    <allowedPlaceTags>
      <li>OriginSpacer</li>
    </allowedPlaceTags>
    <iconPath>World/WorldObjects/Expanding/Town</iconPath>
    <thingStyleCategories>
      <li MayRequire="Ludeon.RimWorld.Ideology">
        <category>Rustic</category>
        <priority>2</priority>
      </li>
    </thingStyleCategories>
    <styleItemTags>
      <li>
        <tag>Rural</tag>
        <baseWeight>1</baseWeight>
        <weightFactor>1</weightFactor>
      </li>
      <li>
        <tag>NoBeard</tag>
        <baseWeight>10</baseWeight>
        <weightFactor>1</weightFactor>
      </li>
      <li>
        <tag>BeardRural</tag>
        <baseWeight>0.25</baseWeight>
        <weightFactor>1</weightFactor>
      </li>
      <li>
        <tag>NoTattoo</tag>
        <baseWeight>1</baseWeight>
        <weightFactor>1</weightFactor>
      </li>
    </styleItemTags>
  </CultureDef>

  
```

> 来自 `Core/Defs/CultureDefs/Cultures.xml`，defName = `Rustican`，XML 节点数 33（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
allowedPlaceTags                               [容器]
allowedPlaceTags/li                            [文本]  例：OriginSpacer / OriginTechnoFeudal / OriginTribal
defName                                        [文本]  例：Astropolitan / Corunan / Kriminul
deityNameMaker                                 [文本]  例：NamerDeityAstropolitan / NamerDeityCorunan / NamerDeityKriminul
deityTypeMaker                                 [文本]  例：DeityTypeMakerAstropolitan / DeityTypeMakerCorunan / DeityTypeMakerKriminul
description                                    [文本]  例：A broad category describing the styles and practices of many pirate groups. / A broad collection of cultures common among frequent space travelers. / A hardy industrial culture common among rimworld outlanders.
festivalNameMaker                              [文本]  例：NamerFestivalAstropolitan / NamerFestivalCorunan / NamerFestivalKriminul
iconPath                                       [文本]  例：UI/Cultures/Astropolitan / World/WorldObjects/Expanding/PirateOutpost / World/WorldObjects/Expanding/Town
ideoNameMaker                                  [文本]  例：NamerIdeoAstropolitan / NamerIdeoCorunan / NamerIdeoKriminul
label                                          [文本]  例：astropolitan / corunan / kriminul
leaderTitleMaker                               [文本]  例：LeaderTitleMaker_Astropolitan / LeaderTitleMaker_Corunan / LeaderTitleMaker_Kriminul
styleItemTags                                  [容器]
styleItemTags/li                               [容器]
styleItemTags/li/baseWeight                    [数值]  例：0.1 / 0.2 / 1
styleItemTags/li/tag                           [文本]  例：BeardRural / BeardUrban / Furskin
styleItemTags/li/weightFactor                  [数值]  例：1
```

## 三、全量字段表（25 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `allowedPlaceTags` | 100.0% (5/5) | 容器 |  |
| `allowedPlaceTags/li` | 100.0% (5/5) | 文本 | OriginSpacer / OriginTechnoFeudal / OriginTribal |
| `defName` | 100.0% (5/5) | 文本 | Astropolitan / Corunan / Kriminul |
| `deityNameMaker` | 100.0% (5/5) | 文本 | NamerDeityAstropolitan / NamerDeityCorunan / NamerDeityKriminul |
| `deityTypeMaker` | 100.0% (5/5) | 文本 | DeityTypeMakerAstropolitan / DeityTypeMakerCorunan / DeityTypeMakerKriminul |
| `description` | 100.0% (5/5) | 文本 | A broad category describing the styles and practices of many pirate groups. / A broad collection of cultures c |
| `festivalNameMaker` | 100.0% (5/5) | 文本 | NamerFestivalAstropolitan / NamerFestivalCorunan / NamerFestivalKriminul |
| `iconPath` | 100.0% (5/5) | 文本 | UI/Cultures/Astropolitan / World/WorldObjects/Expanding/PirateOutpost / World/WorldObjects/Expanding/Town |
| `ideoNameMaker` | 100.0% (5/5) | 文本 | NamerIdeoAstropolitan / NamerIdeoCorunan / NamerIdeoKriminul |
| `label` | 100.0% (5/5) | 文本 | astropolitan / corunan / kriminul |
| `leaderTitleMaker` | 100.0% (5/5) | 文本 | LeaderTitleMaker_Astropolitan / LeaderTitleMaker_Corunan / LeaderTitleMaker_Kriminul |
| `pawnNameMaker` | 40.0% (2/5) | 文本 | NamerPersonCorunan / NamerPersonSophian |
| `pawnNameMakerFemale` | 20.0% (1/5) | 文本 | NamerPersonSophianFemale |
| `preferredWeaponClasses` | 40.0% (2/5) | 容器 |  |
| `preferredWeaponClasses/despised` | 40.0% (2/5) | 文本 | Neolithic / Ultratech |
| `preferredWeaponClasses/noble` | 40.0% (2/5) | 文本 | Neolithic / Ultratech |
| `styleItemTags` | 100.0% (5/5) | 容器 |  |
| `styleItemTags/li` | 580.0% (29/5) | 容器 |  |
| `styleItemTags/li/baseWeight` | 580.0% (29/5) | 数值 | 0.1 / 0.2 / 1 |
| `styleItemTags/li/tag` | 580.0% (29/5) | 文本 | BeardRural / BeardUrban / Furskin |
| `styleItemTags/li/weightFactor` | 580.0% (29/5) | 数值 | 1 |
| `thingStyleCategories` | 60.0% (3/5) | 容器 |  |
| `thingStyleCategories/li` | 60.0% (3/5) | 容器 |  |
| `thingStyleCategories/li/category` | 60.0% (3/5) | 文本 | Rustic / Spikecore / Totemic |
| `thingStyleCategories/li/priority` | 60.0% (3/5) | 数值 | 2 |

## 四、原版 defName 一览（共 5 个，列出前 60）

```text
`Rustican`                        `Astropolitan`                    `Kriminul`                        `Corunan`                       
`Sophian`                       
```
