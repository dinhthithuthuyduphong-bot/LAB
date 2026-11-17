# Phân tích lỗi: `D_hybrid_rerank`

Số câu: 200

## Thống kê theo nhóm

| group       |   n |   ROUGE_L |   pred_words |   cites_unretrieved |   abstains |   starts_can_cu |
|:------------|----:|----------:|-------------:|--------------------:|-----------:|----------------:|
| covered     |  51 |     0.35  |      233.941 |               0.059 |      0.059 |           1     |
| not_covered | 149 |     0.206 |      252.698 |               0.168 |      0.107 |           0.973 |


- `cites_unretrieved`: tỷ lệ câu trả lời nhắc một số hiệu văn bản **không xuất hiện ở đâu** trong ngữ cảnh lấy về (dấu hiệu bịa).
- `abstains`: tỷ lệ câu trả lời nói không tìm thấy thông tin.

## Tốt nhất – nhóm `covered`

**Q1984** (ROUGE-L 0.831, văn bản tham chiếu `14/2022/TT-NHNN`): Những tiêu chuẩn về phẩm chất chung bắt buộc đối với công chức làm việc trong ngành Ngân hàng được quy định như thế nào theo văn bản hiện hành?

- *Tham chiếu:* Căn cứ Điều 3 Thông tư 14/2022/TT-NHNN quy định tiêu chuẩn chung về phẩm chất của công chức ngân hàng như sau:
- Có bản lĩnh chính trị vững vàng, kiên định với chủ nghĩa Mác - Lênin, tư tưởng Hồ Chí Minh
- Nắm vững chủ trương, đường lối, quy định của Đảng, chính sách, pháp luật của Nhà nước
- Trung thành với Tổ quốc; bảo vệ lợi ích của Nhà nước, của nhân dân.
- Thực hiện đầy đủ nghĩa vụ của công c…
- *Dự đoán:* Căn cứ tại Điều 3, khoản 1, 2, 3, 4 Điều 3 và Điều 9 Điều 3 Thông tư 14/2022/TT-NHNN quy định mã số, tiêu chuẩn chuyên môn, nghiệp vụ và xếp lương đối với các ngạch công chức chuyên ngành Ngân hàng do Thống đốc Ngân hàng Nhà nước Việt Nam ban hành, quy định như sau:

- Công chức làm việc trong ngành Ngân hàng phải có bản lĩnh chính trị vững vàng, kiên định với chủ nghĩa Mác - Lênin, tư tưởng Hồ Ch…
- *Ngữ cảnh lấy về:* `14/2022/TT-NHNN#105811|14/2022/TT-NHNN#105812|12/2019/TT-NHNN#75418|956/2003/QĐ-NHNN#377662|12/2019/TT-NHNN#75445`

**Q1442** (ROUGE-L 0.776, văn bản tham chiếu `14/2022/TT-NHNN`): Những yêu cầu chung về phẩm chất đạo đức và chính trị mà một công chức làm việc trong hệ thống ngân hàng phải đáp ứng là gì?

- *Tham chiếu:* Căn cứ theo quy định tại Điều 3 Thông tư 14/2022/TT-NHNN, tiêu chuẩn chung về phẩm chất của công chức ngân hàng đó là:
- Có bản lĩnh chính trị vững vàng, kiên định với chủ nghĩa Mác - Lênin, tư tưởng Hồ Chí Minh; nắm vững chủ trương, đường lối, quy định của Đảng, chính sách, pháp luật của Nhà nước; trung thành với Tổ quốc; bảo vệ lợi ích của Nhà nước, của nhân dân.
- Thực hiện đầy đủ nghĩa vụ của …
- *Dự đoán:* Căn cứ tại Điều 3, khoản 1 Điều 3 Thông tư 14/2022/TT-NHNN quy định mã số, tiêu chuẩn chuyên môn, nghiệp vụ và xếp lương đối với các ngạch công chức chuyên ngành Ngân hàng do Thống đốc Ngân hàng Nhà nước Việt Nam ban hành, quy định:

