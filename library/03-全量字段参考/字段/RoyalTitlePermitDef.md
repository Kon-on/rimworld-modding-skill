# RoyalTitlePermitDef

- **所属线**：世界线
- **原版实例数**：16
- **字段路径数**：31
- **资料片**：Royalty
- **原版出处**：`Royalty/Defs/RoyalTitles/RoyalPermits_Empire.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<RoyalTitlePermitDef>
    <defName>TradeSettlement</defName>
    <label>trade with settlements</label>
  </RoyalTitlePermitDef>

  
```

> 来自 `Royalty/Defs/RoyalTitles/RoyalPermits_Empire.xml`，defName = `TradeSettlement`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：SteelDrop / TradeCaravan / TradeOrbital
label                                          [文本]  例：steel drop / trade with caravans / trade with orbital traders
```

## 三、全量字段表（31 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `cooldownDays` | 56.2% (9/16) | 数值 | 40 / 45 / 50 |
| `defName` | 93.8% (15/16) | 文本 | SteelDrop / TradeCaravan / TradeOrbital |
| `description` | 75.0% (12/16) | 文本 | Call for a drop of 20 packaged survival meals. / Call for a drop of 250 steel. / Call for a drop of 5 glitterw |
| `faction` | 62.5% (10/16) | 文本 | Empire |
| `label` | 93.8% (15/16) | 文本 | steel drop / trade with caravans / trade with orbital traders |
| `layerBlacklist` | 50.0% (8/16) | 容器 |  |
| `layerBlacklist/li` | 50.0% (8/16) | 文本 | Orbit |
| `minTitle` | 75.0% (12/16) | 文本 | Acolyte / Baron / Count |
| `permitPointCost` | 62.5% (10/16) | 数值 | 1 |
| `prerequisite` | 18.8% (3/16) | 文本 | CallLaborerTeam / CallMilitaryAidLarge / CallOrbitalStrike |
| `royalAid` | 81.2% (13/16) | 容器 |  |
| `royalAid/aidDurationDays` | 12.5% (2/16) | 数值 | 4 |
| `royalAid/explosionCount` | 12.5% (2/16) | 数值 | 1 / 6 |
| `royalAid/explosionRadiusRange` | 12.5% (2/16) | 数值 | 5.9 / 7.9 |
| `royalAid/favorCost` | 75.0% (12/16) | 数值 | 4 / 6 / 8 |
| `royalAid/intervalTicks` | 12.5% (2/16) | 数值 | 60 |
| `royalAid/itemsToDrop` | 25.0% (4/16) | 容器 |  |
| `royalAid/itemsToDrop/MealSurvivalPack` | 6.2% (1/16) | 数值 | 20 |
| `royalAid/itemsToDrop/MedicineUltratech` | 6.2% (1/16) | 数值 | 5 |
| `royalAid/itemsToDrop/Silver` | 6.2% (1/16) | 数值 | 500 |
| `royalAid/itemsToDrop/Steel` | 6.2% (1/16) | 数值 | 250 |
| `royalAid/overrideAcceptableTemperatureRange` | 6.2% (1/16) | 文本 | -80~50 |
| `royalAid/pawnCount` | 31.2% (5/16) | 数值 | 4 / 8 |
| `royalAid/pawnKindDef` | 31.2% (5/16) | 文本 | Empire_Common_Laborer / Empire_Fighter_Cataphract / Empire_Fighter_Janissary |
| `royalAid/radius` | 12.5% (2/16) | 数值 | 2.9 / 7.9 |
| `royalAid/targetingRange` | 56.2% (9/16) | 数值 | 39.9 / 44.9 |
| `royalAid/targetingRequireLOS` | 18.8% (3/16) | 布尔 | false |
| `royalAid/warmupTicks` | 12.5% (2/16) | 数值 | 120 |
| `uiPosition` | 75.0% (12/16) | 文本 | (0,0) / (0,1) / (0,4) |
| `usableOnWorldMap` | 12.5% (2/16) | 布尔 | true |
| `workerClass` | 56.2% (9/16) | 文本 | RoyalTitlePermitWorker_CallAid / RoyalTitlePermitWorker_CallLaborers / RoyalTitlePermitWorker_DropResources |

## 四、原版 defName 一览（共 16 个，列出前 60）

```text
`TradeSettlement`                 `TradeOrbital`                    `TradeCaravan`                    ``                              
`FoodDrop`                        `SilverDrop`                      `GlitterMedDrop`                  `SteelDrop`                     
`CallMilitaryAidSmall`            `CallMilitaryAidLarge`            `CallTransportShuttle`            `CallLaborerTeam`               
`CallMilitaryAidGrand`            `CallLaborerGang`                 `CallOrbitalStrike`               `CallOrbitalSalvo`              
```
