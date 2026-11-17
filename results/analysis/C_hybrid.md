# Phân tích lỗi: `C_hybrid`

Số câu: 200

## Thống kê theo nhóm

| group       |   n |   ROUGE_L |   pred_words |   cites_unretrieved |   abstains |   starts_can_cu |
|:------------|----:|----------:|-------------:|--------------------:|-----------:|----------------:|
| covered     |  51 |     0.303 |      246.941 |               0.059 |      0.059 |           1     |
| not_covered | 149 |     0.204 |      233.611 |               0.168 |      0.121 |           0.953 |


- `cites_unretrieved`: tỷ lệ câu trả lời nhắc một số hiệu văn bản **không xuất hiện ở đâu** trong ngữ cảnh lấy về (dấu hiệu bịa).
- `abstains`: tỷ lệ câu trả lời nói không tìm thấy thông tin.

## Tốt nhất – nhóm `covered`

**Q2169** (ROUGE-L 0.599, văn bản tham chiếu `14/2022/TT-NHNN`): Những yêu cầu về năng lực chuyên môn và nghiệp vụ mà một kiểm soát viên chính ngân hàng phải đạt được bao gồm những gì?

- *Tham chiếu:* Căn cứ theo khoản 3 Điều 5 Thông tư 14/2022/TT-NHNN, kiểm soát viên chính ngân hàng phải đáp ứng đủ các tiêu chuẩn về năng lực chuyên môn, nghiệp vụ dưới đây:

- Nắm vững đường lối, chủ trương của Đảng, pháp luật của Nhà nước, chính sách của Ngành về các hoạt động của ngân hàng.
- Nắm vững nghiệp vụ kiểm soát, kiểm toán của Ngân hàng Nhà nước; hướng dẫn và điều hành có hiệu quả hoạt động của kiểm …
- *Dự đoán:* Căn cứ tại Điều 5 Thông tư 14/2022/TT-NHNN quy định mã số, tiêu chuẩn chuyên môn, nghiệp vụ và xếp lương đối với các ngạch công chức chuyên ngành Ngân hàng quy định:

- Một kiểm soát viên chính ngân hàng phải nắm vững đường lối, chủ trương của Đảng, pháp luật của Nhà nước, chính sách của Ngành về các hoạt động của ngân hàng (Điều 5, điểm a).

- Nắm vững nghiệp vụ kiểm soát, kiểm toán của Ngân hàng…
- *Ngữ cảnh lấy về:* `14/2022/TT-NHNN#105824|14/2022/TT-NHNN#105826|12/2019/TT-NHNN#75427|14/2022/TT-NHNN#105825|12/2019/TT-NHNN#75429`

**Q2614** (ROUGE-L 0.591, văn bản tham chiếu `14/2022/TT-NHNN`): Các nguyên tắc khi xếp lương cho công chức thuộc các ngạch chuyên ngành Ngân hàng được quy định ra sao theo Thông tư 14/2022/TT-NHNN?

- *Tham chiếu:* Nguyên tắc xếp lương các ngạch công chức chuyên ngành Ngân hàng được quy định như thế nào?Căn cứ quy định Điều 9 Thông tư 14/2022/TT-NHNN quy định về nguyên tắc xếp lương các ngạch công chức chuyên ngành Ngân hàng như sau:Nguyên tắc xếp lương các ngạch công chức chuyên ngành Ngân hàng1. Việc bổ nhiệm và xếp lương vào các ngạch công chức chuyên ngành Ngân hàng quy định tại Thông tư này phải căn cứ …
- *Dự đoán:* Căn cứ tại Điều 9 Mục I Chương I Thông tư 14/2022/TT-NHNN quy định:

- Việc xếp lương cho công chức thuộc các ngạch chuyên ngành Ngân hàng phải căn cứ vào vị trí việc làm, chức trách, nhiệm vụ và nghiệp vụ chuyên môn đảm nhận của công chức (căn cứ tại Điều 9 Mục 1 Khoản 1 Thông tư 14/2022/TT-NHNN).
- Khi chuyển xếp từ ngạch công chức hiện giữ sang ngạch công chức chuyên ngành Ngân hàng theo Thông …
- *Ngữ cảnh lấy về:* `14/2022/TT-NHNN#105839|14/2022/TT-NHNN#105813|14/2022/TT-NHNN#105841`

**Q1442** (ROUGE-L 0.590, văn bản tham chiếu `14/2022/TT-NHNN`): Những yêu cầu chung về phẩm chất đạo đức và chính trị mà một công chức làm việc trong hệ thống ngân hàng phải đáp ứng là gì?

