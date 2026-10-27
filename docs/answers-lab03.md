\# Lab 03 – Câu hỏi thảo luận



\## 1. Merge base là gì?

Merge base là commit chung gần nhất của hai nhánh, tức điểm mà hai nhánh bắt đầu tách ra. Khi merge, Git so sánh từng nhánh với merge base để biết mỗi bên đã thay đổi gì. Nếu chỉ một bên sửa một đoạn thì Git tự ghép được, còn nếu cả hai bên cùng sửa một đoạn so với merge base thì sinh ra xung đột. Trong bài, `feature/vietnamese-messages` và `feature/show-added-title` cùng tạo từ một master, sau đó cả hai sửa đúng dòng `print("The disc has been added")`, nên nhánh merge sau bị xung đột. Có thể xem merge base bằng `git merge-base <nhánh-1> <nhánh-2>`.



\## 2. Vì sao master và release/\* phải dùng revert?

`git reset` viết lại lịch sử bằng cách dời con trỏ nhánh về trước, làm mất các commit đã có. Với nhánh đã chia sẻ như master và release/\*, người khác đã kéo các commit đó về máy, nên reset sẽ làm lịch sử của họ bị lệch và buộc phải force push (việc này cũng bị branch protection chặn). `git revert` thì tạo một commit mới đảo ngược thay đổi, lịch sử cũ vẫn giữ nguyên, vẫn đi qua PR và review như mọi thay đổi khác, nên an toàn và dễ truy vết. Trong bài, việc hoàn tác tính năng hiển thị tên đĩa được làm bằng `git revert -m 1` trên commit merge của PR, đưa qua nhánh `bugfix/revert-show-added-title` và PR.



\## Ghi chú

PR bugfix/discount-calculation ban đầu được tạo với base `feature/discount`. Do PR feature/discount → master được merge trước, GitHub tự đổi base của PR bugfix sang master (lịch sử PR vẫn ghi lại sự thay đổi base này), sau đó bản sửa được merge thẳng vào master.

