# Phase 3 — Alpha

**Mục tiêu:** Đủ nội dung và hệ thống của Early Access: 3 cõi, Bí Cảnh 25 tầng, Độ Kiếp, ngũ hành, linh mạch. Chưa cân bằng cuối, chưa monetization.
**GDD liên quan:** §2.1-2.8, §3, §4. Backend khung (§5).

## Phạm vi

Feature-complete cho nội dung chơi; chất lượng còn thô ở balance và đánh bóng.

| Có | Không |
|---|---|
| Cõi Linh + Địa (12 vùng sương mù), tổng 18 vùng | Cân bằng cuối, tinh chỉnh kinh tế bằng dữ liệu thật |
| Bí Cảnh tầng 1-25, 3 Yêu Vương | Gacha, IAP, quảng cáo, battle pass |
| **Độ Kiếp** + Điểm Đạo Vận + Đạo Ấn (trait) + Thuốc Kháng Kiếp | Bảng xếp hạng chính thức, sự kiện live |
| **Linh căn** đầy đủ (kể cả dị linh căn) + tương khắc trong chiến đấu | Cosmetic bán được |
| **Linh mạch** + buff công trình + highlight | Localization ngoài tiếng Việt |
| Đủ ~20 công trình (thêm Pháp Bảo Các, Truyền Công Các, Luyện Công Trường, Cường Hoá Lô, quầy pháp bảo) | |
| Cường hoá +1→+10, thu hồi trang bị cũ | |
| Công pháp/bí thuật, tư chất, tính cách, thiên phú | |
| Nhiệm vụ hằng ngày/tuần (khung, chưa live) | |
| Backend khung: tài khoản + cloud save | |

## Hạng mục theo workstream

- **Gameplay:** Độ Kiếp (trận thiên kiếp ngắn, thua = trọng thương mất một phần cấp, **không mất vĩnh viễn**); ngũ hành tính sát thương/khắc; linh mạch trên bản đồ + áp buff; công pháp/bí thuật; cường hoá; mở cõi qua điều kiện vùng cuối + Đạo Vận (GDD §2.8).
- **Kinh tế/Balance:** đường cong 3 cõi đạt mốc Độ Kiếp lần đầu ≤ 8 giờ và hết cõi Địa 40-80 giờ **trong mô phỏng**; chia thang trang bị tier D→S theo cõi.
- **Art/Animation:** toàn bộ yêu thú 3 cõi (dùng biến thể màu có kiểm soát), công trình còn lại, hiệu ứng thiên kiếp, hiệu ứng ngũ hành, bản đồ sương mù 18 vùng.
- **UI/UX:** màn Độ Kiếp, cây Đạo Ấn, màn công pháp, bản đồ thế giới, hiển thị linh mạch.
- **Backend:** đăng nhập, cloud save (chống xung đột nhiều thiết bị cơ bản). Bảng xếp hạng để P4.
- **QA/Analytics:** bộ kiểm hồi quy save/load qua phiên bản; kịch bản chơi tự động hoặc ghi lại cho đường đi chính.

## Deliverables
1. Build chơi từ đầu tới hết cõi Địa.
2. Mô phỏng kinh tế 3 cõi + dữ liệu từ playtest nội bộ.
3. Danh sách lỗi và nợ đánh bóng cho P4.

## Exit criteria
- [ ] Người chơi nội bộ đi hết cõi Địa và thực hiện Độ Kiếp đầu tiên không bị chặn bởi lỗi.
- [ ] Thời gian Độ Kiếp lần đầu trong playtest: 6-10 giờ (mô phỏng khớp ±25%).
- [ ] Đủ 18 vùng, 25 tầng Bí Cảnh, 3 Yêu Vương, ~20 công trình, 4 chức nghiệp chơi được.
- [ ] Mọi mục "Có" ở bảng trên chạy được; không còn crash chặn tiến trình trong 10 lần chơi liên tục.
- [ ] Ba hệ thống đặc trưng (linh căn, linh mạch, Độ Kiếp) tạo khác biệt có thể nêu tên trong playtest ("khác EHT ở chỗ…").
- [ ] Cloud save qua lại giữa 2 thiết bị không mất dữ liệu.
- [ ] Hiệu năng đạt ngưỡng P0 với 30 đệ tử.

## Rủi ro
| Rủi ro | Giảm thiểu |
|---|---|
| Linh mạch trở thành gánh nặng bố trí | Highlight rõ, buff vừa phải, cho dời công trình miễn phí |
| Độ Kiếp quá nặng/nhẹ | Tham số hoá xác suất; thử nhiều mức ở P4 |
| Asset 3 cõi vượt sức | Biến thể màu, tái dùng khung; cắt theo danh sách dưới |
| Kinh tế mất cân khi nội dung tăng | Mô phỏng bằng bảng tính trước khi chỉnh game |

## Cắt giảm được (theo thứ tự)
1. Số vùng/cõi 6 → 5. 2. Biến thể yêu thú. 3. Một số bí thuật. 4. Đạo Ấn còn ít dòng. Giữ nguyên: Độ Kiếp, ngũ hành, linh mạch.

## Ngoài phạm vi
Monetization, bảng xếp hạng live, sự kiện, PvP, offline.
