# Mô hình kinh tế khung — Phase 0

**Trạng thái:** Phần 1 (thời gian tiến trình) xong. Phần 2 (dòng tiền) chưa làm.
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

## Phần 2 — Dòng tiền (chưa làm)

Cần: nguồn/đầu ra Vàng, Linh Thạch, Điểm Đạo Vận theo giờ chơi; giá dịch vụ, chế tác, xây/nâng công trình; kiểm tra không lạm phát và không kẹt. Phụ thuộc danh sách công trình và vật phẩm chi tiết (chưa có).

## Exit criterion P0 liên quan

"Bảng kinh tế khung cho ra đúng hai mốc 8 giờ và 40-80 giờ trong mô hình": **đạt cho phần thời gian**; phần dòng tiền còn mở.
