# Phân tích lỗi: `E_full_fewshot`

Số câu: 200

## Thống kê theo nhóm

| group       |   n |   ROUGE_L |   pred_words |   cites_unretrieved |   abstains |   starts_can_cu |
|:------------|----:|----------:|-------------:|--------------------:|-----------:|----------------:|
| covered     |  51 |     0.329 |      238.078 |               0.02  |      0.157 |           0.765 |
| not_covered | 149 |     0.218 |      233.705 |               0.107 |      0.168 |           0.658 |


- `cites_unretrieved`: tỷ lệ câu trả lời nhắc một số hiệu văn bản **không xuất hiện ở đâu** trong ngữ cảnh lấy về (dấu hiệu bịa).
- `abstains`: tỷ lệ câu trả lời nói không tìm thấy thông tin.

## Tốt nhất – nhóm `covered`

**Q1442** (ROUGE-L 0.766, văn bản tham chiếu `14/2022/TT-NHNN`): Những yêu cầu chung về phẩm chất đạo đức và chính trị mà một công chức làm việc trong hệ thống ngân hàng phải đáp ứng là gì?

- *Tham chiếu:* Căn cứ theo quy định tại Điều 3 Thông tư 14/2022/TT-NHNN, tiêu chuẩn chung về phẩm chất của công chức ngân hàng đó là:
- Có bản lĩnh chính trị vững vàng, kiên định với chủ nghĩa Mác - Lênin, tư tưởng Hồ Chí Minh; nắm vững chủ trương, đường lối, quy định của Đảng, chính sách, pháp luật của Nhà nước; trung thành với Tổ quốc; bảo vệ lợi ích của Nhà nước, của nhân dân.
- Thực hiện đầy đủ nghĩa vụ của …
- *Dự đoán:* Căn cứ theo Điều 3 của Thông tư 12/2019/TT-NHNN quy định về chức danh, mã số ngạch, tiêu chuẩn nghiệp vụ và cách xếp lương các ngạch công chức ngành Ngân hàng, quy định như sau:

1. Có bản lĩnh chính trị vững vàng, kiên định với chủ nghĩa Mác - Lênin, tư tưởng Hồ Chí Minh; nắm vững chủ trương, đường lối, quy định của Đảng, chính sách, pháp luật của Nhà nước; trung thành với Tổ quốc; bảo vệ lợi ích…
- *Ngữ cảnh lấy về:* `14/2022/TT-NHNN#105811|14/2022/TT-NHNN#105812|956/2003/QĐ-NHNN#377662|956/2003/QĐ-NHNN#377675|12/2019/TT-NHNN#75418`

**Q1984** (ROUGE-L 0.684, văn bản tham chiếu `14/2022/TT-NHNN`): Những tiêu chuẩn về phẩm chất chung bắt buộc đối với công chức làm việc trong ngành Ngân hàng được quy định như thế nào theo văn bản hiện hành?

- *Tham chiếu:* Căn cứ Điều 3 Thông tư 14/2022/TT-NHNN quy định tiêu chuẩn chung về phẩm chất của công chức ngân hàng như sau:
- Có bản lĩnh chính trị vững vàng, kiên định với chủ nghĩa Mác - Lênin, tư tưởng Hồ Chí Minh
- Nắm vững chủ trương, đường lối, quy định của Đảng, chính sách, pháp luật của Nhà nước
- Trung thành với Tổ quốc; bảo vệ lợi ích của Nhà nước, của nhân dân.
- Thực hiện đầy đủ nghĩa vụ của công c…
- *Dự đoán:* Căn cứ theo Điều 3, khoản 1, điểm a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, và aa của Thông tư 14/2022/TT-NHNN quy định mã số, tiêu chuẩn chuyên môn, nghiệp vụ và xếp lương đối với các ngạch công chức chuyên ngành Ngân hàng do Thống đốc Ngân hàng Nhà nước Việt Nam ban hành, những tiêu chuẩn về phẩm chất chung bắt buộc đối với công chức làm việc trong ngành Ngân …
- *Ngữ cảnh lấy về:* `14/2022/TT-NHNN#105811|14/2022/TT-NHNN#105812|12/2019/TT-NHNN#75418|956/2003/QĐ-NHNN#377662|12/2019/TT-NHNN#75445`

**Q1440** (ROUGE-L 0.638, văn bản tham chiếu `14/2022/TT-NHNN`): Những chức danh nào được xếp vào nhóm công chức ngân hàng theo quy định hiện hành?

