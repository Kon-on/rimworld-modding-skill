# TerrainDef

## 用途

TerrainDef 定义一种地表：贴图、通行代价、可建造性（`affordances`）、肥力、美观与清洁加成、被污染时的样子、风暴/水淹等特殊行为。它是 BiomeDef 的落地产物——BiomeDef 决定"哪里长什么地形"，TerrainDef 决定"那块地形到底是什么"。与 ThingDef（地板类建筑的建造目标）、Filth（脏污）、Hediff（踩进去受伤）联动。

## 模板

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Defs>

  <!-- ① 室内地板：继承原版 FloorBase，自动获得 layerable / Floor 标签 /
       designationCategory=Floors / 可建造所需的 Heavy 支撑 等默认值。 -->
  <TerrainDef ParentName="FloorBase">
    <defName>EXAMPLE_SaltCuredPlankFloor</defName>
    <label>salt-cured plank floor</label>
    <description>用盐水泡过的木板拼成的地面。踩着暖和，但一点都不防火。</description>

    <!-- 贴图路径不带扩展名 -->
    <texturePath>Terrain/Surfaces/WoodFloor</texturePath>

    <!-- 烧毁后变成什么地形 -->
    <burnedDef>BurnedWoodPlankFloor</burnedDef>

    <!-- 0~255 整数或 0~1 浮点都接受：原版两种写法都有 -->
    <color>(108,78,55)</color>

    <!-- 建造消耗与属性（键是 StatDef defName，键名是 ThingDef defName） -->
    <statBases>
      <WorkToBuild>85</WorkToBuild>
      <Flammability>0.22</Flammability>
    </statBases>
    <costList>
      <WoodLog>3</WoodLog>
    </costList>

    <isPaintable>true</isPaintable>
    <designationHotKey>Misc9</designationHotKey>
    <uiOrder>2000</uiOrder>
  </TerrainDef>

  <!-- ② 自然地表：继承原版 NaturalTerrainBase，自动获得 natural=true /
       Walkable 通行性 / 污染覆盖贴图等默认值。 -->
  <TerrainDef ParentName="NaturalTerrainBase">
    <defName>EXAMPLE_SaltCrustSoil</defName>
    <label>salt-crusted soil</label>
    <description>结成硬壳的盐碱土。走上去咔嚓作响，作物却只能勉强扎下根。</description>

    <texturePath>Terrain/Surfaces/SoilRich</texturePath>
    <pollutedTexturePath>Terrain/Surfaces/SoilPolluted</pollutedTexturePath>

    <!-- 边缘渲染风格：FadeRough / Hard / Water -->
    <edgeType>FadeRough</edgeType>
    <!-- 地形分类：Misc / Sand / Soil 等 -->
    <categoryType>Soil</categoryType>
    <renderPrecedence>340</renderPrecedence>

    <!-- 通行代价：越大越难走 -->
    <pathCost>2</pathCost>

    <statBases>
      <Beauty>-3</Beauty>
      <BeautyOutdoors>0</BeautyOutdoors>
      <Cleanliness>-1</Cleanliness>
    </statBases>

    <!-- 可建造性/可挖掘性标签（TerrainAffordanceDef defName） -->
    <affordances>
      <li>Light</li>
      <li>Medium</li>
      <li>Heavy</li>
      <li>GrowSoil</li>
      <li>Diggable</li>
    </affordances>

    <!-- 踩上去会产生的脏污（ThingDef） -->
    <generatedFilth>Filth_Dirt</generatedFilth>
    <fertility>1.0</fertility>
    <takeFootprints>True</takeFootprints>

    <!-- 踩进去的受伤效果：capacities 是 ToolCapacityDef，hediff 是 HediffDef -->
    <tools>
      <li>
        <label>dirt</label>
        <capacities>
          <li>KickMaterialInEyes</li>
        </capacities>
        <hediff>DirtInEyes</hediff>
        <cooldownTime>1.5</cooldownTime>
      </li>
    </tools>

    <tags>
      <li>Soil</li>
    </tags>
  </TerrainDef>

