# Phân tích lỗi: `B_bm25_legal`

Số câu: 200

## Thống kê theo nhóm

| group       |   n |   ROUGE_L |   pred_words |   cites_unretrieved |   abstains |   starts_can_cu |
|:------------|----:|----------:|-------------:|--------------------:|-----------:|----------------:|
| covered     |  51 |     0.32  |      238.745 |               0.078 |      0.039 |           0.98  |
| not_covered | 149 |     0.193 |      233.49  |               0.168 |      0.121 |           0.926 |


- `cites_unretrieved`: tỷ lệ câu trả lời nhắc một số hiệu văn bản **không xuất hiện ở đâu** trong ngữ cảnh lấy về (dấu hiệu bịa).
- `abstains`: tỷ lệ câu trả lời nói không tìm thấy thông tin.

## Tốt nhất – nhóm `covered`

**Q2648** (ROUGE-L 0.628, văn bản tham chiếu `14/2022/TT-NHNN`): Theo quy định hiện hành, yêu cầu năng lực chuyên môn và nghiệp vụ cụ thể dành cho ngạch Nhân viên Tiền tệ - Kho quỹ gồm những nội dung nào?

- *Tham chiếu:* Tiêu chuẩn về năng lực chuyên môn, nghiệp vụ của ngạch Nhân viên Tiền tệ - Kho quỹ gồm những gì?Căn cứ quy định khoản 3 Điều 8 Thông tư 14/2022/TT-NHNN quy định về ngạch Nhân viên Tiền tệ - Kho quỹ như sau:Theo đó tiêu chuẩn về năng lực chuyên môn, nghiệp vụ của ngạch Nhân viên Tiền tệ - Kho quỹ gồm có:- Nắm vững chế độ, chính sách về quản lý tiền mặt và quản lý kho, quỹ của Ngân hàng Nhà nước;- N…
- *Dự đoán:* Căn cứ tại Điều 7, Điều 8, Điều 11 Thông tư 14/2022/TT-NHNN quy định về ngạch công chức chuyên ngành Ngân hàng, Bộ trưởng Ngân hàng Nhà nước quy định:

Yêu cầu năng lực chuyên môn và nghiệp vụ cụ thể dành cho ngạch Nhân viên Tiền tệ - Kho quỹ gồm những nội dung sau:

- Nắm vững chế độ, chính sách về quản lý tiền mặt và quản lý kho, quỹ của Ngân hàng Nhà nước (Điều 8, Thông tư 14/2022/TT-NHNN).
- N…
- *Ngữ cảnh lấy về:* `14/2022/TT-NHNN#105835|14/2022/TT-NHNN#105845|14/2022/TT-NHNN#105838|1170/QĐ-UBND#57449|29/2022/TT-BTC#234551`

**Q1707** (ROUGE-L 0.612, văn bản tham chiếu `14/2022/TT-NHNN`): Những chức danh và mã số ngạch nào được quy định cho công chức thuộc chuyên ngành Ngân hàng?

- *Tham chiếu:* Căn cứ theo Điều 2 Thông tư 14/2022/TT-NHNN quy định như sau:

Điều 2. Chức danh và mã số ngạch các ngạch công chức chuyên ngành Ngân hàng, gồm:
1. Kiểm soát viên cao cấp ngân hàng Mã số: 07.044
2. Kiểm soát viên chính ngân hàng Mã số: 07.045
3. Kiểm soát viên ngân hàng Mã số: 07.046
4. Thủ kho, thủ quỹ ngân hàng Mã số: 07.048
5. Nhân viên Tiền tệ - Kho quỹ Mã số: 07.047

Như vậy, công chức chuyên…
- *Dự đoán:* Căn cứ tại Điều 1, Khoản 1, Điểm 1 và Điểm 2 Điều 2 Thông tư 12/2019/TT-NHNN quy định về chức danh, mã số ngạch, tiêu chuẩn nghiệp vụ và cách xếp lương các ngạch công chức ngành Ngân hàng do Ngân hàng Nhà nước Việt Nam ban hành (tất cả đều hết hiệu lực từ ngày 01/01/2023), quy định:

- Chức danh và mã số ngạch công chức ngành Ngân hàng gồm:
  1. Ngạch Kiểm soát viên cao cấp ngân hàng
  Mã số ngạch…
- *Ngữ cảnh lấy về:* `12/2019/TT-NHNN#75418|12/2019/TT-NHNN#75417|14/2022/TT-NHNN#105810|12/2019/TT-NHNN#75416|14/2022/TT-NHNN#105842`

