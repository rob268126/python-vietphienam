class BangAmChinh:
    """Bảng 3: Hệ thống âm chính"""

    def __init__(self):
        # (chữ viết, âm vị, STT)
        self.du_lieu = [
            # Nguyên âm đôi (3 ký tự → ưu tiên khớp trước)
            ("iê", "/-ie-/", 14),
            ("yê", "/-ie-/", 14),
            ("ươ", "/-ɯɤ-/", 15),
            ("uô", "/-uo-/", 16),
            ("ua", "/-uo-/", 16),
            ("ia", "/-ie-/", 14),
            ("ưa", "/-ɯɤ-/", 15),
            # Nguyên âm đơn
            ("i", "/-i-/", 1),
            ("y", "/-i-/", 1),
            ("ê", "/-e-/", 2),
            ("e", "/-ɛ-/", 3),
            ("ư", "/-ɯ-/", 4),
            ("ơ", "/-ɤ-/", 5),
            ("a", "/-a-/", 6),
            ("u", "/-u-/", 7),
            ("ô", "/-o-/", 8),
            ("o", "/-ɔ-/", 9),
            ("â", "/-ɤ̆-/", 10),
            ("ă", "/-ɤ̆-/", 12),
        ]
        self.ten_bang = "Bảng 3: Hệ thống âm chính"

    def tim(self, chu_viet):
        """Tìm chữ viết trong bảng"""
        for chu, am_vi, stt in self.du_lieu:
            if chu == chu_viet:
                return am_vi, stt
        return None

    def tach(self, phan_giua):
        """
        Xác định âm chính từ phần giữa (sau khi đã bỏ âm đầu, âm đệm, âm cuối).
        Trả về: (âm chính, STT)
        """
        # Thử khớp từ dài nhất (2 ký tự cho nguyên âm đôi) → 1 ký tự
        for do_dai in [2, 1]:
            if len(phan_giua) >= do_dai:
                phan_am_chinh = phan_giua[:do_dai]
                ket_qua = self.tim(phan_am_chinh)
                if ket_qua is not None:
                    return phan_am_chinh, ket_qua
        return phan_giua, None
