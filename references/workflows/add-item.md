# 工作流：添加一个新物品

> 适用：添加武器、服装、材料、消耗品等可移动物品

## 步骤

### 第 1 步：确定物品设计

列出物品的基本属性：
- **名称**：游戏中显示的名称
- **类型**：武器 / 服装 / 材料 / 消耗品 / 其他
- **贴图**：需要一张 PNG 贴图（参考 `references/07-assets.md`）
- **配方**：如何获得？制作 / 交易 / 掉落？

### 第 2 步：准备贴图

1. 创建 PNG 贴图（推荐 128×128）
2. 放入 `Textures/Things/Item/` 目录
3. 命名：`<Prefix>_<ItemName>.png`

### 第 3 步：编写 ThingDef

在 `Defs/ThingDefs/` 下创建 XML 文件：

- **武器**：使用 `templates/weapon-melee.xml`（近战）或 `templates/weapon-ranged.xml`（远程）
- **服装**：继承 `ApparelBase`，参考原版 `Defs/ThingDefs/Apparel/` 下的服装写法
- **材料/消耗品**：继承 `ResourceBase` 或自定义

参考 `references/03-xml-defs.md` 了解完整标签说明。

### 第 4 步：添加配方（可选）

如果物品需要制作获得，在 `Defs/RecipeDefs/` 下创建配方文件，使用 `templates/recipe.xml` 模板。

### 第 5 步：注册到物品分类

确保 `<thingCategories>` 中包含正确的分类标签：

| 分类 | 用途 |
|------|------|
| `WeaponsMelee` | 近战武器 |
| `WeaponsRanged` | 远程武器 |
| `Apparel` | 服装 |
| `ResourcesRaw` | 原材料 |
| `Manufactured` | 加工品 |
| `Foods` | 食物 |
| `Medicine` | 药品 |

### 第 6 步：测试

1. 启动游戏，启用 Developer Mode
2. Open Debug Actions Menu → **Spawn Thing**
3. 搜索你的物品 defName
4. 确认：
   - [ ] 物品正常生成在地图上
   - [ ] 贴图正确显示
   - [ ] 可被捡起/装备（如果是可装备物品）
   - [ ] 属性（伤害/耐久/价值）符合预期
5. 如果配置了配方，在对应工作台中确认配方出现

### 第 7 步：本地化（可选）

在 `Languages/English/Keyed/` 下添加 `Strings.xml` 实现多语言支持（即使只支持英文也建议添加）。

## 常见问题

### Q: 物品生成了但看不到贴图？
检查 `<texPath>` 是否正确，确认 PNG 在 `Textures/` 下的路径匹配。

### Q: 物品没有出现在任何库存区？
检查 `<thingCategories>` 标签是否正确，确认分类名拼写无误。

### Q: 配方没有出现在工作台上？
检查 `<recipeUsers>` 是否正确指定工作台 defName（如 `TableMachining`）。
