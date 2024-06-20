'''
Hãy viết các chương trình con sau thực hiện trên cây nhị phân:
1.	Kiểm tra cây rỗng
2.	Kiểm tra nút n có phải là nút lá không.
3.	Kiểm tra nút n có phải là nút cha của nút m không.
4.	Tính chiều cao của cây.
5.	Tính số nút của cây 
6.	Duyệt tiền tự, trung tự, hậu tự.
7.	Đếm số nút lá của cây.
8.	Đếm số nút trung gian của cây.
9.	Nút có giá trị lớn nhất, nhỏ nhất, tổng giá trị các nút, trung bình giá trị các nút
'''
# Hướng dẫn:
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
        if khoa < self.khoa:
            if self.trai == None:
                self.trai = Nut(khoa)
            else:
                self.trai.chen(khoa)
        elif khoa > self.khoa:
            if self.phai == None:
                self.phai = Nut(khoa)
            else:
                self.phai.chen(khoa)
        else:
            print(f'Bị trùng khóa {khoa}')
    
        

       
#class nut
#Định nghĩa lớp cây nhị phân tìm kiếm
class CayNhiPhanTimKiem:
    def __init__(self,khoa=None):
        if khoa == None: #Không truyền vào tham số
            self.goc = None
        else:
            self.goc = Nut(khoa)
        #if
    #def
    #chèn vòa 1 giá trị khóa
    def chen(self,khoa):
        if self.goc == None:
            self.goc = Nut(khoa)
        else: #có nút rồi
            self.goc.chen(khoa)
        #if
    #def chèn 1 nút vào cây
    #kiem tra cay rong
    def cay_rong(self):
        if self.goc == None:
            return True
        return False
    def nut_la(self,data1):
        tmp = self.goc
        while tmp != None:
            if tmp.khoa > data1:
                tmp = tmp.trai
            elif tmp.khoa < data1:
                tmp = tmp.phai
            else:
                break
        if tmp is not None and tmp.trai == None and tmp.phai == None:
            return True
        return False
       
   
    
    #kiem tra nut n co phai la nut cha cua nut m
    def nut_cha(self,cha,con):
        if self.cay_rong() == True:
            return False
        elif self.goc != None and self.goc.trai == None and self.goc.phai ==None:
            return False
        else:
            tmp = self.tim(cha)
            if tmp.trai != None:
                if tmp.trai.khoa == con :
                    return True
            if tmp.phai != None:
                if tmp.phai.khoa == con:
                    return True
            return False
    #tinh chieu cao cua cay
    def chieu_cao(self,n):
        if n == None:
            return 0
        return 1 + max(self.chieu_cao(n.trai),self.chieu_cao(n.phai))
    #tinh so nut cua cay
    def so_nut(self,n):
        if n == None:
            return 0
        return 1 + self.so_nut(n.trai) + self.so_nut(n.phai)
    #duyet tien tu là NLR
    def duyet_tien_tu(self,goc=0):
        nut_ht = goc
        if goc == 0:
            nut_ht = self.goc
        if nut_ht == None:
            return []
        else:
            kq = []
            kq.append(nut_ht.khoa)
            kq_trai = self.duyet_tien_tu(nut_ht.trai)
            for x in kq_trai:
                kq.append(x)
            kq_phai = self.duyet_tien_tu(nut_ht.phai)
            for x in kq_phai:
                kq.append(x)
            return kq
    #duyệt trung tự là LNR
    def duyet_trung_tu(self,goc=0):
        nut_ht = goc
        if goc == 0:
            nut_ht = self.goc
        if nut_ht == None:
            return []
        else:
            kq = []
            kq_trai = self.duyet_trung_tu(nut_ht.trai)
            for x in kq_trai:
                kq.append(x)
            kq.append(nut_ht.khoa)
            kq_phai = self.duyet_trung_tu(nut_ht.phai)
            for x in kq_phai:
                kq.append(x)
            return kq
    #duyệt hậu tự là LRN
    def duyet_hau_tu(self,goc=0):
        nut_ht = goc
        if goc == 0:
            nut_ht = self.goc
        if nut_ht == None:
            return []
        else:
            kq = []
            kq_trai = self.duyet_hau_tu(nut_ht.trai)
            for x in kq_trai:
                kq.append(x)
            kq_phai = self.duyet_hau_tu(nut_ht.phai)
            for x in kq_phai:
                kq.append(x)
            kq.append(nut_ht.khoa)
            return kq
    #đếm số nút lá của cây
    def so_nut_la(self):
        global soNutLaCuaCay
        soNutLaCuaCay = 0
        def dem_So_Nut_La1(root):
            global soNutLaCuaCay
            if root != None:
                dem_So_Nut_La1(root.trai)
                if root.trai == None and root.phai == None:
                    soNutLaCuaCay += 1
                dem_So_Nut_La1(root.phai)
        dem_So_Nut_La1(self.goc)
        return soNutLaCuaCay
    
    #đếm số nút trung gian của cây

    def so_nut_trung_gian(self):
        global soNutTrungGianCuaCay
        soNutTrungGianCuaCay = 0
        def dem_So_Nut_Trung_Gian1(root):
            global soNutTrungGianCuaCay
            if root != None:
                dem_So_Nut_Trung_Gian1(root.trai)
                if root.trai != None or root.phai != None:
                    soNutTrungGianCuaCay += 1
                dem_So_Nut_Trung_Gian1(root.phai)
        dem_So_Nut_Trung_Gian1(self.goc)
        return soNutTrungGianCuaCay
    

    
        
    #nut co gia tri lon nhat
    def nut_lon_nhat(self,n):
        if n == None:
            return None
        if n.phai == None:
            return n.khoa
        return self.nut_lon_nhat(n.phai)
    #nut co gia tri nho nhat
    def nut_nho_nhat(self,n):
        if n == None:
            return None
        if n.trai == None:
            return n.khoa
        return self.nut_nho_nhat(n.trai)
    #tong gia tri cac nut
    def tong_gia_tri(self,n):
        if n == None:
            return 0
        return n.khoa + self.tong_gia_tri(n.trai) + self.tong_gia_tri(n.phai)
    #trung binh gia tri cac nut
    def trung_binh_gia_tri(self,n):
        if n == None:
            return 0
        return self.tong_gia_tri(n) / self.so_nut(n)
    #def
    def tim(self,khoa):
        tmp = self.goc
        while tmp != None:
            if tmp.khoa > khoa:
                tmp = tmp.trai
            elif tmp.khoa < khoa:
                tmp = tmp.phai
            else:
                return tmp
        return None

