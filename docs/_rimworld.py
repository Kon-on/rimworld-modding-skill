# -*- coding: utf-8 -*-
r"""定位 RimWorld 安装目录与创意工坊 Harmony 目录 —— 不写死任何本机路径。

解析顺序：环境变量 RIMWORLD_DIR / HARMONY_DIR → Steam 注册表 → Steam 库清单
          steamapps\libraryfolders.vdf → 常见默认位置。找不到时报错并说明怎么设置。

用法：
    from _rimworld import game_dir, harmony_dir
    GAME = game_dir()

直接运行（自检）：python docs/_rimworld.py
"""
import os
import re
from pathlib import Path

HARMONY_WORKSHOP_ID = "2009463077"


def _steam_roots():
    """Steam 客户端安装目录：注册表优先，其次常见默认位置。"""
    raw = []
    try:
        import winreg  # 仅 Windows 有；其它平台走下面的环境变量分支
        for hive, sub in ((winreg.HKEY_CURRENT_USER, r"Software\Valve\Steam"),
                          (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\Valve\Steam"),
                          (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Valve\Steam")):
            try:
                with winreg.OpenKey(hive, sub) as k:
                    for name in ("SteamPath", "InstallPath"):
                        try:
                            v, _ = winreg.QueryValueEx(k, name)
                            if v:
                                raw.append(str(v).replace("/", "\\"))
                        except OSError:
                            pass
            except OSError:
                pass
    except ImportError:
        pass
    for env_name in ("ProgramFiles(x86)", "ProgramFiles"):
        base = os.environ.get(env_name)
        if base:
            raw.append(os.path.join(base, "Steam"))
    out, seen = [], set()
    for r in raw:
        rc = os.path.normpath(r)
        if rc.lower() in seen or not os.path.isdir(rc):
            continue
        seen.add(rc.lower())
        out.append(rc)
    return out


def _library_dirs():
    """所有 Steam 库根目录（含 libraryfolders.vdf 里登记的额外库）。"""
    out, seen = [], set()
    for root in _steam_roots():
        cands = [root]
        vdf = os.path.join(root, "steamapps", "libraryfolders.vdf")
        if os.path.isfile(vdf):
            try:
                text = Path(vdf).read_text(encoding="utf-8", errors="ignore")
                cands += [m.group(1).replace("\\\\", "\\")
                          for m in re.finditer(r'"path"\s+"([^"]+)"', text)]
            except OSError:
                pass
        for c in cands:
            cc = os.path.normpath(c)
            if cc.lower() in seen or not os.path.isdir(cc):
                continue
            seen.add(cc.lower())
            out.append(cc)
    return out


def game_dir():
    """RimWorld 安装根目录（含 Assembly-CSharp.dll 的那一层）。"""
    cands = []
    if os.environ.get("RIMWORLD_DIR"):
        cands.append(os.environ["RIMWORLD_DIR"])
    cands += [os.path.join(lib, "steamapps", "common", "RimWorld") for lib in _library_dirs()]
    for c in cands:
        if c and os.path.isfile(os.path.join(c, "Assembly-CSharp.dll")):
            return os.path.abspath(c)
    raise SystemExit("找不到 RimWorld 安装目录：请设置环境变量 RIMWORLD_DIR 指向游戏根目录"
                     "（含 Assembly-CSharp.dll 的那一层）后重跑。")


def harmony_dir(game=None):
    """创意工坊 Harmony mod 的 Assemblies 目录（含 0Harmony.dll）。"""
    cands = []
    if os.environ.get("HARMONY_DIR"):
        cands.append(os.environ["HARMONY_DIR"])
    g = game or game_dir()
    tail = os.path.join("workshop", "content", "294100", HARMONY_WORKSHOP_ID, "1.7", "Assemblies")
    cands.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(g))), tail))
    cands += [os.path.join(lib, "steamapps", tail) for lib in _library_dirs()]
    for c in cands:
        if c and os.path.isfile(os.path.join(c, "0Harmony.dll")):
            return os.path.abspath(c)
    raise SystemExit("找不到 0Harmony.dll：请订阅创意工坊 Harmony mod（id %s），"
                     "或用环境变量 HARMONY_DIR 指向含 0Harmony.dll 的目录。" % HARMONY_WORKSHOP_ID)


if __name__ == "__main__":
    print("RimWorld = " + game_dir())
    print("Harmony  = " + harmony_dir())
