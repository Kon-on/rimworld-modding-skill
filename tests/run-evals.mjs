#!/usr/bin/env node
/*
 * run-evals.mjs —— rimworld-modding 技能评测运行器（零依赖，Node 18+）
 *
 * 分工：产出必须由 agent 生成（有 skill / 无 skill 各跑一次），断言是机械的，交给脚本。
 * 本脚本只做四件事：列用例、导出提示词包、校验用例结构（CI）、按断言给产出打分。
 *
 * 断言的四种写法（大小写敏感，全部是对产出文本的字面量检查）：
 *   contains          字符串必须出现
 *   contains_any      字符串数组的数组，每一组里**任一**写法出现即算过（用于同义写法）
 *   not_contains      字符串出现即算错（正文里也不许出现，只用于「出现就是错」的写法）
 *   not_contains_line 正则数组，**单独成行**即算错（允许正文里引用/纠错，只禁正文里这样写）
 *
 * 用法：
 *   node tests/run-evals.mjs --list                    列出用例
 *   node tests/run-evals.mjs --prompts                 导出可粘贴给 agent 的提示词包
 *   node tests/run-evals.mjs --validate                校验 evals.json 结构（CI 用）
 *   node tests/run-evals.mjs --check <id> <产出文件>    检查单份产出
 *   node tests/run-evals.mjs --check-all <运行目录>     检查目录下 <id>.md 全部产出并写 results.json
 *   node tests/run-evals.mjs --check-all <dir> --json  同时打印 JSON
 */
import { readFileSync, writeFileSync, existsSync } from "node:fs";
import { dirname, join, resolve, basename } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const EVALS = join(ROOT, "tests/evals.json");
const argv = process.argv.slice(2);
const cmd = argv[0] ?? "--help";
const flag = (f) => argv.includes(f);
const arg = (f) => { const i = argv.indexOf(f); return i >= 0 ? argv[i + 1] : undefined; };

if (!existsSync(EVALS)) { console.error("找不到 " + EVALS); process.exit(2); }
const data = JSON.parse(readFileSync(EVALS, "utf8"));
const prompts = data.prompts ?? [];

function assertText(expect, text) {
  const passed = [], failed = [];
  for (const needle of expect.contains ?? []) {
    if (text.includes(needle)) passed.push({ kind: "contains", needle });
    else failed.push({
      kind: "contains", needle,
      note: text.toLowerCase().includes(String(needle).toLowerCase()) ? "命中但大小写不符" : "未找到",
    });
  }
  for (const group of expect.contains_any ?? []) {
    const alts = Array.isArray(group) ? group : [group];
    const hit = alts.find((s) => text.includes(s));
    if (hit) passed.push({ kind: "contains_any", needle: alts.join(" | "), note: "命中 " + JSON.stringify(hit) });
    else failed.push({ kind: "contains_any", needle: alts.join(" | "), note: "以下写法一个都没出现" });
  }
  for (const needle of expect.not_contains ?? []) {
    if (text.includes(needle)) {
      const line = text.slice(0, text.indexOf(needle)).split("\n").length;
      failed.push({ kind: "not_contains", needle, note: "不应出现，却在第 " + line + " 行出现" });
    } else passed.push({ kind: "not_contains", needle });
  }
  for (const pattern of expect.not_contains_line ?? []) {
    const rx = new RegExp(pattern);
    const lines = text.split("\n");
    const i = lines.findIndex((l) => rx.test(l));
    if (i < 0) passed.push({ kind: "not_contains_line", needle: pattern });
    else failed.push({ kind: "not_contains_line", needle: pattern, note: "不该单独成行，却在第 " + (i + 1) + " 行出现：" + lines[i].trim().slice(0, 80) });
  }
  return { passed, failed };
}

function validate() {
  const bad = [];
  if (!Array.isArray(prompts) || prompts.length === 0) bad.push("prompts 必须是非空数组");
  const ids = new Set();
  prompts.forEach((p, i) => {
    const at = "prompts[" + i + "]";
    if (typeof p.id !== "string" || !/^[a-z0-9-]+$/.test(p.id)) bad.push(at + ".id 必须是 kebab-case 字符串");
    else if (ids.has(p.id)) bad.push(at + ".id 重复：" + p.id); else ids.add(p.id);
    if (typeof p.prompt !== "string" || !p.prompt.trim()) bad.push(at + ".prompt 不能为空");
    const e = p.expect ?? {};
    const lists = [["contains", e.contains], ["not_contains", e.not_contains], ["not_contains_line", e.not_contains_line]];
    const groups = [["contains_any", e.contains_any]];
    if (!lists.some((x) => Array.isArray(x[1]) && x[1].length) && !groups.some((x) => Array.isArray(x[1]) && x[1].length))
      bad.push(at + ".expect 至少要有一组非空断言");
    for (const [k, v] of lists) {
      if (v === undefined) continue;
      if (!Array.isArray(v) || v.some((s) => typeof s !== "string" || !s)) bad.push(at + ".expect." + k + " 必须是非空字符串数组");
    }
    for (const [k, v] of groups) {
      if (v === undefined) continue;
      if (!Array.isArray(v) || !v.length || v.some((g) => !Array.isArray(g) || !g.length || g.some((s) => typeof s !== "string" || !s)))
        bad.push(at + ".expect." + k + " 必须是「非空字符串数组」的数组（例：[['a','b'], ['c']]）");
    }
    for (const s of e.not_contains_line ?? []) {
      try { new RegExp(s); } catch { bad.push(at + ".expect.not_contains_line 里不是合法正则：" + s); }
    }
  });
  console.log("rimworld-modding 评测用例结构校验：" + prompts.length + " 条用例");
  if (!bad.length) { console.log("\u2705 结构合法。"); return 0; }
  bad.forEach((b) => console.log("\u274c " + b));
  return 1;
}

