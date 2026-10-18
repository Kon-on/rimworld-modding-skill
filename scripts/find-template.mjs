#!/usr/bin/env node
// RimWorld 模板检索 —— 在本地 1.7 模板库里找模板、查 Def 类型、查字段路径。
//
// 设计原则：只读、零依赖、**运行时扫描，不生成索引文件**。没有索引文件就没有
// 「索引过期」这件事——这也是这个仓库上一轮最大的教训（手写索引一定会漂移）。
//
// 用法：
//   node scripts/find-template.mjs --list                       列出全部模板
//   node scripts/find-template.mjs 武器                          按关键词找模板/字段
//   node scripts/find-template.mjs --def ThingDef                按 Def 类型找模板 + 必填字段
//   node scripts/find-template.mjs --field verbClass             按字段名查路径与出现率
//   node scripts/find-template.mjs --field verbClass --def ThingDef   限定类型
//   加 --json 输出机器可读结果；加 --lib <路径> 指定模板库。
//
// 库路径解析顺序：--lib → $RIMWORLD_TEMPLATE_LIB → <脚本目录>/assets/rimworld-1.7-templates
//   → <脚本目录或工作目录>/library（也认得改过名/带日期后缀的同结构库目录）
// 退出码：0 有结果；1 查无结果；2 用法错误或找不到模板库。

import { existsSync, readdirSync, readFileSync, statSync } from "node:fs";
import { basename, dirname, join, relative, resolve } from "node:path";
import { fileURLToPath } from "node:url";

export const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const LIB_MARKERS = ["02-模板", "03-全量字段参考"];
const ASSET_NAME = "rimworld-1.7-templates";

const USAGE = [
  "RimWorld 模板检索（本地 1.7 模板库，只读）",
  "",
  "  node scripts/find-template.mjs --list                          列出全部模板（按线分组）",
  "  node scripts/find-template.mjs 武器                             按关键词找模板与字段",
  "  node scripts/find-template.mjs --def ThingDef                   按 Def 类型找模板、字段表、必填字段",
  "  node scripts/find-template.mjs --field verbClass                按字段名查路径、出现率、原版样例",
  "  node scripts/find-template.mjs --field verbClass --def ThingDef  限定 Def 类型",
  "  可选：--json 机器可读输出 ｜ --lib <路径> 指定模板库 ｜ --help",
  "",
  "库路径：--lib → $RIMWORLD_TEMPLATE_LIB → <技能目录>/library → <技能目录>/assets/" + ASSET_NAME,
].join("\n");

// ---------------- 库定位 ----------------
function isLibDir(dir) {
  if (!dir || !existsSync(dir)) return false;
  try {
    return LIB_MARKERS.every((m) => statSync(join(dir, m)).isDirectory());
  } catch {
    return false;
  }
}

function subdirs(dir) {
  try {
    return readdirSync(dir)
      .map((n) => join(dir, n))
      .filter((p) => {
        try { return statSync(p).isDirectory(); } catch { return false; }
      });
  } catch {
    return [];
  }
}

export function locateLibrary(explicit, opts) {
  const o = opts || {};
  const root = o.root || ROOT;
  const cwd = o.cwd || process.cwd();
  const direct = [
    explicit,
    process.env.RIMWORLD_TEMPLATE_LIB,
    join(root, "assets", ASSET_NAME),
    join(root, "library"),
  ].filter(Boolean);
  for (const d of direct) if (isLibDir(d)) return resolve(d);
  const parents = [];
  for (const base of [root, cwd]) parents.push(join(base, "library"), join(base, "成果"), base);
  if (explicit) parents.push(explicit);
  for (const parent of parents) {
    for (const child of subdirs(parent)) if (isLibDir(child)) return resolve(child);
  }
  return null;
}

// ---------------- 读取 ----------------
function walkMd(dir, acc) {
  let entries;
  try { entries = readdirSync(dir, { withFileTypes: true }); } catch { return acc; }
  for (const e of entries) {
    const full = join(dir, e.name);
    if (e.isDirectory()) walkMd(full, acc);
    else if (e.isFile() && /\.md$/i.test(e.name)) acc.push(full);
  }
  return acc;
}

