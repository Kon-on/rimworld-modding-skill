# HediffDef

## 用途
HediffDef 定义角色身上的一条**状态**：伤口、疾病、药物效果、义体部件、灵能增益都走它。核心是 `stages`——按严重度（severity）分段，每段给出自己的标签、疼痛、能力修正和是否致命；配合 `comps` 决定它如何增长、消退和被治疗。
它常与 ThingDef（`spawnThingOnRemoved` 移除后掉落的物品、`descriptionHyperlinks` 的链接）、ThoughtDef（`makesSickThought` 引发的病人心情）、PawnCapacityDef（`stages/li/capMods/li/capacity`）联动。原版共 344 个实例、475 条字段路径。

## 模板
```xml
<?xml version="1.0" encoding="utf-8" ?>
<Defs>

  <!-- 疾病型：可治疗、有免疫流程、按严重度分档 -->
  <HediffDef>
    <defName>EXAMPLE_WoundRot</defName>
    <label>example wound rot</label>
    <labelNoun>an example wound rot</labelNoun>          <!-- 用于"遭受了 xx"这类句式 -->
    <description>Bacterial infection in a wound. Without treatment the bacteria multiply and kill local tissue.</description>

    <!-- 要挂 comps 就必须用 HediffWithComps（原版 46.2% 显式写 hediffClass） -->
    <hediffClass>HediffWithComps</hediffClass>

    <isBad>true</isBad>                                   <!-- 负面状态：影响 UI 配色与部分判断 -->
    <makesSickThought>true</makesSickThought>             <!-- 触发"我生病了"心情 -->
    <tendable>true</tendable>                             <!-- 可被治疗 -->
    <lethalSeverity>1</lethalSeverity>                    <!-- 严重度达到该值即致死 -->
    <maxSeverity>1</maxSeverity>

    <comps>
      <!-- 治疗：定义包扎耗时与治疗后每天降低的严重度 -->
      <li Class="HediffCompProperties_TendDuration">
        <baseTendDurationHours>12</baseTendDurationHours>
        <severityPerDayTended>-0.53</severityPerDayTended>
        <labelTendedWell>bandaged</labelTendedWell>
        <labelTendedWellInner>sutured</labelTendedWellInner>
        <labelSolidTendedWell>set</labelSolidTendedWell>
      </li>
      <!-- 免疫流程：未免疫时如何增长、免疫时如何消退 -->
      <li Class="HediffCompProperties_Immunizable">
        <severityPerDayNotImmune>0.84</severityPerDayNotImmune>
        <immunityPerDaySick>0.6441</immunityPerDaySick>
        <severityPerDayImmune>-0.70</severityPerDayImmune>
        <immunityPerDayNotSick>-0.40</immunityPerDayNotSick>
      </li>
      <!-- 被发现时发信件 -->
      <li Class="HediffCompProperties_Discoverable">
        <sendLetterWhenDiscovered>true</sendLetterWhenDiscovered>
      </li>
    </comps>

    <stages>
      <li>
        <label>minor</label>                              <!-- 第一档不写 minSeverity，默认从 0 开始 -->
        <painOffset>0.05</painOffset>
      </li>
      <li>
        <minSeverity>0.33</minSeverity>
        <label>major</label>
        <painOffset>0.08</painOffset>
      </li>
      <li>
        <minSeverity>0.78</minSeverity>
        <label>extreme</label>
        <lifeThreatening>true</lifeThreatening>           <!-- 该档起视为生命危险 -->
        <vomitMtbDays>0.75</vomitMtbDays>                 <!-- 平均几天呕吐一次 -->
        <capMods>
          <li>
            <capacity>Consciousness</capacity>            <!-- 必须是 PawnCapacityDef 的 defName -->
            <offset>-0.15</offset>                       <!-- 加法修正 -->
          </li>
          <li>
            <capacity>Manipulation</capacity>
            <setMax>0.8</setMax>                         <!-- 上限封顶 -->
          </li>
        </capMods>
      </li>
    </stages>
  </HediffDef>

  <!--
    其它形态的写法（示范，未启用）：
    1) 伤口型（受伤时才用）：
       <hediffClass>Hediff_Injury</hediffClass>
       <displayWound>true</displayWound>
       <injuryProps>
         <painPerSeverity>0.0125</painPerSeverity>
         <bleedRate>0.06</bleedRate>
         <canMerge>false</canMerge>
         <destroyedLabel>Destroyed</destroyedLabel>
       </injuryProps>
       <comps><li Class="HediffCompProperties_GetsPermanent"><permanentLabel>scar</permanentLabel></li></comps>
    2) 义体/植入体型：
       <addedPartProps><solid>true</solid><partEfficiency>1.1</partEfficiency><betterThanNatural>true</betterThanNatural></addedPartProps>
       <spawnThingOnRemoved>DetoxifierLung</spawnThingOnRemoved>
    3) 纯 buff 计时型：
       <comps><li Class="HediffCompProperties_Disappears"><showRemainingTime>true</showRemainingTime><disappearsAfterTicks>60000</disappearsAfterTicks></li></comps>
    4) 其它常用：<initialSeverity>0.5</initialSeverity>、<defaultLabelColor>(0.5, 0.5, 0.5)</defaultLabelColor>、
       <duplicationAllowed>false</duplicationAllowed>、<everCurableByItem>false</everCurableByItem>、
       <tags><li>ArmorGland</li></tags>、<descriptionHyperlinks><ThingDef>DetoxifierLung</ThingDef></descriptionHyperlinks>
  -->

</Defs>
```

