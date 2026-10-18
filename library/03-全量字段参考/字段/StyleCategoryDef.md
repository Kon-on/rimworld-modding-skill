# StyleCategoryDef

- **所属线**：物品线
- **原版实例数**：11
- **字段路径数**：14
- **资料片**：Anomaly、Ideology
- **原版出处**：`Anomaly/Defs/StyleCategoryDefs/StyleCategoryDefs.xml`、`Ideology/Defs/StyleCategoryDefs/StyleCategoryDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<StyleCategoryDef>
    <defName>Horaxian</defName>
    <label>horaxian</label>
    <iconPath>UI/StyleCategories/Horaxian</iconPath>
    <fixedIdeoOnly>true</fixedIdeoOnly>
    <thingDefStyles>
      <li MayRequire="Ludeon.RimWorld.Royalty">
        <thingDef MayRequire="Ludeon.RimWorld.Royalty">MeleeWeapon_Axe</thingDef>
        <styleDef>Horaxian_Axe</styleDef>
      </li>
      <li>
        <thingDef>MeleeWeapon_Knife</thingDef>
        <styleDef>Horaxian_Knife</styleDef>
      </li>
      <li>
        <thingDef>MeleeWeapon_Gladius</thingDef>
        <styleDef>Horaxian_Gladius</styleDef>
      </li>
      <li>
        <thingDef>MeleeWeapon_Mace</thingDef>
        <styleDef>Horaxian_Mace</styleDef>
      </li>
      <li>
        <thingDef>MeleeWeapon_Club</thingDef>
        <styleDef>Horaxian_Club</styleDef>
      </li>
    </thingDefStyles>
  </StyleCategoryDef>
```

> 来自 `Anomaly/Defs/StyleCategoryDefs/StyleCategoryDefs.xml`，defName = `Horaxian`，XML 节点数 21（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
addDesignators/li                              [文本]  例：MorbidSlab_Broad / MorbidSlab_Medium / TotemicSlab_Broad
defName                                        [文本]  例：Christian / Hindu / Horaxian
iconPath                                       [文本]  例：UI/StyleCategories/Christian / UI/StyleCategories/Hindu / UI/StyleCategories/Horaxian
label                                          [文本]  例：Christian / Hindu / Islamic
ritualVisualEffectDef                          [文本]  例：Buddhist / Christian / Hindu
soundOngoingRitual                             [文本]  例：RitualSustainer_Buddhist / RitualSustainer_Christian / RitualSustainer_Hindu
thingDefStyles                                 [容器]
thingDefStyles/li                              [容器]
thingDefStyles/li/styleDef                     [文本]  例：Horaxian_Club / Horaxian_Gladius / Horaxian_Knife
thingDefStyles/li/thingDef                     [文本]  例：MeleeWeapon_Club / MeleeWeapon_Gladius / MeleeWeapon_Knife
```

## 三、全量字段表（14 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `addDesignatorGroups` | 36.4% (4/11) | 容器 |  |
| `addDesignatorGroups/li` | 45.5% (5/11) | 文本 | Floor_Morbid_Carpet / Floor_Morbid_Stone / Floor_Spikecore_Tile |
| `addDesignators` | 54.5% (6/11) | 容器 |  |
| `addDesignators/li` | 118.2% (13/11) | 文本 | MorbidSlab_Broad / MorbidSlab_Medium / TotemicSlab_Broad |
| `defName` | 100.0% (11/11) | 文本 | Christian / Hindu / Horaxian |
| `fixedIdeoOnly` | 9.1% (1/11) | 布尔 | true |
| `iconPath` | 100.0% (11/11) | 文本 | UI/StyleCategories/Christian / UI/StyleCategories/Hindu / UI/StyleCategories/Horaxian |
| `label` | 100.0% (11/11) | 文本 | Christian / Hindu / Islamic |
| `ritualVisualEffectDef` | 90.9% (10/11) | 文本 | Buddhist / Christian / Hindu |
| `soundOngoingRitual` | 90.9% (10/11) | 文本 | RitualSustainer_Buddhist / RitualSustainer_Christian / RitualSustainer_Hindu |
| `thingDefStyles` | 100.0% (11/11) | 容器 |  |
| `thingDefStyles/li` | 1054.5% (116/11) | 容器 |  |
| `thingDefStyles/li/styleDef` | 1054.5% (116/11) | 文本 | Horaxian_Club / Horaxian_Gladius / Horaxian_Knife |
| `thingDefStyles/li/thingDef` | 1054.5% (116/11) | 文本 | MeleeWeapon_Club / MeleeWeapon_Gladius / MeleeWeapon_Knife |

## 四、原版 defName 一览（共 11 个，列出前 60）

```text
`Horaxian`                        `Christian`                       `Islamic`                         `Buddhist`                      
`Hindu`                           `Animalist`                       `Rustic`                          `Techist`                       
`Spikecore`                       `Morbid`                          `Totemic`                       
```
