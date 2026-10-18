# 等离子匕首 / Plasma Dagger

按你的要求：**伤害 18、冷却 1.2 秒、科技等级 Ultratech**。下面是一套可以直接放进 mod 的最简实现（Core 版本，不依赖任何 DLC）。

## 1. 文件结构

```
YourMod/
└── Defs/
    └── ThingDefs/
        └── Weapons_Melee_PlasmaDagger.xml
```

## 2. 武器 Def

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Defs>

  <ThingDef ParentName="BaseMeleeWeapon_Sharp">
    <defName>MeleeWeapon_PlasmaDagger</defName>
    <label>plasma dagger</label>
    <description>A compact blade wrapped in a contained plasma sheath. The edge cuts through armour as if it were cloth, but the emitter needs a moment to recharge between swings.</description>
    <techLevel>Ultratech</techLevel>

    <texPath>Things/Item/Weapon/MeleeWeapon/PlasmaDagger</texPath>
    <graphicClass>Graphic_Single</graphicClass>

    <equippedAngleOffset>-135</equippedAngleOffset>
    <posInfo><MeleeWeapon><scale>0.9</scale></MeleeWeapon></posInfo>
    <weaponClasses>
      <li>Melee</li>
      <li>Sharp</li>
    </weaponClasses>

    <statBases>
      <Mass>1.0</Mass>
      <WorkToMake>9000</WorkToMake>
      <MarketValue>450</MarketValue>
      <MeleeWeapon_DamageMultiplier>1.0</MeleeWeapon_DamageMultiplier>
    </statBases>

    <tools>
      <li>
        <label>dagger</label>
        <capacities>
          <li>Cut</li>
        </capacities>
        <power>18</power>
        <cooldownTime>1.2</cooldownTime>
        <armorPenetration>0.28</armorPenetration>
      </li>
    </tools>

    <costList>
      <Plasteel>25</Plasteel>
      <Steel>10</Steel>
      <ComponentSpacer>2</ComponentSpacer>
    </costList>

    <recipeMaker>
      <recipeUsers>
        <li>FabricationBench</li>
      </recipeUsers>
      <researchPrerequisite>PlasmaWeaponry</researchPrerequisite>
      <skillRequirements>
        <Crafting>8</Crafting>
      </skillRequirements>
    </recipeMaker>

    <!-- 可选：只在特定派系/商人处出现
    <tradeability>Sellable</tradeability>
    -->
  </ThingDef>

</Defs>
```

## 3. 关键数值说明

| 字段 | 值 | 含义 |
| --- | --- | --- |
| `damageType` → `capacities` | `Cut` | 伤害类型（切割）。换成别的 DamageDef defName 就是别的伤害类型 |
| `power` | `18` | 每次命中的基础伤害 |
| `cooldownTime` | `1.2` | 一次挥击后的冷却，单位秒 |
| `armorPenetration` | `0.28` | 穿甲值，越高越能打穿护甲 |
| `techLevel` | `Ultratech` | 科技等级，影响商人/派系生成和 UI 显示 |
| `MeleeWeapon_DamageMultiplier` | `1.0` | 与 power 相乘；通常保持 1.0，把伤害写在 power 上 |

- 单次「挥击周期」约 = 1.2 s 冷却（预热时间对近战同样生效，可另加 `warmupTime`，默认很短）。
- 名义 DPS ≈ 18 / 1.2 ≈ **15**。

## 4. 还差什么

1. **贴图**：`Textures/Things/Item/Weapon/MeleeWeapon/PlasmaDagger.png`（1×2 或 1×1 的 PNG，透明底）。缺贴图会显示成粉紫色方块并在 log 里报 missing texture，但不会崩游戏。
2. **研究项目**：上面写了 `<researchPrerequisite>PlasmaWeaponry</researchPrerequisite>`，但 Core 里并不存在这个 defName。要么新建一个 ResearchProjectDef（例如在 `Defs/ResearchProjectDefs/` 里加一个 `PlasmaWeaponry`），要么把这行删掉、让它在 FabricationBench 直接可造。
3. **About.xml**（mod 根目录，用于让游戏识别）：

```xml
<?xml version="1.0" encoding="utf-8" ?>
<ModMetaData>
  <name>Plasma Dagger</name>
  <author>you</author>
  <supportedVersions>
    <li>1.5</li>
    <li>1.6</li>
  </supportedVersions>
</ModMetaData>
```

## 5. 正式版还要注意（不确定项，建议自行核对）

- **`PlasmaDagger` 的定位/缩放参数**（`equippedAngleOffset`、`posInfo` `scale`）我是按近战武器的通用形态给的，实际握持位置需要进游戏截图微调；如果要更"等离子感"，可以参考 DLC 里 Plasma Sword 的 `posInfo` 写法。
- **`MeleeWeapon_DamageMultiplier` 不是 Core 明文定义过的 StatDef**，我在示例里给了但**建议直接删掉**，避免生成 1.5 版本里出现未知 StatDef 的告警；想调伤害就直接改 `power`。
- **DLC 的 `PlasmaSword` 不在 Core**（Odyssey 或其他 DLC），所以我没法保证它用了哪种 `DamageDef`；本方案刻意只用 Core 的 `Cut`，跨版本最稳。
- **自动出售/掉落**：新武器默认能作为掉落和商品出现，但要真正在派系商人库存里稳定刷出，通常还要靠 `<tradeability>Sellable</tradeability>`、`<thingCategories>`（例如继承 BaseMeleeWeapon_Sharp 已带的武器分类）和派系 `<weaponTags>` 配合；这块各版本差异较大，建议在游戏里用开发者模式 `spawn` 直接调出验证。
- **1.6 与 1.5**：`ParentName="BaseMeleeWeapon_Sharp"` 与 `tools/power/cooldownTime` 结构在两个版本里都成立，`<li>` 列表语法也一样。
