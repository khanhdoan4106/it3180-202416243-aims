\# Lab 05 – Câu hỏi thảo luận



\## 1. Vì sao khi tạo release/lab05 chưa gắn tag v1.1.0?

Tag là định danh cố định, đã chia sẻ thì không được xóa hay di chuyển. Lúc tạo release/lab05 vẫn có thể còn lỗi chưa được đưa vào (như lỗi search\_by\_title ở bài này). Để chưa gắn tag thì có thể đưa bản sửa vào release/lab05 qua PR rồi mới gắn v1.1.0, nên v1.1.0 phát hành ra đã có bản sửa. Nếu gắn tag ngay thì v1.1.0 đã đóng băng kèm lỗi, muốn sửa phải phát hành thêm v1.1.1.



\## 2. Ưu, nhược điểm của upstream first so với release first

Upstream first (Release Flow của Microsoft) sửa lỗi trên master trước rồi cherry-pick sang các nhánh release. Ưu điểm là master không bao giờ thiếu bản sửa, tránh lỗi quay lại ở bản phát hành sau. Nhược điểm là bản vá đến tay người dùng chậm hơn, và bản sửa viết trên master có thể khó áp vào nhánh release cũ vì mã đã thay đổi nhiều.

Release first (cách làm trong học phần) sửa trên nhánh release đang bị lỗi trước rồi mới lan truyền về master. Ưu điểm là vá được bản người dùng đang dùng nhanh nhất, bản sửa viết đúng trên mã của phiên bản đó. Nhược điểm là dễ quên lan truyền về master hoặc các nhánh release khác, nên bắt buộc phải có bước kiểm toán.



\## 3. Nếu quên lan truyền bản sửa sang release/lab05, lệnh nào ở Phần F sẽ phát hiện?

Vòng lặp chạy thử search\_by\_title trên v1.0.1, v1.1.0 và master sẽ in ra 0 ở dòng v1.1.0 thay vì 1, cho thấy bản này vẫn còn lỗi. Ngoài ra lệnh `git log --all --oneline --grep "cherry picked from commit <FIX\_SHA>"` chỉ tìm thấy 1 bản cherry-pick (trên master) thay vì 2, và `git cherry -v origin/release/lab05 origin/release/lab04` sẽ đánh dấu `+` cho commit sửa lỗi, nghĩa là release/lab05 chưa có bản tương đương.

