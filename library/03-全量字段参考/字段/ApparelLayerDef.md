# ApparelLayerDef

- **所属线**：物品线
- **原版实例数**：6
- **字段路径数**：3
- **资料片**：Core
- **原版出处**：`Core/Defs/Misc/ApparelLayerDefs/ApparelLayerDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<ApparelLayerDef>
    <defName>OnSkin</defName>
    <label>skin</label>
    <drawOrder>0</drawOrder>
  </ApparelLayerDef>

  
```

> 来自 `Core/Defs/Misc/ApparelLayerDefs/ApparelLayerDefs.xml`，defName = `OnSkin`，XML 节点数 4（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Belt / Middle / OnSkin
drawOrder                                      [数值]  例：0 / 100 / 200
label                                          [文本]  例：middle / outer / skin
```

## 三、全量字段表（3 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (6/6) | 文本 | Belt / Middle / OnSkin |
| `drawOrder` | 100.0% (6/6) | 数值 | 0 / 100 / 200 |
| `label` | 100.0% (6/6) | 文本 | middle / outer / skin |

## 四、原版 defName 一览（共 6 个，列出前 60）

```text
`OnSkin`                          `Middle`                          `Shell`                           `Belt`                          
`Overhead`                        `EyeCover`                      
```
