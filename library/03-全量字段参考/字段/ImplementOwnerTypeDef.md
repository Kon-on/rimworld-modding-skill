# ImplementOwnerTypeDef

- **所属线**：世界线
- **原版实例数**：5
- **字段路径数**：3
- **资料片**：Core
- **原版出处**：`Core/Defs/Misc/ImplementOwnerTypeDefs/ImplementOwnerTypeDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<ImplementOwnerTypeDef>
    <defName>Bodypart</defName>
    <implementOwnerTypeValue>bodypart</implementOwnerTypeValue>
  </ImplementOwnerTypeDef>

  
```

> 来自 `Core/Defs/Misc/ImplementOwnerTypeDefs/ImplementOwnerTypeDefs.xml`，defName = `Bodypart`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Bodypart / Hediff / Terrain
implementOwnerTypeValue                        [文本]  例：bodypart / hediff / terrain
```

## 三、全量字段表（3 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (5/5) | 文本 | Bodypart / Hediff / Terrain |
| `implementOwnerRuleName` | 60.0% (3/5) | 文本 | WEAPON |
| `implementOwnerTypeValue` | 100.0% (5/5) | 文本 | bodypart / hediff / terrain |

## 四、原版 defName 一览（共 5 个，列出前 60）

```text
`Bodypart`                        `NativeVerb`                      `Weapon`                          `Hediff`                        
`Terrain`                       
```
