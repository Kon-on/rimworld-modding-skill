# MemeDef

## 用途

MemeDef 是意识形态的「思想内核」：一条 meme 决定了这个理念信仰什么、禁忌什么、能解锁哪些仪式与研究者装风格，并在 Ideoligion 创建对话框里作为可勾选项出现。它本身不直接给小人加减心情，而是通过 `requireOne` / `requiredRituals` / `selectOneOrNone` 去**要求或概率性解锁对应的 PreceptDef（戒律）**，再由戒律去挂 ThoughtDef、EventDef 等产生实际效果。因此一个 MemeDef 往往是「一组戒律的入口」，写它之前要先想好它要拉进哪些 issue（如 Ritual、Precepts_Nudity）下的戒律。

## 模板

下面整份文件可直接另存为 `EXAMPLE_Memes.xml` 丢进 `Defs/` 加载（`Blindness_*`、`Darklight_Preferred`、`BlindingCeremony`、`Apparel_Burka`、`SacrificialFlag`、`Cultist`、`Morbid`、`ArchistDescription` 都是在原版里真实存在的 defName，写成这样保证不报红）。

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Defs>

  <!-- ============ ① 普通 Meme：最典型的写法 ============ -->
  <MemeDef>
    <defName>EXAMPLE_Stargazers</defName>
    <label>stargazers</label>
    <description>Our ancestors came from the stars. To look up is to pray.</description>
    <!-- 图标路径不含扩展名；必须指向 UI/ 下的贴图，原版全部是 UI/Memes/<名字> -->
    <iconPath>UI/Memes/Darkness</iconPath>
    <!-- groupDef 必写，且只能取 MemeGroupDef 的 defName：GenderSupremacy / GroupRelation / Individualism / Misc / Primacy / Theist_Embodied / Theist_Abstract（原版一共只有这 7 个） -->
    <groupDef>Misc</groupDef>
    <!-- 影响力档位。注意是数字 0~3，不是 PreceptDef 用的 Low/Medium/High -->
    <impact>1</impact>
    <!-- 在 Meme 列表里的排序权重，原版取值 80 / 999 / 1100 / 1101 -->
    <renderOrder>500</renderOrder>

    <!-- 互斥：带同一个标签的 meme 不会同时出现在一个理念里 -->
    <exclusionTags>
      <li>EXAMPLE_Stargazers</li>
    </exclusionTags>

    <!-- 解锁门槛：内层 li 是「戒律 defName」，外层每个 li 是一组候选，至少命中一条这组候选里有一个可选，这个 meme 才会被提供 -->
    <requireOne>
      <li>
        <li>Darklight_Preferred</li>
        <li>DarknessCombat_Preferred</li>
        <li>Eclipse_Beautiful</li>
      </li>
    </requireOne>

    <!-- generalRules 影响理念里的称谓，必写；键名照抄原版，值里不要留空格 -->
    <generalRules>
      <rulesStrings>
        <li>memeAdjective->stargazing</li>
        <li>memeHyphenPrefix->star</li>
        <li>memeConcept->the void</li>
        <li>memeLeaderNoun->astronomer</li>
        <li>memeLeaderAdjective->astronomical</li>
        <li>memeMoralist->astronomer</li>
      </rulesStrings>
    </generalRules>

    <!-- 理念故事的生成规则。每行形如 类别(tag=meme_<defName>) ->文本；tag 必须等于 meme_ + 本 defName -->
    <descriptionMaker>
      <rules>
        <rulesStrings>
          <li>creation(tag=meme_EXAMPLE_Stargazers) ->[deity0_name] scattered the first stars across the dark.</li>
          <li>intro(tag=meme_EXAMPLE_Stargazers) ->We read the sky the way others read scripture.</li>
          <li>episode(tag=meme_EXAMPLE_Stargazers) ->[member0_name] spent a long night charting the heavens.</li>
          <li>lesson(tag=meme_EXAMPLE_Stargazers) ->The stars do not care, and that is why they are holy.</li>
          <li>lessonReinforcement(tag=meme_EXAMPLE_Stargazers) ->Look up. Remember where we came from.</li>
        </rulesStrings>
      </rules>
    </descriptionMaker>

    <!-- 由这些词自动拼出理念名称/形容词/成员称呼 -->
    <symbolPacks>
      <li>
        <ideoName>Astronomism</ideoName>
        <theme>astronomism</theme>
        <adjective>astronomic</adjective>
        <member>astronomer</member>
      </li>
    </symbolPacks>
  </MemeDef>

  <!-- ============ ② 会强制带仪式的 Meme：requiredRituals + 概率配对 + 建筑/风格联动 ============ -->
  <MemeDef>
    <defName>EXAMPLE_StarRite</defName>
    <label>star rites</label>
    <description>Certain rites must be held, and certain apparel chosen, or the sky is offended.</description>
    <iconPath>UI/Memes/Blindsight</iconPath>
    <groupDef>Individualism</groupDef>
    <impact>2</impact>
    <renderOrder>1100</renderOrder>

    <!-- 硬性要求：precept 是仪式类戒律的 defName，pattern 是对应的 RitualPatternDef defName。可选再补 <building> -->
    <requiredRituals>
      <li>
        <precept>BlindingCeremony</precept>
        <pattern>BlindingCeremony</pattern>
      </li>
    </requiredRituals>

    <!-- 概率配对：noneChance 是「什么都不加」的概率，其余按 preceptThingPairs 随机挑一对（戒律+配套物品） -->
    <selectOneOrNone>
      <noneChance>0.2</noneChance>
      <preceptThingPairs>
        <li>
          <precept>ApparelDesired_Soft_Subordinate</precept>
          <thing>Apparel_Burka</thing>
        </li>
      </preceptThingPairs>
    </selectOneOrNone>

    <!-- 该理念的仪式会消耗的建筑 -->
    <consumableBuildings>
      <li>SacrificialFlag</li>
    </consumableBuildings>

    <!-- 影响世界生成时该理念派系的物品外观风格；li 上可用 MayRequire 标注资料片依赖 -->
    <styleItemTags>
      <li>
        <tag>Cultist</tag>
        <baseWeight>5</baseWeight>
        <weightFactor>1</weightFactor>
      </li>
    </styleItemTags>
    <thingStyleCategories>
      <li MayRequire="Ludeon.RimWorld.Ideology">
        <category>Morbid</category>
        <priority>3</priority>
      </li>
    </thingStyleCategories>

    <!-- 与该 meme 相性相合 / 相斥的特质 -->
    <agreeableTraits>
      <li>DislikesWomen</li>
    </agreeableTraits>

    <generalRules>
      <rulesStrings>
        <li>memeAdjective->star-ritual</li>
        <li>memeConcept->the rite</li>
      </rulesStrings>
    </generalRules>

    <descriptionMaker>
      <rules>
        <rulesStrings>
          <li>creation(tag=meme_EXAMPLE_StarRite) ->The sky demanded a rite, and we gave it.</li>
          <li>lesson(tag=meme_EXAMPLE_StarRite) ->A promise to the sky is a promise to everyone.</li>
        </rulesStrings>
      </rules>
    </descriptionMaker>

    <symbolPacks>
      <li>
        <theme>astrolatry</theme>
        <adjective>astrolatric</adjective>
        <member>astrolater</member>
      </li>
    </symbolPacks>
  </MemeDef>

  <!-- ============ ③ 结构型 Meme：category=Structure，影响整个理念的故事模板与神祇数量 ============ -->
  <MemeDef>
    <defName>EXAMPLE_Structure_Skywatchers</defName>
    <label>skywatchers</label>
    <description>A civilization-spanning faith of observatories and calendars.</description>
    <category>Structure</category>
    <iconPath>UI/Structures/Archist</iconPath>
    <impact>0</impact>
    <!-- 结构型 meme 在随机世界生成时的权重倍率 -->
    <randomizationSelectionWeightFactor>3</randomizationSelectionWeightFactor>
    <!-- 神祇数量：可以是数字，也可以是区间文本 -->
    <deityCount>0</deityCount>
    <!-- 礼拜房间的称呼，直接影响 UI 用词 -->
    <worshipRoomLabel>observatory</worshipRoomLabel>

    <generalRules>
      <rulesStrings>
        <li>memeAdjective->skywatch</li>
        <li>memeConcept->the watch</li>
      </rulesStrings>
    </generalRules>

    <!-- patterns/li/def 指向 IdeoStoryPatternDef 的 defName（原版定义在 Ideology/Defs/RulePackDefs/RulePacks_Ideo_Description.xml）。
         本例借用原版 ArchistDescription 只为保证文件可直接加载；正式 mod 请自写一个 IdeoStoryPatternDef 再填这里。
         constants 用来给那个故事模板传常量，key/value 成对。 -->
    <descriptionMaker>
      <patterns>
        <li>
          <def>ArchistDescription</def>
        </li>
      </patterns>
      <constants>
        <li>
          <key>structure_archist</key>
          <value>true</value>
        </li>
      </constants>
    </descriptionMaker>

    <symbolPacks>
      <li>
        <ideoName>Skywatch</ideoName>
        <theme>skywatch</theme>
        <adjective>skywatch</adjective>
        <member>skywatcher</member>
      </li>
    </symbolPacks>
  </MemeDef>

