# ComplexLayoutDef

- **所属线**：世界线
- **原版实例数**：3
- **字段路径数**：47
- **资料片**：Biotech、Ideology
- **原版出处**：`Ideology/Defs/LayoutDefs/Layouts_Misc.xml`、`Biotech/Defs/LayoutDefs/Layouts_Misc.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<ComplexLayoutDef ParentName="AncientComplex">
    <defName>AncientComplex_Loot</defName>
    <rewardThingSetMakerDef>MapGen_AncientComplexRoomLoot_Better</rewardThingSetMakerDef>
  </ComplexLayoutDef>
```

> 来自 `Ideology/Defs/LayoutDefs/Layouts_Misc.xml`，defName = `AncientComplex_Loot`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：AncientComplex / AncientComplex_Loot / AncientComplex_Mechanitor_Loot
```

## 三、全量字段表（47 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `areaPrunePercent` | 66.7% (2/3) | 数值 | 0.1 |
| `canDisconnectRooms` | 66.7% (2/3) | 布尔 | false |
| `clearDoorFaction` | 66.7% (2/3) | 布尔 | false |
| `corridorDef` | 66.7% (2/3) | 文本 | ComplexCorridor |
| `defName` | 100.0% (3/3) | 文本 | AncientComplex / AncientComplex_Loot / AncientComplex_Mechanitor_Loot |
| `minRoomHeight` | 66.7% (2/3) | 数值 | 7 |
| `minRoomWidth` | 66.7% (2/3) | 数值 | 7 |
| `rewardThingSetMakerDef` | 66.7% (2/3) | 文本 | MapGen_AncientComplexRoomLoot_Better / MapGen_AncientComplexRoomLoot_Default |
| `roomDefs` | 66.7% (2/3) | 容器 |  |
| `roomDefs/AncientArmory` | 33.3% (1/3) | 数值 | 1 |
| `roomDefs/AncientBandNodeRoom` | 33.3% (1/3) | 容器 |  |
| `roomDefs/AncientBandNodeRoom/countRange` | 33.3% (1/3) | 文本 | 0~2 |
| `roomDefs/AncientBandNodeRoom/weight` | 33.3% (1/3) | 数值 | 2 |
| `roomDefs/AncientBarracks` | 33.3% (1/3) | 容器 |  |
| `roomDefs/AncientBarracks/countRange` | 33.3% (1/3) | 文本 | 0~2 |
| `roomDefs/AncientBarracks/weight` | 33.3% (1/3) | 数值 | 2 |
| `roomDefs/AncientEquipmentRoom` | 33.3% (1/3) | 数值 | 1 |
| `roomDefs/AncientLab` | 33.3% (1/3) | 容器 |  |
| `roomDefs/AncientLab/countRange` | 33.3% (1/3) | 文本 | 0~1 |
| `roomDefs/AncientLab/weight` | 33.3% (1/3) | 数值 | 2 |
| `roomDefs/AncientMechGeneratorRoom` | 33.3% (1/3) | 容器 |  |
| `roomDefs/AncientMechGeneratorRoom/weight` | 33.3% (1/3) | 数值 | 1 |
| `roomDefs/AncientMechGestatorRoom` | 33.3% (1/3) | 容器 |  |
| `roomDefs/AncientMechGestatorRoom/weight` | 33.3% (1/3) | 数值 | 1 |
| `roomDefs/AncientPowerRoom` | 33.3% (1/3) | 容器 |  |
| `roomDefs/AncientPowerRoom/countRange` | 33.3% (1/3) | 文本 | 0~3 |
| `roomDefs/AncientPowerRoom/weight` | 33.3% (1/3) | 数值 | 1 |
| `roomDefs/AncientRechargeRoom` | 33.3% (1/3) | 容器 |  |
| `roomDefs/AncientRechargeRoom/weight` | 33.3% (1/3) | 数值 | 1 |
| `roomDefs/AncientStorageRoom` | 33.3% (1/3) | 数值 | 0.5 |
| `roomRewardCrateFactor` | 33.3% (1/3) | 数值 | 0 |
| `threats` | 66.7% (2/3) | 容器 |  |
| `threats/Ambush` | 33.3% (1/3) | 容器 |  |
| `threats/CryptosleepPods` | 33.3% (1/3) | 容器 |  |
| `threats/FuelNode` | 66.7% (2/3) | 容器 |  |
| `threats/FuelNode/maxPerRoom` | 66.7% (2/3) | 数值 | 1 |
| `threats/FuelNode/selectionWeight` | 66.7% (2/3) | 数值 | 3 |
| `threats/Infestation` | 33.3% (1/3) | 容器 |  |
| `threats/MechDrop` | 33.3% (1/3) | 容器 |  |
| `threats/RaidTerminal` | 66.7% (2/3) | 容器 |  |
| `threats/RaidTerminal/chancePerComplex` | 66.7% (2/3) | 数值 | 0.5 |
| `threats/RaidTerminal/maxPerComplex` | 33.3% (1/3) | 数值 | 1 |
| `threats/RaidTerminal/maxPerRoom` | 33.3% (1/3) | 数值 | 1 |
| `threats/SecurityCrate` | 33.3% (1/3) | 数值 | 4 |
| `threats/SleepingInsects` | 33.3% (1/3) | 容器 |  |
| `threats/SleepingMechanoids` | 66.7% (2/3) | 容器 |  |
| `workerClass` | 66.7% (2/3) | 文本 | LayoutWorkerComplex_Ancient / LayoutWorkerComplex_Mechanitor |

## 四、原版 defName 一览（共 3 个，列出前 60）

```text
`AncientComplex_Loot`             `AncientComplex_Mechanitor_Loot`  `AncientComplex`                
```
