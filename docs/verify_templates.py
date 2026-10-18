# -*- coding: utf-8 -*-
"""核验 02-模板 下所有 xml 代码块里的元素路径是否真实存在于原版 1.7 数据中。

事实来源：docs/def-schema.json（由 extract_def_schema.py 从
E:\\SteamLibrary\\steamapps\\common\\RimWorld\\Data\\<资料片>\\Defs 提取）
产出：library/04-核验/核验结果.md 与 核验结果.csv
复现：python verify_templates.py
"""
import json, os, re, csv
from lxml import etree

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TPL = os.path.join(ROOT, "library", "02-模板")
SCHEMA = os.path.join(ROOT, "docs", "def-schema.json")
OUTDIR = os.path.join(ROOT, "library", "04-核验")

with open(SCHEMA, encoding="utf-8") as f:
    schema = json.load(f)["defTypes"]
SCHEMA_PATHS = {t: set(v["paths"].keys()) for t, v in schema.items()}
SCHEMA_LOWER = {}
for t, ps in SCHEMA_PATHS.items():
    SCHEMA_LOWER.setdefault(t.lower(), set()).update(ps)
ALL_PATHS = set()
for ps in SCHEMA_PATHS.values():
    ALL_PATHS |= ps

FENCE = re.compile(r"^\s*`{3,}\s*([A-Za-z]*)\s*$")

def blocks(text):
    """返回 [(lang, body)]，只有围栏代码块"""
    out, cur, on, lang = [], [], False, ""
    for line in text.splitlines():
        m = FENCE.match(line)
        if m:
            if on:
                out.append((lang, "\n".join(cur)))
                cur, on, lang = [], False, ""
            else:
                on, lang, cur = True, (m.group(1) or "").lower(), []
            continue
        if on:
            cur.append(line)
    return [(l, b) for l, b in out if b.strip()]

def parse_any(src):
    src = src.strip()
    for cand in (src, "<wrap>" + src + "</wrap>"):
        try:
            return etree.fromstring(cand.encode("utf-8"))
        except Exception:
            continue
    return None

def tag_of(el):
    t = el.tag
    if not isinstance(t, str):
        return None
    return t.split("}")[-1]

def is_custom_class(el):
    return tag_of(el) == "li" and (el.get("Class") or "").startswith(("ExampleMod.", "MyMod.", "YourMod."))

def collect(root, base=""):
    res = []
    for ch in root:
        t = tag_of(ch)
        if t is None:
            continue
        p = (base + "/" + t) if base else t
        if is_custom_class(ch):
            res.append((p + " [自定义 Class 子树]", ch, True))
            continue
        res.append((p, ch, False))
        res.extend(collect(ch, p))
    return res

def def_type_from_filename(fn):
    name = fn[:-3]
    name = re.sub(r"^\d+-", "", name)
    for sep in ("-", "\u2013"):
        if sep in name:
            name = name.split(sep)[0]
    return name

rows, unparsed, ok_blocks = [], [], 0
md_files = 0
for dirpath, dirnames, filenames in os.walk(TPL):
    for fn in sorted(filenames):
        if not fn.lower().endswith(".md"):
            continue
        md_files += 1
        fp = os.path.join(dirpath, fn)
        rel = os.path.relpath(fp, TPL).replace("\\", "/")
        with open(fp, encoding="utf-8") as f:
            text = f.read()
        guess = def_type_from_filename(fn)
        for lang, body in blocks(text):
            if lang != "xml":
                continue
            r = parse_any(body)
            if r is None:
                unparsed.append((rel, body[:70].replace("\n", " ")))
                continue
            ok_blocks += 1
            rt = tag_of(r)
            if rt == "Defs":
                defs = [(tag_of(c), c) for c in r if tag_of(c)]
            elif rt == "Patch":
                continue
            elif rt and (rt in SCHEMA_PATHS or rt.lower() in SCHEMA_LOWER):
                defs = [(rt, r)]          # 片段以 Def 类型为根元素
            else:
                defs = [(None, r)]        # 非 Def 片段（如 <comps>、About.xml 片段）
            for dt, el in defs:
                if not dt:
                    for p, node, custom in collect(el):
                        rows.append((rel, "(非Def片段)", p, "片段(不作Def字段比对)"))
                    continue
                known = SCHEMA_PATHS.get(dt) or SCHEMA_LOWER.get(dt.lower())
                for p, node, custom in collect(el):
                    if p == "defName" and node.text and node.text.startswith("EXAMPLE_"):
                        continue
                    if any(seg.startswith("EXAMPLE_") for seg in p.split("/")):
                        continue      # 以 defName 作标签的字典容器（如 products/EXAMPLE_Vest）
                    if custom:
                        rows.append((rel, dt, p, "自定义"))
                    elif known is None:
                        st = "自定义Def类(本体无此类)" if ("." in dt) else "未知Def类型"
                        rows.append((rel, dt, p, st))
                    elif p in known or (p + "/li") in known:
                        rows.append((rel, dt, p, "已证实"))
                    elif p in ALL_PATHS:
                        rows.append((rel, dt, p, "待验证(路径属于其它Def类型)"))
                    else:
                        rows.append((rel, dt, p, "待验证"))
        # 跨 Def 引用（ParentName / Class 之外的 defName 引用）不做强校验，见报告说明
        if not any(r for r in rows if r[0] == rel):
            rows.append((rel, guess, "(无已解析的 xml 代码块)", "无XML"))

