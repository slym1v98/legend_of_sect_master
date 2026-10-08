# ADR-002 — Thiết bị tối thiểu và ngưỡng hiệu năng

**Trạng thái:** Đã chốt (người quyết định chọn phương án A)
**Phase:** 0 — Tiền sản xuất
**Liên quan:** ADR-001, GDD §4, `phases/phase-0-preproduction.md`

## Quyết định

**Android trước; iOS sau Early Access** (xem lại ở Phase 5).

## Thiết bị tối thiểu (chuẩn đo)

| Hạng mục | Giá trị |
|---|---|
| OS | Android 8.0+ (API 26) |
| RAM | 3 GB |
| Chip | Tầm thấp (loại Snapdragon 600-series / MediaTek Helio G-series) |
| Màn hình | Dọc, tới 720p là mức chuẩn đo |

Chọn **một máy thật** đại diện làm chuẩn đo và ghi model vào "Máy chuẩn" bên dưới. Không dùng emulator để kết luận hiệu năng.

## Ngưỡng hiệu năng (cảnh tông môn đầy)

Cảnh đo: **30 đệ tử, 25 công trình**, camera di chuyển/zoom, combat ngoài thành tắt.

| Chỉ số | Ngưỡng đạt |
|---|---|
| FPS | ≥ 30 ổn định (p5 ≥ 28), mục tiêu thiết kế 60 trên máy khá |
| RAM | ≤ 1 GB |
| Khởi động lạnh tới màn chơi | ≤ 8 s |
| Dung lượng cài | Mục tiêu ≤ 150 MB cho EA (đo lại ở P2/P3) |
| Pin | Không đo ở P0; bắt đầu theo dõi từ P2 |

Spike P0 đạt khi mọi chỉ số bảng trên đạt trên máy chuẩn. Mức bảng này là điểm khởi đầu, chỉnh lại có ghi lý do.

## Cách đo

- Unity Profiler kết nối qua `adb`; ghi FPS trung bình + p5 trong 60 giây.
- RAM qua Profiler Memory và `adb shell dumpsys meminfo`.
- Khởi động: đo từ chạm icon tới màn chơi, trung bình 5 lần cold start.
- Lưu số đo vào `docs/spikes/` (một file mỗi spike).

## Đánh đổi chấp nhận

- iOS chậm: người chơi iOS (thường doanh thu cao hơn) vào sau EA.
- Android phân mảnh: dùng một máy chuẩn và bổ sung vài máy khác ở P2.

## Máy chuẩn

_Chưa chọn. Điền model + RAM + chip + Android khi có máy._

## Điều kiện xem xét lại

Dữ liệu thị trường mục tiêu cho thấy cần iOS trước EA; hoặc ngưỡng 30fps/1GB không thể đạt sau tối ưu hợp lý.
