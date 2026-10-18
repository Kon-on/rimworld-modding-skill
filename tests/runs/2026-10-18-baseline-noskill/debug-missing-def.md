# 武器 mod 的 defName 在游戏里搜不到：从外到内的排查顺序

一句话：先把「文件有没有被游戏读」「def 有没有进数据库」「你用的搜索框搜的到底是不是 label」这三件事分开，剩下的都是体力活。

## 0. 先分清「搜不到」是哪一种

同一个现象至少对应三种完全不同的原因，先分类，否则会一直在改 XML 却看不到变化：

| 情况 | 特征 | 怎么确认 |
|---|---|---|
| A. def 根本没加载 | 用 label 也搜不到 | 看日志 + 探针 def（第 3 节） |
| B. 加载了，但被同 defName 覆盖 / 被 patch 删掉 | defName 能搜到，但 label、属性、贴图不是你写的 | 看搜到的 label 是不是你自己的；只开 Core + 本 mod 复测 |
| C. def 在数据库里，只是入口找不到 | label 能搜到，换 defName 就没了 | 换入口交叉验证 |

注意：开发者模式里的 def 搜索框、生成物品（spawn thing）列表、以及各种搜索类 mod 的搜索工具，行为并不统一——有的只匹配 label，有的只列「可生成」的 def（abstract 模板不会出现），有的按 thingCategories / weaponClasses 过滤。所以第一步先做交叉验证：**同一把武器，分别用 label 和 defName 各搜一次**，用结果判断落在 A / B / C 哪一类。

## 1. 六个检查点，按顺序走

1. **mod 在模组列表里吗？** 不在 → 问题在 About.xml 或目录结构，跟 def 内容无关。
2. **启用后启动，有红色报错吗？** 有 → 先读红字里最早的一条，那里通常直接写着文件名和出错节点。
3. **日志里搜得到你的 XML 文件名吗？** 搜不到 → 文件没被扫描（第 4 节）。
4. **加一个探针 def**（第 3 节）：探针也搜不到 = 加载层问题；探针能搜到 = 你原来那个 def 的内容问题。
5. **只启用 Core + 本 mod**（+ 必需依赖）再启动一次：结果变了 = 被别的 mod 覆盖或 patch 掉了。
6. **整段复制本体同类武器 def，只改 defName 和 label**：能跑通后，再把自己的字段一段一段加回去，二分定位到具体哪一段把 def 弄没了。

## 2. 看日志（信息量最大的一步）

Windows 日志路径：

```
%USERPROFILE%\AppData\LocalLow\Ludeon Studios\RimWorld by Ludeon Studios\Player.log
```

上一次启动的日志是同目录的 `Player-prev.log`（每次启动会滚动覆盖，所以**出问题后先别关游戏、别重启**，先把日志复制出来）。

- macOS：`~/Library/Logs/Ludeon Studios/RimWorld by Ludeon Studios/Player.log`
- Linux：`~/.config/unity3d/Ludeon Studios/RimWorld by Ludeon Studios/Player.log`

在日志里依次搜这些：

- 你的 mod 文件夹名 / 你的 XML 文件名
- 你的 `defName`
- `XML error`、`Config error`
- `Could not find`、`Duplicate`、`Could not load`、`Texture`、`Assemblies`、`Exception`

重点：

- **XML 错误大多是「宽容」的**：游戏照进，只是某个 def 被丢掉或半残，玩家只会看到红字一闪而过。所以「游戏能进」不等于「你的 def 加载了」。
- 字段名拼错通常抛出 `XML error` 系列的报错，大意是「这个节点不对应该类型的任何字段」（不同版本措辞略有差异），这类报错**不会阻止其它 def 加载**，极容易被忽略。
- 日志报错会带文件路径，可以直接对上具体文件；如果连你的文件名都没出现过，基本就是文件没被扫描。

## 3. 探针 def：先证明「文件真的被读了」

新建一个最小文件（或临时塞进现有文件），只放一个绝不可能重名的 def：

```xml
<?xml version="1.0" encoding="utf-8"?>
<Defs>
  <ThingDef ParentName="BaseHumanMakeableGun">
    <defName>ZZZ_Probe_Test_Weapon_9471</defName>
    <label>ZZZ探针测试武器</label>
    <description>probe</description>
  </ThingDef>
</Defs>
```

重启游戏，去开发者模式里搜 `ZZZ探针测试武器` 或 `ZZZ_Probe_Test_Weapon_9471`：

