# GDD — LegendOfSectMaster

**Phiên bản:** 0.1 — Early Access Scope
**Trạng thái:** Đã duyệt thiết kế theo phần, chờ review file
**Chỉ dẫn sản xuất:** Tài liệu tổng quát, chưa triển khai

---

## 1. Tổng quan

### 1.1 Định danh

| Hạng mục | Nội dung |
|---|---|
| Tên | LegendOfSectMaster |
| Thể loại | Quản lý vi mô (tycoon) + RPG, isometric |
| Nền tảng | Mobile (dọc), F2P + IAP |
| Bối cảnh | Thế giới tu tiên |
| Tham khảo lối chơi | Evil Hunter Tycoon (Super Planet) |
| Dựng hình | Pixel art chibi isometric |
| Mạng lưới | Single-player + bảng xếp hạng online nhẹ |
| Mô hình phát hành | Early Access (mobile: soft-launch → mở rộng) |

### 1.2 Tagline

Dựng tông môn từ phế tích, nuôi đệ tử, độ kiếp, trở thành Đệ Nhất Tông.

### 1.3 Fantasy cốt lõi

Người chơi là **Tông Chủ**, không phải anh hùng. Bạn không tự tay đánh. Bạn **cung cấp** — đan dược, pháp khí, cơm nước, chỗ nghỉ — và đệ tử tự đi chinh chiến. Thắng lợi của tông môn là thắng lợi của bạn cung cấp đúng lúc.

### 1.4 Trụ cột thiết kế

1. **Quản lý vi mô có ý nghĩa.** Mỗi đệ tử có nhu cầu thật (đói, mệt, thương, tâm trạng) và người chơi tự điều — không auto-admin.
2. **Chuỗi cung ứng khép kín.** Đệ tử săn vật liệu → người chơi mua qua Tụ Bảo Các → chế tác → bán lại cho đệ tử. Vòng tiền nhỏ, rõ ràng, luôn có việc để làm.
3. **Tu tiên có chiều sâu.** Linh căn ngũ hành, linh mạch, độ kiếp là khác biệt thật so với EHT — không chỉ đổi tên.

### 1.5 Vòng lặp lõi

```
Đệ tử săn yêu thú ở vùng đã dọn sương
  → rơi vật liệu → đệ tử bán qua Tụ Bảo Các (theo đơn người chơi đặt)
  → người chơi luyện khí / luyện đan / nấu linh thiện
  → bán lại cho đệ tử (thu Linh Thạch)
  → đệ tử mạnh hơn → dọn sương vùng mới, vào bí cảnh sâu hơn
  → đủ cấp → độ kiếp (tái sinh) → mạnh vĩnh viễn → lặp lại
```

### 1.6 Ánh xạ Evil Hunter Tycoon → LegendOfSectMaster

| Evil Hunter Tycoon | LegendOfSectMaster |
|---|---|
| Town / Town Chief | Tông Môn / Tông Chủ |
| Hunter (4 class, tier, trait ngẫu nhiên) | Đệ tử (4 chức nghiệp, tư chất, linh căn) |
| Town Hall | Đại Điện |
| Trading Post | Tụ Bảo Các |
| Blacksmith | Luyện Khí Phòng |
| Alchemist | Đan Phòng |
| Jeweler | Pháp Bảo Các |
| Weapon / Armor / Potion / Accessory Shop | Quầy bán tương ứng |
| Inn | Tĩnh Thất |
| Restaurant | Linh Thiện Đường |
| Infirmary | Y Đường |
| Tavern | Trà Lâu |
| Academy | Truyền Công Các |
| Bounty Hut | Nhiệm Vụ Đường |
| Training Ground | Luyện Công Trường |
| Enhancement Forge | Cường Hoá Lô |
| Sanctuary of Resurrection | Luân Hồi Trì |
| Dungeon (25 tầng) | Bí Cảnh (25 tầng) |
| Field Boss / Boss Horn | Yêu Vương / Triệu Yêu Linh |
| Reincarnation | Độ Kiếp |
| Difficulty modes | Sương mù bản đồ (3 cõi: Phàm → Linh → Địa) |

