"""Pilot A: sinh 12 icon bằng OpenAI và Google với CÙNG prompt. Chạy self-check: python3 -I gen.py --selfcheck
Mặc định chỉ LIỆT KÊ lệnh gọi. Gọi thật (tốn tiền): python3 gen.py --go [--vendor openai|google]
Khoá lấy từ biến môi trường OPENAI_API_KEY / GEMINI_API_KEY; script không in và không ghi khoá.
Ảnh thô -> out/raw/<vendor>/<tên>.png ; đã hậu xử lý -> out/icons/<vendor>/<tên>.png (64x64).
CHƯA KIỂM THỬ với API thật: tên mô hình Google và dạng phản hồi cần xác nhận ở lần chạy đầu.
"""
import argparse, base64, json, os, sys, urllib.request
from pathlib import Path

HERE = Path(__file__).parent
STYLE = ("Single game item icon, pixel art style, bold clean outline, limited palette of jade green, "
         "gold, mist white and lantern red, xianxia cultivation theme, centered, no text, "
         "on a flat solid pure magenta (#FF00FF) background, no shadow on the background.")
ICONS = {  # tên -> mô tả (4 vật liệu, 4 trang bị, 4 tiêu hao; xem docs/content/content.md)
    "mat_beast_fang": "a sharp white beast fang",
    "mat_spirit_herb": "a glowing green spirit herb",
    "mat_ice_scale": "a pale blue ice-fish scale",
    "mat_fire_core": "a small burning red crystal core",
    "gear_sword": "a straight jade-guard cultivator sword",
    "gear_robe": "a folded cultivator robe in teal and gold",
    "gear_bow": "a recurve bow with a jade inlay",
    "gear_talisman": "a yellow paper talisman with red seal marks",
    "use_meal": "a bowl of spirit rice with steam",
    "use_bandage_salve": "a small clay jar of healing salve with a cloth wrap",
    "use_tea": "a small teacup with a green tea leaf",
    "use_pill": "a round golden elixir pill on a tiny dish",
}
MODELS = {"openai": os.environ.get("PILOT_OPENAI_MODEL", "gpt-image-2"),
          "google": os.environ.get("PILOT_GOOGLE_MODEL", "gemini-2.5-flash-image")}


def prompt(desc):
    return f"{desc}. {STYLE}"


def gen_openai(p):
    from openai import OpenAI
    r = OpenAI().images.generate(model=MODELS["openai"], prompt=p, size="1024x1024", quality="medium")
    return base64.b64decode(r.data[0].b64_json)


def gen_google(p):
    key = os.environ["GEMINI_API_KEY"]
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODELS['google']}:generateContent"
    req = urllib.request.Request(url, data=json.dumps({"contents": [{"parts": [{"text": p}]}]}).encode(),
                                 headers={"x-goog-api-key": key, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=180) as f:
        d = json.load(f)
    for part in d["candidates"][0]["content"]["parts"]:
        blob = part.get("inlineData") or part.get("inline_data")
        if blob:
            return base64.b64decode(blob["data"])
    raise RuntimeError("phản hồi không có ảnh: " + json.dumps(d)[:300])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--go", action="store_true")
    ap.add_argument("--vendor", choices=["openai", "google"])
    ap.add_argument("--selfcheck", action="store_true")
    a = ap.parse_args()
    if a.selfcheck:
        assert len(ICONS) == 12 and len(set(ICONS)) == 12
        assert all("#FF00FF" in prompt(d) for d in ICONS.values())
        print("OK: gen self-check (12 prompt, cùng phong cách, nền chroma)")
        return
    vendors = [a.vendor] if a.vendor else ["openai", "google"]
    print(f"{'GỌI THẬT' if a.go else 'DRY-RUN (thêm --go để gọi)'}: {len(vendors) * len(ICONS)} ảnh; mô hình {({v: MODELS[v] for v in vendors})}")
    sys.path.insert(0, str(HERE))
    from postprocess import process
    from PIL import Image
    for v in vendors:
        for name, desc in ICONS.items():
            raw, icon = HERE / "out/raw" / v / f"{name}.png", HERE / "out/icons" / v / f"{name}.png"
            if not a.go:
                print(f"  {v}/{name}: {prompt(desc)[:70]}...")
                continue
            if raw.exists():
                continue
            raw.parent.mkdir(parents=True, exist_ok=True); icon.parent.mkdir(parents=True, exist_ok=True)
            raw.write_bytes((gen_openai if v == "openai" else gen_google)(prompt(desc)))
            process(Image.open(raw), 64).save(icon)
            print(f"  ok {v}/{name}")


if __name__ == "__main__":
    main()
