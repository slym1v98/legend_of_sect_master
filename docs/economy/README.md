# Mô hình kinh tế khung — Phase 0

**Trạng thái:** Phần 1 (thời gian tiến trình) và phần 2 (dòng tiền) xong ở mức khung.
**Liên quan:** GDD §2.5, §8, §9; `phases/phase-0-preproduction.md`.

## Phần 1 — Thời gian tiến trình

`progression_model.py` (stdlib, chạy `python3 -I progression_model.py`, có assert hai mốc).

### Mô hình

Một đệ tử dẫn đầu đi từ cấp 1 tới cap của từng cõi, Độ Kiếp ở mỗi cap rồi reset về cấp 1 (GDD §2.1).

- XP cần để lên cấp L: `100 · L^1.6`
- Tốc độ XP khi đang săn: `3000 · L` mỗi giờ (giả định vùng sương mù luôn theo kịp cấp)
- Giờ chơi = XP / (tốc độ × `DUTY` × `BONUS` × (1 + 0.10 × số lần Độ Kiếp đã qua)) × `OVERHEAD`
- `DUTY` 0.60: tỉ lệ thời gian đệ tử đang săn (phần còn lại ăn/ngủ/chữa/vui do người chơi điều)
- `BONUS` 1.25: nhiệm vụ + Luyện Công Trường. `OVERHEAD` 1.15: dọn sương, Bí Cảnh, Yêu Vương, chế tác

### Kết quả (tham số khởi điểm)

| Cõi | Cap | Giờ giai đoạn | Cộng dồn |
|---|---|---|---|
| Phàm | 30 | 7.2 | **7.2** (mốc: Độ Kiếp đầu ≤ 8h) |
| Linh | 60 | 20.0 | 27.2 |
| Địa | 100 | 41.8 | **69.1** (mốc: 40-80h) |

### Nhạy cảm theo DUTY

| DUTY | Độ Kiếp #1 | Hết cõi Địa |
|---|---|---|
| 0.4 | 10.8 | 103.6 |
| 0.5 | **8.6** | 82.9 |
| 0.6 | 7.2 | 69.1 |
| 0.7 | 6.1 | 59.2 |
| 0.8 | 5.4 | 51.8 |

## Điều cần biết trước khi tin con số

1. **Biên mỏng.** DUTY giảm từ 0.6 xuống 0.5 là trượt cả hai mốc (8.6h và 82.9h). Người chơi chăm đệ tử vụng sẽ ra ngoài mục tiêu. Playtest P1 phải đo DUTY thực tế; đây là biến quan trọng nhất của mô hình.
2. **Một đệ tử, một đường.** Mô hình theo đệ tử dẫn đầu. Chưa tính: nhiều đệ tử chia sẻ vùng, đệ tử mới phải cày lại, nút thắt chế tác/vật liệu.
3. **Độ Kiếp thất bại chưa mô hình.** GDD §2.1: thua mất một phần cấp + thời gian chờ. Sẽ cộng thêm giờ; cần xác suất để tính.
4. **"Hết cõi Địa" giả định** Độ Kiếp ở cap 30 và 60 rồi leo cap 100, mở cõi qua điều kiện vùng + Đạo Vận (GDD §2.8). Điều kiện mở khoá có thể chặn lâu hơn thời gian cày cấp.
5. **Tốc độ XP theo vùng là giả định thẳng** (`3000·L`), chưa gắn với bảng vùng/yêu thú thật.

## Phần 2 — Dòng tiền

`economy_flow.py` (stdlib, `python3 -I economy_flow.py`, có assert). Lấy thời gian từng cõi từ `progression_model.py`, **không nhân đôi nguồn**.

### Mô hình

Chu trình đúng GDD §2.5: đệ tử săn → nhận Vàng + vật liệu → tông mua vật liệu (Tụ Bảo Các) → đệ tử chi Vàng tại tông (nhu cầu, trang bị, kỹ năng) → tông trừ giá vốn → phần ròng chi nâng cấp.

