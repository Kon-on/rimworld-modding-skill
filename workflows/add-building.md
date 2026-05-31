# 工作流：添加一个新建筑

> 适用：添加工作台、发电机、家具、防御设施等建筑

## 步骤

### 第 1 步：确定建筑设计

列出建筑的基本属性：
- **名称**
- **占地面积**（如 1×1, 2×2, 3×2）
- **功能**：生产 / 电力 / 存储 / 防御 / 装饰 / 其他
- **贴图**：推荐尺寸 = 格数 × 256px

### 第 2 步：准备贴图

1. 创建建筑贴图（尺寸 = 宽×高 格数 × 256）
2. 放入 `Textures/Things/Building/`
3. 如需旋转，准备对应的旋转贴图（`_east`, `_north`, `_south` 后缀）

### 第 3 步：编写 BuildingDef

使用 `templates/building.xml` 模板，参考 `references/03-xml-defs.md` 建筑部分。

**注意**：
- `<size>` 决定建筑占几格
- `<designationCategory>` 决定在哪个建造菜单中出现
- `<passability>` 决定小人和物品能否通过

### 第 4 步：添加交互组件（可选）

根据建筑功能添加对应的 Comp：

| 功能 | Comp Class |
|------|-----------|
| 电力消耗 | `CompProperties_Power` |
| 电力生产 | `CompProperties_Power` + `<basePowerConsumption>正值</basePowerConsumption>` |
| 可工作 | `CompProperties_WorkTable` |
| 存储物品 | `CompProperties_Storage` |
| 可加热/制冷 | `CompProperties_TempControl` |
| 可研究 | `CompProperties_ResearchBench` |
| 可建造屋顶 | `CompProperties_Roof` |

### 第 5 步：添加配方（如果是工作台）

如果建筑是工作台，需要指定它可以制作哪些配方：

```xml
<ThingDef>
  ...
  <recipes>
    <li>SR_PlasmaSword</li>
    <li>Brewing</li>
  </recipes>
  ...
</ThingDef>
```

或者通过 Patch 给原版建筑添加配方（参考 `references/04-xml-patching.md`）。

### 第 6 步：设置研究前置（可选）

```xml
<researchPrerequisites>
  <li>Electricity</li>
  <li>MicroelectronicsBasics</li>
</researchPrerequisites>
```

### 第 7 步：测试

1. 启动游戏，启用 Developer Mode + God Mode
2. 在 **Architect** 菜单中找到你的建筑分类
3. 放置建筑，确认：
   - [ ] 建筑正常放置在地图上
   - [ ] 贴图正确显示（旋转后也正确）
   - [ ] 占用格数正确
   - [ ] 小人和物品正确交互（通过/使用）
4. 如果是工作台：确认配方列表正确

## 常见问题

### Q: 建筑放置后贴图错位？
检查 `<fillPercent>` 和 `<drawSize>`，建筑默认 `<fillPercent>` 为 1.0。

### Q: 建筑在建造菜单中找不到？
检查 `<designationCategory>` 拼写是否正确，常见值：`Production`, `Furniture`, `Structure`, `Power`, `Temperature`, `Security`, `Recreation`, `Misc`。

### Q: 建筑无法通电？
确认添加了 `<li Class="CompProperties_Power">` 组件。
