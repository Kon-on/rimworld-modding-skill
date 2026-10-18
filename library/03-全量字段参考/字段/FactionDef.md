# FactionDef

- **所属线**：世界线
- **原版实例数**：39
- **字段路径数**：325
- **资料片**：Anomaly、Biotech、Core、Ideology、Odyssey、Royalty
- **原版出处**：`Core/Defs/FactionDefs/Factions_Hidden.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<FactionDef ParentName="AncientsBase">
    <defName>Ancients</defName>
    <label>neutral ancients</label>
  </FactionDef>

  
```

> 来自 `Core/Defs/FactionDefs/Factions_Hidden.xml`，defName = `Ancients`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
colorSpectrum/li                               [文本]  例：(0.11, 0.478, 0.4) / (0.25, 0.66, 0.94) / (0.35, 0.90, 0.57)
disallowedMemes/li                             [文本]  例：Blindsight / Nudism / Structure_Animist
maxPawnCostPerTotalPointsCurve/points/li       [文本]  例：(100000,10000) / (200,20) / (400,200)
pawnGroupMakers/li                             [容器]
pawnGroupMakers/li/commonality                 [数值]  例：1 / 100 / 150
pawnGroupMakers/li/kindDef                     [文本]  例：Chimeras / Combat / PsychicRitualSiege
pawnGroupMakers/li/options                     [容器]
```

## 三、全量字段表（325 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `allowedArrivalTemperatureRange` | 30.8% (12/39) | 文本 | -100~100 / -100~200 / -5~45 |
| `allowedCultures` | 28.2% (11/39) | 容器 |  |
| `allowedCultures/li` | 28.2% (11/39) | 文本 | Astropolitan / Corunan / Kriminul |
| `allowedMemes` | 10.3% (4/39) | 容器 |  |
| `allowedMemes/li` | 30.8% (12/39) | 文本 | HumanPrimacy / PainIsVirtue / Structure_Archist |
| `animalsFleeDanger` | 2.6% (1/39) | 布尔 | false |
| `apparelStuffFilter` | 15.4% (6/39) | 容器 |  |
| `apparelStuffFilter/disallowedThingDefs` | 2.6% (1/39) | 容器 |  |
| `apparelStuffFilter/disallowedThingDefs/li` | 2.6% (1/39) | 文本 | DevilstrandCloth |
| `apparelStuffFilter/stuffCategoriesToAllow` | 2.6% (1/39) | 容器 |  |
| `apparelStuffFilter/stuffCategoriesToAllow/li` | 5.1% (2/39) | 文本 | Fabric / Metallic |
| `apparelStuffFilter/thingDefs` | 12.8% (5/39) | 容器 |  |
| `apparelStuffFilter/thingDefs/li` | 17.9% (7/39) | 文本 | Cloth / Hyperweave / Plasteel |
| `arrivalLayerWhitelist` | 10.3% (4/39) | 容器 |  |
| `arrivalLayerWhitelist/li` | 17.9% (7/39) | 文本 | Orbit / Surface |
| `arrivalModeWhitelist` | 5.1% (2/39) | 容器 |  |
| `arrivalModeWhitelist/li` | 20.5% (8/39) | 文本 | CenterDrop / EdgeDrop / EdgeDropGroups |
| `autoFlee` | 12.8% (5/39) | 布尔 | false |
| `backstoryFilters` | 43.6% (17/39) | 容器 |  |
| `backstoryFilters/li` | 59.0% (23/39) | 容器 |  |
| `backstoryFilters/li/categories` | 59.0% (23/39) | 容器 |  |
| `backstoryFilters/li/categories/li` | 61.5% (24/39) | 文本 | Cult / Offworld / Outlander |
| `backstoryFilters/li/commonality` | 30.8% (12/39) | 数值 | 0.05 / 0.1 / 0.9 |
| `baseTraderKinds` | 12.8% (5/39) | 容器 |  |
| `baseTraderKinds/li` | 7.7% (3/39) | 文本 | Base_Empire_Standard / Base_Neolithic_Standard / Base_Outlander_Standard |
| `basicMemberKind` | 20.5% (8/39) | 文本 | Colonist / Researcher / Sanguophage |
| `canGenerateQuestSites` | 7.7% (3/39) | 布尔 | false |
| `canPsychicRitualSiege` | 2.6% (1/39) | 布尔 | true |
| `canRequestMilitaryAid` | 5.1% (2/39) | 布尔 | false |
| `canRequestOrbitalTrader` | 5.1% (2/39) | 布尔 | false / true |
| `canRequestTraders` | 5.1% (2/39) | 布尔 | false |
| `canSiege` | 23.1% (9/39) | 布尔 | false / true |
| `canStageAttacks` | 28.2% (11/39) | 布尔 | false / true |
| `canUseAvoidGrid` | 7.7% (3/39) | 布尔 | false |
| `caravanTraderKinds` | 12.8% (5/39) | 容器 |  |
| `caravanTraderKinds/li` | 23.1% (9/39) | 文本 | Caravan_Outlander_BulkGoods / Caravan_Outlander_CombatSupplier / Caravan_Outlander_Exotic |
| `categoryTag` | 30.8% (12/39) | 文本 | Ancient / HoraxCult / Outlander |
| `classicIdeo` | 7.7% (3/39) | 布尔 | true |
| `colorSpectrum` | 51.3% (20/39) | 容器 |  |
| `colorSpectrum/li` | 120.5% (47/39) | 文本 | (0.11, 0.478, 0.4) / (0.25, 0.66, 0.94) / (0.35, 0.90, 0.57) |
| `configurationListOrderPriority` | 43.6% (17/39) | 数值 | 10 / 1000 / 2000 |
| `defName` | 79.5% (31/39) | 文本 | Entities / HoraxCult / ResearchExpedition |
| `deityPresets` | 2.6% (1/39) | 容器 |  |
| `deityPresets/li` | 2.6% (1/39) | 容器 |  |
| `deityPresets/li/gender` | 2.6% (1/39) | 文本 | Male |
| `deityPresets/li/iconPath` | 2.6% (1/39) | 文本 | UI/Deities/DeityGeneric |
| `deityPresets/li/nameType` | 2.6% (1/39) | 容器 |  |
| `deityPresets/li/nameType/name` | 2.6% (1/39) | 文本 | Horax |
| `deityPresets/li/nameType/type` | 2.6% (1/39) | 文本 | God of the Void |
| `description` | 69.2% (27/39) | 文本 | A close-knit band of hulking, fur-bodied pirates of the yttakin xenotype. They r / A team of scientists. / A v |
| `dialogFactionGreetingHostile` | 7.7% (3/39) | 文本 | NeanderthalFactionGreetingHostile / PigFactionGreetingHostile / YttakinFactionGreetingHostile |
| `dialogFactionGreetingHostileAppreciative` | 7.7% (3/39) | 文本 | NeanderthalFactionGreetingHostileAppreciative / PigFactionGreetingHostileAppreciative / YttakinFactionGreeting |
| `dialogFactionGreetingWarm` | 7.7% (3/39) | 文本 | NeanderthalFactionGreetingWarm / PigFactionGreetingWarm / YttakinFactionGreetingWarm |
| `dialogFactionGreetingWary` | 7.7% (3/39) | 文本 | NeanderthalFactionGreetingWary / PigFactionGreetingWary / YttakinFactionGreetingWary |
| `dialogMilitaryAidSent` | 2.6% (1/39) | 文本 | PigMilitaryAidSent |
| `disallowedMemes` | 33.3% (13/39) | 容器 |  |
| `disallowedMemes/li` | 107.7% (42/39) | 文本 | Blindsight / Nudism / Structure_Animist |
| `disallowedPrecepts` | 15.4% (6/39) | 容器 |  |
| `disallowedPrecepts/li` | 51.3% (20/39) | 文本 | ApparelDesired_Soft_Subordinate / ApparelDesired_Strong_Subordinate / Nudity_Female_Mandatory |
| `disallowedRaidAgeRestrictions` | 2.6% (1/39) | 容器 |  |
| `disallowedRaidAgeRestrictions/li` | 2.6% (1/39) | 文本 | Children |
| `disallowedRaidStrategies` | 2.6% (1/39) | 容器 |  |
| `disallowedRaidStrategies/li` | 7.7% (3/39) | 文本 | ImmediateAttackBreaching / ImmediateAttackBreachingSmart / ImmediateAttackSappers |
| `displayInFactionSelection` | 10.3% (4/39) | 布尔 | false |
| `dropPodActive` | 2.6% (1/39) | 文本 | ActiveDropPodMechanoid |
| `dropPodIncoming` | 2.6% (1/39) | 文本 | DropPodIncomingMechanoidRapid |
| `earliestRaidDays` | 5.1% (2/39) | 数值 | 20 / 45 |
| `factionIconPath` | 74.4% (29/39) | 文本 | World/WorldObjects/Expanding/FierceNeanderthalTribe / World/WorldObjects/Expanding/HoraxCult / World/WorldObje |
| `factionNameMaker` | 51.3% (20/39) | 文本 | NamerFactionOutlander / NamerFactionPirateYttakin / NamerFactionTribalImpid |
| `fixedIdeo` | 2.6% (1/39) | 布尔 | true |
| `fixedLeaderKinds` | 7.7% (3/39) | 容器 |  |
| `fixedLeaderKinds/li` | 7.7% (3/39) | 文本 | Empire_Royal_Stellarch / Salvager_Elite / TradersGuild_Magister |
| `fixedName` | 10.3% (4/39) | 文本 | Ancients / Dark entities / Sorne Geneline |
| `forageabilityFactor` | 2.6% (1/39) | 数值 | 1.7 |
| `forcedMemes` | 7.7% (3/39) | 容器 |  |
| `forcedMemes/li` | 12.8% (5/39) | 文本 | Inhuman / Ritualist / Shipborn |
| `generateNewLeaderFromMapMembersOnly` | 10.3% (4/39) | 布尔 | true |
| `hidden` | 25.6% (10/39) | 布尔 | true |
| `hiddenIdeo` | 5.1% (2/39) | 布尔 | true |
| `hostileToFactionlessHumanlikes` | 10.3% (4/39) | 布尔 | true |
| `humanlikeFaction` | 10.3% (4/39) | 布尔 | false / true |
| `ideoDescription` | 2.6% (1/39) | 文本 | You see space as a grid, pure and mathematical. We know it is only the glassy su |
| `ideoName` | 2.6% (1/39) | 文本 | Nightmare Deep |
| `isPlayer` | 10.3% (4/39) | 布尔 | true |
| `label` | 79.5% (31/39) | 文本 | Research Expedition / entities / fierce neanderthal tribe |
| `layerWhitelist` | 5.1% (2/39) | 容器 |  |
| `layerWhitelist/li` | 5.1% (2/39) | 文本 | Orbit |
| `leaderForceGenerateNewPawn` | 2.6% (1/39) | 布尔 | true |
| `leaderTitle` | 25.6% (10/39) | 文本 | boss / chief / leader |
| `listOrderPriority` | 7.7% (3/39) | 数值 | 10 / 20 / 30 |
| `maxConfigurableAtWorldCreation` | 43.6% (17/39) | 数值 | 1 / 9999 |
| `maxPawnCostPerTotalPointsCurve` | 28.2% (11/39) | 容器 |  |
| `maxPawnCostPerTotalPointsCurve/points` | 28.2% (11/39) | 容器 |  |
| `maxPawnCostPerTotalPointsCurve/points/li` | 105.1% (41/39) | 文本 | (100000,10000) / (200,20) / (400,200) |
| `melaninRange` | 2.6% (1/39) | 文本 | 0~0.5 |
| `messageDefendersAttacking` | 5.1% (2/39) | 文本 | Ancient soldiers are attacking. / {0} from {1} are attacking your {2}. |
| `minSettlementTemperatureChanceCurve` | 2.6% (1/39) | 容器 |  |
| `minSettlementTemperatureChanceCurve/points` | 2.6% (1/39) | 容器 |  |
| `minSettlementTemperatureChanceCurve/points/li` | 7.7% (3/39) | 文本 | (17.9,  0.00001) / (18,    1) / (24,    1) |
| `mustStartOneEnemy` | 10.3% (4/39) | 布尔 | false |
| `naturalEnemy` | 5.1% (2/39) | 布尔 | true |
| `neutralArrivalLayerBlacklist` | 2.6% (1/39) | 容器 |  |
| `neutralArrivalLayerBlacklist/li` | 2.6% (1/39) | 文本 | Surface |
| `orbitalTraderKinds` | 5.1% (2/39) | 容器 |  |
| `orbitalTraderKinds/li` | 10.3% (4/39) | 文本 | Orbital_BulkGoods / Orbital_CombatSupplier / Orbital_Exotic |
| `pawnGroupMakers` | 41.0% (16/39) | 容器 |  |
| `pawnGroupMakers/li` | 276.9% (108/39) | 容器 |  |
| `pawnGroupMakers/li/carriers` | 15.4% (6/39) | 容器 |  |
| `pawnGroupMakers/li/carriers/Alpaca` | 15.4% (6/39) | 数值 | 2 / 2.5 |
| `pawnGroupMakers/li/carriers/Dromedary` | 15.4% (6/39) | 数值 | 5 |
| `pawnGroupMakers/li/carriers/Elephant` | 15.4% (6/39) | 数值 | 1 / 2 |
| `pawnGroupMakers/li/carriers/Muffalo` | 15.4% (6/39) | 数值 | 6 |
| `pawnGroupMakers/li/commonality` | 197.4% (77/39) | 数值 | 1 / 100 / 150 |
| `pawnGroupMakers/li/disallowedStrategies` | 15.4% (6/39) | 容器 |  |
| `pawnGroupMakers/li/disallowedStrategies/li` | 15.4% (6/39) | 文本 | Siege |
| `pawnGroupMakers/li/guards` | 15.4% (6/39) | 容器 |  |
| `pawnGroupMakers/li/guards/Empire_Fighter_Cataphract` | 2.6% (1/39) | 数值 | 1.5 |
| `pawnGroupMakers/li/guards/Empire_Fighter_Champion` | 2.6% (1/39) | 数值 | 10 |
| `pawnGroupMakers/li/guards/Empire_Fighter_Janissary` | 2.6% (1/39) | 数值 | 7 |
| `pawnGroupMakers/li/guards/Empire_Fighter_Trooper` | 2.6% (1/39) | 数值 | 10 |
| `pawnGroupMakers/li/guards/Grenadier_Destructive` | 5.1% (2/39) | 数值 | 1.5 / 10 |
| `pawnGroupMakers/li/guards/Mercenary_Elite` | 2.6% (1/39) | 数值 | 10 |
| `pawnGroupMakers/li/guards/Mercenary_Elite_Pig` | 2.6% (1/39) | 数值 | 10 |
| `pawnGroupMakers/li/guards/Mercenary_Gunner` | 2.6% (1/39) | 数值 | 10 |
| `pawnGroupMakers/li/guards/Mercenary_Gunner_Pig` | 2.6% (1/39) | 数值 | 7 |
| `pawnGroupMakers/li/guards/Mercenary_Slasher` | 5.1% (2/39) | 数值 | 10 / 7 |
| `pawnGroupMakers/li/guards/Town_Guard` | 2.6% (1/39) | 数值 | 10 |
| `pawnGroupMakers/li/guards/Town_Guard_Pig` | 2.6% (1/39) | 数值 | 10 |
| `pawnGroupMakers/li/guards/Tribal_Archer` | 7.7% (3/39) | 数值 | 1 / 10 / 8 |
| `pawnGroupMakers/li/guards/Tribal_Archer_Fire` | 2.6% (1/39) | 数值 | 10 |
| `pawnGroupMakers/li/guards/Tribal_Berserker` | 7.7% (3/39) | 数值 | 7 |
| `pawnGroupMakers/li/guards/Tribal_HeavyArcher` | 7.7% (3/39) | 数值 | 1 / 10 / 8 |
| `pawnGroupMakers/li/guards/Tribal_Hunter` | 7.7% (3/39) | 数值 | 1 / 10 / 8 |
| `pawnGroupMakers/li/guards/Tribal_Hunter_Fire` | 2.6% (1/39) | 数值 | 10 |
| `pawnGroupMakers/li/guards/Tribal_Warrior` | 5.1% (2/39) | 数值 | 7 |
| `pawnGroupMakers/li/guards/Tribal_Warrior_Fire` | 2.6% (1/39) | 数值 | 7 |
| `pawnGroupMakers/li/guards/Villager` | 5.1% (2/39) | 数值 | 3 |
| `pawnGroupMakers/li/guards/Villager_Pig` | 2.6% (1/39) | 数值 | 3 |
| `pawnGroupMakers/li/kindDef` | 276.9% (108/39) | 文本 | Chimeras / Combat / PsychicRitualSiege |
| `pawnGroupMakers/li/maxTotalPoints` | 7.7% (3/39) | 数值 | 1000 |
| `pawnGroupMakers/li/options` | 261.5% (102/39) | 容器 |  |
| `pawnGroupMakers/li/options/AncientSoldier` | 2.6% (1/39) | 数值 | 1 |
| `pawnGroupMakers/li/options/Bear_Grizzly` | 2.6% (1/39) | 数值 | 3 |
| `pawnGroupMakers/li/options/Bulbfreak` | 5.1% (2/39) | 数值 | 1 / 3 |
| `pawnGroupMakers/li/options/Chimera` | 2.6% (1/39) | 数值 | 1 |
| `pawnGroupMakers/li/options/Devourer` | 2.6% (1/39) | 数值 | 1 |
| `pawnGroupMakers/li/options/Dreadmeld` | 2.6% (1/39) | 数值 | 1 |
| `pawnGroupMakers/li/options/Drifter` | 10.3% (4/39) | 数值 | 10 |
| `pawnGroupMakers/li/options/Drifter_Yttakin` | 5.1% (2/39) | 数值 | 10 |
| `pawnGroupMakers/li/options/Empire_Fighter_Cataphract` | 7.7% (3/39) | 数值 | 2 |
| `pawnGroupMakers/li/options/Empire_Fighter_Champion` | 7.7% (3/39) | 数值 | 4 |
| `pawnGroupMakers/li/options/Empire_Fighter_Grenadier` | 2.6% (1/39) | 数值 | 2 |
| `pawnGroupMakers/li/options/Empire_Fighter_Janissary` | 7.7% (3/39) | 数值 | 3.5 |
| `pawnGroupMakers/li/options/Empire_Fighter_Trooper` | 7.7% (3/39) | 数值 | 5 |
| `pawnGroupMakers/li/options/Farmer` | 10.3% (4/39) | 数值 | 1 |
| `pawnGroupMakers/li/options/Fingerspike` | 5.1% (2/39) | 数值 | 10 |
| `pawnGroupMakers/li/options/Gorehulk` | 2.6% (1/39) | 数值 | 1 |
| `pawnGroupMakers/li/options/Grenadier_Destructive` | 38.5% (15/39) | 数值 | 0.25 / 1 / 10 |
| `pawnGroupMakers/li/options/Grenadier_EMP` | 12.8% (5/39) | 数值 | 0.25 / 0.5 |
| `pawnGroupMakers/li/options/Grenadier_Smoke` | 12.8% (5/39) | 数值 | 0.25 / 0.5 |
| `pawnGroupMakers/li/options/Grenadier_Tox` | 10.3% (4/39) | 数值 | 10 / 2 |
| `pawnGroupMakers/li/options/Horaxian_Gunner` | 2.6% (1/39) | 数值 | 2 |
| `pawnGroupMakers/li/options/Horaxian_Highthrall` | 5.1% (2/39) | 数值 | 1 |
| `pawnGroupMakers/li/options/Horaxian_Underthrall` | 5.1% (2/39) | 数值 | 8 / 9 |
| `pawnGroupMakers/li/options/Hunter` | 10.3% (4/39) | 数值 | 1 |
| `pawnGroupMakers/li/options/Locust` | 2.6% (1/39) | 数值 | 2 |
| `pawnGroupMakers/li/options/Logger` | 10.3% (4/39) | 数值 | 1 |
| `pawnGroupMakers/li/options/Mech_Apocriton` | 2.6% (1/39) | 数值 | 1 |
| `pawnGroupMakers/li/options/Mech_CentipedeBlaster` | 7.7% (3/39) | 数值 | 10 |
| `pawnGroupMakers/li/options/Mech_CentipedeBurner` | 2.6% (1/39) | 数值 | 5 |
| `pawnGroupMakers/li/options/Mech_CentipedeGunner` | 2.6% (1/39) | 数值 | 5 |
| `pawnGroupMakers/li/options/Mech_Centurion` | 2.6% (1/39) | 数值 | 2 |
| `pawnGroupMakers/li/options/Mech_Cyclops` | 2.6% (1/39) | 数值 | 5 |
| `pawnGroupMakers/li/options/Mech_Diabolus` | 2.6% (1/39) | 数值 | 1 |
| `pawnGroupMakers/li/options/Mech_Lancer` | 7.7% (3/39) | 数值 | 10 |
| `pawnGroupMakers/li/options/Mech_Legionary` | 2.6% (1/39) | 数值 | 2 |
| `pawnGroupMakers/li/options/Mech_Militor` | 7.7% (3/39) | 数值 | 10 / 20 |
| `pawnGroupMakers/li/options/Mech_Pikeman` | 7.7% (3/39) | 数值 | 10 |
| `pawnGroupMakers/li/options/Mech_Scorcher` | 5.1% (2/39) | 数值 | 5 |
| `pawnGroupMakers/li/options/Mech_Scyther` | 7.7% (3/39) | 数值 | 10 |
| `pawnGroupMakers/li/options/Mech_Termite_Breach` | 2.6% (1/39) | 数值 | 1 |
| `pawnGroupMakers/li/options/Mech_Tesseron` | 2.6% (1/39) | 数值 | 5 |
| `pawnGroupMakers/li/options/Mech_Warqueen` | 2.6% (1/39) | 数值 | 1 |
| `pawnGroupMakers/li/options/Megascarab` | 2.6% (1/39) | 数值 | 2 |
| `pawnGroupMakers/li/options/Megaspider` | 2.6% (1/39) | 数值 | 1 |
| `pawnGroupMakers/li/options/Mercenary_Elite` | 25.6% (10/39) | 数值 | 0.25 / 1 / 10 |
| `pawnGroupMakers/li/options/Mercenary_Elite_Pig` | 5.1% (2/39) | 数值 | 10 |
| `pawnGroupMakers/li/options/Mercenary_Elite_Yttakin` | 7.7% (3/39) | 数值 | 1 / 10 |
| `pawnGroupMakers/li/options/Mercenary_EliteTox` | 10.3% (4/39) | 数值 | 1 / 10 / 5 |
| `pawnGroupMakers/li/options/Mercenary_Gunner` | 25.6% (10/39) | 数值 | 0.25 / 1 / 10 |
| `pawnGroupMakers/li/options/Mercenary_Gunner_Pig` | 5.1% (2/39) | 数值 | 7 |
| `pawnGroupMakers/li/options/Mercenary_Gunner_Yttakin` | 7.7% (3/39) | 数值 | 1 / 10 |
| `pawnGroupMakers/li/options/Mercenary_GunnerTox` | 10.3% (4/39) | 数值 | 10 / 2 |
| `pawnGroupMakers/li/options/Mercenary_Heavy` | 15.4% (6/39) | 数值 | 1 / 10 / 6 |
| `pawnGroupMakers/li/options/Mercenary_Heavy_Yttakin` | 5.1% (2/39) | 数值 | 10 / 6 |
| `pawnGroupMakers/li/options/Mercenary_HeavyTox` | 7.7% (3/39) | 数值 | 10 / 6 |
| `pawnGroupMakers/li/options/Mercenary_Slasher` | 25.6% (10/39) | 数值 | 1 / 10 / 3 |
| `pawnGroupMakers/li/options/Mercenary_Slasher_Yttakin` | 7.7% (3/39) | 数值 | 10 / 3 |
| `pawnGroupMakers/li/options/Mercenary_SlasherTox` | 7.7% (3/39) | 数值 | 10 / 3 |
| `pawnGroupMakers/li/options/Mercenary_Sniper` | 20.5% (8/39) | 数值 | 10 / 7 |
| `pawnGroupMakers/li/options/Mercenary_Sniper_Yttakin` | 5.1% (2/39) | 数值 | 10 / 7 |
| `pawnGroupMakers/li/options/Metalhorror` | 2.6% (1/39) | 数值 | 1 |
| `pawnGroupMakers/li/options/Miner` | 10.3% (4/39) | 数值 | 1 |
| `pawnGroupMakers/li/options/Noctol` | 5.1% (2/39) | 数值 | 1 |
| `pawnGroupMakers/li/options/Pirate` | 15.4% (6/39) | 数值 | 10 |
| `pawnGroupMakers/li/options/Pirate_Yttakin` | 5.1% (2/39) | 数值 | 10 |
| `pawnGroupMakers/li/options/PirateBoss` | 23.1% (9/39) | 数值 | 1 / 10 / 5 |
| `pawnGroupMakers/li/options/PirateBossTox` | 12.8% (5/39) | 数值 | 1 / 10 / 5 |
| `pawnGroupMakers/li/options/Salvager_Elite` | 2.6% (1/39) | 数值 | 1 |
| `pawnGroupMakers/li/options/Salvager_Pirate` | 7.7% (3/39) | 数值 | 10 / 20 |
| `pawnGroupMakers/li/options/Salvager_Scrapper` | 2.6% (1/39) | 数值 | 5 |
| `pawnGroupMakers/li/options/Scavenger` | 10.3% (4/39) | 数值 | 10 |
| `pawnGroupMakers/li/options/Scavenger_Yttakin` | 2.6% (1/39) | 数值 | 10 |
| `pawnGroupMakers/li/options/ShamblerGorehulk` | 2.6% (1/39) | 数值 | 1 |
| `pawnGroupMakers/li/options/ShamblerSoldier` | 2.6% (1/39) | 数值 | 2.5 |
| `pawnGroupMakers/li/options/ShamblerSwarmer` | 2.6% (1/39) | 数值 | 50 |
| `pawnGroupMakers/li/options/Sightstealer` | 5.1% (2/39) | 数值 | 1 |
| `pawnGroupMakers/li/options/Spelopede` | 2.6% (1/39) | 数值 | 2 |
| `pawnGroupMakers/li/options/Thrasher` | 15.4% (6/39) | 数值 | 10 / 3 |
| `pawnGroupMakers/li/options/Thrasher_Yttakin` | 7.7% (3/39) | 数值 | 10 / 3 |
| `pawnGroupMakers/li/options/Toughspike` | 5.1% (2/39) | 数值 | 5 |
| `pawnGroupMakers/li/options/Town_Councilman` | 7.7% (3/39) | 数值 | 10 |
| `pawnGroupMakers/li/options/Town_Councilman_Pig` | 7.7% (3/39) | 数值 | 10 |
| `pawnGroupMakers/li/options/Town_Guard` | 7.7% (3/39) | 数值 | 10 |
| `pawnGroupMakers/li/options/Town_Guard_Pig` | 7.7% (3/39) | 数值 | 10 |
| `pawnGroupMakers/li/options/TradersGuild_Child` | 2.6% (1/39) | 数值 | 10 |
| `pawnGroupMakers/li/options/TradersGuild_Citizen` | 5.1% (2/39) | 数值 | 10 / 20 |
| `pawnGroupMakers/li/options/TradersGuild_Elite` | 5.1% (2/39) | 数值 | 10 / 4 |
| `pawnGroupMakers/li/options/TradersGuild_Gunner` | 7.7% (3/39) | 数值 | 10 |
| `pawnGroupMakers/li/options/TradersGuild_Heavy` | 2.6% (1/39) | 数值 | 4 |
| `pawnGroupMakers/li/options/TradersGuild_Slasher` | 5.1% (2/39) | 数值 | 7 |
| `pawnGroupMakers/li/options/Tribal_Archer` | 43.6% (17/39) | 数值 | 1 / 10 / 4 |
| `pawnGroupMakers/li/options/Tribal_Archer_Fire` | 15.4% (6/39) | 数值 | 10 / 5 |
| `pawnGroupMakers/li/options/Tribal_Berserker` | 38.5% (15/39) | 数值 | 10 / 5 / 7 |
| `pawnGroupMakers/li/options/Tribal_Breacher` | 7.7% (3/39) | 数值 | 5 |
| `pawnGroupMakers/li/options/Tribal_ChiefMelee` | 35.9% (14/39) | 数值 | 1.5 / 10 / 3 |
| `pawnGroupMakers/li/options/Tribal_ChiefRanged` | 43.6% (17/39) | 数值 | 1 / 10 / 3 |
| `pawnGroupMakers/li/options/Tribal_Child` | 7.7% (3/39) | 数值 | 10 / 8 |
| `pawnGroupMakers/li/options/Tribal_Child_Fire` | 2.6% (1/39) | 数值 | 20 |
| `pawnGroupMakers/li/options/Tribal_Farmer` | 7.7% (3/39) | 数值 | 1 |
| `pawnGroupMakers/li/options/Tribal_HeavyArcher` | 43.6% (17/39) | 数值 | 1 / 10 / 8 |
| `pawnGroupMakers/li/options/Tribal_Hunter` | 51.3% (20/39) | 数值 | 1 / 10 / 8 |
| `pawnGroupMakers/li/options/Tribal_Hunter_Fire` | 17.9% (7/39) | 数值 | 1 / 10 |
| `pawnGroupMakers/li/options/Tribal_Logger` | 7.7% (3/39) | 数值 | 1 |
| `pawnGroupMakers/li/options/Tribal_Miner` | 7.7% (3/39) | 数值 | 1 |
| `pawnGroupMakers/li/options/Tribal_Penitent` | 15.4% (6/39) | 数值 | 10 / 5 |
| `pawnGroupMakers/li/options/Tribal_Penitent_Fire` | 7.7% (3/39) | 数值 | 10 / 5 |
| `pawnGroupMakers/li/options/Tribal_Warrior` | 25.6% (10/39) | 数值 | 10 / 20 / 5 |
| `pawnGroupMakers/li/options/Tribal_Warrior_Fire` | 12.8% (5/39) | 数值 | 10 / 20 / 5 |
| `pawnGroupMakers/li/options/Trispike` | 5.1% (2/39) | 数值 | 5 |
| `pawnGroupMakers/li/options/Villager` | 7.7% (3/39) | 数值 | 10 / 20 / 5 |
| `pawnGroupMakers/li/options/Villager_Child` | 2.6% (1/39) | 数值 | 10 |
| `pawnGroupMakers/li/options/Villager_Child_Pig` | 2.6% (1/39) | 数值 | 10 |
| `pawnGroupMakers/li/options/Villager_Pig` | 7.7% (3/39) | 数值 | 10 / 20 / 5 |
| `pawnGroupMakers/li/options/Warg` | 7.7% (3/39) | 数值 | 12 / 15 / 5 |
| `pawnGroupMakers/li/options/WildBoar` | 10.3% (4/39) | 数值 | 15 / 3 / 5 |
| `pawnGroupMakers/li/traders` | 15.4% (6/39) | 容器 |  |
| `pawnGroupMakers/li/traders/Empire_Common_Trader` | 2.6% (1/39) | 数值 | 1 |
| `pawnGroupMakers/li/traders/Town_Trader` | 2.6% (1/39) | 数值 | 1 |
| `pawnGroupMakers/li/traders/Town_Trader_Pig` | 2.6% (1/39) | 数值 | 1 |
| `pawnGroupMakers/li/traders/Tribal_Trader` | 7.7% (3/39) | 数值 | 1 |
| `pawnSingular` | 59.0% (23/39) | 文本 | colonist / entity / neanderthal |
| `pawnsPlural` | 61.5% (24/39) | 文本 | colonists / cultists / entities |
| `permanentEnemy` | 20.5% (8/39) | 布尔 | false / true |
| `permanentEnemyToEveryoneExcept` | 7.7% (3/39) | 容器 |  |
| `permanentEnemyToEveryoneExcept/li` | 28.2% (11/39) | 文本 | Entities / Insect / OutlanderCivil |
| `playerInitialSettlementNameMaker` | 2.6% (1/39) | 文本 | NamerInitialSettlementColony |
| `raidCommonalityFromPointsCurve` | 17.9% (7/39) | 容器 |  |
| `raidCommonalityFromPointsCurve/points` | 17.9% (7/39) | 容器 |  |
| `raidCommonalityFromPointsCurve/points/li` | 28.2% (11/39) | 文本 | (0, 0) / (1400, 1.8) / (300,  0) |
| `raidLootMaker` | 17.9% (7/39) | 文本 | MechanoidRaidLootMaker / OutlanderRaidLootMaker / PirateRaidLootMaker |
| `raidLootValueFromPointsCurve` | 7.7% (3/39) | 容器 |  |
| `raidLootValueFromPointsCurve/points` | 7.7% (3/39) | 容器 |  |
| `raidLootValueFromPointsCurve/points/li` | 28.2% (11/39) | 文本 | (0, 0) / (100,   120) / (1000,  500) |
| `raidsForbidden` | 5.1% (2/39) | 布尔 | true |
| `recipePrerequisiteTags` | 2.6% (1/39) | 容器 |  |
| `recipePrerequisiteTags/li` | 2.6% (1/39) | 文本 | Tribal |
| `replacesFaction` | 10.3% (4/39) | 文本 | OutlanderRough / Pirate / TribeRough |
| `requiredCountAtGameStart` | 46.2% (18/39) | 数值 | 0 / 1 |
| `requiredMemes` | 25.6% (10/39) | 容器 |  |
| `requiredMemes/li` | 43.6% (17/39) | 文本 | AnimalPersonhood / Bloodfeeding / Cannibal |
| `requiredPreceptsOnly` | 2.6% (1/39) | 布尔 | true |
| `rescueesCanJoin` | 2.6% (1/39) | 布尔 | true |
| `royalFavorIconPath` | 2.6% (1/39) | 文本 | UI/Icons/RoyalFavor |
| `royalFavorLabel` | 2.6% (1/39) | 文本 | honor |
| `royalTitleInheritanceRelations` | 2.6% (1/39) | 容器 |  |
| `royalTitleInheritanceRelations/li` | 25.6% (10/39) | 文本 | Child / Grandchild / GreatGrandchild |
| `royalTitleInheritanceWorkerClass` | 2.6% (1/39) | 文本 | RoyalTitleInheritanceWorker |
| `royalTitleTags` | 2.6% (1/39) | 容器 |  |
| `royalTitleTags/li` | 2.6% (1/39) | 文本 | EmpireTitle |
| `settlementGenerationWeight` | 15.4% (6/39) | 数值 | 1 |
| `settlementNameMaker` | 46.2% (18/39) | 文本 | NamerSettlementOutlander / NamerSettlementPirateYttakin / NamerSettlementTribalImpid |
| `settlementTexturePath` | 38.5% (15/39) | 文本 | World/WorldObjects/DefaultSettlement / World/WorldObjects/TribalSettlement |
| `startingCountAtWorldCreation` | 7.7% (3/39) | 数值 | 0 |
| `startingResearchTags` | 10.3% (4/39) | 容器 |  |
| `startingResearchTags/li` | 10.3% (4/39) | 文本 | ClassicStart / TribalStart |
| `startingTechprintsResearchTags` | 10.3% (4/39) | 容器 |  |
| `startingTechprintsResearchTags/li` | 20.5% (8/39) | 文本 | ClassicStart / ClassicStartTechprints / TribalStart |
| `structureMemeWeights` | 15.4% (6/39) | 容器 |  |
| `structureMemeWeights/Structure_Animist` | 2.6% (1/39) | 数值 | 4 |
| `structureMemeWeights/Structure_Archist` | 12.8% (5/39) | 数值 | 1 / 10 |
| `structureMemeWeights/Structure_Ideological` | 10.3% (4/39) | 数值 | 1 |
| `structureMemeWeights/Structure_OriginBuddhist` | 5.1% (2/39) | 数值 | 1 |
| `structureMemeWeights/Structure_OriginChristian` | 5.1% (2/39) | 数值 | 1 |
| `structureMemeWeights/Structure_OriginHindu` | 5.1% (2/39) | 数值 | 1 |
| `structureMemeWeights/Structure_OriginIslamic` | 5.1% (2/39) | 数值 | 1 |
| `structureMemeWeights/Structure_TheistAbstract` | 10.3% (4/39) | 数值 | 1 / 2 |
| `structureMemeWeights/Structure_TheistEmbodied` | 10.3% (4/39) | 数值 | 1 |
| `styles` | 7.7% (3/39) | 容器 |  |
| `styles/li` | 12.8% (5/39) | 文本 | Horaxian / Morbid / Techist |
| `techLevel` | 48.7% (19/39) | 文本 | Animal / Industrial / Spacer |
| `visitorTraderKinds` | 10.3% (4/39) | 容器 |  |
| `visitorTraderKinds/li` | 5.1% (2/39) | 文本 | Visitor_Neolithic_Standard / Visitor_Outlander_Standard |
| `xenotypeSet` | 33.3% (13/39) | 容器 |  |
| `xenotypeSet/xenotypeChances` | 33.3% (13/39) | 容器 |  |
| `xenotypeSet/xenotypeChances/Dirtmole` | 15.4% (6/39) | 数值 | 0.05 / 0.1 |
| `xenotypeSet/xenotypeChances/Genie` | 23.1% (9/39) | 数值 | 0.025 / 0.05 / 0.1 |
| `xenotypeSet/xenotypeChances/Highmate` | 7.7% (3/39) | 数值 | 0.025 |
| `xenotypeSet/xenotypeChances/Hussar` | 23.1% (9/39) | 数值 | 0.05 / 0.15 |
| `xenotypeSet/xenotypeChances/Impid` | 7.7% (3/39) | 数值 | 0.025 / 999 |
| `xenotypeSet/xenotypeChances/Neanderthal` | 20.5% (8/39) | 数值 | 0.025 / 0.05 / 999 |
| `xenotypeSet/xenotypeChances/Pigskin` | 15.4% (6/39) | 数值 | 0.025 / 0.05 / 999 |
| `xenotypeSet/xenotypeChances/Starjack` | 17.9% (7/39) | 数值 | 0.025 / 0.1 / 0.25 |
| `xenotypeSet/xenotypeChances/Waster` | 5.1% (2/39) | 数值 | 0.025 / 0.725 |
| `xenotypeSet/xenotypeChances/Yttakin` | 15.4% (6/39) | 数值 | 0.025 / 0.05 / 999 |

## 四、原版 defName 一览（共 39 个，列出前 60）

```text
`Ancients`                        `AncientsHostile`                 `OutlanderRough`                  `TribeRough`                    
`TribeSavage`                     ``                                ``                                ``                              
`OutlanderCivil`                  ``                                ``                                `CannibalPirate`                
`TribeCivil`                      `TribeCannibal`                   `NudistTribe`                     `ResearchExpedition`            
`PlayerColony`                    `GravshipCrew`                    `PlayerTribe`                     `Insect`                        
`Pilgrims`                        `OutlanderRefugee`                `Sanguophages`                    ``                              
`Beggars`                         `HoraxCult`                       `OutlanderRoughPig`               `Entities`                      
`Salvagers`                       `Mechanoid`                       `TradersGuild`                    `PirateYttakin`                 
`TribeRoughNeanderthal`           ``                                `TribeSavageImpid`                `PirateWaster`                  
`Pirate`                          `Empire`                          ``                              
```
