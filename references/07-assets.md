# 07 — 资源制作

> **适用版本**: RimWorld 1.7（实测 1.7.4981 rev136） | **最后更新**: 2026-10-18
>
> 本文的尺寸与朝向结论来自**原版 1.7 资产实测**（安装根 `Assets.zip` 内的 `.dds`，逐张读宽高与 alpha 边界），
> 不是"经验值"。旧文档里的 256×256、1×1 建筑 256×256 等说法与 1.7 原版不符，已按实测改写。

## 目录

- [1.7 的资源形态（与 1.6 的差异）](#17-的资源形态与-16-的差异)
- [纹理格式规范](#纹理格式规范)
- [尺寸：跟随同类原版资产](#尺寸跟随同类原版资产)
- [贴图路径约定（原版实测）](#贴图路径约定原版实测)
- [穿戴贴图（wornGraphicPath）](#穿戴贴图wornGraphicpath)
- [Graphic_Single 还是 Graphic_Random](#graphic_single-还是-graphic_random)
- [着色器类型](#着色器类型)
- [Mask 图层（染色系统）](#mask图层染色系统)
- [音效资源](#音效资源)
- [工具推荐](#工具推荐)
- [常见问题](#常见问题)

## 1.7 的资源形态（与 1.6 的差异）

| 事项 | 1.6 及更早 | **1.7 实测** |
|---|---|---|
| 原版贴图存放位置 | `Data/Core/Textures/**`（散装 png） | **在游戏安装根的 `Assets.zip` 里**（358,892,126 字节），`Data/Core/Textures` 目录**已不存在** |
| zip 里的格式与命名 | png | 每个资源是 `<原路径原名>.dds`，压缩方式为 **Zstd（zip method 93）** |
| 怎么读出来看 | 直接打开 png | Python `zipfile` 会报 `That compression method is not supported`；用 **Node 24** 的 `zlib.zstdDecompressSync` 解 |
| mod 自己的资源 | `Textures/**` 散装 png | **照旧**：mod 用散装 `Textures/**`（PNG），游戏会加载；本仓库的 44 文件测试 mod 就是全散装 PNG，静态核验通过 |

> 想核对自己的贴图尺寸/朝向？最省事的路子是**先把原版同类资产取出来量一遍**，再决定自己画多大。
> 取原版资产的脚本思路见 `docs/verify-testmod.mjs` 与测试 mod 的贴图生成脚本
> `examples/rimtest-mod/RimTestMod/Source/make-textures.py`（含 `--contact-sheet` 出总览图）。

## 纹理格式规范

### 基本要求
- **格式**：PNG（必须）
- **背景**：透明（Alpha 通道）
- **色彩模式**：RGB + Alpha
- **尺寸**：2 的幂**不是**必须的（原版有 128×128、64×64、32×32 等，跟随同类资产即可）
- ⚖️ **版权**：贴图必须原创——不得从其他游戏/网站直接提取，不得使用第三方 IP 角色

### 内容边界（比画布尺寸更重要）
原版几乎不在画布边缘作画：武器的实际像素只占画布中段（下面有实测 bbox）。
画的时候把图形**水平居中、四周留白**，游戏按 alpha 边界定位，不会因为画布大就变大。

## 尺寸：跟随同类原版资产

| 内容类型 | 原版实测尺寸 | 备注 |
|---------|------------|------|
| 近战/远程武器图标 | **128×128** | 内容水平放置：长剑实际像素 bbox ≈ (0, 50, 128, 71)，突击步枪 ≈ (0, 49, 128, 98) |
| 服装/护甲图标 | **128×128** | 例：防弹夹克 128×128，内容几乎占满（bbox ≈ (0,4,128,127)） |
| 穿戴贴图（四向） | **128×128** | 与人形身体贴图同一坐标系 |
| 工作台 | **128×128** | |
| 材料/资源 | **64×64** | 例：`Steel_a` 64×64 |
| 植物 | **64×64** | |
| 子弹/弹丸 | **32×32** | |
| 1×1 建筑 | **64×64 ~ 128×128 都正常** | 原版 `CraftingSpot` 是 64×64；不要迷信"1 格必须 256×256" |
| Preview.png | **640×360** | Steam 创意工坊预览图（About/Preview.png） |

> **武器不要预旋转 45°**：原版武器贴图一律水平绘制（上面 bbox 已证），游戏内的倾斜角度由 Def 的
> `<equippedAngleOffset>`（原版近战常见 -65）控制。预先转了 45° 的贴图在游戏里会转两次。
> 本仓库的贴图生成脚本早期版本就犯过这个错，返工记录见 `docs/verify-testmod.mjs` 的核验项与
> `examples/rimtest-mod/核验报告.md`。

## 贴图路径约定（原版实测）

```
Textures/
├── Things/
│   ├── Item/Equipment/WeaponMelee/        ← 近战武器图标（原版 ExampleName 平铺单文件）
│   ├── Item/Equipment/WeaponRanged/       ← 远程武器图标
│   ├── Item/Resource/                     ← 材料（如 Steel_a.png；变体加 _a/_b/_c 后缀）
│   ├── Building/Production/               ← 工作台等生产建筑
│   ├── Projectile/                        ← 弹丸（如 Bullet_Revolver.png）
│   ├── Plant/                             ← 植物
│   └── Pawn/Humanlike/Apparel/<Name>/<Name>  ← 服装**穿戴**贴图（目录形式，见下节）
├── UI/                                    ← UI 图标
└── Effects/                               ← 特效
```

在 XML 中引用时去掉 `Textures/` 前缀和 `.png` 后缀：
```xml
<texPath>Things/Item/Equipment/WeaponRanged/MyRifle</texPath>
<!-- 对应文件: Textures/Things/Item/Equipment/WeaponRanged/MyRifle.png -->
```

## 穿戴贴图（wornGraphicPath）

服装的"穿在身上"的贴图不是单文件，而是**一个名字 + 一组按朝向/体型命名的文件**：

```xml
<apparel>
  <wornGraphicPath>Things/Pawn/Humanlike/Apparel/MyVest/MyVest</wornGraphicPath>
</apparel>
```

对应磁盘上（`.png` 省略）：

```
Textures/Things/Pawn/Humanlike/Apparel/MyVest/
├── MyVest_south.png      ← 朝南（正面）
├── MyVest_north.png      ← 朝北（背面）
├── MyVest_east.png       ← 朝东（侧面）
└── MyVest_west.png       ← 朝西（镜面，部分 mod 直接复制 east）
```

要点：
- 原版护甲常再按**体型**细分：`MyVest_male_south.png` / `_female_` / `_thin_` / `_fat_` / `_hulk_`；只画一套（无体型后缀）也能用。
- 物品栏/地面上的**图标**用 `<graphicData><texPath>`：原版惯例是同一个目录里再放一个无后缀的 `MyVest.png` 当图标；
  也可以另起目录（如 `Things/Item/Equipment/Apparel/MyVest`），路径对上即可。
- 少画一个朝向 → 该朝向显示紫块/空白；四向齐全最稳。

## Graphic_Single 还是 Graphic_Random

| graphicClass | texPath 应该是 | 用途 |
|---|---|---|
| `Graphic_Single` | **单个文件**（`Things/Plant/MyFlower`） | 绝大多数情况：一个物品一张图 |
| `Graphic_Random` | **一个目录**（`Things/Plant/MyFlower/`，以 `/` 结尾或指向目录名） | 目录里放多张图，成片生成时随机挑一张（原版玫瑰、百合） |
| `Graphic_Multi` | 名字 + 朝向后缀（`_south`/`_north`/`_east`/`_west`） | 建筑、服装穿戴贴图（按朝向切换） |

⚠️ **最常见的坑**：texPath 写的是单文件，却把 graphicClass 写成 `Graphic_Random`。
`Graphic_Collection` 初始化时找不到目录里的贴图，会在日志里报
`No textures found at path …` / `Collection cannot init`，然后显示异常或紫块
（这两条字符串在 1.7 的 `Assembly-CSharp.dll` 里存在，UTF-16）。本仓库的 plant 模板因此默认用 `Graphic_Single`。

## 着色器类型

| Shader Type | 用途 | 说明 |
|------------|------|------|
| `CutoutComplex` | 大多数物品和建筑 | 支持透明，默认推荐（很多原版 Def 根本不写，走默认） |
| `Cutout` | 简单物品 | 无附加效果 |
| `Transparent` | 半透明物品 | 玻璃、全息图；`BaseBullet` 已自带此设置，弹丸 Def 不用重复写 |
| `MetaOverlay` | 覆盖层 | 在物品表面叠加效果 |
| `Skin` | 生物皮肤 | 支持颜色变化 |

## Mask 图层（染色系统）

RimWorld 使用特殊的 Mask 纹理来实现染色（服装染色、武器涂装）。

### Mask 纹理规则
- 文件名加 `_m` 后缀：`SR_PlasmaSword.png` → `SR_PlasmaSword_m.png`
- Mask 图中：
  - **红色通道（R）** = 主色区域
  - **绿色通道（G）** = 副色区域
  - **蓝色通道（B）** = 不参与染色
- 在 Def 中配合使用：
  ```xml
  <graphicData>
    <texPath>Things/Item/SR_PlasmaSword</texPath>
    <graphicClass>Graphic_Single</graphicClass>
    <shaderType>CutoutComplex</shaderType>
    <color>(255,255,255)</color>
    <colorTwo>(180,180,255)</colorTwo>
  </graphicData>
  ```

## 音效资源

### 格式
- **WAV**：推荐
- **OGG**：体积更小，也常用

### SoundDef 示例

```xml
<?xml version="1.0" encoding="utf-8"?>
<Defs>
  <SoundDef>
    <defName>SR_PlasmaSword_Hit</defName>
    <context>MapOnly</context>
    <maxSimultaneous>5</maxSimultaneous>
    <subSounds>
      <li>
        <grains>
          <li Class="AudioGrain_Clip">
            <clipPath>Sounds/Weapons/PlasmaSword_Hit</clipPath>
          </li>
        </grains>
        <volumeRange>0.8~1.0</volumeRange>
        <pitchRange>0.95~1.05</pitchRange>
      </li>
    </subSounds>
  </SoundDef>
</Defs>
```

路径约定：`Sounds/Weapons/`、`Sounds/Buildings/`、`Sounds/UI/`、`Sounds/Ambient/`。
引用**已存在的原版音效**时只写 defName（例如武器的 `<soundCast>Shot_Revolver</soundCast>`、
`<soundCastTail>GunTail_Light</soundCastTail>`），写错名字不会崩，只是没声音——用
`grep -r "Shot_Revolver" Data/Core/Defs/SoundDefs/` 核对。

## 工具推荐

| 工具 | 用途 | 价格 |
|------|------|------|
| **GIMP** | 纹理绘制、Mask 制作 | 免费 |
| **Paint.NET** | 简单纹理编辑 | 免费 |
| **Aseprite** | 像素风格纹理 | 付费 |
| **Audacity** | 音效录制和编辑 | 免费 |
| **BFXR** | 8-bit 音效生成 | 免费（网页版） |
| **Python + Pillow** | 脚本化生成/校验贴图（尺寸、透明度、联络表） | 免费 |

## 常见问题

### Q: 贴图在游戏中显示紫色方块/空白？
按这三条查（1.7 上全部实测过）：
1. **文件不在**：`texPath` 与实际文件对不上（大小写敏感；`.png` 后缀不写进 texPath）。
2. **graphicClass 与 texPath 形态不匹配**：`Graphic_Random` 指向了单文件 → 日志出现
   `No textures found at path …` / `Collection cannot init`。
3. **穿戴贴图缺朝向文件**：`wornGraphicPath` 指向的名字下没有 `_south/_north/_east/_west` 对应文件。

### Q: 贴图太大或太小？
游戏里物品的显示大小由 `<drawSize>`（建筑等）与 `<uiIconScale>`（图标缩放）控制，`<fillPercent>` 控制建筑占格填充率——
**不是**"128px 就等于 1 格"。最稳的校准方式是拿同类原版资产的尺寸和 bbox 当基准（见上文实测表）。

### Q: 我画的武器在游戏里歪了/躺平了？
你把贴图预旋转了。原版武器贴图是水平的，游戏内角度由 `<equippedAngleOffset>` 决定（近战常见 -65）。

### Q: 染色不生效？
确认 Mask 文件命名正确（`_m` 后缀），确认 `<color>` 和 `<colorTwo>` 已设置，
且 `shaderType` 支持染色（`CutoutComplex`）。
