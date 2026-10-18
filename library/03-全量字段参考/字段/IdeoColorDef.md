# IdeoColorDef

- **所属线**：理念线
- **原版实例数**：33
- **字段路径数**：6
- **资料片**：Ideology
- **原版出处**：`Ideology/Defs/IdeoSymbolDefs/IdeoColorDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<IdeoColorDef>
    <defName>LightRed</defName>
    <colorDef>LightRed</colorDef>
  </IdeoColorDef>
  
  
```

> 来自 `Ideology/Defs/IdeoSymbolDefs/IdeoColorDefs.xml`，defName = `LightRed`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
colorDef                                       [文本]  例：DarkGrey / Grey / LightGrey
defName                                        [文本]  例：DarkGrey / Grey / LightGrey
```

## 三、全量字段表（6 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `colorDef` | 100.0% (33/33) | 文本 | DarkGrey / Grey / LightGrey |
| `cultures` | 9.1% (3/33) | 容器 |  |
| `cultures/li` | 9.1% (3/33) | 文本 | Corunan |
| `defName` | 100.0% (33/33) | 文本 | DarkGrey / Grey / LightGrey |
| `memes` | 27.3% (9/33) | 容器 |  |
| `memes/li` | 39.4% (13/33) | 文本 | Cannibal / PainIsVirtue / Supremacist |

## 四、原版 defName 一览（共 33 个，列出前 60）

```text
`LightRed`                        `DarkRed`                         `LightOrange`                     `DarkOrange`                    
`LightOlive`                      `DarkOlive`                       `LightGreen`                      `DarkGreen`                     
`LightTeal`                       `Teal`                            `DarkTeal`                        `LightBlue`                     
`DarkBlue`                        `LightSapphire`                   `Sapphire`                        `DarkSapphire`                  
`LightMauve`                      `Mauve`                           `DarkMauve`                       `LightPurple`                   
`DarkPurple`                      `LightPink`                       `DarkPink`                        `LightGrey`                     
`Grey`                            `DarkGrey`                        `Orange`                          `Blue`                          
`Pink`                            `Red`                             `Olive`                           `Green`                         
`Purple`                        
```