- *Tham chiếu:* Căn cứ theo Điều 2 Thông tư 14/2022/TT-NHNN, công chức ngân hàng gồm các chức danh dưới đây:
- Kiểm soát viên cao cấp ngân hàng, Mã số: 07.044
- Kiểm soát viên chính ngân hàng, Mã số: 07.045
- Kiểm soát viên ngân hàng, Mã số: 07.046
- Thủ kho, thủ quỹ ngân hàng, Mã số: 07.048
- Nhân viên Tiền tệ - Kho quỹ, Mã số: 07.047…
- *Dự đoán:* Căn cứ theo Điều 2 Thông tư 14/2022/TT-NHNN quy định mã số, tiêu chuẩn chuyên môn, nghiệp vụ và xếp lương đối với các ngạch công chức chuyên ngành Ngân hàng do Thống đốc Ngân hàng Nhà nước Việt Nam ban hành, chúng ta có thể xác định được các chức danh thuộc nhóm công chức ngân hàng như sau:

- Kiểm soát viên cao cấp ngân hàng (Mã số: 07.044)
- Kiểm soát viên chính ngân hàng (Mã số: 07.045)
- Kiểm …
- *Ngữ cảnh lấy về:* `12/2019/TT-NHNN#75417|12/2019/TT-NHNN#75446|14/2022/TT-NHNN#105810|112/QĐ-NH9#54056|14/2022/TT-NHNN#105840`

## Kém nhất – nhóm `covered`

**Q1261** (ROUGE-L 0.101, văn bản tham chiếu `07/VBHN-VPQH`): Văn bản Pháp lệnh về ngoại hối hiện hành là văn bản nào và những nghị định, thông tư hướng dẫn liên quan (đã cập nhật đến năm 2025) gồm những văn bản nào?

- *Tham chiếu:* Pháp lệnh ngoại hối mới nhất là Pháp lệnh ngoại hối 2005 được sửa đổi bởi Pháp lệnh sửa đổi Pháp lệnh ngoại hối năm 2013. Văn bản hợp nhất Pháp lệnh ngoại hối mới nhất là Văn bản hợp nhất 07/VBHN-VPQH năm 2013 hợp nhất Pháp lệnh Ngoại hối.

Dưới đây là các văn bản hướng dẫn Pháp lệnh Ngoại hối:

(1) Nghị định
- Nghị định 16/2014/NĐ-CP về quản lý cán cân thanh toán quốc tế của Việt Nam
- Nghị định …
- *Dự đoán:* Căn cứ tại Điều 1 Nghị định số 111/2022/NĐ-CP ngày 18 tháng 10 năm 2022 của Chính phủ quy định về quản lý ngoại hối và một số quy định liên quan, hiện nay văn bản pháp lệnh về ngoại hối hiện hành là Nghị định số 111/2022/NĐ-CP.

Để biết thêm thông tin về các nghị định, thông tư hướng dẫn liên quan đến quản lý ngoại hối, cần truy cập trực tiếp vào văn bản này hoặc các văn bản pháp luật liên quan để…
- *Ngữ cảnh lấy về:* `1937/QĐ-BYT#154275|1176/QĐ-UBND#57911|1017/QĐ-UBND#38168|835/VBHN-BLĐTBXH#363449|3305/VBHN-BLĐTBXH#249171`

**Q2141** (ROUGE-L 0.129, văn bản tham chiếu `14/2022/TT-NHNN`): Theo quy định hiện hành, những yêu cầu phẩm chất chung mà một kiểm soát viên cao cấp ngân hàng phải đáp ứng là gì?

- *Tham chiếu:* Căn cứ theo Điều 3 Thông tư 14/2022/TT-NHNN, tiêu chuẩn chung về phẩm chất đối với kiểm soát viên cao cấp ngân hàng cụ thể như sau:
- Có bản lĩnh chính trị vững vàng, kiên định với chủ nghĩa Mác - Lênin, tư tưởng Hồ Chí Minh; nắm vững chủ trương, đường lối, quy định của Đảng, chính sách, pháp luật của Nhà nước; trung thành với Tổ quốc; bảo vệ lợi ích của Nhà nước, của nhân dân.
- Thực hiện đầy đủ …
- *Dự đoán:* Căn cứ theo Điều 4 Thông tư 12/2019/TT-NHNN quy định về chức danh, mã số ngạch, tiêu chuẩn nghiệp vụ và cách xếp lương các ngạch công chức ngành Ngân hàng do Ngân hàng Nhà nước Việt Nam ban hành, những yêu cầu phẩm chất chung mà một kiểm soát viên cao cấp ngân hàng phải đáp ứng bao gồm:

