
"""
Pilot A: Sinh 12 icon bằng OpenAI và Google với CÙNG prompt.

Kiểm tra:
    python3 -I gen.py --selfcheck

Dry-run:
    python3 gen.py
    python3 gen.py --vendor google

Gọi API thật (tốn tiền):
    python3 gen.py --go --vendor google
    python3 gen.py --go --vendor openai
    python3 gen.py --go

Tùy chỉnh:
    python3 gen.py --go --vendor google --delay 30 --retries 5

API keys:
    OPENAI_API_KEY
    GEMINI_API_KEY

Có thể đặt trong tools/pilot/.env.
Script không in hoặc ghi API key.

Đầu ra:
    out/raw/<vendor>/<name>.png
    out/icons/<vendor>/<name>.png

Tính năng:
    - Retry khi gặp HTTP 429, 500, 502, 503, 504
    - Đọc Retry-After / retryDelay
    - Phát hiện quota limit = 0
    - Delay giữa các API requests
    - Resume không tạo lại ảnh đã có
    - Hậu xử lý raw thành icon 64x64
    - Ghi file ảnh an toàn bằng file tạm
    - Self-check không gọi API

Lưu ý:
    Quota Google phụ thuộc project và billing tier.
    Retry không khắc phục được quota bằng 0 hoặc hết quota ngày.
"""

import argparse
import base64
import json
import os
import random
import re
import sys
import time
import urllib.error
import urllib.request

from pathlib import Path


# ============================================================
# CONFIG
# ============================================================

HERE = Path(__file__).resolve().parent

STYLE = (
    "Single game item icon, pixel art style, "
    "bold clean outline, limited palette of jade green, "
    "gold, mist white and lantern red, "
    "xianxia cultivation theme, centered, no text, "
    "on a flat solid pure magenta (#FF00FF) background, "
    "no shadow on the background."
)

ICONS = {
    # Materials
    "mat_beast_fang": "a sharp white beast fang",
    "mat_spirit_herb": "a glowing green spirit herb",
    "mat_ice_scale": "a pale blue ice-fish scale",
    "mat_fire_core": "a small burning red crystal core",

    # Equipment
    "gear_sword": "a straight jade-guard cultivator sword",
    "gear_robe": "a folded cultivator robe in teal and gold",
    "gear_bow": "a recurve bow with a jade inlay",
    "gear_talisman": "a yellow paper talisman with red seal marks",

    # Consumables
    "use_meal": "a bowl of spirit rice with steam",
    "use_bandage_salve": (
        "a small clay jar of healing salve with a cloth wrap"
    ),
    "use_tea": "a small teacup with a green tea leaf",
    "use_pill": "a round golden elixir pill on a tiny dish",
}

MODELS = {
    "openai": os.environ.get(
        "PILOT_OPENAI_MODEL",
        "gpt-image-2",
    ),
    "google": os.environ.get(
        "PILOT_GOOGLE_MODEL",
        "gemini-2.5-flash-image",
    ),
}

RETRYABLE_HTTP = {429, 500, 502, 503, 504}


# ============================================================
# ENVIRONMENT
# ============================================================

def load_env():
    """
    Đọc tools/pilot/.env.

    Biến môi trường đã tồn tại được ưu tiên.
    Không in API key.
    """
    env_file = HERE / ".env"

    if not env_file.exists():
        return

    for line in env_file.read_text(
        encoding="utf-8"
    ).splitlines():

        line = line.strip()

        if not line or line.startswith("#"):
            continue

        key, sep, value = line.partition("=")

        if not sep:
            continue

        key = key.strip()
        value = value.strip().strip('"').strip("'")

        if key:
            os.environ.setdefault(key, value)


def prompt(description):
    return f"{description}. {STYLE}"


# ============================================================
# HTTP ERROR HANDLING
# ============================================================

