# Phân tích lỗi: `extractive_bm25_baseline_k5`

Số câu: 200

## Thống kê theo nhóm

| group       |   n |   ROUGE_L |   pred_words |   cites_unretrieved |   abstains |   starts_can_cu |
|:------------|----:|----------:|-------------:|--------------------:|-----------:|----------------:|
| covered     |  51 |     0.283 |      418.608 |                   0 |      0     |               0 |
| not_covered | 149 |     0.143 |      418.248 |                   0 |      0.007 |               0 |


- `cites_unretrieved`: tỷ lệ câu trả lời nhắc một số hiệu văn bản **không xuất hiện ở đâu** trong ngữ cảnh lấy về (dấu hiệu bịa).
- `abstains`: tỷ lệ câu trả lời nói không tìm thấy thông tin.

## Tốt nhất – nhóm `covered`

**Q966** (ROUGE-L 0.584, văn bản tham chiếu `14/2022/TT-NHNN`): Ngạch kiểm soát viên trong ngành Ngân hàng được xếp vào loại bảng lương công chức nào theo quy định hiện hành?

- *Tham chiếu:* Căn cứ theo điểm c khoản 1 Điều 10 Thông tư 14/2022/TT-NHNN quy định như sau:
Điều 10. Xếp lương các ngạch công chức chuyên ngành Ngân hàng
1. Các ngạch công chức chuyên ngành Ngân hàng quy định tại Thông tư này áp dụng Bảng 2 (Bảng lương chuyên môn, nghiệp vụ đối với cán bộ, công chức trong các cơ quan nhà nước) ban hành kèm theo Nghị định số 204/2004/NĐ-CP ngày 14 tháng 12 năm 2004 của Chính phủ…
- *Dự đoán:* tiền, phân biệt tiền thật, tiền giả; quy định, quy trình nghiệp vụ về kiểm, đếm, đóng gói, giao nhận tiền, thủ tục thu chi tiền mặt và bảo quản tiền mặt;  d) hướng dẫn được khách hàng chấp hành đúng các thủ tục về lĩnh tiền, nộp tiền ở ngân hàng;  đ) sử dụng thông thạo máy kiểm đếm tiền và các công cụ hỗ trợ khác.  4. tiêu chuẩn về trình độ đào tạo, bồi dưỡng  có bằng tốt nghiệp trung cấp trở lên …
- *Ngữ cảnh lấy về:* `14/2022/TT-NHNN#48561|14/2022/TT-NHNN#48562|12/2019/TT-NHNN#34737|14/2022/TT-NHNN#48564|12/2019/TT-NHNN#34739`

**Q1708** (ROUGE-L 0.578, văn bản tham chiếu `14/2022/TT-NHNN`): Khi mức lương cơ sở được điều chỉnh lên 2,34 triệu đồng/tháng, mức lương theo bảng áp dụng cho ngạch Kiểm soát viên cao cấp (A3.1) sẽ được tính và có các bậc tiền lương cụ thể như thế nào?

- *Tham chiếu:* Căn cứ theo khoản 1 Điều 10 Thông tư 14/2022/TT-NHNN quy định như sau:

Điều 10. Xếp lương các ngạch công chức chuyên ngành Ngân hàng
1. Các ngạch công chức chuyên ngành Ngân hàng quy định tại Thông tư này áp dụng Bảng 2 (Bảng lương chuyên môn, nghiệp vụ đối với cán bộ, công chức trong các cơ quan nhà nước) ban hành kèm theo Nghị định số 204/2004/NĐ-CP ngày 14 tháng 12 năm 2004 của Chính phủ về ch…
- *Dự đoán:* tiền, phân biệt tiền thật, tiền giả; quy định, quy trình nghiệp vụ về kiểm, đếm, đóng gói, giao nhận tiền, thủ tục thu chi tiền mặt và bảo quản tiền mặt;  d) hướng dẫn được khách hàng chấp hành đúng các thủ tục về lĩnh tiền, nộp tiền ở ngân hàng;  đ) sử dụng thông thạo máy kiểm đếm tiền và các công cụ hỗ trợ khác.  4. tiêu chuẩn về trình độ đào tạo, bồi dưỡng  có bằng tốt nghiệp trung cấp trở lên …
- *Ngữ cảnh lấy về:* `14/2022/TT-NHNN#48561|12/2019/TT-NHNN#34737|83-KL/TW#166703|12/2006/TTLT-BTM-BNV-BTC#34051|79/2005/TT-BNV#164383`

