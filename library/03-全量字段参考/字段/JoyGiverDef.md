# JoyGiverDef

- **所属线**：人物线
- **原版实例数**：22
- **字段路径数**：15
- **资料片**：Core、Odyssey、Royalty
- **原版出处**：`Core/Defs/Joy/JoyGivers.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<JoyGiverDef>
    <defName>GoForWalk</defName>
    <giverClass>JoyGiver_GoForWalk</giverClass>
    <baseChance>1</baseChance>
    <jobDef>GoForWalk</jobDef>
    <joyKind>Meditative</joyKind>
  </JoyGiverDef>

  
```

> 来自 `Core/Defs/Joy/JoyGivers.xml`，defName = `GoForWalk`，XML 节点数 6（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
baseChance                                     [数值]  例：0.75 / 1 / 3
defName                                        [文本]  例：GoForWalk / Meditate / Pray
giverClass                                     [文本]  例：JoyGiver_GoForWalk / JoyGiver_InPrivateRoom / JoyGiver_Meditate
jobDef                                         [文本]  例：GoForWalk / Meditate / Pray
joyKind                                        [文本]  例：Gaming_Cerebral / Gaming_Dexterity / Meditative
```

## 三、全量字段表（15 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `baseChance` | 100.0% (22/22) | 数值 | 0.75 / 1 / 3 |
| `canDoWhileInBed` | 18.2% (4/22) | 布尔 | true |
| `defName` | 100.0% (22/22) | 文本 | GoForWalk / Meditate / Pray |
| `desireSit` | 9.1% (2/22) | 布尔 | false |
| `giverClass` | 100.0% (22/22) | 文本 | JoyGiver_GoForWalk / JoyGiver_InPrivateRoom / JoyGiver_Meditate |
| `jobDef` | 90.9% (20/22) | 文本 | GoForWalk / Meditate / Pray |
| `joyKind` | 100.0% (22/22) | 文本 | Gaming_Cerebral / Gaming_Dexterity / Meditative |
| `pctPawnsEverDo` | 9.1% (2/22) | 数值 | 0.4 / 0.5 |
| `requireChair` | 9.1% (2/22) | 布尔 | false |
| `requiredCapacities` | 68.2% (15/22) | 容器 |  |
| `requiredCapacities/li` | 81.8% (18/22) | 文本 | Manipulation / Sight |
| `requiresEnjoyOutdoors` | 9.1% (2/22) | 布尔 | true |
| `thingDefs` | 45.5% (10/22) | 容器 |  |
| `thingDefs/li` | 72.7% (16/22) | 文本 | BilliardsTable / GameOfUrBoard / HoopstoneRing |
| `unroofedOnly` | 4.5% (1/22) | 布尔 | true |

## 四、原版 defName 一览（共 22 个，列出前 60）

```text
`GoForWalk`                       `VisitGrave`                      `SocialRelax`                     `VisitSickPawn`                 
`GoSwimming`                      `TakeDrug`                        `Meditate`                        `Pray`                          
`Skygaze`                         `ViewArt`                         `BuildSnowman`                    `Reading`                       
`Play_Chess`                      `EatChocolate`                    `Play_Horseshoes`                 `Play_Hoopstone`                
`Play_Billiards`                  `Play_GameOfUr`                   `Play_Poker`                      `UseTelescope`                  
`WatchTelevision`                 `Play_MusicalInstrument`        
```
