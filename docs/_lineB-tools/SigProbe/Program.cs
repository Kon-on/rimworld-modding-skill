// AI 辅助生成 —— 临时元数据探针（只读游戏 DLL，不修改任何游戏文件）
// 用途：用真实反射读取 RimWorld 1.7 Assembly-CSharp.dll 与 0Harmony.dll 的类型/成员签名，
// 避免凭记忆写 Harmony 补丁目标与 ThingComp 重写签名。
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Loader;

internal static class Program
{
    // 不写死本机路径：运行时从环境变量取（缺失时报错并说明该指到哪里）
    //   RIMWORLD_DIR = 游戏根目录（含 Assembly-CSharp.dll / UnityStubs.dll / RimWorld.dll 的那一层）
    //   HARMONY_DIR  = 含 0Harmony.dll 的目录（创意工坊 Harmony mod 的 1.7\Assemblies）
    private static readonly string GameDir = Environment.GetEnvironmentVariable("RIMWORLD_DIR") ?? "";
    private static readonly string HarmonyDir = Environment.GetEnvironmentVariable("HARMONY_DIR") ?? "";
    private const char BackTick = (char)96;

    private static int Main(string[] args)
    {
        AssemblyLoadContext.Default.Resolving += Resolve;
        if (args.Length == 0)
        {
            Console.WriteLine("usage: one <GAME|HARMONY|UNITYSTUBS|RIMWORLD|path> <typeFullName> | dump <...> <substr> | list <...> <substr>");
            Console.WriteLine("       GAME/UNITYSTUBS/RIMWORLD 取环境变量 RIMWORLD_DIR，HARMONY 取 HARMONY_DIR；也可直接给 DLL 路径");
            return 2;
        }
        string cmd = args[0];
        try
        {
            if (cmd == "one")
            {
                var asm = Load(args[1]);
                var t = asm.GetType(args[2], throwOnError: false);
                if (t == null) { Console.WriteLine("TYPE NOT FOUND: " + args[2]); return 1; }
                DumpType(t, Console.Out, true);
                return 0;
            }
            if (cmd == "dump" || cmd == "list")
            {
                var asm = Load(args[1]);
                string sub = args.Length > 2 ? args[2] : "";
                foreach (var t in SafeTypes(asm))
                {
                    if (sub.Length > 0 && t.FullName.IndexOf(sub, StringComparison.OrdinalIgnoreCase) < 0) continue;
                    if (cmd == "list") Console.WriteLine(t.FullName);
                    else { DumpType(t, Console.Out, false); Console.WriteLine(); }
                }
                return 0;
            }
        }
        catch (Exception ex) { Console.WriteLine("ERROR: " + ex); return 1; }
        return 2;
    }

    private static Assembly Resolve(AssemblyLoadContext ctx, AssemblyName name)
    {
        string n = name.Name;
        if (n.StartsWith("System.", StringComparison.Ordinal) || n.StartsWith("Microsoft.", StringComparison.Ordinal)
            || n == "netstandard" || n == "mscorlib" || n == "System" || n == "WindowsBase") return null;
        foreach (var dir in new[] { GameDir, HarmonyDir })
        {
            var p = Path.Combine(dir, n + ".dll");
            if (File.Exists(p)) { try { return ctx.LoadFromAssemblyPath(p); } catch (Exception e) { Console.Error.WriteLine("[resolve-fail] " + n + " : " + e.Message); } }
        }
        return null;
    }

    private static string Need(string dir, string env, string what)
    {
        if (string.IsNullOrEmpty(dir)) throw new InvalidOperationException("缺少环境变量 " + env + "，应指向" + what);
        return dir;
    }

    private static Assembly Load(string spec)
    {
        if (spec == "GAME") return AssemblyLoadContext.Default.LoadFromAssemblyPath(Path.Combine(Need(GameDir, "RIMWORLD_DIR", " RimWorld 游戏根目录（含 Assembly-CSharp.dll）"), "Assembly-CSharp.dll"));
        if (spec == "HARMONY") return AssemblyLoadContext.Default.LoadFromAssemblyPath(Path.Combine(Need(HarmonyDir, "HARMONY_DIR", "含 0Harmony.dll 的目录"), "0Harmony.dll"));
        if (spec == "UNITYSTUBS") return AssemblyLoadContext.Default.LoadFromAssemblyPath(Path.Combine(Need(GameDir, "RIMWORLD_DIR", " RimWorld 游戏根目录（含 UnityStubs.dll）"), "UnityStubs.dll"));
        if (spec == "RIMWORLD") return AssemblyLoadContext.Default.LoadFromAssemblyPath(Path.Combine(Need(GameDir, "RIMWORLD_DIR", " RimWorld 游戏根目录（含 RimWorld.dll）"), "RimWorld.dll"));
        return AssemblyLoadContext.Default.LoadFromAssemblyPath(spec);
    }

