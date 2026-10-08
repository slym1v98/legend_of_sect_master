# Nghiên cứu: dùng AI tạo ảnh (OpenAI / Google) làm asset

**Ngày:** 2026-10-08. **Phase 0.** Liên quan: ADR-005, `docs/content/content.md` (số đếm asset), `docs/name-and-competitor-review.md`.

**Giới hạn của nghiên cứu này:** đọc tài liệu chính thức và vài nguồn pháp lý/chính sách; **chưa tạo ảnh nào, chưa thử pipeline**. Một số lượt tìm bị giới hạn tốc độ nên **không tìm được báo cáo thực tế độc lập** về pixel art isometric của từng mô hình. Không phải tư vấn pháp lý. Tên mô hình đổi rất nhanh; kiểm lại trước khi dùng.

## 1. Kết luận ngắn

1. **Dùng được, nhưng không thay hoàn toàn họa sĩ.** Hợp nhất cho concept và biểu tượng (khoảng 165 icon); kém tin cậy nhất cho **hoạt hoạ nhân vật nhất quán** và **hình học isometric chính xác**.
2. **Vấn đề lớn nhất là pháp lý, không phải kỹ thuật:** asset hoàn toàn do AI sinh **không được bảo hộ bản quyền** theo luật Hoa Kỳ hiện hành → ai cũng có thể sao chép sprite của ta. Với một thị trường đã có đối thủ gần (xem `name-and-competitor-review.md`), đây là rủi ro sản phẩm thật.
3. **Phải khai báo** trên Steam (nội dung AI đi kèm game, kể cả ảnh cửa hàng) và Google Play (ảnh cửa hàng/quảng bá). Steam có thể từ chối dù đã khai báo.
4. **Chưa có bằng chứng** về chất lượng pixel art. Cần pilot nhỏ (mục 7) trước khi quyết.

## 2. Đã xác minh và chưa xác minh

| Điều | Trạng thái | Nguồn |
|---|---|---|
| OpenAI: `gpt-image-2` **không hỗ trợ nền trong suốt** | Đã xác minh | Tài liệu OpenAI |
| OpenAI: tự nhận **hạn chế nhất quán** nhân vật lặp lại và **kiểm soát bố cục** | Đã xác minh | Tài liệu OpenAI |
| OpenAI: cần xác minh tổ chức (Organization Verification) để dùng mô hình ảnh | Đã xác minh | Tài liệu OpenAI |
| OpenAI: sửa ảnh theo mask chỉ là hướng dẫn qua prompt, "có thể không theo đúng hình" | Đã xác minh | Tài liệu OpenAI |
| OpenAI: kích thước tuỳ ý, bội số 16px, tối đa 3840px, tỉ lệ dài/ngắn ≤ 3:1 | Đã xác minh | Tài liệu OpenAI |
| Google: mọi ảnh sinh ra có **watermark SynthID** | Đã xác minh | Tài liệu Gemini API |
| Google: hỗ trợ ảnh tham chiếu đa ảnh cho nhất quán nhân vật | Đã xác minh | Tài liệu Google |
| Google: ví dụ isometric trong tài liệu là **3D miniature**, không phải pixel art | Đã xác minh | Tài liệu Gemini API |
| Giá theo ảnh của cả hai | **Chưa xác minh** | — |
| Nền trong suốt của mô hình Google và của `gpt-image-1.x` | **Chưa xác minh** | — |
| Chất lượng pixel art isometric của cả hai | **Chưa xác minh** | — |
| Điều khoản sở hữu đầu ra của OpenAI/Google cho dùng thương mại | **Chưa xác minh** (chỉ đọc được đoạn rời) | — |
| Luật Việt Nam về bản quyền sản phẩm AI | **Không nghiên cứu** | — |

Ghi chú nguồn: một trang tiếp thị bên thứ ba quảng cáo "nhất quán 90-95%" cho mô hình Google. Đó là quảng cáo, **không** dùng làm bằng chứng.

## 3. Kỹ thuật

### 3.1 Điểm yếu chung của mô hình sinh ảnh với pixel art

- Mô hình vẽ ảnh liên tục, **không** căn theo lưới pixel. Đầu ra "giống pixel art" thường có pixel lệch kích thước, viền mờ, màu thừa. Cần hậu xử lý: hạ về độ phân giải mục tiêu bằng nearest-neighbor, ép về bảng màu cố định.
- Nền trong suốt: OpenAI `gpt-image-2` không có. Cách khắc phục: sinh trên nền một màu phẳng rồi tách (chroma key).
- Isometric 2:1 cần hình học chính xác (hộp 2:1, ô lưới khớp). Cả hai hãng đều **tự nhận** điều khiển bố cục yếu; công trình sẽ cần chỉnh tay để khớp ô.
- **Nhất quán** (cùng bảng màu, cùng nét, cùng góc nhìn qua 63 công trình, 36 yêu thú) là điểm yếu được OpenAI tự nêu. Cần bộ ảnh tham chiếu phong cách và kiểm tra thủ công từng ảnh.