def get_retry_delay(error, body, attempt):
    """
    Ưu tiên:
        1. HTTP Retry-After (số giây)
        2. Google retryDelay
        3. Exponential backoff
    """

    retry_after = error.headers.get("Retry-After")

    if retry_after:
        try:
            return max(
                0,
                float(retry_after),
            ) + random.uniform(0, 3)
        except ValueError:
            pass

    try:
        data = json.loads(body)

        details = (
            data.get("error", {})
            .get("details", [])
        )

        for detail in details:
            retry_delay = detail.get("retryDelay")

            if retry_delay:
                match = re.fullmatch(
                    r"(\d+(?:\.\d+)?)s",
                    retry_delay,
                )

                if match:
                    return (
                        float(match.group(1))
                        + random.uniform(0, 3)
                    )

    except (ValueError, TypeError, AttributeError):
        pass

    return min(
        120,
        10 * (2 ** attempt),
    ) + random.uniform(0, 3)


def is_zero_quota(body):
    """
    Phát hiện quota limit = 0 trong phản hồi Google.
    """

    try:
        data = json.loads(body)

        details = (
            data.get("error", {})
            .get("details", [])
        )

        for detail in details:
            for violation in detail.get(
                "violations", []
            ):
                if violation.get("quotaValue") == "0":
                    return True

    except (ValueError, TypeError, AttributeError):
        pass

    return bool(
        re.search(
            r"limit:\s*0(?:\D|$)",
            body,
            re.IGNORECASE,
        )
    )


def request_json(req, retries=5):
    """
    HTTP request với retry.

    Không retry các lỗi HTTP không nằm trong
    RETRYABLE_HTTP.

    Không retry quota limit = 0.
    """

    for attempt in range(retries + 1):

        try:
            with urllib.request.urlopen(
                req,
                timeout=180,
            ) as response:

                return json.load(response)

        except urllib.error.HTTPError as error:

            body = error.read().decode(
                "utf-8",
                errors="replace",
            )

            print(
                f"\n[HTTP {error.code}] API request failed",
                file=sys.stderr,
            )

            # Chỉ hiển thị thông tin lỗi có cấu trúc,
            # tránh in URL/request headers chứa khóa.
            try:
                parsed = json.loads(body)
                api_error = parsed.get("error", {})

                print(
                    json.dumps(
                        api_error,
                        ensure_ascii=False,
                        indent=2,
                    )[:3000],
                    file=sys.stderr,
                )

            except ValueError:
                print(
                    "API trả về lỗi không phải JSON.",
                    file=sys.stderr,
                )

            if error.code not in RETRYABLE_HTTP:
                raise RuntimeError(
                    f"API HTTP {error.code}"
                ) from error

            if error.code == 429 and is_zero_quota(body):
                raise RuntimeError(
                    "Google API quota limit = 0. "
                    "Kiểm tra billing, project và model quota."
                ) from error

            if attempt >= retries:
                raise RuntimeError(
                    f"API HTTP {error.code}: "
                    f"đã retry {retries} lần."
                ) from error

            delay = get_retry_delay(
                error,
                body,
                attempt,
            )

            print(
                f"[RETRY] Đợi {delay:.1f}s "
                f"({attempt + 1}/{retries})",
                flush=True,
            )

            time.sleep(delay)

        except (
            urllib.error.URLError,
            TimeoutError,
        ) as error:

            if attempt >= retries:
                raise RuntimeError(
                    "Lỗi kết nối API sau nhiều lần retry."
                ) from error

            delay = min(
                120,
                10 * (2 ** attempt),
            ) + random.uniform(0, 3)

            print(
                f"[NETWORK] Retry sau {delay:.1f}s"
            )

            time.sleep(delay)

    raise RuntimeError("API request failed")


# ============================================================
# OPENAI IMAGE GENERATION
# ============================================================

def gen_openai(p, retries=5):

    from openai import OpenAI

    client = OpenAI(
        max_retries=retries,
    )

    result = client.images.generate(
        model=MODELS["openai"],
        prompt=p,
        size="1024x1024",
        quality="medium",
    )

    if not result.data:
        raise RuntimeError(
            "OpenAI không trả về dữ liệu ảnh."
        )

    image_data = result.data[0].b64_json

    if not image_data:
        raise RuntimeError(
            "OpenAI không trả về b64_json."
        )

    return base64.b64decode(
        image_data,
        validate=True,
    )


