
import json, io, sys
sys.stdout.reconfigure(encoding='utf-8')
p = r"<REPO_ROOT>\docs\def-schema.json"
d = json.load(open(p, encoding='utf-8'))
t = d["defTypes"]
print("types:", len(t))
rows = sorted(t.items(), key=lambda kv: -kv[1]["instances"])
for k, v in rows:
    print("%-34s inst=%-5d paths=%-4d exp=%s" % (k, v["instances"], v["pathCount"], ",".join(x[:3] for x in v["expansions"])))
