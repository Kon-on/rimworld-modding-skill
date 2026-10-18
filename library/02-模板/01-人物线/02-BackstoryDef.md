# BackstoryDef

## 用途
BackstoryDef 是给小人写**背景故事**（童年 / 成年）的 Def，它决定这个小人出生时的初始技能加成、禁用哪些工作、强制拥有哪些特质，以及在随机生成时被抽中的概率。
它只影响"生成时的起点"：`skillGains` 直接加到初始技能上，`workDisables` 把工作标签从这个人身上永久去掉。它与 TraitDef（`forcedTraits` / `disallowedTraits`）、WorkTypeDef 的工作标签（`requiredWorkTags` / `workDisables`）以及背景分类（`spawnCategories`）联动。原版共 845 个实例、132 条字段路径。
> 大小写特例：原版 `Core/Defs/BackstoryDefs/Solid/Solid_Rare.xml` 里存在 1 个 `<BackStoryDef>`（大写 S）抽象模板，全库仅此 1 例、只含 `shuffleable`。自己写请统一用 `<BackstoryDef>`。

## 模板
```xml
<?xml version="1.0" encoding="utf-8" ?>
<Defs>

  <BackstoryDef>
    <!-- 唯一 ID；原版常与 identifier 写成同一个值（identifier 出现率 71.0%） -->
    <defName>EXAMPLE_DeepMiner30</defName>
    <identifier>EXAMPLE_DeepMiner30</identifier>

    <!-- 槽位：Childhood（童年）或 Adulthood（成年），原版 97.9% 都显式写 -->
    <slot>Adulthood</slot>

    <title>example deep miner</title>
    <titleShort>example miner</titleShort>
    <!-- [PAWN_nameDef] / [PAWN_possessive] / [PAWN_pronoun] 是原版占位符，会按小人替换 -->
    <description>[PAWN_nameDef] spent twelve years in a lightless deep mine, reading the rock and nothing else. [PAWN_pronoun] never learned to talk to people.</description>

    <!-- 技能加成：子元素名 = 技能 defName，值是加减（可为负数）；不是 <li> 列表 -->
    <skillGains>
      <Mining>6</Mining>
      <Construction>3</Construction>
      <Social>-3</Social>
    </skillGains>

    <!-- 参与随机生成时的分类，li 内填 BackstoryCategoryDef 的 defName（样例 Offworld / Researcher / InsectsRelated） -->
    <spawnCategories>
      <li>Offworld</li>
    </spawnCategories>

    <!-- 禁用工作：可写逗号分隔的单个文本，或 li 列表；无禁用写 None -->
    <workDisables>Social</workDisables>
    <!-- 需要的工作标签；无要求写 None（原版 88.3% 就是文本 None） -->
    <requiredWorkTags>None</requiredWorkTags>

    <!-- 强制特质：键 = TraitDef 的 defName，值 = 等级 degree（0 表示唯一度/单一等级） -->
    <forcedTraits>
      <Undergrounder>0</Undergrounder>
    </forcedTraits>

    <!-- 是否参与随机打乱抽取；false 表示只在 spawnCategories 精确投放时使用 -->
    <shuffleable>false</shuffleable>
  </BackstoryDef>

  <!--
    其它可选字段（示范，未启用）：
    <titleFemale> / <titleShortFemale>   女性称谓（原版各 1.5% / 1.7%）
    <bodyTypeGlobal> / <bodyTypeMale> / <bodyTypeFemale>   强制体型（36.1% / 55.1% / 55.1%）
    <possessions><Novel>1</Novel></possessions>            出生携带物，键=ThingDef名，值=数量（11.4%）
    <disallowedTraits><Pyromaniac>0</Pyromaniac></disallowedTraits>  禁止特质，键=特质名，值=degree（0.6%）
    <ignoreIllegalLabelCharacterConfigError>False</ignoreIllegalLabelCharacterConfigError>（35.4%）
    <requiresSpawnCategory>true</requiresSpawnCategory>（0.9%）
  -->

</Defs>
```

