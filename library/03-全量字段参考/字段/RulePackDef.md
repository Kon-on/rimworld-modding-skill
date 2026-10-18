# RulePackDef

- **所属线**：系统线
- **原版实例数**：340
- **字段路径数**：15
- **资料片**：Anomaly、Biotech、Core、Ideology、Odyssey、Royalty
- **原版出处**：`Core/Defs/RulePackDefs/RulePacks_Namers_Art.xml`、`Biotech/Defs/InteractionDefs/Interactions_Social.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<RulePackDef>
    <defName>NamerArtSculpture</defName>
    <include>
      <li>NamerArtCommon</li>
    </include>
  </RulePackDef>

 
```

> 来自 `Core/Defs/RulePackDefs/RulePacks_Namers_Art.xml`，defName = `NamerArtSculpture`，XML 节点数 4（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：DarkDialogue / Description_Tome / NamerArtCubeSculpture
rulePack/rulesStrings/li                       [文本]  例：rambled->chuckled / rambled->rambled / rambled->raved
```

## 三、全量字段表（15 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 99.7% (339/340) | 文本 | DarkDialogue / Description_Tome / NamerArtCubeSculpture |
| `include` | 57.4% (195/340) | 容器 |  |
| `include/li` | 73.5% (250/340) | 文本 | ArtDescriptionUtility_Global / ArtNameUtility / Combat_RangedBase |
| `rulePack` | 85.6% (291/340) | 容器 |  |
| `rulePack/include` | 1.2% (4/340) | 容器 |  |
| `rulePack/include/li` | 1.5% (5/340) | 文本 | LessonInteractionTeachingAdverbs / LessonInteractionTeachingVerbs / NamerAnimalUtility |
| `rulePack/rulesFiles` | 9.7% (33/340) | 容器 |  |
| `rulePack/rulesFiles/li` | 25.0% (85/340) | 文本 | SylN->WordParts/Syllables_Neanderthal / creepjoinerLastname->Names/Creepjoiner_Last / creepjoinerNickname->Nam |
| `rulePack/rulesRaw` | 0.9% (3/340) | 容器 |  |
| `rulePack/rulesRaw/li` | 1.8% (6/340) | 容器 |  |
| `rulePack/rulesRaw/li/gender` | 1.2% (4/340) | 文本 | Female / Male |
| `rulePack/rulesRaw/li/keyword` | 1.8% (6/340) | 文本 | Digit / NamePersonFemale / NamePersonMale |
| `rulePack/rulesRaw/li/range` | 0.3% (1/340) | 文本 | 0~9 |
| `rulePack/rulesStrings` | 84.4% (287/340) | 容器 |  |
| `rulePack/rulesStrings/li` | 2027.3% (6893/340) | 文本 | rambled->chuckled / rambled->rambled / rambled->raved |

## 四、原版 defName 一览（共 340 个，列出前 60）

```text
`NamerArtSculpture`               `NamerArtFurniture`               `NamerArtSarcophagusPlate`        `NamerArtWeaponMelee`           
`NamerArtWeaponGun`               `DeityTypeMakerCorunan`           `DeityTypeMakerRustican`          `DeityTypeMakerKriminul`        
`DeityTypeMakerSophian`           `DeityTypeMakerAstropolitan`      `NamerIdeoSophian`                `NamerFestivalAstropolitan`     
`NamerFestivalRustican`           `NamerFestivalCorunan`            `NamerFestivalKriminul`           `NamerFestivalSophian`          
`Event_UnnaturalCorpseAttack`     `Event_DevourerConsumeLeap`       `Event_DevourerDigestionAborted`  `Event_DevourerDigestionCompleted`
`Event_MetalhorrorEmerged`        `Event_Hypnotized`                `Sentence_RecruitAttemptAccepted`  `Sentence_RecruitAttemptRejected`
`Sentence_MarriageProposalAccepted`  `Sentence_MarriageProposalRejected`  `Sentence_MarriageProposalRejectedBrokeUp`  `Sentence_SocialFightStarted`   
`Battle_Solo`                     `Battle_Duel`                     `Battle_Internal`                 `Battle_War`                    
`Battle_Brawl`                    `Event_AbilityUsed`               `Event_ItemUsed`                  `Maneuver_Slash_MeleeHit`       
`Maneuver_Slash_MeleeDeflect`     `Maneuver_Slash_MeleeMiss`        `Maneuver_Slash_MeleeDodge`       `Maneuver_Stab_MeleeHit`        
`Maneuver_Stab_MeleeDeflect`      `Maneuver_Stab_MeleeMiss`         `Maneuver_Stab_MeleeDodge`        `Maneuver_Smash_MeleeHit`       
`Maneuver_Smash_MeleeDeflect`     `Maneuver_Smash_MeleeMiss`        `Maneuver_Smash_MeleeDodge`       `Maneuver_Scratch_MeleeHit`     
`Maneuver_Scratch_MeleeDeflect`   `Maneuver_Scratch_MeleeMiss`      `Maneuver_Scratch_MeleeDodge`     `Maneuver_Poke_MeleeHit`        
`Maneuver_Poke_MeleeDeflect`      `Maneuver_Poke_MeleeMiss`         `Maneuver_Poke_MeleeDodge`        `Maneuver_Bite_MeleeHit`        
`Maneuver_Bite_MeleeDeflect`      `Maneuver_Bite_MeleeMiss`         `Maneuver_Bite_MeleeDodge`        `Maneuver_KickMaterialInEyes_MeleeDeflect`
```

_余下 280 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
