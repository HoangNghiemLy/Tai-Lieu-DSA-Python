'''
Nhập vào từ modun DSLK lớp DSLienKetHangDoi
Định nghĩa lớp HangDoi gồm các phương thức:
__init__(self): khởi tạo
__str__(self): đổi sang kiểu chuỗi

'''
from demo import DSLienKetHangDoi
class HangDoi:
    #Queue
    def __init__(self):
        self.danh_sach = DSLienKetHangDoi()
    #def
    #đổi về chuỗi
    def __str__(self):
        kq = 'Hang doi ['
        kq = kq + str(self.danh_sach)
        kq = kq + ']'
        return kq
    #def
    #Kiểm tra hàng đợi rỗng
    def la_rong(self):
        #is empty
        return self.danh_sach.dau == None
    #def
    #Xếp hàng
    def xep_hang(self,gia_tri):
        self.danh_sach.them_duoi(gia_tri)
    #def
    #Lấy ra
    def ra_hang(self):
        if self.la_rong():
            return None
        else:
            kq = self.danh_sach.lay_dau() #lấy ra nhưng chưa xóa
            self.danh_sach.xoa_dau()
            return kq
        #if
    #def
#class
def main():
    hang_doi = HangDoi()
    print(hang_doi)
    print('---------Xếp hàng---------')
    for x in range(1,6):
        print(f'*Xếp hàng ->{x}')
        hang_doi.xep_hang(x)
        print(hang_doi)
    #for
    print('---------Ra hàng---------')
    while not hang_doi.la_rong():
        gt = hang_doi.ra_hang()
        print(f'*Ra hàng ->{gt}')
        print(hang_doi)
    #while
#if
if __name__ == '__main__':
    main()
    