- *Tham chiếu:* Căn cứ theo quy định tại Điều 3 Thông tư 14/2022/TT-NHNN, tiêu chuẩn chung về phẩm chất của công chức ngân hàng đó là:
- Có bản lĩnh chính trị vững vàng, kiên định với chủ nghĩa Mác - Lênin, tư tưởng Hồ Chí Minh; nắm vững chủ trương, đường lối, quy định của Đảng, chính sách, pháp luật của Nhà nước; trung thành với Tổ quốc; bảo vệ lợi ích của Nhà nước, của nhân dân.
- Thực hiện đầy đủ nghĩa vụ của …
- *Dự đoán:* Căn cứ tại Điều 3, Khoản 1, Điểm a và Điểm b Điều 3, Khoản 1, Điểm c Điều 6, Điều 3, Khoản 1, Điểm a Điều 6 và Điều 3, Khoản 1, Điểm a Điều 6 Thông tư 14/2022/TT-NHNN quy định mã số, tiêu chuẩn chuyên môn, nghiệp vụ và xếp lương đối với các ngạch công chức chuyên ngành Ngân hàng do Thống đốc Ngân hàng Nhà nước Việt Nam ban hành, cũng như tại Điều 6, Khoản 2, Điểm b Điều 6 Quyết định 956/2003/QĐ-NH…
- *Ngữ cảnh lấy về:* `14/2022/TT-NHNN#105812|956/2003/QĐ-NHNN#377662|363/QĐ-NH9#262136|14/2022/TT-NHNN#105811|54/2016/NQ-HĐND#316474`

## Kém nhất – nhóm `covered`

**Q38** (ROUGE-L 0.003, văn bản tham chiếu `6150/TB-BLĐTBXH`): Ngân hàng BIDV nghỉ Tết Nguyên đán 2025 theo lịch nào, chi tiết các ngày nghỉ và hoạt động kênh dịch vụ trong thời gian đó là ra sao?

