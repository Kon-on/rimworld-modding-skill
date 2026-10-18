# MemeDef

- **所属线**：理念线
- **原版实例数**：38
- **字段路径数**：102
- **资料片**：Anomaly、Biotech、Ideology、Odyssey
- **原版出处**：`Ideology/Defs/MemeDefs/Memes_Structures_OriginsReligious.xml`、`Ideology/Defs/MemeDefs/Memes_Misc.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<MemeDef Name="StructureOriginBase" Abstract="True">
    <category>Structure</category>
    <impact>0</impact>
    <selectOneOrNone>
      <noneChance>0.8</noneChance>
      <preceptThingPairs>
        <li>
          <precept>ApparelDesired_Soft_Subordinate</precept>
          <thing>Apparel_Headwrap</thing>
        </li>
        <li>
          <precept>ApparelDesired_Soft_Subordinate</precept>
          <thing>Apparel_Broadwrap</thing>
        </li>
      </preceptThingPairs>
    </selectOneOrNone>
  </MemeDef>

  
```

> 来自 `Ideology/Defs/MemeDefs/Memes_Structures_OriginsReligious.xml`，defName = ``，XML 节点数 12（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Bloodfeeding / Inhuman / MaleSupremacy
description                                    [文本]  例：Drinking blood is sacred. Bloodfeeders should be worshipped. / Humanity is a barrier to our connection with the machine god and its pleasurable / Men are the superior gender and should rule.
descriptionMaker/rules/rulesStrings/li         [文本]  例：creation(tag=meme_Bloodfeeding)        ->[deity0_name] drank the blood of the st / episode(uses=1,tag=meme_Bloodfeeding)  ->The [deity0_type] [deity0_name] gave to / intro(tag=meme_Bloodfeeding)           ->On the [place_summary] [place_name], du
generalRules                                   [容器]
generalRules/rulesStrings                      [容器]
generalRules/rulesStrings/li                   [文本]  例：memeAdjective->dark / memeAdjective->inhuman / memeAdjective->machine
iconPath                                       [文本]  例：UI/Memes/Bloodfeeding / UI/Memes/Inhuman / UI/Memes/Ritualist
label                                          [文本]  例：bloodfeeding / inhuman / male supremacy
requireOne/li                                  [容器]
requireOne/li/li                               [文本]  例：Lovin_Free / Nudity_Female_NoRules / Nudity_Male_NoRules
symbolPacks/li                                 [容器]
symbolPacks/li/adjective                       [文本]  例：fertilist / manist / masculist
symbolPacks/li/ideoName                        [文本]  例：Fertilism / Manism / Masculinism
symbolPacks/li/member                          [文本]  例：fertilist / manist / masculinist
symbolPacks/li/prefix                          [布尔]  例：true
symbolPacks/li/theme                           [文本]  例：fertility / man / masculinity
```

## 三、全量字段表（102 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `addDesignatorGroups` | 5.3% (2/38) | 容器 |  |
| `addDesignatorGroups/li` | 5.3% (2/38) | 文本 | Floor_MindbendCarpet / Floor_Transhumanist_Carpet |
| `addDesignators` | 10.5% (4/38) | 容器 |  |
| `addDesignators/li` | 18.4% (7/38) | 文本 | NeuralSupercharger / SlabBed / SleepAccelerator |
| `agreeableTraits` | 23.7% (9/38) | 容器 |  |
| `agreeableTraits/DrugDesire` | 5.3% (2/38) | 数值 | 1 / 2 |
| `agreeableTraits/li` | 28.9% (11/38) | 文本 | BodyPurist / DislikesMen / DislikesWomen |
| `allowDuringTutorial` | 5.3% (2/38) | 布尔 | true |
| `allowSymbolsFromDeity` | 7.9% (3/38) | 布尔 | false |
| `apparelRequirements` | 5.3% (2/38) | 容器 |  |
| `apparelRequirements/li` | 5.3% (2/38) | 容器 |  |
| `apparelRequirements/li/requirement` | 5.3% (2/38) | 容器 |  |
| `apparelRequirements/li/requirement/bodyPartGroupsMatchAny` | 5.3% (2/38) | 容器 |  |
| `apparelRequirements/li/requirement/bodyPartGroupsMatchAny/li` | 5.3% (2/38) | 文本 | UpperHead |
| `apparelRequirements/li/requirement/requiredDefs` | 5.3% (2/38) | 容器 |  |
| `apparelRequirements/li/requirement/requiredDefs/li` | 5.3% (2/38) | 文本 | Apparel_TortureCrown |
| `category` | 15.8% (6/38) | 文本 | Structure |
| `consumableBuildings` | 44.7% (17/38) | 容器 |  |
| `consumableBuildings/li` | 44.7% (17/38) | 文本 | Burnbong / CannibalPlatter / Effigy |
| `defName` | 94.7% (36/38) | 文本 | Bloodfeeding / Inhuman / MaleSupremacy |
| `deityCount` | 23.7% (9/38) | 数值/文本 | 0 / 1 / 1~4 |
| `deityNameMakerOverride` | 5.3% (2/38) | 文本 | NamerDeityChristian / NamerDeityIslamic |
| `deityTypeMakerOverride` | 5.3% (2/38) | 文本 | DietyTypeMakerAbrahamic |
| `description` | 94.7% (36/38) | 文本 | Drinking blood is sacred. Bloodfeeders should be worshipped. / Humanity is a barrier to our connection with th |
| `descriptionMaker` | 89.5% (34/38) | 容器 |  |
| `descriptionMaker/constants` | 23.7% (9/38) | 容器 |  |
| `descriptionMaker/constants/li` | 39.5% (15/38) | 容器 |  |
| `descriptionMaker/constants/li/key` | 39.5% (15/38) | 文本 | structure_animist / structure_theist / structure_theistAbstract |
| `descriptionMaker/constants/li/value` | 39.5% (15/38) | 布尔 | true |
| `descriptionMaker/patterns` | 23.7% (9/38) | 容器 |  |
| `descriptionMaker/patterns/li` | 39.5% (15/38) | 容器 |  |
| `descriptionMaker/patterns/li/def` | 39.5% (15/38) | 文本 | AnimistDescription / IdeologicalLesson / TheistFounder |
| `descriptionMaker/patterns/li/weight` | 5.3% (2/38) | 数值 | 1 / 3 |
| `descriptionMaker/rules` | 65.8% (25/38) | 容器 |  |
| `descriptionMaker/rules/rulesStrings` | 65.8% (25/38) | 容器 |  |
| `descriptionMaker/rules/rulesStrings/li` | 1144.7% (435/38) | 文本 | creation(tag=meme_Bloodfeeding)        ->[deity0_name] drank the blood of the st / episode(uses=1,tag=meme_Blo |
| `disagreeableTraits` | 10.5% (4/38) | 容器 |  |
| `disagreeableTraits/li` | 13.2% (5/38) | 文本 | BodyPurist / Gourmand / Transhumanist |
| `exclusionTags` | 39.5% (15/38) | 容器 |  |
| `exclusionTags/li` | 47.4% (18/38) | 文本 | GenderSupremacy / GroupRelation / Individualism |
| `factionWhitelist` | 5.3% (2/38) | 容器 |  |
| `factionWhitelist/li` | 5.3% (2/38) | 文本 | HoraxCult / TradersGuild |
| `fixedDeityNameTypes` | 2.6% (1/38) | 容器 |  |
| `fixedDeityNameTypes/li` | 84.2% (32/38) | 容器 |  |
| `fixedDeityNameTypes/li/name` | 84.2% (32/38) | 文本 | Aranyani / Durga / Nirrti |
| `fixedDeityNameTypes/li/type` | 84.2% (32/38) | 文本 | Forest God / God of Destruction / God of Night |
| `generalRules` | 94.7% (36/38) | 容器 |  |
| `generalRules/rulesStrings` | 94.7% (36/38) | 容器 |  |
| `generalRules/rulesStrings/li` | 1313.2% (499/38) | 文本 | memeAdjective->dark / memeAdjective->inhuman / memeAdjective->machine |
| `groupDef` | 81.6% (31/38) | 文本 | GenderSupremacy / GroupRelation / Individualism |
| `iconPath` | 94.7% (36/38) | 文本 | UI/Memes/Bloodfeeding / UI/Memes/Inhuman / UI/Memes/Ritualist |
| `impact` | 86.8% (33/38) | 数值 | 0 / 1 / 2 |
| `label` | 94.7% (36/38) | 文本 | bloodfeeding / inhuman / male supremacy |
| `preferredWeaponClasses` | 5.3% (2/38) | 容器 |  |
| `preferredWeaponClasses/despised` | 5.3% (2/38) | 文本 | Neolithic / Ultratech |
| `preferredWeaponClasses/noble` | 5.3% (2/38) | 文本 | Neolithic / Ultratech |
| `preventApparelRequirements` | 2.6% (1/38) | 布尔 | true |
| `randomizationSelectionWeightFactor` | 7.9% (3/38) | 数值 | 2 / 3 / 5 |
| `renderOrder` | 52.6% (20/38) | 数值 | 1100 / 1101 / 80 |
| `replacementPatterns` | 7.9% (3/38) | 容器 |  |
| `replacementPatterns/li` | 10.5% (4/38) | 文本 | SacrificeAnimal / SacrificePrisoner |
| `replaceRitualsWithTags` | 7.9% (3/38) | 容器 |  |
| `replaceRitualsWithTags/li` | 7.9% (3/38) | 文本 | CelebratedDate |
| `requireAnyRitualSeat` | 10.5% (4/38) | 容器 |  |
| `requireAnyRitualSeat/li` | 13.2% (5/38) | 文本 | KneelPillow / KneelSheet / Pew |
| `requiredRituals` | 10.5% (4/38) | 容器 |  |
| `requiredRituals/li` | 10.5% (4/38) | 容器 |  |
| `requiredRituals/li/building` | 5.3% (2/38) | 文本 | Burnbong / ChristmasTree |
| `requiredRituals/li/pattern` | 10.5% (4/38) | 文本 | BlindingCeremony / CelebrationTree / ScarificationCeremony |
| `requiredRituals/li/precept` | 10.5% (4/38) | 文本 | BlindingCeremony / DateRitualConsumable / ScarificationCeremony |
| `requireOne` | 57.9% (22/38) | 容器 |  |
| `requireOne/li` | 186.8% (71/38) | 容器 |  |
| `requireOne/li/li` | 281.6% (107/38) | 文本 | Lovin_Free / Nudity_Female_NoRules / Nudity_Male_NoRules |
| `ritualsToMake` | 7.9% (3/38) | 数值 | 1 |
| `selectOneOrNone` | 13.2% (5/38) | 容器 |  |
| `selectOneOrNone/noneChance` | 13.2% (5/38) | 数值 | 0 / 0.2 / 0.8 |
| `selectOneOrNone/preceptThingPairs` | 13.2% (5/38) | 容器 |  |
| `selectOneOrNone/preceptThingPairs/li` | 18.4% (7/38) | 容器 |  |
| `selectOneOrNone/preceptThingPairs/li/precept` | 18.4% (7/38) | 文本 | ApparelDesired_Soft_Subordinate / ApparelDesired_Strong_Subordinate |
| `selectOneOrNone/preceptThingPairs/li/thing` | 18.4% (7/38) | 文本 | Apparel_Burka / Apparel_Slicecap / Apparel_VisageMask |
| `startingResearchProjects` | 7.9% (3/38) | 容器 |  |
| `startingResearchProjects/li` | 7.9% (3/38) | 文本 | Deathrest / Stonecutting / TreeSowing |
| `styleItemTags` | 34.2% (13/38) | 容器 |  |
| `styleItemTags/li` | 63.2% (24/38) | 容器 |  |
| `styleItemTags/li/baseWeight` | 39.5% (15/38) | 数值 | 0 / 0.05 / 1 |
| `styleItemTags/li/tag` | 63.2% (24/38) | 文本 | Cultist / TattooBodyTribal / TattooFaceTribal |
| `styleItemTags/li/weightFactor` | 63.2% (24/38) | 数值 | 0 / 1 / 1.1 |
| `symbolPackOverride` | 10.5% (4/38) | 布尔 | true |
| `symbolPacks` | 73.7% (28/38) | 容器 |  |
| `symbolPacks/li` | 347.4% (132/38) | 容器 |  |
| `symbolPacks/li/adjective` | 347.4% (132/38) | 文本 | fertilist / manist / masculist |
| `symbolPacks/li/ideoName` | 321.1% (122/38) | 文本 | Fertilism / Manism / Masculinism |
| `symbolPacks/li/member` | 347.4% (132/38) | 文本 | fertilist / manist / masculinist |
| `symbolPacks/li/prefix` | 136.8% (52/38) | 布尔 | true |
| `symbolPacks/li/theme` | 210.5% (80/38) | 文本 | fertility / man / masculinity |
| `thingStyleCategories` | 28.9% (11/38) | 容器 |  |
| `thingStyleCategories/li` | 28.9% (11/38) | 容器 |  |
| `thingStyleCategories/li/category` | 28.9% (11/38) | 文本 | Animalist / Christian / Morbid |
| `thingStyleCategories/li/priority` | 28.9% (11/38) | 数值 | 1 / 3 / 4 |
| `veneratedAnimalsCountOffset` | 5.3% (2/38) | 数值 | 1 |
| `veneratedAnimalsCountOverride` | 5.3% (2/38) | 数值 | 0 |
| `worshipRoomLabel` | 23.7% (9/38) | 文本 | pantheon / sanctuary / shrine |

## 四、原版 defName 一览（共 38 个，列出前 60）

```text
``                                ``                                `Ritualist`                       `Structure_Animist`             
`Structure_Archist`               `Structure_TheistEmbodied`        `Inhuman`                         `MaleSupremacy`                 
`Darkness`                        `Structure_Ideological`           `FemaleSupremacy`                 `Loyalist`                      
`Proselytizer`                    `Structure_TheistAbstract`        `Blindsight`                      `TreeConnection`                
`HumanPrimacy`                    `Individualist`                   `Bloodfeeding`                    `Nudism`                        
`NaturePrimacy`                   `Shipborn`                        `Tunneler`                        `Supremacist`                   
`Collectivist`                    `Raider`                          `Guilty`                          `FleshPurity`                   
`Rancher`                         `HighLife`                        `AnimalPersonhood`                `Cannibal`                      
`Structure_OriginBuddhist`        `Structure_OriginChristian`       `Structure_OriginIslamic`         `Transhumanist`                 
`PainIsVirtue`                    `Structure_OriginHindu`         
```