## 字段说明
| 字段 | 出现率 | 值类型 | 说明 |
|---|---|---|---|
| `defName` | 93.9% (323/344) | 文本 | 唯一 ID（其余是 Abstract 模板） |
| `description` | 92.7% (319/344) | 文本 | 描述文本 |
| `label` | 92.2% (317/344) | 文本 | 显示名，样例 `flesh whip` |
| `comps/li` | 100.9% (347/344) | 容器 | 组件列表；本体 `comps` 62.8% (216/344) |
| `stages/li` | 124.1% (427/344) | 容器 | 阶段列表；本体 `stages` 67.7% (233/344) |
| `stages/li/capMods/li/capacity` | 98.8% (340/344) | 文本 | 能力名，样例 Consciousness / Manipulation / Moving |
| `stages/li/capMods` | 57.0% (196/344) | 容器 | 能力修正容器 |
| `stages/li/capMods/li/offset` | 61.6% (212/344) | 数值 | 加法修正，样例 -0.05 / -0.1 |
| `stages/li/minSeverity` | 59.6% (205/344) | 数值 | 该阶段起始严重度 |
| `stages/li/label` | 62.2% (214/344) | 文本 | 阶段名，样例 `acute` / `lingering` |
| `hediffClass` | 46.2% (159/344) | 文本 | 实现类，样例 HediffWithComps / Hediff_Injury / Hediff_MissingPart |
| `labelNoun` | 34.0% (117/344) | 文本 | 名词短语，样例 `a flesh whip` |
| `stages/li/statOffsets` | 30.5% (105/344) | 容器 | 阶段附加数值 |
| `stages/li/painOffset` | 26.7% (92/344) | 数值 | 疼痛增量，样例 0.05 / 0.06 |
| `isBad` | 23.5% (81/344) | 布尔 | 是否负面状态 |
| `stages/li/capMods/li/postFactor` | 22.4% (77/344) | 数值 | 能力乘算修正 |
| `descriptionHyperlinks` | 17.7% (61/344) | 容器 | 描述内链接；子路径 `descriptionHyperlinks/ThingDef` 17.4% (60/344)、`descriptionHyperlinks/HediffDef` 0.9% (3/344) |
| `spawnThingOnRemoved` | 16.9% (58/344) | 文本 | 移除后掉落的 ThingDef |
| `initialSeverity` | 16.3% (56/344) | 数值 | 初始严重度 |
| `comps/li/showRemainingTime` | 16.6% (57/344) | 布尔 | 显示剩余时间 |
| `stages/li/capMods/li/setMax` | 14.5% (50/344) | 数值 | 能力上限封顶 |
| `maxSeverity` | 14.2% (49/344) | 数值 | 严重度上限 |
| `defaultLabelColor` | 14.0% (48/344) | 文本 | 标签颜色，样例 `(0.5, 0.5, 0.5)` |
| `stages/li/statFactors` | 15.7% (54/344) | 容器 | 阶段乘算数值 |
| `comps/li/disappearsAfterTicks` | 13.4% (46/344) | 数值/文本 | 到期消失 |
| `addedPartProps` | 12.5% (43/344) | 容器 | 植入体属性 |
| `addedPartProps/solid` | 11.9% (41/344) | 布尔 | 是否为实体部件 |
| `comps/li/severityPerDay` | 11.6% (40/344) | 数值 | 每日严重度变化 |
| `stages/li/vomitMtbDays` | 10.8% (37/344) | 数值 | 呕吐平均间隔 |
| `stages/li/partEfficiencyOffset` | 10.5% (36/344) | 数值 | 部件效率修正 |
| `everCurableByItem` | 9.3% (32/344) | 布尔 | 是否可被物品治愈 |
| `addedPartProps/partEfficiency` | 8.4% (29/344) | 数值 | 部件效率 |
| `injuryProps` | 8.1% (28/344) | 容器 | 伤口属性容器 |
| `lethalSeverity` | 7.0% (24/344) | 数值 | 致死严重度 |
| `stages/li/lifeThreatening` | 7.0% (24/344) | 布尔 | 该阶段是否生命危险 |
| `stages/li/becomeVisible` | 7.0% (24/344) | 布尔 | 该阶段是否可见 |
| `stages/li/painFactor` | 6.7% (23/344) | 数值 | 疼痛系数 |
| `injuryProps/destroyedLabel` | 6.7% (23/344) | 文本 | 部件被毁时的标签 |
| `tendable` | 6.7% (23/344) | 布尔 | 是否可治疗 |
| `comps/li/permanentLabel` | 6.1% (21/344) | 文本 | 永久化后的标签，样例 `scar` |
| `injuryProps/painPerSeverity` | 5.8% (20/344) | 数值 | 每点严重度的疼痛 |
| `makesSickThought` | 5.8% (20/344) | 布尔 | 是否引发病人心情 |
| `injuryProps/canMerge` | 5.5% (19/344) | 布尔 | 同部位伤口是否合并 |
| `comps/li/labelTendedWell`、`comps/li/labelTendedWellInner`、`comps/li/labelSolidTendedWell` | 各 5.5% (19/344) | 文本 | 治疗完成后的标签，样例 `bandaged` / `sutured` / `set` |
| `stages/li/hungerRateFactorOffset` | 5.2% (18/344) | 数值 | 饥饿速率增量 |
| `comps/li/baseTendDurationHours` | 4.4% (15/344) | 数值 | 基础包扎耗时（小时） |
| `stages/li/hediffGivers` | 4.4% (15/344) | 容器 | 阶段内再引发其它 hediff |
| `descriptionShort` | 4.1% (14/344) | 文本 | 简短描述 |
| `duplicationAllowed` | 4.1% (14/344) | 布尔 | 是否允许重复实例 |
| `minSeverity` | 4.1% (14/344) | 数值 | 全局最小严重度 |
| `comps/li/severityPerDayTended` | 3.8% (13/344) | 数值 | 治疗状态下每日严重度变化 |
| `injuryProps/bleedRate` | 3.8% (13/344) | 数值 | 出血速率，样例 0.06 / 0.12 |
| `comps/li/severityPerDayNotImmune` | 3.5% (12/344) | 数值 | 未免疫时每日增长 |
| `keepOnBodyPartRestoration` | 3.5% (12/344) | 布尔 | 部件修复后是否保留 |
| `priceImpact` | 3.5% (12/344) | 布尔 | 是否影响价格 |
| `comps/li/immunityPerDaySick`、`comps/li/immunityPerDayNotSick` | 各 2.3% (8/344) | 数值 | 免疫度每日变化 |
| `tags/li` | 2.3% (8/344) | 文本 | 自定义标签 |
| `displayWound` | 2.0% (7/344) | 布尔 | 是否显示伤口 |
| `comps/li/compClass` | 2.0% (7/344) | 文本 | 组件实现类 |