</Defs>
```

## 字段说明

| 字段 | 出现率 | 值类型 | 说明 |
| --- | --- | --- | --- |
| `defName` | 94.7% (36/38) | 文本 | 必填。全局唯一 ID；`descriptionMaker` 里的 `tag=meme_<defName>` 就用它。 |
| `label` | 94.7% (36/38) | 文本 | 界面显示名（小写，如 bloodfeeding）。 |
| `description` | 94.7% (36/38) | 文本 | Meme 卡片上的说明文字，纯文本。 |
| `iconPath` | 94.7% (36/38) | 文本 | 图标贴图路径（不含扩展名），原版全部为 `UI/Memes/<名字>`。 |
| `groupDef` | 81.6% (31/38) | 文本 | **必写**。所属分组，值必须是 `MemeGroupDef` 的 defName：原版仅 `GenderSupremacy`、`GroupRelation`、`Individualism`、`Misc`、`Primacy`、`Theist_Embodied`、`Theist_Abstract` 七个。 |
| `impact` | 86.8% (33/38) | 数值 | 影响力档位，**数字** `0`–`3`（和 PreceptDef 的 Low/Medium/High 文本不同）。 |
| `renderOrder` | 52.6% (20/38) | 数值 | 在 Meme 列表/生成顺序里的排序值。 |
| `exclusionTags/li` | 47.4% (18/38) | 文本 | 互斥标签：带同一标签的 Meme 不会同时出现。 |
| `requireOne/li/li` | 281.6% (107/38) | 文本 | 可用性门槛：外层每个 `<li>` 是一组候选，内层的值是 **PreceptDef 的 defName**，表示“至少要有一条这些戒律存在”这个 Meme 才会被提供。 |
| `generalRules/rulesStrings/li` | 1313.2% (499/38) | 文本 | **必写**。文本替换规则，形如 `<li>memeAdjective->dark</li>`；原版用到的键有 `memeAdjective`、`memeHyphenPrefix`、`memeConcept`、`memeCreed`、`memeLeaderNoun`、`memeLeaderAdjective`、`memeMoralist`。 |
| `descriptionMaker/rules/rulesStrings/li` | 1144.7% (435/38) | 文本 | 理念故事生成规则，形如 `<li>creation(tag=meme_Darkness) ->...</li>`；`tag=` 必须等于 `meme_<你的defName>`。 |
| `descriptionMaker/patterns/li/def` | 39.5% (15/38) | 文本 | 指向 **IdeoStoryPatternDef** 的 defName（结构型 Meme 用它引用一整段故事模板，原版定义在 `Ideology/Defs/RulePackDefs/RulePacks_Ideo_Description.xml`）。 |
| `descriptionMaker/constants/li/key` | 39.5% (15/38) | 文本 | 向故事模板注入常量：`key` + `value` 成对出现（如 `structure_archist` = `true`）。 |
| `symbolPacks/li` | 347.4% (132/38) |  | 理念名称/形容词族，用于“Archism / archist”这类自动起名。 |
| `symbolPacks/li/theme` | 210.5% (80/38) | 文本 | 符号主题词（用作名称词根）。 |
| `symbolPacks/li/adjective` | 347.4% (132/38) | 文本 | 理念形容词（archist）。 |
| `symbolPacks/li/member` | 347.4% (132/38) | 文本 | 成员称呼（archist）。 |
| `symbolPacks/li/ideoName` | 321.1% (122/38) | 文本 | 可选的成品理念名（如 Archism）；不给时由 theme/adjective 组合生成。 |
| `category` | 15.8% (6/38) | 文本 | 只有结构型 Meme 会写，值仅见 `Structure`。 |
| `deityCount` | 23.7% (9/38) | 数值/文本 | 神祇数量，可为数字或区间文本，如 `0` / `1` / `1~4`。 |
| `randomizationSelectionWeightFactor` | 7.9% (3/38) | 数值 | 随机世界生成时被抽中的权重倍率（结构型常用 3）。 |
| `worshipRoomLabel` | 23.7% (9/38) | 文本 | 礼拜房间的称呼（shrine / sanctuary / pantheon），影响 UI 用词。 |
| `requiredRituals/li/precept` | 10.5% (4/38) | 文本 | 必须存在的仪式戒律 defName（与 `pattern`、可选 `building` 成组）。 |
| `requiredRituals/li/pattern` | 10.5% (4/38) | 文本 | 对应的 RitualPatternDef defName。 |
| `selectOneOrNone/noneChance` | 13.2% (5/38) | 数值 | 按权重随机时的“什么都不加”概率。 |
| `selectOneOrNone/preceptThingPairs/li/precept` | 18.4% (7/38) | 文本 | 随机二选一：候选戒律 defName。 |
| `selectOneOrNone/preceptThingPairs/li/thing` | 18.4% (7/38) | 文本 | 随机二选一：与上一条戒律配对的 ThingDef defName。 |
| `consumableBuildings/li` | 44.7% (17/38) | 文本 | 该 Meme 仪式会消耗的建筑 defName。 |
| `styleItemTags/li/tag` | 63.2% (24/38) | 文本 | 风格物品标签（影响生成物品外观）。 |
| `styleItemTags/li/baseWeight` | 39.5% (15/38) | 数值 | 基线权重。 |
| `styleItemTags/li/weightFactor` | 63.2% (24/38) | 数值 | 该风格的权重倍率。 |
| `thingStyleCategories/li/category` | 28.9% (11/38) | 文本 | 物品风格类别，如 `Morbid`。 |
| `thingStyleCategories/li/priority` | 28.9% (11/38) | 数值 | 该风格的优先级。 |
| `fixedDeityNameTypes/li/name` | 84.2% (32/38) | 文本 | 固定神名（与 `type` 成组，用于现实宗教型理念）。 |
| `fixedDeityNameTypes/li/type` | 84.2% (32/38) | 文本 | 该神的头衔/类型，如 God of Creation。 |
| `agreeableTraits/li` | 28.9% (11/38) | 文本 | 与该 Meme 相配的特质 defName。 |
| `disagreeableTraits/li` | 13.2% (5/38) | 文本 | 与该 Meme 相斥的特质 defName。 |
| `startingResearchProjects/li` | 7.9% (3/38) | 文本 | 给该理念的起始研究项目 defName。 |
| `replaceRitualsWithTags/li` | 7.9% (3/38) | 文本 | 用标签替换仪式需求（配合 RitualPatternDef 的 `tags` 使用）。 |
| `addDesignators/li` | 18.4% (7/38) | 文本 | 额外解锁的设计ator（建造/命令）defName。 |
| `consumableBuildings` | 44.7% (17/38) |  | 容器，见上面的 `consumableBuildings/li`。 |

## 常见坑

1. **`<groupDef>` 写错或漏写**：它必须取 MemeGroupDef 的 defName，原版一共只有 `GenderSupremacy`、`GroupRelation`、`Individualism`、`Misc`、`Primacy`、`Theist_Embodied`、`Theist_Abstract` 七个。写一个不存在的分组，meme 不会出现在创建理念界面（推测：分组无法解析导致该 meme 在 UI 里被跳过）。
2. **`<impact>` 写成 `Low`/`Medium`/`High`**：MemeDef 的 impact 是数字 `0`~`3`（原版样例只有 0/1/2/3），PreceptDef 才是文本档位；两种 Def 的取值不能互抄。
3. **`descriptionMaker/rules/rulesStrings` 的 tag 与 defName 不一致**：行首必须是 `类别(tag=meme_<defName>) ->`，写成别的名字这段文字永远不会被用到，且不会报错——故事文本会静默缺失（推测：规则匹配不到就退回默认文案）。
4. **`requireOne` 里填 meme 名而不是戒律名**：原版的 `requireOne/li/li` 里全是 PreceptDef（如 `Lovin_Free`、`Nudity_Male_NoRules`、`Darklight_Preferred`），填成 meme 则条件永远不成立，该 meme 变相被禁用。
5. **把 `requiredPreceptsOnly` 写进 MemeDef**：**该字段在 MemeDef 的全量字段表（102 条路径）里不存在**，全库检索显示它只属于 FactionDef（`Anomaly/Defs/FactionDefs/Factions_Misc.xml` 里 `<requiredPreceptsOnly>true</requiredPreceptsOnly>`，与 `<forcedMemes>`、`<disallowedPrecepts>` 连用，出现率仅 0.0256%）。想在 meme 侧做「只允许这些戒律」，MemeDef 里可用的近似手段是 `selectOneOrNone`（noneChance + preceptThingPairs）与 `requireOne`。
6. **结构型 meme 乱填 `category`**：全量字段表里 `category` 只出现过 `Structure` 这一个值，且结构型 meme 往往与 `randomizationSelectionWeightFactor`、`deityCount`、`worshipRoomLabel` 一起出现；给普通 meme 加 `category` 属于未验证用法（**待验证**）。

## 核验

- **每个字段路径**都逐条对照 `<REPO_ROOT>\docs\def-schema.json` 中 `defTypes.MemeDef`（38 个实例、102 条路径）生成字段说明表，写入前用脚本断言路径存在（0 个缺失）；出现率数字与 `03-全量字段参考\字段\MemeDef.md` 一致。
- **① 普通 Meme 骨架**逐字核对 `Ideology/Defs/MemeDefs/Memes_Misc.xml` 的 `Darkness`（defName/label/description/iconPath/groupDef=Misc/impact=3/exclusionTags/requireOne/generalRules/descriptionMaker/rules/renderOrder）与 `Blindsight`（requiredRituals 结构）。
- **groupDef 七个合法值**：核对 `MemeGroupDef` 在全库的 defName 全集（GenderSupremacy、GroupRelation、Individualism、Misc、Primacy、Theist_Embodied、Theist_Abstract）。
- **② 仪式联动**：`requiredRituals/li/{precept,pattern}` 取自 `Ideology/Defs/MemeDefs/Memes_Misc.xml` 的 `Blindsight`；`selectOneOrNone/{noneChance,preceptThingPairs}` 取自 `Ideology/Defs/MemeDefs/Memes_GenderSupremacy.xml`；`styleItemTags` 与 `thingStyleCategories`（含 `li MayRequire` 写法）取自 `Anomaly/Defs/MemeDefs/Memes_Misc.xml` 的 `Inhuman` 与 `Ritualist`；`consumableBuildings` 取自 `Ideology/Defs/MemeDefs/Memes_GroupRelation.xml` 的 `Supremacist`；`agreeableTraits` 取自 `Memes_GenderSupremacy.xml` 的 `MaleSupremacy`。
- **③ 结构型 Meme**：逐字核对 `Ideology/Defs/MemeDefs/Memes_Structures_Basic.xml` 的 `Structure_Archist`（category=Structure/iconPath=UI/Structures/Archist/impact=0/randomizationSelectionWeightFactor=3/deityCount=0/descriptionMaker/patterns+constants/worshipRoomLabel=shrine/symbolPacks）。`descriptionMaker/patterns/li/def` 的指向类型由 `Ideology/Defs/RulePackDefs/RulePacks_Ideo_Description.xml`（`IdeoStoryPatternDef` / `defName=ArchistDescription`，该文件 262-271 行）确认。
- **`requiredPreceptsOnly` 结论**：由 def-schema.json 全库检索（254 个 DefType、1560 个 def 文件）确认该路径只出现在 `FactionDef`，MemeDef 的 102 条路径中无同名或近似路径；原版唯一用例见 `Anomaly/Defs/FactionDefs/Factions_Misc.xml`。
- 未实际启动游戏加载本模板；XML 结构、元素名与属性名均取自上述原版文件与字段表，**是否能在运行时正确注册未做游戏内验证**。
