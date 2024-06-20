import os

class NODE:
    def __init__(self,data):
        self.data = data
        self.pLeft = None
        self.pRight = None

class Binary_Tree:
    def __init__(self):
        self.root = None
    
    def themVaoCay(self, data1):
        def themVaoCay1(root, data1):
            if root == None:
                return NODE(data1)
            elif root.data > data1:
                root.pLeft = themVaoCay1(root.pLeft, data1)
            elif root.data < data1:
                root.pRight = themVaoCay1(root.pRight, data1)
            else:
                print("Trùng ma ")
                return root
                
            return root
        self.root = themVaoCay1(self.root, data1)

    def LNR(self):
        def LNR1(root):
            if root != None:
                LNR1(root.pLeft)
                print(f"{root.data} ", end='')
                LNR1(root.pRight)
        LNR1(self.root)

    def dem_So_Nut_La(self):
        def dem_So_Nut_La1(root):
            if root == None:
                return 0
            elif root != None and root.pLeft == None and root.pRight == None:
                return 1 + dem_So_Nut_La1(root.pLeft) + dem_So_Nut_La1(root.pRight)
            return 0 + dem_So_Nut_La1(root.pLeft) + dem_So_Nut_La1(root.pRight)
        return dem_So_Nut_La1(self.root)
    

    def tinhChieuCaoCuaCay(self):
        def tinhChieuCaoCuaCay1(root):
            if root == None:
                return 0
            else:
                trai = tinhChieuCaoCuaCay1(root.pLeft)
                phai = tinhChieuCaoCuaCay1(root.pRight)
                s = 0
                if trai >= phai:
                    s = trai + 1
                else:
                    s = phai + 1
                return s
        return tinhChieuCaoCuaCay1(self.root)
    
    def timKiemMotNode(self, kk):
        tmp = self.root
        while tmp is not None:
            if tmp.data > kk:
                tmp = tmp.pLeft
            elif tmp.data < kk:
                tmp = tmp.pRight
            else:
                return tmp.data
        return None
    
    def xoaNodeBatKy(self, x):
    
        if self.root is None:
            return
        
        
        t = self.root
        parent = t

        while t != None and t.data != x:
            parent = t
            if t.data > x: t = t.pLeft
            elif t.data < x: t = t.pRight
        if t != None:   
            q = None

            if t.pLeft != None and t.pRight != None:
                parent = t
                r = t.pLeft
                while r.pRight != None:
                    parent = r
                    r = r.pRight

                t.data = r.data
                t = r
            if t.pLeft == None: q = t.pRight
            else: q = t.pLeft
            if parent.data >= t.data: 
                if t.data == self.root.data:
                    if self.root.pLeft == None and self.root.pRight != None:
                        self.root = self.root.pRight
                    elif self.root.pLeft != None and self.root.pRight == None:
                        self.root = self.root.pLeft
                    elif self.root.pLeft != None and self.root.pRight != None and parent.data == self.root.data:
                        self.root.pLeft = q
                parent.pLeft = q
            elif parent.data <= t.data: parent.pRight = q
            del t

b = Binary_Tree()

# b.themVaoCay(5)
# b.themVaoCay(3)
# b.themVaoCay(2)
# b.themVaoCay(4)
# b.themVaoCay(10)
# b.themVaoCay(56)
# b.themVaoCay(6)
# b.themVaoCay(47)
# b.themVaoCay(1000)

b.themVaoCay(5)
b.themVaoCay(6)
b.themVaoCay(7)
b.themVaoCay(8)
b.themVaoCay(9)


# cHÈN


# duyệt LNR


#tìm kiếm 


# xóa 



while True:
    os.system("cls")
    print("1. Thêm một node nhưng là ước số của 441")
    print("2. Duyệt Cây LNR")
    print("3. Đếm Node lá.")
    print("4. Đêms chiều cao của cây.")
    print("5. Tìm kiếm một node bất kỳ")
    print("6. Xóa một node bất kỳ.")
    huy = input("Nhập lựa chọn (Nhập 0 để out): ")
    if huy  == '1':
        n = int(input("Nhập số bạn muốn thêm dô: "))
        if 441%n == 0:
            b.themVaoCay(n)
        else:
            print("Không thể thêm !!!")
        os.system("pause")
    elif huy == '2':
        b.LNR()
        os.system("pause")
    elif huy == '3':
        print(f"Số node lá của cây là: {b.dem_So_Nut_La()}")
        os.system("pause")
    elif huy == '4':
        print(f"Chiều cao của cây là: {b.tinhChieuCaoCuaCay()}")
        os.system("pause")
    elif huy == '5':
        cc = int(input("Tìm kiếm node bạn muốn: "))
        if b.timKiemMotNode(cc) == None:
            print("Không tìm thấy !!!")
        else:
            print("Đã tìm thấy !!!")
        os.system("pause")
    elif huy == '6':
        cc1 = int(input("Xóa một node mà bạn muốn: "))

        if b.timKiemMotNode(cc1) == None:
            print("Không tìm thấy !!!")
        else:
            b.xoaNodeBatKy(cc1)
            print("Xóa thành công !!!")
        os.system("pause")
    elif huy == '0':
        print("Kết thúc chương trình")
        break

    else:
        print("Nhập sai !!!")
        os.system("pause")