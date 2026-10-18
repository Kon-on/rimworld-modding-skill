# BiomeDef

## 用途

BiomeDef 定义一个生物群系：地形怎么长（`terrainsByFertility` + `terrainPatchMakers`）、长什么植物和动物（`wildPlants` / `wildAnimals`）、常见病、常见天气配比、可否建家与生成据点。它是世界生成与地图生成之间最重要的一层——每张地图的地表成分几乎都由它决定。上接 WorldGen（`workerClass` 决定该群系在地球上出现在什么纬度/温度带），下联 TerrainDef（地形）、ThingDef（植物）、PawnKindDef（动物）、WeatherDef（天气配比）、IncidentDef（疾病）。

> **重要更正（写给需要 `rocks` / `plantWildnessByLayer` 的读者）**：这两个字段在 RimWorld 1.7 的 BiomeDef 中**不存在**。核验方式：`docs/def-schema.json` 里 BiomeDef 的 288 条路径中没有 `rocks` / `plantWildnessByLayer` / `rockNoise` / `rockChunkChance`（`layers` 也没有）；并且全本体 `Data/**/Defs/**/*.xml` 中 `<rocks>` 出现次数为 **0**。1.7 里岩石类型改由 `forceRockTypes` / `extraRockTypes`（引用 ThingDef）控制，见下表。

## 模板

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Defs>

  <!-- 一个自定义生物群系：温带海滨盐碱地。
       workerClass 决定它在星球上生成的位置规则——这里复用原版温带森林的 worker，
       所以它不会跑到极端纬度去；要真正改变分布规律必须写自己的 BiomeWorker 类。 -->
  <BiomeDef>
    <defName>EXAMPLE_SaltMarsh</defName>
    <label>salt marsh</label>
    <description>潮水退去后留下的咸沼泽。草木稀疏，水洼遍野，走起来比平地慢得多。</description>

    <workerClass>BiomeWorker_TemperateForest</workerClass>

    <!-- 动物/植物总体密度 -->
    <animalDensity>1.3</animalDensity>
    <plantDensity>0.35</plantDensity>
    <movementDifficulty>1.5</movementDifficulty>

    <!-- 世界生成权重（0 = 不生成据点） -->
    <settlementSelectionWeight>0.25</settlementSelectionWeight>

    <!-- 星球视图上的群系贴图（无扩展名） -->
    <texture>World/Biomes/TemperateForest</texture>

    <!-- 采集 -->
    <forageability>0.5</forageability>
    <foragedFood>RawBerries</foragedFood>
    <wildPlantRegrowDays>25</wildPlantRegrowDays>

    <!-- 海岸/湖泊/河岸/泥地专用地形 -->
    <lakeBeachTerrain>Sand</lakeBeachTerrain>
    <riverbankTerrain>Riverbank</riverbankTerrain>
    <riverbankSizeRange>6~8</riverbankSizeRange>
    <mudTerrain>Marsh</mudTerrain>

    <!-- 环境音 -->
    <soundsAmbient>
      <li>Ambient_NightInsects_Standard</li>
    </soundsAmbient>

    <!-- 疾病：diseaseInc 指向 IncidentDef，commonality 是相对权重 -->
    <diseaseMtbDays>60</diseaseMtbDays>
    <diseases>
      <li>
        <diseaseInc>Disease_Flu</diseaseInc>
        <commonality>100</commonality>
      </li>
      <li>
        <diseaseInc>Disease_Plague</diseaseInc>
        <commonality>80</commonality>
      </li>
      <li>
        <diseaseInc>Disease_Malaria</diseaseInc>
        <commonality>50</commonality>
      </li>
    </diseases>

    <!-- 肥力值落在区间内就长成对应地形：这里低肥力是泥土，高肥力是沃土 -->
    <terrainsByFertility>
      <li>
        <terrain>Mud</terrain>
        <min>-999</min>
        <max>0.5</max>
      </li>
      <li>
        <terrain>Soil</terrain>
        <min>0.5</min>
        <max>0.87</max>
      </li>
      <li>
        <terrain>SoilRich</terrain>
        <min>0.87</min>
        <max>999</max>
      </li>
    </terrainsByFertility>

    <!-- 柏林噪声地形斑块：按噪声值区间换成水洼/沼泽，isPond 表示水体会连成池塘 -->
    <terrainPatchMakers>
      <li>
        <perlinFrequency>0.015</perlinFrequency>
        <isPond>true</isPond>
        <thresholds>
          <li>
            <terrain>Marsh</terrain>
            <min>0.73</min>
            <max>0.80</max>
          </li>
          <li>
            <terrain>Mud</terrain>
            <min>0.80</min>
            <max>0.93</max>
          </li>
          <li>
            <terrain>WaterShallow</terrain>
            <min>0.93</min>
            <max>999</max>
          </li>
        </thresholds>
      </li>
    </terrainPatchMakers>

    <!-- 天气配比：键是 WeatherDef defName，值是相对权重 -->
    <baseWeatherCommonalities>
      <Clear>12</Clear>
      <Fog>2</Fog>
      <Rain>2</Rain>
      <DryThunderstorm>1</DryThunderstorm>
      <RainyThunderstorm>1</RainyThunderstorm>
      <FoggyRain>1</FoggyRain>
      <SnowGentle>1</SnowGentle>
      <SnowHard>1</SnowHard>
      <GrayPall>1</GrayPall>
      <Overcast>2</Overcast>
    </baseWeatherCommonalities>

    <!-- 野生植物：键是 ThingDef defName，值是权重 -->
    <wildPlants>
      <Plant_Grass>3.0</Plant_Grass>
      <Plant_GrayGrass>2</Plant_GrayGrass>
      <Plant_Bush>0.3</Plant_Bush>
      <Plant_Berry>0.07</Plant_Berry>
      <Plant_Reeds>1.2</Plant_Reeds>
      <Plant_HealrootWild>0.05</Plant_HealrootWild>
      <Plant_TreeOak>0.15</Plant_TreeOak>
    </wildPlants>

    <!-- 野生动物：键是 PawnKindDef defName，值是权重 -->
    <wildAnimals>
      <Hare>1.0</Hare>
      <Rat>1.0</Rat>
      <Deer>0.5</Deer>
      <WildBoar>0.5</WildBoar>
      <Turkey>0.5</Turkey>
      <Raccoon>0.5</Raccoon>
      <Tortoise>0.3</Tortoise>
      <Gazelle>0.3</Gazelle>
      <Boomalope>0.4</Boomalope>
      <Cougar>0.07</Cougar>
      <Lynx>0.07</Lynx>
      <Warg>0.07</Warg>
    </wildAnimals>

    <!-- 可以给商队当驮兽的动物（PawnKindDef） -->
    <allowedPackAnimals>
      <li>Muffalo</li>
      <li>Alpaca</li>
    </allowedPackAnimals>
  </BiomeDef>

