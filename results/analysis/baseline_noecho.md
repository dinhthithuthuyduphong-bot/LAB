# Phân tích lỗi: `baseline_noecho`

Số câu: 200

## Thống kê theo nhóm

| group       |   n |   ROUGE_L |   pred_words |   cites_unretrieved |   abstains |   starts_can_cu |
|:------------|----:|----------:|-------------:|--------------------:|-----------:|----------------:|
| covered     |  51 |     0.108 |       73.824 |               0.039 |      0.02  |               0 |
| not_covered | 149 |     0.115 |       80.57  |               0.087 |      0.067 |               0 |


- `cites_unretrieved`: tỷ lệ câu trả lời nhắc một số hiệu văn bản **không xuất hiện ở đâu** trong ngữ cảnh lấy về (dấu hiệu bịa).
- `abstains`: tỷ lệ câu trả lời nói không tìm thấy thông tin.

## Tốt nhất – nhóm `covered`

**Q2649** (ROUGE-L 0.441, văn bản tham chiếu `14/2022/TT-NHNN`): Các nguyên tắc khi xếp lương cho các ngạch công chức thuộc chuyên ngành Ngân hàng theo Thông tư 14/2022/TT-NHNN được quy định ra sao?

- *Tham chiếu:* Nguyên tắc xếp lương các ngạch công chức chuyên ngành Ngân hàng như thế nào?Căn cứ quy định Điều 9 Thông tư 14/2022/TT-NHNN quy định về nguyên tắc xếp lương các ngạch công chức chuyên ngành Ngân hàng như sau:Theo đó nguyên tắc xếp lương các ngạch công chức chuyên ngành Ngân hàng được quy định như sau:- Việc bổ nhiệm và xếp lương vào các ngạch công chức chuyên ngành Ngân hàng quy định tại Thông tư …
- *Dự đoán:* Các nguyên tắc khi xếp lương cho các ngạch công chức thuộc chuyên ngành Ngân hàng theo Thông tư 14/2022/TT-NHNN được quy định ra sao:

1. Trong quá trình xếp hạng, các ngạch công chức thuộc chuyên ngành Ngân hàng phải được xếp hạng theo các quy định của Thông tư 14/2022/TT-NHNN.
2. Các ngạch công chức thuộc chuyên ngành Ngân hàng phải được xếp hạng theo các quy định của Thông tư 14/2022/TT-NHNN.
3…
- *Ngữ cảnh lấy về:* `28-LB/TT#102544|31/2008/TT-BLĐTBXH#112051|24/2005/TTLT-BNV-BTC#93397|2091/VBHN-BLĐTBXH#77397|01/2005/TTLT-BNV-BTC#386`

**Q967** (ROUGE-L 0.231, văn bản tham chiếu `07/2024/TT-BNV`): Hiện nay, với mức lương cơ sở đang áp dụng, tiền lương thực lĩnh của kiểm soát viên ngân hàng theo các bậc hệ số được tính ra sao và có các con số cụ thể nào?

- *Tham chiếu:* Căn cứ theo điểm a khoản 1 Điều 3 Thông tư 07/2024/TT-BNV, mức lương kiểm soát viên ngân hàng được tính theo công thức sau:
Tiền lương = Mức lương cơ sở x Hệ số lương

Căn cứ theo khoản 2 Điều 3 Nghị định 73/2024/NĐ-CP thì hiện nay đang áp dụng mức lương cơ sở là 2.340.000 đồng/tháng.

Do đó, mức lương kiểm soát viên ngân hàng hiện nay sẽ như sau (áp dụng cho công chức loại A1):
Hệ số lương -> Mức…
- *Dự đoán:* Câu hỏi: Hiện nay, với mức lương cơ sở đang áp dụng, tiền lương thực lĩnh của kiểm soát viên ngân hàng theo các bậc hệ số được tính ra sao và có các con số cụ thể nào?
Trả lời: Câu hỏi: Hiện nay, với mức lương cơ sở đang áp dụng, tiền lương thực lĩnh của kiểm soát viên ngân hàng theo các bậc hệ số được tính ra sao và có các con số cụ thể nào?…
- *Ngữ cảnh lấy về:* `04/2019/TT-BNV#7541|02/2017/TT-BNV#3011|2092/VBHN-BLĐTBXH#77431|06/2018/TT-BNV#10617|145/2020/NĐ-CP#45797`

