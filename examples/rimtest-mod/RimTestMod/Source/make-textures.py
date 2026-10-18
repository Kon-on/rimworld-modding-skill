#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
make-textures.py -- 环世界「完整测试 Mod」(rimtest-mod) 全部 PNG 贴图的程序化生成脚本
AI 辅助生成（本文件由 AI 编写；全部图形为原创几何绘制，未引用任何第三方素材）

用法:
    python make-textures.py                      生成全部贴图 -> 写 Textures/_MANIFEST.json -> 自检
    python make-textures.py --verify-only        只读回已有 PNG 校验（尺寸/RGBA/非空/透明角/sha256）
    python make-textures.py --out <dir>          覆盖 mod 根目录（默认 = 本脚本上两级目录）
    python make-textures.py --contact-sheet <f>  另存一张开发总览图（不是 mod 素材，仅自检用）

可重跑性: 无随机源、无时间戳、无网络；同一 Pillow 版本下输出字节级一致。
风格: 纯几何 + 线性渐变 + 高斯发光；青蓝主色 #38D8E8 + 深灰金属 #4A525E；透明 RGBA 背景。
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps
from PIL import __version__ as PILLOW_VERSION

# ─────────────────────────── 全局常量 ───────────────────────────

SS = 4  # 超采样倍率：所有图形按 SS 倍绘制，最后 LANCZOS 缩回目标尺寸，得到清晰抗锯齿边缘

C = {
    "cyan":     (56, 216, 232, 255),
    "cyan_dk":  (14, 110, 140, 255),
    "cyan_lt":  (168, 232, 255, 255),
    "glow":     (232, 251, 255, 255),
    "blue":     (60, 130, 246, 255),
    "violet":   (128, 92, 232, 255),
    "metal_dk": (43, 48, 56, 255),
    "metal":    (74, 82, 94, 255),
    "metal_lt": (138, 148, 162, 255),
    "outline":  (16, 22, 30, 255),
    "leaf":     (62, 122, 68, 255),
    "leaf_lt":  (104, 168, 96, 255),
    "bg_dk":    (11, 18, 30, 255),
    "bg_lt":    (22, 34, 47, 255),
}

# ─────────────────────────── 绘图基元 ───────────────────────────

def P(x, y):
    return (x * SS, y * SS)

def B(x0, y0, x1, y1):
    return (x0 * SS, y0 * SS, x1 * SS, y1 * SS)

def LY(pts):
    return [(x * SS, y * SS) for x, y in pts]

def WD(v):
    return max(1, int(round(v * SS)))

def new_canvas(w, h):
    return Image.new("RGBA", (int(round(w * SS)), int(round(h * SS))), (0, 0, 0, 0))

def finish(img, w, h):
    return img.resize((int(w), int(h)), Image.LANCZOS)

def new_mask(img):
    m = Image.new("L", img.size, 0)
    return m, ImageDraw.Draw(m)

def poly(d, pts, fill=None, outline=None, width=1.6):
    d.polygon(LY(pts), fill=fill)
    if outline is not None:
        seq = LY(pts)
        d.line(seq + [seq[0]], fill=outline, width=WD(width), joint="curve")

def rect(d, x0, y0, x1, y1, fill=None, outline=None, width=1.6):
    d.rectangle(B(x0, y0, x1, y1), fill=fill,
                outline=outline, width=WD(width) if outline is not None else 0)

def rrect(d, x0, y0, x1, y1, r, fill=None, outline=None, width=1.6):
    d.rounded_rectangle(B(x0, y0, x1, y1), radius=r * SS, fill=fill,
                        outline=outline, width=WD(width) if outline is not None else 0)

def ell(d, cx, cy, rx, ry, fill=None, outline=None, width=1.6):
    d.ellipse(B(cx - rx, cy - ry, cx + rx, cy + ry), fill=fill,
              outline=outline, width=WD(width) if outline is not None else 0)

def seg(d, x0, y0, x1, y1, fill, width=1.6):
    d.line([P(x0, y0), P(x1, y1)], fill=fill, width=WD(width))

def grad_fill(img, mask, c1, c2, direction=(0.0, 1.0)):
    """在 mask 区域内填充沿 direction（屏幕坐标，y 向下）的线性渐变：起点色 c1 -> 终点色 c2。"""
    w, h = img.size
    dx, dy = direction
    n = math.hypot(dx, dy) or 1.0
    dx, dy = dx / n, dy / n
    projs = [x * dx + y * dy for x in (0.0, w) for y in (0.0, h)]
    lo, hi = min(projs), max(projs)
    grad = Image.new("L", (w, h), 0)
    gd = ImageDraw.Draw(grad)
    steps = max(8, int(math.hypot(w, h)))
    px, py = -dy, dx
    big = float(w + h)
    for i in range(steps + 1):
        t = i / steps
        p = lo + (hi - lo) * t
        cx, cy = dx * p, dy * p
        gd.line([(cx - px * big, cy - py * big), (cx + px * big, cy + py * big)],
                fill=int(round(t * 255)), width=2)
    img.paste(ImageOps.colorize(grad, c1[:3], c2[:3]).convert("RGBA"), (0, 0), mask)

def add_glow(img, mask, color, radius, alpha=150):
    layer = Image.new("RGBA", img.size, color[:3] + (0,))
    blurred = mask.filter(ImageFilter.GaussianBlur(radius * SS))
    layer.putalpha(blurred.point(lambda v: int(v * alpha / 255.0)))
    img.alpha_composite(layer)

def fit_h(layer, canvas_w, canvas_h, target_w=118.0, cx=None, cy=None):
    """把水平绘制的工件按不透明包围盒缩放到 target_w（逻辑像素）宽并水平居中合成。

    1.7 原版武器贴图本身就是水平绘制（实测 AssaultRifle 占 y 49..98、Gladius 占 y 50..71，
    均横跨整幅 128 画布），装备/瞄准时由 PawnRenderer 按朝向自行旋转 45 度，因此不要预先斜置。"""
    box = layer.getchannel("A").getbbox()
    out = new_canvas(canvas_w, canvas_h)
    if box is None:
        return out
    art = layer.crop(box)
    s = (target_w * SS) / float(art.width)
    art = art.resize((max(1, int(round(art.width * s))), max(1, int(round(art.height * s)))), Image.LANCZOS)
    ox = int(round(canvas_w * SS / 2.0 - art.width / 2.0)) if cx is None else int(round(cx * SS - art.width / 2.0))
    oy = int(round(canvas_h * SS / 2.0 - art.height / 2.0)) if cy is None else int(round(cy * SS - art.height / 2.0))
    out.alpha_composite(art, (ox, oy))
    return out

