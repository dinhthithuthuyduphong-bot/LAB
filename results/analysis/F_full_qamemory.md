# Phân tích lỗi: `F_full_qamemory`

Số câu: 200

## Thống kê theo nhóm

| group       |   n |   ROUGE_L |   pred_words |   cites_unretrieved |   abstains |   starts_can_cu |
|:------------|----:|----------:|-------------:|--------------------:|-----------:|----------------:|
| covered     |  51 |     0.311 |      249.824 |               0.039 |      0.118 |           0.98  |
| not_covered | 149 |     0.31  |      239.651 |               0.349 |      0.067 |           0.785 |


- `cites_unretrieved`: tỷ lệ câu trả lời nhắc một số hiệu văn bản **không xuất hiện ở đâu** trong ngữ cảnh lấy về (dấu hiệu bịa).
- `abstains`: tỷ lệ câu trả lời nói không tìm thấy thông tin.

## Tốt nhất – nhóm `covered`

**Q1984** (ROUGE-L 0.778, văn bản tham chiếu `14/2022/TT-NHNN`): Những tiêu chuẩn về phẩm chất chung bắt buộc đối với công chức làm việc trong ngành Ngân hàng được quy định như thế nào theo văn bản hiện hành?

- *Tham chiếu:* Căn cứ Điều 3 Thông tư 14/2022/TT-NHNN quy định tiêu chuẩn chung về phẩm chất của công chức ngân hàng như sau:
- Có bản lĩnh chính trị vững vàng, kiên định với chủ nghĩa Mác - Lênin, tư tưởng Hồ Chí Minh
- Nắm vững chủ trương, đường lối, quy định của Đảng, chính sách, pháp luật của Nhà nước
- Trung thành với Tổ quốc; bảo vệ lợi ích của Nhà nước, của nhân dân.
- Thực hiện đầy đủ nghĩa vụ của công c…
- *Dự đoán:* Căn cứ theo Điều 3, khoản 1, 2, 3 và 4 Điều 3 Thông tư 14/2022/TT-NHNN quy định về tiêu chuẩn chung về phẩm chất của công chức chuyên ngành Ngân hàng, Thống đốc Ngân hàng Nhà nước Việt Nam ban hành, chúng ta có thể trích dẫn như sau:

1. Có bản lĩnh chính trị vững vàng, kiên định với chủ nghĩa Mác - Lênin, tư tưởng Hồ Chí Minh; nắm vững chủ trương, đường lối, quy định của Đảng, chính sách, pháp lu…
- *Ngữ cảnh lấy về:* `14/2022/TT-NHNN#105811|14/2022/TT-NHNN#105812|12/2019/TT-NHNN#75418|956/2003/QĐ-NHNN#377662|12/2019/TT-NHNN#75445`

**Q2169** (ROUGE-L 0.752, văn bản tham chiếu `14/2022/TT-NHNN`): Những yêu cầu về năng lực chuyên môn và nghiệp vụ mà một kiểm soát viên chính ngân hàng phải đạt được bao gồm những gì?

- *Tham chiếu:* Căn cứ theo khoản 3 Điều 5 Thông tư 14/2022/TT-NHNN, kiểm soát viên chính ngân hàng phải đáp ứng đủ các tiêu chuẩn về năng lực chuyên môn, nghiệp vụ dưới đây:

- Nắm vững đường lối, chủ trương của Đảng, pháp luật của Nhà nước, chính sách của Ngành về các hoạt động của ngân hàng.
- Nắm vững nghiệp vụ kiểm soát, kiểm toán của Ngân hàng Nhà nước; hướng dẫn và điều hành có hiệu quả hoạt động của kiểm …
- *Dự đoán:* Căn cứ theo Điều 5 Thông tư 14/2022/TT-NHNN quy định về tiêu chuẩn chuyên môn, nghiệp vụ và xếp lương đối với các ngạch công chức chuyên ngành Ngân hàng, chúng ta có thể xác định những yêu cầu về năng lực chuyên môn và nghiệp vụ mà một kiểm soát viên chính ngân hàng phải đạt được như sau:

1. Nắm vững đường lối, chủ trương của Đảng, pháp luật của Nhà nước, chính sách của Ngành về các hoạt động của…
- *Ngữ cảnh lấy về:* `14/2022/TT-NHNN#105824|14/2022/TT-NHNN#105825|14/2022/TT-NHNN#105826|12/2019/TT-NHNN#75427|12/2019/TT-NHNN#75428`

