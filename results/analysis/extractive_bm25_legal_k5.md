# Phân tích lỗi: `extractive_bm25_legal_k5`

Số câu: 200

## Thống kê theo nhóm

| group       |   n |   ROUGE_L |   pred_words |   cites_unretrieved |   abstains |   starts_can_cu |
|:------------|----:|----------:|-------------:|--------------------:|-----------:|----------------:|
| covered     |  51 |     0.337 |      393.902 |                   0 |      0     |               0 |
| not_covered | 149 |     0.159 |      400.168 |                   0 |      0.013 |               0 |


- `cites_unretrieved`: tỷ lệ câu trả lời nhắc một số hiệu văn bản **không xuất hiện ở đâu** trong ngữ cảnh lấy về (dấu hiệu bịa).
- `abstains`: tỷ lệ câu trả lời nói không tìm thấy thông tin.

## Tốt nhất – nhóm `covered`

**Q1570** (ROUGE-L 0.635, văn bản tham chiếu `5015/TB-LĐTBXH`): Ngân hàng Vietcombank có lịch nghỉ lễ Quốc khánh 2/9/2024 như thế nào? Căn cứ quy định chung, Vietcombank nghỉ những ngày nào trong dịp này?

- *Tham chiếu:* Căn cứ Mục 5 Thông báo 5015/TB-LĐTBXH năm 2023 về nghỉ tết Âm lịch và nghỉ lễ Quốc khánh năm 2024 đối với cán bộ, công chức, viên chức và người lao động:5. Đối với người lao động không thuộc đối tượng quy định tại khoản 1 Thông báo này, người sử dụng lao động quyết định lựa chọn phương án nghỉ tết Âm lịch và nghỉ lễ Quốc khánh năm 2024 như sau:- Đối với dịp nghỉ tết Âm lịch: lựa chọn 01 ngày cuối …
- *Dự đoán:* năm 2024 từ thứ Bảy ngày 31/8/2024 đến hết thứ Ba ngày 03/9/2024 Dương lịch. Đợt nghỉ này bao gồm 02 ngày nghỉ lễ Quốc khánh, 02 ngày nghỉ hằng tuần.
3. Các cơ quan, đơn vị thực hiện lịch nghỉ tết Âm lịch và nghỉ lễ Quốc khánh năm 2024 lưu ý thực hiện: bố trí, sắp xếp các bộ phận làm việc hợp lý để giải quyết công việc liên tục, đảm bảo tốt công tác phục vụ tổ chức, Nhân dân.
4. Các cơ quan, đơn v…
- *Ngữ cảnh lấy về:* `5015/TB-LĐTBXH#305998|5015/TB-LĐTBXH#305999|4875/TB-BLĐTBXH#301054|6150/TB-BLĐTBXH#330485|119/TB-LĐTBXH#61187`

**Q966** (ROUGE-L 0.611, văn bản tham chiếu `14/2022/TT-NHNN`): Ngạch kiểm soát viên trong ngành Ngân hàng được xếp vào loại bảng lương công chức nào theo quy định hiện hành?

- *Tham chiếu:* Căn cứ theo điểm c khoản 1 Điều 10 Thông tư 14/2022/TT-NHNN quy định như sau:
Điều 10. Xếp lương các ngạch công chức chuyên ngành Ngân hàng
1. Các ngạch công chức chuyên ngành Ngân hàng quy định tại Thông tư này áp dụng Bảng 2 (Bảng lương chuyên môn, nghiệp vụ đối với cán bộ, công chức trong các cơ quan nhà nước) ban hành kèm theo Nghị định số 204/2004/NĐ-CP ngày 14 tháng 12 năm 2004 của Chính phủ…
- *Dự đoán:* Điều 10. Xếp lương các ngạch công chức chuyên ngành Ngân hàng
1. Các ngạch công chức chuyên ngành Ngân hàng quy định tại Thông tư này áp dụng Bảng 2 (Bảng lương chuyên môn, nghiệp vụ đối với cán bộ, công chức trong các cơ quan nhà nước) ban hành kèm theo Nghị định số 204/2004/NĐ-CP ngày 14 tháng 12 năm 2004 của Chính phủ về chế độ tiền lương đối với cán bộ, công chức, viên chức và lực lượng vũ tra…
- *Ngữ cảnh lấy về:* `14/2022/TT-NHNN#105840|12/2019/TT-NHNN#75446|14/2022/TT-NHNN#105843|12/2019/TT-NHNN#75417|12/2019/TT-NHNN#75429`

