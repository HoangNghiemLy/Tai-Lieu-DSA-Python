import os
class Nut:
    def __init__(self,khoa=None):
        self.khoa = khoa
        self.trai = None
        self.phai = None
    #def
    def chen(self,khoa):
        if self is None:
            nut = Nut(khoa)
            self = nut
            return
        #if Nút chưa được khởi tạo
        #nút đã khởi tạo rồi, Nút khác None
        if khoa < self.khoa:
            if self.trai == None:
                self.trai = Nut(khoa) # Nút trái chưa có giá trị
            else:
                self.trai.chen(khoa)
            #if
        elif khoa > self.khoa:
            if self.phai == None:
                self.phai = Nut(khoa)
            else:
                #có nút bên phải rồi
                self.phai.chen(khoa)
            #if 
        else:
        #Không lớn hơn hay không nhỏ hơn, bị trùng khóa
            print(f'Bị trùng khóa {khoa}')
    #def
class CayNhiPhanTimKiem:
    def __init__(self,khoa=None):
        if khoa == None: #Không truyền vào tham số
            self.goc = None
        else:
            self.goc = Nut(khoa)
        #if
    #def
    #khởi tạo cây
    def chen(self,khoa):
        if self.goc == None:
            self.goc = Nut(khoa)
        else: #có nút rồi
            self.goc.chen(khoa)
        #if
    #def chèn 1 nút vào cây
    #Duyệt và xuất dữ liệu của cây theo thức tự LNR ra màn hình.
    def duyet_LNR(self,goc=0):
        nut_ht = goc
        if goc == 0:
            nut_ht = self.goc
        if nut_ht == None:
            return []
        else:
            kq = []
            kq_trai = self.duyet_LNR(nut_ht.trai)
            for x in kq_trai:
                kq.append(x)
            kq.append(nut_ht.khoa)
            kq_phai = self.duyet_LNR(nut_ht.phai)
            for x in kq_phai:
                kq.append(x)
            return kq
        #if
    #def
    #duyệt NLR
    def duyet_NLR(self,goc=0):
        nut_ht = goc
        if goc == 0:
            nut_ht = self.goc
        if nut_ht == None:
            return []
        else:
            kq = []
            kq.append(nut_ht.khoa)
            kq_trai = self.duyet_NLR(nut_ht.trai)
            for x in kq_trai:
                kq.append(x)
            kq_phai = self.duyet_NLR(nut_ht.phai)
            for x in kq_phai:
                kq.append(x)
            return kq
        #if
    #def
    #duyệt LRN 
    def duyet_LRN(self,goc=0):
        nut_ht = goc
        if goc == 0:
            nut_ht = self.goc
        if nut_ht == None:
            return []
        else:
            kq = []
            kq_trai = self.duyet_LRN(nut_ht.trai)
            for x in kq_trai:
                kq.append(x)
            kq_phai = self.duyet_LRN(nut_ht.phai)
            for x in kq_phai:
                kq.append(x)
            kq.append(nut_ht.khoa)
            return kq
        #if
    #def

    #đếm số nút lá của cây
    def dem_so_nut_la(self):
        if self.goc == None:
            return 0
        else:
            return self.dem_la(self.goc)
        #if
    #def
    def dem_la(self,nut):
        if nut == None:
            return 0
        if nut.trai == None and nut.phai == None:
            return 1
        return self.dem_la(nut.trai) + self.dem_la(nut.phai)
    #def
    #Tính chiều cao của cây
    def chieu_cao(self,n):
        if n == None:
            return 0
        return 1 + max(self.chieu_cao(n.trai),self.chieu_cao(n.phai))
    #def
    #Tìm kiếm một Node có giá trị được nhập vào từ bàn phím.
    def tim_kiem(self,khoa):
        if self.goc == None:
            return
        nut_ht = self.goc
        kq=''
        while (nut_ht != None and nut_ht.khoa != khoa):
            kq = kq+f'{nut_ht.khoa} -> '
            if khoa <= nut_ht.khoa:
                nut_ht = nut_ht.trai
            else:
                nut_ht = nut_ht.phai
            #if
        #while
        if nut_ht == None:
            return None
        else:
            kq = kq+f'{nut_ht.khoa}'
            return kq
        #if
    #def
    #Xóa một Node có giá trị được nhập vào từ bàn phím.
    def xoa(self,khoa):
        nut_cha = None
        cha_con = None
        nut_ht = self.goc
        #tìm nút xóa,
        #các trường hợp xóa nút lá, xóa nút có 1 con trái, xóa nút có 1 con phải
        #xóa nút có cả 2 con, xóa nút gốc
        while nut_ht != None:
            if nut_ht.khoa > khoa: #khóa xóa nhỏ hơn
                nut_cha = nut_ht
                nut_ht = nut_ht.trai #tìm nhánh bên trái
                cha_con = 'trai'
            elif nut_ht.khoa < khoa:
                nut_cha = nut_ht
                nut_ht = nut_ht.phai
                cha_con ='phai'
            else: #bằng, tìm thấy nghĩa là xóa nút này
                if nut_cha == None: #nút gốc
                    #Xóa nút gốc
                    #nếu nút gốc không có 2 con
                    if nut_ht.trai == None and nut_ht.phai == None:
                        #xóa nút gốc mà không có con
                        self.goc = None
                    #if
                    elif nut_ht.trai == None:
                        #Nút trái không có con, xóa nút gốc chỉ có 1 nút con bên phải
                        self.goc = nut_ht.phai
                    elif nut_ht.phai == None:
                        #xóa nút chỉ có 1 con bên trái
                        self.goc = nut_ht.trai
                    else:
                        #xóa nút gốc có đủ 2 con
                        #xoay trái
                        self.goc = nut_ht.phai
                        tam = self.goc
                        while tam.trai != None:
                            #truy tìm đến cực trái để gắn nhánh trái xuống bên trái của nút trái
                            tam = tam.trai
                        #while
                        tam.trai = nut_ht.trai
                    #if
                elif nut_ht.trai == None and nut_ht.phai == None:
                    #Không phải nút gốc, xóa nút lá, không có con trái và phải
                    if cha_con =='trai':
                        nut_cha.trai = None
                    else:
                        nut_cha.phai = None
                    #if
                elif nut_ht.trai == None:
                    #không phải nút lá mà là nút giữa
                    #xóa nút chỉ có 1 con bên phải
                    if cha_con == 'trai':
                        nut_cha.trai = nut_ht.phai
                    else:
                        nut_cha.phai = nut_ht.phai
                    #if
                elif nut_ht.phai == None:
                    #xóa nút giữa chỉ có 1 con bên trái
                    if cha_con =='trai':
                        nut_cha.trai = nut_ht.trai
                    else:
                        nut_cha.phai = nut_ht.trai
                    #if
                else:
                    #xóa nút có đủ 2 con
                    #xoay trái
                    if cha_con == 'trai':
                        nut_cha.trai = nut_ht.phai
                    else:
                        nut_cha.phai = nut_ht.phai
                    #if
                    if nut_ht.phai.trai == None:
                        nut_ht.phai.trai = nut_ht.trai
                    else: #nút chưa là None, truy tìm nút tận cùng bên trái
                        tam = nut_ht.phai
                        while tam.trai != None:
                            tam = tam.trai
                        #while
                        tam.trai = nut_ht.trai
                    #if
                #if
                del nut_ht
                break
            #if
        #while
    #def
    

