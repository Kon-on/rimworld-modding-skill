# MutantDef

- **所属线**：人物线
- **原版实例数**：4
- **字段路径数**：138
- **资料片**：Anomaly
- **原版出处**：`Anomaly/Defs/Misc/Mutants.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<MutantDef ParentName="BaseMutantEntity">
    <defName>AwokenCorpse</defName>
    <label>awoken corpse</label>
    <hediff>AwokenCorpse</hediff>
    <thinkTree>AwokenCorpse</thinkTree>
    <thinkTreeConstant>AwokenCorpseConstant</thinkTreeConstant>
    <useCorpseGraphics>true</useCorpseGraphics>
    <deathOnDownedChance>0</deathOnDownedChance>
    <canTravelInCaravan>false</canTravelInCaravan>
    <respectsAllowedArea>false</respectsAllowedArea>
    <canGainXP>false</canGainXP>
    <entitledToMedicalCare>false</entitledToMedicalCare>
    <showInScenarioEditor>false</showInScenarioEditor>
    <restoreLegs>true</restoreLegs>
    <defaultFaction>Entities</defaultFaction>
    <woundColor>(0.3, 0.3, 0.0, 1.0)</woundColor>
    <anomalyKnowledgeOffset>0.4</anomalyKnowledgeOffset>
    <knowledgeCategory>Basic</knowledgeCategory>
    <psychicShockUntargetable>true</psychicShockUntargetable>
    <canOpenAnyDoor>true</canOpenAnyDoor>
    <givesHediffs>
      <li>
        <def>RapidRegeneration</def>
      </li>
    </givesHediffs>
    <abilities>
      <li>UnnaturalCorpseSkip</li>
    </abilities>
  </MutantDef>
```

