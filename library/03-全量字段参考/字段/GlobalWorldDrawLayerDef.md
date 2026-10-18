# GlobalWorldDrawLayerDef

- **所属线**：表现线
- **原版实例数**：2
- **字段路径数**：2
- **资料片**：Core
- **原版出处**：`Core/Defs/GlobalWorldDrawLayerDefs/GlobalWorldDrawLayers.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<GlobalWorldDrawLayerDef>
    <defName>Stars</defName>
    <worldDrawLayer>GlobalDrawLayer_Stars</worldDrawLayer>
  </GlobalWorldDrawLayerDef>

  
```

> 来自 `Core/Defs/GlobalWorldDrawLayerDefs/GlobalWorldDrawLayers.xml`，defName = `Stars`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Stars / Sun
worldDrawLayer                                 [文本]  例：GlobalDrawLayer_Stars / GlobalDrawLayer_Sun
```

## 三、全量字段表（2 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (2/2) | 文本 | Stars / Sun |
| `worldDrawLayer` | 100.0% (2/2) | 文本 | GlobalDrawLayer_Stars / GlobalDrawLayer_Sun |

## 四、原版 defName 一览（共 2 个，列出前 60）

```text
`Stars`                           `Sun`                           
```