Nguyên tắc: giữ nguyên khung thành công của EHT, thay toàn bộ lớp vỏ bằng tu tiên, thêm 3 hệ thống đặc trưng (§2.4) và bỏ hệ thống chuyển độ khó (thay bằng dọn sương mù — §3).

---

## 2. Hệ thống lõi

### 2.1 Đệ tử

#### Tuyển mộ

- Đệ tử tự ghé xin vào định kỳ với tần suất thấp (phần lớn tư chất thấp).
- **Bài Trắc Duyên** (gacha) là nguồn tuyển chính: tiêu Linh Thạch hoặc Vé Trắc Duyên.
- Quá mức chỗ ở: không nhận thêm; buộc bãi chức (trục xuất) hoặc nâng cấp nhà ở.

#### Thành phần mỗi đệ tử

| Thành phần | Mô tả |
|---|---|
| Chức nghiệp | Kiếm Tu, Thể Tu, Cung Tu, Pháp Tu (xem mục Chức nghiệp) |
| Tư chất | S / A / B / C — ảnh hưởng tốc độ lên cấp và chỉ số mỗi cấp |
| Linh căn | Ngũ hành: Kim / Mộc / Thuỷ / Hoả / Thổ; tỉ lệ hiếm: **dị linh căn** (2 hệ) |
| Tính cách | Ngẫu nhiên (chăm chỉ, kén ăn, chiến sĩ bẩm sinh…) — ảnh hưởng hành vi và nhu cầu |
| Thiên phú | Dòng đặc biệt cố định theo đệ tử |

#### Nhu cầu & trạng thái (thủ công)

| Nhu cầu | Giảm dần | Hậu quả khi cạn | Hồi phục |
|---|---|---|---|
| Đói | No → Đói | Giảm DPS, từ chối đi đánh | Ăn tại Linh Thiện Đường |
| Thể lực | Đầy → Kiệt | Không ra trận | Nghỉ tại Tĩnh Thất |
| Thương tích | HP cao → 0 | Chết → Luân Hồi Trì (mất Vàng + thời gian chờ) | Chữa tại Y Đường |
| Tâm trạng | Vui → Cáu | Không nhận nhiệm vụ, thao tác chậm | Giải trí tại Trà Lâu |

Thao tác người chơi: bấm đệ tử → menu ngữ cảnh (ăn / nghỉ / chữa / giải trí / giao nhiệm vụ / điều đến vùng / bán vật liệu / trang bị). **Đúng thao tác của EHT — không có auto-admin.**

#### Cấp, đẳng cấp và Độ Kiếp

- Cấp tối đa theo cõi: Phàm 30, Linh 60, Địa 100.
- Đạt cap → mở **Độ Kiếp**: đệ tử đối kháng một trận thiên kiếp ngắn (đánh boss mini, có rủi ro).
  - **Thành công:** reset về cấp 1, nhận **+1 Điểm Đạo Vận**, +10% tiềm năng vĩnh viễn (mọi chỉ số cơ bản).
  - **Thất bại:** đệ tử trọng thương, mất một phần cấp, hồi sau thời gian chờ. **Không mất vĩnh viễn.**
- **Thuốc Kháng Kiếp** (chế tác tại Đan Phòng): giảm tỉ lệ thất bại.
- **Điểm Đạo Vận** dùng mở **Đạo Ấn** (trait): dòng mạnh như "Thuộc tính Hoả +15%", "Hồi thể lực nhanh".
- **Công pháp / Bí thuật** học tại Truyền Công Các — chiếm slot, nâng cấp được.

> Đánh đổi thiết kế: tái sinh kiểu EHT (mất sạch, mạnh lại) là loop nghiện. Giữ loop đó, bỏ hình phạt vĩnh viễn để tránh review xấu F2P.

#### Vai trò ngoài chiến đấu

Đệ tử cũng là cư dân: mang vật liệu về, mua đồ ở quầy, dùng dịch vụ trong tông môn. Nhu cầu của họ chính là doanh thu của người chơi.

#### Chức nghiệp (4)

