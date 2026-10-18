
# -*- coding: utf-8 -*-
"""Extract the complete Def schema of RimWorld 1.7 from the shipped XML.
Deterministic + reproducible: re-run to regenerate the same JSON.
"""
import os, json, sys
from pathlib import Path
from lxml import etree
from collections import defaultdict

# 仓库根 = 本脚本所在目录（docs/）的上一级；换机器、换 clone 都不用改路径
ROOT = Path(__file__).resolve().parents[1]
GAME = r"E:\SteamLibrary\steamapps\common\RimWorld"
DATA = os.path.join(GAME, "Data")
OUT  = str(ROOT / "docs")

MAX_SAMPLES = 4
MAX_DEFNAMES = 40

def kind_of(text):
    t = (text or "").strip()
    if t == "": return "empty"
    if t in ("True", "False", "true", "false"): return "bool"
    try:
        float(t); return "number"
    except Exception:
        return "text"

schemas = {}
errors = []
file_count = 0

files = []
for root, dirs, fnames in os.walk(DATA):
    parts = root[len(DATA)+1:].split(os.sep) if len(root) > len(DATA) else []
    if len(parts) >= 2 and parts[1] == "Defs":
        for fn in fnames:
            if fn.lower().endswith(".xml"):
                files.append(os.path.join(root, fn))

for path in sorted(files):
    rel = path[len(DATA)+1:]
    exp = rel.split(os.sep)[0]
    try:
        tree = etree.parse(path)
    except Exception as e:
        errors.append({"file": rel, "error": str(e)[:200]})
        continue
    root_el = tree.getroot()
    if root_el is None or root_el.tag != "Defs":
        continue
    file_count += 1
    for defnode in root_el:
        dtype = defnode.tag
        if not isinstance(dtype, str):
            continue
        sch = schemas.get(dtype)
        if sch is None:
            sch = schemas[dtype] = {
                "instances": 0, "expansions": set(), "defNames": [],
                "paths": defaultdict(lambda: {"n": 0, "kinds": set(), "samples": set(), "attrs": set()}),
                "classes": set(),
            }
        sch["instances"] += 1
        sch["expansions"].add(exp)

        defname = None
        dn = defnode.find("defName")
        if dn is not None and dn.text:
            defname = dn.text.strip()
        if defname and len(sch["defNames"]) < MAX_DEFNAMES:
            sch["defNames"].append(defname)

        if "Class" in defnode.attrib:
            sch["classes"].add(defnode.attrib["Class"])

        stack = [(defnode, "")]
        while stack:
            node, prefix = stack.pop()
            for child in node:
                tag = child.tag
                if not isinstance(tag, str):
                    continue
                p = (prefix + "/" + tag) if prefix else tag
                rec = sch["paths"][p]
                rec["n"] += 1
                if child.attrib:
                    for a in child.attrib:
                        if len(rec["attrs"]) < 8:
                            rec["attrs"].add(a)
                if len(child) == 0:
                    txt = (child.text or "").strip()
                    if len(rec["kinds"]) < 3:
                        rec["kinds"].add(kind_of(txt))
                    if txt and len(rec["samples"]) < MAX_SAMPLES:
                        rec["samples"].add(txt[:80])
                else:
                    stack.append((child, p))

out = {}
for dtype, sch in schemas.items():
    inst = sch["instances"]
    paths = {}
    for p, rec in sch["paths"].items():
        paths[p] = {
            "n": rec["n"],
            "ratio": round(rec["n"] / inst, 4),
            "kind": sorted(rec["kinds"]),
            "samples": sorted(rec["samples"]),
            "attrs": sorted(rec["attrs"]),
        }
    out[dtype] = {
        "instances": inst,
        "expansions": sorted(sch["expansions"]),
        "defNames": sch["defNames"],
        "classes": sorted(sch["classes"]),
        "pathCount": len(paths),
        "paths": dict(sorted(paths.items())),
    }

os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "def-schema.json"), "w", encoding="utf-8") as f:
    json.dump({"game": GAME, "defFilesParsed": file_count, "defTypes": out}, f,
              ensure_ascii=False, separators=(",", ":"))

with open(os.path.join(OUT, "def-types-index.csv"), "w", encoding="utf-8-sig", newline="") as f:
    f.write("defType,instances,pathCount,expansions,fieldCount_required,sampleDefNames\n")
    for dtype, d in sorted(out.items(), key=lambda kv: -kv[1]["instances"]):
        req = sum(1 for p, r in d["paths"].items() if r["ratio"] >= 0.9)
        f.write("%s,%d,%d,\"%s\",%d,\"%s\"\n" % (
            dtype, d["instances"], d["pathCount"], "|".join(d["expansions"]), req,
            "|".join(d["defNames"][:6])))

print(json.dumps({
    "defFilesParsed": file_count,
    "defTypes": len(out),
    "parseErrors": len(errors),
    "jsonBytes": os.path.getsize(os.path.join(OUT, "def-schema.json")),
    "errors": errors[:5],
}, ensure_ascii=False, indent=1))