### 3.2 Tham chiếu một pipeline có sẵn

Có một plugin Godot mã nguồn mở dùng Gemini cho pixel art với pipeline: ép bảng màu → sinh → hạ về độ phân giải đích → chỉnh nhiều lượt. Dùng làm ý tưởng pipeline (một dự án đơn lẻ, **không** phải bằng chứng chất lượng). Ta dùng Unity nên không dùng được plugin này, chỉ học cách làm.

### 3.3 Pipeline đề xuất (nếu pilot đạt)

```
Ảnh tham chiếu phong cách + bảng màu cố định (do họa sĩ chốt)
  → sinh trên nền một màu phẳng, kích thước lớn
  → tách nền (chroma key)
  → hạ về kích thước pixel mục tiêu (nearest-neighbor)
  → ép về bảng màu
  → họa sĩ chỉnh tay (viền, ô lưới, bóng)
  → vào Unity
```

Mỗi bước sau "sinh" có thể viết thành script trong `tools/` (Python, Pillow) để lặp lại được.

## 4. Bản quyền

- Cục Bản quyền Hoa Kỳ: bảo hộ cần **tác giả là con người**; nếu các yếu tố sáng tạo truyền thống do máy tạo ra thì tác phẩm không đủ điều kiện đăng ký. Phần do con người **chỉnh sửa hoặc sắp xếp đủ sáng tạo** có thể được bảo hộ, chỉ cho **phần đóng góp của con người** (Registration Guidance 2023; báo cáo Part 2 về khả năng bảo hộ, 2025).
- Hệ quả thực tế:
  - Sprite **hoàn toàn do AI** → không có bản quyền → bên khác sao chép được.
  - Sprite **AI + họa sĩ chỉnh sửa đáng kể** → bảo hộ một phần, ranh giới mơ hồ, chưa có ngưỡng rõ.
  - **Mã, thiết kế hệ thống, âm thanh, tên, cốt truyện do người viết** vẫn được bảo hộ bình thường; rủi ro chỉ ở hình ảnh AI.
- Bài của một văn phòng luật còn nêu: nhà thầu dùng AI có thể khiến điều khoản chuyển giao quyền "chuyển giao không có gì". Nếu thuê họa sĩ ngoài, hợp đồng phải quy định rõ việc dùng AI.
- **Việc cần làm nếu dùng AI:** lưu **nguồn gốc từng asset** (prompt, ảnh gốc AI, các bản chỉnh, bản cuối), vì có thể cần chứng minh phần đóng góp người.
- **Luật Việt Nam và thị trường mục tiêu: chưa nghiên cứu.** Cần hỏi luật sư sở hữu trí tuệ trước P4.

## 5. Chính sách cửa hàng

| Cửa hàng | Yêu cầu | Ghi chú |
|---|---|---|
| **Steam** | Bắt buộc khai báo nội dung AI **đi kèm game** và **tiêu thụ bởi người chơi** (hình, âm, văn bản), **gồm cả trang cửa hàng và tài liệu quảng bá**. Hiển thị công khai ở "About This Game". Công cụ hỗ trợ lập trình và concept không phát hành thì **không** phải khai | Chính sách viết lại 01/2026. Valve **có thể từ chối** dù đã khai báo (ví dụ lo ngại nguồn dữ liệu huấn luyện). Bạn **tự chịu** trách nhiệm không vi phạm bản quyền |
| **Google Play** | Tự khai báo từng **asset hình ảnh/video của trang cửa hàng và quảng bá** (Play Console); asset khai sẽ được gắn nhãn AI | Chính sách "AI-Generated Content" của Play nhắm vào **ứng dụng sinh nội dung bằng AI lúc chạy**; game với asset tạo sẵn không rơi vào đó. Art **trong game** không thấy yêu cầu riêng trong nguồn đọc được |
| **Apple App Store** | Nguồn thứ cấp (2025): chưa có yêu cầu riêng | **Chưa xác minh bằng nguồn chính thức** |

Dự án nhắm mobile (Google Play trước, ADR-002). Steam chỉ khi cân nhắc PC sau EA. Dù vậy cần thận trọng: người chơi và cộng đồng game có thể phản ứng với nhãn AI, nhất là thể loại có nhiều họa sĩ pixel art.

## 6. Phân loại asset (số đếm từ `content.md`)