**Q1709** (ROUGE-L 0.659, văn bản tham chiếu `14/2022/TT-NHNN`): Những tiêu chuẩn phẩm chất chung nào được quy định đối với công chức thuộc chuyên ngành Ngân hàng?

- *Tham chiếu:* Căn cứ theo Điều 3 Thông tư 14/2022/TT-NHNN quy định về tiêu chuẩn chung về phẩm chất như sau:

Điều 3. Tiêu chuẩn chung về phẩm chất
1. Có bản lĩnh chính trị vững vàng, kiên định với chủ nghĩa Mác - Lênin, tư tưởng Hồ Chí Minh; nắm vững chủ trương, đường lối, quy định của Đảng, chính sách, pháp luật của Nhà nước; trung thành với Tổ quốc; bảo vệ lợi ích của Nhà nước, của nhân dân.
2. Thực hiện đầy…
- *Dự đoán:* Căn cứ theo Điều 3 của Thông tư 14/2022/TT-NHNN quy định về tiêu chuẩn chung về phẩm chất của công chức chuyên ngành Ngân hàng, chúng ta có thể phân tích như sau:

1. Có bản lĩnh chính trị vững vàng, kiên định với chủ nghĩa Mác - Lênin, tư tưởng Hồ Chí Minh; nắm vững chủ trương, đường lối, quy định của Đảng, chính sách, pháp luật của Nhà nước; trung thành với Tổ quốc; bảo vệ lợi ích của Nhà nước, …
- *Ngữ cảnh lấy về:* `14/2022/TT-NHNN#105811|14/2022/TT-NHNN#105812|12/2019/TT-NHNN#75418|956/2003/QĐ-NHNN#377662|14/2022/TT-NHNN#105826`

## Kém nhất – nhóm `covered`

**Q1261** (ROUGE-L 0.056, văn bản tham chiếu `07/VBHN-VPQH`): Văn bản Pháp lệnh về ngoại hối hiện hành là văn bản nào và những nghị định, thông tư hướng dẫn liên quan (đã cập nhật đến năm 2025) gồm những văn bản nào?

- *Tham chiếu:* Pháp lệnh ngoại hối mới nhất là Pháp lệnh ngoại hối 2005 được sửa đổi bởi Pháp lệnh sửa đổi Pháp lệnh ngoại hối năm 2013. Văn bản hợp nhất Pháp lệnh ngoại hối mới nhất là Văn bản hợp nhất 07/VBHN-VPQH năm 2013 hợp nhất Pháp lệnh Ngoại hối.

Dưới đây là các văn bản hướng dẫn Pháp lệnh Ngoại hối:

(1) Nghị định
- Nghị định 16/2014/NĐ-CP về quản lý cán cân thanh toán quốc tế của Việt Nam
- Nghị định …
- *Dự đoán:* Căn cứ tại Điều 111 Luật Các tổ chức tín dụng 2024 quy định:

1. Tổng giám đốc (Giám đốc) của tổ chức tín dụng là công ty cổ phần sẽ do Hội đồng quản trị, Hội đồng thành viên, chủ sở hữu của tổ chức đó bổ nhiệm.

Như vậy, thẩm quyền bổ nhiệm chức danh Tổng giám đốc (Giám đốc) tại một tổ chức tín dụng hoạt động theo mô hình công ty cổ phần nằm ở Hội đồng quản trị, Hội đồng thành viên, chủ sở hữu củ…
- *Ngữ cảnh lấy về:* `1937/QĐ-BYT#154275|1176/QĐ-UBND#57911|1017/QĐ-UBND#38168|835/VBHN-BLĐTBXH#363449|3305/VBHN-BLĐTBXH#249171`

**Q38** (ROUGE-L 0.143, văn bản tham chiếu `6150/TB-BLĐTBXH`): Ngân hàng BIDV nghỉ Tết Nguyên đán 2025 theo lịch nào, chi tiết các ngày nghỉ và hoạt động kênh dịch vụ trong thời gian đó là ra sao?

