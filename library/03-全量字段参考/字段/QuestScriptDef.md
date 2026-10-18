# QuestScriptDef

- **所属线**：世界线
- **原版实例数**：156
- **字段路径数**：1008
- **资料片**：Anomaly、Biotech、Core、Ideology、Odyssey、Royalty
- **原版出处**：`Anomaly/Defs/QuestScriptDefs/Script_CreepjoinerJoins.xml`、`Royalty/Defs/QuestScriptDefs/Scripts_Utility_TransportShip.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<QuestScriptDef ParentName="CreepjoinerArrivalBase">
    <defName>CreepJoinerArrival</defName>
    <root Class="QuestNode_Root_Creepjoiner_Arrival"/>
  </QuestScriptDef>

  
```

> 来自 `Anomaly/Defs/QuestScriptDefs/Script_CreepjoinerJoins.xml`，defName = `CreepJoinerArrival`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：CreepJoinerArrival / CreepJoinerArrival_Metalhorror / EndGame_VoidMonolith
questContentRules/rulesStrings/li              [文本]  例：darknessStartedLetterLabel->Unnatural darkness / darknessStartedLetterText->An unnatural darkness has descended. Inhuman things m / structuresArrivingAlertExplanation->The boundary between our world and the void 
questDescriptionRules/rulesStrings/li          [文本]  例：questDescription-> / questDescription->You've intercepted a distress signal from a nearby camp of [fa / questDescription->Your colonists all feel a psychic message echoing. It's a sign
questNameRules/rulesStrings/li                 [文本]  例：questDescription->creepjoiner / questName->Anomaly monolith / questName->Distress signal
root                                           [容器]
root/nodes/li                                  [容器]
root/nodes/li/allowedLandmarks/li              [文本]  例：Lake / LakeWithIsland / LakeWithIslands
root/nodes/li/node                             [容器]
root/nodes/li/node/nodes/li                    [容器]
```

## 三、全量字段表（1008 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `affectedByPoints` | 2.6% (4/156) | 布尔 | false |
| `affectedByPopulation` | 2.6% (4/156) | 布尔 | true |
| `autoAccept` | 35.9% (56/156) | 布尔 | true |
| `canGiveRoyalFavor` | 7.7% (12/156) | 布尔 | true |
| `canOccurOnAllPlanetLayers` | 11.5% (18/156) | 布尔 | true |
| `decreeSelectionWeight` | 0.6% (1/156) | 数值 | 1 |
| `decreeTags` | 0.6% (1/156) | 容器 |  |
| `decreeTags/li` | 0.6% (1/156) | 文本 | All |
| `defaultChallengeRating` | 14.1% (22/156) | 数值 | 1 / 3 / 4 |
| `defaultCharity` | 9.0% (14/156) | 布尔 | true |
| `defaultHidden` | 12.2% (19/156) | 布尔 | false / true |
| `defName` | 96.8% (151/156) | 文本 | CreepJoinerArrival / CreepJoinerArrival_Metalhorror / EndGame_VoidMonolith |
| `endOnColonyMove` | 1.3% (2/156) | 布尔 | false |
| `epic` | 0.6% (1/156) | 布尔 | true |
| `epicParent` | 2.6% (4/156) | 文本 | RelicHunt |
| `everAcceptableInSpace` | 9.0% (14/156) | 布尔 | true |
| `expireDaysRange` | 20.5% (32/156) | 数值/文本 | 0.3 / 2 / 20~30 |
| `failedOrExpiredHistoryEvent` | 9.0% (14/156) | 文本 | CharityRefused_IntroWimp / CharityRefused_RefugeePodCrash / CharityRefused_ThreatReward_Joiner |
| `givenBy` | 7.7% (12/156) | 容器 |  |
| `givenBy/li` | 15.4% (24/156) | 文本 | Beggars / OrbitalScanner / Reading |
| `hideInvolvedFactionsInfo` | 3.2% (5/156) | 布尔 | true |
| `hideOnCleanup` | 0.6% (1/156) | 布尔 | true |
| `isRootSpecial` | 30.8% (48/156) | 布尔 | true |
| `minRefireDays` | 4.5% (7/156) | 数值 | 120 / 200 / 240 |
| `questAvailableLetterDef` | 0.6% (1/156) | 文本 | NewQuest_ThreatBig |
| `questAvailableLetterLabel` | 5.8% (9/156) | 文本 | Gravcore detected: Ancient reactor / Gravcore detected: Cave entrance / Gravcore detected: Mechanoid platform |
| `questAvailableLetterTextIsDescription` | 9.0% (14/156) | 布尔 | true |
| `questContentRules` | 16.7% (26/156) | 容器 |  |
| `questContentRules/rulesStrings` | 16.7% (26/156) | 容器 |  |
| `questContentRules/rulesStrings/li` | 137.2% (214/156) | 文本 | darknessStartedLetterLabel->Unnatural darkness / darknessStartedLetterText->An unnatural darkness has descende |
| `questDescriptionAndNameRules` | 7.7% (12/156) | 容器 |  |
| `questDescriptionAndNameRules/rulesStrings` | 7.7% (12/156) | 容器 |  |
| `questDescriptionAndNameRules/rulesStrings/li` | 19.2% (30/156) | 文本 | complex->complex / complex->compound / complex->installation |
| `questDescriptionRules` | 77.6% (121/156) | 容器 |  |
| `questDescriptionRules/include` | 4.5% (7/156) | 容器 |  |
| `questDescriptionRules/include/li` | 4.5% (7/156) | 文本 | QuestConstructionDescriptionCommon / QuestHospitalityCommon |
| `questDescriptionRules/rulesStrings` | 77.6% (121/156) | 容器 |  |
| `questDescriptionRules/rulesStrings/li` | 359.6% (561/156) | 文本 | questDescription-> / questDescription->You've intercepted a distress signal from a nearby camp of [fa / questD |
| `questNameRules` | 68.6% (107/156) | 容器 |  |
| `questNameRules/include` | 1.3% (2/156) | 容器 |  |
| `questNameRules/include/li` | 1.3% (2/156) | 文本 | QuestConstructionNameCommon |
| `questNameRules/rulesFiles` | 1.9% (3/156) | 容器 |  |
| `questNameRules/rulesFiles/li` | 1.9% (3/156) | 文本 | place_end->WordParts/PlaceEndings |
| `questNameRules/rulesStrings` | 67.3% (105/156) | 容器 |  |
| `questNameRules/rulesStrings/li` | 528.2% (824/156) | 文本 | questDescription->creepjoiner / questName->Anomaly monolith / questName->Distress signal |
| `questSubjectRules` | 7.0% (11/156) | 容器 |  |
| `questSubjectRules/rulesStrings` | 7.0% (11/156) | 容器 |  |
| `questSubjectRules/rulesStrings/li` | 54.5% (85/156) | 文本 | subject->alpha thrumbos / subject->rare animals / subject->rare thrumbos |
| `randomlySelectable` | 7.7% (12/156) | 布尔 | false |
| `root` | 96.8% (151/156) | 容器 |  |
| `root/allowedBiomes` | 3.2% (5/156) | 容器 |  |
| `root/allowedBiomes/li` | 16.7% (26/156) | 文本 | ExtremeDesert / GlacialPlain / Glowforest |
| `root/chance` | 0.6% (1/156) | 数值 | 0.5 |
| `root/combatPointsFactor` | 0.6% (1/156) | 数值 | 0.5 |
| `root/curve` | 0.6% (1/156) | 容器 |  |
| `root/curve/points` | 0.6% (1/156) | 容器 |  |
| `root/curve/points/li` | 3.9% (6/156) | 文本 | 1600, 2600 / 200, 550 / 400, 1100 |
| `root/customLetterLabel` | 0.6% (1/156) | 文本 | $customLetterLabel |
| `root/customLetterLabelRules` | 0.6% (1/156) | 文本 | $customLetterLabelRules |
| `root/customLetterText` | 0.6% (1/156) | 文本 | $customLetterText |
| `root/customLetterTextRules` | 0.6% (1/156) | 文本 | $customLetterTextRules |
| `root/distanceFromColonyRange` | 5.8% (9/156) | 文本 | 10~60 / 2~8 / 3~15 |
| `root/elseNode` | 0.6% (1/156) | 容器 |  |
| `root/elseNode/nodes` | 0.6% (1/156) | 容器 |  |
| `root/elseNode/nodes/li` | 1.3% (2/156) | 容器 |  |
| `root/elseNode/nodes/li/checkDiseaseContractChance` | 0.6% (1/156) | 布尔 | true |
| `root/elseNode/nodes/li/hediffDef` | 0.6% (1/156) | 文本 | $lodgersDisease |
| `root/elseNode/nodes/li/name` | 0.6% (1/156) | 文本 | lodgersAreSick |
| `root/elseNode/nodes/li/partsToAffect` | 0.6% (1/156) | 文本 | $lodgersDiseasePartsToAffect |
| `root/elseNode/nodes/li/pawns` | 0.6% (1/156) | 文本 | $lodgers |
| `root/elseNode/nodes/li/value` | 0.6% (1/156) | 布尔 | true |
| `root/faction` | 0.6% (1/156) | 文本 | $siteFaction |
| `root/factionsToDrawLeaderFrom` | 0.6% (1/156) | 容器 |  |
| `root/factionsToDrawLeaderFrom/li` | 1.9% (3/156) | 文本 | Empire / OutlanderCivil / OutlanderRough |
| `root/hiddenSitePartsPossible` | 0.6% (1/156) | 文本 | $hiddenSitePartsPossible |
| `root/layer` | 6.4% (10/156) | 文本 | Orbit / Surface |
| `root/maxHilliness` | 0.6% (1/156) | 文本 | SmallHills |
| `root/mechGroups` | 0.6% (1/156) | 容器 |  |
| `root/mechGroups/li` | 1.9% (3/156) | 容器 |  |
| `root/mechGroups/li/options` | 1.9% (3/156) | 容器 |  |
| `root/mechGroups/li/options/li` | 3.9% (6/156) | 容器 |  |
| `root/mechGroups/li/options/li/pawnKind` | 3.9% (6/156) | 文本 | Mech_Militor / Mech_Scorcher / Mech_Scyther |
| `root/mechGroups/li/options/li/requireOneOf` | 1.9% (3/156) | 布尔 | true |
| `root/mechGroups/li/options/li/weight` | 3.9% (6/156) | 数值 | 1 / 2 |
| `root/mechTypes` | 0.6% (1/156) | 容器 |  |
| `root/mechTypes/li` | 1.3% (2/156) | 文本 | Mech_Constructoid / Mech_Lifter |
| `root/minHilliness` | 0.6% (1/156) | 文本 | Mountainous |
| `root/node` | 0.6% (1/156) | 容器 |  |
| `root/node/nodes` | 0.6% (1/156) | 容器 |  |
| `root/node/nodes/li` | 1.3% (2/156) | 容器 |  |
| `root/node/nodes/li/allowBleedingWounds` | 0.6% (1/156) | 布尔 | false |
| `root/node/nodes/li/name` | 0.6% (1/156) | 文本 | lodgersAreDowned |
| `root/node/nodes/li/pawns` | 0.6% (1/156) | 文本 | $lodgers |
| `root/node/nodes/li/value` | 0.6% (1/156) | 布尔 | true |
| `root/nodes` | 56.4% (88/156) | 容器 |  |
| `root/nodes/li` | 474.4% (740/156) | 容器 |  |
| `root/nodes/li/acceptChildren` | 0.6% (1/156) | 文本 | $acceptChildren |
| `root/nodes/li/acceptColonists` | 1.3% (2/156) | 文本 | $acceptColonists |
| `root/nodes/li/addToList` | 1.9% (3/156) | 文本 | thingsToDrop |
| `root/nodes/li/adultChance` | 0.6% (1/156) | 数值 | 0.5 |
| `root/nodes/li/aggressive` | 0.6% (1/156) | 文本 | Assault |
| `root/nodes/li/allowActiveTradeRequest` | 0.6% (1/156) | 布尔 | false |
| `root/nodes/li/allowAlly` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/allowedLandmarks` | 8.3% (13/156) | 容器 |  |
| `root/nodes/li/allowedLandmarks/li` | 238.5% (372/156) | 文本 | Lake / LakeWithIsland / LakeWithIslands |
| `root/nodes/li/allowEnemy` | 5.8% (9/156) | 布尔 | false / true |
| `root/nodes/li/allowNeutral` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/allowPermanentEnemy` | 0.6% (1/156) | 布尔 | false |
| `root/nodes/li/allowPermanentEnemyFaction` | 1.3% (2/156) | 布尔 | false |
| `root/nodes/li/allowPregnant` | 1.3% (2/156) | 布尔 | false / true |
| `root/nodes/li/amount` | 0.6% (1/156) | 文本 | $royalFavorReward |
| `root/nodes/li/animalsToHuntCountRandomFactorRange` | 0.6% (1/156) | 文本 | 0.85~1.15 |
| `root/nodes/li/arrivalMode` | 1.3% (2/156) | 文本 | $arrivalMode / RandomDrop |
| `root/nodes/li/biocodeApparelChance` | 0.6% (1/156) | 数值 | 1 |
| `root/nodes/li/biocodeWeaponChance` | 0.6% (1/156) | 数值 | 1 |
| `root/nodes/li/canBeSpace` | 13.5% (21/156) | 布尔/文本 | $canBeSpace / false / true |
| `root/nodes/li/canRetargetAnyMap` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/canSelectComboLandmarks` | 1.3% (2/156) | 布尔 | false |
| `root/nodes/li/canSendLetter` | 0.6% (1/156) | 布尔 | false |
| `root/nodes/li/canSendMessage` | 0.6% (1/156) | 布尔 | false |
| `root/nodes/li/canTimeoutOrFlee` | 0.6% (1/156) | 文本 | $canTimeoutOrFlee |
| `root/nodes/li/challengeRating` | 1.3% (2/156) | 文本 | $challengeRating |
| `root/nodes/li/chancesCurve` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/chancesCurve/points` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/chancesCurve/points/li` | 3.9% (6/156) | 文本 | (0, 0) / (1, 7) / (2, 1) |
| `root/nodes/li/change` | 0.6% (1/156) | 数值 | -100 |
| `root/nodes/li/childChance` | 0.6% (1/156) | 数值 | 0.5 |
| `root/nodes/li/choices` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/choices/li` | 2.6% (4/156) | 容器 |  |
| `root/nodes/li/choices/li/categoryTag` | 1.3% (2/156) | 文本 | Outlander / Tribal |
| `root/nodes/li/choices/li/factionDef` | 1.3% (2/156) | 文本 | Empire / Pirate |
| `root/nodes/li/choices/li/pawnKinds` | 2.6% (4/156) | 容器 |  |
| `root/nodes/li/choices/li/pawnKinds/li` | 9.6% (15/156) | 文本 | Mercenary_Elite_Acidifier / Mercenary_Gunner_Acidifier / Mercenary_Slasher_Acidifier |
| `root/nodes/li/clampRangeBySiteParts` | 1.3% (2/156) | 布尔 | true |
| `root/nodes/li/colonyPercentage` | 0.6% (1/156) | 文本 | $colonyPercentageToLend |
| `root/nodes/li/contents` | 3.2% (5/156) | 文本 | $contents / $itemPodsContents / $thingsToDrop |
| `root/nodes/li/convertTo` | 1.9% (3/156) | 文本 | Boolean |
| `root/nodes/li/count` | 1.9% (3/156) | 文本 | $countToHunt / $countToProduce / $harvestItemCount |
| `root/nodes/li/curve` | 3.2% (5/156) | 文本 | $pointsCurve |
| `root/nodes/li/curve/points` | 2.6% (4/156) | 容器 |  |
| `root/nodes/li/curve/points/li` | 8.3% (13/156) | 文本 | ( 800, 1) / 0, 1.15 / 300000, 0.85 |
| `root/nodes/li/customLetterLabel` | 3.2% (5/156) | 文本 | $customLetterLabel |
| `root/nodes/li/customLetterLabelRules` | 3.2% (5/156) | 文本 | $customLetterLabelRules |
| `root/nodes/li/customLetterText` | 3.9% (6/156) | 文本 | $customLetterText / {BASETEXT}\n\nBecause you accepted [asker_nameDef], [asker_factionName] has beco |
| `root/nodes/li/customLetterTextRules` | 3.2% (5/156) | 文本 | $customLetterTextRules |
| `root/nodes/li/def` | 79.5% (124/156) | 文本 | Util_AdjustPointsForDistantFight / Util_GenerateSite / Util_GetDefaultRewardValueFromPoints |
| `root/nodes/li/defsToExcludeFromHyperlinks` | 0.6% (1/156) | 文本 | Human |
| `root/nodes/li/delayTicks` | 30.1% (47/156) | 数值/文本 | $(randInt(12,28)*60000) / $(randInt(7,15)*60000) / $timeout |
| `root/nodes/li/desperateIgnoreDistance` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/destroyOnCleanup` | 1.3% (2/156) | 布尔 | true |
| `root/nodes/li/disabledWorkTags` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/disabledWorkTags/li` | 2.6% (4/156) | 文本 | Animals / Intellectual / Social |
| `root/nodes/li/distanceFromColonyRange` | 3.9% (6/156) | 文本 | 1~3 / 20~80 / 2~8 |
| `root/nodes/li/dontRequest` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/dontRequest/li` | 1.3% (2/156) | 文本 | Gravcore / Leather_Patch |
| `root/nodes/li/downside` | 0.6% (1/156) | 文本 | Metalhorror |
| `root/nodes/li/duration` | 1.9% (3/156) | 文本 | $duration / $gameConditionDuration / $timeout |
| `root/nodes/li/elseNode` | 32.0% (50/156) | 容器 |  |
| `root/nodes/li/elseNode/chance` | 0.6% (1/156) | 数值 | 0.5 |
| `root/nodes/li/elseNode/curve` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/elseNode/curve/points` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/elseNode/curve/points/li` | 5.1% (8/156) | 文本 | 1000,  300 / 2000,  425 / 35,   35 |
| `root/nodes/li/elseNode/def` | 1.9% (3/156) | 文本 | Hospitality_Util_DecideRandomLodgerCount |
| `root/nodes/li/elseNode/elseNode` | 2.6% (4/156) | 容器 |  |
| `root/nodes/li/elseNode/elseNode/def` | 0.6% (1/156) | 文本 | Util_MaybeApplyGoodwillForMood |
| `root/nodes/li/elseNode/elseNode/elseNode` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/elseNode/elseNode/elseNode/chance` | 0.6% (1/156) | 文本 | $helpersChance |
| `root/nodes/li/elseNode/elseNode/elseNode/elseNode` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/elseNode/elseNode/elseNode/elseNode/name` | 0.6% (1/156) | 文本 | helpersCount |
| `root/nodes/li/elseNode/elseNode/elseNode/elseNode/value` | 0.6% (1/156) | 数值 | 0 |
| `root/nodes/li/elseNode/elseNode/elseNode/node` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li` | 7.0% (11/156) | 容器 |  |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/areHelpers` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/def` | 0.6% (1/156) | 文本 | Util_ChooseRandomQuestHelperKind |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/elseNode` | 1.3% (2/156) | 容器 |  |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/elseNode/name` | 0.6% (1/156) | 文本 | helpersLeaveAfterTicks |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/elseNode/nodes` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/elseNode/nodes/li` | 1.3% (2/156) | 容器 |  |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/elseNode/nodes/li/curve` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/elseNode/nodes/li/curve/points` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/elseNode/nodes/li/curve/points/li` | 2.6% (4/156) | 文本 | (1000, 6) / (2000, 9) / (260,  1) |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/elseNode/nodes/li/name` | 0.6% (1/156) | 文本 | helpersCount |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/elseNode/nodes/li/roundRandom` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/elseNode/nodes/li/storeAs` | 0.6% (1/156) | 文本 | helpersMaxCount |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/elseNode/nodes/li/value` | 1.3% (2/156) | 文本 | $(randInt(1, $helpersMaxCount)) / $points |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/elseNode/value` | 0.6% (1/156) | 文本 | $(10*60000) |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/factionOf` | 0.6% (1/156) | 文本 | $asker |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/factionType` | 0.6% (1/156) | 文本 | HomeFaction |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/inSignalRemovePawn` | 0.6% (1/156) | 文本 | helpers.RanWild |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/inSignalsRemovePawn` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/inSignalsRemovePawn/li` | 1.3% (2/156) | 文本 | lodgers.BecameMutant / lodgers.RanWild |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/joinPlayer` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/loopCount` | 0.6% (1/156) | 文本 | $helpersCount |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/name` | 1.3% (2/156) | 文本 | helpersCount / helpersLeaveAfterTicks |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/node` | 1.9% (3/156) | 容器 |  |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/node/addToList` | 0.6% (1/156) | 文本 | helpers |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/node/allowPregnant` | 0.6% (1/156) | 布尔 | false |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/node/biocodeApparelChance` | 0.6% (1/156) | 数值 | 1 |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/node/biocodeWeaponChance` | 0.6% (1/156) | 数值 | 1 |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/node/def` | 0.6% (1/156) | 文本 | Util_ArriveByDropPodsOrShuttle |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/node/delayTicks` | 0.6% (1/156) | 文本 | $helpersLeaveAfterTicks |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/node/faction` | 0.6% (1/156) | 文本 | $askerFaction |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/node/giveDependentDrugs` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/node/kindDef` | 0.6% (1/156) | 文本 | $helperKind |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/node/mustBeCapableOfViolence` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/node/node` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/node/node/nodes` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/node/node/nodes/li` | 1.3% (2/156) | 容器 |  |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/node/node/nodes/li/inSignalRemovePawn` | 0.6% (1/156) | 文本 | helpers.RanWild |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/node/node/nodes/li/node` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/node/node/nodes/li/node/filterDeadPawnsFromLookTargets` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/node/node/nodes/li/node/label` | 0.6% (1/156) | 文本 | [helpersLabelSingOrPlural] leaving |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/node/node/nodes/li/node/lookTargets` | 0.6% (1/156) | 文本 | $helpers |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/node/node/nodes/li/node/text` | 0.6% (1/156) | 文本 | The [helpersLabelSingOrPlural] sent by [asker_nameDef] to aid you [helpersHasHav |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/node/node/nodes/li/pawns` | 1.3% (2/156) | 文本 | $helpers |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/node/node/nodes/li/sendStandardLetter` | 0.6% (1/156) | 布尔 | false |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/node/parms` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/node/parms/arrivingPawns` | 0.6% (1/156) | 文本 | $helpers |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/node/parms/arrivingPawnsLabelDef` | 0.6% (1/156) | 文本 | the [helpersLabelSingOrPlural] |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/node/parms/customLetterLabel` | 0.6% (1/156) | 文本 | [helpersLabelSingOrPlural] arrived |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/node/parms/customLetterText` | 0.6% (1/156) | 文本 | The [helpersLabelSingOrPlural] sent by [asker_nameDef] [helpersHasHave] arrived  |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/node/prohibitedTraits` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/node/prohibitedTraits/li` | 0.6% (1/156) | 文本 | Greedy |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/parms` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/parms/factionOf` | 0.6% (1/156) | 文本 | $asker |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/pawns` | 2.6% (4/156) | 文本 | $helpers |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/sendStandardLetter` | 0.6% (1/156) | 布尔 | false |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/storeAs` | 0.6% (1/156) | 文本 | askerFaction |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/thing` | 0.6% (1/156) | 文本 | $asker |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/value` | 0.6% (1/156) | 文本 | $generateShuttleOrPods |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/value1` | 0.6% (1/156) | 文本 | $helpersLeaveAfterTicks |
| `root/nodes/li/elseNode/elseNode/elseNode/node/nodes/li/value2` | 0.6% (1/156) | 数值 | 0 |
| `root/nodes/li/elseNode/elseNode/node` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/elseNode/elseNode/node/name` | 0.6% (1/156) | 文本 | helpersCount |
| `root/nodes/li/elseNode/elseNode/node/value` | 0.6% (1/156) | 数值 | 0 |
| `root/nodes/li/elseNode/elseNode/nodes` | 1.3% (2/156) | 容器 |  |
| `root/nodes/li/elseNode/elseNode/nodes/li` | 2.6% (4/156) | 容器 |  |
| `root/nodes/li/elseNode/elseNode/nodes/li/elseNode` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/elseNode/elseNode/nodes/li/elseNode/elseNode` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/elseNode/elseNode/nodes/li/elseNode/elseNode/inSignal` | 0.6% (1/156) | 文本 | monumentMarker.MonumentCompleted |
| `root/nodes/li/elseNode/elseNode/nodes/li/elseNode/elseNode/node` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/elseNode/elseNode/nodes/li/elseNode/elseNode/node/nodes` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/elseNode/elseNode/nodes/li/elseNode/elseNode/node/nodes/li` | 1.9% (3/156) | 容器 |  |
| `root/nodes/li/elseNode/elseNode/nodes/li/elseNode/elseNode/node/nodes/li/delayTicks` | 0.6% (1/156) | 文本 | $keepMonumentTicks |
| `root/nodes/li/elseNode/elseNode/nodes/li/elseNode/elseNode/node/nodes/li/expiryInfoPart` | 0.6% (1/156) | 文本 | Do not destroy the monument for {0} |
| `root/nodes/li/elseNode/elseNode/nodes/li/elseNode/elseNode/node/nodes/li/expiryInfoPartTip` | 0.6% (1/156) | 文本 | Do not destroy the monument for {0} |
| `root/nodes/li/elseNode/elseNode/nodes/li/elseNode/elseNode/node/nodes/li/inSignal` | 0.6% (1/156) | 文本 | monumentMarker.MonumentDestroyed |
| `root/nodes/li/elseNode/elseNode/nodes/li/elseNode/elseNode/node/nodes/li/inspectString` | 0.6% (1/156) | 文本 | Keep monument {0} |
| `root/nodes/li/elseNode/elseNode/nodes/li/elseNode/elseNode/node/nodes/li/inspectStringTargets` | 0.6% (1/156) | 文本 | $monumentMarker |
| `root/nodes/li/elseNode/elseNode/nodes/li/elseNode/elseNode/node/nodes/li/label` | 0.6% (1/156) | 文本 | Monument completed |
| `root/nodes/li/elseNode/elseNode/nodes/li/elseNode/elseNode/node/nodes/li/letterDef` | 0.6% (1/156) | 文本 | PositiveEvent |
| `root/nodes/li/elseNode/elseNode/nodes/li/elseNode/elseNode/node/nodes/li/node` | 1.3% (2/156) | 容器 |  |
| `root/nodes/li/elseNode/elseNode/nodes/li/elseNode/elseNode/node/nodes/li/node/nodes` | 1.3% (2/156) | 容器 |  |
| `root/nodes/li/elseNode/elseNode/nodes/li/elseNode/elseNode/node/nodes/li/node/nodes/li` | 2.6% (4/156) | 容器 |  |
| `root/nodes/li/elseNode/elseNode/nodes/li/elseNode/elseNode/node/nodes/li/node/nodes/li/change` | 0.6% (1/156) | 文本 | $goodwillChangeIfMonumentDestroyed |
| `root/nodes/li/elseNode/elseNode/nodes/li/elseNode/elseNode/node/nodes/li/node/nodes/li/factionOf` | 0.6% (1/156) | 文本 | $asker |
| `root/nodes/li/elseNode/elseNode/nodes/li/elseNode/elseNode/node/nodes/li/node/nodes/li/label` | 0.6% (1/156) | 文本 | Monument destroyed |
| `root/nodes/li/elseNode/elseNode/nodes/li/elseNode/elseNode/node/nodes/li/node/nodes/li/outcome` | 1.3% (2/156) | 文本 | Fail / Success |
| `root/nodes/li/elseNode/elseNode/nodes/li/elseNode/elseNode/node/nodes/li/node/nodes/li/reason` | 0.6% (1/156) | 文本 | MonumentDestroyed |
| `root/nodes/li/elseNode/elseNode/nodes/li/elseNode/elseNode/node/nodes/li/node/nodes/li/text` | 0.6% (1/156) | 文本 | [asker_nameDef] is offended that you allowed the monument to be ruined so soon a |
| `root/nodes/li/elseNode/elseNode/nodes/li/elseNode/elseNode/node/nodes/li/text` | 0.6% (1/156) | 文本 | You completed construction of the monument.\n\nYou must not destroy it for at le |
| `root/nodes/li/elseNode/elseNode/nodes/li/elseNode/node` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/elseNode/elseNode/nodes/li/elseNode/node/nodes` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/elseNode/elseNode/nodes/li/elseNode/node/nodes/li` | 1.3% (2/156) | 容器 |  |
| `root/nodes/li/elseNode/elseNode/nodes/li/elseNode/node/nodes/li/inSignal` | 0.6% (1/156) | 文本 | monumentMarker.MonumentCompleted |
| `root/nodes/li/elseNode/elseNode/nodes/li/elseNode/node/nodes/li/name` | 0.6% (1/156) | 文本 | goodwillChangeIfMonumentDestroyed |
| `root/nodes/li/elseNode/elseNode/nodes/li/elseNode/node/nodes/li/outcome` | 0.6% (1/156) | 文本 | Success |
| `root/nodes/li/elseNode/elseNode/nodes/li/elseNode/node/nodes/li/sendStandardLetter` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/elseNode/elseNode/nodes/li/elseNode/thing` | 0.6% (1/156) | 文本 | $asker |
| `root/nodes/li/elseNode/elseNode/nodes/li/name` | 1.3% (2/156) | 文本 | hiddenSitePartsPossible / sitePartsTags |
| `root/nodes/li/elseNode/elseNode/nodes/li/node` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/elseNode/elseNode/nodes/li/node/inSignal` | 0.6% (1/156) | 文本 | monumentMarker.MonumentCompleted |
| `root/nodes/li/elseNode/elseNode/nodes/li/node/outcome` | 0.6% (1/156) | 文本 | Success |
| `root/nodes/li/elseNode/elseNode/nodes/li/node/sendStandardLetter` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/elseNode/elseNode/nodes/li/storeAs` | 0.6% (1/156) | 文本 | askerFaction |
| `root/nodes/li/elseNode/elseNode/nodes/li/thing` | 0.6% (1/156) | 文本 | $asker |
| `root/nodes/li/elseNode/elseNode/nodes/li/value` | 1.9% (3/156) | 布尔/文本 | $askerFaction / false |
| `root/nodes/li/elseNode/elseNode/nodes/li/value/li` | 1.3% (2/156) | 容器 |  |
| `root/nodes/li/elseNode/elseNode/nodes/li/value/li/tag` | 1.3% (2/156) | 文本 | QuestActiveThreat / QuestActiveThreatDefenseNoHidden |
| `root/nodes/li/elseNode/elseNode/value1` | 0.6% (1/156) | 文本 | $points |
| `root/nodes/li/elseNode/elseNode/value2` | 0.6% (1/156) | 数值 | 260 |
| `root/nodes/li/elseNode/factionOf` | 1.3% (2/156) | 文本 | $asker |
| `root/nodes/li/elseNode/factionType` | 0.6% (1/156) | 文本 | HostFaction |
| `root/nodes/li/elseNode/hostileWeight` | 0.6% (1/156) | 数值 | 0 |
| `root/nodes/li/elseNode/inSignal` | 0.6% (1/156) | 文本 | askerFaction.BecameHostileToPlayer |
| `root/nodes/li/elseNode/inSignalsRemovePawn` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/elseNode/inSignalsRemovePawn/li` | 0.6% (1/156) | 文本 | lodgers.BecameMutant |
| `root/nodes/li/elseNode/minTechLevel` | 0.6% (1/156) | 文本 | Industrial |
| `root/nodes/li/elseNode/mustBeFactionLeader` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/elseNode/mustBeNonHostileToPlayer` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/elseNode/name` | 14.1% (22/156) | 文本 | minPointsThreeStar / minPointsTwoStar / peacefulChallengeRating |
| `root/nodes/li/elseNode/node` | 3.9% (6/156) | 容器 |  |
| `root/nodes/li/elseNode/node/inSignal` | 0.6% (1/156) | 文本 | monumentMarker.MonumentCompleted |
| `root/nodes/li/elseNode/node/name` | 1.9% (3/156) | 文本 | challengeRating / helpersCount / sitePartsTags |
| `root/nodes/li/elseNode/node/nodes` | 1.3% (2/156) | 容器 |  |
| `root/nodes/li/elseNode/node/nodes/li` | 2.6% (4/156) | 容器 |  |
| `root/nodes/li/elseNode/node/nodes/li/inSignal` | 0.6% (1/156) | 文本 | pickupShipThing.SentSatisfied |
| `root/nodes/li/elseNode/node/nodes/li/label` | 0.6% (1/156) | 文本 | Quest failed: [resolvedQuestName] |
| `root/nodes/li/elseNode/node/nodes/li/letterDef` | 0.6% (1/156) | 文本 | NegativeEvent |
| `root/nodes/li/elseNode/node/nodes/li/name` | 0.6% (1/156) | 文本 | goodwillRewardForMood |
| `root/nodes/li/elseNode/node/nodes/li/outcome` | 0.6% (1/156) | 文本 | Fail |
| `root/nodes/li/elseNode/node/nodes/li/outSignalFailed` | 0.6% (1/156) | 文本 | GoodwillForAverageMood.Failed |
| `root/nodes/li/elseNode/node/nodes/li/outSignalSuccess` | 0.6% (1/156) | 文本 | GoodwillForAverageMood.Success |
| `root/nodes/li/elseNode/node/nodes/li/pawns` | 0.6% (1/156) | 文本 | $lodgers |
| `root/nodes/li/elseNode/node/nodes/li/text` | 0.6% (1/156) | 文本 | [asker_faction_name] are now hostile towards you. [failLetterEndingQuest] |
| `root/nodes/li/elseNode/node/nodes/li/value` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/elseNode/node/outcome` | 0.6% (1/156) | 文本 | Success |
| `root/nodes/li/elseNode/node/sendStandardLetter` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/elseNode/node/value` | 1.9% (3/156) | 数值/文本 | $peacefulChallengeRating / 0 |
| `root/nodes/li/elseNode/node/value/li` | 1.9% (3/156) | 容器 |  |
| `root/nodes/li/elseNode/node/value/li/chance` | 0.6% (1/156) | 数值 | 0.25 |
| `root/nodes/li/elseNode/node/value/li/tag` | 1.9% (3/156) | 文本 | QuestActiveThreat / QuestActiveThreatDefense |
| `root/nodes/li/elseNode/nodes` | 9.0% (14/156) | 容器 |  |
| `root/nodes/li/elseNode/nodes/li` | 12.8% (20/156) | 容器 |  |
| `root/nodes/li/elseNode/nodes/li/contents` | 0.6% (1/156) | 文本 | $arrivingPawns |
| `root/nodes/li/elseNode/nodes/li/curve` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/elseNode/nodes/li/curve/points` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/elseNode/nodes/li/curve/points/li` | 1.3% (2/156) | 文本 | (1500, 800) / (300,  200) |
| `root/nodes/li/elseNode/nodes/li/hostileWeight` | 1.3% (2/156) | 数值 | 0 / 0.15 |
| `root/nodes/li/elseNode/nodes/li/minTechLevel` | 0.6% (1/156) | 文本 | Industrial |
| `root/nodes/li/elseNode/nodes/li/mustBeFactionLeader` | 1.3% (2/156) | 布尔 | true |
| `root/nodes/li/elseNode/nodes/li/mustBeNonHostileToPlayer` | 1.3% (2/156) | 布尔 | true |
| `root/nodes/li/elseNode/nodes/li/name` | 10.3% (16/156) | 文本 | askerIsNull / askerSeniorityRange / discoveryMethod |
| `root/nodes/li/elseNode/nodes/li/roundRandom` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/elseNode/nodes/li/selectionWeight` | 2.6% (4/156) | 数值 | 0.4 / 0.6 |
| `root/nodes/li/elseNode/nodes/li/storeAs` | 1.9% (3/156) | 文本 | asker / askerSeniorityMax |
| `root/nodes/li/elseNode/nodes/li/useTradeDropSpot` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/elseNode/nodes/li/value` | 10.9% (17/156) | 布尔/数值/文本 | $points / 100~$askerSeniorityMax / You have discovered |
| `root/nodes/li/elseNode/options` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/elseNode/options/li` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/elseNode/options/li/kindDef` | 0.6% (1/156) | 文本 | SpaceRefugee_Clothed |
| `root/nodes/li/elseNode/options/li/weight` | 0.6% (1/156) | 数值 | 1 |
| `root/nodes/li/elseNode/pawns` | 0.6% (1/156) | 文本 | $lodgers |
| `root/nodes/li/elseNode/selectionWeight` | 0.6% (1/156) | 数值 | 1.0 |
| `root/nodes/li/elseNode/storeAs` | 2.6% (4/156) | 文本 | asker / askerFaction / lodgersPawnKind |
| `root/nodes/li/elseNode/thing` | 0.6% (1/156) | 文本 | $asker |
| `root/nodes/li/elseNode/value` | 15.4% (24/156) | 布尔/数值/文本 | 0 / 0.15 / 0.25 |
| `root/nodes/li/elseNode/value1` | 0.6% (1/156) | 文本 | $points |
| `root/nodes/li/elseNode/value2` | 0.6% (1/156) | 数值 | 500 |
| `root/nodes/li/ensureHostile` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/exclude` | 0.6% (1/156) | 文本 | $raid1/enemyFaction |
| `root/nodes/li/faction` | 17.3% (27/156) | 文本 | $faction / $siteFaction / Empire |
| `root/nodes/li/factionOf` | 3.2% (5/156) | 文本 | $asker / $factionOf |
| `root/nodes/li/factionType` | 3.2% (5/156) | 文本 | HomeFaction |
| `root/nodes/li/failIfNotFound` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/failIfSmaller` | 1.9% (3/156) | 数值 | 10 |
| `root/nodes/li/fallback` | 0.6% (1/156) | 文本 | Mercenary_Gunner_Acidifier |
| `root/nodes/li/filterDeadPawnsFromLookTargets` | 0.6% (1/156) | 布尔 | True |
| `root/nodes/li/forbidAnyTitle` | 0.6% (1/156) | 布尔 | True |
| `root/nodes/li/forcedTraits` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/forcedTraits/li` | 0.6% (1/156) | 文本 | Wimp |
| `root/nodes/li/gameCondition` | 0.6% (1/156) | 文本 | $gameCondition |
| `root/nodes/li/generateQuestParts` | 1.3% (2/156) | 布尔 | false |
| `root/nodes/li/giveToAccepter` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/goodwillChange` | 0.6% (1/156) | 文本 | $goodwillPenaltyPawn |
| `root/nodes/li/goodwillChangeAmount` | 0.6% (1/156) | 数值 | -5 |
| `root/nodes/li/goodwillChangeFactionOf` | 0.6% (1/156) | 文本 | $asker |
| `root/nodes/li/goodwillChangeReason` | 0.6% (1/156) | 文本 | MonumentConstructionMapRemoved |
| `root/nodes/li/historyDef` | 4.5% (7/156) | 文本 | CharityFulfilled_ThreatReward_Joiner |
| `root/nodes/li/hivesCount` | 0.6% (1/156) | 文本 | $hivesCount |
| `root/nodes/li/hostileWeight` | 1.3% (2/156) | 数值 | 0.15 |
| `root/nodes/li/ifWorldPawnThenMustBeFreeOrLeader` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/inSignal` | 61.5% (96/156) | 文本 | escapeShip.LaunchedShip / escapeShip.ReactorDestroyed / site.AllEnemiesDefeated |
| `root/nodes/li/inSignalChoiceUsed` | 3.9% (6/156) | 文本 | escapeShip.LaunchedShip / pickupShipThing.Sent / site.MapGenerated |
| `root/nodes/li/inSignalDisable` | 14.1% (22/156) | 文本 | DecreeCompleted / monumentMarker.MonumentCompleted / pickupShipThing.SentWithExtraColonists |
| `root/nodes/li/inSignalEnable` | 0.6% (1/156) | 文本 | site.MapGenerated |
| `root/nodes/li/inSignalLeave` | 0.6% (1/156) | 文本 | EndRaid |
| `root/nodes/li/inSignalRemovePawn` | 2.6% (4/156) | 文本 | asker.RanWild / laborers.RanWild / lodgers.RanWild |
| `root/nodes/li/inSignals` | 10.3% (16/156) | 容器 |  |
| `root/nodes/li/inSignals/li` | 18.6% (29/156) | 文本 | fugitive.Destroyed / lodgers.ChangedFaction / lodgers.ChangedHostFaction |
| `root/nodes/li/inSignalsRemovePawn` | 3.2% (5/156) | 容器 |  |
| `root/nodes/li/inSignalsRemovePawn/li` | 5.8% (9/156) | 文本 | lodgers.BecameMutant / lodgers.RanWild |
| `root/nodes/li/inspectString` | 0.6% (1/156) | 文本 | Time left: {0} |
| `root/nodes/li/inspectStringTargets` | 0.6% (1/156) | 文本 | $monumentMarker |
| `root/nodes/li/isQuestTimeout` | 14.1% (22/156) | 布尔 | true |
| `root/nodes/li/isSingleReward` | 1.9% (3/156) | 布尔 | true |
| `root/nodes/li/items` | 1.9% (3/156) | 文本 | $generatedItemStashThings |
| `root/nodes/li/items/li` | 1.3% (2/156) | 文本 | PsychicAmplifier |
| `root/nodes/li/jobDef` | 1.3% (2/156) | 文本 | Unload / WaitTime |
| `root/nodes/li/joinPlayer` | 3.9% (6/156) | 布尔/文本 | $joinPlayer / True / true |
| `root/nodes/li/kindDef` | 2.6% (4/156) | 文本 | Empire_Fighter_Trooper / Empire_Royal_NobleWimp / SpaceRefugee |
| `root/nodes/li/label` | 3.2% (5/156) | 文本 | $customLetterLabel / Laborers arrived / Quest failed: [resolvedQuestName] |
| `root/nodes/li/labelRules` | 0.6% (1/156) | 文本 | $customLetterLabelRules |
| `root/nodes/li/layerDef` | 1.3% (2/156) | 文本 | Orbit |
| `root/nodes/li/layerWhitelist` | 3.9% (6/156) | 容器 |  |
| `root/nodes/li/layerWhitelist/li` | 3.9% (6/156) | 文本 | Orbit / Surface |
| `root/nodes/li/leaderMustBeSafe` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/leaveImmediatelyWhenSatisfied` | 0.6% (1/156) | 文本 | $leaveImmediatelyWhenSatisfied |
| `root/nodes/li/letterDef` | 0.6% (1/156) | 文本 | NegativeEvent |
| `root/nodes/li/lodger` | 1.9% (3/156) | 文本 | $asker |
| `root/nodes/li/lodgers` | 2.6% (4/156) | 文本 | $asker / $laborers / $lodgers |
| `root/nodes/li/lookTargets` | 1.9% (3/156) | 文本 | $arrivingPawns / $laborers / $site |
| `root/nodes/li/loopCount` | 5.1% (8/156) | 数值/文本 | $childCount / $lodgersCount / $raidCount |
| `root/nodes/li/makePrisoners` | 1.3% (2/156) | 布尔/文本 | $makePrisoners / False |
| `root/nodes/li/map` | 2.6% (4/156) | 文本 | $map |
| `root/nodes/li/mapOf` | 1.3% (2/156) | 文本 | $asker / $titleHolder |
| `root/nodes/li/max` | 1.9% (3/156) | 数值 | 70 |
| `root/nodes/li/maxCountOneStar` | 0.6% (1/156) | 数值 | 20 |
| `root/nodes/li/maxCountThreeStar` | 0.6% (1/156) | 数值 | 20 |
| `root/nodes/li/maxCountTwoStar` | 0.6% (1/156) | 数值 | 20 |
| `root/nodes/li/maxMarketValueFactor` | 0.6% (1/156) | 数值 | 0.85 |
| `root/nodes/li/maxPlantGrowDays` | 0.6% (1/156) | 数值 | 10 |
| `root/nodes/li/maxSize` | 1.9% (3/156) | 文本 | $largestClearArea |
| `root/nodes/li/maxTileDistance` | 0.6% (1/156) | 数值 | 32 |
| `root/nodes/li/mentalStateDef` | 0.6% (1/156) | 文本 | ManhunterPermanent |
| `root/nodes/li/minAge` | 1.3% (2/156) | 文本 | $minAge |
| `root/nodes/li/mineables` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/mineables/li` | 1.9% (3/156) | 文本 | MineableGold / MineablePlasteel / MineableUranium |
| `root/nodes/li/minimumTitle` | 0.6% (1/156) | 文本 | Count |
| `root/nodes/li/minStuffCommonality` | 0.6% (1/156) | 数值 | 1 |
| `root/nodes/li/modID` | 0.6% (1/156) | 文本 | Ludeon.RimWorld.Biotech |
| `root/nodes/li/monumentMarker` | 7.0% (11/156) | 文本 | $monumentMarker |
| `root/nodes/li/mustBeFactionLeader` | 1.9% (3/156) | 布尔 | true |
| `root/nodes/li/mustBeHostileToFactionOf` | 1.9% (3/156) | 文本 | $asker |
| `root/nodes/li/mustBeInfestable` | 1.3% (2/156) | 布尔 | true |
| `root/nodes/li/mustBeOfKind` | 0.6% (1/156) | 文本 | Empire_Royal_Stellarch |
| `root/nodes/li/mustBePermanentEnemy` | 3.2% (5/156) | 布尔 | true |
| `root/nodes/li/mustBeWorldPawn` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/mustHaveFreeColonistsAvailableCount` | 0.6% (1/156) | 数值 | 2 |
| `root/nodes/li/mustHaveGoodwillRewardsEnabled` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/name` | 64.7% (101/156) | 文本 | asker / rewardValue / siteDistRange |
| `root/nodes/li/node` | 135.9% (212/156) | 容器 |  |
| `root/nodes/li/node/addToHyperlinks` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/node/addToList` | 4.5% (7/156) | 文本 | laborers / lodgers |
| `root/nodes/li/node/allowAddictions` | 2.6% (4/156) | 布尔 | false |
| `root/nodes/li/node/allowPregnant` | 3.9% (6/156) | 布尔 | false |
| `root/nodes/li/node/biocodeApparelChance` | 3.2% (5/156) | 数值 | 1 |
| `root/nodes/li/node/biocodeWeaponChance` | 3.2% (5/156) | 数值 | 1 |
| `root/nodes/li/node/change` | 0.6% (1/156) | 文本 | $goodwillChangeOnShuttleDestroyed |
| `root/nodes/li/node/choices` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/node/choices/li` | 2.6% (4/156) | 容器 |  |
| `root/nodes/li/node/choices/li/categoryTag` | 1.3% (2/156) | 文本 | Outlander / Tribal |
| `root/nodes/li/node/choices/li/factionDef` | 1.3% (2/156) | 文本 | Empire / Pirate |
| `root/nodes/li/node/choices/li/pawnKinds` | 2.6% (4/156) | 容器 |  |
| `root/nodes/li/node/choices/li/pawnKinds/li` | 5.8% (9/156) | 文本 | Mercenary_Gunner_Acidifier / Mercenary_Slasher / SpaceRefugee_Clothed |
| `root/nodes/li/node/curve` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/node/curve/points` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/node/curve/points/li` | 5.1% (8/156) | 文本 | 1000,  600 / 2000,  1000 / 35,   35 |
| `root/nodes/li/node/def` | 3.9% (6/156) | 文本 | DecreeUnmet / Util_Raid |
| `root/nodes/li/node/delayTicks` | 5.1% (8/156) | 数值/文本 | $($decreeDays*60000) / 300 |
| `root/nodes/li/node/disabledWorkTags` | 1.3% (2/156) | 容器 |  |
| `root/nodes/li/node/disabledWorkTags/li` | 1.3% (2/156) | 文本 | AllWork |
| `root/nodes/li/node/elseNode` | 1.3% (2/156) | 容器 |  |
| `root/nodes/li/node/elseNode/chance` | 0.6% (1/156) | 数值 | 0.5 |
| `root/nodes/li/node/elseNode/node` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/node/elseNode/node/name` | 0.6% (1/156) | 文本 | hiddenSitePartsPossible |
| `root/nodes/li/node/elseNode/node/value` | 0.6% (1/156) | 布尔 | false |
| `root/nodes/li/node/elseNode/nodes` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/node/elseNode/nodes/li` | 1.9% (3/156) | 容器 |  |
| `root/nodes/li/node/elseNode/nodes/li/customLetterLabel` | 0.6% (1/156) | 文本 | [animalKindDef_label] arrived |
| `root/nodes/li/node/elseNode/nodes/li/customLetterText` | 0.6% (1/156) | 文本 | The [animalKindDef_label] that [asker_nameDef] was fleeing has arrived.\n\nIt tu |
| `root/nodes/li/node/elseNode/nodes/li/kindDef` | 0.6% (1/156) | 文本 | $animalKindDef |
| `root/nodes/li/node/elseNode/nodes/li/pawns` | 0.6% (1/156) | 文本 | $peacefulAnimal |
| `root/nodes/li/node/elseNode/nodes/li/storeAs` | 0.6% (1/156) | 文本 | peacefulAnimal |
| `root/nodes/li/node/ensureNonNumericName` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/node/faction` | 4.5% (7/156) | 文本 | $askerFaction / $enemyFaction / $permitFaction |
| `root/nodes/li/node/factionOf` | 0.6% (1/156) | 文本 | $asker |
| `root/nodes/li/node/fallback` | 0.6% (1/156) | 文本 | SpaceRefugee_Clothed |
| `root/nodes/li/node/getRaidersFromMapParent` | 0.6% (1/156) | 文本 | $site |
| `root/nodes/li/node/giveDependentDrugs` | 1.9% (3/156) | 布尔 | true |
| `root/nodes/li/node/hediffDef` | 0.6% (1/156) | 文本 | BloodRot |
| `root/nodes/li/node/inSignalDisable` | 0.6% (1/156) | 文本 | DecreeCompleted |
| `root/nodes/li/node/isChild` | 1.3% (2/156) | 布尔 | false / true |
| `root/nodes/li/node/kindDef` | 4.5% (7/156) | 文本 | $laborersPawnKind / $lodgersPawnKind / Empire_Fighter_StellicGuardMelee |
| `root/nodes/li/node/label` | 0.6% (1/156) | 文本 | Monument completed |
| `root/nodes/li/node/letterDef` | 0.6% (1/156) | 文本 | PositiveEvent |
| `root/nodes/li/node/mustBeCapableOfViolence` | 1.3% (2/156) | 布尔 | true |
| `root/nodes/li/node/name` | 15.4% (24/156) | 文本 | excludeAskerFaction / selectionWeightThreeStar / selectionWeightTwoStar |
| `root/nodes/li/node/node` | 8.3% (13/156) | 容器 |  |
| `root/nodes/li/node/node/animalCount` | 0.6% (1/156) | 数值 | 1 |
| `root/nodes/li/node/node/customLetterLabel` | 0.6% (1/156) | 文本 | Manhunting [animalKindDef_label] |
| `root/nodes/li/node/node/customLetterText` | 0.6% (1/156) | 文本 | The [animalKindDef_label] which was following [asker_nameFull] has arrived in th |
| `root/nodes/li/node/node/def` | 1.9% (3/156) | 文本 | Hospitality_Util_DecideLodgerCountFromPoints |
| `root/nodes/li/node/node/name` | 1.3% (2/156) | 文本 | customLetterLabel / customLetterText |
| `root/nodes/li/node/node/nodes` | 3.9% (6/156) | 容器 |  |
| `root/nodes/li/node/node/nodes/li` | 9.0% (14/156) | 容器 |  |
| `root/nodes/li/node/node/nodes/li/elseNode` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/node/node/nodes/li/elseNode/delayTicks` | 0.6% (1/156) | 数值 | 60000 |
| `root/nodes/li/node/node/nodes/li/elseNode/node` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/node/node/nodes/li/goodwillChangeAmount` | 0.6% (1/156) | 数值 | -5 |
| `root/nodes/li/node/node/nodes/li/goodwillChangeFactionOf` | 0.6% (1/156) | 文本 | $asker |
| `root/nodes/li/node/node/nodes/li/goodwillChangeReason` | 0.6% (1/156) | 文本 | QuestPawnLost |
| `root/nodes/li/node/node/nodes/li/items` | 0.6% (1/156) | 文本 | $upgradeItem |
| `root/nodes/li/node/node/nodes/li/label` | 1.3% (2/156) | 文本 | Guest lost: {SUBJECT_definite} / Quest completed |
| `root/nodes/li/node/node/nodes/li/letterDef` | 1.3% (2/156) | 文本 | NegativeEvent / PositiveEvent |
| `root/nodes/li/node/node/nodes/li/name` | 1.3% (2/156) | 文本 | lodgers / lodgersCountToGenerate |
| `root/nodes/li/node/node/nodes/li/node` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/node/node/nodes/li/outcome` | 2.6% (4/156) | 文本 | Fail / Success |
| `root/nodes/li/node/node/nodes/li/parms` | 1.9% (3/156) | 容器 |  |
| `root/nodes/li/node/node/nodes/li/parms/allowGoodwill` | 1.9% (3/156) | 布尔 | true |
| `root/nodes/li/node/node/nodes/li/parms/allowRoyalFavor` | 1.9% (3/156) | 布尔 | true |
| `root/nodes/li/node/node/nodes/li/parms/thingRewardItemsOnly` | 1.3% (2/156) | 布尔 | true |
| `root/nodes/li/node/node/nodes/li/parms/thingRewardRequired` | 1.3% (2/156) | 布尔 | true |
| `root/nodes/li/node/node/nodes/li/pawns` | 0.6% (1/156) | 文本 | $asker |
| `root/nodes/li/node/node/nodes/li/text` | 1.3% (2/156) | 文本 | You have successfully completed the quest '[resolvedQuestName]'! / [letterSubject], who you were charged to pr |
| `root/nodes/li/node/node/nodes/li/value` | 1.3% (2/156) | 文本 | $($lodgersCountToGenerate - 1) / $asker |
| `root/nodes/li/node/node/nodes/li/value1` | 0.6% (1/156) | 文本 | $helpersCount |
| `root/nodes/li/node/node/nodes/li/value2` | 0.6% (1/156) | 数值 | 1 |
| `root/nodes/li/node/node/outcome` | 0.6% (1/156) | 文本 | Fail |
| `root/nodes/li/node/node/parms` | 1.9% (3/156) | 容器 |  |
| `root/nodes/li/node/node/parms/pointsCurve` | 1.9% (3/156) | 容器 |  |
| `root/nodes/li/node/node/parms/pointsCurve/points` | 1.9% (3/156) | 容器 |  |
| `root/nodes/li/node/node/parms/pointsCurve/points/li` | 7.0% (11/156) | 文本 | (0,  1) / (3000, 20) / (4000, 30) |
| `root/nodes/li/node/node/value` | 1.3% (2/156) | 文本 | [defaultSiteAppearedLetterLabel] / [defaultSiteAppearedLetterText] |
| `root/nodes/li/node/nodes` | 69.9% (109/156) | 容器 |  |
| `root/nodes/li/node/nodes/li` | 158.3% (247/156) | 容器 |  |
| `root/nodes/li/node/nodes/li/addCampLootReward` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/node/nodes/li/addToHyperlinks` | 1.9% (3/156) | 布尔 | true |
| `root/nodes/li/node/nodes/li/addToLookTargets` | 0.6% (1/156) | 布尔 | False |
| `root/nodes/li/node/nodes/li/change` | 3.2% (5/156) | 数值/文本 | $goodwillChangeIfMonumentDestroyed / $goodwillChangeOnShuttleDestroyed / $goodwillPenaltyPawn |
| `root/nodes/li/node/nodes/li/customLetterLabel` | 1.3% (2/156) | 文本 | Payment arrived / {BASELABEL}: Chasing [joiner_nameDef] |
| `root/nodes/li/node/nodes/li/customLetterText` | 1.9% (3/156) | 文本 | You have defeated the bandit camp!\n\nThe payment from [asker_faction_name] has  / {BASETEXT}\n\n[manhunterArr |
| `root/nodes/li/node/nodes/li/def` | 13.5% (21/156) | 文本 | Decree_Util_Reward / Util_JoinerWalkIn / Util_TransportShip_DropOff |
| `root/nodes/li/node/nodes/li/delayTicks` | 4.5% (7/156) | 数值/文本 | $(randInt(5,15)*60) / $haveToProtectForTicks / $keepMonumentTicks |
| `root/nodes/li/node/nodes/li/destroyOrPassToWorldOnCleanup` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/node/nodes/li/disabledWorkTags` | 1.3% (2/156) | 容器 |  |
| `root/nodes/li/node/nodes/li/disabledWorkTags/li` | 1.3% (2/156) | 文本 | AllWork |
| `root/nodes/li/node/nodes/li/elseNode` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/node/nodes/li/elseNode/name` | 0.6% (1/156) | 文本 | nextRaidDelayTicks |
| `root/nodes/li/node/nodes/li/elseNode/value` | 0.6% (1/156) | 文本 | $raid(($raidLoopCounter))/raidDelayTicks |
| `root/nodes/li/node/nodes/li/endingText` | 0.6% (1/156) | 文本 | The high stellarch will now welcome you into the Imperial flotilla as an honored |
| `root/nodes/li/node/nodes/li/expiryInfoPart` | 1.9% (3/156) | 文本 | Do not destroy the monument for {0} / Protect the monument for {0} |
| `root/nodes/li/node/nodes/li/expiryInfoPartTip` | 1.9% (3/156) | 文本 | Do not destroy the monument for {0} / Protect the monument until {0} |
| `root/nodes/li/node/nodes/li/faction` | 1.9% (3/156) | 文本 | $permitFaction |
| `root/nodes/li/node/nodes/li/factionOf` | 1.9% (3/156) | 文本 | $asker |
| `root/nodes/li/node/nodes/li/getRaidersFromMapParent` | 1.9% (3/156) | 文本 | $site |
| `root/nodes/li/node/nodes/li/goodwillChangeAmount` | 18.6% (29/156) | 数值 | -5 |
| `root/nodes/li/node/nodes/li/goodwillChangeFactionOf` | 18.6% (29/156) | 文本 | $asker |
| `root/nodes/li/node/nodes/li/goodwillChangeReason` | 18.6% (29/156) | 文本 | MemberMissedShuttle / MonumentConstructionExpired / QuestPawnLost |
| `root/nodes/li/node/nodes/li/hediffDef` | 1.9% (3/156) | 文本 | Abasia / BloodRot |
| `root/nodes/li/node/nodes/li/heir` | 0.6% (1/156) | 文本 | $titleHeir |
| `root/nodes/li/node/nodes/li/holder` | 0.6% (1/156) | 文本 | $titleHolder |
| `root/nodes/li/node/nodes/li/inSignal` | 5.1% (8/156) | 文本 | DroppedMonumentMarkerCopy / monumentMarker.MonumentCompleted / monumentMarker.MonumentDestroyed |
| `root/nodes/li/node/nodes/li/inSignalEnable` | 1.3% (2/156) | 文本 | monumentMarker.MonumentCompleted |
| `root/nodes/li/node/nodes/li/inspectString` | 4.5% (7/156) | 文本 | Keep monument {0} / Protect for {0} / Should depart on shuttle |
| `root/nodes/li/node/nodes/li/inspectStringTargets` | 1.9% (3/156) | 文本 | $monumentMarker |
| `root/nodes/li/node/nodes/li/introText` | 0.6% (1/156) | 文本 | You've escaped on the Imperial shuttle! |
| `root/nodes/li/node/nodes/li/items` | 0.6% (1/156) | 文本 | $upgradeItem |
| `root/nodes/li/node/nodes/li/kindDef` | 0.6% (1/156) | 文本 | $helperKind |
| `root/nodes/li/node/nodes/li/label` | 44.9% (70/156) | 文本 | Monument time expired / New monument marker arrived / Quest expired: [resolvedQuestName] |
| `root/nodes/li/node/nodes/li/lendColonistsToFactionOf` | 0.6% (1/156) | 文本 | $asker |
| `root/nodes/li/node/nodes/li/letterDef` | 21.8% (34/156) | 文本 | NegativeEvent / PositiveEvent |
| `root/nodes/li/node/nodes/li/lookTargets` | 3.2% (5/156) | 文本 | $pickupShipThing |
| `root/nodes/li/node/nodes/li/name` | 5.8% (9/156) | 文本 | childCount / goodwillChangeOnShuttleDestroyed / pawnsLabelDef |
| `root/nodes/li/node/nodes/li/node` | 9.6% (15/156) | 容器 |  |
| `root/nodes/li/node/nodes/li/node/name` | 1.9% (3/156) | 文本 | haveToProtectForTicks |
| `root/nodes/li/node/nodes/li/node/nodes` | 6.4% (10/156) | 容器 |  |
| `root/nodes/li/node/nodes/li/node/nodes/li` | 13.5% (21/156) | 容器 |  |
| `root/nodes/li/node/nodes/li/node/nodes/li/compareAs` | 0.6% (1/156) | 文本 | int |
| `root/nodes/li/node/nodes/li/node/nodes/li/count` | 0.6% (1/156) | 数值 | 1 |
| `root/nodes/li/node/nodes/li/node/nodes/li/def` | 2.6% (4/156) | 文本 | DecreeFailed / DecreeMet / Util_Raid |
| `root/nodes/li/node/nodes/li/node/nodes/li/elseNode` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/node/nodes/li/node/nodes/li/elseNode/parms` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/node/nodes/li/node/nodes/li/elseNode/parms/thingRewardItemsOnly` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/node/nodes/li/node/nodes/li/goodwillChangeAmount` | 0.6% (1/156) | 文本 | $goodwillChangeOnShuttleDestroyed |
| `root/nodes/li/node/nodes/li/node/nodes/li/goodwillChangeFactionOf` | 0.6% (1/156) | 文本 | $asker |
| `root/nodes/li/node/nodes/li/node/nodes/li/goodwillChangeReason` | 0.6% (1/156) | 文本 | ShuttleDestroyed |
| `root/nodes/li/node/nodes/li/node/nodes/li/inSignal` | 1.3% (2/156) | 文本 | GoodwillForAverageMood.Failed / GoodwillForAverageMood.Success |
| `root/nodes/li/node/nodes/li/node/nodes/li/label` | 1.3% (2/156) | 文本 | Monument destroyed / Shuttle destroyed |
| `root/nodes/li/node/nodes/li/node/nodes/li/letterDef` | 0.6% (1/156) | 文本 | NegativeEvent |
| `root/nodes/li/node/nodes/li/node/nodes/li/lookTargets` | 0.6% (1/156) | 文本 | monumentMarker |
| `root/nodes/li/node/nodes/li/node/nodes/li/messageType` | 0.6% (1/156) | 文本 | NegativeEvent |
| `root/nodes/li/node/nodes/li/node/nodes/li/name` | 1.3% (2/156) | 文本 | points / sendStandardLetter |
| `root/nodes/li/node/nodes/li/node/nodes/li/node` | 3.2% (5/156) | 容器 |  |
| `root/nodes/li/node/nodes/li/node/nodes/li/node/elseNode` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/node/nodes/li/node/nodes/li/node/elseNode/def` | 0.6% (1/156) | 文本 | Util_GameConditionNegativeRandom |
| `root/nodes/li/node/nodes/li/node/nodes/li/node/node` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/node/nodes/li/node/nodes/li/node/node/nodes` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/node/nodes/li/node/nodes/li/node/node/nodes/li` | 3.9% (6/156) | 容器 |  |
| `root/nodes/li/node/nodes/li/node/nodes/li/node/node/nodes/li/def` | 3.9% (6/156) | 文本 | Util_GameConditionNegativeRandom / Util_Infestation / Util_MechCluster |
| `root/nodes/li/node/nodes/li/node/nodes/li/node/nodes` | 1.3% (2/156) | 容器 |  |
| `root/nodes/li/node/nodes/li/node/nodes/li/node/nodes/li` | 1.9% (3/156) | 容器 |  |
| `root/nodes/li/node/nodes/li/node/nodes/li/node/nodes/li/factionOf` | 0.6% (1/156) | 文本 | $asker |
| `root/nodes/li/node/nodes/li/node/nodes/li/node/nodes/li/inSignal` | 0.6% (1/156) | 文本 | GoodwillForAverageMood.Success |
| `root/nodes/li/node/nodes/li/node/nodes/li/node/nodes/li/label` | 1.3% (2/156) | 文本 | Quest completed |
| `root/nodes/li/node/nodes/li/node/nodes/li/node/nodes/li/letterDef` | 1.3% (2/156) | 文本 | PositiveEvent |
| `root/nodes/li/node/nodes/li/node/nodes/li/node/nodes/li/text` | 1.3% (2/156) | 文本 | You have successfully completed the quest '[resolvedQuestName]'!\n\nWhile [lodge / You have successfully compl |
| `root/nodes/li/node/nodes/li/node/nodes/li/node/outSignals` | 0.6% (1/156) | 文本 | AllRaidsSent |
| `root/nodes/li/node/nodes/li/node/nodes/li/node/parms` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/node/nodes/li/node/nodes/li/node/parms/allowGoodwill` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/node/nodes/li/node/nodes/li/node/parms/allowRoyalFavor` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/node/nodes/li/node/nodes/li/outcome` | 3.2% (5/156) | 文本 | Fail / Success |
| `root/nodes/li/node/nodes/li/node/nodes/li/outSignals` | 0.6% (1/156) | 文本 | AllRaidsSent |
| `root/nodes/li/node/nodes/li/node/nodes/li/parms` | 1.9% (3/156) | 容器 |  |
| `root/nodes/li/node/nodes/li/node/nodes/li/parms/allowGoodwill` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/node/nodes/li/node/nodes/li/parms/allowRoyalFavor` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/node/nodes/li/node/nodes/li/parms/customLetterLabel` | 1.3% (2/156) | 文本 | $customLetterLabel / {BASELABEL} chasing [../joiner_nameDef] |
| `root/nodes/li/node/nodes/li/node/nodes/li/parms/customLetterLabelRules` | 0.6% (1/156) | 文本 | $customLetterLabelRules |
| `root/nodes/li/node/nodes/li/node/nodes/li/parms/customLetterText` | 1.3% (2/156) | 文本 | $customLetterText / {BASETEXT}
                        \nThe [enemyFaction_pawnsPlural] are coming f |
