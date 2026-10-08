"""Mô hình dòng tiền (Phase 0). Stdlib only. Chạy: python3 -I economy_flow.py

Trả lời ba câu, theo từng cõi (Phàm/Linh/Địa), với tham số khởi điểm:
  (1) Tông có kiếm đủ Vàng để nâng cấp công trình đúng nhịp cõi không?
  (2) Mức giá trang bị bền vững cho đệ tử là bao nhiêu?
  (3) Người chơi miễn phí chạm pity gacha sau bao lâu?
Thời gian từng cõi lấy từ progression_model.py (nguồn duy nhất).
Mọi số là điểm khởi đầu, chốt bằng playtest (GDD §9).
"""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("pm", Path(__file__).with_name("progression_model.py"))
pm = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(pm)

# --- Đệ tử và thu nhập (mọi đại lượng tính theo giờ săn, theo cấp L) ---
N = {"Phàm": 8, "Linh": 14, "Địa": 22}    # số đệ tử trung bình mỗi cõi (slot tối đa 30)
DROP_GOLD = 30     # Vàng rơi cá nhân / giờ săn / cấp
DROP_MAT = 20      # giá trị vật liệu rơi / giờ săn / cấp
MAT_SOLD = 0.7     # phần vật liệu mà tông mua qua Tụ Bảo Các (còn lại đệ tử giữ/bỏ)
# Đệ tử chi tại tông (phần thu nhập đệ tử); phần còn lại là tiết kiệm
SPEND = {"needs": 0.30, "gear": 0.45, "skill": 0.08}
# Giá vốn của tông trên doanh thu mỗi loại (nguyên liệu nấu/chế, phần trả lại đệ tử khi học)
COGS = {"needs": 0.35, "gear": 0.20, "skill": 0.40}

# --- Chi nâng cấp ---
GH_BASE, GH_GROWTH = 450, 1.9             # nâng Đại Điện cấp k -> k+1 = BASE * GROWTH^(k-1)
GH_STEPS = {"Phàm": [1, 2], "Linh": [3, 4, 5], "Địa": [6, 7, 8]}   # Đại Điện 1->3, 3->6, 6->9
OTHER_MULT = 3.0   # chi nâng các công trình khác = 3 x chi nâng Đại Điện cùng cõi (mỗi cái <= cấp Đại Điện)
SINK_OTHER = 0.30  # phần thu nhập ròng dành cho hồi sinh, cường hoá, chế tác; nâng cấp được dùng tối đa 1 - SINK_OTHER

# --- Linh Thạch và gacha ---
PULL_COST, PITY = 100, 50
SS_PER_HOUR = 60         # nhiệm vụ hằng ngày: 90 Linh Thạch/ngày, giả định 1.5 giờ chơi/ngày
SS_BOSS = 3 * 150        # Yêu Vương: 3 lần hạ / cõi x 150
SS_REALM_FLOOR = 25 * 20  # Bí Cảnh: thưởng lần đầu qua 25 tầng x 20 (tính cho cả game)


def avg_level(cap):
    """Cấp trung bình theo thời gian: mỗi cấp tốn giờ ~ XP_C*L^K / (RATE_A*L^P)."""
    w = [(L, pm.XP_C * L**pm.XP_K / (pm.RATE_A * L**pm.RATE_P)) for L in range(1, cap)]
    return sum(L * x for L, x in w) / sum(x for _, x in w)


def realm_flow():
    out = []
    stage = pm.run()
    prev_cap = 0
    for name, cap, hours, _ in stage:
        L = avg_level(cap)
        inc = DROP_GOLD + MAT_SOLD * DROP_MAT            # thu nhập đệ tử / giờ săn / cấp
        revenue = inc * sum(SPEND.values())
        cogs = inc * sum(SPEND[k] * COGS[k] for k in SPEND)
        net_unit = revenue - MAT_SOLD * DROP_MAT - cogs   # sau khi trả vật liệu cho đệ tử và giá vốn
        active = N[name] * pm.DUTY * hours                # giờ-đệ-tử đang săn
        net = net_unit * L * active
        gh = sum(GH_BASE * GH_GROWTH ** (k - 1) for k in GH_STEPS[name])
        bill = gh * (1 + OTHER_MULT)
        # ngân sách trang bị mỗi đệ tử trong cõi, chia cho số món (tier x 3 ô)
        gear_budget = inc * SPEND["gear"] * L * pm.DUTY * hours
        tiers = {"Phàm": 2, "Linh": 2, "Địa": 1}[name]
        out.append(dict(realm=name, cap=cap, hours=hours, avg_level=L, net=net, bill=bill,
                        ratio=bill / net, gear_per_piece=gear_budget / (tiers * 3)))
        prev_cap = cap
    return out


def pity_hours(total_hours):
    """Giờ chơi để người chơi miễn phí tích đủ PITY lượt kéo."""
    total_ss = SS_PER_HOUR * total_hours + 3 * SS_BOSS + SS_REALM_FLOOR
    rate = total_ss / total_hours
    return PITY * PULL_COST / rate, total_ss / PULL_COST


if __name__ == "__main__":
    rows = realm_flow()
    print(f"{'Cõi':<6}{'Giờ':>6}{'Cấp TB':>8}{'Thu ròng tông':>15}{'Chi nâng cấp':>14}{'Chi/Thu':>9}{'Giá/món':>10}")
    for r in rows:
        print(f"{r['realm']:<6}{r['hours']:>6.1f}{r['avg_level']:>8.1f}{r['net']:>15,.0f}{r['bill']:>14,.0f}"
              f"{r['ratio']:>9.2f}{r['gear_per_piece']:>10,.0f}")

    cap_ratio = 1 - SINK_OTHER
    for r in rows:
        assert 0.5 <= r["ratio"] <= cap_ratio, f"{r['realm']}: chi/thu {r['ratio']:.2f} ngoài [0.5, {cap_ratio:.2f}]"
    spread = max(r["ratio"] for r in rows) / min(r["ratio"] for r in rows)
    assert spread <= 1.4, f"Chênh chi/thu giữa các cõi {spread:.2f} > 1.4 (một cõi quá rẻ/đắt)"
    assert 1 - sum(SPEND.values()) > 0, "Đệ tử chi quá thu nhập: ví âm"

    total = sum(r["hours"] for r in rows)
    ph, pulls = pity_hours(total)
    print(f"\nChênh chi/thu giữa các cõi: {spread:.2f}x (ngưỡng 1.4x)")
    print(f"Ví đệ tử tiết kiệm: {1 - sum(SPEND.values()):.0%} thu nhập")
    print(f"Linh Thạch miễn phí tới hết cõi Địa: {pulls:.0f} lượt kéo; chạm pity {PITY} lượt sau {ph:.0f} giờ")
    assert 30 <= ph <= 80, f"Pity miễn phí sau {ph:.0f}h ngoài [30, 80]"
    print("\nOK: cả ba kiểm tra đạt ở tham số khởi điểm.")
