# RuleDef

- **所属线**：系统线
- **原版实例数**：112
- **字段路径数**：12
- **资料片**：Anomaly、Biotech、Core、Ideology、Odyssey、Royalty
- **原版出处**：`Anomaly/Defs/RuleDefs/Rules_Complex.xml`、`Ideology/Defs/RuleDefs/Rules_Complex.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<RuleDef>
    <defName>RandomFleshbeastGroup</defName>
    <symbol>randomFleshbeastGroup</symbol>
    <resolvers>
      <li Class="SymbolResolver_RandomFleshbeastGroup"/>
    </resolvers>
  </RuleDef>
```

> 来自 `Anomaly/Defs/RuleDefs/Rules_Complex.xml`，defName = `RandomFleshbeastGroup`，XML 节点数 5（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：AncientComplex_Mechanitor / OutdoorsPath / RandomFleshbeastGroup
resolvers                                      [容器]
resolvers/li                                   [容器]
symbol                                         [文本]  例：ancientMechanitorComplex / outdoorsPath / randomFleshbeastGroup
```

## 三、全量字段表（12 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (112/112) | 文本 | AncientComplex_Mechanitor / OutdoorsPath / RandomFleshbeastGroup |
| `resolvers` | 100.0% (112/112) | 容器 |  |
| `resolvers/li` | 110.7% (124/112) | 容器 |  |
| `resolvers/li/allowRoof` | 0.9% (1/112) | 布尔 | false |
| `resolvers/li/bladelinkChance` | 0.9% (1/112) | 数值 | 0.02 |
| `resolvers/li/interior` | 8.9% (10/112) | 文本 | interior_batteryRoom / interior_brewery / interior_diningRoom |
| `resolvers/li/minRectSize` | 52.7% (59/112) | 文本 | (10, 10) / (18, 18) / (3, 3) |
| `resolvers/li/psychicChance` | 0.9% (1/112) | 数值 | 0.02 |
| `resolvers/li/selectionWeight` | 7.1% (8/112) | 数值 | 0.3 / 0.65 / 0.75 |
| `resolvers/li/techprintChance` | 0.9% (1/112) | 数值 | 0.033 |
| `resolvers/li/useRandomCarpet` | 0.9% (1/112) | 布尔 | true |
| `symbol` | 100.0% (112/112) | 文本 | ancientMechanitorComplex / outdoorsPath / randomFleshbeastGroup |

## 四、原版 defName 一览（共 112 个，列出前 60）

```text
`RandomFleshbeastGroup`           `Unpollute`                       `BasePart`                        `BasePart_Outdoors`             
`BasePart_Outdoors_LeafPossiblyDecorated`  `Clear`                           `SingleThing`                     `SinglePawn`                    
`Filth`                           `FloorFill`                       `RemoveDangerousTerrain`          `Roof`                          
`OutdoorsCampfire`                `FirefoamPopper`                  `PawnGroup`                       `ThingSet`                      
`LootScatter`                     `Doors`                           `ExtraDoor`                       `EdgeSandbags`                  
`EdgeWalls`                       `EdgeFloor`                       `AncientCryptosleepCasket`        `EdgeThing`                     
`CultivatedPlants`                `Bed`                             `PrisonerBed`                     `SoundOneShotAction`            
`UnfoggedTrigger`                 `ContainerEmptiedTrigger`         `OpenDoorAction`                  `RandomMechanoidGroup`          
`FillWithBeds`                    `Stockpile`                       `Farm`                            `FillWithThings`                
`Refuel`                          `ChargeBatteries`                 `PlaceChairsNearTables`           `RandomlyPlaceMealsOnTables`    
`AddWortToFermentingBarrels`      `Street`                          `EdgeStreet`                      `IndoorLighting`                
`OutdoorLighting`                 `InnerStockpile`                  `Message`                         `SleepingMechanoids`            
`Interior_Storage`                `Interior_Barracks`               `Interior_PrisonCell`             `Ship_Core`                     
`Ship_Pregen`                     `Ship_Spine`                      `Ship_Populate`                   `Ambush`                        
`AncientAltar`                    `DesiccatedCorpses`               `ArchonexusResearchBuildings`     `LandingPad`                    
```

_余下 52 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
