# AbilityDef

## 用途
AbilityDef 定义一种**主动技能**：灵能、种族能力、装备技能、灵能仪式都走它。它由三块组成：`verbProperties` 决定"怎么放、能选什么目标"，`statBases` 决定消耗与持续时间（灵能系统读 `Ability_PsyfocusCost` / `Ability_EntropyGain`），`comps` 决定"放完发生什么"。
它与 GeneDef（`abilities` 授予基因能力）、RoyalTitleDef（`grantedAbilities`）、HediffDef（`comps/li/abilityDefs`）、MentalStateDef 与 InteractionDef（社交类能力）联动；能力本身不解决"怎么获得"，需要由上述任一途径授予。原版共 107 个实例、260 条字段路径。
> **字段名澄清（重要·待验证项）**：任务书中提到的 `ai_CanDoWhileDowned` 在 `docs/def-schema.json` 全文中检索命中为 0，本机 1.7.4981 rev136 的原版 AbilityDef **不存在该路径**（254 份字段参考中同样没有）。它属"原版未见、无法证实"项，本模板**不使用**；原版实际存在的 AI 相关字段只有 `aiCanUse`、`ai_IsIncendiary`、`ai_IsOffensive`、`ai_SearchAOEForTargets`。

## 模板
```xml
<?xml version="1.0" encoding="utf-8" ?>
<Defs>

  <AbilityDef>
    <defName>EXAMPLE_StunPulse</defName>
    <label>example stun pulse</label>
    <description>Momentarily disrupt motor function in the target's brain, preventing any movement.</description>
    <iconPath>UI/Abilities/Stun</iconPath>

    <level>1</level>                                      <!-- 灵能等级（决定谁能学） -->
    <hotKey>Misc3</hotKey>                                <!-- KeyBindingDef 名 -->
    <hostile>false</hostile>                              <!-- 是否算敌对行为 -->
    <casterMustBeCapableOfViolence>false</casterMustBeCapableOfViolence>

    <!-- 冷却：可直接写区间，也可写单值 -->
    <cooldownTicksRange>180~480</cooldownTicksRange>

    <!-- 灵能系统读取的数值 -->
    <statBases>
      <Ability_EntropyGain>12</Ability_EntropyGain>
      <Ability_PsyfocusCost>0.01</Ability_PsyfocusCost>
      <Ability_Duration>3</Ability_Duration>
      <Ability_EffectRadius>0</Ability_EffectRadius>
    </statBases>

    <!-- 施放形态与可选目标 -->
    <verbProperties>
      <verbClass>Verb_CastAbility</verbClass>             <!-- 能力用 Verb_CastAbility；射击型用 Verb_AbilityShoot -->
      <warmupTime>0.25</warmupTime>
      <range>24.9</range>
      <drawAimPie>false</drawAimPie>
      <targetParams>
        <canTargetSelf>false</canTargetSelf>
        <canTargetAnimals>true</canTargetAnimals>
        <canTargetHumans>true</canTargetHumans>
        <canTargetMechs>false</canTargetMechs>
        <canTargetBuildings>false</canTargetBuildings>
        <neverTargetIncapacitated>true</neverTargetIncapacitated>
      </targetParams>
    </verbProperties>

    <!-- 效果：Class 是 Properties 类，效果逻辑写在 compClass -->
    <comps>
      <li Class="CompProperties_AbilityGiveHediff">
        <compClass>CompAbilityEffect_GiveHediff</compClass>
        <hediffDef>PsychicAnesthesia</hediffDef>          <!-- 这里填 HediffDef 的 defName -->
        <replaceExisting>true</replaceExisting>
        <onlyBrain>true</onlyBrain>
      </li>
      <li Class="CompProperties_AbilityFleckOnTarget">
        <fleckDef>PsycastPsychicEffect</fleckDef>         <!-- 视觉特效 -->
      </li>
    </comps>
  </AbilityDef>

  <!--
    其它可选字段（示范，未启用）：
    AI 相关（原版全部可用字段）：
      <aiCanUse>true</aiCanUse>                        （18.7%）
      <ai_IsOffensive>true</ai_IsOffensive>            （2.8%）
      <ai_IsIncendiary>true</ai_IsIncendiary>          （3.7%）
      <ai_SearchAOEForTargets>true</ai_SearchAOEForTargets>（1.9%）
    （注意：原版没有 ai_CanDoWhileDowned，写了不会被读取）
    灵能/头衔体系接入：<abilityClass>Psycast</abilityClass>、<category>Psychic</category>、
      <groupDef>Leader</groupDef>、<groupAbility>true</groupAbility>、<gizmoClass>Command_Ability</gizmoClass>
    次数与冷却：<charges>3</charges> + <cooldownPerCharge>true</cooldownPerCharge>
    界面与提示：<showWhenDrafted>false</showWhenDrafted>、<displayGizmoWhileUndrafted>true</displayGizmoWhileUndrafted>、
      <disableGizmoWhileUndrafted>false</disableGizmoWhileUndrafted>、<writeCombatLog>true</writeCombatLog>、
      <showPsycastEffects>false</showPsycastEffects>、<uiOrder>1</uiOrder>、<displayOrder>100</displayOrder>
    预热与表演：<jobDef>CastAbilityOnThingMelee</jobDef>、<warmupSound>Psycast_WordOf_Warmup</warmupSound>、
      <warmupMote>Mote_WarmupWordOf</warmupMote>、<warmupMoteSocialSymbol>UI/Abilities/PreachHealth</warmupMoteSocialSymbol>、
      <stunTargetWhileCasting>true</stunTargetWhileCasting>、<targetRequired>true</targetRequired>
    施法后：<sendMessageOnCooldownComplete>true</sendMessageOnCooldownComplete>
  -->

</Defs>
```

