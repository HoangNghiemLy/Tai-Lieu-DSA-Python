'''
2)Ứng dụng tree trong những bài toán đơn giản. 
Bài toán: Viết chương trình theo các yêu cầu sau:
1.Nhập dữ liệu cho cây và kiểm tra nếu masv trùng thì thông báo trùng và nhập lại masv khác.
2.Duyệt và xuất dữ liệu của cây theo thức tự LNR ra màn hình.
3.Sắp xếp cây theo trường dữ liệu.
4.Đếm số nút lá của cây
5.Tính chiều cao của cây
6.Chèn một Node vào cây.
7.Tìm kiếm một Node có giá trị được nhập vào từ bàn phím.
8.Xóa một Node.
'''


#Code:
import os 
class Node:
    def __init__(self, masv, tensv, diem):
        self.masv = masv
        self.tensv = tensv
        self.diem = diem
        self.trai = None
        self.phai = None

    def chen(self, masv, tensv, diem):
        if masv < self.masv:
            if self.trai is None:
                self.trai = Node(masv, tensv, diem)
            else:
                self.trai.chen(masv, tensv, diem)
        elif masv > self.masv:
            if self.phai is None:
                self.phai = Node(masv, tensv, diem)
            else:
                self.phai.chen(masv, tensv, diem)
        else:
            print(f'Mã sinh viên {masv} bị trùng')

    def duyet(self, goc=0):
        #duyệt theo LNR
        nut_ht = goc
        if goc == 0:
            nut_ht = self

        if nut_ht is None:
            return []
        else:
            kq = []
            kq_trai = self.duyet(nut_ht.trai)
            for i in kq_trai:
                kq.append(i)
            kq.append((nut_ht.masv, nut_ht.tensv, nut_ht.diem))
            kq_phai = self.duyet(nut_ht.phai)
            for i in kq_phai:
                kq.append(i)
            return kq
        
    
    def xuat (self):
        #Xuất dữ liệu của cây
        for masv, tensv, diem in self.duyet():
            print(f'Mã sinh viên: {masv}, Tên sinh viên: {tensv}, Điểm: {diem}')
    
    def sap_xep(self):
        #Sắp xếp cây theo trường dữ liệu
        return sorted(self.duyet(), key=lambda x: x[2])
    
    def dem_nut_la(self, goc=0):
        #Đếm số nút lá của cây
        nut_ht = goc
        if goc == 0:
            nut_ht = self
        if nut_ht is None:
            return 0
        if nut_ht.trai is None and nut_ht.phai is None:
            return 1
        return self.dem_nut_la(nut_ht.trai) + self.dem_nut_la(nut_ht.phai)
    
    def chieu_cao(self, goc=0):
        #Tính chiều cao của cây
        nut_ht = goc
        if goc == 0:
            nut_ht = self
        if nut_ht is None:
            return 0
        return max(self.chieu_cao(nut_ht.trai), self.chieu_cao(nut_ht.phai)) + 1
    
    def tim_kiem(self, masv, goc=0):
        #Tìm kiếm một Node có giá trị được nhập vào từ bàn phím
        nut_ht = goc
        if goc == 0:
            nut_ht = self
        if nut_ht is None:
            return None
        if nut_ht.masv == masv:
            return nut_ht
        if masv < nut_ht.masv:
            return self.tim_kiem(masv, nut_ht.trai)
        return self.tim_kiem(masv, nut_ht.phai)
    
    def xoa(self,goc,ma_sv):
        #Xóa một Node có giá trị được nhập vào từ bàn phím
        if goc is None:
            return goc
        if ma_sv < goc.masv:
            goc.trai = self.xoa(goc.trai, ma_sv)
        elif ma_sv > goc.masv:
            goc.phai = self.xoa(goc.phai, ma_sv)
        else:
            if goc.trai is None:
                return goc.phai
            elif goc.phai is None:
                return goc.trai
            goc.masv = self.tim_min(goc.phai)
            goc.phai = self.xoa(goc.phai, goc.masv)
        return goc
    
    def kiem_tra_rong(self):
        if self.masv is None:
            return True
        return False
    def in_cay(self):
        if self.kiem_tra_rong() == True:
            return
        else:
            if self.trai != None:
                self.trai.in_cay()
            print(f'Mã sinh viên: {self.masv}, Tên sinh viên: {self.tensv}, Điểm: {self.diem}')
            if self.phai != None:
                self.phai.in_cay()
    
    

    

#class nut
                    
def main():
    while True:
        os.system('cls')
        print('1. Nhập dữ liệu cho cây')
        print('2. Duyệt và xuất dữ liệu của cây theo thức tự LNR')
        print('3. Sắp xếp cây theo trường dữ liệu')
        print('4. Đếm số nút lá của cây')
        print('5. Tính chiều cao của cây')
        print('6. Chèn một Node vào cây')
        print('7. Tìm kiếm một Node có giá trị được nhập vào từ bàn phím')
        print('8. Xóa một Node')
        print('9. In cây')
        print('10. Thoát')
        chon = int(input('Chọn chức năng: '))
        if chon == 1:
            n = int(input('Nhập số lượng sinh viên: '))
            masv = int(input('Nhập mã sinh viên: '))
            tensv = input('Nhập tên sinh viên: ')
            diem = float(input('Nhập điểm: '))
            goc = Node(masv, tensv, diem)
            for i in range(n-1):
                masv = int(input('Nhập mã sinh viên: '))
                tensv = input('Nhập tên sinh viên: ')
                diem = float(input('Nhập điểm: '))
                goc.chen(masv, tensv, diem)
        elif chon == 2:
            for masv, tensv, diem in goc.duyet():
                print(f'Mã sinh viên: {masv}, Tên sinh viên: {tensv}, Điểm: {diem}')

        elif chon == 3:
            for masv, tensv, diem in goc.sap_xep():
                print(f'Mã sinh viên: {masv}, Tên sinh viên: {tensv}, Điểm: {diem}')
        elif chon == 4:
            print(f'Số nút lá của cây là: {goc.dem_nut_la()}')
        elif chon == 5:
            print(f'Chiều cao của cây là: {goc.chieu_cao()}')
        elif chon == 6:
            masv = int(input('Nhập mã sinh viên: '))
            tensv = input('Nhập tên sinh viên: ')
            diem = float(input('Nhập điểm: '))
            goc.chen(masv, tensv, diem)
        elif chon == 7:
            masv = int(input('Nhập mã sinh viên cần tìm: '))
            node = goc.tim_kiem(masv)
            if node is not None:
                print(f'Mã sinh viên: {node.masv}, Tên sinh viên: {node.tensv}, Điểm: {node.diem}')
            else:
                print('Không tìm thấy sinh viên')
        elif chon == 8:
            ma_sv = int(input('Nhập mã sinh viên cần xóa: '))
            if goc.tim_kiem(ma_sv) is not None:
                goc = goc.xoa(goc, ma_sv)
                print('Xóa thành công')
            else:
                print(f'Không tìm thấy sinh viên {ma_sv}')
           
            
        elif chon == 9:
            goc.in_cay()
        elif chon == 10:
            print('Thoát chương trình')
            break
        else:
            print('Chọn chức năng không hợp lệ')
        os.system('pause')


if __name__ == '__main__':
    main()