- Có bản lĩnh chính trị vững vàng, kiên định với chủ nghĩa Mác - Lênin, tư tưởng Hồ Chí Minh; nắm vững chủ trương, đường lối, quy định của Đảng, chính sách, pháp luật…
- *Ngữ cảnh lấy về:* `14/2022/TT-NHNN#105811|14/2022/TT-NHNN#105812|956/2003/QĐ-NHNN#377662|956/2003/QĐ-NHNN#377675|12/2019/TT-NHNN#75418`

**Q2648** (ROUGE-L 0.645, văn bản tham chiếu `14/2022/TT-NHNN`): Theo quy định hiện hành, yêu cầu năng lực chuyên môn và nghiệp vụ cụ thể dành cho ngạch Nhân viên Tiền tệ - Kho quỹ gồm những nội dung nào?

- *Tham chiếu:* Tiêu chuẩn về năng lực chuyên môn, nghiệp vụ của ngạch Nhân viên Tiền tệ - Kho quỹ gồm những gì?Căn cứ quy định khoản 3 Điều 8 Thông tư 14/2022/TT-NHNN quy định về ngạch Nhân viên Tiền tệ - Kho quỹ như sau:Theo đó tiêu chuẩn về năng lực chuyên môn, nghiệp vụ của ngạch Nhân viên Tiền tệ - Kho quỹ gồm có:- Nắm vững chế độ, chính sách về quản lý tiền mặt và quản lý kho, quỹ của Ngân hàng Nhà nước;- N…
- *Dự đoán:* Căn cứ tại Điều 8. Ngạch Nhân viên Tiền tệ - Kho quỹ, Thông tư 14/2022/TT-NHNN quy định về tiêu chuẩn năng lực chuyên môn, nghiệp vụ như sau:

