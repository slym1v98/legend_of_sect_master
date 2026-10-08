"""Mô hình thời gian tiến trình (Phase 0). Stdlib only. Chạy: python3 -I progression_model.py

Trả lời một câu: với tham số khởi điểm, đệ tử dẫn đầu mất bao nhiêu giờ để
  (1) Độ Kiếp lần đầu (cap 30, cõi Phàm)         -> mốc GDD §8: <= 8 giờ
  (2) đi hết cõi Địa lần đầu (cap 100)           -> mốc GDD §8: 40-80 giờ
Mọi số là điểm khởi đầu, chốt bằng playtest (GDD §9).
"""

# --- Tham số (chỉnh ở đây, chạy lại) ---
XP_C, XP_K = 100, 1.6        # xp_to_next(L) = C * L^K
RATE_A, RATE_P = 3000, 1.0   # xp/giờ khi đang săn = A * L^P (vùng sương mù theo kịp cấp)
DUTY = 0.60                  # tỉ lệ thời gian săn (phần còn lại: ăn/ngủ/chữa/vui do người chơi điều)
BONUS = 1.25                 # nhiệm vụ Nhiệm Vụ Đường + Luyện Công Trường
POTENCY = 0.10               # mỗi Độ Kiếp thành công: +10% tiềm năng (GDD §2.1) -> nhân tốc độ xp
OVERHEAD = 1.15              # thời gian ngoài cày cấp: dọn sương, Bí Cảnh, Yêu Vương, chế tác
STAGES = [("Phàm", 30), ("Linh", 60), ("Địa", 100)]  # cap theo cõi (GDD §2.1); Độ Kiếp ở mỗi cap


def stage_hours(cap, tribulations_done, duty=DUTY):
    """Giờ chơi để một đệ tử đi từ cấp 1 tới cap, sau khi đã Độ Kiếp `tribulations_done` lần."""
    m = 1 + POTENCY * tribulations_done
    grind = sum(XP_C * L**XP_K / (RATE_A * L**RATE_P * duty * BONUS * m) for L in range(1, cap))
    return grind * OVERHEAD


def run(duty=DUTY):
    rows, t = [], 0.0
    for n, (name, cap) in enumerate(STAGES):
        h = stage_hours(cap, n, duty)
        t += h
        rows.append((name, cap, h, t))
    return rows


if __name__ == "__main__":
    print(f"{'Cõi':<6}{'Cap':>5}{'Giờ giai đoạn':>15}{'Giờ cộng dồn':>14}")
    for name, cap, h, t in run():
        print(f"{name:<6}{cap:>5}{h:>15.1f}{t:>14.1f}")

    rows = run()
    first_trib, total = rows[0][3], rows[-1][3]
    assert 5 <= first_trib <= 8, f"Độ Kiếp đầu {first_trib:.1f}h ngoài [5, 8]"
    assert 40 <= total <= 80, f"Tổng {total:.1f}h ngoài [40, 80]"

    print("\nNhạy cảm theo DUTY (người chơi chăm đệ tử kém -> săn ít hơn):")
    print(f"{'DUTY':>6}{'Độ Kiếp #1':>12}{'Hết cõi Địa':>13}")
    for d in (0.4, 0.5, 0.6, 0.7, 0.8):
        r = run(d)
        print(f"{d:>6.1f}{r[0][3]:>12.1f}{r[-1][3]:>13.1f}")
    print("\nOK: hai mốc đạt ở tham số khởi điểm.")
