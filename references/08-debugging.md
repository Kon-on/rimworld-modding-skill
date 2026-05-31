# 08 — 调试与排错

> **适用版本**: RimWorld 1.6 | **最后更新**: 2026-05-31

## 开发者模式

### 启用方式
1. 游戏主菜单 → **选项（Options）**
2. 勾选 **"开发者模式（Development Mode）"**
3. 屏幕顶部出现一排开发工具按钮

### 常用开发工具
- **Open Debug Actions Menu**（⚙️ 图标）→ 最常用的工具集
  - `Spawn Thing` — 直接生成物品测试
  - `Execute Incident` — 触发任意事件
  - `Apply Damage` — 对选中对象施加伤害
  - `Give Hediff` — 施加健康效果
- **Open Debug Log** — 查看实时日志
- **God Mode** — 无敌模式 + 免费建造

## 日志文件

### Player.log 位置

| 系统 | 路径 |
|------|------|
| Windows | `%USERPROFILE%\AppData\LocalLow\Ludeon Studios\RimWorld by Ludeon Studios\Player.log` |
| Linux | `~/.config/unity3d/Ludeon Studios/RimWorld by Ludeon Studios/Player.log` |
| macOS | `~/Library/Logs/Ludeon Studios/RimWorld by Ludeon Studios/Player.log` |

### 日志解读

```
[<你的packageId>] Harmony patches applied.     ← 你的 mod 正常启动
Could not resolve cross-reference to ...      ← XML Def 引用错误
NullReferenceException: Object reference not set  ← C# 空引用错误
```

### 输出自定义日志

```csharp
// 信息级别
Log.Message($"SR: Processing {thing.Label}");

// 警告级别（黄色）
Log.Warning($"SR: Missing texture for {thing.def.defName}");

// 错误级别（红色）
Log.Error($"SR: Failed to load {thing.def.defName}, reason: {ex.Message}");
```

## 常见错误速查

### 🔴 红字错误（游戏内弹窗）

| 错误信息 | 可能原因 | 解决方法 |
|----------|---------|---------|
| `Could not resolve cross-reference to ...` | defName 拼写错误或目标 Def 不存在 | 检查 XML 中的 defName 引用，确认目标 Def 已加载 |
| `Could not find type ...` | C# 类名错误或 DLL 未加载 | 检查 XML 中的 `Class=` 属性，确认 DLL 在 Assemblies/ 中 |
| `XML error: unexpected token` | XML 语法错误（标签未闭合） | 用 XML 验证器检查文件格式 |
| `Duplicate defName: ...` | 两个 Def 使用了相同的 defName | 确保你的前缀是唯一的 |

### ⬜ 白窗/灰窗（游戏加载时卡住）

1. **最近安装的 mod 冲突**——二分法排查：禁用一半 mod，逐步缩小范围
2. **XML 解析错误**——检查最后修改的 XML 文件是否有标签未闭合
3. **DLL 依赖缺失**——确认所有引用的 DLL 都已正确打包

### ❌ NullReferenceException

最常见的 C# 错误。原因：访问了为 `null` 的对象。

```csharp
// ❌ 危险写法
Pawn pawn = Find.AnyThing<Pawn>();
pawn.health.AddHediff(someHediff);  // pawn 可能为 null

// ✅ 安全写法
Pawn pawn = Find.AnyThing<Pawn>();
if (pawn != null)
{
    pawn.health.AddHediff(someHediff);
}
// 或使用模式匹配
if (Find.AnyThing<Pawn>() is Pawn pawn)
{
    pawn.health.AddHediff(someHediff);
}
```

## 隔离测试流程

当怀疑是 mod 冲突时：

1. 只加载你的 mod + Harmony + Core
2. 确认问题是否复现
   - **不复现** → mod 冲突，二分法找出冲突 mod
   - **复现** → 你的 mod 有 bug，进入下一步
3. 查看 Player.log，搜索你的 mod 前缀
4. 在可疑代码处加入 `Log.Message()` 输出变量值
5. 逐步缩小问题范围

## 开发中快速重载

- 修改 XML → 不需要重启游戏，在主菜单点击 **"Reset Mods"** 或直接开始新游戏
- 修改 C# 代码 → 必须重新编译 + 重启游戏
- 修改纹理 → 直接替换文件，游戏可能缓存需要重启

## 常见问题 FAQ

### Q: 为什么我的 mod 在 Mod 列表中不显示？
检查 About.xml 是否语法正确，`packageId` 是否与其他 mod 重复。

### Q: 开发模式下物品怎么生成？
Open Debug Actions Menu → Spawn Thing → 搜索你的物品 defName → 点击生成。

### Q: Harmony 补丁没有生效？
1. 确认 `[StaticConstructorOnStartup]` 类被正确调用（检查 Log.Message 输出）
2. 确认 patch 类的访问修饰符是 `public static`
3. 确认补丁所在的 DLL 在 Assemblies/ 中
