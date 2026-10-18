# RoomPart_GestationTankDef

- **所属线**：世界线
- **原版实例数**：1
- **字段路径数**：5
- **资料片**：Odyssey
- **原版出处**：`Odyssey/Defs/RoomPartDefs/RoomParts_Common.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<RoomPart_GestationTankDef>
    <defName>GestationTanks</defName>
    <options>
      <Proximity>0.2</Proximity>
      <Dormant>0.3</Dormant>
      <Empty>0.5</Empty>
    </options>
  </RoomPart_GestationTankDef>

  
```

> 来自 `Odyssey/Defs/RoomPartDefs/RoomParts_Common.xml`，defName = `GestationTanks`，XML 节点数 6（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：GestationTanks
options                                        [容器]
options/Dormant                                [数值]  例：0.3
options/Empty                                  [数值]  例：0.5
options/Proximity                              [数值]  例：0.2
```

## 三、全量字段表（5 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (1/1) | 文本 | GestationTanks |
| `options` | 100.0% (1/1) | 容器 |  |
| `options/Dormant` | 100.0% (1/1) | 数值 | 0.3 |
| `options/Empty` | 100.0% (1/1) | 数值 | 0.5 |
| `options/Proximity` | 100.0% (1/1) | 数值 | 0.2 |

## 四、原版 defName 一览（共 1 个，列出前 60）

```text
`GestationTanks`                
```