- Về năng lực chuyên môn, nghiệp vụ:
+ Nắm vững chế độ, chính sách về quản lý tiền mặt và quản lý kho, quỹ của Ngân hàng Nhà nước (Điều 8, điểm a);
+ Nắm vững quy định của Ngân hàng Nhà nước về thu đổi tiền rách nát, hư hỏng, không đủ tiêu chuẩn lưu thông (…
- *Ngữ cảnh lấy về:* `14/2022/TT-NHNN#105838|14/2022/TT-NHNN#105837|1170/QĐ-UBND#57449|14/2022/TT-NHNN#105835|223/QĐ-UBND#183034`

## Kém nhất – nhóm `covered`

**Q1261** (ROUGE-L 0.068, văn bản tham chiếu `07/VBHN-VPQH`): Văn bản Pháp lệnh về ngoại hối hiện hành là văn bản nào và những nghị định, thông tư hướng dẫn liên quan (đã cập nhật đến năm 2025) gồm những văn bản nào?

- *Tham chiếu:* Pháp lệnh ngoại hối mới nhất là Pháp lệnh ngoại hối 2005 được sửa đổi bởi Pháp lệnh sửa đổi Pháp lệnh ngoại hối năm 2013. Văn bản hợp nhất Pháp lệnh ngoại hối mới nhất là Văn bản hợp nhất 07/VBHN-VPQH năm 2013 hợp nhất Pháp lệnh Ngoại hối.

Dưới đây là các văn bản hướng dẫn Pháp lệnh Ngoại hối:

(1) Nghị định
- Nghị định 16/2014/NĐ-CP về quản lý cán cân thanh toán quốc tế của Việt Nam
- Nghị định …
- *Dự đoán:* Căn cứ tại Điều 3, Nghị định số 111/2022/NĐ-CP ngày 28 tháng 10 năm 2022 quy định:

Văn bản Pháp lệnh về ngoại hối hiện hành là Nghị định số 111/2022/NĐ-CP ngày 28 tháng 10 năm 2022 của Chính phủ. 

Những nghị định, thông tư hướng dẫn liên quan đến văn bản này (đã cập nhật đến năm 2025) gồm:

- Nghị định số 111/2022/NĐ-CP ngày 28 tháng 10 năm 2022 của Chính phủ quy định về quản lý ngoại hối và một…
- *Ngữ cảnh lấy về:* `1937/QĐ-BYT#154275|1176/QĐ-UBND#57911|1017/QĐ-UBND#38168|835/VBHN-BLĐTBXH#363449|3305/VBHN-BLĐTBXH#249171`

**Q38** (ROUGE-L 0.140, văn bản tham chiếu `6150/TB-BLĐTBXH`): Ngân hàng BIDV nghỉ Tết Nguyên đán 2025 theo lịch nào, chi tiết các ngày nghỉ và hoạt động kênh dịch vụ trong thời gian đó là ra sao?

- *Tham chiếu:* Lịch nghỉ Tết ngân hàng BIDV 2025 mới nhất, chi tiết?Theo Thông báo 6150/TB-BLĐTBXH năm 2024, lịch nghỉ Tết Nguyên đán 2025 chi tiết như sau:- Đối với cán bộ, công chức, viên chức và người lao động của các cơ quan hành chính, sự nghiệp, tổ chức chính trị, tổ chức chính trị - xã hội được nghỉ 09 ngày từ thứ Bảy ngày 25/1 (26 tháng Chạp năm Giáp Thìn) đến hết Chủ nhật ngày 2/2 (mùng 5 tháng Giêng nă…
- *Dự đoán:* Căn cứ tại Điều 1 Kế hoạch 94/KH-LĐLĐ năm 2024 quy định: "Những hình thức động viên, chăm lo khác. Có hình thức động viên đoàn viên công đoàn, người lao động trực Tết thực hiện tốt nhiệm vụ, đảm bảo an toàn." Đây là một trong những quy định liên quan đến việc tổ chức các hoạt động chăm lo tết cho người lao động. Tuy nhiên, không có thông tin cụ thể về lịch nghỉ Tết Nguyên đán 2025 hoặc chi tiết về…
- *Ngữ cảnh lấy về:* `94/KH-LĐLĐ#376964|146/KH-TLĐ#100747|48/KH-LĐLĐ#302800|84/KH-TLĐ#365319|09/TB-BTC#36088`

**Q2141** (ROUGE-L 0.141, văn bản tham chiếu `14/2022/TT-NHNN`): Theo quy định hiện hành, những yêu cầu phẩm chất chung mà một kiểm soát viên cao cấp ngân hàng phải đáp ứng là gì?

- *Tham chiếu:* Căn cứ theo Điều 3 Thông tư 14/2022/TT-NHNN, tiêu chuẩn chung về phẩm chất đối với kiểm soát viên cao cấp ngân hàng cụ thể như sau:
- Có bản lĩnh chính trị vững vàng, kiên định với chủ nghĩa Mác - Lênin, tư tưởng Hồ Chí Minh; nắm vững chủ trương, đường lối, quy định của Đảng, chính sách, pháp luật của Nhà nước; trung thành với Tổ quốc; bảo vệ lợi ích của Nhà nước, của nhân dân.
- Thực hiện đầy đủ …
- *Dự đoán:* Căn cứ tại Điều 4. Ngạch Kiểm soát viên cao cấp ngân hàng [Thông tư 14/2022/TT-NHNN], quy định như sau:

- Yêu cầu phẩm chất chung mà một kiểm soát viên cao cấp ngân hàng phải đáp ứng bao gồm:
  - Có kinh nghiệm trên các lĩnh vực nghiệp vụ tiền tệ, tín dụng, ngân hàng.
  - Có chứng chỉ bồi dưỡng kiến thức, kỹ năng quản lý nhà nước đối với công chức ngạch chuyên viên cao cấp (hoặc tương đương) hoặc…
- *Ngữ cảnh lấy về:* `14/2022/TT-NHNN#105819|14/2022/TT-NHNN#105818|12/2019/TT-NHNN#75423|12/2019/TT-NHNN#75425|12/2019/TT-NHNN#75424`

## Tốt nhất – nhóm `not_covered`

**Q701** (ROUGE-L 0.695, văn bản tham chiếu `571/2002/QĐ-NHNN`): Theo quy định hiện hành, Agribank được phép huy động vốn bằng những phương thức, công cụ nào?

- *Tham chiếu:* Theo khoản 1 Điều 5 Điều lệ về tổ chức và hoạt động của Ngân hàng Nông nghiệp và phát triển nông thôn Việt Nam ban hành kèm theo Quyết định 571/2002/QĐ-NHNN quy định như sau:

Điều 5.
1. Ngân hàng Nông nghiệp huy động vốn dưới các hình thức sau:
a) Nhận tiền gửi của các tổ chức, cá nhân và tổ chức tín dụng khác dưới các hình thức tiền gửi không kỳ hạn, tiền gửi có kỳ hạn và các loại tiền gửi khác.…
- *Dự đoán:* Căn cứ tại Điều 5, Chương 2, Mục 1, Điều 5 của Quyết định 122/2001/QĐ-NHNN ban hành Điều lệ mẫu về tổ chức và hoạt động của Ngân hàng thương mại nhà nước quy định: Ngân hàng huy động vốn dưới các hình thức như nhận tiền gửi của các tổ chức, cá nhân và các tổ chức tín dụng khác dưới các hình thức tiền gửi không kỳ hạn, tiền gửi có kỳ hạn và các loại tiền gửi khác; phát hành chứng chỉ tiền gửi, trái…
- *Ngữ cảnh lấy về:* `122/2001/QĐ-NHNN#68067|4468/QĐ-BNN-KTHT#288587|4468/QĐ-BNN-KTHT#288584|122/2020/QH14#68294|4468/QĐ-BNN-KTHT#288579`

**Q1881** (ROUGE-L 0.483, văn bản tham chiếu `115/2015/NĐ-CP`): Theo quy định hiện hành, vào thời điểm nào phải lấy tỷ giá ngoại tệ để chuyển đổi tiền lương tính đóng BHXH bắt buộc khi hợp đồng lao động ghi lương bằng ngoại tệ?

- *Tham chiếu:* Theo Điều 26 Nghị định 115/2015/NĐ-CP có quy định về chuyển đổi tiền lương bằng ngoại tệ sang đồng Việt Nam để đóng bảo hiểm xã hội như sau:

Điều 26. Quy định chuyển đổi tiền lương bằng ngoại tệ sang đồng Việt Nam để đóng bảo hiểm xã hội
Người lao động có tiền lương ghi trong hợp đồng lao động bằng ngoại tệ thì việc đóng bảo hiểm xã hội và ghi sổ bảo hiểm xã hội được thực hiện như sau:
1. Tiền lư…
- *Dự đoán:* Căn cứ tại Điều 3 Quyết định 902/QĐ-BHXH năm 2007 quy định về quản lý thu bảo hiểm xã hội, bảo hiểm y tế bắt buộc quy định: "Tiền lương, tiền công tháng đóng bảo hiểm xã hội được tính bằng đồng Việt Nam trên cơ sở tiền lương, tiền công bằng ngoại tệ được chuyển đổi bằng đồng Việt Nam theo tỷ giá giao dịch bình quân trên thị trường ngoại tệ liên ngân hàng do Ngân hàng Nhà nước Việt Nam công bố tại …
- *Ngữ cảnh lấy về:* `03/2007/TT-BLĐTBXH#10803|902/QĐ-BHXH#371635|1438/HD-BHXH#97910|06/TT-LĐTBXH#24564|17/2008/TT-BLĐTBXH#137684`

**Q430** (ROUGE-L 0.441, văn bản tham chiếu `94/2025/NĐ-CP`): Nếu cần mẫu đơn đề nghị dừng thử nghiệm có kiểm soát trong lĩnh vực ngân hàng, chỗ nào tải bản Mẫu số 07 (Phụ lục 1 kèm Nghị định 94/2025/NĐ-CP)?

- *Tham chiếu:* Tải về mẫu đơn đề nghị dừng thử nghiệm có kiểm soát trong lĩnh vực ngân hàng chi tiết ở đâu?

Căn cứ theo Mẫu số 07 Phụ lục 1 Danh mục mẫu văn bản hồ sơ, thủ tục ban hành kèm theo Nghị định 94/2025/NĐ-CP quy định như sau:

Dưới đây là Mẫu đơn đề nghị dừng thử nghiệm có kiểm soát trong lĩnh vực ngân hàng:

Tải về Mẫu đơn đề nghị dừng thử nghiệm có kiểm soát trong lĩnh vực ngân hàng:Tải về

Ghi chú:…
- *Dự đoán:* Căn cứ tại Điều 18, Khoản 1, Điểm e) Nghị định 49/2018/NĐ-CP quy định về kiểm định chất lượng giáo dục nghề nghiệp số 49/2018/NĐ-CP ngày 28/11/2018 quy định:

