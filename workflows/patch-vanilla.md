# 工作流：修改原版内容

> 适用：调整原版（或其他 mod）的物品/建筑/机制

## 选择修改方式

```
想修改什么？
│
├─ 数值/属性（伤害、成本、贴图、分类...）
│   └─ 使用 XML PatchOperations（修改数据）⭐ 简单
│
├─ 行为/逻辑（AI 决策、战斗计算、生成规则...）
│   └─ 使用 Harmony 补丁（修改代码）⭐ 中等难度
│
└─ 两者都需要
    └─ XML Patch 改数据 + Harmony 改逻辑
```

## 方式 1：XML PatchOperations

详见 `references/04-xml-patching.md`。

### 完整流程

1. 确定要修改的目标 Def 的 defName
2. 用 dnSpy 打开 Assembly-CSharp.dll，或查看 `RimWorld/Data/Core/Defs/` 确认 Def 的 XML 结构
3. 编写 XPath 选择器定位目标节点
4. 在 `Patches/` 下创建 Patch 文件
5. 测试

### 示例：降低原版物品成本

```xml
<?xml version="1.0" encoding="utf-8"?>
<Patch>
  <!-- 将防弹衣的材料成本从 150 降到 80 -->
  <Operation Class="PatchOperationReplace">
    <xpath>/Defs/ThingDef[defName="Apparel_ArmorVest"]/costList/Steel</xpath>
    <value>
      <Steel>80</Steel>
    </value>
  </Operation>
</Patch>
```

## 方式 2：Harmony 补丁

详见 `references/06-harmony.md`。

### 完整流程

1. 确定要修改的目标方法（类名 + 方法名）
2. 用 dnSpy 或 RimSage 查看方法签名（参数类型、返回类型）
3. 决定使用 Prefix（前置拦截）、Postfix（后置拦截）还是 Transpiler
4. 编写 patch 代码（使用 `templates/harmony-patch.cs`）
5. 编译 → 放入 Assemblies/ → 测试

### 示例：修改战斗伤害计算

```csharp
[HarmonyPatch(typeof(Verb_MeleeAttack), "GetDamageAmount")]
public static class Patch_GetDamageAmount
{
    [HarmonyPostfix]
    public static void Postfix(ref float __result, Verb_MeleeAttack __instance)
    {
        // 如果是 SR_ 特殊武器，伤害翻倍
        if (__instance.EquipmentSource?.def.defName?.StartsWith("SR_") == true)
        {
            __result *= 2f;
        }
    }
}
```

## 测试流程

### XML Patch 测试
1. 确保 Patch 文件在 `Patches/` 下
2. 启动游戏 → 开发者模式下 spawn 目标物品
3. 检查属性是否按预期变化
4. 关闭其他 mod 测试是否冲突

### Harmony Patch 测试
1. 确认 `[StaticConstructorOnStartup]` 入口类的 `Log.Message()` 在 Player.log 中出现
2. 在 patch 方法中添加 `Log.Message()` 确认被调用
3. 测试目标行为是否按预期变化
4. 测试边界情况：保存/读档 后行为是否正常

## 常见问题

### Q: XML Patch 没生效？
检查 XPath 是否精确匹配目标 defName，检查 Patch 文件是否在 `Patches/` 目录下（不是 `Defs/`）。

### Q: Harmony 补丁和另一个 mod 冲突？
两个 mod patch 了同一个方法。用 Harmony ID + `[HarmonyPriority]` 控制执行顺序。

### Q: 修改后存档坏了？
这是 mod 开发的日常——建议用单独的测试存档。XML Patch 修改数据通常安全，C# 修改逻辑可能破坏存档兼容。