**Q46** (ROUGE-L 0.602, văn bản tham chiếu `6150/TB-BLĐTBXH`): Ngân hàng OCB (Ngân hàng TMCP Phương Đông) nghỉ Tết Âm lịch năm 2025 vào ngày nào và lịch khai trương trở lại ra sao?

- *Tham chiếu:* Căn cứ theo Thông báo 6150/TB-BLĐTBXH năm 2024 hướng dẫn nghỉ Tết Âm lịch 2025 đối với cán bộ, công chức, viên chức và người lao động như sau:
- Cán bộ, công chức, viên chức và người lao động của các cơ quan hành chính, sự nghiệp, tổ chức chính trị, tổ chức chính trị - xã hội được nghỉ Tết Âm lịch 2025 từ ngày 25/01/2025 đến hết Chủ nhật ngày 02/02/2025 dương lịch (tức ngày 26 tháng Chạp năm Giáp …
- *Dự đoán:* Căn cứ tại Điều 1 Thông báo 6150/TB-BLĐTBXH năm 2024 quy định:

Công chức, viên chức và người lao động của các cơ quan hành chính, sự nghiệp, tổ chức chính trị, tổ chức chính trị - xã hội được nghỉ dịp tết Âm lịch năm 2025 từ thứ Bảy ngày 25/01/2025 Dương lịch (tức ngày 26 tháng Chạp năm Giáp Thìn) đến hết Chủ nhật ngày 02/02/2025 Dương lịch (tức ngày mùng 5 tháng Giêng năm Ất Tỵ).

Căn cứ tại Điề…
- *Ngữ cảnh lấy về:* `6150/TB-BLĐTBXH#330482|1202/TB-UBND#65796|1202/TB-UBND#65797|4875/TB-BLĐTBXH#301053|6150/TB-BLĐTBXH#330485`

## Kém nhất – nhóm `covered`

**Q1261** (ROUGE-L 0.074, văn bản tham chiếu `07/VBHN-VPQH`): Văn bản Pháp lệnh về ngoại hối hiện hành là văn bản nào và những nghị định, thông tư hướng dẫn liên quan (đã cập nhật đến năm 2025) gồm những văn bản nào?

- *Tham chiếu:* Pháp lệnh ngoại hối mới nhất là Pháp lệnh ngoại hối 2005 được sửa đổi bởi Pháp lệnh sửa đổi Pháp lệnh ngoại hối năm 2013. Văn bản hợp nhất Pháp lệnh ngoại hối mới nhất là Văn bản hợp nhất 07/VBHN-VPQH năm 2013 hợp nhất Pháp lệnh Ngoại hối.

Dưới đây là các văn bản hướng dẫn Pháp lệnh Ngoại hối:

(1) Nghị định
- Nghị định 16/2014/NĐ-CP về quản lý cán cân thanh toán quốc tế của Việt Nam
- Nghị định …
- *Dự đoán:* Căn cứ tại Điều 5.3 Thông tư 06/2008/TT-BTP hướng dẫn về tổ chức cán bộ các cơ quan thi hành án dân sự địa phương số 06/2008/TT-BTP ngày 15/02/2008 quy định:

Văn bản Pháp lệnh về ngoại hối hiện hành là văn bản chưa được xác định trong các trích đoạn được cung cấp. Để trả lời câu hỏi này chính xác, cần truy cứu thêm vào các văn bản pháp luật về ngoại hối hiện hành.

Những nghị định, thông tư hướng…
- *Ngữ cảnh lấy về:* `1937/QĐ-BYT#154275|1176/QĐ-UBND#57862|1176/QĐ-UBND#57911|1176/QĐ-UBND#58035|06/2008/TT-BTP#21925`

**Q30** (ROUGE-L 0.101, văn bản tham chiếu `6150/TB-BLĐTBXH`): Vietcombank sẽ nghỉ Tết Nguyên đán 2025 trong khoảng thời gian nào, và khi nào ngân hàng hoạt động trở lại? (vui lòng nêu căn cứ pháp lý nếu có)

- *Tham chiếu:* Theo Thông báo 6150/TB-BLĐTBXH năm 2024, lịch nghỉ Tết Nguyên đán 2025 chi tiết như sau:
- Đối với cán bộ, công chức, viên chức và người lao động của các cơ quan hành chính, sự nghiệp, tổ chức chính trị, tổ chức chính trị - xã hội được nghỉ 09 ngày từ thứ Bảy ngày 25/1 (26 tháng Chạp năm Giáp Thìn) đến hết Chủ nhật ngày 2/2 (mùng 5 tháng Giêng năm Ất Tỵ). Đợt nghỉ này bao gồm 05 ngày nghỉ tết Âm l…
- *Dự đoán:* Theo các văn bản pháp luật được cung cấp, không có quy định cụ thể về việc nghỉ Tết Nguyên đán hay thời gian hoạt động trở lại của các tổ chức, doanh nghiệp, bao gồm cả Vietcombank. Các văn bản chỉ đề cập đến các hoạt động chăm sóc, động viên người lao động trong dịp Tết Nguyên đán, nhưng không đưa ra thông tin về lịch nghỉ Tết hoặc thời gian hoạt động trở lại của các tổ chức.

Căn cứ tại Điều 111…
- *Ngữ cảnh lấy về:* `146/KH-TLĐ#100748|84/KH-TLĐ#365319|15/2017/QĐ-UBND#116390|84/KH-TLĐ#365336|84/KH-TLĐ#365320`

**Q1441** (ROUGE-L 0.126, văn bản tham chiếu `14/2022/TT-NHNN`): Người tốt nghiệp cử nhân ngành luật có đủ điều kiện để tuyển dụng vào các vị trí công chức tại Ngân hàng Nhà nước không, và nếu được thì ở những ngạch nào?

- *Tham chiếu:* Từ những căn cứ sau đây, cử nhân luật có thể trở thành công chức ngân hàng đối với một số ngạch (không áp dụng cho tất cả các ngạch):

Căn cứ theo điểm a khoản 4 Điều 4 Thông tư 14/2022/TT-NHNN quy định như sau:
Điều 4. Ngạch Kiểm soát viên cao cấp ngân hàng
[...]4. Tiêu chuẩn về trình độ đào tạo, bồi dưỡnga) Có bằng tốt nghiệp đại học trở lên với ngành hoặc chuyên ngành: kinh tế, tài chính, ngân …
- *Dự đoán:* Căn cứ tại Điều 5, Điểm a Khoản 4 Quyết định 28/2006/QĐ-NHNN quy định: "CB, CC, VC cấp Vụ và tương đương, lãnh đạo Chi nhánh Ngân hàng Nhà nước tỉnh, thành phố trực thuộc Trung ương" thì người tốt nghiệp cử nhân ngành luật có thể đáp ứng điều kiện cử đi đào tạo văn bằng cấp quốc gia. Tuy nhiên, để tuyển dụng vào các vị trí công chức tại Ngân hàng Nhà nước, người này cần đáp ứng thêm các điều kiện …
- *Ngữ cảnh lấy về:* `28/2006/QĐ-NHNN#226375|12/2019/TT-NHNN#75448|09/2004/TT-BNV#32967|276/1997/QĐ-NH9#219489|28/2006/QĐ-NHNN#226373`

