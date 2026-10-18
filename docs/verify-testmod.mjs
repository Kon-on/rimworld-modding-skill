#!/usr/bin/env node
// 环世界完整测试 mod —— 静态核验器
// 用法：node docs/verify-testmod.mjs [--mod <目录>] [--json]
// 核验项：XML 良构 / defName 唯一与前缀 / ParentName 与 defName 引用可解析 / texPath 文件存在 /
//         字段路径对照 1.7 字段总表 / techLevel 等枚举合法性 / Patch 结构与 xpath 语法 / C# 类型在 DLL 里真实存在
import fs from "node:fs";
import path from "node:path";

const args = process.argv.slice(2);
const argOf = (k, d) => { const i = args.indexOf(k); return i >= 0 ? args[i + 1] : d; };
const MOD = argOf("--mod", "<REPO_ROOT>\\examples\\rimtest-mod\\RimTestMod");
const RIMWORLD = argOf("--rimworld", "E:\\SteamLibrary\\steamapps\\common\\RimWorld");
const LIBRARY = argOf("--library", "<REPO_ROOT>\\library");
const JSON_OUT = argOf("--out", path.join(MOD, "..", "核验报告.json"));

const problems = [];
const notes = [];
const P = (level, check, message) => problems.push({ level, check, message });

// ---------- 极简 XML 解析器（够用且能报错） ----------
function parseXml(src, file) {
  const root = { tag: "#root", attrs: {}, children: [], text: "" };
  const stack = [root];
  let i = 0;
  const err = (m) => { throw new Error(file + ": " + m + " @" + i); };
  while (i < src.length) {
    const lt = src.indexOf("<", i);
    if (lt < 0) { stack[stack.length - 1].text += src.slice(i); break; }
    stack[stack.length - 1].text += src.slice(i, lt);
    if (src.startsWith("<!--", lt)) { const e = src.indexOf("-->", lt); if (e < 0) err("注释未闭合"); i = e + 3; continue; }
    if (src.startsWith("<![CDATA[", lt)) { const e = src.indexOf("]]>", lt); if (e < 0) err("CDATA 未闭合"); stack[stack.length - 1].text += src.slice(lt + 9, e); i = e + 3; continue; }
    if (src.startsWith("<?", lt)) { const e = src.indexOf("?>", lt); if (e < 0) err("处理指令未闭合"); i = e + 2; continue; }
    if (src.startsWith("<!", lt)) { const e = src.indexOf(">", lt); i = e + 1; continue; }
    const gt = src.indexOf(">", lt);
    if (gt < 0) err("标签未闭合");
    let body = src.slice(lt + 1, gt);
    const selfClose = body.endsWith("/");
    if (selfClose) body = body.slice(0, -1);
    const isClose = body.startsWith("/");
    if (isClose) body = body.slice(1);
    const m = /^([A-Za-z_][\w.:-]*)\s*([\s\S]*)$/.exec(body);
    if (!m) err("非法标签名: " + body);
    const tag = m[1], rest = m[2];
    const attrs = {};
    const re = /([A-Za-z_][\w.:-]*)\s*=\s*"([^"]*)"/g; let a;
    while ((a = re.exec(rest))) attrs[a[1]] = a[2];
    if (isClose) {
      const top = stack.pop();
      if (!top || top.tag !== tag) err("标签不匹配：</" + tag + "> 对上了 <" + (top && top.tag) + ">");
      i = gt + 1; continue;
    }
    const node = { tag, attrs, children: [], text: "" };
    stack[stack.length - 1].children.push(node);
    if (!selfClose) stack.push(node);
    i = gt + 1;
  }
  if (stack.length !== 1) throw new Error(file + ": 有未闭合标签 <" + stack[stack.length - 1].tag + ">");
  return root;
}

function walk(dir, out = []) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) walk(p, out); else out.push(p);
  }
  return out;
}
const rel = (p, base) => path.relative(base, p).replace(/\\/g, "/");

// ---------- 1. 读 mod 的全部 XML ----------
const allFiles = fs.existsSync(MOD) ? walk(MOD) : [];
const xmlFiles = allFiles.filter(f => f.toLowerCase().endsWith(".xml") && !/_SPEC\.md$/i.test(f));
const trees = new Map();
for (const f of xmlFiles) {
  const src = fs.readFileSync(f, "utf8");
  try { trees.set(f, parseXml(src, rel(f, MOD))); }
  catch (e) { P("error", "xml-wellformed", e.message); }
}
console.log("[1] XML 良构：" + xmlFiles.length + " 个文件解析，" + problems.filter(p => p.check === "xml-wellformed").length + " 个失败");

