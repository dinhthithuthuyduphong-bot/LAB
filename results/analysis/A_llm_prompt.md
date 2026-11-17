# Phân tích lỗi: `A_llm_prompt`

Số câu: 200

## Thống kê theo nhóm

| group       |   n |   ROUGE_L |   pred_words |   cites_unretrieved |   abstains |   starts_can_cu |
|:------------|----:|----------:|-------------:|--------------------:|-----------:|----------------:|
| covered     |  51 |     0.214 |      228.569 |               0.314 |      0.176 |           0.882 |
| not_covered | 149 |     0.195 |      200.779 |               0.349 |      0.389 |           0.664 |


- `cites_unretrieved`: tỷ lệ câu trả lời nhắc một số hiệu văn bản **không xuất hiện ở đâu** trong ngữ cảnh lấy về (dấu hiệu bịa).
- `abstains`: tỷ lệ câu trả lời nói không tìm thấy thông tin.

## Tốt nhất – nhóm `covered`

**Q1570** (ROUGE-L 0.514, văn bản tham chiếu `5015/TB-LĐTBXH`): Ngân hàng Vietcombank có lịch nghỉ lễ Quốc khánh 2/9/2024 như thế nào? Căn cứ quy định chung, Vietcombank nghỉ những ngày nào trong dịp này?

- *Tham chiếu:* Căn cứ Mục 5 Thông báo 5015/TB-LĐTBXH năm 2023 về nghỉ tết Âm lịch và nghỉ lễ Quốc khánh năm 2024 đối với cán bộ, công chức, viên chức và người lao động:5. Đối với người lao động không thuộc đối tượng quy định tại khoản 1 Thông báo này, người sử dụng lao động quyết định lựa chọn phương án nghỉ tết Âm lịch và nghỉ lễ Quốc khánh năm 2024 như sau:- Đối với dịp nghỉ tết Âm lịch: lựa chọn 01 ngày cuối …
- *Dự đoán:* Căn cứ tại Điều 112 Bộ Luật Lao động 2019 quy định: Người lao động được nghỉ bù ngày nghỉ hằng tuần nếu ngày nghỉ hằng tuần trùng với ngày nghỉ lễ, tết quy định tại khoản 1 Điều 112 Bộ Luật Lao động. 

Theo thông báo 5015/TB-LĐTBXH số 5015/TB-LĐTBXH ngày 22/11/2023 của Bộ Lao động - Thương binh và Xã hội, đối với người lao động không thuộc đối tượng quy định tại khoản 1 thông báo này, người sử dụn…
- *Ngữ cảnh lấy về:* `5015/TB-LĐTBXH#140722|5034/TB-LĐTBXH#140808|5015/TB-LĐTBXH#140724|1202/TB-UBND#30241|4875/TB-BLĐTBXH#138440`

**Q2612** (ROUGE-L 0.403, văn bản tham chiếu `5015/TB-LĐTBXH`): Ngân hàng có thể tiếp tục làm việc tới ngày nào trước khi nghỉ Tết Âm lịch năm 2024 theo quy định hiện hành và quy chế riêng của từng ngân hàng?

- *Tham chiếu:* Ngân hàng làm việc tới ngày mấy tết âm lịch 2024?Căn cứ tại Thông báo 5015/TB-LĐTBXH năm 2023 về việc nghỉ tết Âm lịch của cán bộ, công chức, viên chức và người lao động như sau:1. Cán bộ, công chức, viên chức và người lao động của các cơ quan hành chính, sự nghiệp, tổ chức chính trị, tổ chức chính trị - xã hội (sau đây gọi tắt là công chức, viên chức) được nghỉ tết Âm lịch năm 2024 từ thứ Năm ngà…
- *Dự đoán:* Căn cứ tại Điều 5 Thông báo 5015/TB-LĐTBXH năm 2023 quy định:

- Đối với người lao động không thuộc đối tượng quy định tại khoản 1 Thông báo này, người sử dụng lao động quyết định lựa chọn phương án nghỉ tết âm lịch và nghỉ lễ quốc khánh năm 2024 như sau:

+ Đối với dịp nghỉ tết âm lịch: Lựa chọn 01 ngày cuối năm quý mão và 04 ngày đầu năm giáp thìn hoặc 02 ngày cuối năm quý mão và 03 ngày đầu năm…
- *Ngữ cảnh lấy về:* `4875/TB-BLĐTBXH#138440|5034/TB-LĐTBXH#140808|5015/TB-LĐTBXH#140722|233-HĐBT#87360|309-LĐTL#109573`

