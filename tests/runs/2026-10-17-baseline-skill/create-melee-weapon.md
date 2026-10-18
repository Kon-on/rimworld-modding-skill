# create-melee-weapon — 等离子匕首

> 运行条件：加载 rimworld-modding 技能，按技能指引产出。
> 环境：RimSage MCP 未配置 → 走核验源降级路径第 ② 级（对照 assets/templates/weapon-melee.xml，该模板验证状态为「已验证——基于原版 BaseWeapons.xml」）。

## 结论先说

近战武器用 `ParentName="BaseMeleeWeapon_Sharp_Quality"` 继承原版全部通用组件，不要手写 comps、也不要把材料清单一项项列出来——材料用 costStuffCount + stuffCategories 表达。你给的两个数值直接落在 `<tools>` 上：伤害 18 → `<power>18</power>`，冷却 1.2 秒 → `<cooldownTime>1.2</cooldownTime>`。

科技等级用 `<techLevel>Ultra</techLevel>`：TechLevel 是枚举，合法值只有 Neolithic / Medieval / Industrial / Spacer / Ultra / Archotech（原版枚举里没有带后缀的拼法），所以这里取 Ultra。

## 文件：Defs/ThingDefs_Misc/Weapons/PlasmaDagger.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<!-- 等离子匕首模板 | AI 辅助生成 -->
<Defs>
  <ThingDef ParentName="BaseMeleeWeapon_Sharp_Quality">
    <defName>YourPrefix_MeleeWeapon_PlasmaDagger</defName>
    <label>等离子匕首</label>
    <description>一把刃口被等离子场包裹的匕首，割开装甲如同切开油脂。</description>

    <techLevel>Ultra</techLevel>
    <possessionCount>1</possessionCount>

    <costStuffCount>40</costStuffCount>
    <stuffCategories>
      <li>Metallic</li>
    </stuffCategories>

    <statBases>
      <WorkToMake>9000</WorkToMake>
      <Mass>1.5</Mass>
    </statBases>

    <equippedAngleOffset>-55</equippedAngleOffset>
    <weaponTags>
      <li>YourPrefix_PlasmaDagger</li>
    </weaponTags>

    <tools>
      <li>
        <label>刃</label>
        <capacities>
          <li>Cut</li>
        </capacities>
        <power>18</power>
        <cooldownTime>1.2</cooldownTime>
        <armorPenetration>0.20</armorPenetration>
      </li>
      <li>
        <label>柄</label>
        <capacities>
          <li>Blunt</li>
        </capacities>
        <power>6</power>
        <cooldownTime>1.2</cooldownTime>
        <armorPenetration>0.05</armorPenetration>
      </li>
    </tools>

    <!-- 等离子附加灼烧：确认 DamageDef 名称后再保留本段 -->
    <extraMeleeDamages>
      <li>
        <def>Burn</def>
        <amount>3</amount>
      </li>
    </extraMeleeDamages>

    <graphicData>
      <texPath>Things/Item/Equipment/Weapons/YourPrefix_PlasmaDagger</texPath>
      <graphicClass>Graphic_Single</graphicClass>
      <shaderType>CutoutComplex</shaderType>
    </graphicData>
    <uiIconScale>1.2</uiIconScale>

    <recipeMaker>
      <researchPrerequisite>Smithing</researchPrerequisite>
      <skillRequirements>
        <Crafting>4</Crafting>
      </skillRequirements>
      <workAmount>9000</workAmount>
    </recipeMaker>
  </ThingDef>
</Defs>
```

## 落地与核验

1. 替换 `YourPrefix`（你的 mod 前缀，全仓唯一）、`YourPrefix_PlasmaDagger`（贴图路径）后，文件放到 `Defs/ThingDefs_Misc/Weapons/PlasmaDagger.xml`。
2. 贴图放 `Textures/Things/Item/Equipment/Weapons/YourPrefix_PlasmaDagger.png`，否则游戏里是粉红方块。
3. 待核验项（本机没有可读的原版目录，以下是模板继承值，第一次进游戏请核对）：
   - 属性名 `cooldownTime` / `armorPenetration`：核对 `Data/Core/Defs/ThingDefs_Misc/Weapons/MeleeMedieval.xml` 里 `<tools>` 的写法。
   - `Burn` 是否为合法 DamageDef：在 `Data/Core/Defs/DamageDefs/` 里 grep `<defName>Burn`；名字不对就删掉整段 `<extraMeleeDamages>`。
   - `possessionCount`、`costStuffCount`、`stuffCategories` 已由模板 `weapon-melee.xml` 对照原版确认过，可直接用。
4. 首次进游戏用开发者模式（Options → Developer mode）看日志无红字，再进存档测试手感；配方自动出现在「制作」的锻造台上（研究前置 Smithing，需先研究完）。
5. 交付前记得在 `About.xml` 的 description 末尾保留 AI 辅助生成标注（技能第 6 节要求）。

## 一句话自查

继承 `BaseMeleeWeapon_Sharp_Quality` → 只写「个性化字段」：defName / label / description / techLevel / costStuffCount / stuffCategories / statBases / tools / graphicData / recipeMaker。通用组件（装备、禁用、风格、耐久）全在父级里。
