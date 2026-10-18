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
| `2026-10-17-baseline-skill` | 加载技能；RimSage MCP 未配置，走降级路径第 ② 级（对照 `assets/templates/` + 本地 grep 原版的路子） | 3 / 4 | 23 / 24（96 分） | 2026-10-17 |

未通过的一条：`create-ranged-weapon` 缺 `verbClass="Verb_Shoot"`。这不是产出错了，是断言写错了——见下节。

## 已知断言缺陷（记录在案，未擅自修改）

改断言让它变绿，等于把测试改成迎合答案。以下三条等 owner 定夺：

1. **`verbClass="Verb_Shoot"` 是属性写法，技能教的是元素写法。** `assets/templates/weapon-ranged.xml:44` 写的是 `<verbClass>Verb_Shoot</verbClass>`，本 baseline 也这么写。断言把「用哪种 XML 语法」当成了「用了哪个 verb 类」。建议改为 `"Verb_Shoot"`，或同时接受两种写法。
2. **`not_contains: "Ultratech"` 会惩罚诚实纠错。** 用户提示词里把 `Ultra` 写错时，正确回答应该是「这个值不合法，用 Ultra」——但那句话本身就含被禁字面量。本 baseline 是绕开字面量通过的（只输出合法值），等于断言在教「别指出用户的错」。建议改为 `<techLevel>Ultratech</techLevel>`，只禁「把错值写进 Def」。
3. **`not_contains: "costList"` 同类问题。** 「不要手写 costList，用 costStuffCount」是正确的提醒，却会被判失败（本轮已按断言改了措辞）。建议加尖括号：`<costList>`。

## RED baseline（待补）

现有 baseline 都是「有技能」条件下的。要证明断言真能区分好坏，还需要一次**不加载技能**的对照：同样 4 条提示词，存到 `tests/runs/<日期>-baseline-noskill/`。

预期：无技能的回答会命中 `not_contains`（把错枚举照抄进 Def）、或漏 `contains`（不会用 `BaseHumanMakeableGun` 父级、不知道去 grep 原版）。如果无技能也能拿 90 分以上，说明这组断言太弱，需要加得更刁。

## 加用例时遵守

- 只断言**能被机械判定的正确性**：字段名、父级名、枚举值、必须走到的排查动作。不断言文风、语气、段落结构。
- 字面量要带 XML 语境（`<techLevel>Ultra</techLevel>`），裸词会误伤正常文案——本目录已经踩过两次。
- 每条用例 ≤ 8 条断言；一条用例只考一个能力点（写 Def / 查枚举 / 排查错误）。
- 加完跑 `--validate`，并同步更新上面的 baseline 表。

## 四条用例各自考什么

| id | 考什么 |
|---|---|
| `create-melee-weapon` | 近战武器能否选对父级、材料成本写对、科技等级枚举值不写错 |
| `create-ranged-weapon` | 远程武器能否分清「武器 Def」与「子弹 Def」、射程字段写哪 |
| `check-techlevel-enum` | 枚举值是否给全、是否编造不存在的值 |
| `debug-missing-def` | 排查顺序是否「先看日志 → 先查原版 → 再查自己的 mod」，有没有具体动作而非空话 |
