# ResearchProjectDef

- **所属线**：系统线
- **原版实例数**：168
- **字段路径数**：43
- **资料片**：Anomaly、Biotech、Core、Ideology、Odyssey、Royalty
- **原版出处**：`Biotech/Defs/ResearchProjectDefs/ResearchProjects_Mechanitor.xml`、`Core/Defs/ResearchProjectDefs/ResearchProjects_2_Electricity.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<ResearchProjectDef Abstract="True" Name="MechtechBase">
    <techLevel>Industrial</techLevel>
    <requiresMechanitor>true</requiresMechanitor>
  </ResearchProjectDef>

  
```

> 来自 `Biotech/Defs/ResearchProjectDefs/ResearchProjects_Mechanitor.xml`，defName = ``，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：BioferriteExtraction / BioferriteHarvesting / BioferriteIgnition
description                                    [文本]  例：Build bioferrite harvesters that automatically extract bioferrite from captured  / Create advanced weapons that use bioferrite as a fuel source. / Extract bioferrite directly from captured entities. Use it to craft weapons and 
generalRules                                   [容器]
generalRules/rulesStrings                      [容器]
generalRules/rulesStrings/li                   [文本]  例：subject->bioferrite extraction / subject_story->extracted an organic compound from a rapidly mutating flesh sampl / subject_story->investigated reports of an archotech phenomenon
label                                          [文本]  例：bioferrite extraction / bioferrite harvester / bioferrite shaping
prerequisites/li                               [文本]  例：BioferriteExtraction / BioferriteShaping / Electricity
researchViewX                                  [数值]  例：0.00 / 1.00 / 3.00
researchViewY                                  [数值]  例：3.40 / 4.00 / 5.10
```

## 三、全量字段表（43 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `baseCost` | 67.9% (114/168) | 数值 | 1000 / 1400 / 200 |
| `customUnlockTexts` | 0.6% (1/168) | 容器 |  |
| `customUnlockTexts/li` | 0.6% (1/168) | 文本 | Fishing zone |
| `defName` | 97.6% (164/168) | 文本 | BioferriteExtraction / BioferriteHarvesting / BioferriteIgnition |
| `description` | 97.6% (164/168) | 文本 | Build bioferrite harvesters that automatically extract bioferrite from captured  / Create advanced weapons tha |
| `discoveredLetterDisabledWhen` | 0.6% (1/168) | 容器 |  |
| `discoveredLetterDisabledWhen/bigThreatsDisabled` | 0.6% (1/168) | 布尔 | true |
| `discoveredLetterText` | 2.4% (4/168) | 文本 | Escaping from this planet - it would be freedom at last, and maybe a return home / You now have the technology |
| `discoveredLetterTitle` | 2.4% (4/168) | 文本 | About: Electricity / About: Getting advanced components / About: Getting vacstone |
| `generalRules` | 97.6% (164/168) | 容器 |  |
| `generalRules/rulesStrings` | 97.6% (164/168) | 容器 |  |
| `generalRules/rulesStrings/li` | 578.6% (972/168) | 文本 | subject->bioferrite extraction / subject_story->extracted an organic compound from a rapidly mutating flesh sa |
| `heldByFactionCategoryTags` | 2.4% (4/168) | 容器 |  |
| `heldByFactionCategoryTags/li` | 2.4% (4/168) | 文本 | Empire / Outlander |
| `hiddenPrerequisites` | 19.6% (33/168) | 容器 |  |
| `hiddenPrerequisites/li` | 22.0% (37/168) | 文本 | Batteries / ComplexFurniture / GunTurrets |
| `hideWhen` | 4.8% (8/168) | 容器 |  |
| `hideWhen/mortarsDisabled` | 0.6% (1/168) | 布尔 | true |
| `hideWhen/trapsDisabled` | 0.6% (1/168) | 布尔 | true |
| `hideWhen/turretsDisabled` | 3.6% (6/168) | 布尔 | true |
| `knowledgeCategory` | 23.8% (40/168) | 文本 | Advanced / Basic |
| `knowledgeCost` | 23.8% (40/168) | 数值 | 10 / 20 / 5 |
| `label` | 97.6% (164/168) | 文本 | bioferrite extraction / bioferrite harvester / bioferrite shaping |
| `prerequisites` | 86.9% (146/168) | 容器 |  |
| `prerequisites/li` | 102.4% (172/168) | 文本 | BioferriteExtraction / BioferriteShaping / Electricity |
| `recalculatePower` | 0.6% (1/168) | 布尔 | true |
| `requiredAnalyzed` | 2.4% (4/168) | 容器 |  |
| `requiredAnalyzed/li` | 2.4% (4/168) | 文本 | NanostructuringChip / PowerfocusChip / SignalChip |
| `requiredResearchBuilding` | 28.6% (48/168) | 文本 | HiTechResearchBench |
| `requiredResearchFacilities` | 13.7% (23/168) | 容器 |  |
| `requiredResearchFacilities/li` | 13.7% (23/168) | 文本 | MultiAnalyzer |
| `requireGravEngineInspected` | 0.6% (1/168) | 布尔 | true |
| `requiresMechanitor` | 0.6% (1/168) | 布尔 | true |
| `researchViewX` | 97.6% (164/168) | 数值 | 0.00 / 1.00 / 3.00 |
| `researchViewY` | 97.6% (164/168) | 数值 | 3.40 / 4.00 / 5.10 |
| `tab` | 23.8% (40/168) | 文本 | Anomaly |
| `tags` | 7.7% (13/168) | 容器 |  |
| `tags/li` | 8.3% (14/168) | 文本 | ClassicStart / ShipRelated / TribalStart |
| `teachConcept` | 1.2% (2/168) | 文本 | Fishing / VoidProvocation |
| `techLevel` | 67.3% (113/168) | 文本 | Industrial / Neolithic / Spacer |
| `techprintCommonality` | 1.8% (3/168) | 数值 | 1 / 2 / 3 |
| `techprintCount` | 1.8% (3/168) | 数值 | 1 / 2 |
| `techprintMarketValue` | 4.2% (7/168) | 数值 | 1000 / 1500 / 2000 |

## 四、原版 defName 一览（共 168 个，列出前 60）

```text
``                                ``                                ``                                ``                              
`HeavyBridges`                    `Smithing`                        `Devilstrand`                     `CarpetMaking`                  
`Brewing`                         `BasicGravtech`                   `HunterDrones`                    `VenomSynthesis`                
`BioferriteExtraction`            `ToxifierGenerator`               `PsychoidBrewing`                 `TreeSowing`                    
`ComplexFurniture`                `ComplexClothing`                 `DrugProduction`                  `Pemmican`                      
`PsychiteRefining`                `WakeUpProduction`                `GoJuiceProduction`               `PenoxycylineProduction`        
`LongBlades`                      `Greatbow`                        `Batteries`                       `BiofuelRefining`               
`WatermillGenerator`              `Prosthetics`                     `MicroelectronicsBasics`          `ShipReactor`                   
`SkinHardening`                   `HealingFactors`                  `FleshShaping`                    `MolecularAnalysis`             
`CircadianInfluence`              `GhoulEnhancements`               `SecurityDoor`                    `BasicMechtech`                 
`Xenogermination`                 `Deathrest`                       `FertilityProcedures`             `ToxGas`                        
`Stonecutting`                    `RecurveBow`                      `PlateArmor`                      `SolarPanels`                   
`Autodoors`                       `Hydroponics`                     `PackagedSurvivalMeal`            `GeothermalPower`               
`SterileMaterials`                `ColoredLights`                   `Gunsmithing`                     `BlowbackOperation`             
`GasOperation`                    `DeepDrilling`                    `ShipEngine`                      `Fishing`                       
```

_余下 108 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
