# DifficultyDef

- **所属线**：世界线
- **原版实例数**：7
- **字段路径数**：35
- **资料片**：Core
- **原版出处**：`Core/Defs/Misc/DifficultyDefs/Difficulties.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<DifficultyDef>
    <defName>Custom</defName>
    <label>Custom</label>
    <description>This setting allows you to define your own playstyle in detail.

(*SectionTitle)Recommended for:(/SectionTitle)

- Players who are happy with one of the standard playstyles levels, but want to change a few things.
- Players who want to experiment with something different.</description>
    <isCustom>true</isCustom>
    <!-- no specific values defined, they are aren't used when Custom is selected -->
  </DifficultyDef>
```

> 来自 `Core/Defs/Misc/DifficultyDefs/Difficulties.xml`，defName = `Custom`，XML 节点数 6（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Easy / Medium / Peaceful
description                                    [文本]  例：Build a community in a sandbox environment. Major direct threats are disabled, b / Build a community with a taste of danger. Threats appear, but they're weakened.
 / Strive to survive on a rough, tough planet. There will be triumph and tragedy.


label                                          [文本]  例：adventure story / community builder / peaceful
```

## 三、全量字段表（35 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `adaptationEffectFactor` | 42.9% (3/7) | 数值 | 0.4 / 0.7 / 0.9 |
| `adaptationGrowthRateFactorOverZero` | 85.7% (6/7) | 数值 | 0 / 0.25 / 0.75 |
| `allowBigThreats` | 14.3% (1/7) | 布尔 | false |
| `allowCaveHives` | 14.3% (1/7) | 布尔 | false |
| `allowExtremeWeatherIncidents` | 28.6% (2/7) | 布尔 | false |
| `allowIntroThreats` | 14.3% (1/7) | 布尔 | false |
| `allowViolentQuests` | 14.3% (1/7) | 布尔 | false |
| `butcherYieldFactor` | 28.6% (2/7) | 数值 | 0.8 / 0.9 |
| `colonistMoodOffset` | 85.7% (6/7) | 数值 | -5 / 0 / 10 |
| `cropYieldFactor` | 85.7% (6/7) | 数值 | 0.8 / 0.95 / 1 |
| `deepDrillInfestationChanceFactor` | 85.7% (6/7) | 数值 | 0 / 0.25 / 0.75 |
| `defName` | 100.0% (7/7) | 文本 | Easy / Medium / Peaceful |
| `description` | 100.0% (7/7) | 文本 | Build a community in a sandbox environment. Major direct threats are disabled, b / Build a community with a ta |
| `difficulty` | 85.7% (6/7) | 数值 | 0 / 1 / 2 |
| `diseaseIntervalFactor` | 85.7% (6/7) | 数值 | 1 / 1.5 / 2.5 |
| `enemyDeathOnDownedChanceFactor` | 85.7% (6/7) | 数值 | 0.5 / 0.90 / 1 |
| `enemyReproductionRateFactor` | 85.7% (6/7) | 数值 | 0.1 / 0.15 / 0.5 |
| `fishingYieldFactor` | 28.6% (2/7) | 数值 | 0.8 / 0.9 |
| `foodPoisonChanceFactor` | 85.7% (6/7) | 数值 | 0.3 / 0.5 / 0.75 |
| `isCustom` | 14.3% (1/7) | 布尔 | true |
| `label` | 100.0% (7/7) | 文本 | adventure story / community builder / peaceful |
| `maintenanceCostFactor` | 85.7% (6/7) | 数值 | 1 |
| `manhunterChanceOnDamageFactor` | 14.3% (1/7) | 数值 | 0.25 |
| `mineYieldFactor` | 85.7% (6/7) | 数值 | 0.8 / 0.95 / 1 |
| `minThreatPointsRangeCeiling` | 28.6% (2/7) | 数值 | 45 |
| `nomadicMineableResourcesFactor` | 85.7% (6/7) | 数值 | 0.5 / 0.75 / 1 |
| `peacefulTemples` | 14.3% (1/7) | 布尔 | true |
| `playerPawnInfectionChanceFactor` | 57.1% (4/7) | 数值 | 0.3 / 0.5 / 0.75 |
| `predatorsHuntHumanlikes` | 28.6% (2/7) | 布尔 | false |
| `researchSpeedFactor` | 85.7% (6/7) | 数值 | 0.9 / 0.95 / 1 |
| `scariaRotChance` | 85.7% (6/7) | 数值 | 0 / 0.000 / 0.333 |
| `studyEfficiencyFactor` | 57.1% (4/7) | 数值 | 0.8 / 0.9 / 1.2 |
| `threatScale` | 85.7% (6/7) | 数值 | 0.10 / 0.30 / 0.60 |
| `tradePriceFactorLoss` | 28.6% (2/7) | 数值 | 0.10 / 0.20 |
| `wastepackInfestationChanceFactor` | 85.7% (6/7) | 数值 | 0 / 0.25 / 0.5 |

## 四、原版 defName 一览（共 7 个，列出前 60）

```text
`Custom`                          `Rough`                           `Medium`                          `Easy`                          
`Hard`                            `Extreme`                         `Peaceful`                      
```
