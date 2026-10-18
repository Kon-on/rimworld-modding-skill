# IdeoPresetDef

- **所属线**：理念线
- **原版实例数**：25
- **字段路径数**：8
- **资料片**：Anomaly、Biotech、Ideology
- **原版出处**：`Ideology/Defs/PreconfiguredIdeos/IdeoPresetDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<IdeoPresetDef>
    <defName>Cannibals</defName>
    <label>cannibals</label>
    <description>The flesh of man and woman is the highest form of sustenance. Also, it's just delicious.\n\nWill have gladiator duels, prisoner sacrifices, and human meat feasts.</description>
    <categoryDef>Strong</categoryDef>
    <memes>
      <li>Cannibal</li>
    </memes>
  </IdeoPresetDef>

  
```

> 来自 `Ideology/Defs/PreconfiguredIdeos/IdeoPresetDefs.xml`，defName = `Cannibals`，XML 节点数 7（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
categoryDef                                    [文本]  例：Intense / Mild / Strong
defName                                        [文本]  例：Blood_Worshippers / ClassicLike / Unity_Family
description                                    [文本]  例：The community is a family of hard-working, like-minded people. Putting yourself  / There is no truth except the void. Let us learn its secrets and bathe in the end / We are the children of the night, the thralls of the ancient blood drinkers. Let
label                                          [文本]  例：blood worshippers / classic-like / unity family
memes                                          [容器]
memes/li                                       [文本]  例：Bloodfeeding / PainIsVirtue / Ritualist
```

## 三、全量字段表（8 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `categoryDef` | 100.0% (25/25) | 文本 | Intense / Mild / Strong |
| `classicPlus` | 4.0% (1/25) | 布尔 | true |
| `defName` | 100.0% (25/25) | 文本 | Blood_Worshippers / ClassicLike / Unity_Family |
| `description` | 100.0% (25/25) | 文本 | The community is a family of hard-working, like-minded people. Putting yourself  / There is no truth except th |
| `iconPath` | 4.0% (1/25) | 文本 | UI/HeroArt/RimWorldLogo |
| `label` | 100.0% (25/25) | 文本 | blood worshippers / classic-like / unity family |
| `memes` | 100.0% (25/25) | 容器 |  |
| `memes/li` | 204.0% (51/25) | 文本 | Bloodfeeding / PainIsVirtue / Ritualist |

## 四、原版 defName 一览（共 25 个，列出前 60）

```text
`Cannibals`                       `Blood_Worshippers`               `Unity_Family`                    `Human_Purists`                 
`High_Collectivists`              `Free_Ranchers`                   `Violent_Dominators`              `Techno_Utopians`               
`Painful_Purists`                 `ProHuman_Darklovers`             `NatureOverMan`                   `Domination_Gang`               
`Nudist_Recruiters`               `Criminal_Gang`                   `Feminine_Ravagers`               `Martyrs`                       
`Mole_People`                     `Tree_Worshippers`                `Blindness_Cult`                  `Feral_People`                  
`Naked_Maneaters`                 `VoidFollowers`                   `ClassicLike`                     `Cowboys`                       
`Progressive_Humanism`          
```
