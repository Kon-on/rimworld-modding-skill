# ThingDef

## 用途

建筑是 ThingDef 的一支：`category` 为 Building，`thingClass` 通常写 Building / Building_WorkTable / Building_Door / Building_Crate。造价由 `costStuffCount` + `stuffCategories`（可选材料）或 `costList`（固定材料）加 `statBases/WorkToBuild`（建造工作量）决定；占地与通行由 `size`、`passability`、`pathCost`、`fillPercent`、`terrainAffordanceNeeded` 决定。工作台类建筑还要靠 `building/workTableRoomRole` + `building/workTableNotInRoomRoleFactor` 参与房间角色判定，并在 `inspectorTabs` 里挂 `ITab_Bills` 才有"清单"页。它与 StuffCategoryDef、ThingCategoryDef（BuildingsProduction/BuildingsFurniture）、PlaceWorker、DesignationCategoryDef、RecipeDef 联动。

**先纠正两个常见误写**：原版 1.7 的 ThingDef 字段表里**不存在 `filthAffordance` 路径**（本地实测 0 命中），脏污相关真实路径只有 `statBases/FilthRate`（2.8%，58/2054）与顶层 `filthLeaving`（0.6%，13/2054）；也不存在小写 `workToBuild`，真实路径是 `statBases/WorkToBuild`（14.5%，297/2054）。

