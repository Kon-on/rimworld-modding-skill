#!/usr/bin/env node
// 模板检索的冒烟测试：先跑它，再信它。
// 用法：node tests/test-find-template.mjs
// 库不在本机时（例如刚 clone 下来还没放数据）会明确打印「跳过」并以 0 退出——
// 跳过不等于通过，输出里会写清楚。
import { existsSync } from "node:fs";
import { main, locateLibrary } from "../scripts/find-template.mjs";

const lib = locateLibrary();
if (!lib) {
  console.log("⚠️  跳过：本机未找到 RimWorld 1.7 模板库。");
  console.log("   期望路径：library/（或设置环境变量 RIMWORLD_TEMPLATE_LIB / 用 --lib 指定）");
  process.exit(0);
}

let pass = 0;
const failures = [];

function run(args) {
  const lines = [];
  const code = main(args, { out: (s) => lines.push(s) });
  return { code, text: lines.join("\n") };
}
function check(name, fn) {
  try {
    const problem = fn();
    if (problem) failures.push(`${name} —— ${problem}`);
    else { pass++; console.log(`✅ ${name}`); }
  } catch (e) {
    failures.push(`${name} —— 抛异常：${e.message}`);
  }
}
const need = (haystack, needle) => (haystack.includes(needle) ? null : `输出里没有 "${needle}"`);

console.log(`模板库：${lib}`);

check("--list 列出全部模板（含武器模板与 C# 线）", () => {
  const { code, text } = run(["--list"]);
  if (code !== 0) return `退出码 ${code}`;
  return need(text, "01-ThingDef-武器.md") ?? need(text, "07-CSharp");
});

check("--def ThingDef：给出 4 份模板 + 字段表 + 实例数", () => {
  const { code, text } = run(["--def", "ThingDef"]);
  if (code !== 0) return `退出码 ${code}`;
  return need(text, "01-ThingDef-武器.md")
    ?? need(text, "04-ThingDef-动物.md")
    ?? need(text, "字段/ThingDef.md")
    ?? need(text, "2054");
});

check("--field verbClass：命中嵌套路径与出现率", () => {
  const { code, text } = run(["--field", "verbClass"]);
  if (code !== 0) return `退出码 ${code}`;
  return need(text, "verbs/li/verbClass") ?? need(text, "ThingDef") ?? need(text, "%");
});

check("关键词检索「武器」命中武器模板", () => {
  const { code, text } = run(["武器"]);
  if (code !== 0) return `退出码 ${code}`;
  return need(text, "01-ThingDef-武器.md");
});

check("查不到时以非零码退出（关键词）", () => {
  const { code } = run(["ZZ_不存在的关键字_ZZ"]);
  return code === 1 ? null : `期望退出码 1，实际 ${code}`;
});

check("查不到时以非零码退出（Def 类型）", () => {
  const { code } = run(["--def", "ZZNotADefType"]);
  return code === 1 ? null : `期望退出码 1，实际 ${code}`;
});

check("--json 输出可被 JSON.parse 且带 defType", () => {
  const { code, text } = run(["--json", "--def", "ThingDef"]);
  if (code !== 0) return `退出码 ${code}`;
  try {
    const j = JSON.parse(text);
    return j.defType === "ThingDef" ? null : `defType = ${j.defType}`;
  } catch (e) { return `不是合法 JSON：${e.message}`; }
});

console.log(`\n通过 ${pass} / ${pass + failures.length}`);
if (failures.length) {
  console.log("\n失败：");
  for (const f of failures) console.log("❌ " + f);
  process.exit(1);
}
