from demo import DSLienKetHangDoi
class NganXep:
    def __init__(self):
        self.danh_sach = DSLienKetHangDoi()
    #def
    #Kiểm tra danh sách có rỗng không
    def la_rong(self):
        return self.danh_sach.dau == None
    #def
    #Đổi sang kiểu chuỗi
    def __str__(self):
        kq ='Ngăn xếp ['
        kq = kq + str(self.danh_sach)
        kq = kq +']'
        return kq
    #def
    #Đẩy 1 phần tử vào
    def day_vao(self,gia_tri):
        self.danh_sach.them_dau(gia_tri)
    #def
    #Lấy ra 1 phần tử
    def lay_ra(self):
        if self.la_rong():
            return None
        else:
            kq = self.danh_sach.lay_dau()
            self.danh_sach.xoa_dau() # xóa khỏi danh sách
            return kq
        #if
    #def
#class
def main():
    ngan_xep = NganXep()
    print(ngan_xep)
    print('---------Đẩy vào---------')
    for i in range (1,6):
        print(f'*Đẩy vào -> {i}')
        ngan_xep.day_vao(i)
        print(ngan_xep)
    #for
    print('---------Lấy ra---------')
    while not ngan_xep.la_rong():
        gt = ngan_xep.lay_ra()
        print(f'*Lấy ra -> {gt}')
        print(ngan_xep)
    #while
#if
if __name__ == '__main__':
    main()