## 字段说明
| 字段 | 出现率 | 值类型 | 说明 |
|---|---|---|---|
| `defName` | 92.5% (99/107) | 文本 | 唯一 ID（其余是 Abstract 模板） |
| `label` | 90.6% (97/107) | 文本 | 技能名，样例 `consume leap` / `spike launch` |
| `description` | 89.7% (96/107) | 文本 | 技能说明 |
| `verbProperties` | 88.8% (95/107) | 容器 | 施放参数容器 |
| `comps` | 86.9% (93/107) | 容器 | 效果组件容器；`comps/li` 143.0% (153/107) |
| `iconPath` | 82.2% (88/107) | 文本 | 图标，样例 `UI/Abilities/ShapeFlesh` |
| `verbProperties/targetParams` | 78.5% (84/107) | 容器 | 可选目标规则 |
| `verbProperties/warmupTime` | 78.5% (84/107) | 数值 | 预热秒数，样例 0 / 0.25 / 0.5 |
| `verbProperties/range` | 77.6% (83/107) | 数值 | 射程，样例 17.9 / 3.9 / 5.9 |
| `casterMustBeCapableOfViolence` | 58.9% (63/107) | 布尔 | 施法者是否需要能施暴 |
| `verbProperties/verbClass` | 54.2% (58/107) | 文本 | 样例 Verb_CastAbility / Verb_AbilityShoot |
| `statBases` | 42.1% (45/107) | 容器 | 数值容器 |
| `hotKey` | 40.2% (43/107) | 文本 | 快捷键绑定，样例 Misc1 / Misc3 / Misc12 |
| `cooldownTicksRange` | 39.2% (42/107) | 数值/文本 | 冷却，样例 120 / 130 / 180~480 |
| `comps/li/compClass` | 39.2% (42/107) | 文本 | 效果实现类，样例 CompAbilityEffect_GiveHediff |
| `verbProperties/targetParams/canTargetSelf` | 37.4% (40/107) | 布尔 | 可指向自己 |
| `verbProperties/targetParams/canTargetAnimals` | 31.8% (34/107) | 布尔 | 可指向动物 |
| `verbProperties/targetParams/canTargetBuildings` | 30.8% (33/107) | 布尔 | 可指向建筑 |
| `verbProperties/targetParams/canTargetLocations` | 29.0% (31/107) | 布尔 | 可指向地点 |
| `hostile` | 29.9% (32/107) | 布尔 | 是否敌对行为 |
| `verbProperties/drawAimPie` | 29.9% (32/107) | 布尔 | 是否画瞄准扇形 |
| `verbProperties/soundCast` | 29.0% (31/107) | 容器/文本 | 施放音效 |
| `statBases/Ability_Duration` | 28.0% (30/107) | 数值 | 持续时间，样例 0 / 15 / 40 |
| `level` | 27.1% (29/107) | 数值 | 灵能等级，样例 1 / 2 / 3 |
| `statBases/Ability_PsyfocusCost` | 26.2% (28/107) | 数值 | 灵能专注消耗，样例 0.01 / 0.03 |
| `displayGizmoWhileUndrafted` | 25.2% (27/107) | 布尔 | 未征召时显示按钮 |
| `disableGizmoWhileUndrafted` | 25.2% (27/107) | 布尔 | 未征召时禁用按钮 |
| `comps/li/hediffDef` | 24.3% (26/107) | 文本 | 施加的 hediff，样例 AgonyPulse / Metalblood |
| `verbProperties/requireLineOfSight` | 22.4% (24/107) | 布尔 | 是否要求视线 |
| `showPsycastEffects` | 21.5% (23/107) | 布尔 | 显示灵能特效 |
| `writeCombatLog` | 21.5% (23/107) | 布尔 | 写入战斗日志 |
| `verbProperties/targetParams/canTargetMechs` | 20.6% (22/107) | 布尔 | 可指向机械体 |
| `verbProperties/targetParams/canTargetPawns` | 19.6% (21/107) | 布尔 | 可指向角色 |
| `comps/li/fleckDef` | 19.6% (21/107) | 文本 | 特效，样例 BloodSplash / PsycastPsychicEffect |
| `jobDef` | 19.6% (21/107) | 文本 | 施放用的 JobDef，样例 CastAbilityOnThingMelee |
| `statBases/Ability_EntropyGain` | 19.6% (21/107) | 数值 | 灵能熵增，样例 0 / 12 / 20 |
| `aiCanUse` | 18.7% (20/107) | 布尔 | 是否允许 AI 使用 |
| `statBases/Ability_EffectRadius` | 17.8% (19/107) | 数值 | 效果半径，样例 0 / 2.9 / 5 |
| `stunTargetWhileCasting` | 16.8% (18/107) | 布尔 | 施法时定身目标 |
| `targetRequired` | 16.8% (18/107) | 布尔 | 是否必须有目标 |
| `warmupStartSound` | 15.9% (17/107) | 文本 | 预热音效 |
| `comps/li/psychic` | 15.9% (17/107) | 布尔 | 是否灵能效果 |
| `sendMessageOnCooldownComplete` | 14.0% (15/107) | 布尔 | 冷却结束发消息 |
| `comps/li/goodwillImpact` | 14.0% (15/107) | 数值 | 好感影响，样例 -15 / -25 |
| `displayOrder` | 13.1% (14/107) | 数值 | 排序 |
| `warmupMoteSocialSymbol` | 13.1% (14/107) | 文本 | 预热气泡图标 |
| `verbProperties/targetParams/canTargetSubhumans` | 13.1% (14/107) | 布尔 | 可指向亚人 |
| `comps/li/sound` | 12.2% (13/107) | 文本 | 组件音效 |
| `warmupSound` | 12.2% (13/107) | 文本 | 预热音效 |
| `comps/li/replaceExisting` | 11.2% (12/107) | 布尔 | 覆盖已有效果 |
| `groupDef` | 11.2% (12/107) | 文本 | 能力分组，样例 Leader / Moralist |
| `showWhenDrafted` | 11.2% (12/107) | 布尔 | 征召时是否显示 |
| `verbProperties/targetParams/canTargetHumans` | 11.2% (12/107) | 布尔 | 可指向人类 |
| `comps/li/onlyBrain` | 11.2% (12/107) | 布尔 | 只作用于脑部 |
| `canUseAoeToGetTargets` | 10.3% (11/107) | 布尔 | 允许范围选取目标 |
| `comps/li/projectileDef` | 10.3% (11/107) | 文本 | 发射物，样例 PiercingSpine / Proj_Acid |
| `category` | 9.3% (10/107) | 文本 | 分类，样例 Psychic / Sanguophage / Skip |
| `comps/li/durationMultiplier` | 9.3% (10/107) | 文本 | 持续时间受哪个能力值放大 |
| `comps/li/onlyApplyToSelf` | 9.3% (10/107) | 布尔 | 只作用于自己 |
| `uiOrder` | 8.4% (9/107) | 数值 | 界面排序 |
| `comps/li/stateDef` | 6.5% (7/107) | 文本 | 施加的精神状态 |
| `comps/li/interactionDef` | 6.5% (7/107) | 文本 | 社交交互 |
| `verbProperties/targetParams/neverTargetHostileFaction` | 6.5% (7/107) | 布尔 | 不指向敌对派系 |
| `verbProperties/defaultProjectile` | 5.6% (6/107) | 文本 | 默认发射物 |
| `verbProperties/targetParams/neverTargetIncapacitated` | 4.7% (5/107) | 布尔 | 不指向失能者 |
| `verbProperties/targetParams/canTargetEntities` | 4.7% (5/107) | 布尔 | 可指向异象实体 |
| `verbProperties/label` | 4.7% (5/107) | 文本 | 施放动作名 |
| `comps/li/fleckDefs/li` | 7.5% (8/107) | 文本 | 多个特效率 |
| `comps/li/stunTicks` | 3.7% (4/107) | 文本 | 定身时长，样例 18~60 |
| `comps/li/maintainForTicks` | 3.7% (4/107) | 数值 | 维持时长 |
| `comps/li/preCastTicks` | 3.7% (4/107) | 数值 | 施放前延迟 |
| `charges` | 3.7% (4/107) | 数值 | 使用次数 |
| `ai_IsIncendiary` | 3.7% (4/107) | 布尔 | 带燃烧属性 |
| `ai_IsOffensive` | 2.8% (3/107) | 布尔 | 归为进攻性 |
| `ai_SearchAOEForTargets` | 1.9% (2/107) | 布尔 | 范围搜索目标 |
| `cooldownPerCharge` | 1.9% (2/107) | 布尔 | 每次数独立冷却 |
| `abilityClass` | 0.9% (1/107) | 文本 | 样例 Psycast |
| `gizmoClass` | 2.8% (3/107) | 文本 | 按钮类，样例 Command_Ability |
| `groupAbility` | 2.8% (3/107) | 布尔 | 是否为组能力 |
| `verbProperties/minRange` | 1.9% (2/107) | 数值 | 最小射程 |
| `verbProperties/nonInterruptingSelfCast` | 2.8% (3/107) | 布尔 | 自施放不打断 |