- *Tham chiếu:* Lịch nghỉ Tết ngân hàng BIDV 2025 mới nhất, chi tiết?Theo Thông báo 6150/TB-BLĐTBXH năm 2024, lịch nghỉ Tết Nguyên đán 2025 chi tiết như sau:- Đối với cán bộ, công chức, viên chức và người lao động của các cơ quan hành chính, sự nghiệp, tổ chức chính trị, tổ chức chính trị - xã hội được nghỉ 09 ngày từ thứ Bảy ngày 25/1 (26 tháng Chạp năm Giáp Thìn) đến hết Chủ nhật ngày 2/2 (mùng 5 tháng Giêng nă…
- *Dự đoán:* Căn cứ tại Điều 55 Luật Các tổ chức tín dụng 2024 quy định về thẩm quyền bổ nhiệm Tổng giám đốc (Giám đốc) tại một tổ chức tín dụng hoạt động theo mô hình công ty cổ phần, chúng ta có thể xác định rằng:

- Tổng giám đốc (Giám đốc) của tổ chức tín dụng là công ty cổ phần sẽ do Hội đồng quản trị, Hội đồng thành viên, chủ sở hữu của tổ chức đó bổ nhiệm. 

Căn cứ tại Điều 112 Bộ luật Lao động 2019 quy…
- *Ngữ cảnh lấy về:* `94/KH-LĐLĐ#376964|146/KH-TLĐ#100747|48/KH-LĐLĐ#302800|84/KH-TLĐ#365319|09/TB-BTC#36088`

**Q2647** (ROUGE-L 0.150, văn bản tham chiếu `5015/TB-LĐTBXH`): Ngân hàng sẽ nghỉ Tết Âm lịch năm 2024 vào những ngày nào theo quy định và lịch tham khảo của các ngân hàng thương mại?

- *Tham chiếu:* Lịch nghỉ Tết âm lịch của ngân hàng 2024?Căn cứ tại Thông báo 5015/TB-LĐTBXH năm 2023 về việc nghỉ tết Âm lịch của cán bộ, công chức, viên chức và người lao động như sau:1. Cán bộ, công chức, viên chức và người lao động của các cơ quan hành chính, sự nghiệp, tổ chức chính trị, tổ chức chính trị - xã hội (sau đây gọi tắt là công chức, viên chức) được nghỉ tết Âm lịch năm 2024 từ thứ Năm ngày 08/02/…
- *Dự đoán:* Căn cứ tại Điều 55 Luật Các tổ chức tín dụng 2024 quy định về chức danh Tổng giám đốc (Giám đốc) tại tổ chức tín dụng hoạt động theo mô hình công ty cổ phần, chúng ta chưa tìm thấy quy định cụ thể về thẩm quyền bổ nhiệm Tổng giám đốc (Giám đốc) tại tổ chức tín dụng. Tuy nhiên, có thể dựa vào quy định chung về bổ nhiệm lãnh đạo trong các cơ quan hành chính, sự nghiệp và tổ chức chính trị - xã hội.
…
- *Ngữ cảnh lấy về:* `5015/TB-LĐTBXH#305998|5015/TB-LĐTBXH#305997|6150/TB-BLĐTBXH#330485|1202/TB-UBND#65796|6150/TB-BLĐTBXH#330482`

## Tốt nhất – nhóm `not_covered`

**Q2264** (ROUGE-L 0.996, văn bản tham chiếu `Không trích xuất được`): Liệu người lao động có được nhận tiền thưởng nhân dịp nghỉ lễ 30/4/2024 hay không và căn cứ pháp lý để xác định điều này là gì?

- *Tham chiếu:* Căn cứ theo Điều 104 Bộ luật Lao động 2019 quy định về thưởng cho người lao động như sau:

Điều 104. Thưởng
1. Thưởng là số tiền hoặc tài sản hoặc bằng các hình thức khác mà người sử dụng lao động thưởng cho người lao động căn cứ vào kết quả sản xuất, kinh doanh, mức độ hoàn thành công việc của người lao động.
2. Quy chế thưởng do người sử dụng lao động quyết định và công bố công khai tại nơi làm …
- *Dự đoán:* Căn cứ tại Điều 104 Bộ luật Lao động 2019 quy định về thưởng cho người lao động như sau: Điều 104. Thưởng
1. Thưởng là số tiền hoặc tài sản hoặc bằng các hình thức khác mà người sử dụng lao động thưởng cho người lao động căn cứ vào kết quả sản xuất, kinh doanh, mức độ hoàn thành công việc của người lao động.
2. Quy chế thưởng do người sử dụng lao động quyết định và công bố công khai tại nơi làm vi…
- *Ngữ cảnh lấy về:* `1570/TB-BLĐTBXH#112617|6150/TB-BLĐTBXH#330486|1202/TB-UBND#65798|342/TB-UBND#254127|6150/TB-BLĐTBXH#330485`

**Q217** (ROUGE-L 0.951, văn bản tham chiếu `Không trích xuất được`): Các nội dung bắt buộc phải có trong phương án hợp nhất toàn bộ cổ phần hoặc phần vốn góp của quỹ tín dụng nhân dân đang bị kiểm soát đặc biệt (theo quy định tại Điều 177 Luật Các tổ chức tín dụng 2024) là gì?

- *Tham chiếu:* Căn cứ tại khoản 1 Điều 177 Luật Các tổ chức tín dụng 2024 quy định về phương án hợp nhất toàn bộ cổ phần, phần vốn góp của quỹ tín dụng nhân dân được kiểm soát đặc biệt bao gồm những nội dung như sau:- Tên phương án hợp nhất toàn bộ cổ phần, phần vốn góp và quy trình thực hiện phương án;- Thông tin về tổ chức tín dụng bị hợp nhất, nhà đầu tư nhận chuyển nhượng toàn bộ cổ phần, phần vốn góp, bao g…
- *Dự đoán:* Căn cứ tại Điều 177 Luật Các tổ chức tín dụng 2024 quy định về phương án hợp nhất toàn bộ cổ phần hoặc phần vốn góp của quỹ tín dụng nhân dân đang bị kiểm soát đặc biệt, các nội dung bắt buộc phải có bao gồm:

- Tên phương án hợp nhất toàn bộ cổ phần hoặc phần vốn góp và quy trình thực hiện phương án;
- Thông tin về tổ chức tín dụng bị hợp nhất, nhận hợp nhất nhà đầu tư nhận chuyển nhượng toàn bộ …
- *Ngữ cảnh lấy về:* `20/VBHN-NHNN#172472|06/CT-TTg#24041|06/CT-TTg#24048|06/CT-TTg#24040|41/2024/QH15#280428`

**Q1229** (ROUGE-L 0.896, văn bản tham chiếu `Không trích xuất được`): Trong những tình huống cụ thể nào bắt buộc các đối tượng phải gửi báo cáo về giao dịch đáng ngờ tới Ngân hàng Nhà nước theo Luật Phòng, chống rửa tiền?

- *Tham chiếu:* Căn cứ theo khoản 1 Điều 26 Luật Phòng, chống rửa tiền 2022 quy định về báo cáo giao dịch đáng ngờ như sau:Điều 26. Báo cáo giao dịch đáng ngờ1. Đối tượng báo cáo có trách nhiệm báo cáo giao dịch đáng ngờ cho Ngân hàng Nhà nước Việt Nam trong trường hợp sau đây:a) Khi biết giao dịch được thực hiện theo yêu cầu của bị can, bị cáo, người bị kết án và có cơ sở hợp lý để nghi ngờ tài sản trong giao dị…
- *Dự đoán:* Căn cứ tại Điều 26 Luật Phòng, chống rửa tiền 2022 quy định như sau:

