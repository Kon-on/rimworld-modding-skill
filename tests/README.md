# 评测（evals）

技能宣称「让第一次写 mod 的人一次写对」，但这个宣称没有可复现的证据。这个目录把「写对」落成**机械断言**：一组固定提示词 + 每条用例的字面量断言（`contains` / `contains_any` / `not_contains` / `not_contains_line`，语义见下节）。

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
| `2026-10-18-baseline-noskill` | **不加载技能**（明令禁止读技能仓库、禁止调用 `skill` 工具），同一天同一模型的对照臂 | 1 / 4 | 14 / 25（56 分） | 2026-10-18 |
| `2026-10-18-baseline-skill` | 加载技能；RimSage MCP 未配置，走降级路径第 ② 级 | 4 / 4 | 25 / 25（100 分） | 2026-10-18 |
| `2026-10-17-baseline-skill` | 加载技能；RimSage MCP 未配置（对照 `assets/templates/` + 本地 grep 原版的路子） | 2 / 4 | 23 / 25（92 分） | 2026-10-17 |

上表分数是 **2026-10-18 修订断言后**（见下节）用同一批产出重算的：10-17 那行当时还按旧断言调过措辞，与 10-18 两行不可直接比较；10-18 的 GREEN 臂是自然作答，没有为迎合字面量改写答案。同样三份产出在修订前分别是 23/24、11/24、18/24。

## 断言修订记录（2026-10-18）

改断言让它变绿，等于把测试改成迎合答案。所以下面每一条修改都附了 1.7 原版/本仓库模板的实测依据——修的是断言把「用哪种写法」当成「对不对」的毛病，不是迁就某一份答案：

| # | 原断言 | 为什么是断言错 | 现断言 |
|---|---|---|---|
| 1 | `contains: "verbClass=\"Verb_Shoot\""` | 只有属性写法算过；原版 Core 全库 33 处 `verbClass` 全是元素写法、属性写法 0 处，技能模板 `assets/templates/weapon-ranged.xml:112` 也是元素写法 | `contains: "Verb_Shoot"`（只考用了哪个 verb 类） |
| 2 | `not_contains: "Ultratech"` | 裸词禁令会惩罚「指出用户写错了」的正确回答（合法值是 `Ultra`） | `contains: "<techLevel>Ultra</techLevel>"` + `not_contains_line: ^\s*<techLevel>\s*Ultratech\s*</techLevel>`（只禁写进 Def） |
| 3 | `not_contains: "costList"` | 近战该用 `costStuffCount`，但**远程武器原版就是 `costList`**（`RangedIndustrial.xml` 14 处），笼统禁它等于禁掉正确写法 | 近战保留 `not_contains_line: ^\s*<costList>`；远程删掉这条 |
| 4 | `contains: "rangedWeapon_Range"` | 1.6 时代的顶层字段，1.7 已移除（全库 0 处），射程写在 `verbs/li/range`；旧断言只有「警告该字段废弃」的答案才过 | `contains: "<range>"` + `not_contains_line: ^\s*<rangedWeapon_Range[\s>/]` |
| 5 | `contains: "RimSage" / "grep" / "Data/Core/Defs" / "先查原版"` | 四种动作各有无穷措辞，两臂实测都被误判——该用例不可度量 | `contains_any` 四组：`Player.log`｜`Logs\Player.log` 或 `Logs/Player.log`｜`Data/Core/Defs` 或 `原版` 或 `Core`｜`grep` 或 `搜索` 或 `检索` 或 `find` |

## RED 对照：技能到底有没有用（2026-10-18 已补）

同一天、同一模型，两臂各 4 条提示词、各派一个互不相干的 agent：

| 臂 | 条件 | 用例全通过 | 断言 | 运行目录 |
|---|---|---|---|---|
| RED | 明令禁止读技能仓库、禁止调用 `skill` 工具 | 1 / 4 | 14 / 25（56 分） | `2026-10-18-baseline-noskill` |
| GREEN | 先读 `SKILL.md`，按技能流程作答 | 4 / 4 | 25 / 25（100 分） | `2026-10-18-baseline-skill` |

断言修订后两臂之间不再有争议条目：**25 比 14，且差距全落在两条「写 Def」用例上**。差距是**实质错误**，不是措辞差异：

- `create-melee-weapon`：RED 把 `<techLevel>Ultratech</techLevel>` 写进 Def（非法枚举值，游戏加载会报 `is not a valid value for`），并用 `costList` 绕过 `costStuffCount` / `stuffCategories`；GREEN 9 / 9，走技能已验证模板，并显式纠正用户给错的枚举值。
- `create-ranged-weapon`：RED 把伤害写在 verb 的 `damageAmountBase`（1.7 原版把弹丸伤害放在 `projectile/damageAmountBase`）、父级用 `BaseWeapon`、verb 类用 `Verb_LaunchProjectile`；GREEN 5 / 5，弹丸与枪体两段分清。
- `check-techlevel-enum`：两臂都满分。这类「模型本来就知道」的知识点，技能带不来分，只能证明断言没写错。
- `debug-missing-def`：GREEN 4 / 4、RED 3 / 4——RED 差在「1.7 日志在 `Logs\Player.log`」这一组（它给的是旧 Unity 路径）。这条用例现在的区分度就落在日志路径上。

本轮 GREEN 臂顺带查出技能文档两处过时，已按实测修掉（2026-10-18）：

1. `references/08-debugging.md` 的日志路径少了 `Logs\` 一层（1.7 实测 `…\RimWorld by Ludeon Studios\Logs\Player.log`）；Linux/macOS 的旧 Unity 路径与若干 1.6 菜单标签也一并按「不再保证 / 查不到」改写，`Spawn Thing` 纠正为 DLL 里实际存在的 `Spawn thing`。
2. `references/workflows/debug-crash.md:37-46` 的「开发者控制台」`list defs` / `spawn` 在 1.7 是死路（`Assembly-CSharp.dll` 无 `DevConsole` / `ExecuteCommand`），已整段换成「1.7 没有开发者控制台」+ 可用入口表（读日志 / 静态核验 / debug actions 菜单）。

## 加用例时遵守

- 只断言**能被机械判定的正确性**：字段名、父级名、枚举值、必须走到的排查动作。不断言文风、语气、段落结构。
- 四种写法按需选：`contains`（必须出现）、`contains_any`（同义写法任一命中，一组算 1 条断言）、`not_contains`（出现即错）、`not_contains_line`（正则，逐行锚定，禁止某种写法单独成行）。
- **不要用裸词做负断言**：负断言要么带 XML 语境（`<costList>`），要么锚行首（`^\s*<costList>`）——本目录已经踩过多次（见上节）。
- 每条用例 ≤ 10 条断言；一条用例只考一个能力点（写 Def / 查枚举 / 排查错误）。
- 加完跑 `--validate`，并同步更新上面的 baseline 表。

## 四条用例各自考什么

| id | 考什么 |
|---|---|
| `create-melee-weapon` | 近战武器能否选对父级、材料成本写对、科技等级枚举值不写错 |
| `create-ranged-weapon` | 远程武器能否分清「武器 Def」与「子弹 Def」、射程字段写哪 |
| `check-techlevel-enum` | 枚举值是否给全、是否编造不存在的值 |
| `debug-missing-def` | 排查顺序是否「先看日志 → 先查原版 → 再查自己的 mod」，有没有具体动作而非空话 |
