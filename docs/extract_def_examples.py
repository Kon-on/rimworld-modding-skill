
# -*- coding: utf-8 -*-
"""Extract, for every Def type in RimWorld 1.7, the smallest and the median-size
real vanilla instance (as literal XML) plus an instance index."""
import os, json
from pathlib import Path
from lxml import etree

# 仓库根 = 本脚本所在目录（docs/）的上一级；换机器、换 clone 都不用改路径
ROOT = Path(__file__).resolve().parents[1]
GAME = r"E:\SteamLibrary\steamapps\common\RimWorld"
DATA = os.path.join(GAME, "Data")
OUT  = str(ROOT / "docs")

def nodecount(el):
    return sum(1 for _ in el.iter())

files = []
for root, dirs, fnames in os.walk(DATA):
    parts = root[len(DATA)+1:].split(os.sep) if len(root) > len(DATA) else []
    if len(parts) >= 2 and parts[1] == "Defs":
        for fn in fnames:
            if fn.lower().endswith(".xml"):
                files.append(os.path.join(root, fn))

inst = {}   # defType -> list of dicts
for path in sorted(files):
    rel = path[len(DATA)+1:]
    try:
        tree = etree.parse(path)
    except Exception:
        continue
    root_el = tree.getroot()
    if root_el is None or root_el.tag != "Defs":
        continue
    for dn in root_el:
        t = dn.tag
        if not isinstance(t, str):
            continue
        name = dn.findtext("defName") or ""
        inst.setdefault(t, []).append({
            "defName": name,
            "file": rel.replace(os.sep, "/"),
            "nodes": nodecount(dn),
            "xml": etree.tostring(dn, pretty_print=True, encoding="unicode"),
        })

out = {}
index = []
for t, lst in inst.items():
    lst.sort(key=lambda x: x["nodes"])
    n = len(lst)
    smallest = lst[0]
    median = lst[n // 2]
    out[t] = {
        "instances": n,
        "smallest": smallest,
        "median": median,
        "allDefNames": [x["defName"] for x in lst],
    }
    for x in lst[:25]:
        index.append((t, x["defName"], x["nodes"], x["file"]))

os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "def-examples.json"), "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, separators=(",", ":"))

with open(os.path.join(OUT, "def-instances-index.csv"), "w", encoding="utf-8-sig", newline="") as f:
    f.write("defType,defName,nodes,file\n")
    for t, name, n, fl in index:
        f.write('%s,"%s",%d,%s\n' % (t, name, n, fl))

print(json.dumps({
    "defTypes": len(out),
    "totalInstances": sum(v["instances"] for v in out.values()),
    "examplesBytes": os.path.getsize(os.path.join(OUT, "def-examples.json")),
    "indexRows": len(index),
}, ensure_ascii=False))
