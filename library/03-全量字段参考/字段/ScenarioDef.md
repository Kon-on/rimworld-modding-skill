# ScenarioDef

- **所属线**：世界线
- **原版实例数**：10
- **字段路径数**：84
- **资料片**：Anomaly、Biotech、Core、Odyssey
- **原版出处**：`Core/Defs/Scenarios/Scenarios_Classic.xml`、`Biotech/Defs/Scenarios/Scenarios.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<ScenarioDef ParentName="Crashlanded">
    <defName>Tutorial</defName>
    <label>tutorial</label>
    <scenario>
      <showInUI>false</showInUI>
      <parts>
        <li Class="ScenPart_ScatterThingsNearPlayerStart">
          <def>ScatterThingsAnywhere</def>
          <thingDef>Cloth</thingDef>
          <count>300</count>
        </li>
      </parts>
    </scenario>
  </ScenarioDef>
  

  
```

> 来自 `Core/Defs/Scenarios/Scenarios_Classic.xml`，defName = `Tutorial`，XML 节点数 10（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Crashlanded / Mechanitor / Sanguophage
label                                          [文本]  例：Crashlanded / The Anomaly / The Mechanitor
scenario                                       [容器]
scenario/parts                                 [容器]
scenario/parts/li                              [容器]
scenario/parts/li/count                        [数值]  例：5 / 70 / 700
scenario/parts/li/def                          [文本]  例：AutoActivateMonolith / CreateIncident / ScatterThingsAnywhere
scenario/parts/li/method                       [文本]  例：DropPods / Gravship / NearColonists
scenario/parts/li/project                      [文本]  例：BasicMechtech / Batteries / MicroelectronicsBasics
scenario/parts/li/thingDef                     [文本]  例：Plasteel / ShipChunk / Steel
scenario/parts/li/visible                      [布尔]  例：false
```

## 三、全量字段表（84 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 90.0% (9/10) | 文本 | Crashlanded / Mechanitor / Sanguophage |
| `description` | 80.0% (8/10) | 文本 | The three of you awake in your cryptosleep sarcophagi to the sound of sirens and / When a dark stranger offere |
| `label` | 90.0% (9/10) | 文本 | Crashlanded / The Anomaly / The Mechanitor |
| `scenario` | 100.0% (10/10) | 容器 |  |
| `scenario/parts` | 100.0% (10/10) | 容器 |  |
| `scenario/parts/li` | 1340.0% (134/10) | 容器 |  |
| `scenario/parts/li/allowedDevelopmentalStages` | 10.0% (1/10) | 文本 | Adult, Child |
| `scenario/parts/li/allowRoofed` | 50.0% (5/10) | 布尔 | false |
| `scenario/parts/li/bondToRandomPlayerPawnChance` | 30.0% (3/10) | 数值 | 1.0 |
| `scenario/parts/li/chance` | 70.0% (7/10) | 数值 | 0.04 / 0.5 / 1.0 |
| `scenario/parts/li/closeSound` | 80.0% (8/10) | 文本 | GameStartSting |
| `scenario/parts/li/connections` | 20.0% (2/10) | 容器 |  |
| `scenario/parts/li/connections/Surface` | 20.0% (2/10) | 容器 |  |
| `scenario/parts/li/connections/Surface/zoomMode` | 20.0% (2/10) | 文本 | ZoomIn |
| `scenario/parts/li/context` | 80.0% (8/10) | 文本 | PlayerStarter |
| `scenario/parts/li/count` | 640.0% (64/10) | 数值 | 5 / 70 / 700 |
| `scenario/parts/li/customSummary` | 20.0% (2/10) | 文本 | Start with one adult or child sanguophage and one other colonist of any age. / Start with one ghoul and three  |
| `scenario/parts/li/def` | 1340.0% (134/10) | 文本 | AutoActivateMonolith / CreateIncident / ScatterThingsAnywhere |
| `scenario/parts/li/delayTicks` | 10.0% (1/10) | 数值 | 480000 |
| `scenario/parts/li/hediff` | 60.0% (6/10) | 文本 | FleshWhip / FleshmassLung / FleshmassStomach |
| `scenario/parts/li/hide` | 20.0% (2/10) | 布尔 | true |
| `scenario/parts/li/hideOffMap` | 10.0% (1/10) | 布尔 | true |
| `scenario/parts/li/incident` | 10.0% (1/10) | 文本 | RefugeePodCrash_Ghoul |
| `scenario/parts/li/kindCounts` | 10.0% (1/10) | 容器 |  |
| `scenario/parts/li/kindCounts/li` | 10.0% (1/10) | 容器 |  |
| `scenario/parts/li/kindCounts/li/count` | 10.0% (1/10) | 数值 | 1 |
| `scenario/parts/li/kindCounts/li/kindDef` | 10.0% (1/10) | 文本 | Mechanitor |
| `scenario/parts/li/kindCounts/li/requiredAtStart` | 10.0% (1/10) | 布尔 | true |
| `scenario/parts/li/layer` | 20.0% (2/10) | 文本 | Orbit |
| `scenario/parts/li/layerDef` | 10.0% (1/10) | 文本 | Orbit |
| `scenario/parts/li/leftBehindPawnKind` | 10.0% (1/10) | 文本 | Mechanitor |
| `scenario/parts/li/levelRange` | 10.0% (1/10) | 文本 | 0~0.1 |
| `scenario/parts/li/mapGenerator` | 10.0% (1/10) | 文本 | OrbitalRelay |
| `scenario/parts/li/maxDays` | 10.0% (1/10) | 数值 | 15 |
| `scenario/parts/li/mechKind` | 20.0% (2/10) | 文本 | Mech_Constructoid / Mech_Lifter |
| `scenario/parts/li/method` | 90.0% (9/10) | 文本 | DropPods / Gravship / NearColonists |
| `scenario/parts/li/minDays` | 10.0% (1/10) | 数值 | 12 |
| `scenario/parts/li/mutantCounts` | 10.0% (1/10) | 容器 |  |
| `scenario/parts/li/mutantCounts/li` | 20.0% (2/10) | 容器 |  |
| `scenario/parts/li/mutantCounts/li/allowedDevelopmentalStages` | 10.0% (1/10) | 文本 | Adult |
| `scenario/parts/li/mutantCounts/li/count` | 20.0% (2/10) | 数值 | 1 / 3 |
| `scenario/parts/li/mutantCounts/li/mutant` | 20.0% (2/10) | 容器/文本 | Ghoul |
| `scenario/parts/li/mutantCounts/li/requiredAtStart` | 10.0% (1/10) | 布尔 | true |
| `scenario/parts/li/need` | 10.0% (1/10) | 文本 | Food |
| `scenario/parts/li/overrideKinds` | 10.0% (1/10) | 容器 |  |
| `scenario/parts/li/overrideKinds/li` | 10.0% (1/10) | 容器 |  |
| `scenario/parts/li/overrideKinds/li/pawnKind` | 10.0% (1/10) | 文本 | Sanguophage_Player |
| `scenario/parts/li/overrideKinds/li/xenotype` | 10.0% (1/10) | 文本 | Sanguophage |
| `scenario/parts/li/overseenByPlayerPawnChance` | 20.0% (2/10) | 数值 | 1 |
| `scenario/parts/li/pawnChoiceCount` | 80.0% (8/10) | 数值 | 8 |
| `scenario/parts/li/pawnCount` | 50.0% (5/10) | 数值 | 1 / 3 / 5 |
| `scenario/parts/li/project` | 90.0% (9/10) | 文本 | BasicMechtech / Batteries / MicroelectronicsBasics |
| `scenario/parts/li/quality` | 30.0% (3/10) | 文本 | Good / Masterwork / Normal |
| `scenario/parts/li/questDef` | 10.0% (1/10) | 文本 | MechanoidSignal |
| `scenario/parts/li/settingsDef` | 20.0% (2/10) | 文本 | Orbit |
| `scenario/parts/li/severityRange` | 60.0% (6/10) | 文本 | 0.2~0.4 / 1~1 |
| `scenario/parts/li/stuff` | 80.0% (8/10) | 文本 | Jade / Plasteel / Steel |
| `scenario/parts/li/tag` | 20.0% (2/10) | 文本 | Orbit |
| `scenario/parts/li/text` | 70.0% (7/10) | 文本 | The ancient monolith unleashed an energy pulse that tore your research vessel ap / The gods were very angry. T |
| `scenario/parts/li/textKey` | 10.0% (1/10) | 文本 | GameStartDialog |
| `scenario/parts/li/thingDef` | 780.0% (78/10) | 文本 | Plasteel / ShipChunk / Steel |
| `scenario/parts/li/visible` | 130.0% (13/10) | 布尔 | false |
| `scenario/parts/li/xenotypeCounts` | 10.0% (1/10) | 容器 |  |
| `scenario/parts/li/xenotypeCounts/li` | 20.0% (2/10) | 容器 |  |
| `scenario/parts/li/xenotypeCounts/li/allowedDevelopmentalStages` | 10.0% (1/10) | 文本 | Adult, Child |
| `scenario/parts/li/xenotypeCounts/li/count` | 20.0% (2/10) | 数值 | 1 |
| `scenario/parts/li/xenotypeCounts/li/description` | 10.0% (1/10) | 文本 | non-baby sanguophage |
| `scenario/parts/li/xenotypeCounts/li/requiredAtStart` | 10.0% (1/10) | 布尔 | true |
| `scenario/parts/li/xenotypeCounts/li/xenotype` | 20.0% (2/10) | 文本 | Baseliner / Sanguophage |
| `scenario/playerFaction` | 40.0% (4/10) | 容器 |  |
| `scenario/playerFaction/def` | 10.0% (1/10) | 文本 | PlayerFaction |
| `scenario/playerFaction/factionDef` | 40.0% (4/10) | 文本 | GravshipCrew / PlayerColony / PlayerTribe |
| `scenario/showInUI` | 10.0% (1/10) | 布尔 | false |
| `scenario/standardAnomalyPlaystyleOnly` | 10.0% (1/10) | 布尔 | true |
| `scenario/summary` | 80.0% (8/10) | 文本 | One crashlanded sanguophage needing blood to survive, and one human colonist. / One mechanitor and a few serva |
| `scenario/surfaceLayer` | 10.0% (1/10) | 容器 |  |
| `scenario/surfaceLayer/connections` | 10.0% (1/10) | 容器 |  |
| `scenario/surfaceLayer/connections/Orbit` | 10.0% (1/10) | 容器 |  |
| `scenario/surfaceLayer/connections/Orbit/zoomMode` | 10.0% (1/10) | 文本 | ZoomOut |
| `scenario/surfaceLayer/def` | 10.0% (1/10) | 文本 | SurfaceLayerFixed |
| `scenario/surfaceLayer/hide` | 10.0% (1/10) | 布尔 | true |
| `scenario/surfaceLayer/layer` | 10.0% (1/10) | 文本 | Surface |
| `scenario/surfaceLayer/settingsDef` | 10.0% (1/10) | 文本 | Surface |
| `scenario/surfaceLayer/tag` | 10.0% (1/10) | 文本 | Surface |

## 四、原版 defName 一览（共 10 个，列出前 60）

```text
`Tutorial`                        ``                                `NakedBrutality`                  `TheRichExplorer`               
`Sanguophage`                     `Mechanitor`                      `LostTribe`                       `Crashlanded`                   
`TheGravship`                     `TheAnomaly`                    
```
