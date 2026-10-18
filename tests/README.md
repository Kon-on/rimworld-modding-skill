# 评测（evals）

技能宣称「让第一次写 mod 的人一次写对」，但这个宣称没有可复现的证据。这个目录把「写对」落成**机械断言**：一组固定提示词 + 每条用例的 `contains` / `not_contains` 字面量。

分工：**产出由 agent 生成，判定由脚本完成**。断言必须机械可判，所以这里不用 LLM 打分——同一份回答，任何人跑脚本都得到同一个分数。

## 怎么跑

```bash
node tests/run-evals.mjs --validate          # 校验用例结构（CI 每次提交都跑）
node tests/run-evals.mjs --list              # 看用例
node tests/run-evals.mjs --prompts           # 导出提示词包，粘贴给你要测的 agent
node tests/run-evals.mjs --check <id> <file> # 只检查一份产出
node tests/run-evals.mjs --check-all <dir>   # 检查一个运行目录，打印分数并写 results.json
node tests/test-find-template.mjs            # 模板检索脚本冒烟测试
node tests/test-xml-lint.mjs                 # XML 模板良构性测试
```

运行目录约定：`tests/runs/<日期>-<条件>/`，每个用例一个 `<id>.md`（回答原文，不做任何美化加工），`results.json` 由脚本生成，不要手改。

## 模板检索脚本的冒烟测试

`scripts/find-template.mjs` 是技能运行时查模板库的入口，它的行为由 `tests/test-find-template.mjs` 守住：模板清单、按 Def 类型查模板与必填字段、按字段名查路径与出现率、关键词检索、查无结果返回非零码、`--json` 可被解析。

它读 `library/`（301 文件，随仓库提交）。**库不在本机时脚本打印「⚠️ 跳过」并以 0 退出**——这样没带数据的新 clone 和 CI 不会误红；代价是这条测试等于没跑，别把它当证据。

## XML 模板良构性测试

技能承诺「有模板 → 直接用（免核验）」，所以模板必须是**合法 XML**——不是「看起来对」就行。本项目曾 8 个模板里 7 个解析失败：元素文本里写了 `<YourPrefix>` 这种尖括号占位符（XML 解析器把它当标签，报 `The 'YourName' start tag … does not match the end tag of 'defName'`），以及注释里出现 `--` 连字符 runs。

`scripts/xml-lint.mjs` 是零依赖的良构扫描器，`tests/test-xml-lint.mjs` 守两件事：两个历史缺陷必须被判非法（回归护栏），`assets/templates/*.xml` 全部必须良构。这条测试**不需要模板库**，任何环境都会真跑。

写法约定：模板里的用户自定义值用 `{{YourXxx}}`（如 `{{YourPrefix}}_Weapon_{{YourName}}`），不要写 `<YourXxx>`。

## 当前 baseline

| 运行目录 | 条件 | 用例全通过 | 断言 | 日期 |
|---|---|---|---|---|
| `2026-10-18-baseline-noskill` | **不加载技能**（明令禁止读技能仓库、禁止调用 `skill` 工具），同一天同一模型的对照臂 | 1 / 4 | 11 / 24（46 分） | 2026-10-18 |
| `2026-10-18-baseline-skill` | 加载技能；RimSage MCP 未配置，走降级路径第 ② 级 | 1 / 4 | 18 / 24（75 分） | 2026-10-18 |
| `2026-10-17-baseline-skill` | 加载技能；RimSage MCP 未配置，走降级路径第 ② 级（对照 `assets/templates/` + 本地 grep 原版的路子） | 3 / 4 | 23 / 24（96 分） | 2026-10-17 |

`2026-10-17` 那一行当时按断言调过措辞（见下节第 2、3 条），分数偏高，**不能**与 10-18 两行直接比较。10-18 的 GREEN 臂是自然作答，没有为迎合字面量改写答案，因此被判负的条目里有 4 条属于断言缺陷；两臂的对照结论见「RED 对照」一节。

## 已知断言缺陷（记录在案，未擅自修改）

改断言让它变绿，等于把测试改成迎合答案。以下四条等 owner 定夺：

