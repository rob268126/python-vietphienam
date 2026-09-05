class KetQuaPhienAm:
    """Lưu kết quả phiên âm cho 1 âm tiết"""

    def __init__(self, am_tiet):
        self.am_tiet = am_tiet
        self.am_dau = None       # (chữ viết, âm vị, STT)
        self.am_dem = None       # (chữ viết, âm vị, STT)
        self.am_chinh = None     # (chữ viết, âm vị, STT)
        self.am_cuoi = None      # (chữ viết, âm vị, STT)

    def hien_thi(self):
        """In kết quả phiên âm ra màn hình"""
        print("\n" + "=" * 60)
        print(f"  PHIÊN ÂM: \"{self.am_tiet}\"")
        print("=" * 60)

        # Âm đầu
        if self.am_dau[0] == "":
            print(f"  Âm đầu  : /ʔ-/ (zero)     → Bảng 1, STT 22")
        else:
            chu, am_vi, stt = self.am_dau
            print(f"  Âm đầu  : {am_vi:<10} (chữ: \"{chu}\") → Bảng 1, STT {stt}")

        # Âm đệm
        if self.am_dem[0] == "":
            print(f"  Âm đệm  : /zero/          → Bảng 2, STT 2")
        else:
            chu, am_vi, stt = self.am_dem
            print(f"  Âm đệm  : {am_vi:<10} (chữ: \"{chu}\") → Bảng 2, STT {stt}")

        # Âm chính
        chu, am_vi, stt = self.am_chinh
        if am_vi:
            print(f"  Âm chính: {am_vi:<10} (chữ: \"{chu}\") → Bảng 3, STT {stt}")
        else:
            print(f"  Âm chính: (chưa nhận diện được: \"{chu}\")")

        # Âm cuối
        if self.am_cuoi[0] == "":
            print(f"  Âm cuối : /zero/          → Bảng 4, STT 9")
        else:
            chu, am_vi, stt = self.am_cuoi
            print(f"  Âm cuối : {am_vi:<10} (chữ: \"{chu}\") → Bảng 4, STT {stt}")

        print("=" * 60)
