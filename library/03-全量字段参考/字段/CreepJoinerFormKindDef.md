# CreepJoinerFormKindDef

- **所属线**：世界线
- **原版实例数**：9
- **字段路径数**：121
- **资料片**：Anomaly
- **原版出处**：`Anomaly/Defs/CreepjoinerDefs/Forms.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<CreepJoinerFormKindDef Abstract="True" Name="BaseCreepJoinerKind" ParentName="BasePlayerPawnKind">
    <race>CreepJoiner</race>
    <canBeScattered>false</canBeScattered>
    <apparelAllowHeadgearChance>0</apparelAllowHeadgearChance>
    <combatPower>55</combatPower>
    <humanPregnancyChance>0</humanPregnancyChance>
    <initialResistanceRange>0~0</initialResistanceRange>
    <invNutrition>10</invNutrition>
    <studiableAsPrisoner>true</studiableAsPrisoner>
    <acceptArrestChanceFactor>0.8</acceptArrestChanceFactor>
    <basePrisonBreakMtbDays>30</basePrisonBreakMtbDays>
    <initialWillRange>80~90</initialWillRange>
    <showInDebugSpawner>false</showInDebugSpawner>
    <apparelIgnoreSeasons>false</apparelIgnoreSeasons>
    <isFighter>false</isFighter>
    <generateInitialNonFamilyRelations>false</generateInitialNonFamilyRelations>
    <fixedChildBackstories>
      <li>UnknownChildhood</li>
    </fixedChildBackstories>
    <fixedAdultBackstories>
      <li>UnknownAdulthood</li>
    </fixedAdultBackstories>
  </CreepJoinerFormKindDef>

  
```