- Có kinh nghiệm công tác ở ngạch kiểm soát viên chính ngân hàng hoặc tương đương. Công chức dự thi nâng ngạch …
- *Ngữ cảnh lấy về:* `14/2022/TT-NHNN#105819|14/2022/TT-NHNN#105818|12/2019/TT-NHNN#75423|12/2019/TT-NHNN#75425|12/2019/TT-NHNN#75424`

**Q2168** (ROUGE-L 0.171, văn bản tham chiếu `14/2022/TT-NHNN`): Mức hệ số lương áp dụng cho ngạch kiểm soát viên chính trong ngành ngân hàng hiện là bao nhiêu?

- *Tham chiếu:* Căn cứ theo điểm a khoản 1 Điều 10 Thông tư 14/2022/TT-NHNN quy định như sau:

Điều 10. Xếp lương các ngạch công chức chuyên ngành Ngân hàng
1. Các ngạch công chức chuyên ngành Ngân hàng quy định tại Thông tư này áp dụng Bảng 2 (Bảng lương chuyên môn, nghiệp vụ đối với cán bộ, công chức trong các cơ quan nhà nước) ban hành kèm theo Nghị định số 204/2004/NĐ-CP ngày 14 tháng 12 năm 2004 của Chính ph…
- *Dự đoán:* Căn cứ theo Điều 10, Mục 1, Điểm b) Thông tư 12/2019/TT-NHNN quy định về chức danh, mã số ngạch, tiêu chuẩn nghiệp vụ và cách xếp lương các ngạch công chức ngành Ngân hàng, mức hệ số lương áp dụng cho ngạch kiểm soát viên chính ngân hàng là từ hệ số lương 4,40 đến hệ số lương 6,78.…
- *Ngữ cảnh lấy về:* `14/2022/TT-NHNN#105840|12/2019/TT-NHNN#75446|12/2019/TT-NHNN#75417|14/2022/TT-NHNN#105841|12/2019/TT-NHNN#75429`

## Tốt nhất – nhóm `not_covered`

**Q701** (ROUGE-L 0.581, văn bản tham chiếu `571/2002/QĐ-NHNN`): Theo quy định hiện hành, Agribank được phép huy động vốn bằng những phương thức, công cụ nào?

- *Tham chiếu:* Theo khoản 1 Điều 5 Điều lệ về tổ chức và hoạt động của Ngân hàng Nông nghiệp và phát triển nông thôn Việt Nam ban hành kèm theo Quyết định 571/2002/QĐ-NHNN quy định như sau:

Điều 5.
1. Ngân hàng Nông nghiệp huy động vốn dưới các hình thức sau:
a) Nhận tiền gửi của các tổ chức, cá nhân và tổ chức tín dụng khác dưới các hình thức tiền gửi không kỳ hạn, tiền gửi có kỳ hạn và các loại tiền gửi khác.…
- *Dự đoán:* Căn cứ theo Điều 5 của Quyết định 122/2001/QĐ-NHNN ban hành Điều lệ mẫu về tổ chức và hoạt động của Ngân hàng thương mại nhà nước quy định: Ngân hàng huy động vốn dưới các hình thức như sau: 1. Nhận tiền gửi của các tổ chức, cá nhân và các tổ chức tín dụng khác dưới các hình thức tiền gửi không kỳ hạn, tiền gửi có kỳ hạn và các loại tiền gửi khác. 2. Phát hành chứng chỉ tiền gửi, trái phiếu và giấ…
- *Ngữ cảnh lấy về:* `122/2001/QĐ-NHNN#68067|4468/QĐ-BNN-KTHT#288587|4468/QĐ-BNN-KTHT#288584|122/2020/QH14#68294|4468/QĐ-BNN-KTHT#288579`

**Q1152** (ROUGE-L 0.475, văn bản tham chiếu `33/2024/TT-NHNN`): Giấy phép ghi thời hạn hoạt động của tổ chức tài chính vi mô tối đa bao lâu và phạm vi/địa bàn hoạt động được cấp theo những tiêu chí nào theo Thông tư 33/2024?

