import os
class NhanVien:
    def __init__(self,luong, name, id):
        self.luong = luong
        self.name = name
        self.id = id

    def str__(self):
        return f"ID: {self.id}, Name: {self.name}, Luong: {self.luong}"

class NODE:
    def __init__(self, data):
        self.data = data
        self.pLeft = None
        self.pRight = None

class Binary_Tree:
    def __init__(self):
        self.root = None
    
    def themVaoCay(self, data):

        def themVaoCay1(root, data):
            if root == None:
                return NODE(data)
            elif root.data.id > data.id:
                root.pLeft = themVaoCay1(root.pLeft, data)
            elif root.data.id < data.id:
                root.pRight = themVaoCay1(root.pRight, data)
            else:
                print("Trung ma!!!")
                return root
            return root
        self.root = themVaoCay1(self.root, data)

    def LNR(self):
        def LNR1(root):
            if root is not None:
                LNR1(root.pLeft)
                print(root.data.id)
                LNR1(root.pRight)
        LNR1(self.root)

    def NLR(self):
        def NLR1(root):
            if root != None:
                print(root.data.id)
                NLR1(root.pLeft)
                NLR1(root.pRight)
        NLR1(self.root)

    def tongGiaTri(self):
        def tongGiaTri1(root):
            if root == None:
                return 0
            else: return root.data.id + tongGiaTri1(root.pLeft) + tongGiaTri1(root.pRight)

        return tongGiaTri1(self.root)
    
    def chieuCao(self):
        def chieuCao1(root):
            if root is None:
                return 0
            else:
                left_height = chieuCao1(root.pLeft)
                right_height = chieuCao1(root.pRight)
                return max(left_height, right_height) + 1

        return chieuCao1(self.root)
    
    def timKiem(self, id):
        def timKiem1(root, id):
            if root is None:
                return None
            elif root.data.id == id:
                return root.data
            elif root.data.id > id:
                return timKiem1(root.pLeft, id)
            else:
                return timKiem1(root.pRight, id)

        result = timKiem1(self.root, id)
        if result is not None:
            print(result.str__())
        else:
            print("Khong co")

    def xoaNodeBatKy(self, x):
    
        if self.root is None:
            return
        
        if self.root != None and self.root.pLeft == None and self.root.pRight == None:
            self.root = None
        
        t = self.root
        parent = t

        while t != None and t.data.id != x:
            parent = t
            if t.data.id > x: t = t.pLeft
            elif t.data.id < x: t = t.pRight
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
            if parent.data.id >= t.data.id: 
                if t.data.id == self.root.data.id:
                    if self.root.pLeft == None and self.root.pRight != None:
                        self.root = self.root.pRight
                    elif self.root.pLeft != None and self.root.pRight == None:
                        self.root = self.root.pLeft
                    elif self.root.pLeft != None and self.root.pRight != None and parent.data.id == self.root.data.id:
                        self.root.pLeft = q
                parent.pLeft = q
            elif parent.data.id <= t.data.id: parent.pRight = q
            del t

    def vietRaFile(self):
        def vietRaFile1(root, file):
            if root is not None:
                vietRaFile1(root.pLeft, file)
                vietRaFile1(root.pRight, file)
                file.write(root.data.str__() + "\n")

        file_path = "output.txt"
        with open(file_path, "w") as file:
            vietRaFile1(self.root, file)
        print("Successfully written to file:", file_path)




        
    
    # def LNR(self):
    #     def LNR1(root):
    #         LNR1(root.pLeft)
    #         print(root.)
ss = Binary_Tree()
tmp = NhanVien(111,"uhyfuerf", 50)
tmp1 = NhanVien(202, "ergergeg", 20)
tmp2 = NhanVien(701, "ergergeg", 70)
tmp3 = NhanVien(620, "ergergeg", 60)
tmp4 = NhanVien(853, "ergergeg", 85)
ss.themVaoCay(tmp)
ss.themVaoCay(tmp1)
ss.themVaoCay(tmp2)
ss.themVaoCay(tmp3)
ss.themVaoCay(tmp4)

ss.LNR()

while(True):
    os.system("cls")
    print("1. Them nhan vien.")
    print("2. NLR.")
    print("3. LNR.")
    print("4. In ra file")
    print("5. Tong gia tri.")
    print("6. Chieu cao cua cay.")
    print("7. Tim kiem nhan vien.")
    print("8. Xoa mot node.")
    s = input("Nhap lua chon ma ban muon (Nhap 0 de thoat): ")
    if s == "1":
        id = int(input("Nhap ID: "))
        name = input("Nhap ten: ")
        luong = int(input("Nhap luong: "))
        if id%1 == 0:
            nv = NhanVien(id, name, luong)
            ss.themVaoCay(nv)
        else:
            print("Khong the them !!!")

    elif s == "2":
        ss.NLR()
        os.system("pause")
    elif s == "3":
        ss.LNR()
        os.system("pause")
    elif s == '4':
        ss.vietRaFile()
        os.system("pause")
    elif s == '5':
        print(f"Tong gia tri: {ss.tongGiaTri()}")
        os.system("pause")
    elif s == '6':
        print(f"Chieu cao cua cay: {ss.chieuCao()}")
        os.system("pause")
    elif s == '7':
        id = int(input("Nhap id ban muon tim: "))
        ss.timKiem(id)
        os.system("pause")
    elif s == '8':
        id = int(input("Nhap id: "))
        ss.xoaNodeBatKy(id)
    elif s == "0":
        print("Ket thuc chuong trinh !!!")
        break
    else:
        print("Lua chon khong hop le!")





