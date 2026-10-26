\# AIMS-mini – Use case



Actor: \*\*Customer\*\*



| Use case | Mô tả |

|---|---|

| Add DVD to cart | Thêm một đĩa vào giỏ, tối đa 20 đĩa |

| Remove DVD from cart | Xóa một đĩa khỏi giỏ |

| View cart | Xem danh sách đĩa và tổng tiền (`print\_cart`) |

| Search by title | Tìm đĩa theo tên (`search\_by\_title`) |



```mermaid

flowchart LR

&#x20;   C((Customer)) --> A\[Add DVD to cart]

&#x20;   C --> R\[Remove DVD from cart]

&#x20;   C --> V\[View cart]

&#x20;   C --> S\[Search by title]

```

