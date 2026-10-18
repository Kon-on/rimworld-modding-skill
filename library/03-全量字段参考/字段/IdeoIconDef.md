# IdeoIconDef

- **所属线**：理念线
- **原版实例数**：94
- **字段路径数**：6
- **资料片**：Ideology
- **原版出处**：`Ideology/Defs/IdeoSymbolDefs/IdeoIconDefs_Specific.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<IdeoIconDef>
    <defName>ElementB</defName>
    <iconPath>UI/Ideoligions/ElementB</iconPath>
  </IdeoIconDef>

  
```

> 来自 `Ideology/Defs/IdeoSymbolDefs/IdeoIconDefs_Specific.xml`，defName = `ElementB`，XML 节点数 3（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：AnimalsA / AnimalsB / AnimalsC
iconPath                                       [文本]  例：UI/Ideoligions/AnimalsA / UI/Ideoligions/AnimalsB / UI/Ideoligions/AnimalsC
memes/li                                       [文本]  例：AnimalPersonhood / Rancher / Structure_Archist
```

## 三、全量字段表（6 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `cultures` | 27.7% (26/94) | 容器 |  |
| `cultures/li` | 29.8% (28/94) | 文本 | Astropolitan / Corunan / Kriminul |
| `defName` | 100.0% (94/94) | 文本 | AnimalsA / AnimalsB / AnimalsC |
| `iconPath` | 100.0% (94/94) | 文本 | UI/Ideoligions/AnimalsA / UI/Ideoligions/AnimalsB / UI/Ideoligions/AnimalsC |
| `memes` | 68.1% (64/94) | 容器 |  |
| `memes/li` | 139.4% (131/94) | 文本 | AnimalPersonhood / Rancher / Structure_Archist |

## 四、原版 defName 一览（共 94 个，列出前 60）

```text
`ElementB`                        `AbstractsA`                      `AbstractsB`                      `AbstractsC`                    
`AbstractsD`                      `AbstractsE`                      `CirclesA`                        `CirclesB`                      
`CirclesC`                        `CirclesD`                        `CirclesE`                        `Dotcircle`                     
`DoubleLoop`                      `PoliticalE`                      `RoundA`                          `RoundB`                        
`RoundC`                          `RoundD`                          `RoundE`                          `SpiralsB`                      
`SpiralsC`                        `SpiralsD`                        `SpiralsE`                        `StarsA`                        
`StarsB`                          `StarsC`                          `StarsD`                          `StarsE`                        
`TripleCross`                     `Archist_Lance`                   `Archist_Spikes`                  `ArchotechA`                    
`ArchotechB`                      `ArchotechC`                      `ArchotechD`                      `ArchotechE`                    
`ElementA`                        `FlowerSharp`                     `NatureB`                         `NatureC`                       
`NatureE`                         `PirateE`                         `PoliticalD`                      `ReligionE`                     
`SpiralsA`                        `TechAtom`                        `TechGearchains`                  `TechHand`                      
`AnimalsA`                        `AnimalsB`                        `AnimalsC`                        `AnimalsD`                      
`AnimalsE`                        `DownBurst`                       `ElementD`                        `ElementE`                      
`EmbodiedTheist_Bolthand`         `EmbodiedTheist_Punchcloud`       `NatureD`                         `ScarHands`                     
```

_余下 34 个 defName 见原版 `Data/<资料片>/Defs` 对应目录。_
