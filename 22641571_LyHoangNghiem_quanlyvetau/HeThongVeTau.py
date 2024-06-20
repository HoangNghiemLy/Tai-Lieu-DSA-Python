import json 
import KhachHangMuaVe as kh
class HeThongVeTau:
#Sử dụng ArrayList để lưu trữ danh sách vé đã bán
#Sử dụng LinkedList để lưu trữ danh sách khách hàng đang chờ mua vé
    def __init__(self):
        self.dsve= []
        self.dskh= []
#Tìm kiếm khách hàng đợi vé khi biết cmnd 
    def timKiem(self,cmnd):
        for i in range(len(self.dskh)):
            if self.dskh[i].cmnd == cmnd:
                return self.dskh[i]
        return None
#Thêm một khách hàng mới vào hàng đợi mua vé
    def them(self,cmnd,ten,gaden,giave):
        ku=self.timKiem(cmnd)
        if ku==None:
            tmp=kh.KhachHang(cmnd,ten,gaden,giave)
            self.dskh.append(tmp)
        else:
            kh.Gaden = gaden
            kh.Giave = giave
#Bán vé cho một khách hàng. Bán cho người đăng kí trước
    def banve(self):
        if len(self.dskh)==0:
            return None
        kh=self.dskh.pop(0)
        self.dsve.append(kh)
        return kh
#Hiển thị danh sách khách hàng
    def hienthidanhsachkh(self):
        return self.dskh
#Hủy một khách hàng ra khỏi danh sách
    def huykhachhang(self,cmnd):
        kh=self.timKiem(cmnd)
        if kh!=None:
            self.dskh.remove(kh)
            return True
        else:
            return False

#Mục thống kê tình hình: cho biết còn bao nhiêu khách hàng chờ nhận vé, bao nhiêu khách hàng đã nhận vé, tổng số tiền đã thu về là bao nhiêu.
    def thongke(self):
        tongtien=0
        for kh in self.dsve:
            tongtien+=kh.Giave
        return len(self.dskh),len(self.dsve),tongtien
#Hiển thị danh sách các ga đến đang chờ mua vé
    def hienthidsgadangchomuave(self):
        ds=[]
        for kh in self.dskh:
            ds.append(kh.Gaden)
        return set(ds)
#Số vé tương ứng cho ga đang chờ mua vé
    def sovetuongung(self,gaden):
        dem=0
        for kh in self.dskh:
            if kh.Gaden==gaden:
                dem+=1
        return dem
#Sửa thông tin khách hàng khi biết cmnd
    def sua(self,cmnd,ten,gaden,giave):
        kh=self.timKiem(cmnd)
        if kh!=None:
            kh.Ten=ten
            kh.Gaden=gaden
            kh.Giave=giave
            return True
        else:
            return False
    
   


            