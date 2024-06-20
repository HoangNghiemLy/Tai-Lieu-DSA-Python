'''
Định nghĩa lớp DSLK mô tả 1 danh sách liên kết gồm các phương thức:
__init__(self): khởi tạo
__str__(self)__:đổi sang kiểu chuỗi
them_dau(self,gia_tri): thêm phần tử vào đầu danh sách
them_cuoi(self,gia_tri): thêm phần tử vào cuối danh sách
lay_dau(self): lấy giá trị phần tử dầu danh sách
xoa_dau(self): xóa phần tử đầu danh sách
'''
class Nut:
    def __init__(self,gia_tri):
        self.gia_tri = gia_tri
        self.nut_ke_tiep = None
    #def
#class
class DSLienKetHangDoi:
    def __init__(self):
        self.dau = None
        self.duoi = None
    #def
    #đổi về chuỗi
    def __str__(self):
        kq = ''
        stt = 0
        hien_tai = self.dau
        while hien_tai != None:
            stt += 1
            if stt == 1:
                kq = kq + str(hien_tai.gia_tri)
            else:
                kq = kq +'->'+str(hien_tai.gia_tri)
            #if
            hien_tai = hien_tai.nut_ke_tiep
        #while
        return kq
    #def        
    #Thêm đầu
    def them_dau(self,gia_tri):
        nut = Nut(gia_tri)
        if self.dau  == None:
            self.dau = nut
            self.duoi = nut
        else:
            nut.nut_ke_tiep = self.dau
            self.dau = nut
        #if
    #def
    #Thêm cuối
    def them_duoi(self,gia_tri):
        nut = Nut(gia_tri)
        if self.dau == None:
            self.dau = nut
            self.duoi = nut
        else:
            self.duoi.nut_ke_tiep = nut
            self.duoi = nut
        #if
    #def
    #Lấy giá trị phần tử đầu tiên danh sách
    def lay_dau(self):
        if self.dau == None:
            return None
        else:
            return self.dau.gia_tri
        #if
    #def
    #Xóa phần tử đầu danh sách
    def xoa_dau(self):
        tam = self.dau
        if self.dau == self.duoi:
            self.dau = None
            self.duoi = None
        else:
            self.dau = self.dau.nut_ke_tiep
        #if
        del tam 
    #def
#class     

    

