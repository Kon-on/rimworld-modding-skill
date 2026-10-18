# WeaponCategoryDef

- **所属线**：物品线
- **原版实例数**：16
- **字段路径数**：1
- **资料片**：Odyssey、Royalty
- **原版出处**：`Odyssey/Defs/WeaponTraitDefs/WeaponCategoryDefs.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<WeaponCategoryDef>
    <defName>Ranged</defName>
  </WeaponCategoryDef>

  
```

> 来自 `Odyssey/Defs/WeaponTraitDefs/WeaponCategoryDefs.xml`，defName = `Ranged`，XML 节点数 2（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Bow / BulletFiring / Ranged
```

## 三、全量字段表（1 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (16/16) | 文本 | Bow / BulletFiring / Ranged |

## 四、原版 defName 一览（共 16 个，列出前 60）

```text
`Ranged`                          `BulletFiring`                    `Bow`                             `Rifle`                         
`Sighted`                         `Scoped`                          `Shotgun`                         `BurstFire`                     
`LowStoppingPower`                `Gun`                             `PelletFiring`                    `PulseCharge`                   
`Pistol`                          `BeamWeapon`                      `Attachable`                      `BladeLink`                     
```
