# GeneDef

## 用途
GeneDef 是 Biotech 的**基因**定义：一段可遗传（或可注射）的性状，带数值修正、外观改变、能力授予和遗传代价。基因用 `biostatMet`（代谢）/ `biostatCpx`（复杂度）/ `biostatArc`（远古级）三个生物统计值互相平衡——给好处的基因通常要负代谢。
它与 XenotypeDef（异种人由一组 GeneDef 组成）、AbilityDef（`abilities` 直接授予主动技能）、TraitDef（`forcedTraits` / `suppressedTraits`）、HediffDef（`hediffGiversCannotGive` / `makeImmuneTo`）以及渲染节点（发型、肤色、体型）联动。原版共 202 个实例、191 条字段路径。
> 字段名澄清（重要）：字段参考与 `docs/def-schema.json` 中**没有** `biostatFactors` 和 `disposition` 这两个路径（前者实为 `biostatMet`/`biostatCpx`/`biostatArc` 三个独立字段）。它们属「待验证」项，本模板不使用。

## 模板
```xml
<?xml version="1.0" encoding="utf-8" ?>
<Defs>

  <!-- 数值型基因：靠 statFactors / statOffsets 改数值 -->
  <GeneDef>
    <defName>EXAMPLE_SwiftHealing</defName>
    <label>example fast healing</label>
    <labelShortAdj>example-heal</labelShortAdj>          <!-- 用于"xx 人"式合成词 -->
    <description>Carriers of this gene heal from wounds twice as fast as normal.</description>
    <iconPath>UI/Icons/Genes/Gene_WoundHealingRateFast</iconPath>

    <displayCategory>Healing</displayCategory>            <!-- 基因库中的分组，值是 GeneCategoryDef 的 defName -->
    <displayOrderInCategory>40</displayOrderInCategory>

    <!-- 生物统计：代谢(Met)为负=负担更重，复杂度(Cpx)与远古(Arc)是稀有度门槛 -->
    <biostatMet>-2</biostatMet>
    <biostatCpx>1</biostatCpx>

    <statFactors>
      <InjuryHealingFactor>2</InjuryHealingFactor>        <!-- 乘法：×2 愈合速度 -->
    </statFactors>
    <statOffsets>
      <ComfyTemperatureMin>-5</ComfyTemperatureMin>       <!-- 加法：耐受更低温度 -->
    </statOffsets>

    <!-- 互斥标签：同标签的基因不能同时存在于一个异种人身上 -->
    <exclusionTags>
      <li>WoundHealingRate</li>
    </exclusionTags>

    <marketValueFactor>1.25</marketValueFactor>           <!-- 携带者市场价值倍数 -->

    <!-- 姓名生成符号包：影响随机姓名 -->
    <symbolPack>
      <prefixSymbols>
        <li><symbol>stout</symbol></li>
        <li><symbol>hard</symbol><weight>2</weight></li>
      </prefixSymbols>
      <suffixSymbols>
        <li><symbol>heal</symbol></li>
      </suffixSymbols>
    </symbolPack>
  </GeneDef>

  <!-- 能力型基因：abilities 授予 AbilityDef，并在描述里加超链接 -->
  <GeneDef>
    <defName>EXAMPLE_FireBile</defName>
    <label>example fire bile</label>
    <description>Carriers can spew burning bile from a special organ.</description>
    <iconPath>UI/Icons/Genes/Gene_Firespew</iconPath>
    <displayCategory>Ability</displayCategory>
    <displayOrderInCategory>50</displayOrderInCategory>

    <abilities>
      <li>FireSpew</li>                                   <!-- 这里写 AbilityDef 的 defName -->
    </abilities>
    <descriptionHyperlinks>
      <AbilityDef>FireSpew</AbilityDef>                   <!-- 让描述里的技能名可点击 -->
    </descriptionHyperlinks>

    <biostatMet>-2</biostatMet>
    <marketValueFactor>1.5</marketValueFactor>

    <symbolPack>
      <wholeNameSymbols>
        <li><symbol>burner</symbol></li>
      </wholeNameSymbols>
    </symbolPack>
  </GeneDef>

  <!--
    其它可选字段（示范，未启用）：
    <prerequisite>Hemogenic</prerequisite>                前置基因（3.0%）
    <geneClass>Gene_Clotting</geneClass>                  自定义实现类（4.5%）
    <minAgeActive>13</minAgeActive>                       生效最小年龄（3.0%）
    <selectionWeight>0.05</selectionWeight>               随机基因库权重（10.9%）
    <canGenerateInGeneSet>false</canGenerateInGeneSet>    是否进入随机基因池（4.5%）
    <randomChosen>true</randomChosen>                     随机选中（4.0%）
    <passOnDirectly>false</passOnDirectly>                是否直接遗传（1.5%）
    <forcedTraits><li><def>Delicate</def><degree>-1</degree></li></forcedTraits>   强制特质（3.0%）
    <suppressedTraits><li><def>Pyromaniac</def></li></suppressedTraits>            抑制特质（0.5%）
    <makeImmuneTo><li>Malaria</li></makeImmuneTo>         免疫疾病（0.5%）
    <hediffGiversCannotGive><li>BadBack</li></hediffGiversCannotGive>（0.5%）
    <disablesNeeds><li>Rest</li></disablesNeeds> / <enablesNeeds><li>Deathrest</li></enablesNeeds>
    <capMods><li><capacity>Manipulation</capacity><offset>0.05</offset></li></capMods>（2.0%）
    <hairColorOverride>(0.2, 0.2, 0.2)</hairColorOverride> / <skinColorBase> / <skinColorOverride>
    <bodyType>Hulk</bodyType> / <forcedHeadTypes><li>Furskin_Average1</li></forcedHeadTypes>
    <renderNodeProperties>...</renderNodeProperties>      自定义渲染节点（6.9%）
  -->

</Defs>
```

