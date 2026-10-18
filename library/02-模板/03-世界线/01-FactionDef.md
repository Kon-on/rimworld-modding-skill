# FactionDef

## 用途

FactionDef 定义一个派系：世界生成时按它决定生成多少据点、据点长什么样，袭击/商队怎么组队（`pawnGroupMakers`），以及派系的名字、颜色、图标从哪来。它上接世界生成与关系系统，下联 PawnKindDef（兵种）、TraderKindDef（商队/据点商人）、RulePackDef（命名器）、ThingSetMakerDef（袭击掉落）、MemeDef（Ideology 理念）与 XenotypeDef（Biotech 异种）。玩家自己的派系（`PlayerColony`/`PlayerTribe`）与隐藏派系（`Ancients`）也用它。

## 模板

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Defs>

  <!-- 一个自成一体的自定义人类派系：能生成据点、派商队、组织袭击。
       本模板不继承任何 Abstract 父定义，所有字段自带，复制即用。 -->
  <FactionDef>
    <defName>EXAMPLE_SaltMercenaries</defName>
    <label>salt mercenaries</label>
    <description>一支为钱卖命的雇佣兵团，靠海吃海，谁的银子给得多就替谁站岗。</description>

    <!-- 成员称呼：事件文本里会用到（单数/复数都要给）。 -->
    <pawnSingular>salt mercenary</pawnSingular>
    <pawnsPlural>salt mercenaries</pawnsPlural>

    <!-- 派系大类标签：原版值有 Outlander / Tribal / Pirate / Ancient / HoraxCult 等，
         用于 UI 分组与部分生成规则。 -->
    <categoryTag>Outlander</categoryTag>
    <techLevel>Industrial</techLevel>
    <listOrderPriority>45</listOrderPriority>

    <!-- 世界生成 -->
    <settlementGenerationWeight>1</settlementGenerationWeight>
    <requiredCountAtGameStart>1</requiredCountAtGameStart>
    <maxConfigurableAtWorldCreation>9999</maxConfigurableAtWorldCreation>
    <configurationListOrderPriority>45</configurationListOrderPriority>

    <!-- 图标与命名器（贴图路径不带扩展名；命名器指向 RulePackDef） -->
    <factionIconPath>World/WorldObjects/Expanding/Town</factionIconPath>
    <settlementTexturePath>World/WorldObjects/DefaultSettlement</settlementTexturePath>
    <factionNameMaker>NamerFactionOutlander</factionNameMaker>
    <settlementNameMaker>NamerSettlementOutlander</settlementNameMaker>

    <!-- 派系在地图上的着色：0~1 的 (r, g, b)，取区间内随机值 -->
    <colorSpectrum>
      <li>(0.35, 0.30, 0.60)</li>
      <li>(0.45, 0.40, 0.90)</li>
    </colorSpectrum>

    <!-- 文化与背景故事过滤（categories 用 BackstoryDef 的分类字符串） -->
    <allowedCultures>
      <li>Rustican</li>
    </allowedCultures>
    <backstoryFilters>
      <li>
        <categories>
          <li>Outlander</li>
        </categories>
        <commonality>0.95</commonality>
      </li>
      <li>
        <categories>
          <li>Offworld</li>
        </categories>
        <commonality>0.05</commonality>
      </li>
    </backstoryFilters>

    <!-- 超出该温度区间就不会派袭击/商队过来 -->
    <allowedArrivalTemperatureRange>-40~45</allowedArrivalTemperatureRange>

    <!-- 商队与据点商人（TraderKindDef） -->
    <caravanTraderKinds>
      <li>Caravan_Outlander_BulkGoods</li>
      <li>Caravan_Outlander_CombatSupplier</li>
    </caravanTraderKinds>
    <baseTraderKinds>
      <li>Base_Outlander_Standard</li>
    </baseTraderKinds>

    <!-- 袭击点数 → 该派系出动权重 的曲线：原版部落用恒定 1 -->
    <raidCommonalityFromPointsCurve>
      <points>
        <li>(0, 1)</li>
      </points>
    </raidCommonalityFromPointsCurve>

    <!-- 单个 Pawn 的花费上限随总点数上升：防止一开局就刷出顶级单位 -->
    <maxPawnCostPerTotalPointsCurve>
      <points>
        <li>(0,35)</li>
        <li>(70, 50)</li>
        <li>(700, 100)</li>
        <li>(1300, 150)</li>
        <li>(100000, 10000)</li>
      </points>
    </maxPawnCostPerTotalPointsCurve>

    <!-- 袭击者身上的战利品（ThingSetMakerDef） -->
    <raidLootMaker>OutlanderRaidLootMaker</raidLootMaker>

    <!-- 组队方案：kindDef 说明这队人拿来做什麼 -->
    <pawnGroupMakers>
      <li>
        <!-- 普通战斗：键是 PawnKindDef 名，值是权重 -->
        <kindDef>Combat</kindDef>
        <options>
          <Mercenary_Slasher>7</Mercenary_Slasher>
          <Mercenary_Gunner>10</Mercenary_Gunner>
          <Mercenary_Elite>10</Mercenary_Elite>
        </options>
      </li>
      <li>
        <!-- 商队：traders 是商人本人，carriers 是驮兽，guards 是护卫 -->
        <kindDef>Trader</kindDef>
        <traders>
          <Town_Trader>1</Town_Trader>
        </traders>
        <carriers>
          <Muffalo>6</Muffalo>
          <Dromedary>5</Dromedary>
        </carriers>
        <guards>
          <Mercenary_Gunner>10</Mercenary_Gunner>
        </guards>
      </li>
      <li>
        <!-- 变体方案：给低权重、限制总点数、禁掉某种袭击策略 -->
        <kindDef>Combat</kindDef>
        <commonality>2.5</commonality>
        <maxTotalPoints>1000</maxTotalPoints>
        <disallowedStrategies>
          <li>Siege</li>
        </disallowedStrategies>
        <options>
          <Mercenary_Gunner>10</Mercenary_Gunner>
        </options>
      </li>
    </pawnGroupMakers>

    <canSiege>true</canSiege>
    <canStageAttacks>true</canStageAttacks>

    <!-- Ideology：不许信的 meme（MayRequire 保证没装 DLC 时不报错） -->
    <disallowedMemes>
      <li MayRequire="Ludeon.RimWorld.Ideology">Structure_Animist</li>
      <li MayRequire="Ludeon.RimWorld.Ideology">Nudism</li>
    </disallowedMemes>

    <!-- Biotech：异种出现概率 -->
    <xenotypeSet>
      <xenotypeChances>
        <Hussar MayRequire="Ludeon.RimWorld.Biotech">0.05</Hussar>
        <Dirtmole MayRequire="Ludeon.RimWorld.Biotech">0.05</Dirtmole>
        <Genie MayRequire="Ludeon.RimWorld.Biotech">0.025</Genie>
        <Neanderthal MayRequire="Ludeon.RimWorld.Biotech">0.025</Neanderthal>
      </xenotypeChances>
    </xenotypeSet>
  </FactionDef>