**Q2140** (ROUGE-L 0.611, văn bản tham chiếu `14/2022/TT-NHNN`): Ngạch Kiểm soát viên cao cấp trong ngân hàng yêu cầu bằng đại học chuyên ngành nào theo quy định hiện hành?

- *Tham chiếu:* Căn cứ theo điểm a khoản 4 Điều 4 Thông tư 14/2022/TT-NHNN quy định như sau:
Điều 4. Ngạch Kiểm soát viên cao cấp ngân hàng...4. Tiêu chuẩn về trình độ đào tạo, bồi dưỡnga) Có bằng tốt nghiệp đại học trở lên với ngành hoặc chuyên ngành: kinh tế, tài chính, ngân hàng, kế toán, kiểm toán, công nghệ thông tin, xây dựng, luật;b) Có bằng tốt nghiệp cao cấp lý luận chính trị hoặc bằng cao cấp lý luận ch…
- *Dự đoán:* i) Có kinh nghiệm trên các lĩnh vực nghiệp vụ tiền tệ, tín dụng, ngân hàng.
4. Tiêu chuẩn về trình độ đào tạo, bồi dưỡng
a) Có bằng tốt nghiệp đại học trở lên với ngành hoặc chuyên ngành: kinh tế, tài chính, ngân hàng, kế toán, kiểm toán, công nghệ thông tin, xây dựng, luật;
b) Có bằng tốt nghiệp cao cấp lý luận chính trị hoặc bằng cao cấp lý luận chính trị - hành chính hoặc có giấy xác nhận trình…
- *Ngữ cảnh lấy về:* `14/2022/TT-NHNN#105819|14/2022/TT-NHNN#105820|12/2019/TT-NHNN#75424|14/2022/TT-NHNN#105843|12/2019/TT-NHNN#75446`

## Kém nhất – nhóm `covered`

**Q1440** (ROUGE-L 0.102, văn bản tham chiếu `14/2022/TT-NHNN`): Những chức danh nào được xếp vào nhóm công chức ngân hàng theo quy định hiện hành?

- *Tham chiếu:* Căn cứ theo Điều 2 Thông tư 14/2022/TT-NHNN, công chức ngân hàng gồm các chức danh dưới đây:
- Kiểm soát viên cao cấp ngân hàng, Mã số: 07.044
- Kiểm soát viên chính ngân hàng, Mã số: 07.045
- Kiểm soát viên ngân hàng, Mã số: 07.046
- Thủ kho, thủ quỹ ngân hàng, Mã số: 07.048
- Nhân viên Tiền tệ - Kho quỹ, Mã số: 07.047…
- *Dự đoán:* Điều 1
Nay quy định việc phân cấp tạm thời thẩm quyền ký quyết định nâng bậc, xếp bậc lương công chức viên chức Ngân hàng như sau :
1.1. Uỷ quyền Vụ trưởng Vụ tổ chức, cán bộ và đào tạo ký quyết định nâng bậc, xếp bậc lương đối với chức danh công chức, viên chức từ ngạch chuyên viên có mã số 01.003 và tương đương trở xuống thuộc biên chế Ngân hàng Nhà nước bao gồm công chức, viên chức thuộc Vụ, Cụ…
- *Ngữ cảnh lấy về:* `155/QĐ-NH9#111643|112/QĐ-NH9#54055|12/2019/TT-NHNN#75415|112/QĐ-NH9#54056|170/2016/TT-BQP#129694`

**Q1261** (ROUGE-L 0.107, văn bản tham chiếu `07/VBHN-VPQH`): Văn bản Pháp lệnh về ngoại hối hiện hành là văn bản nào và những nghị định, thông tư hướng dẫn liên quan (đã cập nhật đến năm 2025) gồm những văn bản nào?

- *Tham chiếu:* Pháp lệnh ngoại hối mới nhất là Pháp lệnh ngoại hối 2005 được sửa đổi bởi Pháp lệnh sửa đổi Pháp lệnh ngoại hối năm 2013. Văn bản hợp nhất Pháp lệnh ngoại hối mới nhất là Văn bản hợp nhất 07/VBHN-VPQH năm 2013 hợp nhất Pháp lệnh Ngoại hối.

Dưới đây là các văn bản hướng dẫn Pháp lệnh Ngoại hối:

