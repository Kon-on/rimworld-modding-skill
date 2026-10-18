
import json, sys
sys.stdout.reconfigure(encoding='utf-8')
d = json.load(open(r"<REPO_ROOT>\docs\def-schema.json", encoding='utf-8'))
names = sorted(d["defTypes"].keys(), key=str.lower)
print(len(names))
for i in range(0, len(names), 4):
    print("  ".join("%-34s" % n for n in names[i:i+4]))
