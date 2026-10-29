\# Changelog



Mọi thay đổi đáng chú ý của AIMS-mini được ghi lại trong tệp này.

Định dạng theo \[Keep a Changelog](https://keepachangelog.com/), đánh số theo \[Semantic Versioning](https://semver.org/).



\## \[Unreleased]



\## \[1.0.0] - 2026-10-29

\### Added

\- Cart.print\_cart() hiển thị chi tiết giỏ hàng, xử lý giỏ trống

\- search\_by\_title() tìm đĩa theo tên

\- Cart.total\_cost\_with\_discount() tính tổng tiền sau giảm giá

\- Thông báo thêm đĩa bằng tiếng Việt

\- In số phiên bản khi chạy chương trình

\- Pull request template, tài liệu use case, unit test



\### Changed

\- Chuyển mã nguồn vào package aims



\### Fixed

\- Giỏ hàng nhận đĩa thứ 21 dù giới hạn là 20 (#8)

\- Tính sai tổng tiền sau giảm giá và chưa kiểm tra phần trăm hợp lệ

