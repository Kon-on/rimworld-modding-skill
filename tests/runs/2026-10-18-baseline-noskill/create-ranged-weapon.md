# 离子步枪（Ion Rifle）——RimWorld 远程武器 ThingDef

> 说明：下面是**完整可直接落地**的模组代码，射程 30、单发伤害 15，按你的要求写死在这两个字段上。
> 所有内容凭 RimWorld 模组制作的通识给出（未逐行比对 1.5/1.6 的 XSD），可疑处我都在文中标注了"不确定"。

## 一、目录结构

```
IonRifleMod/
├── About/
│   └── About.xml
├── Defs/
│   ├── ThingDefs/
│   │   └── Weapons_Ranged_IonRifle.xml
│   │   └── Projectiles_IonRifle.xml        （可选：想自定义弹道时用）
│   ├── RecipeDefs/
│   │   └── Recipes_IonRifle.xml
│   └── ResearchProjectDefs/
│       └── Research_IonRifle.xml           （可选：自定义研究）
└── Textures/
    └── Things/
        └── Item/
            └── Equipment/
                └── IonRifle.png            （128×64 左右，透明底，枪口朝右/朝上按原版风格）
```

要点：**文件名随便取**，RimWorld 是扫描整个 `Defs/` 目录加载的，目录名和文件名都不参与匹配；但 `defName` 必须全局唯一。

## 二、About/About.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<ModMetaData>
  <name>Ion Rifle</name>
  <author>你的名字</author>
  <packageId>yourname.ionrifle</packageId>
  <supportedVersions>
    <li>1.5</li>
    <li>1.6</li>
  </supportedVersions>
  <description>Adds the ion rifle, a spacer-tier ranged weapon with 30 tile range and 15 damage per shot.</description>
</ModMetaData>
```

- `packageId` 只能小写字母、数字和点，**必须是全局唯一**，重复会导致模组无法加载。
- `supportedVersions` 里写错版本会让游戏提示"可能不兼容"，按你实际发布的版本填。

## 三、武器本体 Defs/ThingDefs/Weapons_Ranged_IonRifle.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<Defs>

  <ThingDef ParentName="BaseWeapon">
    <defName>IonRifle</defName>
    <label>ion rifle</label>
    <description>A spacer-made directed-energy rifle that accelerates ionized particles down a magnetic channel. Longer reach than a charge rifle, and each hit lands harder, at the cost of a slower and heavier frame.</description>

    <!-- 贴图：去掉 .png 后缀，路径相对 Textures/ -->
    <graphicData>
      <texPath>Things/Item/Equipment/IonRifle</texPath>
      <graphicClass>Graphic_Single</graphicClass>
      <drawSize>1.4</drawSize>
    </graphicData>

    <techLevel>Spacer</techLevel>
    <weaponClasses>
      <li>SpacerGun</li>
    </weaponClasses>

    <!-- 让武器能出现在商人库存 / 生成规则里；拼错会静默报 XML 错误，先少写几个更保险 -->
    <tradeTags>
      <li>TradeTag_Weapon</li>
      <li>RangedWeapon</li>
    </tradeTags>

    <weaponTags>
      <li>SpacerGun</li>
      <li>Gun</li>
      <li>Rifle</li>
    </weaponTags>

    <statBases>
      <WorkToMake>24000</WorkToMake>
      <Mass>4.2</Mass>
      <MarketValue>1250</MarketValue>
      <AccuracyTouch>0.50</AccuracyTouch>
      <AccuracyShort>0.70</AccuracyShort>
      <AccuracyMedium>0.85</AccuracyMedium>
      <AccuracyLong>0.92</AccuracyLong>
      <RangedWeapon_Cooldown>1.5</RangedWeapon_Cooldown>
    </statBases>

    <equippedStatOffsets />

    <!-- 近战：被打脸时的枪托伤害 -->
    <tools>
      <li>
        <label>stock</label>
        <capacities>
          <li>Blunt</li>
        </capacities>
        <power>9</power>
        <cooldown>2</cooldown>
      </li>
      <li>
        <label>barrel</label>
        <capacities>
          <li>Blunt</li>
          <li>Poke</li>
        </capacities>
        <power>9</power>
        <cooldown>2</cooldown>
      </li>
    </tools>

    <!-- ★ 核心：射程与伤害都在这里 -->
    <verbs>
      <li Class="Verb_LaunchProjectile">
        <verbClass>Verb_LaunchProjectile</verbClass>
        <label>ion burst</label>
        <range>30</range>              <!-- 射程 30 格 -->
        <minRange>1.2</minRange>
        <warmupTime>1.6</warmupTime>
        <defaultProjectile>Bullet_ChargeRifle</defaultProjectile>
        <forcedMissRadius>0.0</forcedMissRadius>
        <burstShotCount>3</burstShotCount>
        <burstShotDelay>4</burstShotDelay>
        <ticksBetweenBurstShots>4</ticksBetweenBurstShots>
        <cooldownTime>1.5</cooldownTime>
        <damageDef>RangedStab</damageDef>
        <damageAmountBase>15</damageAmountBase>   <!-- 单发伤害 15 -->
        <soundCast>Shot_ChargeRifle</soundCast>
        <soundCastTail>GunTail_Medium</soundCastTail>
        <muzzleFlashScale>9</muzzleFlashScale>
      </li>
    </verbs>

    <comps>
      <li Class="CompProperties_Biocodable">
        <compClass>CompBiocodable</compClass>
      </li>
    </comps>
  </ThingDef>

</Defs>
```

