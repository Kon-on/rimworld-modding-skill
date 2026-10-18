# ScenPartDef

- **所属线**：世界线
- **原版实例数**：41
- **字段路径数**：17
- **资料片**：Anomaly、Biotech、Core、Odyssey
- **原版出处**：`Core/Defs/Scenarios/ScenParts_Various.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<ScenPartDef ParentName="DisallowDesignatorBase">
    <defName>Rule_DisallowDesignator_ZoneAdd_Growing</defName>
    <label>cannot sow</label>
    <description>Cannot sow plants on the ground.</description>
    <designatorType>Designator_ZoneAdd_Growing</designatorType>
  </ScenPartDef>

  
```

> 来自 `Core/Defs/Scenarios/ScenParts_Various.xml`，defName = `Rule_DisallowDesignator_ZoneAdd_Growing`，XML 节点数 5（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：AutoActivateMonolith / ConfigurePawnsMutants / ScenPart_MonolithGeneration
label                                          [文本]  例：automatically activate monolith / start with mechanoid / starting people
scenPartClass                                  [文本]  例：ScenPart_AutoActivateMonolith / ScenPart_ConfigPage_ConfigureStartingPawns_Mutants / ScenPart_MonolithGeneration
```

## 三、全量字段表（17 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `canBePlayerAddedRemoved` | 7.3% (3/41) | 布尔 | false |
| `canBeRandomlyAdded` | 7.3% (3/41) | 布尔 | false |
| `category` | 87.8% (36/41) | 文本 | Fixed / Misc / Rule |
| `defName` | 97.6% (40/41) | 文本 | AutoActivateMonolith / ConfigurePawnsMutants / ScenPart_MonolithGeneration |
| `description` | 9.8% (4/41) | 文本 | Cannot hunt. / Cannot mine. / Cannot sow plants on the ground. |
| `designatorType` | 9.8% (4/41) | 文本 | Designator_Hunt / Designator_Mine / Designator_Tame |
| `durationRandomRange` | 2.4% (1/41) | 文本 | 90~500 |
| `gameCondition` | 2.4% (1/41) | 文本 | Planetkiller |
| `gameConditionTargetsWorld` | 2.4% (1/41) | 布尔 | true |
| `genStep` | 4.9% (2/41) | 文本 | AncientExostriderRemains / VoidMonolith |
| `label` | 97.6% (40/41) | 文本 | automatically activate monolith / start with mechanoid / starting people |
| `maxUses` | 24.4% (10/41) | 数值 | 1 |
| `pageClass` | 9.8% (4/41) | 文本 | Page_ConfigureStartingPawns |
| `preventRemovalOfFaction` | 2.4% (1/41) | 文本 | Mechanoid |
| `scenPartClass` | 90.2% (37/41) | 文本 | ScenPart_AutoActivateMonolith / ScenPart_ConfigPage_ConfigureStartingPawns_Mutants / ScenPart_MonolithGenerati |
| `selectionWeight` | 68.3% (28/41) | 数值 | 0 / 0.2 / 0.7 |
| `summaryPriority` | 82.9% (34/41) | 数值 | 100 / 1000 / 470 |

## 四、原版 defName 一览（共 41 个，列出前 60）

```text
`Rule_DisallowDesignator_ZoneAdd_Growing`  `Rule_DisallowDesignator_Mine`    `Rule_DisallowDesignator_Hunt`    `Rule_DisallowDesignator_Tame`  
`AutoActivateMonolith`            `PlayerFaction`                   `PlayerPawnsArriveMethod`         `ForcedMap`                     
`GameStartDialog`                 ``                                `StartingMech`                    `ConfigPage_ConfigureStartingPawns`
`ForcedTrait`                     `ForcedHediff`                    `Naked`                           `SetNeedLevel`                  
`StartingResearch`                `StatFactor`                      `DisableIncident`                 `CreateIncident`                
`DisableQuest`                    `CreateQuest`                     `Rule_DisallowBuilding`           `PermanentGameCondition`        
`StartingAnimal`                  `StartingThing_Defined`           `ScatterThingsNearPlayerStart`    `ScatterThingsAnywhere`         
`PursuingMechanoids`              `ConfigurePawnsMutants`           `ConfigurePawnsKindDefs`          `ConfigurePawnsXenotypes`       
`SurfaceLayerFixed`               `PlanetLayerFixed`                `PawnFilter_Age`                  `OnPawnDeathExplode`            
`NoPossessions`                   `PlanetLayer`                     `ScenPart_MonolithGeneration`     `DisableExostriderRemains`      
`GameCondition_Planetkiller`    
```
