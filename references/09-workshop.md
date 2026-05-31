# 09 — Steam Workshop 发布

> **适用版本**: RimWorld 1.6 | **最后更新**: 2026-05-31


## 目录

- [发布前检查清单](#发布前检查清单)
- [Steam Workshop 上传步骤](#steamworkshop上传步骤)
- [版本管理](#版本管理)
- [Mod 描述最佳实践](#mod描述最佳实践)
- [兼容性声明](#兼容性声明)
- [更新 Mod](#更新mod)
- [常见问题](#常见问题)

## 发布前检查清单

在发布前确认以下所有项：

- [ ] **About.xml** 完整且正确：`packageId` 唯一，`name` 和 `description` 已填写
- [ ] **Preview.png** 存在且尺寸为 640×360
- [ ] ⚖️ **法律自查**：无抄袭原版源码、无盗用其他 mod 资产、无第三方 IP 侵权
- [ ] **贴图/音效均为原创**或使用合规免费素材
- [ ] **目录结构**正确（无多余文件，如 `.git/`、`obj/`、`Source/`）
- [ ] **Def 测试**通过（开发者模式下 spawn 所有物品正常）
- [ ] **无红字错误**（检查 Player.log）
- [ ] **兼容性测试**完成（与主要 DLC 和热门 mod 无冲突）
- [ ] **版本号**已设定（`About.xml` 或 `ModSync.xml`）

## Steam Workshop 上传步骤

### 方法 1：游戏内直接上传（推荐）

1. 启动 RimWorld
2. 主菜单 → **Mod**
3. 找到你的 mod → 点击右侧 **"上传到创意工坊"（Upload to Steam Workshop）**
4. 填写信息：
   - **标题（Title）**：Mod 显示名称
   - **描述（Description）**：使用 BBCode 格式
   - **预览图（Preview Image）**：`About/Preview.png`
   - **标签（Tags）**：选择合适的标签
   - **可见性（Visibility）**：公开 / 仅好友 / 隐藏
5. 点击 **发布（Publish）**

### 方法 2：手动上传（高级）

1. 将 mod 文件夹放入：
   ```
   <Steam>/steamapps/workshop/content/294100/<WorkshopID>/
   ```
2. 使用 SteamCMD 上传（见 Valve 官方文档）

## 版本管理

### 语义化版本

使用 `major.minor.patch` 格式：

```
1.0.0  → 第一个正式版
1.0.1  → 修复 bug
1.1.0  → 新增功能，向后兼容
2.0.0  → 重大更新，可能不兼容旧存档
```

### ModSync.xml（可选）

```xml
<?xml version="1.0" encoding="utf-8"?>
<ModSync>
  <version>1.0.0</version>
  <updateNotes>
    1.0.0: Initial release
    1.0.1: Fixed NullReferenceException in combat
    1.1.0: Added plasma rifle variant
  </updateNotes>
</ModSync>
```

## Mod 描述最佳实践

### 好描述的结构

一个优秀的 Workshop 描述应包含：

```
[简短的一句话介绍——用最吸引人的方式说明你的 mod 做什么]

[详细说明——特性列表]
- 特性 1：xxx
- 特性 2：xxx
- 特性 3：xxx

[兼容性]
- 兼容 1.6
- 需要/不兼容的 DLC
- 已知兼容/冲突的 mod

[安装方式]
- 订阅即可，在 Mod 列表中启用

[FAQ]
Q: xxx?
A: xxx

[反馈/建议]
- Steam 评论区
- GitHub Issues: <link>
- Discord: <link>

[鸣谢]
- 致谢名单
```

## 兼容性声明

```markdown
## Compatibility

### Required
- Harmony (自动订阅)

### Supported DLCs
- ✅ Core (1.6)
- ✅ Royalty
- ✅ Ideology
- ✅ Biotech
- ⚠️ Anomaly (部分兼容)

### Known Conflicts
- ❌ Combat Extended v1.5+ (需要兼容补丁)
- ⚠️ Vanilla Weapons Expanded (加载顺序：本 mod 放后面)
```

## 更新 Mod

1. 修改代码/XML
2. 更新版本号
3. 在 Workshop 页面点击 **"更新"（Update）**
4. 填写更新日志（Changelog）

### 更新注意事项
- **XML 修改通常兼容旧存档**，可以在 changelog 中说明
- **C# 修改可能破坏存档**，务必在 changelog 中注明 `⚠️ 需要新游戏`
- **删除 Def 会破坏所有引用该 Def 的存档**——用 `[Obsolete]` 标记而不是直接删除

## 常见问题

### Q: 上传后 mod 列表中不显示？
等待 Steam 同步（通常几分钟），重启游戏。

### Q: 其他人订阅后报错？
确认你的 mod 不依赖本地绝对路径，检查所有引用的 DLL 是否已打包到 `Assemblies/`。

### Q: 如何删除已发布的 mod？
Steam Workshop 不允许完全删除，但可以设为"隐藏"。在 Workshop 页面 → 可见性 → 隐藏。
