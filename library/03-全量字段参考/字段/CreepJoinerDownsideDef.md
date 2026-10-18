# CreepJoinerDownsideDef

- **所属线**：世界线
- **原版实例数**：9
- **字段路径数**：27
- **资料片**：Anomaly
- **原版出处**：`Anomaly/Defs/CreepjoinerDefs/Downsides.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<CreepJoinerDownsideDef>
    <defName>Nothing</defName>
    <label>nothing</label>
    <weight>1</weight>
  </CreepJoinerDownsideDef>
  
  
```

> 来自 `Anomaly/Defs/CreepjoinerDefs/Downsides.xml`，defName = `Nothing`，XML 节点数 4（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Aggressive / Leaves / Metalhorror
label                                          [文本]  例：aggressive / leaves / metalhorror
```

## 三、全量字段表（27 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `canOccurRandomly` | 11.1% (1/9) | 布尔 | false |
| `canOccurWhenImprisoned` | 44.4% (4/9) | 布尔 | true |
| `canOccurWhileDowned` | 11.1% (1/9) | 布尔 | false |
| `defName` | 100.0% (9/9) | 文本 | Aggressive / Leaves / Metalhorror |
| `excludes` | 11.1% (1/9) | 容器 |  |
| `excludes/li` | 11.1% (1/9) | 文本 | FleshbeastEmergence |
| `hasLetter` | 33.3% (3/9) | 布尔 | true |
| `hediffs` | 22.2% (2/9) | 容器 |  |
| `hediffs/li` | 22.2% (2/9) | 文本 | CrumblingMindUndiagnosedCreepjoiner / OrganDecayUndiagnosedCreepjoiner |
| `label` | 100.0% (9/9) | 文本 | aggressive / leaves / metalhorror |
| `letterDef` | 33.3% (3/9) | 文本 | NegativeEvent / NeutralEvent / ThreatSmall |
| `letterDesc` | 33.3% (3/9) | 文本 | {PAWN_nameDef} has involuntarily released a wave of psychic suffering! {PAWN_pro / {PAWN_nameDef} thanks you f |
| `letterLabel` | 33.3% (3/9) | 文本 | Psychic agony / {PAWN_nameDef} departure / {PAWN_nameDef} hostile |
| `minCombatPoints` | 11.1% (1/9) | 数值 | 300 |
| `mustBeConscious` | 11.1% (1/9) | 布尔 | true |
| `repeats` | 11.1% (1/9) | 布尔 | true |
| `requires` | 11.1% (1/9) | 容器 |  |
| `requires/li` | 11.1% (1/9) | 文本 | Assault |
| `surgicalInspectionLetterExtra` | 11.1% (1/9) | 文本 | {SURGEON_nameDef} detected a faint but painful psychic presence emanating from { |
| `traits` | 22.2% (2/9) | 容器 |  |
| `traits/Disturbing` | 11.1% (1/9) | 容器 |  |
| `traits/VoidFascination` | 11.1% (1/9) | 容器 |  |
| `triggerMinDays` | 11.1% (1/9) | 数值 | 5 |
| `triggerMtbDays` | 11.1% (1/9) | 数值 | 30 |
| `triggersAfterDays` | 44.4% (4/9) | 文本 | 1~3 / 3~5 / 9~30 |
| `weight` | 22.2% (2/9) | 数值 | 1 / 3 |
| `workerType` | 44.4% (4/9) | 文本 | CreepJoinerWorker_AggressiveDownside / CreepJoinerWorker_DepartDownside / CreepJoinerWorker_MetalhorrorDownsid |

## 四、原版 defName 一览（共 9 个，列出前 60）

```text
`Nothing`                         `EntityJailbreaker`               `Disturbing`                      `CrumblingMind`                 
`OrganDecay`                      `Leaves`                          `Aggressive`                      `Metalhorror`                   
`PsychicAgony`                  
```
