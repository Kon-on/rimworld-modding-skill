# SketchResolverDef

- **所属线**：世界线
- **原版实例数**：33
- **字段路径数**：3
- **资料片**：Biotech、Core、Ideology、Odyssey、Royalty
- **原版出处**：`Core/Defs/SketchResolverDefs/SketchResolvers.xml`、`Biotech/Defs/SketchResolverDefs/SketchResolvers.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<SketchResolverDef>
    <defName>Symmetry</defName>
    <resolver Class="SketchResolver_Symmetry"/>
  </SketchResolverDef>

  
```

> 来自 `Core/Defs/SketchResolverDefs/SketchResolvers.xml`，defName = `Symmetry`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：AncientBandNodeRoom / AncientMechGeneratorRoom / AncientMechGestatorRoom
resolver                                       [容器]
```

## 三、全量字段表（3 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (33/33) | 文本 | AncientBandNodeRoom / AncientMechGeneratorRoom / AncientMechGestatorRoom |
| `isRoot` | 54.5% (18/33) | 布尔 | true |
| `resolver` | 100.0% (33/33) | 容器 |  |

## 四、原版 defName 一览（共 33 个，列出前 60）

```text
`Symmetry`                        `AssignRandomStuff`               `FloorFill`                       `AddColumns`                    
`AddCornerThings`                 `AddThingsCentral`                `AddWallEdgeThings`               `AddInnerMonuments`             
`DamageBuildingsLight`            `DamageBuildings`                 `AncientConcretePad`              `CerebrexCore`                  
`MechhiveLaunchPad`               `MechhiveProcessorArray`          `MechhiveGuardOutpost`            `AncientRechargeRoom`           
`AncientMechGestatorRoom`         `AncientMechGeneratorRoom`        `AncientBandNodeRoom`             `Monument`                      
`MonumentRuin`                    `AncientBarracks`                 `AncientStorageRoom`              `AncientEquipmentRoom`          
`AncientPowerRoom`                `AncientLab`                      `AncientArmory`                   `AncientUtilityBuilding`        
`AncientLandingPad`               `AncientHatch`                    `Gravship`                        `MechCluster`                   
`MechClusterWalls`              
```