- *Tham chiếu:* Lịch nghỉ Tết ngân hàng BIDV 2025 mới nhất, chi tiết?Theo Thông báo 6150/TB-BLĐTBXH năm 2024, lịch nghỉ Tết Nguyên đán 2025 chi tiết như sau:- Đối với cán bộ, công chức, viên chức và người lao động của các cơ quan hành chính, sự nghiệp, tổ chức chính trị, tổ chức chính trị - xã hội được nghỉ 09 ngày từ thứ Bảy ngày 25/1 (26 tháng Chạp năm Giáp Thìn) đến hết Chủ nhật ngày 2/2 (mùng 5 tháng Giêng nă…
- *Dự đoán:* Căn cứ tại Điều 1, Khoản 1, Điểm a, Điểm b, Điểm c, Điểm d, Điểm e, Điểm f, Điểm g, Điểm h, Điểm i, Điểm j, Điểm k, Điểm l, Điểm m, Điểm n, Điểm o, Điểm p, Điểm q, Điểm r, Điểm s, Điểm t, Điểm u, Điểm v, Điểm w, Điểm x, Điểm y, Điểm z, Điểm aa, Điểm bb, Điểm cc, Điểm dd, Điểm ee, Điểm ff, Điểm gg, Điểm hh, Điểm ii, Điểm jj, Điểm kk, Điểm ll, Điểm mm, Điểm nn, Điểm oo, Điểm pp, Điểm qq, Điểm rr, Đi…
- *Ngữ cảnh lấy về:* `94/KH-LĐLĐ#376964|5446/HD-NHCS#315654|82/2014/NQ-HĐND#362433|5446/HD-NHCS#315674|15/2017/QĐ-UBND#116390`

**Q2612** (ROUGE-L 0.012, văn bản tham chiếu `5015/TB-LĐTBXH`): Ngân hàng có thể tiếp tục làm việc tới ngày nào trước khi nghỉ Tết Âm lịch năm 2024 theo quy định hiện hành và quy chế riêng của từng ngân hàng?

- *Tham chiếu:* Ngân hàng làm việc tới ngày mấy tết âm lịch 2024?Căn cứ tại Thông báo 5015/TB-LĐTBXH năm 2023 về việc nghỉ tết Âm lịch của cán bộ, công chức, viên chức và người lao động như sau:1. Cán bộ, công chức, viên chức và người lao động của các cơ quan hành chính, sự nghiệp, tổ chức chính trị, tổ chức chính trị - xã hội (sau đây gọi tắt là công chức, viên chức) được nghỉ tết Âm lịch năm 2024 từ thứ Năm ngà…
- *Dự đoán:* Căn cứ tại Điều 111, Điều 112, Điều 113, Điều 114, Điều 115, Điều 116, Điều 117, Điều 118, Điều 119, Điều 120, Điều 121, Điều 122, Điều 123, Điều 124, Điều 125, Điều 126, Điều 127, Điều 128, Điều 129, Điều 130, Điều 131, Điều 132, Điều 133, Điều 134, Điều 135, Điều 136, Điều 137, Điều 138, Điều 139, Điều 140, Điều 141, Điều 142, Điều 143, Điều 144, Điều 145, Điều 146, Điều 147, Điều 148, Điều 149,…
- *Ngữ cảnh lấy về:* `5015/TB-LĐTBXH#305997|5015/TB-LĐTBXH#305999|1202/TB-UBND#65797|6150/TB-BLĐTBXH#330482|1202/TB-UBND#65796`

**Q2167** (ROUGE-L 0.029, văn bản tham chiếu `14/2022/TT-NHNN`): Để được công nhận là kiểm soát viên chính trong ngành ngân hàng, ứng viên cần có bằng đại học chuyên ngành nào?

- *Tham chiếu:* Căn cứ theo điểm a khoản 4 Điều 5 Thông tư 14/2022/TT-NHNN quy định như sau:

Điều 5. Ngạch Kiểm soát viên chính ngân hàng...
4. Tiêu chuẩn về trình độ đào tạo, bồi dưỡn
ga) Có bằng tốt nghiệp đại học trở lên với ngành hoặc chuyên ngành: kinh tế, tài chính, ngân hàng, kế toán, kiểm toán, công nghệ thông tin, xây dựng, luật;
b) Có chứng chỉ bồi dưỡng kiến thức, kỹ năng quản lý nhà nước đối với công…
- *Dự đoán:* Căn cứ tại Điều 5, khoản e, điểm a, Điều 5, khoản d, Điều 6, khoản d, Điều 5, khoản e, Điều 5, khoản e, Điều 5, khoản e, Điều 5, khoản e, Điều 5, khoản e, Điều 5, khoản e, Điều 5, khoản e, Điều 5, khoản e, Điều 5, khoản e, Điều 5, khoản e, Điều 5, khoản e, Điều 5, khoản e, Điều 5, khoản e, Điều 5, khoản e, Điều 5, khoản e, Điều 5, khoản e, Điều 5, khoản e, Điều 5, khoản e, Điều 5, khoản e, Điều 5,…
- *Ngữ cảnh lấy về:* `12/2019/TT-NHNN#75429|14/2022/TT-NHNN#105826|12/2019/TT-NHNN#75430|12/2019/TT-NHNN#75435|14/2022/TT-NHNN#105824`

## Tốt nhất – nhóm `not_covered`

**Q701** (ROUGE-L 0.669, văn bản tham chiếu `571/2002/QĐ-NHNN`): Theo quy định hiện hành, Agribank được phép huy động vốn bằng những phương thức, công cụ nào?

- *Tham chiếu:* Theo khoản 1 Điều 5 Điều lệ về tổ chức và hoạt động của Ngân hàng Nông nghiệp và phát triển nông thôn Việt Nam ban hành kèm theo Quyết định 571/2002/QĐ-NHNN quy định như sau:

Điều 5.
1. Ngân hàng Nông nghiệp huy động vốn dưới các hình thức sau:
a) Nhận tiền gửi của các tổ chức, cá nhân và tổ chức tín dụng khác dưới các hình thức tiền gửi không kỳ hạn, tiền gửi có kỳ hạn và các loại tiền gửi khác.…
- *Dự đoán:* Căn cứ tại Điều 5, Chương 2, Mục 1 Điều lệ mẫu về tổ chức và hoạt động của Ngân hàng thương mại nhà nước số 122/2001/QĐ-NHNN quy định:

Ngân hàng thương mại nhà nước huy động vốn dưới các hình thức sau:

1. Nhận tiền gửi của các tổ chức, cá nhân và các tổ chức tín dụng khác dưới các hình thức tiền gửi không kỳ hạn, tiền gửi có kỳ hạn và các loại tiền gửi khác.
2. Phát hành chứng chỉ tiền gửi, trái…
- *Ngữ cảnh lấy về:* `4468/QĐ-BNN-KTHT#288587|122/2001/QĐ-NHNN#68067|4468/QĐ-BNN-KTHT#288584|47/2009/QĐ-UBND#298285|2375/QĐ-BNV#194105`