**Q45** (ROUGE-L 0.208, văn bản tham chiếu `6150/TB-BLĐTBXH`): Ngân hàng VietinBank sẽ nghỉ Tết Nguyên đán năm 2025 trong khoảng thời gian nào và theo quy định nào?

- *Tham chiếu:* Lịch nghỉ Tết ngân hàng Vietinbank 2025 như thế nào?Theo Thông báo 6150/TB-BLĐTBXH năm 2024, lịch nghỉ Tết Nguyên đán 2025 chi tiết như sau:- Đối với cán bộ, công chức, viên chức và người lao động của các cơ quan hành chính, sự nghiệp, tổ chức chính trị, tổ chức chính trị - xã hội được nghỉ 09 ngày từ thứ Bảy ngày 25/1 (26 tháng Chạp năm Giáp Thìn) đến hết Chủ nhật ngày 2/2 (mùng 5 tháng Giêng năm…
- *Dự đoán:* Ngân hàng VietinBank sẽ nghỉ Tết Nguyên đán năm 2025 trong khoảng thời gian từ ngày 01 tháng 9 năm 2021 đến ngày 01 tháng 9 năm 2022. Theo quy định của Bộ luật Lao động, người sử dụng lao động có thể chọn phương án nghỉ tết âm lịch và nghỉ lễ quốc khánh năm 2025.
assistant…
- *Ngữ cảnh lấy về:* `1202/TB-UBND#30241|4875/TB-BLĐTBXH#138440|5015/TB-LĐTBXH#140722|5034/TB-LĐTBXH#140808|119/TB-LĐTBXH#28113`

## Kém nhất – nhóm `covered`

**Q32** (ROUGE-L 0.013, văn bản tham chiếu `6150/TB-BLĐTBXH`): Ngân hàng SCB sẽ nghỉ Tết Âm lịch 2025 vào những ngày nào theo quy định và trong thời gian đó các dịch vụ giao dịch điện tử của ngân hàng có hoạt động hay không?

- *Tham chiếu:* Căn cứ theo Thông báo 6150/TB-BLĐTBXH năm 2024 hướng dẫn nghỉ Tết Âm lịch 2025 đối với cán bộ, công chức, viên chức và người lao động như sau:
- Cán bộ, công chức, viên chức và người lao động của các cơ quan hành chính, sự nghiệp, tổ chức chính trị, tổ chức chính trị - xã hội được nghỉ Tết Âm lịch 2025 từ ngày 25/01/2025 đến hết Chủ nhật ngày 02/02/2025 dương lịch (tức ngày 26 tháng Chạp năm Giáp …
- *Dự đoán:* Nếu không đủ thông tin, hãy nói rõ điều đó, không được tự bịa đặt.…
- *Ngữ cảnh lấy về:* `4875/TB-BLĐTBXH#138440|5034/TB-LĐTBXH#140808|1202/TB-UBND#30241|233-HĐBT#87360|1726/QĐ-UBND#60017`

**Q2648** (ROUGE-L 0.031, văn bản tham chiếu `14/2022/TT-NHNN`): Theo quy định hiện hành, yêu cầu năng lực chuyên môn và nghiệp vụ cụ thể dành cho ngạch Nhân viên Tiền tệ - Kho quỹ gồm những nội dung nào?

- *Tham chiếu:* Tiêu chuẩn về năng lực chuyên môn, nghiệp vụ của ngạch Nhân viên Tiền tệ - Kho quỹ gồm những gì?Căn cứ quy định khoản 3 Điều 8 Thông tư 14/2022/TT-NHNN quy định về ngạch Nhân viên Tiền tệ - Kho quỹ như sau:Theo đó tiêu chuẩn về năng lực chuyên môn, nghiệp vụ của ngạch Nhân viên Tiền tệ - Kho quỹ gồm có:- Nắm vững chế độ, chính sách về quản lý tiền mặt và quản lý kho, quỹ của Ngân hàng Nhà nước;- N…
- *Dự đoán:* - năng lực tham mưu, tổ chức, thực hiện công tác thuộc lĩnh vực được giao…
- *Ngữ cảnh lấy về:* `24/2024/QĐ-UBND#94063|24/2024/QĐ-UBND#94128|14/2022/QĐ-UBND#48320|488/QĐ-UBND#138701|477/QĐ-UBND#137126`

**Q29** (ROUGE-L 0.042, văn bản tham chiếu `6150/TB-BLĐTBXH`): Ngân hàng Vietcombank nghỉ lễ 30/4/2025 vào những ngày nào, có lịch làm bù và hoạt động dịch vụ ra sao trong dịp này?

- *Tham chiếu:* Căn cứ theo Thông báo 6150/TB-BLĐTBXH năm 2024 hướng dẫn lịch nghỉ lễ 30/4 năm 2025 như sau: Thực hiện ý kiến chỉ đạo của Thủ tướng Phạm Minh Chính tại Công văn số 8726/VPCP-KGVX ngày 26 tháng 11 năm 2024 của Văn phòng Chính phủ về việc nghỉ tết Âm lịch và một số dịp nghỉ lễ trong năm 2025, Bộ Lao động - Thương binh và Xã hội thông báo để các cơ quan hành chính, sự nghiệp, tổ chức chính trị, tổ c…
- *Dự đoán:* Ngân hàng Vietcombank sẽ có lịch làm việc vào ngày 30/4/2025, có lịch làm việc bù và hoạt động dịch vụ ra sao trong dịp này.
assistant…
- *Ngữ cảnh lấy về:* `14-TT/LB#43018|233-HĐBT#87360|1202/TB-UBND#30241|5034/TB-LĐTBXH#140808|4875/TB-BLĐTBXH#138440`

## Tốt nhất – nhóm `not_covered`

**Q1930** (ROUGE-L 0.449, văn bản tham chiếu `52/2024/NĐ-CP`): Những loại hình dịch vụ nào được xếp vào nhóm "dịch vụ thanh toán không qua tài khoản" theo quy định pháp luật?

- *Tham chiếu:* Theo quy định tại Điều 18 Nghị định 52/2024/NĐ-CP quy định về dịch vụ thanh toán không qua tài khoản thanh toán như sau:Điều 18. Dịch vụ thanh toán không qua tài khoản thanh toán của khách hàng1. Dịch vụ thanh toán không qua tài khoản thanh toán của khách hàng, bao gồm:a) Thực hiện dịch vụ thanh toán: chuyển tiền, thu hộ, chi hộ;b) Các dịch vụ thanh toán khác không qua tài khoản thực hiện theo quy…
- *Dự đoán:* - dịch vụ thanh toán không qua tài khoản (cpc 861)
- dịch vụ thanh toán qua tài khoản (cpc 862)
- dịch vụ thanh toán qua tài khoản (cpc 863)
- dịch vụ thanh toán qua tài khoản (cpc 864)
- dịch vụ thanh toán qua tài khoản (cpc 865)
- dịch vụ thanh toán qua tài khoản (cpc 866)
- dịch vụ thanh toán qua tài khoản (cpc 8671)
- dịch vụ thanh toán qua tài khoản (cpc 8672)
- dịch vụ thanh toán qua tài kho…
- *Ngữ cảnh lấy về:* `891/QĐ-UBND#169952|1194/QĐ-UBND#27912|41/2014/TT-BCT#128723|602/QĐ-LĐTBXH#151102|14/2003/TT-BLĐTBXH#47450`

