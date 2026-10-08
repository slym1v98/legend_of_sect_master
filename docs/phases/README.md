# Kế hoạch phase — LegendOfSectMaster

Nguồn: [`../GDD.md`](../GDD.md) (§7.3 lộ trình). Kế hoạch cấp milestone, **không có lịch**, **không phải task code**. Mỗi phase kết thúc bằng exit criteria kiểm chứng được; chưa đạt thì chưa sang phase sau.

## Tổng quan

| Phase | Tên | Mục tiêu một dòng | Câu hỏi phải trả lời |
|---|---|---|---|
| 0 | [Tiền sản xuất](phase-0-preproduction.md) | Chốt engine, backend, art pipeline, bảng kinh tế khung | Làm được bằng công cụ nào, với chi phí asset nào? |
| 1 | [Prototype](phase-1-prototype.md) | Lưới isometric + 1 đệ tử + nhu cầu + 1 vùng săn | Quản lý thủ công nhu cầu có vui không? |
| 2 | [Vertical slice](phase-2-vertical-slice.md) | Chuỗi cung ứng đầy đủ cõi Phàm, chất lượng gần bản phát hành | Vòng lặp lõi 1-2 giờ đầu có cuốn không? |
| 3 | [Alpha](phase-3-alpha.md) | Đủ 3 cõi, Bí Cảnh 25 tầng, Độ Kiếp, ba hệ thống đặc trưng | Nội dung đủ 40-80 giờ chưa? Có đủ khác EHT? |
| 4 | [Beta kín](phase-4-closed-beta.md) | Online nhẹ, monetization, cân bằng bằng dữ liệu thật | KPI giữ chân và kinh tế có đạt không? |
| 5 | [Early Access](phase-5-early-access.md) | Phát hành, vận hành, đo KPI | Phản hồi thị trường, ưu tiên post-EA |

## Quy ước chung

- **Workstream:** Gameplay · Kinh tế/Balance · Art/Animation · UI/UX · Backend/Online · QA/Analytics · Monetization.
- **Cổng phase:** hết phase chỉ sang phase sau khi mọi exit criteria đạt, hoặc người quyết định ghi lại ngoại lệ có lý do.
- **Cắt giảm:** nếu trễ, cắt theo thứ tự ở mục "Cắt giảm được" của từng phase; không cắt trụ cột GDD §1.4.
- **Con số:** mọi số liệu là điểm khởi đầu (GDD §9), chốt bằng playtest.
- **Đo được:** exit criteria nào cần số liệu thì ghi rõ cách đo.

## Phụ thuộc giữa phase

```
P0 ──▶ P1 ──▶ P2 ──▶ P3 ──▶ P4 ──▶ P5
        │      │       │
        │      │       └─ backend khung bắt đầu từ P3
        │      └─ khoá art style + UI kit ở P2
        └─ bỏ dự án nếu quản lý thủ công không vui (cổng go/no-go)
```
