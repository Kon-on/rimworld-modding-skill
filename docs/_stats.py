
# -*- coding: utf-8 -*-
import json, sys, os, collections
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
# 仓库根 = 本脚本所在目录（docs/）的上一级；换机器、换 clone 都不用改路径
ROOT = Path(__file__).resolve().parents[1]
P = str(ROOT / "docs")
s = json.load(open(os.path.join(P,"def-schema.json"), encoding="utf-8"))
types = s["defTypes"]
import importlib.util
spec = importlib.util.spec_from_file_location("b", os.path.join(P,"build_tier_b.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
LINE_OF = m.LINE_OF; LINE_NAME = m.LINE_NAME

agg = collections.defaultdict(lambda: {"types":0,"inst":0,"paths":0})
for t, i in types.items():
    a = agg[LINE_OF[t]]
    a["types"] += 1; a["inst"] += i["instances"]; a["paths"] += i["pathCount"]
print("PER LINE")
for k in ["pawn","item","world","ideo","visual","system"]:
    a = agg[k]
    print("  %-6s types=%3d instances=%6d paths=%6d" % (LINE_NAME[k], a["types"], a["inst"], a["paths"]))
tt = sum(a["types"] for a in agg.values()); ti = sum(a["inst"] for a in agg.values()); tp = sum(a["paths"] for a in agg.values())
print("  TOTAL  types=%3d instances=%6d paths=%6d" % (tt, ti, tp))

print("\nTOP 20 BY INSTANCES")
for t, i in sorted(types.items(), key=lambda kv: -kv[1]["instances"])[:20]:
    print("  %-26s %5d inst  %4d paths  %s" % (t, i["instances"], i["pathCount"], LINE_NAME[LINE_OF[t]]))

print("\nEXPANSION PRESENCE (types appearing in each)")
c = collections.Counter()
for t,i in types.items():
    for e in i["expansions"]: c[e]+=1
print("  ", dict(c))
print("\nCORE-ONLY TYPES:", sum(1 for t,i in types.items() if i["expansions"]==["Core"]))
print("MULTI-EXPANSION TYPES:", sum(1 for t,i in types.items() if len(i["expansions"])>1))

print("\nTYPES WITH >=1 REQUIRED FIELD:", sum(1 for t,i in types.items() if any(v["ratio"]>=0.9 for v in i["paths"].values())))
print("LOWEST-INSTANCE TYPES (<=6):")
for t,i in sorted(types.items(), key=lambda kv: kv[1]["instances"])[:12]:
    print("  %-26s %d inst  %d paths" % (t, i["instances"], i["pathCount"]))