# ─────────────────────────── 素材 1: 等离子匕首（近战武器物品图标）───────────────────────────

def mk_plasma_dagger():
    work = new_canvas(150, 40)
    d = ImageDraw.Draw(work)

    # 刀身（水平绘制，刀尖朝 +x；与原版 Gladius 一样保持水平，装备时由游戏按朝向旋转）
    blade = [(42, 14.5), (74, 13.0), (104, 16.0), (121, 20.0), (104, 24.0), (74, 27.0), (42, 25.5)]
    bm, bd = new_mask(work)
    bd.polygon(LY(blade), fill=255)
    add_glow(work, bm, C["cyan"], 6.0, 120)
    add_glow(work, bm, C["glow"], 2.2, 70)
    poly(d, blade, fill=None, outline=C["outline"], width=1.4)
    grad_fill(work, bm, C["violet"], C["cyan_lt"], direction=(1.0, 0.0))
    poly(d, blade, fill=None, outline=C["outline"], width=1.4)

    # 刀脊高光（贯穿刀身中轴的亮线）
    seg(d, 44, 20.0, 118, 20.0, C["glow"], 1.3)
    seg(d, 44, 20.0, 118, 20.0, C["cyan"], 0.6)

    # 护手
    rrect(d, 35.5, 7.5, 41.5, 32.5, 1.6, fill=C["metal_lt"], outline=C["outline"], width=1.4)
    seg(d, 38.5, 9.0, 38.5, 31.0, C["metal_dk"], 1.0)

    # 握柄（深色 + 缠带）
    rrect(d, 12.0, 15.0, 35.0, 25.0, 3.0, fill=C["metal_dk"], outline=C["outline"], width=1.4)
    for x in (16.0, 20.0, 24.0, 28.0, 32.0):
        seg(d, x, 16.2, x, 23.8, C["metal"], 1.1)
    seg(d, 14.0, 19.2, 33.0, 19.2, C["cyan"], 0.9)

    # 尾端配重 + 能量宝石
    ell(d, 10.0, 20.0, 6.2, 6.2, fill=C["metal"], outline=C["outline"], width=1.4)
    gm, gd_ = new_mask(work)
    gd_.ellipse(B(7.4, 17.4, 12.6, 22.6), fill=255)
    add_glow(work, gm, C["cyan"], 3.0, 160)
    ell(d, 10.0, 20.0, 2.6, 2.6, fill=C["glow"])

    return fit_h(work, 128, 128, target_w=120.0, cy=62.0)

# ─────────────────────────── 素材 2: 离子步枪（远程武器物品图标）───────────────────────────

def mk_ion_rifle():
    work = new_canvas(150, 54)
    d = ImageDraw.Draw(work)

    # 枪托
    poly(d, [(8, 20), (24, 17.5), (24, 36.5), (8, 34)], fill=C["metal_dk"], outline=C["outline"], width=1.4)
    # 机匣主体
    rrect(d, 22, 16.5, 96, 37.5, 2.6, fill=None, outline=C["outline"], width=1.4)
    body_m, body_d = new_mask(work)
    body_d.rounded_rectangle(B(22, 16.5, 96, 37.5), radius=2.6 * SS, fill=255)
    grad_fill(work, body_m, C["metal_dk"], C["metal"], direction=(0.0, 1.0))
    rrect(d, 22, 16.5, 96, 37.5, 2.6, fill=None, outline=C["outline"], width=1.4)
    # 机匣顶面高光
    seg(d, 25, 18.8, 93, 18.8, C["metal_lt"], 1.2)
    # 抛壳口 / 散热槽
    for x in (30.0, 35.0, 40.0, 45.0):
        seg(d, x, 21.5, x, 32.0, C["metal"], 1.0)
    # 枪管
    rrect(d, 94, 23.0, 132, 30.5, 1.4, fill=C["metal"], outline=C["outline"], width=1.3)
    seg(d, 96, 25.0, 130, 25.0, C["metal_lt"], 0.9)
    # 枪口能量环 + 辉光
    mm, md_ = new_mask(work)
    md_.rounded_rectangle(B(130, 20.5, 138, 33.5), radius=1.5 * SS, fill=255)
    add_glow(work, mm, C["cyan"], 4.5, 190)
    rrect(d, 130, 20.5, 138, 33.5, 1.5, fill=C["cyan_lt"], outline=C["outline"], width=1.3)
    seg(d, 133, 22.5, 133, 31.5, C["glow"], 1.2)
    # 顶部导轨 + 瞄准镜
    rect(d, 40, 12.5, 74, 17.5, fill=C["metal_dk"], outline=C["outline"], width=1.2)
    rrect(d, 44, 7.5, 70, 14.5, 2.0, fill=C["metal"], outline=C["outline"], width=1.3)
    ell(d, 48.5, 11.0, 1.9, 1.9, fill=C["glow"])
    ell(d, 65.5, 11.0, 1.6, 1.6, fill=C["cyan"])
    # 能量槽（蓝白发光，本体特征）
    em, ed = new_mask(work)
    ed.rounded_rectangle(B(58, 33.5, 92, 46.5), radius=2.4 * SS, fill=255)
    add_glow(work, em, C["cyan"], 3.6, 175)
    rrect(d, 58, 33.5, 92, 46.5, 2.4, fill=C["cyan_dk"], outline=C["outline"], width=1.3)
    grad_fill(work, em, C["cyan_dk"], C["cyan_lt"], direction=(1.0, 0.0))
    rrect(d, 58, 33.5, 92, 46.5, 2.4, fill=None, outline=C["outline"], width=1.3)
    for x in (66.0, 75.0, 84.0):
        seg(d, x, 35.0, x, 45.0, C["outline"], 1.1)
    rrect(d, 61, 38.0, 89, 42.0, 1.4, fill=C["glow"])
    # 握把
    poly(d, [(45, 37), (56, 37), (52, 52), (41, 52)], fill=C["metal_dk"], outline=C["outline"], width=1.3)
    for k in range(4):
        yy = 40.0 + k * 3.0
        seg(d, 44.0 + k * 0.9, yy, 54.0 - k * 1.1, yy, C["metal"], 0.9)
    # 弹匣
    poly(d, [(64, 37), (77, 37), (79, 50), (66, 50)], fill=C["metal"], outline=C["outline"], width=1.2)
    seg(d, 67, 47.5, 77, 47.5, C["cyan"], 1.0)

    return fit_h(work, 128, 128, target_w=124.0, cy=66.0)

