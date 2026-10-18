# GameSetupStepDef

- **所属线**：系统线
- **原版实例数**：4
- **字段路径数**：3
- **资料片**：Core、Odyssey
- **原版出处**：`Core/Defs/Misc/GameSetupStepDefs/GameSetupSteps.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<GameSetupStepDef>
    <defName>Grids</defName>
    <order>0</order>
    <setupStep Class="GameSetupStep_Grids"/>
  </GameSetupStepDef>

  
```

> 来自 `Core/Defs/Misc/GameSetupStepDefs/GameSetupSteps.xml`，defName = `Grids`，XML 节点数 4（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Components / Grids / TileElementsCore
order                                          [数值]  例：0 / 100 / 200
setupStep                                      [容器]
```

## 三、全量字段表（3 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (4/4) | 文本 | Components / Grids / TileElementsCore |
| `order` | 100.0% (4/4) | 数值 | 0 / 100 / 200 |
| `setupStep` | 100.0% (4/4) | 容器 |  |

## 四、原版 defName 一览（共 4 个，列出前 60）

```text
`Grids`                           `Components`                      `TileElementsCore`                `TileElementsOdyssey`           
```
