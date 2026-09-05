# Phiên âm tiếng Việt (âm vị học)

Chương trình đơn giản để phân tích và hiển thị phiên âm (âm vị) cho các từ tiếng Việt theo bảng âm đầu, âm đệm, âm chính và âm cuối.

Ngôn ngữ: Python

Tính năng chính:
- Tách âm đầu, âm đệm, âm chính và âm cuối của một âm tiết tiếng Việt.
- Hiển thị kết quả phiên âm với ký hiệu âm vị và tham chiếu bảng.

Yêu cầu:
- Python 3.8+ 
- Không cần thư viện ngoài (không có dependency)

Cách chạy:
1. Mở terminal và chuyển tới thư mục dự án:

```bash
cd /path/to/vietphienam
```

2. Chạy chương trình:

```bash
python3 main.py
```

3. Nhập từ hoặc câu cần phiên âm khi được nhắc. Gõ `q` để thoát.

Ví dụ:

```
Nhập từ hoặc câu cần phiên âm (nhấn 'q' để thoát):
> kim
```

Tệp chính:
- `main.py` — entrypoint tương tác.
- `PhienAmTiengViet/PhienAmTiengViet.py` — lớp xử lý phiên âm.