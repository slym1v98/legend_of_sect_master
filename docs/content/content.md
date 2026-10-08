# Danh mục nội dung — Early Access

**Phase 0 deliverable.** Vùng, yêu thú, vật liệu, vật phẩm, kỹ năng. Nguồn cho dòng tiền và ước lượng asset.
**Liên quan:** GDD §2.1-2.8; `buildings.md`; `docs/glossary.md`. Mọi số là điểm khởi đầu.

## Nguyên tắc

- **Cõi Phàm đặt tên đầy đủ** (là nội dung Phase 2 vertical slice). **Cõi Linh, Địa chỉ định số lượng và khuôn mẫu**, đặt tên ở Phase 3.
- Giá và công thức chi tiết nằm ở phần dòng tiền, theo công thức `(loại, bậc)`, không gán tay từng món.
- **Hệ ngũ hành của trang bị lấy từ Lõi Ngũ Hành khi chế**, không có món riêng theo hệ; dùng đổi bảng màu trên một sprite gốc (tiết kiệm asset, giữ GDD §2.1 "vũ khí theo chức nghiệp + hệ").
- Tên mới sẽ vào `glossary.md` khi duyệt.

## 1. Vùng sương mù (18)

Mỗi cõi 6 vùng: 5 vùng theo ngũ hành + 1 vùng cuối chứa Yêu Vương (điều kiện mở cõi sau, GDD §2.8).

### Cõi Phàm

| # | Vùng | Hệ | Yêu thú | Vật liệu rơi (hiếm→thường) |
|---|---|---|---|---|
| 1 | Hắc Thạch Pha | Kim | Thiết Giáp Dã Trư, Kim Nha Lang | Kim Nha; Thiết Giáp Phiến |
| 2 | Lục Trúc Lâm | Mộc | Thanh Đằng Yêu, Mộc Linh Hầu | Linh Mộc Tâm; Thanh Đằng |
| 3 | Hàn Đàm | Thuỷ | Hàn Đàm Quy, Băng Lân Ngư | Băng Lân; Hàn Quy Giáp |
| 4 | Xích Hoả Cốc | Hoả | Xích Diễm Hồ, Hoả Tích Dịch | Hoả Tích Hạch; Xích Hồ Mao |
| 5 | Hoàng Sa Nguyên | Thổ | Hoàng Sa Hạt, Nham Thạch Quái | Nham Tinh; Sa Hạt Độc Châm |
| 6 | Cổ Mộ Địa | Hỗn | Cổ Mộ Thi Quái, Âm Hồn | Âm Hồn Châu; Cổ Cốt. **Yêu Vương Phàm: Hắc Phong Lang Vương** |

### Cõi Linh và Địa (khuôn mẫu)

Mỗi cõi: cùng cấu trúc 6 vùng (5 hệ + vùng Yêu Vương). 2 yêu thú thường mỗi vùng, 1 Yêu Vương.

## 2. Yêu thú

| Loại | Phàm | Linh | Địa | Tổng |
|---|---|---|---|---|
| Yêu thú thường (2 loại × 6 vùng) | 12 | 12 | 12 | 36 |
| Yêu Vương | 1 | 1 | 1 | 3 |
| Boss tầng Bí Cảnh (duy nhất, mỗi 5 tầng) | 2 (tầng 5, 10) | 2 (15, 20) | 1 (25) | 5 |

- Boss của 20 tầng còn lại là **biến thể** (đổi màu/kích cỡ) của boss duy nhất gần nhất, không vẽ mới.
- Mục tiêu để giảm asset: tối thiểu một nửa yêu thú Linh/Địa là biến thể bảng màu/kích cỡ từ khung gốc cõi Phàm (GDD §9 "tái dùng sprite").

## 3. Vật liệu

### Cõi Phàm (16 món)

| Nhóm | Món | Nguồn |
|---|---|---|
| Vật liệu cơ bản (4) | Yêu Nhục, Linh Thảo, Thô Thiết, Mộc Liệu | Rơi từ mọi yêu thú thường (theo hệ vùng) |
| Vật liệu vùng (12) | 2 mỗi vùng ở bảng mục 1 | Yêu thú vùng đó |

Công dụng nhóm cơ bản: Yêu Nhục → nấu linh thiện; Linh Thảo → thuốc băng/cao và đan; Thô Thiết + Mộc Liệu → xây và nâng cấp công trình, Đại Điện.

### Lõi Ngũ Hành (15)

5 hệ × 3 phẩm (Hạ phẩm cõi Phàm, Trung phẩm cõi Linh, Thượng phẩm cõi Địa). Rơi hiếm từ yêu thú đúng hệ và Bí Cảnh; quyết định hệ của trang bị khi chế.

### Cõi Linh và Địa

Mỗi cõi: 4 vật liệu cơ bản bậc cao + 12 vật liệu vùng (Tinh Hoa Bí Cảnh tính riêng, mục dưới). Tên đặt ở Phase 3.

### Tinh Hoa Bí Cảnh (6)

2 mỗi cõi, **chỉ rơi từ Bí Cảnh** (tầng sâu hơn → xác suất cao hơn). Dùng cho đồ bậc cao và cường hoá.

**Tổng vật liệu:** Phàm 16 + Linh 16 + Địa 16 + Lõi 15 + Tinh Hoa 6 = **69**.

## 4. Trang bị

### Bậc theo cõi

