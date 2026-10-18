# debug-missing-def — defName 在游戏里搜不到

> 运行条件：加载 rimworld-modding 技能，按技能指引产出。
> 环境：RimSage MCP 未配置 → 走核验源降级路径第 ② 级（本地 grep 原版 Data/Core/Defs）。

按「先看日志 → 先查原版 → 再查自己的 mod」的顺序走，90% 的情况在第一步就能定位。

## 第 1 步：看日志（先看日志，不要先猜）

Windows 日志路径：

`C:/Users/<你>/AppData/LocalLow/Ludeon Studios/RimWorld by Ludeon Studios/Player.log`

搜关键词：`XML error`、`Could not load`、`Config error`、`is not a valid value`、你的文件名。

**XML 语法错误会让整份文件被静默丢弃**——游戏内不会弹窗，但日志里一定有行号。这是 defName 搜不到的第一大原因：

```
XML error: Duplicate node <li> ... in file .../PlasmaDagger.xml line 27
XmlException: Unexpected node type Element. ReadElementString only valid on text nodes.
```

## 第 2 步：先查原版，确认 defName 与结构本身没问题

```bash
# 1) 有没有同名 Def？（重名会被后加载的覆盖）
grep -rn "<defName>YourPrefix_MeleeWeapon_PlasmaDagger</defName>" "<游戏目录>/Data/Core/Defs"

# 2) 你要继承的父级是否存在、拼写对不对
grep -rn "Name=\"BaseMeleeWeapon_Sharp_Quality\"" "<游戏目录>/Data/Core/Defs"

# 3) 属性名是否是本版本的真实字段
grep -rn "cooldownTime\|armorPenetration" "<游戏目录>/Data/Core/Defs/ThingDefs_Misc/Weapons/MeleeMedieval.xml"
```

先查原版有两个好处：确认字段名（RimWorld 1.5 → 1.6 改过字段），以及拿到可复制的正确写法。RimSage MCP 可用时，也可以直接语义检索「近战武器 tools 字段」这类问题。MCP 与本地 grep 都没有 → 向用户索要游戏目录路径；都拿不到就明确标注「⚠️ 待验证草稿」，不要编字段名。

## 第 3 步：查自己的 mod 目录结构与元数据

| 检查项 | 正确 | 常见错误 |
|---|---|---|
| Defs 位置 | `<mod根>/Defs/…/X.xml` | 塞进 `About/` 里、或 `About/Defs/` |
| 根节点 | `<Defs>` | 直接以 `<ThingDef>` 开头 |
| About.xml | 有 `<packageId>` 且唯一 | 缺 packageId、packageId 与其他 mod 重复 |
| LoadFolders.xml | 1.6 目录映射正确 | 只写了 1.5 的 `<v1.5>`，1.6 下文件根本没被加载 |
| 版本目录 | 1.6 用 `1.6/` 或根目录平铺 | 文件放在 `1.5/` 里而游戏是 1.6 |
| 文件扩展名 | `.xml` 且非 0 字节 | `.XML`、`.txt`、空文件 |
| 编码 | UTF-8（带不带 BOM 均可） | GBK 编码 + 中文 label 导致整份文件丢弃 |

## 第 4 步：游戏内确认

1. Options → Developer mode 打开开发者模式；
2. 开发者菜单里看 Def 数据库（`DefDatabase` 相关条目 / Debug log），搜 defName；
3. 如果 Def 存在但搜不到物品：那是 `<label>` 或搜索关键字的问题，检查是否给了中文 label（游戏内搜索按 label 走）；
4. 如果 Def 不存在：回到第 1 步看日志，此时日志里必然有对应报错。

## 第 5 步：二分法定位（文件多、日志又被别的东西淹没时）

把 `Defs/` 下一半文件移走 → 重启 → 看 defName 是否出现。能出现说明问题在被移走的那一半，逐步缩小到单个文件；再注释掉 50% 行，找到报错行。

## 快速自检清单

- [ ] Player.log 里搜过 `XML error` 与你的文件名
- [ ] `Defs/` 位置与 `LoadFolders.xml` 覆盖了 1.6
- [ ] `About.xml` 的 `packageId` 存在且唯一
- [ ] 根节点是 `<Defs>`，无重复 defName
- [ ] 父级名字与原版一致（先查原版，别凭记忆写）
- [ ] 开发者模式里能看到这个 Def

六条都过了还没有的话，把 Player.log 的前 50 行 + 你的 XML 贴出来——报错行号通常就写在那里。
