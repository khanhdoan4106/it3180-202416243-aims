\# Lab 02 – Câu hỏi thảo luận



\## 1. Vì sao phải đồng bộ master trước khi gửi PR?

Khi nhánh tính năng được tạo từ một bản master cũ, trong lúc làm thì master có thể đã nhận thêm thay đổi của người khác (như `print\_cart` ở PR #4). Đồng bộ master vào nhánh trước khi gửi PR giúp phát hiện và xử lý xung đột ngay trên nhánh của mình, đồng thời chạy thử được chương trình với code mới nhất. Nhờ vậy thứ được review cũng chính là thứ sẽ được tích hợp vào master, tránh trường hợp từng nhánh chạy đúng nhưng ghép lại thì lỗi.



\## 2. Khi nào không được rebase?

Không nên rebase những commit đã push và người khác đã dùng (như master, release/\* hoặc nhánh làm chung), vì rebase tạo commit mới với SHA khác, làm lịch sử của người khác bị lệch và phải force push. Rebase chỉ nên dùng trên nhánh riêng, chưa chia sẻ, để làm gọn lịch sử trước khi gửi PR.

## 3. feature/* khác topic/* ra sao?
`feature/*` dùng cho một tính năng mới của chương trình, có thay đổi mã nguồn và hành vi (ví dụ `feature/cart-print`, `feature/search-by-title`). `topic/*` dùng cho các thay đổi theo chủ đề không phải tính năng, như tài liệu, cấu hình, template (ví dụ `topic/pr-template`, `topic/use-case-diagram`). Tên nhánh giúp nhìn vào là biết mục đích của thay đổi.

## Ghi chú về các kiểu merge
- PR #4 (cart-print): Create a merge commit, giữ đủ 3 commit chi tiết.
- PR #5 (search-by-title): lỡ chọn merge commit thay vì squash; vì master đã được bảo vệ nên không viết lại lịch sử, kiểu Squash được thực hiện ở PR câu trả lời Lab 02.
- PR #6 (use-case-diagram): Rebase and merge, commit được đặt thẳng lên master với SHA mới.