| Cõi | Bậc trang bị chế được |
|---|---|
| Phàm | D, C |
| Linh | B, A |
| Địa | S |

Cõi Địa chỉ một bậc: tiến trình dựa vào **cường hoá +1 → +10** và hiếm của lõi/tinh hoa. **Cần xác nhận ở dòng tiền** rằng một bậc là đủ cho 40+ giờ cuối.

### Khung gốc mỗi bậc (10 món chế được)

| Ô | Số món | Ghi chú |
|---|---|---|
| Vũ khí | 4 | Mỗi chức nghiệp một loại (kiếm, thương/thuẫn, cung, chùy/phù) |
| Giáp thân | 4 | Mỗi chức nghiệp một loại |
| Phụ kiện | 2 | Nhẫn, phù hộ mệnh (chế ở Pháp Bảo Các) |

5 bậc × 10 = **50 món chế được**.

### Mũ (chỉ từ Bí Cảnh)

2 món mỗi bậc × 5 bậc = **10 món**, không chế được (giống mũ chỉ rơi từ dungeon ở EHT).

### Hiển thị trên nhân vật

**Chỉ hiển thị vũ khí và màu áo theo bậc**; giáp/mũ/phụ kiện không đổi sprite nhân vật. Quyết định để giữ tổ hợp animation thấp (đệ tử × trang bị).

## 5. Vật tiêu hao

| Loại | Chế ở | Món | Chi tiết |
|---|---|---|---|
| Linh thiện | `MealHall` | 6 | 2 món mỗi cõi; hồi **Đói** |
| Phòng nghỉ | `RestChamber` | 3 | Phòng Thường, Phòng Thượng, Phòng Thiên; hồi **Thể lực** |
| Thuốc băng/cao | `HealingHall` | 3 | Thảo Dược Băng, Linh Dược Cao, Hồi Xuân Tán; hồi **Thương tích** |
| Trà/rượu | `TeaHouse` | 3 | Thanh Trà, Linh Tửu, Tiên Nhưỡng; hồi **Tâm trạng** |
| Hồi phục đan | `AlchemyRoom` | 3 | Hạ/Trung/Thượng; đệ tử dùng trong trận |
| Tăng chỉ số tạm | `AlchemyRoom` | 12 | 4 chỉ số (công, thủ, tốc, bạo kích) × 3 bậc |
| Thuốc Kháng Kiếp | `AlchemyRoom` | 3 | Giảm tỉ lệ thất bại Độ Kiếp (mỗi cõi 1 bậc) |
| Triệu Yêu Hương | `AlchemyRoom` | 3 | Mỗi cõi một loại; dùng ở `BeastSummonBell` |

**Tổng: 36 món tiêu hao.**

## 6. Công pháp, bí thuật, Đạo Ấn

| Loại | Số lượng | Ghi chú |
|---|---|---|
| Công pháp (kỹ năng chủ động) | 20 gốc (4 chức nghiệp × 5 hệ), mỗi cái 3 bậc nâng | Hệ lấy từ linh căn (GDD §2.2) |
| Bí thuật (bị động, tăng chỉ số nhỏ) | 10 | Né, thể lực, hồi phục, v.v. |
| Đạo Ấn (trait mở bằng Điểm Đạo Vận) | 24 | Dòng mạnh, ví dụ "Hoả +15%" |

## 7. Số đếm asset (đếm, chưa ước giờ công)

| Nhóm | Số lượng gốc | Ghi chú giảm asset |
|---|---|---|
| Công trình | 63 sprite + 21 lớp phủ | Xem `buildings.md` |
| Đệ tử | 4 chức nghiệp × ~10 hoạt hoạ (idle, đi, đánh, bị thương, chết, ăn, ngủ, chữa, giải trí, nhặt) | Vẽ **2 hướng**, lật gương thành 4 |
| Yêu thú thường | 36 thiết kế | ≥ 50% là biến thể màu/kích cỡ |
| Yêu Vương | 3 | |
| Boss tầng Bí Cảnh | 5 duy nhất (+ 20 biến thể màu) | |
| Biểu tượng vật liệu | 69 | |
| Biểu tượng trang bị | 50 chế được + 10 mũ = 60 | Hệ ngũ hành bằng đổi bảng màu |
| Biểu tượng tiêu hao | 36 | |
| Hiệu ứng công pháp | 20 (4 kiểu theo chức nghiệp × 5 màu hệ) | |
| Hiệu ứng khác | Thiên kiếp, sương mù, linh mạch, Yêu Vương xuất hiện | |
| Địa hình + bản đồ | 3 cõi × 6 vùng | Dùng chung ô nền theo hệ |
| UI | Chưa đếm | Khoá cùng UI kit ở P2 |

## 8. Điểm cần quyết sau

1. **Cõi Địa chỉ một bậc trang bị (S)**: xác nhận ở dòng tiền.
2. ~~Thuốc đột phá~~: **đã bỏ** khỏi GDD §2.6 (không có cơ chế; Độ Kiếp đã đảm nhiệm vai trò đột phá). GDD §2.2 "nguyên liệu đột phá" đổi thành "vật liệu hiếm".
3. **Bí Cảnh phần thưởng**: bảng rơi theo tầng chưa lập; thuộc dòng tiền.
4. **Số loại vật liệu 69** có thể nhiều so với giá trị chơi; cân nhắc hợp nhất ở dòng tiền nếu nhiều món không có công thức dùng.