## 常见坑
1. **不要写 `ai_CanDoWhileDowned`**：本机 1.7.4981 rev136 的原版 AbilityDef 没有这个路径（`docs/def-schema.json` 全文检索 0 命中，254 份字段参考中也无）。原版能用的 AI 字段只有 `aiCanUse`（18.7%）、`ai_IsIncendiary`（3.7%）、`ai_IsOffensive`（2.8%）、`ai_SearchAOEForTargets`（1.9%）。【待验证：任务书里该字段名的来源未能证实】
2. `comps/li` 的 `Class` 属性是 **Properties 类**，真正的效果逻辑写在 `compClass` 里，两个都要写且要配对：原版 `Royalty/Defs/AbilityDefs/Abilities.xml:32-33` 是 `Class="CompProperties_AbilityGiveHediff"` + `<compClass>CompAbilityEffect_GiveHediff</compClass>`。
3. 光有 AbilityDef 不等于小人有这个技能：必须有授予途径——基因 `abilities`、`RoyalTitleDef` 的 `grantedAbilities`、hediff 的 `comps/li/abilityDefs`，或接入灵能体系（`category` / `groupDef` / `abilityClass`）。原版 `PsycastBaseSkip`（`Abilities.xml:5-7`）就是靠 `ParentName`+`category` 接入的。
4. `hotKey` 要填已存在的 KeyBindingDef 名（原版样例 `Misc1` / `Misc3` / `Misc12`），自造字符串不生效。【推测】
5. `verbProperties` 出现率 88.8%、其中 `targetParams` 78.5%、`warmupTime` 78.5%、`range` 77.6%——要做"选目标施放"的能力，这三项基本是必需的；只写 `comps` 会出现技能没有施放动作的情况。
6. `cooldownTicksRange` 支持"单值"与"区间"两种写法（原版样例 `120` 与 `180~480` 都存在）；用 `charges` 做有限次数技能时，注意配 `cooldownPerCharge`（1.9%）。