1. **`verbClass="Verb_Shoot"` 是属性写法，技能教的是元素写法。** `assets/templates/weapon-ranged.xml:85` 写的是 `<verbClass>Verb_Shoot</verbClass>`，本 baseline 也这么写。断言把「用哪种 XML 语法」当成了「用了哪个 verb 类」。建议改为 `"Verb_Shoot"`，或同时接受两种写法。
2. **`not_contains: "Ultratech"` 会惩罚诚实纠错。** 用户提示词里把 `Ultra` 写错时，正确回答应该是「这个值不合法，用 Ultra」——但那句话本身就含被禁字面量。本 baseline 是绕开字面量通过的（只输出合法值），等于断言在教「别指出用户的错」。建议改为 `<techLevel>Ultratech</techLevel>`，只禁「把错值写进 Def」。
3. **`not_contains: "costList"` 同类问题。** 「不要手写 costList，用 costStuffCount」是正确的提醒，却会被判失败（本轮已按断言改了措辞）。建议加尖括号：`<costList>`，而且只保留在近战用例里——远程武器的原版枪械本来就是 `costList`（`Gun_Revolver`、`Gun_ChargeRifle`），在 `create-ranged-weapon` 里禁它等于禁掉正确写法。
4. **`contains: "rangedWeapon_Range"` 是 1.6 时代的旧路径，1.7 已移除。** 1.7 原版全库查不到 `rangedWeapon_Range` 这个字段路径，射程写在 `verbs/li/range`（Core 的 `RangedIndustrial.xml` 等 9 个武器文件实测，74/2054 个 ThingDef 用到）；技能模板 `assets/templates/weapon-ranged.xml:8-11` 教的正是「别把 `rangedWeapon_Range` 写在顶层」。这条断言现在只在答案**警告该字段已废弃**时才通过（2026-10-18 的 GREEN 臂就是这样过的），却让把 `<range>` 正确写进 verb 的答案（RED 臂）判负。建议改为断言 verb 段里的 `<range>`。

## RED 对照：技能到底有没有用（2026-10-18 已补）

同一天、同一模型，两臂各 4 条提示词、各派一个互不相干的 agent：

| 臂 | 条件 | 用例全通过 | 断言 | 运行目录 |
|---|---|---|---|---|
| RED | 明令禁止读技能仓库、禁止调用 `skill` 工具 | 1 / 4 | 11 / 24（46 分） | `2026-10-18-baseline-noskill` |
| GREEN | 先读 `SKILL.md`，按技能流程作答 | 1 / 4 | 18 / 24（75 分） | `2026-10-18-baseline-skill` |

按上节 4 条断言缺陷折算，GREEN 是 3 / 4（21 / 24），RED 仍是 1 / 4。差距集中在两条「写 Def」用例，而且是**实质错误**，不是措辞差异：

- `create-melee-weapon`：RED 把 `<techLevel>Ultratech</techLevel>` 写进 Def（非法枚举值，游戏加载会报 `is not a valid value for`），并用 `costList` 绕过 `costStuffCount` / `stuffCategories`；GREEN 8 / 8，走技能已验证模板，并显式纠正用户给错的枚举值。
- `create-ranged-weapon`：RED 把伤害写在 verb 的 `damageAmountBase`（1.7 原版把弹丸伤害放在 `projectile/damageAmountBase`）、父级用 `BaseWeapon`、verb 类用 `Verb_LaunchProjectile`；GREEN 走模板，弹丸与枪体两段分清。
- `check-techlevel-enum`：RED 也全过。这类「模型本来就知道」的知识点，技能带不来分，只能证明断言没写错。
- `debug-missing-def`：两臂都只过 1 / 4，失败的全是短语断言（`RimSage` / `grep` / `Data/Core/Defs` / `先查原版`）——**该用例目前不可度量**，需要改成「同类动作任一命中」，例如 `RimSage` 或 `MCP`、`原版` 或 `Core`、`grep` 或 `检索`。

本轮 GREEN 臂顺带查出技能文档两处过时（已独立复核，尚未改技能内容，等 owner 定夺）：

1. `references/08-debugging.md:42` 的日志路径少了 `Logs\` 一层。1.7 实测是 `%USERPROFILE%\AppData\LocalLow\Ludeon Studios\RimWorld by Ludeon Studios\Logs\Player.log`，旧路径已不存在。
2. `references/workflows/debug-crash.md:41-46` 的「开发者控制台」`list defs` / `spawn` 在 1.7 是死路：`Assembly-CSharp.dll` 里没有 `DevConsole` / `ExecuteCommand` 字符串，只剩调试动作面板（`Dev_ToggleDevPalette` / `DebugActionsPalette`）。

## 加用例时遵守

- 只断言**能被机械判定的正确性**：字段名、父级名、枚举值、必须走到的排查动作。不断言文风、语气、段落结构。
- 字面量要带 XML 语境（`<techLevel>Ultra</techLevel>`），裸词会误伤正常文案——本目录已经踩过多次（见上节）。
- 每条用例 ≤ 8 条断言；一条用例只考一个能力点（写 Def / 查枚举 / 排查错误）。
- 加完跑 `--validate`，并同步更新上面的 baseline 表。

## 四条用例各自考什么

| id | 考什么 |
|---|---|
| `create-melee-weapon` | 近战武器能否选对父级、材料成本写对、科技等级枚举值不写错 |
| `create-ranged-weapon` | 远程武器能否分清「武器 Def」与「子弹 Def」、射程字段写哪 |
| `check-techlevel-enum` | 枚举值是否给全、是否编造不存在的值 |
| `debug-missing-def` | 排查顺序是否「先看日志 → 先查原版 → 再查自己的 mod」，有没有具体动作而非空话 |
