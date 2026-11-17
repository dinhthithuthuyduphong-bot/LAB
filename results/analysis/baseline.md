# Phân tích lỗi: `baseline`

Số câu: 200

## Thống kê theo nhóm

| group       |   n |   ROUGE_L |   pred_words |   cites_unretrieved |   abstains |   starts_can_cu |
|:------------|----:|----------:|-------------:|--------------------:|-----------:|----------------:|
| covered     |  51 |     0.13  |      2317.28 |               0.039 |          1 |               0 |
| not_covered | 149 |     0.084 |      2386.79 |               0.107 |          1 |               0 |


- `cites_unretrieved`: tỷ lệ câu trả lời nhắc một số hiệu văn bản **không xuất hiện ở đâu** trong ngữ cảnh lấy về (dấu hiệu bịa).
- `abstains`: tỷ lệ câu trả lời nói không tìm thấy thông tin.

## Tốt nhất – nhóm `covered`

**Q31** (ROUGE-L 0.337, văn bản tham chiếu `6150/TB-BLĐTBXH`): Ngân hàng LPBank nghỉ lễ 30/4 và 1/5 năm 2025 từ ngày nào và khi nào hoạt động giao dịch trở lại? Văn bản nào hướng dẫn lịch này và các lưu ý liên quan?

- *Tham chiếu:* Căn cứ theo Thông báo 6150/TB-BLĐTBXH năm 2024 hướng dẫn lịch nghỉ lễ 30 4 năm 2025 như sau: Thực hiện ý kiến chỉ đạo của Thủ tướng Phạm Minh Chính tại Công văn số 8726/VPCP-KGVX ngày 26 tháng 11 năm 2024 của Văn phòng Chính phủ về việc nghỉ tết Âm lịch và một số dịp nghỉ lễ trong năm 2025, Bộ Lao động - Thương binh và Xã hội thông báo để các cơ quan hành chính, sự nghiệp, tổ chức chính trị, tổ c…
- *Dự đoán:* 
Bạn là một trợ lý thông minh. Trả lời câu hỏi dựa trên ngữ cảnh sau.
Nếu không đủ thông tin, hãy nói rõ điều đó, không được tự bịa đặt.

Ngữ cảnh:
lđtbxh ngày 03/12/2024 của bộ lao động thương binh và xã hội; đảm bảo thời gian nghỉ tết âm lịch liền 05 ngày liên tục và nghỉ lễ quốc khánh năm 2025 liền 02 ngày liên tục.  - thông báo phương án nghỉ tết âm lịch và nghỉ lễ quốc khánh năm 2025 cho ngườ…
- *Ngữ cảnh lấy về:* `1202/TB-UBND#30241|6150/TB-BLĐTBXH#151750|1202/TB-UBND#30242|5034/TB-LĐTBXH#140808|4875/TB-BLĐTBXH#138440`

**Q43** (ROUGE-L 0.328, văn bản tham chiếu `6150/TB-BLĐTBXH`): Ngân hàng TMCP Sài Gòn (SCB) nghỉ lễ 30/4 và 01/5 năm 2025 như thế nào theo quy định của cơ quan nhà nước?

- *Tham chiếu:* Lịch nghỉ lễ 30 4 1 5 năm 2025 ngân hàng SCB?Căn cứ theo Thông báo 6150/TB-BLĐTBXH năm 2024 hướng dẫn lịch nghỉ lễ 30 4 năm 2025 như sau:Thực hiện ý kiến chỉ đạo của Thủ tướng Phạm Minh Chính tại Công văn số 8726/VPCP-KGVX ngày 26 tháng 11 năm 2024 của Văn phòng Chính phủ về việc nghỉ tết Âm lịch và một số dịp nghỉ lễ trong năm 2025, Bộ Lao động - Thương binh và Xã hội thông báo để các cơ quan h…
- *Dự đoán:* 
Bạn là một trợ lý thông minh. Trả lời câu hỏi dựa trên ngữ cảnh sau.
Nếu không đủ thông tin, hãy nói rõ điều đó, không được tự bịa đặt.

Ngữ cảnh:
bộ lao động -  thương binh và xã hội   -------  cộng hòa xã hội  chủ nghĩa việt nam   độc lập - tự do - hạnh phúc    ---------------  số:  6150/tb-blđtbxh  hà nội, ngày 03  tháng 12 năm 2024      thông báo  về việc nghỉ tết âm lịch, nghỉ lễ quốc khánh,…
- *Ngữ cảnh lấy về:* `6150/TB-BLĐTBXH#151750|1202/TB-UBND#30240|1202/TB-UBND#30241|6150/TB-BLĐTBXH#151753|1570/TB-BLĐTBXH#51649`

