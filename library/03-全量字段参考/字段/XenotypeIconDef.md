# XenotypeIconDef

- **所属线**：表现线
- **原版实例数**：11
- **字段路径数**：2
- **资料片**：Biotech
- **原版出处**：`Biotech/Defs/GeneDefs/XenotypeIconDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<XenotypeIconDef>
    <defName>Basic</defName>
    <texPath>UI/Icons/Xenotypes/Other</texPath>
  </XenotypeIconDef>

  
```

> 来自 `Biotech/Defs/GeneDefs/XenotypeIconDefs.xml`，defName = `Basic`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Basic / Crown / Ears
texPath                                        [文本]  例：UI/Icons/Xenotypes/Custom/CustomXenotypeIcon1 / UI/Icons/Xenotypes/Custom/CustomXenotypeIcon2 / UI/Icons/Xenotypes/Custom/CustomXenotypeIcon3
```

## 三、全量字段表（2 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (11/11) | 文本 | Basic / Crown / Ears |
| `texPath` | 100.0% (11/11) | 文本 | UI/Icons/Xenotypes/Custom/CustomXenotypeIcon1 / UI/Icons/Xenotypes/Custom/CustomXenotypeIcon2 / UI/Icons/Xenot |

## 四、原版 defName 一览（共 11 个，列出前 60）

```text
`Basic`                           `Crown`                           `Horn`                            `Ears`                          
`Frown`                           `Skull`                           `SkullThin`                       `Crescent`                      
`Lop`                             `Rect`                            `Furred`                        
```