# ─────────────────────────── 素材 3: 离子子弹（32x32）───────────────────────────

def mk_ion_bullet():
    img = new_canvas(32, 32)
    d = ImageDraw.Draw(img)
    # 水平胶囊，弹头朝右（ProjectileDef 的 drawRotated 会按飞行方向旋转这张图）
    capsule = [(6.5, 12.6), (20.0, 11.4), (26.0, 16.0), (20.0, 20.6), (6.5, 19.4)]
    cm, cd = new_mask(img)
    cd.polygon(LY(capsule), fill=255)
    add_glow(img, cm, C["cyan"], 3.8, 205)
    add_glow(img, cm, C["glow"], 1.6, 120)
    poly(d, capsule, fill=None, outline=C["outline"], width=0.9)
    grad_fill(img, cm, C["blue"], C["glow"], direction=(1.0, 0.0))
    poly(d, capsule, fill=None, outline=C["cyan_dk"], width=0.8)
    # 弹芯
    seg(d, 9.0, 16.0, 22.5, 16.0, C["glow"], 1.6)
    ell(d, 24.0, 16.0, 1.6, 1.6, fill=C["glow"])
    # 尾迹
    seg(d, 4.0, 16.0, 7.5, 16.0, C["cyan"], 1.2)
    return img

# ─────────────────────────── 素材 4: 战术背心（物品图标）───────────────────────────

def mk_vest_icon():
    img = new_canvas(128, 128)
    d = ImageDraw.Draw(img)
    body = [(24, 26), (38, 16), (90, 16), (104, 26), (108, 44), (108, 96), (100, 110), (28, 110), (20, 96), (20, 44)]

    bm, bd = new_mask(img)
    bd.polygon(LY(body), fill=255)
    add_glow(img, bm, C["cyan"], 2.6, 60)
    poly(d, body, fill=None, outline=C["outline"], width=2.0)
    grad_fill(img, bm, C["metal_dk"], C["metal"], direction=(0.0, 1.0))
    poly(d, body, fill=None, outline=C["outline"], width=2.0)

    # 肩带
    poly(d, [(38, 16), (50, 16), (44, 40), (30, 34)], fill=C["metal_lt"], outline=C["outline"], width=1.5)
    poly(d, [(78, 16), (90, 16), (98, 34), (84, 40)], fill=C["metal_lt"], outline=C["outline"], width=1.5)
    # 领口
    poly(d, [(52, 16), (64, 34), (76, 16)], fill=C["metal_dk"], outline=C["outline"], width=1.5)
    seg(d, 53, 18, 64, 33, C["cyan"], 1.2)
    seg(d, 75, 18, 64, 33, C["cyan"], 1.2)
    # 胸板
    rrect(d, 30, 34, 56, 62, 3.0, fill=C["metal"], outline=C["outline"], width=1.5)
    rrect(d, 72, 34, 98, 62, 3.0, fill=C["metal"], outline=C["outline"], width=1.5)
    for k in range(3):
        yy = 40.0 + k * 7.0
        seg(d, 33, yy, 53, yy, C["metal_dk"], 1.1)
        seg(d, 75, yy, 95, yy, C["metal_dk"], 1.1)
    # 中央能量核心
    cm, cd = new_mask(img)
    cd.ellipse(B(52, 44, 76, 68), fill=255)
    add_glow(img, cm, C["cyan"], 3.0, 165)
    ell(d, 64, 56, 12.0, 12.0, fill=C["cyan_dk"], outline=C["outline"], width=1.6)
    grad_fill(img, cm, C["cyan_dk"], C["cyan_lt"], direction=(1.0, -1.0))
    ell(d, 64, 56, 12.0, 12.0, fill=None, outline=C["outline"], width=1.6)
    ell(d, 64, 56, 5.2, 5.2, fill=C["glow"])
    for ang in (0, 60, 120, 180, 240, 300):
        rx = 64 + 9.4 * math.cos(math.radians(ang))
        ry = 56 + 9.4 * math.sin(math.radians(ang))
        seg(d, rx, ry, 64 + 13.6 * math.cos(math.radians(ang)), 56 + 13.6 * math.sin(math.radians(ang)), C["cyan"], 1.0)
    # 腰袋
    rrect(d, 26, 70, 54, 96, 2.6, fill=C["metal_dk"], outline=C["outline"], width=1.5)
    rrect(d, 74, 70, 102, 96, 2.6, fill=C["metal_dk"], outline=C["outline"], width=1.5)
    seg(d, 26, 82, 54, 82, C["outline"], 1.1)
    seg(d, 74, 82, 102, 82, C["outline"], 1.1)
    ell(d, 40, 76, 1.8, 1.8, fill=C["cyan"])
    ell(d, 88, 76, 1.8, 1.8, fill=C["cyan"])
    # 侧面束带
    for side in (0, 1):
        x0 = 20 if side == 0 else 100
        rect(d, x0, 66, x0 + 8, 70, fill=C["cyan_dk"], outline=C["outline"], width=1.0)
        rect(d, x0, 88, x0 + 8, 92, fill=C["cyan_dk"], outline=C["outline"], width=1.0)
    # 下摆能量条
    rrect(d, 30, 100, 98, 106, 2.0, fill=C["cyan_dk"], outline=C["outline"], width=1.2)
    seg(d, 34, 103, 94, 103, C["cyan"], 1.1)
    return img

# ─────────────────────────── 素材 5: 战术背心（四个朝向的穿戴外观）───────────────────────────
# 对位依据（已从游戏根 Assets.zip 解出原版参考贴图实测，Rosetta: Resources/Textures/Things/...）:
#   Naked_Male_south  128x128 躯干 x 38..89 / y 40..107（肩线 y≈44，下摆 y≈104）
#   FlakJacket_male_south 128x128 x 33..93 / y 28..110
# 故本背心南/北朝向占 x 34..94、y 42..106；侧视（east/west）占 x 44..86、y 44..104。

VEST_SIL = [(38, 48), (46, 42), (54, 42), (57, 52), (71, 52), (74, 42), (82, 42), (90, 48),
            (94, 60), (94, 96), (86, 106), (42, 106), (34, 96), (34, 60)]