- **搜得到** → 加载链路是通的，问题在你原来那个 def 的内容（第 5 节），或者你原来那个 defName 被覆盖了。
- **搜不到** → 问题在「mod 目录 → XML 文件」这一层（第 4、6 节），先别动 def 内容。

想把「文件到底读没读」再坐实：故意在探针里制造一个明显错误（把 `<label>` 拼成 `<lable>`，或把 `<Defs>` 写成 `<Defss>`），看日志有没有对应报错。**完全没反应 = 文件根本没进解析器。**

## 4. 「文件没被读到」的常见原因

按踩坑频率排：

1. **扩展名其实是 `.xml.txt`**。Windows 默认隐藏扩展名，记事本存成 `MyWeapon.xml.txt`，游戏不会读。资源管理器里勾上「文件扩展名」看一眼。
2. **不在 `Defs/` 下**。必须是 mod 根目录下的 `Defs`（可以有任意层子目录，会递归扫描）；放在 `Patches/`、`About/`、`Textures/` 下都不会当作 def 加载。`Patches/` 只放 `<Patch>` 补丁。
3. **版本子目录没配 `LoadFolders.xml`**。如果你把内容放在 `1.5/Defs/...` 这类版本目录里，必须在 mod 根放 `LoadFolders.xml` 声明对应关系，否则只扫根目录。
4. **根节点不对**。一个 XML 文件只能有一个根节点，且必须是 `<Defs>`；把多个 `<Defs>` 粘进同一个文件、或外面再套一层 `<ThingDefs>`，解析失败后整份文件都不加载。
5. **XML 语法错误**。`<description>` 里写了裸的 `&` 或 `<`，注释里出现 `--`，用了全角括号或中文引号，某个标签没闭合——整份文件直接解析失败，而日志里可能只有一行。
6. **不可见字符 / 编码问题**。从网页或聊天窗口粘来的 defName 里可能混进全角字符、零宽空格、不换行空格。在 VS Code 里打开、显示空白字符，把 defName 手打一遍试试。

另外两点常被忽略：**改完 XML 必须重启游戏**（def 不会热重载）；如果你测试的是 Steam 创意工坊订阅版，确认游戏读的就是你改的那份文件夹——本地开发建议直接把 mod 放到 `RimWorld/Mods/YourMod` 下。

## 5. def 本身的高频错误

1. **`<defName>` 写成了 `<Name>`**。`Name` 是给 abstract 模板用的（供 `ParentName` 引用），不是真实 def 的注册名。真实 def 必须有 `<defName>`；缺 defName 的非 abstract def 会被跳过。
2. **误加了 `Abstract="True"`**。abstract def 只当模板，不会作为可生成物品出现，搜索入口里通常也看不到。
3. **defName 重复**。和其它 mod（或你自己另一份文件）撞名时，后加载的覆盖先加载的；有时控制台报重复 def 的错，有时只是静默覆盖。**所有 defName 都加 mod 前缀**（`MyMod_PlasmaRifle` 这种）能省掉一大半这类问题。判断自己是否被覆盖：搜出来的 label 不是你写的那串，就是被顶替了。
4. **XML 里的类型名不对**。武器是 `ThingDef`，没有 `WeaponDef` 这个东西；写成 `<thingDef>` 也一样不加载，大小写要完全一致。
5. **`ParentName` 指向的父节点不存在 / 还没加载**。父节点名在 1.4 / 1.5 / 1.6 之间增删过，照抄旧教程很容易指向一个当前版本不存在的模板；跨 mod 引用父节点时还要在 `About.xml` 里写 `loadAfter`，否则父节点可能还没加载。
6. **`thingClass` 指向的 C# 类找不到**。自己写 ThingDef 子类时：DLL 要放在 `Assemblies/` 下、命名空间和类名要完全对上、要继承 `ThingWithComps`。DLL 没编进去或类名打错，def 会加载失败并报红字。
7. **远程武器缺 `verbs`，或 `defaultProjectile` 指向不存在的 def**。`defaultProjectile` 必须是真实存在的 ThingDef（例如 `Bullet_ChargeRifle`）；引用不存在的会报 `Config error` / `Could not find`，表现为枪能出现但打不出子弹，或者干脆不出现。
8. **近战武器缺 `tools`**。近战伤害来自 `tools` 列表，其中 `capacities` 填的是 DamageDef 的 defName（`Blunt`、`Cut`、`Stab` 等），写错名字就报找不到 def。
9. **`graphicData.texPath` 路径错**。路径相对 mod 根目录、指向 `Textures/` 下的文件、不带扩展名；`graphicClass` 一般是 `Graphic_Single`。路径错通常只报贴图加载失败，def 还在（表现为粉块 / 空图）。
10. **分类字段和版本不匹配**。`category`、`thingCategories`（如 `WeaponsRanged`）以及新版引入的 `weaponClasses` 在版本之间有变化，照抄旧模板会出现「加载了但按分类翻不到」。
11. **`recipeMaker` 引用了不存在的工作台或配方**（想让它可制作的话），报错形式同样是找不到 def。
12. **`<li>` 列表结构写错**。`verbs`、`tools`、`comps`、`statBases` 这些列表里每一项必须是 `<li>`，层级写错或漏了，对应内容会被忽略，严重的会导致整个 def 报废。

