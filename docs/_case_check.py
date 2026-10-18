
# -*- coding: utf-8 -*-
import json, sys, os
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
# 仓库根 = 本脚本所在目录（docs/）的上一级；换机器、换 clone 都不用改路径
ROOT = Path(__file__).resolve().parents[1]
P = str(ROOT / "docs")
s = json.load(open(os.path.join(P,"def-schema.json"), encoding="utf-8"))["defTypes"]
e = json.load(open(os.path.join(P,"def-examples.json"), encoding="utf-8"))
for pair in [("BackstoryDef","BackStoryDef"), ("JobDef","jobDef")]:
    print("="*70)
    for t in pair:
        if t not in s:
            print(t, "MISSING"); continue
        i = s[t]
        print("%-16s instances=%d paths=%d expansions=%s classes=%s" %
              (t, i["instances"], i["pathCount"], i["expansions"], i["classes"][:3]))
        print("   small.file:", e[t]["smallest"]["file"], "| defName:", e[t]["smallest"]["defName"])
        print("   med.file  :", e[t]["median"]["file"], "| defName:", e[t]["median"]["defName"])
        print("   names[:6] :", i["defNames"][:6])
    a, b = pair
    if a in s and b in s:
        pa, pb = set(s[a]["paths"]), set(s[b]["paths"])
        print("  same path set:", pa == pb, "| only in %s:" % a, len(pa-pb), "| only in %s:" % b, len(pb-pa))
        print("  sampleA:", sorted(pa-pb)[:6])
        print("  sampleB:", sorted(pb-pa)[:6])