(1) Nghị định
- Nghị định 16/2014/NĐ-CP về quản lý cán cân thanh toán quốc tế của Việt Nam
- Nghị định …
- *Dự đoán:* 1.2.1. Tuyên truyền, phổ biến Nghị định số 39/2015/NĐ-CP, Thông tư liên tịch số 07/2016/TTLT-BYT-BTC-BLĐTBXH
a) Mục đích, yêu cầu:
Bảo đảm phổ biến kịp thời, đầy đủ nội dung của các văn bản pháp luật tới đối tượng được hỗ trợ quy định tại Thông tư số 07/2016/TTLT-BYT-BTC-BLĐTBXH và viên chức dân số làm việc trong các đơn vị sự nghiệp dân số, y tế công lập theo quy định tại Thông tư số 08/2016/TTLT…
- *Ngữ cảnh lấy về:* `1937/QĐ-BYT#154275|1176/QĐ-UBND#57862|1176/QĐ-UBND#57911|1176/QĐ-UBND#58035|06/2008/TT-BTP#21925`

**Q35** (ROUGE-L 0.112, văn bản tham chiếu `6150/TB-BLĐTBXH`): Chi tiết lịch nghỉ Tết Nguyên đán 2025 của Agribank được quy định thế nào và ngân hàng có hoạt động giao dịch nào vẫn thực hiện được trong thời gian nghỉ?

- *Tham chiếu:* Theo Thông báo 6150/TB-BLĐTBXH năm 2024, lịch nghỉ Tết Nguyên đán 2025 chi tiết như sau:
- Đối với cán bộ, công chức, viên chức và người lao động của các cơ quan hành chính, sự nghiệp, tổ chức chính trị, tổ chức chính trị - xã hội được nghỉ 09 ngày từ thứ Bảy ngày 25/1 (26 tháng Chạp năm Giáp Thìn) đến hết Chủ nhật ngày 2/2 (mùng 5 tháng Giêng năm Ất Tỵ). Đợt nghỉ này bao gồm 05 ngày nghỉ tết Âm l…
- *Dự đoán:* những hình thức động viên, chăm lo khác. Có hình thức động viên đoàn viên công đoàn, người lao động trực Tết thực hiện tốt nhiệm vụ, đảm bảo an toàn.
- Công đoàn cơ sở tham gia với lãnh đạo đơn vị, doanh nghiệp xây dựng phương án chi trả tiền lương, tiền thưởng và các khoản phúc lợi khác doanh nghiệp sẽ thực hiện trong dịp tết Nguyên đán; sớm công khai thời gian trả thưởng và lịch nghỉ Tết cho ngư…
- *Ngữ cảnh lấy về:* `94/KH-LĐLĐ#376964|15/2017/QĐ-UBND#116390|84/KH-TLĐ#365336|48/KH-LĐLĐ#302800|146/KH-TLĐ#100747`

## Tốt nhất – nhóm `not_covered`

**Q1881** (ROUGE-L 0.589, văn bản tham chiếu `115/2015/NĐ-CP`): Theo quy định hiện hành, vào thời điểm nào phải lấy tỷ giá ngoại tệ để chuyển đổi tiền lương tính đóng BHXH bắt buộc khi hợp đồng lao động ghi lương bằng ngoại tệ?

- *Tham chiếu:* Theo Điều 26 Nghị định 115/2015/NĐ-CP có quy định về chuyển đổi tiền lương bằng ngoại tệ sang đồng Việt Nam để đóng bảo hiểm xã hội như sau:

Điều 26. Quy định chuyển đổi tiền lương bằng ngoại tệ sang đồng Việt Nam để đóng bảo hiểm xã hội
Người lao động có tiền lương ghi trong hợp đồng lao động bằng ngoại tệ thì việc đóng bảo hiểm xã hội và ghi sổ bảo hiểm xã hội được thực hiện như sau:
1. Tiền lư…
- *Dự đoán:* có tiền lương, tiền công ghi trong hợp đồng lao động bằng ngoại tệ thì việc đóng bảo hiểm xã hội và ghi sổ bảo hiểm xã hội được thực hiện như sau:
a) Tiền lương, tiền công tháng đóng bảo hiểm xã hội được tính bằng đồng Việt Nam trên cơ sở tiền lương, tiền công bằng ngoại tệ được chuyển đổi bằng đồng Việt Nam theo tỷ giá giao dịch bình quân trên thị trường ngoại tệ liên ngân hàng do Ngân hàng Nhà n…
- *Ngữ cảnh lấy về:* `03/2007/TT-BLĐTBXH#10803|902/QĐ-BHXH#371635|1438/HD-BHXH#97910|17/2008/TT-BLĐTBXH#137684|119-HĐBT#60434`

