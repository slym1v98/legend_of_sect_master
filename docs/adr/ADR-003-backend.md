# ADR-003 — Backend: Firebase

**Trạng thái:** Đã chốt (người quyết định chọn phương án A)
**Phase:** 0 — Tiền sản xuất (chỉ quyết định; triển khai từ Phase 3)
**Liên quan:** ADR-001, GDD §5, §6; `phases/phase-3-alpha.md`, `phases/phase-4-closed-beta.md`

## Bối cảnh

Online nhẹ (GDD §5.1): tài khoản, cloud save, bảng xếp hạng tuần, sự kiện theo lịch. Không PvP, không guild, không real-time. Game chính chạy local.

## Quyết định

Dùng **Firebase**:

| Nhu cầu | Dịch vụ |
|---|---|
| Tài khoản | Authentication (ẩn danh trước, liên kết Google Sign-In sau) |
| Cloud save | Firestore (một document/người chơi; có trường phiên bản save) |
| Bảng xếp hạng tuần | Firestore + Cloud Functions (xác thực và ghi điểm) |
| Sự kiện/tham số theo lịch | Remote Config |
| Crash | Crashlytics (xem ADR-004) |

## Lý do

- SDK Unity chính thức, tài liệu nhiều.
- Tài khoản ẩn danh giảm rào cản; liên kết sau để không mất tiến trình khi đổi máy.
- Trả theo mức dùng, tầng free đủ cho beta kín.
- Không tự dựng/vận hành server.

## Nguyên tắc dữ liệu

- Client **không** tự ghi điểm xếp hạng: gửi bản tóm tắt tiến trình lên Cloud Function, function kiểm tra hợp lệ rồi ghi. Mức xác thực cơ bản ở P4.
- Save có `schemaVersion`; migrate được giữa các bản.
- Xung đột nhiều thiết bị: ghi kèm `updatedAt` + `deviceId`, hỏi người chơi chọn bản khi lệch (xử lý ở P3).
- Chỉ lưu dữ liệu tối thiểu cho gameplay; chính sách quyền riêng tư ở P4.

## Đánh đổi chấp nhận

- Khoá vào hệ Google; chuyển đi sau cần viết lớp tách (giữ truy cập qua một interface mỏng ở client).
- Chi phí đọc/ghi Firestore tăng theo người chơi; cần ngân sách và cảnh báo chi phí từ P4.
- Firebase có độ trễ/hạn mức; không dùng cho gameplay thời gian thực (đã ngoài phạm vi).

## Việc kéo theo

- [ ] P0: không dựng backend; chỉ xác nhận SDK Unity tương thích phiên bản Unity đã chọn (ghi vào ADR-001).
- [ ] P3: tài khoản + cloud save. P4: bảng xếp hạng, Remote Config.

## Điều kiện xem xét lại

Chi phí dự báo vượt ngân sách; yêu cầu real-time (PvP/guild) vào roadmap; hoặc hạn chế khu vực/pháp lý với Google ở thị trường mục tiêu.