**Q1640** (ROUGE-L 0.281, văn bản tham chiếu `5015/TB-LĐTBXH`): Ngân hàng sẽ nghỉ lễ Quốc khánh 2/9 năm 2024 vào những ngày nào theo quy định hiện hành?

- *Tham chiếu:* Căn cứ Mục 5 Thông báo 5015/TB-LĐTBXH năm 2023 về nghỉ tết Âm lịch và nghỉ lễ Quốc khánh năm 2024 đối với cán bộ, công chức, viên chức và người lao động:5. Đối với người lao động không thuộc đối tượng quy định tại khoản 1 Thông báo này, người sử dụng lao động quyết định lựa chọn phương án nghỉ tết Âm lịch và nghỉ lễ Quốc khánh năm 2024 như sau:- Đối với dịp nghỉ tết Âm lịch: lựa chọn 01 ngày cuối …
- *Dự đoán:* 
Bạn là một trợ lý thông minh. Trả lời câu hỏi dựa trên ngữ cảnh sau.
Nếu không đủ thông tin, hãy nói rõ điều đó, không được tự bịa đặt.

Ngữ cảnh:
lđtbxh ngày 03/12/2024 của bộ lao động thương binh và xã hội; đảm bảo thời gian nghỉ tết âm lịch liền 05 ngày liên tục và nghỉ lễ quốc khánh năm 2025 liền 02 ngày liên tục.  - thông báo phương án nghỉ tết âm lịch và nghỉ lễ quốc khánh năm 2025 cho ngườ…
- *Ngữ cảnh lấy về:* `1202/TB-UBND#30241|5015/TB-LĐTBXH#140724|1202/TB-UBND#30242|5015/TB-LĐTBXH#140722|6150/TB-BLĐTBXH#151753`

## Kém nhất – nhóm `covered`

**Q1440** (ROUGE-L 0.035, văn bản tham chiếu `14/2022/TT-NHNN`): Những chức danh nào được xếp vào nhóm công chức ngân hàng theo quy định hiện hành?

- *Tham chiếu:* Căn cứ theo Điều 2 Thông tư 14/2022/TT-NHNN, công chức ngân hàng gồm các chức danh dưới đây:
- Kiểm soát viên cao cấp ngân hàng, Mã số: 07.044
- Kiểm soát viên chính ngân hàng, Mã số: 07.045
- Kiểm soát viên ngân hàng, Mã số: 07.046
- Thủ kho, thủ quỹ ngân hàng, Mã số: 07.048
- Nhân viên Tiền tệ - Kho quỹ, Mã số: 07.047…
- *Dự đoán:* 
Bạn là một trợ lý thông minh. Trả lời câu hỏi dựa trên ngữ cảnh sau.
Nếu không đủ thông tin, hãy nói rõ điều đó, không được tự bịa đặt.

Ngữ cảnh:
định tại điều 4 thông tư này thực hiện theo quy định tại điểm a khoản 2 mục ii thông tư số 02/2007/tt-bnv ngày 25 tháng 5 năm 2007 của bộ nội vụ hướng dẫn xếp lương khi nâng ngạch, chuyển ngạch, chuyển loại công chức, viên chức.  điều 6. tổ chức thực h…
- *Ngữ cảnh lấy về:* `03/2009/TTLT-BNV-BKH&ĐT#5027|17/2019/TT-BLĐTBXH#63711|12/2019/TT-NHNN#34737|36/2017/QĐ-UBND#121395|207/2017/TT-BQP#77055`

**Q2648** (ROUGE-L 0.047, văn bản tham chiếu `14/2022/TT-NHNN`): Theo quy định hiện hành, yêu cầu năng lực chuyên môn và nghiệp vụ cụ thể dành cho ngạch Nhân viên Tiền tệ - Kho quỹ gồm những nội dung nào?

- *Tham chiếu:* Tiêu chuẩn về năng lực chuyên môn, nghiệp vụ của ngạch Nhân viên Tiền tệ - Kho quỹ gồm những gì?Căn cứ quy định khoản 3 Điều 8 Thông tư 14/2022/TT-NHNN quy định về ngạch Nhân viên Tiền tệ - Kho quỹ như sau:Theo đó tiêu chuẩn về năng lực chuyên môn, nghiệp vụ của ngạch Nhân viên Tiền tệ - Kho quỹ gồm có:- Nắm vững chế độ, chính sách về quản lý tiền mặt và quản lý kho, quỹ của Ngân hàng Nhà nước;- N…
- *Dự đoán:* 
Bạn là một trợ lý thông minh. Trả lời câu hỏi dựa trên ngữ cảnh sau.
Nếu không đủ thông tin, hãy nói rõ điều đó, không được tự bịa đặt.

