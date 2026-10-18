# WorkGiverDef

## 用途

「谁去干什么」的派活规则定义：它把一个 `WorkTypeDef`（工作表里的一行）接到一个 C# 工作类 `giverClass` 上，由该类去扫描地图、挑目标并生成 Job。想让小人自动去干活，光有 `JobDef` 不够，必须有一份 WorkGiverDef 把它挂到工作表上。

配套关系：`workType` 指向 `WorkTypeDef` 的 defName（原版 22 个工种全部至少被一个 giver 引用）；`giverClass` 必须是真实存在的 C# 类（原版共 115 个不同类名）；`fixedBillGiverDefs/li` 指向 `ThingDef` 的 defName；`requiredCapacities/li` 指向 `PawnCapacityDef`（原版只用 Manipulation / Moving / Talking）；`equivalenceGroup` 指向 `WorkGiverEquivalenceGroupDef`（原版 3 个）。原版 1.7 共 155 个实例、33 条字段路径。

## 模板

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Defs>

  <!-- 在指定工作台上做活的 giver：原版 20 个 WorkGiver_DoBill 类 giver 都是这个写法 -->
  <WorkGiverDef>
    <defName>EXAMPLE_DoBillsAlloyBench</defName>
    <label>make alloy items</label>

    <!-- 真正干活的 C# 类，必须是 WorkGiver 的子类 -->
    <giverClass>WorkGiver_DoBill</giverClass>

    <!-- 挂到哪一行工作；必须是某个 WorkTypeDef 的 defName -->
    <workType>Crafting</workType>

    <!-- 同一 workType 内的检查顺序，数值越大越先被检查（证据推断，待验证） -->
    <priorityInType>60</priorityInType>

    <!-- 工作菜单里的动词与进行时 -->
    <verb>make</verb>
    <gerund>making alloy items</gerund>

    <!-- 小人必须具备的身体能力 -->
    <requiredCapacities>
      <li>Manipulation</li>
    </requiredCapacities>

    <!-- 这个 giver 服务哪些工作台（ThingDef 的 defName）。
         注意：这里借用了原版电熔炉只为让本文件可直接加载，你自己的 mod 里请换成自己的 ThingDef -->
    <fixedBillGiverDefs>
      <li>ElectricSmelter</li>
    </fixedBillGiverDefs>

    <!-- 持续性的活（如做东西）不被饥饿/疲劳打断 -->
    <prioritizeSustains>true</prioritizeSustains>

    <!-- 机械族能不能干这份活（原版 32/155 写它） -->
    <canBeDoneByMechs>false</canBeDoneByMechs>
  </WorkGiverDef>

  <!-- 同一批工作台挂到另一个工种的例子：原版同一 ThingDef 被多个 giver 引用很常见 -->
  <WorkGiverDef>
    <defName>EXAMPLE_DoBillsAlloyBenchSmithing</defName>
    <label>smelt alloys at alloy bench</label>
    <giverClass>WorkGiver_DoBill</giverClass>
    <workType>Smithing</workType>
    <priorityInType>55</priorityInType>
    <verb>smelt</verb>
    <gerund>smelting alloys</gerund>
    <requiredCapacities>
      <li>Manipulation</li>
    </requiredCapacities>
    <fixedBillGiverDefs>
      <li>ElectricSmelter</li>
    </fixedBillGiverDefs>
    <canBeDoneByMechs>true</canBeDoneByMechs>
  </WorkGiverDef>

