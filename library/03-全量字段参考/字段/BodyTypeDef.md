# BodyTypeDef

- **所属线**：人物线
- **原版实例数**：8
- **字段路径数**：26
- **资料片**：Biotech、Core
- **原版出处**：`Biotech/Defs/Misc/BodyTypeDefs/BodyTypes.xml`、`Core/Defs/Misc/BodyTypeDefs/BodyTypes.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<BodyTypeDef Abstract="True" Name="Juvenile">
    <headOffset>(0.04, 0.34)</headOffset>
    <bedOffset>-0.08</bedOffset>
    <bodyNakedGraphicPath>Things/Pawn/Humanlike/Bodies/Naked_Child</bodyNakedGraphicPath>
    <bodyDessicatedGraphicPath>Things/Pawn/Humanlike/Bodies/Dessicated/Dessicated_Child</bodyDessicatedGraphicPath>
  </BodyTypeDef>
  
  
```

> 来自 `Biotech/Defs/Misc/BodyTypeDefs/BodyTypes.xml`，defName = ``，XML 节点数 5（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
attachPoints/li                                [容器]
attachPoints/li/offset                         [文本]  例：(-.1, 0, -.2) / (-.1, 0, .25) / (.1, 0, -.2)
attachPoints/li/type                           [文本]  例：PlatformRestraint0 / PlatformRestraint1 / PlatformRestraint2
attachPointsDessicated/li                      [容器]
attachPointsDessicated/li/offset               [文本]  例：(-.1, 0, -.2) / (-.1, 0, .25) / (.1, 0, -.2)
attachPointsDessicated/li/type                 [文本]  例：PlatformRestraint0 / PlatformRestraint1 / PlatformRestraint2
woundAnchors/li                                [容器]
woundAnchors/li/canMirror                      [布尔]  例：false
woundAnchors/li/debugColor                     [文本]  例：(0,0,0,1) / (0,0,1,1) / (1,0,1,1)
woundAnchors/li/group                          [文本]  例：FullHead / Torso
woundAnchors/li/layer                          [文本]  例：Head
woundAnchors/li/narrowCrown                    [布尔]  例：true
woundAnchors/li/offset                         [文本]  例：(-0.008, 0, 0.19) / (-0.06, 0, 0.2) / (0.008, 0, 0.19)
woundAnchors/li/range                          [数值]  例：0 / 0.03 / 0.06
woundAnchors/li/rotation                       [文本]  例：East / South / West
woundAnchors/li/tag                            [文本]  例：LeftEye / RightEye / RightLeg
```

## 三、全量字段表（26 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `attachPoints` | 87.5% (7/8) | 容器 |  |
| `attachPoints/li` | 350.0% (28/8) | 容器 |  |
| `attachPoints/li/offset` | 350.0% (28/8) | 文本 | (-.1, 0, -.2) / (-.1, 0, .25) / (.1, 0, -.2) |
| `attachPoints/li/type` | 350.0% (28/8) | 文本 | PlatformRestraint0 / PlatformRestraint1 / PlatformRestraint2 |
| `attachPointsDessicated` | 75.0% (6/8) | 容器 |  |
| `attachPointsDessicated/li` | 300.0% (24/8) | 容器 |  |
| `attachPointsDessicated/li/offset` | 300.0% (24/8) | 文本 | (-.1, 0, -.2) / (-.1, 0, .25) / (.1, 0, -.2) |
| `attachPointsDessicated/li/type` | 300.0% (24/8) | 文本 | PlatformRestraint0 / PlatformRestraint1 / PlatformRestraint2 |
| `bedOffset` | 12.5% (1/8) | 数值 | -0.08 |
| `bodyDessicatedGraphicPath` | 75.0% (6/8) | 文本 | Things/Pawn/Humanlike/Bodies/Dessicated/Dessicated_Child / Things/Pawn/Humanlike/Bodies/Dessicated/Dessicated_ |
| `bodyGraphicScale` | 87.5% (7/8) | 文本 | (0.5, 0.5) / (0.6, 0.65) / (1, 0.9) |
| `bodyNakedGraphicPath` | 75.0% (6/8) | 文本 | Things/Pawn/Humanlike/Bodies/Naked_Child / Things/Pawn/Humanlike/Bodies/Naked_Female / Things/Pawn/Humanlike/B |
| `defName` | 87.5% (7/8) | 文本 | Baby / Child / Female |
| `headOffset` | 75.0% (6/8) | 文本 | (0.04, 0.34) / (0.09, 0.34) / (0.10, 0.34) |
| `woundAnchors` | 87.5% (7/8) | 容器 |  |
| `woundAnchors/li` | 1575.0% (126/8) | 容器 |  |
| `woundAnchors/li/canMirror` | 875.0% (70/8) | 布尔 | false |
| `woundAnchors/li/debugColor` | 1575.0% (126/8) | 文本 | (0,0,0,1) / (0,0,1,1) / (1,0,1,1) |
| `woundAnchors/li/group` | 350.0% (28/8) | 文本 | FullHead / Torso |
| `woundAnchors/li/layer` | 700.0% (56/8) | 文本 | Head |
| `woundAnchors/li/narrowCrown` | 175.0% (14/8) | 布尔 | true |
| `woundAnchors/li/offset` | 1575.0% (126/8) | 文本 | (-0.008, 0, 0.19) / (-0.06, 0, 0.2) / (0.008, 0, 0.19) |
| `woundAnchors/li/range` | 1575.0% (126/8) | 数值 | 0 / 0.03 / 0.06 |
| `woundAnchors/li/rotation` | 1575.0% (126/8) | 文本 | East / South / West |
| `woundAnchors/li/tag` | 1225.0% (98/8) | 文本 | LeftEye / RightEye / RightLeg |
| `woundScale` | 25.0% (2/8) | 数值 | 0.5 / 0.7 |

## 四、原版 defName 一览（共 8 个，列出前 60）

```text
``                                `Hulk`                            `Baby`                            `Child`                         
`Male`                            `Female`                          `Thin`                            `Fat`                           
```
