# ShipJobDef

- **所属线**：世界线
- **原版实例数**：7
- **字段路径数**：3
- **资料片**：Core
- **原版出处**：`Core/Defs/ShipJobDefs/ShipJobDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<ShipJobDef>
    <defName>WaitTime</defName>
    <jobClass>ShipJob_WaitTime</jobClass>
  </ShipJobDef>

  
```

> 来自 `Core/Defs/ShipJobDefs/ShipJobDefs.xml`，defName = `WaitTime`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Arrive / FlyAway / Unload
jobClass                                       [文本]  例：ShipJob_Arrive / ShipJob_FlyAway / ShipJob_Unload
```

## 三、全量字段表（3 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `blocksDisposalIfQueuedUnspawned` | 28.6% (2/7) | 布尔 | false |
| `defName` | 100.0% (7/7) | 文本 | Arrive / FlyAway / Unload |
| `jobClass` | 100.0% (7/7) | 文本 | ShipJob_Arrive / ShipJob_FlyAway / ShipJob_Unload |

## 四、原版 defName 一览（共 7 个，列出前 60）

```text
`WaitTime`                        `Arrive`                          `Unload_Destination`              `WaitForever`                   
`WaitSendable`                    `Unload`                          `FlyAway`                       
```