Ngữ cảnh:
trình đào tạo.  + định mức nguyên, nhiên vật liệu cho bảo trì, bảo dưỡng định kỳ thiết bị.  + khối lượng (số lượng) vật tư cần thiết, phải có ban đầu để phục vụ cho đào tạo đáp ứng yêu cầu của một kỹ năng.  4. định mức cơ sở vật chất:  - định mức cơ sở…
- *Ngữ cảnh lấy về:* `24/2024/QĐ-UBND#94063|24/2024/QĐ-UBND#94128|14/2022/QĐ-UBND#48320|488/QĐ-UBND#138701|477/QĐ-UBND#137126`

**Q967** (ROUGE-L 0.048, văn bản tham chiếu `07/2024/TT-BNV`): Hiện nay, với mức lương cơ sở đang áp dụng, tiền lương thực lĩnh của kiểm soát viên ngân hàng theo các bậc hệ số được tính ra sao và có các con số cụ thể nào?

- *Tham chiếu:* Căn cứ theo điểm a khoản 1 Điều 3 Thông tư 07/2024/TT-BNV, mức lương kiểm soát viên ngân hàng được tính theo công thức sau:
Tiền lương = Mức lương cơ sở x Hệ số lương

Căn cứ theo khoản 2 Điều 3 Nghị định 73/2024/NĐ-CP thì hiện nay đang áp dụng mức lương cơ sở là 2.340.000 đồng/tháng.

Do đó, mức lương kiểm soát viên ngân hàng hiện nay sẽ như sau (áp dụng cho công chức loại A1):
Hệ số lương -> Mức…
- *Dự đoán:* 
Bạn là một trợ lý thông minh. Trả lời câu hỏi dựa trên ngữ cảnh sau.
Nếu không đủ thông tin, hãy nói rõ điều đó, không được tự bịa đặt.

Ngữ cảnh:
quy định tại điều 1 thông tư này được tính theo mức lương cơ sở 1.490.000 đồng/tháng từ ngày 01 tháng 7 năm 2019.  3. thông tư này thay thế thông tư số 06/2018/tt-bnv ngày 31 tháng 5 năm 2018 của bộ nội vụ hướng dẫn thực hiện mức lương cơ sở đối với cá…
- *Ngữ cảnh lấy về:* `04/2019/TT-BNV#7541|02/2017/TT-BNV#3011|2092/VBHN-BLĐTBXH#77431|06/2018/TT-BNV#10617|145/2020/NĐ-CP#45797`

## Tốt nhất – nhóm `not_covered`

**Q1881** (ROUGE-L 0.171, văn bản tham chiếu `115/2015/NĐ-CP`): Theo quy định hiện hành, vào thời điểm nào phải lấy tỷ giá ngoại tệ để chuyển đổi tiền lương tính đóng BHXH bắt buộc khi hợp đồng lao động ghi lương bằng ngoại tệ?

- *Tham chiếu:* Theo Điều 26 Nghị định 115/2015/NĐ-CP có quy định về chuyển đổi tiền lương bằng ngoại tệ sang đồng Việt Nam để đóng bảo hiểm xã hội như sau:

Điều 26. Quy định chuyển đổi tiền lương bằng ngoại tệ sang đồng Việt Nam để đóng bảo hiểm xã hội
Người lao động có tiền lương ghi trong hợp đồng lao động bằng ngoại tệ thì việc đóng bảo hiểm xã hội và ghi sổ bảo hiểm xã hội được thực hiện như sau:
1. Tiền lư…
- *Dự đoán:* 
Bạn là một trợ lý thông minh. Trả lời câu hỏi dựa trên ngữ cảnh sau.
Nếu không đủ thông tin, hãy nói rõ điều đó, không được tự bịa đặt.

Ngữ cảnh:
b thông tư này để tính hưởng bảo hiểm xã hội.  7. đối với người lao động có tiền lương, tiền công ghi trong hợp đồng lao động bằng ngoại tệ thì việc đóng bảo hiểm xã hội và ghi sổ bảo hiểm xã hội được thực hiện như sau:  a) tiền lương, tiền công tháng …
- *Ngữ cảnh lấy về:* `03/2007/TT-BLĐTBXH#4888|05-LB/TC/LĐTBXH#8278|959/QĐ-BHXH#173540|107/2003/TTLT-BTC-BLĐTBXH#20688|114/2002/NĐ-CP#25553`

