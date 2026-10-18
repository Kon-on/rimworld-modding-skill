# TraderKindDef

- **所属线**：世界线
- **原版实例数**：20
- **字段路径数**：51
- **资料片**：Core、Royalty
- **原版出处**：`Royalty/Defs/TraderKindDefs/TraderKinds_Caravan_Empire.xml`、`Core/Defs/TraderKindDefs/TraderKinds_Orbital_Misc.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<TraderKindDef>
    <defName>Empire_Caravan_TributeCollector</defName>
    <label>royal tribute collector</label>
    <requestable>False</requestable>
    <commonality>1</commonality>
    <category>TributeCollector</category>
    <tradeCurrency>Favor</tradeCurrency>
    <faction>Empire</faction>
    <hideThingsNotWillingToTrade>True</hideThingsNotWillingToTrade>
    <stockGenerators>
      <!-- Buying -->
      <li Class="StockGenerator_BuySlaves"/>
      <li Class="StockGenerator_BuySingleDef">
        <thingDef>Gold</thingDef>
      </li>
    </stockGenerators>
  </TraderKindDef>
```

> 来自 `Royalty/Defs/TraderKindDefs/TraderKinds_Caravan_Empire.xml`，defName = `Empire_Caravan_TributeCollector`，XML 节点数 14（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Base_Neolithic_Standard / Base_Outlander_Standard / Caravan_Neolithic_BulkGoods
stockGenerators                                [容器]
stockGenerators/li                             [容器]
stockGenerators/li/categoryDef                 [文本]  例：Books / Drugs / FoodRaw
stockGenerators/li/countRange                  [数值/文本]  例：-1~2 / -3~1 / 1~1
stockGenerators/li/excludedThingDefs           [容器]
stockGenerators/li/excludedThingDefs/li        [文本]  例：Bioferrite / GravlitePanel / Tome
stockGenerators/li/maxTechLevelGenerate        [文本]  例：Neolithic
stockGenerators/li/tag                         [文本]  例：Art / ImplantEmpireRoyal / MusicalInstrument
stockGenerators/li/thingDef                    [文本]  例：AnimusStone / Gold / MedicineHerbal
stockGenerators/li/thingDefCountRange          [数值/文本]  例：0~3 / 2 / 2~4
stockGenerators/li/totalPriceRange             [文本]  例：200~600 / 300~700 / 300~800
stockGenerators/li/tradeTag                    [文本]  例：Artifact / BasicClothing / Clothing
stockGenerators/li/tradeTagsSell/li            [文本]  例：AnimalFarm / AnimalFighter / AnimalPet
```

## 三、全量字段表（51 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `category` | 20.0% (4/20) | 文本 | Slaver / TributeCollector |
| `commonality` | 15.0% (3/20) | 数值 | 1 |
| `commonalityMultFromPopulationIntent` | 15.0% (3/20) | 容器 |  |
| `commonalityMultFromPopulationIntent/points` | 15.0% (3/20) | 容器 |  |
| `commonalityMultFromPopulationIntent/points/li` | 45.0% (9/20) | 文本 | (0.2, 0) / (1,   1) / (2,   3) |
| `defName` | 100.0% (20/20) | 文本 | Base_Neolithic_Standard / Base_Outlander_Standard / Caravan_Neolithic_BulkGoods |
| `faction` | 40.0% (8/20) | 文本 | Empire / TradersGuild |
| `hideThingsNotWillingToTrade` | 5.0% (1/20) | 布尔 | True |
| `label` | 85.0% (17/20) | 文本 | bulk goods trader / shaman merchant / slaver |
| `orbital` | 25.0% (5/20) | 布尔 | true |
| `permitRequiredForTrading` | 15.0% (3/20) | 文本 | TradeCaravan / TradeOrbital / TradeSettlement |
| `requestable` | 20.0% (4/20) | 布尔 | False / false |
| `stockGenerators` | 100.0% (20/20) | 容器 |  |
| `stockGenerators/li` | 2505.0% (501/20) | 容器 |  |
| `stockGenerators/li/apparelTag` | 30.0% (6/20) | 文本 | Royal |
| `stockGenerators/li/categoryDef` | 260.0% (52/20) | 文本 | Books / Drugs / FoodRaw |
| `stockGenerators/li/checkTemperature` | 15.0% (3/20) | 布尔 | false |
| `stockGenerators/li/countChances` | 70.0% (14/20) | 容器 |  |
| `stockGenerators/li/countChances/li` | 85.0% (17/20) | 容器 |  |
| `stockGenerators/li/countChances/li/chance` | 85.0% (17/20) | 数值 | 0.5 / 1 |
| `stockGenerators/li/countChances/li/count` | 85.0% (17/20) | 数值 | 1 / 2 / 3 |
| `stockGenerators/li/countRange` | 1630.0% (326/20) | 数值/文本 | -1~2 / -3~1 / 1~1 |
| `stockGenerators/li/createMatingPair` | 55.0% (11/20) | 容器 |  |
| `stockGenerators/li/createMatingPair/li` | 55.0% (11/20) | 文本 | AnimalFarm |
| `stockGenerators/li/customCountRanges` | 20.0% (4/20) | 容器 |  |
| `stockGenerators/li/customCountRanges/Hyperweave` | 20.0% (4/20) | 文本 | 100~200 / 40~120 / 50~200 |
| `stockGenerators/li/customCountRanges/Luciferium` | 5.0% (1/20) | 文本 | 7~25 |
| `stockGenerators/li/customCountRanges/MedicineUltratech` | 5.0% (1/20) | 文本 | 2~15 |
| `stockGenerators/li/excludedCategories` | 30.0% (6/20) | 容器 |  |
| `stockGenerators/li/excludedCategories/li` | 30.0% (6/20) | 文本 | EggsFertilized |
| `stockGenerators/li/excludedThingDefs` | 160.0% (32/20) | 容器 |  |
| `stockGenerators/li/excludedThingDefs/li` | 265.0% (53/20) | 文本 | Bioferrite / GravlitePanel / Tome |
| `stockGenerators/li/kindCountRange` | 70.0% (14/20) | 数值/文本 | 1~2 / 2~2 / 2~4 |
| `stockGenerators/li/maxTechLevelBuy` | 5.0% (1/20) | 文本 | Ultra |
| `stockGenerators/li/maxTechLevelGenerate` | 95.0% (19/20) | 文本 | Neolithic |
| `stockGenerators/li/maxWildness` | 30.0% (6/20) | 数值 | 0.70 |
| `stockGenerators/li/respectPopulationIntent` | 15.0% (3/20) | 布尔 | true |
| `stockGenerators/li/slaveKindDef` | 5.0% (1/20) | 文本 | Slave_Empire |
| `stockGenerators/li/tag` | 340.0% (68/20) | 文本 | Art / ImplantEmpireRoyal / MusicalInstrument |
| `stockGenerators/li/thingDef` | 1090.0% (218/20) | 文本 | AnimusStone / Gold / MedicineHerbal |
| `stockGenerators/li/thingDefCountRange` | 445.0% (89/20) | 数值/文本 | 0~3 / 2 / 2~4 |
| `stockGenerators/li/thingDefs` | 40.0% (8/20) | 容器 |  |
| `stockGenerators/li/thingDefs/li` | 85.0% (17/20) | 文本 | Chocolate / Cloth / Kibble |
| `stockGenerators/li/totalPriceRange` | 150.0% (30/20) | 文本 | 200~600 / 300~700 / 300~800 |
| `stockGenerators/li/tradeTag` | 435.0% (87/20) | 文本 | Artifact / BasicClothing / Clothing |
| `stockGenerators/li/tradeTagsBuy` | 65.0% (13/20) | 容器 |  |
| `stockGenerators/li/tradeTagsBuy/li` | 85.0% (17/20) | 文本 | AnimalExotic / AnimalUncommon |
| `stockGenerators/li/tradeTagsSell` | 70.0% (14/20) | 容器 |  |
| `stockGenerators/li/tradeTagsSell/li` | 140.0% (28/20) | 文本 | AnimalFarm / AnimalFighter / AnimalPet |
| `stockGenerators/li/weaponTag` | 35.0% (7/20) | 文本 | Bladelink / SpacerGun / UltratechMelee |
| `tradeCurrency` | 5.0% (1/20) | 文本 | Favor |

## 四、原版 defName 一览（共 20 个，列出前 60）

```text
`Empire_Caravan_TributeCollector`  `Caravan_Neolithic_Slaver`        `Visitor_Outlander_Standard`      `Visitor_Neolithic_Standard`    
`Caravan_Outlander_CombatSupplier`  `Orbital_CombatSupplier`          `Caravan_Neolithic_WarMerchant`   `Caravan_Outlander_PirateMerchant`
`Caravan_Neolithic_BulkGoods`     `Caravan_Neolithic_ShamanMerchant`  `Orbital_PirateMerchant`          `Caravan_Outlander_BulkGoods`   
`Empire_Caravan_TraderGeneral`    `Orbital_Empire`                  `Caravan_Outlander_Exotic`        `Base_Neolithic_Standard`       
`Orbital_BulkGoods`               `Orbital_Exotic`                  `Base_Empire_Standard`            `Base_Outlander_Standard`       
```