| `root/nodes/li/node/nodes/li/node/nodes/li/parms/customLetterTextRules` | 0.6% (1/156) | 文本 | $customLetterTextRules |
| `root/nodes/li/node/nodes/li/node/nodes/li/parms/enemyFaction` | 1.3% (2/156) | 文本 | $enemyFaction |
| `root/nodes/li/node/nodes/li/node/nodes/li/parms/inSignal` | 1.3% (2/156) | 文本 | $inSignal |
| `root/nodes/li/node/nodes/li/node/nodes/li/parms/map` | 1.3% (2/156) | 文本 | $map |
| `root/nodes/li/node/nodes/li/node/nodes/li/parms/points` | 1.3% (2/156) | 文本 | $points |
| `root/nodes/li/node/nodes/li/node/nodes/li/parms/tag` | 0.6% (1/156) | 文本 | lord |
| `root/nodes/li/node/nodes/li/node/nodes/li/parms/walkInSpot` | 0.6% (1/156) | 文本 | $walkInSpot |
| `root/nodes/li/node/nodes/li/node/nodes/li/pawn` | 1.3% (2/156) | 文本 | $asker |
| `root/nodes/li/node/nodes/li/node/nodes/li/pawns` | 0.6% (1/156) | 文本 | $asker |
| `root/nodes/li/node/nodes/li/node/nodes/li/prefix` | 1.3% (2/156) | 文本 | raid$raidLoopCounter / raid2 |
| `root/nodes/li/node/nodes/li/node/nodes/li/text` | 1.9% (3/156) | 文本 | The monument for the quest '[resolvedQuestName]' has been violated. Consequences / The shuttle sent to drop of |
| `root/nodes/li/node/nodes/li/node/nodes/li/value` | 1.3% (2/156) | 布尔/文本 | $($pointsOriginal * 1.75) / false |
| `root/nodes/li/node/nodes/li/node/nodes/li/value1` | 0.6% (1/156) | 文本 | $raidLoopCounter |
| `root/nodes/li/node/nodes/li/node/nodes/li/value2` | 0.6% (1/156) | 文本 | $($raidCount - 1) |
| `root/nodes/li/node/nodes/li/node/outcome` | 0.6% (1/156) | 文本 | Success |
| `root/nodes/li/node/nodes/li/node/parms` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/node/nodes/li/node/parms/allowGoodwill` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/node/nodes/li/node/parms/allowRoyalFavor` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/node/nodes/li/node/sendStandardLetter` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/node/nodes/li/node/value` | 1.9% (3/156) | 文本 | $(roundToTicksRough(randInt(20, 40)*60000)) / $(roundToTicksRough(randInt(41, 60)*60000)) / $(roundToTicksRoug |
| `root/nodes/li/node/nodes/li/nodeIfChosenPawnSignalUsed` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/node/nodes/li/nodeIfChosenPawnSignalUsed/chosenPawnSignal` | 0.6% (1/156) | 文本 | ChosenPawnForReward |
| `root/nodes/li/node/nodes/li/nodeIfChosenPawnSignalUsed/label` | 0.6% (1/156) | 文本 | [asker_faction_royalFavorLabel] |
| `root/nodes/li/node/nodes/li/nodeIfChosenPawnSignalUsed/letterDef` | 0.6% (1/156) | 文本 | ChoosePawn |
| `root/nodes/li/node/nodes/li/nodeIfChosenPawnSignalUsed/text` | 0.6% (1/156) | 文本 | These colonists participated in the victory for the quest [resolvedQuestName]. [ |
| `root/nodes/li/node/nodes/li/nodeIfChosenPawnSignalUsed/useColonistsOnMap` | 0.6% (1/156) | 文本 | $site |
| `root/nodes/li/node/nodes/li/nodes` | 9.0% (14/156) | 容器 |  |
| `root/nodes/li/node/nodes/li/nodes/li` | 66.0% (103/156) | 容器 |  |
| `root/nodes/li/node/nodes/li/nodes/li/allowedHiddenFactions` | 5.1% (8/156) | 文本 | Mechanoid |
| `root/nodes/li/node/nodes/li/nodes/li/allowEnemy` | 5.1% (8/156) | 布尔 | true |
| `root/nodes/li/node/nodes/li/nodes/li/duration` | 8.3% (13/156) | 文本 | $shuttleDelayTicks |
| `root/nodes/li/node/nodes/li/nodes/li/faction` | 5.1% (8/156) | 文本 | $enemyFaction |
| `root/nodes/li/node/nodes/li/nodes/li/incidentDef` | 8.3% (13/156) | 文本 | MechCluster / RaidEnemy |
| `root/nodes/li/node/nodes/li/nodes/li/inSignalDisable` | 8.3% (13/156) | 文本 | ShuttleArrived |
| `root/nodes/li/node/nodes/li/nodes/li/mustBeHostileToFactionOf` | 5.1% (8/156) | 文本 | $asker |
| `root/nodes/li/node/nodes/li/nodes/li/mustBePermanentEnemy` | 5.1% (8/156) | 布尔 | true |
| `root/nodes/li/node/nodes/li/nodes/li/name` | 50.0% (78/156) | 文本 | rewardValueFromThreats / threatFactor / threatPoints |
| `root/nodes/li/node/nodes/li/nodes/li/nodes` | 2.6% (4/156) | 容器 |  |
| `root/nodes/li/node/nodes/li/nodes/li/nodes/li` | 9.0% (14/156) | 容器 |  |
| `root/nodes/li/node/nodes/li/nodes/li/nodes/li/allowEnemy` | 1.3% (2/156) | 布尔 | true |
| `root/nodes/li/node/nodes/li/nodes/li/nodes/li/def` | 2.6% (4/156) | 文本 | Util_Infestation / Util_ManhunterPack / Util_Raid |
| `root/nodes/li/node/nodes/li/nodes/li/nodes/li/mustBePermanentEnemy` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/node/nodes/li/nodes/li/nodes/li/name` | 5.1% (8/156) | 文本 | customLetterLabel / customLetterText |
| `root/nodes/li/node/nodes/li/nodes/li/nodes/li/storeAs` | 1.3% (2/156) | 文本 | enemyFaction |
| `root/nodes/li/node/nodes/li/nodes/li/nodes/li/value` | 5.1% (8/156) | 文本 | Site appeared to harass [joiner_nameDef]: [site_label] / [joiner_nameDef] has admitted what [joiner_pronoun] w |
| `root/nodes/li/node/nodes/li/nodes/li/points` | 8.3% (13/156) | 文本 | $threatPoints |
| `root/nodes/li/node/nodes/li/nodes/li/randomIncidents` | 8.3% (13/156) | 文本 | $threatCount |
| `root/nodes/li/node/nodes/li/nodes/li/startOffsetTicks` | 8.3% (13/156) | 文本 | $(0.25 * 60000) / $(2.5 * 60000) / $(4 * 60000) |
| `root/nodes/li/node/nodes/li/nodes/li/storeAs` | 5.1% (8/156) | 文本 | enemyFaction |
| `root/nodes/li/node/nodes/li/nodes/li/value` | 50.0% (78/156) | 数值/文本 | $($points * $threatFactor * $threatCount * 1.4) / $($points * $threatFactor + 3 * $helpersPoints / $threatCoun |
| `root/nodes/li/node/nodes/li/otherPawn` | 0.6% (1/156) | 文本 | $titleHolder |
| `root/nodes/li/node/nodes/li/outcome` | 41.0% (64/156) | 文本 | Fail / Success / Unknown |
| `root/nodes/li/node/nodes/li/outSignalColonistsDied` | 0.6% (1/156) | 文本 | ColonistsDied |
| `root/nodes/li/node/nodes/li/outSignalComplete` | 0.6% (1/156) | 文本 | ColonistsReturned |
| `root/nodes/li/node/nodes/li/outSignalResult` | 1.3% (2/156) | 文本 | DroppedMonumentMarkerCopy |
| `root/nodes/li/node/nodes/li/outSignals` | 9.0% (14/156) | 文本 | DecreeCompleted / JoinerArrived / ManhuntersArrived |
| `root/nodes/li/node/nodes/li/parms` | 9.6% (15/156) | 容器 |  |
| `root/nodes/li/node/nodes/li/parms/acceptChildren` | 0.6% (1/156) | 布尔 | false |
| `root/nodes/li/node/nodes/li/parms/acceptColonists` | 1.3% (2/156) | 布尔 | true |
| `root/nodes/li/node/nodes/li/parms/allowDevelopmentPoints` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/node/nodes/li/parms/allowGoodwill` | 2.6% (4/156) | 布尔 | true |
| `root/nodes/li/node/nodes/li/parms/allowRoyalFavor` | 2.6% (4/156) | 布尔 | true |
| `root/nodes/li/node/nodes/li/parms/chosenPawnSignal` | 0.6% (1/156) | 文本 | ChosenPawnForReward |
| `root/nodes/li/node/nodes/li/parms/contents` | 0.6% (1/156) | 文本 | $arrivingPawns |
| `root/nodes/li/node/nodes/li/parms/customLetterLabel` | 1.3% (2/156) | 文本 | {BASELABEL} chasing [../joiner_nameDef] / {BASELABEL}: Chasing [joiner_nameDef] |
| `root/nodes/li/node/nodes/li/parms/customLetterText` | 3.2% (5/156) | 文本 | Since you accepted [../joiner_nameDef], [../threat] have set up a nearby site to / [defaultSiteAppearedLetterT |
| `root/nodes/li/node/nodes/li/parms/enemyFaction` | 0.6% (1/156) | 文本 | $enemyFaction |
| `root/nodes/li/node/nodes/li/parms/inSignal` | 1.9% (3/156) | 文本 | $inSignal |
| `root/nodes/li/node/nodes/li/parms/leaveDelayTicks` | 3.2% (5/156) | 数值/文本 | $(3*60000) / $shuttleLeaveDelayTicks / 45000 |
| `root/nodes/li/node/nodes/li/parms/leaveImmediatelyWhenSatisfied` | 1.3% (2/156) | 布尔 | true |
| `root/nodes/li/node/nodes/li/parms/map` | 1.9% (3/156) | 文本 | $map |
| `root/nodes/li/node/nodes/li/parms/minAge` | 0.6% (1/156) | 文本 | $minAge |
| `root/nodes/li/node/nodes/li/parms/onlyAcceptColonists` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/node/nodes/li/parms/onlyAcceptHealthy` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/node/nodes/li/parms/overrideMass` | 0.6% (1/156) | 数值 | 999999999 |
| `root/nodes/li/node/nodes/li/parms/owningFaction` | 0.6% (1/156) | 文本 | Empire |
| `root/nodes/li/node/nodes/li/parms/points` | 1.9% (3/156) | 文本 | $points |
| `root/nodes/li/node/nodes/li/parms/requireColonistCount` | 0.6% (1/156) | 文本 | $colonistsToLendCount |
| `root/nodes/li/node/nodes/li/parms/requiredPawns` | 2.6% (4/156) | 文本 | $asker / $laborers / $lodgers |
| `root/nodes/li/node/nodes/li/parms/sendAwayIfAllDespawned` | 0.6% (1/156) | 文本 | $lodgers |
| `root/nodes/li/node/nodes/li/parms/tag` | 0.6% (1/156) | 文本 | infestation |
| `root/nodes/li/node/nodes/li/parms/thingRewardItemsOnly` | 1.3% (2/156) | 布尔 | true |
| `root/nodes/li/node/nodes/li/parms/thingRewardRequired` | 1.3% (2/156) | 布尔 | true |
| `root/nodes/li/node/nodes/li/parms/walkInSpot` | 0.6% (1/156) | 文本 | $walkInSpot |
| `root/nodes/li/node/nodes/li/pawnKind` | 0.6% (1/156) | 文本 | $lodgersPawnKind |
| `root/nodes/li/node/nodes/li/pawns` | 6.4% (10/156) | 文本 | $helpers / $lodgers / $titlePreviousHeir |
| `root/nodes/li/node/nodes/li/prefix` | 1.9% (3/156) | 文本 | raid1 / site |
| `root/nodes/li/node/nodes/li/reason` | 3.2% (5/156) | 文本 | LaborersMissedShuttle / MonumentConstructionExpired / MonumentDestroyed |
| `root/nodes/li/node/nodes/li/returnLentColonistsInTicks` | 0.6% (1/156) | 文本 | $($lendForDays*60000) |
| `root/nodes/li/node/nodes/li/selectionWeight` | 1.3% (2/156) | 数值 | 0.2 / 0.8 |
| `root/nodes/li/node/nodes/li/sendStandardLetter` | 3.2% (5/156) | 布尔/文本 | $sendStandardLetter / true |
| `root/nodes/li/node/nodes/li/shuttle` | 0.6% (1/156) | 文本 | $pickupShipThing |
| `root/nodes/li/node/nodes/li/signalListenMode` | 1.9% (3/156) | 文本 | Always / OngoingOrNotYetAccepted |
| `root/nodes/li/node/nodes/li/storeAs` | 2.6% (4/156) | 文本 | helperCombatPower / lodgersBodySize / nextRaidDelayTicks |
| `root/nodes/li/node/nodes/li/tag` | 0.6% (1/156) | 文本 | $signalTag |
| `root/nodes/li/node/nodes/li/targets` | 2.6% (4/156) | 文本 | $asker / $laborers / $lodgers |
| `root/nodes/li/node/nodes/li/text` | 44.9% (70/156) | 文本 | After being discovered, the bandit camp has dispersed. The quest [resolvedQuestN / Intercepted communications  |
| `root/nodes/li/node/nodes/li/value` | 7.0% (11/156) | 布尔/数值/文本 | $(randInt(0, $lodgersCountToGenerate / 2)) / $arrivingPawnsLabelDef / $raid(($raidLoopCounter))/raidDelayTicks |
| `root/nodes/li/node/nodes/li/value1` | 3.2% (5/156) | 文本 | $challengeRating / $nextRaidDelayTicks / $rewardValue |
| `root/nodes/li/node/nodes/li/value2` | 3.2% (5/156) | 数值 | 1 / 2 / 3 |
| `root/nodes/li/node/nodes/li/waitUntilPlayerHasHomeMap` | 1.9% (3/156) | 布尔 | true |
| `root/nodes/li/node/outcome` | 13.5% (21/156) | 文本 | Fail / Success |
| `root/nodes/li/node/parms` | 1.9% (3/156) | 容器 |  |
| `root/nodes/li/node/parms/allowedThreats` | 0.6% (1/156) | 文本 | Raids |
| `root/nodes/li/node/parms/currentThreatPointsFactor` | 0.6% (1/156) | 数值 | 1.4 |
| `root/nodes/li/node/parms/customLetterLabel` | 1.3% (2/156) | 文本 | {BASELABEL} chasing [../joiner_nameDef] / {BASELABEL}: Loyalty squad |
| `root/nodes/li/node/parms/customLetterText` | 1.3% (2/156) | 文本 | {BASETEXT}
              \nThe [enemyFaction_pawnsPlural] have come to get [../j / {BASETEXT}\n\nThis is the l |
| `root/nodes/li/node/parms/enemyFaction` | 1.3% (2/156) | 文本 | $enemyFaction / Empire |
| `root/nodes/li/node/parms/inSignal` | 1.3% (2/156) | 文本 | $inSignal |
| `root/nodes/li/node/parms/map` | 1.3% (2/156) | 文本 | $map |
| `root/nodes/li/node/parms/minSpacingDays` | 0.6% (1/156) | 数值 | 0.04 |
| `root/nodes/li/node/parms/minThreatPoints` | 0.6% (1/156) | 数值 | 500 |
| `root/nodes/li/node/parms/numIncidentsRange` | 0.6% (1/156) | 文本 | 1~2 |
| `root/nodes/li/node/parms/offDays` | 0.6% (1/156) | 数值 | 0.5 |
| `root/nodes/li/node/parms/onDays` | 0.6% (1/156) | 数值 | 1.0 |
| `root/nodes/li/node/parms/points` | 1.3% (2/156) | 文本 | $points / $raidPoints |
| `root/nodes/li/node/parms/walkInSpot` | 1.3% (2/156) | 文本 | $walkInSpot |
| `root/nodes/li/node/pawn` | 3.2% (5/156) | 文本 | $asker |
| `root/nodes/li/node/pawns` | 1.9% (3/156) | 文本 | $lodgers / $lodgersWithRoyalTitles |
| `root/nodes/li/node/points` | 1.3% (2/156) | 文本 | $($points + $helpersPoints) / $threatPoints |
| `root/nodes/li/node/prefix` | 1.3% (2/156) | 文本 | raid |
| `root/nodes/li/node/reason` | 0.6% (1/156) | 文本 | ShuttleDestroyed |
| `root/nodes/li/node/sendStandardLetter` | 5.8% (9/156) | 布尔 | true |
| `root/nodes/li/node/sitePartDefs` | 0.6% (1/156) | 文本 | $sitePartDefs |
| `root/nodes/li/node/storeAs` | 2.6% (4/156) | 文本 | lodgersPawnKind / points / rewardValue |
| `root/nodes/li/node/tag` | 0.6% (1/156) | 文本 | cluster |
| `root/nodes/li/node/text` | 0.6% (1/156) | 文本 | You completed construction of the monument.\n\nYou must now protect the monument |
| `root/nodes/li/node/value` | 19.2% (30/156) | 布尔/数值/文本 | 0.5 / 0.7 / 0.85 |
| `root/nodes/li/node/value/li` | 2.6% (4/156) | 容器 |  |
| `root/nodes/li/node/value/li/chance` | 1.3% (2/156) | 数值 | 0.05 / 0.25 |
| `root/nodes/li/node/value/li/tag` | 2.6% (4/156) | 文本 | QuestActiveThreat / QuestActiveThreatDefense |
| `root/nodes/li/node/value1` | 0.6% (1/156) | 文本 | $rewardValue |
| `root/nodes/li/node/value2` | 0.6% (1/156) | 数值 | 1.7 |
| `root/nodes/li/node/waitUntilPlayerHasHomeMap` | 1.3% (2/156) | 布尔 | true |
| `root/nodes/li/nodeIfChosenPawnSignalUsed` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/nodeIfChosenPawnSignalUsed/chosenPawnSignal` | 0.6% (1/156) | 文本 | ChosenPawnForReward |
| `root/nodes/li/nodeIfChosenPawnSignalUsed/label` | 0.6% (1/156) | 文本 | [asker_faction_royalFavorLabel] |
| `root/nodes/li/nodeIfChosenPawnSignalUsed/letterDef` | 0.6% (1/156) | 文本 | ChoosePawn |
| `root/nodes/li/nodeIfChosenPawnSignalUsed/text` | 0.6% (1/156) | 文本 | Who should be credited with [asker_faction_royalFavorLabel] for fulfilling the t |
| `root/nodes/li/nodeIfChosenPawnSignalUsed/useColonistsFromCaravanArg` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/nodes` | 5.8% (9/156) | 容器 |  |
| `root/nodes/li/nodes/li` | 16.0% (25/156) | 容器 |  |
| `root/nodes/li/nodes/li/allowPermanentEnemyFaction` | 2.6% (4/156) | 布尔 | false |
| `root/nodes/li/nodes/li/canGeneratePawn` | 1.3% (2/156) | 布尔 | true |
| `root/nodes/li/nodes/li/elseNode` | 1.3% (2/156) | 容器 |  |
| `root/nodes/li/nodes/li/elseNode/elseNode` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/nodes/li/elseNode/elseNode/elseNode` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/nodes/li/elseNode/elseNode/elseNode/pawns` | 0.6% (1/156) | 文本 | $lodgers |
| `root/nodes/li/nodes/li/elseNode/elseNode/elseNode/storeAs` | 0.6% (1/156) | 文本 | lodgersWithMoodThreshold |
| `root/nodes/li/nodes/li/elseNode/elseNode/elseNode/storeCountAs` | 0.6% (1/156) | 文本 | lodgersCountWithMoodThreshold |
| `root/nodes/li/nodes/li/elseNode/elseNode/value` | 0.6% (1/156) | 文本 | $lodgersHaveBloodRotAndParalysis |
| `root/nodes/li/nodes/li/elseNode/name` | 0.6% (1/156) | 文本 | lodgersCountWithMoodThreshold |
| `root/nodes/li/nodes/li/elseNode/value` | 1.3% (2/156) | 数值/文本 | $lodgersAreParalyzed / 0 |
| `root/nodes/li/nodes/li/excludeFactionDefs` | 0.6% (1/156) | 文本 | $excludeFactionDefs |
| `root/nodes/li/nodes/li/hostileWeight` | 3.9% (6/156) | 数值 | 0.15 |
| `root/nodes/li/nodes/li/ifWorldPawnThenMustBeFreeOrLeader` | 0.6% (1/156) | 文本 | $ifWorldPawnThenMustBeFreeOrLeader |
| `root/nodes/li/nodes/li/mustBeFactionLeader` | 2.6% (4/156) | 布尔 | true |
| `root/nodes/li/nodes/li/mustBeNonHostileToPlayer` | 1.3% (2/156) | 布尔/文本 | $askerMustBeNonHostileToPlayer / true |
| `root/nodes/li/nodes/li/mustHaveRoyalTitleInCurrentFaction` | 1.3% (2/156) | 布尔 | true |
| `root/nodes/li/nodes/li/name` | 3.2% (5/156) | 文本 | askerIsNull / lodgersAreParalyzed / lodgersCountWithMoodThreshold |
| `root/nodes/li/nodes/li/node` | 3.9% (6/156) | 容器 |  |
| `root/nodes/li/nodes/li/node/def` | 0.6% (1/156) | 文本 | Util_ApplyMoodThreshold |
| `root/nodes/li/nodes/li/node/name` | 1.9% (3/156) | 文本 | lodgersHaveBloodRot / lodgersHaveMoodThreshold / lodgersHaveNoConditions |
| `root/nodes/li/nodes/li/node/nodes` | 1.3% (2/156) | 容器 |  |
| `root/nodes/li/nodes/li/node/nodes/li` | 1.9% (3/156) | 容器 |  |
| `root/nodes/li/nodes/li/node/nodes/li/name` | 1.9% (3/156) | 文本 | lodgersCountWithMoodThreshold / lodgersHaveBloodRotAndParalysis / lodgersWithMoodThreshold |
| `root/nodes/li/nodes/li/node/nodes/li/value` | 1.9% (3/156) | 布尔/文本 | $lodgers / $lodgersCount / true |
| `root/nodes/li/nodes/li/node/parms` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/nodes/li/node/parms/moodThresholdPawns` | 0.6% (1/156) | 文本 | $lodgersWithMoodThreshold |
| `root/nodes/li/nodes/li/node/parms/storeMoodThresholdAs` | 0.6% (1/156) | 文本 | lodgersMoodThreshold |
| `root/nodes/li/nodes/li/node/parms/storeNormalizedMoodThresholdAs` | 0.6% (1/156) | 文本 | lodgersMoodThresholdNormalized |
| `root/nodes/li/nodes/li/node/value` | 1.9% (3/156) | 布尔 | true |
| `root/nodes/li/nodes/li/nodes` | 5.1% (8/156) | 容器 |  |
| `root/nodes/li/nodes/li/nodes/li` | 11.5% (18/156) | 容器 |  |
| `root/nodes/li/nodes/li/nodes/li/allowPermanentEnemyFaction` | 1.3% (2/156) | 布尔 | false |
| `root/nodes/li/nodes/li/nodes/li/canGeneratePawn` | 1.3% (2/156) | 布尔 | true |
| `root/nodes/li/nodes/li/nodes/li/elseNode` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/nodes/li/nodes/li/elseNode/name` | 0.6% (1/156) | 文本 | askerSeniorityRange |
| `root/nodes/li/nodes/li/nodes/li/elseNode/value` | 0.6% (1/156) | 文本 | 100~850 |
| `root/nodes/li/nodes/li/nodes/li/excludeFactionDefs` | 0.6% (1/156) | 文本 | $excludeFactionDefs |
| `root/nodes/li/nodes/li/nodes/li/hostileWeight` | 1.9% (3/156) | 数值 | 0.15 |
| `root/nodes/li/nodes/li/nodes/li/ifWorldPawnThenMustBeFree` | 0.6% (1/156) | 文本 | $ifWorldPawnThenMustBeFree |
| `root/nodes/li/nodes/li/nodes/li/minTechLevel` | 1.3% (2/156) | 文本 | Industrial |
| `root/nodes/li/nodes/li/nodes/li/mustBeFactionLeader` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/nodes/li/nodes/li/mustBeNonHostileToPlayer` | 0.6% (1/156) | 文本 | $askerMustBeNonHostileToPlayer |
| `root/nodes/li/nodes/li/nodes/li/mustHaveRoyalTitleInCurrentFaction` | 1.3% (2/156) | 布尔 | true |
| `root/nodes/li/nodes/li/nodes/li/mustHaveSettlementOnLayer` | 0.6% (1/156) | 文本 | $mustHaveSettlementOnLayer |
| `root/nodes/li/nodes/li/nodes/li/name` | 8.3% (13/156) | 文本 | challengeRating / pointsFactor / returnLetterText |
| `root/nodes/li/nodes/li/nodes/li/requireResearchedBedroomFurnitureIfRoyal` | 0.6% (1/156) | 文本 | $royalAskerNeedsResearchedFurniture |
| `root/nodes/li/nodes/li/nodes/li/root` | 1.3% (2/156) | 文本 | dutyDescription / dutyRoyalDescription |
| `root/nodes/li/nodes/li/nodes/li/rules` | 1.3% (2/156) | 容器 |  |
| `root/nodes/li/nodes/li/nodes/li/rules/rulesStrings` | 1.3% (2/156) | 容器 |  |
| `root/nodes/li/nodes/li/nodes/li/rules/rulesStrings/li` | 7.7% (12/156) | 文本 | dutyRoyalDescription->explore a swamp / dutyRoyalDescription->negotiate with a tribe / dutyRoyalDescription->p |
| `root/nodes/li/nodes/li/nodes/li/seniorityRange` | 1.3% (2/156) | 文本 | $askerSeniorityRange / 250~850 |
| `root/nodes/li/nodes/li/nodes/li/storeAs` | 3.2% (5/156) | 文本 | asker / dutyDescription / dutyRoyalDescription |
| `root/nodes/li/nodes/li/nodes/li/value` | 7.7% (12/156) | 数值/文本 | $pointsFactorThreeStar / $pointsFactorTwoStar / 2 |
| `root/nodes/li/nodes/li/nodes/li/value/li` | 2.6% (4/156) | 容器 |  |
| `root/nodes/li/nodes/li/nodes/li/value/li/tag` | 2.6% (4/156) | 文本 | MechClusterForceNoConditionCauser / Outpost / QuestConditionCauser |
| `root/nodes/li/nodes/li/selectionWeight` | 14.1% (22/156) | 数值/文本 | $selectionWeightThreeStar / $selectionWeightTwoStar / 0.2 |
| `root/nodes/li/nodes/li/storeAs` | 3.9% (6/156) | 文本 | asker |
| `root/nodes/li/nodes/li/value` | 3.2% (5/156) | 布尔/文本 | $lodgersHaveMoodThreshold / true |
| `root/nodes/li/nodes/li/value1` | 3.2% (5/156) | 文本 | $lodgersCountWithMoodThreshold / $points |
| `root/nodes/li/nodes/li/value2` | 3.2% (5/156) | 数值/文本 | $bloodRotMinPoints / $noConditionsMaxPoints / 240 |
| `root/nodes/li/ofPawn` | 0.6% (1/156) | 文本 | $asker |
| `root/nodes/li/oneStarRange` | 1.3% (2/156) | 文本 | 0.0~0.35 / 5~10 |
| `root/nodes/li/onlyAcceptColonists` | 1.3% (2/156) | 文本 | $onlyAcceptColonists |
| `root/nodes/li/onlyAcceptHealthy` | 1.3% (2/156) | 文本 | $onlyAcceptHealthy |
| `root/nodes/li/options` | 1.9% (3/156) | 容器 |  |
| `root/nodes/li/options/li` | 3.9% (6/156) | 数值 | 0.25 / 0.3 / 0.35 |
| `root/nodes/li/options/li/anyAnimal` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/options/li/kindDef` | 0.6% (1/156) | 文本 | SpaceRefugee_Clothed |
| `root/nodes/li/options/li/mustBeAbleToHandleAnimal` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/options/li/onlyAllowedFleshType` | 0.6% (1/156) | 文本 | Normal |
| `root/nodes/li/options/li/weight` | 1.3% (2/156) | 数值 | 1 |
| `root/nodes/li/outcome` | 9.6% (15/156) | 文本 | Fail / InvalidPreAcceptance / Success |
| `root/nodes/li/outSignal` | 0.6% (1/156) | 文本 | ManhuntersNeutralized |
| `root/nodes/li/outSignalComplete` | 1.3% (2/156) | 文本 | PeaceTalksTimeout / TradeRequestTimeout |
| `root/nodes/li/outSignalPawnsNotAvailable` | 0.6% (1/156) | 文本 | Incompletable |
| `root/nodes/li/overrideMass` | 0.6% (1/156) | 文本 | $overrideMass |
| `root/nodes/li/owningFaction` | 1.3% (2/156) | 文本 | $owningFaction |
| `root/nodes/li/parms` | 26.9% (42/156) | 容器 |  |
| `root/nodes/li/parms/allowGoodwill` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/parms/allowRoyalFavor` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/parms/arrivingPawns` | 1.3% (2/156) | 文本 | $arrivingPawns / $lodgers |
| `root/nodes/li/parms/arrivingPawnsLabelDef` | 1.3% (2/156) | 文本 | [asker_nameDef] / [lodgersLabelSingOrPluralDef] |
| `root/nodes/li/parms/askerIsNullChance` | 0.6% (1/156) | 数值 | 0 |
| `root/nodes/li/parms/askerMustBeNonHostileToPlayer` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/parms/bloodRotAndParalysisWeight` | 1.9% (3/156) | 数值 | 0 |
| `root/nodes/li/parms/bloodRotMinPoints` | 0.6% (1/156) | 数值 | 499 |
| `root/nodes/li/parms/bloodRotWeight` | 1.9% (3/156) | 数值 | 1 |
| `root/nodes/li/parms/canBeSpace` | 1.3% (2/156) | 布尔 | true |
| `root/nodes/li/parms/chosenPawnSignal` | 0.6% (1/156) | 文本 | ChosenPawnForReward |
| `root/nodes/li/parms/contents` | 0.6% (1/156) | 文本 | $laborers |
| `root/nodes/li/parms/customLetterLabel` | 1.3% (2/156) | 文本 | [asker_faction_leaderTitle] arrived / [lodgersLabelSingOrPlural] arrived |
| `root/nodes/li/parms/customLetterText` | 1.9% (3/156) | 文本 | The [asker_faction_leaderTitle] of [asker_faction_name], has arrived.\n\nProtect / [lodgersLabelSingOrPluralDe |
| `root/nodes/li/parms/disallowedThingDefs` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/parms/disallowedThingDefs/li` | 0.6% (1/156) | 文本 | $requestedThing |
| `root/nodes/li/parms/excludeAskerFactionDefs` | 0.6% (1/156) | 文本 | $excludeAskerFaction |
| `root/nodes/li/parms/excludeFactionDefs` | 0.6% (1/156) | 文本 | $excludeAskerFactionDefs |
| `root/nodes/li/parms/factionOf` | 0.6% (1/156) | 文本 | $asker |
| `root/nodes/li/parms/generateShuttleOrPods` | 0.6% (1/156) | 布尔 | false |
| `root/nodes/li/parms/giveToCaravan` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/parms/helpersChance` | 3.2% (5/156) | 数值/文本 | $helpersChance / 0.4 |
| `root/nodes/li/parms/helpersLeaveAfterTicks` | 1.3% (2/156) | 数值 | -1 |
| `root/nodes/li/parms/hiddenSitePartsPossible` | 4.5% (7/156) | 布尔/文本 | $hiddenSitePartsPossible / false / true |
| `root/nodes/li/parms/ifWorldPawnThenMustBeFree` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/parms/ifWorldPawnThenMustBeFreeOrLeader` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/parms/joiningPawns` | 1.3% (2/156) | 文本 | $lodgers |
| `root/nodes/li/parms/joinPlayer` | 1.3% (2/156) | 布尔/文本 | $lodgersAreNotPrisoners / true |
| `root/nodes/li/parms/makePrisoners` | 0.6% (1/156) | 文本 | $lodgersArePrisoners |
| `root/nodes/li/parms/minPointsThreeStar` | 1.3% (2/156) | 数值 | 350 / 600 |
| `root/nodes/li/parms/minPointsTwoStar` | 1.3% (2/156) | 数值 | 250 / 400 |
| `root/nodes/li/parms/moodThresholdWeight` | 1.9% (3/156) | 数值 | 0 / 1 |
| `root/nodes/li/parms/noConditionsMaxPoints` | 0.6% (1/156) | 数值 | 701 |
| `root/nodes/li/parms/noConditionsWeight` | 1.9% (3/156) | 数值 | 1 |
| `root/nodes/li/parms/noWorkWeight` | 1.9% (3/156) | 数值 | 0 / 4 |
| `root/nodes/li/parms/owningFaction` | 0.6% (1/156) | 文本 | $permitFaction |
| `root/nodes/li/parms/paralysisWeight` | 1.9% (3/156) | 数值 | 1 |
| `root/nodes/li/parms/peacefulChallengeRating` | 0.6% (1/156) | 数值 | 1 |
| `root/nodes/li/parms/points` | 1.9% (3/156) | 文本 | $($points * 0.75 * 1.4) / $($points + $helpersPoints) / $sitePoints |
| `root/nodes/li/parms/pointsFactorThreeStar` | 6.4% (10/156) | 数值 | 1 / 2 |
| `root/nodes/li/parms/pointsFactorTwoStar` | 6.4% (10/156) | 数值 | 1 / 1.5 |
| `root/nodes/li/parms/royalAskerNeedsResearchedFurniture` | 1.3% (2/156) | 布尔/文本 | $royalAskerNeedsResearchedFurniture / true |
| `root/nodes/li/parms/selectionWeightOneStar` | 3.9% (6/156) | 数值 | 0.4 / 0.5 |
| `root/nodes/li/parms/selectionWeightThreeStar` | 3.9% (6/156) | 数值 | 0.2 / 0.25 / 0.3 |
| `root/nodes/li/parms/selectionWeightTwoStar` | 3.9% (6/156) | 数值 | 0.3 / 0.35 |
| `root/nodes/li/parms/sendArrivalLetter` | 3.2% (5/156) | 布尔 | false / true |
| `root/nodes/li/parms/siteFaction` | 0.6% (1/156) | 文本 | Empire |
| `root/nodes/li/parms/worldObjectDef` | 0.6% (1/156) | 文本 | ClaimableSite |
| `root/nodes/li/pawn` | 2.6% (4/156) | 文本 | $asker / $prisoner / $refugee |
| `root/nodes/li/pawns` | 19.9% (31/156) | 文本 | $asker / $joiner / $lodgers |
| `root/nodes/li/peaceTalksCantExist` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/permitShuttle` | 1.3% (2/156) | 文本 | $permitShuttle |
| `root/nodes/li/plant` | 0.6% (1/156) | 文本 | $plantToHarvest |
| `root/nodes/li/playerCantBeAttackingCurrently` | 0.6% (1/156) | 布尔 | true |
| `root/nodes/li/pointsCurve` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/pointsCurve/points` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/pointsCurve/points/li` | 3.2% (5/156) | 文本 | (100, 1) / (1000, 8) / (200, 2) |
| `root/nodes/li/pointsPerArea` | 1.9% (3/156) | 数值 | 6.0 / 8.3 |
| `root/nodes/li/pointsToAnimalDifficultyCurve` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/pointsToAnimalDifficultyCurve/points` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/pointsToAnimalDifficultyCurve/points/li` | 1.9% (3/156) | 文本 | (2000, 1500) / (4000, 3600) / (50, 200) |
| `root/nodes/li/pointsToAnimalsToHuntCountCurve` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/pointsToAnimalsToHuntCountCurve/points` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/pointsToAnimalsToHuntCountCurve/points/li` | 1.9% (3/156) | 文本 | (100, 1) / (1000, 10) / (3000, 20) |
| `root/nodes/li/pointsToMaxItemMarketValueCurve` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/pointsToMaxItemMarketValueCurve/points` | 0.6% (1/156) | 容器 |  |
| `root/nodes/li/pointsToMaxItemMarketValueCurve/points/li` | 1.9% (3/156) | 文本 | (300, 800) / (5000, 4000) / (700, 1500) |
| `root/nodes/li/pointsToRequiredWorkCurve` | 1.3% (2/156) | 容器 |  |
| `root/nodes/li/pointsToRequiredWorkCurve/points` | 1.3% (2/156) | 容器 |  |
| `root/nodes/li/pointsToRequiredWorkCurve/points/li` | 5.1% (8/156) | 文本 | (100, 20000) / (1400, 80000) / (2800, 120000) |
| `root/nodes/li/preferCloserTiles` | 8.3% (13/156) | 布尔 | true |
| `root/nodes/li/preferMapWithMinFreeColonists` | 0.6% (1/156) | 文本 | $colonistsToLendCount |
| `root/nodes/li/productionItemCountRandomFactorRange` | 0.6% (1/156) | 文本 | 0.75~1.25 |
| `root/nodes/li/qualityGenerator` | 0.6% (1/156) | 文本 | Reward |
| `root/nodes/li/race` | 0.6% (1/156) | 文本 | $animalToHunt |
| `root/nodes/li/raidAttackRemainingHoursRange` | 0.6% (1/156) | 文本 | 6~48 |
| `root/nodes/li/raidChance` | 0.6% (1/156) | 数值 | 1 |
| `root/nodes/li/raidLetterText` | 0.6% (1/156) | 文本 | {BASETEXT}\n\nThe [enemyFaction_pawnsPlural] [attackReason]. |
| `root/nodes/li/raidPawnKind` | 0.6% (1/156) | 文本 | $raidPawnKind |
| `root/nodes/li/range` | 1.3% (2/156) | 文本 | 0.7~1.3 / 1~3 |
| `root/nodes/li/reason` | 1.3% (2/156) | 文本 | AcceptedDeserter / LaborersMissedShuttle |
| `root/nodes/li/rejection` | 0.6% (1/156) | 文本 | AggressiveRejection |
| `root/nodes/li/requestedThingCount` | 0.6% (1/156) | 文本 | $requestedThingCount |
| `root/nodes/li/requestedThingDef` | 0.6% (1/156) | 文本 | $requestedThing |
| `root/nodes/li/requireColonistCount` | 1.3% (2/156) | 文本 | $requireColonistCount |
| `root/nodes/li/requiredItems` | 1.3% (2/156) | 文本 | $requiredItems |
| `root/nodes/li/requiredPawns` | 1.3% (2/156) | 文本 | $requiredPawns |
| `root/nodes/li/reserach` | 1.3% (2/156) | 文本 | BasicGravtech |
| `root/nodes/li/rewardDetailsHidden` | 2.6% (4/156) | 布尔 | true |
| `root/nodes/li/roundRandom` | 1.9% (3/156) | 布尔 | True / true |
| `root/nodes/li/selectLandmarkChance` | 9.0% (14/156) | 数值 | 0 / 0.05 / 0.5 |
| `root/nodes/li/sendAwayIfAllDespawned` | 0.6% (1/156) | 文本 | $sendAwayIfAllDespawned |
| `root/nodes/li/sendStandardLetter` | 3.9% (6/156) | 布尔 | false / true |
| `root/nodes/li/settlement` | 1.3% (2/156) | 文本 | $settlement |
| `root/nodes/li/shipJobStartMode` | 1.3% (2/156) | 文本 | Instant |
| `root/nodes/li/shipThing` | 1.3% (2/156) | 文本 | $dropoffShipThing / $pickupShipThing |
| `root/nodes/li/signalListenMode` | 3.9% (6/156) | 文本 | NotYetAcceptedOnly / OngoingOnly |
| `root/nodes/li/site` | 0.6% (1/156) | 文本 | $site |
| `root/nodes/li/sitePartDef` | 7.0% (11/156) | 文本 | OpportunitySite_AncientChemfuelRefinery / OpportunitySite_AncientGarrison / OpportunitySite_AncientLaunchSite |
| `root/nodes/li/sitePartDefs` | 9.0% (14/156) | 文本 | $site/sitePartDefs / $sitePartDefs |
| `root/nodes/li/sitePartsParams` | 1.9% (3/156) | 文本 | $sitePartsParams |
| `root/nodes/li/sitePartsTags` | 7.0% (11/156) | 文本 | $sitePartsTags |
| `root/nodes/li/sitePartsTags/li` | 9.6% (15/156) | 容器 |  |
| `root/nodes/li/sitePartsTags/li/chance` | 3.2% (5/156) | 文本 | $siteThreatChance |
| `root/nodes/li/sitePartsTags/li/tag` | 9.6% (15/156) | 文本 | BanditCamp / DownedRefugee / DownedRefugeeQuestThreat |
| `root/nodes/li/sketch` | 1.9% (3/156) | 文本 | $monumentSketch / $sketch |
| `root/nodes/li/storeAggressiveAs` | 0.6% (1/156) | 文本 | aggressive |
| `root/nodes/li/storeAnimalToHuntAs` | 0.6% (1/156) | 文本 | animalToHunt |
| `root/nodes/li/storeAs` | 69.9% (109/156) | 文本 | rewardValue / sitePartDefs / sitePoints |
| `root/nodes/li/storeBenefitAs` | 0.6% (1/156) | 文本 | benefit |
| `root/nodes/li/storeCanCaravanAs` | 0.6% (1/156) | 文本 | canCaravan |
| `root/nodes/li/storeCountToHuntAs` | 0.6% (1/156) | 文本 | countToHunt |
| `root/nodes/li/storeDownsideAs` | 0.6% (1/156) | 文本 | downside |
| `root/nodes/li/storeEstimatedTravelTimeAs` | 0.6% (1/156) | 文本 | estimatedTravelTime |
| `root/nodes/li/storeFactionAs` | 5.8% (9/156) | 文本 | siteFaction |
| `root/nodes/li/storeFactionLeaderAs` | 0.6% (1/156) | 文本 | asker |
| `root/nodes/li/storeFormAs` | 0.6% (1/156) | 文本 | form |
| `root/nodes/li/storeGameConditionAs` | 0.6% (1/156) | 文本 | gameCondition |
| `root/nodes/li/storeGameConditionDescriptionFutureAs` | 0.6% (1/156) | 文本 | gameConditionDescriptionFuture |
| `root/nodes/li/storeGameConditionDifficultyAs` | 0.6% (1/156) | 文本 | gameConditionDifficulty |
| `root/nodes/li/storeGameConditionDurationAs` | 0.6% (1/156) | 文本 | gameConditionDuration |
| `root/nodes/li/storeGrowDaysAs` | 0.6% (1/156) | 文本 | growDays |
| `root/nodes/li/storeHarvestItemCountAs` | 0.6% (1/156) | 文本 | harvestItemCount |
| `root/nodes/li/storeHarvestItemDefAs` | 0.6% (1/156) | 文本 | plantToHarvest |
| `root/nodes/li/storeHasQualityAs` | 0.6% (1/156) | 文本 | requestedThingHasQuality |
| `root/nodes/li/storeLoopCounterAs` | 0.6% (1/156) | 文本 | raidLoopCounter |
| `root/nodes/li/storeMarketValueAs` | 2.6% (4/156) | 文本 | monumentRequiredResourcesMarketValue / requestedThingMarketValue |
| `root/nodes/li/storeProductionItemCountAs` | 0.6% (1/156) | 文本 | countToProduce |
| `root/nodes/li/storeProductionItemDefAs` | 0.6% (1/156) | 文本 | defToProduce |
| `root/nodes/li/storeProductionItemLabelAs` | 0.6% (1/156) | 文本 | thingToProduceLabel |
| `root/nodes/li/storeProductionItemStuffAs` | 0.6% (1/156) | 文本 | stuffToProduce |
| `root/nodes/li/storeRejectionAs` | 0.6% (1/156) | 文本 | rejection |
| `root/nodes/li/storeSitePartsParamsAs` | 7.0% (11/156) | 文本 | sitePartsParams |
| `root/nodes/li/storeThingAs` | 0.6% (1/156) | 文本 | requestedThing |
| `root/nodes/li/storeThingCountAs` | 0.6% (1/156) | 文本 | requestedThingCount |
| `root/nodes/li/structureMutator` | 3.2% (5/156) | 文本 | AncientChemfuelRefinery / AncientGarrison / AncientLaunchSite |
| `root/nodes/li/stuff` | 0.6% (1/156) | 文本 | $stuffToProduce |
| `root/nodes/li/tag` | 3.9% (6/156) | 文本 | $signalTag / $tag / EndGame_ShipEscape |
| `root/nodes/li/text` | 3.2% (5/156) | 文本 | $customLetterText / The laborers from [permitFaction_name] have arrived. A shuttle will come to coll / [factio |
| `root/nodes/li/textRules` | 0.6% (1/156) | 文本 | $customLetterTextRules |
| `root/nodes/li/thing` | 3.9% (6/156) | 文本 | $asker / $monumentMarker |
| `root/nodes/li/things` | 1.9% (3/156) | 文本 | $itemPodsContents / $monumentMarker |
| `root/nodes/li/thingSetMaker` | 1.9% (3/156) | 文本 | Reward_GravshipUpgrade / Reward_ItemsStandard |
| `root/nodes/li/thingsToExcludeFromHyperlinks` | 0.6% (1/156) | 文本 | $monumentMarkerMinified |
| `root/nodes/li/threeStarRange` | 1.3% (2/156) | 文本 | 0.61~0.75 / 20~30 |
| `root/nodes/li/threshold` | 1.3% (2/156) | 文本 | $lodgersMoodThreshold / $moodThreshold |
| `root/nodes/li/ticks` | 0.6% (1/156) | 文本 | $leaveDelayTicks |
| `root/nodes/li/tile` | 9.0% (14/156) | 文本 | $siteTile / $tile |
| `root/nodes/li/title` | 0.6% (1/156) | 文本 | Yeoman |
| `root/nodes/li/totalMarketValueRange` | 0.6% (1/156) | 文本 | $itemPodsTotalMarketValueRange |
| `root/nodes/li/transportShip` | 5.1% (8/156) | 文本 | $dropOffShip / $pickUpShip |
| `root/nodes/li/twoStarRange` | 1.3% (2/156) | 文本 | 0.36~0.6 / 10~20 |
| `root/nodes/li/unsatisfiedDropMode` | 0.6% (1/156) | 文本 | All |
| `root/nodes/li/useDifficultyFactor` | 0.6% (1/156) | 布尔 | false |
| `root/nodes/li/useOnlyResourcesAvailableOnMap` | 1.9% (3/156) | 文本 | $map |
| `root/nodes/li/useTradeDropSpot` | 1.9% (3/156) | 布尔 | true |
| `root/nodes/li/value` | 62.8% (98/156) | 布尔/数值/文本 | $($requestedThingMarketValue * $wealthRewardValueFactor * randFloat(1.5, 2.1)) / $(30*60000) / $mapWealth |
| `root/nodes/li/value1` | 11.5% (18/156) | 文本 | $points / $raidCountMinusOne / $requestedThing |
| `root/nodes/li/value2` | 11.5% (18/156) | 数值/文本 | $minPointsTwoStar / $pointsFactor / 1.75 |
| `root/nodes/li/waitUntilPlayerHasHomeMap` | 4.5% (7/156) | 布尔 | true |
| `root/nodes/li/walkInSpot` | 0.6% (1/156) | 文本 | $walkInSpot |
| `root/nodes/li/workAmountRandomFactorRange` | 0.6% (1/156) | 文本 | 0.75~1.25 |
| `root/nodes/li/workRandomFactorRange` | 0.6% (1/156) | 文本 | 0.75~1.25 |
| `root/nodes/li/worldObject` | 17.9% (28/156) | 文本 | $escapeShip / $peaceTalks / $site |
| `root/nodes/li/worldObjectDef` | 5.1% (8/156) | 文本 | AsteroidMiningSite / ClaimableSite / ClaimableSpaceSite |
| `root/nodes/li/worldObjects` | 8.3% (13/156) | 文本 | $escapeShip / $peaceTalks / $site |
| `root/options` | 1.3% (2/156) | 容器 |  |
| `root/options/li` | 6.4% (10/156) | 容器 |  |
| `root/options/li/def` | 6.4% (10/156) | 文本 | FibrousMechanites / GutWorms / MuscleParasites |
| `root/options/li/partsToAffect` | 0.6% (1/156) | 容器 |  |
| `root/options/li/partsToAffect/li` | 0.6% (1/156) | 文本 | Stomach |
| `root/requiredSubquestsGiven` | 4.5% (7/156) | 数值 | 1 / 2 / 3 |
| `root/requiresLandmark` | 0.6% (1/156) | 布尔 | true |
| `root/selectLandmarkChance` | 6.4% (10/156) | 数值 | 0 / 1 |
| `root/singleSitePartRules` | 0.6% (1/156) | 容器 |  |
| `root/singleSitePartRules/rulesStrings` | 0.6% (1/156) | 容器 |  |
| `root/singleSitePartRules/rulesStrings/li` | 13.5% (21/156) | 文本 | root(priority=1,sitePart==ClimateAdjuster)->there's (*Threat)a climate adjuster  / root(priority=1,sitePart==P |
| `root/siteFactions` | 0.6% (1/156) | 容器 |  |
| `root/siteFactions/li` | 1.3% (2/156) | 文本 | Pirate / PirateWaster |
| `root/sitePartsParams` | 0.6% (1/156) | 文本 | $sitePartsParams |
| `root/storeAs` | 1.3% (2/156) | 文本 | rewardValue / site |
| `root/storeHediffAs` | 1.3% (2/156) | 文本 | lodgersDisease |
| `root/storePartsToAffectAs` | 1.3% (2/156) | 文本 | lodgersDiseasePartsToAffect |
| `root/subquestDefs` | 0.6% (1/156) | 容器 |  |
| `root/subquestDefs/li` | 5.8% (9/156) | 文本 | Gravcore_AncientReactor / Gravcore_InsectLair / Gravcore_MechanoidRelay |
| `root/tile` | 0.6% (1/156) | 文本 | $siteTile |
| `root/value` | 0.6% (1/156) | 文本 | $points |
| `rootEarliestDay` | 0.6% (1/156) | 数值 | 45 |
| `rootIncreasesPopulation` | 5.8% (9/156) | 布尔 | true |
| `rootMinPoints` | 24.4% (38/156) | 数值 | 0 / 300 / 350 |
| `rootMinProgressScore` | 8.3% (13/156) | 数值 | 10 / 3 / 5 |
| `rootSelectionWeight` | 41.0% (64/156) | 数值 | 0 / 0.5 / 1 |
| `rootSelectionWeightFactorFromPointsCurve` | 0.6% (1/156) | 容器 |  |
| `rootSelectionWeightFactorFromPointsCurve/points` | 0.6% (1/156) | 容器 |  |
| `rootSelectionWeightFactorFromPointsCurve/points/li` | 1.9% (3/156) | 文本 | (0,3) / (200,3) / (500,1) |
| `sendAvailableLetter` | 3.2% (5/156) | 布尔 | false / true |
| `successHistoryEvent` | 14.1% (22/156) | 文本 | CharityFulfilled_RefugeePodCrash / CharityFulfilled_ThreatReward_Joiner / CharityFulfilled_WandererJoins |

## 四、原版 defName 一览（共 156 个，列出前 60）

```text
`CreepJoinerArrival`              ``                                `Decree_Util_Reward`              `MysteriousCargoRevenantSpine`  
`Util_MechCluster`                `MysteriousCargoUnnaturalCorpse`  `MysteriousCargoCube`             `Hospitality_Util_DecideLodgerCountFromPoints`
`DelayedRewardDropPods`           ``                                `Util_RandomSelectDiseaseAnimal`  `Util_Constants_Monuments`      
`Util_ManhunterPack`              `MonolithMigration`               `AncientSignalActivation`         `BestowingCeremony`             
``                                `EndGame_VoidMonolith`            `Util_JoinerThreat_Joiner`        `MechanoidSignal`               
`Util_GetDefaultRewardValueFromPoints`  `EndGame_ArchonexusVictory`       `CreepJoinerArrival_Metalhorror`  `RefugeePodCrash_Ghoul`         
`MechanitorStartingMech`          `WandererJoins`                   `RefugeeDelayedReward`            `OpportunitySite_DistressCall`  
`SightstealerArrival`             `Util_GameConditionNegativeRandom`  `Util_Infestation`                `RefugeePodCrash_Baby`          
`RefugeePodCrash`                 `Util_Raid`                       `WandererJoinAbasia`              `EndGame_ArchonexusVictory_SecondCycle`
`Gravcore_InsectLair`             `Gravcore_AncientReactor`         `Gravcore_OrbitalMechanoidPlatform`  `Gravcore_OrbitalAncientPlatform`
``                                `Gravcore_Mechhive`               `EndGame_ArchonexusVictory_FirstCycle`  `Bossgroup`                     
`PollutionRaid`                   `Util_JoinerDropIn`               `Util_MaybeApplyGoodwillForMood`  `UnnaturalDarkness`             
`Opportunity_AncientInfestedSettlement`  `Gravcore_FrozenTerraformer`      `Util_JoinerWalkIn`               `Opportunity_AncientStructureLaunchSite`
`Opportunity_AncientStructureWarehouse`  `GravEngine`                      `GravshipWreckage`                `EndGame_ArchonexusVictory_ThirdCycle`
`Opportunity_AncientStructureChemfuelRefinery`  `Gravcore_AncientStockpile`       `Util_RandomSelectDiseaseHuman`   `Hospitality_Util_AddHealthConditions`
```

_余下 96 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
