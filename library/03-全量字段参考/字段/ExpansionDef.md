# ExpansionDef

- **所属线**：系统线
- **原版实例数**：6
- **字段路径数**：12
- **资料片**：Core
- **原版出处**：`Core/Defs/Misc/ExpansionDefs/ExpansionDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<ExpansionDef>
    <defName>Core</defName>
    <label>Core</label>
    <description>Core RimWorld content.</description>
    <linkedMod>Ludeon.RimWorld</linkedMod>
    <iconPath>UI/HeroArt/RimWorldLogo</iconPath>
    <backgroundPath>UI/HeroArt/BGPlanet</backgroundPath>
    <isCore>True</isCore>
  </ExpansionDef>

  
```

> 来自 `Core/Defs/Misc/ExpansionDefs/ExpansionDefs.xml`，defName = `Core`，XML 节点数 8（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
backgroundPath                                 [文本]  例：UI/HeroArt/BGPlanet / UI/HeroArt/MenuBG_Biotech / UI/HeroArt/MenuBG_Ideology
defName                                        [文本]  例：Biotech / Core / Ideology
description                                    [文本]  例：Core RimWorld content. / Create your own belief system with fine control over behaviors, preferences, rit / Fight or ally with the new Shattered Empire faction.

Gain psychic powers throug
iconPath                                       [文本]  例：UI/HeroArt/ExpansionIcon_Biotech / UI/HeroArt/ExpansionIcon_Ideology / UI/HeroArt/ExpansionIcon_Royalty
label                                          [文本]  例：Biotech / Core / Ideology
linkedMod                                      [文本]  例：Ludeon.RimWorld / Ludeon.RimWorld.Biotech / Ludeon.RimWorld.Ideology
```

## 三、全量字段表（12 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `backgroundPath` | 100.0% (6/6) | 文本 | UI/HeroArt/BGPlanet / UI/HeroArt/MenuBG_Biotech / UI/HeroArt/MenuBG_Ideology |
| `defName` | 100.0% (6/6) | 文本 | Biotech / Core / Ideology |
| `description` | 100.0% (6/6) | 文本 | Core RimWorld content. / Create your own belief system with fine control over behaviors, preferences, rit / Fi |
| `iconPath` | 100.0% (6/6) | 文本 | UI/HeroArt/ExpansionIcon_Biotech / UI/HeroArt/ExpansionIcon_Ideology / UI/HeroArt/ExpansionIcon_Royalty |
| `isCore` | 16.7% (1/6) | 布尔 | True |
| `label` | 100.0% (6/6) | 文本 | Biotech / Core / Ideology |
| `linkedMod` | 100.0% (6/6) | 文本 | Ludeon.RimWorld / Ludeon.RimWorld.Biotech / Ludeon.RimWorld.Ideology |
| `notOwnedIconPath` | 83.3% (5/6) | 文本 | UI/HeroArt/NotOwned_Anomaly / UI/HeroArt/NotOwned_Biotech / UI/HeroArt/NotOwned_Ideology |
| `previewImagesFolderPath` | 83.3% (5/6) | 文本 | UI/HeroArt/Preview_Anomaly / UI/HeroArt/Preview_Biotech / UI/HeroArt/Preview_Ideology |
| `primaryColor` | 83.3% (5/6) | 文本 | (125, 179, 179) / (179, 125, 125) / (179, 179, 125) |
| `siteUrl` | 83.3% (5/6) | 文本 | https://rimworldgame.com/ |
| `steamUrl` | 83.3% (5/6) | 文本 | https://store.steampowered.com/app/1392840 / https://store.steampowered.com/app/1826140 / https://store.steamp |

## 四、原版 defName 一览（共 6 个，列出前 60）

```text
`Core`                            `Royalty`                         `Ideology`                        `Biotech`                       
`Anomaly`                         `Odyssey`                       
```