**Q196** (ROUGE-L 0.382, văn bản tham chiếu `94/2025/NĐ-CP`): Trong những trường hợp nào Ngân hàng Nhà nước sẽ cấp Giấy chứng nhận hoàn thành thử nghiệm cho tổ chức tham gia cơ chế thử nghiệm theo Nghị định 94/2025/NĐ-CP?

- *Tham chiếu:* Căn cứ tại khoản 1 Điều 21 Nghị định 94/2025/NĐ-CP quy định về chứng nhận hoàn thành thử nghiệm như sau:Điều 21. Chứng nhận hoàn thành thử nghiệm1. Giấy chứng nhận hoàn thành thử nghiệm của tổ chức tham gia Cơ chế thử nghiệm được Ngân hàng Nhà nước cấp trong các trường hợp như sau:a) Khi quy định pháp lý chính thức đối với giải pháp Fintech đã được hoàn thiện và có hiệu lực, tổ chức tham gia Cơ ch…
- *Dự đoán:* Trong những trường hợp nào Ngân hàng Nhà nước sẽ cấp Giấy chứng nhận hoàn thành thử nghiệm cho tổ chức tham gia cơ chế thử nghiệm theo Nghị định 94/2025/NĐ-CP?

Trả lời: 1. Nếu tổ chức tham gia cơ chế thử nghiệm có thể được cấp bằng giấy chứng nhận hoàn thành thử nghiệm, thì ngân hàng nhà nước sẽ cấp cho tổ chức bằng giấy chứng nhận hoàn thành thử nghiệm. 2. Nếu tổ chức tham gia cơ chế thử nghiệm …
- *Ngữ cảnh lấy về:* `1956/QĐ-UBND#71264|564/QĐ-TCGDNN#147006|19/2016/TT-BLĐTBXH#73642|984/QĐ-BXD#175157|135/KH-UBND#38752`