**Q39** (ROUGE-L 0.368, văn bản tham chiếu `6150/TB-BLĐTBXH`): TPBank nghỉ Tết Âm lịch năm 2025 vào những ngày nào theo thông báo chính thức, và hệ thống ngân hàng có hoạt động trong thời gian đó không?

- *Tham chiếu:* Căn cứ theo Thông báo 6150/TB-BLĐTBXH năm 2024 hướng dẫn nghỉ tết Âm lịch, nghỉ lễ Quốc khánh, nghỉ lễ ngày Chiến thắng 30/4 và ngày Quốc tế lao động 01/5 năm 2025 đối với cán bộ, công chức, viên chức và người lao động như sau:- Cán bộ, công chức, viên chức và người lao động của các cơ quan hành chính, sự nghiệp, tổ chức chính trị, tổ chức chính trị - xã hội được nghỉ Tết Âm lịch 2025 từ thứ Bảy n…
- *Dự đoán:* Căn cứ tại Điều 5 Thông báo 4875/TB-BLĐTBXH năm 2020 về nghỉ tết âm lịch và quốc khánh trong năm 2021 đối với cán bộ, công chức, viên chức và người lao động do Bộ Lao động - Thương binh và Xã hội ban hành quy định:

- Đối với người lao động không thuộc đối tượng quy định tại khoản 1 Thông báo này, người sử dụng lao động quyết định lựa chọn phương án nghỉ tết âm lịch và nghỉ lễ quốc khánh năm 2021 …
- *Ngữ cảnh lấy về:* `4875/TB-BLĐTBXH#138440|5034/TB-LĐTBXH#140808|5015/TB-LĐTBXH#140722|1202/TB-UBND#30241|233-HĐBT#87360`

## Kém nhất – nhóm `covered`

**Q37** (ROUGE-L 0.023, văn bản tham chiếu `6150/TB-BLĐTBXH`): Ngân hàng MB (MBBank Quân đội) nghỉ lễ dịp 30/4 - 1/5/2025 như thế nào theo quy định hiện hành?

- *Tham chiếu:* Căn cứ theo Thông báo 6150/TB-BLĐTBXH năm 2024 hướng dẫn lịch nghỉ lễ 30 4 1 5 năm 2025 như sau:
Thực hiện ý kiến chỉ đạo của Thủ tướng Phạm Minh Chính tại Công văn số 8726/VPCP-KGVX ngày 26 tháng 11 năm 2024 của Văn phòng Chính phủ về việc nghỉ tết Âm lịch và một số dịp nghỉ lễ trong năm 2025, Bộ Lao động - Thương binh và Xã hội thông báo để các cơ quan hành chính, sự nghiệp, tổ chức chính trị, t…
- *Dự đoán:* Căn cứ tại Điều 31, Khoản 1, Điểm a, Điều 32, Khoản 1, Điểm a, Điều 33, Khoản 1, Điểm a, Điều 34, Khoản 1, Điểm a, Điều 35, Khoản 1, Điểm a, Điều 36, Khoản 1, Điểm a, Điều 37, Khoản 1, Điểm a, Điều 38, Khoản 1, Điểm a, Điều 39, Khoản 1, Điểm a, Điều 40, Khoản 1, Điểm a, Điều 41, Khoản 1, Điểm a, Điều 42, Khoản 1, Điểm a, Điều 43, Khoản 1, Điểm a, Điều 44, Khoản 1, Điểm a, Điều 45, Khoản 1, Điểm a,…
- *Ngữ cảnh lấy về:* `6150/TB-BLĐTBXH#151750|1570/TB-BLĐTBXH#51649|1570/TB-BLĐTBXH#51651|342/TB-UBND#116935|1202/TB-UBND#30240`

**Q2647** (ROUGE-L 0.068, văn bản tham chiếu `5015/TB-LĐTBXH`): Ngân hàng sẽ nghỉ Tết Âm lịch năm 2024 vào những ngày nào theo quy định và lịch tham khảo của các ngân hàng thương mại?