function list() {
  console.log("共 " + prompts.length + " 条评测用例（tests/evals.json）\n");
  for (const p of prompts) {
    const c = (p.expect?.contains ?? []).length, a = (p.expect?.contains_any ?? []).length;
    const n = (p.expect?.not_contains ?? []).length, r = (p.expect?.not_contains_line ?? []).length;
    console.log("- " + p.id + "  [必须包含 " + c + " 项 / 同义任一 " + a + " 组 / 必须不含 " + n + " 项 / 禁单独成行 " + r + " 条]");
    console.log("    " + p.prompt);
  }
}

function promptPack() {
  console.log("# rimworld-modding 评测提示词包\n");
  console.log("把每条提示词原样发给 agent，把回答原样存成 <运行目录>/<id>.md，再跑：");
  console.log("    node tests/run-evals.mjs --check-all <运行目录>\n");
  for (const p of prompts) {
    console.log("## " + p.id);
    console.log("提示词：" + p.prompt);
    if ((p.expect?.contains ?? []).length) console.log("必须包含：" + p.expect.contains.map((s) => JSON.stringify(s)).join(" / "));
    if ((p.expect?.contains_any ?? []).length) console.log("必须包含（同义任一）：" + p.expect.contains_any.map((g) => g.map((s) => JSON.stringify(s)).join(" 或 ")).join(" / "));
    if ((p.expect?.not_contains ?? []).length) console.log("必须不含：" + p.expect.not_contains.map((s) => JSON.stringify(s)).join(" / "));
    if ((p.expect?.not_contains_line ?? []).length) console.log("禁止单独成行：" + p.expect.not_contains_line.map((s) => JSON.stringify(s)).join(" / "));
    console.log("");
  }
}

function checkOne(id, file) {
  const p = prompts.find((x) => x.id === id);
  if (!p) { console.log("\u274c 没有这条用例：" + id); return false; }
  if (!existsSync(file)) { console.log("\u274c 找不到产出文件：" + file); return false; }
  const text = readFileSync(file, "utf8");
  const { passed, failed } = assertText(p.expect ?? {}, text);
  const ok = failed.length === 0;
  console.log((ok ? "\u2705" : "\u274c") + " " + id + (ok ? "" : "") + "  —— 通过 " + passed.length + " / 失败 " + failed.length + "  （" + basename(file) + "）");
  for (const f of failed) console.log("      \u2716 [" + f.kind + "] " + JSON.stringify(f.needle) + " —— " + f.note);
  return ok;
}

if (cmd === "--list") { list(); }
else if (cmd === "--prompts") { promptPack(); }
else if (cmd === "--validate") { process.exit(validate()); }
else if (cmd === "--check") {
  const id = arg("--check"), file = argv[argv.indexOf("--check") + 2];
  if (!id || !file) { console.error("用法：--check <用例id> <产出文件>"); process.exit(2); }
  process.exit(checkOne(id, file) ? 0 : 1);
} else if (cmd === "--check-all") {
  const dir = arg("--check-all");
  if (!dir) { console.error("用法：--check-all <运行目录>"); process.exit(2); }
  const results = [];
  let allOk = true;
  console.log("运行目录：" + dir + "\n");
  for (const p of prompts) {
    const file = join(dir, p.id + ".md");
    if (!existsSync(file)) {
      results.push({ id: p.id, ok: false, missing: true, passed: 0, failed: 0, failures: [{ kind: "missing", needle: "", note: "缺少产出文件" }] });
      allOk = false;
      console.log("\u26a0\ufe0f  " + p.id + " —— 缺少产出文件：" + file);
      continue;
    }
    const text = readFileSync(file, "utf8");
    const { passed, failed } = assertText(p.expect ?? {}, text);
    if (failed.length) allOk = false;
    results.push({ id: p.id, ok: failed.length === 0, passed: passed.length, failed: failed.length, failures: failed });
    console.log((failed.length ? "\u274c" : "\u2705") + " " + p.id + " —— 断言通过 " + passed.length + " / 失败 " + failed.length);
    for (const f of failed) console.log("      \u2716 [" + f.kind + "] " + JSON.stringify(f.needle) + " —— " + f.note);
  }
  const total = results.reduce((a, r) => a + r.passed + r.failed, 0);
  const passedTotal = results.reduce((a, r) => a + r.passed, 0);
  const summary = { promptsOk: results.filter((r) => r.ok).length, promptsTotal: prompts.length,
    assertionsPassed: passedTotal, assertionsTotal: total,
    score: total ? Math.round((passedTotal / total) * 100) : 0 };
  console.log("\n合计：" + summary.promptsOk + "/" + summary.promptsTotal + " 条用例全通过；断言 " + passedTotal + "/" + total + "（" + summary.score + "/100）");
  const out = { run: basename(resolve(dir)), date: new Date().toISOString().slice(0, 10), summary, results };
  writeFileSync(join(dir, "results.json"), JSON.stringify(out, null, 2) + "\n");
  console.log("已写入 " + join(dir, "results.json"));
  if (flag("--json")) console.log(JSON.stringify(out, null, 2));
  process.exit(allOk ? 0 : 1);
} else {
  console.log("rimworld-modding 评测运行器\n");
  console.log("  --list                    列出用例");
  console.log("  --prompts                 导出提示词包");
  console.log("  --validate                校验 evals.json 结构（CI）");
  console.log("  --check <id> <file>       检查单份产出");
  console.log("  --check-all <dir>         检查运行目录并写 results.json");
}