> 来自 `Anomaly/Defs/CreepjoinerDefs/Forms.xml`，defName = ``，XML 节点数 20（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
requires/li                                    [文本]  例：DeathRefusal / Fleshcrafter / Occultist
```

## 三、全量字段表（121 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `acceptArrestChanceFactor` | 11.1% (1/9) | 数值 | 0.8 |
| `apparelAllowHeadgearChance` | 22.2% (2/9) | 数值 | 0 / 0.2 |
| `apparelColor` | 33.3% (3/9) | 文本 | (156,31,56) / (211,211,211) / (58,58,58) |
| `apparelIgnoreSeasons` | 11.1% (1/9) | 布尔 | false |
| `apparelMoney` | 11.1% (1/9) | 文本 | 90~280 |
| `apparelRequired` | 33.3% (3/9) | 容器 |  |
| `apparelRequired/li` | 77.8% (7/9) | 文本 | Apparel_BasicShirt / Apparel_HatTop / Apparel_Jacket |
| `apparelTags` | 44.4% (4/9) | 容器 |  |
| `apparelTags/li` | 44.4% (4/9) | 文本 | IndustrialAdvanced / IndustrialBasic |
| `basePrisonBreakMtbDays` | 11.1% (1/9) | 数值 | 30 |
| `beardTagFilter` | 44.4% (4/9) | 容器 |  |
| `beardTagFilter/tags` | 44.4% (4/9) | 容器 |  |
| `beardTagFilter/tags/li` | 44.4% (4/9) | 文本 | NoBeard |
| `beardTagFilter/whitelist` | 44.4% (4/9) | 布尔 | true |
| `bodyTypeGraphicPaths` | 22.2% (2/9) | 容器 |  |
| `bodyTypeGraphicPaths/Fat` | 22.2% (2/9) | 文本 | Things/Pawn/Humanlike/Bodies/CultEscapee_Fat / Things/Pawn/Humanlike/Bodies/Leathery_Fat |
| `bodyTypeGraphicPaths/Female` | 22.2% (2/9) | 文本 | Things/Pawn/Humanlike/Bodies/CultEscapee_Female / Things/Pawn/Humanlike/Bodies/Leathery_Female |
| `bodyTypeGraphicPaths/Hulk` | 22.2% (2/9) | 文本 | Things/Pawn/Humanlike/Bodies/CultEscapee_Hulk / Things/Pawn/Humanlike/Bodies/Leathery_Hulk |
| `bodyTypeGraphicPaths/Male` | 22.2% (2/9) | 文本 | Things/Pawn/Humanlike/Bodies/CultEscapee_Male / Things/Pawn/Humanlike/Bodies/Leathery_Male |
| `bodyTypeGraphicPaths/Thin` | 22.2% (2/9) | 文本 | Things/Pawn/Humanlike/Bodies/CultEscapee_Thin / Things/Pawn/Humanlike/Bodies/Leathery_Thin |
| `canBeScattered` | 11.1% (1/9) | 布尔 | false |
| `combatPower` | 11.1% (1/9) | 数值 | 55 |
| `defName` | 88.9% (8/9) | 文本 | CreepDrifter / DarkScholar / DealMaker |
| `excludes` | 22.2% (2/9) | 容器 |  |
| `excludes/li` | 44.4% (4/9) | 文本 | Assault / Joybringer / Metalhorror |
| `existingDamage` | 22.2% (2/9) | 容器 |  |
| `existingDamage/li` | 33.3% (3/9) | 容器 |  |
| `existingDamage/li/chance` | 22.2% (2/9) | 数值 | 0.5 |
| `existingDamage/li/damage` | 33.3% (3/9) | 文本 | SurgicalCut |
| `existingDamage/li/groups` | 33.3% (3/9) | 容器 |  |
| `existingDamage/li/groups/li` | 55.6% (5/9) | 文本 | Arms / FullHead / Legs |
| `fixedAdultBackstories` | 11.1% (1/9) | 容器 |  |
| `fixedAdultBackstories/li` | 11.1% (1/9) | 文本 | UnknownAdulthood |
| `fixedChildBackstories` | 11.1% (1/9) | 容器 |  |
| `fixedChildBackstories/li` | 11.1% (1/9) | 文本 | UnknownChildhood |
| `fixedInventory` | 55.6% (5/9) | 容器 |  |
| `fixedInventory/Apparel_BasicShirt` | 33.3% (3/9) | 容器 |  |
| `fixedInventory/Apparel_BasicShirt/quality` | 33.3% (3/9) | 文本 | Poor |
| `fixedInventory/Apparel_BasicShirt/stuff` | 33.3% (3/9) | 文本 | Cloth / Leather_Patch / WoolBison |
| `fixedInventory/Apparel_CollarShirt` | 11.1% (1/9) | 容器 |  |
| `fixedInventory/Apparel_CollarShirt/quality` | 11.1% (1/9) | 文本 | Good |
| `fixedInventory/Apparel_CollarShirt/stuff` | 11.1% (1/9) | 文本 | Cloth |
| `fixedInventory/Apparel_Duster` | 11.1% (1/9) | 容器 |  |
| `fixedInventory/Apparel_Duster/quality` | 11.1% (1/9) | 文本 | Poor |
| `fixedInventory/Apparel_Duster/stuff` | 11.1% (1/9) | 文本 | WoolBison |
| `fixedInventory/Apparel_LabCoat` | 11.1% (1/9) | 容器 |  |
| `fixedInventory/Apparel_LabCoat/color` | 11.1% (1/9) | 文本 | (240, 240, 240) |
| `fixedInventory/Apparel_LabCoat/quality` | 11.1% (1/9) | 文本 | Good |
| `fixedInventory/Apparel_LabCoat/stuff` | 11.1% (1/9) | 文本 | Cloth |
| `fixedInventory/Apparel_Pants` | 44.4% (4/9) | 容器 |  |
| `fixedInventory/Apparel_Pants/quality` | 44.4% (4/9) | 文本 | Good / Poor |
| `fixedInventory/Apparel_Pants/stuff` | 44.4% (4/9) | 文本 | Cloth / Leather_Patch / Synthread |
| `fixedInventory/Apparel_Robe` | 11.1% (1/9) | 容器 |  |
| `fixedInventory/Apparel_Robe/quality` | 11.1% (1/9) | 文本 | Poor |
| `fixedInventory/Apparel_Robe/stuff` | 11.1% (1/9) | 文本 | Cloth |
| `fixedInventory/Gun_BoltActionRifle` | 11.1% (1/9) | 容器 |  |
| `fixedInventory/Gun_ChargeLance` | 11.1% (1/9) | 容器 |  |
| `fixedInventory/Gun_Revolver` | 11.1% (1/9) | 容器 |  |
| `fixedInventory/MeleeWeapon_Knife` | 11.1% (1/9) | 容器 |  |
| `fixedInventory/MeleeWeapon_Knife/quality` | 11.1% (1/9) | 文本 | Poor |
| `fixedInventory/MeleeWeapon_Knife/stuff` | 11.1% (1/9) | 文本 | Steel |
| `forcedHair` | 11.1% (1/9) | 文本 | Bald |
| `forcedHeadTypes` | 44.4% (4/9) | 容器 |  |
| `forcedHeadTypes/li` | 66.7% (6/9) | 文本 | DarkScholar_Female / DarkScholar_Male / Leathery_Female |
| `forcedTraits` | 33.3% (3/9) | 容器 |  |
| `forcedTraits/Abrasive` | 11.1% (1/9) | 容器 |  |
| `forcedTraits/Beauty` | 11.1% (1/9) | 数值 | 2 |
| `forcedTraits/Psychopath` | 11.1% (1/9) | 容器 |  |
| `forcedTraits/TooSmart` | 11.1% (1/9) | 容器 |  |
| `forceNormalGearQuality` | 33.3% (3/9) | 布尔 | false |
| `gearHealthRange` | 11.1% (1/9) | 文本 | 0.2~0.6 |
| `generateInitialNonFamilyRelations` | 11.1% (1/9) | 布尔 | false |
| `hairTagFilter` | 11.1% (1/9) | 容器 |  |
| `hairTagFilter/tags` | 11.1% (1/9) | 容器 |  |
| `hairTagFilter/tags/li` | 11.1% (1/9) | 文本 | Bald |
| `hairTagFilter/whitelist` | 11.1% (1/9) | 布尔 | true |
| `humanPregnancyChance` | 11.1% (1/9) | 数值 | 0 |
| `ignoreIdeoApparelColors` | 33.3% (3/9) | 布尔 | true |
| `initialResistanceRange` | 11.1% (1/9) | 文本 | 0~0 |
| `initialWillRange` | 11.1% (1/9) | 文本 | 80~90 |
| `inventoryOptions` | 11.1% (1/9) | 容器 |  |
| `inventoryOptions/skipChance` | 11.1% (1/9) | 数值 | 0.9 |
| `inventoryOptions/subOptionsChooseOne` | 11.1% (1/9) | 容器 |  |
| `inventoryOptions/subOptionsChooseOne/li` | 11.1% (1/9) | 容器 |  |
| `inventoryOptions/subOptionsChooseOne/li/countRange` | 11.1% (1/9) | 数值 | 1 |
| `inventoryOptions/subOptionsChooseOne/li/thingDef` | 11.1% (1/9) | 文本 | MedicineHerbal |
| `invNutrition` | 22.2% (2/9) | 数值 | 0 / 10 |
| `isFighter` | 11.1% (1/9) | 布尔 | false |
| `itemQuality` | 44.4% (4/9) | 文本 | Good / Poor |
| `label` | 88.9% (8/9) | 文本 | dark scholar / deal maker / drifter |
| `letterLabel` | 88.9% (8/9) | 文本 | A dark scholar covered with twisted scars is approaching the colony. / A ragged stranger with leathery skin is |
| `letterPrompt` | 88.9% (8/9) | 文本 | A stunningly good-looking stranger stands in front of you. {PAWN_possessive} fac / The dark scholar slouches i |
| `maxApparelQuality` | 33.3% (3/9) | 文本 | Good / Poor |
| `maxGenerationAge` | 88.9% (8/9) | 数值 | 40 / 60 / 70 |
| `minApparelQuality` | 33.3% (3/9) | 文本 | Good / Poor |
| `minGenerationAge` | 88.9% (8/9) | 数值 | 20 / 35 / 40 |
| `missingParts` | 22.2% (2/9) | 容器 |  |
| `missingParts/li` | 55.6% (5/9) | 容器 |  |
| `missingParts/li/bodyPart` | 55.6% (5/9) | 文本 | Arm / Eye |
| `missingParts/li/chance` | 33.3% (3/9) | 数值 | 0.5 |
| `race` | 11.1% (1/9) | 文本 | CreepJoiner |
| `requires` | 55.6% (5/9) | 容器 |  |
| `requires/li` | 188.9% (17/9) | 文本 | DeathRefusal / Fleshcrafter / Occultist |
| `showInDebugSpawner` | 11.1% (1/9) | 布尔 | false |
| `skills` | 33.3% (3/9) | 容器 |  |
| `skills/li` | 44.4% (4/9) | 容器 |  |
| `skills/li/range` | 44.4% (4/9) | 文本 | 13~18 / 14~20 |
| `skills/li/skill` | 44.4% (4/9) | 文本 | Intellectual / Shooting / Social |
| `startingHediffs` | 11.1% (1/9) | 容器 |  |
| `startingHediffs/li` | 11.1% (1/9) | 容器 |  |
| `startingHediffs/li/chance` | 11.1% (1/9) | 数值 | 0.5 |
| `startingHediffs/li/def` | 11.1% (1/9) | 文本 | Tentacle |
| `studiableAsPrisoner` | 11.1% (1/9) | 布尔 | true |
| `techHediffsChance` | 11.1% (1/9) | 数值 | 0.15 |
| `techHediffsMoney` | 11.1% (1/9) | 文本 | 50~50 |
| `techHediffsTags` | 11.1% (1/9) | 容器 |  |
| `techHediffsTags/li` | 11.1% (1/9) | 文本 | Poor |
| `weaponMoney` | 11.1% (1/9) | 文本 | 60~200 |
| `weaponTags` | 11.1% (1/9) | 容器 |  |
| `weaponTags/li` | 22.2% (2/9) | 文本 | MedievalMeleeBasic / NeolithicMeleeBasic |
| `weight` | 88.9% (8/9) | 数值 | 1 |

## 四、原版 defName 一览（共 9 个，列出前 60）

```text
``                                `TimelessOne`                     `Blindhealer`                     `CreepDrifter`                  
`LoneGenius`                      `LeatheryStranger`                `DealMaker`                       `DarkScholar`                   
`CultEscapee`                   
```
