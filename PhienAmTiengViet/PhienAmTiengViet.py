from BangAmDau.BangAmDau import BangAmDau
from BangAmDem.BangAmDem import BangAmDem
from BangAmChinh.BangAmChinh import BangAmChinh
from BangAmCuoi.BangAmCuoi import BangAmCuoi
from KetQuaPhienAm.KetQuaPhienAm import KetQuaPhienAm

class PhienAmTiengViet:
    def __init__(self):
        self.bang_am_dau = BangAmDau()
        self.bang_am_dem = BangAmDem()
        self.bang_am_chinh = BangAmChinh()
        self.bang_am_cuoi = BangAmCuoi()

    def phien_am(self, tu_goc, tu_bo_dau, thanh_dieu):
        ket_qua = KetQuaPhienAm(tu_goc, tu_bo_dau, thanh_dieu)

        # BƯỚC 1: Tách âm đầu
        am_dau, phan_van = self.bang_am_dau.tach(tu_bo_dau)
        if am_dau:
            am_vi, stt = self.bang_am_dau.tim(am_dau)
            ket_qua.am_dau = (am_dau, am_vi, stt)
        else:
            ket_qua.am_dau = ("", "/ʔ-/", 22)

        # BƯỚC 2: Tách âm cuối
        am_cuoi, phan_giua = self.bang_am_cuoi.tach(phan_van)
        if am_cuoi:
            am_vi, stt = self.bang_am_cuoi.tim(am_cuoi)
            ket_qua.am_cuoi = (am_cuoi, am_vi, stt)
        else:
            ket_qua.am_cuoi = ("", "/zero/", 9)

        # BƯỚC 3: Tách âm đệm
        am_dem, phan_am_chinh = self.bang_am_dem.tach(phan_giua, am_dau)
        if am_dem:
            am_vi, stt = self.bang_am_dem.tim(am_dem)
            ket_qua.am_dem = (am_dem, am_vi, stt)
        else:
            ket_qua.am_dem = ("", "/zero/", 2)

        # BƯỚC 4: Xác định âm chính
        am_chinh, ket_qua_am_chinh = self.bang_am_chinh.tach(phan_am_chinh)
        if ket_qua_am_chinh:
            am_vi, stt = ket_qua_am_chinh
            ket_qua.am_chinh = (am_chinh, am_vi, stt)
        else:
            ket_qua.am_chinh = (am_chinh, None, None)

        return ket_qua