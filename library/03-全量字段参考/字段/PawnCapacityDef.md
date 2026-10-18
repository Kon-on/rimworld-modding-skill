# PawnCapacityDef

- **所属线**：人物线
- **原版实例数**：11
- **字段路径数**：17
- **资料片**：Core
- **原版出处**：`Core/Defs/PawnCapacityDefs/PawnCapacity.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<PawnCapacityDef>
    <defName>Sight</defName>
    <label>sight</label>
    <listOrder>60</listOrder>
    <workerClass>PawnCapacityWorker_Sight</workerClass>
    <showOnAnomalyEntities>false</showOnAnomalyEntities>
  </PawnCapacityDef>

  
```

> 来自 `Core/Defs/PawnCapacityDefs/PawnCapacity.xml`，defName = `Sight`，XML 节点数 6（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Consciousness / Manipulation / Moving
label                                          [文本]  例：consciousness / manipulation / moving
listOrder                                      [数值]  例：10 / 20 / 30
showOnAnomalyEntities                          [布尔]  例：false
workerClass                                    [文本]  例：PawnCapacityWorker_Consciousness / PawnCapacityWorker_Manipulation / PawnCapacityWorker_Moving
```

## 三、全量字段表（17 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (11/11) | 文本 | Consciousness / Manipulation / Moving |
| `label` | 100.0% (11/11) | 文本 | consciousness / manipulation / moving |
| `labelAnomalyEntity` | 9.1% (1/11) | 文本 | Sentience |
| `labelDrones` | 27.3% (3/11) | 文本 | Performance / battery integrity / pneumatics |
| `labelMechanoids` | 36.4% (4/11) | 文本 | Communication / Data processing / fluid reprocessing |
| `lethalFlesh` | 45.5% (5/11) | 布尔 | true |
| `lethalMechanoids` | 27.3% (3/11) | 布尔 | true |
| `listOrder` | 100.0% (11/11) | 数值 | 10 / 20 / 30 |
| `minForCapable` | 9.1% (1/11) | 数值 | 0.15 |
| `minValue` | 9.1% (1/11) | 数值 | 0.1 |
| `showOnAnimals` | 9.1% (1/11) | 布尔 | false |
| `showOnAnomalyEntities` | 90.9% (10/11) | 布尔 | false |
| `showOnCaravanHealthTab` | 27.3% (3/11) | 布尔 | true |
| `showOnDrones` | 45.5% (5/11) | 布尔 | false |
| `showOnMechanoids` | 45.5% (5/11) | 布尔 | false / true |
| `workerClass` | 100.0% (11/11) | 文本 | PawnCapacityWorker_Consciousness / PawnCapacityWorker_Manipulation / PawnCapacityWorker_Moving |
| `zeroIfCannotBeAwake` | 36.4% (4/11) | 布尔 | true |

## 四、原版 defName 一览（共 11 个，列出前 60）

```text
`Sight`                           `Hearing`                         `Manipulation`                    `Moving`                        
`Breathing`                       `Metabolism`                      `Talking`                         `Eating`                        
`Consciousness`                   `BloodFiltration`                 `BloodPumping`                  
```
