# PawnRenderTreeDef

- **所属线**：表现线
- **原版实例数**：11
- **字段路径数**：72
- **资料片**：Anomaly、Core
- **原版出处**：`Core/Defs/PawnRenderTreeDefs/PawnRenderTreeDefs.xml`、`Anomaly/Defs/PawnRenderTreeDefs/PawnRenderTreeDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<PawnRenderTreeDef>
    <defName>Misc</defName>
    <root Class="PawnRenderNodeProperties_Parent">
      <debugLabel>Root</debugLabel>
      <tagDef>Root</tagDef>
      <children>
        <li>
          <debugLabel>Body</debugLabel>
          <tagDef>Body</tagDef>
          <nodeClass>PawnRenderNode_AnimalPart</nodeClass>
          <useRottenColor>true</useRottenColor>
          <children>
            <li>
              <debugLabel>Wounds</debugLabel>
              <nodeClass>PawnRenderNode_AnimalPart</nodeClass>
              <workerClass>PawnRenderNodeWorker_OverlayWounds</workerClass>
              <overlayLayer>Body</overlayLayer>
              <useGraphic>false</useGraphic>
              <baseLayer>3</baseLayer>
            </li>
            <li>
              <debugLabel>Firefoam</debugLabel>
              <nodeClass>PawnRenderNode_AnimalPart</nodeClass>
              <workerClass>PawnRenderNodeWorker_OverlayFirefoam</workerClass>
              <overlayLayer>Body</overlayLayer>
              <useGraphic>false</useGraphic>
              <baseLayer>5</baseLayer>
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
```