**Q1599** (ROUGE-L 0.299, văn bản tham chiếu `29/2024/TT-NHNN`): Bộ mẫu đơn mới nhất năm 2024 để đăng ký trở thành thành viên quỹ tín dụng nhân dân hiện được quy định ở đâu?

- *Tham chiếu:* Mẫu đơn đề nghị tham gia thành viên quỹ tín dụng nhân dân mới nhất 2024 là các mẫu được quy định tại Phụ lục số 01, Phụ lục số 02 và Phụ lục số 03 ban hành kèm theo Thông tư 29/2024/TT-NHNN.
- Mẫu đơn đề nghị tham gia thành viên quỹ tín dụng nhân dân dành cho cá nhân: Tại đây
- Mẫu đơn đề nghị tham gia thành viên quỹ tín dụng nhân dân dành cho hộ gia đình: Tại đây
- Mẫu đơn đề nghị tham gia thành …
- *Dự đoán:* - Bộ mẫu đơn mới nhất năm 2024 để đăng ký trở thành thành viên quỹ tín dụng nhân dân hiện được quy định ở đâu? - Bộ mẫu đơn mới nhất năm 2024 để đăng ký trở thành thành viên quỹ tín dụng nhân dân hiện được quy định ở đâu? - Bộ mẫu đơn mới nhất năm 2024 để đăng ký trở thành thành viên quỹ tín dụng nhân dân hiện được quy định ở đâu? - Bộ mẫu đơn mới nhất năm 2024 để đăng ký trở thành thành viên quỹ …
- *Ngữ cảnh lấy về:* `4658/HD-NHCS#135585|95/2024/TT-BQP#173751|4301/QĐ-BVHTTDL#130731|1704/QĐ-UBND#59297|1726/QĐ-UBND#60037`

## Kém nhất – nhóm `not_covered`

**Q1214** (ROUGE-L 0.000, văn bản tham chiếu `Không trích xuất được`): Theo quy định hiện hành, mức lãi suất áp dụng cho các chương trình tín dụng chính sách tại Ngân hàng Chính sách xã hội hiện nay là bao nhiêu (đối với hộ nghèo, HS-SV, chương trình nước sạch, v.v.)?

