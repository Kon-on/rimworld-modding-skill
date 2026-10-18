# FleshTypeDef

- **所属线**：人物线
- **原版实例数**：7
- **字段路径数**：32
- **资料片**：Anomaly、Core、Odyssey
- **原版出处**：`Anomaly/Defs/Misc/FleshTypeDefs/FleshType.xml`、`Core/Defs/Misc/FleshTypeDefs/FleshType.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<FleshTypeDef>
    <defName>EntityMechanical</defName>
    <corpseCategory>CorpsesEntity</corpseCategory>
    <damageEffecter>Damage_HitMechanoid</damageEffecter>
    <isOrganic>false</isOrganic>
    <genericWounds>
      <li>
        <texture>Things/Pawn/Wounds/WoundMechA</texture>
      </li>
      <li>
        <texture>Things/Pawn/Wounds/WoundMechB</texture>
      </li>
      <li>
        <texture>Things/Pawn/Wounds/WoundMechC</texture>
      </li>
    </genericWounds>
  </FleshTypeDef>

  
```

> 来自 `Anomaly/Defs/Misc/FleshTypeDefs/FleshType.xml`，defName = `EntityMechanical`，XML 节点数 12（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
corpseCategory                                 [文本]  例：CorpsesAnimal / CorpsesEntity / CorpsesInsect
damageEffecter                                 [文本]  例：Damage_HitFlesh / Damage_HitInsect / Damage_HitMechanoid
defName                                        [文本]  例：EntityFlesh / EntityMechanical / Fleshbeast
genericWounds                                  [容器]
genericWounds/li                               [容器]
genericWounds/li/texture                       [文本]  例：Things/Pawn/Wounds/WoundFleshC / Things/Pawn/Wounds/WoundMechA / Things/Pawn/Wounds/WoundMechB
hediffWounds/li/wounds/li                      [容器]
hediffWounds/li/wounds/li/displayOverApparel   [布尔]  例：false / true
hediffWounds/li/wounds/li/displayPermanent     [布尔]  例：false
hediffWounds/li/wounds/li/drawOffsetEastWest   [文本]  例：(-0.03, 0.001, -0.24) / (0, -0.001, -0.24)
hediffWounds/li/wounds/li/drawOffsetSouth      [文本]  例：(0, -0.001, -0.24) / (0, 0.001, -0.24)
hediffWounds/li/wounds/li/texture              [文本]  例：Things/Pawn/Wounds/PorcupineQuillA / Things/Pawn/Wounds/PorcupineQuillB / Things/Pawn/Wounds/PorcupineQuillC
hediffWounds/li/wounds/li/tintWithSkinColor    [布尔]  例：false / true
isOrganic                                      [布尔]  例：false / true
```

## 三、全量字段表（32 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `bandagedWounds` | 14.3% (1/7) | 容器 |  |
| `bandagedWounds/li` | 42.9% (3/7) | 容器 |  |
| `bandagedWounds/li/texture` | 42.9% (3/7) | 文本 | Things/Pawn/Wounds/BandagedA / Things/Pawn/Wounds/BandagedB / Things/Pawn/Wounds/BandagedC |
| `corpseCategory` | 100.0% (7/7) | 文本 | CorpsesAnimal / CorpsesEntity / CorpsesInsect |
| `damageEffecter` | 100.0% (7/7) | 文本 | Damage_HitFlesh / Damage_HitInsect / Damage_HitMechanoid |
| `defName` | 100.0% (7/7) | 文本 | EntityFlesh / EntityMechanical / Fleshbeast |
| `genericWounds` | 100.0% (7/7) | 容器 |  |
| `genericWounds/li` | 300.0% (21/7) | 容器 |  |
| `genericWounds/li/color` | 42.9% (3/7) | 文本 | 0.23,0.20,0.17 |
| `genericWounds/li/texture` | 300.0% (21/7) | 文本 | Things/Pawn/Wounds/WoundFleshC / Things/Pawn/Wounds/WoundMechA / Things/Pawn/Wounds/WoundMechB |
| `hediffWounds` | 14.3% (1/7) | 容器 |  |
| `hediffWounds/li` | 42.9% (3/7) | 容器 |  |
| `hediffWounds/li/hediff` | 42.9% (3/7) | 文本 | MissingBodyPart / PorcupineQuill / Scarification |
| `hediffWounds/li/wounds` | 42.9% (3/7) | 容器 |  |
| `hediffWounds/li/wounds/li` | 128.6% (9/7) | 容器 |  |
| `hediffWounds/li/wounds/li/displayOverApparel` | 100.0% (7/7) | 布尔 | false / true |
| `hediffWounds/li/wounds/li/displayPermanent` | 100.0% (7/7) | 布尔 | false |
| `hediffWounds/li/wounds/li/drawOffsetEastWest` | 128.6% (9/7) | 文本 | (-0.03, 0.001, -0.24) / (0, -0.001, -0.24) |
| `hediffWounds/li/wounds/li/drawOffsetSouth` | 128.6% (9/7) | 文本 | (0, -0.001, -0.24) / (0, 0.001, -0.24) |
| `hediffWounds/li/wounds/li/flipOnRotation` | 28.6% (2/7) | 文本 | South |
| `hediffWounds/li/wounds/li/flipOnWoundAnchorTag` | 28.6% (2/7) | 文本 | LeftEye |
| `hediffWounds/li/wounds/li/flipWest` | 28.6% (2/7) | 布尔 | true |
| `hediffWounds/li/wounds/li/missingBodyPartFresh` | 28.6% (2/7) | 布尔 | false / true |
| `hediffWounds/li/wounds/li/onlyOnPart` | 28.6% (2/7) | 文本 | Eye |
| `hediffWounds/li/wounds/li/scale` | 28.6% (2/7) | 数值 | 0.7 |
| `hediffWounds/li/wounds/li/texture` | 100.0% (7/7) | 文本 | Things/Pawn/Wounds/PorcupineQuillA / Things/Pawn/Wounds/PorcupineQuillB / Things/Pawn/Wounds/PorcupineQuillC |
| `hediffWounds/li/wounds/li/textureEast` | 28.6% (2/7) | 文本 | Things/Pawn/Wounds/MissingEye_Fresh / Things/Pawn/Wounds/MissingEye_Scar_east |
| `hediffWounds/li/wounds/li/textureNorth` | 28.6% (2/7) | 文本 | Things/Pawn/Wounds/MissingEye_Fresh / Things/Pawn/Wounds/MissingEye_Scar_south |
| `hediffWounds/li/wounds/li/textureSouth` | 28.6% (2/7) | 文本 | Things/Pawn/Wounds/MissingEye_Fresh / Things/Pawn/Wounds/MissingEye_Scar_south |
| `hediffWounds/li/wounds/li/textureWest` | 28.6% (2/7) | 文本 | Things/Pawn/Wounds/MissingEye_Fresh / Things/Pawn/Wounds/MissingEye_Scar_east |
| `hediffWounds/li/wounds/li/tintWithSkinColor` | 114.3% (8/7) | 布尔 | false / true |
| `isOrganic` | 100.0% (7/7) | 布尔 | false / true |

## 四、原版 defName 一览（共 7 个，列出前 60）

```text
`EntityMechanical`                `EntityFlesh`                     `Fleshbeast`                      `Mechanoid`                     
`Drone`                           `Insectoid`                       `Normal`                        
```