### 关于射程 30 与伤害 15 的准确位置

| 需求 | 字段 | 位置 |
| --- | --- | --- |
| 射程 30 格 | `<range>30</range>` | `verbs` → `li` |
| 单发伤害 15 | `<damageAmountBase>15</damageAmountBase>` | 同一个 `li` 里，紧挨着 `damageDef` |

容易踩的坑：

1. **伤害不要写进 `statBases`**。`statBases` 里的 `AccuracyXxx`、`Mass` 这类才是 StatDef；伤害是 verb 的属性，写错位置游戏会在启动时抛 XML 错误。
2. `damageAmountBase` 的好处是**覆盖投射物的伤害**。所以你可以直接复用 `Bullet_ChargeRifle` 这个投射物，它本来 12 伤害，武器上写了 15 就以 15 结算——这也是原版 ChargeLance 之类的做法。
3. `range` 的判定单位是**格（cell/tile）**，30 格已经比原版突击步枪（约 25.9）远，接近狙击枪（约 45）的一半。
4. 30 格会进入 `AccuracyLong` 之外的 `AccuracyExtreme` 区间（>25 格）。如果你不写 `AccuracyExtreme`，游戏默认按 1.0 处理，所以建议要么显式补一个 `<AccuracyExtreme>0.85</AccuracyExtreme>`，要么接受默认值——**这一点我记不准默认值到底是哪一档，建议实机用开发者模式打开信息卡核对一次**。
5. `burstShotCount` + `burstShotDelay` + `ticksBetweenBurstShots` 三个字段在原版里属于历史遗留，不同版本生效的字段名略有差别（`burstShotDelay` 是旧写法，新版本是 `ticksBetweenBurstShots`）。**同时写上不报错**，但如果你发现点射间隔不对，删掉其中一个再测。
6. 不想要点射就删掉 `burstShotCount` 那几行，改成单发。

## 四、（可选）自定义投射物 Defs/ThingDefs/Projectiles_IonRifle.xml

想让弹道带点蓝色辉光、或换一种伤害类型再加这个；不加就继续用 `Bullet_ChargeRifle`。

