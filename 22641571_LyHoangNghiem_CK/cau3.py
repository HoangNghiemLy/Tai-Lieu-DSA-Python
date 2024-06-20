import os 
class VeTau:
    def __init__(self,ten,giave,id):
        self.ten = ten
        self.giave = giave
        self.id = id
    def __str__(self):
        return f"ID: {self.id}, Ten: {self.ten}, Gia ve: {self.giave}"
class Node:
    def __init__(self,data):
        self.data = data
        self.pLeft = None
        self.pRight = None
class CayNhiPhanTimKiem:
    def __init__(self):
        self.root = None
    def themVaoCay(self,data):
        def themVaoCay1(root,data):
            if root == None:
                return Node(data)
            elif root.data.id > data.id:
                root.pLeft = themVaoCay1(root.pLeft, data)
            elif root.data.id < data.id:
                root.pRight = themVaoCay1(root.pRight, data)
            else:
                print("Trùng mã ID!!!")
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
            else:
                return root.data.id +tongGiaTri1(root.pLeft) + tongGiaTri1(root.pRight)
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
    
    def timKiem(self,id):
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
            print(result.__str__())
        else:
            print("Không tìm thấy ID")
    
    def xoaNodeBatKy(self, x):
        if self.root is None:
            return
        if self.root != None and self.root.pLeft == None and self.pRight == None:
            self.root = None
        
        t=self.root
        parent = t
        while t != None and t.data.id != x:
            parent = t
            if t.data.id > x:
                t = t.pLeft
            elif t.data.id < x:
                t = t.pRight
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
            if t.pLeft == None:
                q = t.pRight
            else:
                q = t.pLeft
            if parent.data.id >= t.data.id:
                if t.data.id == self.root.data.id:
                    if self.root.pLeft == None and self.root.pRight != None:
                        self.root = self.root.pRight
                    elif self.root.pLeft != None and self.root.pRight == None:
                        self.root = self.root.pLeft
                    elif self.root.pLeft != None and self.root.pRight != None and parent.data.id == self.root.data.id:
                        self.root.pLeft = q
                parent.pLeft = q
            elif parent.data.id <= t.data.id:
                parent.pRight = q
            del t
    def vietRaFile(self):
        def vietRaFile1(root,file):
            if root is not None:
                vietRaFile1(root.pLeft,file)
                vietRaFile1(root.pRight,file)
                file.write(root.data.str__()+"\n")
        file = open("output.txt","w")
        vietRaFile1(self.root,file)
        file.close()


bnt = CayNhiPhanTimKiem()
tmp = VeTau("Ly Hoang Nghiem", 100000, 10)
tmp1 = VeTau("ABC", 500000, 2)
tmp2 = VeTau("DEF", 1000000, 8)
tmp3 = VeTau("DDD", 60000, 70)
tmp4 = VeTau("GHJ", 80000, 1)
bnt.themVaoCay(tmp)
bnt.themVaoCay(tmp1)
bnt.themVaoCay(tmp2)
bnt.themVaoCay(tmp3)
bnt.themVaoCay(tmp4)

bnt.LNR()
while(True):
    os.system("cls")
    print("1. Them ve tau.")
    print("2. NLR.")
    print("3. LNR.")
    print("4. Tong gia tri.")
    print("5. Chieu cao.")
    print("6. Tim kiem.")
    print("7. Xoa node bat ky.")
    print("8. In ra file.")
    print("9. Thoat.")
    choice = input("Nhap lua chon: ")
    if choice == "1":
        id = int(input("Nhap ID: "))
        ten = input("Nhap ten: ")
        giave = int(input("Nhap gia ve: "))
        tmp = VeTau(ten, giave, id)
        bnt.themVaoCay(tmp)
    elif choice == "2":
        bnt.NLR()
    elif choice == "3":
        bnt.LNR()
    elif choice == "4":
        print(bnt.tongGiaTri())
    elif choice == "5":
        print(bnt.chieuCao())
    elif choice == "6":
        id = int(input("Nhap ID: "))
        bnt.timKiem(id)
    elif choice == "7":
        id = int(input("Nhap ID: "))
        bnt.xoaNodeBatKy(id)
    elif choice == "8":
        bnt.vietRaFile()
    elif choice == "9":
        print("Tam biet!!!")
        break
    else:
        print("Lua chon khong hop le!!!")
    input("Enter de tiep tuc...")


