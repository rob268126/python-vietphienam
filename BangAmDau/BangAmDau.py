class BangAmDau:
    """Bảng 1: Hệ thống âm đầu - 22 phụ âm"""

    def __init__(self):
        # Danh sách: (chữ viết, âm vị, STT trong bảng)
        # Sắp xếp từ DÀI → NGẮN để ưu tiên khớp trước
        self.du_lieu = [
            # 3 ký tự
            ("ngh", "/ŋ-/", 19),
            # 2 ký tự
            ("ph", "/f-/", 3),
            ("th", "/tʼ-/", 6),
            ("gi", "/z-/", 9),
            ("ch", "/c-/", 13),
            ("tr", "/ʈ-/", 14),
            ("nh", "/ɲ-/", 15),
            ("kh", "/χ-/", 18),
            ("ng", "/ŋ-/", 19),
            ("gh", "/ɣ-/", 20),
            # 1 ký tự
            ("b", "/b-/", 1),
            ("m", "/m-/", 2),
            ("v", "/v-/", 4),
            ("t", "/t-/", 5),
            ("đ", "/d-/", 7),
            ("n", "/n-/", 8),
            ("d", "/z-/", 9),
            ("r", "/ʐ-/", 10),
            ("x", "/s-/", 11),
            ("s", "/ʂ-/", 12),
            ("l", "/l-/", 16),
            ("c", "/k-/", 17),
            ("k", "/k-/", 17),
            ("q", "/k-/", 17),
            ("h", "/h-/", 21),
        ]
        self.ten_bang = "Bảng 1: Hệ thống âm đầu"

    def tim(self, chu_viet):
        """Tìm chữ viết trong bảng, trả về (âm vị, STT) hoặc None"""
        for chu, am_vi, stt in self.du_lieu:
            if chu == chu_viet:
                return am_vi, stt
        return None

    def tach(self, am_tiet):
        """
        Tách âm đầu ra khỏi âm tiết.
        Trả về: (âm đầu, phần còn lại)
        """
        # Thử khớp từ dài nhất (3 ký tự) → ngắn nhất (1 ký tự)
        for do_dai in [3, 2, 1]:
            if len(am_tiet) >= do_dai:
                phan_dau = am_tiet[:do_dai]
                ket_qua = self.tim(phan_dau)
                if ket_qua is not None:
                    return phan_dau, am_tiet[do_dai:]
        # Không có âm đầu (âm tiết bắt đầu bằng nguyên âm)
        return "", am_tiet
