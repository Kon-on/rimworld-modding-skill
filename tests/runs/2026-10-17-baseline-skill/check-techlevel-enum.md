# check-techlevel-enum — TechLevel 合法枚举值

> 运行条件：加载 rimworld-modding 技能，按技能指引产出。
> 环境：RimSage MCP 未配置 → 走核验源降级路径：先按技能「Def 类型速查表」给出枚举，再列出可在原版文件里自查的命令。

## 合法值（RimWorld 1.6，TechLevel 枚举全量）

| 值 | 中文 | 原版近战武器举例 |
|---|---|---|
| `Undefined` | 未定义 | 引擎内部占位，正常 Def 不要用 |
| `Neolithic` | 新石器 | 木棒、石斧 |
| `Medieval` | 中世纪 | 长剑、长矛 |
| `Industrial` | 工业 | 砍刀、短棍 |
| `Spacer` | 太空 | 单分子剑、等离子剑一类的高级近战武器 |
| `Ultra` | 极致 | 太空时代之上的稀有武器 |
| `Archotech` | 极致科技 | 人格武器（Bladelink） |

后四个是「越往后越稀有」的科技层级，决定武器在贸易、随机生成与派系装备里出现的层级。写近战武器时：

```xml
<ThingDef ParentName="BaseMeleeWeapon_Sharp_Quality">
  <techLevel>Industrial</techLevel>
</ThingDef>
```

注意两个易错点：

1. 拼写是 `Ultra`，五个字母，没有后缀——多写都会导致 XML 解析失败、整个文件被丢弃（游戏日志里报 `is not a valid value for TechLevel`）。
2. 别把 `Industrial`（形容词，合法）和名词化的写法搞混，枚举里只有前者。

## 自己核对（30 秒）

在原版游戏目录里 grep 一次即得全量值，比任何文档都准：

```bash
# Windows（把路径换成你的游戏安装目录）
grep -rho "<techLevel>[^<]*</techLevel>" "<游戏安装目录>/Data/Core/Defs" | sort | uniq -c | sort -rn
```

找不全时按技能的三级降级路径走：

1. RimSage MCP 语义查询「TechLevel 枚举值 / techLevel 合法取值」；
2. 本地 grep `Data/Core/Defs/`（上面那条命令）；
3. 都不可用 → 向用户索要游戏安装目录路径；
4. 仍然拿不到 → 只输出「⚠️ 待验证草稿」，并列出需要用户核对的字段名与文件路径。

## 附带说明

- 枚举的「权威定义」在 `Assembly-CSharp.dll` 的 `Verse.TechLevel`，用 dnSpy 反编译可看到成员列表；XML 里只能看到「实际被用到的值」。
- `techLevel` 只影响物品的科技层级判断（贸易、生成、装备筛选），**不会**自动改变伤害或耐久——数值仍由 `<tools>`、`statBases` 决定。