## 字段说明
| 字段 | 出现率 | 值类型 | 说明 |
|---|---|---|---|
| `defName` | 83.2% (168/202) | 文本 | 唯一 ID（其余是 Abstract 模板） |
| `label` | 79.7% (161/202) | 文本 | 基因名，样例 `fire spew` |
| `description` | 70.8% (143/202) | 文本 | 描述文本 |
| `displayOrderInCategory` | 68.8% (139/202) | 数值 | 组内排序 |
| `iconPath` | 65.3% (132/202) | 文本 | 图标路径，样例 `UI/Icons/Genes/Gene_Firespew` |
| `symbolPack/prefixSymbols/li/symbol` | 211.4% (427/202) | 文本 | 名前缀符号；`symbolPack` 本体 50.5% (102/202) |
| `symbolPack/prefixSymbols/li/weight` | 5.0% (10/202) | 数值 | 符号权重 |
| `biostatMet` | 43.1% (87/202) | 数值 | 代谢值，负=负担，样例 -1 / -2 / -3 |
| `displayCategory` | 38.1% (77/202) | 文本 | 分组，样例 Ability / Archite / Cosmetic / Healing |
| `labelShortAdj` | 32.2% (65/202) | 文本 | 短形容词，样例 `bald` / `coagulator` |
| `symbolPack/suffixSymbols/li/symbol` | 63.9% (129/202) | 文本 | 名后缀符号 |
| `biostatCpx` | 23.8% (48/202) | 数值 | 复杂度，样例 0 / 1 / 2 |
| `exclusionTags/li` | 24.3% (49/202) | 文本 | 互斥标签；本体 21.8% (44/202) |
| `statOffsets` | 11.9% (24/202) | 容器 | 加法修正容器 |
| `statFactors` | 10.9% (22/202) | 容器 | 乘法修正容器 |
| `symbolPack/wholeNameSymbols/li/symbol` | 14.4% (29/202) | 文本 | 整名符号 |
| `selectionWeight` | 10.9% (22/202) | 数值 | 基因库随机权重 |
| `hairColorOverride` | 8.9% (18/202) | 文本 | 发色覆盖，样例 `(0.65, 0.65, 0.65)` |
| `forcedHeadTypes/li` | 8.4% (17/202) | 文本 | 强制头型；本体 1.5% (3/202) |
| `renderNodeProperties` | 6.9% (14/202) | 容器 | 自定义渲染节点 |
| `customEffectDescriptions/li` | 6.9% (14/202) | 文本 | 附加效果说明行 |
| `skinColorOverride` | 5.9% (12/202) | 文本 | 肤色覆盖，样例 `(55, 55, 55)` |
| `canGenerateInGeneSet` | 4.5% (9/202) | 布尔 | 是否进入随机基因池 |
| `geneClass` | 4.5% (9/202) | 文本 | 自定义实现类，样例 `Gene_Clotting` |
| `abilities/li` | 4.5% (9/202) | 文本 | 授予的 AbilityDef defName |
| `descriptionHyperlinks/AbilityDef` | 4.5% (9/202) | 文本 | 描述里可点击的 AbilityDef |
| `minMelanin` | 4.5% (9/202) | 数值 | 最小黑色素 |
| `skinColorBase` | 4.5% (9/202) | 文本 | 肤色基色 |
| `endogeneCategory` | 4.5% (9/202) | 文本 | 内源基因分类，样例 BodyType / Ears / Jaw |
| `biostatArc` | 4.0% (8/202) | 数值 | 远古级标记，样例 1 / 2 |
| `randomChosen` | 4.0% (8/202) | 布尔 | 随机选中 |
| `marketValueFactor` | 4.0% (8/202) | 数值 | 市场价值倍数 |
| `randomBrightnessFactor` | 3.5% (7/202) | 数值 | 随机色亮度系数 |
| `prerequisite` | 3.0% (6/202) | 文本 | 前置基因，样例 `Hemogenic` |
| `minAgeActive` | 3.0% (6/202) | 数值 | 最小生效年龄 |
| `forcedTraits/li/def` | 3.0% (6/202) | 文本 | 强制特质名；同级 `forcedTraits/li/degree` 1.0% (2/202) 写等级 |
| `beardTagFilter/tags/li` | 3.0% (6/202) | 文本 | 胡子标签过滤；含 `whitelist` 布尔 |
| `capMods/li/capacity` | 2.0% (4/202) | 文本 | 能力修正，样例 `Manipulation` |
| `bodyType` | 2.0% (4/202) | 文本 | 强制体型，样例 `Fat` / `Hulk` / `Standard` |
| `passOnDirectly` | 1.5% (3/202) | 布尔 | 是否直接遗传 |
| `immuneToToxGasExposure` | 1.5% (3/202) | 布尔 | 免疫毒气 |
| `disablesNeeds/li` / `enablesNeeds/li` | 各 1.0% (2/202) | 文本 | 禁用/启用需求 |
| `makeImmuneTo/li` | 4.5% (9/202) | 文本 | 免疫疾病；本体 0.5% (1/202) |
| `hediffGiversCannotGive/li` | 4.5% (9/202) | 文本 | 不会获得的 hediff；本体 0.5% |

