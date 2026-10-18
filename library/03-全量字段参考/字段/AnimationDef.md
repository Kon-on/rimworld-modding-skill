# AnimationDef

- **所属线**：表现线
- **原版实例数**：13
- **字段路径数**：16
- **资料片**：Anomaly
- **原版出处**：`Anomaly/Defs/AnimationDefs/Revenant.xml`、`Anomaly/Defs/AnimationDefs/HoldingPlatformPawns.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<AnimationDef>
    <defName>RevenantSpasm</defName>
    <keyframeParts>
      <li>
        <key>Head</key>
        <value>
          <workerType>AnimationWorker_RevenantSpasm</workerType>
        </value>
      </li>
    </keyframeParts>
  </AnimationDef>

  
```

> 来自 `Anomaly/Defs/AnimationDefs/Revenant.xml`，defName = `RevenantSpasm`，XML 节点数 7（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：DeathRefusalTwitches / DevourerDigesting / HoldingPlatformLungeRight
durationTicks                                  [数值]  例：120 / 180 / 400
keyframeParts                                  [容器]
keyframeParts/li                               [容器]
keyframeParts/li/key                           [文本]  例：Head / Root
keyframeParts/li/value                         [容器]
keyframeParts/li/value/keyframes               [容器]
keyframeParts/li/value/keyframes/li            [容器]
keyframeParts/li/value/keyframes/li/angle      [数值]  例：-1 / -2 / 1
keyframeParts/li/value/keyframes/li/offset     [文本]  例：(.2, 0, .05) / (0, 0, .02) / (0, 0, .1)
keyframeParts/li/value/keyframes/li/tick       [数值]  例：176 / 177 / 178
keyframeParts/li/value/workerType              [文本]  例：AnimationWorker_Keyframes / AnimationWorker_RevenantHypnotise / AnimationWorker_RevenantSpasm
```

## 三、全量字段表（16 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (13/13) | 文本 | DeathRefusalTwitches / DevourerDigesting / HoldingPlatformLungeRight |
| `durationTicks` | 92.3% (12/13) | 数值 | 120 / 180 / 400 |
| `keyframeParts` | 100.0% (13/13) | 容器 |  |
| `keyframeParts/li` | 100.0% (13/13) | 容器 |  |
| `keyframeParts/li/key` | 100.0% (13/13) | 文本 | Head / Root |
| `keyframeParts/li/value` | 100.0% (13/13) | 容器 |  |
| `keyframeParts/li/value/keyframes` | 92.3% (12/13) | 容器 |  |
| `keyframeParts/li/value/keyframes/li` | 2730.8% (355/13) | 容器 |  |
| `keyframeParts/li/value/keyframes/li/angle` | 2684.6% (349/13) | 数值 | -1 / -2 / 1 |
| `keyframeParts/li/value/keyframes/li/offset` | 323.1% (42/13) | 文本 | (.2, 0, .05) / (0, 0, .02) / (0, 0, .1) |
| `keyframeParts/li/value/keyframes/li/tick` | 2730.8% (355/13) | 数值 | 176 / 177 / 178 |
| `keyframeParts/li/value/pivot` | 7.7% (1/13) | 文本 | (0.5, 0) |
| `keyframeParts/li/value/workerType` | 100.0% (13/13) | 文本 | AnimationWorker_Keyframes / AnimationWorker_RevenantHypnotise / AnimationWorker_RevenantSpasm |
| `playWhenDowned` | 61.5% (8/13) | 布尔 | true |
| `posRotScale` | 7.7% (1/13) | 数值 | .2 |
| `startOnRandomTick` | 76.9% (10/13) | 布尔 | false / true |

## 四、原版 defName 一览（共 13 个，列出前 60）

```text
`RevenantSpasm`                   `RevenantHypnotise`               `UnnaturalCorpseAwokenKilling`    `DevourerDigesting`             
`ShamblerSway`                    `ShamblerRise`                    `HoldingPlatformWiggleLight`      `DeathRefusalTwitches`          
`HoldingPlatformWiggleIntense`    `HoldingPlatformLungeUp`          `HoldingPlatformLungeRight`       `HoldingPlatformLungeDown`      
`HoldingPlatformLungeLeft`      
```