> 来自 `Anomaly/Defs/Misc/Mutants.xml`，defName = `AwokenCorpse`，XML 节点数 25（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
drugWhitelist/li                               [文本]  例：JuggernautSerum / MetalbloodSerum / MindNumbSerum
forcedHeadTypes/li                             [文本]  例：Ghoul_Heavy / Ghoul_Narrow / Ghoul_Normal
removesHediffs/li                              [文本]  例：CryptosleepSickness / LuciferiumAddiction / LuciferiumHigh
tools/li                                       [容器]
tools/li/alwaysTreatAsWeapon                   [布尔]  例：true
tools/li/capacities                            [容器]
tools/li/capacities/li                         [文本]  例：Bite / Scratch
tools/li/chanceFactor                          [数值]  例：0.5 / 1 / 1.5
tools/li/cooldownTime                          [数值]  例：2
tools/li/label                                 [文本]  例：left hand / right claw / right hand
tools/li/labelNoLocation                       [文本]  例：claw / hand
tools/li/linkedBodyPartsGroup                  [文本]  例：LeftHand / RightHand / Teeth
tools/li/power                                 [数值]  例：7.0 / 8.2
tools/li/soundMeleeHit                         [文本]  例：Pawn_Ghoul_Scratch / Pawn_Melee_HumanBite_Hit
tools/li/soundMeleeMiss                        [文本]  例：Pawn_Melee_HumanBite_Miss / Pawn_Melee_SmallScratch_Miss
whitelistedFloatMenuProviders/li               [文本]  例：FloatMenuOptionProvider_DraftedAttack / FloatMenuOptionProvider_DraftedMove / FloatMenuOptionProvider_GhoulRest
```

## 三、全量字段表（138 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `abilities` | 25.0% (1/4) | 容器 |  |
| `abilities/li` | 25.0% (1/4) | 文本 | UnnaturalCorpseSkip |
| `abilityWhitelist` | 25.0% (1/4) | 容器 |  |
| `abilityWhitelist/li` | 75.0% (3/4) | 文本 | CorrosiveSpray / GhoulFrenzy / MetalbloodInjection |
| `allowEatingCorpses` | 25.0% (1/4) | 布尔 | true |
| `allowedDevelopmentalStages` | 25.0% (1/4) | 文本 | Adult |
| `anomalyKnowledgeOffset` | 75.0% (3/4) | 数值 | 0 / 0.4 / 0.5 |
| `beardTagFilter` | 25.0% (1/4) | 容器 |  |
| `beardTagFilter/tags` | 25.0% (1/4) | 容器 |  |
| `beardTagFilter/tags/li` | 25.0% (1/4) | 文本 | NoBeard |
| `beardTagFilter/whitelist` | 25.0% (1/4) | 布尔 | true |
| `bloodDef` | 25.0% (1/4) | 文本 | Filth_DarkBlood |
| `bloodSmearDef` | 25.0% (1/4) | 文本 | Filth_DarkBloodSmear |
| `bodyTypeGraphicPaths` | 25.0% (1/4) | 容器 |  |
| `bodyTypeGraphicPaths/Fat` | 25.0% (1/4) | 文本 | Things/Pawn/Ghoul/Bodies/Ghoulskin_Fat |
| `bodyTypeGraphicPaths/Female` | 25.0% (1/4) | 文本 | Things/Pawn/Ghoul/Bodies/Ghoulskin_Female |
| `bodyTypeGraphicPaths/Hulk` | 25.0% (1/4) | 文本 | Things/Pawn/Ghoul/Bodies/Ghoulskin_Hulk |
| `bodyTypeGraphicPaths/Male` | 25.0% (1/4) | 文本 | Things/Pawn/Ghoul/Bodies/Ghoulskin_Male |
| `bodyTypeGraphicPaths/Thin` | 25.0% (1/4) | 文本 | Things/Pawn/Ghoul/Bodies/Ghoulskin_Thin |
| `breathesAir` | 25.0% (1/4) | 布尔 | false |
| `canAttackWhileCrawling` | 25.0% (1/4) | 布尔 | true |
| `canBeCapturedToHoldingPlatform` | 25.0% (1/4) | 布尔 | true |
| `canBeDrafted` | 25.0% (1/4) | 布尔 | false |
| `canBleed` | 25.0% (1/4) | 布尔 | false |
| `canCarryPawns` | 25.0% (1/4) | 布尔 | false |
| `canGainXP` | 50.0% (2/4) | 布尔 | false |
| `canOpenAnyDoor` | 25.0% (1/4) | 布尔 | true |
| `canOpenDoors` | 25.0% (1/4) | 布尔 | false |
| `canTend` | 25.0% (1/4) | 布尔 | false |
| `canTravelInCaravan` | 50.0% (2/4) | 布尔 | false |
| `canUseDrugs` | 25.0% (1/4) | 布尔 | true |
| `clearMutantStatusOnDeath` | 25.0% (1/4) | 布尔 | true |
| `clearsEgo` | 25.0% (1/4) | 布尔 | true |
| `codexEntry` | 50.0% (2/4) | 文本 | Ghoul / Shambler |
| `consideredSubhuman` | 25.0% (1/4) | 布尔 | true |
| `deathLetter` | 25.0% (1/4) | 文本 | One of your ghouls has died. |
| `deathLetterExtra` | 25.0% (1/4) | 文本 | Unlike regular colonists, ghouls do not need to be buried and their death will n |
| `deathOnDownedChance` | 75.0% (3/4) | 数值 | 0 / 0.25 |
| `defaultFaction` | 50.0% (2/4) | 文本 | Entities |
| `defName` | 75.0% (3/4) | 文本 | AwokenCorpse / Ghoul / Shambler |
| `description` | 50.0% (2/4) | 文本 | A creature who has been raised from the dead by corrupted nano-scale archites.\n / A person who has been turne |
| `disableAging` | 25.0% (1/4) | 布尔 | true |
| `disableApparel` | 25.0% (1/4) | 布尔 | true |
| `disableEatingAtTable` | 25.0% (1/4) | 布尔 | true |
| `disableFlying` | 25.0% (1/4) | 布尔 | true |
| `disableHostilityResponse` | 25.0% (1/4) | 布尔 | true |
| `disableNeeds` | 25.0% (1/4) | 布尔 | true |
| `disableOwnership` | 25.0% (1/4) | 布尔 | true |
| `disablePolicies` | 25.0% (1/4) | 布尔 | true |
| `disablesGenes` | 50.0% (2/4) | 容器 |  |
| `disablesGenes/li` | 75.0% (3/4) | 文本 | Deathrest / Furskin / Hemogenic |
| `disablesIdeo` | 25.0% (1/4) | 布尔 | true |
| `disableTitles` | 25.0% (1/4) | 布尔 | true |
| `drugWhitelist` | 25.0% (1/4) | 容器 |  |
| `drugWhitelist/li` | 125.0% (5/4) | 文本 | JuggernautSerum / MetalbloodSerum / MindNumbSerum |
| `entitledToMedicalCare` | 50.0% (2/4) | 布尔 | false |
| `foodType` | 25.0% (1/4) | 文本 | CarnivoreAnimalStrict |
| `forcedHeadTypes` | 25.0% (1/4) | 容器 |  |
| `forcedHeadTypes/li` | 100.0% (4/4) | 文本 | Ghoul_Heavy / Ghoul_Narrow / Ghoul_Normal |
| `givesHediffs` | 50.0% (2/4) | 容器 |  |
| `givesHediffs/li` | 50.0% (2/4) | 容器 |  |
| `givesHediffs/li/def` | 50.0% (2/4) | 文本 | RapidRegeneration / Regeneration |
| `givesHediffs/li/severity` | 25.0% (1/4) | 数值 | 0.1 |
| `hairColorOverride` | 25.0% (1/4) | 文本 | (0.65, 0.65, 0.65) |
| `hairTagFilter` | 25.0% (1/4) | 容器 |  |
| `hairTagFilter/tags` | 25.0% (1/4) | 容器 |  |
| `hairTagFilter/tags/li` | 25.0% (1/4) | 文本 | Ghoul |
| `hairTagFilter/whitelist` | 25.0% (1/4) | 布尔 | true |
| `hediff` | 75.0% (3/4) | 文本 | AwokenCorpse / Ghoul / Shambler |
| `hediffGivers` | 25.0% (1/4) | 容器 |  |
| `hediffGivers/li` | 25.0% (1/4) | 容器 |  |
| `hediffGivers/li/hediff` | 25.0% (1/4) | 文本 | MeatHunger |
| `hideLabel` | 25.0% (1/4) | 布尔 | true |
| `incapableOfSocialInteractions` | 25.0% (1/4) | 布尔 | true |
| `isConsideredCorpse` | 25.0% (1/4) | 布尔 | true |
| `isImmuneToInfections` | 25.0% (1/4) | 布尔 | true |
| `knowledgeCategory` | 75.0% (3/4) | 文本 | Basic |
| `label` | 75.0% (3/4) | 文本 | awoken corpse / ghoul / shambler |
| `makesFootprints` | 25.0% (1/4) | 布尔 | false |
| `namePrefix` | 25.0% (1/4) | 文本 | shambler |
| `needWhitelist` | 25.0% (1/4) | 容器 |  |
| `needWhitelist/li` | 25.0% (1/4) | 文本 | Food |
| `overrideFoodType` | 25.0% (1/4) | 布尔 | true |
| `overrideInspectString` | 25.0% (1/4) | 布尔 | true |
| `overrideLabel` | 25.0% (1/4) | 布尔 | true |
| `partsCleanAndDroppable` | 25.0% (1/4) | 布尔 | false |
| `preventsMentalBreaks` | 25.0% (1/4) | 布尔 | true |
| `producesBioferrite` | 25.0% (1/4) | 布尔 | true |
| `psychicShockUntargetable` | 25.0% (1/4) | 布尔 | true |
| `relativeTurnedThought` | 25.0% (1/4) | 文本 | BecameGhoul |
| `removeAddictions` | 25.0% (1/4) | 布尔 | true |
| `removeAllInjuries` | 25.0% (1/4) | 布尔 | true |
| `removeChronicIllnesses` | 25.0% (1/4) | 布尔 | true |
| `removePermanentInjuries` | 25.0% (1/4) | 布尔 | true |
| `removesHediffs` | 25.0% (1/4) | 容器 |  |
| `removesHediffs/li` | 575.0% (23/4) | 文本 | CryptosleepSickness / LuciferiumAddiction / LuciferiumHigh |
| `renderNodeProperties` | 25.0% (1/4) | 容器 |  |
| `renderNodeProperties/li` | 50.0% (2/4) | 容器 |  |
| `renderNodeProperties/li/baseLayer` | 50.0% (2/4) | 数值 | 20 |
| `renderNodeProperties/li/debugLabel` | 50.0% (2/4) | 文本 | Shambler wounds |
| `renderNodeProperties/li/nodeClass` | 25.0% (1/4) | 文本 | PawnRenderNode_AnimalPart |
| `renderNodeProperties/li/overlayLayer` | 50.0% (2/4) | 文本 | Body |
| `renderNodeProperties/li/pawnType` | 50.0% (2/4) | 文本 | HumanlikeOnly / NonHumanlikeOnly |
| `renderNodeProperties/li/workerClass` | 50.0% (2/4) | 文本 | PawnRenderNodeWorker_OverlayShambler |
| `respectsAllowedArea` | 50.0% (2/4) | 布尔 | false |
| `restoreLegs` | 50.0% (2/4) | 布尔 | true |
| `showInScenarioEditor` | 25.0% (1/4) | 布尔 | false |
| `showJobReport` | 25.0% (1/4) | 布尔 | true |
| `skinColorOverride` | 25.0% (1/4) | 文本 | (0.58, 0.62, 0.55) |
| `soundAttack` | 50.0% (2/4) | 文本 | Pawn_Ghoul_Attack / Pawn_Shambler_Attack |
| `soundAttackChance` | 50.0% (2/4) | 数值 | 0.25 |
| `soundCall` | 50.0% (2/4) | 文本 | Pawn_Ghoul_Call / Pawn_Shambler_Call |
| `soundDeath` | 50.0% (2/4) | 文本 | Pawn_Ghoul_Killed / Pawn_Shambler_Killed |
| `soundWounded` | 50.0% (2/4) | 文本 | Pawn_Ghoul_Pain / Pawn_Shambler_Wounded |
| `standingAnimation` | 25.0% (1/4) | 文本 | ShamblerSway |
| `tameable` | 25.0% (1/4) | 布尔 | false |
| `terminatePregnancy` | 25.0% (1/4) | 布尔 | true |
| `thinkTree` | 75.0% (3/4) | 文本 | AwokenCorpse / Ghoul / Shambler |
| `thinkTreeConstant` | 75.0% (3/4) | 文本 | AwokenCorpseConstant / GhoulConstant / ShamblerConstant |
| `tools` | 50.0% (2/4) | 容器 |  |
| `tools/li` | 150.0% (6/4) | 容器 |  |
| `tools/li/alwaysTreatAsWeapon` | 100.0% (4/4) | 布尔 | true |
| `tools/li/capacities` | 150.0% (6/4) | 容器 |  |
| `tools/li/capacities/li` | 150.0% (6/4) | 文本 | Bite / Scratch |
| `tools/li/chanceFactor` | 150.0% (6/4) | 数值 | 0.5 / 1 / 1.5 |
| `tools/li/cooldownTime` | 150.0% (6/4) | 数值 | 2 |
| `tools/li/label` | 150.0% (6/4) | 文本 | left hand / right claw / right hand |
| `tools/li/labelNoLocation` | 100.0% (4/4) | 文本 | claw / hand |
| `tools/li/linkedBodyPartsGroup` | 150.0% (6/4) | 文本 | LeftHand / RightHand / Teeth |
| `tools/li/power` | 150.0% (6/4) | 数值 | 7.0 / 8.2 |
| `tools/li/soundMeleeHit` | 100.0% (4/4) | 文本 | Pawn_Ghoul_Scratch / Pawn_Melee_HumanBite_Hit |
| `tools/li/soundMeleeMiss` | 100.0% (4/4) | 文本 | Pawn_Melee_HumanBite_Miss / Pawn_Melee_SmallScratch_Miss |
| `useCorpseGraphics` | 50.0% (2/4) | 布尔 | true |
| `whitelistedFloatMenuProviders` | 50.0% (2/4) | 容器 |  |
| `whitelistedFloatMenuProviders/li` | 125.0% (5/4) | 文本 | FloatMenuOptionProvider_DraftedAttack / FloatMenuOptionProvider_DraftedMove / FloatMenuOptionProvider_GhoulRes |
| `workDisables` | 25.0% (1/4) | 容器 |  |
| `workDisables/li` | 50.0% (2/4) | 文本 | AllWork / Shooting |
| `woundColor` | 50.0% (2/4) | 文本 | (0.3, 0.3, 0.0, 1.0) |

## 四、原版 defName 一览（共 4 个，列出前 60）

```text
`AwokenCorpse`                    ``                                `Shambler`                        `Ghoul`                         
```