- Không có quy định cụ thể về mẫu đơn đề nghị dừng thử nghiệm có kiểm soát trong lĩnh vực ngân hàng.
- Theo đó, không thể trích dẫn được mẫu số 07 (Phụ lục 1 kèm Nghị định 94/2025/NĐ-CP) để tải mẫu đơn đề nghị dừng thử nghiệm có kiểm soát tr…
- *Ngữ cảnh lấy về:* `1986/QĐ-UBND#157934|5673/QĐ-UBND#320116|860/QĐ-BLĐTBXH#366496|49/2018/NĐ-CP#305213|1776/QĐ-CT#134469`

## Kém nhất – nhóm `not_covered`

**Q114** (ROUGE-L 0.010, văn bản tham chiếu `273/NQ-CP`): Có đúng là theo chỉ đạo của Chính phủ, phương án cơ cấu lại SCB phải được hoàn tất trước ngày 15/9/2025 không?

- *Tham chiếu:* Căn cứ theo tiểu tiết 3 tiết b tiểu mục 1 Mục 2 Nghị quyết 273/NQ-CP năm 2025, Chính phủ yêu cầu Ngân hàng Nhà nước Việt Nam chủ trì, phối hợp với các cơ quan, địa phương chú trọng thực hiện hiệu quả các nội dung trọng tâm sau: II. Nhiệm vụ, giải pháp chủ yếu thời gian tới [...] 1. Tiếp tục ưu tiên tối đa cho thúc đẩy tăng trưởng gắn với giữ vững ổn định kinh tế vĩ mô, kiểm soát lạm phát, bảo đảm …
- *Dự đoán:* Căn cứ tại Điều 10, khoản 3, điểm 3, khoản 3, điểm 3, khoản 3, điểm 3, khoản 3, điểm 3, khoản 3, điểm 3, khoản 3, điểm 3, khoản 3, điểm 3, khoản 3, điểm 3, khoản 3, điểm 3, khoản 3, điểm 3, khoản 3, điểm 3, khoản 3, điểm 3, khoản 3, điểm 3, khoản 3, điểm 3, khoản 3, điểm 3, khoản 3, điểm 3, khoản 3, điểm 3, khoản 3, điểm 3, khoản 3, điểm 3, khoản 3, điểm 3, khoản 3, điểm 3, khoản 3, điểm 3, khoản …
- *Ngữ cảnh lấy về:* `19/2004/TT-BLĐTBXH#159316|5524/QĐ-UBND#317446|20/2005/QĐ-BTC#169596|6168/QĐ-UBND#330582|20/2005/QĐ-BTC#169614`

