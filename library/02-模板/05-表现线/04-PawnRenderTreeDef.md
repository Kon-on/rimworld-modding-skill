# PawnRenderTreeDef

## 用途
描述一个 Pawn（殖民者、动物、机械体、异象实体）**怎么被画出来**：一棵渲染节点树，每个节点决定用哪张贴图、画在哪一层、四个朝向各自的偏移/旋转/翻转、以及伤口/泡沫这类覆盖层挂在哪里。当你需要一整套自定义外观结构（例如自造多肢体生物、带外壳的实体）时才写它；只给现有小人加一个附件不要写这个 Def，见「常见坑」第 6 条。
它自己不会生效：必须由 ThingDef 的 `race/renderTree` 按 `defName` 引用（原版 `Core\Defs\ThingDefs_Races\Races_Humanlike.xml:89` 是 `<renderTree>Humanlike</renderTree>`，`Core\Defs\ThingDefs_Races\Races_Animal_Base.xml:22/:64` 分别是 `Misc` 与 `Animal`，`Anomaly\Defs\ThingDefs_Races\Races_Fleshbeasts.xml:71/:201/:297/:414/:534` 分别是 Bulbfreak/Toughspike/Trispike/Fingerspike/Dreadmeld）。
联动 Def：`PawnRenderNodeTagDef`（决定 `tagDef` 能写哪 5 个名字）、`RenderSkipFlagDef`（决定 `skipFlag` 能写哪 7 个名字）；节点类 `nodeClass`/`workerClass`/`li` 的 `Class` 都是 C# 类型名（见「常见坑」第 5 条）。
全量数据：1.7.4981 全库只有 **11 个** PawnRenderTreeDef 实例、**72 条**不同字段路径，仅 Core 与 Anomaly 两个资料片提供（Core 3 个：Humanlike / Animal / Misc；Anomaly 8 个：Bulbfreak / Toughspike / Trispike / Fingerspike / Dreadmeld / Revenant / Devourer / Nociosphere）——它是官方给「整套新生物外形」准备的机制，不是日常小改动用得上的东西。

## 模板

