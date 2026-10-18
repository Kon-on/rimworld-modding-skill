# MechWeightClassDef

- **所属线**：人物线
- **原版实例数**：4
- **字段路径数**：3
- **资料片**：Core
- **原版出处**：`Core/Defs/MechWeightClassDefs/MechWeightClassDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<MechWeightClassDef>
    <defName>Light</defName>
    <label>light</label>
  </MechWeightClassDef>

  
```

> 来自 `Core/Defs/MechWeightClassDefs/MechWeightClassDefs.xml`，defName = `Light`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Heavy / Light / Medium
label                                          [文本]  例：heavy / light / medium
```

## 三、全量字段表（3 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `canResurrect` | 25.0% (1/4) | 布尔 | false |
| `defName` | 100.0% (4/4) | 文本 | Heavy / Light / Medium |
| `label` | 100.0% (4/4) | 文本 | heavy / light / medium |

## 四、原版 defName 一览（共 4 个，列出前 60）

```text
`Light`                           `Medium`                          `Heavy`                           `UltraHeavy`                    
```