**Q1057** (ROUGE-L 0.423, văn bản tham chiếu `26/2024/TT-NHNN`): Khi nào thì hợp đồng cho thuê tài chính giữa công ty cho thuê tài chính và bên thuê tài chính được coi là có hiệu lực?

- *Tham chiếu:* Căn cứ theo khoản 2 Điều 18 Thông tư 26/2024/TT-NHNN quy định về hợp đồng cho thuê tài chính như sau:
Điều 18. Hợp đồng cho thuê tài chính
[...]2. Hợp đồng cho thuê tài chính có hiệu lực từ ngày được các bên thỏa thuận trong hợp đồng cho thuê tài chính.
3. Việc đăng ký hợp đồng cho thuê tài chính thực hiện theo quy định của pháp luật.

Theo đó, hợp đồng cho thuê tài chính của công ty cho thuê tài …
- *Dự đoán:* Căn cứ tại Điều 1.1 Thông tư 15/2001/TT-BTCCBCP quy định: "Hợp đồng thuê khoán tài sản: được ký kết giữa bên giao tài sản và bên thuê tài sản theo quy định của Bộ luật Dân sự". 

Căn cứ tại Điều 1.1 Thông tư 15/2001/TT-BTCCBCP, hợp đồng cho thuê tài chính giữa công ty cho thuê tài chính và bên thuê tài chính được coi là có hiệu lực kể từ ngày ký kết. Theo quy định tại Điều 1.1 Thông tư 15/2001/TT-…
- *Ngữ cảnh lấy về:* `03/2019/TT-BNV#12108|2401/HD-NHCS#198911|15/2001/TT-BTCCBCP#114326|5446/HD-NHCS#315670|29/2005/TT-BLĐTBXH#232782`

**Q1881** (ROUGE-L 0.415, văn bản tham chiếu `115/2015/NĐ-CP`): Theo quy định hiện hành, vào thời điểm nào phải lấy tỷ giá ngoại tệ để chuyển đổi tiền lương tính đóng BHXH bắt buộc khi hợp đồng lao động ghi lương bằng ngoại tệ?

- *Tham chiếu:* Theo Điều 26 Nghị định 115/2015/NĐ-CP có quy định về chuyển đổi tiền lương bằng ngoại tệ sang đồng Việt Nam để đóng bảo hiểm xã hội như sau:

Điều 26. Quy định chuyển đổi tiền lương bằng ngoại tệ sang đồng Việt Nam để đóng bảo hiểm xã hội
Người lao động có tiền lương ghi trong hợp đồng lao động bằng ngoại tệ thì việc đóng bảo hiểm xã hội và ghi sổ bảo hiểm xã hội được thực hiện như sau:
1. Tiền lư…
- *Dự đoán:* Căn cứ tại Điều 2.3 và Điều 2.4 của Quyết định 902/QĐ-BHXH năm 2007 quy định về quản lý thu bảo hiểm xã hội, bảo hiểm y tế bắt buộc quy định: "Tiền lương, tiền công tháng để đóng BHXH của người lao động thuộc các hộ kinh doanh cá thể, tổ hợp tác và cá nhân là mức tiền lương, tiền công do người sử dụng lao động quy định nhưng phải đăng ký với cơ quan quản lý nhà nước về lao động theo phân cấp quản …
- *Ngữ cảnh lấy về:* `902/QĐ-BHXH#371635|03/2007/TT-BLĐTBXH#10803|1438/HD-BHXH#97910|10-LĐTBXH/TT#36644|902/QĐ-BHXH#371636`

## Kém nhất – nhóm `not_covered`

**Q507** (ROUGE-L 0.007, văn bản tham chiếu `25/2013/TT-NHNN`): Những loại tiền nào được xác định là không đạt tiêu chuẩn lưu thông theo quy định hiện hành?

- *Tham chiếu:* Tiêu chuẩn tiền không đủ tiêu chuẩn lưu thông gồm cách loại tiền nào?Theo Điều 4 Thông tư 25/2013/TT-NHNN quy định tiêu chuẩn tiền không đủ tiêu chuẩn lưu thông như sau:(1) Tiền rách nát, hư hỏng do quá trình lưu thông (nhóm nguyên nhân khách quan):- Tiền giấy bị thay đổi màu sắc, mờ nhạt hình ảnh hoa văn, chữ, số; nhàu, nát, nhòe, bẩn, cũ; rách rời hay liền mảnh được can dán lại nhưng còn nguyên …
- *Dự đoán:* Căn cứ tại Điều 9, Khoản 1, Điểm e, Điểm đ, Điểm đ Điều 8, Khoản 3, Điểm a, Điểm b, Điểm c, Điểm d, Điểm đ, Điểm e, Điểm f, Điểm g, Điểm h, Điểm i, Điểm k Điều 8, Khoản 3, Điểm a Điều 8, Khoản 3, Điểm a Điều 8, Khoản 3, Điểm a Điều 8, Khoản 3, Điểm a Điều 8, Khoản 3, Điểm a Điều 8, Khoản 3, Điểm a Điều 8, Khoản 3, Điểm a Điều 8, Khoản 3, Điểm a Điều 8, Khoản 3, Điểm a Điều 8, Khoản 3, Điểm a Điều …
- *Ngữ cảnh lấy về:* `12/2019/TT-NHNN#75444|14/2022/TT-NHNN#105838|14/2022/TT-NHNN#105837|25-CP#205436|521/QĐ-SNV#311071`

