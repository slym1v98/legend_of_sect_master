# Bảng thuật ngữ — LegendOfSectMaster

**Phase 0 deliverable.** Nguồn duy nhất cho tên hiển thị (tiếng Việt) và định danh trong code (tiếng Anh). Thêm thuật ngữ mới ở đây trước khi dùng trong UI/code.

**Quy ước**
- UI/tài liệu: tiếng Việt, Hán-Việt viết hoa chữ đầu mỗi từ (`Tụ Bảo Các`).
- Code: tiếng Anh, `PascalCase` cho kiểu, `snake_case` cho khoá dữ liệu/sự kiện analytics (ADR-004). Không dùng tiếng Việt có dấu trong định danh.
- Chuỗi hiển thị nằm trong file localization, không nhúng cứng vào code.

## Nhân vật & vai trò

| Tiếng Việt | Code | Ghi chú |
|---|---|---|
| Tông Môn | `Sect` | Thế chỗ "Town" |
| Tông Chủ | `SectMaster` | Người chơi |
| Đệ tử | `Disciple` | Thế chỗ "Hunter" |
| Chức nghiệp | `Class` → `DiscipleClass` | Tránh trùng từ khoá `class` |
| Kiếm Tu | `Swordsman` | Cận chiến cân bằng |
| Thể Tu | `BodyCultivator` | Tank |
| Cung Tu | `Archer` | Xa |
| Pháp Tu | `Mage` | Phép/hỗ trợ |
| Tư chất | `Aptitude` | S/A/B/C |
| Linh căn | `SpiritRoot` | Ngũ hành |
| Dị linh căn | `MutantSpiritRoot` | Hai hệ |
| Tính cách | `Temperament` | Ngẫu nhiên, ảnh hưởng hành vi |
| Thiên phú | `Talent` | Dòng cố định theo đệ tử |
| Yêu thú | `Beast` | Quái thường |
| Yêu Vương | `BeastKing` | Field boss |

## Ngũ hành

| Tiếng Việt | Code |
|---|---|
| Kim | `Metal` |
| Mộc | `Wood` |
| Thuỷ | `Water` |
| Hoả | `Fire` |
| Thổ | `Earth` |
| Tương sinh / Tương khắc | `Generates` / `Overcomes` |

## Nhu cầu & trạng thái

| Tiếng Việt | Code |
|---|---|
| Đói | `Hunger` |
| Thể lực | `Stamina` |
| Thương tích | `Injury` |
| Tâm trạng | `Mood` |

## Công trình

| Tiếng Việt | Code | Thế chỗ (EHT) |
|---|---|---|
| Đại Điện | `GrandHall` | Town Hall |
| Tụ Bảo Các | `TreasureExchange` | Trading Post |
| Nhà ở | `Dormitory` | House |
| Luyện Khí Phòng | `ForgeRoom` | Blacksmith |
| Đan Phòng | `AlchemyRoom` | Alchemist |
| Pháp Bảo Các | `ArtifactPavilion` | Jeweler |
| Quầy vũ khí / giáp / đan / pháp bảo | `WeaponStall` / `ArmorStall` / `PillStall` / `ArtifactStall` | Shops |
| Tĩnh Thất | `RestChamber` | Inn |
| Linh Thiện Đường | `MealHall` | Restaurant |
| Y Đường | `HealingHall` | Infirmary |
| Trà Lâu | `TeaHouse` | Tavern |
| Truyền Công Các | `TechniquePavilion` | Academy |
| Nhiệm Vụ Đường | `MissionHall` | Bounty Hut |
| Luyện Công Trường | `TrainingYard` | Training Ground |
| Cường Hoá Lô | `EnhancementFurnace` | Enhancement Forge |
| Luân Hồi Trì | `RevivalPool` | Sanctuary of Resurrection |
| Bí Cảnh Cổ Môn | `RealmGate` | Dungeon Entrance |
| Triệu Yêu Linh | `BeastSummonBell` | Boss Horn |

## Hệ thống & nội dung

| Tiếng Việt | Code | Ghi chú |
|---|---|---|
| Linh mạch | `LeyLine` | Buff công trình đặt trên ô hợp hệ |
| Sương mù | `Fog` | Thế chỗ chọn độ khó |
| Vùng | `Zone` | Ô vùng trên bản đồ |
| Cõi | `Realm` | Phàm / Linh / Địa |
| Phàm / Linh / Địa | `Mortal` / `Spirit` / `Earth` | **Trùng `Earth` (Thổ)** → dùng `EarthRealm` cho cõi, `Earth` giữ cho ngũ hành |
| Bí Cảnh | `SecretRealm` | 25 tầng |
| Độ Kiếp | `Tribulation` | Thế chỗ Reincarnation |
| Thuốc Kháng Kiếp | `TribulationPill` | Giảm tỉ lệ thua |
| Công pháp | `Technique` | |
| Bí thuật | `SecretArt` | |
| Bài Trắc Duyên | `DiscipleDraw` | Gacha |
| Vé Trắc Duyên | `DrawTicket` | |
| Luyện khí / Luyện đan | `Forging` / `Alchemy` | Hoạt động chế tác |
| Cường hoá | `Enhancement` | +1 → +10 |
| Cải trang | `Skin` | Cosmetic |
| Nhiệm vụ | `Mission` | Hằng ngày / tuần / tân thủ |

## Tiền & chỉ số tiến trình

| Tiếng Việt | Code |
|---|---|
| Vàng | `Gold` |
| Linh Thạch | `SpiritStone` |
| Điểm Đạo Vận | `DaoPoint` |
| Cấp | `Level` |
| Tier trang bị D/C/B/A/S | `GearTier` |

## Cần quyết định

1. **"Thiện Nguyện"** (GDD §2.1 dùng cho trait mở bằng Đạo Vận) nghĩa là "lời nguyện lành", lệch với tu tiên. Đề xuất đổi thành **Đạo Ấn** (`DaoMark`). Chưa sửa GDD, chờ bạn quyết.
2. Cõi **Địa** trùng chữ với hệ **Thổ**/`Earth` về tên code; đã tách `EarthRealm`. Nếu muốn tránh nhầm cả ở UI, cân nhắc đổi cõi Địa → **Đất** hoặc giữ nguyên.
3. "Thể Tu" dùng cho chức nghiệp; "thể lực" là nhu cầu. Khác nghĩa, trùng âm "thể" — chấp nhận, hai chỗ hiển thị khác nhau.