| Tham số | Giá trị | Ý nghĩa |
|---|---|---|
| Số đệ tử trung bình | 8 / 14 / 22 | Phàm / Linh / Địa (slot tối đa 30) |
| Vàng rơi, vật liệu rơi | 30 / 20 mỗi giờ săn mỗi cấp | Cá nhân đệ tử |
| Tông mua vật liệu | 70% | Qua Tụ Bảo Các |
| Đệ tử chi tại tông | 30% nhu cầu, 45% trang bị, 8% kỹ năng | Còn 17% tiết kiệm |
| Giá vốn tông trên doanh thu | 35% / 20% / 40% | Nhu cầu / trang bị / kỹ năng |
| Nâng Đại Điện cấp k→k+1 | `450 · 1.9^(k-1)` | Công trình khác = 3 × chi Đại Điện cùng cõi |

### Kết quả

| Cõi | Giờ | Cấp TB | Thu ròng tông | Chi nâng cấp | Chi/Thu | Ngân sách mỗi món trang bị |
|---|---|---|---|---|---|---|
| Phàm | 7.2 | 18.2 | 7,839 | 5,220 | 0.67 | 258 |
| Linh | 20.0 | 36.6 | 77,299 | 42,302 | 0.55 | 1,454 |
| Địa | 41.8 | 61.2 | 423,923 | 290,149 | 0.68 | 10,148 |

- Chi/Thu cân bằng giữa các cõi (chênh 1.25×, ngưỡng 1.4×): không cõi nào quá rẻ hoặc quá đắt.
- Ví đệ tử tiết kiệm 17%: không âm.
- Linh Thạch miễn phí tới hết cõi Địa ≈ **60 lượt kéo**; chạm pity (50 lượt) sau **58 giờ**.

## Điều cần biết trước khi tin con số

Những điểm của phần 1 vẫn đúng. Thêm:

6. **Tham số nâng cấp được chỉnh để qua chính ngưỡng của mô hình.** Ngưỡng (Chi/Thu 0.5–0.7, chênh ≤ 1.4×, pity 30–80 giờ) do tôi đặt, không lấy từ dữ liệu. Lưới quét `GH_BASE` 100–800 × `GH_GROWTH` 1.5–2.0 chỉ có **một** cấu hình qua cả hai điều kiện đầu (450, 1.9): biên rất hẹp, chỉ cần đổi một tham số khác là vỡ. Coi đây là "mô hình nhất quán nội bộ", chưa phải "kinh tế đã cân bằng".
7. **Ngân sách mỗi món tăng ~39× từ Phàm lên Địa** (258 → 10,148). Có chủ đích (cõi sau giàu hơn), nhưng cần playtest xem đệ tử có đủ tiền mua đồ đúng nhịp.
8. **Chưa mô hình:** Đạo Vận (cung/cầu của Đạo Ấn), chi tiết chế tác (thời gian, tỉ lệ thất bại, hàng đợi), bảng rơi Bí Cảnh, chi phí hồi sinh, cường hoá +1→+10, thu hồi trang bị cũ. Phần Linh Thạch chỉ tính nguồn miễn phí và pity, chưa tính giá cửa hàng IAP.
9. **Số đệ tử theo cõi (8/14/22) là giả định** về tốc độ mở slot; thực tế phụ thuộc Nhà ở và gacha.
10. **Mọi giá trị rơi và tỉ lệ chi** là điểm khởi đầu không có nguồn tham chiếu; số liệu EHT chưa thu thập (GDD §9).

## Exit criterion P0 liên quan

"Bảng kinh tế khung cho ra đúng hai mốc 8 giờ và 40-80 giờ trong mô hình": **đạt** cho thời gian (phần 1) và có thêm dòng tiền nhất quán (phần 2), với các lưu ý ở trên. Chưa phải bằng chứng cân bằng; kiểm chứng thật ở Phase 1-2.
