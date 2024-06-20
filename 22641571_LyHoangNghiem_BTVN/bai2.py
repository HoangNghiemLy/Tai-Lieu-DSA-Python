
'''
Viết chương trình thực hiện các yêu cầu sau:
1.	Khởi tạo một cây nhị phân.
2.	Tính và trả về tổng giá trị các node trên cây nhị phân gồm các giá trị nguyên
Gợi ý: tham khảo hàm NLR để viết hàm SumTree
3.	Tìm giá trị nguyên lớn nhất và nhỏ nhất trong số các phần tử nguyên trên cây nhị phân tìm kiếm gồm các giá trị nguyên
Gợi ý: dựa vào tính chất của cây nhị phân
4.	Tính và trả về số lượng các node của cây nhị phân gồm các giá trị nguyên
Gợi ý: tham khảo hàm NLR để viết hàm CountNode
5.	Tính và trả về số lượng các node lá trên cây
'''
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
    #khởi tạo cây
    def chen(self,khoa):
        if self.goc == None:
            self.goc = Nut(khoa)
        else: #có nút rồi
            self.goc.chen(khoa)
        #if
    #def chèn 1 nút vào cây 
    #tính tổng các node, tham khảo hàm NLR
    def SumTree(self):
        if self.goc == None:
            return 0
        else:
            return self.SumNode(self.goc)
        #if
    #def
    def SumNode(self,nut):
        if nut == None:
            return 0
        return nut.khoa + self.SumNode(nut.trai) + self.SumNode(nut.phai)
    #def
    #tìm giá trị lớn nhất
    def nut_max(self,n):
        if n == None:
            return None
        if n.phai == None:
            return n.khoa
        return self.nut_max(n.phai)
    #def
    def nut_min(self,n):
        if n == None:
            return None
        if n.trai == None:
            return n.khoa
        return self.nut_min(n.trai)
    #def

    #đếm số node
    def CountNode(self):
        if self.goc == None:
            return 0
        else:
            return self.CountNodeTree(self.goc)
        #if
    #def
    def CountNodeTree(self,nut):
        if nut == None:
            return 0
        return 1 + self.CountNodeTree(nut.trai) + self.CountNodeTree(nut.phai)
    #def
    #đếm số node lá
    def CountLeafNode(self):
        if self.goc == None:
            return 0
        else:
            return self.CountLeafNodeTree(self.goc)
        #if
    #def
    def CountLeafNodeTree(self,nut):
        if nut == None:
            return 0
        if nut.trai == None and nut.phai == None:
            return 1
        return self.CountLeafNodeTree(nut.trai) + self.CountLeafNodeTree(nut.phai)
    #def
while True:
    os.system('cls')
    print('1. Khởi tạo một cây nhị phân.')
    print('2. Tính và trả về tổng giá trị các node trên cây nhị phân gồm các giá trị nguyên')
    print('3. Tìm giá trị nguyên lớn nhất và nhỏ nhất trong số các phần tử nguyên trên cây nhị phân tìm kiếm gồm các giá trị nguyên')
    print('4. Tính và trả về số lượng các node của cây nhị phân gồm các giá trị nguyên')
    print('5. Tính và trả về số lượng các node lá trên cây')
    print('6. Thoát')
    luachon = (input('Mời bạn chọn: '))
    if luachon == '1':
        cay = CayNhiPhanTimKiem()
        n = int(input('Nhập số lượng node: '))
        for i in range(n):
            khoa = int(input('Nhập giá trị node: '))
            cay.chen(khoa)

    elif luachon == '2':
        print(f'Tổng các node trên cây là: {cay.SumTree()}')
        os.system('pause')
    elif luachon == '3':
        print(f'Node lớn nhất là: {cay.nut_max(cay.goc)}')
        print(f'Node nhỏ nhất là: {cay.nut_min(cay.goc)}')

        os.system('pause')
    elif luachon == '4':
        print(f'Số lượng các node là: {cay.CountNode()}')
        os.system('pause')
    elif luachon == '5':
        print(f'Số lượng các node lá là: {cay.CountLeafNode()}')
        os.system('pause')
    elif luachon == '6':
        print('Cảm ơn bạn đã sử dụng dịch vụ')
        break
    else:
        print('Sai chức năng, mời bạn chọn lại')
        os.system('pause')

    