**Q2168** (ROUGE-L 0.558, văn bản tham chiếu `14/2022/TT-NHNN`): Mức hệ số lương áp dụng cho ngạch kiểm soát viên chính trong ngành ngân hàng hiện là bao nhiêu?

- *Tham chiếu:* Căn cứ theo điểm a khoản 1 Điều 10 Thông tư 14/2022/TT-NHNN quy định như sau:

Điều 10. Xếp lương các ngạch công chức chuyên ngành Ngân hàng
1. Các ngạch công chức chuyên ngành Ngân hàng quy định tại Thông tư này áp dụng Bảng 2 (Bảng lương chuyên môn, nghiệp vụ đối với cán bộ, công chức trong các cơ quan nhà nước) ban hành kèm theo Nghị định số 204/2004/NĐ-CP ngày 14 tháng 12 năm 2004 của Chính ph…
- *Dự đoán:* tiền, phân biệt tiền thật, tiền giả; quy định, quy trình nghiệp vụ về kiểm, đếm, đóng gói, giao nhận tiền, thủ tục thu chi tiền mặt và bảo quản tiền mặt;  d) hướng dẫn được khách hàng chấp hành đúng các thủ tục về lĩnh tiền, nộp tiền ở ngân hàng;  đ) sử dụng thông thạo máy kiểm đếm tiền và các công cụ hỗ trợ khác.  4. tiêu chuẩn về trình độ đào tạo, bồi dưỡng  có bằng tốt nghiệp trung cấp trở lên …
- *Ngữ cảnh lấy về:* `14/2022/TT-NHNN#48561|14/2022/TT-NHNN#48562|08/2022/TT-BNNPTNT#14345|14/2022/TT-NHNN#48564|12/2019/TT-NHNN#34739`

## Kém nhất – nhóm `covered`

**Q43** (ROUGE-L 0.064, văn bản tham chiếu `6150/TB-BLĐTBXH`): Ngân hàng TMCP Sài Gòn (SCB) nghỉ lễ 30/4 và 01/5 năm 2025 như thế nào theo quy định của cơ quan nhà nước?

- *Tham chiếu:* Lịch nghỉ lễ 30 4 1 5 năm 2025 ngân hàng SCB?Căn cứ theo Thông báo 6150/TB-BLĐTBXH năm 2024 hướng dẫn lịch nghỉ lễ 30 4 năm 2025 như sau:Thực hiện ý kiến chỉ đạo của Thủ tướng Phạm Minh Chính tại Công văn số 8726/VPCP-KGVX ngày 26 tháng 11 năm 2024 của Văn phòng Chính phủ về việc nghỉ tết Âm lịch và một số dịp nghỉ lễ trong năm 2025, Bộ Lao động - Thương binh và Xã hội thông báo để các cơ quan h…
- *Dự đoán:* 10  59  cđcs trường cđ sư phạm trung ương  tp.hcm  10  60  cđcs trường cđ bách việt (nova)  10  61  cđcs trường cđ giao thông vận tải  trung ương vi  10  62  cđcs trường cđ bc công nghệ và quản  trị doanh nghiệp  10  63  cđcs trường cđ giao thông vận tải  trung ương iii  10  64  cđcs trường đh rmit việt nam  10  65  cđcs trường đh tư thục quốc tế sài  gòn  10  66  cđcs trường đh gia định  10  67  …
- *Ngữ cảnh lấy về:* `70/KH-LĐLĐ#159411|6150/TB-BLĐTBXH#151753|1570/TB-BLĐTBXH#51651|1202/TB-UBND#30242|1202/TB-UBND#30240`

**Q1261** (ROUGE-L 0.093, văn bản tham chiếu `07/VBHN-VPQH`): Văn bản Pháp lệnh về ngoại hối hiện hành là văn bản nào và những nghị định, thông tư hướng dẫn liên quan (đã cập nhật đến năm 2025) gồm những văn bản nào?