- *Tham chiếu:* Lịch nghỉ Tết âm lịch của ngân hàng 2024?Căn cứ tại Thông báo 5015/TB-LĐTBXH năm 2023 về việc nghỉ tết Âm lịch của cán bộ, công chức, viên chức và người lao động như sau:1. Cán bộ, công chức, viên chức và người lao động của các cơ quan hành chính, sự nghiệp, tổ chức chính trị, tổ chức chính trị - xã hội (sau đây gọi tắt là công chức, viên chức) được nghỉ tết Âm lịch năm 2024 từ thứ Năm ngày 08/02/…
- *Dự đoán:* Căn cứ tại Điều 112 Bộ Luật Lao động 2012 quy định về quyền và nghĩa vụ của người lao động trong việc nghỉ phép, nghỉ lễ, Tết, nghỉ bù, nghỉ hưởng lương, nghỉ dưỡng sức, nghỉ sinh, nghỉ thai sản, nghỉ bệnh, nghỉ hưu, nghỉ phép riêng, nghỉ phép thăm thân, nghỉ phép chữa bệnh, nghỉ phép quân sự, nghỉ phép công tác, nghỉ phép đi học, nghỉ phép đi khám chữa bệnh, nghỉ phép đi làm việc ở nước ngoài, ng…
- *Ngữ cảnh lấy về:* `5015/TB-LĐTBXH#140722|4875/TB-BLĐTBXH#138440|5034/TB-LĐTBXH#140808|1202/TB-UBND#30241|61/TTr-LĐTBXH#152302`

**Q34** (ROUGE-L 0.072, văn bản tham chiếu `6150/TB-BLĐTBXH`): Ngân hàng HDBank sẽ nghỉ Tết Âm lịch 2025 vào những ngày nào theo thông báo chính thức?

- *Tham chiếu:* Lịch nghỉ tết ngân hàng HDBank 2025?Căn cứ theo Thông báo 6150/TB-BLĐTBXH năm 2024 hướng dẫn nghỉ Tết Âm lịch 2025 đối với cán bộ, công chức, viên chức và người lao động như sau:- Cán bộ, công chức, viên chức và người lao động của các cơ quan hành chính, sự nghiệp, tổ chức chính trị, tổ chức chính trị - xã hội được nghỉ Tết Âm lịch 2025 từ ngày 25/01/2025 đến hết Chủ nhật ngày 02/02/2025 dương lịc…
- *Dự đoán:* Căn cứ tại Điều 112 Bộ Luật Lao động 2012 quy định về thời gian nghỉ lễ, Tết, ngày nghỉ hằng năm, ngày nghỉ bù, ngày nghỉ riêng, ngày nghỉ phép, ngày nghỉ hưởng lương, ngày nghỉ không hưởng lương, ngày nghỉ không làm việc, ngày nghỉ không hưởng lương nhưng vẫn làm việc, ngày nghỉ không làm việc nhưng vẫn hưởng lương, ngày nghỉ không làm việc cũng không hưởng lương, ngày nghỉ không làm việc cũng kh…
- *Ngữ cảnh lấy về:* `5015/TB-LĐTBXH#140722|5034/TB-LĐTBXH#140808|4875/TB-BLĐTBXH#138440|1202/TB-UBND#30241|20/2023/TT-BCT#78651`

## Tốt nhất – nhóm `not_covered`

**Q1057** (ROUGE-L 0.473, văn bản tham chiếu `26/2024/TT-NHNN`): Khi nào thì hợp đồng cho thuê tài chính giữa công ty cho thuê tài chính và bên thuê tài chính được coi là có hiệu lực?

- *Tham chiếu:* Căn cứ theo khoản 2 Điều 18 Thông tư 26/2024/TT-NHNN quy định về hợp đồng cho thuê tài chính như sau:
Điều 18. Hợp đồng cho thuê tài chính
[...]2. Hợp đồng cho thuê tài chính có hiệu lực từ ngày được các bên thỏa thuận trong hợp đồng cho thuê tài chính.
3. Việc đăng ký hợp đồng cho thuê tài chính thực hiện theo quy định của pháp luật.

Theo đó, hợp đồng cho thuê tài chính của công ty cho thuê tài …
- *Dự đoán:* Căn cứ tại Điều 111 Bộ Luật Dân sự 2005 quy định:

Hợp đồng cho thuê tài chính giữa công ty cho thuê tài chính và bên thuê tài chính có hiệu lực kể từ khi được công chứng hoặc chứng thực. 

Vì vậy, căn cứ vào quy định trên, hợp đồng cho thuê tài chính giữa công ty cho thuê tài chính và bên thuê tài chính chỉ có hiệu lực kể từ khi được công chứng hoặc chứng thực. Không có quy định cụ thể về thời đi…
- *Ngữ cảnh lấy về:* `15/2001/TT-BTCCBCP#52451|12/2022/NĐ-CP#34992|28/2020/NĐ-CP#104880|55/2013/NĐ-CP#146402|4441/VBHN-BLĐTBXH#132352`

**Q1881** (ROUGE-L 0.457, văn bản tham chiếu `115/2015/NĐ-CP`): Theo quy định hiện hành, vào thời điểm nào phải lấy tỷ giá ngoại tệ để chuyển đổi tiền lương tính đóng BHXH bắt buộc khi hợp đồng lao động ghi lương bằng ngoại tệ?