1. Đối tượng báo cáo có trách nhiệm báo cáo giao dịch đáng ngờ cho Ngân hàng Nhà nước Việt Nam trong trường hợp sau đây:
   a) Khi biết giao dịch được thực hiện theo yêu cầu của bị can, bị cáo, người bị kết án và có cơ sở hợp lý để nghi ngờ tài sản trong giao dịch là tài sản thuộc quyền sở hữu hoặc có nguồn gốc thuộc quyền sở hữ…
- *Ngữ cảnh lấy về:* `122/2001/QĐ-NHNN#68125|122/2001/QĐ-NHNN#68123|10/2021/TT-NHNN#50151|122/2001/QĐ-NHNN#68074|1383/QĐ-LĐTBXH#88349`

## Kém nhất – nhóm `not_covered`

**Q1392** (ROUGE-L 0.010, văn bản tham chiếu `17/2024/TT-NHNN`): Nếu có người lạ chuyển tiền nhầm vào tài khoản của tôi thì nên xử lý thế nào theo pháp luật và có phải hoàn trả không?

- *Tham chiếu:* Đầu tiên, tại khoản 1 Điều 579 Bộ luật Dân sự 2015 về nghĩa vụ hoàn trả như sau: "Người chiếm hữu, người sử dụng tài sản của người khác mà không có căn cứ pháp luật thì phải hoàn trả cho chủ sở hữu, chủ thể có quyền khác đối với tài sản đó; nếu không tìm được chủ sở hữu, chủ thể có quyền khác đối với tài sản thì phải giao cho cơ quan nhà nước có thẩm quyền, trừ trường hợp quy định tại Điều 236 Bộ …
- *Dự đoán:* Căn cứ tại Điều 2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.…
- *Ngữ cảnh lấy về:* `959/QĐ-BHXH#377986|595/QĐ-BHXH#327218|922/VBHN-BHXH#374499|2525/VBHN-BHXH#206453|959/QĐ-BHXH#377985`