## 模板

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Defs>

  <!-- ================= 1) 工作台（可换材料制造的建筑） ================= -->
  <!-- ParentName="BenchBase"（Core/Defs/ThingDefs_Buildings/Buildings_Production.xml:125）提供：
       category=Building、thingClass=Building、canOverlapZones=false、minifiedDef=MinifiedThing、
       terrainAffordanceNeeded=Medium、thingCategories(BuildingsProduction)、placeWorkers、
       building{buildingTags Production, workTableRoomRole Workshop}。 -->
  <ThingDef ParentName="BenchBase">
    <defName>EXAMPLE_TableWeaver</defName>
    <label>示例织机</label>
    <description>一台示例工作台，用于演示建筑字段布局。</description>
    <!-- 覆盖父类：这是一个带"清单"页的工作台 -->
    <thingClass>Building_WorkTable</thingClass>
    <graphicData>
      <texPath>Things/Building/Production/TableTailorHand</texPath>
      <graphicClass>Graphic_Multi</graphicClass>
      <drawSize>(3.5,1.5)</drawSize>
      <shaderType>CutoutComplex</shaderType>
      <damageData>
        <cornerTL>Damage/Corner</cornerTL>
        <cornerTR>Damage/Corner</cornerTR>
        <cornerBL>Damage/Corner</cornerBL>
        <cornerBR>Damage/Corner</cornerBR>
      </damageData>
    </graphicData>
    <castEdgeShadows>true</castEdgeShadows>
    <staticSunShadowHeight>0.20</staticSunShadowHeight>
    <!-- 可选材料路线：材料数量 + 允许的材料类别（StuffCategoryDef 的 6 个取值） -->
    <costStuffCount>75</costStuffCount>
    <stuffCategories>
      <li>Metallic</li>
      <li>Woody</li>
    </stuffCategories>
    <altitudeLayer>Building</altitudeLayer>
    <fillPercent>0.5</fillPercent>
    <useHitPoints>true</useHitPoints>
    <!-- 建造工作量写在这里，不写 WorkToMake（那是制造台产物的字段） -->
    <statBases>
      <WorkToBuild>2000</WorkToBuild>
      <MaxHitPoints>180</MaxHitPoints>
      <Flammability>1.0</Flammability>
      <WorkTableWorkSpeedFactor>0.5</WorkTableWorkSpeedFactor>
    </statBases>
    <!-- 占地格数：宽×高，必须是整数格 -->
    <size>(3,1)</size>
    <designationCategory>Production</designationCategory>
    <uiOrder>2400</uiOrder>
    <!-- 工人可以走过去穿过它 -->
    <passability>PassThroughOnly</passability>
    <pathCost>50</pathCost>
    <hasInteractionCell>true</hasInteractionCell>
    <interactionCellOffset>(0,0,-1)</interactionCellOffset>
    <surfaceType>Item</surfaceType>
    <inspectorTabs>
      <li>ITab_Bills</li>
    </inspectorTabs>
    <building>
      <buildingTags>
        <li>Production</li>
      </buildingTags>
      <spawnedConceptLearnOpportunity>BillsTab</spawnedConceptLearnOpportunity>
      <paintable>true</paintable>
      <workTableRoomRole>Workshop</workTableRoomRole>
      <workTableNotInRoomRoleFactor>0.8</workTableNotInRoomRoleFactor>
    </building>
    <!-- 只写字段表里存在的子元素路径；Class 属性值照抄原版 Buildings_Production.xml -->
    <comps>
      <li Class="CompProperties_AffectedByFacilities">
        <linkableFacilities>
          <li>ToolCabinet</li>
        </linkableFacilities>
      </li>
    </comps>
    <placeWorkers>
      <li>PlaceWorker_ShowFacilitiesConnections</li>
      <li>PlaceWorker_PreventInteractionSpotOverlap</li>
    </placeWorkers>
    <!-- 前置研究：写在 ThingDef 顶层，与 recipeMaker/researchPrerequisite 不同 -->
    <researchPrerequisites>
      <li>ComplexClothing</li>
    </researchPrerequisites>
  </ThingDef>

  <!-- ================= 2) 墙（不可通行、固定材料清单的另一条路线） ================= -->
  <ThingDef ParentName="BuildingBase">
    <defName>EXAMPLE_Wall_Reinforced</defName>
    <label>示例加固墙</label>
    <description>一堵示例墙。</description>
    <thingClass>Building</thingClass>
    <category>Building</category>
    <graphicData>
      <texPath>Things/Building/Linked/Wall</texPath>
      <graphicClass>Graphic_Appearances</graphicClass>
      <linkType>CornerFiller</linkType>
      <linkFlags>
        <li>Wall</li>
        <li>Rock</li>
      </linkFlags>
    </graphicData>
    <uiIconPath>Things/Building/Linked/WallSmooth_MenuIcon</uiIconPath>
    <statBases>
      <MaxHitPoints>300</MaxHitPoints>
      <WorkToBuild>135</WorkToBuild>
      <Flammability>0</Flammability>
    </statBases>
    <costStuffCount>5</costStuffCount>
    <stuffCategories>
      <li>Stony</li>
    </stuffCategories>
    <leaveResourcesWhenKilled>false</leaveResourcesWhenKilled>
    <altitudeLayer>Building</altitudeLayer>
    <passability>Impassable</passability>
    <blockWind>true</blockWind>
    <castEdgeShadows>true</castEdgeShadows>
    <fillPercent>1</fillPercent>
    <coversFloor>true</coversFloor>
    <tickerType>Never</tickerType>
    <rotatable>false</rotatable>
    <selectable>true</selectable>
    <neverMultiSelect>true</neverMultiSelect>
    <useStuffTerrainAffordance>true</useStuffTerrainAffordance>
    <terrainAffordanceNeeded>Heavy</terrainAffordanceNeeded>
    <holdsRoof>true</holdsRoof>
    <designationCategory>Structure</designationCategory>
    <uiOrder>2000</uiOrder>
    <staticSunShadowHeight>1.0</staticSunShadowHeight>
    <blockLight>true</blockLight>
    <canOverlapZones>false</canOverlapZones>
    <thingCategories>
      <li>Buildings</li>
    </thingCategories>
    <replaceTags>
      <li>Wall</li>
    </replaceTags>
    <building>
      <paintable>true</paintable>
      <isInert>true</isInert>
      <isWall>true</isWall>
      <supportsWallAttachments>true</supportsWallAttachments>
      <ai_chillDestination>false</ai_chillDestination>
      <relatedBuildCommands>
        <li>Door</li>
        <li>Vent</li>
      </relatedBuildCommands>
    </building>
    <damageMultipliers>
      <li>
        <damageDef>Bomb</damageDef>
        <multiplier>2</multiplier>
      </li>
    </damageMultipliers>
    <designationHotKey>Misc3</designationHotKey>
  </ThingDef>