## 字段说明
| 字段 | 出现率 | 值类型 | 说明 |
|---|---|---|---|
| `defName` | 100.0% (845/845) | 文本 | 唯一 ID |
| `title` | 100.0% (845/845) | 文本 | 完整称谓，如 `navy scientist` |
| `titleShort` | 100.0% (845/845) | 文本 | 短称谓，如 `scientist` |
| `description` | 100.0% (845/845) | 文本 | 背景叙述，含 `[PAWN_nameDef]` 等占位符 |
| `skillGains` | 98.8% (835/845) | 容器 | 初始技能加成容器 |
| `slot` | 97.9% (827/845) | 文本 | `Childhood` 或 `Adulthood` |
| `requiredWorkTags` | 88.3% (746/845) | 文本 | 需要的工作标签；文本形式 `None` 极常见 |
| `workDisables` | 81.3% (687/845) | 文本 | 禁用工作，逗号分隔，如 `Caring, Social, Firefighting` |
| `shuffleable` | 71.2% (602/845) | 布尔 | 是否参与随机打乱抽取 |
| `identifier` | 71.0% (600/845) | 文本 | 背景标识，原版常与 defName 相同 |
| `spawnCategories/li` | 143.6% (1213/845) | 文本 | 生成分类；本体 `spawnCategories` 68.8% (581/845) |
| `bodyTypeFemale` | 55.1% (466/845) | 文本 | 强制女性体型 |
| `bodyTypeMale` | 55.1% (466/845) | 文本 | 强制男性体型 |
| `bodyTypeGlobal` | 36.1% (305/845) | 文本 | 强制通用体型 |
| `ignoreIllegalLabelCharacterConfigError` | 35.4% (299/845) | 布尔 | 关闭称谓字符检查 |
| `requiredWorkTags/li` | 23.5% (199/845) | 文本 | 列表写法，样例 `Artistic` / `Caring` / `Intellectual` |
| `forcedTraits` | 17.6% (149/845) | 容器 | 强制特质；键=TraitDef 名，值=degree，如 `Psychopath` 0 / `Industriousness` 1 |
| `workDisables/li` | 15.7% (133/845) | 文本 | 列表写法，样例 `Crafting` / `ManualDumb` / `Social` |
| `skillGains/Social` | 42.5% (359/845) | 数值 | 技能加成，样例 1 / 6 / 7 |
| `skillGains/Shooting` | 39.5% (334/845) | 数值 | 技能加成，样例 -4 / 4 |
| `skillGains/Melee` | 38.8% (328/845) | 数值 | 技能加成，样例 2 / 4 / 5 |
| `skillGains/Intellectual` | 35.0% (296/845) | 数值 | 技能加成 |
| `skillGains/Crafting` | 27.1% (229/845) | 数值 | 技能加成 |
| `skillGains/Construction` | 23.9% (202/845) | 数值 | 技能加成 |
| `skillGains/Medicine` | 23.8% (201/845) | 数值 | 技能加成 |
| `skillGains/Artistic` | 18.1% (153/845) | 数值 | 技能加成 |
| `skillGains/Plants` | 16.1% (136/845) | 数值 | 技能加成 |
| `skillGains/Cooking` | 14.7% (124/845) | 数值 | 技能加成 |
| `skillGains/Mining` | 13.2% (112/845) | 数值 | 技能加成 |
| `skillGains/Animals` | 8.2% (69/845) | 数值 | 技能加成 |
| `possessions` | 11.4% (96/845) | 容器 | 出生携带物，键=ThingDef 名，值=数量 |
| `titleShortFemale` | 1.7% (14/845) | 文本 | 女性短称谓 |
| `titleFemale` | 1.5% (13/845) | 文本 | 女性完整称谓 |
| `requiresSpawnCategory` | 0.9% (8/845) | 布尔 | 是否必须命中 spawnCategories |
| `disallowedTraits` | 0.6% (5/845) | 容器 | 禁止特质，键=特质名，值=degree |

## 常见坑
1. `forcedTraits` / `disallowedTraits` / `possessions` 都是**"以 defName 为标签名"的字典**，不是 `<li>` 列表：正确写法是 `<forcedTraits><TooSmart>0</TooSmart></forcedTraits>`（原版 `Core/Defs/BackstoryDefs/Solid/Solid_Child.xml:26-28`）。写成 `<li>Industriousness</li>` 不会生效。
2. `skillGains` 的子元素名同样是技能 defName（`<Mining>6</Mining>`），不是 `<li>`；技能名拼错时这条加成不会应用。【推测：拼错是否进日志未核实】
3. `slot` 只有 `Childhood` / `Adulthood` 两个合法值（原版 97.9% 都写）；写其它值这份背景无法被正常分配。【推测：未核实具体报错行为】
4. `workDisables` 与 `requiredWorkTags` 都支持单行文本形式，无禁用/无要求时原版写 `None`（如 `Solid_Child.xml:45-46`）；写不存在的 WorkType 名会被忽略。【推测】
5. `title` 与 `titleShort` 原版出现率均为 100.0%，缺一个界面会显示空称谓。
6. 大小写特例：全库只有 `Solid_Rare.xml` 用 `<BackStoryDef>`（大写 S，仅 1 例、仅含 `shuffleable`）；自定义请写 `<BackstoryDef>`，不要照抄这个特例。

## 核验
- 模板字段与逐行写法对照原版 `Core/Defs/BackstoryDefs/Solid/Solid_Child.xml`：`FallenProdigy40`(:4-30) 给出 defName/identifier/slot/title/titleShort/description/skillGains（`<Construction>2</Construction>` 等）/spawnCategories `Cult`/workDisables `Social`/requiredWorkTags `None`/forcedTraits `<TooSmart>0</TooSmart>`/shuffleable `False`；`FarmKid60`(:32-48) 给出 `<workDisables>None</workDisables>` 与纯 skillGains 的简写形态。
- 最小可加载范例（仅 6 个字段）见 `Anomaly/Defs/BackstoryDefs/Solid/Solid.xml` 的 `UnknownChildhood`。
- 大小写变体的唯一实例见 `Core/Defs/BackstoryDefs/Solid/Solid_Rare.xml`（`<BackStoryDef Abstract="True" Name="Solid">`，仅 `shuffleable`）。
- 出现率与样例值来自 `library/03-全量字段参考/字段/BackstoryDef.md` 与同目录 `BackStoryDef_variant.md`。
- 其它可交叉核对文件：`Core/Defs/BackstoryDefs/Shuffled/Tribal_Child.xml`、`Shuffled/Offworld_Glitterworld_Adult.xml`、`Shuffled/Pirate_Adult.xml`。