```xml
<?xml version="1.0" encoding="utf-8"?>
<Defs>

  <ThingDef ParentName="BaseBullet">
    <defName>IonRifle_Projectile</defName>
    <label>ion bolt</label>
    <graphicData>
      <texPath>Things/Projectile/ion_bolt</texPath>
      <graphicClass>Graphic_Single</graphicClass>
      <drawSize>3.0</drawSize>
    </graphicData>
    <projectile>
      <damageDef>RangedStab</damageDef>
      <damageAmountBase>15</damageAmountBase>
      <speed>60</speed>
      <stoppingPower>1.5</stoppingPower>
    </projectile>
  </ThingDef>

</Defs>
```

改用它时，把武器 verb 里的 `defaultProjectile` 换成 `<defaultProjectile>IonRifle_Projectile</defaultProjectile>`。

关于 `damageDef` 的选择（**这三条的机制我很确定，但哪条最"好玩"取决于你**）：

- `RangedStab`：跟普通子弹一样会被护甲减免（Sharp 护甲生效），最好平衡，**推荐先用它**。
- `RangedBurn`：能量武器的"离子/灼烧"感更强，而且**大多数护甲不防 Burn**——因此 15 点灼烧实际收益远高于 15 点穿刺，容易超模。
- `Bomb` / 自定义 DamageDef：想做真正的"离子"属性（比如专门打机械族）就自己写一个 DamageDef，需要另建 `Defs/DamageDefs/`。

## 五、配方 Defs/RecipeDefs/Recipes_IonRifle.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<Defs>

  <RecipeDef ParentName="BaseWeaponRecipe">
    <defName>MakeIonRifle</defName>
    <label>make ion rifle</label>
    <description>Craft an ion rifle.</description>
    <jobString>Making an ion rifle.</jobString>
    <workAmount>24000</workAmount>
    <workSpeedStat>GeneralLaborSpeed</workSpeedStat>
    <requiredGiverWorkType>Crafting</requiredGiverWorkType>
    <researchPrerequisite>ChargedShot</researchPrerequisite>
    <skillRequirements>
      <Crafting>8</Crafting>
    </skillRequirements>
    <ingredients>
      <li>
        <filter>
          <thingDefs>
            <li>Steel</li>
          </thingDefs>
        </filter>
        <count>80</count>
      </li>
      <li>
        <filter>
          <thingDefs>
            <li>Plasteel</li>
          </thingDefs>
        </filter>
        <count>45</count>
      </li>
      <li>
        <filter>
          <thingDefs>
            <li>ComponentSpacer</li>
          </thingDefs>
        </filter>
        <count>4</count>
      </li>
    </ingredients>
    <products>
      <IonRifle>1</IonRifle>
    </products>
  </RecipeDef>

</Defs>
```

**最容易漏的一步：配方的 `recipeUsers`。** 上面的 `BaseWeaponRecipe` 只给了基础结构，想让它在机械加工台出现，需要在配方里补：

```xml
<recipeUsers>
  <li>TableMachining</li>
</recipeUsers>
```

或者在 `Defs/` 里加一个 Patch 挂到机械加工台上：

```xml
<?xml version="1.0" encoding="utf-8"?>
<Patch>
  <Operation Class="PatchOperationAdd">
    <xpath>Defs/ThingDef[defName="TableMachining"]/recipes</xpath>
    <value>
      <li>MakeIonRifle</li>
    </value>
  </Operation>
</Patch>
```

（`TableMachining` 是机械加工台的 defName，这个我比较确定。但 `BaseWeaponRecipe` 这个 ParentName 以及 `requiredGiverWorkType` 等字段在不同版本里是否存在，**我没法在这里 100% 确认**——如果启动报"找不到 parentName"，就把 `ParentName` 去掉、按原版 ChargeRifle 的配方照抄结构。）

没有配方的武器也不会崩，只是**只能从商人/战利品里出**，不能造。

## 六、研究（可选）

上面的配方挂在原版 `ChargedShot`（充能射击）后面，好处是零额外代码。想做成独立科技树节点：

```xml
<?xml version="1.0" encoding="utf-8"?>
<Defs>
  <ResearchProjectDef>
    <defName>IonRifleTech</defName>
    <label>ion weaponry</label>
    <description>Unlock the ion rifle.</description>
    <baseCost>3200</baseCost>
    <techLevel>Spacer</techLevel>
    <prerequisites>
      <li>ChargedShot</li>
    </prerequisites>
    <requiredResearchBuilding>HiTechResearchBench</requiredResearchBuilding>
    <requiredResearchFacilities>
      <li>MultiAnalyzer</li>
    </requiredResearchFacilities>
    <position>x: 12, y: 4</position>
  </ResearchProjectDef>
