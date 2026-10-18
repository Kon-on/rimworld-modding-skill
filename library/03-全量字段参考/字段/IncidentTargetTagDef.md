# IncidentTargetTagDef

- **所属线**：世界线
- **原版实例数**：7
- **字段路径数**：1
- **资料片**：Core、Odyssey
- **原版出处**：`Core/Defs/Misc/IncidentTargetTypeDefs/IncidentTargetTagDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<IncidentTargetTagDef>
    <defName>Map_PlayerHome</defName>
  </IncidentTargetTagDef>
  
  
```

> 来自 `Core/Defs/Misc/IncidentTargetTypeDefs/IncidentTargetTagDefs.xml`，defName = `Map_PlayerHome`，XML 节点数 2（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Map_Misc / Map_PlayerHome / Map_RaidBeacon
```

## 三、全量字段表（1 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (7/7) | 文本 | Map_Misc / Map_PlayerHome / Map_RaidBeacon |

## 四、原版 defName 一览（共 7 个，列出前 60）

```text
`Map_PlayerHome`                  `Map_TempIncident`                `Map_Misc`                        `Map_RaidBeacon`                
`Caravan`                         `World`                           `Gravship`                      
```
