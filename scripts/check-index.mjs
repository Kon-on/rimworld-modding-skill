#!/usr/bin/env node
/*
 * check-index.mjs —— rimworld-modding skill 的机械一致性校验（零依赖，Node 18+）
 *
 * 为什么存在：SKILL.md 的「模板 ↔ Def 类型对照表」和「子文件索引」是手写索引。
 * 手写索引会在目录重命名后静默漂移（本项目曾发生 38 处路径漂移而无人发现）。
 * 机械约束交给脚本，人只负责内容。
 *
 * 校验项：
 *   1. 仓库内所有 Markdown 中出现的 skill 内相对路径必须真实存在
 *   2. 不得出现重构前的旧路径前缀（templates/、workflows/、evals/）
 *   2b. 索引区块里写到的文件必须真实存在（防止索引里留下死条目）
 *   3. assets/templates/*、references/*.md、references/workflows/*.md 必须被索引区块收录
 *      （templates 还需出现在对照表区块：SKILL.md 自己要求"更新两处列表"）
 *   4. 模板注释头必须写明「验证状态：」与 AI 生成标注（仅 .xml/.cs）
 *   5. XML 模板必须良构：标签配对、注释里不得出现 `--`、占位符用 {{YourXxx}} 而非 <YourXxx>
 *
 * 用法：
 *   node scripts/check-index.mjs            校验，有问题退出码 1
 *   node scripts/check-index.mjs --strict   警告也视为失败
 *   node scripts/check-index.mjs --json     机器可读输出（CI 用）
 */
import { readFileSync, readdirSync, existsSync, statSync } from "node:fs";
import { dirname, join, resolve, relative } from "node:path";
import { fileURLToPath } from "node:url";
import { xmlProblems } from "./xml-lint.mjs";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const STRICT = process.argv.includes("--strict");
const AS_JSON = process.argv.includes("--json");

const findings = [];
const add = (level, code, message) => findings.push({ level, code, message });

const readLines = (p) => readFileSync(join(ROOT, p), "utf8").split(/\r?\n/);

// ---------- 1. 目录实际内容 ----------
function listDir(rel, keep) {
  const abs = join(ROOT, rel);
  if (!existsSync(abs)) { add("error", "dir-missing", `目录不存在：${rel}`); return []; }
  return readdirSync(abs).filter((f) => statSync(join(abs, f)).isFile() && keep(f)).sort();
}
const TEMPLATES = listDir("assets/templates", (f) => /\.(xml|cs|md)$/.test(f));
const REFERENCES = listDir("references", (f) => f.endsWith(".md"));
const WORKFLOWS = listDir("references/workflows", (f) => f.endsWith(".md"));

if (!existsSync(join(ROOT, "learnings/errors.txt"))) add("warn", "learnings-missing", "缺少 learnings/errors.txt");

// ---------- 2. 索引区块 ----------
const SKILL = readFileSync(join(ROOT, "SKILL.md"), "utf8");
function region(name) {
  const start = `<!-- INDEX:${name}:START -->`;
  const end = `<!-- INDEX:${name}:END -->`;
  const i = SKILL.indexOf(start), j = SKILL.indexOf(end);
  if (i === -1 || j === -1 || j < i) {
    add("error", "index-marker-missing", `SKILL.md 缺少索引区块标记：${start} … ${end}`);
    return "";
  }
  return SKILL.slice(i + start.length, j);
}
const REGIONS = {
  TABLE: region("TABLE"),
  TEMPLATES: region("TEMPLATES"),
  REFERENCES: region("REFERENCES"),
  WORKFLOWS: region("WORKFLOWS"),
};

// ---------- 3. 路径引用扫描 ----------
const SKILL_PREFIX = /^(assets|references|scripts|tests|learnings|docs|library|examples)\//;
const LEGACY_PREFIX = /^(templates|workflows|evals)\//;
const known = new Set([
  ...TEMPLATES.map((f) => `assets/templates/${f}`),
  ...REFERENCES.map((f) => `references/${f}`),
  ...WORKFLOWS.map((f) => `references/workflows/${f}`),
  "learnings/errors.txt",
]);

// 全仓 Markdown：SKILL.md、README.md、references/**、tests/README.md …（文档之间也会互相引用路径）
const MD_FILES = [
  "SKILL.md", "README.md", "CHANGELOG.md", "tests/README.md",
  ...REFERENCES.map((f) => `references/${f}`),
  ...WORKFLOWS.map((f) => `references/workflows/${f}`),
  ...TEMPLATES.filter((f) => f.endsWith(".md")).map((f) => `assets/templates/${f}`),
].filter((f) => existsSync(join(ROOT, f)));

