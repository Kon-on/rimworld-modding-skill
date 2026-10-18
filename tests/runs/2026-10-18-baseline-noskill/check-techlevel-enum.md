# RimWorld 近战武器的 techLevel 合法值

近战武器**没有**独立的一套 techLevel 枚举。它用的是通用枚举 `Verse.TechLevel`（XML 里就是 `ThingDef` 上的 `<techLevel>` 元素），所有 ThingDef（近战/远程武器、衣物、建筑、仿生体……）共用同一套值。

## 合法值（共 8 个，按“先进程度”从低到高）

| XML 中写的值 | 序号 | 用途 |
| --- | --- | --- |
| `Undefined` | 0 | 默认值。ThingDef 不写 `<techLevel>` 时就是它 |
| `Animal` | 1 | 动物/野兽档，动物 ThingDef 用；近战武器不会用 |
| `Neolithic` | 2 | 新石器/部落档：短棍、长矛 |
| `Medieval` | 3 | 中世纪档：长剑、钉头锤、战锤 |
| `Industrial` | 4 | 工业档：小刀 / 短刀一类 |
| `Spacer` | 5 | 星际档：单分子剑、等离子剑、宙斯锤（Royalty 人格武器） |
| `Ultra` | 6 | 超科技档，原版近战武器基本不用，多见于特殊物品 / mod |
| `Archotech` | 7 | 远古科技档，原版主要用于远古物品（如远古仿生体），近战武器基本不用 |

## XML 写法示例

```xml
<ThingDef ParentName="BaseMeleeWeapon_Sharp">
  <defName>MySpacerSword</defName>
  <label>spacer sword</label>
  <techLevel>Spacer</techLevel>
  <tools>
    <!-- 近战伤害靠 tools 定义 -->
  </tools>
</ThingDef>
```

## 注意点

1. **只能从上面这 8 个里挑，不能自定义新值**：`TechLevel` 是写死在 C# 里的 enum，XML 里写一个不存在的名字会在加载/解析时报错。
2. **顺序 = 先进度**：游戏内部多处直接按枚举顺序比较大小（物品生成、贸易、科技门槛等），mod 想让武器“更高级”就把档位往上调；`Undefined`(0) 一般等价于“没设置”。
3. 近战武器实际会用到的通常只有 `Neolithic` / `Medieval` / `Industrial` / `Spacer`（内容型 mod 可能用 `Ultra` / `Archotech`）。
4. `techLevel` **不直接**影响伤害或护甲穿透：数值由 `<tools>`、材质（stuff）和近战相关 stat 决定；techLevel 主要作用在归类 / 生成 / 贸易层面。
5. 大小写建议严格照枚举名写（`Industrial`，别写 `industrial`）。RimWorld 的 XML 枚举解析是否大小写不敏感我记不确切，按原样写最稳妥。

## 不确定的部分（如实说明）

- 上面 8 个成员及其顺序来自我的记忆（`Verse.TechLevel` / `TechLevelUtility.ToStringHuman`），其中 `Animal`、`Ultra` 的确切位置建议再对本机反编译的 `Assembly-CSharp.dll` 或 RimWorld Wiki 的 Tech level 页面复核一次。
- 各把原版近战武器具体挂哪一档，我给的只是典型例子，不保证逐个 def 都对得上。
- 另外提醒：`Animal` / `Undefined` 对武器来说基本等于“不适用”，如果你在写武器 def，建议直接用 Neolithic 起的档位。