## 常见坑
1. 挂了 `comps` 就要把 `hediffClass` 写成 `HediffWithComps`（或它的子类）；原版带 comps 的定义几乎都显式声明了 hediffClass（46.2% 的实例写了该字段）。【推测：不写时 comps 是否被忽略未核实】
2. `tendable` 只表示"可以被治疗"；要让治疗真的降低严重度，必须同时挂 `HediffCompProperties_TendDuration` 并给出 `severityPerDayTended`——原版 `Flu` 与 `WoundInfection` 都是 `tendable` + TendDuration 成对出现（`Hediffs_Local_Infections.xml:277-282`、`:214-219`）。
3. `stages/li` 的 `minSeverity` 必须随顺序递增，第一档通常不写（默认 0）；只写 `<minSeverity>0</minSeverity>` 也可以（原版样例值里就有 0）。跳档或倒序会让中间严重度落不到任何阶段。【推测】
4. `capMods/li/capacity` 的值必须是已存在的 PawnCapacityDef defName（Consciousness / Manipulation / Moving / Breathing / Sight …），拼错会在加载或运行时失效。
5. `injuryProps` 主要给 `Hediff_Injury` 系使用（原版 `Hediffs_Local_Injuries.xml:30-35` 的 `InjuryBase` 抽象模板统一声明 `hediffClass`/`tendable`/`displayWound`/`labelNounPretty`）；给普通状态写这些字段没有意义。【推测】
6. `comps/li` 的 `Class` 属性（如 `Class="HediffCompProperties_TendDuration"`）必须与实际子元素匹配：`severityPerDayTended` 只有挂在 TendDuration 下才被读取。