**Q2047** (ROUGE-L 0.020, văn bản tham chiếu `32/2015/TT-NHNN`): Kế toán trưởng của một quỹ tín dụng nhân dân có được nhận khoản vay dưới hình thức vay không có bảo đảm từ chính quỹ tín dụng đó hay không?

- *Tham chiếu:* Quỹ tín dụng nhân dân là gì? Căn cứ tại khoản 6 Điều 4 Luật Các tổ chức tín dụng 2010 có quy định về quỹ tín dụng nhân dân như sau:
Giải thích từ ngữ
Trong Luật này, các từ ngữ dưới đây được hiểu như sau:...6. Quỹ tín dụng nhân dân là tổ chức tín dụng do các pháp nhân, cá nhân và hộ gia đình tự nguyện thành lập dưới hình thức hợp tác xã để thực hiện một số hoạt động ngân hàng theo quy định của Luậ…
- *Dự đoán:* Căn cứ tại Điều 1, Điều 2, Điều 7 và Điều 11, Điều 12, Điều 13, Điều 14, Điều 15, Điều 16, Điều 17, Điều 18, Điều 19, Điều 20, Điều 21, Điều 22, Điều 23, Điều 24, Điều 25, Điều 26, Điều 27, Điều 28, Điều 29, Điều 30, Điều 31, Điều 32, Điều 33, Điều 34, Điều 35, Điều 36, Điều 37, Điều 38, Điều 39, Điều 40, Điều 41, Điều 42, Điều 43, Điều 44, Điều 45, Điều 46, Điều 47, Điều 48, Điều 49, Điều 50, Điề…
- *Ngữ cảnh lấy về:* `337/QĐ-UBND#250999|06/CT-TTg#24044|06/CT-TTg#24040|06/CT-TTg#24046|365/2004/QĐ-NHNN#262464`

