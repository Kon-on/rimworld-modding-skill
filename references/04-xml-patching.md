# 04 — XML PatchOperations

> **适用版本**: RimWorld 1.6 | **最后更新**: 2026-05-31


## 目录

- [概述](#概述)
- [XPath 选择器基础](#xpath选择器基础)
- [五种 Patch 操作](#五种patch操作)
- [条件补丁](#条件补丁)
- [实战示例](#实战示例)
- [调试 Patch](#调试patch)
- [最佳实践](#最佳实践)

## 概述

PatchOperations 让你在不修改原版文件的情况下，修改原版（或其他 mod）的 XML Def。所有补丁放在 `Patches/` 目录下，游戏加载时自动应用。

**核心优势**：多个 mod 可以 patch 同一个 Def 而不会互相覆盖。

## XPath 选择器基础

Patch 使用 XPath 定位要修改的 XML 节点：

| XPath 表达式 | 说明 | 示例 |
|-------------|------|------|
| `/Defs` | 根节点 | `/Defs` |
| `/Defs/ThingDef[defName="Gun_Revolver"]` | 按 defName 精确匹配 | 选中左轮手枪 |
| `/Defs/ThingDef[defName="Gun_Revolver"]/statBases` | 选中 statBases 节点 | |
| `*/li[1]` | 第一个 li 子元素 | 选中列表第一项 |
| `*[MayRequire="ludeon.rimworld.biotech"]` | 按属性匹配 | 条件加载的节点 |

## 五种 Patch 操作

### 1. PatchOperationAdd — 添加

```xml
<?xml version="1.0" encoding="utf-8"?>
<Patch>
  <!-- 给左轮手枪添加一个武器标签 -->
  <Operation Class="PatchOperationAdd">
    <xpath>/Defs/ThingDef[defName="Gun_Revolver"]/weaponTags</xpath>
    <value>
      <li>SR_QuickDraw</li>
    </value>
  </Operation>
</Patch>
```

### 2. PatchOperationRemove — 删除

```xml
<Patch>
  <!-- 删除左轮手枪的武器标签 -->
  <Operation Class="PatchOperationRemove">
    <xpath>/Defs/ThingDef[defName="Gun_Revolver"]/weaponTags/li[.="SimpleGun"]</xpath>
  </Operation>
</Patch>
```

### 3. PatchOperationReplace — 替换

```xml
<Patch>
  <!-- 替换左轮手枪的市场价值 -->
  <Operation Class="PatchOperationReplace">
    <xpath>/Defs/ThingDef[defName="Gun_Revolver"]/statBases/MarketValue</xpath>
    <value>
      <MarketValue>500</MarketValue>
    </value>
  </Operation>
</Patch>
```

### 4. PatchOperationSet — 设置属性值

```xml
<Patch>
  <!-- 修改左轮手枪的标签文本 -->
  <Operation Class="PatchOperationSet">
    <xpath>/Defs/ThingDef[defName="Gun_Revolver"]/label</xpath>
    <value>heavy revolver</value>
  </Operation>
</Patch>
```

### 5. PatchOperationInsert — 插入

```xml
<Patch>
  <!-- 在 recipeMaker 的第一个子元素之前插入研究前置 -->
  <Operation Class="PatchOperationInsert">
    <xpath>/Defs/ThingDef[defName="Gun_Revolver"]/recipeMaker/*[1]</xpath>
    <order>Prepend</order>  <!-- Prepend=之前 Append=之后 -->
    <value>
      <researchPrerequisite>Gunsmithing</researchPrerequisite>
    </value>
  </Operation>
</Patch>
```

## 条件补丁

### PatchOperationConditional — 按条件决定是否执行

```xml
<Patch>
  <!-- 仅在 CE (Combat Extended) 激活时执行 -->
  <Operation Class="PatchOperationConditional">
    <xpath>/Defs/ThingDef[defName="Gun_Revolver"]</xpath>
    <nomatch Class="PatchOperationFindMod">
      <mods>
        <li>Combat Extended</li>
      </mods>
      <match Class="PatchOperationAdd">
        <xpath>/Defs/ThingDef[defName="Gun_Revolver"]/statBases</xpath>
        <value>
          <Bulk>2.0</Bulk>
        </value>
      </match>
    </nomatch>
  </Operation>
</Patch>
```

### PatchOperationFindMod — 按 mod 存在性匹配

```xml
<Patch>
  <!-- 仅在 Vanilla Expanded Framework 存在时执行 -->
  <Operation Class="PatchOperationFindMod">
    <mods>
      <li>Vanilla Expanded Framework</li>
    </mods>
    <match Class="PatchOperationAdd">
      <xpath>/Defs/ThingDef[defName="Gun_Revolver"]/comps</xpath>
      <value>
        <li Class="VFECore.CompProperties_ToggleableOverlay">
          <graphicData>
            <texPath>Things/Item/SR_RevolverOverlay</texPath>
          </graphicData>
        </li>
      </value>
    </match>
  </Operation>
</Patch>
```

## 实战示例

### 示例 1：修改原版武器伤害

```xml
<?xml version="1.0" encoding="utf-8"?>
<Patch>
  <!-- 将左轮手枪的伤害从 12 提升到 18 -->
  <Operation Class="PatchOperationReplace">
    <xpath>/Defs/ThingDef[defName="Gun_Revolver"]/tools/li/power</xpath>
    <value>
      <power>18</power>
    </value>
  </Operation>
</Patch>
```

### 示例 2：给原版工作台添加配方

```xml
<?xml version="1.0" encoding="utf-8"?>
<Patch>
  <!-- 给机械加工台添加等离子长剑的配方 -->
  <Operation Class="PatchOperationAdd">
    <xpath>/Defs/ThingDef[defName="TableMachining"]/recipes</xpath>
    <value>
      <li>SR_PlasmaSword</li>
    </value>
  </Operation>
</Patch>
```

### 示例 3：修改原版建筑贴图

```xml
<?xml version="1.0" encoding="utf-8"?>
<Patch>
  <!-- 用自定义贴图替换研究台的外观 -->
  <Operation Class="PatchOperationReplace">
    <xpath>/Defs/ThingDef[defName="HiTechResearchBench"]/graphicData/texPath</xpath>
    <value>
      <texPath>Things/Building/SR_ResearchBench</texPath>
    </value>
  </Operation>
</Patch>
```

## 调试 Patch

1. **路径不对怎么办？** — 在游戏中用开发者控制台输入 `list defs` 查看 Def 实际结构
2. **Patch 没生效？** — 检查 XPath 是否精确匹配，大小写敏感
3. **多个 patch 冲突？** — 加载顺序由 mod 排序决定，后加载的 patch 最后应用

## 最佳实践

- ✅ 一个 Patch 文件只处理一类修改（如 `Patch_Vanilla_Weapons.xml`）
- ✅ 添加注释说明为什么要这样 patch
- ✅ 使用精确的 XPath，避免误伤其他 Def
- ❌ 不要用 patch 修改其他 mod 的内部逻辑（用 Harmony 代替）
- ❌ 避免 patch 覆盖范围过大（如 `//li` 选中所有 li）
