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

## 常用调试命令（开发者控制台）

在开发者模式下按 `` ` ``（反引号）打开开发者控制台：

| 命令 | 作用 |
|------|------|
| `list defs ThingDef` | 列出所有 ThingDef |
| `list defs <YourPrefix>` | 列出你的 mod 的 Def |
| `spawn <defName>` | 生成指定物品 |

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
