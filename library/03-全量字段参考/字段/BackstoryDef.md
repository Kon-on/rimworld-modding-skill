# BackstoryDef

- **所属线**：人物线
- **原版实例数**：845
- **字段路径数**：132
- **资料片**：Anomaly、Core、Royalty
- **原版出处**：`Anomaly/Defs/BackstoryDefs/Solid/Solid.xml`、`Core/Defs/BackstoryDefs/Solid/Solid_Child.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<BackstoryDef>
    <defName>UnknownChildhood</defName>
    <title>unknown</title>
    <titleShort>unknown</titleShort>
    <description>[PAWN_nameDef]'s origins are unknown.</description>
    <shuffleable>false</shuffleable>
  </BackstoryDef>
  
  
```

> 来自 `Anomaly/Defs/BackstoryDefs/Solid/Solid.xml`，defName = `UnknownChildhood`，XML 节点数 6（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：NavyScientist52 / SewerKid57 / UnknownAdulthood
description                                    [文本]  例：Interstellar warfare is won by technology, so glitterworld navies are always at  / [PAWN_nameDef] found it easy to relate to others and mediate conflict. [PAWN_pro / [PAWN_nameDef] grew up in the sludge-smeared sewers of a polluted industrial wor
skillGains                                     [容器]
slot                                           [文本]  例：Adulthood / Childhood
spawnCategories/li                             [文本]  例：InsectsRelated / Offworld / Researcher
title                                          [文本]  例：glitterworld empath / navy scientist / sewer kid
titleShort                                     [文本]  例：empath / scientist / sewer boy
```

## 三、全量字段表（132 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `bodyTypeFemale` | 55.1% (466/845) | 文本 | Female / Hulk / Male |
| `bodyTypeGlobal` | 36.1% (305/845) | 文本 | Fat / Female / Male |
| `bodyTypeMale` | 55.1% (466/845) | 文本 | Fat / Hulk / Male |
| `defName` | 100.0% (845/845) | 文本 | NavyScientist52 / SewerKid57 / UnknownAdulthood |
| `description` | 100.0% (845/845) | 文本 | Interstellar warfare is won by technology, so glitterworld navies are always at  / [PAWN_nameDef] found it eas |
| `disallowedTraits` | 0.6% (5/845) | 容器 |  |
| `disallowedTraits/Gay` | 0.1% (1/845) | 数值 | 0 |
| `disallowedTraits/Psychopath` | 0.2% (2/845) | 容器/数值 | 0 |
| `disallowedTraits/Pyromaniac` | 0.1% (1/845) | 容器 |  |
| `disallowedTraits/ShootingAccuracy` | 0.1% (1/845) | 数值 | -1 |
| `forcedTraits` | 17.6% (149/845) | 容器 |  |
| `forcedTraits/Abrasive` | 0.5% (4/845) | 数值 | 0 |
| `forcedTraits/AnnoyingVoice` | 0.1% (1/845) | 数值 | 0 |
| `forcedTraits/Ascetic` | 0.5% (4/845) | 数值 | 0 |
| `forcedTraits/Beauty` | 1.5% (13/845) | 数值 | -1 / 1 / 2 |
| `forcedTraits/Bisexual` | 0.1% (1/845) | 容器 |  |
| `forcedTraits/Bloodlust` | 0.6% (5/845) | 数值 | 0 |
| `forcedTraits/BodyPurist` | 0.2% (2/845) | 数值 | 0 |
| `forcedTraits/Brawler` | 0.5% (4/845) | 数值 | 0 |
| `forcedTraits/DislikesMen` | 0.1% (1/845) | 数值 | 0 |
| `forcedTraits/DrugDesire` | 0.7% (6/845) | 数值 | -1 / 1 / 2 |
| `forcedTraits/FastLearner` | 0.5% (4/845) | 数值 | 0 |
| `forcedTraits/Gay` | 0.1% (1/845) | 容器 |  |
| `forcedTraits/Gourmand` | 0.4% (3/845) | 数值 | 0 |
| `forcedTraits/Greedy` | 0.8% (7/845) | 数值 | 0 |
| `forcedTraits/Immunity` | 0.2% (2/845) | 数值 | -1 |
| `forcedTraits/Industriousness` | 2.0% (17/845) | 数值 | -1 / -2 / 1 |
| `forcedTraits/Kind` | 0.7% (6/845) | 容器/数值 | 0 |
| `forcedTraits/NaturalMood` | 0.4% (3/845) | 数值 | 1 |
| `forcedTraits/Nerves` | 0.7% (6/845) | 数值 | -1 / -2 / 1 |
| `forcedTraits/Neurotic` | 0.4% (3/845) | 数值 | 1 / 2 |
| `forcedTraits/Nimble` | 0.6% (5/845) | 数值 | 0 |
| `forcedTraits/PsychicSensitivity` | 0.2% (2/845) | 数值 | 1 / 2 |
| `forcedTraits/Psychopath` | 2.4% (20/845) | 容器/数值 | 0 |
| `forcedTraits/Pyromaniac` | 0.4% (3/845) | 容器/数值 | 0 |
| `forcedTraits/QuickSleeper` | 0.2% (2/845) | 数值 | 0 |
| `forcedTraits/ShootingAccuracy` | 0.6% (5/845) | 数值 | -1 / 1 |
| `forcedTraits/SpeedOffset` | 0.4% (3/845) | 数值 | 2 |
| `forcedTraits/TooSmart` | 0.5% (4/845) | 数值 | 0 |
| `forcedTraits/TorturedArtist` | 0.1% (1/845) | 容器 |  |
| `forcedTraits/Tough` | 0.6% (5/845) | 数值 | 0 |
| `forcedTraits/Transhumanist` | 0.1% (1/845) | 数值 | 0 |
| `forcedTraits/Undergrounder` | 1.5% (13/845) | 数值 | 0 |
| `forcedTraits/Wimp` | 0.1% (1/845) | 数值 | 0 |
| `identifier` | 71.0% (600/845) | 文本 | ArmyCook0 / CivilEngineer2 / MadScientist22 |
| `ignoreIllegalLabelCharacterConfigError` | 35.4% (299/845) | 布尔 | False |
| `possessions` | 11.4% (96/845) | 容器 |  |
| `possessions/AestheticNose` | 0.2% (2/845) | 数值 | 1 |
| `possessions/AncientMiningCharge` | 0.1% (1/845) | 数值 | 1 |
| `possessions/Apparel_Cape` | 0.2% (2/845) | 数值 | 1 |
| `possessions/Apparel_CeremonialCultistMask` | 0.1% (1/845) | 数值 | 1 |
| `possessions/Apparel_CowboyHat` | 0.1% (1/845) | 数值 | 1 |
| `possessions/Apparel_CultistMask` | 0.1% (1/845) | 数值 | 1 |
| `possessions/Apparel_Duster` | 0.1% (1/845) | 数值 | 1 |
| `possessions/Apparel_GasMask` | 0.1% (1/845) | 数值 | 1 |
| `possessions/Apparel_PackTurret` | 0.2% (2/845) | 数值 | 1 |
| `possessions/Beer` | 0.2% (2/845) | 数值 | 1 / 6 |
| `possessions/BlocksMarble` | 0.1% (1/845) | 数值 | 10 |
| `possessions/BlocksVacstone` | 0.1% (1/845) | 数值 | 20 |
| `possessions/Bow_Short` | 0.1% (1/845) | 数值 | 1 |
| `possessions/Cloth` | 0.1% (1/845) | 数值 | 10 |
| `possessions/ComponentIndustrial` | 0.1% (1/845) | 数值 | 3 |
| `possessions/Drum` | 0.1% (1/845) | 数值 | 1 |
| `possessions/EggCobraFertilized` | 0.1% (1/845) | 数值 | 1 |
| `possessions/Flake` | 0.1% (1/845) | 数值 | 20 |
| `possessions/GameOfUrBoard` | 0.2% (2/845) | 数值 | 1 |
| `possessions/Gold` | 0.1% (1/845) | 数值 | 5 |
| `possessions/Gun_Autopistol` | 0.1% (1/845) | 数值 | 1 |
| `possessions/Gun_Revolver` | 0.1% (1/845) | 数值 | 1 |
| `possessions/Gun_SniperRifle` | 0.4% (3/845) | 数值 | 1 |
| `possessions/Hay` | 0.2% (2/845) | 数值 | 10 |
| `possessions/Heart` | 0.1% (1/845) | 数值 | 1 |
| `possessions/InsectJelly` | 0.1% (1/845) | 数值 | 5 |
| `possessions/Jade` | 0.4% (3/845) | 数值 | 2 / 3 |
| `possessions/Kibble` | 0.2% (2/845) | 数值 | 10 / 3 |
| `possessions/Kidney` | 0.2% (2/845) | 数值 | 1 |
| `possessions/Leather_Bear` | 0.1% (1/845) | 数值 | 10 |
| `possessions/Map` | 0.1% (1/845) | 数值 | 1 |
| `possessions/MealFine` | 0.1% (1/845) | 数值 | 3 |
| `possessions/MealLavish` | 0.4% (3/845) | 数值 | 1 / 2 |
| `possessions/MealNutrientPaste` | 0.1% (1/845) | 数值 | 4 |
| `possessions/MealSurvivalPack` | 0.2% (2/845) | 数值 | 2 / 3 |
| `possessions/Meat_Bison` | 0.1% (1/845) | 数值 | 5 |
| `possessions/Meat_Pig` | 0.1% (1/845) | 数值 | 5 |
| `possessions/Meat_Thrumbo` | 0.1% (1/845) | 数值 | 10 |
| `possessions/MedicineHerbal` | 0.2% (2/845) | 数值 | 5 |
| `possessions/MedicineIndustrial` | 0.4% (3/845) | 数值 | 3 / 4 |
| `possessions/MedicineUltratech` | 0.2% (2/845) | 数值 | 2 |
| `possessions/MeleeWeapon_LongSword` | 0.1% (1/845) | 数值 | 1 |
| `possessions/MeleeWeapon_Spear` | 0.1% (1/845) | 数值 | 1 |
| `possessions/Milk` | 0.1% (1/845) | 数值 | 3 |
| `possessions/NerveSpiker` | 0.1% (1/845) | 数值 | 1 |
| `possessions/Novel` | 0.7% (6/845) | 数值 | 1 |
| `possessions/Penoxycyline` | 0.1% (1/845) | 数值 | 10 |
| `possessions/Pila` | 0.2% (2/845) | 数值 | 1 |
| `possessions/PilotAssistant` | 0.1% (1/845) | 数值 | 1 |
| `possessions/PlantPot` | 0.1% (1/845) | 数值 | 1 |
| `possessions/Plasteel` | 0.1% (1/845) | 数值 | 5 |
| `possessions/PsychiteTea` | 0.1% (1/845) | 数值 | 3 |
| `possessions/Schematic` | 0.2% (2/845) | 数值 | 1 |
| `possessions/SentienceCatalyst` | 0.1% (1/845) | 数值 | 1 |
| `possessions/SunLamp` | 0.1% (1/845) | 数值 | 1 |
| `possessions/TextBook` | 1.2% (10/845) | 数值 | 1 |
| `possessions/ThrumboHorn` | 0.1% (1/845) | 数值 | 1 |
| `possessions/WoodLog` | 0.4% (3/845) | 数值 | 1 / 10 |
| `possessions/WoolMuffalo` | 0.1% (1/845) | 数值 | 4 |
| `requiredWorkTags` | 88.3% (746/845) | 文本 | None |
| `requiredWorkTags/li` | 23.5% (199/845) | 文本 | Artistic / Caring / Intellectual |
| `requiresSpawnCategory` | 0.9% (8/845) | 布尔 | true |
| `shuffleable` | 71.2% (602/845) | 布尔 | False / false |
| `skillGains` | 98.8% (835/845) | 容器 |  |
| `skillGains/Animals` | 8.2% (69/845) | 数值 | 3 / 4 / 6 |
| `skillGains/Artistic` | 18.1% (153/845) | 数值 | 4 / 5 / 7 |
| `skillGains/Construction` | 23.9% (202/845) | 数值 | -4 / -5 / 3 |
| `skillGains/Cooking` | 14.7% (124/845) | 数值 | 2 / 3 / 6 |
| `skillGains/Crafting` | 27.1% (229/845) | 数值 | -3 / -4 / 2 |
| `skillGains/Intellectual` | 35.0% (296/845) | 数值 | -3 / 2 / 3 |
| `skillGains/Medicine` | 23.8% (201/845) | 数值 | 1 / 2 / 3 |
| `skillGains/Melee` | 38.8% (328/845) | 数值 | 2 / 4 / 5 |
| `skillGains/Mining` | 13.2% (112/845) | 数值 | -3 / -5 / 3 |
| `skillGains/Plants` | 16.1% (136/845) | 数值 | -4 / 4 / 6 |
| `skillGains/Shooting` | 39.5% (334/845) | 数值 | -4 / -5 / 4 |
| `skillGains/Social` | 42.5% (359/845) | 数值 | 1 / 6 / 7 |
| `slot` | 97.9% (827/845) | 文本 | Adulthood / Childhood |
| `spawnCategories` | 68.8% (581/845) | 容器 |  |
| `spawnCategories/li` | 143.6% (1213/845) | 文本 | InsectsRelated / Offworld / Researcher |
| `title` | 100.0% (845/845) | 文本 | glitterworld empath / navy scientist / sewer kid |
| `titleFemale` | 1.5% (13/845) | 文本 | housewife / medieval lady / policewoman |
| `titleShort` | 100.0% (845/845) | 文本 | empath / scientist / sewer boy |
| `titleShortFemale` | 1.7% (14/845) | 文本 | housewife / lady / policewoman |
| `workDisables` | 81.3% (687/845) | 文本 | Caring, Social, Firefighting / Hauling, Mining / ManualDumb, Crafting |
| `workDisables/li` | 15.7% (133/845) | 文本 | Crafting / ManualDumb / Social |

## 四、原版 defName 一览（共 845 个，列出前 60）

```text
`UnknownChildhood`                `LiamCustomChildhood`             `TynanCustomChildhood`            `MateCustomChildhood`           
`UnknownAdulthood`                `Newborn79`                       `Child27`                         `VatgrownChild11`               
`JoeCustomChildhood`              `ChildTribal`                     `ColonyChild59`                   `TribeChild19`                  
`BuddingArtist44`                 `CynapseCustomChildhood`          `OskarCustomChildhood`            `WillCustomChildhood`           
`WillCustomAdulthood`             `FeyCustomChildhood`              `Colonist97`                      `TribeMember57`                 
`FireKeeper44`                    `CrashBaby32`                     `JoeCustomAdulthood`              `SewerKid57`                    
`Herder19`                        `IndustrialOrphan13`              `UrbworldUrchin61`                `TribeChild40`                  
`Scavenger22`                     `CaveChild30`                     `Bully70`                         `VoyagerChild94`                
`StreetChild4`                    `PrivilegedChild86`               `Orphan25`                        `ShootingComa59`                
`ReEducatedYouth23`               `HelpDeskWorker31`                `RebelWriter82`                   `SpoiledBrat59`                 
`AngryStudent88`                  `NathanCustomChildhood`           `RichKid61`                       `Regent9`                       
`UrbanLordling82`                 `PamperedLordling37`              `WreckageExplorer93`              `ApocalypseSurvivor23`          
`IllegalShipwright76`             `MuffaloShaman95`                 `ReclusiveChild81`                `VengefulChild43`               
`Hideaway7`                       `VatgrownMedic53`                 `StreetKid19`                     `FrontierMarshal54`             
`MidworldGeek18`                  `CatHerder4`                      `HackerProdigy84`                 `UrbworldUrchin90`              
```

_余下 785 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