## 常见坑
1. **不要写 `biostatFactors` 或 `disposition`**：`docs/def-schema.json` 与 254 份字段参考里都没有这两个路径（本机 1.7 实测），实际字段是 `biostatMet` / `biostatCpx` / `biostatArc`。写了不会被应用。【待验证：RimWorld 对未知字段的报错文本未核实】
2. `statFactors` 是乘法、`statOffsets` 是加法，写反会得到离谱数值（原版 Healing 组用 `<InjuryHealingFactor>2</InjuryHealingFactor>` 表示"两倍愈合"）。
3. `exclusionTags` 是分组互斥用的自定义字符串：同一组基因必须写**同一个标签**（原版治愈速度组统一写 `WoundHealingRate`），否则异种人身上会出现两个互斥基因。
4. `abilities` 里写的是 **AbilityDef 的 defName**；只写 `abilities` 而不同时写 `descriptionHyperlinks/AbilityDef`，技能名在描述里不会变成可点击链接（原版 `Biotech/Defs/GeneDefs/GeneDefs_Abilities.xml:11-16` 两者都写）。
5. 想让基因出现在随机基因库，需要配合 `selectionWeight` / `canGenerateInGeneSet` / `randomChosen`（原版出现率 10.9% / 4.5% / 4.0%）。【推测：三者的具体筛选顺序未核实】
6. `displayCategory` 的值必须是已存在的 GeneCategoryDef（原版样例 Ability / Archite / Cosmetic / Healing），写一个不存在的分类会让基因在基因库里无处显示。【推测】

## 核验
- 数值型基因逐行对照原版 `Biotech/Defs/GeneDefs/GeneDefs_Health.xml`：`WoundHealing_Slow`(:13-29) 给出 label / labelShortAdj / description / iconPath / displayOrderInCategory / statFactors(`InjuryHealingFactor` 0.5) / biostatMet 2 / symbolPack；`WoundHealing_Fast`(:31-48) 给 biostatMet -2；`WoundHealing_SuperFast`(:50-68) 给 `marketValueFactor` 1.25；抽象模板 `GeneHealingRateBase`(:6-11) 给出 `displayCategory` + `exclusionTags/WoundHealingRate` 的互斥写法。
- 能力型基因逐行对照原版 `Biotech/Defs/GeneDefs/GeneDefs_Abilities.xml` 的 `FireSpew`(:4-40)：`abilities/li`、`descriptionHyperlinks/AbilityDef`、`biostatMet`、`marketValueFactor`、`symbolPack/wholeNameSymbols/prefixSymbols/suffixSymbols` 全部有出处。
- 出现率、值类型、样例值来自 `library/03-全量字段参考/字段/GeneDef.md`（202 个原版实例实测）；`biostatFactors`/`disposition` 的不存在性通过对 `docs/def-schema.json` 全文检索与对该字段目录全量检索确认（0 命中）。
- 其它可交叉核对文件：`Biotech/Defs/GeneDefs/GeneDefs_Cosmetic.xml`、`GeneDefs_Misc.xml`、`GeneDefs_Sanguophage.xml`、`XenotypeDefs.xml`（XenotypeDef 里按 defName 引用这些基因）。