| Chức nghiệp | Vai trò | Vũ khí chính |
|---|---|---|
| Kiếm Tu | Sát thương cận chiến cân bằng | Kiếm |
| Thể Tu | Tank, kéo sát thương | Thương / thuẫn |
| Cung Tu | Sát thương từ xa | Cung |
| Pháp Tu | Sát thương phép, hỗ trợ | Chùy / phù |

---

### 2.2 Chiến đấu

#### Ngoài thành (vùng sương mù)

- Đệ tử tự động chiến đấu khi đã được điều đến vùng (auto-battle như EHT).
- Người chơi quyết định **trước trận**: giao vùng, chọn đội, trang bị. Không điều khiển trực tiếp trong trận.
- Vật phẩm rơi vãi mặt đất → **tap để nhặt** (giữ nguyên cơ chế EHT).

#### Bí Cảnh

- Tổ đội tối đa 5 đệ tử.
- Cấu trúc 3 lượt: 2 lượt quái + 1 lượt boss.
- Đệ tử phải đủ no / đủ ngủ / đã chữa mới chịu vào.
- Phần thưởng ngẫu nhiên: trang bị, vật liệu hiếm, đan dược. Tầng càng sâu càng hiếm.

#### Yêu Vương (field boss)

- Kích hoạt tại **Triệu Yêu Linh** → triệu hồi Yêu Vương ở vùng ngoài.
- Cả tông cùng đánh → thưởng lớn (nguyên liệu đột phá, Linh Thạch).
- Có thời gian hồi kích hoạt.

#### Ngũ hành trong chiến đấu

- Mỗi skill đệ tử gắn hệ (Kim/Mộc/Thuỷ/Hoả/Thổ), hiện hiệu ứng màu.
- Tương khắc tính theo ngũ hành kẻ địch: khắc được thì tăng sát thương, bị khắc thì giảm.
- Linh căn đệ tử quyết định hệ skill chủ đạo → người chơi sắp đội hình theo vùng yêu thú.

---

### 2.3 Tông môn (city builder)

#### Xây dựng

- Lưới **isometric 2:1**; đặt / di chuyển công trình tự do.
- Ô có **linh mạch** hợp hệ → buff hiệu quả công trình (hiển thị highlight rõ ràng).
- **Đại Điện** là khoá chính: cấp Đại Điện quyết định công trình nào được mở / nâng cấp.

#### Danh sách công trình Early Access (~20)

| Công trình | Chức năng |
|---|---|
| Đại Điện | Khoá tiến trình, quản lý tông môn |
| Tụ Bảo Các | Đặt đơn mua vật liệu từ đệ tử |
| Nhà ở (upgrade) | Mở slot đệ tử |
| Luyện Khí Phòng | Chế tạo vũ khí |
| Đan Phòng | Chế tạo đan dược |
| Pháp Bảo Các | Chế tạo trang sức / phù |
| Quầy vũ khí | Bán vũ khí cho đệ tử |
| Quầy giáp | Bán giáp |
| Quầy đan | Bán đan |
| Quầy pháp bảo | Bán pháp bảo |
| Tĩnh Thất | Hồi thể lực |
| Linh Thiện Đường | Ăn uống |
| Y Đường | Chữa thương |
| Trà Lâu | Giải trí, hồi tâm trạng |
| Truyền Công Các | Học / nâng công pháp, bí thuật |
| Nhiệm Vụ Đường | Giao nhiệm vụ |
| Luyện Công Trường | Kinh nghiệm nhanh |
| Cường Hoá Lô | Cường hoá trang bị +1 → +10 |
| Luân Hồi Trì | Hồi sinh đệ tử chết |
| Bí Cảnh Cổ Môn | Vào Bí Cảnh |
| Triệu Yêu Linh | Gọi Yêu Vương |

#### Mỹ thuật công trình

- **Cải trang công trình** (cosmetic, IAP) — nguồn doanh thu.
- Công trình **cố định hướng** (không xoay) — tiết kiệm sprite.
- Khi đệ tử đứng sau công trình → công trình chuyển trong suốt.

---

### 2.4 Ba hệ thống đặc trưng (khác biệt so với EHT)

