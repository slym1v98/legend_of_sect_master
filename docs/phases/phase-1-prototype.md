# Phase 1 — Prototype

**Mục tiêu:** Chứng minh lõi vui: quản lý thủ công nhu cầu đệ tử trên lưới isometric. Đây là **cổng go/no-go** cho cả dự án.
**GDD liên quan:** §1.3-1.5, §2.1 (nhu cầu), §2.3 (xây dựng cơ bản), §2.2 (săn ngoài thành), §4.

## Phạm vi

Bản chơi được nội bộ, art tạm được, không cần đẹp.

| Có | Không |
|---|---|
| Lưới isometric 2:1, đặt/di chuyển công trình | Linh mạch, ngũ hành |
| 1 loại đệ tử (chọn 1 chức nghiệp), vài đệ tử cùng lúc | 4 chức nghiệp đầy đủ, gacha |
| 4 nhu cầu: Đói, Thể lực, Thương tích, Tâm trạng | Độ Kiếp, Bí Cảnh, Yêu Vương |
| 4 công trình dịch vụ: Linh Thiện Đường, Tĩnh Thất, Y Đường, Trà Lâu | Chế tác, Tụ Bảo Các, quầy bán |
| 1 vùng săn, đệ tử tự đánh, rơi vật phẩm tap nhặt | Sương mù, nhiều vùng |
| Menu ngữ cảnh trên đệ tử (ăn/nghỉ/chữa/vui/đi săn) | Hàng loạt, nhiệm vụ |
| Vàng cơ bản (nguồn: săn; chi: dịch vụ) | Linh Thạch, Đạo Vận |
| Save/load cục bộ | Online, monetization |

## Hạng mục theo workstream

- **Gameplay:** state machine nhu cầu (giảm theo thời gian/hành động; cạn → từ chối đi săn), AI di chuyển tới công trình, combat tự động rất đơn giản, rơi vật phẩm và nhặt.
- **Kinh tế:** công thức rơi Vàng, giá dịch vụ, tốc độ giảm nhu cầu; mục tiêu: người chơi luôn có việc nhưng không quá tải với ~6 đệ tử.
- **Art:** sprite tạm theo phong cách đã duyệt ở P0 (1 đệ tử, 4 công trình, 1 địa hình, 1 yêu thú).
- **UI/UX:** thanh dưới tối thiểu, menu ngữ cảnh khi bấm đệ tử/công trình, thanh trạng thái nhu cầu.
- **QA/Analytics:** log phiên chơi (thao tác/phút, nhu cầu cạn lần mấy, thời gian chờ) để đánh giá cảm giác.

## Deliverables
1. Bản build chơi được trên thiết bị thật.
2. Log + bản ghi quan sát playtest nội bộ.
3. Báo cáo go/no-go.

## Exit criteria
- [ ] Playtest nội bộ ≥ 5 người, mỗi người chơi liên tục ≥ 20 phút không cần hướng dẫn trực tiếp ngoài 1 trang giới thiệu.
- [ ] Đa số (định lượng trước: ≥ 4/5) nói rằng thao tác chăm đệ tử "có việc để làm" và không quá tải với 6 đệ tử.
- [ ] Không có nhu cầu nào bị đánh giá "vô nghĩa" hay "quá phiền".
- [ ] Hiệu năng đạt ngưỡng P0 với ~6 đệ tử.
- [ ] Báo cáo go/no-go: go, hoặc ghi rõ điều chỉnh thiết kế (có thể quay lại sửa GDD §2.1).

## Rủi ro
| Rủi ro | Giảm thiểu |
|---|---|
| Quản lý thủ công mệt hoặc chán (đã biết từ review EHT) | Đây chính là thứ cần kiểm chứng; thử sớm thao tác chọn nhiều |
| Mải làm đẹp thay vì kiểm chứng | Art tạm, khoá phạm vi theo bảng trên |

## Cắt giảm được
Tâm trạng/Trà Lâu có thể hoãn sang P2 nếu 3 nhu cầu còn lại đã đủ đánh giá.

## Ngoài phạm vi
Mọi thứ ở cột "Không" bên trên.
