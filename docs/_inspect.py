
import json, sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
# 仓库根 = 本脚本所在目录（docs/）的上一级；换机器、换 clone 都不用改路径
ROOT = Path(__file__).resolve().parents[1]
d = json.load(open(ROOT / "docs" / "def-schema.json", encoding='utf-8'))
print("TOP KEYS:", list(d.keys()))
print("meta:", json.dumps({k:v for k,v in d.items() if not isinstance(v,(dict,list))}, ensure_ascii=False)[:600])
dt = d["defTypes"]
print("N types:", len(dt))
td = dt["TraitDef"]
print("TraitDef entry keys:", list(td.keys()))
for k,v in td.items():
    if isinstance(v,(str,int,float,bool)) or v is None:
        print("  ", k, "=", v)
    elif isinstance(v,list):
        print("  ", k, "= list len", len(v), "first:", json.dumps(v[:2], ensure_ascii=False)[:400])
    else:
        print("  ", k, "= dict keys", list(v.keys())[:8])
print()
print("--- sample path entries ---")
for k in list(td.keys()):
    v = td[k]
    if isinstance(v, dict) and v and all(isinstance(x, dict) for x in v.values()):
        items = list(v.items())[:5]
        print("PATHDICT", k)
        for pk, pv in items:
            print("   ", pk, "->", json.dumps(pv, ensure_ascii=False)[:300])
        break
e = json.load(open(ROOT / "docs" / "def-examples.json", encoding='utf-8'))
print()
print("EXAMPLES N:", len(e))
print("TraitDef ex keys:", list(e["TraitDef"].keys()))
print(e["TraitDef"]["smallest"]["file"], "|", e["TraitDef"]["smallest"]["defName"], "| nodes", e["TraitDef"]["smallest"]["nodes"])
print(e["TraitDef"]["smallest"]["xml"][:400])
