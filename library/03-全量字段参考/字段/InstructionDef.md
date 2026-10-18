# InstructionDef

- **所属线**：系统线
- **原版实例数**：37
- **字段路径数**：24
- **资料片**：Core
- **原版出处**：`Core/Defs/Tutor/Instructions.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<InstructionDef>
    <defName>MapCameraDolly</defName>
    <text>Here you are on the surface!\n\nNow try moving the camera around.\n\nUse the {Key:MapDolly_Up}-{Key:MapDolly_Left}-{Key:MapDolly_Down}-{Key:MapDolly_Right} keys, or click and drag with the middle mouse button.\n\nTry it now!</text>
    <textController>Here you are on the surface!\n\nNow try moving the camera around with the left joystick.\n\nTry it now!</textController>
    <eventTagInitiate>GameStartDialogClosed</eventTagInitiate>
    <instructionClass>Instruction_LearnConcept</instructionClass>
    <concept>CameraDolly</concept>
  </InstructionDef>

  
```

> 来自 `Core/Defs/Tutor/Instructions.xml`，defName = `MapCameraDolly`，XML 节点数 7（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
actionTagsAllowed/li                           [文本]  例：ChooseBiome-TemperateForest-Flat-None / GotoNextPage / GotoPrevPage
defName                                        [文本]  例：ChooseLandingSite / CreateWorldParams / RandomizeCharacter
eventTagInitiate                               [文本]  例：PageStart-ConfigureStartingPawns / PageStart-CreateWorldParams / PageStart-SelectStartingSite
highlightTags/li                               [文本]  例：NextPage / RandomizePawn / ReorderPawn
text                                           [文本]  例：Here you choose your starting site.\n\nClick a temperate forest (light green) wi / If you don't like a character, you can regenerate them!\n\nClick the RANDOMIZE b / Now you choose which characters you want to use.\n\nDRAG a character from the "l
```

## 三、全量字段表（24 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `actionTagsAllowed` | 83.8% (31/37) | 容器 |  |
| `actionTagsAllowed/li` | 283.8% (105/37) | 文本 | ChooseBiome-TemperateForest-Flat-None / GotoNextPage / GotoPrevPage |
| `concept` | 13.5% (5/37) | 文本 | CameraDolly / CameraZoom / Pause |
| `defName` | 100.0% (37/37) | 文本 | ChooseLandingSite / CreateWorldParams / RandomizeCharacter |
| `endTutorial` | 2.7% (1/37) | 布尔 | true |
| `eventTagInitiate` | 100.0% (37/37) | 文本 | PageStart-ConfigureStartingPawns / PageStart-CreateWorldParams / PageStart-SelectStartingSite |
| `eventTagInitiateSource` | 2.7% (1/37) | 文本 | ReorderCharacters |
| `eventTagsEnd` | 35.1% (13/37) | 容器 |  |
| `eventTagsEnd/li` | 35.1% (13/37) | 文本 | Designate-ZoneAddStockpile_Resources / PageClosed / RandomizePawn |
| `giveOnActivateCount` | 2.7% (1/37) | 数值 | 75 |
| `giveOnActivateDef` | 2.7% (1/37) | 文本 | RawPotatoes |
| `highlightTags` | 83.8% (31/37) | 容器 |  |
| `highlightTags/li` | 194.6% (72/37) | 文本 | NextPage / RandomizePawn / ReorderPawn |
| `instructionClass` | 73.0% (27/37) | 文本 | Instruction_BuildRoomWalls / Instruction_LearnConcept / Instruction_PlaceStockpile |
| `onMapInstruction` | 46.0% (17/37) | 文本 | Allow this / Build a door over one wall / Build walls |
| `recipeDef` | 2.7% (1/37) | 文本 | CookMealSimple |
| `recipeTargetCount` | 2.7% (1/37) | 数值 | 10 |
| `rejectInputMessage` | 83.8% (31/37) | 文本 | Click GENERATE to generate your world. / Please choose a temperate forest site with no hills (light green with |
| `resetBuildDesignatorStuffs` | 10.8% (4/37) | 布尔 | true |
| `startCentered` | 2.7% (1/37) | 布尔 | true |
| `targetCount` | 24.3% (9/37) | 数值 | 1 / 10 / 3 |
| `text` | 100.0% (37/37) | 文本 | Here you choose your starting site.\n\nClick a temperate forest (light green) wi / If you don't like a charact |
| `textController` | 27.0% (10/37) | 文本 | Great!\n\nYou can also zoom in and out with {Key:MapZoom_In} and {Key:MapZoom_Ou / Here you are on the surface |
| `thingDef` | 18.9% (7/37) | 文本 | AnimalSleepingSpot / Bed / HorseshoesPin |

## 四、原版 defName 一览（共 37 个，列出前 60）

```text
`MapCameraDolly`                  `MapCameraZoom`                   `EndStockpileDesignating`         `EquipWeapons`                  
`Pause`                           `TimeControls`                    `OpenMainTabWork`                 `ChangeWorkSettings`            
`OpenMainTabResearch`             `UndraftAll`                      `ReorderCharacters`               `SelectResearchProject`         
`CreateWorldParams`               `ChooseLandingSite`               `FinishSandbags`                  `RandomizeCharacter`            
`AcceptStartingPawns`             `SetToGrowRice`                   `MineSteel`                       `ChopTrees`                     
`ChooseStoryteller`               `ExpandAreaHome`                  `ExpandAreaBuildRoof`             `BuildSandbags`                 
`MakeStockpile`                   `UnforbidStartingResources`       `BuildTorchLamp`                  `BuildAnimalSleepingSpot`       
`MakeGrowingZone`                 `BuildFueledStove`                `BuildRoomWalls`                  `BuildRoomDoor`                 
`AddBillSimpleMeal`               `DownRaider`                      `BuildBeds`                       `BuildHorseshoesPin`            
`BuildSimpleResearchBench`      
```