#class
l=CayNhiPhanTimKiem()
l.chen(10)
l.chen(5)
l.chen(15)
l.chen(3)
l.chen(7)

while True:
    os.system('cls')
    print('1. Thêm 1 nút vào cây nếu nó là ước số của 3 số cuối của MASV (571) vào cây nhị phân tìm kiếm')
    print('2. Duyệt và xuất dữ liệu của cây theo thức tự LNR')
    print('3. Đếm số nút lá của cây')
    print('4. Tính chiều cao của cây')
    print('5. Chèn một Node vào cây')
    print('6. Tìm kiếm một Node có giá trị được nhập vào từ bàn phím')
    print('7. Xóa một Node có giá trị được nhập vào từ bàn phím')
    print('8. Duyệt cây theo thứ tự NLR')
    print('9. Duyệt cây theo thứ tự LRN')
    print('0. Thoát')
    cn = input('Chọn chức năng: ')
    if cn == "1":
        value = int(input("Nhập giá trị cần thêm vào cây: "))
        divisor = 571
        if divisor % value == 0:  # Kiểm tra nút mới có là ước số của 711 không
            l.chen(value)
            print("Thêm thành công")
        else:
            print("Không thêm được")
        input('Enter để tiếp tục...')
    elif cn == '2':
        kq = l.duyet_LNR()
        print(kq)
        input('Enter để tiếp tục...')
    elif cn == '3':
        kq = l.dem_so_nut_la()
        print(f'Số nút lá của cây là: {kq}')
        input('Enter để tiếp tục...')
    elif cn == '4':
        kq = l.chieu_cao(l.goc)
        print(f'Chiều cao của cây là: {kq}')
        input('Enter để tiếp tục...')
    elif cn == '5':
        x = int(input('Nhập giá trị cho node cần chèn: '))
        l.chen(x)
    elif cn == '6':
        x = int(input('Nhập giá trị cần tìm: '))
        kq = l.tim_kiem(x)
        if kq == None:
            print('Không tìm thấy')
        else:
            print(f'Tìm thấy: {kq}')
        input('Enter để tiếp tục...')
    elif cn == '7':
        x = int(input('Nhập giá trị cần xóa: '))
        if l.tim_kiem(x) == None:
            print('Không tìm thấy')
        else:
            l.xoa(x)
            print('Xóa thành công')
        input('Enter để tiếp tục...')
    elif cn == '8':
        kq = l.duyet_NLR()
        print(kq)
        input('Enter để tiếp tục...')
    elif cn == '9':
        kq = l.duyet_LRN()
        print(kq)
        input('Enter để tiếp tục...')
    elif cn == '0':
        print('Thoát chương trình')
        break
    else:
        print('Chọn chức năng không hợp lệ')
        input('Enter để tiếp tục...')