- *Tham chiếu:* Theo Điều 26 Nghị định 115/2015/NĐ-CP có quy định về chuyển đổi tiền lương bằng ngoại tệ sang đồng Việt Nam để đóng bảo hiểm xã hội như sau:

Điều 26. Quy định chuyển đổi tiền lương bằng ngoại tệ sang đồng Việt Nam để đóng bảo hiểm xã hội
Người lao động có tiền lương ghi trong hợp đồng lao động bằng ngoại tệ thì việc đóng bảo hiểm xã hội và ghi sổ bảo hiểm xã hội được thực hiện như sau:
1. Tiền lư…
- *Dự đoán:* Căn cứ tại Điều 7, Khoản 1 Điểm b Thông tư số 03/2007/TT-BLĐTBXH quy định: "tiền lương, tiền công tháng đóng bảo hiểm xã hội được tính bằng đồng Việt Nam trên cơ sở tiền lương, tiền công bằng ngoại tệ được chuyển đổi bằng đồng Việt Nam theo tỷ giá giao dịch bình quân trên thị trường ngoại tệ liên ngân hàng do Ngân hàng Nhà nước Việt Nam công bố tại thời điểm ngày 02 tháng 01 cho 6 tháng đầu năm và…
- *Ngữ cảnh lấy về:* `03/2007/TT-BLĐTBXH#4888|05-LB/TC/LĐTBXH#8278|959/QĐ-BHXH#173540|107/2003/TTLT-BTC-BLĐTBXH#20688|114/2002/NĐ-CP#25553`

**Q430** (ROUGE-L 0.431, văn bản tham chiếu `94/2025/NĐ-CP`): Nếu cần mẫu đơn đề nghị dừng thử nghiệm có kiểm soát trong lĩnh vực ngân hàng, chỗ nào tải bản Mẫu số 07 (Phụ lục 1 kèm Nghị định 94/2025/NĐ-CP)?

- *Tham chiếu:* Tải về mẫu đơn đề nghị dừng thử nghiệm có kiểm soát trong lĩnh vực ngân hàng chi tiết ở đâu?

Căn cứ theo Mẫu số 07 Phụ lục 1 Danh mục mẫu văn bản hồ sơ, thủ tục ban hành kèm theo Nghị định 94/2025/NĐ-CP quy định như sau:

Dưới đây là Mẫu đơn đề nghị dừng thử nghiệm có kiểm soát trong lĩnh vực ngân hàng:

Tải về Mẫu đơn đề nghị dừng thử nghiệm có kiểm soát trong lĩnh vực ngân hàng:Tải về

Ghi chú:…
- *Dự đoán:* Căn cứ tại Điều 11, Nghị định số 94/2025/NĐ-CP ngày 25/11/2025 quy định:

Mẫu số 07 (Phụ lục 1) được quy định tại Điều 11 của Nghị định số 94/2025/NĐ-CP, không phải là mẫu đơn đề nghị dừng thử nghiệm có kiểm soát trong lĩnh vực ngân hàng. 

Để có mẫu đơn đề nghị dừng thử nghiệm có kiểm soát trong lĩnh vực ngân hàng, bạn nên tham khảo tại Phụ lục 1 kèm theo Nghị định số 94/2025/NĐ-CP, hoặc liên hệ …
- *Ngữ cảnh lấy về:* `186/QĐ-UBND#67345|1088/QĐ-UBND#21192|4174/QĐ-UBND#128249|1968/QĐ-UBND-HC#71842|2857/QĐ-UBND#103432`

## Kém nhất – nhóm `not_covered`

**Q1229** (ROUGE-L 0.027, văn bản tham chiếu `Không trích xuất được`): Trong những tình huống cụ thể nào bắt buộc các đối tượng phải gửi báo cáo về giao dịch đáng ngờ tới Ngân hàng Nhà nước theo Luật Phòng, chống rửa tiền?