# ============================================================
# GOOGLE GEMINI IMAGE GENERATION
# ============================================================

def gen_google(p, retries=5):

    key = os.environ["GEMINI_API_KEY"]

    model = MODELS["google"]

    url = (
        "https://generativelanguage.googleapis.com/"
        f"v1beta/models/{model}:generateContent"
    )

    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": p,
                    }
                ]
            }
        ],
        "generationConfig": {
            "responseModalities": [
                "IMAGE",
            ],
        },
    }

    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode(
            "utf-8"
        ),
        headers={
            "x-goog-api-key": key,
            "Content-Type": "application/json",
        },
        method="POST",
    )

    response = request_json(
        request,
        retries=retries,
    )

    candidates = response.get(
        "candidates",
        [],
    )

    for candidate in candidates:

        content = candidate.get(
            "content",
            {},
        )

        for part in content.get(
            "parts",
            [],
        ):

            blob = (
                part.get("inlineData")
                or part.get("inline_data")
            )

            if blob and blob.get("data"):

                return base64.b64decode(
                    blob["data"],
                    validate=True,
                )

    raise RuntimeError(
        "Google trả về thành công nhưng không có ảnh. "
        "Response: "
        + json.dumps(
            response,
            ensure_ascii=False,
        )[:1000]
    )


# ============================================================
# FILE HANDLING
# ============================================================

def save_raw_image(data, path):
    """
    Xác thực dữ liệu ảnh rồi lưu PNG.

    Dùng file tạm để tránh để lại ảnh hỏng
    nếu quá trình ghi bị gián đoạn.
    """

    from PIL import Image
    from io import BytesIO

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with Image.open(BytesIO(data)) as image:
        image.load()
        image = image.convert("RGBA")

        temp_path = path.with_suffix(
            ".tmp.png"
        )

        try:
            image.save(
                temp_path,
                format="PNG",
            )

            temp_path.replace(path)

        finally:
            temp_path.unlink(
                missing_ok=True,
            )


def create_icon(raw_path, icon_path):
    """
    Hậu xử lý ảnh thành icon 64x64.
    """

    from PIL import Image
    from postprocess import process

    icon_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    temp_path = icon_path.with_suffix(
        ".tmp.png"
    )

    try:
        with Image.open(raw_path) as image:

            image.load()

            result = process(
                image,
                64,
            )

            result.save(
                temp_path,
                format="PNG",
            )

        temp_path.replace(icon_path)

    finally:
        temp_path.unlink(
            missing_ok=True,
        )


# ============================================================
# SELF CHECK
# ============================================================

def selfcheck():

    assert len(ICONS) == 12

    assert len(set(ICONS)) == 12

    assert all(
        "#FF00FF" in prompt(description)
        for description in ICONS.values()
    )

    assert len(
        [k for k in ICONS if k.startswith("mat_")]
    ) == 4

    assert len(
        [k for k in ICONS if k.startswith("gear_")]
    ) == 4

    assert len(
        [k for k in ICONS if k.startswith("use_")]
    ) == 4

    assert is_zero_quota(
        '{"error":{"message":"limit: 0"}}'
    )

    assert not is_zero_quota(
        '{"error":{"message":"limit: 10"}}'
    )

    print(
        "OK: gen self-check "
        "(12 prompts, 4+4+4, chroma background, "
        "quota detection)"
    )


# ============================================================
# MAIN
# ============================================================

