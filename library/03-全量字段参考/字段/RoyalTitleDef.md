# RoyalTitleDef

- **所属线**：世界线
- **原版实例数**：13
- **字段路径数**：76
- **资料片**：Royalty
- **原版出处**：`Royalty/Defs/RoyalTitles/RoyalTitles_Empire.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<RoyalTitleDef Abstract="True" Name="BaseEmpireTitle">
    <tags>
      <li>EmpireTitle</li>
    </tags>
    <awardThought>GainedTitle</awardThought>
    <lostThought>LostTitle</lostThought>
  </RoyalTitleDef>

  
```

> 来自 `Royalty/Defs/RoyalTitles/RoyalTitles_Empire.xml`，defName = ``，XML 节点数 5（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
bedroomRequirements/li                         [容器]
bedroomRequirements/li/buildingTags            [容器]
bedroomRequirements/li/buildingTags/li         [文本]  例：Anomaly / Biotech / Production
bedroomRequirements/li/labelKey                [文本]  例：RoomRequirementAllFloored / RoomRequirementNoAnomalyBuildings / RoomRequirementNoBiotechBuildings
bedroomRequirements/li/thingDef                [文本]  例：Drape / Dresser / EndTable
bedroomRequirements/li/things/li               [文本]  例：DeathrestCasket / DoubleBed / RoyalBed
disabledWorkTags/li                            [文本]  例：Cleaning / ManualDumb / Mining
foodRequirement/allowedDefs/li                 [文本]  例：Ambrosia / InsectJelly / Milk
permits/li                                     [文本]  例：TradeCaravan / TradeOrbital / TradeSettlement
requiredApparel/li                             [容器]
requiredApparel/li/allowedTags                 [容器]
requiredApparel/li/allowedTags/li              [文本]  例：Cape / Mechlord / PrestigeCombatGear
requiredApparel/li/bodyPartGroupsMatchAny      [容器]
requiredApparel/li/bodyPartGroupsMatchAny/li   [文本]  例：FullHead / Torso / UpperHead
requiredApparel/li/requiredTags                [容器]
requiredApparel/li/requiredTags/li             [文本]  例：RoyalTier2 / RoyalTier5 / RoyalTier6
throneRoomRequirements/li                      [容器]
throneRoomRequirements/li/buildingTags         [容器]
throneRoomRequirements/li/buildingTags/li      [文本]  例：Anomaly / Bed / Biotech
throneRoomRequirements/li/count                [数值]  例：2 / 4 / 6
throneRoomRequirements/li/labelKey             [文本]  例：RoomRequirementNoAltars / RoomRequirementNoAnomalyBuildings / RoomRequirementNoBeds
throneRoomRequirements/li/things               [容器]
throneRoomRequirements/li/things/li            [文本]  例：Brazier / DarklightBrazier / GrandThrone
```

## 三、全量字段表（76 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `allowDignifiedMeditationFocus` | 7.7% (1/13) | 布尔 | False |
| `awardThought` | 7.7% (1/13) | 文本 | GainedTitle |
| `awardWorkerClass` | 7.7% (1/13) | 文本 | RoyalTitleAwardWorker_Instant |
| `bedroomRequirements` | 46.2% (6/13) | 容器 |  |
| `bedroomRequirements/li` | 415.4% (54/13) | 容器 |  |
| `bedroomRequirements/li/area` | 46.2% (6/13) | 数值 | 16 / 24 / 30 |
| `bedroomRequirements/li/buildingTags` | 138.5% (18/13) | 容器 |  |
| `bedroomRequirements/li/buildingTags/li` | 138.5% (18/13) | 文本 | Anomaly / Biotech / Production |
| `bedroomRequirements/li/count` | 23.1% (3/13) | 数值 | 1 |
| `bedroomRequirements/li/disablingPrecepts` | 46.2% (6/13) | 容器 |  |
| `bedroomRequirements/li/disablingPrecepts/li` | 46.2% (6/13) | 文本 | SlabBed_Preferred |
| `bedroomRequirements/li/impressiveness` | 38.5% (5/13) | 数值 | 40 / 50 / 70 |
| `bedroomRequirements/li/labelKey` | 184.6% (24/13) | 文本 | RoomRequirementAllFloored / RoomRequirementNoAnomalyBuildings / RoomRequirementNoBiotechBuildings |
| `bedroomRequirements/li/tags` | 46.2% (6/13) | 容器 |  |
| `bedroomRequirements/li/tags/li` | 76.9% (10/13) | 文本 | FineFloor / Floor |
| `bedroomRequirements/li/thingDef` | 100.0% (13/13) | 文本 | Drape / Dresser / EndTable |
| `bedroomRequirements/li/things` | 46.2% (6/13) | 容器 |  |
| `bedroomRequirements/li/things/li` | 115.4% (15/13) | 文本 | DeathrestCasket / DoubleBed / RoyalBed |
| `canBeInherited` | 38.5% (5/13) | 布尔 | True |
| `changeHeirQuestPoints` | 53.8% (7/13) | 数值 | 1000 / 1200 / 1600 |
| `commonality` | 76.9% (10/13) | 数值 | 0 / 0.1 / 0.6 |
| `decreeMentalBreakCommonality` | 30.8% (4/13) | 数值 | 12 / 2 / 4 |
| `decreeMtbDays` | 30.8% (4/13) | 数值 | -1 |
| `decreeTags` | 30.8% (4/13) | 容器 |  |
| `decreeTags/li` | 30.8% (4/13) | 文本 | All |
| `defName` | 84.6% (11/13) | 文本 | Acolyte / Freeholder / Knight |
| `description` | 84.6% (11/13) | 文本 | The Imperial title of freeholder is used by the Empire to signifies a fully-resp / The Imperial title of novic |
| `disabledJoyKinds` | 30.8% (4/13) | 容器 |  |
| `disabledJoyKinds/li` | 30.8% (4/13) | 文本 | Gaming_Dexterity |
| `disabledWorkTags` | 46.2% (6/13) | 容器 |  |
| `disabledWorkTags/li` | 115.4% (15/13) | 文本 | Cleaning / ManualDumb / Mining |
| `favorCost` | 53.8% (7/13) | 数值 | 1 / 10 / 6 |
| `foodRequirement` | 46.2% (6/13) | 容器 |  |
| `foodRequirement/allowedDefs` | 46.2% (6/13) | 容器 |  |
| `foodRequirement/allowedDefs/li` | 161.5% (21/13) | 文本 | Ambrosia / InsectJelly / Milk |
| `foodRequirement/allowedTypes` | 46.2% (6/13) | 文本 | Processed, Liquor |
| `foodRequirement/minQuality` | 46.2% (6/13) | 文本 | MealFine / MealLavish / MealSimple |
| `grantedAbilities` | 30.8% (4/13) | 容器 |  |
| `grantedAbilities/li` | 30.8% (4/13) | 文本 | Speech |
| `label` | 84.6% (11/13) | 文本 | acolyte / freeholder / knight |
| `labelFemale` | 7.7% (1/13) | 文本 | empress |
| `lostThought` | 7.7% (1/13) | 文本 | LostTitle |
| `maxPsylinkLevel` | 53.8% (7/13) | 数值 | 1 / 2 / 3 |
| `minExpectation` | 46.2% (6/13) | 文本 | High / Moderate / Noble |
| `permitPointsAwarded` | 38.5% (5/13) | 数值 | 1 |
| `permits` | 38.5% (5/13) | 容器 |  |
| `permits/li` | 100.0% (13/13) | 文本 | TradeCaravan / TradeOrbital / TradeSettlement |
| `recruitmentResistanceOffset` | 61.5% (8/13) | 数值 | 10 / 25 / 40 |
| `replaceOnRecruited` | 7.7% (1/13) | 文本 | Consul |
| `requiredApparel` | 76.9% (10/13) | 容器 |  |
| `requiredApparel/li` | 153.8% (20/13) | 容器 |  |
| `requiredApparel/li/allowedTags` | 153.8% (20/13) | 容器 |  |
| `requiredApparel/li/allowedTags/li` | 515.4% (67/13) | 文本 | Cape / Mechlord / PrestigeCombatGear |
| `requiredApparel/li/bodyPartGroupsMatchAny` | 153.8% (20/13) | 容器 |  |
| `requiredApparel/li/bodyPartGroupsMatchAny/li` | 223.1% (29/13) | 文本 | FullHead / Torso / UpperHead |
| `requiredApparel/li/requiredTags` | 153.8% (20/13) | 容器 |  |
| `requiredApparel/li/requiredTags/li` | 153.8% (20/13) | 文本 | RoyalTier2 / RoyalTier5 / RoyalTier6 |
| `requiredMinimumApparelQuality` | 30.8% (4/13) | 文本 | Normal |
| `seniority` | 84.6% (11/13) | 数值 | 0 / 100 / 200 |
| `speechCooldown` | 30.8% (4/13) | 数值 | 1200000 / 600000 / 900000 |
| `suppressIdleAlert` | 23.1% (3/13) | 布尔 | true |
| `tags` | 7.7% (1/13) | 容器 |  |
| `tags/li` | 7.7% (1/13) | 文本 | EmpireTitle |
| `throneRoomRequirements` | 46.2% (6/13) | 容器 |  |
| `throneRoomRequirements/li` | 592.3% (77/13) | 容器 |  |
| `throneRoomRequirements/li/area` | 46.2% (6/13) | 数值 | 24 / 30 / 40 |
| `throneRoomRequirements/li/buildingTags` | 184.6% (24/13) | 容器 |  |
| `throneRoomRequirements/li/buildingTags/li` | 184.6% (24/13) | 文本 | Anomaly / Bed / Biotech |
| `throneRoomRequirements/li/count` | 100.0% (13/13) | 数值 | 2 / 4 / 6 |
| `throneRoomRequirements/li/impressiveness` | 38.5% (5/13) | 数值 | 120 / 160 / 60 |
| `throneRoomRequirements/li/labelKey` | 323.1% (42/13) | 文本 | RoomRequirementNoAltars / RoomRequirementNoAnomalyBuildings / RoomRequirementNoBeds |
| `throneRoomRequirements/li/tags` | 46.2% (6/13) | 容器 |  |
| `throneRoomRequirements/li/tags/li` | 69.2% (9/13) | 文本 | FineFloor / Floor |
| `throneRoomRequirements/li/thingDef` | 69.2% (9/13) | 文本 | Column / Drape / Piano |
| `throneRoomRequirements/li/things` | 161.5% (21/13) | 容器 |  |
| `throneRoomRequirements/li/things/li` | 315.4% (41/13) | 文本 | Brazier / DarklightBrazier / GrandThrone |

## 四、原版 defName 一览（共 13 个，列出前 60）

```text
``                                `Freeholder`                      `Yeoman`                          `Duke`                          
`Consul`                          `Emperor`                         `Stellarch`                       `Acolyte`                       
``                                `Knight`                          `Praetor`                         `Baron`                         
`Count`                         
```