- *Tham chiếu:* Căn cứ Điều 26 Thông tư 33/2024/TT-NHNN quy định về thời hạn hoạt động và địa bàn hoạt động như sau:Điều 26. Thời hạn hoạt động và địa bàn hoạt động1. Thời hạn hoạt động của tổ chức tài chính vi mô được ghi trong Giấy phép tối đa không quá 50 năm.2. Địa bàn hoạt động của tổ chức tài chính vi mô được quy định trong Giấy phép.3. Tổ chức tài chính vi mô thực hiện mở rộng mạng lưới hoạt động ra ngoài …
- *Dự đoán:* Căn cứ theo Điều 1 Thông tư 33/2024 quy định như sau: Điều 1. Giấy phép ghi thời hạn hoạt động của tổ chức tài chính vi mô
1. Thời hạn hoạt động của tổ chức tài chính vi mô được ghi trong Giấy phép và tối đa không quá 05 năm, kể từ ngày cấp.
2. Phạm vi/địa bàn hoạt động của tổ chức tài chính vi mô được xác định dựa trên quy định của pháp luật về tổ chức và hoạt động của tổ chức tài chính vi mô.

N…
- *Ngữ cảnh lấy về:* `20/LĐTBXH-TT#172231|165/QĐ-UBND#122461|1345/VBHN-BLĐTBXH#83065|31/2024/QĐ-UBND#244882|31/2024/QĐ-UBND#244820`

**Q1881** (ROUGE-L 0.449, văn bản tham chiếu `115/2015/NĐ-CP`): Theo quy định hiện hành, vào thời điểm nào phải lấy tỷ giá ngoại tệ để chuyển đổi tiền lương tính đóng BHXH bắt buộc khi hợp đồng lao động ghi lương bằng ngoại tệ?

- *Tham chiếu:* Theo Điều 26 Nghị định 115/2015/NĐ-CP có quy định về chuyển đổi tiền lương bằng ngoại tệ sang đồng Việt Nam để đóng bảo hiểm xã hội như sau:

Điều 26. Quy định chuyển đổi tiền lương bằng ngoại tệ sang đồng Việt Nam để đóng bảo hiểm xã hội
Người lao động có tiền lương ghi trong hợp đồng lao động bằng ngoại tệ thì việc đóng bảo hiểm xã hội và ghi sổ bảo hiểm xã hội được thực hiện như sau:
1. Tiền lư…
- *Dự đoán:* Căn cứ tại Điều 3 Quyết định 902/QĐ-BHXH năm 2007 quy định về quản lý thu bảo hiểm xã hội, bảo hiểm y tế bắt buộc, do Tổng Giám đốc Bảo hiểm Xã hội Việt Nam ban hành, chúng ta có thể xác định:

1. Khi tiền lương, tiền công tháng đóng bảo hiểm xã hội được ghi trong hợp đồng lao động bằng ngoại tệ, thì tiền lương, tiền công tháng đóng bảo hiểm xã hội được tính bằng đồng Việt Nam trên cơ sở tiền lươn…
- *Ngữ cảnh lấy về:* `03/2007/TT-BLĐTBXH#10803|902/QĐ-BHXH#371635|1438/HD-BHXH#97910|06/TT-LĐTBXH#24564|17/2008/TT-BLĐTBXH#137684`

## Kém nhất – nhóm `not_covered`

**Q880** (ROUGE-L 0.017, văn bản tham chiếu `Không trích xuất được`): Theo Điều lệ ban hành kèm Quyết định 1515/QĐ-TTg, nhiệm vụ và chức năng chính của Ngân hàng Phát triển Việt Nam gồm những hoạt động nào?

- *Tham chiếu:* Căn cứ theo Điều 10 Điều lệ tổ chức và hoạt động của Ngân hàng Phát triển Việt Nam ban hành kèm theo Quyết định 1515/QĐ-TTg năm 2015, chức năng và nhiệm vụ của Ngân hàng Phát triển Việt Nam đó là:
- Hoạt động huy động vốn:
+ Phát hành trái phiếu được Chính phủ bảo lãnh theo quy định của pháp luật;
+ Phát hành trái phiếu, kỳ phiếu, chứng chỉ tiền gửi, giấy tờ có giá bằng đồng Việt Nam của Ngân hàng…
- *Dự đoán:* Căn cứ tại Điều 1, Điều 2, Điều 3, Điều 4, Điều 5, Điều 6, Điều 7, Điều 8, Điều 9, Điều 10, Điều 11, Điều 12, Điều 13, Điều 14, Điều 15, Điều 16, Điều 17, Điều 18, Điều 19, Điều 20, Điều 21, Điều 22, Điều 23, Điều 24, Điều 25, Điều 26, Điều 27, Điều 28, Điều 29, Điều 30, Điều 31, Điều 32, Điều 33, Điều 34, Điều 35, Điều 36, Điều 37, Điều 38, Điều 39, Điều 40, Điều 41, Điều 42, Điều 43, Điều 44, Đi…
- *Ngữ cảnh lấy về:* `122/2001/QĐ-NHNN#68109|122/2001/QĐ-NHNN#68108|405/QĐ-NHPT#275617|105/NQ-CP#42658|11/2007/TT-BLĐTBXH#61781`