</Defs>
```

## 字段说明

| 字段 | 出现率 | 值类型 | 说明 |
|---|---|---|---|
| `defName` / `label` | 83.2% (114/137) | 文本 | 必填标识与内部名 |
| `description` | 24.1% (33/137) | 文本 | 描述文本 |
| `texturePath` | 52.5% (72/137) | 文本 | 主贴图路径（不带扩展名） |
| `pollutedTexturePath` | 19.7% (27/137) | 文本 | 被污染时替换的贴图 |
| `edgeType` | 27.0% (37/137) | 文本 | 边缘渲染风格（原版样例 FadeRough / Hard / Water） |
| `renderPrecedence` | 50.4% (69/137) | 数值 | 渲染层级（原版样例 240 / 251 / 340） |
| `pathCost` | 24.8% (34/137) | 数值 | 通行代价（原版样例 1 / 2 / 14） |
| `statBases` | 40.2% (55/137) | 容器 | 键是 StatDef defName |
| `statBases/Beauty` | 32.9% (45/137) | 数值 | 美观（原版样例 -10 / -2 / -1） |
| `statBases/BeautyOutdoors` | 10.2% (14/137) | 数值 | 室外美观（原版样例 -5 / 0） |
| `statBases/Cleanliness` | 20.4% (28/137) | 数值 | 清洁度（原版样例 -3 / -0.1 / 0.2） |
| `statBases/WorkToBuild` | 16.1% (22/137) | 数值 | 建造工作量（原版样例 100 / 120 / 300） |
| `statBases/Flammability` | 8.0% (11/137) | 数值 | 可燃性（原版样例 0.15 / 0.22 / 0.32） |
| `statBases/MarketValue`、`StyleDominance` | 3.6% (5/137) | 数值 | 其它 StatDef |
| `affordances/li` | 86.9% (119/137) | 文本 | TerrainAffordanceDef：能否被建造/挖掘（原版样例 Light / Medium / Heavy / Walkable / Diggable / GrowSoil） |
| `tags / tags/li` | 29.9% (24/137) / 32.1% (44/137) | 文本 | **自由字符串标签**（原版值 Soil / Floor / Road / FineFloor）。本体**没有** TerrainTagDef 这个 Def 类型，所以这里不是跨 Def 引用 |
| `color` | 38.7% (53/137) | 文本 | 染色，`(r,g,b)` 0~255 或 0~1（原版两种写法都有：`(108,78,55)` 与 `(0.369, 0.369, 0.369)`） |
| `fertility` | 25.6% (35/137) | 数值 | 肥力（原版样例 0 / 1 / 1.0） |
| `takeFootprints` | 10.9% (15/137) | 布尔 | 是否留下脚印（原版写作 True / true 两种） |
| `generatedFilth` | 13.1% (18/137) | 文本 | ThingDef：踩过产生的脏污（原版样例 Filth_Dirt / Filth_Sand） |
| `scatterType` | 9.5% (13/137) | 文本 | 散布装饰风格（原版样例 Rocky / SoftDry / SoftGray） |
| `costList` | 38.0% (52/137) | 容器 | 建造消耗：键是 ThingDef defName |
| `costList/WoodLog`、`costList/BlocksGranite` | 2.2% (3/137) / 4.4% (6/137) | 数值 | 具体材料（原版样例 WoodLog 12/20/3、BlocksGranite 20/4） |
| `constructEffect` | 5.8% (8/137) | 文本 | EffecterDef defName（原版样例 ConstructDirt / ConstructWood / ConstructMetal） |
| `designationCategory` | 10.2% (14/137) | 文本 | DesignationCategoryDef（原版样例 Floors / Structure） |
| `designationHotKey` | 8.8% (12/137) | 文本 | 快捷键（原版样例 Misc6 / Misc7 / Misc8 / Misc9） |
| `uiOrder` | 9.5% (13/137) | 数值 | 建造菜单排序（原版样例 2010 / 2020 / 2030） |
| `isPaintable` | 11.7% (16/137) | 布尔 | 能否被刷漆染色 |
| `burnedDef` | 3.6% (5/137) | 文本 | TerrainDef：烧毁后变成什么（原版样例 BurnedCarpet / BurnedStrawMatting） |
| `layerable` | 5.8% (8/137) | 布尔 | 是否可被上层地形覆盖（`FloorBase` 里是 true） |
| `natural` | 2.9% (4/137) | 布尔 | 是否自然地表（`NaturalTerrainBase` 里是 true） |
| `driesTo` | 9.5% (13/137) | 文本 | TerrainDef：干涸后变成什么（原版样例 Gravel / Sand / Soil） |
| `terrainAffordanceNeeded` | 2.2% (3/137) | 文本 | 自身建造时需要的地基（原版样例 Heavy / Bridgeable / Walkable） |
| `pollutionShaderType`、`pollutionOverlayTexturePath`、`pollutionColor`、`pollutionOverlayScale` | 8.8% / 13.1% / 10.2% / 3.6% | 文本 | 污染覆盖外观（由 `FloorBase`/`NaturalTerrainBase` 继承即可） |
| `waterBodyType` / `waterDepthShader` | 7.3% (10/137) / 5.8% (8/137) | 文本 | 水体类型与深度着色器（原版样例 Freshwater / Saltwater、Map/WaterDepth） |
| `tools/li/{label,capacities,hediff,cooldownTime}` | 8.8% (12/137) | 容器 | 踩踏/踢起物：capacities 是 ToolCapacityDef，hediff 是 HediffDef |
| `researchPrerequisites/li` | 7.3% (10/137) | 文本 | ResearchProjectDef：建造前置研究 |
| `constructionSkillPrerequisite` | 7.3% (10/137) | 数值 | 建造技能门槛（原版样例 3 / 6） |
| `resourcesFractionWhenDeconstructed` | 3.6% (5/137) | 数值 | 拆除返还比例（原版样例 0 / 1） |
| `categoryType` | 10.9% (15/137) | 文本 | 地形大类（原版样例 Misc / Sand / Soil） |
| `drawStyleCategory` | 2.2% (3/137) | 文本 | 绘制分组（原版样例 FilledRectangle / Floors / Foundations） |
| `canEverTerraform` | 2.2% (3/137) | 布尔 | 能否被地形改造 |
| `passability` | 2.2% (3/137) | 文本 | 通行性（原版样例 Impassable） |
| `filthAcceptanceMask/li` | 5.1% (7/137) | 文本 | 接受哪些脏污类别（原版样例 None / Unnatural） |
| `placeWorkers/li` | 2.2% (3/137) | 文本 | C# 类名（PlaceWorker_*） |

## 常见坑

1. **XML 元素名是 `tags`，不是 `terrainTags`。** C# 侧属性叫 `terrainTags`，但 XML 里写 `<tags>`（字段表里只有 `tags` / `tags/li`）。而且本体**没有** TerrainTagDef 这个 Def 类型——它是自由字符串，原版用过 Soil / Floor / Road / FineFloor。
2. **`affordances` 必须是 TerrainAffordanceDef defName。** 本模板用的 `Light / Medium / Heavy / GrowSoil / Diggable` 均为原版实有标签；写一个不存在的标签会让"能不能在这块地上盖东西"的判定直接失败【待验证：具体表现未实测】。
3. **`ParentName` 极省事但会隐藏默认值。** 本模板的两个 def 分别继承 `FloorBase` 与 `NaturalTerrainBase`（都在 `Core/Defs/TerrainDefs/Terrain_Floors.xml` 与 `Terrain_Natural.xml` 里）。忘了继承又只写一半字段，常见后果是地板不出现在建造菜单（缺 `designationCategory`）或自然地形没有 `Walkable` 导致小人绕路。
4. **`color` 有两种量纲**：`(108,78,55)` 是 0~255，`(0.369, 0.369, 0.369)` 是 0~1，原版两种都在用；三者混着写（如 `(0.5, 128, 0.5)`）的行为【推测】会按同一尺度解释，容易得到过曝或全黑。
5. **`texturePath` 不带扩展名、不带 `Textures/` 前缀**（原版 `Terrain/Surfaces/WoodFloor`）。另外本体根本没有松散 `Textures/` 目录——原版贴图全打包在 `Assets.zip` 里（`Resources/Textures/Terrain/Surfaces/WoodFloor.psd.dds`）；mod 侧贴图该怎么放【待验证】，本次未实测 mod 加载路径。
6. **`statBases` / `costList` / `tags` 的"键"是元素名**：`<WorkToBuild>85</WorkToBuild>`、`<WoodLog>3</WoodLog>`。写成 `<li>…` 不会被识别。
7. **`pollutionShaderType` 的值是着色器名（如 `TerrainFadeRoughSoftLight`），不是 Def。** 本模板没有写它，直接继承父定义。

## 核验

- **字段合法性**：逐条对照 `library/03-全量字段参考/字段/TerrainDef.md` 的「全量字段表（160 条路径）」。
- **原版写法依据**（相对 `E:\SteamLibrary\steamapps\common\RimWorld\Data\`）：
  - `Core/Defs/TerrainDefs/Terrain_Natural.xml`：`NaturalTerrainBase`（父定义全貌）与 `Soil`（本模板 ② 的骨架：texturePath / pollutedTexturePath / edgeType / categoryType / renderPrecedence / pathCost / statBases / scatterType / affordances / generatedFilth / fertility / takeFootprints / tools / tags）。
  - `Core/Defs/TerrainDefs/Terrain_Floors.xml`：`FloorBase`（父定义全貌）与 `WoodPlankFloor`（本模板 ① 的骨架：renderPrecedence / description / texturePath / burnedDef / color / pollutionShaderType / isPaintable / statBases / costList / constructEffect / designationHotKey / uiOrder）。
  - `Core/Defs/TerrainDefs/Terrain_Water.xml`：`WaterShallow`（`waterDepthShader`、`driesTo` 的写法）。
- **跨 Def 引用**：`WoodLog` / `BlocksGranite` 为 ThingDef；`Filth_Dirt` 为 ThingDef；`DirtInEyes` 为 HediffDef；`KickMaterialInEyes` 为 ToolCapacityDef；`Beauty` / `BeautyOutdoors` / `Cleanliness` / `WorkToBuild` / `Flammability` / `MarketValue` / `StyleDominance` 为 StatDef；`Light` / `Medium` / `Heavy` / `Walkable` / `Diggable` / `GrowSoil` / `Bridgeable` 为 TerrainAffordanceDef；`Floors` / `Structure` 为 DesignationCategoryDef；`BurnedWoodPlankFloor` 为 TerrainDef——全部通过扫描本体 `Data/**/Defs/**/*.xml` 建立类型索引后比对通过。
- **`tags` 不是 Def 引用**：由 `docs/def-schema.json` 中 DefType 清单不含 `TerrainTagDef` 确认。
- **贴图**：`Terrain/Surfaces/WoodFloor`、`Terrain/Surfaces/SoilRich`、`Terrain/Surfaces/SoilPolluted`、`Terrain/Surfaces/Marsh` 均已在本体 `Assets.zip` 中命中。
