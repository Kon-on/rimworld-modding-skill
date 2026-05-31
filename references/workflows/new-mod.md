# 工作流：从零创建一个新 Mod（测试版先行）

> 适用：第一次做 RimWorld mod，或开始一个全新项目

## 概述

所有 mod 创建遵循 **测试版先行** 原则：

1. **生成测试版**（快速验证功能是否正确）
2. **开发者进游戏测试**（Spawn、确认属性、检查红字）
3. **修复 bug**（直到确认无误）
4. **正规化**（清理命名、补全 About.xml、准备发布）

---

## 阶段一：生成测试版

### 第 0 步：配置 RimSage MCP（强烈推荐）

```bash
claude mcp add rimworld-source --transport http https://mcp.rimsage.com/mcp
```

> 首次索引需 30-60 分钟。不想用 MCP 时用 `RimWorld/Data/Core/Defs/` 本地文件替代。

### 第 1 步：确定 Mod 信息（测试版）

测试版使用宽松命名，方便快速迭代：

| 项目 | 测试版取值 | 说明 |
|------|-----------|------|
| Mod 名称 | `<功能描述> (Test)` | 如 "Rainbow Cat Sword (Test)" |
| packageId | `test.<功能名>` | 如 `test.rainbowcatsword`——标记为测试版 |
| 前缀 | 2-4 字符 | **用户自行选择**（如 `TST_`） |
| 作者 | **用户自行填写** | |
| 目标版本 | 1.6 | |
| namespace | `<前缀>.<Mod名>` | 用户根据前缀自行确定 |

### 第 2 步：验证原版结构（铁律）

**在生成任何 Def 之前，必须先查原版对应文件验证：**

1. 用 `grep` 搜索 `RimWorld/Data/Core/Defs/` 中类似物品
2. 读原版文件，确认 ParentName、字段名、枚举值
3. 只写已验证的字段

详见 SKILL.md 第 5 节 "铁律"。

### 第 3 步：创建测试版目录

在 `<RimWorld>/Mods/<ModName>Test/` 下创建：

```
<ModName>Test/
├── About/
├── Defs/ThingDefs/
├── Textures/Things/Item/
└── Patches/
```

### 第 4 步：生成 Def 和贴图

- 武器 → `templates/weapon-melee.xml` 或 `weapon-ranged.xml`
- 建筑 → `templates/building.xml`
- 服装 → 参考原版 `Apparel_Various.xml` 结构
- 植物 → 参考原版 `Plants_Cultivated.xml` 结构

**贴图**：测试版可以先用原版贴图路径（如 `Things/Plant/Rose`），正规化时再替换。

### 第 5 步：告知开发者测试方法

生成完成后，告诉开发者：

```
测试步骤：
1. 启动 RimWorld → Mod 列表勾选 "<ModName> (Test)"
2. Developer Mode → Spawn Thing → 搜索 defName
3. 确认：贴图正常 / 属性正确 / 无红字
4. 反馈：有 bug 说 bug，没问题说 "OK 可以正规化"
```

---

## 阶段二：测试 → 修复循环

开发者反馈后：

| 反馈 | 处理 |
|------|------|
| "OK / 没问题 / 可以正规化" | 进入阶段三：正规化 |
| "XX 报错了" | 读取 Player.log → 定位问题 → 修 XML → 让开发者重测 |
| "XX 属性不对" | 调整 statBases → 让开发者重测 |
| "贴图不显示" | 检查 texPath → 修复 → 重测 |

**此阶段不修改 About.xml 和 packageId**——保持测试版状态，快速迭代。

---

## 阶段三：正规化

开发者确认无 bug 后，执行 `workflows/formalize-mod.md`：

1. 清理 packageId（去掉 `test.` 前缀）
2. 补全 About.xml（正式名称、完整描述）
3. 替换测试贴图为正式贴图
4. 添加 Preview.png（640×360）
5. 可选：准备 Steam Workshop 发布

---

## 检查清单

**测试版通过标准：**
- [ ] Dev Mode 下 Spawn 成功
- [ ] 贴图正确显示
- [ ] 属性符合预期
- [ ] 无红字/白窗
- [ ] 开发者口头确认 "OK"
