# JoyKindDef

- **所属线**：人物线
- **原版实例数**：10
- **字段路径数**：3
- **资料片**：Core
- **原版出处**：`Core/Defs/Joy/JoyKinds.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<JoyKindDef>
    <defName>Gaming_Dexterity</defName>
    <label>dexterity play</label>
  </JoyKindDef>

  
```

> 来自 `Core/Defs/Joy/JoyKinds.xml`，defName = `Gaming_Dexterity`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Gaming_Cerebral / Gaming_Dexterity / Meditative
label                                          [文本]  例：cerebral play / dexterity play / social interaction
```

## 三、全量字段表（3 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (10/10) | 文本 | Gaming_Cerebral / Gaming_Dexterity / Meditative |
| `label` | 100.0% (10/10) | 文本 | cerebral play / dexterity play / social interaction |
| `needsThing` | 20.0% (2/10) | 布尔 | false |

## 四、原版 defName 一览（共 10 个，列出前 60）

```text
`Gaming_Dexterity`                `Gaming_Cerebral`                 `Television`                      `Telescope`                     
`HighCulture`                     `Chemical`                        `Gluttonous`                      `Reading`                       
`Meditative`                      `Social`                        
```
