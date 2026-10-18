# RitualVisualEffectDef

- **所属线**：理念线
- **原版实例数**：20
- **字段路径数**：39
- **资料片**：Core、Ideology
- **原版出处**：`Ideology/Defs/Rituals/Ritual_VisualEffects.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<RitualVisualEffectDef ParentName="RitualGlowAbstract">
    <defName>Basic</defName>
    <tintColor>(100, 165, 255)</tintColor>
  </RitualVisualEffectDef>
  
  
```

> 来自 `Ideology/Defs/Rituals/Ritual_VisualEffects.xml`，defName = `Basic`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
comps/li                                       [容器]
defName                                        [文本]  例：Basic / Hindu / Islamic
```

## 三、全量字段表（39 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `comps` | 85.0% (17/20) | 容器 |  |
| `comps/li` | 120.0% (24/20) | 容器 |  |
| `comps/li/area` | 35.0% (7/20) | 文本 | (24, 22) / (27, 28) / (5, 6) |
| `comps/li/colorOverride` | 5.0% (1/20) | 文本 | (255, 255, 255, 255) |
| `comps/li/compClass` | 50.0% (10/20) | 文本 | CompRitualEffect_ConstantCenter / CompRitualEffect_SpawnOnOrganizer |
| `comps/li/concentration` | 5.0% (1/20) | 数值 | 3 |
| `comps/li/delay` | 10.0% (2/20) | 数值 | 34 |
| `comps/li/eastRotationOffset` | 5.0% (1/20) | 文本 | (0.5, 0, 0.2) |
| `comps/li/effecterDef` | 15.0% (3/20) | 文本 | Damage_HitFleshGruesome / SpikecoreSparks |
| `comps/li/fleckDef` | 45.0% (9/20) | 文本 | BlurrySpark / Bokeh / Skull |
| `comps/li/maxBursts` | 10.0% (2/20) | 数值 | 1 |
| `comps/li/maxDistance` | 5.0% (1/20) | 数值 | 12 |
| `comps/li/maxOffset` | 5.0% (1/20) | 数值 | 0.4 |
| `comps/li/minDist` | 5.0% (1/20) | 数值 | 2 |
| `comps/li/moteDef` | 55.0% (11/20) | 文本 | Mote_RitualGlowRays / Mote_RitualSmoke / Mote_RitualSmokeThick |
| `comps/li/moteDefs` | 5.0% (1/20) | 容器 |  |
| `comps/li/moteDefs/li` | 15.0% (3/20) | 文本 | Mote_RitualTechLineA / Mote_RitualTechLineB / Mote_RitualTechLineC |
| `comps/li/northRotationOffset` | 5.0% (1/20) | 文本 | (0, 0, 0.5) |
| `comps/li/numCopies` | 15.0% (3/20) | 数值 | 5 |
| `comps/li/offset` | 35.0% (7/20) | 文本 | (-5, 0, 0) / (-6, 0, 4) / (0, 0, 0.5) |
| `comps/li/onlySpawnInSameRoom` | 35.0% (7/20) | 布尔 | true |
| `comps/li/overrideColors` | 10.0% (2/20) | 容器 |  |
| `comps/li/overrideColors/li` | 30.0% (6/20) | 文本 | (158, 235, 95) / (183, 248, 114) / (199, 233, 79) |
| `comps/li/radius` | 25.0% (5/20) | 数值 | 3 / 6 / 7.0 |
| `comps/li/requiredTag` | 5.0% (1/20) | 文本 | Arrived |
| `comps/li/roleId` | 10.0% (2/20) | 文本 | animal / prisoner |
| `comps/li/roomCheckOffset` | 10.0% (2/20) | 文本 | (0, 0, -1) |
| `comps/li/rotation` | 20.0% (4/20) | 文本 | -15~15 / -35~35 / -5~75 |
| `comps/li/rotationRate` | 5.0% (1/20) | 数值 | 100 |
| `comps/li/scale` | 5.0% (1/20) | 文本 | 0.8~1.2 |
| `comps/li/scalePositionWithRoom` | 50.0% (10/20) | 布尔 | true |
| `comps/li/scaleWithRoom` | 35.0% (7/20) | 布尔 | true |
| `comps/li/spawnCount` | 40.0% (8/20) | 数值 | 1 / 12 / 2 |
| `comps/li/spawnIntervalTicks` | 45.0% (9/20) | 数值 | 3 / 45 / 8 |
| `comps/li/velocity` | 15.0% (3/20) | 文本 | -1.8~-2.2 / 1.8~2.2 |
| `comps/li/velocityDir` | 15.0% (3/20) | 文本 | (1, 0, 0) |
| `comps/li/westRotationOffset` | 5.0% (1/20) | 文本 | (-0.5, 0, 0.2) |
| `defName` | 90.0% (18/20) | 文本 | Basic / Hindu / Islamic |
| `tintColor` | 55.0% (11/20) | 文本 | (100, 165, 255) / (161, 255, 88) / (222, 85, 101) |

## 四、原版 defName 一览（共 20 个，列出前 60）

```text
`Basic`                           `Islamic`                         `Christian`                       ``                              
``                                `Duel`                            `DanceParty`                      `Funeral`                       
`SacrificePrisoner`               `SacrificeAnimal`                 `DrumParty`                       `Speech`                        
`Hindu`                           `Totemic`                         `Buddhist`                        `Morbid`                        
`Rustic`                          `Techist`                         `Spikecore`                       `Animalist`                     
```