#### Linh căn ngũ hành

Mỗi đệ tử mang linh căn Kim / Mộc / Thuỷ / Hoả / Thổ (hiếm: dị linh căn 2 hệ). Linh căn quyết định:

- Hệ skill chủ đạo trong chiến đấu.
- Hiệu suất ở vùng yêu thú cùng hệ / khắc hệ.
- Độ hợp với trang bị ngũ hành tương ứng.

#### Linh mạch

Đường linh mạch chạy ngầm dưới lưới isometric. Đặt công trình lên ô linh mạch hợp hệ → buff (ví dụ: Luyện Khí Phòng trên mạch Hoả +15% tốc độ chế tác, Y Đường trên mạch Mộc +15% tốc độ chữa). Chiều sâu bố trí tông môn thay vì chỉ thẩm mỹ.

#### Độ Kiếp

Xem mục "Cấp, đẳng cấp và Độ Kiếp". Luồng: đủ cấp → trận thiên kiếp → thắng thì mạnh vĩnh viễn / thua thì hồi phục. Nhân tố rủi ro – thưởng có chủ đích, gắn chặt fantasy tu tiên.

---

### 2.5 Kinh tế & chuỗi cung ứng

```
Vật liệu (đệ tử săn / bí cảnh)
  → Tụ Bảo Các: đặt đơn mua (giống request của EHT)
  → Chế tác: khí / đan / pháp bảo / linh thiện (tốn thời gian + Vàng)
  → Quầy bán cho đệ tử (tự mua khi có nhu cầu)
  → Linh Thạch về người chơi
```

#### Loại tiền

| Tiền | Nguồn | Dùng cho |
|---|---|---|
| Vàng | Giết yêu thú, đơn hàng | Xây / nâng công trình, chế tác cơ bản |
| Linh Thạch | Bán đồ cho đệ tử, Yêu Vương, IAP | Trắc Duyên, vật hiếm, tiện ích |
| Điểm Đạo Vận | Độ kiếp thành công | Mở Đạo Ấn (trait) |

#### Đòn bẩy kinh tế

Nhân lực: đệ tử no / đủ ngủ thì mới đi săn. Giữ nhịp phục vụ là việc căng thẳng chính của người chơi — đây là điểm vui đã được EHT kiểm chứng.

---

### 2.6 Chế tác

| Lớp | Nơi | Nội dung |
|---|---|---|
| Luyện khí | Luyện Khí Phòng | Vũ khí theo chức nghiệp + hệ ngũ hành; tier D/C/B/A/S theo cõi |
| Luyện đan | Đan Phòng | Đan hồi phục, thuốc nâng chỉ số tạm, Kháng Kiếp, thuốc đột phá |
| Pháp bảo | Pháp Bảo Các | Vòng tay, nhẫn, phù |
| Cường hoá | Cường Hoá Lô | +1 → +10; **cho thu hồi trang bị cũ** (sửa phàn nàn EHT) |

- Rèn / luyện có tỉ lệ thành công (flavour tu tiên): thất bại mất nguyên liệu ở mức chấp nhận được, không sát phạt quá mức.
- Chế tác chạy theo hàng đợi có giới hạn; mở rộng hàng đợi = tiện ích IAP.

---

### 2.7 Nhiệm vụ & nội dung định kỳ

| Loại | Nơi | Đặc điểm |
|---|---|---|
| Hướng dẫn tân thủ | Questline cố định | Dẫn qua toàn bộ hệ thống (EHT làm tốt — giữ) |
| Hằng ngày | Nhiệm Vụ Đường | Giao thủ công cho đệ tử |
| Tuần / sự kiện | Theo lịch server | Phân bố nhiệm vụ theo mốc tuần |

**Chốt: EA không có tiến trình offline.** Game chỉ chạy khi mở.

---

### 2.8 Nội dung 3 cõi (scope EA)

| Cõi | Vùng sương mù | Bí cảnh | Yêu Vương | Cấp max |
|---|---|---|---|---|
| Phàm | 6 vùng | Tầng 1–10 | Yêu Vương Phàm | 30 |
| Linh | 6 vùng | Tầng 11–20 | Yêu Vương Linh | 60 |
| Địa | 6 vùng | Tầng 21–25 | Yêu Vương Địa | 100 |

