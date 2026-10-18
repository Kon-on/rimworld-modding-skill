# WeaponClassDef

- **所属线**：物品线
- **原版实例数**：10
- **字段路径数**：2
- **资料片**：Core
- **原版出处**：`Core/Defs/WeaponClassDefs/WeaponClassDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<WeaponClassDef>
    <defName>Melee</defName>
    <label>melee</label>
  </WeaponClassDef>

  
```

> 来自 `Core/Defs/WeaponClassDefs/WeaponClassDefs.xml`，defName = `Melee`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Melee / MeleeBlunt / MeleePiercer
label                                          [文本]  例：melee / melee blunt / melee piercer
```

## 三、全量字段表（2 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (10/10) | 文本 | Melee / MeleeBlunt / MeleePiercer |
| `label` | 100.0% (10/10) | 文本 | melee / melee blunt / melee piercer |

## 四、原版 defName 一览（共 10 个，列出前 60）

```text
`Melee`                           `Ranged`                          `MeleePiercer`                    `MeleeBlunt`                    
`LongShots`                       `ShortShots`                      `RangedHeavy`                     `RangedLight`                   
`Neolithic`                       `Ultratech`                     
```
