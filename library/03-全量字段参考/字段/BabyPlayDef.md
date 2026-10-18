# BabyPlayDef

- **所属线**：人物线
- **原版实例数**：3
- **字段路径数**：3
- **资料片**：Biotech
- **原版出处**：`Biotech/Defs/BabyPlayDefs/BabyPlay.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<BabyPlayDef>
    <defName>PlayStatic</defName>
    <workerClass>BabyPlayGiver_PlayStatic</workerClass>
    <jobDef>PlayStatic</jobDef>
  </BabyPlayDef>

  
```

> 来自 `Biotech/Defs/BabyPlayDefs/BabyPlay.xml`，defName = `PlayStatic`，XML 节点数 4（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：PlayStatic / PlayToys / PlayWalking
jobDef                                         [文本]  例：PlayStatic / PlayToys / PlayWalking
workerClass                                    [文本]  例：BabyPlayGiver_PlayStatic / BabyPlayGiver_PlayToys / BabyPlayGiver_PlayWalking
```

## 三、全量字段表（3 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (3/3) | 文本 | PlayStatic / PlayToys / PlayWalking |
| `jobDef` | 100.0% (3/3) | 文本 | PlayStatic / PlayToys / PlayWalking |
| `workerClass` | 100.0% (3/3) | 文本 | BabyPlayGiver_PlayStatic / BabyPlayGiver_PlayToys / BabyPlayGiver_PlayWalking |

## 四、原版 defName 一览（共 3 个，列出前 60）

```text
`PlayStatic`                      `PlayWalking`                     `PlayToys`                      
```