**Q2047** (ROUGE-L 0.153, văn bản tham chiếu `32/2015/TT-NHNN`): Kế toán trưởng của một quỹ tín dụng nhân dân có được nhận khoản vay dưới hình thức vay không có bảo đảm từ chính quỹ tín dụng đó hay không?

- *Tham chiếu:* Quỹ tín dụng nhân dân là gì? Căn cứ tại khoản 6 Điều 4 Luật Các tổ chức tín dụng 2010 có quy định về quỹ tín dụng nhân dân như sau:
Giải thích từ ngữ
Trong Luật này, các từ ngữ dưới đây được hiểu như sau:...6. Quỹ tín dụng nhân dân là tổ chức tín dụng do các pháp nhân, cá nhân và hộ gia đình tự nguyện thành lập dưới hình thức hợp tác xã để thực hiện một số hoạt động ngân hàng theo quy định của Luậ…
- *Dự đoán:* 
Bạn là một trợ lý thông minh. Trả lời câu hỏi dựa trên ngữ cảnh sau.
Nếu không đủ thông tin, hãy nói rõ điều đó, không được tự bịa đặt.

Ngữ cảnh:
nhật bản theo hợp đồng thì thực hiện cho vay trực tiếp tại ngân hàng chính sách xã hội nơi cho vay.  - riêng trường hợp cho người lao động vay ký quỹ đi làm việc có thời hạn tại hàn quốc theo chương trình eps thực hiện quy trình, thủ tục cho vay theo q…
- *Ngữ cảnh lấy về:* `23/2018/QĐ-UBND#90593|8055/NHCS-TDSV#164952|365/2004/QĐ-NHNN#120817|4658/HD-NHCS#135580|151/2014/TT-BTC#49646`

**Q2175** (ROUGE-L 0.151, văn bản tham chiếu `17/2015/TT-NHNN`): Theo quy định hiện hành, cơ quan nào chịu trách nhiệm tiếp nhận hồ sơ và thực hiện việc sửa đổi, cập nhật thông tin ngân hàng trong hệ thống của Ngân hàng Nhà nước?

- *Tham chiếu:* Căn cứ theo khoản 6 Điều 11 Thông tư 17/2015/TT-NHNN được sửa đổi bởi khoản 7 Điều 1 Thông tư 18/2023/TT-NHNN có hiệu lực từ ngày 01/07/2024 quy định như sau:
Điều 11. Trình tự, thủ tục điều chỉnh thông tin ngân hàng...2. Đối với các tổ chức tín dụng (trừ quỹ tín dụng nhân dân), chi nhánh ngân hàng nước ngoài, khi có thay đổi thông tin ngân hàng quy định tại Khoản 1 Điều 8 Thông tư này, trong thời…
- *Dự đoán:* 
Bạn là một trợ lý thông minh. Trả lời câu hỏi dựa trên ngữ cảnh sau.
Nếu không đủ thông tin, hãy nói rõ điều đó, không được tự bịa đặt.

Ngữ cảnh:
tiếp nhận, rà soát thông báo của tổ chức tín dụng, chi nhánh ngân hàng nước ngoài quy định tại khoản 2 điều 11 thông tư này. trường hợp phát hiện sai sót, cơ quan thanh tra, giám sát ngân hàng yêu cầu tổ chức tín dụng, chi nhánh ngân hàng nước ngoài xử…
- *Ngữ cảnh lấy về:* `20/VBHN-NHNN#79057|10/2021/TT-NHNN#22965|03/2022/QĐ-UBND#5641|6187/QĐ-UBND#151919|20/VBHN-NHNN#79055`

## Kém nhất – nhóm `not_covered`

**Q1906** (ROUGE-L 0.030, văn bản tham chiếu `29/2024/TT-NHNN`): Theo Thông tư 29/2024/TT-NHNN, quỹ tín dụng nhân dân phải dùng mẫu sổ vốn góp nào cho thành viên?