- *Tham chiếu:* Pháp lệnh ngoại hối mới nhất là Pháp lệnh ngoại hối 2005 được sửa đổi bởi Pháp lệnh sửa đổi Pháp lệnh ngoại hối năm 2013. Văn bản hợp nhất Pháp lệnh ngoại hối mới nhất là Văn bản hợp nhất 07/VBHN-VPQH năm 2013 hợp nhất Pháp lệnh Ngoại hối.

Dưới đây là các văn bản hướng dẫn Pháp lệnh Ngoại hối:

(1) Nghị định
- Nghị định 16/2014/NĐ-CP về quản lý cán cân thanh toán quốc tế của Việt Nam
- Nghị định …
- *Dự đoán:* nền văn hoá việt nam tiên tiến, đậm đà bản sắc dân tộc"  2.3. pháp luật (luật, pháp lệnh và các văn bản pháp quy) của nhà nước về chuyên ngành thí sinh dự thi (luật báo chí, luật xuất bản, các nghị định của chính phủ có liên quan đến ngành văn hoá - thông tin);   2.4. pháp lệnh cán bộ, công chức; pháp lệnh chống tham nhũng; pháp lệnh thực hành tiết kiệm, chống lãng phí và các văn bản hướng dẫn thự…
- *Ngữ cảnh lấy về:* `14/2000/QĐ-BVHTT#47446|41/1997/TTLB-BTC-BNG#128423|1936/QĐ-UBND#70728|1315/2000/TT-BQP#36757|04/CT-UB#7998`

**Q1440** (ROUGE-L 0.094, văn bản tham chiếu `14/2022/TT-NHNN`): Những chức danh nào được xếp vào nhóm công chức ngân hàng theo quy định hiện hành?

- *Tham chiếu:* Căn cứ theo Điều 2 Thông tư 14/2022/TT-NHNN, công chức ngân hàng gồm các chức danh dưới đây:
- Kiểm soát viên cao cấp ngân hàng, Mã số: 07.044
- Kiểm soát viên chính ngân hàng, Mã số: 07.045
- Kiểm soát viên ngân hàng, Mã số: 07.046
- Thủ kho, thủ quỹ ngân hàng, Mã số: 07.048
- Nhân viên Tiền tệ - Kho quỹ, Mã số: 07.047…
- *Dự đoán:* ngân  hàng nhà nước   việt nam   --------  cộng  hòa xã hội chủ nghĩa việt nam   độc lập - tự do - hạnh phúc    ---------------  số:  155/qđ-nh9  hà  nội, ngày 22 tháng 07 năm 1994     quyết định  về việc phân cấp tạm thời quyền quyết định lương công chức, viên chức ngân hàng  thống đốc ngân hàng nhà nước  - căn cứ pháp lệnh ngân hàng nhà nước ngày 23/05/1990 ;  - căn cứ nghị định 15/cp ngày 02/03…
- *Ngữ cảnh lấy về:* `155/QĐ-NH9#51203|112/QĐ-NH9#24800|12/2019/TT-NHNN#34726|12/2019/TT-NHNN#34739|170/2016/TT-BQP#59472`

## Tốt nhất – nhóm `not_covered`

**Q1881** (ROUGE-L 0.356, văn bản tham chiếu `115/2015/NĐ-CP`): Theo quy định hiện hành, vào thời điểm nào phải lấy tỷ giá ngoại tệ để chuyển đổi tiền lương tính đóng BHXH bắt buộc khi hợp đồng lao động ghi lương bằng ngoại tệ?

- *Tham chiếu:* Theo Điều 26 Nghị định 115/2015/NĐ-CP có quy định về chuyển đổi tiền lương bằng ngoại tệ sang đồng Việt Nam để đóng bảo hiểm xã hội như sau:

