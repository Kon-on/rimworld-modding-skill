# NegativeFishingOutcomeDef

- **所属线**：世界线
- **原版实例数**：11
- **字段路径数**：9
- **资料片**：Odyssey
- **原版出处**：`Odyssey/Defs/Misc/NegativeFishingOutcomes.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<NegativeFishingOutcomeDef>
    <defName>DogfishEscape</defName>
    <fishType>Fish_Dogfish</fishType>
    <letterLabel>Dogfish escape</letterLabel>
    <letterText>While reeling in a dogfish, {PAWN_nameDef} nearly bitten by the thrashing creature.\n\nThe fish escaped in the confusion.</letterText>
    <letterDef>NeutralEvent</letterDef>
  </NegativeFishingOutcomeDef>
  
  
```

> 来自 `Odyssey/Defs/Misc/NegativeFishingOutcomes.xml`，defName = `DogfishEscape`，XML 节点数 6（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：DogfishBite / DogfishEscape / PiranhaAttack
fishType                                       [文本]  例：Fish_Catfish / Fish_Dogfish / Fish_Guppy
letterDef                                      [文本]  例：NegativeEvent / NeutralEvent
letterLabel                                    [文本]  例：Dogfish bite / Dogfish escape / Piranha attack
letterText                                     [文本]  例：While fishing, {PAWN_nameDef} got too close to the water and was attacked by a f / While fishing, {PAWN_nameDef} got too close to the water and was bitten by a pir / While reeling in a dogfish, {PAWN_nameDef} nearly bitten by the thrashing creatu
```

## 三、全量字段表（9 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `addsHediff` | 9.1% (1/11) | 文本 | ToxicBuildup |
| `damageAmountRange` | 54.5% (6/11) | 文本 | 1~2 / 4~6 / 6~12 |
| `damageDef` | 54.5% (6/11) | 文本 | Bite / Blunt / Stab |
| `defName` | 100.0% (11/11) | 文本 | DogfishBite / DogfishEscape / PiranhaAttack |
| `fishType` | 100.0% (11/11) | 文本 | Fish_Catfish / Fish_Dogfish / Fish_Guppy |
| `hediffSeverity` | 9.1% (1/11) | 数值 | 0.1 |
| `letterDef` | 100.0% (11/11) | 文本 | NegativeEvent / NeutralEvent |
| `letterLabel` | 100.0% (11/11) | 文本 | Dogfish bite / Dogfish escape / Piranha attack |
| `letterText` | 100.0% (11/11) | 文本 | While fishing, {PAWN_nameDef} got too close to the water and was attacked by a f / While fishing, {PAWN_nameDe |

## 四、原版 defName 一览（共 11 个，列出前 60）

```text
`DogfishEscape`                   `CatfishEscape`                   `GuppyEscape`                     `TunaEscape`                    
`MarlinEscape`                    `PiranhaBite`                     `PiranhaAttack`                   `DogfishBite`                   
`MarlinAttack`                    `FrostfishAttack`                 `CatfishSpine`                  
```
