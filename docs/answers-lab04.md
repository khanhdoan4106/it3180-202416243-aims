\# Lab 04 – Câu hỏi thảo luận



\## 1. Vì sao chuẩn bị phát hành trên master trước, không sửa trên nhánh release?

Số phiên bản và CHANGELOG được cập nhật trên master qua PR, sau đó mới tạo release/lab04 từ master. Như vậy nhánh release chỉ là bản chụp của master tại thời điểm đã được review, không có commit riêng nào phải đồng bộ ngược lại. Nếu sửa trực tiếp trên nhánh release thì master sẽ thiếu các thay đổi đó, lần phát hành sau dễ bị mất CHANGELOG hoặc số phiên bản sai.



\## 2. Vì sao release/\* không merge vào master? So sánh với GitFlow

Trong Release Flow, mọi thay đổi đều bắt đầu từ master rồi mới sang nhánh release, nên master luôn có đủ mọi thứ mà release có. Merge ngược release vào master không đem lại gì mới, ngược lại còn đem về số phiên bản cũ và gây xung đột (ví dụ 1.0.1 trên release với 1.1.0 trên master). Bản sửa lỗi trên release được đưa về master bằng cherry-pick có chọn lọc. GitFlow thì khác: có thêm nhánh develop, nhánh release và hotfix sau khi hoàn tất phải merge về cả main lẫn develop. GitFlow chặt chẽ hơn nhưng nhiều nhánh sống lâu và nhiều lần merge hơn, còn Release Flow giữ master là nguồn duy nhất và các nhánh release chỉ để bảo trì.



\## 3. Vì sao lên 1.0.0 mà không phải 0.4.0?

Theo Semantic Versioning, các phiên bản 0.y.z là giai đoạn phát triển ban đầu, chưa ổn định, có thể thay đổi bất cứ lúc nào. Lab 01 đến Lab 03 tương ứng v0.1.0 đến v0.3.0. Đến Lab 04, chương trình đã có đủ chức năng chính, có test, có CHANGELOG và được đóng băng thành bản phát hành chính thức, nên đánh dấu 1.0.0 để cam kết giữ tương thích. Từ đây thêm tính năng thì tăng MINOR (1.1.0), chỉ sửa lỗi thì tăng PATCH (1.0.1).

