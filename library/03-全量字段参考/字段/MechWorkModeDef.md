# MechWorkModeDef

- **所属线**：人物线
- **原版实例数**：4
- **字段路径数**：7
- **资料片**：Biotech
- **原版出处**：`Biotech/Defs/Misc/MechWorkModes.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<MechWorkModeDef>
    <defName>Work</defName>
    <label>work</label>
    <description>Work autonomously according to mechanoid type. Automatically go to rechargers and recharge when needed.</description>
    <iconPath>UI/Icons/WorkMode/Work</iconPath>
  </MechWorkModeDef>

  
```

> 来自 `Biotech/Defs/Misc/MechWorkModes.xml`，defName = `Work`，XML 节点数 5（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Escort / Recharge / SelfShutdown
description                                    [文本]  例：Go into a dormant self-charging state that very slowly regains energy without a  / Go to rechargers and recharge, even if already well-charged. / Stay near the mechanitor and fight nearby enemies. Follow the mechanitor, even o
iconPath                                       [文本]  例：UI/Icons/WorkMode/Escort / UI/Icons/WorkMode/Recharge / UI/Icons/WorkMode/SelfShutdown
label                                          [文本]  例：dormant self-charge / escort / recharge
```

## 三、全量字段表（7 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (4/4) | 文本 | Escort / Recharge / SelfShutdown |
| `description` | 100.0% (4/4) | 文本 | Go into a dormant self-charging state that very slowly regains energy without a  / Go to rechargers and rechar |
| `iconPath` | 100.0% (4/4) | 文本 | UI/Icons/WorkMode/Escort / UI/Icons/WorkMode/Recharge / UI/Icons/WorkMode/SelfShutdown |
| `ignoreGroupChargeLimits` | 25.0% (1/4) | 布尔 | true |
| `label` | 100.0% (4/4) | 文本 | dormant self-charge / escort / recharge |
| `uiOrder` | 75.0% (3/4) | 数值 | 200 / 300 / 400 |
| `workerClass` | 25.0% (1/4) | 文本 | WorkModeDrawer_Escort |

## 四、原版 defName 一览（共 4 个，列出前 60）

```text
`Work`                            `SelfShutdown`                    `Escort`                          `Recharge`                      
```
