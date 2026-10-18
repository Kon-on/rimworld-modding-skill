# ManeuverDef

- **所属线**：世界线
- **原版实例数**：12
- **字段路径数**：16
- **资料片**：Core、Odyssey
- **原版出处**：`Core/Defs/Maneuvers/Maneuvers.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<ManeuverDef>
    <defName>Slash</defName>
    <requiredCapacity>Cut</requiredCapacity>
    <verb>
      <verbClass>Verb_MeleeAttackDamage</verbClass>
      <meleeDamageDef>Cut</meleeDamageDef>
    </verb>
    <logEntryDef>MeleeAttack</logEntryDef>
    <combatLogRulesHit>Maneuver_Slash_MeleeHit</combatLogRulesHit>
    <combatLogRulesDeflect>Maneuver_Slash_MeleeDeflect</combatLogRulesDeflect>
    <combatLogRulesMiss>Maneuver_Slash_MeleeMiss</combatLogRulesMiss>
    <combatLogRulesDodge>Maneuver_Slash_MeleeDodge</combatLogRulesDodge>
  </ManeuverDef>

  
```

> 来自 `Core/Defs/Maneuvers/Maneuvers.xml`，defName = `Slash`，XML 节点数 11（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
combatLogRulesDeflect                          [文本]  例：Maneuver_Scratch_MeleeDeflect / Maneuver_Slash_MeleeDeflect / Maneuver_Smash_MeleeDeflect
combatLogRulesDodge                            [文本]  例：Maneuver_Scratch_MeleeDodge / Maneuver_Slash_MeleeDodge / Maneuver_Smash_MeleeDodge
combatLogRulesHit                              [文本]  例：Maneuver_Scratch_MeleeHit / Maneuver_Slash_MeleeHit / Maneuver_Smash_MeleeHit
combatLogRulesMiss                             [文本]  例：Maneuver_Scratch_MeleeMiss / Maneuver_Slash_MeleeMiss / Maneuver_Smash_MeleeMiss
defName                                        [文本]  例：Demolish / Slash / Smash
logEntryDef                                    [文本]  例：MeleeAttack / SandInEyes
requiredCapacity                               [文本]  例：Blunt / Cut / Demolish
verb                                           [容器]
verb/meleeDamageDef                            [文本]  例：Blunt / Cut / Demolish
verb/verbClass                                 [文本]  例：Verb_MeleeApplyHediff / Verb_MeleeAttackDamage
```

## 三、全量字段表（16 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `combatLogRulesDeflect` | 100.0% (12/12) | 文本 | Maneuver_Scratch_MeleeDeflect / Maneuver_Slash_MeleeDeflect / Maneuver_Smash_MeleeDeflect |
| `combatLogRulesDodge` | 100.0% (12/12) | 文本 | Maneuver_Scratch_MeleeDodge / Maneuver_Slash_MeleeDodge / Maneuver_Smash_MeleeDodge |
| `combatLogRulesHit` | 100.0% (12/12) | 文本 | Maneuver_Scratch_MeleeHit / Maneuver_Slash_MeleeHit / Maneuver_Smash_MeleeHit |
| `combatLogRulesMiss` | 100.0% (12/12) | 文本 | Maneuver_Scratch_MeleeMiss / Maneuver_Slash_MeleeMiss / Maneuver_Smash_MeleeMiss |
| `defName` | 100.0% (12/12) | 文本 | Demolish / Slash / Smash |
| `logEntryDef` | 100.0% (12/12) | 文本 | MeleeAttack / SandInEyes |
| `requiredCapacity` | 100.0% (12/12) | 文本 | Blunt / Cut / Demolish |
| `verb` | 100.0% (12/12) | 容器 |  |
| `verb/ai_IsBuildingDestroyer` | 8.3% (1/12) | 布尔 | true |
| `verb/bodypartTagTarget` | 8.3% (1/12) | 文本 | SightSource |
| `verb/commonalityVsEdificeFactor` | 8.3% (1/12) | 数值 | 0.01 |
| `verb/impactFleck` | 8.3% (1/12) | 文本 | SandInEyes |
| `verb/linkedBodyPartsGroup` | 8.3% (1/12) | 文本 | Feet |
| `verb/meleeDamageDef` | 91.7% (11/12) | 文本 | Blunt / Cut / Demolish |
| `verb/minIntelligence` | 8.3% (1/12) | 文本 | ToolUser |
| `verb/verbClass` | 100.0% (12/12) | 文本 | Verb_MeleeApplyHediff / Verb_MeleeAttackDamage |

## 四、原版 defName 一览（共 12 个，列出前 60）

```text
`Slash`                           `Stab`                            `Smash`                           `Scratch`                       
`ScratchToxic`                    `Poke`                            `ToxicBite`                       `PorcupineBite`                 
`PorcupineScratch`                `Demolish`                        `Bite`                            `KickMaterialInEyes`            
```
