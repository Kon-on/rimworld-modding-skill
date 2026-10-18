# WorldObjectDef

- **所属线**：世界线
- **原版实例数**：38
- **字段路径数**：36
- **资料片**：Core、Ideology、Odyssey、Royalty
- **原版出处**：`Core/Defs/WorldObjectDefs/WorldObjects.xml`、`Odyssey/Defs/WorldObjectDefs/WorldObjects.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<WorldObjectDef Name="StaticWorldObjectBase" Abstract="True">
    <inspectorTabs>
      <li>WITab_Terrain</li>
      <li>WITab_Planet</li>
      <li>WITab_Orbit</li>
    </inspectorTabs>
  </WorldObjectDef>
  
  
```

> 来自 `Core/Defs/WorldObjectDefs/WorldObjects.xml`，defName = ``，XML 节点数 5（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

_该类型没有出现率≥90% 的字段（字段高度自由）。_

## 三、全量字段表（36 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `allowCaravanIncidentsWhichGenerateMap` | 10.5% (4/38) | 布尔 | true |
| `blockExitGridUntilBattleIsWon` | 2.6% (1/38) | 布尔 | true |
| `canBePlayerHome` | 21.1% (8/38) | 布尔 | true |
| `canHaveMap` | 10.5% (4/38) | 布尔 | false |
| `canResizeToGravship` | 2.6% (1/38) | 布尔 | true |
| `comps` | 26.3% (10/38) | 容器 |  |
| `comps/li` | 76.3% (29/38) | 容器 |  |
| `defName` | 86.8% (33/38) | 文本 | AbandonedSettlement / Ambush / Caravan |
| `description` | 57.9% (22/38) | 文本 | A base of one of the factions. / A group of traveling people. / An abandoned settlement. |
| `drawAltitudeOffset` | 2.6% (1/38) | 数值 | 0.01 |
| `expandingIcon` | 42.1% (16/38) | 布尔 | true |
| `expandingIconColor` | 10.5% (4/38) | 容器/文本 | (162,164,149) / (255,255,255,255) |
| `expandingIconDrawSize` | 18.4% (7/38) | 数值 | 1 / 1.1 / 1.35 |
| `expandingIconMaskTexture` | 2.6% (1/38) | 文本 | World/WorldObjects/Expanding/ResourceAsteroid_m |
| `expandingIconPriority` | 39.5% (15/38) | 数值 | 10 / 100 / 20 |
| `expandingIconTexture` | 47.4% (18/38) | 文本 | World/WorldObjects/Expanding/Ambush / World/WorldObjects/Expanding/Caravan / World/WorldObjects/Expanding/Dest |
| `expandingShader` | 2.6% (1/38) | 文本 | CutoutComplexUI |
| `expandMore` | 18.4% (7/38) | 布尔 | true |
| `fullyExpandedInSpace` | 13.2% (5/38) | 布尔 | true |
| `IncidentTargetTags` | 26.3% (10/38) | 容器 |  |
| `IncidentTargetTags/li` | 26.3% (10/38) | 文本 | Caravan / Map_Misc / Map_PlayerHome |
| `inspectorTabs` | 5.3% (2/38) | 容器 |  |
| `inspectorTabs/li` | 23.7% (9/38) | 文本 | WITab_Caravan_Gear / WITab_Caravan_Health / WITab_Caravan_Needs |
| `isTempIncidentMapOwner` | 7.9% (3/38) | 布尔 | true |
| `label` | 89.5% (34/38) | 文本 | abandoned settlement / ambush / caravan |
| `mapGenerator` | 31.6% (12/38) | 文本 | BasePlayer_SecondArchonexusCycle / BasePlayer_ThirdArchonexusCycle / EscapeShip |
| `nameMaker` | 7.9% (3/38) | 文本 | NamerWorldObject_AsteroidBasic |
| `neverMultiSelect` | 2.6% (1/38) | 布尔 | true |
| `overrideMapSize` | 10.5% (4/38) | 文本 | (200, 1, 200) / (200,1,200) / (250,1,250) |
| `requiresSignalJammerToReach` | 5.3% (2/38) | 布尔 | true |
| `saved` | 2.6% (1/38) | 布尔 | false |
| `texture` | 44.7% (17/38) | 文本 | World/WorldObjects/Ambush / World/WorldObjects/Caravan / World/WorldObjects/JourneyDestination |
| `treatAsPlayerHome` | 7.9% (3/38) | 布尔 | true |
| `useDynamicDrawer` | 15.8% (6/38) | 布尔 | true |
| `validLaunchTarget` | 7.9% (3/38) | 布尔 | false |
| `worldObjectClass` | 68.4% (26/38) | 文本 | AbandonedSettlement / Caravan / CaravansBattlefield |

## 四、原版 defName 一览（共 38 个，列出前 60）

```text
``                                `PocketMap`                       `Settlement_SecondArchonexusCycle`  `Settlement_ThirdArchonexusCycle`
``                                `Space`                           `TravelingShuttle`                `DestroyedSpaceSettlement`      
`AsteroidBasic`                   `Mechhive`                        `PassengerShuttle`                `AbandonedLandmark`             
`AbandonedSettlement`             `Debug_Arena`                     `GravshipLaunch`                  `AbandonedCamp`                 
`ClaimableSpaceSite`              `OrbitalItemStash`                `AbandonedArchotechStructures`    ``                              
`ClaimableSite`                   `PeaceTalks`                      `AsteroidMiningSite`              `DestroyedSettlement`           
`RoutePlannerWaypoint`            ``                                ``                                `SpaceSettlement`               
`SpaceSite`                       `TravellingTransporters`          `Settlement`                      `Gravship`                      
`AttackedNonPlayerCaravan`        `Ambush`                          `Camp`                            `Site`                          
`EscapeShip`                      `Caravan`                       
```