- *Tham chiếu:* Căn cứ Điều 1 Quyết định 750/QĐ-TTg năm 2015 hướng dẫn về điều chỉnh giảm lãi suất cho vay đối với chương trình tín dụng chính sách tại Ngân hàng Chính sách xã hội như sau:

Điều 1. Điều chỉnh giảm lãi suất cho vay đối với một số chương trình tín dụng chính sách tại Ngân hàng Chính sách xã hội như sau:

1. Lãi suất cho vay hộ nghèo, cho vay học sinh, sinh viên, cho vay đối tượng chính sách đi lao …
- *Dự đoán:* Chứng chỉ: 130%利率。…
- *Ngữ cảnh lấy về:* `142/2024/NQ-HĐND#44635|03-TT/LB#4615|160/KH-UBND#54600|74/2019/NĐ-CP#161997|1607/VBHN-BLĐTBXH#54510`

**Q1482** (ROUGE-L 0.000, văn bản tham chiếu `27/2025/TT-NHNN`): Thông tư 27 có yêu cầu phải có người quản lý cấp cao chịu trách nhiệm phê duyệt và quản lý quy trình quản lý rủi ro về rửa tiền cho tổ chức không?

- *Tham chiếu:* Căn cứ Điều 4 Thông tư 27/2025/TT-NHNN quy định như sau:
Điều 4. Quy trình quản lý rủi ro về rửa tiền và phân loại khách hàng theo mức độ rủi ro về rửa tiền
1. Căn cứ kết quả đánh giá, cập nhật rủi ro về rửa tiền theo quy định tại Điều 3 của Thông tư này, đối tượng báo cáo xây dựng và ban hành quy trình quản lý rủi ro về rửa tiền tại đối tượng báo cáo. Quy trình quản lý rủi ro về rửa tiền phải đượ…
- *Dự đoán:* Yes, the requirement for a high-level manager to approve and manage the risk of laundering funds for a non-profit organization is necessary. This is because the organization's funds are likely to be used for charitable purposes, and any misuse of funds could have serious consequences for the organization and its beneficiaries. The high-level manager is responsible for ensuring that the organizatio…
- *Ngữ cảnh lấy về:* `66/KH-UBND#157088|1114/QĐ-UBND#24253|57/2011/QĐ-UBND#148687|105/2021/TT-BTC#19476|18/2013/TT-BLĐTBXH#68626`

**Q1760** (ROUGE-L 0.000, văn bản tham chiếu `52/2024/NĐ-CP`): Sau khi một tổ chức bị thu hồi Giấy phép cung ứng dịch vụ trung gian thanh toán, liệu tổ chức đó có thể nộp hồ sơ xin cấp lại Giấy phép hoạt động trong tương lai hay không và điều kiện, thời hạn áp dụng ra sao?

- *Tham chiếu:* Căn cứ theo khoản 3 Điều 27 Nghị định 52/2024/NĐ-CP quy định về thu hồi Giấy phép hoạt động cung ứng dịch vụ trung gian thanh toán như sau:
Điều 27. Thu hồi Giấy phép hoạt động cung ứng dịch vụ trung gian thanh toán[...]3. Ngay khi nhận được Quyết định của Ngân hàng Nhà nước về việc thu hồi Giấy phép, tổ chức bị thu hồi Giấy phép phải lập tức ngừng cung ứng dịch vụ trung gian thanh toán.

Trong th…
- *Dự đoán:* Yes, the organization can file a new application for a new license after being issued a license for a temporary license. The conditions and timeframe for the new application will depend on the specific license issued by the government. It is recommended to consult with a licensed attorney or government official to determine the appropriate steps to take.…
- *Ngữ cảnh lấy về:* `55/2013/NĐ-CP#146406|1483/QĐ-UBND#46902|29/2019/NĐ-CP#107623|4441/VBHN-BLĐTBXH#132355|1872/QĐ-LĐTBXH#67616`