## 核验
- 疾病型模板逐行对照原版 `Core/Defs/HediffDefs/Hediffs_Local_Infections.xml`：`WoundInfection`(:206-269) 给出 makesSickThought / lethalSeverity / tendable / comps(TendDuration `baseTendDurationHours`+`severityPerDayTended`、Immunizable 四个数值、Discoverable `sendLetterWhenDiscovered`) / stages 的 minSeverity 0.33、0.78、0.87 与 label minor/major/extreme、painOffset、lifeThreatening、capMods(`Consciousness` + offset/setMax)；`Flu`(:271-349) 给出同样的三档结构、`vomitMtbDays` 与 `TendDuration`/`Immunizable` 数值组。
- 伤口型与植入体型写法对照原版 `Core/Defs/HediffDefs/Hediffs_Local_Injuries.xml`：`MissingBodyPart`(:6-26，hediffClass `Hediff_MissingPart`/defaultLabelColor/forceRenderTreeRecache/tendable/displayWound/injuryProps/`HediffCompProperties_TendDuration`)、`InjuryBase`(:30-35，抽象模板的 hediffClass `Hediff_Injury`+`labelNounPretty`)、`Misc`(:37-58，`HediffCompProperties_GetsPermanent` 的 `permanentLabel` scar 与 injuryProps 的 painPerSeverity/bleedRate/canMerge/destroyedLabel)。
- 最小可加载范例见 `Anomaly/Defs/HediffDefs/Hediffs_BodyParts_Prosthetic.xml` 的 `AddedMutationBase`（只有 `<organicAddedBodypart>true</organicAddedBodypart>`）。
- 出现率与样例值来自 `library/03-全量字段参考/字段/HediffDef.md`（344 个原版实例实测）。其余可交叉核对文件：`Core/Defs/HediffDefs/Hediffs_Local_Chronic.xml`、`Hediffs_Global_Temperature.xml`、`Hediffs_Global_Misc.xml`。
