"""Hậu xử lý ảnh AI -> icon pixel art (pilot). Cần Pillow. Chạy self-check: python3 -I postprocess.py
Dùng:  python3 -I postprocess.py in.png out.png [kích_thước=64]
Quy trình: tách nền chroma (#FF00FF) -> cắt khít -> đặt vào ô vuông -> hạ cỡ BOX -> ép về bảng màu.
Bảng màu dưới đây là bản tạm cho pilot; họa sĩ chốt bảng thật ở Phase 0 (ADR art).
"""
import sys
from PIL import Image

KEY = (255, 0, 255)
TOL = 90  # khoảng cách RGB tối đa coi là nền
PALETTE = [  # ngọc, vàng kim, trắng sương, đỏ đèn lồng, nâu, tối
    "#0b1f1a", "#16453a", "#1f6b57", "#2f9a7d", "#6fcfb0", "#c9f2e2",
    "#3b2a14", "#7a5a22", "#c89b3c", "#f2d27a", "#fff3c4",
    "#5e1414", "#a82a2a", "#e0533f", "#f4f7f5", "#a9b8b3", "#5b6b66",
]
PAL = [tuple(int(h[i:i + 2], 16) for i in (1, 3, 5)) for h in PALETTE]


def nearest(rgb):
    return min(PAL, key=lambda p: sum((a - b) ** 2 for a, b in zip(p, rgb)))


def process(img, size=64):
    img = img.convert("RGBA")
    px = img.load()
    for y in range(img.height):
        for x in range(img.width):
            r, g, b, _ = px[x, y]
            if sum((a - k) ** 2 for a, k in zip((r, g, b), KEY)) ** 0.5 <= TOL:
                px[x, y] = (0, 0, 0, 0)
    box = img.getbbox()
    if box is None:
        raise ValueError("ảnh trống sau khi tách nền")
    img = img.crop(box)
    side = max(img.size)
    canvas = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    canvas.paste(img, ((side - img.width) // 2, (side - img.height) // 2))
    small = canvas.resize((size, size), Image.BOX)
    out = small.load()
    for y in range(size):
        for x in range(size):
            r, g, b, a = out[x, y]
            out[x, y] = (*nearest((r, g, b)), 255) if a >= 128 else (0, 0, 0, 0)
    return small


def _selfcheck():
    src = Image.new("RGB", (512, 512), KEY)
    p = src.load()
    for y in range(512):
        for x in range(512):
            if (x - 256) ** 2 + (y - 256) ** 2 < 150 ** 2:
                p[x, y] = (200, 40, 40)
    out = process(src, 32)
    assert out.size == (32, 32)
    assert out.getpixel((0, 0))[3] == 0, "góc phải trong suốt"
    c = out.getpixel((16, 16))
    assert c[3] == 255 and c[:3] in PAL, "tâm đục và nằm trong bảng màu"
    assert all(q[:3] in PAL for q in out.getdata() if q[3] == 255), "mọi pixel đục thuộc bảng màu"
    print("OK: postprocess self-check")


if __name__ == "__main__":
    if len(sys.argv) >= 3:
        process(Image.open(sys.argv[1]), int(sys.argv[3]) if len(sys.argv) > 3 else 64).save(sys.argv[2])
    else:
        _selfcheck()