以下 4 个 def 覆盖原版全部写法：①简单动物树 ②附件/抽搐树 ③人形挂点树 ④多层外壳树。字段与取值全部来自原版文件，`defName` 已换成 `EXAMPLE_` 前缀。

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Defs>

  <!-- ① 最基础的一套：照 Core 的 Animal 树形制（Body + 覆盖层 + 被搬运物）。
       所有 nodeClass/workerClass/li Class 都取自 Core\Defs\PawnRenderTreeDefs\PawnRenderTreeDefs.xml:146-190。 -->
  <PawnRenderTreeDef>
    <defName>EXAMPLE_SkyGrazerTree</defName>
    <root Class="PawnRenderNodeProperties_Parent">
      <debugLabel>Root</debugLabel>
      <tagDef>Root</tagDef>
      <children>
        <li>
          <debugLabel>Body</debugLabel>
          <tagDef>Body</tagDef>
          <nodeClass>PawnRenderNode_AnimalPart_Body</nodeClass>
          <workerClass>PawnRenderNodeWorker_AnimalBody</workerClass>
          <useRottenColor>true</useRottenColor>
          <children>
            <!-- 伤口覆盖层：自己不画本体贴图，只把伤口画到 Body 之上 -->
            <li>
              <debugLabel>Wounds</debugLabel>
              <nodeClass>PawnRenderNode_AnimalPart</nodeClass>
              <workerClass>PawnRenderNodeWorker_OverlayWounds</workerClass>
              <overlayLayer>Body</overlayLayer>
              <useGraphic>false</useGraphic>
              <baseLayer>3</baseLayer>
            </li>
            <!-- 驮包：rotDrawMode 写 Fresh, Rotting 表示新鲜/腐烂两种尸体状态都要画 -->
            <li>
              <debugLabel>Pack</debugLabel>
              <nodeClass>PawnRenderNode_AnimalPack</nodeClass>
              <workerClass>PawnRenderNodeWorker_AnimalPack</workerClass>
              <rotDrawMode>Fresh, Rotting</rotDrawMode>
              <baseLayer>5</baseLayer>
            </li>
            <!-- 灭火泡沫覆盖层 -->
            <li>
              <debugLabel>Firefoam</debugLabel>
              <nodeClass>PawnRenderNode_AnimalPart</nodeClass>
              <workerClass>PawnRenderNodeWorker_OverlayFirefoam</workerClass>
              <overlayLayer>Body</overlayLayer>
              <useGraphic>false</useGraphic>
              <baseLayer>10</baseLayer>
            </li>
          </children>
        </li>
        <!-- 被搬运/持握的东西由这个容器节点负责画（Class 决定它是搬运容器） -->
        <li Class="PawnRenderNodeProperties_Carried">
          <debugLabel>Carried thing</debugLabel>
          <workerClass>PawnRenderNodeWorker_Carried</workerClass>
        </li>
      </children>
    </root>
  </PawnRenderTreeDef>

  <!-- ② 带附件（触手/尖刺）：附件节点自带贴图、尺寸、绑定的身体部位组和各朝向偏移。
       Class+字段组合取自 Anomaly 的 Bulbfreak（第 18-35 行）与 Trispike（第 349-379 行），两者拼在一起只为示范。 -->
  <PawnRenderTreeDef>
    <defName>EXAMPLE_TentacleBeastTree</defName>
    <root Class="PawnRenderNodeProperties_Parent">
      <debugLabel>Root</debugLabel>
      <tagDef>Root</tagDef>
      <children>
        <li>
          <debugLabel>Body</debugLabel>
          <tagDef>Body</tagDef>
          <useRottenColor>true</useRottenColor>
          <nodeClass>PawnRenderNode_AnimalPart</nodeClass>
          <children>
            <!-- Spastic = 会不定期抽搐的附件节点（rotationRange/scaleRange/durationTicksRange/nextSpasmTicksRange 都是它的参数） -->
            <li Class="PawnRenderNodeProperties_Spastic">
              <debugLabel>TentacleA</debugLabel>
              <texPath>Things/Pawn/Fleshbeast/Bulbfreak/Tentacles/BulbfreakTentacleA</texPath>
              <drawSize>1.1</drawSize>
              <useRottenColor>true</useRottenColor>
              <!-- 该身体部位被切断后，这个节点就不再绘制 -->
              <linkedBodyPartsGroup>FirstTentacle</linkedBodyPartsGroup>
              <rotDrawMode>Fresh, Rotting</rotDrawMode>
              <rotateFacing>false</rotateFacing>
              <rotationRange>-30~30</rotationRange>
              <scaleRange>0.9~1.1</scaleRange>
              <durationTicksRange>10~35</durationTicksRange>
              <nextSpasmTicksRange>10~50</nextSpasmTicksRange>
              <baseLayer>10</baseLayer>
              <drawData>
                <!-- pivot 是归一化轴心，放在贴图根部，附件才会绕根部甩动 -->
                <defaultData>
                  <pivot>(0.5, 0.95)</pivot>
                  <layer>-7</layer>
                </defaultData>
                <dataNorth><offset>(-0.2, 0, 1.15)</offset></dataNorth>
                <dataEast><offset>(0.6, 0, 0.15)</offset></dataEast>
                <dataSouth>
                  <offset>(0.2, 0, -0.15)</offset>
                  <layer>10</layer>
                </dataSouth>
                <dataWest><flip>true</flip></dataWest>
              </drawData>
            </li>
          </children>
        </li>
        <li Class="PawnRenderNodeProperties_Carried">
          <debugLabel>Carried thing</debugLabel>
          <workerClass>PawnRenderNodeWorker_Carried</workerClass>
        </li>
      </children>
    </root>
  </PawnRenderTreeDef>

  <!-- ③ 人形挂点树：如果你自造的是「人形」生物，一定要有 tagDef=ApparelBody / ApparelHead 的节点，
       原版服装、头饰、植入物都按这两个标签找挂点（Core 文件第 44-48、120-124 行）。
       纹身节点（Class=PawnRenderNodeProperties_Tattoo，需 Ideology）与襁褓节点（Class=PawnRenderNodeProperties_Swaddle，需 Biotech）见 Core 第 20-43、88-95 行。 -->
  <PawnRenderTreeDef>
    <defName>EXAMPLE_AnthropoidTree</defName>
    <root Class="PawnRenderNodeProperties_Parent">
      <debugLabel>Root</debugLabel>
      <tagDef>Root</tagDef>
      <children>
        <li>
          <debugLabel>Body</debugLabel>
          <nodeClass>PawnRenderNode_Body</nodeClass>
          <workerClass>PawnRenderNodeWorker_Body</workerClass>
          <tagDef>Body</tagDef>
          <skipFlag>Body</skipFlag>
          <colorType>Skin</colorType>
          <useRottenColor>true</useRottenColor>
          <useSkinShader>true</useSkinShader>
          <children>
            <li Class="PawnRenderNodeProperties_Overlay">
              <debugLabel>Wounds - pre apparel</debugLabel>
              <workerClass>PawnRenderNodeWorker_OverlayWounds</workerClass>
              <overlayLayer>Body</overlayLayer>
              <baseLayer>8</baseLayer>
            </li>
            <li Class="PawnRenderNodeProperties_Parent">
              <debugLabel>Apparel root</debugLabel>
              <tagDef>ApparelBody</tagDef>
              <baseLayer>20</baseLayer>
            </li>
            <li Class="PawnRenderNodeProperties_Overlay">
              <debugLabel>Wounds - post apparel</debugLabel>
              <workerClass>PawnRenderNodeWorker_OverlayWounds</workerClass>
              <overlayOverApparel>true</overlayOverApparel>
              <overlayLayer>Body</overlayLayer>
              <baseLayer>30</baseLayer>
            </li>
            <li Class="PawnRenderNodeProperties_Overlay">
              <debugLabel>Firefoam</debugLabel>
              <workerClass>PawnRenderNodeWorker_OverlayFirefoam</workerClass>
              <overlayLayer>Body</overlayLayer>
              <baseLayer>40</baseLayer>
            </li>
          </children>
        </li>
        <!-- 断头贴图：Head 被切除后画这个（texPath 换成你自己的） -->
        <li>
          <debugLabel>Head stump</debugLabel>
          <nodeClass>PawnRenderNode_Stump</nodeClass>
          <workerClass>PawnRenderNodeWorker_Stump</workerClass>
          <texPath>Things/Pawn/Humanlike/Heads/None_Average_Stump</texPath>
          <baseLayer>50</baseLayer>
          <colorType>Skin</colorType>
          <skipFlag>Head</skipFlag>
          <useSkinShader>true</useSkinShader>
          <useRottenColor>true</useRottenColor>
          <rotDrawMode>Fresh, Rotting</rotDrawMode>
        </li>
        <li>
          <debugLabel>Head</debugLabel>
          <nodeClass>PawnRenderNode_Head</nodeClass>
          <workerClass>PawnRenderNodeWorker_Head</workerClass>
          <tagDef>Head</tagDef>
          <skipFlag>Head</skipFlag>
          <baseLayer>50</baseLayer>
          <colorType>Skin</colorType>
          <useRottenColor>true</useRottenColor>
          <useSkinShader>true</useSkinShader>
          <children>
            <li>
              <debugLabel>Hair</debugLabel>
              <nodeClass>PawnRenderNode_Hair</nodeClass>
              <workerClass>PawnRenderNodeWorker_FlipWhenCrawling</workerClass>
              <rotDrawMode>Fresh, Rotting</rotDrawMode>
              <colorType>Hair</colorType>
              <skipFlag>Hair</skipFlag>
              <baseLayer>62</baseLayer>
            </li>
            <li Class="PawnRenderNodeProperties_Overlay">
              <debugLabel>Head wounds</debugLabel>
              <workerClass>PawnRenderNodeWorker_OverlayWounds</workerClass>
              <overlayLayer>Head</overlayLayer>
              <baseLayer>65</baseLayer>
            </li>
            <li Class="PawnRenderNodeProperties_Parent">
              <debugLabel>Apparel root</debugLabel>
              <tagDef>ApparelHead</tagDef>
              <baseLayer>70</baseLayer>
            </li>
            <li Class="PawnRenderNodeProperties_Overlay">
              <debugLabel>Status overlay</debugLabel>
              <workerClass>PawnRenderNodeWorker_OverlayStatus</workerClass>
              <baseLayer>100</baseLayer>
            </li>
          </children>
        </li>
        <li Class="PawnRenderNodeProperties_Carried">
          <debugLabel>Weapon/carried thing</debugLabel>
          <workerClass>PawnRenderNodeWorker_Carried</workerClass>
        </li>
      </children>
    </root>
  </PawnRenderTreeDef>

  <!-- ④ 多层外壳：节点可以再带子节点（原版最深三层，Nociosphere 第 910-920 行）。
       Class 是 Anomaly 程序集里的类型，所以用 MayRequire 限定资料片；缺 Anomaly 时该 li 会被跳过。
       第三层那个 li 原版只出现过 Class 属性，所以这里不给它写 MayRequire。 -->
  <PawnRenderTreeDef>
    <defName>EXAMPLE_ShellBeastTree</defName>
    <root Class="PawnRenderNodeProperties_Parent">
      <debugLabel>Root</debugLabel>
      <tagDef>Root</tagDef>
      <children>
        <li>
          <debugLabel>Body</debugLabel>
          <tagDef>Body</tagDef>
          <nodeClass>PawnRenderNode_AnimalPart</nodeClass>
          <children>
            <li Class="PawnRenderNodeProperties_NociosphereSegment" MayRequire="Ludeon.RimWorld.Anomaly">
              <debugLabel>Shell_A</debugLabel>
              <texPath>Things/Pawn/Nociosphere/Shell/Nociosphere_ShellA</texPath>
              <maskPath>Things/Pawn/Nociosphere/Shell/Nociosphere_ShellA_Mask</maskPath>
              <baseLayer>4</baseLayer>
              <!-- 顶层的 offset 只有两段文本（逗号分隔、无括号），与 drawData 里的三元组不同 -->
              <offset>0.5,1.75</offset>
              <children>
                <li Class="PawnRenderNodeProperties_NociosphereSegmentOutline">
                  <texPath>Things/Pawn/Nociosphere/Shell/Nociosphere_ShellA_Outline</texPath>
                </li>
              </children>
            </li>
          </children>
        </li>
      </children>
    </root>
  </PawnRenderTreeDef>

  <!-- 让渲染树真正生效：必须有一个 ThingDef 的 race 块指向它的 defName。
       原版写法见 Core\Defs\ThingDefs_Races\Races_Animal_Base.xml:21-23，整个 race 块只有一个 renderTree：
         <race>
           <renderTree>EXAMPLE_SkyGrazerTree</renderTree>
         </race>
       注意上面这段只是示意的片段，要放进你自己的 ThingDef 里，不要单独当 Def 文件加载。 -->