**Q1402** (ROUGE-L 0.020, văn bản tham chiếu `32/2024/TT-NHNN`): Chức năng và phạm vi hoạt động của văn phòng đại diện trong nước thuộc sở hữu ngân hàng thương mại được quy định như thế nào theo Thông tư 32/2024/TT-NHNN?

- *Tham chiếu:* Căn cứ theo quy định tại khoản 5 Điều 3 Thông tư 32/2024/TT-NHNN như sau:
Điều 3. Giải thích từ ngữ
Trong Thông tư này, những từ ngữ dưới đây được hiểu như sau:[...]4. Chi nhánh quản lý phòng giao dịch là chi nhánh được giao thực hiện một số nội dung quản lý đối với phòng giao dịch trên địa bàn cùng một tỉnh, thành phố theo quy định nội bộ của ngân hàng thương mại và phù hợp với quy định của Thông…
- *Dự đoán:* Căn cứ tại Điều 25, Điểm d Khoản 2 Điều 18, Điều 21, Điều 4, Điều 1, Điều 25, Điều 18, Điều 21, Điều 4, Điều 1, Điều 25, Điều 18, Điều 21, Điều 4, Điều 1, Điều 25, Điều 18, Điều 21, Điều 4, Điều 1, Điều 25, Điều 18, Điều 21, Điều 4, Điều 1, Điều 25, Điều 18, Điều 21, Điều 4, Điều 1, Điều 25, Điều 18, Điều 21, Điều 4, Điều 1, Điều 25, Điều 18, Điều 21, Điều 4, Điều 1, Điều 25, Điều 18, Điều 21, Điề…
- *Ngữ cảnh lấy về:* `122/2001/QĐ-NHNN#68084|1370/QĐ-NHNN#86602|15/2019/NĐ-CP#116771|1370/QĐ-NHNN#86595|122/2001/QĐ-NHNN#68089`
