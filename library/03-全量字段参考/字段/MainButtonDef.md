# MainButtonDef

- **所属线**：系统线
- **原版实例数**：15
- **字段路径数**：14
- **资料片**：Biotech、Core、Ideology
- **原版出处**：`Core/Defs/Misc/MainButtonDefs/MainButtons.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<MainButtonDef>
    <defName>Inspect</defName>
    <label>inspect</label>
    <tabWindowClass>MainTabWindow_Inspect</tabWindowClass>
    <buttonVisible>false</buttonVisible>
  </MainButtonDef>
  
  
```

> 来自 `Core/Defs/Misc/MainButtonDefs/MainButtons.xml`，defName = `Inspect`，XML 节点数 5（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Architect / Inspect / Mechs
description                                    [文本]  例：Choose which colonist does what kinds of work, and in what order. / Designate where to build, farm, store items, and so on. / Schedule colonists' activities to certain times of day, and set their allowed ar
label                                          [文本]  例：architect / inspect / mechs
order                                          [数值]  例：1 / 10 / 20
tabWindowClass                                 [文本]  例：MainTabWindow_Architect / MainTabWindow_Inspect / MainTabWindow_Mechs
```

## 三、全量字段表（14 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `buttonVisible` | 6.7% (1/15) | 布尔 | false |
| `canBeTutorDenied` | 6.7% (1/15) | 布尔 | false |
| `closesWorldView` | 53.3% (8/15) | 布尔 | true |
| `defaultHotKey` | 66.7% (10/15) | 文本 | F1 / F2 / F3 |
| `defName` | 100.0% (15/15) | 文本 | Architect / Inspect / Mechs |
| `description` | 93.3% (14/15) | 文本 | Choose which colonist does what kinds of work, and in what order. / Designate where to build, farm, store item |
| `iconPath` | 26.7% (4/15) | 文本 | UI/Buttons/MainButtons/Factions / UI/Buttons/MainButtons/History / UI/Buttons/MainButtons/Ideoligions |
| `label` | 100.0% (15/15) | 文本 | architect / inspect / mechs |
| `minimized` | 26.7% (4/15) | 布尔 | True |
| `order` | 93.3% (14/15) | 数值 | 1 / 10 / 20 |
| `tabWindowClass` | 93.3% (14/15) | 文本 | MainTabWindow_Architect / MainTabWindow_Inspect / MainTabWindow_Mechs |
| `validWithClassicIdeo` | 6.7% (1/15) | 布尔 | false |
| `validWithoutMap` | 40.0% (6/15) | 布尔 | true |
| `workerClass` | 20.0% (3/15) | 文本 | MainButtonWorker_ToggleMechTab / MainButtonWorker_ToggleResearchTab / MainButtonWorker_ToggleWorld |

## 四、原版 defName 一览（共 15 个，列出前 60）

```text
`Inspect`                         `Mechs`                           `Architect`                       `Work`                          
`Schedule`                        `Assign`                          `Animals`                         `Wildlife`                      
`Research`                        `Quests`                          `World`                           `Factions`                      
`History`                         `Menu`                            `Ideos`                         
```