</Defs>
```

## 字段说明

| 字段 | 出现率 | 值类型 | 说明 |
|---|---|---|---|
| `defName` | 79.5% (31/39) | 文本 | 唯一标识；被别处引用时写这个名字 |
| `label` | 79.5% (31/39) | 文本 | 内部/调试用名；玩家看到的派系名由 `factionNameMaker` 生成 |
| `description` | 69.2% (27/39) | 文本 | 派系详情里的描述 |
| `pawnSingular` / `pawnsPlural` | 59.0% (23/39) / 61.5% (24/39) | 文本 | 成员单/复数称呼，事件文本会套用 |
| `categoryTag` | 30.8% (12/39) | 文本 | 派系大类（原版值：Ancient / Outlander / Pirate / HoraxCult 等） |
| `techLevel` | 48.7% (19/39) | 文本 | 科技等级枚举名（原版样例：Animal / Industrial / Spacer） |
| `listOrderPriority` | 7.7% (3/39) | 数值 | 派系列表排序 |
| `factionIconPath` | 74.4% (29/39) | 文本 | 图标贴图路径（无扩展名） |
| `settlementTexturePath` | 38.5% (15/39) | 文本 | 据点在星球视图上的贴图 |
| `factionNameMaker` | 51.3% (20/39) | 文本 | RulePackDef defName，生成派系名 |
| `settlementNameMaker` | 46.2% (18/39) | 文本 | RulePackDef defName，生成据点名 |
| `colorSpectrum/li` | 120.5% (47/39) | 文本 | 派系着色区间，`(r, g, b)`，0~1 浮点 |
| `settlementGenerationWeight` | 15.4% (6/39) | 数值 | 世界生成据点的权重 |
| `requiredCountAtGameStart` | 46.2% (18/39) | 数值 | 开局必须存在的数量 |
| `maxConfigurableAtWorldCreation` | 43.6% (17/39) | 数值 | 世界创建界面可配置上限（9999≈无限） |
| `configurationListOrderPriority` | 43.6% (17/39) | 数值 | 世界创建界面排序 |
| `allowedArrivalTemperatureRange` | 30.8% (12/39) | 文本 | `min~max`，超出则不来袭击/商队 |
| `caravanTraderKinds/li` | 23.1% (9/39) | 文本 | TraderKindDef：地图上的商队 |
| `baseTraderKinds/li` | 7.7% (3/39) | 文本 | TraderKindDef：据点里的商人 |
| `raidLootMaker` | 17.9% (7/39) | 文本 | ThingSetMakerDef：袭击者死亡掉落 |
| `raidCommonalityFromPointsCurve/points/li` | 28.2% (11/39) | 文本 | 曲线点 `(点数, 权重)` |
| `maxPawnCostPerTotalPointsCurve/points/li` | 105.1% (41/39) | 文本 | 曲线点 `(总点数, 单价上限)` |
| `pawnGroupMakers` | 41.0% (16/39) | 容器 | 组队方案列表 |
| `pawnGroupMakers/li/kindDef` | 276.9% (108/39) | 文本 | 方案用途（原版：Combat / Peaceful / Trader / Settlement / Miners / Hunters / Loggers / Farmers） |
| `pawnGroupMakers/li/options` | 261.5% (102/39) | 容器 | PawnKindDef 名 → 权重 |
| `pawnGroupMakers/li/commonality` | 197.4% (77/39) | 数值 | 该方案被选中的相对权重 |
| `pawnGroupMakers/li/traders` | 15.4% (6/39) | 容器 | 商人 PawnKindDef → 数量 |
| `pawnGroupMakers/li/carriers` | 15.4% (6/39) | 容器 | 驮兽 PawnKindDef → 数量 |
| `pawnGroupMakers/li/guards` | 15.4% (6/39) | 容器 | 护卫 PawnKindDef → 数量 |
| `pawnGroupMakers/li/maxTotalPoints` | 7.7% (3/39) | 数值 | 该方案允许消耗的点数上限 |
| `pawnGroupMakers/li/disallowedStrategies/li` | 15.4% (6/39) | 文本 | 禁用的袭击策略（原版样例：Siege） |
| `canSiege` / `canStageAttacks` | 23.1% (9/39) / 28.2% (11/39) | 布尔 | 能否攻城 / 能否组织多波进攻 |
| `backstoryFilters/li/categories/li` | 61.5% (24/39) | 文本 | 背景故事分类过滤（原版：Outlander / Offworld / Cult） |
| `backstoryFilters/li/commonality` | 30.8% (12/39) | 数值 | 该过滤组权重 |
| `disallowedMemes/li` | 107.7% (42/39) | 文本 | Ideology：禁用的 meme |
| `requiredMemes/li` | 43.6% (17/39) | 文本 | Ideology：必须有的 meme |
| `xenotypeSet/xenotypeChances` | 33.3% (13/39) | 容器 | Biotech：XenotypeDef → 概率 |

## 常见坑

1. **`pawnGroupMakers` 里的每个键都必须是一个真实存在的 PawnKindDef。** 原版 `options` 的键全部能在 PawnKindDef 中命中（本模板用到的 `Mercenary_Slasher` / `Mercenary_Gunner` / `Mercenary_Elite` / `Town_Trader` / `Muffalo` / `Dromedary` 已逐个核验）。写错名字的后果【待验证】：本次未启动游戏，未能取得具体报错文本。
2. **`factionNameMaker` / `settlementNameMaker` / `raidLootMaker` / `caravanTraderKinds` 全是跨 Def 引用**，分别要求 RulePackDef / ThingSetMakerDef / TraderKindDef。这几处写错不会给出直观提示，核验办法：在 `Data/` 下 grep `<defName>`。
3. **`categoryTag` 不是枚举，而是自由字符串标签。** 本模板填原版已有的 `Outlander`。若改成自建标签（原版有 `HoraxCult` 这种先例），是否会丢失原版某些按 `Outlander` 判定的行为【推测】：原版对 `categoryTag` 的消费点分散，本次未逐处追踪。
4. **原版几乎所有人类派系都继承 `FactionBase`，但那个父定义只有两个字段**（`raidLootValueFromPointsCurve`、`messageDefendersAttacking`，见 `Core/Defs/FactionDefs/Factions_Base.xml`）。本模板不继承父定义，字段全部自带，因此不存在"父定义没给默认值"的缺口。
5. **DLC 字段必须加 `MayRequire`。** `xenotypeSet` 引用 Biotech 异种、`disallowedMemes` 引用 Ideology meme，未装 DLC 时缺 `MayRequire` 会因找不到对应 Def 而报错。注意 `MayRequire` 是结构化 XML 属性（原版遍地使用，如 `Core/Defs/FactionDefs/Factions_Misc.xml` 里 `<Blindsight MayRequire="Ludeon.RimWorld.Ideology">`），它不是 Def 字段。
6. **`options`/`carriers`/`guards`/`traders` 的"键"是 XML 元素名，不是子元素。** 写 `<Mercenary_Gunner>10</Mercenary_Gunner>`；写成 `<li><def>…` 解析不出来。
7. **曲线点写在 `<li>(x, y)</li>` 里，逗号后空格可有可无**（原版两种写法都有：`(0,35)` 与 `(0, 1)`）。写成 `<li>0,1</li>` 不被识别【推测：格式由 FloatCurve 解析器决定，未实测】。

## 核验

- **本模板字段是否合法**：逐条对照 `library/03-全量字段参考/字段/FactionDef.md` 的「全量字段表（325 条路径）」，模板里出现的每个元素名都能在该表中找到同名路径。
- **原版写法依据**（相对 `<游戏安装目录>\Data\`）：
  - `Core/Defs/FactionDefs/Factions_Base.xml`：唯一父定义 `FactionBase` 的全部内容（2 个字段）。
  - `Core/Defs/FactionDefs/Factions_Misc.xml`：`OutlanderFactionBase`（pawnsPlural / categoryTag / caravanTraderKinds / baseTraderKinds / maxPawnCostPerTotalPointsCurve / pawnGroupMakers 全量写法）、`OutlanderCivil`（colorSpectrum + worldCreation 配置字段）、`TribeRough`（raidCommonalityFromPointsCurve 曲线）、`PirateBandBase`（maxTotalPoints / disallowedStrategies）。
  - `Core/Defs/FactionDefs/Factions_Hidden.xml`：`Ancients`（该 DefType 的最小实例）。
- **跨 Def 引用**：模板引用的 `NamerFactionOutlander`、`NamerSettlementOutlander` 已核验存在且类型为 RulePackDef；`Caravan_Outlander_BulkGoods` / `Caravan_Outlander_CombatSupplier` / `Base_Outlander_Standard` 为 TraderKindDef；`OutlanderRaidLootMaker` 为 ThingSetMakerDef；`Rustican` 为 CultureDef；`Structure_Animist` / `Nudism` 为 MemeDef；`Hussar` / `Dirtmole` / `Genie` / `Neanderthal` 为 XenotypeDef；`Villager` / `Town_Guard` / `Mercenary_Gunner` 等为 PawnKindDef。核验方式：扫描全部原版 `Data/**/Defs/**/*.xml` 建立"defType → defName"索引后逐一比对。
- **贴图路径**：`World/WorldObjects/Expanding/Town`、`World/WorldObjects/DefaultSettlement` 已在本体 `Assets.zip` 中央目录中命中（原版贴图打包为 `Resources/Textures/<路径>.psd.dds`，游戏根目录下没有松散 `Textures/` 目录）。
