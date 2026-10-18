# 近战武器 `techLevel` 的合法值

`ThingDef.techLevel` 用的是 `RimWorld.TechLevel` 枚举，一共 8 个成员。下面是完整清单（枚举值顺序即序号）：

| 合法值 | 序号 | 大致含义 | 近战武器里什么时候用 |
|---|:--:|---|---|
| `Undefined` | 0 | 未定义（**默认值**，XML 里不写就是它） | 不要显式写 |
| `Animal` | 1 | 动物级——没有工艺，靠天生器官 | 爪牙、角、尾刺这类"天生武器" |
| `Neolithic` | 2 | 新石器——木、石、骨 | 木棒 `Club`、石刀 `Knife`、长矛 `Spear` |
| `Medieval` | 3 | 中世纪——锻铁 | 钉锤 `Mace`、长剑 `LongSword` |
| `Industrial` | 4 | 工业时代 | 现代工厂量产的刀斧 |
| `Spacer` | 5 | 太空时代（电荷/单体工艺） | 单体剑、电荷武器这一档 |
| `Ultra` | 6 | 超科技 | 等离子剑/匕首这类"比太空级更狠"的人造武器 |
| `Archotech` | 7 | 远古科技——非人造，基本靠遗迹掉落 | 神器级、不该能造出来的武器 |

**最容易踩的坑：没有 `Ultratech`，超科技就是 `Ultra`。** 游戏内文案把它显示成 "ultratech"（武器标签里还有 `UltratechMelee` 这种字符串），所以很自然手写就多打了 `ch`——写错会在加载时报红字，字段回落到默认值。

## 实际写法

```xml
<ThingDef ParentName="BaseMeleeWeapon">
    <defName>YourMod_PlasmaBlade</defName>
    <label>等离子刃</label>
    <!-- 合法值：Animal / Neolithic / Medieval / Industrial / Spacer / Ultra / Archotech -->
    <techLevel>Ultra</techLevel>
</ThingDef>
```

`Undefined` 虽然也能解析，但它是 0 号值，含义就是"没填"，在按科技等级排序/比较的逻辑里排最前——所以近战武器建议明确写一个真实等级，别写 `Undefined`。

## 近战武器常选哪几个

原版近战武器实际只用到 4 档：`Neolithic`（`Club`/`Knife`/`Spear`）、`Medieval`（`Mace`/`LongSword`/`Gladius`）、`Spacer`、`Ultra`。你要做"更先进的近战武器"，从 `Spacer`、`Ultra`、`Archotech` 里挑；做部落风就从 `Neolithic`、`Medieval` 挑。

## 核验来源

以下都对过本机安装版 RimWorld 1.7.4981 rev136（`<游戏安装目录>`）：

1. **枚举本体**——反射 `Assembly-CSharp.dll` 的 `RimWorld.TechLevel`，得到 `Undefined=0, Animal=1, Neolithic=2, Medieval=3, Industrial=4, Spacer=5, Ultra=6, Archotech=7`；
2. **实际用法**——扫 `Data` 下 Core / Royalty / Ideology / Biotech / Anomaly / Odyssey 全部 XML，`<techLevel>` 共 258 处，分布为 Industrial 110、Spacer 60、Neolithic 40、Medieval 23、Ultra 13、Archotech 10、Animal 2——`Undefined` 一次都没被显式写过，也确实没有 `Ultratech`。

技能自带的 `assets/templates/weapon-melee.xml` 注释里也标注了这一串合法值，可直接套用。