**Q1930** (ROUGE-L 0.021, văn bản tham chiếu `52/2024/NĐ-CP`): Những loại hình dịch vụ nào được xếp vào nhóm "dịch vụ thanh toán không qua tài khoản" theo quy định pháp luật?

- *Tham chiếu:* Theo quy định tại Điều 18 Nghị định 52/2024/NĐ-CP quy định về dịch vụ thanh toán không qua tài khoản thanh toán như sau:Điều 18. Dịch vụ thanh toán không qua tài khoản thanh toán của khách hàng1. Dịch vụ thanh toán không qua tài khoản thanh toán của khách hàng, bao gồm:a) Thực hiện dịch vụ thanh toán: chuyển tiền, thu hộ, chi hộ;b) Các dịch vụ thanh toán khác không qua tài khoản thực hiện theo quy…
- *Dự đoán:* Căn cứ tại Điều 3, khoản 3, Điều 4, Điều 5, Điều 6, Điều 7, Điều 8, Điều 9, Điều 10, Điều 11, Điều 12, Điều 13, Điều 14, Điều 15, Điều 16, Điều 17, Điều 18, Điều 19, Điều 20, Điều 21, Điều 22, Điều 23, Điều 24, Điều 25, Điều 26, Điều 27, Điều 28, Điều 29, Điều 30, Điều 31, Điều 32, Điều 33, Điều 34, Điều 35, Điều 36, Điều 37, Điều 38, Điều 39, Điều 40, Điều 41, Điều 42, Điều 43, Điều 44, Điều 45, …
- *Ngữ cảnh lấy về:* `20/2007/CT-TTg#169705|20/2007/CT-TTg#169706|20/2007/CT-TTg#169704|20/CT-UBND#172046|06/CT-UBND#24180`

**Q1214** (ROUGE-L 0.040, văn bản tham chiếu `Không trích xuất được`): Theo quy định hiện hành, mức lãi suất áp dụng cho các chương trình tín dụng chính sách tại Ngân hàng Chính sách xã hội hiện nay là bao nhiêu (đối với hộ nghèo, HS-SV, chương trình nước sạch, v.v.)?

- *Tham chiếu:* Căn cứ Điều 1 Quyết định 750/QĐ-TTg năm 2015 hướng dẫn về điều chỉnh giảm lãi suất cho vay đối với chương trình tín dụng chính sách tại Ngân hàng Chính sách xã hội như sau:

Điều 1. Điều chỉnh giảm lãi suất cho vay đối với một số chương trình tín dụng chính sách tại Ngân hàng Chính sách xã hội như sau:

1. Lãi suất cho vay hộ nghèo, cho vay học sinh, sinh viên, cho vay đối tượng chính sách đi lao …
- *Dự đoán:* Căn cứ tại Điều 6.1, khoản 6.1, Điểm 6.1 và Điều 6.2, khoản 6.2, Điểm 6.2, khoản 6.2, Điều 6.2, khoản 6.2, Điều 6.2, khoản 6.2, Điều 6.2, khoản 6.2, Điều 6.2, khoản 6.2, Điều 6.2, khoản 6.2, Điều 6.2, khoản 6.2, Điều 6.2, khoản 6.2, Điều 6.2, khoản 6.2, Điều 6.2, khoản 6.2, Điều 6.2, khoản 6.2, Điều 6.2, khoản 6.2, Điều 6.2, khoản 6.2, Điều 6.2, khoản 6.2, Điều 6.2, khoản 6.2, Điều 6.2, khoản 6.2,…
- *Ngữ cảnh lấy về:* `8055/NHCS-TDSV#359082|04/2010/QĐ-UBND#14997|16/2023/QĐ-TTg#127932|1321/QĐ-UBND#80852|150/KH-UBND#107717`
