# TraitDef

## 用途
TraitDef 定义**特质**：「工作狂」「嗜血」「慢性子」这类固化在角色身上的性格与倾向。核心结构是 `degreeDatas`——一个特质可以带多个等级（degree），每个等级有自己的名字、描述和数值修正，原版 `SpeedOffset`（慢性子→小跑者）就是三级写法。
它与 GeneDef（`forcedTraits`）、BackstoryDef（`forcedTraits` / `disallowedTraits`）、PawnKindDef（`disallowedTraits`）联动决定谁能拿到它；又通过 ThoughtDef（`nullifyingTraits` / `requiredTraits`）、精神崩溃、灵感系统间接影响心情与人际。原版共 51 个实例、122 条字段路径。

## 模板
```xml
<?xml version="1.0" encoding="utf-8" ?>
<Defs>

  <!-- 多等级特质：每个 <li> 是一个 degree，用 <degree> 标明等级数值 -->
  <TraitDef>
    <defName>EXAMPLE_SpeedOffset</defName>

    <!-- 随机出现权重：0 = 不会随机生成，只能由剧本/基因/背景给（原版 PerfectMemory 就是 0） -->
    <commonality>2</commonality>

    <degreeDatas>
      <li>
        <label>example slowpoke</label>
        <description>[PAWN_nameDef] is always falling behind the group whenever [PAWN_pronoun] goes anywhere.</description>
        <degree>-1</degree>
        <statOffsets>
          <MoveSpeed>-0.2</MoveSpeed>          <!-- 加法修正：-0.2 移动速度 -->
        </statOffsets>
        <disallowedInspirations>
          <li>Frenzy_Go</li>                   <!-- 该等级下禁止触发的灵感 -->
        </disallowedInspirations>
      </li>
      <li>
        <label>example fast walker</label>
        <description>[PAWN_nameDef] likes to be where [PAWN_pronoun] is going.</description>
        <degree>1</degree>
        <statOffsets>
          <MoveSpeed>0.2</MoveSpeed>
        </statOffsets>
      </li>
      <li>
        <label>example jogger</label>
        <description>[PAWN_nameDef] always moves with a sense of urgency.</description>
        <degree>2</degree>
        <statOffsets>
          <MoveSpeed>0.4</MoveSpeed>
        </statOffsets>
      </li>
    </degreeDatas>

    <!-- 互斥标签：同标签的特质不会同时出现在一个人身上（原版用 SexualOrientation / Toughness 等） -->
    <exclusionTags>
      <li>EXAMPLE_Speed</li>
    </exclusionTags>
  </TraitDef>

  <!-- 单等级特质：省略 degree 与多个 <li>，只有一条 -->
  <TraitDef>
    <defName>EXAMPLE_DeepFocus</defName>
    <commonality>1</commonality>
    <degreeDatas>
      <li>
        <label>example deep focus</label>
        <description>[PAWN_nameDef] shuts the world out when working.</description>
        <!-- 加法修正：标签必须是 StatDef 的 defName，值可正可负 -->
        <statOffsets>
          <GlobalLearningFactor>0.15</GlobalLearningFactor>
        </statOffsets>
        <!-- 乘法修正：原版 TraitDef 只用到下面这三个统计项 -->
        <statFactors>
          <CertaintyLossFactor>1.15</CertaintyLossFactor>
        </statFactors>
        <statOffsets>
          <MentalBreakThreshold>-0.04</MentalBreakThreshold>
        </statOffsets>
      </li>
    </degreeDatas>

    <!-- 与哪些特质互斥（双向声明更稳） -->
    <conflictingTraits>
      <li>Nerves</li>
    </conflictingTraits>
  </TraitDef>

  <!--
    其它可选字段（示范，未启用）：
    <requiredWorkTags><li>Violent</li></requiredWorkTags>        拥有者必须具备的工作标签（原版 Bloodlust 用 Violent）
    <disabledWorkTags><li>Firefighting</li></disabledWorkTags>   拥有者被禁用的工作
    <forcedPassions><li>Artistic</li></forcedPassions>           强制激情
    <conflictingPassions><li>Shooting</li></conflictingPassions>
    <commonalityFemale>0.3</commonalityFemale>                   女性专属权重
    <allowOnHostileSpawn>false</allowOnHostileSpawn>
    degreeDatas/li 内还可用：allowedMeditationFocusTypes / disablesNeeds / enablesNeeds /
      skillGains（如 <Shooting>-10</Shooting>）/ socialFightChanceFactor / hungerRateFactor /
      marketValueFactorOffset / randomMentalState / theOnlyAllowedMentalBreaks /
      disallowedMentalStates / disallowedThoughts / possessions（键=ThingDef名，值=数量）
  -->

</Defs>
```

