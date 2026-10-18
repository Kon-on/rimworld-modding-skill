# DebugTabMenuDef

- **所属线**：系统线
- **原版实例数**：3
- **字段路径数**：4
- **资料片**：Core
- **原版出处**：`Core/Defs/DebugTabMenuDefs/DebugTabMenuDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<DebugTabMenuDef>
    <defName>Actions</defName>
    <label>actions/tools</label>
    <menuClass>DebugTabMenu_Actions</menuClass>
    <displayOrder>0</displayOrder>
  </DebugTabMenuDef>

  
```

> 来自 `Core/Defs/DebugTabMenuDefs/DebugTabMenuDefs.xml`，defName = `Actions`，XML 节点数 5（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Actions / Output / Settings
displayOrder                                   [数值]  例：0 / 100 / 200
label                                          [文本]  例：actions/tools / output / settings
menuClass                                      [文本]  例：DebugTabMenu_Actions / DebugTabMenu_Output / DebugTabMenu_Settings
```

## 三、全量字段表（4 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (3/3) | 文本 | Actions / Output / Settings |
| `displayOrder` | 100.0% (3/3) | 数值 | 0 / 100 / 200 |
| `label` | 100.0% (3/3) | 文本 | actions/tools / output / settings |
| `menuClass` | 100.0% (3/3) | 文本 | DebugTabMenu_Actions / DebugTabMenu_Output / DebugTabMenu_Settings |

## 四、原版 defName 一览（共 3 个，列出前 60）

```text
`Actions`                         `Settings`                        `Output`                        
```