## 6. 排除「别的 mod 干的」

- 只留 Core + 本 mod（+ 必须依赖）启动一次。
- 二分法：启用一半 mod 试一次，逐步收敛到具体哪个 mod。
- 别的 mod 完全可能用 `PatchOperationRemove` / `PatchOperationReplace` 按 defName 精准删掉或改掉你的 def；你自己的 `Patches/` 里也可能有这么一条，排查时先禁掉。
- 把日志按 defName 搜一遍，看有没有重复定义的记录。

## 7. 版本与安装层面的坑

- `About/About.xml`：`<packageId>` 必须唯一（`author.modname` 形式，小写）；1.4+ 需要 `<supportedVersions>` 列表（写你实际支持的版本）。版本不匹配会红字警告，可能被自动禁用。
- `packageId` 和别的 mod 撞了，会有一个静默不加载。
- mod 必须是一个文件夹，结构大致为：`About/`、`Defs/`、`Textures/`、`Patches/`、`Assemblies/`（有 C# 才需要）、可选的 `LoadFolders.xml`。
- 订阅版的本地缓存可能不是你以为的那一份；本地开发放 `RimWorld/Mods/` 直接测试最省心。

## 8. 最后一招：直接问 DefDatabase

如果 mod 有 C# 部分，最确定的验证是让游戏自己回答：

```csharp
var def = DefDatabase<ThingDef>.GetNamedSilentFail("MyMod_PlasmaRifle");
Log.Message(def == null
    ? "[probe] def 不存在"
    : $"[probe] 已加载 label={def.label} class={def.thingClass.Name}");
```

放在 `Mod` 的构造函数或任意开发者模式能触发的代码里，重启后看日志：

- `def 不存在` → 回到第 3、4、6 节。
- 存在但 `label` 不是你的 → 被别的 mod 同名覆盖了（第 5 节第 3 条）。

## 附：最小可加载骨架（示意）

父节点名以你游戏版本本体 `Data/Core/Defs/` 下的武器文件为准。**最稳的做法不是抄骨架，而是整段复制一个原版武器再改 defName / label / 贴图**：

```xml
<?xml version="1.0" encoding="utf-8"?>
<Defs>
  <ThingDef ParentName="BaseHumanMakeableGun">
    <defName>MyMod_PlasmaRifle</defName>
    <label>等离子步枪</label>
    <description>一把实验性步枪。</description>
    <graphicData>
      <texPath>Things/Weapons/MyMod_PlasmaRifle</texPath>
      <graphicClass>Graphic_Single</graphicClass>
    </graphicData>
    <verbs>
      <li>
        <verbClass>Verb_Shoot</verbClass>
        <hasStandardCommand>true</hasStandardCommand>
        <defaultProjectile>Bullet_ChargeRifle</defaultProjectile>
        <warmupTime>0.8</warmupTime>
        <range>25.9</range>
        <burstShotCount>3</burstShotCount>
        <ticksBetweenBurstShots>8</ticksBetweenBurstShots>
      </li>
    </verbs>
  </ThingDef>
</Defs>
```

## 十五分钟最短路径

1. 看模组列表里有没有这个 mod、启动有没有红字。
2. 打开 `Player.log`，搜自己的 XML 文件名和 defName。
3. 加探针 def，判断问题在「加载层」还是「def 内容层」。
4. 加载层 → 查扩展名、目录、根节点、语法错误、LoadFolders。
5. 内容层 → 用本体武器整段替换、只改 defName/label，跑通后二分加字段；同时只开 Core 排除覆盖。
6. 全程给所有 defName 加唯一前缀。

按这个顺序查，基本不需要猜。