## 字段说明
| 字段 | 出现率 | 值类型 | 说明 |
|---|---|---|---|
| `defName` | 100.0% (51/51) | 文本 | 唯一 ID |
| `degreeDatas` | 100.0% (51/51) | 容器 | 等级列表容器，必填 |
| `degreeDatas/li/label` | 143.1% (73/51) | 文本 | 该等级的显示名（多等级会 >100%） |
| `degreeDatas/li/description` | 143.1% (73/51) | 文本 | 该等级描述，含 `{PAWN_nameDef}` / `{PAWN_pronoun}` 占位符 |
| `commonality` | 76.5% (39/51) | 数值 | 随机出现权重，0 表示不随机生成 |
| `degreeDatas/li/degree` | 62.7% (32/51) | 数值 | 等级数值，样例 -1 / -2 / 1 / 2 |
| `degreeDatas/li/statOffsets` | 62.7% (32/51) | 容器 | 加法修正容器 |
| `conflictingTraits/li` | 41.2% (21/51) | 文本 | 互斥特质；本体 `conflictingTraits` 25.5% (13/51) |
| `degreeDatas/li/possessions` | 33.3% (17/51) | 容器 | 该等级携带物，键=ThingDef 名，值=数量文本或空 |
| `degreeDatas/li/statFactors` | 27.5% (14/51) | 容器 | 乘法修正容器 |
| `degreeDatas/li/allowedMeditationFocusTypes/li` | 21.6% (11/51) | 文本 | 允许的冥想类型，样例 Flame / Morbid |
| `degreeDatas/li/marketValueFactorOffset` | 13.7% (7/51) | 数值 | 市场价值修正 |
| `exclusionTags/li` | 13.7% (7/51) | 文本 | 互斥标签，样例 SexualOrientation / Toughness |
| `requiredWorkTags/li` | 9.8% (5/51) | 文本 | 要求的工作标签，样例 Violent |
| `degreeDatas/li/skillGains` | 5.9% (3/51) | 容器 | 技能加成，键=技能 defName |
| `degreeDatas/li/randomMentalState` | 5.9% (3/51) | 文本 | 随机精神崩溃类型 |
| `degreeDatas/li/theOnlyAllowedMentalBreaks/li` | 5.9% (3/51) | 文本 | 只允许这些崩溃 |
| `commonalityFemale` | 3.9% (2/51) | 数值 | 女性权重 |
| `degreeDatas/li/disablesNeeds/li` | 7.8% (4/51) | 文本 | 禁用需求，样例 Comfort / Food / Outdoors |
| `degreeDatas/li/disallowedInspirations/li` | 3.9% (2/51) | 文本 | 禁止的灵感，样例 Frenzy_Go |
| `degreeDatas/li/disallowedMeditationFocusTypes/li` | 3.9% (2/51) | 文本 | 禁止的冥想类型 |
| `degreeDatas/li/socialFightChanceFactor` | 2.0% (1/51) | 数值 | 打架概率倍数（原版 Bloodlust 为 4） |
| `degreeDatas/li/hungerRateFactor` | 2.0% (1/51) | 数值 | 饥饿速率倍数 |
| `degreeDatas/li/randomDiseaseMtbDays` | 2.0% (1/51) | 数值 | 随机疾病平均间隔天数 |
| `degreeDatas/li/enablesNeeds/li` | 2.0% (1/51) | 文本 | 启用需求，样例 Indoors |
| `allowOnHostileSpawn` | 2.0% (1/51) | 布尔 | 是否允许出现在敌对生成中 |
| `disabledWorkTags` | 2.0% (1/51) | 文本 | 禁用的工作标签 |
| `forcedPassions/li` / `conflictingPassions/li` | 各 2.0% (1/51) | 文本 | 强制/互斥激情 |
| `degreeDatas/li/statOffsets/MoveSpeed` | 5.9% (3/51) | 数值 | 样例 -0.2 / 0.2 / 0.4 |
| `degreeDatas/li/statOffsets/MentalBreakThreshold` | 13.7% (7/51) | 数值 | 样例 -0.09 / 0.08 / 0.12 |
| `degreeDatas/li/statOffsets/WorkSpeedGlobal` | 11.8% (6/51) | 数值 | 样例 -0.20 / 0.20 |
| `degreeDatas/li/statOffsets/PawnBeauty` | 7.8% (4/51) | 数值 | 样例 -2 / -1 / 1 |
| `degreeDatas/li/statOffsets/PsychicSensitivity` | 7.8% (4/51) | 数值 | 样例 -1 / 0.4 |
| `degreeDatas/li/statFactors/CertaintyLossFactor` | 21.6% (11/51) | 数值 | 样例 0.25 / 2 |

