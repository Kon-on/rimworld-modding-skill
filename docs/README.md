# docs/ —— 构建与核验证据

这个目录不是技能的教学内容，而是**本仓库结论的原材料与复算入口**：技能里每一句「1.7 实测」都应当能在这里找到对应的数据或脚本。技能运行时不需要它（只有 `library/` 是运行时依赖）。

原来的目录名是 `过程/`，与 `library/`（原 `成果/RimWorld-1.7-代码模板集`）、`examples/`（原 `成果/环世界-完整测试mod`）一起在 2026-10-18 的上传整理中改成英文名。

## 里面有什么

| 路径 | 内容 |
|------|------|
| `def-schema.json`（1.6 MB） | 从本机 RimWorld 1.7.4981 rev136 的 `Data/**` 提取的 Def 字段模式；`library/03-全量字段参考/` 里每张字段表的「数据来源」就是它 |
| `def-examples.json`（593 KB） | 同来源的字段取值样例 |
| `def-types-index.csv` / `def-instances-index.csv` | Def 类型与原版实例索引（覆盖率统计用） |
| `csharp-api.json`（1.0 MB） | 反射 `Assembly-CSharp.dll` 得到的公开类型/成员快照 |
| `extract_def_schema.py` / `extract_def_examples.py` | 生成上面两份 JSON 的提取脚本（需要本机装有游戏） |
| `verify_templates.py` / `build_tier_b.py` | 模板库的构建与核验脚本 |
| `verify-testmod.mjs` | 完整测试 mod 的静态核验器（8 类检查），默认核 `examples/rimtest-mod/RimTestMod`，报告写到 `examples/rimtest-mod/核验报告.json` |
| `unitystubs-stubs.txt` / `unitystubs-stub-signatures.txt` | UnityStubs 兼容层的类型与签名快照（1.7 用 Waylith 替换 Unity 后挖出来的） |
| `_*.ps1` / `_*.py` / `_*.out.txt` | 一次性探针脚本与原始输出（API 差异、成员搜索、贴图总览等），保留下的是证据不是工具 |
| `差异-16到17.md` / `验证-csharp-1.7.md` / `样本-17版mod结构.md` / `_TESTING.draft.md` | 梳理阶段的中间分析稿；结论已并入 `references/` 与 `library/` |

> **已移除**：原 `rimtest-mod/` 是与 `examples/rimtest-mod/RimTestMod/` 逐文件重复的工作副本（44 个文件全同），2026-10-18 结构整理时移出仓库；其中唯一没有对应产物的一份 `_SPEC.md` 规格书移到 `examples/rimtest-mod/_SPEC.md`。

## 复算入口

```bash
# 核验完整测试 mod（8 类静态检查；退出码 0 = 无 error）
node docs/verify-testmod.mjs

# 核验模板库（需要本机装有 RimWorld 1.7）
python docs/verify_templates.py
```

> 这些脚本都用**脚本自身位置**推导仓库根（Python `Path(__file__).resolve().parents[1]`、PowerShell `Split-Path -Parent $PSScriptRoot`、Node `import.meta.url`），在任意工作目录下执行都可以，换机器、换 clone 都不用改路径。原版游戏目录也不写死：先看环境变量 `RIMWORLD_DIR`，再看 Steam 注册表与库清单（`libraryfolders.vdf`）自动探测，也可以用 `--rimworld <游戏安装目录>` 显式指定。
>
> 文档与脚本统一用占位符表示机器相关路径：`<游戏安装目录>` = 含 `Assembly-CSharp.dll` 的 RimWorld 根目录；`<创意工坊目录>` = `<Steam 库>\steamapps\workshop\content\294100`；`<Steam 库>` = Steam 库根目录。 仓库自身路径用仓库相对写法（如 `docs/def-schema.json`）。

## 不在这里的东西

- 原始游戏文件：本目录只存**提取结果**，不含任何原版 `Data/` 内容或游戏 DLL。
- 编译中间产物（`obj/` `bin/` `__pycache__/`）：已移入回收站，`.gitignore` 也挡住了它们。
