# 工作流：正规化 Mod（测试版 → 正式版）

> 触发条件：开发者确认测试版无 bug，口头说 "OK / 可以正规化 / 没问题"

## 概述

将测试版 mod 升级为正式版，清理临时命名、补全元信息、准备发布。

---

## 步骤

### 第 1 步：确认正规化信息

请开发者确认以下最终信息：

| 项目 | 测试版（当前） | 正式版（需确认） |
|------|--------------|-----------------|
| Mod 名称 | `<名> (Test)` | **去掉 (Test)**，或改为正式名 |
| packageId | `test.xxx` | **去掉 `test.` 前缀**，如 `konon.rainbowcatsword` |
| 作者 | （已有） | **确认无误** |
| 描述 | 简单描述 | **补全为正式描述**（英文+中文） |
| 贴图 | 测试用占位贴图 | **替换为正式贴图** |
| 前缀 | （可保留） | **确认是否要改** |

### 第 2 步：更新 About.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<ModMetaData>
  <packageId>konon.modname</packageId>          <!-- 去掉 test. 前缀 -->
  <name>正式 Mod 名称</name>                     <!-- 去掉 (Test) -->
  <author>开发者确认的作者名</author>
  <supportedVersions><li>1.6</li></supportedVersions>
  <description>完整的 mod 描述。\n\n包含特性列表、使用方法等。</description>
</ModMetaData>
```

### 第 3 步：替换正式贴图

- 如果测试版用了占位贴图（原版路径），现在替换为你的正式 PNG
- 更新 `<texPath>` 指向正式贴图文件
- 贴图规范见 `references/07-assets.md`
- 添加 `About/Preview.png`（640×360，Steam Workshop 预览图）

### 第 4 步：清理测试残留

- [ ] 检查所有 defName，确认没有临时命名（如 `TST_Test_xxx`）
- [ ] 检查所有 XML 注释，清理调试用注释
- [ ] 确认 `Patches/` 中没有测试用的临时 Patch
- [ ] 如果有 C# DLL，确认编译模式改为 Release

### 第 5 步：最终验证

在游戏内做最后一次完整测试：

- [ ] Mod 列表显示正式名称（无 "(Test)"）
- [ ] Spawn 所有物品/建筑正常
- [ ] 贴图全部正确显示
- [ ] 查看 Player.log 无红字
- [ ] 存档/读档正常

---

## 之后：发布到 Steam Workshop？

如果开发者想发布，加载 `references/09-workshop.md` 进行 Steam Workshop 上传。

不想发布也可以——mod 在本地 Mods 文件夹里就能正常使用。

---

## 检查清单

- [ ] packageId 已去掉 `test.` 前缀
- [ ] About.xml 名称、作者、描述全部补全
- [ ] 正式贴图就位，占位贴图已移除
- [ ] Preview.png 已添加
- [ ] 无测试残留命名
- [ ] 最终游戏测试通过
