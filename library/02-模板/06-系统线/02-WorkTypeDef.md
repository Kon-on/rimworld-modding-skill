# WorkTypeDef

## 用途

工作类型定义，也就是「工作」标签页里的一行（Mining、Cooking、Smithing 之类）。写完它，玩家才能在小人身上给这一行排优先级；但 `WorkTypeDef` 本身不描述「怎么干活」——真正的行为在 `WorkGiverDef` 里，由后者的 `workType` 指回本 Def 的 defName。

它必须的伙伴：`WorkGiverDef`（原版 22 个 WorkTypeDef 全部至少被一个 WorkGiverDef 的 `workType` 引用，无孤立工种）。`workTags/li` 的取值来自游戏的 WorkTags 枚举，`relevantSkills/li` 的取值来自 `SkillDef`（原版 12 个技能）。原版 1.7 共 22 个实例、14 条字段路径。

## 模板

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Defs>

  <!-- 一个完整工种：字段路径全部取自原版 Core/Defs/WorkTypeDefs/WorkTypes.xml -->
  <WorkTypeDef>
    <defName>EXAMPLE_AlloySmithing</defName>

    <!-- 四个界面用文本：工作表短名、小人身上的标签、进行时、动词 -->
    <labelShort>alloy smithing</labelShort>
    <pawnLabel>Alloy smith</pawnLabel>
    <gerundLabel>alloy smithing</gerundLabel>
    <description>Smelt and work alien alloys at an alloy bench.</description>
    <verb>Smith</verb>

    <!-- 数值越大，在「工作」标签页里越靠上。原版区间 100(Research)~1400(Firefighter)；
         要在 Smithing(470) 与 Tailoring(450) 之间插一个新工种，取 450~470 之间的值即可 -->
    <naturalPriority>465</naturalPriority>

    <!-- 工作标签：取值是 WorkTags 枚举名，不是技能名 -->
    <workTags>
      <li>AllWork</li>
      <li>Commoner</li>
      <li>ManualSkilled</li>
      <li>Crafting</li>
    </workTags>

    <!-- 相关技能：必须是 SkillDef 的 defName（这里用原版技能 Crafting）；
         整个 relevantSkills 省略 = 该工种不需要任何技能 -->
    <relevantSkills>
      <li>Crafting</li>
    </relevantSkills>

    <!-- 新开局时该工种默认是否已勾选（原版 7/22 写 true） -->
    <alwaysStartActive>false</alwaysStartActive>

    <!-- 只有有能力的殖民者才会被派这个活（原版 10/22 写 true） -->
    <requireCapableColonist>true</requireCapableColonist>
  </WorkTypeDef>

  <!-- 无技能需求的简单工种：省略 relevantSkills，workTags 只用泛用标签 -->
  <WorkTypeDef>
    <defName>EXAMPLE_AlloyHauling</defName>
    <labelShort>alloy hauling</labelShort>
    <pawnLabel>Alloy hauler</pawnLabel>
    <gerundLabel>alloy hauling</gerundLabel>
    <description>Carry alien alloy stock around the colony.</description>
    <verb>Haul</verb>
    <naturalPriority>290</naturalPriority>
    <workTags>
      <li>AllWork</li>
      <li>Commoner</li>
      <li>ManualDumb</li>
      <li>Hauling</li>
    </workTags>

    <!-- 禁止奴隶从事该工作（原版 5/22 写 true，如 Warden、Hunting、Art、Research） -->
    <disabledForSlaves>false</disabledForSlaves>
  </WorkTypeDef>

