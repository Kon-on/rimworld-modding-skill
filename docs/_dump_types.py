
import json, io, sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
# 仓库根 = 本脚本所在目录（docs/）的上一级；换机器、换 clone 都不用改路径
ROOT = Path(__file__).resolve().parents[1]
p = ROOT / "docs" / "def-schema.json"
d = json.load(open(p, encoding='utf-8'))
t = d["defTypes"]
print("types:", len(t))
rows = sorted(t.items(), key=lambda kv: -kv[1]["instances"])
for k, v in rows:
    print("%-34s inst=%-5d paths=%-4d exp=%s" % (k, v["instances"], v["pathCount"], ",".join(x[:3] for x in v["expansions"])))
