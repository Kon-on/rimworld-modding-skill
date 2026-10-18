# PlaceDef

- **所属线**：理念线
- **原版实例数**：20
- **字段路径数**：8
- **资料片**：Ideology、Royalty
- **原版出处**：`Royalty/Defs/Misc/Places.xml`、`Ideology/Defs/Misc/PlaceDefs/Places.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<PlaceDef>
    <defName>Sophiamunda</defName>
    <tags>
      <li>OriginTechnoFeudal</li>
    </tags>
    <placeRules>
      <include>
        <li MayRequire="Ludeon.RimWorld.Ideology">PlaceMakerCommon</li>
      </include>
      <rulesStrings>
        <!-- Sophiamunda is the shattered empire's home world. -->
        <li>place_name-&gt;Sophiamunda</li>
        <li>place_adjective-&gt;Sophian</li>
        <li>place_summary-&gt;techno-feudal world</li>
        <li>place_community-&gt;castle</li>
        <li>place_community-&gt;palace</li>
        <li>place_job-&gt;knight</li>
        <li>place_job-&gt;squire</li>
        <li>place_job-&gt;duke</li>
        <li>place_job-&gt;maid</li>
        <li>place_job-&gt;swordsmith</li>
        <li>place_personalWeapon-&gt;persona plasmasword</li>
        <li>place_personalWeapon-&gt;warhammer</li>
        <li>place_massWeapon-&gt;an orbital mech cluster targeter</li>
        <li>place_massWeapon-&gt;a bio-engineered plague</li>
        <li>place_massWeapon-&gt;an army of fallen knights</li>
        <li>place_foeLeader-&gt;revolutionist</li>
        <li>place_foeSoldiers-&gt;rebels</li>
      </rulesStrings>
    </placeRules>
  </PlaceDef>
```

> 来自 `Royalty/Defs/Misc/Places.xml`，defName = `Sophiamunda`，XML 节点数 26（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Boccocarro / Chelis / Ilwaba
placeRules                                     [容器]
placeRules/include                             [容器]
placeRules/include/li                          [文本]  例：PlaceMakerCommon
placeRules/rulesStrings                        [容器]
placeRules/rulesStrings/li                     [文本]  例：place_adjective->Oubanyeni / place_community->tree-top village / place_name->Oubanyen
tags                                           [容器]
tags/li                                        [文本]  例：OriginSpacer / OriginTechnoFeudal / OriginTribal
```

## 三、全量字段表（8 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (20/20) | 文本 | Boccocarro / Chelis / Ilwaba |
| `placeRules` | 100.0% (20/20) | 容器 |  |
| `placeRules/include` | 100.0% (20/20) | 容器 |  |
| `placeRules/include/li` | 100.0% (20/20) | 文本 | PlaceMakerCommon |
| `placeRules/rulesStrings` | 100.0% (20/20) | 容器 |  |
| `placeRules/rulesStrings/li` | 1860.0% (372/20) | 文本 | place_adjective->Oubanyeni / place_community->tree-top village / place_name->Oubanyen |
| `tags` | 100.0% (20/20) | 容器 |  |
| `tags/li` | 145.0% (29/20) | 文本 | OriginSpacer / OriginTechnoFeudal / OriginTribal |

## 四、原版 defName 一览（共 20 个，列出前 60）

```text
`Sophiamunda`                     `Nuchadus`                        `Yttak`                           `Xanides`                       
`Lutuni`                          `AturaStation`                    `Oubanyen`                        `Chelis`                        
`Ilwaba`                          `Boccocarro`                      `Bagua5`                          `Rhydell`                       
`Iwamura`                         `Kemia`                           `Rogia`                           `Novaroma`                      
`Filson`                          `Zoutera`                         `Wavia`                           `Creticon`                      
```