</Defs>
```

## 字段说明

全量 14 条路径（出现率 = 该路径在原版 22 个实例中的出现比例，直接取自字段参考）。

| 字段 | 出现率 | 值类型 | 说明 |
|---|---|---|---|
| `defName` | 100.0% (22/22) | 文本 | Def 唯一 ID，被 WorkGiverDef 的 workType 引用 |
| `labelShort` | 100.0% (22/22) | 文本 | 工作表里的短名，例：firefight / childcare |
| `pawnLabel` | 100.0% (22/22) | 文本 | 小人的工种标签，例：Firefighter / Patient |
| `gerundLabel` | 100.0% (22/22) | 文本 | 进行时描述，例：firefighting / caring |
| `description` | 100.0% (22/22) | 文本 | 悬停说明文字 |
| `verb` | 100.0% (22/22) | 文本 | 动词，例：Extinguish / Care / Become patient |
| `naturalPriority` | 100.0% (22/22) | 数值 | 工作表排序权重，越大越靠上；原版 100~1400 |
| `workTags` | 90.9% (20/22) | 容器 | 工作标签列表（缺的 2 个是 Patient、PatientBedRest） |
| `workTags/li` | 318.2% (70/22) | 文本 | 平均每个工种 3.2 个标签 |
| `relevantSkills` | 72.7% (16/22) | 容器 | 相关技能列表；缺的 6 个 = 无技能需求工种 |
| `relevantSkills/li` | 77.3% (17/22) | 文本 | SkillDef 的 defName |
| `requireCapableColonist` | 45.5% (10/22) | 布尔 | 只派有能力的殖民者 |
| `alwaysStartActive` | 31.8% (7/22) | 布尔 | 新开局默认勾选 |
| `disabledForSlaves` | 22.7% (5/22) | 布尔 | 禁止奴隶从事 |

原版 `workTags/li` 出现过的全部 20 个取值（次数）：AllWork 20、Commoner 18、ManualSkilled 8、Crafting 3、Intellectual 2、Social 2、Caring 2、PlantWork 2、ManualDumb 2、Firefighting 1、Animals 1、Cooking 1、Violent 1、Hunting 1、Shooting 1、Constructing 1、Mining 1、Artistic 1、Hauling 1、Cleaning 1。

原版 `relevantSkills/li` 出现过的全部取值（次数）：Crafting 3、Intellectual 2、Social 2、Animals 2、Plants 2、Medicine 1、Cooking 1、Shooting 1、Construction 1、Mining 1、Artistic 1。技能全集（Core/Defs/SkillDefs/Skills.xml）：Shooting、Melee、Construction、Mining、Cooking、Plants、Animals、Crafting、Artistic、Medicine、Social、Intellectual。

## 常见坑

1. **只加 `WorkTypeDef`、不加 `WorkGiverDef`，等于加了一行没有活干的工种。** 原版 22 个 WorkTypeDef 100% 都有 WorkGiverDef 的 `workType` 指回来（实测 22/22）。反过来，WorkGiverDef 指向不存在的 workType 时，该 giver 不会挂到任何一行上（推测会报配置错误）。
2. **`workTags/li` 写的是 WorkTags 枚举名，不是技能名。** 两者有大量同名成员（Intellectual、Social、Cooking、Animals、Shooting、Crafting、Artistic、Mining 同时是技能名与工作标签名）；最容易写混的是 Construction（技能）与 Constructing（工作标签）——原版 workTags 里只出现 Constructing。照抄上面「workTags 取值清单」里的名字最稳。
3. **`naturalPriority` 越大越靠上（证据推断，待验证）。** 依据：原版 Firefighter 1400 排在最上、Research 100 排在最下。要在两个已有工种之间插入，取中间值即可（如 Smithing 470 与 Tailoring 450 之间取 465）。两个工种取相同值时的先后顺序未核实（待验证）。
4. **`relevantSkills` 整个省略表示「不需要技能」。** 原版省略的 6 个正是无技能需求的工种：Firefighter、Patient、PatientBedRest、BasicWorker、Hauling、Cleaning。写了技能名就必须精确匹配 SkillDef 的 defName，写成别的名字会让该工种永远提示技能不足、无人可派（推测）。
5. **`defName`、`labelShort`、`pawnLabel`、`gerundLabel`、`description`、`verb`、`naturalPriority` 原版 22/22 全写，可视为必填。** 缺 `labelShort` 之类会让「工作」标签页出现空白行（推测）。
6. **`alwaysStartActive`（7/22）、`requireCapableColonist`（10/22）、`disabledForSlaves`（5/22）三者互相独立。** 不写就走缺省值，缺省值本身未反编译核实（待验证）；需要特定行为时请显式写出。

## 核验

本模板逐字段对照的原版位置（相对 <游戏安装目录>\Data\）：

| 模板里的写法 | 原版依据 |
|---|---|
| `defName` / `labelShort` / `pawnLabel` / `gerundLabel` / `description` / `verb` / `naturalPriority` / `workTags` / `relevantSkills` / `requireCapableColonist` / `alwaysStartActive` | Core/Defs/WorkTypeDefs/WorkTypes.xml（Firefighter：workTags Firefighting/Commoner/AllWork、requireCapableColonist true、alwaysStartActive true、naturalPriority 1400；Doctor：relevantSkills Medicine、workTags Caring/Commoner/AllWork；Patient 与 PatientBedRest 不写 workTags 与 relevantSkills） |
| 无技能工种、`disabledForSlaves` | 同上文件（Warden 1100 写 requireCapableColonist 与 disabledForSlaves 与 relevantSkills Social；Hauling 300、Cleaning 200 省略 relevantSkills） |
| 其它资料片的工种 | Biotech/Defs/WorkTypeDefs/WorkTypes.xml（Childcare 1175）、Anomaly/Defs/WorkTypeDefs/WorkTypes.xml（DarkStudy 150） |
| `workTags/li` 与 `relevantSkills/li` 的合法取值 | WorkTags 取值来自 WorkTypes.xml 三个文件的全量统计（20 个值，见上）；技能取值来自 Core/Defs/SkillDefs/Skills.xml |
| 各字段出现率 | library/03-全量字段参考/字段/WorkTypeDef.md（22 实例 / 14 路径），由 docs/def-schema.json 实测生成 |
