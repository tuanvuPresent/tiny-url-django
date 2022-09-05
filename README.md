# short-url-django

---
### Vì sao cần phải rút gọn link
- Dễ nhớ
- URL ngắn mất ít không gian hơn
- Rất tiện lợi khi quản lý và phân tích đo lường số lượng truy cập
---
### Chức năng
- Với một URL sẽ tạo một bí danh ngắn hơn và duy nhất của nó. Đây được gọi là một liên kết ngắn. Liên kết này phải đủ ngắn để có thể dễ dàng sao chép và dán vào các ứng dụng.
---
### Ước tính
- Lượng truy cập, bộ nhớ, băng thông,...
---
### Database
- MongoDb
---
### Cache
- Redis
---
### Thuật toán
- Nếu sử dụng MD5, SHA256 ( Nếu nhiều người dùng nhập cùng một URL, họ có thể nhận được cùng một URL rút gọn và có thể xảy ra va chạm)
- Có thế dùng KGS
---
### Run
```
docker-compose build
docker-compose up -d
```
