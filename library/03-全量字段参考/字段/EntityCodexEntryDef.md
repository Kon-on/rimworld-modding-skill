# EntityCodexEntryDef

- **所属线**：世界线
- **原版实例数**：27
- **字段路径数**：20
- **资料片**：Anomaly
- **原版出处**：`Anomaly/Defs/EntityCodexEntryDefs/EntityCodexEntryDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<EntityCodexEntryDef>
    <defName>HarbingerTree</defName>
    <label>harbinger tree</label>
    <category>Basic</category>
    <uiIconPath>UI/CodexEntries/HarbingerTree</uiIconPath>
    <useDescriptionFrom>Plant_TreeHarbinger</useDescriptionFrom>
    <linkedThings>
      <li>Plant_TreeHarbinger</li>
    </linkedThings>
    <provocationIncidents>
      <li>HarbingerTreeProvoked</li>
    </provocationIncidents>
    <orderInCategory>100</orderInCategory>
  </EntityCodexEntryDef>

  
```

> 来自 `Anomaly/Defs/EntityCodexEntryDefs/EntityCodexEntryDefs.xml`，defName = `HarbingerTree`，XML 节点数 11（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
category                                       [文本]  例：Advanced / Basic / Ultimate
defName                                        [文本]  例：Fleshbeasts / HarbingerTree / Sightstealer
label                                          [文本]  例：fleshbeast / harbinger tree / sightstealer
linkedThings/li                                [文本]  例：Fingerspike / Plant_TreeHarbinger / Trispike
orderInCategory                                [数值]  例：0 / 100 / 200
provocationIncidents/li                        [文本]  例：FleshbeastAttack / HarbingerTreeProvoked / ShamblerSwarmAnimals
uiIconPath                                     [文本]  例：UI/CodexEntries/Fleshbeasts / UI/CodexEntries/HarbingerTree / UI/CodexEntries/Sightstealer
```

## 三、全量字段表（20 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `allowDiscoveryWhileMapGenerating` | 7.4% (2/27) | 布尔 | true |
| `category` | 100.0% (27/27) | 文本 | Advanced / Basic / Ultimate |
| `defName` | 100.0% (27/27) | 文本 | Fleshbeasts / HarbingerTree / Sightstealer |
| `description` | 22.2% (6/27) | 文本 | A corpse-gray cloud composed of microscopic self-powered archites created by som / A person implanted with an  |
| `discoveredResearchProjects` | 55.6% (15/27) | 容器 |  |
| `discoveredResearchProjects/li` | 70.4% (19/27) | 文本 | GhoulInfusion / ProximityDetector / SummonFleshbeastsPlayer |
| `discoveryType` | 11.1% (3/27) | 文本 | BecameVisible / Unfog |
| `hideInPlaystyles` | 11.1% (3/27) | 容器 |  |
| `hideInPlaystyles/li` | 11.1% (3/27) | 文本 | AmbientHorror |
| `label` | 100.0% (27/27) | 文本 | fleshbeast / harbinger tree / sightstealer |
| `linkedIncidents` | 7.4% (2/27) | 容器 |  |
| `linkedIncidents/li` | 7.4% (2/27) | 文本 | BloodRain / DeathPall |
| `linkedThings` | 81.5% (22/27) | 容器 |  |
| `linkedThings/li` | 92.6% (25/27) | 文本 | Fingerspike / Plant_TreeHarbinger / Trispike |
| `orderInCategory` | 100.0% (27/27) | 数值 | 0 / 100 / 200 |
| `provocationIncidents` | 88.9% (24/27) | 容器 |  |
| `provocationIncidents/li` | 103.7% (28/27) | 文本 | FleshbeastAttack / HarbingerTreeProvoked / ShamblerSwarmAnimals |
| `startDiscovered` | 3.7% (1/27) | 布尔 | true |
| `uiIconPath` | 100.0% (27/27) | 文本 | UI/CodexEntries/Fleshbeasts / UI/CodexEntries/HarbingerTree / UI/CodexEntries/Sightstealer |
| `useDescriptionFrom` | 77.8% (21/27) | 文本 | Gorehulk / Plant_TreeHarbinger / Sightstealer |

## 四、原版 defName 一览（共 27 个，列出前 60）

```text
`HarbingerTree`                   `PitGate`                         `FleshmassHeart`                  `Noctolith`                     
`Noctol`                          `TwistedObelisk`                  `CorruptedObelisk`                `WarpedObelisk`                 
`UnnaturalCorpse`                 `VoidStructure`                   `Devourer`                        `VoidNode`                      
`VoidMonolith`                    `Ghoul`                           `Gorehulk`                        `Deathpall`                     
`FleshmassNucleus`                `Chimera`                         `Metalhorror`                     `Nociosphere`                   
`GoldenCube`                      `Sightstealer`                    `Shambler`                        `Dreadmeld`                     
`BloodRain`                       `Revenant`                        `Fleshbeasts`                   
```