| Nhóm | Số lượng | Hợp AI? | Lý do |
|---|---|---|---|
| Concept, bảng tâm trạng, ý tưởng | — | **Hợp** | Không phát hành thì không phải khai báo Steam, không ảnh hưởng bản quyền sản phẩm |
| Icon vật liệu / trang bị / tiêu hao | 69 + 60 + 36 = **165** | **Hợp nhất** | Nhỏ, độc lập, ít cần nhất quán chuyển động; hệ ngũ hành bằng đổi bảng màu |
| Sprite công trình tĩnh | 63 (+ 21 lớp phủ) | **Một phần** | Cần khớp ô lưới 2:1 và nhất quán phong cách; AI cho bản nháp, người chỉnh |
| Yêu thú | 36 thiết kế (≥ 50% biến thể màu) | **Một phần** | Thiết kế gốc dùng được; biến thể làm bằng bảng màu, không cần AI |
| Nền địa hình, vật trang trí | Chưa đếm | **Một phần** | Cần ghép khít, tile |
| Nhân vật đệ tử, hoạt hoạ | 4 chức nghiệp × ~10 hoạt hoạ × 2 hướng | **Kém hợp** | Nhất quán khung này qua khung khác và qua hoạt hoạ là điểm yếu được nêu rõ |
| Hiệu ứng công pháp | 20 | **Kém hợp** | Chuyển động, nhiều khung |
| UI kit | Chưa đếm | **Kém hợp** | Cần chính xác, nhất quán, chữ |

## 7. Pilot đề xuất (rẻ, quyết định bằng dữ liệu)

**Mục tiêu:** trả lời "AI tạo ra bao nhiêu phần trăm công việc dùng được" trước khi cam kết.

| Thử nghiệm | Nội dung | Tiêu chí đạt (gợi ý, do tôi đặt) |
|---|---|---|
| A. Icon | 12 icon (4 vật liệu, 4 trang bị, 4 tiêu hao), cùng bảng màu | ≥ 60% icon dùng được sau tối đa 3 lần sinh; 2 người duyệt nhận xét cùng một phong cách |
| B. Công trình | 3 công trình (2×2, 3×3, 4×3) theo ô 2:1 | Sau hậu xử lý + chỉnh tay hợp lý, khớp ô lưới và đặt cạnh nhau trên lưới Unity không lộ khác phong cách |
| C. Nhân vật | 1 đệ tử: tư thế đứng 4 hướng/2 hướng, cùng một nhân vật | Nhận ra là cùng một nhân vật; nếu không → AI bị loại khỏi nhân vật |
| D. So thời gian | Cùng 12 icon do họa sĩ vẽ tay | So tổng thời gian kể cả chỉnh sửa; AI chỉ đáng dùng nếu rẻ hơn rõ rệt |

Chạy trên **cả hai hãng** với cùng prompt, cùng bảng màu. Ghi vào `docs/spikes/`. Cần: API key (OpenAI cần xác minh tổ chức) và **một người có mắt pixel art** để chấm.

## 8. Quyết định cần người quyết định

1. **Chấp nhận rủi ro bản quyền** của asset AI không? Cụ thể: icon bị sao chép thì chấp nhận được; còn nhân vật, công trình đặc trưng thì sao?
2. **Phạm vi AI:** chỉ concept + icon, hay thêm công trình/yêu thú? (Khuyến nghị: bắt đầu concept + icon, mở rộng theo kết quả pilot.)
3. **Công khai nhãn AI** trên cửa hàng: chấp nhận không?
4. **Hợp đồng nhà thầu** (nếu thuê ngoài): cấm hay cho phép AI, bắt buộc khai báo.
5. **Ai chạy pilot** (cần API key và người chấm).

## Nguồn

- Tài liệu OpenAI Image generation: platform.openai.com/docs/guides/image-generation
- Tài liệu Gemini API image generation: ai.google.dev/gemini-api/docs/image-generation
- US Copyright Office: Registration Guidance (Federal Register, 2023-03-16); *Copyright and Artificial Intelligence, Part 2: Copyrightability* (2025)
- CRS: *Generative AI and Copyright Law* (LSB10922)
- Steamworks Content Survey (partner.steamgames.com/doc/gettingstarted/contentsurvey)
- Google Play: *Declaring AI-generated content in Play Console*; *AI-Generated Content policy*
- Bài tổng hợp: promise.legal (2026-05-05); legalmoveslawfirm.com (2026-03-05) — **nguồn thứ cấp**, dùng để định hướng, chưa phải căn cứ pháp lý
- SynidSweet/godot-ai-image-generator (GitHub): chỉ để tham khảo pipeline
