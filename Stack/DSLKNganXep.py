class NganXep:
    def __init__(self):
        self.danh_sach = []
    def is_Empty(self):
        return len(self.danh_sach) == 0
    def push(self,gia_tri):
        self.danh_sach.insert(0,gia_tri)
    def __str__(self):
        kq = 'Ngăn xếp ['
        stt = 0
        for x in self.danh_sach:
            stt += 1
            if stt == 1:
                kq += str(x)
            else:
                kq += ' ->'+str(x)
        kq += ']'
        return kq
    def pop(self):
        if self.is_Empty():
            return None
        return self.danh_sach.pop(0)
    
#tạo đối tượng ngăn xếp
if __name__ == '__main__':
    ngan_xep = NganXep()
    print(ngan_xep)
    print('-----Đẩy vào------')
    for i in range(1,6):
        print(f'* Đẩy vào {i}')
        ngan_xep.push(i)
        print(ngan_xep)
    #for
    print('-----Lấy ra------')
    while not ngan_xep.is_Empty():
        gt = ngan_xep.pop()
        print(f'* Lấy ra {gt}')
        print(ngan_xep)
        