**Q579** (ROUGE-L 0.080, văn bản tham chiếu `40/2024/TT-NHNN`): Khi đăng ký mở ví điện tử, người sử dụng phải nộp những giấy tờ, tài liệu và dữ liệu nào theo quy định hiện hành?

- *Tham chiếu:* Căn cứ theo Điều 18 Thông tư 40/2024/TT-NHNN quy định hồ sơ mở ví điện tử như sau:
(1) Hồ sơ mở ví điện tử bao gồm các tài liệu, thông tin, dữ liệu
- Thỏa thuận mở và sử dụng ví điện tử theo quy định tại Điều 19 Thông tư 40/2024/TT-NHNN;
- Các tài liệu, thông tin, dữ liệu để xác minh thông tin nhận biết khách hàng theo quy định tại (2), (3).

(2) Tài liệu, thông tin, dữ liệu về giấy tờ tùy thân củ…
- *Dự đoán:* Theo các văn bản pháp luật được cung cấp, không có quy định cụ thể về việc đăng ký mở ví điện tử hoặc nộp giấy tờ, tài liệu và dữ liệu nào cho việc này. Các văn bản chỉ đề cập đến quy trình nộp hồ sơ trực tuyến cho các thủ tục hành chính khác nhau như việc làm, giáo dục nghề nghiệp, bảo hiểm xã hội, và lĩnh vực khác. Do đó, không có thẩm quyền bổ nhiệm chức danh Tổng giám đốc (Giám đốc) tại một tổ…
- *Ngữ cảnh lấy về:* `936/QĐ-UBND#375623|78/QĐ-UBND#357391|3612/QĐ-BHXH#261415|71/QĐ-UBND#348636|2618/QĐ-UBND#211845`

**Q2392** (ROUGE-L 0.100, văn bản tham chiếu `48/2018/TT-NHNN`): Cho tôi hỏi quy cách tính lãi đối với tiền gửi tiết kiệm (cả không kỳ hạn và có kỳ hạn) theo quy định cập nhật 2024 như thế nào và ngân hàng phải nhận/chi trả tiền gửi ở đâu theo pháp luật?

- *Tham chiếu:* Hướng dẫn cách tính tiền lãi gửi tiết kiệm ngân hàng theo kỳ hạn mới nhất 2024 chi tiết như sau:

[1] Gửi tiết kiệm không kỳ hạn
Gửi tiền ngân hàng không kỳ hạn là một hình thức tiết kiệm linh hoạt cho phép người gửi tiền vào tài khoản ngân hàng mà không cần cam kết về thời gian. Tức người gửi có thể rút tiền mặt bất cứ thời điểm nào và không cần thông báo trước với ngân hàng.

Theo đó, cách tính …
- *Dự đoán:* Căn cứ theo Điều 6 Quyết định 40/2021/QĐ-TTg về Quỹ Hỗ trợ việc làm ngoài nước do Thủ tướng Chính phủ ban hành, quy định như sau:

- Ngân hàng thương mại được phép sử dụng tối đa 50% số kết dư Quỹ năm trước liền kề để gửi có kỳ hạn tại Ngân hàng thương mại Việt Nam nhưng kỳ hạn tối đa không quá 03 năm. Mức tiền gửi, kỳ hạn tiền gửi, chi nhánh ngân hàng nhận tiền gửi do Giám đốc Quỹ quyết định căn …
- *Ngữ cảnh lấy về:* `28/2019/QĐ-UBND#228041|28/2019/QĐ-UBND#228002|28/2019/QĐ-UBND#227980|40/2021/QĐ-TTg#277057|37/2013/QĐ-UBND#266933`
