# 07 — 资源制作

> **适用版本**: RimWorld 1.6 | **最后更新**: 2026-05-31


## 目录

- [纹理格式规范](#纹理格式规范)
- [着色器类型](#着色器类型)
- [Mask 图层（染色系统）](#mask图层染色系统)
- [音效资源](#音效资源)
- [工具推荐](#工具推荐)
- [常见问题](#常见问题)

## 纹理格式规范

### 基本要求
- **格式**：PNG（必须）
- **背景**：透明（Alpha 通道）
- **色彩模式**：RGB + Alpha
- ⚖️ **版权**：贴图必须原创——不得从其他游戏/网站直接提取，不得使用第三方 IP 角色

### 尺寸建议

| 内容类型 | 推荐尺寸 | 说明 |
|---------|---------|------|
| 物品（武器/服装/材料） | 128×128 或 256×256 | 游戏中会自动缩放 |
| 建筑（1×1） | 256×256 | 一个单元格的建筑 |
| 建筑（多格） | 按格数 × 256 | 3×2 建筑 = 768×512 |
| UI 图标 | 32×32 或 64×64 | 科技树图标等 |
| Preview.png | 640×360 | Steam Workshop 预览图 |

### 贴图路径约定

```
Textures/
├── Things/
│   ├── Item/          ← 物品贴图
│   ├── Building/      ← 建筑贴图
│   ├── Plant/         ← 植物贴图
│   └── Pawn/          ← 生物贴图
├── UI/                ← UI 图标
│   ├── Icons/
│   └── Overlays/
└── Effects/           ← 特效贴图
```

在 XML 中引用时去掉 `Textures/` 前缀和 `.png` 后缀：
```xml
<texPath>Things/Item/SR_PlasmaSword</texPath>
<!-- 对应文件: Textures/Things/Item/SR_PlasmaSword.png -->
```

## 着色器类型

| Shader Type | 用途 | 说明 |
|------------|------|------|
| `CutoutComplex` | 大多数物品和建筑 | 支持透明，默认推荐 |
| `Cutout` | 简单物品 | 无附加效果的物品 |
| `Transparent` | 半透明物品 | 玻璃、全息图 |
| `MetaOverlay` | 覆盖层 | 用于在物品表面叠加效果 |
| `Skin` | 生物皮肤 | 支持颜色变化的生物 |

## Mask 图层（染色系统）

RimWorld 使用特殊的 Mask 纹理来实现染色功能（如服装染色、武器涂装）。

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
- **WAV**：推荐，Unity 原生支持
- **OGG**：更小的文件体积
- **MP3**：不推荐（Unity 解码性能差）

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

### 音效路径约定

```
Sounds/
├── Weapons/
├── Buildings/
├── UI/
└── Ambient/
```

## 工具推荐

| 工具 | 用途 | 价格 |
|------|------|------|
| **GIMP** | 纹理绘制、Mask 制作 | 免费 |
| **Paint.NET** | 简单纹理编辑 | 免费 |
| **Aseprite** | 像素风格纹理 | 付费 |
| **Audacity** | 音效录制和编辑 | 免费 |
| **BFXR** | 8-bit 音效生成 | 免费（网页版） |

## 常见问题

### Q: 贴图在游戏中显示紫色方块？
Unity 无法加载纹理——检查文件是否为 PNG 格式，路径是否正确。

### Q: 贴图太大或太小？
游戏中物品默认缩放：128px 纹理在游戏中约为 1 格大小。调整 `<fillPercent>` 控制贴图填充率（0-1）。

### Q: 染色不生效？
确认 Mask 文件命名正确（`_m` 后缀），确认 `<color>` 和 `<colorTwo>` 已设置。