- *Tham chiếu:* Mẫu sổ vốn góp của thành viên quỹ tín dụng nhân dân được quy định tại Phụ lục số 04 ban hành kèm theo Thông tư 29/2024/TT-NHNN, mẫu có dạng như sau:
Tải Mẫu sổ vốn góp của thành viên quỹ tín dụng nhân dân theo Thông tư 29
Tại đây
Mẫu sổ vốn góp của thành viên quỹ tín dụng nhân dân theo Thông tư 29? (Hình từ Internet)…
- *Dự đoán:* 
Bạn là một trợ lý thông minh. Trả lời câu hỏi dựa trên ngữ cảnh sau.
Nếu không đủ thông tin, hãy nói rõ điều đó, không được tự bịa đặt.

Ngữ cảnh:
mại được phép xem xét, quyết định và tự chịu trách nhiệm về quyết định của mình khi cho vay đến 20 triệu đồng không phải áp dụng biện pháp bảo đảm bằng tài sản trong trường hợp cho vay thông qua hộ gia đình của người lao động ở nông thôn, mà hộ gia đìn…
- *Ngữ cảnh lấy về:* `365/2004/QĐ-NHNN#120817|61/2015/NĐ-CP#152126|373/2003/QĐ-NHNN#122021|109/KH-UBND#21749|04/CTr-UBND#8002`

**Q1093** (ROUGE-L 0.038, văn bản tham chiếu `09/2023/TT-NHNN`): Pháp luật có yêu cầu phải đợi cho giao dịch hoàn tất mới được gửi báo cáo về giao dịch đáng ngờ hay báo cáo có thể được gửi trước khi giao dịch kết thúc?

- *Tham chiếu:* Căn cứ theo khoản 2 Điều 7 Thông tư 09/2023/TT-NHNN quy định về chế độ báo cáo giao dịch đáng ngờ như sau: Điều 7. Chế độ báo cáo giao dịch đáng ngờ [...] 2. Việc báo cáo giao dịch đáng ngờ theo quy định tại Điều 26 Luật Phòng, chống rửa tiền không phụ thuộc vào lượng tiền giao dịch của khách hàng, giao dịch đó đã hoàn thành hay chưa. [...] Như vậy, việc báo cáo giao dịch đáng ngờ của các đối tượn…
- *Dự đoán:* 
Bạn là một trợ lý thông minh. Trả lời câu hỏi dựa trên ngữ cảnh sau.
Nếu không đủ thông tin, hãy nói rõ điều đó, không được tự bịa đặt.

Ngữ cảnh:
tiết lộ, kể cả sau khi không còn công tác nữa, mọi bí mật thương mại hoặc các quy trình bí mật hoặc thông tin cá nhân của thuyền viên có thể có được trong khi họ làm nhiệm vụ.  12. các thanh tra viên phải gửi báo cáo mỗi đợt kiểm tra cho cơ quan có thẩ…
- *Ngữ cảnh lấy về:* `Khongso#176279|23/2021/NĐ-CP#90709|3040/QĐ-UBND#108585|2007/VBHN-BLĐTBXH#74713|1511/QĐ-LĐTBXH#49513`

**Q1854** (ROUGE-L 0.039, văn bản tham chiếu `Không trích xuất được`): Khái niệm “công cụ chuyển nhượng” được hiểu như thế nào theo pháp luật hiện hành?

- *Tham chiếu:* Theo quy định tại khoản 1 Điều 4 Luật Các công cụ chuyển nhượng 2005 quy định về công cụ chuyển nhượng như sau:Điều 4. Giải thích từ ngữTrong Luật này, các từ ngữ sau đây được hiểu như sau:1. Công cụ chuyển nhượng là giấy tờ có giá ghi nhận lệnh thanh toán hoặc cam kết thanh toán không điều kiện một số tiền xác định vào một thời điểm nhất định....Như vậy, công cụ chuyển nhượng là giấy tờ có giá gh…
- *Dự đoán:* 
Bạn là một trợ lý thông minh. Trả lời câu hỏi dựa trên ngữ cảnh sau.
Nếu không đủ thông tin, hãy nói rõ điều đó, không được tự bịa đặt.

Ngữ cảnh:
đây được chuyển sang ngạch nhân viên bảo quản kho dự trữ - mã số ngạch 19.224 theo quy định tại mục iv của quyết định số 136/2005/qđ-bnv ngày 19 tháng 12 năm 2005 của bộ trưởng bộ nội vụ ban hành tiêu chuẩn, nghiệp vụ các ngạch công chức ngành dự trữ q…
- *Ngữ cảnh lấy về:* `84/2006/TTLT-BTC-BNV#167603|1026/QĐ-UBND#17792|10/2004/TT-BNV#21895|33/2007/QĐ-UBND#115849|370-HĐBT#121652`