## Tốt nhất – nhóm `not_covered`

**Q1881** (ROUGE-L 0.410, văn bản tham chiếu `115/2015/NĐ-CP`): Theo quy định hiện hành, vào thời điểm nào phải lấy tỷ giá ngoại tệ để chuyển đổi tiền lương tính đóng BHXH bắt buộc khi hợp đồng lao động ghi lương bằng ngoại tệ?

- *Tham chiếu:* Theo Điều 26 Nghị định 115/2015/NĐ-CP có quy định về chuyển đổi tiền lương bằng ngoại tệ sang đồng Việt Nam để đóng bảo hiểm xã hội như sau:

Điều 26. Quy định chuyển đổi tiền lương bằng ngoại tệ sang đồng Việt Nam để đóng bảo hiểm xã hội
Người lao động có tiền lương ghi trong hợp đồng lao động bằng ngoại tệ thì việc đóng bảo hiểm xã hội và ghi sổ bảo hiểm xã hội được thực hiện như sau:
1. Tiền lư…
- *Dự đoán:* Căn cứ tại Điều 3 Quyết định 902/QĐ-BHXH năm 2007 quy định về quản lý thu bảo hiểm xã hội, bảo hiểm y tế bắt buộc quy định:

2.4. Tiền lương, tiền công tháng để đóng BHXH của người lao động thuộc các hộ kinh doanh cá thể, tổ hợp tác và cá nhân là mức tiền lương, tiền công do người sử dụng lao động quy định nhưng phải đăng ký với cơ quan quản lý nhà nước về lao động theo phân cấp quản lý. 

2.4.1. …
- *Ngữ cảnh lấy về:* `03/2007/TT-BLĐTBXH#10803|902/QĐ-BHXH#371635|1438/HD-BHXH#97910|17/2008/TT-BLĐTBXH#137684|119-HĐBT#60434`

