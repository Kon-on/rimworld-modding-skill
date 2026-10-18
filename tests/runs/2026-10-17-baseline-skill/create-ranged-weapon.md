# create-ranged-weapon — 离子步枪

> 运行条件：加载 rimworld-modding 技能，按技能指引产出。
> 环境：RimSage MCP 未配置 → 走核验源降级路径第 ② 级（对照 assets/templates/weapon-ranged.xml，验证状态为「已验证——基于原版 BaseWeapons.xml」）。

## 结论先说

远程枪械用 `ParentName="BaseHumanMakeableGun"`（继承链 BaseWeapon → BaseGun → BaseGunWithQuality → BaseMakeableGun → BaseHumanMakeableGun，已内置 recipeMaker、weaponTags、装备组件）。

射程 30 → `<rangedWeapon_Range>30</rangedWeapon_Range>`（不是 `<range>`，也不是写在 verbs 里）。

**伤害 15 不在武器 Def 上，而在子弹 Def 的 `<projectile><damageAmountBase>` 里**——这是远程武器最常见的错误来源。所以下面给两个 Def。

## 文件一：Defs/ThingDefs_Misc/Weapons/IonRifle.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<!-- 离子步枪模板 | AI 辅助生成 -->
<Defs>
  <ThingDef ParentName="BaseHumanMakeableGun">
    <defName>YourPrefix_Gun_IonRifle</defName>
    <label>离子步枪</label>
    <description>加速离子弹丸的制式步枪，射程远、后坐温和。</description>

    <techLevel>Spacer</techLevel>
    <possessionCount>1</possessionCount>

    <costStuffCount>60</costStuffCount>
    <stuffCategories>
      <li>Metallic</li>
    </stuffCategories>

    <statBases>
      <WorkToMake>14000</WorkToMake>
      <Mass>3.2</Mass>
      <AccuracyTouch>0.75</AccuracyTouch>
      <AccuracyShort>0.85</AccuracyShort>
      <AccuracyMedium>0.70</AccuracyMedium>
      <AccuracyLong>0.50</AccuracyLong>
    </statBases>

    <weaponTags>
      <li>YourPrefix_IonRifle</li>
    </weaponTags>

    <verbClass>Verb_Shoot</verbClass>
    <rangedWeapon_Cooldown>1.20</rangedWeapon_Cooldown>
    <rangedWeapon_WarmupTime>1.00</rangedWeapon_WarmupTime>
    <rangedWeapon_Range>30</rangedWeapon_Range>

    <defaultProjectile>YourPrefix_Bullet_IonRifle</defaultProjectile>

    <graphicData>
      <texPath>Things/Item/Equipment/Weapons/YourPrefix_IonRifle</texPath>
      <graphicClass>Graphic_Single</graphicClass>
      <shaderType>CutoutComplex</shaderType>
    </graphicData>
    <uiIconScale>1.0</uiIconScale>

    <recipeMaker>
      <researchPrerequisite>Gunsmithing</researchPrerequisite>
      <skillRequirements>
        <Crafting>6</Crafting>
      </skillRequirements>
      <workAmount>14000</workAmount>
    </recipeMaker>
  </ThingDef>
</Defs>
```

## 文件二：Defs/ThingDefs_Misc/Weapons/IonRifle_Bullet.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<!-- 离子弹 | AI 辅助生成 -->
<Defs>
  <ThingDef ParentName="BaseBullet">
    <defName>YourPrefix_Bullet_IonRifle</defName>
    <label>离子弹</label>

    <projectile>
      <damageAmountBase>15</damageAmountBase>
      <stoppingPower>1.5</stoppingPower>
      <speed>70</speed>
    </projectile>

    <graphicData>
      <texPath>Things/Projectile/IonRifle_Bullet</texPath>
      <graphicClass>Graphic_Single</graphicClass>
    </graphicData>
  </ThingDef>
</Defs>
```

## 落地与核验

1. 两个 Def 可以放同一个文件，也可以分两个文件——同一次加载都生效；文件名与 defName 无关，只与目录位置有关。
2. 贴图：武器 `Textures/Things/Item/Equipment/Weapons/YourPrefix_IonRifle.png`，弹丸 `Textures/Things/Projectile/IonRifle_Bullet.png`。
3. 待核验项（本机无可读原版目录，第一次进游戏核对）：
   - 父级名称 `BaseBullet`：在 `Data/Core/Defs/ThingDefs_Misc/Weapons/` 下 grep `BaseBullet` 确认本版本的确切拼法。
   - `<speed>` 单位与量级、`<stoppingPower>` 是否必填：对照原版 `Bullet_AssaultRifle`。
   - `rangedWeapon_Range`、`rangedWeapon_Cooldown`、`rangedWeapon_WarmupTime` 三个字段名已由模板 `weapon-ranged.xml` 对照原版确认。
4. 测射程：进游戏后装备并查看「信息」页的射程数值，应为 30 格；开发者模式可开 `God mode` 快速造一把。
5. 交付前在 `About.xml` description 末尾保留 AI 辅助生成标注。

## 一句话自查

伤害看子弹、射程看武器、精度看 statBases 的四个 Accuracy* ——改完任一项，进游戏实测一次，不要只看 XML。