- 18 vùng sương mù, 25 tầng bí cảnh, 3 Yêu Vương.
- Điều kiện mở cõi sau: hoàn thành vùng cuối cõi trước + đủ Điểm Đạo Vận tích luỹ.

---

## 3. Sương mù bản đồ (thay hệ thống chuyển độ khó)

- Bản đồ thế giới isometric chia ô vùng, bao phủ **sương mù**.
- Dọn sương bằng điều kiện đệ tử hoàn thành tại chỗ: diệt đủ yêu thú / thu thập đủ vật liệu / hạ yêu vương vùng trước.
- Vùng càng xa tông môn → yêu thú mạnh hơn, vật liệu hiếm hơn, phần thưởng cao hơn.
- 3 cõi = 3 tầng khu vực lớn của cùng bản đồ.
- **Không có nút đổi độ khó** (khác EHT): khó là thứ người chơi tự mở bằng cách tiến về phía trước.

---

## 4. Đồ hoạ & UX

### 4.1 Hướng hình ảnh

- **Pixel art chibi isometric**, tông tu tiên (mây, đèn lồng, tiên khí).
- Lưới isometric 2:1; camera kéo / zoom được.
- Công trình cố định hướng (không xoay 4 hướng) — tiết kiệm asset.
- Che khuất: công trình chuyển trong suốt khi đệ tử đứng sau.
- Tông màu chủ đạo: xanh ngọc, vàng kim, trắng sương, đèn lồng đỏ.

### 4.2 UX mobile

- Giao diện dọc; thanh dưới gồm: **Xây · Đệ tử · Bí cảnh · Kho · Nhiệm vụ**.
- Bấm trực tiếp đệ tử / công trình trên bản đồ để mở menu ngữ cảnh.
- Danh sách đệ tử: **lọc + chọn nhiều** để giao vùng hàng loạt — giữ thao tác thủ công nhưng giảm mỏi tay (sửa phàn nàn EHT về thao tác từng người một).
- Di chuyển / xếp lại công trình miễn phí (sửa phàn nàn EHT: layout khoá cứng).
- Tốc độ game: không có buff tua máy trả phí; nhịp game do người chơi điều khiển bằng thao tác.

---

## 5. Mạng lưới & cộng đồng

### 5.1 Online nhẹ (đã chốt)

Single-player là lõi. Server chỉ lo:

- **Bảng xếp hạng tuần:** Tông môn mạnh nhất, tầng Bí Cảnh cao nhất, số lần Độ Kiếp — phần thưởng cosmetic cho top.
- **Cloud save** (tài khoản).
- Sự kiện theo lịch (nhiệm vụ tuần).

### 5.2 Không có trong EA

PvP đấu trường, bang hội / guild raid, tiến trình offline — đều đẩy sang post-EA (backend lớn, rủi ro EA).

---

## 6. Monetization (F2P)

### 6.1 Nguồn doanh thu

| Nguồn | Nội dung | Ghi chú |
|---|---|---|
| Gacha Trắc Duyên | Vé mời đệ tử tư chất cao | Pity cứng (đảm bảo S sau N lượt), công khai tỉ lệ |
| Cosmetic | Trang phục đệ tử, cải trang công trình, hiệu ứng | Nguồn doanh thu chính, không cộng chỉ số |
| Tiện ích | Mở rộng kho, thêm slot nhà, hàng đợi chế tác, thêm slot đội Bí Cảnh | Không ảnh hưởng độ khó |
| Quảng cáo thưởng | Rương linh bảo, nhân đôi phần thưởng Bí Cảnh | Tuỳ chọn xem, như EHT |
| Gói tân thủ / Battle pass nhẹ | Gói 1 lần + pass theo mùa | Cosmetic + tiện ích |

### 6.2 Nguyên tắc