</Defs>
```

## 字段说明

全量 33 条路径（出现率 = 该路径在原版 155 个实例中的出现比例，直接取自字段参考）。

| 字段 | 出现率 | 值类型 | 说明 |
|---|---|---|---|
| `defName` | 99.4% (154/155) | 文本 | Def 唯一 ID；缺的 1 个是 Biotech 的 Abstract 基类 |
| `giverClass` | 98.1% (152/155) | 文本 | C# 工作类名，例：WorkGiver_DoBill / WorkGiver_FightFires |
| `label` | 97.4% (151/155) | 文本 | 工作菜单里的名称，例：make things at serum lab |
| `gerund` | 94.8% (147/155) | 文本 | 进行时，例：capturing / releasing |
| `verb` | 94.8% (147/155) | 文本 | 动词，例：capture / release |
| `workType` | 94.2% (146/155) | 文本 | 挂到哪个 WorkTypeDef，例：Crafting / Hauling / Smithing |
| `priorityInType` | 94.2% (146/155) | 数值 | 同工种内检查优先级，原版 5~9999、中位 90 |
| `requiredCapacities` | 88.4% (137/155) | 容器 | 必需的身体能力 |
| `requiredCapacities/li` | 89.7% (139/155) | 文本 | 原版只用 Manipulation / Moving / Talking |
| `prioritizeSustains` | 29.0% (45/155) | 布尔 | 持续工作时不被饥饿疲劳打断 |
| `canBeDoneByMechs` | 20.6% (32/155) | 布尔 | 机械族可否执行 |
| `fixedBillGiverDefs` | 12.9% (20/155) | 容器 | 固定服务的工作台（ThingDef）列表 |
| `fixedBillGiverDefs/li` | 16.1% (25/155) | 文本 | ThingDef 的 defName，例：BioferriteShaper / MechGestator |
| `scanCells` | 7.7% (12/155) | 布尔 | 扫描型 giver 是否扫描格子 |
| `scanThings` | 7.7% (12/155) | 布尔 | 扫描型 giver 是否扫描物品 |
| `equivalenceGroup` | 4.5% (7/155) | 文本 | 互斥组，原版只有 FeedPatientAnimals / ReleasePrisoner / AssistInConstruction |
| `nonColonistsCanDo` | 4.5% (7/155) | 布尔 | 非殖民者可做 |
| `tagToGive` | 4.5% (7/155) | 文本 | 做该活时给小人打的状态标签，例：Fieldwork / RestingForMedicalReasons |
| `canBeDoneWhileDrafted` | 3.2% (5/155) | 布尔 | 征召状态下也能做 |
| `emergency` | 2.6% (4/155) | 布尔 | 紧急工作（原版有大写 True 与小写 true 两种写法） |
| `directOrderable` | 1.3% (2/155) | 布尔 | 能否被右键直接指派 |
| `doesSmoothing` | 1.3% (2/155) | 布尔 | 是否属于磨平作业 |
| `scannerDef` | 1.3% (2/155) | 文本 | 关联的扫描器 ThingDef，例：GroundPenetratingScanner |
| `workTags` | 1.3% (2/155) | 容器 | 原版仅 2 个 giver 写它 |
| `workTags/li` | 1.3% (2/155) | 文本 | 原版取值 Intellectual / Social |
| `autoTakeablePriorityDrafted` | 0.7% (1/155) | 数值 | 例：20 |
| `billGiversAllAnimals` | 0.7% (1/155) | 布尔 | 原版样例 true |
| `billGiversAllAnimalsCorpses` | 0.7% (1/155) | 布尔 | 原版样例 true |
| `billGiversAllHumanlikes` | 0.7% (1/155) | 布尔 | 原版样例 true |
| `billGiversAllHumanlikesCorpses` | 0.7% (1/155) | 布尔 | 原版样例 true |
| `feedAnimalsOnly` | 0.7% (1/155) | 布尔 | 只喂动物 |
| `feedHumanlikesOnly` | 0.7% (1/155) | 布尔 | 只喂人类 |
| `forceFleck` | 0.7% (1/155) | 文本 | 强制播放的特效，例：FeedbackExtinguish |

## 常见坑

1. **`workType` 必须精确匹配某个 WorkTypeDef 的 defName。** 原版 9 个没有 workType 的 giver 全是靠 `ParentName` 从父 Def 继承来的（如 Biotech 的 HaulToCarrier 继承 HaulToBase、Core 的 DoctorTendToSelfEmergency 继承 DoctorTendToSelf）；自己新写的 giver 请显式写 workType，否则它不会挂到工作表上（推测会报配置错误）。
2. **`giverClass` 必须是真实存在的 C# 类。** 原版用到 115 个不同类名，常见可复用的有 WorkGiver_DoBill（做活，20 个实例）、WorkGiver_FightFires、WorkGiver_TakeToBed 等。写一个不存在的类名，加载时该 Def 会失败（推测：ConfigError）。
3. **`priorityInType` 是「同工种内的检查顺序」，越大越先被检查（证据推断，待验证）。** 依据：Doctor 组里紧急治疗 DoctorTendEmergency 是 110（最高，且 emergency=true），Hauling 组里 TakeEntityToHoldingPlatform 是 300、RearmTurrets 是 150。原版取值 5~9999、中位 90。想让自己的活优先于同工种的某个原版活，取比它更大的值。
4. **`fixedBillGiverDefs/li` 里必须写 ThingDef 的 defName 且该 ThingDef 必须存在。** 原版 20 个 DoBill 类 giver 全部写了它（不写，这类 giver 就没有可服务的工作台）。本模板为让文件能直接加载借用了原版 ElectricSmelter（Core/Defs/ThingDefs_Buildings/Buildings_Production.xml）；换成你自己 ThingDef 的 defName 才是正常的 mod 写法，指向不存在的 ThingDef 会加载报错（推测）。
5. **`equivalenceGroup` 的取值必须来自 WorkGiverEquivalenceGroupDef。** 原版全集只有 3 个：FeedPatientAnimals、ReleasePrisoner、AssistInConstruction，与 `equivalenceGroup` 出现的 3 种取值一一对应；自己编一个名字不会让两组工作互斥（推测）。
6. **`requiredCapacities/li` 原版只出现 Manipulation / Moving / Talking 三个 PawnCapacityDef。** 写其它能力名（如 Sight）原版没有先例，是否生效未核实（待验证）。
7. **`label` / `verb` / `gerund` 决定工作菜单里的文字。** 原版 94.8%~97.4% 都写；缺 `label` 时菜单项会没有名称（推测：显示为空白或 defName）。

## 核验

本模板逐字段对照的原版位置（相对 <游戏安装目录>\Data\）：

| 模板里的写法 | 原版依据 |
|---|---|
| `giverClass WorkGiver_DoBill` + `workType` + `fixedBillGiverDefs` + `verb`/`gerund` | Core/Defs/WorkGiverDefs/WorkGivers.xml（DoBillsCook：workType Cooking、fixedBillGiverDefs ElectricStove/FueledStove；DoBillsCookCampfire：Campfire；DoBillsButcherFlesh：TableButcher/ButcherSpot——20 个 DoBill 实例均如此） |
| `requiredCapacities Manipulation` + `priorityInType` + `prioritizeSustains` + `emergency` | 同上文件（DoctorTendEmergency：Manipulation、110、prioritizeSustains true、emergency true；FightFires：workType Firefighter、emergency true、verb extinguish、gerund extinguishing、canBeDoneWhileDrafted true、autoTakeablePriorityDrafted 20、forceFleck FeedbackExtinguish、directOrderable false） |
| `canBeDoneByMechs` / `feedHumanlikesOnly` / `feedAnimalsOnly` / `equivalenceGroup` | 同上文件（DoctorFeedHumanlikes：feedHumanlikesOnly true、canBeDoneByMechs true；DoctorTendToSelf：canBeDoneByMechs false；HandlingFeedPatientAnimals：feedAnimalsOnly true、equivalenceGroup FeedPatientAnimals；DoBillsMedicalHumanOperation：billGiversAllHumanlikes + billGiversAllHumanlikesCorpses；DoBillsMedicalAnimalOperation：billGiversAllAnimals + billGiversAllAnimalsCorpses） |
| `ParentName` 继承（可省 label/giverClass/workType） | Biotech/Defs/WorkGiverDefs/WorkGivers.xml（Abstract Name=HaulToBase；HaulToCarrier 只写 defName/label/giverClass）；Core/Defs/WorkGiverDefs/WorkGivers.xml（DoctorTendToSelfEmergency 继承 DoctorTendToSelf、BasicReleasePrisoner 继承 ReleasePrisoner、HandlingFeedPatientAnimals 继承 FeedAnimals） |
| `workType` 的合法取值（22 个工种全部被引用） | Core/Biotech/Anomaly 的 Defs/WorkTypeDefs/WorkTypes.xml 与 Defs/WorkGiverDefs/WorkGivers.xml 交叉核对（实测 22/22 均有 giver） |
| `equivalenceGroup` 的 3 个合法取值 | library/03-全量字段参考/字段/WorkGiverEquivalenceGroupDef.md（3 实例）与 WorkGiverDef.md 的 equivalenceGroup 取值比对 |
| 各字段出现率 | library/03-全量字段参考/字段/WorkGiverDef.md（155 实例 / 33 路径），由 docs/def-schema.json 实测生成 |
