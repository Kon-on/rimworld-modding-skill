# ImpactSoundTypeDef

- **所属线**：表现线
- **原版实例数**：7
- **字段路径数**：3
- **资料片**：Biotech、Core
- **原版出处**：`Core/Defs/Misc/ImpactSoundTypeDefs/ImpactSoundTypeDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<ImpactSoundTypeDef>
    <defName>Bullet</defName>
  </ImpactSoundTypeDef>

  
```

> 来自 `Core/Defs/Misc/ImpactSoundTypeDefs/ImpactSoundTypeDefs.xml`，defName = `Bullet`，XML 节点数 2（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Blunt / Bullet / MechBandShockwave
```

## 三、全量字段表（3 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (7/7) | 文本 | Blunt / Bullet / MechBandShockwave |
| `playOnlyIfHitPawn` | 42.9% (3/7) | 布尔 | true |
| `soundDef` | 28.6% (2/7) | 文本 | MechBandShockwave / ToxicBuildupGained |

## 四、原版 defName 一览（共 7 个，列出前 60）

```text
`Bullet`                          `Slice`                           `Blunt`                           `Electric`                      
`Tornado`                         `MechBandShockwave`               `Toxic`                         
```