## 常见坑
- **`statOffsets`/`statFactors` 下的标签必须是 StatDef 的 defName**：写错的标签不会报错但也不生效；原版 TraitDef 的 `statFactors` 只用到 `CertaintyLossFactor` / `IncomingDamageFactor` / `PawnTrapSpringChance`，`GlobalLearningFactor` 原版只出现在 `statOffsets` 里。
1. `statOffsets` / `statFactors` / `label` / `description` 都在 **`degreeDatas/li` 内部**，TraitDef 根上没有这些字段（原版 100% 的 label/description 都在 li 里）。
2. `commonality` 是权重不是百分比，且允许 0：`PerfectMemory` 用 0 表示只能被脚本/事件授予（原版 `Anomaly/Defs/TraitDefs/Traits.xml`）。想让特质稀有就把值调小，而不是删掉该字段。
3. 多等级特质靠每个 `<li>` 里的 `<degree>` 数值区分（原版 62.7% 写了 degree）；单等级简写可以完全不写 degree，但**同名特质不要在同一 def 里写重复 degree**。【推测：重复 degree 的后果未核实】
4. `exclusionTags` 里的字符串是自定义标签，不要求全局唯一，但要让两个特质互斥，必须写**同一个标签**（原版样例 SexualOrientation / Toughness）。
5. `conflictingTraits` 只是阻止同时生成；它不会在运行时把已经存在的特质移除。【推测】
6. `description` 用 `{PAWN_nameDef}`（花括号）而 BackstoryDef 用 `[PAWN_nameDef]`（方括号），两套占位符不要混用——写错会原样显示在 UI 上。

## 核验
- 单等级写法的逐行对照：原版 `Core/Defs/TraitDefs/Traits_Singular.xml` 的 `Nudist`(:4-13，commonality 0.7 + degreeDatas/li label+description)、`Kind`(:35-51，含 `conflictingTraits` 与 li 内 `statFactors`)、`Bloodlust`(:15-33，含 `socialFightChanceFactor`、`allowedMeditationFocusTypes`、`possessions`、TraitDef 级 `requiredWorkTags`)、`Psychopath`(:53-69，无 commonality)。
- **多等级（degree）写法**的对照在另一个文件：`Core/Defs/TraitDefs/Traits_Spectrum.xml`——`SpeedOffset`(:4-36) 给出三级 degree（-1 / 1 / 2）+ 每级 `statOffsets/MoveSpeed` + `disallowedInspirations/Frenzy_Go`；`DrugDesire`(:38-60 起) 给出 degree 2/1/-1 + `marketValueFactorOffset` + `disallowedMentalStates`。注意：`Traits_Singular.xml` 中 grep `<degree>` 无命中，度数特质只在 `Traits_Spectrum.xml`。
- 最小可加载范例见 `Anomaly/Defs/TraitDefs/Traits.xml` 的 `PerfectMemory`。
- 出现率与样例值来自 `library/03-全量字段参考/字段/TraitDef.md`（51 个原版实例实测）。