</Defs>
```

然后把配方里的 `<researchPrerequisite>ChargedShot</researchPrerequisite>` 换成 `IonRifleTech`。`position` 是研究树上的坐标，随便挑个空格。

## 七、贴图

- 路径 `Textures/Things/Item/Equipment/IonRifle.png` 对应 `<texPath>Things/Item/Equipment/IonRifle</texPath>`，**不要写 .png 后缀**。
- 原版枪械贴图通常是横向的矩形（约 128×64），实体手持时会被缩放/旋转，`drawSize` 用来微调大小。
- 懒得画图就先复用原版贴图：把 `texPath` 改成 `Things/Item/Equipment/WeaponRanged/ChargeRifle`（**这个确切的路径写法我不能保证，建议在 RimWorld 安装目录 `Data/Core/Textures/` 下自己找一下 charge rifle 的 png，把相对路径抄过来**）。
- 贴图缺失不会报错，只会在游戏里显示成一个粉色方块。

## 八、上线前自查清单

- [ ] `packageId` 小写、唯一、带命名空间前缀
- [ ] `defName` 全局唯一（叫 `IonRifle` 和你可能装的其它模组撞名的概率不低，建议改成 `YourName_IonRifle`）
- [ ] `range` = 30、`damageAmountBase` = 15 都在 **verb 里**，不在 `statBases` 里
- [ ] `defaultProjectile` 指向的 defName 真实存在（默认的 `Bullet_ChargeRifle` 是原版的，稳妥）
- [ ] 贴图路径存在，否则出现粉色方块
- [ ] 开发者模式 → 打开信息卡，确认射程 30、伤害 15、材质/科技等级显示正确
- [ ] 若用了配方：机械加工台能看到配方，材料够时能开工
- [ ] 若装了其它改武器数值的模组，注意它们可能用 Patch 覆盖你的 verb

## 九、平衡性提醒（数值来源就是你的需求，但这把确实偏强）

- 原版充能步枪单发约 12 伤害、射程约 25.9；你这把 15 伤害 + 30 射程，还是 3 连点射的话，**有效 DPS 会明显高于原版充能步枪**，属于"后期强力武器"档位。
- 如果实测觉得超模，优先动这几个值（都不影响你要求的 30/15）：
  - `cooldownTime` 1.5 → 2.0 以上
  - `burstShotCount` 3 → 1 或 2
  - `warmupTime` 1.6 → 2.0
  - 精度曲线整体下调（近距离 0.50 已经是"贴脸很差"，可以再压低）
- 30 射程在开阔地图上收益很大，但地图边缘之外打不到东西，实战意义受地形限制。

## 十、我不确定的地方（如实列出）

1. `ticksBetweenBurstShots` vs `burstShotDelay` 在当前版本哪个生效。
2. `AccuracyExtreme` 不显式声明时的默认值。
3. `BaseWeaponRecipe` / `BaseBullet` / `BaseWeapon` 这几个 ParentName 在各版本里是否存在、字段是否一致。
4. `tradeTags` 里 `RangedWeapon` 这个标签名是否正确（拼错只会静默不生效，不会崩，但拿不到想要的商人库存行为）。
5. 原版 charge rifle 贴图的确切相对路径。

以上 5 条都建议用"照抄原版对应 Def 的结构"来消除风险——最保险的做法是打开 `RimWorld/Data/Core/Defs/ThingDefs/Weapons/`（路径大致如此）里的原版武器 XML，把 ChargeRifle 复制一份再改数值。