**Q1930** (ROUGE-L 0.405, văn bản tham chiếu `52/2024/NĐ-CP`): Những loại hình dịch vụ nào được xếp vào nhóm "dịch vụ thanh toán không qua tài khoản" theo quy định pháp luật?

- *Tham chiếu:* Theo quy định tại Điều 18 Nghị định 52/2024/NĐ-CP quy định về dịch vụ thanh toán không qua tài khoản thanh toán như sau:Điều 18. Dịch vụ thanh toán không qua tài khoản thanh toán của khách hàng1. Dịch vụ thanh toán không qua tài khoản thanh toán của khách hàng, bao gồm:a) Thực hiện dịch vụ thanh toán: chuyển tiền, thu hộ, chi hộ;b) Các dịch vụ thanh toán khác không qua tài khoản thực hiện theo quy…
- *Dự đoán:* Căn cứ tại Điều 2, Điểm a Khoản 2 Điều 1 Thông tư 02/2011/TT-NHNN quy định: "Dịch vụ thanh toán không qua tài khoản bao gồm các dịch vụ thanh toán không sử dụng tài khoản ngân hàng như chuyển tiền qua hệ thống chuyển mạch ngân hàng, chuyển tiền qua hệ thống thanh toán điện tử, thanh toán qua thẻ tín dụng, thẻ ghi nợ, thanh toán qua dịch vụ chuyển tiền điện tử, thanh toán qua hình thức chuyển tiền …
- *Ngữ cảnh lấy về:* `20/2007/CT-TTg#169706|06/CT-UBND#24181|18/2007/CT-UBND#148971|17/CT-UBND#139817|20/CT-UBND#172046`

**Q1057** (ROUGE-L 0.391, văn bản tham chiếu `26/2024/TT-NHNN`): Khi nào thì hợp đồng cho thuê tài chính giữa công ty cho thuê tài chính và bên thuê tài chính được coi là có hiệu lực?

- *Tham chiếu:* Căn cứ theo khoản 2 Điều 18 Thông tư 26/2024/TT-NHNN quy định về hợp đồng cho thuê tài chính như sau:
Điều 18. Hợp đồng cho thuê tài chính
[...]2. Hợp đồng cho thuê tài chính có hiệu lực từ ngày được các bên thỏa thuận trong hợp đồng cho thuê tài chính.
3. Việc đăng ký hợp đồng cho thuê tài chính thực hiện theo quy định của pháp luật.

Theo đó, hợp đồng cho thuê tài chính của công ty cho thuê tài …
- *Dự đoán:* Căn cứ tại Điều 4.1 điểm a Khoản 1 Điều 1 Thông tư 03/2019/TT-BNV sửa đổi quy định về hợp đồng cho thuê tài sản quy định: "Hợp đồng thuê khoán tài sản được ký kết giữa bên giao tài sản và bên thuê tài sản theo quy định của Bộ luật Dân sự". 

Căn cứ tại Điều 11 Quyết định 122/2001/QĐ-NHNN ban hành Điều lệ mẫu về tổ chức và hoạt động của Ngân hàng thương mại nhà nước quy định: "Ngân hàng phải thành …
- *Ngữ cảnh lấy về:* `03/2019/TT-BNV#12108|15/2001/TT-BTCCBCP#114326|29/2005/TT-BLĐTBXH#232782|122/2001/QĐ-NHNN#68073|39/2016/NĐ-CP#274059`

## Kém nhất – nhóm `not_covered`

**Q2698** (ROUGE-L 0.015, văn bản tham chiếu `Không trích xuất được`): Trong Luật Các tổ chức tín dụng 2024 có quy định gì mới về khái niệm và xử lý khi xảy ra rút tiền hàng loạt tại tổ chức tín dụng (so với luật trước đây)?

- *Tham chiếu:* Theo khoản 31 Điều 4 Luật Các tổ chức tín dụng 2024 quy định về rút tiền hàng loạt như sau:
Giải thích từ ngữ Trong Luật này, các từ ngữ dưới đây được hiểu như sau:... 
31. Rút tiền hàng loạt là việc tổ chức tín dụng bị nhiều người gửi tiền cùng rút tiền dẫn đến tổ chức tín dụng có nguy cơ mất khả năng chi trả hoặc mất khả năng chi trả theo quy định của Thống đốc Ngân hàng Nhà nước.

