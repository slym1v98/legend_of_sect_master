# Phase 0 — Tiền sản xuất

**Mục tiêu:** Chốt các quyết định kỹ thuật và sản xuất còn bỏ ngỏ để Phase 1 bắt đầu mà không phải đổi hướng.
**GDD liên quan:** §1.1, §4, §5, §6, §9.

## Phạm vi

Quyết định và thử nghiệm bỏ đi. **Không** có code giữ lại, không có tính năng phát hành.

## Hạng mục theo workstream

### Kỹ thuật (quyết định)
- Chọn **engine** (ứng viên: Unity, Godot). Tiêu chí: 2D isometric trên mobile, tilemap/depth sort, hiệu năng thiết bị tầm thấp, kinh nghiệm team, chi phí/giấy phép.
- Chọn **backend** cho online nhẹ: auth, cloud save, bảng xếp hạng tuần. Tiêu chí: chi phí nhỏ, không tự dựng server, chống gian lận mức cơ bản.
- Chọn **analytics/crash** SDK.
- Chốt **nền tảng mục tiêu đầu tiên** (Android trước hay cả iOS) và cấu hình thiết bị tối thiểu.

### Spike kỹ thuật (đo được, bỏ sau khi trả lời)
- Isometric: lưới 2:1, đặt/di chuyển công trình, depth sort, công trình trong suốt khi đệ tử đứng sau. Câu hỏi: có đạt 60fps với ~30 đệ tử + ~25 công trình trên thiết bị tầm thấp?
- AI đệ tử: ~30 tác nhân tự tìm đường tới công trình. Câu hỏi: chi phí pathfinding?
- Save/load: tuần tự hoá trạng thái tông môn. Câu hỏi: kích thước, thời gian, khả năng migrate phiên bản.

### Kinh tế / Balance
- Bảng tính khung: nguồn và vòng chảy Vàng, Linh Thạch, Điểm Đạo Vận (GDD §2.5).
- Thời gian mục tiêu: Độ Kiếp lần đầu ≤ 8 giờ; hết cõi Địa 40-80 giờ (GDD §8). Dựng mô hình ngược từ hai mốc này.
- Tham chiếu số liệu EHT (cấp, tier, giá) để làm điểm xuất phát; ghi nguồn.

### Art
- Thử phong cách: 1 đệ tử (4 chức nghiệp khung chung), 3 công trình, 1 khối đất có linh mạch, bảng màu (GDD §4.1).
- Ước lượng chi phí asset: số sprite/công trình/đệ tử/yêu thú cho EA đầy đủ.
- Chốt pipeline: công cụ pixel art, quy cách xuất, quy ước đặt tên, kích thước ô lưới.

### Sản xuất
- Danh sách thuật ngữ Hán-Việt thống nhất (tên công trình, tiền, trạng thái) — làm nguồn cho localization sau này.
- Quyết định cấu trúc repo, quy trình build, nhánh.
- Rà pháp lý: tên game, nhận diện, đối chiếu EHT để không sao chép tài sản (chỉ mượn cơ chế).

## Deliverables
1. Tài liệu quyết định engine/backend/analytics (ADR ngắn mỗi quyết định).
2. Kết quả spike isometric / AI / save (số đo + kết luận).
3. Bảng tính kinh tế khung.
4. Gói thử phong cách art + ước lượng asset.
5. Bảng thuật ngữ.

## Exit criteria
- [ ] Engine và backend đã chốt, có ADR.
- [ ] Spike isometric đạt ngưỡng hiệu năng đã đặt trước trên thiết bị tối thiểu (ngưỡng ghi trong ADR).
- [ ] Bảng kinh tế khung cho ra đúng hai mốc 8 giờ và 40-80 giờ trong mô hình.
- [ ] Ước lượng asset cho EA hoàn chỉnh vừa nguồn lực; nếu không, đã quyết cắt scope (xem bên dưới).
- [ ] Người quyết định duyệt phong cách art.

## Rủi ro
| Rủi ro | Giảm thiểu |
|---|---|
| Chọn engine sai, đổi giữa chừng | Spike thật trên thiết bị tầm thấp trước khi chốt |
| Ước lượng asset vượt sức | Cắt theo thứ tự ở dưới trước khi vào P1 |
| Mô hình kinh tế không chạm 2 mốc | Phát hiện sớm ở đây, rẻ hơn sửa sau |

## Cắt giảm được
Giảm số vùng sương mù mỗi cõi; giảm số tier trang bị; giảm số kiểu yêu thú dùng chung sprite biến thể màu.

## Ngoài phạm vi
Mọi tính năng chơi được; monetization; online thật.
