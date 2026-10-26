\# Lab 02 – Câu hỏi thảo luận



\## 1. Vì sao phải đồng bộ master trước khi gửi PR?

Khi nhánh tính năng được tạo từ một bản master cũ, trong lúc làm thì master có thể đã nhận thêm thay đổi của người khác (như `print\_cart` ở PR #4). Đồng bộ master vào nhánh trước khi gửi PR giúp phát hiện và xử lý xung đột ngay trên nhánh của mình, đồng thời chạy thử được chương trình với code mới nhất. Nhờ vậy thứ được review cũng chính là thứ sẽ được tích hợp vào master, tránh trường hợp từng nhánh chạy đúng nhưng ghép lại thì lỗi.



\## 2. Khi nào không được rebase?

Không nên rebase những commit đã push và người khác đã dùng (như master, release/\* hoặc nhánh làm chung), vì rebase tạo commit mới với SHA khác, làm lịch sử của người khác bị lệch và phải force push. Rebase chỉ nên dùng trên nhánh riêng, chưa chia sẻ, để làm gọn lịch sử trước khi gửi PR.