Điều 26. Quy định chuyển đổi tiền lương bằng ngoại tệ sang đồng Việt Nam để đóng bảo hiểm xã hội
Người lao động có tiền lương ghi trong hợp đồng lao động bằng ngoại tệ thì việc đóng bảo hiểm xã hội và ghi sổ bảo hiểm xã hội được thực hiện như sau:
1. Tiền lư…
- *Dự đoán:* thành viên, chủ tịch công ty, thành viên hội đồng quản trị, tổng giám đốc, phó tổng giám đốc, giám đốc, phó giám đốc, kế toán trưởng và kiểm soát viên là mức tiền lương do điều lệ của công ty quy định nhưng phải được đăng ký với cơ quan quản lý nhà nước về lao động tỉnh, thành phố.  2.2. tiền lương, tiền công tháng đóng bhxh, bhyt của người lao động trong hợp tác xã là mức tiền lương, tiền công đư…
- *Ngữ cảnh lấy về:* `902/QĐ-BHXH#170675|1438/HD-BHXH#44911|03/2007/TT-BLĐTBXH#4888|3636/QĐ-BHXH#120606|107/2003/TTLT-BTC-BLĐTBXH#20688`

**Q2000** (ROUGE-L 0.281, văn bản tham chiếu `49/2018/TT-NHNN`): Quy định về rút tiền trước hạn đối với khoản tiền gửi kỳ hạn quy định như thế nào, bao gồm cơ chế xác định lãi suất khi rút trước thời hạn?

- *Tham chiếu:* Việc chi trả trước hạn tiền gửi có kỳ hạn được quy định như thế nào? Căn cứ theo Điều 10 Thông tư 49/2018/TT-NHNN quy định như sau:
Điều 10. Chi trả trước hạn tiền gửi có kỳ hạn
1. Việc chi trả trước hạn tiền gửi có kỳ hạn được thực hiện theo thỏa thuận giữa tổ chức tín dụng và khách hàng tại thỏa thuận tiền gửi có kỳ hạn.
2. Lãi suất áp dụng đối với tiền gửi có kỳ hạn chi trả trước hạn phù hợp vớ…
- *Dự đoán:* sang kỳ gửi 12 tháng tiếp theo. thời gian gửi dưới 12 tháng, tiền gửi ký quỹ của bên b được áp dụng lãi suất tiền gửi không kỳ hạn do bên a công bố tại thời điểm rút tiền.  - trong thời gian 6 tháng còn lại, tiền gửi ký quỹ (bao gồm gốc và lãi nhập gốc) của bên b được chuyển sang áp dụng theo loại tiền gửi có kỳ hạn 6 tháng. lãi suất áp dụng bằng lãi suất tiền gửi có kỳ hạn 6 tháng trả lãi cuối kỳ…
- *Ngữ cảnh lấy về:* `2401/HD-NHCS#91267|17/2007/TTLT-BLĐTBXH-NHNNVN#63036|3672/NHCS-TDNN#120869|2401/HD-NHCS#91259|3672/NHCS-TDNN#120863`

**Q1114** (ROUGE-L 0.241, văn bản tham chiếu `Không trích xuất được`): Ai được xem là người đại diện hợp pháp của một tổ chức tín dụng theo Luật?

- *Tham chiếu:* Căn cứ theo khoản 1 Điều 11 Luật Các tổ chức tín dụng 2024 quy định như sau:
Điều 11. Người đại diện theo pháp luật của tổ chức tín dụng
1. Người đại diện theo pháp luật của tổ chức tín dụng được quy định tại Điều lệ của tổ chức tín dụng và phải là một trong những người sau đây:
a) Chủ tịch Hội đồng quản trị hoặc Chủ tịch Hội đồng thành viên của tổ chức tín dụng;
b) Tổng giám đốc (Giám đốc) của tổ…
- *Dự đoán:* của pháp luật.  2. văn bản của tổ chức tín dụng, chi nhánh ngân hàng nước ngoài đề nghị ngân hàng nhà nước chấp thuận danh sách dự kiến nhân sự phải do người đại diện theo pháp luật hoặc người đại diện theo ủy quyền (sau đây gọi là người đại diện hợp pháp) ký.  trường hợp văn bản đề nghị của tổ chức tín dụng, chi nhánh ngân hàng nước ngoài do người đại diện theo ủy quyền ký, hồ sơ phải có văn bản …
- *Ngữ cảnh lấy về:* `20/VBHN-NHNN#79047|20/VBHN-NHNN#79063|13/2020/TT-NHNN#42371|20/VBHN-NHNN#79059|20/VBHN-NHNN#79051`

## Kém nhất – nhóm `not_covered`