def main():

    parser = argparse.ArgumentParser(
        description="Pilot A - Xianxia icon generation"
    )

    parser.add_argument(
        "--go",
        action="store_true",
        help="Gọi API thật (tốn tiền)",
    )

    parser.add_argument(
        "--vendor",
        choices=[
            "openai",
            "google",
        ],
        help="Chọn API provider",
    )

    parser.add_argument(
        "--selfcheck",
        action="store_true",
        help="Kiểm tra script không gọi API",
    )

    parser.add_argument(
        "--delay",
        type=float,
        default=20.0,
        help="Delay giữa các request, mặc định 20s",
    )

    parser.add_argument(
        "--retries",
        type=int,
        default=5,
        help="Số lần retry tối đa, mặc định 5",
    )

    args = parser.parse_args()

    if args.selfcheck:
        selfcheck()
        return

    if args.delay < 0:
        parser.error("--delay phải >= 0")

    if args.retries < 0:
        parser.error("--retries phải >= 0")

    load_env()

    vendors = (
        [args.vendor]
        if args.vendor
        else ["openai", "google"]
    )

    required_keys = {
        "openai": "OPENAI_API_KEY",
        "google": "GEMINI_API_KEY",
    }

    if args.go:

        missing = [
            required_keys[v]
            for v in vendors
            if not os.environ.get(
                required_keys[v]
            )
        ]

        if missing:
            sys.exit(
                "Thiếu API key: "
                + ", ".join(missing)
                + ". Hãy đặt trong tools/pilot/.env "
                "hoặc biến môi trường."
            )

    print(
        f"{'GỌI THẬT' if args.go else 'DRY-RUN'}: "
        f"{len(vendors) * len(ICONS)} ảnh; "
        f"mô hình "
        f"{ {v: MODELS[v] for v in vendors} }",
        flush=True,
    )

    if args.go:
        print(
            f"Delay: {args.delay}s | "
            f"Retries: {args.retries}",
            flush=True,
        )

    for vendor in vendors:

        generator = (
            gen_openai
            if vendor == "openai"
            else gen_google
        )

        last_request_time = None

        for index, (name, description) in enumerate(
            ICONS.items(),
            start=1,
        ):

            raw_path = (
                HERE
                / "out"
                / "raw"
                / vendor
                / f"{name}.png"
            )

            icon_path = (
                HERE
                / "out"
                / "icons"
                / vendor
                / f"{name}.png"
            )

            if not args.go:

                print(
                    f"  [{index:02d}/12] "
                    f"{vendor}/{name}: "
                    f"{prompt(description)[:70]}..."
                )

                continue

            # Icon đã có thì bỏ qua.
            if icon_path.exists():

                print(
                    f"  [{index:02d}/12] "
                    f"SKIP {vendor}/{name}: "
                    "icon đã tồn tại",
                    flush=True,
                )

                continue

            # Chỉ gọi API nếu chưa có raw.
            if not raw_path.exists():

                # Delay giữa các lần gọi API,
                # không delay khi chỉ hậu xử lý.
                if last_request_time is not None:

                    elapsed = (
                        time.monotonic()
                        - last_request_time
                    )

                    remaining = (
                        args.delay - elapsed
                    )

                    if remaining > 0:

                        print(
                            f"  Đợi {remaining:.1f}s...",
                            flush=True,
                        )

                        time.sleep(remaining)

                print(
                    f"  [{index:02d}/12] "
                    f"GEN {vendor}/{name}",
                    flush=True,
                )

                # Ghi nhận trước khi gọi, kể cả
                # request thất bại.
                last_request_time = time.monotonic()

                try:
                    data = generator(
                        prompt(description),
                        retries=args.retries,
                    )

                    save_raw_image(
                        data,
                        raw_path,
                    )

                except Exception as error:

                    print(
                        f"\n[FAILED] "
                        f"{vendor}/{name}: "
                        f"{error}",
                        file=sys.stderr,
                        flush=True,
                    )

                    print(
                        "Dừng để tránh gọi API "
                        "liên tục khi quota bị giới hạn.",
                        file=sys.stderr,
                    )

                    raise SystemExit(1) from error

            else:

                print(
                    f"  [{index:02d}/12] "
                    f"RAW EXISTS {vendor}/{name}",
                    flush=True,
                )

            # Hậu xử lý.
            try:

                create_icon(
                    raw_path,
                    icon_path,
                )

            except Exception as error:

                print(
                    f"[POSTPROCESS FAILED] "
                    f"{vendor}/{name}: {error}",
                    file=sys.stderr,
                )

                raise SystemExit(1) from error

            print(
                f"  [{index:02d}/12] "
                f"OK {vendor}/{name}",
                flush=True,
            )

    print(
        "\nHoàn tất. "
        "Các ảnh đã tồn tại được giữ nguyên.",
        flush=True,
    )


if __name__ == "__main__":
    main()
