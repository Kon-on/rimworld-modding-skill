/*
 * xml-lint.mjs —— 零依赖的 XML 良构性极简扫描（Node 18+，无第三方库）
 *
 * 为什么存在：技能承诺「有模板 → 直接用（免核验）」。若模板本身不是合法 XML，
 * 这条承诺就是错的——本项目曾 8 个 XML 模板里 7 个解析失败，两类原因：
 *   1) 元素文本里写了尖括号占位符：<defName><YourPrefix>_Weapon_<YourName></defName>
 *      （占位符正确写法是 {{YourPrefix}}_Weapon_{{YourName}}）
 *   2) 注释里出现 -- 连字符 runs（XML 规定注释内容不得含 '--'，也不得以 '-' 结尾）
 *
 * 只做良构性（标签配对、注释/CDATA/声明闭合），不做 schema 校验，不解析实体。
 * 用法：import { xmlProblems } from "./xml-lint.mjs";
 *      xmlProblems(source) → [[行号, 说明], …]（空数组 = 良构）
 */
export function xmlProblems(src) {
  const problems = [];
  const lineAt = (idx) => src.slice(0, idx).split("\n").length;
  const stack = [];
  let i = 0;
  while (i < src.length) {
    const lt = src.indexOf("<", i);
    if (lt === -1) break;
    if (src.startsWith("<!--", lt)) {
      const end = src.indexOf("-->", lt + 4);
      if (end === -1) { problems.push([lineAt(lt), "注释未闭合"]); break; }
      const body = src.slice(lt + 4, end);
      if (body.includes("--")) problems.push([lineAt(lt), "注释内容含 '--'（XML 非法）"]);
      if (body.endsWith("-")) problems.push([lineAt(lt), "注释以 '-' 结尾（XML 非法）"]);
      i = end + 3; continue;
    }
    if (src.startsWith("<![CDATA[", lt)) {
      const end = src.indexOf("]]>", lt + 9);
      if (end === -1) { problems.push([lineAt(lt), "CDATA 未闭合"]); break; }
      i = end + 3; continue;
    }
    if (src.startsWith("<?", lt)) {
      const end = src.indexOf("?>", lt + 2);
      if (end === -1) { problems.push([lineAt(lt), "XML 声明未闭合"]); break; }
      i = end + 2; continue;
    }
    if (src.startsWith("<!", lt)) {
      const end = src.indexOf(">", lt + 2);
      if (end === -1) break;
      i = end + 1; continue;
    }
    const m = /^<(\/?)([A-Za-z_][A-Za-z0-9_.:-]*)([^<>]*?)(\/?)>/.exec(src.slice(lt));
    if (!m) {
      const snippet = src.slice(lt, lt + 40).replace(/\s+/g, " ");
      problems.push([lineAt(lt), `非法／未闭合的标签：${snippet}`]);
      const nxt = src.indexOf(">", lt);
      if (nxt === -1) break;
      i = nxt + 1; continue;
    }
    const closing = m[1], name = m[2], selfClose = m[4];
    if (closing) {
      const top = stack.pop();
      if (top !== name) problems.push([lineAt(lt), `标签不配对：</${name}> 对应 <${top ?? "（无）"}>`]);
    } else if (!selfClose) stack.push(name);
    i = lt + m[0].length;
  }
  if (stack.length) problems.push([lineAt(src.length - 1), `标签未闭合：<${stack.join(">, <")}>`]);
  return problems;
}
