# SpecialThingFilterDef

## 用途

SpecialThingFilterDef 定义存储区/清单界面里的"特殊过滤项"——即那些无法用"某类物品"表达的筛选条件，例如"允许腐肉""允许敌人机械尸体""允许研究用书"。原版只有 49 个实例、8 条字段路径（本文件已把它们全部覆盖）。它靠 `parentCategory` 挂到某个过滤分类下，`allowedByDefault` 决定新游戏默认是否勾选，`workerClass` 才是真正决定"什么样的东西通过"的实现，`saveKey` 是写进存档的设置键。它与 RecipeDef（`fixedIngredientFilter/specialFiltersToDisallow`、`forceHiddenSpecialFilters`）、ThingFilter 系统联动。

## 模板

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Defs>

  <!-- ================= 抽象基类：给一组过滤项统一 parentCategory ================= -->
  <!-- 原版写法：Core/Defs/Misc/SpecialThingFilterDefs/SpecialThingFilters.xml:248 的 BaseBookResearchFilter。
       Abstract="True" 的 Def 不会被加载成实际过滤项，只被子项继承。 -->
  <SpecialThingFilterDef Name="EXAMPLE_BaseSampleFilter" Abstract="True">
    <parentCategory>Root</parentCategory>
    <allowedByDefault>true</allowedByDefault>
  </SpecialThingFilterDef>

  <!-- ================= 一个实际可用的过滤项 ================= -->
  <!-- workerClass 决定判定逻辑，原版 95.9%（47/49）都写了它。
       纯 XML 的 mod 只能复用原版已有的 worker；要新的判定逻辑必须自己写 C# 类。 -->
  <SpecialThingFilterDef ParentName="EXAMPLE_BaseSampleFilter">
    <defName>EXAMPLE_AllowSampleOre</defName>
    <label>allow sample ore</label>
    <description>允许这类示例矿石进入库存。</description>
    <!-- 存档键：玩家在这项上的勾选状态以此键写入存档 -->
    <saveKey>allowSampleOre</saveKey>
    <!-- 默认不勾选，避免污染玩家已有存档的库存设置 -->
    <allowedByDefault>false</allowedByDefault>
    <!-- 复用原版 worker：按"已腐烂"判定（SpecialThingFilterWorker_Rotten） -->
    <workerClass>SpecialThingFilterWorker_Rotten</workerClass>
    <!-- 是否在界面上允许玩家改（原版仅 8.2% 写，缺省即视为可改） -->
    <configurable>true</configurable>
  </SpecialThingFilterDef>

</Defs>
```

## 字段说明

`SpecialThingFilterDef` 全类型只有 8 条路径，下表是**全部**字段（出现率分母 49）。

| 字段 | 出现率 | 值类型 | 说明 |
|---|---|---|---|
| `defName` | 95.9% (47/49) | 文本 | 唯一名；原版 49 个里绝大多数以 `Allow` 开头。 |
| `label` | 95.9% (47/49) | 文本 | 界面显示名；原版惯例是 "allow xxx"（allow enemy mech corpses）。 |
| `saveKey` | 95.9% (47/49) | 文本 | 存档键（allowAnomalyResearch / allowCorpsesMechEnemy），必须唯一且稳定。 |
| `workerClass` | 95.9% (47/49) | 文本 | 判定逻辑类名（SpecialThingFilterWorker_Rotten / _CorpsesEnemy / _AllowMainResearch）。 |
| `allowedByDefault` | 71.4% (35/49) | 布尔 | 新游戏默认是否勾选（false / true）。 |
| `parentCategory` | 71.4% (35/49) | 文本 | 挂在哪个过滤分类下（Corpses / CorpsesHumanlike / CorpsesMechanoid / ResearchGain / SkillGain / Root / Animals …）。 |
| `description` | 71.4% (35/49) | 文本 | 悬浮说明（Allow organic things which have started to rot.）。 |
| `configurable` | 8.2% (4/49) | 布尔 | 是否允许玩家在界面上修改（原版多为 true 或省略）。 |

## 常见坑

1. **`workerClass` 是唯一决定"筛什么"的字段**：8 条字段里只有它带逻辑（95.9%，47/49 都写）。**纯 XML 的新增过滤项只能复用原版已有的 worker 类**（如 `SpecialThingFilterWorker_Rotten`）；要写新判定必须提供同名 C# 类，否则加载时找不到类型（**推测**，未实测）。
2. **`parentCategory` 决定它出现在哪个折叠面板下**：不写（或写错）就不会挂进任何分类，玩家在界面上找不到它（**推测**）。原版抽象基类正是把 `parentCategory` + `allowedByDefault` 放在基类里让子项共享（`BaseBookResearchFilter` 第 248 行）。
3. **`saveKey` 发布后不要改**：它是写进存档的设置键（95.9% 都写），改名会让老存档里玩家的勾选状态丢失（**推测**）。
4. **`saveKey` / `defName` 必须全局唯一**：与其它 mod 撞名会互相覆盖（**推测**）；建议加 mod 前缀，例如 `myMod_allowSampleOre`。
5. **`allowedByDefault` 留空的语义**：原版 71.4% 显式写了它，其余多为抽象基类继承而来；新过滤项若希望"默认允许"，显式写 `true` 更稳妥（**推测**）。
6. **`configurable` 只影响界面可改性**：原版仅 8.2%（4/49）写这个字段，说明绝大多数过滤项是默认可改的（**推测**）。

## 核验

- **逐字段对照**：`03-全量字段参考/字段/SpecialThingFilterDef.md` 全类型只有 8 条路径，本文件的字段说明表已把它们全部列出（分母 49）。可用机器可读版复核：
  `Select-String -Path '03-全量字段参考\字段总表.csv' -Pattern ',SpecialThingFilterDef,'`。
- **结构照抄原版**（路径相对 `E:\SteamLibrary\steamapps\common\RimWorld\Data\`）：
  - `Core/Defs/Misc/SpecialThingFilterDefs/SpecialThingFilters.xml`：AllowCorpsesColonist（第 4 行，`parentCategory=CorpsesHumanlike` + `allowedByDefault=false` + `saveKey` + `workerClass` 的标准六件套）、AllowLargeCorpses（第 24 行，带 `configurable=true`）、AllowRotten（第 35 行）、AllowFresh（第 45 行）、BaseBookResearchFilter（第 248 行，抽象基类只写 `parentCategory`+`allowedByDefault`）、AllowMainResearch（第 253 行，通过 `ParentName` 继承）。
- **取值来源**：`parentCategory` 的可用值来自原版实际写法（Root / Corpses / CorpsesHumanlike / CorpsesMechanoid / CorpsesEntity / ResearchGain / SkillGain / Animals / Meat 等）；`workerClass` 的可用值只能取自原版已有类名（字段表 examples 列出的 12 个 `SpecialThingFilterWorker_*` 样例即出自上述文件）。
- **Def 级属性说明**：`ParentName` / `Abstract` / `Name` 不在字段表内，属 Def 框架属性，本模板照抄原版 `BaseBookResearchFilter` 的抽象写法。
- **待验证项**：常见坑 1–6 中标注"推测"的行为后果未在本机启动游戏实测；其中"必须提供同名 C# 类"一条只依据原版 workerClass 命名规律判断，未查反编译源码。
