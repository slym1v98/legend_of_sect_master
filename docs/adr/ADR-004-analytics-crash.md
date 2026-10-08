# ADR-004 — Analytics và crash: Firebase Analytics + Crashlytics

**Trạng thái:** Đã chốt (người quyết định chọn phương án A)
**Phase:** 0 — Tiền sản xuất (quyết định; tích hợp từ Phase 1-2)
**Liên quan:** ADR-003, GDD §8; `phases/phase-1-prototype.md`, `phases/phase-2-vertical-slice.md`

## Quyết định

Dùng **Firebase Analytics** + **Crashlytics** (cùng SDK với ADR-003).

## Lý do

- Một SDK cho auth, analytics, crash; ít phụ thuộc.
- Miễn phí; đủ funnel, cohort D1/D7/D30, sự kiện tuỳ biến — các KPI ở GDD §8.
- Crashlytics cho chỉ số crash-free (mục tiêu ≥ 99% ở P4).

## Sự kiện tối thiểu (khung, mở rộng theo phase)

| Phase | Sự kiện |
|---|---|
| P1 | `session_start/end`, `need_depleted{need}`, `action_manual{type}`, `dispatch_hunt` |
| P2 | `tutorial_step{id}`, `tutorial_complete`, `craft_start/finish`, `order_placed`, `dungeon_enter{floor}`, `fog_cleared{zone}` |
| P3 | `tribulation_start/result`, `realm_unlocked`, `cloud_save_conflict` |
| P4 | `gacha_pull{banner,rarity}`, `iap_purchase{sku}`, `rewarded_ad{placement}`, `leaderboard_submit` |

Tên sự kiện dùng `snake_case`, tham số kiểu cố định, ghi trong một file danh mục (tạo ở P1) để không trôi.

## Nguyên tắc

- Không thu thập dữ liệu cá nhân ngoài ID ẩn danh; có chọn đồng ý theo quy định vùng (hoàn thiện ở P4).
- P1 (nội bộ) log phục vụ playtest; có thể ghi thêm ra file cục bộ để xem nhanh không cần mạng.
- Dữ liệu phễu monetization ở P4; cần phân tích sâu thì xuất sang BigQuery.

## Đánh đổi chấp nhận

- Dashboard game (economy/progression) kém chuyên dụng hơn GameAnalytics.
- Giới hạn số tham số/sự kiện tuỳ biến của Firebase; thiết kế sự kiện gọn.

## Điều kiện xem xét lại

Cần dashboard economy chuyên sâu mà BigQuery + công cụ tự dựng không đáp ứng được trong P4.
