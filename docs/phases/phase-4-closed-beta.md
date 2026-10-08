# Phase 4 — Beta kín

**Mục tiêu:** Đưa game tới trạng thái phát hành: online nhẹ, monetization, cân bằng bằng dữ liệu thật, đạt KPI giữ chân mục tiêu.
**GDD liên quan:** §5, §6, §8, §9.

## Phạm vi

| Có | Không |
|---|---|
| Bảng xếp hạng tuần (tông mạnh nhất, tầng Bí Cảnh cao nhất, số lần Độ Kiếp) + phần thưởng cosmetic | PvP, guild, offline |
| Gacha Trắc Duyên: pity cứng, công khai tỉ lệ | Nội dung post-EA |
| Cosmetic: trang phục đệ tử, cải trang công trình, hiệu ứng | |
| Tiện ích IAP: kho, slot nhà, hàng đợi chế tác, slot đội Bí Cảnh | |
| Quảng cáo thưởng (tuỳ chọn): rương linh bảo, nhân đôi thưởng Bí Cảnh | |
| Gói tân thủ + battle pass nhẹ | |
| Nhiệm vụ tuần/sự kiện theo lịch server | |
| Analytics đầy đủ, dashboard KPI | |

## Hạng mục theo workstream

- **Backend/Online:** bảng xếp hạng, reset tuần, phát thưởng; sự kiện theo lịch; chống gian lận mức cơ bản (kiểm tra hợp lệ phía server cho điểm xếp hạng); giám sát.
- **Monetization:** cửa hàng, bảng giá thử, kiểm tra nguyên tắc GDD §6.2 (không bán auto, không bán sức mạnh trực tiếp, mọi thứ kiếm được bằng chơi); tuân thủ quy định cửa hàng ứng dụng/công khai tỉ lệ.
- **Kinh tế/Balance:** chỉnh bằng dữ liệu thật: tốc độ tiến trình, tỉ lệ Độ Kiếp thất bại, tỉ lệ chế tác, mức rơi, pity.
- **Gameplay:** sửa theo phản hồi; đánh bóng; thêm tinh chỉnh tiện thao tác (chọn nhiều, lọc).
- **Art/UI:** hoàn thiện, bộ cosmetic bán được, màn cửa hàng.
- **QA/Analytics:** kiểm thử thiết bị rộng, kiểm thử thanh toán, kiểm thử ổn định dài (soak), giám sát crash.
- **Pháp lý/Vận hành:** chính sách quyền riêng tư, điều khoản, xếp hạng độ tuổi, hỗ trợ khách hàng cơ bản.

## Deliverables
1. Bản build ứng viên phát hành (RC).
2. Báo cáo KPI beta và quyết định cân bằng.
3. Quy trình vận hành: phát hành bản vá, xử lý sự cố, hỗ trợ.
4. Checklist đã ký của cửa hàng ứng dụng.

## Exit criteria (khớp GDD §8, đo trên nhóm beta kín)
- [ ] Hoàn thành quest tân thủ ≥ 70%.
- [ ] Giữ chân D1 ≥ 40%, D7 ≥ 15%. (D30 ≥ 6% đo được khi beta đủ dài; nếu không đủ thời gian, ghi nhận và tiếp tục đo ở P5.)
- [ ] Độ Kiếp lần đầu trong 8 giờ chơi đầu (trung vị).
- [ ] Thời lượng tới hết cõi Địa nằm trong 40-80 giờ (trung vị người đi hết).
- [ ] Không còn lỗi mất dữ liệu/mất tiền ở mức nghiêm trọng; crash-free ≥ 99%.
- [ ] Gacha công khai tỉ lệ, pity hoạt động đúng; kiểm toán nội bộ xác nhận.
- [ ] Không phát hiện đường nào mua được lợi thế mà người chơi không thể kiếm bằng chơi.
- [ ] Hồ sơ cửa hàng đủ điều kiện nộp.

## Rủi ro
| Rủi ro | Giảm thiểu |
|---|---|
| KPI giữ chân thấp | Phân tích điểm rớt, thử nghiệm A/B nhẹ cho quest/phần thưởng sớm |
| Gacha gây tiếng xấu | Pity cứng, công khai tỉ lệ, đường kiếm miễn phí rõ (GDD §9) |
| Gian lận xếp hạng | Xác thực server, giới hạn thưởng cho top là cosmetic |
| Nhóm beta không đại diện | Tuyển từ nhóm người chơi tycoon/idle, không chỉ người quen |

## Cắt giảm được
Battle pass có thể hoãn sang sau EA; sự kiện tuần chỉ giữ một loại; bớt cosmetic. Giữ nguyên: pity, công khai tỉ lệ, tuân thủ cửa hàng.

## Ngoài phạm vi
Nội dung mới ngoài scope EA (GDD §7.2).