**Q531** (ROUGE-L 0.282, văn bản tham chiếu `60/2024/TT-NHNN`): Thông tư số 60/2024/TT-NHNN về dịch vụ ngân quỹ cho tổ chức tín dụng và chi nhánh ngân hàng nước ngoài đã được ban hành chưa và các đối tượng áp dụng gồm những ai?

- *Tham chiếu:* Ngày 31/12/2024, Thống đốc Ngân hàng Nhà nước Việt Nam ban hành Thông tư 60/2024/TT-NHNN quy định về dịch vụ ngân quỹ cho tổ chức tín dụng, chi nhánh ngân hàng nước ngoài. Căn cứ theo Điều 2 Thông tư 60/2024/TT-NHNN quy định đối tượng áp dụng như sau: - Ngân hàng thương mại, chi nhánh ngân hàng nước ngoài, ngân hàng hợp tác xã thực hiện cung ứng dịch vụ ngân quỹ cho tổ chức tín dụng, chi nhánh ngâ…
- *Dự đoán:* quan đến việc cấp giấy phép, tổ chức và hoạt động của tổ chức tín dụng, chi nhánh ngân hàng nước ngoài, có hiệu lực kể từ ngày 26 tháng 8 năm 2019.
[5] Điểm này được bổ sung theo quy định tại Khoản 4 Điều 2 của Thông tư số 13/2019/TT-NHNN sửa đổi, bổ sung một số điều của các Thông tư có liên quan đến việc cấp giấy phép, tổ chức và hoạt động của tổ chức tín dụng, chi nhánh ngân hàng nước ngoài, có …
- *Ngữ cảnh lấy về:* `20/VBHN-NHNN#172521|20/VBHN-NHNN#172522|20/VBHN-NHNN#172523|13/2020/TT-NHNN#92227|13/2020/TT-NHNN#92228`

**Q715** (ROUGE-L 0.270, văn bản tham chiếu `Không trích xuất được`): Cơ quan nào có thẩm quyền cấp giấy phép thành lập và hoạt động cho tổ chức tín dụng?

- *Tham chiếu:* Căn cứ theo khoản 15 Điều 4 Luật Các tổ chức tín dụng 2024 quy định như sau:
Điều 4. Giải thích từ ngữ
Trong Luật này, các từ ngữ dưới đây được hiểu như sau:[...]15. Giấy phép bao gồm Giấy phép thành lập và hoạt động của tổ chức tín dụng, Giấy phép thành lập chi nhánh ngân hàng nước ngoài, Giấy phép thành lập văn phòng đại diện nước ngoài do Ngân hàng Nhà nước cấp. Văn bản của Ngân hàng Nhà nước v…
- *Dự đoán:* a) Thay đổi chức năng, phạm vi hoạt động của tổ chức, cơ sở giáo dục nghề nghiệp nước ngoài;
b) Thay đổi trụ sở của tổ chức, cơ sở giáo dục nghề nghiệp nước ngoài từ quốc gia này sang quốc gia khác;
c) Bị mất hoặc rách nát giấy phép thành lập văn phòng đại diện.
3. Trong thời hạn 10 ngày làm việc, kể từ ngày có sự thay đổi hoặc bị mất, rách nát giấy phép thành lập văn phòng đại diện hoặc 30 ngày t…
- *Ngữ cảnh lấy về:* `15/2019/NĐ-CP#116685|20/VBHN-NHNN#172524|20/VBHN-NHNN#172522|20/VBHN-NHNN#172523|2022/VBHN-BLĐTBXH#164238`

## Kém nhất – nhóm `not_covered`

**Q1854** (ROUGE-L 0.056, văn bản tham chiếu `Không trích xuất được`): Khái niệm “công cụ chuyển nhượng” được hiểu như thế nào theo pháp luật hiện hành?

- *Tham chiếu:* Theo quy định tại khoản 1 Điều 4 Luật Các công cụ chuyển nhượng 2005 quy định về công cụ chuyển nhượng như sau:Điều 4. Giải thích từ ngữTrong Luật này, các từ ngữ sau đây được hiểu như sau:1. Công cụ chuyển nhượng là giấy tờ có giá ghi nhận lệnh thanh toán hoặc cam kết thanh toán không điều kiện một số tiền xác định vào một thời điểm nhất định....Như vậy, công cụ chuyển nhượng là giấy tờ có giá gh…
- *Dự đoán:* 1.4. Xây dựng tiêu chuẩn
1. 5. Áp dụng tiêu chuẩn
2. Đo lường
2.1. Khái niệm về đo lường học
2.2. Đơn vị đo
2.3. Chuẩn đo lường
3. Chất lượng
3.1. Khái niệm về chất lượng
3.2. Quản lý chất lượng
3.3. Hệ thống quản lý chất lượng
3.4. Quá trình xây dựng và áp dụng ISO 9000 vào CQ/TC/DN
3.5. Hệ thống quản lý chất lượng theo tiêu chuẩn ISO 9001: 2008
3.6. Các hệ thống quản lý chất lượng khác
3.7. Các …
- *Ngữ cảnh lấy về:* `2476/QĐ-BKHCN#202571|12/VBHN-BTTTT#77429|28/2007/CT-UBND#226421|2367/QĐ-BNV#192832|17/2021/TT-BTTTT#139246`

