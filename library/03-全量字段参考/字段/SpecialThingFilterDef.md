# SpecialThingFilterDef

- **所属线**：物品线
- **原版实例数**：49
- **字段路径数**：8
- **资料片**：Anomaly、Biotech、Core、Ideology
- **原版出处**：`Core/Defs/Misc/SpecialThingFilterDefs/SpecialThingFilters.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<SpecialThingFilterDef Abstract="True" Name="BaseBookResearchFilter">
    <parentCategory>ResearchGain</parentCategory>
    <allowedByDefault>true</allowedByDefault>
  </SpecialThingFilterDef>
  
  
```

> 来自 `Core/Defs/Misc/SpecialThingFilterDefs/SpecialThingFilters.xml`，defName = ``，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：AllowAnomalyResearch / AllowCorpsesMechEnemy / AllowCorpsesMechFriendly
label                                          [文本]  例：allow enemy mech corpses / allow friendly mech corpses / allow unnatural corpses
saveKey                                        [文本]  例：allowAnomalyResearch / allowCorpsesMechEnemy / allowCorpsesMechFriendly
workerClass                                    [文本]  例：SpecialThingFilterWorker_AllowAnomalyResearch / SpecialThingFilterWorker_CorpsesEnemy / SpecialThingFilterWorker_CorpsesFriendly
```

## 三、全量字段表（8 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `allowedByDefault` | 71.4% (35/49) | 布尔 | false / true |
| `configurable` | 8.2% (4/49) | 布尔 | false / true |
| `defName` | 95.9% (47/49) | 文本 | AllowAnomalyResearch / AllowCorpsesMechEnemy / AllowCorpsesMechFriendly |
| `description` | 71.4% (35/49) | 文本 | Allow books with information that advances anomaly research. / Allow strange and unnatural dead bodies. / Allo |
| `label` | 95.9% (47/49) | 文本 | allow enemy mech corpses / allow friendly mech corpses / allow unnatural corpses |
| `parentCategory` | 71.4% (35/49) | 文本 | Corpses / CorpsesHumanlike / CorpsesMechanoid |
| `saveKey` | 95.9% (47/49) | 文本 | allowAnomalyResearch / allowCorpsesMechEnemy / allowCorpsesMechFriendly |
| `workerClass` | 95.9% (47/49) | 文本 | SpecialThingFilterWorker_AllowAnomalyResearch / SpecialThingFilterWorker_CorpsesEnemy / SpecialThingFilterWork |

## 四、原版 defName 一览（共 49 个，列出前 60）

```text
``                                ``                                `AllowAnomalyResearch`            `AllowMainResearch`             
`AllowBookShooting`               `AllowBookMelee`                  `AllowBookConstruction`           `AllowBookMining`               
`AllowBookCooking`                `AllowBookPlants`                 `AllowBookAnimals`                `AllowBookCrafting`             
`AllowBookArtistic`               `AllowBookMedicine`               `AllowBookSocial`                 `AllowBookIntellectual`         
`AllowSmeltableApparel`           `AllowNonSmeltableApparel`        `AllowBurnableApparel`            `AllowNonBurnableApparel`       
`AllowNonSmeltableWeapons`        `AllowNonBurnableWeapons`         `AllowBurnableWeapons`            `AllowBiocodedWeapons`          
`AllowNonBiocodedWeapons`         `AllowBiocodedApparel`            `AllowNonBiocodedApparel`         `AllowCorpsesUnnatural`         
`AllowCorpsesMechFriendly`        `AllowCorpsesMechEnemy`           `AllowCorpsesColonist`            `AllowCorpsesStranger`          
`AllowRotten`                     `AllowFresh`                      `AllowSmeltable`                  `AllowUnfinished`               
`AllowNonDeadmansApparel`         `AllowDeadmansApparel`            `AllowFemaleGender`               `AllowMaleGender`               
`AllowCorpsesSlave`               `AllowVegetarian`                 `AllowCarnivore`                  `AllowCannibal`                 
`AllowInsectMeat`                 `AllowLargeCorpses`               `AllowPlantFood`                  `AllowChildOnlyApparel`         
`AllowAdultOnlyApparel`         
```
