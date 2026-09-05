import sys
from PhienAmTiengViet.PhienAmTiengViet import PhienAmTiengViet
from XuLyCau.XuLyCau import XuLyCau
from XuLyDau.XuLyDau import XuLyDau

def main():
    phien_am = PhienAmTiengViet()
    xu_ly_cau = XuLyCau()
    xu_ly_dau = XuLyDau()
    
    print("\nPHIÊN ÂM ÂM VỊ HỌC TIẾNG VIỆT")
    
    while True:
        print("\nNhập từ hoặc câu cần phiên âm (nhấn 'q' để thoát):")
        user_input = input("> ").strip()
        
        # Check thoát
        if user_input.lower() == 'q':
            while True:
                confirm = input("Bạn có chắc chắn muốn thoát? (y/n): ").strip().lower()
                if confirm == 'y':
                    print("Cảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
                    return
                elif confirm == 'n':
                    break
                else:
                    print("Vui lòng nhập 'y' hoặc 'n'.")
            continue
            
        if not user_input:
            continue
            
        # Tách câu thành danh sách từ
        danh_sach_tu = xu_ly_cau.tach_tu(user_input)
        
        if not danh_sach_tu:
            print("Không tìm thấy từ hợp lệ.")
            continue
            
        # Lặp qua từng từ để phiên âm
        for tu_goc in danh_sach_tu:
            # Tách dấu thanh điệu
            tu_bo_dau, thanh_dieu = xu_ly_dau.tach_dau(tu_goc)
            
            # Thực hiện phiên âm
            ket_qua = phien_am.phien_am(tu_goc, tu_bo_dau, thanh_dieu)
            ket_qua.hien_thi()

if __name__ == "__main__":
    main()