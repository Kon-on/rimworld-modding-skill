# 工作流：排查崩溃/报错

> 适用：mod 加载时报错、游戏中出现红字/白窗、游戏崩溃

## 快速决策树

```
游戏/Mod 出现问题
│
├─ 游戏加载时卡住/白窗？
│   ├─ 关闭所有 mod，只开你的 → 正常？ → mod 冲突，二分法排查
│   └─ 只开你的也卡住 → XML 语法错误 → 用 XML 验证器检查
│
├─ 弹出红字错误？
│   ├─ "Could not resolve cross-reference" → 检查 defName 引用
│   ├─ "Could not find type" → 检查 Class= 属性 / DLL 是否正确加载
│   ├─ "Duplicate defName" → 改前缀，确保全局唯一
│   └─ NullReferenceException → 查看日志堆栈，定位具体行
│
├─ Mod 列表中看不到你的 mod？
│   └─ 检查 About.xml 语法 + packageId 是否重复
│
└─ 游戏中行为异常（但不报错）？
    ├─ 在可疑代码中加入 Log.Message() 输出变量值
    ├─ 用开发者模式手动测试每个功能
    └─ 检查 Harmony 补丁是否成功加载（看日志中你的 Log.Message）
```

## 二分法排查 Mod 冲突

1. 禁用所有 mod，只留 Core + Harmony + 你的 mod
2. **问题消失？** → 是 mod 冲突
3. 启用一半 mod，测试
4. 反复二分，直到找到冲突 mod
5. 查看冲突 mod 是否 patch 了相同的类/方法

## 1.7 没有开发者控制台（旧命令一律按不存在处理）

1.6 及更早的教程会让你按 `` ` ``（反引号）打开「开发者控制台」，敲 `list defs`、`spawn <defName>`——**1.7 已经移除**：`Assembly-CSharp.dll` 里查不到 `DevConsole` / `ExecuteCommand` 字符串，照抄这些命令不会有任何反应。1.7 能用的入口是：

| 想做的事 | 1.7 里的做法 |
|----------|--------------|
| 确认 Def 到底有没有加载 | 读 `Logs\Player.log`（路径与查找办法见 `references/08-debugging.md`），搜 XML 报错与你的 packageId；或对 mod 目录跑静态核验：`node docs/verify-testmod.mjs --mod <mod 目录>`（本仓库脚本） |
| 把物品生成出来看效果 | 开发者模式 → 顶部工具栏的 debug actions 菜单 → `Spawning` → `Spawn thing` → 搜你的 defName |
| 触发事件 / 折腾选中单位 | 同一菜单的其余分类（`General` / `Pawns` / `Anomaly`），对选中单位可用 `Apply damage`、`Kill`、`Down`、`Recruit` 等动作 |
| 看游戏这一局的运行日志 | 直接打开用户数据目录里的 `Logs\Player.log`（`Logs\` 与 `Config\` 同级） |

## 获取帮助时应该提供的信息

在贴吧/论坛/Discord 求助时，附上以下内容有助于快速定位问题：

1. **Player.log** 完整内容（使用 Pastebin 等工具上传）
2. **你的 mod 的 About.xml**
3. **出错相关代码**（XML 片段或 C# 代码）
4. **其他已加载 mod 列表**
5. **复现步骤**：做了什么操作触发了问题？

## 记录教训

定位并修复问题后，将本次错误总结为一句话追加到 `learnings/errors.txt`，
格式：`YYYY-MM-DD | <类别> | <一句话总结>`

常见类别：XML / C# / Harmony / Path / Other