> 来自 `Core/Defs/PawnRenderTreeDefs/PawnRenderTreeDefs.xml`，defName = `Misc`，XML 节点数 29（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Bulbfreak / Fingerspike / Toughspike
root                                           [容器]
root/children                                  [容器]
root/children/li                               [容器]
root/children/li/children                      [容器]
root/children/li/children/li                   [容器]
root/children/li/children/li/baseLayer         [数值]  例：0 / 10 / 20
root/children/li/children/li/children          [容器]
root/children/li/children/li/children/li       [容器]
root/children/li/children/li/children/li/texPath [文本]  例：Things/Pawn/Nociosphere/Shell/Nociosphere_ShellK_Outline / Things/Pawn/Nociosphere/Shell/Nociosphere_ShellL_Outline / Things/Pawn/Nociosphere/Shell/Nociosphere_ShellM_Outline
root/children/li/children/li/debugLabel        [文本]  例：Firefoam / TentacleI / TentacleJ
root/children/li/children/li/drawData          [容器]
root/children/li/children/li/drawData/dataEast [容器]
root/children/li/children/li/drawData/dataEast/offset [文本]  例：(0.05, 0, 0.36) / (0.1, 0, 0.3) / (0.1, 0, 0.4)
root/children/li/children/li/drawData/dataNorth [容器]
root/children/li/children/li/drawData/dataNorth/offset [文本]  例：(-0.05, 0, 1.15) / (-0.35, 0, 1.2) / (-0.5, 0, 1.03)
root/children/li/children/li/drawData/dataSouth [容器]
root/children/li/children/li/drawData/dataSouth/layer [数值]  例：10 / 14 / 15
root/children/li/children/li/drawData/dataSouth/offset [文本]  例：(-0.05, 0, -0.18) / (0.1, 0, -0.15) / (0.35, 0, -0.2)
root/children/li/children/li/drawData/dataSouth/rotationOffset [数值]  例：-60 / 180 / 35
root/children/li/children/li/drawData/dataWest [容器]
root/children/li/children/li/drawData/dataWest/flip [布尔]  例：true
root/children/li/children/li/drawData/defaultData [容器]
root/children/li/children/li/drawData/defaultData/layer [数值]  例：-10 / -2 / -7
root/children/li/children/li/drawData/defaultData/pivot [文本]  例：(0.5, 0.95)
root/children/li/children/li/drawSize          [数值]  例：1.05 / 1.1 / 1.2
root/children/li/children/li/durationTicksRange [文本]  例：10~35 / 10~60 / 15~45
root/children/li/children/li/linkedBodyPartsGroup [文本]  例：FifthTentacle / FourthTentacle / SecondTentacle
root/children/li/children/li/maskPath          [文本]  例：Things/Pawn/Nociosphere/Shell/Nociosphere_ShellJ_Mask / Things/Pawn/Nociosphere/Shell/Nociosphere_ShellK_Mask / Things/Pawn/Nociosphere/Shell/Nociosphere_ShellL_Mask
root/children/li/children/li/nextSpasmTicksRange [文本]  例：10~50 / 20~60 / 5~30
root/children/li/children/li/nodeClass         [文本]  例：PawnRenderNode_AnimalPart / PawnRenderNode_Beard / PawnRenderNode_Hair
root/children/li/children/li/offset            [文本]  例：-0.25,-1.65 / 0,-1.75 / 0.25,-1.65
root/children/li/children/li/overlayLayer      [文本]  例：Body / Head
root/children/li/children/li/rotateFacing      [布尔]  例：false
root/children/li/children/li/rotationRange     [文本]  例：-18~18 / -25~25 / -30~30
root/children/li/children/li/rotDrawMode       [文本]  例：Fresh, Rotting
root/children/li/children/li/texPath           [文本]  例：Things/Pawn/Fleshbeast/Bulbfreak/Tentacles/BulbfreakTentacleA / Things/Pawn/Fleshbeast/Bulbfreak/Tentacles/BulbfreakTentacleB / Things/Pawn/Fleshbeast/Bulbfreak/Tentacles/BulbfreakTentacleC
root/children/li/children/li/useGraphic        [布尔]  例：false
root/children/li/children/li/useRottenColor    [布尔]  例：true
root/children/li/children/li/workerClass       [文本]  例：PawnRenderNodeWorker_FlipWhenCrawling / PawnRenderNodeWorker_OverlayFirefoam / PawnRenderNodeWorker_OverlayStatus
root/children/li/debugLabel                    [文本]  例：Body / Carried thing / Head
root/children/li/nodeClass                     [文本]  例：PawnRenderNode_AnimalPart / PawnRenderNode_Devourer / PawnRenderNode_Head
root/children/li/tagDef                        [文本]  例：Body / Head
root/children/li/useRottenColor                [布尔]  例：true
root/children/li/workerClass                   [文本]  例：PawnRenderNodeWorker_AnimalBody / PawnRenderNodeWorker_Carried / PawnRenderNodeWorker_Head
root/debugLabel                                [文本]  例：Root
root/tagDef                                    [文本]  例：Root
```

## 三、全量字段表（72 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (11/11) | 文本 | Bulbfreak / Fingerspike / Toughspike |
| `root` | 100.0% (11/11) | 容器 |  |
| `root/children` | 100.0% (11/11) | 容器 |  |
| `root/children/li` | 209.1% (23/11) | 容器 |  |
| `root/children/li/baseLayer` | 18.2% (2/11) | 数值 | 50 |
| `root/children/li/children` | 109.1% (12/11) | 容器 |  |
| `root/children/li/children/li` | 654.5% (72/11) | 容器 |  |
| `root/children/li/children/li/baseLayer` | 518.2% (57/11) | 数值 | 0 / 10 / 20 |
| `root/children/li/children/li/brightnessRange` | 9.1% (1/11) | 文本 | 0.6~0.89 |
| `root/children/li/children/li/children` | 127.3% (14/11) | 容器 |  |
| `root/children/li/children/li/children/li` | 127.3% (14/11) | 容器 |  |
| `root/children/li/children/li/children/li/texPath` | 127.3% (14/11) | 文本 | Things/Pawn/Nociosphere/Shell/Nociosphere_ShellK_Outline / Things/Pawn/Nociosphere/Shell/Nociosphere_ShellL_Ou |
| `root/children/li/children/li/colorType` | 36.4% (4/11) | 文本 | Hair / Skin |
| `root/children/li/children/li/debugLabel` | 654.5% (72/11) | 文本 | Firefoam / TentacleI / TentacleJ |
| `root/children/li/children/li/drawData` | 245.4% (27/11) | 容器 |  |
| `root/children/li/children/li/drawData/dataEast` | 190.9% (21/11) | 容器 |  |
| `root/children/li/children/li/drawData/dataEast/layer` | 36.4% (4/11) | 数值 | -5 |
| `root/children/li/children/li/drawData/dataEast/offset` | 172.7% (19/11) | 文本 | (0.05, 0, 0.36) / (0.1, 0, 0.3) / (0.1, 0, 0.4) |
| `root/children/li/children/li/drawData/dataEast/rotationOffset` | 36.4% (4/11) | 数值 | 245 / 41 / 91 |
| `root/children/li/children/li/drawData/dataNorth` | 245.4% (27/11) | 容器 |  |
| `root/children/li/children/li/drawData/dataNorth/flip` | 9.1% (1/11) | 布尔 | true |
| `root/children/li/children/li/drawData/dataNorth/layer` | 72.7% (8/11) | 数值 | -5 / 10 / 14 |
| `root/children/li/children/li/drawData/dataNorth/offset` | 218.2% (24/11) | 文本 | (-0.05, 0, 1.15) / (-0.35, 0, 1.2) / (-0.5, 0, 1.03) |
| `root/children/li/children/li/drawData/dataNorth/rotationOffset` | 81.8% (9/11) | 数值 | -20 / -45 / 160 |
| `root/children/li/children/li/drawData/dataSouth` | 200.0% (22/11) | 容器 |  |
| `root/children/li/children/li/drawData/dataSouth/flip` | 36.4% (4/11) | 布尔 | true |
| `root/children/li/children/li/drawData/dataSouth/layer` | 90.9% (10/11) | 数值 | 10 / 14 / 15 |
| `root/children/li/children/li/drawData/dataSouth/offset` | 190.9% (21/11) | 文本 | (-0.05, 0, -0.18) / (0.1, 0, -0.15) / (0.35, 0, -0.2) |
| `root/children/li/children/li/drawData/dataSouth/rotationOffset` | 100.0% (11/11) | 数值 | -60 / 180 / 35 |
| `root/children/li/children/li/drawData/dataWest` | 154.6% (17/11) | 容器 |  |
| `root/children/li/children/li/drawData/dataWest/flip` | 100.0% (11/11) | 布尔 | true |
| `root/children/li/children/li/drawData/dataWest/layer` | 27.3% (3/11) | 数值 | -5 |
| `root/children/li/children/li/drawData/dataWest/offset` | 81.8% (9/11) | 文本 | (0, 0, 0.1) / (0, 0, 0.15) / (0.95, 0, 0.4) |
| `root/children/li/children/li/drawData/dataWest/rotationOffset` | 36.4% (4/11) | 数值 | -245 / -41 / -91 |
| `root/children/li/children/li/drawData/defaultData` | 145.4% (16/11) | 容器 |  |
| `root/children/li/children/li/drawData/defaultData/flip` | 63.6% (7/11) | 布尔 | true |
| `root/children/li/children/li/drawData/defaultData/layer` | 136.4% (15/11) | 数值 | -10 / -2 / -7 |
| `root/children/li/children/li/drawData/defaultData/offset` | 9.1% (1/11) | 文本 | (0, 0, 0.3) |
| `root/children/li/children/li/drawData/defaultData/pivot` | 136.4% (15/11) | 文本 | (0.5, 0.95) |
| `root/children/li/children/li/drawData/defaultData/rotationOffset` | 45.5% (5/11) | 数值 | 180 |
| `root/children/li/children/li/drawSize` | 209.1% (23/11) | 数值 | 1.05 / 1.1 / 1.2 |
| `root/children/li/children/li/durationTicksRange` | 100.0% (11/11) | 文本 | 10~35 / 10~60 / 15~45 |
| `root/children/li/children/li/linkedBodyPartsGroup` | 209.1% (23/11) | 文本 | FifthTentacle / FourthTentacle / SecondTentacle |
| `root/children/li/children/li/maskPath` | 118.2% (13/11) | 文本 | Things/Pawn/Nociosphere/Shell/Nociosphere_ShellJ_Mask / Things/Pawn/Nociosphere/Shell/Nociosphere_ShellK_Mask  |
| `root/children/li/children/li/nextSpasmTicksRange` | 100.0% (11/11) | 文本 | 10~50 / 20~60 / 5~30 |
| `root/children/li/children/li/nodeClass` | 209.1% (23/11) | 文本 | PawnRenderNode_AnimalPart / PawnRenderNode_Beard / PawnRenderNode_Hair |
| `root/children/li/children/li/offset` | 127.3% (14/11) | 文本 | -0.25,-1.65 / 0,-1.75 / 0.25,-1.65 |
| `root/children/li/children/li/overlayLayer` | 200.0% (22/11) | 文本 | Body / Head |
| `root/children/li/children/li/overlayOverApparel` | 9.1% (1/11) | 布尔 | true |
| `root/children/li/children/li/rotateFacing` | 100.0% (11/11) | 布尔 | false |
| `root/children/li/children/li/rotationRange` | 100.0% (11/11) | 文本 | -18~18 / -25~25 / -30~30 |
| `root/children/li/children/li/rotDrawMode` | 145.4% (16/11) | 文本 | Fresh, Rotting |
| `root/children/li/children/li/scaleRange` | 63.6% (7/11) | 文本 | 0.95~1.05 / 0.9~1.1 |
| `root/children/li/children/li/skipFlag` | 18.2% (2/11) | 文本 | Beard / Hair |
| `root/children/li/children/li/swaddleColorOffset` | 9.1% (1/11) | 数值 | 0.1 |
| `root/children/li/children/li/tagDef` | 27.3% (3/11) | 文本 | ApparelBody / ApparelHead / Head |
| `root/children/li/children/li/texPath` | 381.8% (42/11) | 文本 | Things/Pawn/Fleshbeast/Bulbfreak/Tentacles/BulbfreakTentacleA / Things/Pawn/Fleshbeast/Bulbfreak/Tentacles/Bul |
| `root/children/li/children/li/useGraphic` | 136.4% (15/11) | 布尔 | false |
| `root/children/li/children/li/useRottenColor` | 254.6% (28/11) | 布尔 | true |
| `root/children/li/children/li/workerClass` | 263.6% (29/11) | 文本 | PawnRenderNodeWorker_FlipWhenCrawling / PawnRenderNodeWorker_OverlayFirefoam / PawnRenderNodeWorker_OverlaySta |
| `root/children/li/colorType` | 27.3% (3/11) | 文本 | Skin |
| `root/children/li/debugLabel` | 209.1% (23/11) | 文本 | Body / Carried thing / Head |
| `root/children/li/nodeClass` | 118.2% (13/11) | 文本 | PawnRenderNode_AnimalPart / PawnRenderNode_Devourer / PawnRenderNode_Head |
| `root/children/li/rotDrawMode` | 9.1% (1/11) | 文本 | Fresh, Rotting |
| `root/children/li/skipFlag` | 27.3% (3/11) | 文本 | Body / Head |
| `root/children/li/tagDef` | 109.1% (12/11) | 文本 | Body / Head |
| `root/children/li/texPath` | 9.1% (1/11) | 文本 | Things/Pawn/Humanlike/Heads/None_Average_Stump |
| `root/children/li/useRottenColor` | 109.1% (12/11) | 布尔 | true |
| `root/children/li/useSkinShader` | 27.3% (3/11) | 布尔 | true |
| `root/children/li/workerClass` | 136.4% (15/11) | 文本 | PawnRenderNodeWorker_AnimalBody / PawnRenderNodeWorker_Carried / PawnRenderNodeWorker_Head |
| `root/debugLabel` | 100.0% (11/11) | 文本 | Root |
| `root/tagDef` | 100.0% (11/11) | 文本 | Root |

## 四、原版 defName 一览（共 11 个，列出前 60）

```text
`Misc`                            `Devourer`                        `Animal`                          `Revenant`                      
`Fingerspike`                     `Toughspike`                      `Trispike`                        `Humanlike`                     
`Nociosphere`                     `Bulbfreak`                       `Dreadmeld`                     
```
