# Phase 2 — Vertical slice

**Mục tiêu:** Một lát cắt hoàn chỉnh, chất lượng gần bản phát hành: toàn bộ chuỗi cung ứng trong **cõi Phàm** và phần đầu progression. Khoá art style và UI kit.
**GDD liên quan:** §1.5 (vòng lặp lõi), §2.1, §2.3, §2.5, §2.6, §2.7, §3, §2.8 (cõi Phàm), §4.

## Phạm vi

| Có | Không |
|---|---|
| Vòng lặp lõi đầy đủ: săn → Tụ Bảo Các → chế tác → quầy → Linh Thạch | Cõi Linh, Địa |
| Cõi Phàm: 6 vùng sương mù, Yêu Vương Phàm, Bí Cảnh tầng 1-10 | Bí Cảnh tầng 11-25 |
| 4 chức nghiệp, tư chất, tính cách, cấp tới 30 | Linh căn đầy đủ, linh mạch, Độ Kiếp (xem ghi chú) |
| Công trình: Đại Điện, Tụ Bảo Các, Nhà ở, Luyện Khí Phòng, Đan Phòng, quầy vũ khí, quầy giáp, quầy đan, 4 dịch vụ (16 công trình, Đại Điện ≤ cấp 3, xem `docs/content/buildings.md`), Nhiệm Vụ Đường, Luân Hồi Trì, Bí Cảnh Cổ Môn, Triệu Yêu Linh | Pháp Bảo Các, Truyền Công Các, Luyện Công Trường, Cường Hoá Lô |
| Quest tân thủ (dẫn qua phần đã có) | Hằng ngày/tuần, sự kiện |
| Sương mù: cơ chế dọn vùng | Cloud save, bảng xếp hạng |
| Chọn nhiều đệ tử + giao vùng hàng loạt | Gacha, IAP, quảng cáo |

Ghi chú: Linh căn xuất hiện ở dạng nhãn + hiệu ứng tương khắc đơn giản để thử ngũ hành sớm; chiều sâu đầy đủ ở P3.

## Hạng mục theo workstream

- **Gameplay:** hệ thống đơn hàng Tụ Bảo Các; chế tác có thời gian, hàng đợi, tỉ lệ thành công; quầy bán + hành vi mua của đệ tử; Bí Cảnh 3 lượt tổ đội 5; Yêu Vương; sương mù; nhiệm vụ tân thủ.
- **Kinh tế/Balance:** dựng đường cong cõi Phàm theo mô hình P0; điều chỉnh tới khi 1-2 giờ đầu chạy trơn; ghi lại hệ số vào bảng tính.
- **Art/Animation:** bộ asset chất lượng phát hành cho cõi Phàm: đệ tử 4 chức nghiệp (idle/đi/đánh/chết), công trình đã liệt kê, yêu thú cõi Phàm, hiệu ứng ngũ hành cơ bản, UI kit. **Khoá phong cách** ở cuối phase.
- **UI/UX:** thanh dưới đầy đủ (Xây · Đệ tử · Bí cảnh · Kho · Nhiệm vụ), danh sách đệ tử có lọc/chọn nhiều, kho, màn chế tác, màn đơn hàng.
- **Backend:** chưa. Chỉ save cục bộ hoàn chỉnh + hệ thống phiên bản save.
- **QA/Analytics:** funnel tân thủ, thời gian mỗi mốc, điểm rớt; hiệu năng trên bộ thiết bị mục tiêu.

## Deliverables
1. Build chơi liền mạch từ đầu tới hết cõi Phàm.
2. Bộ art + UI kit đã khoá.
3. Bảng cân bằng cõi Phàm.
4. Báo cáo playtest ngoài nhóm.

## Exit criteria
- [ ] Playtest ≥ 15 người ngoài đội, ≥ 60% hoàn thành quest tân thủ.
- [ ] ≥ 60% muốn chơi tiếp sau phiên 1-2 giờ (khảo sát ngắn).
- [ ] Không có chuỗi cung ứng nào "đứt" (người chơi kẹt không có hành động hợp lý) — kiểm bằng log và quan sát.
- [ ] Hiệu năng đạt ngưỡng P0 với 20 đệ tử, ~20 công trình.
- [ ] Phong cách art + UI kit được duyệt và khoá; ước lượng asset cho P3 cập nhật.
- [ ] Mô hình kinh tế cõi Phàm khớp dữ liệu playtest trong ±25% ở mốc thời gian chính.

## Rủi ro
| Rủi ro | Giảm thiểu |
|---|---|
| Chuỗi cung ứng quá phức tạp cho người mới | Quest tân thủ dẫn từng bước; đo điểm rớt |
| Chi phí asset vượt dự kiến | Tái dùng sprite khung chung; công trình cố định hướng (GDD §4.1) |
| Kinh tế lệch khi thêm hệ thống | Giữ bảng tính là nguồn duy nhất, mọi chỉnh sửa qua nó |

## Cắt giảm được
Bí Cảnh còn 5 tầng; ít vùng sương hơn (4); bỏ Yêu Vương nếu thiếu thời gian (hoãn P3).

## Ngoài phạm vi
Ngũ hành chiều sâu, linh mạch, Độ Kiếp, online, monetization.
