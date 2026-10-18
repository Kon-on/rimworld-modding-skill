# AbilityGroupDef

- **所属线**：人物线
- **原版实例数**：3
- **字段路径数**：5
- **资料片**：Ideology
- **原版出处**：`Ideology/Defs/AbilityDefs/Abilities.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<AbilityGroupDef>
    <defName>MultiRole</defName>
    <cooldownTicks>180000</cooldownTicks>
  </AbilityGroupDef>
  
  
```

> 来自 `Ideology/Defs/AbilityDefs/Abilities.xml`，defName = `MultiRole`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
cooldownTicks                                  [数值]  例：180000 / 600000
defName                                        [文本]  例：Leader / Moralist / MultiRole
ritualRoleIds/li                               [文本]  例：leader / moralist / speaker
```

## 三、全量字段表（5 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `cooldownTicks` | 100.0% (3/3) | 数值 | 180000 / 600000 |
| `defName` | 100.0% (3/3) | 文本 | Leader / Moralist / MultiRole |
| `ritualRoleIds` | 66.7% (2/3) | 容器 |  |
| `ritualRoleIds/li` | 100.0% (3/3) | 文本 | leader / moralist / speaker |
| `sendMessageOnCooldownComplete` | 66.7% (2/3) | 布尔 | true |

## 四、原版 defName 一览（共 3 个，列出前 60）

```text
`MultiRole`                       `Moralist`                        `Leader`                        
```
