# ADR-001 — Engine: Unity

**Trạng thái:** Đã chốt (người quyết định chọn trực tiếp)
**Phase:** 0 — Tiền sản xuất
**Liên quan:** GDD §1.1, §4; `phases/phase-0-preproduction.md`

## Bối cảnh

Mobile F2P + IAP, 2D pixel art isometric, ~30 đệ tử tự tìm đường + ~25 công trình, online nhẹ. Cần hệ sinh thái IAP/ads/analytics chín muồi.

## Quyết định

Dùng **Unity** (2D, URP 2D). Phiên bản **LTS** được chọn khi cài, ghi vào mục "Phiên bản" bên dưới.

## Lý do

- Hệ sinh thái mobile F2P chín nhất: IAP, ads thưởng, analytics, Google Play Games, tài liệu nhiều.
- Có sẵn Isometric Tilemap và 2D tooling.
- Unity Hub đã có trên máy dev.

## Đánh đổi chấp nhận

- Nặng hơn Godot; build và editor chậm hơn.
- Isometric depth sort, công trình trong suốt khi bị che phải tự dựng (đưa vào spike).
- Điều khoản giấy phép/phí: phải kiểm tra điều khoản hiện hành tại thời điểm chốt phiên bản và sau mỗi lần nâng cấp lớn.

## Việc kéo theo (Phase 0)

- [ ] Cài Unity LTS + Android Build Support; điền phiên bản vào đây.
- [ ] Spike isometric (lưới 2:1, đặt/di chuyển công trình, depth sort, trong suốt khi bị che) với ngưỡng hiệu năng ghi trong ADR-002.
- [ ] Spike AI ~30 tác nhân, spike save/load.
- [ ] ADR-002: thiết bị tối thiểu + ngưỡng hiệu năng. ADR-003: backend. ADR-004: analytics/crash.

## Phiên bản

_Chưa cài._

## Điều kiện xem xét lại

Spike isometric không đạt ngưỡng hiệu năng trên thiết bị tối thiểu sau tối ưu hợp lý, hoặc điều khoản giấy phép thay đổi bất lợi.