**Q1214** (ROUGE-L 0.033, văn bản tham chiếu `Không trích xuất được`): Theo quy định hiện hành, mức lãi suất áp dụng cho các chương trình tín dụng chính sách tại Ngân hàng Chính sách xã hội hiện nay là bao nhiêu (đối với hộ nghèo, HS-SV, chương trình nước sạch, v.v.)?

- *Tham chiếu:* Căn cứ Điều 1 Quyết định 750/QĐ-TTg năm 2015 hướng dẫn về điều chỉnh giảm lãi suất cho vay đối với chương trình tín dụng chính sách tại Ngân hàng Chính sách xã hội như sau:

Điều 1. Điều chỉnh giảm lãi suất cho vay đối với một số chương trình tín dụng chính sách tại Ngân hàng Chính sách xã hội như sau:

1. Lãi suất cho vay hộ nghèo, cho vay học sinh, sinh viên, cho vay đối tượng chính sách đi lao …
- *Dự đoán:* Căn cứ tại Điều 6.1 và 6.2 Điểm 6.1, Điều 6.2, Điều 6.3 và Điều 6.4 Điểm 6.3, Điều 6.4, Điều 6.5 Điểm 6.5, Điều 6.6 Điểm 6.6, Điều 6.7 Điểm 6.7, Điều 6.8 Điểm 6.8, Điều 6.9 Điểm 6.9, Điều 6.10 Điểm 6.10, Điều 6.11 Điểm 6.11, Điều 6.12 Điểm 6.12, Điều 6.13 Điểm 6.13, Điều 6.14 Điểm 6.14, Điều 6.15 Điểm 6.15, Điều 6.16 Điểm 6.16, Điều 6.17 Điểm 6.17, Điều 6.18 Điểm 6.18, Điều 6.19 Điểm 6.19, Điều 6.…
- *Ngữ cảnh lấy về:* `8055/NHCS-TDSV#359082|71/2009/QĐ-TTg#348329|73/2008/TT-BTC#350968|1321/QĐ-UBND#80852|45/2024/NQ-HĐND#293644`

**Q1433** (ROUGE-L 0.072, văn bản tham chiếu `25/2013/TT-NHNN`): Theo quy định hiện hành, những trường hợp nào được coi là tiền không đạt tiêu chuẩn lưu thông (ví dụ tiền giấy, tiền kim loại bị hư hỏng hoặc lỗi kỹ thuật)?

- *Tham chiếu:* Tiền không đủ tiêu chuẩn lưu thông là tiền như thế nào?Căn cứ Điều 4 Thông tư 25/2013/TT-NHNN quy định về tiêu chuẩn tiền không đủ tiêu chuẩn lưu thông như sau:Điều 4. Tiêu chuẩn tiền không đủ tiêu chuẩn lưu thông1. Tiền rách nát, hư hỏng do quá trình lưu thông (nhóm nguyên nhân khách quan):a) Tiền giấy bị thay đổi màu sắc, mờ nhạt hình ảnh hoa văn, chữ, số; nhàu, nát, nhòe, bẩn, cũ; rách rời hay …
- *Dự đoán:* Theo các quy định pháp luật được trích dẫn, không có quy định cụ thể về thẩm quyền bổ nhiệm chức danh Tổng giám đốc (Giám đốc) tại một tổ chức tín dụng hoạt động theo mô hình công ty cổ phần. Tuy nhiên, có một số quy định liên quan đến chức danh và tiêu chuẩn nghiệp vụ của các vị trí công chức trong ngành Ngân hàng:

Căn cứ theo Điều 9 Thông tư 14/2022/TT-NHNN quy định về chức danh, mã số ngạch, t…
- *Ngữ cảnh lấy về:* `14/2022/TT-NHNN#105838|12/2019/TT-NHNN#75444|14/2022/TT-NHNN#105837|95#377129|04/NĐHN-BNV#17777`