## 核验
- 模板逐行对照原版 `Royalty/Defs/AbilityDefs/Abilities.xml`：`Stun`(:45-77) 给出 level / iconPath `UI/Abilities/Stun` / writeCombatLog / hotKey `Misc3` / casterMustBeCapableOfViolence / statBases(`Ability_EntropyGain` `Ability_PsyfocusCost` `Ability_Duration`) / verbProperties(warmupTime、range、targetParams/canTargetAnimals) / comps(`CompProperties_AbilityEffectWithDuration`+`compClass`+`durationMultiplier`+`psychic`+`goodwillImpact`、`CompProperties_AbilityFleckOnTarget`+`fleckDef`)；`Painblock`(:9-43) 给出 `CompProperties_AbilityGiveHediff` + `compClass CompAbilityEffect_GiveHediff` + `hediffDef PsychicAnesthesia` 的配对写法；`WordOfBase`(:869-879) 给出 jobDef / warmupMote / warmupSound / category / stunTargetWhileCasting / showPsycastEffects / displayGizmoWhileUndrafted / disableGizmoWhileUndrafted；`WordOfTrust`(:895-922) 给出 verbProperties 的 `onlyTargetPrisonersOfColony`、`neverTargetIncapacitated` 与 statBases/`Ability_PsyfocusCost`。
- 最小可加载范例见同文件 `PsycastBaseSkip`(:5-7)：`<AbilityDef Name="PsycastBaseSkip" ParentName="PsycastBase" Abstract="True"><category>Skip</category></AbilityDef>`。
- `ai_CanDoWhileDowned` 的不存在性：对 `docs/def-schema.json` 全文检索该字符串命中 0 次；同时该字符串在 `library/03-全量字段参考/字段/` 全部 254 份字段参考中也无命中。
- 出现率与样例值来自 `library/03-全量字段参考/字段/AbilityDef.md`（107 个原版实例实测）。
- 待验证项：灵能基类 `PsycastBase` 本身**不在** `Royalty/Defs/AbilityDefs/Abilities.xml` 中定义（该文件中 `Name="PsycastBase"` 只出现在 ParentName 引用处），其定义位置未确认；如需做灵能能力，请先在 `Royalty/Defs` 下搜索 `PsycastBase` 的定义文件，或改用 `category`+`level`+`statBases` 自建。