VEST_SIDE = [(46, 50), (54, 44), (74, 44), (82, 50), (86, 62), (86, 94), (80, 104), (52, 104),
             (44, 94), (44, 62)]

def _vest_body_shape(pts, glow=62, glow_r=2.6):
    img = new_canvas(128, 128)
    d = ImageDraw.Draw(img)
    m, md = new_mask(img)
    md.polygon(LY(pts), fill=255)
    add_glow(img, m, C["cyan"], glow_r, glow)
    poly(d, pts, fill=None, outline=C["outline"], width=1.6)
    grad_fill(img, m, C["metal_lt"], C["metal"], direction=(0.0, 1.0))
    poly(d, pts, fill=None, outline=C["outline"], width=1.6)
    return img, d

def mk_vest_worn_south():
    img, d = _vest_body_shape(VEST_SIL)
    # 正面: 领口包边 + 两条肩带 + 胸板能量核心 + 胸袋/腰袋 + 青蓝下摆条
    poly(d, [(54, 42), (57.5, 52), (70.5, 52), (74, 42)], fill=None, outline=C["cyan"], width=1.3)
    for x0 in (38, 74):
        rrect(d, x0, 44, x0 + 16, 60, 2.4, fill=C["metal_lt"], outline=C["outline"], width=1.3)
        seg(d, x0 + 3, 48, x0 + 13, 48, C["metal_dk"], 1.1)
        seg(d, x0 + 3, 56, x0 + 13, 56, C["metal_dk"], 1.1)
        seg(d, x0 + 3, 44.5, x0 + 13, 44.5, C["cyan_dk"], 1.0)
    rrect(d, 52, 58, 76, 86, 3.0, fill=C["metal_dk"], outline=C["outline"], width=1.4)
    cm, cd = new_mask(img)
    cd.ellipse(B(56, 64, 72, 80), fill=255)
    add_glow(img, cm, C["cyan"], 3.0, 175)
    ell(d, 64, 72, 8.0, 8.0, fill=C["cyan_dk"], outline=C["outline"], width=1.4)
    grad_fill(img, cm, C["cyan_dk"], C["cyan_lt"], direction=(1.0, -1.0))
    ell(d, 64, 72, 8.0, 8.0, fill=None, outline=C["outline"], width=1.4)
    ell(d, 64, 72, 3.4, 3.4, fill=C["glow"])
    seg(d, 54, 84, 74, 84, C["cyan"], 1.1)
    for x0 in (36, 80):
        rrect(d, x0, 60, x0 + 12, 78, 2.0, fill=C["metal"], outline=C["outline"], width=1.2)
        seg(d, x0, 66, x0 + 12, 66, C["outline"], 1.0)
        ell(d, x0 + 6, 63, 1.6, 1.6, fill=C["cyan"])
    for x0 in (40, 72):
        rrect(d, x0, 88, x0 + 16, 102, 2.2, fill=C["metal_dk"], outline=C["outline"], width=1.2)
        rect(d, x0 + 2, 90, x0 + 14, 93, fill=C["metal_lt"], outline=C["outline"], width=1.0)
    rrect(d, 38, 102, 90, 106, 1.6, fill=C["cyan_dk"], outline=C["outline"], width=1.1)
    seg(d, 42, 104, 86, 104, C["cyan"], 1.0)
    return img

def mk_vest_worn_north():
    img, d = _vest_body_shape(VEST_SIL)
    # 背面: 领口包边 + 中缝 + X 型束带 + 菱形能量徽记（north = 背对镜头）
    poly(d, [(54, 42), (57.5, 52), (70.5, 52), (74, 42)], fill=None, outline=C["cyan"], width=1.3)
    rrect(d, 50, 56, 78, 92, 3.0, fill=C["metal"], outline=C["outline"], width=1.4)
    seg(d, 64, 44, 64, 56, C["metal_lt"], 2.0)
    seg(d, 52, 58, 76, 90, C["metal_dk"], 2.4)
    seg(d, 76, 58, 52, 90, C["metal_dk"], 2.4)
    cm, cd = new_mask(img)
    cd.polygon(LY([(64, 64), (73, 74), (64, 84), (55, 74)]), fill=255)
    add_glow(img, cm, C["cyan"], 3.0, 165)
    poly(d, [(64, 64), (73, 74), (64, 84), (55, 74)], fill=C["cyan_dk"], outline=C["outline"], width=1.3)
    poly(d, [(64, 68), (69.5, 74), (64, 80), (58.5, 74)], fill=C["glow"])
    for x0 in (36, 80):
        rrect(d, x0, 60, x0 + 12, 78, 2.0, fill=C["metal"], outline=C["outline"], width=1.2)
        seg(d, x0, 66, x0 + 12, 66, C["outline"], 1.0)
    for x0 in (40, 72):
        rrect(d, x0, 88, x0 + 16, 102, 2.2, fill=C["metal_dk"], outline=C["outline"], width=1.2)
        rect(d, x0 + 2, 90, x0 + 14, 93, fill=C["metal_lt"], outline=C["outline"], width=1.0)
    rrect(d, 38, 102, 90, 106, 1.6, fill=C["cyan_dk"], outline=C["outline"], width=1.1)
    seg(d, 42, 104, 86, 104, C["cyan"], 1.0)
    return img

def mk_vest_worn_east():
    img, d = _vest_body_shape(VEST_SIDE)
    # 侧视: 肩带 + 背带扣 + 前襟能量条 + 侧袋（east = 面向 +x，正面在右）
    rrect(d, 52, 46, 70, 60, 2.4, fill=C["metal_lt"], outline=C["outline"], width=1.3)
    seg(d, 55, 49, 67, 49, C["metal_dk"], 1.1)
    seg(d, 52.5, 46.5, 69.5, 46.5, C["cyan_dk"], 1.0)
    seg(d, 64, 44, 64, 56, C["metal_dk"], 1.2)
    cm, cd = new_mask(img)
    cd.rounded_rectangle(B(76, 62, 81, 78), radius=1.8 * SS, fill=255)
    add_glow(img, cm, C["cyan"], 2.6, 175)
    rrect(d, 76, 62, 81, 78, 1.8, fill=C["cyan_dk"], outline=C["outline"], width=1.1)
    seg(d, 78.5, 64, 78.5, 76, C["glow"], 1.0)
    rrect(d, 70, 58, 84, 88, 3.0, fill=C["metal"], outline=C["outline"], width=1.3)
    seg(d, 70, 66, 84, 66, C["outline"], 1.0)
    rrect(d, 46, 66, 60, 86, 2.2, fill=C["metal_dk"], outline=C["outline"], width=1.2)
    seg(d, 46, 76, 60, 76, C["outline"], 1.0)
    ell(d, 53, 70, 1.6, 1.6, fill=C["cyan"])
    rrect(d, 44, 100, 86, 104, 1.6, fill=C["cyan_dk"], outline=C["outline"], width=1.1)
    seg(d, 48, 102, 82, 102, C["cyan"], 1.0)
    return img

