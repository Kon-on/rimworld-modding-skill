# 04 — XML PatchOperations

> **适用版本**: RimWorld 1.7（实测 1.7.4981 rev136） | **最后更新**: 2026-10-18
>
> ⚠️ **1.7 移除了 `PatchOperationSet`**（旧教程常见）——它不存在，要用属性操作就用 `PatchOperationAttributeSet`。可用类型全清单见下节（反射 `Verse.PatchOperation*` 实测）。


## 目录

- [概述](#概述)
- [XPath 选择器基础](#xpath选择器基础)
- [节点名与 Class 属性](#节点名与-class-属性)
- [1.7 可用的补丁操作（全清单）](#17-可用的补丁操作全清单)
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

## 节点名与 Class 属性

补丁文件长这样：

```xml
<?xml version="1.0" encoding="utf-8"?>
<Patch>
  <Operation Class="PatchOperationReplace">   <!-- 节点名固定为 Operation，具体类型由 Class 属性决定 -->
    <xpath>/Defs/ThingDef[defName="Gun_Revolver"]/statBases/RangedWeapon_Cooldown</xpath>
    <value><RangedWeapon_Cooldown>1.4</RangedWeapon_Cooldown></value>
  </Operation>
</Patch>
```

- 节点名是 `Operation`（**不是**操作类名），类型由 `Class` 属性给出（`DirectXmlToObject.ClassTypeOf` 对字面量 `"Class"` 特判）。
- `xpath` 用 `/Defs/…` 与 `Defs/…` 都能命中（原版两种写法都有）。
- 列表节点**默认是追加语义**：想整段替换父类给的列表，必须写 `<recipeUsers Inherit="False">`（原版 `Gun_ChargeRifle` 即此写法）。

## 1.7 可用的补丁操作（全清单）

反射 `Assembly-CSharp.dll` 实测 1.7 共 16 个 `Verse.PatchOperation*` 类型（3 个抽象基类不可直接用），**没有** `PatchOperationSet`：

| Class | 作用 | 必要子节点 |
|-------|------|-----------|
| `PatchOperationAdd` | 往容器/列表追加 | `xpath` + `value` |
| `PatchOperationReplace` | 替换匹配到的节点 | `xpath` + `value` |
| `PatchOperationRemove` | 删除匹配到的节点 | `xpath` |
| `PatchOperationInsert` | 把 `value` 插成匹配节点的**兄弟**，`<order>Prepend/Append</order>` 控制前后 | `xpath`（必须指向已存在的**子节点**）+ `value` |
| `PatchOperationAttributeSet` | 设置匹配节点上的**属性** | `xpath` + `attribute` + `value` |
| `PatchOperationAttributeAdd` | 添加属性（已存在则失败） | 同上 |
| `PatchOperationAttributeRemove` | 删除属性 | `xpath` + `attribute` |
| `PatchOperationAddModExtension` | 给 Def 追加 ModExtension | `xpath` + `value` |
| `PatchOperationSetName` | 重命名匹配节点 | `xpath` + `name` |
| `PatchOperationTest` | 断言 xpath 命中，失败即中止 | `xpath` |
| `PatchOperationSequence` | 顺序执行子操作，前一步失败则停止 | `operations` 列表 |
| `PatchOperationConditional` | 命中走 `match`，否则走 `nomatch` | `xpath` + `match`/`nomatch` |
| `PatchOperationFindMod` | 装了指定 mod 走 `match`，否则 `nomatch` | `mods` + `match`/`nomatch` |

> 原版自带的补丁里 `PatchOperationReplace` 24 处、`PatchOperationAdd` 3 处、`PatchOperationAttributeSet` 3 处；`Insert`/`Sequence`/`Test`/`SetName`/`AddModExtension` 在 1.7 原版 Data 里**没有先例**——能用，但出问题时要自己扛，别指望抄原版。

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

### 4. PatchOperationAttributeSet — 设置属性值

> 旧教程写的 `PatchOperationSet` 在 1.7 **不存在**（这个类已被移除）。改属性用下面这个；改节点内容用 Replace。

```xml
<Patch>
  <!-- 把某 Def 的 ParentName 换成另一个基类（原版 Royalty 就是这么给仿生肢换父类的） -->
  <Operation Class="PatchOperationAttributeSet">
    <xpath>Defs/ThingDef[defName="PowerClaw"]</xpath>
    <attribute>ParentName</attribute>
    <value>BodyPartProstheticMakeableBase</value>
  </Operation>
</Patch>
```

> 想改 `<label>` 这类**元素**而不是属性？那是 Replace（`<xpath>…/label</xpath>` + `<value><label>新名字</label></value>`），而且玩家可见文本应当走语言文件（DefInjected），不要在补丁里硬写中文/英文。

### 5. PatchOperationInsert — 插入

⚠️ **语义坑（本测试 mod 踩过）**：Insert 把 `value` 插到**匹配节点的同级**（兄弟位置），所以 `xpath` 必须指向"列表里已经存在的某一项"，**不能指向列表容器本身**。

```xml
<Patch>
  <!-- ✅ 正确：指向 tools 里已有的第一项，把新工具插到它前面 -->
  <Operation Class="PatchOperationInsert">
    <xpath>/Defs/ThingDef[defName="Gun_Revolver"]/tools/li[1]</xpath>
    <order>Prepend</order>  <!-- Prepend=插在匹配节点之前，Append=之后 -->
    <value>
      <li>
        <label>stock</label>
        <capacities><li>Blunt</li></capacities>
        <power>9</power>
        <cooldownTime>2</cooldownTime>
      </li>
    </value>
  </Operation>
</Patch>
```

```xml
<!-- ❌ 错误：xpath 指向列表容器 /tools。<li> 会被插到 <ThingDef> 的直接子级，
     而 ThingDef 没有名为 li 的字段 → 加载时抛 XML 字段错误（本测试 mod 首版即此写法，静态评审时拦下） -->
<xpath>/Defs/ThingDef[defName="Gun_Revolver"]/tools</xpath>
```

> 要往列表**追加**一项，用 `PatchOperationAdd` 指向容器（这是原版惯例）；只有当你要的插入位置不是列表末尾时才用 Insert。

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

1. **Patch 没生效 / 报错** — 游戏启动日志会给出**补丁文件路径 + 出错的 Class 与 xpath**，先读日志；xpath 大小写敏感，`defName` 必须与目标 Def 完全一致。
2. **路径对不对，不用开游戏也能验** — 用 .NET 的 XPath 直接对原版文件跑一遍：
   ```powershell
   $doc = New-Object System.Xml.XmlDocument
   $doc.Load("<RimWorld>\Data\Core\Defs\ThingDefs_Misc\Weapons\RangedIndustrial.xml")
   ($doc.SelectNodes('/Defs/ThingDef[defName="Gun_Revolver"]/tools/li[1]')).Count   # 期望 1
   ```
   写补丁前先确认"命中恰好 1 处"：命中 0 处 = 路径写错；命中多处 = 会误伤，要加限定。
3. **多个 patch 冲突** — 加载顺序由 mod 排序决定，后加载的 patch 最后应用；可以用 `PatchOperationConditional`/`PatchOperationTest` 做保险。
4. **想确认补丁目标 Def 是否被别的 mod 改过** — 用开发者模式的日志/Def 查看工具，或把日志贴出来按 `08-debugging.md` 的流程排查。

> 1.7 客户端可依赖的是：启动日志、游戏内开发者菜单（Dev mode）与上面这种外部 XPath 验证。看到旧文档里的"开发者控制台命令"时先在游戏里确认它确实存在，别照抄。

## 最佳实践

- ✅ 一个 Patch 文件只处理一类修改（如 `Patch_Vanilla_Weapons.xml`）
- ✅ 添加注释说明为什么要这样 patch（含原版出处文件与行号，便于以后复核）
- ✅ 使用精确的 XPath，避免误伤其他 Def；下手前用外部 XPath 确认"命中恰好 1 处"
- ✅ 列表要整段替换时写 `Inherit="False"`；只是追加就用默认追加语义
- ❌ 不要用 patch 修改其他 mod 的内部逻辑（用 Harmony 代替）
- ❌ 避免 patch 覆盖范围过大（如 `//li` 选中所有 li）
- ❌ 不要用 `PatchOperationSet`（1.7 不存在）
