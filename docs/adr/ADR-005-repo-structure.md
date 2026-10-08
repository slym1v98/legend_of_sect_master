# ADR-005 — Cấu trúc repo

**Trạng thái:** Đề xuất mặc định (chưa có phản đối); đổi được trước khi tạo project Unity
**Phase:** 0 — Tiền sản xuất
**Liên quan:** ADR-001, `phases/phase-0-preproduction.md`

## Quyết định

Một repo (monorepo). **Project Unity nằm trong `game/`**, không ở gốc.

```
LegendOfSectMaster/
├── docs/            GDD, phases, ADR, economy, glossary (đã có)
├── game/            Project Unity (tạo ở bước spike; thư mục này chưa tồn tại)
├── tools/           Script hỗ trợ ngoài Unity (mô hình kinh tế, kiểm dữ liệu...) — tạo khi cần
├── .gitignore       Quy tắc Unity bắt đầu bằng game/
├── .gitattributes   Chuẩn hoá dòng, đánh dấu nhị phân
└── README.md
```

Không tạo thư mục rỗng trước khi có nội dung.

## Lý do

- Docs và công cụ sống chung, không lẫn vào `Assets/`.
- Unity ở thư mục con để mở rộng (backend Cloud Functions ở P3-P4 có thể thêm `backend/` cạnh `game/`).
- Một lịch sử commit gắn tài liệu với code.

## Quy ước

- **Nhánh:** `main` luôn build được từ P1 trở đi; việc mới trên nhánh `feat/<tên>`; gộp qua pull request.
- **Commit:** tiếng Anh, tiền tố `feat:` `fix:` `docs:` `chore:`; một thay đổi logic mỗi commit.
- **Unity:** bật Visible Meta Files + Force Text serialization (mặc định); commit `.meta` cùng asset.
- **Tên định danh code:** theo `docs/glossary.md`.
- **Bí mật:** keystore, khoá ký, `.env` không bao giờ vào repo (đã chặn trong `.gitignore`). Quyết định `google-services.json` (ADR-003) khi tích hợp Firebase.

## Việc chờ

- [ ] **Cài `git-lfs`** (cần quyền quản trị hệ thống, người dùng tự chạy) rồi `git lfs track` cho `*.psd *.aseprite *.wav *.ogg *.mp3`. Làm trước khi commit asset nhị phân lớn đầu tiên; sau đó mới đưa LFS vào `.gitattributes`.
- [ ] Tạo project Unity vào `game/` khi bắt đầu spike (ADR-001 chọn LTS).
- [ ] Cân nhắc CI build Android từ P1-P2.

## Đánh đổi

Monorepo lớn dần khi có asset; LFS giảm nhẹ. Nếu art tách đội/ngoài, xét lại để tách repo asset.

## Điều kiện xem xét lại

Backend hoặc art cần quyền truy cập/nhịp phát hành độc lập.
