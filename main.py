import sys
from PhienAmTiengViet.PhienAmTiengViet import PhienAmTiengViet

if __name__ == "__main__":
    
    phien_am = PhienAmTiengViet()

    print("PHIÊN ÂM ÂM VỊ TIẾNG VIỆT")

    tu_can_phien_am = input("\n  Nhập từ cần phiên âm: ").strip()

    # Thực hiện phiên âm
    ket_qua = phien_am.phien_am(tu_can_phien_am)

    # Hiển thị kết quả
    ket_qua.hien_thi()

    # phiên âm nhiều từ 
    # danh_sach = ["trăm", "năm", "trong", "cõi", "người", "ta"]
    # phien_am.phien_am_nhieu_tu(danh_sach)