// ---------- 2. 收集 Defs ----------
const defs = [];
for (const [file, tree] of trees) {
  if (!/[\\/]Defs[\\/]/i.test(file)) continue;
  for (const node of tree.children) for (const def of node.children) {
    if (def.tag === "#root" || !def.tag.endsWith("Def")) continue;
    const dn = def.children.find(c => c.tag === "defName");
    defs.push({ file: rel(file, MOD), type: def.tag, name: dn ? dn.text.trim() : null, node: def });
  }
}
const nameSeen = new Map();
for (const d of defs) {
  if (!d.name) { P("warn", "defName-missing", d.file + " 里有一个 " + d.type + " 没有 defName（应确认是否为 Abstract 模板）"); continue; }
  if (nameSeen.has(d.name)) P("error", "defName-unique", "defName 重复：" + d.name + "（" + nameSeen.get(d.name) + " 与 " + d.file + "）");
  nameSeen.set(d.name, d.file);
  if (!d.name.startsWith("DM_")) P("error", "defName-prefix", d.name + " 未使用约定前缀 DM_");
}
console.log("[2] Def 数量：" + defs.length + "（defName 唯一性、DM_ 前缀已查）");

// ---------- 3. 原版 defName / Name 索引 ----------
const vanillaNames = new Set();
const vanillaFiles = [];
for (const dlc of fs.readdirSync(path.join(RIMWORLD, "Data"))) {
  const dir = path.join(RIMWORLD, "Data", dlc, "Defs");
  if (!fs.existsSync(dir)) continue;
  for (const f of walk(dir)) if (f.toLowerCase().endsWith(".xml")) vanillaFiles.push(f);
}
for (const f of vanillaFiles) {
  const src = fs.readFileSync(f, "utf8");
  for (const m of src.matchAll(/<(?:defName|Name)>([^<]+)<\/(?:defName|Name)>/g)) vanillaNames.add(m[1].trim());
  for (const m of src.matchAll(/\sName="([^"]+)"/g)) vanillaNames.add(m[1].trim());
}
for (const f of xmlFiles) { const s = fs.readFileSync(f, "utf8"); for (const m of s.matchAll(/\sName="([^"]+)"/g)) nameSeen.set(m[1].trim(), rel(f, MOD)); }
console.log("[3] 原版索引：" + vanillaFiles.length + " 个 XML，" + vanillaNames.size + " 个 defName/Name");

for (const d of defs) {
  const pn = d.node.attrs["ParentName"];
  if (pn && !vanillaNames.has(pn) && !nameSeen.has(pn)) P("error", "parent-exists", d.name + " 的 ParentName=\"" + pn + "\" 在原版 1.7 与本 mod 里都找不到");
}
// 被引用为「某个 defName 值」的字段（挑选会真实影响加载的那些）
const REF_FIELDS = new Set(["thingDefs", "thingDef", "harvestedThingDef", "recipeUsers", "stuff", "minifiedDef", "recipe", "researchPrerequisite"]);
const CS_FIELDS = new Set(["graphicClass", "verbClass", "thingClass", "workerClass", "compClass"]);
// 游戏程序集里的类型名索引（用于核验 XML 里写的 C# 类是否真实存在）
const dllIndex = (() => {
  let s = "";
  for (const n of ["Assembly-CSharp.dll", "RimWorld.dll"]) {
    const p = path.join(RIMWORLD, n);
    if (fs.existsSync(p)) s += fs.readFileSync(p).toString("latin1");
  }
  return s;
})();
for (const d of defs) {
  const stack = [d.node];
  while (stack.length) {
    const n = stack.pop();
    for (const c of n.children) {
      if (REF_FIELDS.has(c.tag)) {
        const v = c.text.trim();
        if (v && !v.includes(".") && !nameSeen.has(v) && !vanillaNames.has(v)) {
          P("warn", "def-ref", d.name + " 的 <" + c.tag + "> 引用了 " + v + "，原版与本 mod 都查不到");
        }
      }
      if (CS_FIELDS.has(c.tag)) {
        const v = c.text.trim();
        const short = v.split(".").pop();
        if (v && !dllIndex.includes(short)) {
          P("warn", "csharp-class", d.name + " 的 <" + c.tag + "> 指向 C# 类 " + v + "，在 Assembly-CSharp.dll / RimWorld.dll 的类名索引里找不到（若是 mod 自带类可忽略）");
        }
      }
      stack.push(c);
    }
  }
}

// ---------- 4. texPath 与贴图文件 ----------
const TEX_KEYS = new Set(["texPath", "immatureGraphicPath"]);
const texChecks = [];
for (const [file, tree] of trees) {
  const stack = [tree];
  while (stack.length) {
    const n = stack.pop();
    for (const c of n.children) {
      if (TEX_KEYS.has(c.tag)) {
        const v = c.text.trim();
        const p = path.join(MOD, "Textures", v + ".png");
        texChecks.push({ file: rel(file, MOD), texPath: v, ok: fs.existsSync(p), looked: rel(p, MOD) });
      }
      if (c.tag === "wornGraphicPath") {
        const v = c.text.trim();
        const dir = path.join(MOD, "Textures", v);
        const dirs = path.dirname(dir);
        const base = path.basename(dir);
        const need = ["north", "south", "east", "west"].map(d => path.join(dirs, base + "_" + d + ".png"));
        texChecks.push({ file: rel(file, MOD), texPath: v + " (_north/_south/_east/_west)", ok: need.every(x => fs.existsSync(x)), looked: rel(dirs, MOD) });
      }
      stack.push(c);
    }
  }
}
for (const t of texChecks) if (!t.ok) P("error", "texPath", t.file + " 的 texPath「" + t.texPath + "」找不到文件：" + t.looked);
console.log("[4] texPath 引用：" + texChecks.length + " 处，缺失 " + texChecks.filter(t => !t.ok).length + " 处");

// ---------- 5. 字段路径对照 1.7 字段总表 ----------
const csv = fs.readFileSync(path.join(LIBRARY, "03-全量字段参考", "字段总表.csv"), "utf8").split(/\r?\n/);
const fieldPaths = new Map();   // DefType -> Set(path)
const fieldRate = new Map();    // DefType|path -> 出现率
for (const line of csv) {
  if (!line || line.startsWith("线,")) continue;
  const c = line.split(",");
  if (c.length < 7) continue;
  const [, defType, p, , , rate] = c;
  if (!fieldPaths.has(defType)) fieldPaths.set(defType, new Set());
  fieldPaths.get(defType).add(p);
  fieldRate.set(defType + "|" + p, parseFloat(rate));
}
const unknownFields = [];
let fieldChecks = 0;
for (const d of defs) {
  const known = fieldPaths.get(d.type);
  if (!known) { P("warn", "field-table-missing", "字段表里没有 " + d.type + " 这个 Def 类型（无法核验字段）"); continue; }
  const walkNode = (node, prefix) => {
    for (const c of node.children) {
      const p = prefix ? prefix + "/" + c.tag : c.tag;
      if (c.tag === "defName" || c.tag === "ParentName" || c.tag === "Name" || c.tag === "Abstract" || c.tag === "Class" ||
          c.tag === "label" || c.tag === "description" || c.tag === "li" || c.tag === "value" || c.tag === "xpath" || c.tag === "success" || c.tag === "nomatch") {
        walkNode(c, p); continue;
      }
      fieldChecks++;
      if (!known.has(p)) unknownFields.push({ def: d.name, type: d.type, field: p, rate: fieldRate.get(d.type + "|" + p) });
      walkNode(c, p);
    }
  };
  walkNode(d.node, "");
}
if (unknownFields.length) {
  for (const u of unknownFields.slice(0, 60)) P("warn", "field-unknown", u.def + "（" + u.type + "）的字段路径 " + u.field + " 在 1.7 字段表里查不到");
}
console.log("[5] 字段路径核验：" + fieldChecks + " 处，字段表未收录 " + unknownFields.length + " 处");

// ---------- 6. 枚举合法性 ----------
const ENUMS = {
  techLevel: ["Neolithic", "Medieval", "Industrial", "Spacer", "Ultra", "Animal", "Anomaly"],
  "plant/purpose": ["Food", "Beauty", "Health"],
};
for (const d of defs) {
  const stack = [d.node];
  while (stack.length) {
    const n = stack.pop();
    for (const c of n.children) {
      if (c.tag === "techLevel") {
        const v = c.text.trim();
        if (!ENUMS.techLevel.includes(v)) P("error", "enum", d.name + " 的 techLevel=\"" + v + "\" 不是 1.7 合法值（合法：" + ENUMS.techLevel.join("/") + "）");
      }
      if (c.tag === "purpose") {
        const v = c.text.trim();
        if (!ENUMS["plant/purpose"].includes(v)) P("warn", "enum", d.name + " 的 plant/purpose=\"" + v + "\" 未在 1.7 实测值（" + ENUMS["plant/purpose"].join("/") + "）中出现");
      }
      stack.push(c);
    }
  }
}

// ---------- 7. Patches 结构与 xpath 语法 ----------
const patchFiles = xmlFiles.filter(f => /[\\/]Patches[\\/]/i.test(f));
const KNOWN_OPS = ["PatchOperationAdd", "PatchOperationReplace", "PatchOperationInsert", "PatchOperationRemove", "PatchOperationSequence", "PatchOperationTest", "PatchOperationFindMod", "PatchOperationConditional", "PatchOperationAttributeSet", "PatchOperationAttributeAdd", "PatchOperationAddModExtension"];
let opsSeen = new Set();
for (const f of patchFiles) {
  const tree = trees.get(f); if (!tree) continue;
  const stack = [tree];
  while (stack.length) {
    const n = stack.pop();
    for (const c of n.children) {
      if (c.tag === "Operation") {
        const cls = String(c.attrs["Class"] || "").trim();
        opsSeen.add(cls);
        if (!KNOWN_OPS.includes(cls)) P("warn", "patch-op", rel(f, MOD) + " 的 Operation Class=\"" + cls + "\" 不在已知 PatchOperation 列表中");
      }
      if (c.tag === "xpath") {
        const xp = c.text.trim();
        const bad = [/^\/?Defs\b.*=>/.test(xp), !xp.startsWith("/")];
        if (!xp.startsWith("/")) P("error", "xpath", rel(f, MOD) + " 的 xpath 不以 / 开头：" + xp);
        const brackets = (xp.match(/\[/g) || []).length - (xp.match(/\]/g) || []).length;
        if (brackets !== 0) P("error", "xpath", rel(f, MOD) + " 的 xpath 方括号不配对：" + xp);
      }
      stack.push(c);
    }
  }
}
console.log("[7] Patch 文件：" + patchFiles.length + " 个，用到的 Operation：" + [...opsSeen].join(", "));

// ---------- 8. C# 程序集与 XML 里引用的类型 ----------
const asmDir = path.join(MOD, "Assemblies");
const asms = fs.existsSync(asmDir) ? fs.readdirSync(asmDir).filter(f => f.endsWith(".dll")) : [];
const asmText = asms.map(f => fs.readFileSync(path.join(asmDir, f)).toString("latin1")).join("\n");
const classRefs = [];
for (const [file, tree] of trees) {
  const stack = [tree];
  while (stack.length) {
    const n = stack.pop();
    for (const c of n.children) {
      if (c.tag === "li" && c.attrs["Class"]) classRefs.push({ file: rel(file, MOD), cls: c.attrs["Class"] });
      if (c.tag === "compClass") classRefs.push({ file: rel(file, MOD), cls: c.text.trim() });
      stack.push(c);
    }
  }
}
for (const r of classRefs) {
  const short = r.cls.split(".").pop();
  if (!r.cls.startsWith("Demo.RimTestMod")) { continue; }
  const found = asmText.includes(short);
  if (!found) P("error", "csharp-type", r.file + " 引用了 C# 类型 " + r.cls + "，但在 Assemblies 里的 DLL 中找不到该类型名");
  else notes.push("C# 类型核对通过：" + r.cls + " 存在于 " + asms.join("/"));
}
console.log("[8] DLL：" + (asms.length ? asms.join(", ") : "（尚无）") + "；XML 引用的自定义类型 " + classRefs.filter(r => r.cls.startsWith("Demo.")).length + " 处");

// ---------- 汇总 ----------
const errs = problems.filter(p => p.level === "error");
const warns = problems.filter(p => p.level === "warn");
const report = {
  mod: MOD, generatedAt: new Date().toISOString(),
  counts: { xmlFiles: xmlFiles.length, defs: defs.length, vanillaXml: vanillaFiles.length, vanillaNames: vanillaNames.size, texRefs: texChecks.length, fieldChecks, assemblies: asms },
  errors: errs, warnings: warns, notes,
};
fs.writeFileSync(JSON_OUT, JSON.stringify(report, null, 2), "utf8");
console.log("\n=== 结果 ===");
console.log("错误 " + errs.length + " 项，警告 " + warns.length + " 项");
for (const p of errs.slice(0, 40)) console.log("  [错误/" + p.check + "] " + p.message);
for (const p of warns.slice(0, 25)) console.log("  [警告/" + p.check + "] " + p.message);
console.log("\n报告已写入 " + JSON_OUT);
process.exit(errs.length ? 1 : 0);
