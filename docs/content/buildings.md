# Danh mục công trình — Early Access

**Phase 0 deliverable.** Nguồn cho: phần dòng tiền của bảng kinh tế (`docs/economy/`), ước lượng asset, phạm vi Phase 2-3.
**Liên quan:** GDD §2.3, §2.4; `docs/glossary.md` (định danh code). Mọi con số là **điểm khởi đầu**, chốt bằng playtest (GDD §9).

## Quy tắc chung

- **Đại Điện (`GrandHall`)** cấp 1-9 là khoá chính. Cấp mọi công trình khác ≤ cấp Đại Điện.
- Cõi gợi ý theo cấp Đại Điện: **Phàm = 1-3, Linh = 4-6, Địa = 7-9** (đồng bộ độ khó, không chặn cứng việc mở cõi; mở cõi vẫn qua sương mù + Đạo Vận, GDD §2.8).
- Lưới isometric 2:1; kích thước tính theo ô (rộng × sâu). Công trình **cố định hướng** (GDD §4.1).
- **Linh mạch:** đặt đúng hệ ưa thích trên ô linh mạch cùng hệ → **+15% tốc độ hoạt động chính** (ví dụ chế tác, hồi phục). Không phạt khi đặt sai hệ. Công trình không hệ thì không hưởng buff.
- **Hình ảnh theo cấp:** 3 bậc diện mạo (cấp 1-3, 4-6, 7-9), mỗi bậc 1 sprite tĩnh + dùng chung một lớp phủ hoạt hoạ "đang hoạt động".
- **Công suất** (số đệ tử phục vụ cùng lúc) và **thời gian chế tác** là tham số cho bảng dòng tiền; chưa chốt ở tài liệu này.

## Danh sách 21 công trình

Cột "ĐĐ" = cấp Đại Điện tối thiểu để xây.

### Nền móng và nơi ở

| Công trình | Code | ĐĐ | Ô | Số lượng tối đa | Vai trò |
|---|---|---|---|---|---|
| Đại Điện | `GrandHall` | 1 | 4×4 | 1 | Khoá cấp công trình; nâng cấp tốn Vàng + vật liệu xây |
| Tụ Bảo Các | `TreasureExchange` | 1 | 3×3 | 1 | Đặt đơn vật liệu; đệ tử đang rảnh bán lại cho tông theo đơn |
| Nhà ở | `Dormitory` | 1 | 3×3 | 3 | Slot đệ tử: **6 + tổng cấp các Nhà ở, tối đa 30** |
| Luân Hồi Trì | `RevivalPool` | 1 | 2×2 | 1 | Hồi sinh đệ tử chết (tốn Vàng + thời gian chờ) |

### Dịch vụ cho nhu cầu đệ tử

Mỗi dịch vụ **tiêu hao** vật phẩm do người chơi chế (xem `content.md`), giống chuỗi EHT: người chơi chế → đệ tử mua → Vàng về tông.

| Công trình | Code | ĐĐ | Ô | Nhu cầu | Vật tiêu hao | Hệ ưa linh mạch |
|---|---|---|---|---|---|---|
| Linh Thiện Đường | `MealHall` | 1 | 3×3 | Đói | Linh thiện (nấu tại chỗ) | Thổ |
| Tĩnh Thất | `RestChamber` | 1 | 3×3 | Thể lực | Phòng nghỉ (sản xuất tại chỗ) | Thuỷ |
| Y Đường | `HealingHall` | 1 | 3×3 | Thương tích | Thuốc băng/cao (sản xuất tại chỗ) | Mộc |
| Trà Lâu | `TeaHouse` | 2 | 3×3 | Tâm trạng | Trà/rượu (sản xuất tại chỗ) | Thuỷ |

### Chế tác và bán