**Q1452** (ROUGE-L 0.007, văn bản tham chiếu `21/2024/TT-NHNN`): Trong thủ tục sử dụng nghiệp vụ thư tín dụng, trong trường hợp nào khách hàng phải khai báo thông tin về các cá nhân, tổ chức liên quan cho ngân hàng?

- *Tham chiếu:* Căn cứ theo Điều 14 Thông tư 21/2024/TT-NHNN quy định về hồ sơ đề nghị cấp tín dụng như sau:

Điều 14. Hồ sơ đề nghị cấp tín dụng
Khi có nhu cầu được cung cấp nghiệp vụ thư tín dụng, khách hàng phải gửi cho ngân hàng:
1. Thông tin, tài liệu, dữ liệu chứng minh đủ điều kiện cấp tín dụng theo quy định tại Điều 21, Điều 27, Điều 31 và Điều 40 Thông tư này.
2. Thông tin về người có liên quan với khách…
- *Dự đoán:* năm 20...: ……………… lao động, lý do: …………………………………….  - tháng ……… năm 20...…
- *Ngữ cảnh lấy về:* `6199/HD-NHCS#151968|2129/HD-NHCS#79955|41/2018/TT-BLĐTBXH#128860|6199/HD-NHCS#151960|5446/HD-NHCS#145101`

**Q1854** (ROUGE-L 0.050, văn bản tham chiếu `Không trích xuất được`): Khái niệm “công cụ chuyển nhượng” được hiểu như thế nào theo pháp luật hiện hành?

- *Tham chiếu:* Theo quy định tại khoản 1 Điều 4 Luật Các công cụ chuyển nhượng 2005 quy định về công cụ chuyển nhượng như sau:Điều 4. Giải thích từ ngữTrong Luật này, các từ ngữ sau đây được hiểu như sau:1. Công cụ chuyển nhượng là giấy tờ có giá ghi nhận lệnh thanh toán hoặc cam kết thanh toán không điều kiện một số tiền xác định vào một thời điểm nhất định....Như vậy, công cụ chuyển nhượng là giấy tờ có giá gh…
- *Dự đoán:* điều  hành.                    kt053  kiến thức về cách lưu  lượng truyền qua mạng (ví dụ: giao thức tcp, ip, mô hình osi,...).                    kt055  kiến thức về các khái  niệm tính toán song song và phân tán.                    kt061  kiến thức về các khái  niệm công nghệ truy cập từ xa.                    kt063  kiến thức về các khái  niệm chính trong quản lý bảo mật an toàn thông tin mạng …
- *Ngữ cảnh lấy về:* `17/2021/TT-BTTTT#63836|2476/QĐ-BKHCN#92971|1714/QĐ-UBND#59641|12/VBHN-BTTTT#35623|41/2014/TT-BCT#128726`

**Q786** (ROUGE-L 0.076, văn bản tham chiếu `52/2024/NĐ-CP`): Theo quy định pháp luật hiện hành, khái niệm “dịch vụ ví điện tử” được định nghĩa như thế nào?

- *Tham chiếu:* Căn cứ tại khoản 16 Điều 3 Nghị định 52/2024/NĐ-CP quy định về giải thích dịch vụ ví điện tử như sau:
Điều 3. Giải thích từ ngữ
Trong Nghị định này, các từ ngữ dưới đây được hiểu như sau:
[...]16. Dịch vụ ví điện tử là dịch vụ do ngân hàng, chi nhánh ngân hàng nước ngoài, tổ chức cung ứng dịch vụ trung gian thanh toán cung ứng cho khách hàng để nạp tiền vào ví điện tử, rút tiền ra khỏi ví điện tử …
- *Dự đoán:* các công cụ tương quan sự kiện  an toàn thông tin mạng.                       kt111  kiến ​​thức về luật chứng cứ điện tử.                       kt112  kiến thức về các quy tắc pháp lý về chứng  cứ và thủ tục tòa án.                       kt117  kiến ​​thức về kỹ thuật quản trị hệ thống,  mạng và cứng hóa (hardening) hệ điều hành.                       kt118  kiến thức về luật, nghị định, chỉ thị,…
- *Ngữ cảnh lấy về:* `12/VBHN-BTTTT#35623|17/2021/TT-BTTTT#63828|2375/QĐ-BNV#89079|2367/QĐ-BNV#88422|2367/QĐ-BNV#88423`