const refs = new Map();
for (const file of MD_FILES) {
  readLines(file).forEach((line, idx) => {
    const n = idx + 1;
    for (const m of line.matchAll(/`([^`]+)`|\]\(([^)\s#]+)\)/g)) {
      let raw = (m[1] ?? m[2] ?? "").trim().replace(/^[./]+/, "").replace(/[。，；、）)]+$/, "");
      if (!raw) continue;
      // CHANGELOG.md 是历史记录：它必须能写出「templates/ → assets/templates/」这类
      // 迁移说明，提到旧路径是内容本身，不是漂移。这里只豁免 legacy 规则，
      // 该文件里的路径引用仍会在下面按存在性校验。其他文档提到旧前缀一律报错。
      if (LEGACY_PREFIX.test(raw)) {
        if (file === "CHANGELOG.md") continue;
        add("error", "legacy-path", `${file}:${n} 使用了重构前的旧路径 \`${raw}\``);
        continue;
      }
      if (!SKILL_PREFIX.test(raw)) continue;
      if (/[*<>…\s]/.test(raw)) continue;
      raw = raw.replace(/:\d+(-\d+)?$/, "");          // 去掉 `file.md:44` 这类行号后缀
      if (raw.endsWith("/")) continue;                    // 目录引用不逐个校验
      if (!refs.has(raw)) refs.set(raw, []);
      refs.get(raw).push(`${file}:${n}`);
    }
  });
}
for (const [p, lines] of refs) {
  if (existsSync(join(ROOT, p))) continue;
  const base = p.split("/").pop();
  const near = [...known].filter((k) => k.endsWith("/" + base));
  add("error", "path-missing",
    `引用的路径不存在：\`${p}\`` + (lines.length ? `（${lines.join("、")}）` : "") +
    (near.length ? `；可能是：\`${near[0]}\`` : ""));
}

// 索引区块里写到的文件必须真实存在（写了不存在的条目也要报错）
for (const [name, text] of Object.entries(REGIONS)) {
  for (const m of text.matchAll(/(?:assets\/templates|references\/workflows|references)\/[A-Za-z0-9._-]+\.(?:md|xml|cs)/g)) {
    if (!existsSync(join(ROOT, m[0]))) add("error", "index-stale", `${name} 区块引用了不存在的文件：\`${m[0]}\``);
  }
}

// ---------- 4. 索引覆盖率 ----------
function coverage(files, prefix, regionName, regionText, label) {
  for (const f of files) {
    const p = `${prefix}${f}`;
    if (!regionText.includes(p)) add("error", "index-missing", `${label} 未收录：\`${p}\`（应在 ${regionName}）`);
  }
}
coverage(TEMPLATES, "assets/templates/", "对照表区块", REGIONS.TABLE, "模板");
coverage(TEMPLATES, "assets/templates/", "子文件索引-代码模板", REGIONS.TEMPLATES, "模板");
coverage(REFERENCES, "references/", "子文件索引-知识参考", REGIONS.REFERENCES, "参考文档");
coverage(WORKFLOWS, "references/workflows/", "子文件索引-工作流", REGIONS.WORKFLOWS, "工作流");

// ---------- 5. 模板标注 ----------
for (const f of TEMPLATES) {
  if (!/\.(xml|cs)$/.test(f)) continue;
  const head = readFileSync(join(ROOT, "assets/templates", f), "utf8").split(/\r?\n/).slice(0, 16).join("\n");
  if (!head.includes("验证状态：")) add("warn", "marker-status", `assets/templates/${f} 注释头缺少「验证状态：已验证／待核验」`);
  if (!head.includes("AI 辅助生成")) add("warn", "marker-ai", `assets/templates/${f} 注释头缺少「AI 辅助生成」标注`);
}

// ---------- 6. XML 模板良构性 ----------
// 扫描器在 scripts/xml-lint.mjs（独立成模块，便于单测：tests/test-xml-lint.mjs）。
// 技能承诺「有模板 → 直接用（免核验）」，因此模板必须是合法 XML：
// 占位符写成 {{YourXxx}}（不是 <YourXxx>），注释里不得出现 -- 连字符 runs。
for (const f of TEMPLATES) {
  if (!f.endsWith(".xml")) continue;
  const src = readFileSync(join(ROOT, "assets/templates", f), "utf8");
  for (const [line, msg] of xmlProblems(src)) add("error", "xml-invalid", `assets/templates/${f}:${line} ${msg}；元素名里不能写占位符（文本占位符用 {{YourXxx}}；<products> 这类"元素名即 defName"的写法请写具体名，如 <YourProductDefName>）`);
}

// ---------- 输出 ----------
const errors = findings.filter((f) => f.level === "error");
const warns = findings.filter((f) => f.level === "warn");
if (AS_JSON) {
  console.log(JSON.stringify({ ok: errors.length === 0, errors, warnings: warns,
    counts: { templates: TEMPLATES.length, references: REFERENCES.length, workflows: WORKFLOWS.length } }, null, 2));
} else {
  console.log("rimworld-modding 索引校验");
  console.log(`仓库：${ROOT}`);
  console.log(`扫描：${TEMPLATES.length} 模板 / ${REFERENCES.length} 参考 / ${WORKFLOWS.length} 工作流 / ${MD_FILES.length} 份 Markdown / ${refs.size} 处路径引用\n`);
  if (!findings.length) console.log("\u2705 全部通过：路径引用、索引覆盖率、模板标注、XML 良构性均一致。");
  for (const f of errors) console.log(`\u274c [${f.code}] ${f.message}`);
  for (const f of warns) console.log(`\u26a0\ufe0f  [${f.code}] ${f.message}`);
  if (findings.length) console.log(`\n共 ${errors.length} 个错误、${warns.length} 个警告。`);
}
process.exit(errors.length || (STRICT && warns.length) ? 1 : 0);