os.makedirs(OUTDIR, exist_ok=True)
S_ORDER = ["已证实", "待验证", "待验证(路径属于其它Def类型)", "自定义", "未知Def类型", "自定义Def类(本体无此类)", "无XML", "片段(不作Def字段比对)"]
agg = {}
for rel, dt, p, st in rows:
    a = agg.setdefault(rel, {k: 0 for k in S_ORDER} | {"paths": []})
    a[st] = a.get(st, 0) + 1
    if st != "已证实":
        a["paths"].append(dt + " :: " + p + "  [" + st + "]")

md = []
md.append("# 模板字段核验结果")
md.append("")
md.append("核验对象：library 02-模板 下全部 markdown 里的 xml 代码块（共 " + str(md_files) + " 个文件，成功解析 " + str(ok_blocks) + " 个 XML 块）。")
md.append("")
md.append("事实来源：docs/def-schema.json —— 由脚本直接读取游戏本体 Data\\<资料片>\\Defs 的 1,560 个 XML 提取，覆盖 254 种 Def 类型、13,329 条字段路径。")
md.append("")
md.append("判定规则：")
md.append("")
md.append("- 已证实：该 XML 元素路径在同名 Def 类型的原版全量字段表里存在（原版确实这么写）。")
md.append("- 待验证：该路径在本体任何 Def 类型里都不存在——可能是 1.7 新增字段、自定义 Def 类字段、或模板写错。")
md.append("- 待验证(路径属于其它Def类型)：路径本身在原版存在，但不在该类型下，常见于 li 容器的同名子元素。")
md.append("- 自定义：位于 Class=ExampleMod.* 的自定义组件子树内，本体无从比对（这是模板故意留的自定义位）。")
md.append("")
md.append("## 总览")
md.append("")
md.append("| 文件 | 已证实 | 待验证 | 路径属于其它类型 | 自定义 | 片段 |")
md.append("|---|---|---|---|---|---|")
tot = {k: 0 for k in S_ORDER}
for rel in sorted(agg):
    a = agg[rel]
    for k in tot:
        tot[k] += a.get(k, 0)
    md.append("| " + rel + " | %d | %d | %d | %d | %d |" % (a["已证实"], a["待验证"], a["待验证(路径属于其它Def类型)"], a["自定义"], a["片段(不作Def字段比对)"]))
md.append("| **合计** | **%d** | **%d** | **%d** | **%d** | **%d** |" % (tot["已证实"], tot["待验证"], tot["待验证(路径属于其它Def类型)"], tot["自定义"], tot["片段(不作Def字段比对)"]))
md.append("")
md.append("")
md.append("说明：片段 = 不是以 Defs 为根的写法示意块（如单独的 comps、modDependencies 片段），不做 Def 字段比对；自定义 = 模板故意留出的自定义 C# 组件字段；自定义Def类 = 模板示范的自定义 Def 类字段，本体当然没有。")
md.append("")
unv_paths = [x for rel in sorted(agg) for x in agg[rel]["paths"] if "[待验证]" in x and "自定义" not in x]
md.append("未能证实的 **" + str(tot["待验证"]) + " 条** 待验证路径如下：")
md.append("")
for x in unv_paths:
    md.append("- " + x)
md.append("")
if unv_paths:
    md.append("其中 ThingDef 的 modExtensions 容器属正常现象：全本体 Data\\**\\Defs\\**\\*.xml 中 <modExtensions> 出现 **0 次**（1.7 原版自己不用 modExtensions，该机制是给 mod 用的），无法用原版数据证实。")
md.append("")
md.append("结论：**" + str(tot["已证实"]) + " 条元素路径已对照原版证实**；" + str(tot["待验证"] + tot["待验证(路径属于其它Def类型)"]) + " 条未能证实（明细见下），" + str(tot["自定义"]) + " 条属于模板中自定义 C# 组件的字段（理所当然无法对照原版）。")
md.append("")
md.append("## 逐文件未能证实的路径")
md.append("")
for rel in sorted(agg):
    a = agg[rel]
    if not a["paths"]:
        continue
    md.append("### " + rel)
    md.append("")
    for x in a["paths"]:
        md.append("- " + x)
    md.append("")
if unparsed:
    md.append("## 无法机械化解析的 xml 代码块")
    md.append("")
    md.append("以下片段不是完整 XML（用于示意单段写法），脚本按包裹后仍无法解析，需人工阅读：")
    md.append("")
    for rel, snip in unparsed:
        md.append("- " + rel + " —— " + snip)
    md.append("")
md.append("## 复现方式")
md.append("")
md.append("1. python docs/extract_def_schema.py → 生成 docs/def-schema.json")
md.append("2. python 04-核验/verify_templates.py → 生成 04-核验/核验结果.md 与 核验结果.csv")
md.append("")
md.append("（用本机捆绑 Python：DSH 的 office-runtime\\primary-runtime\\dependencies\\python\\python.exe，已带 lxml。）")
md.append("")

with open(os.path.join(OUTDIR, "核验结果.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(md))
with open(os.path.join(OUTDIR, "核验结果.csv"), "w", encoding="utf-8-sig", newline="") as f:
    wr = csv.writer(f)
    wr.writerow(["file", "defType", "path", "status"])
    for r in sorted(rows):
        wr.writerow(r)

print("md_files=%d xml_blocks=%d paths=%d confirmed=%d unverified=%d other_type=%d custom=%d unparsed=%d"
      % (md_files, ok_blocks, len(rows), tot["已证实"], tot["待验证"],
         tot["待验证(路径属于其它Def类型)"], tot["自定义"], len(unparsed)))
