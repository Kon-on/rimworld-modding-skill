# 武器 mod 在游戏里搜不到 defName —— 排查顺序

先分清两类问题，它们的修法完全不同：

- **A 类：Def 根本没加载**（不在 DefDatabase 里）→ 查 Player.log + 静态核验
- **B 类：Def 加载了，只是某个界面搜不出来**（搜索框过滤的是显示文本／label，不是 defName；生成菜单按分类过滤；制作列表要配方）→ 换搜索词、换入口

判断入口只有一个：**Player.log**。下面按「先看日志 → 静态核验 → 游戏内确认 → 武器特有的坑」走。

---

## 第 0 步：确认这个 mod 真的被加载了（约 30 秒）

1. **启用状态**记在
   `%USERPROFILE%\AppData\LocalLow\Ludeon Studios\RimWorld by Ludeon Studios\Config\ModsConfig.xml`
   看 `<activeMods>` 里有没有你的 `packageId`（是 packageId，不是文件夹名）。

2. **看日志**——1.7 实测路径，注意比老文档多一层 `Logs\`：

   ```text
   %USERPROFILE%\AppData\LocalLow\Ludeon Studios\RimWorld by Ludeon Studios\Logs\Player.log
   ```

   日志头两行长这样，可用来确认是不是本次启动：

   ```text
   === Waylith log ===
   Version:   1.7.4981.136
   ```

   错误行长这样（1.7 格式，带 `ERROR [Verse]` 前缀）：

   ```text
   2026-10-18 18:37:37.767 ERROR [Verse] Failed to find Verse.WorkTypeDef named Fishing. There are 22 defs of this type loaded.
   ```

   在日志里搜这些词：`XML error`、`Could not find parent`、`lacks a defName`、`Adding duplicate`、`Config error`、`Failed to find`、`Could not find a type named`，以及你的 defName 和 packageId。

3. **改完要重载**：改 XML → 回主菜单重新加载模组或重开档；改 C# → 重新编译 + 重启游戏。

如果日志里连你 mod 的一行痕迹都没有，说明 mod 根本没被识别，先修这四条：

- 解压多套了一层——本地 mod 只认 `Mods\<文件夹名>\About\About.xml` 这一层，`Mods\MyMod\MyMod\About\...` 就不会出现在模组列表里；
- About.xml 语法错误，或 `packageId` 与其他 mod 重复；
- `supportedVersions` 没写 `1.7`；
- 写了 `LoadFolders.xml` 却没有 `<v1.7>` 块 → 1.7 下没有任何目录被映射（最保险写 `<v1.7><li>/</li></v1.7>`）。

---

## 第 1 步：按日志原文对号入座（括号里是 1.7 实测字符串）

| 日志里看到 | 含义 | 怎么修 |
|---|---|---|
| `XML error: Could not find parent node named "A" for node "B".` | ParentName 拼错，或父级是个没加载的抽象 def | 核对父级名：近战 `BaseMeleeWeapon_Sharp_Quality`、远程 `BaseHumanMakeableGun`、弹丸 `BaseBullet`、服装 `ApparelMakeableBase`、材料 `ResourceBase`、工作台 `BenchBase`、植物 `PlantBase`；抽象父级在原版里写作 `<ThingDef Name="...">`，用这个形式去原版 XML 里 grep 确认 |
| `XML error: Could not register node named "X" because this name is already used.` | 同名节点重复（自己文件之间，或跨 mod） | 换专属前缀，保证全局唯一 |
| `Adding duplicate <DefType> name: X` / `Tried to add null def to DefDatabase.` | defName 撞车，后加载的那份被丢掉 | 你搜不到的很可能是「你的那份」——尤其你把 defName 起成了和原版或别的 mod 一样的名字 |
| `... with label ... lacks a defName. Giving name Unnamed...` | 漏了 `<defName>`，或写成了 `<ThingDef Name="X">` | 正常 def 一律用 `<defName>`；只有要被继承的抽象 def 才用 `Name=`（抽象 def 不出现在生成列表，也搜不到） |
| `Could not find a type named X` | XML 里的 `thingClass` / `Class=` 类名错，或 DLL 没进 `Assemblies/` | 写全名（`命名空间.类名`），DLL 放进 `Assemblies/`，1.7 目标框架 net10.0 |
| `Config error in X: ...` / `'Value' is not a valid value for Field. Valid values are: ...` | 字段值非法 | 两个高频：`techLevel` 写成 `Ultratech`（合法值是 `Ultra`）；远程武器还在顶层写 `rangedWeapon_Cooldown` / `warmupTime` / `range` / `verbClass` |
| 只说文件与行号的 `XML error`（标签不匹配之类） | XML 不良构 → **整个文件被丢弃**，里面所有 def 一起消失 | 检查标签闭合；注释里不能出现 `--`；元素文本里不能写 `<YourPrefix>` 这种尖括号占位符 |
| `Failed to find <Type> named X. There are N defs of this type loaded.` | 某个 defName 引用找不到（远程武器的 `defaultProjectile`、配方产物、工作台 `recipeUsers` 等） | 把被引用的 def 补上或改对拼写——弹丸 Def 也要一起加载 |
| `Could not load Texture2D at '...'` / `Collection cannot init: No textures found at path ...` | 贴图问题，**不会**让 defName 搜不到，别被它带偏 | 单张贴图用 `Graphic_Single`；`Graphic_Random` / `Graphic_Collection` 要求 texPath 是目录 |
| 完全没有你 mod 的痕迹 | mod 没被加载 | 回到第 0 步那四条 |

> 还有一个静默跳过：某条 def 上写了 `MayRequire="某个mod/DLC"`，而玩家没装那个 mod → 这条 def 被整条跳过，**不报错**。

---

## 第 2 步：不开游戏，先静态核验一遍（30 秒）

本仓库自带一个零依赖核验器，可以直接指向你自己的 mod 目录（默认参数指向示例 mod，用 `--mod` 覆盖）：

```powershell
node docs/verify-testmod.mjs --mod "<你的 mod 目录>" --rimworld "<RimWorld 安装目录>"
```

它查 8 类：XML 良构 / defName 唯一且带前缀 / ParentName 与 defName 引用能否解析 / texPath 文件是否存在 / 字段路径是否在 1.7 字段总表里 / techLevel 等枚举合法性 / Patch 结构与 xpath / XML 里引用的自定义 C# 类型在 DLL 中是否存在。有硬错误时退出码 1，加 `--json` 供机器读。

实测输出形如：

```text
[1] XML 良构：19 个文件解析，0 个失败
[3] 原版索引：1560 个 XML，12415 个 defName/Name
[5] 字段路径核验：241 处，字段表未收录 4 处
=== 结果 === 错误 0 项，警告 4 项
```

字段名或枚举值拿不准时，别凭记忆写：

```powershell
node scripts/find-template.mjs --def ThingDef      # 该 Def 类型的模板与必填字段
node scripts/find-template.mjs --field verbClass   # 字段路径、出现率、原版样例值
```

---

## 第 3 步：游戏内确认「在不在」和「为什么搜不到」

1. 开发者模式（Options → 开发者模式）→ Debug actions 菜单 → `Spawn thing`。
2. **搜索框过滤的是菜单条目的显示文本，条目上显示的是 label**（做了中文本地化就是中文）。
   所以：**别用 defName 搜，改用 label 搜**，中英各试一次。用 defName 搜不到、用 label 搜得到，是很常见的「假故障」。
3. 还是看不到，再查这两条：
   - `<ThingDef Name="...">` 这种抽象 def 不会出现在生成列表里；
   - 分类/父级没生效：正常武器应有 `category=Item`（一般由 `ParentName` 带来）且 `thingClass` 存在。
4. 如果你要搜的其实是**制作菜单／工作台账单列表**（"我的枪怎么造不出来"），那考的不是 defName，而是 `recipeMaker` / `RecipeDef` + 工作台 `recipeUsers` + 研究前置——搜索词对不上就永远看不到。

> 补一句：技能旧文档里写的开发者控制台命令（`list defs ThingDef`、`spawn <defName>`）在 **1.7 原版不存在**——本机 1.7.4981.136 的 `Assembly-CSharp.dll` 里没有任何命令行/控制台类字符串，游戏只提供调试动作面板（快捷键见 Options → KeyBindings → "toggle debug actions menu"）和日志窗口。别沿着控制台这条路排查。

---

## 第 4 步：武器这个类型特有的三个坑

1. **远程武器在 1.7 不再读顶层 `rangedWeapon_Cooldown` / `warmupTime` / `range` / `verbClass`**：冷却写 `statBases/RangedWeapon_Cooldown`，射程／预热／弹丸写 `verbs/li/{verbClass, warmupTime, range, defaultProjectile}`。写成旧写法通常**不报红字**，但武器没有 verb → 表现是「东西在、用不了」，很容易被误判成「没加载」。
2. **弹丸 Def 要一起存在**：`defaultProjectile` 指向的 defName 必须真实存在且已加载，否则日志里会出现 `Failed to find` 一类引用错误。
3. **列表节点默认是追加**：要覆盖父 Def 的列表（如 `recipeUsers`、`tools`）必须写 `Inherit="False"`，否则只写你自己的那部分，会和父级的值混在一起。

---

## 最小自查清单

- [ ] `ModsConfig.xml` 的 `<activeMods>` 里有你的 `packageId`
- [ ] `Logs\Player.log` 里搜 `XML error` / `Could not find parent` / `lacks a defName` / `Adding duplicate` / `Config error`，逐条对上第 1 步
- [ ] `node docs/verify-testmod.mjs --mod "<你的 mod 目录>"` 报 0 错误
- [ ] Dev → Spawn thing 里用 **label**（中文 + 英文）各搜一次
- [ ] defName 用 ASCII + 专属前缀，不与原版重名；是 `<defName>` 而不是 `Name=`
- [ ] XML 在 `Defs/` 下（子目录可以），`LoadFolders.xml`（若存在）含 `<v1.7><li>/</li></v1.7>`

**四步都过了还搜不到**，把这三样贴出来就能定位：

1. `Player.log` 里提到你 defName / packageId 的全部行（带上下文）；
2. 你的 `About.xml`；
3. 那个武器 `ThingDef` 的完整 XML（附 `Defs/` 下的相对路径）。

（本机已实测 RimWorld 1.7.4981.136，我也可以直接把上面第 2 步的核验器指向你的 mod 目录，把有问题的文件与行列出来。）
