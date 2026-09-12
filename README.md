# Bài tập giữa kỹ Môn Xử lý tiếng nói
 
## Đồ án giữa kỳ #1
Hãy viết chương trình phiên âm âm vị học với đầu vào là một câu tiếng Việt và đầu ra là chuỗi các âm tiết đã được phiên âm âm vị học.  
Vd: “Nếu biết rằng em đã có chồng, trời ơi người ấy có buồn không”
=> neu5 biet5 ʐăŋ2 ɛm1 da3 kɔ5 coŋ2, ʈɤi2 ɤi1 ŋɯɤi2 ɤ̌i5 kɔ5 buon2 χoŋ1

## Đồ án giữa kỳ#2
Hãy viết chương trình thống kê dựa trên từ điển tiếng Việt (đã cung cấp) các thông số sau:  
(a): Số lượng âm tiết tiếng Việt khác nhau có trong từ điển.  
(b): Số lượng âm tiết khả dĩ có trong tiếng Việt tính theo tổ hợp:  
    [Phụ_âm_đầu * Âm_Đệm * Âm_Chính * Âm_Cuối * Thanh_điệu].   
(c): So sánh 2 con số (a) và (b) và giải thích lý do tại sao có sự chênh lệch này?  
(d): Tìm ra các quy luật (có thể có) trong hệ thống âm tiết tiếng Việt về:  
- Bình diện ngữ âm: những âm vị nào thường/phải đi với những âm vị nào? Vd.: /q/-/u/  
- Bình diện ngữ pháp: những từ có những âm vị nào thường có xu hướng mang từ loại (A,N,V,..) nào?  
- Bình diện ngữ nghĩa: những từ có những âm vị nào thường có xu hướng mang ý nghĩa nào? Vd: từ chỉ người mẹ thường bắt đầu là phụ âm “m”, như: mẹ, má, mạ; mother, mom, mama, mutter,...; những từ ghép có khuôn vần “ch-v” thường có ý nghĩa “không ổn định”, như: chênh vênh, chạng vạng, chóng vánh, chật vật, chới với, ...; từ đơn có âm chính là “e” , là “ô” , ...; bắt đầu là “đ” , ...?  



## Chạy project
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

