# LogEntryDef

- **所属线**：系统线
- **原版实例数**：2
- **字段路径数**：3
- **资料片**：Core
- **原版出处**：`Core/Defs/Misc/LogEntryDefs/LogEntryDef.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<LogEntryDef>
    <defName>MeleeAttack</defName>
    <iconDamaged>Things/Mote/BattleSymbols/Blood</iconDamaged>
    <iconDamagedFromInstigator>Things/Mote/BattleSymbols/BloodTarget</iconDamagedFromInstigator>
  </LogEntryDef>

  
```

> 来自 `Core/Defs/Misc/LogEntryDefs/LogEntryDef.xml`，defName = `MeleeAttack`，XML 节点数 4（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：MeleeAttack / SandInEyes
iconDamaged                                    [文本]  例：Things/Mote/BattleSymbols/Blood / Things/Mote/BattleSymbols/SandInEyes
iconDamagedFromInstigator                      [文本]  例：Things/Mote/BattleSymbols/BloodTarget / Things/Mote/BattleSymbols/SandInEyesTarget
```

## 三、全量字段表（3 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (2/2) | 文本 | MeleeAttack / SandInEyes |
| `iconDamaged` | 100.0% (2/2) | 文本 | Things/Mote/BattleSymbols/Blood / Things/Mote/BattleSymbols/SandInEyes |
| `iconDamagedFromInstigator` | 100.0% (2/2) | 文本 | Things/Mote/BattleSymbols/BloodTarget / Things/Mote/BattleSymbols/SandInEyesTarget |

## 四、原版 defName 一览（共 2 个，列出前 60）

```text
`MeleeAttack`                     `SandInEyes`                    
```