def mk_vest_worn_west():
    return mk_vest_worn_east().transpose(Image.FLIP_LEFT_RIGHT)

# ─────────────────────────── 素材 6: 测试合金（材料，64x64）───────────────────────────

def _ingot(d, x, y, w=32.0, h=13.0, dx=7.0, dy=5.0):
    top = [(x, y), (x + dx, y - dy), (x + w + dx, y - dy), (x + w, y)]
    right = [(x + w, y), (x + w + dx, y - dy), (x + w + dx, y - dy + h), (x + w, y + h)]
    front = [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
    poly(d, top, fill=C["metal_lt"], outline=C["outline"], width=1.1)
    poly(d, right, fill=C["metal_dk"], outline=C["outline"], width=1.1)
    poly(d, front, fill=C["metal"], outline=C["outline"], width=1.1)
    seg(d, x + 3, y + 3.2, x + w - 3, y + 3.2, C["metal_lt"], 1.2)
    seg(d, x + dx, y - dy + 1.6, x + w + dx - 2, y - dy + 1.6, C["cyan"], 1.0)

def mk_alloy():
    img = new_canvas(64, 64)
    d = ImageDraw.Draw(img)
    _ingot(d, 6.0, 44.0)
    _ingot(d, 26.0, 44.0)
    _ingot(d, 16.0, 26.0)
    # 顶部一块的能量高光
    m, md = new_mask(img)
    md.polygon(LY([(16, 21), (23, 16), (55, 16), (48, 21)]), fill=255)
    add_glow(img, m, C["cyan"], 2.4, 110)
    return img

# ─────────────────────────── 素材 7: 测试工作台（建筑，128x128 俯视）───────────────────────────

def mk_bench():
    img = new_canvas(128, 128)
    d = ImageDraw.Draw(img)
    # 桌腿（俯视下沿可见的四角）
    for (x, y) in ((16, 100), (104, 100), (16, 36), (104, 36)):
        rect(d, x - 4, y - 4, x + 4, y + 4, fill=C["metal_dk"], outline=C["outline"], width=1.2)
    # 台面
    rrect(d, 12, 22, 116, 108, 6.0, fill=None, outline=C["outline"], width=2.0)
    tm, td = new_mask(img)
    td.rounded_rectangle(B(12, 22, 116, 108), radius=6.0 * SS, fill=255)
    grad_fill(img, tm, C["metal"], C["metal_dk"], direction=(0.0, 1.0))
    rrect(d, 12, 22, 116, 108, 6.0, fill=None, outline=C["outline"], width=2.0)
    # 台面内嵌金属板
    rrect(d, 18, 28, 110, 102, 4.0, fill=None, outline=C["metal_dk"], width=1.6)
    # 中央能量加工槽
    em, ed = new_mask(img)
    ed.rounded_rectangle(B(28, 46, 96, 76), radius=4.0 * SS, fill=255)
    add_glow(img, em, C["cyan"], 4.0, 150)
    rrect(d, 28, 46, 96, 76, 4.0, fill=C["cyan_dk"], outline=C["outline"], width=1.8)
    grad_fill(img, em, C["cyan_dk"], C["cyan"], direction=(1.0, 0.0))
    rrect(d, 28, 46, 96, 76, 4.0, fill=None, outline=C["outline"], width=1.8)
    for x in (45.0, 62.0, 79.0):
        seg(d, x, 47.5, x, 74.5, C["outline"], 1.4)
    rrect(d, 32, 57, 92, 65, 2.0, fill=C["glow"])
    # 左侧夹具
    rrect(d, 20, 84, 46, 98, 3.0, fill=C["metal"], outline=C["outline"], width=1.6)
    seg(d, 24, 91, 42, 91, C["metal_dk"], 1.4)
    rrect(d, 48, 84, 66, 98, 3.0, fill=C["metal_dk"], outline=C["outline"], width=1.6)
    # 右侧工具/锯片
    rrect(d, 78, 84, 108, 98, 3.0, fill=C["metal"], outline=C["outline"], width=1.6)
    ell(d, 93, 91, 5.4, 5.4, fill=C["metal_lt"], outline=C["outline"], width=1.2)
    ell(d, 93, 91, 1.8, 1.8, fill=C["outline"])
    # 右上角控制面板
    rrect(d, 82, 28, 108, 42, 2.6, fill=C["metal_dk"], outline=C["outline"], width=1.5)
    pm, pd = new_mask(img)
    pd.rounded_rectangle(B(86, 31, 104, 39), radius=1.6 * SS, fill=255)
    add_glow(img, pm, C["cyan"], 2.4, 170)
    rrect(d, 86, 31, 104, 39, 1.6, fill=C["cyan_dk"], outline=C["outline"], width=1.1)
    seg(d, 88, 35, 95, 35, C["cyan_lt"], 1.3)
    seg(d, 88, 37, 101, 37, C["cyan"], 1.0)
    ell(d, 100, 33.5, 1.6, 1.6, fill=C["glow"])
    return img

# ─────────────────────────── 素材 8: 测试花（植物，64x64）───────────────────────────

def mk_bloom():
    img = new_canvas(64, 64)
    d = ImageDraw.Draw(img)
    ground = Image.new("L", img.size, 0)
    gd = ImageDraw.Draw(ground)
    gd.ellipse(B(20, 54, 44, 60), fill=90)
    add_glow(img, ground, C["outline"], 2.0, 90)
    # 叶片
    poly(d, [(30, 56), (16, 42), (26, 38), (34, 52)], fill=C["leaf"], outline=C["outline"], width=1.1)
    poly(d, [(34, 56), (48, 44), (54, 50), (38, 58)], fill=C["leaf_lt"], outline=C["outline"], width=1.1)
    poly(d, [(32, 57), (30, 40), (36, 40), (36, 57)], fill=C["leaf"], outline=C["outline"], width=1.0)
    # 三根花茎 + 花冠
    stems = [((32, 56), (18, 26)), ((33, 56), (32, 16)), ((35, 56), (47, 24))]
    for (a, b) in stems:
        seg(d, a[0], a[1], b[0], b[1], C["leaf"], 1.5)
    blooms = [(18, 24, 8.0), (32, 15, 9.0), (47, 22, 8.0)]
    for (cx, cy, r) in blooms:
        fm, fd = new_mask(img)
        fd.ellipse(B(cx - r, cy - r, cx + r, cy + r), fill=255)
        add_glow(img, fm, C["cyan"], 3.2, 150)
    for (cx, cy, r) in blooms:
        for ang in range(0, 360, 45):
            px = cx + (r * 0.62) * math.cos(math.radians(ang))
            py = cy + (r * 0.62) * math.sin(math.radians(ang))
            ell(d, px, py, r * 0.42, r * 0.42, fill=C["cyan_lt"], outline=C["outline"], width=0.9)
        ell(d, cx, cy, r * 0.52, r * 0.52, fill=C["cyan"], outline=C["outline"], width=1.0)
        ell(d, cx, cy, r * 0.24, r * 0.24, fill=C["glow"])
    return img

# ─────────────────────────── 素材 9: mod 预览图（640x360，含 mod 名文字）───────────────────────────

# 字体目录由环境变量推导（不写死盘符）；全都不存在时 resolve_font() 返回 None，退回 Pillow 默认字体
_FONT_DIR = os.path.join(os.environ.get("WINDIR") or os.environ.get("SystemRoot") or "C:/Windows", "Fonts")
FONT_CANDIDATES = [
    os.path.join(_FONT_DIR, _n) for _n in (
        "msyhbd.ttc", "msyh.ttc", "msyhl.ttc", "simhei.ttf", "Dengb.ttf", "Deng.ttf",
        "segoeuib.ttf", "arialbd.ttf", "arial.ttf",
    )
]
CJK_HINTS = ("msyh", "simhei", "deng", "simsun", "noto")

def resolve_font():
    for p in FONT_CANDIDATES:
        if os.path.exists(p):
            return p
    return None

def load_font(path, px):
    if path is None:
        return ImageFont.load_default()
    try:
        return ImageFont.truetype(path, int(round(px * SS)))
    except Exception:
        return ImageFont.load_default()

def mk_preview(font_path):
    W, H = 640, 360
    img = new_canvas(W, H)
    d = ImageDraw.Draw(img)
    # 背景渐变 + 网格
    bgm = Image.new("L", img.size, 255)
    grad_fill(img, bgm, C["bg_dk"], C["bg_lt"], direction=(0.35, 1.0))
    for x in range(0, W + 1, 32):
        seg(d, x, 0, x, H, (26, 42, 58, 255), 0.6)
    for y in range(0, H + 1, 32):
        seg(d, 0, y, W, y, (26, 42, 58, 255), 0.6)
    # 右下角辉光
    gm, gd = new_mask(img)
    gd.ellipse(B(W - 200, H - 150, W + 120, H + 120), fill=255)
    add_glow(img, gm, C["cyan"], 26.0, 70)
    # 外框
    d.rectangle(B(0.8, 0.8, W - 0.8, H - 0.8), outline=(30, 78, 96, 255), width=WD(1.6))

    cjk = font_path is not None and any(k in os.path.basename(font_path).lower() for k in CJK_HINTS)
    title = "完整测试 Mod (Test)" if cjk else "Complete Test Mod (Test)"
    f_title = load_font(font_path, 44)
    f_sub = load_font(font_path, 16)
    f_chip = load_font(font_path, 14)
    f_cap = load_font(font_path, 11)
    f_foot = load_font(font_path, 12)

    d.text(P(36, 30), title, font=f_title, fill=(238, 252, 255, 255), anchor="la")
    rect(d, 36, 92, 196, 95.5, fill=C["cyan"])
    d.text(P(36, 106), "RimWorld 1.7  ·  Demo.RimTestMod  ·  test.rimtestmod",
           font=f_sub, fill=C["metal_lt"], anchor="la")

    chips = [("XML Def 模板路径", "近战/远程/服装/材料/建筑/配方"),
             ("C# ThingComp + Harmony", "Demo.RimTestMod 独立补丁程序集"),
             ("贴图 · 本地化 · PatchOperation", "全部资源原创程序化生成")]
    y = 146.0
    for (head, sub) in chips:
        rrect(d, 34, y, 320, y + 40, 4.0, fill=(14, 24, 36, 255), outline=(34, 74, 92, 255), width=1.4)
        rect(d, 34, y, 38.5, y + 40, fill=C["cyan_dk"])
        d.text(P(46, y + 8), head, font=f_chip, fill=(206, 236, 246, 255), anchor="la")
        d.text(P(46, y + 24), sub, font=f_cap, fill=(126, 152, 170, 255), anchor="la")
        y += 47.0

    # 右侧图标面板：复用三张主素材（按 SS 分辨率直接缩放，保持锐利）
    rrect(d, 348, 30, 606, 322, 6.0, fill=(9, 15, 24, 255), outline=(34, 74, 92, 255), width=1.6)
    icons = [("DM_PlasmaDagger", mk_plasma_dagger()), ("DM_IonRifle", mk_ion_rifle()), ("DM_TestVest", mk_vest_icon())]
    px = 74
    x0 = 366.0
    for (name, ss_img) in icons:
        ic = ss_img.resize((int(px * SS), int(px * SS)), Image.LANCZOS)
        img.alpha_composite(ic, (int(x0 * SS), int(58 * SS)))
        d.text(P(x0 + px / 2.0, 142), name, font=f_cap, fill=(150, 176, 194, 255), anchor="ma")
        x0 += px + 8.0
    seg(d, 366, 160, 588, 160, (34, 74, 92, 255), 1.3)
    d.text(P(366, 172), "12 张原创 PNG 贴图（全部程序化生成）" if cjk else "12 original PNG textures (procedural)",
           font=f_chip, fill=(206, 236, 246, 255), anchor="la")
    tips = ["WeaponMelee / WeaponRanged / Projectile",
            "Apparel 物品图标 + 4 朝向穿戴外观",
            "Resource / Building / Plant / Preview"]
    yy = 200.0
    for t in tips:
        ell(d, 371, yy + 6, 2.2, 2.2, fill=C["cyan"])
        d.text(P(380, yy), t, font=f_cap, fill=(126, 152, 170, 255), anchor="la")
        yy += 26.0
    d.text(P(366, 288), "Coherent 128x128 / 64x64 / 32x32 RGBA" if not cjk else "统一规格 128x128 / 64x64 / 32x32 RGBA",
           font=f_cap, fill=(96, 124, 142, 255), anchor="la")

    footer = "AI 辅助生成  ·  仅用于 rimworld-modding 技能端到端测试" if cjk else "AI-assisted  ·  skill end-to-end test asset"
    d.text(P(36, 332), footer, font=f_foot, fill=(110, 132, 150, 255), anchor="la")
    d.text(P(604, 332), "v0.1", font=f_foot, fill=(110, 132, 150, 255), anchor="ra")
    return img

# ─────────────────────────── 素材注册表（路径 / 尺寸 / texPath 契约）───────────────────────────

SPECS = [
    dict(path="Textures/Things/Item/Equipment/WeaponMelee/DM_PlasmaDagger.png", w=128, h=128,
         maker=mk_plasma_dagger, texpath="Things/Item/Equipment/WeaponMelee/DM_PlasmaDagger",
         method="几何矢量绘制：水平刀身多边形 + 沿刀轴 violet->cyan 线性渐变 + 高斯辉光 + 深色描边，"
                "保持水平（与原版 Gladius 一致，装备旋转交给游戏），按 alpha 包围盒适配 120px 宽、4x 超采样 LANCZOS 缩放",
         defs="DM_Weapon_PlasmaDagger"),
    dict(path="Textures/Things/Item/Equipment/WeaponRanged/DM_IonRifle.png", w=128, h=128,
         maker=mk_ion_rifle, texpath="Things/Item/Equipment/WeaponRanged/DM_IonRifle",
         method="几何矢量绘制：水平枪身圆角矩形组 + 蓝白发光能量槽 + 枪口能量环辉光，"
                "保持水平（与原版 AssaultRifle 一致），适配 124px 宽、4x 超采样 LANCZOS 缩放",
         defs="DM_Weapon_IonRifle"),
    dict(path="Textures/Things/Projectile/DM_IonRifleBullet.png", w=32, h=32,
         maker=mk_ion_bullet, texpath="Things/Projectile/DM_IonRifleBullet",
         method="胶囊多边形弹体（弹头朝 +x，供 drawRotated 旋转）+ blue->glow 线性渐变 + 大半径高斯辉光",
         defs="DM_Projectile_IonRifle"),
    dict(path="Textures/Things/Item/Equipment/Apparel/DM_TestVest.png", w=128, h=128,
         maker=mk_vest_icon, texpath="Things/Item/Equipment/Apparel/DM_TestVest",
         method="几何矢量绘制：背心正面轮廓多边形 + 肩带/胸板/腰袋/束带 + 中央青蓝能量核心（径向辉光）",
         defs="DM_Apparel_TestVest（物品图标）"),
    dict(path="Textures/Things/Pawn/Humanlike/Apparel/DM_TestVest/DM_TestVest_south.png", w=128, h=128,
         maker=mk_vest_worn_south, texpath="Things/Pawn/Humanlike/Apparel/DM_TestVest/DM_TestVest",
         method="穿戴外观（正面）：躯干轮廓按原版实测 x 34..94 / y 42..106 + 领口包边 + 肩带 + 胸口能量核心 + 胸袋腰袋 + 青蓝下摆条",
         defs="DM_Apparel_TestVest（穿戴，south）"),
    dict(path="Textures/Things/Pawn/Humanlike/Apparel/DM_TestVest/DM_TestVest_north.png", w=128, h=128,
         maker=mk_vest_worn_north, texpath="Things/Pawn/Humanlike/Apparel/DM_TestVest/DM_TestVest",
         method="穿戴外观（背面）：同款轮廓 + 背甲平板 + 中缝 + X 型束带 + 菱形能量徽记 + 背袋",
         defs="DM_Apparel_TestVest（穿戴，north）"),
    dict(path="Textures/Things/Pawn/Humanlike/Apparel/DM_TestVest/DM_TestVest_east.png", w=128, h=128,
         maker=mk_vest_worn_east, texpath="Things/Pawn/Humanlike/Apparel/DM_TestVest/DM_TestVest",
         method="穿戴外观（右侧视）：原版实测侧身轮廓 x 44..86 / y 44..104 + 肩带 + 背带扣 + 前襟能量条 + 侧袋",
         defs="DM_Apparel_TestVest（穿戴，east）"),
    dict(path="Textures/Things/Pawn/Humanlike/Apparel/DM_TestVest/DM_TestVest_west.png", w=128, h=128,
         maker=mk_vest_worn_west, texpath="Things/Pawn/Humanlike/Apparel/DM_TestVest/DM_TestVest",
         method="穿戴外观（左侧视）：east 图的水平镜像（原版同类贴图同样使用镜像）",
         defs="DM_Apparel_TestVest（穿戴，west）"),
    dict(path="Textures/Things/Item/Resource/DM_TestAlloy.png", w=64, h=64,
         maker=mk_alloy, texpath="Things/Item/Resource/DM_TestAlloy",
         method="几何矢量绘制：三块等轴合金锭（顶/正/侧面三色面）+ 顶面青蓝高光",
         defs="DM_Stuff_TestAlloy"),
    dict(path="Textures/Things/Building/Production/DM_TestBench.png", w=128, h=128,
         maker=mk_bench, texpath="Things/Building/Production/DM_TestBench",
         method="几何矢量绘制（俯视）：台面渐变 + 中央能量加工槽（分段+辉光）+ 夹具/锯片 + 四角桌腿 + 控制面板",
         defs="DM_Building_TestBench"),
    dict(path="Textures/Things/Plant/DM_TestBloom.png", w=64, h=64,
         maker=mk_bloom, texpath="Things/Plant/DM_TestBloom",
         method="几何矢量绘制：三茎绿叶 + 三朵八瓣青蓝花（花瓣+花心辉光）+ 根际阴影",
         defs="DM_Plant_TestBloom"),
    dict(path="About/Preview.png", w=640, h=360, maker=None,
         texpath=None, method="合成预览图：深色渐变背景 + 网格 + 青蓝辉光 + 标题文字（含 mod 名）+ 三张主素材缩略图面板",
         defs="Steam/About 预览图（非游戏内贴图）"),
]

# ─────────────────────────── 生成 / 校验 ───────────────────────────

def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def alpha_bbox(im):
    return im.getchannel("A").getbbox()

def generate(root, contact_sheet=None):
    font_path = resolve_font()
    print("[font] " + (font_path if font_path else "!! 未找到可用 TTF，Preview 文字将回退默认字体"))
    ok = True
    made = []
    for spec in SPECS:
        dst = os.path.join(root, spec["path"].replace("/", os.sep))
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        if spec["maker"] is None:
            ss_img = mk_preview(font_path)
        else:
            ss_img = spec["maker"]()
        final = finish(ss_img, spec["w"], spec["h"])
        final.save(dst, format="PNG", optimize=True)
        made.append((spec, dst))
        print("[gen ] " + spec["path"] + "  " + str(spec["w"]) + "x" + str(spec["h"]))
    # 逐张读回校验
    manifest = []
    for (spec, dst) in made:
        im = Image.open(dst)
        im.load()
        size_ok = (im.size == (spec["w"], spec["h"]))
        mode_ok = (im.mode == "RGBA")
        bytes_ = os.path.getsize(dst)
        nonempty = bytes_ > 0
        bb = alpha_bbox(im)
        corner = im.getpixel((0, 0))[3] if im.mode == "RGBA" else 255
        transparent = (corner == 0) or (spec["path"].endswith("Preview.png"))
        has_pixels = bb is not None
        good = size_ok and mode_ok and nonempty and transparent and has_pixels
        ok = ok and good
        print("[" + ("OK  " if good else "FAIL") + "] " + spec["path"].ljust(66)
              + str(im.size[0]) + "x" + str(im.size[1]) + " " + im.mode
              + " " + str(bytes_) + "B  sha256=" + sha256_of(dst)[:16]
              + "  alpha_bbox=" + str(bb))
        manifest.append(dict(
            file=spec["path"],
            width=im.size[0], height=im.size[1], mode=im.mode, bytes=bytes_,
            sha256=sha256_of(dst),
            texPath=spec["texpath"],
            usedBy=spec["defs"],
            method=spec["method"],
        ))
    if contact_sheet:
        _write_contact_sheet(made, contact_sheet)
        print("[sheet] " + contact_sheet)
    return ok, manifest, font_path

def _write_contact_sheet(made, out_path):
    cols = 4
    cell = 156
    rows = (len(made) + cols - 1) // cols
    sheet = Image.new("RGBA", (cols * cell, rows * (cell + 22)), (18, 24, 32, 255))
    sd = ImageDraw.Draw(sheet)
    f = ImageFont.load_default()
    for i, (spec, dst) in enumerate(made):
        im = Image.open(dst).convert("RGBA")
        scale = min((cell - 24) / im.width, (cell - 24) / im.height, 3.0)
        th = im.resize((max(1, int(im.width * scale)), max(1, int(im.height * scale))), Image.NEAREST)
        cx = (i % cols) * cell
        cy = (i // cols) * (cell + 22)
        sd.rectangle([cx, cy, cx + cell - 1, cy + cell + 21], outline=(60, 78, 96, 255))
        sheet.alpha_composite(th, (cx + (cell - th.width) // 2, cy + (cell - th.height) // 2))
        sd.text((cx + 4, cy + cell + 4), os.path.basename(spec["path"]), font=f, fill=(200, 220, 235, 255))
    sheet.convert("RGB").save(out_path)

def verify_only(root):
    print("[verify-only] root=" + root)
    ok = True
    for spec in SPECS:
        dst = os.path.join(root, spec["path"].replace("/", os.sep))
        if not os.path.exists(dst):
            print("[FAIL] 缺失 " + spec["path"])
            ok = False
            continue
        im = Image.open(dst)
        im.load()
        good = (im.size == (spec["w"], spec["h"])) and im.mode == "RGBA" and os.path.getsize(dst) > 0
        ok = ok and good
        print("[" + ("OK  " if good else "FAIL") + "] " + spec["path"].ljust(66)
              + str(im.size[0]) + "x" + str(im.size[1]) + " " + im.mode + " " + str(os.path.getsize(dst)) + "B")
    return ok

def write_manifest(root, manifest, script_path):
    payload = dict(
        mod="rimtest-mod",
        generator="Source/make-textures.py",
        generator_sha256=sha256_of(script_path),
        ai_note="AI 辅助生成；全部图形为原创几何绘制，未使用任何第三方 IP 素材",
        environment=dict(python=sys.version.split()[0], pillow=PILLOW_VERSION, supersample=SS),
        reproducible="无随机源/时间戳/网络；命令: python Source/make-textures.py",
        palette="#38D8E8 青蓝主色 / #A8E4FF 亮青 / #8020E8->128,92,232 紫 / #2B3038-#8A94A2 深灰金属",
        texPath_contract=[
            dict(defName="DM_Weapon_PlasmaDagger", texPath="Things/Item/Equipment/WeaponMelee/DM_PlasmaDagger"),
            dict(defName="DM_Weapon_IonRifle", texPath="Things/Item/Equipment/WeaponRanged/DM_IonRifle"),
            dict(defName="DM_Projectile_IonRifle", texPath="Things/Projectile/DM_IonRifleBullet"),
            dict(defName="DM_Apparel_TestVest", texPath="Things/Item/Equipment/Apparel/DM_TestVest"),
            dict(defName="DM_Apparel_TestVest(worn)", texPath="Things/Pawn/Humanlike/Apparel/DM_TestVest/DM_TestVest"),
            dict(defName="DM_Stuff_TestAlloy", texPath="Things/Item/Resource/DM_TestAlloy"),
            dict(defName="DM_Building_TestBench", texPath="Things/Building/Production/DM_TestBench"),
            dict(defName="DM_Plant_TestBloom", texPath="Things/Plant/DM_TestBloom"),
        ],
        files=manifest,
    )
    dst = os.path.join(root, "Textures", "_MANIFEST.json")
    with open(dst, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
        f.write(chr(10))
    print("[manifest] " + dst)
    return dst

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=None)
    ap.add_argument("--verify-only", action="store_true")
    ap.add_argument("--contact-sheet", default=None)
    args = ap.parse_args()
    script_path = os.path.abspath(__file__)
    root = args.out or os.path.dirname(os.path.dirname(script_path))
    if args.verify_only:
        sys.exit(0 if verify_only(root) else 1)
    ok, manifest, font_path = generate(root, args.contact_sheet)
    write_manifest(root, manifest, script_path)
    print("[summary] " + str(len(manifest)) + " 张; 校验" + ("全部通过" if ok else "存在失败"))
    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
