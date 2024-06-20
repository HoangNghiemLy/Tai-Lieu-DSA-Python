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
        return self.duyet(nut_ht.trai) + [(nut_ht.masv, nut_ht.tensv, nut_ht.diem)] + self.duyet(nut_ht.phai)
    
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
    
    def xoa(self, masv, goc=0):

        nut_ht = goc
        if goc == 0:
            nut_ht = self
        if nut_ht is None:
            return None
        if masv < nut_ht.masv:
            nut_ht.trai = self.xoa(masv, nut_ht.trai)
        elif masv > nut_ht.masv:
            nut_ht.phai = self.xoa(masv, nut_ht.phai)
        else:
            if nut_ht.trai is None:
                return nut_ht.phai
            if nut_ht.phai is None:
                return nut_ht.trai
            nut_ht.masv, nut_ht.tensv, nut_ht.diem = self.tim_min(nut_ht.phai)
            nut_ht.phai = self.xoa(nut_ht.masv, nut_ht.phai)
        return nut_ht
    


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
        print('9. Thoát')
        chon = int(input('Chọn chức năng: '))
        if chon == 1:
            n = int(input('Nhập số lượng sinh viên: '))
            masv = input('Nhập mã sinh viên: ')
            tensv = input('Nhập tên sinh viên: ')
            diem = float(input('Nhập điểm: '))
            goc = Node(masv, tensv, diem)
            for i in range(n-1):
                masv = input('Nhập mã sinh viên: ')
                tensv = input('Nhập tên sinh viên: ')
                diem = float(input('Nhập điểm: '))
                goc.chen(masv, tensv, diem)
        elif chon == 2:
            goc.xuat()
        elif chon == 3:
            for masv, tensv, diem in goc.sap_xep():
                print(f'Mã sinh viên: {masv}, Tên sinh viên: {tensv}, Điểm: {diem}')
        elif chon == 4:
            print(f'Số nút lá của cây là: {goc.dem_nut_la()}')
        elif chon == 5:
            print(f'Chiều cao của cây là: {goc.chieu_cao()}')
        elif chon == 6:
            masv = input('Nhập mã sinh viên: ')
            tensv = input('Nhập tên sinh viên: ')
            diem = float(input('Nhập điểm: '))
            goc.chen(masv, tensv, diem)
        elif chon == 7:
            masv = input('Nhập mã sinh viên cần tìm: ')
            node = goc.tim_kiem(masv)
            if node is not None:
                print(f'Mã sinh viên: {node.masv}, Tên sinh viên: {node.tensv}, Điểm: {node.diem}')
            else:
                print('Không tìm thấy sinh viên')
        elif chon == 8:
            masv = input('Nhập mã sinh viên cần xóa: ')
            goc = goc.xoa(masv)
        elif chon == 9:
            break
        else:
            print('Chọn chức năng không hợp lệ')
        input('Nhấn Enter để tiếp tục...')
    print('Kết thúc chương trình')

if __name__ == '__main__':
    main()