</Defs>
```

## 字段说明

| 字段 | 出现率 | 值类型 | 说明 |
|---|---|---|---|
| `defName` / `label` / `description` | 100.0% (25/25) | 文本 | 三个必填 |
| `workerClass` | 80.0% (20/25) | 文本 | C# 类名，决定该群系在地球上的生成分布（原版样例 BiomeWorker_BorealForest / BiomeWorker_IceSheet） |
| `animalDensity` | 84.0% (21/25) | 数值 | 动物总体密度（原版样例 0 / 1.1 / 2.8；TemperateForest 用 3.7） |
| `plantDensity` | 84.0% (21/25) | 数值 | 植物总体密度（原版样例 0 / 0.19 / 0.40 / 0.65） |
| `movementDifficulty` | 68.0% (17/25) | 数值 | 整体通行难度加成 |
| `settlementSelectionWeight` | 68.0% (17/25) | 数值 | 世界生成据点的权重（0 = 不生成） |
| `texture` | 76.0% (19/25) | 文本 | 星球视图贴图（原版样例 World/Biomes/BorealForest） |
| `forageability` | 68.0% (17/25) | 数值 | 采集产出倍率（原版样例 0 / 0.5 / 0.75 / 1） |
| `foragedFood` | 52.0% (13/25) | 文本 | ThingDef：采集到的食物（原版样例 RawAgave / RawBerries / RawFungus） |
| `wildPlantRegrowDays` | 56.0% (14/25) | 数值 | 野生植物再生天数（原版样例 15 / 20 / 25） |
| `diseaseMtbDays` | 80.0% (20/25) | 数值 | 疾病平均间隔天数（原版样例 0 / 45 / 60） |
| `diseases/li/diseaseInc`、`/commonality` | 700.0% (175/25) | 文本 / 数值 | 疾病 IncidentDef → 相对权重（出现率>100% 是因为列表内可多条） |
| `terrainsByFertility/li/{terrain,min,max}` | 128.0% (32/25) | 容器 | 肥力区间 → TerrainDef |
| `terrainPatchMakers/li/perlinFrequency` | 92.0% (23/25) | 数值 | 噪声频率（原版样例 0.015 / 0.027 / 0.028） |
| `terrainPatchMakers/li/thresholds/li/{terrain,min,max}` | 172.0% (43/25) | 容器 | 噪声区间 → TerrainDef |
| `terrainPatchMakers/li/isPond` | 36.0% (9/25) | 布尔 | 该斑块是否作为水体 |
| `baseWeatherCommonalities/<WeatherDef>` | 88.0% (22/25) | 数值 | 天气相对权重（原版样例 Clear 18 / Rain 2 / SnowHard 40） |
| `wildAnimals/<PawnKindDef>` | 68.0% (17/25) | 数值 | 动物权重（原版样例 Hare 1.0 / Cougar 0.07） |
| `wildPlants/<ThingDef>` | 60.0% (15/25) | 数值 | 植物权重（原版样例 Plant_Grass 5.0 / Plant_Berry 0.07） |
| `coastalWildAnimals/<PawnKindDef>` | 64.0% (16/25) | 数值 | 海岸线专属动物（Odyssey 起大量使用） |
| `pollutionWildAnimals/<PawnKindDef>` | 60.0% (15/25) | 数值 | 污染地块上的动物 |
| `allowedPackAnimals/li` | 136.0% (34/25) | 文本 | 可用驮兽 PawnKindDef |
| `soundsAmbient/li` | 76.0% (19/25) | 文本 | SoundDef 环境音 |
| `lakeBeachTerrain` / `riverbankTerrain` / `mudTerrain` | 68.0% / 52.0% / 36.0% | 文本 | 湖岸 / 河岸 / 泥地 TerrainDef |
| `riverbankSizeRange` | 48.0% (12/25) | 文本 | 河岸宽度范围（原版样例 `6~12`） |
| `forceRockTypes/li` / `extraRockTypes/li` | 4.0% (1/25) | 文本 | ThingDef：强制/追加岩石类型（原版样例 SolidIce / Vacstone） |
| `allowFarmingCamps` | 44.0% (11/25) | 布尔 | 是否允许农耕营地 |
| `allowRivers` / `allowRoads` | 24.0% (6/25) | 布尔 | 是否允许河流 / 道路 |
| `campSelectionWeight` | 40.0% (10/25) | 数值 | 营地生成权重 |
| `canAutoChoose` | 12.0% (3/25) | 布尔 | 世界创建时是否可被自动选中 |
| `maxFishPopulation` / `fishTypes` | 76.0% (19/25) / 64.0% (16/25) | 数值 / 容器 | 钓鱼系统（Odyssey） |
| `extraGenSteps/li` / `preventGenSteps/li` | 40.0% (10/25) / 48.0% (12/25) | 文本 | GenStepDef：追加 / 移除地图生成步骤 |
| `hasBedrock` / `isExtremeBiome` / `generatesNaturally` | 12.0% / 16.0% / 16.0% | 布尔 | 其它开关 |
| `settleWarning` | 24.0% (6/25) | 文本 | 在此建家时的警告文本 |

## 常见坑

1. **`rocks` 与 `plantWildnessByLayer` 在 1.7 已不存在。** 见文首"重要更正"：schema 的 288 条路径里没有它们，全本体 XML 里 `<rocks>` 出现 0 次。需要控制岩石请用 `forceRockTypes` / `extraRockTypes`（引用 ThingDef，例如 `SolidIce` / `Vacstone`）。
2. **`wildAnimals` / `wildPlants` / `coastalWildAnimals` / `pollutionWildAnimals` 的"键是 defName、值是权重"**，键必须真实存在（动物是 PawnKindDef，植物是 ThingDef）。本模板用到的 `Hare`、`Rat`、`Deer`、`WildBoar`、`Turkey`、`Raccoon`、`Tortoise`、`Gazelle`、`Boomalope`、`Cougar`、`Lynx`、`Warg`、`Plant_Grass`、`Plant_GrayGrass`、`Plant_Bush`、`Plant_Berry`、`Plant_Reeds`、`Plant_HealrootWild`、`Plant_TreeOak` 已逐个核验存在。
3. **`baseWeatherCommonalities` 的键是 WeatherDef defName**（`Clear` / `Fog` / `Rain` / `SnowGentle` / `SnowHard` / `GrayPall` / `Overcast` / `DryThunderstorm` / `RainyThunderstorm` / `FoggyRain` 均已核验）。只在 BiomeDef 里写而不写 WeatherDef 本体，那个键指向的空气就会缺失。
4. **`terrainsByFertility` 的区间要覆盖整个肥力范围**（原版用 `-999` 到 `999` 兜底）。留缝隙会导致某些地块没有地形可用——具体表现【待验证】，本次未启动游戏复现。
5. **`workerClass` 决定群系在地球上的分布，不是"外观"。** 复用 `BiomeWorker_TemperateForest` 会让新群系出现在温带；想让新群系出现在别处，必须自己写 BiomeWorker 类（本体 `Assembly-CSharp.dll` 中实测共 19 个原版 `BiomeWorker_*`）。
6. **`terrainPatchMakers` 的 `thresholds` 必须单调且不留空隙**（原版写法是 `0.73→0.80→0.93→999` 首尾相接）。乱序或重叠会得到难以预料的地形噪声图【推测：基于原版全部 23 个实例的一致写法】。
7. **DLC 键要加 `MayRequire`**，例如 `pollutionWildAnimals` 里的 Biotech 动物、`fishTypes` 里的 Odyssey 鱼（原版 `Odyssey/Defs/BiomeDefs` 与 `Core/Defs/BiomeDefs/Biomes_Temperate.xml` 都这么写）。

## 核验

- **字段合法性**：逐条对照 `library/03-全量字段参考/字段/BiomeDef.md` 的「全量字段表（288 条路径）」。模板中所有元素名都能在该表命中；`rocks` / `plantWildnessByLayer` 的缺失也由该表 + `docs/def-schema.json` 双重确认。
- **原版写法依据**（相对 `<游戏安装目录>\Data\`）：
  - `Core/Defs/BiomeDefs/Biomes_Temperate.xml`：`TemperateForest`（本模板骨架：workerClass / animalDensity / plantDensity / settlementSelectionWeight / movementDifficulty / lakeBeachTerrain / riverbankTerrain / riverbankSizeRange / texture / forageability / foragedFood / wildPlantRegrowDays / diseaseMtbDays / diseases / terrainsByFertility / terrainPatchMakers / baseWeatherCommonalities / wildPlants / wildAnimals / pollutionWildAnimals / coastalWildAnimals / allowedPackAnimals）。
  - `Core/Defs/BiomeDefs/Biomes_Misc.xml`：`Biome_Underground`（带 `Name` 的抽象/特殊群系写法）。
  - `Odyssey/Defs/BiomeDefs/Space.xml`：`SpaceBiome`（抽象父定义 + `ParentName` 继承的实例）。
  - `Anomaly/Defs/MapGeneration/{LabyrinthMapGenerator,MetalHellMapGenerator,UndercaveMapGenerator}.xml`：异常群系与其地图生成器的配合写法。
- **跨 Def 引用**：`Mud` / `Soil` / `SoilRich` / `Marsh` / `WaterShallow` / `Sand` / `Riverbank` 为 TerrainDef；`Clear` / `Fog` / `Rain` / `DryThunderstorm` / `RainyThunderstorm` / `FoggyRain` / `SnowGentle` / `SnowHard` / `GrayPall` / `Overcast` 为 WeatherDef；`Disease_Flu` / `Disease_Plague` / `Disease_Malaria` 为 IncidentDef；`RawBerries` 为 ThingDef；`Ambient_NightInsects_Standard` 为 SoundDef——全部通过扫描本体 `Data/**/Defs/**/*.xml` 建立"defType → defName"索引后比对通过。
- **类名**：`BiomeWorker_TemperateForest` 已在本体 `Assembly-CSharp.dll` 中命中。
- **贴图**：`World/Biomes/TemperateForest` 已在本体 `Assets.zip` 中命中（打包为 `Resources/Textures/World/Biomes/TemperateForest.psd.dds`）。