**Q1693** (ROUGE-L 0.065, văn bản tham chiếu `Không trích xuất được`): Theo Luật Căn cước 2023, ở độ tuổi nào phải thu thập thông tin sinh trắc học khi đăng ký làm thẻ căn cước và trường hợp trẻ em thì thủ tục thực hiện ra sao?

- *Tham chiếu:* Căn cứ khoản 2 Điều 23 Luật Căn cước 2023 quy định về thủ tục làm thẻ căn cước như sau:
Điều 23. Trình tự, thủ tục cấp thẻ căn cước...1. Trình tự, thủ tục cấp thẻ căn cước cho người từ đủ 14 tuổi trở lên được thực hiện như sau:...b) Người tiếp nhận thu nhận thông tin nhân dạng và thông tin sinh trắc học gồm ảnh khuôn mặt, vân tay, mống mắt của người cần cấp thẻ căn cước;...2. Người dưới 14 tuổi ho…
- *Dự đoán:* 1. Tên người sử dụng lao động:
2. Mã số thuế/đăng ký kinh doanh:
3. Địa chỉ:
4. Tài khoản của người sử dụng lao động:
II. DANH SÁCH NGƯỜI LAO ĐỘNG NGỪNG VIỆC
TT
Họ và tên
Phòng, ban, phân xưởng làm việc
Loại hợp đồng lao động
Số sổ bảo hiểm
Thời gian ngừng việc (từ ngày tháng năm đến ngày tháng năm)
Số tiền hỗ trợ
Số CMT/thẻ căn cước công dân
Ghi chú
…
Cộng
(Số tiền hỗ trợ bằng chữ: ………………………………….…
- *Ngữ cảnh lấy về:* `1968/QĐ-UBND-HC#156697|1397/QĐ-UBND#89766|3109/QĐ-UBND#241274|1934/QĐ-UBND#153897|3003/QĐ-UBND#235325`

**Q2698** (ROUGE-L 0.088, văn bản tham chiếu `Không trích xuất được`): Trong Luật Các tổ chức tín dụng 2024 có quy định gì mới về khái niệm và xử lý khi xảy ra rút tiền hàng loạt tại tổ chức tín dụng (so với luật trước đây)?

- *Tham chiếu:* Theo khoản 31 Điều 4 Luật Các tổ chức tín dụng 2024 quy định về rút tiền hàng loạt như sau:
Giải thích từ ngữ Trong Luật này, các từ ngữ dưới đây được hiểu như sau:... 
31. Rút tiền hàng loạt là việc tổ chức tín dụng bị nhiều người gửi tiền cùng rút tiền dẫn đến tổ chức tín dụng có nguy cơ mất khả năng chi trả hoặc mất khả năng chi trả theo quy định của Thống đốc Ngân hàng Nhà nước.

Ngoài ra, Luậ…
- *Dự đoán:* 4. Bố cục chương trình, kế hoạch công tác
5. Bố cục lịch công tác hàng tuần của cơ quan, tổ chức
CHUYÊN ĐỀ 14
KỸ NĂNG THU NHẬP VÀ XỬ LÝ THÔNG TIN TRONG QUẢN LÝ HÀNH CHÍNH NHÀ NƯỚC
(8 tiết trong đó giảng 4 tiết, thảo luận 4 tiết)
I. THU NHẬP VÀ PHÂN TÍCH THÔNG TIN TRONG QUẢN LÝ HÀNH CHÍNH NHÀ NƯỚC
1. Khái niệm thông tin
2. Phân loại thông tin trong quản lý nhà nước
3. Vai trò và đặc điểm của thông …
- *Ngữ cảnh lấy về:* `07/2006/QĐ-BNV#25138|20/2019/TT-BLĐTBXH#171209|2270/QĐ-BNV#184732|06/CT-TTg#24047|20/VBHN-NHNN#172463`
