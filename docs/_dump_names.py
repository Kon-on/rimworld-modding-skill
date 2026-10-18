
import json, sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
# 仓库根 = 本脚本所在目录（docs/）的上一级；换机器、换 clone 都不用改路径
ROOT = Path(__file__).resolve().parents[1]
d = json.load(open(ROOT / "docs" / "def-schema.json", encoding='utf-8'))
names = sorted(d["defTypes"].keys(), key=str.lower)
print(len(names))
for i in range(0, len(names), 4):
    print("  ".join("%-34s" % n for n in names[i:i+4]))