    private static IEnumerable<Type> SafeTypes(Assembly asm)
    {
        try { return asm.GetTypes(); }
        catch (ReflectionTypeLoadException ex)
        {
            Console.Error.WriteLine("[warn] ReflectionTypeLoadException, " + ex.LoaderExceptions.Length + " loader exceptions");
            foreach (var le in ex.LoaderExceptions.Take(3)) Console.Error.WriteLine("   => " + le.Message);
            return ex.Types.Where(t => t != null);
        }
    }

    private static string TName(Type t)
    {
        if (t == null) return "?";
        if (t.IsGenericParameter) return t.Name;
        if (t.IsArray) return TName(t.GetElementType()) + "[]";
        if (t.IsByRef) return TName(t.GetElementType()) + "&";
        if (!t.IsGenericType) return t.FullName ?? t.Name;
        var def = t.GetGenericTypeDefinition();
        string bn = (def.FullName ?? def.Name);
        int tick = bn.IndexOf(BackTick);
        if (tick > 0) bn = bn.Substring(0, tick);
        return bn + "<" + string.Join(",", t.GetGenericArguments().Select(TName)) + ">";
    }

    private static string Mods(MethodBase m)
    {
        var parts = new List<string>();
        if (m.IsPublic) parts.Add("public"); else if (m.IsFamily) parts.Add("protected"); else if (m.IsAssembly) parts.Add("internal"); else if (m.IsFamilyOrAssembly) parts.Add("protected internal"); else parts.Add("private");
        if (m.IsStatic) parts.Add("static");
        if (m.IsAbstract) parts.Add("abstract");
        else if (m.IsVirtual && !m.IsFinal) parts.Add("virtual");
        if (m.IsDefined(typeof(System.Runtime.CompilerServices.ExtensionAttribute), false)) parts.Add("ext");
        return string.Join(" ", parts);
    }

    private static void DumpType(Type t, TextWriter w, bool members)
    {
        string kind = t.IsEnum ? "enum" : t.IsValueType ? "struct" : t.IsInterface ? "interface" : t.IsClass ? "class" : "type";
        string bt = t.BaseType != null ? " : " + TName(t.BaseType) : "";
        string ifaces = t.GetInterfaces().Length > 0 ? " :: " + string.Join(", ", t.GetInterfaces().Select(TName)) : "";
        w.WriteLine("TYPE " + (t.IsPublic ? "public " : t.IsNotPublic ? "internal " : "") + (t.IsAbstract && t.IsSealed ? "static " : "") + kind + " " + TName(t) + bt + ifaces);

        if (members)
        {
            foreach (var f in t.GetFields(BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance | BindingFlags.Static | BindingFlags.DeclaredOnly).OrderBy(f => f.Name))
                w.WriteLine("  FIELD " + (f.IsPublic ? "public" : f.IsFamily ? "protected" : f.IsAssembly ? "internal" : "private") + (f.IsStatic ? " static" : "") + (f.IsInitOnly ? " readonly" : "") + " " + TName(f.FieldType) + " " + f.Name + (f.IsLiteral && f.IsStatic ? " = " + (f.GetRawConstantValue() ?? "null") : ""));
            foreach (var p in t.GetProperties(BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance | BindingFlags.Static | BindingFlags.DeclaredOnly).OrderBy(p => p.Name))
                w.WriteLine("  PROP " + TName(p.PropertyType) + " " + p.Name + " { " + (p.CanRead ? "get; " : "") + (p.CanWrite ? "set; " : "") + "}");
            foreach (var c in t.GetConstructors(BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance | BindingFlags.Static | BindingFlags.DeclaredOnly))
                w.WriteLine("  CTOR " + Mods(c) + " .ctor(" + string.Join(", ", c.GetParameters().Select(P)) + ")");
            foreach (var m in t.GetMethods(BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance | BindingFlags.Static | BindingFlags.DeclaredOnly).OrderBy(m => m.Name).ThenBy(m => m.GetParameters().Length))
                w.WriteLine("  METHOD " + Mods(m) + " " + TName(m.ReturnType) + " " + m.Name + (m.IsGenericMethodDefinition ? "<" + string.Join(",", m.GetGenericArguments().Select(a => a.Name)) + ">" : "") + "(" + string.Join(", ", m.GetParameters().Select(P)) + ")");
        }
        else
        {
            int mcount = 0; try { mcount = t.GetMethods(BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance | BindingFlags.Static | BindingFlags.DeclaredOnly).Length; } catch { }
            w.WriteLine("      [methods=" + mcount + "]");
        }
    }

    private static string P(ParameterInfo p)
    {
        string s = (p.ParameterType.IsByRef ? (p.IsOut ? "out " : "ref ") : "") + TName(p.ParameterType) + " " + p.Name;
        if (p.HasDefaultValue && p.DefaultValue != null && !(p.DefaultValue is DBNull)) s += " = " + p.DefaultValue;
        return s;
    }
}