- *Tham chiếu:* Căn cứ theo khoản 1 Điều 26 Luật Phòng, chống rửa tiền 2022 quy định về báo cáo giao dịch đáng ngờ như sau:Điều 26. Báo cáo giao dịch đáng ngờ1. Đối tượng báo cáo có trách nhiệm báo cáo giao dịch đáng ngờ cho Ngân hàng Nhà nước Việt Nam trong trường hợp sau đây:a) Khi biết giao dịch được thực hiện theo yêu cầu của bị can, bị cáo, người bị kết án và có cơ sở hợp lý để nghi ngờ tài sản trong giao dị…
- *Dự đoán:* Căn cứ tại Điều 18, Khoản 2, Điều 19, Điều 20, Điểm a, b, c, d, đ, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, Điều 31, Điều 32, Điều 33, Điều 34, Điều 35, Điều 36, Điều 37, Điều 38, Điều 39, Điều 40, Điều 41, Điều 42, Điều 43, Điều 44, Điều 45, Điều 46, Điều 47, Điều 48, Điều 49, Điều 50, Điều 51, Điều 52, Điều 53, Điều 54, Điều 55, Điều 56, Điều 57, Điều 58, Điều 59, Điều 6…
- *Ngữ cảnh lấy về:* `03/2024/QĐ-UBND#5791|03/2013/TT-BLĐTBXH#5231|900/QĐ-BHTG#170549|21-TT/LB#79154|13-TT/LB#35984`

**Q692** (ROUGE-L 0.028, văn bản tham chiếu `Không trích xuất được`): Nếu thực hiện giao dịch, nhận hoặc sử dụng đồng Pi để thanh toán tại Việt Nam thì có thể bị truy cứu trách nhiệm hình sự hay bị phạt tù không, và theo quy định nào?

- *Tham chiếu:* Thanh toán bằng đồng Pi có bị đi tù? Căn cứ tại điểm h khoản 1 Điều 206 Bộ luật Hình sự 2015 được sửa đổi bởi khoản 48 Điều 1 Luật sửa đổi Bộ luật Hình sự 2017, quy định tội vi phạm quy định trong hoạt động của các tổ chức tín dụng, chi nhánh ngân hàng nước ngoài:
Điều 206. Tội vi phạm quy định trong hoạt động của các tổ chức tín dụng, chi nhánh ngân hàng nước ngoài
1. Người nào thực hiện một tron…
- *Dự đoán:* Căn cứ tại Điều 211, Điều 212, Điều 213, Điều 214, Điều 215, Điều 216, Điều 217, Điều 218, Điều 219, Điều 220, Điều 221, Điều 222, Điều 223, Điều 224, Điều 225, Điều 226, Điều 227, Điều 228, Điều 229, Điều 230, Điều 231, Điều 232, Điều 233, Điều 234, Điều 235, Điều 236, Điều 237, Điều 238, Điều 239, Điều 240, Điều 241, Điều 242, Điều 243, Điều 244, Điều 245, Điều 246, Điều 247, Điều 248, Điều 249,…
- *Ngữ cảnh lấy về:* `12/2022/NĐ-CP#35045|12/2022/NĐ-CP#35054|95/2013/NĐ-CP#173698|4756/VBHN-BLĐTBXH#136974|02/2023/QĐ-UBND#3434`

**Q1688** (ROUGE-L 0.029, văn bản tham chiếu `52/2024/NĐ-CP`): Khi làm hồ sơ mở tài khoản thanh toán tại Ngân hàng Nhà nước, tổ chức phải nộp những giấy tờ nào để chứng minh việc thành lập và hoạt động hợp pháp?

- *Tham chiếu:* Căn cứ theo quy định tại khoản 2 Điều 14 Nghị định 52/2024/NĐ-CP, quy định hồ sơ mở tài khoản thanh toán tại Ngân hàng Nhà nước như sau:
Điều 14. Hồ sơ và trình tự thủ tục mở, đóng tài khoản thanh toán tại Ngân hàng Nhà nước của tổ chức tín dụng, chi nhánh ngân hàng nước ngoài, Kho bạc Nhà nước
[...]2. Hồ sơ mở tài khoản thanh toán tại Ngân hàng Nhà nước, bao gồm:
a) Đơn đề nghị mở tài khoản thanh…
- *Dự đoán:* Căn cứ tại Điều 11, Khoản 1, Điểm a, Điểm b, Điểm c, Điểm d Điều 12, Điều 13, Điều 14, Điều 15, Điều 16, Điều 17, Điều 18, Điều 19, Điều 20, Điều 21, Điều 22, Điều 23, Điều 24, Điều 25, Điều 26, Điều 27, Điều 28, Điều 29, Điều 30, Điều 31, Điều 32, Điều 33, Điều 34, Điều 35, Điều 36, Điều 37, Điều 38, Điều 39, Điều 40, Điều 41, Điều 42, Điều 43, Điều 44, Điều 45, Điều 46, Điều 47, Điều 48, Điều 49…
- *Ngữ cảnh lấy về:* `2286/QĐ-UBND#85147|57/2007/QĐ-UBND#148603|2401/HD-NHCS#91260|61/2015/NĐ-CP#152126|23/2021/NĐ-CP#90702`
