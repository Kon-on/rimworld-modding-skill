#!/usr/bin/env node
/*
 * test-xml-lint.mjs —— scripts/xml-lint.mjs 的冒烟测试（零依赖）
 *
 * 为什么存在：技能承诺「有模板 → 直接用（免核验）」，因此模板必须是合法 XML。
 * 本项目曾 8 个 XML 模板里 7 个解析失败（尖括号占位符 + 注释里的 --）。
 * 这里用两个历史缺陷当固定样本，保证回归时立刻报错。
 */
import { readFileSync, readdirSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { xmlProblems } from "../scripts/xml-lint.mjs";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..");
let pass = 0, fail = 0;
const check = (name, cond, detail = "") => {
  if (cond) { console.log("✅ " + name); pass++; }
  else { console.log("❌ " + name + (detail ? " — " + detail : "")); fail++; }
};

// 1) 历史缺陷（修复前 assets/templates/weapon-melee.xml 的原貌）
const bad1 = [
  "<Defs>",
  '  <ThingDef ParentName="BaseMeleeWeapon_Sharp_Quality">',
  "    <defName><YourPrefix>_Weapon_<YourName></defName>",
  "  </ThingDef>",
  "</Defs>",
].join("\n");
const p1 = xmlProblems(bad1);
check("尖括号占位符 <YourPrefix> 被判非法", p1.length > 0, JSON.stringify(p1));

// 2) 历史缺陷（修复前 assets/templates/plant.xml 的原貌）
const bad2 = ["<Defs>", "  <!-- 分隔线 ------ 下面是正文 -->", "  <ThingDef><defName>X</defName></ThingDef>", "</Defs>"].join("\n");
check("注释内容含 '--' 被判非法", xmlProblems(bad2).some(([, m]) => m.includes("'--'")), JSON.stringify(xmlProblems(bad2)));
const bad3 = "<Defs><!--文字---></Defs>";
check("注释以 '-' 结尾被判非法", xmlProblems(bad3).some(([, m]) => m.includes("结尾")), JSON.stringify(xmlProblems(bad3)));

// 3) 修复后的正确写法必须良构
const good = [
  '<?xml version="1.0" encoding="utf-8"?>',
  "<Defs>",
  "  <!-- == 注释 == -->",
  '  <ThingDef ParentName="BaseMeleeWeapon_Sharp_Quality">',
  "    <defName>{{YourPrefix}}_Weapon_{{YourName}}</defName>",
  "    <selfClosing />",
  "  </ThingDef>",
  "</Defs>",
  "",
].join("\n");
check("{{YourXxx}} 占位符写法良构", xmlProblems(good).length === 0, JSON.stringify(xmlProblems(good)));

// 4) 标签不配对必须被发现
check("标签不配对被发现", xmlProblems("<Defs><A></B></Defs>").length > 0);

// 5) 仓库现有 XML 模板全部良构（这是这条测试真正要守住的不变量）
const dir = join(ROOT, "assets/templates");
const xmls = readdirSync(dir).filter((f) => f.endsWith(".xml")).sort();
for (const f of xmls) {
  const probs = xmlProblems(readFileSync(join(dir, f), "utf8"));
  check("assets/templates/" + f + " 良构", probs.length === 0, JSON.stringify(probs));
}

console.log("\n" + pass + "/" + (pass + fail) + " 通过（XML 模板 " + xmls.length + " 个）");
process.exit(fail ? 1 : 0);
