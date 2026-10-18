# IdeoIconDef

> 类型：`IdeoIconDef` ｜ 出现范围：Ideology ｜ 原版实例 **94** 个 ｜ 字段路径 **6** 条

## 用途

定义理念编辑器里的**一组图标**。它是全部 254 种类型里字段最少的一类——只有 6 条路径。

作用是：当理念包含某些信条或文化时，编辑器优先给出对应的图标选项。

**典型用途**：给新信条配专属图标、给新文化配图标组。

## 模板

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Defs>

  <IdeoIconDef>
    <defName>EXAMPLE_IconsA</defName>
    <iconPath>UI/Ideoligions/EXAMPLE_IconsA</iconPath>

    <!-- 用哪些信条时把这些图标排到前面 -->
    <memes>
      <li>EXAMPLE_Craftism</li>
    </memes>

    <!-- 用哪些文化时把这些图标排到前面 -->
    <cultures>
      <li>Astropolitan</li>
    </cultures>
  </IdeoIconDef>
</Defs>
```

## 字段说明

> 出现率＝该字段在原版同类实例中出现的比例。**超过 100%** 说明它是数组子元素。
> 完整字段表见 `03-全量字段参考/字段/IdeoIconDef.md`。

| 字段 | 出现率 | 值类型 | 原版样例值 |
|---|---:|---|---|
| `memes/li` | 139% | 字符串 | AnimalPersonhood ／ Rancher |
| `defName` | 100% | 字符串 | AnimalsA ／ AnimalsB |
| `iconPath` | 100% | 字符串 | UI/Ideoligions/AnimalsA ／ UI/Ideoligions/AnimalsB |
| `memes` | 68% |  | — |
| `cultures/li` | 30% | 字符串 | Astropolitan ／ Corunan |
| `cultures` | 28% |  | — |

## 常见坑

- **`iconPath` 指向的是图标「图集」**，实际图标资源一般与它同名的目录/图集一起打包，只写路径不给图会显示空白。
- **`memes/li` 与 `cultures/li` 都是可选**（68% / 28%），不写就是一组永远可选的通用图标。
- **原版 94 个实例、只有 6 条字段路径**：它是「最小可用 Def」的样板，适合用来理解 Def 的基本骨架。
- **它只影响图标排序，不影响玩法**。想让新信条有专属图标，光写这个还不够，还要有对应的贴图文件。

## 核验

本模板的每个字段均可在下列原版文件中找到同名路径：

- `Data/Ideology/Defs/IdeoIconDefs/IdeoIcons.xml`
