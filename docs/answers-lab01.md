\# Lab 01 – Câu hỏi thảo luận



\## 1. Cấu hình --global được lưu ở đâu? Khác gì so với --local?

Khi dùng `--global`, cấu hình được lưu trong tệp `.gitconfig` ở thư mục người dùng (ví dụ `C:/Users/PC/.gitconfig`), nên mọi repo trên máy đều dùng chung. Còn `--local` lưu trong `.git/config` của riêng repo đang làm, chỉ có tác dụng với repo đó. Nếu cả hai cùng đặt một thông tin thì Git lấy theo `--local`. Có thể kiểm tra bằng lệnh `git config --list --show-origin` để thấy giá trị nào nằm ở tệp nào.



\## 2. Vì sao dùng git mv?

`git mv` giúp Git hiểu đây là di chuyển/đổi tên tệp chứ không phải xóa tệp cũ rồi tạo tệp mới. Nhờ vậy lịch sử của `cart.py` và `dvd.py` vẫn được giữ lại, chạy `git log --follow -- aims/cart.py` vẫn thấy các commit từ lúc tệp còn ở thư mục gốc. Trên Pull Request, tab Files changed cũng hiện là "renamed" nên người review dễ hiểu thay đổi.



\## 3. release/lab01 có phải là baseline không?

Có, vì đây là phiên bản đã được chốt để nộp bài, muốn sửa thì phải đi qua quy trình (tạo nhánh hotfix rồi PR) chứ không sửa tùy tiện. Tuy vậy nhánh vẫn có thể bị thêm commit, nên để đánh dấu cố định đúng một phiên bản thì cần gắn thêm tag (như `v0.1.0` ở Lab 04).



\## 4. Vì sao không commit thẳng lên master dù làm một mình?

Dù làm một mình, việc đi qua nhánh và PR giúp master luôn ở trạng thái chạy được. Mỗi thay đổi đều có PR ghi lại mục đích, nội dung và cách kiểm thử, nên sau này xem lại hay hoàn tác đều dễ hơn. Ngoài ra cách làm này giúp quen với quy trình làm việc nhóm thực tế, khi có branch protection hay CI thì mọi thay đổi đều phải qua PR.