</Defs>
```

## 字段说明

出现率来自 `03-全量字段参考/字段/ThingDef.md`（分母 2054）。

| 字段 | 出现率 | 值类型 | 说明 |
|---|---|---|---|
| `building` | 19.4% (398/2054) | 容器 | 建筑专有参数节点，几乎所有建筑 Def 都有。 |
| `building/isInert` | 3.0% (62/2054) | 布尔 | 无生命物：不参与温度/精神等主动逻辑。 |
| `building/deconstructible` | 3.3% (68/2054) | 布尔 | 能否被拆除。 |
| `building/claimable` | 4.0% (82/2054) | 布尔 | 能否被认领占有。 |
| `building/repairable` | 1.5% (31/2054) | 布尔 | 能否维修。 |
| `building/paintable` | 3.6% (74/2054) | 布尔 | 能否用染料刷漆。 |
| `building/isTargetable` | 1.5% (31/2054) | 布尔 | 能否被选为攻击目标。 |
| `building/isWall` | 0.1% (1/2054) | 布尔 | 是否按墙处理（原版仅 Wall 写 true）。 |
| `building/supportsWallAttachments` | 0.2% (5/2054) | 布尔 | 墙上能否挂附件。 |
| `building/buildingTags/li` | 3.8% (77/2054) | 文本 | Anomaly / Bed / Biotech / Production 等标签。 |
| `building/workTableRoomRole` | 1.3% (27/2054) | 容器/文本 | 工作台所属房间角色（Workshop/Laboratory/Kitchen）。 |
| `building/workTableNotInRoomRoleFactor` | 0.9% (19/2054) | 数值 | 不在对应房间时的工作速度系数，原版 0.8。 |
| `building/relatedBuildCommands/li` | 1.6% (32/2054) | 文本 | 建造菜单里一起显示的相邻建筑（Door/Vent 等）。 |
| `building/spawnedConceptLearnOpportunity` | 1.1% (23/2054) | 文本 | 建成后解锁的概念（BillsTab）。 |
| `building/uninstallWork` | 0.3% (6/2054) | 数值 | 拆卸工作量，原版 1250/1800/2500。 |
| `building/destroySound` | 3.1% (64/2054) | 文本 | 被摧毁音效（BuildingDestroyed_Metal_Small 等）。 |
| `building/blueprintClass` | 0.4% (8/2054) | 文本 | 蓝图类（Blueprint_Build / Blueprint_Door / Blueprint_Storage）。 |
| `building/blueprintGraphicData/texPath` | 0.7% (14/2054) | 文本 | 蓝图贴图。 |
| `size` | 19.2% (395/2054) | 文本 | 占地格数，形如 `(2, 2)` / `(3,3)`。 |
| `passability` | 15.6% (321/2054) | 文本 | Impassable / PassThroughOnly / Standable。 |
| `pathCost` | 14.3% (294/2054) | 数值 | 通行代价，原版 0 / 14 / 30。 |
| `fillPercent` | 17.7% (363/2054) | 数值 | 占格填充率，影响掩体与遮挡。 |
| `terrainAffordanceNeeded` | 8.3% (170/2054) | 容器/文本 | 需要的建造地形（Diggable / Heavy / Light）。 |
| `useStuffTerrainAffordance` | 0.4% (8/2054) | 布尔 | 用地形要求替换材料要求。 |
| `costStuffCount` | 8.4% (172/2054) | 数值 | 可选材料路线的材料数量（20 / 25 / 70）。 |
| `stuffCategories/li` | 15.2% (313/2054) | 文本 | Metallic / Woody / Stony / Fabric / Leathery / Bioferrite。 |
| `costList` | 17.0% (350/2054) | 容器 | 固定材料清单，子元素名 = 物价 defName。 |
| `costList/Steel` | 10.0% (206/2054) | 数值 | 钢铁用量（15 / 25 / 150）。 |
| `statBases/WorkToBuild` | 14.5% (297/2054) | 数值 | 建造工作量（0 / 1800 / 2000）。 |
| `statBases/MaxHitPoints` | 32.4% (665/2054) | 数值 | 耐久。 |
| `statBases/Flammability` | 22.2% (456/2054) | 数值 | 可燃性。 |
| `statBases/Mass` | 23.9% (490/2054) | 数值 | 质量，影响搬运与压塌。 |
| `statBases/WorkTableWorkSpeedFactor` | 0.1% (3/2054) | 数值 | 工作台速度系数（0.5）。 |
| `statBases/FilthRate` | 2.8% (58/2054) | 数值 | **脏污相关的真实字段之一**（2 / 4 / 20）。 |
| `filthLeaving` | 0.6% (13/2054) | 文本 | **另一个脏污字段**：被摧毁后留下的污物（Filth_RubbleBuilding）。 |
| `designationCategory` | 8.1% (166/2054) | 容器/文本 | 建造菜单分类（Structure/Production/Furniture）。 |
| `designationHotKey` | 4.8% (98/2054) | 文本 | 建造快捷键（Misc1 / Misc11）。 |
| `uiOrder` | 7.4% (152/2054) | 数值 | 建造菜单内排序。 |
| `uiIconPath` | 3.5% (72/2054) | 文本 | 建造菜单图标（与物品贴图分开）。 |
| `uiIconPathsStuff` | 0.1% (2/2054) | 容器 | 按材料换菜单图标（`li/appearance` 0.1%、`li/iconPath` 0.1%）。 |
| `hasInteractionCell` | 2.9% (60/2054) | 布尔 | 是否有交互格（工作台站位）。 |
| `interactionCellOffset` | 3.2% (65/2054) | 文本 | 交互格相对偏移，如 `(0,0,-1)`。 |
| `interactionCellIcon` | 0.2% (5/2054) | 文本 | 交互格图标（DiningChair）。 |
| `inspectorTabs/li` | 4.2% (87/2054) | 文本 | 额外选项卡（ITab_Bills / ITab_Entity）。 |
| `placeWorkers/li` | 10.1% (208/2054) | 文本 | 放置期检查器（PlaceWorker_ShowFacilitiesConnections 等）。 |
| `minifiedDef` | 4.5% (93/2054) | 容器/文本 | 被搬运时的"打包件"Def（MinifiedThing）。 |
| `canOverlapZones` | 5.7% (116/2054) | 布尔 | 能否与种植区等zone重叠。 |
| `researchPrerequisites` / `/li` | 7.3% (151/2054) | 容器 / 文本 | 建造前置研究（顶层写法，与 recipeMaker 的不同）。 |
| `replaceTags/li` | 0.6% (12/2054) | 文本 | 同类替换标签（Wall / Door / Bed）。 |
| `blockWind` | 3.1% (63/2054) | 布尔 | 是否挡风。 |
| `holdsRoof` | 0.8% (17/2054) | 布尔 | 是否撑屋顶。 |
| `blockLight` | 0.9% (18/2054) | 布尔 | 是否挡光。 |
| `staticSunShadowHeight` | 3.9% (80/2054) | 数值 | 太阳阴影高度（0 / 0.15 / 0.20）。 |
| `castEdgeShadows` | 4.8% (99/2054) | 布尔 | 是否投边缘阴影。 |
| `coversFloor` | 0.3% (7/2054) | 布尔 | 是否覆盖地板。 |
| `fertility` | 0.5% (10/2054) | 数值 | 肥力（0 / 1.0 / 2.8）。 |
| `leaveResourcesWhenKilled` | 2.2% (45/2054) | 布尔 | 被摧毁后是否留下资源。 |
| `soundImpactDefault` | 1.5% (31/2054) | 文本 | 默认撞击音效。 |
| `damageMultipliers` | 0.5% (11/2054) | 容器 | 针对特定伤害的倍率（`li/damageDef` 0.6%、`li/multiplier` 0.6%）。 |
| `comps/li/linkableFacilities/li` | 2.3% (48/2054) | 文本 | 可连接的设施（ToolCabinet / Electroharvester）。 |
| `graphicData/shaderType` | 14.3% (293/2054) | 文本 | 着色方式（CutoutComplex 用于带遮罩的贴图）。 |
| `graphicData/damageData` | 7.9% (163/2054) | 容器 | 破损贴图分片（cornerTL/TR/BL/BR 等）。 |

## 常见坑

1. **`filthAffordance` 不存在**：本次对 `03-全量字段参考/字段/ThingDef.md` 与 `docs/def-schema.json` 双向检索均为 0 命中。要控制脏污只有两条真路径：`statBases/FilthRate`（2.8%，58/2054，控制小人/动物走过后掉多少）与顶层 `filthLeaving`（0.6%，13/2054，控制被摧毁时铺什么污物）。
2. **`workToBuild` 小写路径不存在**：真实路径是 `statBases/WorkToBuild`（14.5%，297/2054）。写在 `building` 节点里或写成小写驼峰都不会生效。
3. **建造工作量与制造工作量是两个字段**：建筑用 `statBases/WorkToBuild`，工作台"做出来的东西"的耗时用 `statBases/WorkToMake`（8.1%，167/2054）或 RecipeDef 的 `workAmount`。混用会让建造瞬间完成或永远建不完（**推测**）。
4. **`size` 与贴图 `drawSize` 不是一回事**：`size` 是占地格数（`(3,1)`），写在 `graphicData/drawSize` 的是贴图尺寸（`(3.5,1.5)`）。只改图形尺寸不会改变碰撞与占地（依据 HandTailoringBench 同时写了两者）。
5. **工作台要 `ITab_Bills` 才有清单页**：`inspectorTabs/li`（4.2%，87/2054）不写，建筑能放下但点不出"清单/制作"界面（**推测**，未实测）。
6. **`comps` 的 `Class` 属性不在字段表内**：字段表只收录子元素路径（如 `comps/li/linkableFacilities/li` 2.3%）。写 `<li Class="CompProperties_Xxx">` 时，Class 值必须照抄原版同名 Def 的既有写法——本模板取自 `Core/Defs/ThingDefs_Buildings/Buildings_Production.xml:337`（HandTailoringBench 的 `CompProperties_AffectedByFacilities`）。

## 核验

- **逐字段对照**：上表每条出现率都取自 `03-全量字段参考/字段/ThingDef.md` 的"全量字段表"（分母 2054），可用机器可读版复核：
  `Select-String -Path '03-全量字段参考\字段总表.csv' -Pattern ',ThingDef,statBases/WorkToBuild,'`（列顺序 line,defType,path,present,instances,ratio,kind,samples,sourceFile）。
- **负面结论的核验方式**：`filthAffordance`、`workToBuild` 在字段表与 `docs/def-schema.json` 中均检索不到（0 命中），故本文件明确不写这两个路径。
- **结构照抄原版**（路径相对 `<游戏安装目录>\Data\`）：
  - `Core/Defs/ThingDefs_Buildings/Buildings_Production.xml`：BenchBase（第 125 行）、HandTailoringBench（第 290 行，本模板工作台的逐字段来源）、TableMachining（第 592 行）、TableStonecutter（第 860 行）。
  - `Core/Defs/ThingDefs_Buildings/Buildings_Structure.xml`：Wall（第 218 行，本模板第二个 def 的来源）、DoorBase（第 7 行）、Door（第 65 行）。
  - `Core/Defs/ThingDefs_Buildings/Buildings_Base.xml`：BuildingBase（第 4 行，提供 category/thingClass/altitudeLayer 等基类字段）。
  - `Core/Defs/Misc/StuffCategoryDefs/StuffCategories.xml`（Metallic/Woody/Stony 等 6 个材料类别）、`Core/Defs/ThingCategoryDefs/ThingCategories.xml`（Buildings / BuildingsProduction）。
- **Def 级属性说明**：`ParentName` / `Abstract` / `Name` / `MayRequire` 不是字段表收录的字段路径，属 Def 框架属性，照抄原版写法。
- **待验证项**：常见坑中标注"推测"的三条（WorkToBuild 与 WorkToMake 混用后果、缺 ITab_Bills 的界面表现、尺寸与贴图不一致的表现）只在本机静态比对 Def 得出，未启动游戏实测。
