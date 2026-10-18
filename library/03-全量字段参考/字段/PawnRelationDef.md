# PawnRelationDef

- **所属线**：人物线
- **原版实例数**：28
- **字段路径数**：23
- **资料片**：Biotech、Core
- **原版出处**：`Core/Defs/PawnRelationDefs/PawnRelations_FamilyByChoice.xml`、`Core/Defs/PawnRelationDefs/PawnRelations_FamilyByBlood.xml`
- **数据来源**：`docs/def-schema.json` + `docs/def-examples.json`（由本机 RimWorld 1.7.4981 rev136 实测提取）

## 一、最小真实范例（原版原样，可直接复制改名）

```xml
<PawnRelationDef>
    <workerClass>PawnRelationWorker_Stepparent</workerClass>
    <defName>Stepparent</defName>
    <label>stepfather</label>
    <labelFemale>stepmother</labelFemale>
    <importance>150</importance>
    <opinionOffset>5</opinionOffset>
    <implied>true</implied>
  </PawnRelationDef>
  
  
```

> 来自 `Core/Defs/PawnRelationDefs/PawnRelations_FamilyByChoice.xml`，defName = `Stepparent`，XML 节点数 8（该类型中最小）

## 二、核心字段（出现率 ≥90%，可视为必填）

```text
defName                                        [文本]  例：Child / Overseer / Parent
implied                                        [布尔]  例：false / true
importance                                     [数值]  例：100 / 185 / 190
label                                          [文本]  例：birth father / father / overseer
opinionOffset                                  [数值]  例：10 / 15 / 20
workerClass                                    [文本]  例：PawnRelationWorker_Child / PawnRelationWorker_Overseer / PawnRelationWorker_Parent
```

## 三、全量字段表（23 条路径）

| 路径 | 出现率 | 值类型 | 原版样例值 |
|---|---|---|---|
| `defName` | 100.0% (28/28) | 文本 | Child / Overseer / Parent |
| `diedThought` | 75.0% (21/28) | 文本 | MyBirthMotherDied / MyBrotherDied / MyFatherDied |
| `diedThoughtFemale` | 25.0% (7/28) | 文本 | MyDaughterDied / MyMotherDied / MyNieceDied |
| `familyByBloodRelation` | 60.7% (17/28) | 布尔 | true |
| `generationChanceFactor` | 28.6% (8/28) | 数值 | 0.08 / 0.35 / 0.4 |
| `implied` | 100.0% (28/28) | 布尔 | false / true |
| `importance` | 100.0% (28/28) | 数值 | 100 / 185 / 190 |
| `inbredChanceOnChild` | 57.1% (16/28) | 数值 | 0 / 0.2 / 0.4 |
| `incestOpinionOffset` | 25.0% (7/28) | 数值 | -15 / -30 |
| `killedThought` | 75.0% (21/28) | 文本 | KilledMyBirthMother / KilledMyBrother / KilledMyFather |
| `killedThoughtFemale` | 10.7% (3/28) | 文本 | KilledMyDaughter / KilledMyMother / KilledMySister |
| `label` | 100.0% (28/28) | 文本 | birth father / father / overseer |
| `labelFemale` | 71.4% (20/28) | 文本 | birth mother / daughter / mother |
| `lostThought` | 75.0% (21/28) | 文本 | MyBirthMotherLost / MyBrotherLost / MyFatherLost |
| `lostThoughtFemale` | 28.6% (8/28) | 文本 | MyDaughterLost / MyMotherLost / MyNieceLost |
| `opinionOffset` | 96.4% (27/28) | 数值 | 10 / 15 / 20 |
| `reflexive` | 25.0% (7/28) | 布尔 | true |
| `removeOnDeath` | 3.6% (1/28) | 布尔 | true |
| `removeOnLeftBehind` | 3.6% (1/28) | 布尔 | true |
| `romanceChanceFactor` | 60.7% (17/28) | 数值 | 0.03 / 0.25 / 0.5 |
| `soldThoughts` | 50.0% (14/28) | 容器 |  |
| `soldThoughts/li` | 53.6% (15/28) | 文本 | SoldMyBondedAnimal / SoldMyBondedAnimalMood / SoldMyLovedOne |
| `workerClass` | 92.9% (26/28) | 文本 | PawnRelationWorker_Child / PawnRelationWorker_Overseer / PawnRelationWorker_Parent |

## 四、原版 defName 一览（共 28 个，列出前 60）

```text
`Stepparent`                      `Stepchild`                       `ParentInLaw`                     `ChildInLaw`                    
`Overseer`                        `ExLover`                         `ExSpouse`                        `Kin`                           
`CousinOnceRemoved`               `SecondCousin`                    `Bond`                            `GreatGrandparent`              
`GreatGrandchild`                 `GranduncleOrGrandaunt`           `GrandnephewOrGrandniece`         `Lover`                         
`ParentBirth`                     `Grandparent`                     `Grandchild`                      `Cousin`                        
`HalfSibling`                     `Spouse`                          `Fiance`                          `NephewOrNiece`                 
`UncleOrAunt`                     `Parent`                          `Child`                           `Sibling`                       
```
