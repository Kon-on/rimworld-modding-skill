# PawnTableDef

- **所属线**：表现线
- **原版实例数**：6
- **字段路径数**：5
- **资料片**：Biotech、Core
- **原版出处**：`Core/Defs/Misc/PawnTableDefs/PawnTables.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<PawnTableDef>
    <defName>Work</defName>
    <workerClass>PawnTable_PlayerPawns</workerClass>
    <columns>
      <li>LabelWithIcon</li>
      <li MayRequire="Ludeon.RimWorld.Ideology">Guest</li>
      <li>Faction</li>
      <li MayRequire="Ludeon.RimWorld.Ideology">Ideo</li>
      <li MayRequire="Ludeon.RimWorld.Biotech">Xenotype</li>
      <li>CopyPasteWorkPriorities</li>
      <li>RemainingSpace</li>
    </columns>
  </PawnTableDef>

  
```

> 来自 `Core/Defs/Misc/PawnTableDefs/PawnTables.xml`，defName = `Work`，XML 节点数 11（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
columns                                        [容器]
columns/li                                     [文本]  例：DraftMech / Energy / GapTiny
defName                                        [文本]  例：Assign / Mechs / Restrict
workerClass                                    [文本]  例：PawnTable_Animals / PawnTable_Mechs / PawnTable_PlayerPawns
```

## 三、全量字段表（5 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `columns` | 100.0% (6/6) | 容器 |  |
| `columns/li` | 1300.0% (78/6) | 文本 | DraftMech / Energy / GapTiny |
| `defName` | 100.0% (6/6) | 文本 | Assign / Mechs / Restrict |
| `minWidth` | 16.7% (1/6) | 数值 | 0 |
| `workerClass` | 100.0% (6/6) | 文本 | PawnTable_Animals / PawnTable_Mechs / PawnTable_PlayerPawns |

## 四、原版 defName 一览（共 6 个，列出前 60）

```text
`Work`                            `Restrict`                        `Mechs`                           `Wildlife`                      
`Assign`                          `Animals`                       
```