#class
l = CayNhiPhanTimKiem()
l.chen(50)
l.chen(30)
l.chen(70)
l.chen(20)
l.chen(40)
l.chen(60)
l.chen(80)
l.chen(10)
l.chen(25)
l.chen(35)
while True:
    os.system('cls')
    print('1. Chèn')
    print('2. Kiểm tra cây rỗng')
    print('3. Kiểm tra nút n có phải là nút lá không')
    print('4. Kiểm tra nút n có phải là nút cha của nút m không')
    print('5. Tính chiều cao của cây')
    print('6. Tính số nút của cây')
    print('7. Duyệt tiền tự, trung tự, hậu tự')
    print('8. Đếm số nút lá của cây')
    print('9. Đếm số nút trung gian của cây')
    print('10. Nút có giá trị lớn nhất, nhỏ nhất, tổng giá trị các nút, trung bình giá trị các nút')
    print('11. Thoát')
    luachon = (input('Mời bạn chọn: '))
    if luachon =='1':
        data = int(input('Nhập số lượng nút: '))
        for i in range(data):
            n = int(input('Nhập giá trị: '))
            l.chen(n)
    elif luachon == '2':
        if l.cay_rong() == True:
            print('Cây rỗng')
        else:
            print('Cây không rỗng')
        input('Nhấn enter để tiếp tục')
    elif luachon == '3':
        data1 = int(input('Nhập giá trị nút: '))
        if l.nut_la(data1) == True:
            print('Nút này là nút lá')
        else:
            print('Nút này không phải là nút lá')
        input('Nhấn enter để tiếp tục')
    elif luachon == '4':
        cha = int(input('Nhập giá trị nút cha: '))
        con = int(input('Nhập giá trị nút con: '))
        if l.nut_cha(cha,con) == True:
            print('Nút này là nút cha')
        else:
            print('Nút này không phải là nút cha')
        input('Nhấn enter để tiếp tục')
    elif luachon == '5':
        print(f'Chiều cao của cây là: {l.chieu_cao(l.goc)}')
        input('Nhấn enter để tiếp tục')
    elif luachon == '6':
        print(f'Số nút của cây là: {l.so_nut(l.goc)}')
        input('Nhấn enter để tiếp tục')
    elif luachon == '7':
        print(f'Duyệt tiền tự: {l.duyet_tien_tu()}')
        print(f'Duyệt trung tự: {l.duyet_trung_tu()}')
        print(f'Duyệt hậu tự: {l.duyet_hau_tu()}')
        input('Nhấn enter để tiếp tục')
    elif luachon == '8':
        print(f'Số nút lá của cây là: {l.so_nut_la()}')
        input('Nhấn enter để tiếp tục')
    elif luachon == '9':
        print(f'Số nút trung gian của cây là: {l.so_nut_trung_gian()}')
        input('Nhấn enter để tiếp tục')
    elif luachon == '10':
        print(f'Nút có giá trị lớn nhất: {l.nut_lon_nhat(l.goc)}')
        print(f'Nút có giá trị nhỏ nhất: {l.nut_nho_nhat(l.goc)}')
        print(f'Tổng giá trị các nút: {l.tong_gia_tri(l.goc)}')
        print(f'Trung bình giá trị các nút: {l.trung_binh_gia_tri(l.goc)}')
        input('Nhấn enter để tiếp tục')
    elif luachon == '11':
        print('Chương trình kết thúc')
        break
    else:
        print('Nhập sai, mời nhập lại')
        input('Nhấn enter để tiếp tục')
#while