function parseTemplate(lib, lineDir, full) {
  const file = basename(full);
  const stem = file.replace(/\.md$/i, "").replace(/^\d+-/, "");
  const dash = stem.indexOf("-");
  const head = dash === -1 ? stem : stem.slice(0, dash);
  let defType = null;
  let variant = null;
  if (/^[A-Za-z]+Def$/.test(head)) {
    defType = head;
    variant = dash === -1 ? null : stem.slice(dash + 1);
  } else if (/^[A-Za-z]+Def$/.test(stem)) {
    defType = stem;
  }
  const kind = defType ? "XML" : (/csharp/i.test(lineDir) ? "C#" : "其它");
  return {
    line: lineDir,
    group: lineDir.replace(/^\d+-/, ""),
    file,
    path: relative(lib, full).split("\\").join("/"),
    defType,
    variant,
    kind,
    full,
    title: null,
    text: null,
  };
}

function parseIndex(lib) {
  const file = join(lib, "03-全量字段参考", "00-字段索引.md");
  const map = new Map();
  if (!existsSync(file)) return map;
  let group = "";
  for (const line of readFileSync(file, "utf8").split(/\r?\n/)) {
    const h = line.match(/^##\s+([^（(]+)/);
    if (h) { group = h[1].trim(); continue; }
    const cells = line.split("|").map((s) => s.trim());
    if (cells.length < 8) continue;
    if (!/^[A-Za-z_][A-Za-z0-9_]*$/.test(cells[1])) continue;
    if (!/^\d+$/.test(cells[2])) continue;
    map.set(cells[1], {
      defType: cells[1],
      group,
      instances: Number(cells[2]),
      fields: Number(cells[3]),
      required: Number(cells[4]),
      dlc: cells[5],
    });
  }
  return map;
}

function parseCsvLine(line) {
  const out = [];
  let cur = "";
  let quoted = false;
  for (let i = 0; i < line.length; i++) {
    const c = line[i];
    if (quoted) {
      if (c === '"') {
        if (line[i + 1] === '"') { cur += '"'; i++; } else quoted = false;
      } else cur += c;
    } else if (c === '"') quoted = true;
    else if (c === ",") { out.push(cur); cur = ""; }
    else cur += c;
  }
  out.push(cur);
  return out;
}

function readFieldRows(lib) {
  const file = join(lib, "03-全量字段参考", "字段总表.csv");
  if (!existsSync(file)) return [];
  const text = readFileSync(file, "utf8").replace(/^\uFEFF/, "");
  const lines = text.split(/\r?\n/).filter((l) => l.length > 0);
  const head = parseCsvLine(lines[0]);
  const rows = [];
  for (let i = 1; i < lines.length; i++) {
    const cells = parseCsvLine(lines[i]);
    if (cells.length < head.length) continue;
    const row = {};
    head.forEach((k, j) => { row[k.trim()] = cells[j]; });
    row.instances = Number(row.instances);
    row.present = Number(row.present);
    row.ratio = Number(row.ratio);
    rows.push(row);
  }
  return rows;
}

export function loadLibrary(lib) {
  if (!lib) return null;
  const templates = [];
  for (const lineDir of subdirs(join(lib, "02-模板"))) {
    for (const full of walkMd(lineDir, [])) {
      templates.push(parseTemplate(lib, basename(lineDir), full));
    }
  }
  templates.sort((a, b) => a.path.localeCompare(b.path, "zh"));
  const fieldTableDir = join(lib, "03-全量字段参考", "字段");
  const fieldTables = new Set(
    existsSync(fieldTableDir)
      ? readdirSync(fieldTableDir).filter((f) => /\.md$/i.test(f)).map((f) => f.replace(/\.md$/i, ""))
      : []
  );
  return { lib, templates, index: parseIndex(lib), fieldTables, fieldTableDir };
}

function templateText(t) {
  if (t.text === null) {
    try { t.text = readFileSync(t.full, "utf8"); } catch { t.text = ""; }
  }
  return t.text;
}

function excerpt(t, limit) {
  const text = templateText(t);
  const title = text.match(/^#\s+(.+)$/m);
  t.title = title ? title[1].trim() : t.file.replace(/\.md$/i, "");
  const section = text.match(/##\s*用途\s*\n+([\s\S]*?)(\n##|\n*$)/);
  let s = section ? section[1] : text;
  s = s.replace(/^[>\s]+/gm, " ").replace(/[#*|]/g, "").replace(/\s+/g, " ").trim();
  const cap = limit || 150;
  return s.length > cap ? s.slice(0, cap) + "…" : s;
}

const pad = (s, n) => (s.length >= n ? s : s + " ".repeat(n - s.length));
const pct = (r) => (r * 100).toFixed(1) + "%";
const label = (t) => (t.defType ? t.defType + (t.variant ? " · " + t.variant : "") : t.kind);

// ---------------- 查询 ----------------
function matchScore(t, kw) {
  const lower = kw.toLowerCase();
  const text = templateText(t);
  let score = 0;
  if (t.file.toLowerCase().includes(lower)) score += 200;
  if (t.defType && t.defType.toLowerCase().includes(lower)) score += 150;
  const counts = text.toLowerCase().split(lower).length - 1;
  if (counts > 0) score += Math.min(counts, 20) * 4;
  const head = text.split(/\n##\s/)[0] || "";
  if (head.toLowerCase().includes(lower)) score += 40;
  return score;
}

function findDefs(lib, name) {
  const lower = name.toLowerCase();
  const exact = [];
  for (const key of lib.index.keys()) if (key.toLowerCase() === lower) exact.push(key);
  if (exact.length) return { hits: exact, fuzzy: false };
  const prefix = [];
  for (const key of lib.index.keys()) if (key.toLowerCase().startsWith(lower)) prefix.push(key);
  if (prefix.length) return { hits: prefix.sort(), fuzzy: false };
  const contains = [];
  for (const key of lib.index.keys()) if (key.toLowerCase().includes(lower)) contains.push(key);
  if (contains.length) return { hits: contains.sort(), fuzzy: true };
  const tables = [];
  for (const key of lib.fieldTables) if (key.toLowerCase().includes(lower)) tables.push(key);
  return { hits: tables.sort(), fuzzy: true, fromTablesOnly: true };
}

function requiredFields(rows, defType, threshold) {
  const th = threshold === undefined ? 0.9 : threshold;
  return rows
    .filter((r) => r.defType === defType && r.ratio >= th)
    .sort((a, b) => b.ratio - a.ratio || a.path.localeCompare(b.path));
}

// ---------------- 输出 ----------------
function emitList(out, lib) {
  const byLine = new Map();
  for (const t of lib.templates) {
    if (!byLine.has(t.line)) byLine.set(t.line, []);
    byLine.get(t.line).push(t);
  }
  out("模板库：" + lib.lib);
  out("模板 " + lib.templates.length + " 份 ｜ 字段表 " + lib.fieldTables.size + " 张 ｜ Def 类型 " + lib.index.size + " 种");
  for (const line of [...byLine.keys()].sort()) {
    const list = byLine.get(line);
    out("");
    out("[ " + line + " ]  " + list.length + " 份");
    for (const t of list) out("  " + pad(t.path, 48) + label(t));
  }
  out("");
  out("打开：read 工具读上面的路径（相对模板库根目录）；或 node scripts/find-template.mjs --def <DefType>");
}

export function main(argv, opts) {
  const o = opts || {};
  const out = o.out || ((s) => process.stdout.write(s + "\n"));
  const args = (argv || []).slice();
  const keywords = [];
  let wantLib = null;
  let defArg = null;
  let fieldArg = null;
  let doList = false;
  let json = false;

  while (args.length) {
    const a = args.shift();
    if (a === "--list" || a === "-l") doList = true;
    else if (a === "--json") json = true;
    else if (a === "--lib") { wantLib = args.shift(); if (!wantLib) { out("✖ --lib 需要一个路径"); return 2; } }
    else if (a === "--def") { defArg = args.shift(); if (!defArg) { out("✖ --def 需要一个 Def 类型名，例如 --def ThingDef"); return 2; } }
    else if (a === "--field") { fieldArg = args.shift(); if (!fieldArg) { out("✖ --field 需要一个字段名，例如 --field verbClass"); return 2; } }
    else if (a === "--help" || a === "-h") { out(USAGE); return 0; }
    else if (a.startsWith("-")) { out("✖ 未知参数：" + a); out(USAGE); return 2; }
    else keywords.push(a);
  }

  const lib = locateLibrary(wantLib, o);
  if (!lib) {
    out("✖ 找不到 RimWorld 1.7 模板库（需要同时含 " + LIB_MARKERS.join(" / ") + " 的目录）。");
    out("  三种指定方式：--lib <路径> ｜ 环境变量 RIMWORLD_TEMPLATE_LIB=<路径> ｜ 放到 library/ 下");
    return 2;
  }
  const L = loadLibrary(lib);

  if (doList) {
    if (json) out(JSON.stringify({ lib, mode: "list", templates: L.templates.map((t) => ({ path: t.path, line: t.line, defType: t.defType, variant: t.variant, kind: t.kind })) }, null, 2));
    else emitList(out, L);
    return 0;
  }

  if (fieldArg) {
    const rows = readFieldRows(lib);
    const kw = fieldArg.toLowerCase();
    const hits = rows.filter((r) => r.path.toLowerCase().includes(kw) && (!defArg || r.defType.toLowerCase() === defArg.toLowerCase()));
    if (!hits.length) {
      out("✖ 字段表里查不到「" + fieldArg + "」" + (defArg ? "（限定 " + defArg + "）" : "") + "。");
      out("  可能：写法不同（原版路径是 verbs/li/verbClass 这种形式）｜ 属其它版本 ｜ 不是原版机制");
      return 1;
    }
    const groups = new Map();
    for (const r of hits) {
      if (!groups.has(r.defType)) groups.set(r.defType, []);
      groups.get(r.defType).push(r);
    }
    const ordered = [...groups.entries()].sort((a, b) => b[1][0].ratio - a[1][0].ratio || b[1].length - a[1].length);
    if (json) {
      out(JSON.stringify({
        lib, mode: "field", query: fieldArg, defFilter: defArg || null, total: hits.length,
        groups: ordered.map(([defType, list]) => ({
          defType,
          instances: list[0].instances,
          hits: list.map((r) => ({ path: r.path, present: r.present, instances: r.instances, ratio: r.ratio, kind: r.kind, samples: r.samples, sourceFile: r.sourceFile })),
        })),
      }, null, 2));
      return 0;
    }
    out("字段「" + fieldArg + "」命中 " + hits.length + " 条" + (defArg ? "（限定 " + defArg + "）" : "") + "：");
    for (const [defType, list] of ordered.slice(0, 12)) {
      out("");
      out(defType + "（原版 " + list[0].instances + " 个实例，匹配 " + list.length + " 条）");
      const sorted = list.slice().sort((a, b) => b.ratio - a.ratio);
      for (const r of sorted.slice(0, 8)) {
        const zero = r.present === 0 ? "  ⚠ 原版全库 0 次使用（mod 专用或已废弃）" : "";
        out("  " + pad(r.path, 44) + pad(pct(r.ratio) + " (" + r.present + "/" + r.instances + ")", 18) + pad(r.kind, 8) + (r.samples ? String(r.samples).slice(0, 40) : "-") + zero);
        out("  " + " ".repeat(44) + "出处：" + r.sourceFile);
      }
      if (list.length > 8) out("  …另有 " + (list.length - 8) + " 条，省略");
    }
    if (ordered.length > 12) out("");
    if (ordered.length > 12) out("…另有 " + (ordered.length - 12) + " 个 Def 类型命中，用 --def 收窄");
    out("");
    out("出现率 = 该字段在原版同类型实例中的出现比例：≥90% 基本必填 ｜ 40–90% 常见 ｜ <10% 特例");
    out("列表项路径（含 /li）的出现率可超过 100%：那是平均每实例项数（211.4% = 平均每实例 2.1 项），不是比例。");
    return 0;
  }

  if (defArg) {
    const found = findDefs(L, defArg);
    if (!found.hits.length) {
      out("✖ 字段表里没有「" + defArg + "」这个 Def 类型（共 " + L.index.size + " 种）。");
      out("  提示：名字以原版 XML 标签为准（如 ThingDef、PawnKindDef、BackstoryDef）；不确定时用关键词检索。");
      return 1;
    }
    if (found.hits.length > 1 && !found.fuzzy) {
      out("匹配到多个 Def 类型：" + found.hits.join("、"));
      out("（按最接近的 " + found.hits[0] + " 继续，精确名字请照抄原版标签）");
    }
    const name = found.hits[0];
    const meta = L.index.get(name);
    const templates = L.templates.filter((t) => t.defType && t.defType.toLowerCase() === name.toLowerCase());
    const rows = readFieldRows(lib);
    const required = requiredFields(rows, name);
    const total = rows.filter((r) => r.defType === name).length;
    const tablePath = L.fieldTables.has(name) ? "03-全量字段参考/字段/" + name + ".md" : null;

    if (json) {
      out(JSON.stringify({
        lib, mode: "def", defType: name, meta: meta || null, fieldTable: tablePath,
        templates: templates.map((t) => ({ path: t.path, variant: t.variant, defType: t.defType, kind: t.kind, excerpt: excerpt(t, 200) })),
        required: required.map((r) => ({ path: r.path, ratio: r.ratio, present: r.present, instances: r.instances, kind: r.kind, samples: r.samples })),
      }, null, 2));
      return 0;
    }
    out("Def 类型：" + name + (meta ? "（" + meta.group + "）" : ""));
    if (meta) out("原版实例 " + meta.instances + " ｜ 字段路径 " + meta.fields + " ｜ ≥90% 字段 " + meta.required + " ｜ 资料片：" + (meta.dlc || "-"));
    else out("（注：不在索引里，可能是大小写变体；但字段表确有该类型）");
    out("");
    if (templates.length) {
      out("模板（" + templates.length + " 份）：");
      for (const t of templates) {
        out("  " + t.path);
        out("      " + excerpt(t, 140));
      }
    } else {
      out("模板：暂无（这份 Def 类型还没写模板——按 SKILL.md 的三层决策走核验，产出后建议补模板）");
    }
    if (tablePath) {
      out("");
      out("字段表：" + tablePath + "（" + total + " 条路径）");
    }
    out("");
    if (required.length) {
      out("≥90% 字段（视为必填，共 " + required.length + " 条）：");
      for (const r of required.slice(0, 40)) {
        out("  " + pad(r.path, 40) + pad(pct(r.ratio) + " (" + r.present + "/" + r.instances + ")", 18) + pad(r.kind, 8) + (r.samples ? String(r.samples).slice(0, 36) : "-"));
      }
      if (required.length > 40) out("  …另有 " + (required.length - 40) + " 条，见字段表");
    } else {
      out("≥90% 字段：无——该类型字段按需组合，没有统一必填项（照原版同类实例抄更可靠）。");
    }
    out("");
    out("下一步：--field <字段名> 查具体字段 ｜ read 上面的模板 ｜ 核验时对照字段表");
    return 0;
  }

  if (keywords.length) {
    const scored = L.templates
      .map((t) => {
        let best = 0;
        for (const kw of keywords) best = Math.max(best, matchScore(t, kw));
        return { t, score: best };
      })
      .filter((x) => x.score > 0)
      .sort((a, b) => b.score - a.score);
    const rows = readFieldRows(lib);
    const fieldHits = [];
    for (const kw of keywords) {
      for (const r of rows) if (r.path.toLowerCase().includes(kw.toLowerCase())) fieldHits.push(r);
    }
    if (!scored.length && !fieldHits.length) {
      out("✖ 没有匹配「" + keywords.join(" ") + "」的模板或字段。");
      out("  换个中文说法（武器/衣物/动物/基因/事件/天气/研究/心情/特效），或用 --def <DefType> / --field <字段名>。");
      return 1;
    }
    if (json) {
      out(JSON.stringify({
        lib, mode: "keyword", keywords,
        templates: scored.slice(0, 12).map((x) => ({ path: x.t.path, score: x.score, defType: x.t.defType, variant: x.t.variant, kind: x.t.kind, excerpt: excerpt(x.t, 200) })),
        fields: fieldHits.slice(0, 40).map((r) => ({ defType: r.defType, path: r.path, ratio: r.ratio, present: r.present, instances: r.instances, kind: r.kind })),
      }, null, 2));
      return 0;
    }
    out("关键词：" + keywords.join(" ") + " ｜ 模板库：" + lib);
    out("");
    out("模板命中 " + scored.length + " 份（按相关度）：");
    for (const x of scored.slice(0, 8)) {
      out("  " + x.t.path);
      out("      " + label(x.t) + " ｜ " + excerpt(x.t, 150));
    }
    if (scored.length > 8) out("  …另有 " + (scored.length - 8) + " 份，收窄关键词即可");
    if (fieldHits.length) {
      out("");
      out("字段命中 " + fieldHits.length + " 条（英文名匹配）：");
      for (const r of fieldHits.slice(0, 8)) {
        out("  " + pad(r.defType, 18) + pad(r.path, 40) + pct(r.ratio) + " (" + r.present + "/" + r.instances + ")");
      }
    }
    out("");
    out("下一步：--def <DefType> 看必填字段 ｜ --field <字段名> 查路径合法性 ｜ read 上面的路径");
    return 0;
  }

  out(USAGE);
  return 0;
}

const invoked = process.argv[1] && resolve(process.argv[1]) === resolve(fileURLToPath(import.meta.url));
if (invoked) process.exit(main(process.argv.slice(2)));
