class KetQuaPhienAm:
    def __init__(self, tu_goc, tu_bo_dau, thanh_dieu):
        self.tu_goc = tu_goc
        self.am_tiet = tu_bo_dau
        self.thanh_dieu = thanh_dieu
        self.am_dau = None
        self.am_dem = None
        self.am_chinh = None
        self.am_cuoi = None

    def hien_thi(self):
        print("\n" + "=" * 60)
        print(f"  TỪ GỐC: \"{self.tu_goc}\"")
        print(f"  THANH ĐIỆU: {self.thanh_dieu.upper()}")
        print(f"  ÂM TIẾT (đã bỏ dấu): \"{self.am_tiet}\"")
        print("-" * 60)

        if self.am_dau[0] == "":
            print(f"  Âm đầu  : /ʔ-/ (zero)     → Bảng 1, STT 22")
        else:
            chu, am_vi, stt = self.am_dau
            print(f"  Âm đầu  : {am_vi:<10} (chữ: \"{chu}\") → Bảng 1, STT {stt}")

        if self.am_dem[0] == "":
            print(f"  Âm đệm  : /zero/          → Bảng 2, STT 2")
        else:
            chu, am_vi, stt = self.am_dem
            print(f"  Âm đệm  : {am_vi:<10} (chữ: \"{chu}\") → Bảng 2, STT {stt}")

        if self.am_chinh[1]:
            chu, am_vi, stt = self.am_chinh
            print(f"  Âm chính: {am_vi:<10} (chữ: \"{chu}\") → Bảng 3, STT {stt}")
        else:
            print(f"  Âm chính: (chưa nhận diện được: \"{self.am_chinh[0]}\")")

        if self.am_cuoi[0] == "":
            print(f"  Âm cuối : /zero/          → Bảng 4, STT 9")
        else:
            chu, am_vi, stt = self.am_cuoi
            print(f"  Âm cuối : {am_vi:<10} (chữ: \"{chu}\") → Bảng 4, STT {stt}")

        print("=" * 60)