1. Mọi thứ mua được đều có thể kiếm bằng chơi (chậm hơn).
2. **Không bán auto-admin** — quản lý thủ công là lõi thiết kế, không phải thứ để bán.
3. Không bán sức mạnh trực tiếp.
4. Sửa các phàn nàn EHT về tiền: thu hồi đồ cũ có giá hợp lý, xếp lại layout miễn phí, không khoá tính năng cơ bản sau paywall.

---

## 7. Scope Early Access

### 7.1 Có trong EA

- Toàn bộ §2–§4: 3 cõi, 18 vùng sương mù, 25 tầng Bí Cảnh, 3 Yêu Vương.
- ~20 công trình, 4 chức nghiệp, ngũ hành, linh mạch, Độ Kiếp.
- Quest tân thủ, nhiệm vụ hằng ngày / tuần.
- Gacha Trắc Duyên, cosmetic, bảng xếp hạng tuần, cloud save.

### 7.2 Không có trong EA (post-EA)

- PvP đấu trường, bang hội.
- Tiến trình offline.
- Cõi Thiên / Thần.
- Chức nghiệp thứ 5.
- Thú cưng, hệ thống khai quật (giống roadmap EHT).

### 7.3 Lộ trình (cấp cao, chưa có lịch)

1. **Prototype:** lưới isometric + 1 đệ tử + nhu cầu + 1 vùng săn.
2. **Vertical slice:** chuỗi cung ứng đầy đủ cõi Phàm.
3. **Alpha:** 3 cõi + Bí Cảnh + Độ Kiếp.
4. **Beta kín:** cân balance kinh tế, monetization.
5. **Early Access** → roadmap post-EA theo phản hồi.

---

## 8. KPI mục tiêu EA

| KPI | Mục tiêu |
|---|---|
| Hoàn thành hướng dẫn tân thủ | ≥ 70% |
| Giữ chân D1 | ≥ 40% |
| Giữ chân D7 | ≥ 15% |
| Giữ chân D30 | ≥ 6% |
| Thời lượng nội dung đến hết cõi Địa lần đầu | 40–80 giờ |
| Lần Độ Kiếp đầu tiên | Trong 8 giờ chơi đầu |

---

## 9. Rủi ro & giảm thiểu

| Rủi ro | Giảm thiểu |
|---|---|
| Bị coi là clone EHT | 3 hệ thống đặc trưng (ngũ hành, linh mạch, Độ Kiếp) + sương mù thay độ khó |
| Quản lý thủ công mệt khi đệ tử đông | Chọn nhiều, giao vùng hàng loạt, giới hạn slot ở EA |
| Cân bằng kinh tế chuỗi cung ứng | Bảng tính kinh tế riêng, thử nghiệm sớm ở vertical slice |
| Isometric tốn asset | Công trình cố định hướng, tái dùng sprite, 4 chức nghiệp dùng chung khung animation |
| Gacha gây tiếng xấu | Pity cứng, công khai tỉ lệ, đường kiếm miễn phí rõ ràng |
| Số liệu tham chiếu EHT chưa có | Mọi con số trong tài liệu này là **điểm khởi điểm**, chốt lại qua playtest |

---

## 10. Các quyết định đã chốt (design decisions log)

| Quyết định | Lựa chọn |
|---|---|
| Nền tảng / doanh thu | Mobile F2P + IAP |
| Mức khác biệt so với EHT | Khung EHT + 3 hệ thống đặc trưng |
| Mạng lưới EA | Single-player + leaderboard tuần |
| Mức tự động hóa | Thủ công toàn bộ như EHT, không auto-admin |
| Scope progression | 3 cõi, 25 tầng Bí Cảnh, Độ Kiếp |
| Cơ chế độ khó | Không chuyển độ khó — dọn sương mù mở map |
| Hình ảnh | Pixel art chibi **isometric**, tông tu tiên |
| Tiến trình offline | Không có trong EA |
| Độ kiếp thất bại | Mất một phần cấp, không mất đệ tử vĩnh viễn |

---

*GDD này là tài liệu thiết kế tổng quát. Mọi con số (tỉ lệ, thời gian, KPI) là điểm khởi đầu để cân bằng, sẽ được chốt lại trong quá trình playtest.*