Ngoài ra, Luậ…
- *Dự đoán:* Căn cứ tại Điều 1, Điều 2, Điều 3, Điều 4, Điều 5, Điều 6, Điều 7, Điều 8, Điều 9, Điều 10, Điều 11, Điều 12, Điều 13, Điều 14, Điều 15, Điều 16, Điều 17, Điều 18, Điều 19, Điều 20, Điều 21, Điều 22, Điều 23, Điều 24, Điều 25, Điều 26, Điều 27, Điều 28, Điều 29, Điều 30, Điều 31, Điều 32, Điều 33, Điều 34, Điều 35, Điều 36, Điều 37, Điều 38, Điều 39, Điều 40, Điều 41, Điều 42, Điều 43, Điều 44, Đi…
- *Ngữ cảnh lấy về:* `07/2006/QĐ-BNV#25138|20/2019/TT-BLĐTBXH#171209|2270/QĐ-BNV#184732|06/CT-TTg#24047|20/VBHN-NHNN#172463`

**Q2284** (ROUGE-L 0.019, văn bản tham chiếu `46/2014/TT-NHNN`): Khi thực hiện cung cấp dịch vụ thanh toán điện tử, tổ chức cung ứng phải đáp ứng những yêu cầu pháp lý nào?

- *Tham chiếu:* Căn cứ Điều 5 Thông tư 46/2014/TT-NHNN quy định dịch vụ thanh toán giao dịch bằng phương tiện điện tử:
Điều 5. Dịch vụ thanh toán giao dịch bằng phương tiện điện tử
Tổ chức cung ứng dịch vụ thanh toán khi cung ứng các dịch vụ thanh toán giao dịch bằng phương tiện điện tử phải đáp ứng các yêu cầu sau:
1. Tuân thủ các quy định về việc lập, xử lý, sử dụng, bảo quản, lưu trữ chứng từ điện tử theo quy …
- *Dự đoán:* Căn cứ tại Điều 11, Khoản 1, Điểm c và d Điều 12, Khoản 1, Điểm c Điều 13, Khoản 1 Điều 14, Khoản 1 Điều 15, Điều 16, Điều 17, Điều 18, Điều 19, Điều 20, Điều 21, Điều 22, Điều 23, Điều 24, Điều 25, Điều 26, Điều 27, Điều 28, Điều 29, Điều 30, Điều 31, Điều 32, Điều 33, Điều 34, Điều 35, Điều 36, Điều 37, Điều 38, Điều 39, Điều 40, Điều 41, Điều 42, Điều 43, Điều 44, Điều 45, Điều 46, Điều 47, Điề…
- *Ngữ cảnh lấy về:* `20/2007/CT-TTg#169704|124/KH-UBND#69565|20/2007/CT-TTg#169705|1823/KH-BHXH#142003|1823/KH-BHXH#142004`

**Q1673** (ROUGE-L 0.024, văn bản tham chiếu `32/2015/TT-NHNN`): Những khoản mục chính nào phải được đưa vào quy định nội bộ của quỹ tín dụng nhân dân liên quan tới việc duy trì tỷ lệ an toàn vốn tối thiểu?

- *Tham chiếu:* Tại khoản 2 Điều 4 Thông tư 32/2015/TT-NHNN được sửa đổi bởi khoản 4 Điều 1 Thông tư 13/2024/TT-NHNN quy định như sau:

Điều 4. Quy định nội bộ
1. Quỹ tín dụng nhân dân phải có quy định nội bộ về quản lý tỷ lệ an toàn vốn tối thiểu, quản lý thanh khoản (tỷ lệ khả năng chi trả, tỷ lệ tối đa của nguồn vốn ngắn hạn được sử dụng để cho vay trung hạn và dài hạn, tỷ lệ tổng mức nhận tiền gửi so với vốn …
- *Dự đoán:* Căn cứ tại Điều 4, khoản 1, Điều 5, khoản 1 Điều 6, Điều 7, Điều 8, Điều 9, Điều 10, Điều 11, Điều 12, Điều 13, Điều 14, Điều 15, Điều 16, Điều 17, Điều 18, Điều 19, Điều 20, Điều 21, Điều 22, Điều 23, Điều 24, Điều 25, Điều 26, Điều 27, Điều 28, Điều 29, Điều 30, Điều 31, Điều 32, Điều 33, Điều 34, Điều 35, Điều 36, Điều 37, Điều 38, Điều 39, Điều 40, Điều 41, Điều 42, Điều 43, Điều 44, Điều 45, …
- *Ngữ cảnh lấy về:* `06/CT-TTg#24041|06/CT-TTg#24050|06/CT-TTg#24051|176/QĐ-TTg#133895|219/QĐ-NHNN#177805`
