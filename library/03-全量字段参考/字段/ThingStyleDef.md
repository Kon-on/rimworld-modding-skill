# ThingStyleDef

- **所属线**：表现线
- **原版实例数**：126
- **字段路径数**：30
- **资料片**：Anomaly、Ideology、Royalty
- **原版出处**：`Ideology/Defs/ThingStyleDefs/ThingStyleDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<ThingStyleDef ParentName="IdeoColumnStyleBase">
    <defName>Morbid_Column</defName>
    <graphicData>
      <texPath>Things/Building/BuildingStyles/Morbid/MorbidColumn</texPath>
    </graphicData>
  </ThingStyleDef>

  
```

> 来自 `Ideology/Defs/ThingStyleDefs/ThingStyleDefs.xml`，defName = `Morbid_Column`，XML 节点数 4（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Horaxian_Axe / Horaxian_Gladius / Horaxian_Knife
graphicData                                    [容器]
graphicData/texPath                            [文本]  例：Things/Item/Equipment/WeaponMelee/HoraxianAxe / Things/Item/Equipment/WeaponMelee/HoraxianGladius / Things/Item/Equipment/WeaponMelee/HoraxianKnife
```

## 三、全量字段表（30 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 97.6% (123/126) | 文本 | Horaxian_Axe / Horaxian_Gladius / Horaxian_Knife |
| `graphicData` | 100.0% (126/126) | 容器 |  |
| `graphicData/damageData` | 6.3% (8/126) | 容器 |  |
| `graphicData/damageData/cornerBL` | 2.4% (3/126) | 文本 | Damage/Corner |
| `graphicData/damageData/cornerBR` | 2.4% (3/126) | 文本 | Damage/Corner |
| `graphicData/damageData/cornerTL` | 2.4% (3/126) | 文本 | Damage/Corner |
| `graphicData/damageData/cornerTR` | 2.4% (3/126) | 文本 | Damage/Corner |
| `graphicData/damageData/enabled` | 1.6% (2/126) | 布尔 | false |
| `graphicData/damageData/rect` | 1.6% (2/126) | 文本 | (0.2,0.2,0.6,0.6) |
| `graphicData/damageData/rectE` | 2.4% (3/126) | 文本 | (0.234375,0.296875,0.5,0.546875) / (0.28125,0.25,0.453125,0.25) |
| `graphicData/damageData/rectN` | 2.4% (3/126) | 文本 | (0.125,0.296875,0.734375,0.421875) / (0.25,0.234375,0.5,0.28125) |
| `graphicData/damageData/rectS` | 2.4% (3/126) | 文本 | (0.125,0.296875,0.734375,0.421875) / (0.25,0.234375,0.5,0.28125) |
| `graphicData/damageData/rectW` | 2.4% (3/126) | 文本 | (0.234375,0.296875,0.5,0.546875) / (0.28125,0.25,0.453125,0.25) |
| `graphicData/drawOffset` | 0.8% (1/126) | 文本 | (0,0,0.2) |
| `graphicData/drawOffsetEast` | 0.8% (1/126) | 文本 | (0.9,0,0) |
| `graphicData/drawOffsetNorth` | 0.8% (1/126) | 文本 | (0,0,0.9) |
| `graphicData/drawOffsetSouth` | 0.8% (1/126) | 文本 | (0,0,-0.9) |
| `graphicData/drawOffsetWest` | 0.8% (1/126) | 文本 | (-0.9,0,0) |
| `graphicData/drawSize` | 50.0% (63/126) | 数值/文本 | (0.75,1.25) / (3,3) / 0.8 |
| `graphicData/graphicClass` | 73.0% (92/126) | 文本 | Graphic_Multi / Graphic_Random / Graphic_Single |
| `graphicData/shaderType` | 1.6% (2/126) | 文本 | CutoutComplex |
| `graphicData/shadowData` | 10.3% (13/126) | 容器 |  |
| `graphicData/shadowData/offset` | 1.6% (2/126) | 文本 | (0, 0, -0.28) / (0,0,-0.23) |
| `graphicData/shadowData/volume` | 10.3% (13/126) | 文本 | (0.3, 0.5, 0.3) / (0.8, 1, 0.8) / (2.4, 1, 0.8) |
| `graphicData/texPath` | 97.6% (123/126) | 文本 | Things/Item/Equipment/WeaponMelee/HoraxianAxe / Things/Item/Equipment/WeaponMelee/HoraxianGladius / Things/Ite |
| `overrideLabel` | 0.8% (1/126) | 文本 | samurai helmet |
| `uiIconPath` | 11.1% (14/126) | 文本 | Things/Building/BuildingStyles/Morbid/MorbidTorchLamp_MenuIcon / Things/Building/BuildingStyles/Morbid/WallLam |
| `uiIconScale` | 11.1% (14/126) | 数值 | 1.14 / 1.23 / 1.6 |
| `useWornGraphicMask` | 0.8% (1/126) | 布尔 | true |
| `wornGraphicPath` | 21.4% (27/126) | 文本 | Things/Pawn/Humanlike/Apparel/Dreadmask/Dreadmask / Things/Pawn/Humanlike/Apparel/SpikedApex/SpikedApex / Thin |

## 四、原版 defName 一览（共 126 个，列出前 60）

```text
`Morbid_Column`                   `Totemic_Column`                  `Spikecore_Column`                `Rustic_Column`                 
`Techist_Column`                  `Horaxian_Axe`                    `Horaxian_Knife`                  `Horaxian_Gladius`              
`Horaxian_Mace`                   `Horaxian_Club`                   `Christian_SculptureSmall`        `Islamic_SculptureSmall`        
`Buddhist_SculptureSmall`         `Hindu_SculptureSmall`            `Morbid_SculptureSmall`           `Morbid_Table1x2c`              
`Morbid_Table2x2c`                `Morbid_Table2x4c`                `Morbid_Table3x3c`                `Morbid_StandingLamp`           
`Morbid_WallLamp`                 `Morbid_WallTorch`                `Totemic_SculptureSmall`          `Totemic_Table1x2c`             
`Totemic_Table2x2c`               `Totemic_Table2x4c`               `Totemic_Table3x3c`               `Totemic_StandingLamp`          
`Totemic_WallLamp`                `Totemic_WallTorch`               `Spikecore_Table1x2c`             `Spikecore_Table2x2c`           
`Spikecore_Table2x4c`             `Spikecore_Table3x3c`             `Spikecore_StandingLamp`          `Spikecore_WallLamp`            
`Spikecore_WallTorch`             `Rustic_StandingLamp`             `Rustic_WallLamp`                 `Rustic_WallTorch`              
`Rustic_Table1x2c`                `Rustic_Table2x2c`                `Rustic_Table2x4c`                `Rustic_Table3x3c`              
`Animalist_SculptureSmall`        `Techist_StandingLamp`            `Techist_WallLamp`                `Techist_Table1x2c`             
`Techist_Table2x2c`               `Techist_Table2x4c`               `Techist_Table3x3c`               `Christian_IdeogramA`           
`Christian_IdeogramB`             `Islamic_IdeogramA`               `Islamic_IdeogramB`               `Buddhist_IdeogramA`            
`Buddhist_IdeogramB`              `Hindu_SimpleHelmet`              `Hindu_AdvancedHelmet`            `Hindu_IdeogramA`               
```

_余下 66 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
