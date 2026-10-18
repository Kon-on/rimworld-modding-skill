# ThingCategoryDef

- **所属线**：物品线
- **原版实例数**：78
- **字段路径数**：5
- **资料片**：Anomaly、Core、Odyssey
- **原版出处**：`Core/Defs/ThingCategoryDefs/ThingCategories.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<ThingCategoryDef>
    <defName>Root</defName>
    <label>root</label>
  </ThingCategoryDef>

  
```

> 来自 `Core/Defs/ThingCategoryDefs/ThingCategories.xml`，defName = `Root`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：BodyPartsGhoul / CorpsesEntity / Foods
label                                          [文本]  例：entity corpses / foods / ghoul
parent                                         [文本]  例：BodyParts / Corpses / Foods
```

## 三、全量字段表（5 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (78/78) | 文本 | BodyPartsGhoul / CorpsesEntity / Foods |
| `iconPath` | 25.6% (20/78) | 文本 | UI/Icons/ThingCategories/FoodMeals / UI/Icons/ThingCategories/FoodRaw / UI/Icons/ThingCategories/Foods |
| `label` | 100.0% (78/78) | 文本 | entity corpses / foods / ghoul |
| `parent` | 97.4% (76/78) | 文本 | BodyParts / Corpses / Foods |
| `resourceReadoutRoot` | 14.1% (11/78) | 布尔 | true |

## 四、原版 defName 一览（共 78 个，列出前 60）

```text
`Root`                            `BookEffects`                     `CorpsesEntity`                   `BodyPartsGhoul`                
`Items`                           `Unfinished`                      `Artifacts`                       `InertRelics`                   
`Neurotrainers`                   `NeurotrainersPsycast`            `NeurotrainersSkill`              `Techprints`                    
`BodyParts`                       `BodyPartsNatural`                `BodyPartsSimple`                 `BodyPartsProsthetic`           
`BodyPartsBionic`                 `BodyPartsUltra`                  `BodyPartsArchotech`              `BodyPartsMechtech`             
`Books`                           `ItemsMisc`                       `Weapons`                         `WeaponsMelee`                  
`WeaponsMeleeBladelink`           `WeaponsRanged`                   `WeaponsUnique`                   `Grenades`                      
`Apparel`                         `Headgear`                        `ApparelArmor`                    `ArmorHeadgear`                 
`ApparelUtility`                  `ApparelNoble`                    `HeadgearNoble`                   `ApparelMisc`                   
`Buildings`                       `BuildingsArt`                    `BuildingsProduction`             `BuildingsFurniture`            
`BuildingsPower`                  `BuildingsSecurity`               `BuildingsMisc`                   `BuildingsJoy`                  
`BuildingsTemperature`            `BuildingsSpecial`                `Chunks`                          `Animals`                       
`Plants`                          `Stumps`                          `Corpses`                         `CorpsesHumanlike`              
`CorpsesAnimal`                   `CorpsesInsect`                   `CorpsesMechanoid`                `SkillGain`                     
`ResearchGain`                    `CorpsesDrone`                    `MeatRaw`                         `PlantFoodRaw`                  
```

_余下 18 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