</Defs>
```

## 字段说明

出现率口径：该路径在全部 11 个 PawnRenderTreeDef 实例中出现次数 / 11（原版 def-schema.json 实测值），抄自 `03-全量字段参考\字段\PawnRenderTreeDef.md`。表中 72 行 = 该 DefType 的全部字段路径，无遗漏、无杜撰。

| 字段 | 出现率 | 值类型 | 说明 |
| --- | --- | --- | --- |
| `defName` | 100.0% (11/11) | 文本 | 必填。全局唯一 ID；由 ThingDef 的 `race/renderTree` 按它引用（见「常见坑」第 6 条）。 |
| `root` | 100.0% (11/11) | 容器 | **必写**，根节点属性。11/11 原版 PawnRenderTreeDef 都写成 `<root Class="PawnRenderNodeProperties_Parent">`（该 Class 是原版唯一取值）。（元素可用属性：Class） |
| `root/children` | 100.0% (11/11) | 容器 | 根节点下的子节点列表。整个渲染树就是这棵嵌套的 li 树。 |
| `root/children/li` | 209.1% (23/11) | 容器 | 一个渲染节点。可用 `Class` 属性指定节点属性类（原版取值：PawnRenderNodeProperties_Parent、_Overlay、_Tattoo、_Swaddle、_Carried、_Spastic、_BulbfreakTentacle、_NociosphereSegment、_NociosphereSegmentOutline）。（元素可用属性：Class） |
| `root/children/li/baseLayer` | 18.2% (2/11) | 数值 | 该节点的绘制层级号（排序键）。同一父节点下的兄弟按它排序，原版常见 0/2/3/5/8/10/20/30/40/50/70/85/100。 |
| `root/children/li/children` | 109.1% (12/11) | 容器 | 子节点容器，可继续嵌套（原版最深三层：Nociosphere 的外壳 + 描边）。 |
| `root/children/li/children/li` | 654.5% (72/11) | 容器 | 深层子节点。可用 `Class` 与 `MayRequire` 属性（如原版 Humanlike 的 `<li Class="PawnRenderNodeProperties_Tattoo" MayRequire="Ludeon.RimWorld.Ideology">`）。（元素可用属性：Class、MayRequire） |
| `root/children/li/children/li/baseLayer` | 518.2% (57/11) | 数值 | 绘制层级号，嵌套层同样使用（出现率 >100% 因为一个 def 内出现多次）。 |
| `root/children/li/children/li/brightnessRange` | 9.1% (1/11) | 文本 | 亮度范围，如 `0.6~0.89`（原版只用在婴儿襁褓节点）。 |
| `root/children/li/children/li/children` | 127.3% (14/11) | 容器 | 该节点字段，含义与上层同名项一致。 |
| `root/children/li/children/li/children/li` | 127.3% (14/11) | 容器 | 该节点字段，含义与上层同名项一致。（元素可用属性：Class） |
| `root/children/li/children/li/children/li/texPath` | 127.3% (14/11) | 文本 | 节点贴图路径。嵌套层（第三层）目前只用它：原版 Nociosphere 的外壳描边 <li Class="PawnRenderNodeProperties_NociosphereSegmentOutline"><texPath>…_Outline</texPath></li>。 |
| `root/children/li/children/li/colorType` | 36.4% (4/11) | 文本 | 取色类型：Skin、Hair。 |
| `root/children/li/children/li/debugLabel` | 654.5% (72/11) | 文本 | 节点名（调试用），嵌套层里几乎每个节点都写。 |
| `root/children/li/children/li/drawData` | 245.5% (27/11) | 容器 | 按朝向区分绘制参数的容器，四个固定朝向子元素 dataNorth/dataEast/dataSouth/dataWest 加一个 defaultData。 |
| `root/children/li/children/li/drawData/dataEast` | 190.9% (21/11) | 容器 | 该节点字段，含义与上层同名项一致。 |
| `root/children/li/children/li/drawData/dataEast/layer` | 36.4% (4/11) | 数值 | 该节点字段，含义与上层同名项一致。 |
| `root/children/li/children/li/drawData/dataEast/offset` | 172.7% (19/11) | 文本 | 该节点的固定偏移，写法是**逗号分隔的两段文本**（如 `0.5,1.75`、`-0.25,-1.65`），注意与 drawData 里的 `(x, y, z)` 三元组写法不同。 |
| `root/children/li/children/li/drawData/dataEast/rotationOffset` | 36.4% (4/11) | 数值 | 该节点字段，含义与上层同名项一致。 |
| `root/children/li/children/li/drawData/dataNorth` | 245.5% (27/11) | 容器 | 该节点字段，含义与上层同名项一致。 |
| `root/children/li/children/li/drawData/dataNorth/flip` | 9.1% (1/11) | 布尔 | 该节点字段，含义与上层同名项一致。 |
| `root/children/li/children/li/drawData/dataNorth/layer` | 72.7% (8/11) | 数值 | 该节点字段，含义与上层同名项一致。 |
| `root/children/li/children/li/drawData/dataNorth/offset` | 218.2% (24/11) | 文本 | 该节点的固定偏移，写法是**逗号分隔的两段文本**（如 `0.5,1.75`、`-0.25,-1.65`），注意与 drawData 里的 `(x, y, z)` 三元组写法不同。 |
| `root/children/li/children/li/drawData/dataNorth/rotationOffset` | 81.8% (9/11) | 数值 | 该节点字段，含义与上层同名项一致。 |
| `root/children/li/children/li/drawData/dataSouth` | 200.0% (22/11) | 容器 | 该节点字段，含义与上层同名项一致。 |
| `root/children/li/children/li/drawData/dataSouth/flip` | 36.4% (4/11) | 布尔 | 该节点字段，含义与上层同名项一致。 |
| `root/children/li/children/li/drawData/dataSouth/layer` | 90.9% (10/11) | 数值 | 该节点字段，含义与上层同名项一致。 |
| `root/children/li/children/li/drawData/dataSouth/offset` | 190.9% (21/11) | 文本 | 该节点的固定偏移，写法是**逗号分隔的两段文本**（如 `0.5,1.75`、`-0.25,-1.65`），注意与 drawData 里的 `(x, y, z)` 三元组写法不同。 |
| `root/children/li/children/li/drawData/dataSouth/rotationOffset` | 100.0% (11/11) | 数值 | 该节点字段，含义与上层同名项一致。 |
| `root/children/li/children/li/drawData/dataWest` | 154.5% (17/11) | 容器 | 该节点字段，含义与上层同名项一致。 |
| `root/children/li/children/li/drawData/dataWest/flip` | 100.0% (11/11) | 布尔 | 该节点字段，含义与上层同名项一致。 |
| `root/children/li/children/li/drawData/dataWest/layer` | 27.3% (3/11) | 数值 | 该节点字段，含义与上层同名项一致。 |
| `root/children/li/children/li/drawData/dataWest/offset` | 81.8% (9/11) | 文本 | 该节点的固定偏移，写法是**逗号分隔的两段文本**（如 `0.5,1.75`、`-0.25,-1.65`），注意与 drawData 里的 `(x, y, z)` 三元组写法不同。 |
| `root/children/li/children/li/drawData/dataWest/rotationOffset` | 36.4% (4/11) | 数值 | 该节点字段，含义与上层同名项一致。 |
| `root/children/li/children/li/drawData/defaultData` | 145.5% (16/11) | 容器 | 该节点字段，含义与上层同名项一致。 |
| `root/children/li/children/li/drawData/defaultData/flip` | 63.6% (7/11) | 布尔 | 该节点字段，含义与上层同名项一致。 |
| `root/children/li/children/li/drawData/defaultData/layer` | 136.4% (15/11) | 数值 | 该节点字段，含义与上层同名项一致。 |
| `root/children/li/children/li/drawData/defaultData/offset` | 9.1% (1/11) | 文本 | 该节点的固定偏移，写法是**逗号分隔的两段文本**（如 `0.5,1.75`、`-0.25,-1.65`），注意与 drawData 里的 `(x, y, z)` 三元组写法不同。 |
| `root/children/li/children/li/drawData/defaultData/pivot` | 136.4% (15/11) | 文本 | 该节点字段，含义与上层同名项一致。 |
| `root/children/li/children/li/drawData/defaultData/rotationOffset` | 45.5% (5/11) | 数值 | 该节点字段，含义与上层同名项一致。 |
| `root/children/li/children/li/drawSize` | 209.1% (23/11) | 数值 | 该节点贴图的绘制尺寸（1.05、1.1、1.2、1.4、6 等）。 |
| `root/children/li/children/li/durationTicksRange` | 100.0% (11/11) | 文本 | 动画/痉挛持续 tick 范围，如 `10~35`、`10~60`。 |
| `root/children/li/children/li/linkedBodyPartsGroup` | 209.1% (23/11) | 文本 | 绑定到哪个身体部件组（BodyPartGroupDef 名），如 FirstTentacle、FifthTentacle；该部件被切断后这个节点就不再绘制。 |
| `root/children/li/children/li/maskPath` | 118.2% (13/11) | 文本 | 遮罩贴图路径（与 texPath 配套，做形状裁剪/发光），如 Things/Pawn/Nociosphere/Shell/Nociosphere_ShellA_Mask。 |
| `root/children/li/children/li/nextSpasmTicksRange` | 100.0% (11/11) | 文本 | 两次痉挛之间的等待 tick 范围，如 `10~50`、`20~60`（配合 PawnRenderNodeProperties_Spastic）。 |
| `root/children/li/children/li/nodeClass` | 209.1% (23/11) | 文本 | 节点类名（嵌套层同样使用）：原版出现的全部取值是 PawnRenderNode_AnimalPart(25 次)、PawnRenderNode_AnimalPart_Body、PawnRenderNode_AnimalPack、PawnRenderNode_Body、PawnRenderNode_Head、PawnRenderNode_Stump、PawnRenderNode_Tattoo_Body、PawnRenderNode_Tattoo_Head、PawnRenderNode_Beard、PawnRenderNode_Hair、PawnRenderNode_Swaddle、PawnRenderNode_Devourer。 |
| `root/children/li/children/li/offset` | 127.3% (14/11) | 文本 | 该节点的固定偏移，写法是**逗号分隔的两段文本**（如 `0.5,1.75`、`-0.25,-1.65`），注意与 drawData 里的 `(x, y, z)` 三元组写法不同。 |
| `root/children/li/children/li/overlayLayer` | 200.0% (22/11) | 文本 | 覆盖层归属（Body、Head），配合 PawnRenderNodeProperties_Overlay 使用：把伤口/泡沫等覆盖画到身体或头部之上。 |
| `root/children/li/children/li/overlayOverApparel` | 9.1% (1/11) | 布尔 | 是否画在衣服之上（原版 1 例，true；用于「衣服之上的伤口」）。 |
| `root/children/li/children/li/rotDrawMode` | 145.5% (16/11) | 文本 | 旋转绘制模式，原版写法 `Fresh, Rotting`。 |
| `root/children/li/children/li/rotateFacing` | 100.0% (11/11) | 布尔 | 是否让贴图随朝向翻转；原版 11 处全部写 `false`（出现在 `PawnRenderNodeProperties_Spastic` 节点上，见 Anomaly 文件 354/386/418 行）。 |
| `root/children/li/children/li/rotationRange` | 100.0% (11/11) | 文本 | 随机旋转角范围，如 `-18~18`、`-30~30`。 |
| `root/children/li/children/li/scaleRange` | 63.6% (7/11) | 文本 | 随机缩放范围，如 `0.9~1.1`、`0.95~1.05`。 |
| `root/children/li/children/li/skipFlag` | 18.2% (2/11) | 文本 | 渲染跳过标记（RenderSkipFlagDef 名），原版取值 Body、Head、Hair、Beard。 |
| `root/children/li/children/li/swaddleColorOffset` | 9.1% (1/11) | 数值 | 襁褓染色偏移，原版 1 例 0.1。 |
| `root/children/li/children/li/tagDef` | 27.3% (3/11) | 文本 | 节点标签（PawnRenderNodeTagDef 的 5 个 defName 之一：Root、Head、ApparelHead、Body、ApparelBody）。 |
| `root/children/li/children/li/texPath` | 381.8% (42/11) | 文本 | 节点贴图路径。嵌套层（第三层）目前只用它：原版 Nociosphere 的外壳描边 <li Class="PawnRenderNodeProperties_NociosphereSegmentOutline"><texPath>…_Outline</texPath></li>。 |
| `root/children/li/children/li/useGraphic` | 136.4% (15/11) | 布尔 | 是否使用图形（`false` 表示不画本体，只作为覆盖层容器），原版取值 false。 |
| `root/children/li/children/li/useRottenColor` | 254.5% (28/11) | 布尔 | 是否使用腐烂色变体，样例 true（嵌套层 28 次）。 |
| `root/children/li/children/li/workerClass` | 263.6% (29/11) | 文本 | 节点工作类名。原版出现的全部取值是 PawnRenderNodeWorker_OverlayWounds(11)、PawnRenderNodeWorker_OverlayFirefoam(11)、PawnRenderNodeWorker_Carried(10)、PawnRenderNodeWorker_AnimalBody(2)、PawnRenderNodeWorker_Body、PawnRenderNodeWorker_Body_Tattoo、PawnRenderNodeWorker_Swaddle、PawnRenderNodeWorker_Stump、PawnRenderNodeWorker_Head、PawnRenderNodeWorker_Tattoo_Head、PawnRenderNodeWorker_Beard、PawnRenderNodeWorker_FlipWhenCrawling、PawnRenderNodeWorker_OverlayStatus、PawnRenderNodeWorker_AnimalPack。 |
| `root/children/li/colorType` | 27.3% (3/11) | 文本 | 取色类型，原版取值 Skin、Hair。 |
| `root/children/li/debugLabel` | 209.1% (23/11) | 文本 | 节点名，便于调试定位（Body、Head、Wounds、Firefoam、Apparel root、Weapon/carried thing…）。原版嵌套层里也几乎都写。 |
| `root/children/li/nodeClass` | 118.2% (13/11) | 文本 | 节点类名，决定这个节点怎么取图形（如 PawnRenderNode_AnimalPart、PawnRenderNode_Body、PawnRenderNode_Head、PawnRenderNode_Devourer）。不写时用默认节点类（推测）。 |
| `root/children/li/rotDrawMode` | 9.1% (1/11) | 文本 | 在哪些旋转绘制模式下绘制，原版写法 `Fresh, Rotting`（逗号分隔）。 |
| `root/children/li/skipFlag` | 27.3% (3/11) | 文本 | 渲染跳过标记（配合 RenderSkipFlagDef），原版取值 Body、Head、Hair、Beard。 |
| `root/children/li/tagDef` | 109.1% (12/11) | 文本 | 节点标签，供服装/植入物等系统按标签查找挂点。原版取值只有 Body、Head、ApparelBody、ApparelHead。 |
| `root/children/li/texPath` | 9.1% (1/11) | 文本 | 该节点的贴图路径（不带前导斜杠、无扩展名），如 Things/Pawn/Humanlike/Heads/None_Average_Stump。 |
| `root/children/li/useRottenColor` | 109.1% (12/11) | 布尔 | 是否使用腐烂色变体（尸体/腐化提醒），样例 true。 |
| `root/children/li/useSkinShader` | 27.3% (3/11) | 布尔 | 是否用皮肤着色器（人形生物的身体/头/断肢用 true）。 |
| `root/children/li/workerClass` | 136.4% (15/11) | 文本 | 节点工作类名，决定绘制逻辑（如 PawnRenderNodeWorker_AnimalBody、PawnRenderNodeWorker_OverlayWounds、PawnRenderNodeWorker_Carried、PawnRenderNodeWorker_Swaddle、PawnRenderNodeWorker_FlipWhenCrawling、PawnRenderNodeWorker_OverlayStatus）。 |
| `root/debugLabel` | 100.0% (11/11) | 文本 | 根节点名，11/11 原版都写 `Root`。调试用，但原版一律写。 |
| `root/tagDef` | 100.0% (11/11) | 文本 | 根节点标签，11/11 原版都写 `Root`（取值来自 PawnRenderNodeTagDef 的 5 个 defName）。 |

## 常见坑

1. **`root` 必须写成 `<root Class="PawnRenderNodeProperties_Parent">`，并带 `<debugLabel>Root</debugLabel>` 与 `<tagDef>Root</tagDef>`。** 11/11 个原版实例都这么写（Core 第 6-8、148-150、194-196 行；Anomaly 全部 8 个 def 同形）。只写裸 `<root>` 会退化成默认节点属性类型，行为**待验证**（未实测）；`root` 上的 `Class` 是原版该字段唯一出现过的属性（属性集只有 Class）。
2. **`tagDef` 只能取 5 个名字、`skipFlag` 只能取 7 个名字。** `tagDef`：Root、Head、ApparelHead、Body、ApparelBody（= `PawnRenderNodeTagDef` 的全部 defName）；`skipFlag`：None、Head、Hair、Beard、Eyes、Body、Tattoos（= `RenderSkipFlagDef` 的全部 defName，原版实际只用到 Body、Head、Beard、Hair）。写别的名字时，服装/断肢/发型系统按名字找不到挂点，节点会被跳过甚至整棵树加载失败——**推测**（未实测报错文本）。自造人形生物时，`tagDef=ApparelBody` 与 `tagDef=ApparelHead` 的两个空节点（无贴图）是衣服、头饰能穿上的前提（Core 第 44-48、120-124 行）。
3. **`baseLayer` 只在同一父节点的兄弟之间排序，不是全局层级。** 原版 Body 的子节点用 2/8/10/20/30/40，Head 的子节点用 52/60/62/65/70/85/100，Anomaly 里不同父的兄弟又各自用 3/4/5/6/10/20；数值本身没有跨树的绝对含义。字段表里深层路径出现率 >100%（例如 `root/children/li/children/li/baseLayer` = 518.2%，57/11）不是「要写很多次」，而是同一个 def 内同一路径多次出现——出现率的分母是 def 数（11），不是元素数。
4. **三套坐标/朝向写法不能混。** 顶层 `offset` 是逗号分隔的两段文本、无括号（Anomaly:915 `0.5,1.75`、:1070 `0,-1.75`）；`drawData` 里的 `offset` 是带括号的三元组（Anomaly:29 `(-0.2, 0, 1.15)`、:834 `(0, 0, 0.55)`）；`pivot` 是带括号的归一化两元组 `(0.5, 0.95)`（Anomaly:26）。写成另一种形式会解析失败——**推测**（格式差异来自原版实测，未实测错误文本）。`drawData` 的子元素名固定为 `defaultData` / `dataNorth` / `dataEast` / `dataSouth` / `dataWest`，只写需要区分的朝向即可（Bulbfreak 只写 defaultData+North+East+South，Trispike 四个全写）；拼错名字该朝向配置不生效——**推测**。
5. **只写这棵树不会改变任何 Pawn。** 必须让 ThingDef 的 `race/renderTree` 指向它的 `defName`（见「核验」清单）。而且 `nodeClass`、`workerClass`、`li` 的 `Class` 都是 C# 类型名：自造新类必须自己在程序集里实现并让加载器能按名字解析，否则加载时报找不到类型——**推测**（原版全部取值都落在 Core/Anomaly 程序集内；未实测第三方类的加载报错文本）。
6. **只想「加一个附件/眼睛/伤疤」不要写 PawnRenderTreeDef。** 原版新增外观更常用其它 DefType 上的 `renderNodeProperties`：`GeneDef`（6.9%，`Biotech\Defs\GeneDefs\GeneDefs_Endogenes.xml:137`）、`HediffDef`（2.6%，`Core\Defs\HediffDefs\BodyParts\Hediffs_BodyParts_Bionic.xml:57`，配套 `forceRenderTreeRecache` 见 `Core\Defs\HediffDefs\Hediffs_Local_Misc.xml:164`）、`MutantDef`（25%）、`TraitDef` 的子字段 `degreeDatas/li/renderNodeProperties`（2.0%，`Anomaly\Defs\TraitDefs\Traits.xml:54`）、`ThingDef` 的 `comps/li/renderNodeProperties`（0.1%）。这些路径分别属于各自的 DefType，**不在本文件的 72 条字段表里**，写的时候要去对应 DefType 的字段表核。顺带一条 1.7 的事实：对全部 254 个 DefType 的全量扫描中**已经不存在任何 `graphicSet` 路径**（0 条），与「渲染树取代旧的 GraphicSet 写法」的说法一致；但 Ludeon 究竟在哪个版本移除、是否还有代码回退路径**待验证**（本次未比对 1.6 源码或程序集）。

## 核验

本模板的核实方式与依据：

- **字段表**：72 行全部由 `docs/def-schema.json` 的 `defTypes.PawnRenderTreeDef`（instances=11、pathCount=72）程序化导出，出现率 = 出现次数/11，与同行参考 `03-全量字段参考\字段\PawnRenderTreeDef.md` 逐字一致；导出时对每条路径做了存在性断言，**0 条缺失**。
- **模板内的每个元素/属性**：用程序（去掉注释后逐 token 建栈）把模板 XML 的每个元素路径与属性跟同一份 schema 比对：**4 个 def、57 条不同元素路径、175 个元素、18 处属性用法（全部是 `Class` / `MayRequire`）——0 条越界**，即模板里没有任何一个字段或属性是字段表中不存在的。
- **Core 依据文件**：`Core\Defs\PawnRenderTreeDefs\PawnRenderTreeDefs.xml`（全文 231 行）——Humanlike 第 4-144 行（root Class:6、debugLabel:7、tagDef:8、Body:10-63、tagDef Body:14、skipFlag Body:15、colorType Skin:16、useRottenColor:17、useSkinShader:18、Tattoo+MayRequire Ideology:20-28、Wounds pre apparel:29-34、Swaddle+MayRequire Biotech:35-43、ApparelBody 挂点:44-48、Wounds post apparel:49-55、Firefoam:56-61、Head stump:65-76、Head:77-137、tagDef Head:81、skipFlag Head:82、baseLayer 50:83、Head tattoo:88-95、Beard:96-104、Hair:105-113、Head wounds:114-119、ApparelHead 挂点:120-124、Firefoam:125-130、Status overlay:131-135、Carried:138-141）、Animal 第 146-190 行（Body:152-183、PawnRenderNode_AnimalPart_Body:155、Worker_AnimalBody:156、Wounds:159-166、Pack:167-173、Firefoam:174-181、Carried:184-187）、Misc 第 192-228 行。
- **Anomaly 依据文件**：`Anomaly\Defs\PawnRenderTreeDefs\PawnRenderTreeDefs.xml`（全文 1084 行、8 个 def）——Bulbfreak:6-233（`Class=PawnRenderNodeProperties_BulbfreakTentacle`:18、drawSize:21、useRottenColor:22、linkedBodyPartsGroup:23、drawData/defaultData/pivot/layer:24-28、dataNorth/dataEast/dataSouth:29-34）、Toughspike:236、Trispike:338（`Class=PawnRenderNodeProperties_Spastic`:349、rotDrawMode:353、rotateFacing:354、rotationRange:355、scaleRange:356、durationTicksRange:357、nextSpasmTicksRange:358、drawData 四朝向:362-379）、Fingerspike:460、Dreadmeld:524、Revenant:814（tagDef Head:827、drawData 四朝向偏移:832-840）、Devourer:861（`PawnRenderNode_Devourer`:870）、Nociosphere:900-1081（`Class=PawnRenderNodeProperties_NociosphereSegment`:910、maskPath:913、顶层 offset:915、三层嵌套 outline:916-920、末段 baseLayer 0:1069 + offset `0,-1.75`:1070）。
- **ThingDef 引用方式**：`Core\Defs\ThingDefs_Races\Races_Humanlike.xml:89`、`Core\Defs\ThingDefs_Races\Races_Animal_Base.xml:21-23`（race 块只有 renderTree）与 `:64`、`Anomaly\Defs\ThingDefs_Races\Races_Fleshbeasts.xml:71/:201/:297/:414/:534`、`Anomaly\Defs\ThingDefs_Races\Races_Entities_Misc.xml:26` 附近。
- **`tagDef` / `skipFlag` 取值全集**：`def-schema.json` 中 `PawnRenderNodeTagDef`（5 个 defName：Root、Head、ApparelHead、Body、ApparelBody）与 `RenderSkipFlagDef`（7 个 defName：None、Head、Hair、Beard、Eyes、Body、Tattoos）。
- **第 6 条坑的联动证据**（这些路径属其它 DefType）：`Biotech\Defs\GeneDefs\GeneDefs_Endogenes.xml:137`、`Core\Defs\HediffDefs\BodyParts\Hediffs_BodyParts_Bionic.xml:57`、`Core\Defs\HediffDefs\BodyParts\Hediffs_BodyParts_Archotech.xml:34`、`Core\Defs\HediffDefs\Hediffs_Local_Misc.xml:164`（forceRenderTreeRecache）、`:166`、`Core\Defs\HediffDefs\Hediffs_Local_Injuries.xml:14`、`Anomaly\Defs\TraitDefs\Traits.xml:54`；各 DefType 的出现率（GeneDef 6.9%、HediffDef 2.6%、MutantDef 25%、TraitDef 2.0%、ThingDef 0.1%）同样来自 `def-schema.json`。
- **待验证项**（本文件里已逐条标注）：①裸 `<root>` 不带 Class 的后果；②tagDef/skipFlag 写未定义名字的后果；③三套坐标写法的解析报错；④drawData 子元素名拼错的后果；⑤自造 nodeClass/workerClass/Class 的加载报错；⑥GraphicSet 在哪个版本被移除、是否还有回退路径。以上都只有原版正向写法证据，没有反向实验证据，故不做断言。