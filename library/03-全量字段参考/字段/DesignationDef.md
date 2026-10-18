# DesignationDef

- **所属线**：系统线
- **原版实例数**：27
- **字段路径数**：6
- **资料片**：Core
- **原版出处**：`Core/Defs/Misc/Designations/Designations.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<DesignationDef>
    <defName>Haul</defName>
    <texturePath>Designations/Haul</texturePath>
    <targetType>Thing</targetType>
  </DesignationDef>

  
```

> 来自 `Core/Defs/Misc/Designations/Designations.xml`，defName = `Haul`，XML 节点数 4（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Haul / Mine / MineVein
targetType                                     [文本]  例：Cell / Thing
texturePath                                    [文本]  例：Designations/Haul / Designations/Mine / Designations/MineVein
```

## 三、全量字段表（6 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (27/27) | 文本 | Haul / Mine / MineVein |
| `designateCancelable` | 3.7% (1/27) | 布尔 | false |
| `removeIfBuildingDespawned` | 11.1% (3/27) | 布尔 | true |
| `shouldBatchDraw` | 3.7% (1/27) | 布尔 | false |
| `targetType` | 100.0% (27/27) | 文本 | Cell / Thing |
| `texturePath` | 100.0% (27/27) | 文本 | Designations/Haul / Designations/Mine / Designations/MineVein |

## 四、原版 defName 一览（共 27 个，列出前 60）

```text
`Haul`                            `Deconstruct`                     `Uninstall`                       `ExtractTree`                   
`CutPlant`                        `HarvestPlant`                    `Hunt`                            `SmoothFloor`                   
`SmoothWall`                      `PaintBuilding`                   `RemovePaintBuilding`             `RemovePaintFloor`              
`RemoveFloor`                     `RemoveFoundation`                `Strip`                           `Slaughter`                     
`Tame`                            `Open`                            `EjectFuel`                       `ReleaseAnimalToWild`           
`ExtractSkull`                    `FillIn`                          `Mine`                            `MineVein`                      
`PaintFloor`                      `Flick`                           `Plan`                          
```
