class BangAmDem:
    """Bảng 2: Hệ thống âm đệm - 2 bán nguyên âm"""

    def __init__(self):
        self.du_lieu = [
            ("u", "/-w-/", 1),
            ("o", "/-w-/", 1),
        ]
        self.ten_bang = "Bảng 2: Hệ thống âm đệm"

    def tim(self, chu_viet):
        """Tìm chữ viết trong bảng"""
        for chu, am_vi, stt in self.du_lieu:
            if chu == chu_viet:
                return am_vi, stt
        return None

    def tach(self, van, am_dau):
        """
        Tách âm đệm ra khỏi vần.
        Quy tắc:
          - Sau 'q': luôn có âm đệm 'u'
          - 'u' đứng trước nguyên âm → âm đệm
          - 'o' đứng trước nguyên âm → âm đệm
        Trả về: (âm đệm, phần còn lại)
        """
        if not van:
            return "", van

        # Trường hợp 1: sau 'q' luôn có âm đệm 'u'
        if am_dau == "q" and van.startswith("u"):
            return "u", van[1:]

        # Trường hợp 2: 'u' đứng trước một nguyên âm → âm đệm
        if van[0] == "u" and len(van) > 1:
            ky_tu_sau = van[1]
            # Các nguyên âm có thể đứng sau âm đệm 'u'
            if ky_tu_sau in "aeêiơâoyư":
                return "u", van[1:]

        # Trường hợp 3: 'o' đứng trước một nguyên âm → âm đệm
        if van[0] == "o" and len(van) > 1:
            ky_tu_sau = van[1]
            if ky_tu_sau in "aeêơâă":
                return "o", van[1:]

        # Không có âm đệm
        return "", van
