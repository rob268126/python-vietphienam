class BangAmCuoi:
    """Bảng 4: Hệ thống âm cuối"""

    def __init__(self):
        # (chữ viết, âm vị, STT)
        # Sắp xếp từ DÀI → NGẮN
        self.du_lieu = [
            # 2 ký tự
            ("nh", "/-ɲ/", 5),
            ("ng", "/-ŋ/", 5),
            ("ch", "/-k/", 6),
            # 1 ký tự
            ("m", "/-m/", 1),
            ("n", "/-n/", 2),
            ("p", "/-p/", 3),
            ("t", "/-t/", 4),
            ("c", "/-k/", 6),
            ("o", "/-w/", 7),
            ("u", "/-w/", 7),
            ("i", "/-j/", 8),
            ("y", "/-j/", 8),
        ]
        self.ten_bang = "Bảng 4: Hệ thống âm cuối"

    def tim(self, chu_viet):
        """Tìm chữ viết trong bảng"""
        for chu, am_vi, stt in self.du_lieu:
            if chu == chu_viet:
                return am_vi, stt
        return None

    def tach(self, van):
        """
        Tách âm cuối từ vần (từ PHẢI sang).
        Trả về: (âm cuối, phần còn lại)
        """
        if not van:
            return "", van

        # Thử khớp từ dài nhất (2 ký tự) → 1 ký tự
        for do_dai in [2, 1]:
            if len(van) >= do_dai:
                phan_cuoi = van[-do_dai:]  # Lấy từ cuối
                ket_qua = self.tim(phan_cuoi)
                if ket_qua is not None:
                    # Kiểm tra: phần còn lại sau khi bỏ âm cuối phải khác rỗng
                    phan_con_lai = van[:-do_dai]
                    if phan_con_lai:  # Vẫn còn nguyên âm
                        return phan_cuoi, phan_con_lai

        # Không có âm cuối
        return "", van