| Công trình | Code | ĐĐ | Ô | Chức năng | Hệ ưa linh mạch |
|---|---|---|---|---|---|
| Luyện Khí Phòng | `ForgeRoom` | 2 | 3×3 | Chế vũ khí **và giáp thân** | Hoả |
| Quầy vũ khí | `WeaponStall` | 2 | 2×2 | Bán vũ khí cho đệ tử | — |
| Quầy giáp | `ArmorStall` | 2 | 2×2 | Bán giáp thân và mũ (mũ từ Bí Cảnh) | — |
| Đan Phòng | `AlchemyRoom` | 3 | 3×3 | Chế đan: hồi phục, tăng chỉ số tạm, Kháng Kiếp; hương Triệu Yêu | Mộc |
| Quầy đan | `PillStall` | 3 | 2×2 | Bán đan cho đệ tử | — |
| Pháp Bảo Các | `ArtifactPavilion` | 5 | 3×3 | Chế nhẫn, phù hộ mệnh | Kim |
| Quầy pháp bảo | `ArtifactStall` | 5 | 2×2 | Bán pháp bảo | — |

### Nâng sức mạnh đệ tử

| Công trình | Code | ĐĐ | Ô | Chức năng | Hệ ưa linh mạch |
|---|---|---|---|---|---|
| Nhiệm Vụ Đường | `MissionHall` | 2 | 3×3 | Giao nhiệm vụ hằng ngày/tuần, thưởng kinh nghiệm và vật phẩm | — |
| Truyền Công Các | `TechniquePavilion` | 4 | 3×3 | Học và nâng công pháp, bí thuật (đệ tử trả phí, tông nhận phần lớn) | — |
| Luyện Công Trường | `TrainingYard` | 4 | 4×3 | Kinh nghiệm nhanh cho đệ tử cấp thấp | Kim |
| Cường Hoá Lô | `EnhancementFurnace` | 4 | 3×3 | Cường hoá +1 → +10; **thu hồi trang bị cũ** (GDD §2.6) | Hoả |

### Ra ngoài

| Công trình | Code | ĐĐ | Ô | Chức năng |
|---|---|---|---|---|
| Bí Cảnh Cổ Môn | `RealmGate` | 3 | 4×3 | Vào Bí Cảnh, tổ đội tối đa 5 |
| Triệu Yêu Linh | `BeastSummonBell` | 3 | 2×2 | Gọi Yêu Vương bằng Triệu Yêu Hương; có thời gian hồi |

## Mở khoá theo cấp Đại Điện

| ĐĐ | Mở thêm | Số công trình |
|---|---|---|
| 1 | GrandHall, TreasureExchange, Dormitory, RevivalPool, MealHall, RestChamber, HealingHall | 7 |
| 2 | ForgeRoom, WeaponStall, ArmorStall, MissionHall, TeaHouse | 5 |
| 3 | AlchemyRoom, PillStall, RealmGate, BeastSummonBell | 4 |
| 4 | TechniquePavilion, TrainingYard, EnhancementFurnace | 3 |
| 5 | ArtifactPavilion, ArtifactStall | 2 |
| 6-9 | Không thêm công trình mới; mở trần cấp công trình | 0 |

Tổng 21. Phase 2 (cõi Phàm, ĐĐ ≤ 3) = 16 công trình; Phase 3 thêm 5.

## Số lượng asset công trình

| Hạng mục | Số lượng |
|---|---|
| Sprite tĩnh (21 công trình × 3 bậc diện mạo) | 63 |
| Lớp phủ hoạt hoạ "đang hoạt động" (mỗi công trình 1) | 21 |
| Vật liệu xây giai đoạn thi công (dùng chung) | 3 |
| Cải trang công trình (cosmetic, P4) | Chưa tính |

## Điểm cần quyết sau

1. **Công suất dịch vụ** (đệ tử/lần, thời gian/lần theo cấp) và **thời gian chế tác** theo cấp: quyết trong phần dòng tiền.
2. **Đại Điện cấp 6-9 không mở công trình mới**: chỉ mở trần cấp. Xác nhận ở playtest rằng đủ động lực nâng cấp.
3. **Buff linh mạch +15% đồng đều cho mọi công trình** là đơn giản hoá; nếu một số buff quá mạnh/yếu, tách theo công trình.
