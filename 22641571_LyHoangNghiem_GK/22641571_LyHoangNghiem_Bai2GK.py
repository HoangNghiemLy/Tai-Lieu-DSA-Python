import os
class KhachHangMuaVe:
    def __init__(self,cmnd,hoten,gaden,giave):
        self.cmnd = cmnd
        self.hoten = hoten
        self.gaden = gaden
        self.giave = giave
    def getCMND(self):
        return self.cmnd
    def setCMND(self,cmnd):
        self.cmnd = cmnd
    def getHoTen(self):
        return self.hoten
    def setHoTen(self,hoten):
        self.hoten = hoten
    def getGaDen(self):
        return self.gaden
    def setGaDen(self,gaden):
        self.gaden = gaden
    def getGiaVe(self):
        return self.giave
    def setGiaVe(self,giave):
        self.giave = giave
    def hienthi(self):
        return f"CMND: {self.cmnd}, Họ tên: {self.hoten}, Ga đến: {self.gaden}, Giá vé: {self.giave}" 
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linked_List:
    def __init__(self):
        self.pHead = None
    def isEmpty(self):
        return self.pHead == None
    def addQueue(self,data):
        p = self.pHead
        while p != None:
            if p.data.getCMND() == data.getCMND():
                print("Khách hàng đã tồn tại, yêu cầu nhập lại!")    
                return
            p = p.next
        p = Node(data)
        if self.isEmpty():
            self.pHead = p
            return
        q = self.pHead
        while q.next != None:
            q = q.next
        q.next = p
        print("Đã thêm khách hàng vào hàng đợi")
    def removeQueue(self):
        if self.isEmpty():
            return None
        p = self.pHead
        self.pHead = p.next
        return p.data
    def removeQueueEnd(self):
        if self.isEmpty():
            return None
        p = self.pHead
        q = None
        while p.next != None:
            q = p
            p = p.next
        if q == None:
            self.pHead = None
        else:
            q.next = None
        return p.data
    def removeQueueCMND(self,cmnd):
        if self.isEmpty():
            return None
        p = self.pHead
        q = None
        while p != None:
            if p.data.getCMND() == cmnd:
                if q == None:
                    self.pHead = p.next
                else:
                    q.next = p.next
                return p.data
            q = p
            p = p.next
        return None
    def display(self):
        p = self.pHead
        while p != None:
            print(p.data.hienthi())
            p = p.next
    def searchCMND(self,cmnd):
        p = self.pHead
        while p != None:
            if p.data.getCMND() == cmnd:
                print(p.data.hienthi())
                return
            p = p.next
        print("Không tìm thấy khách hàng")
    def sort(self):
        p = self.pHead
        while p != None:
            q = p.next
            while q != None:
                if p.data.getCMND() > q.data.getCMND():
                    temp = p.data
                    p.data = q.data
                    q.data = temp
                q = q.next
            p = p.next
class Stack:
    def __init__(self):
        self.pHead1 = None
    def isEmpty(self):
        return self.pHead1 == None
    def push(self,data):
        if data.getCMND() % 2 == 0:
            p = Node(data)
            p.next = self.pHead1
            self.pHead1 = p
    def display(self):
        p = self.pHead1
        while p != None:
            print(p.data.hienthi())
            p = p.next
    
    
l = Linked_List()
a=Stack()

l.addQueue(KhachHangMuaVe(130,"Nguyễn Văn A","Hà Nội",100000))
l.addQueue(KhachHangMuaVe(141,"Nguyễn Văn B","Hồ Chí Minh",200000))
l.addQueue(KhachHangMuaVe(121,"Nguyễn Văn C","Đà Nẵng",300000))
l.addQueue(KhachHangMuaVe(130,"Nguyễn Văn D","Hải Phòng",400000))
l.addQueue(KhachHangMuaVe(199,"Nguyễn Văn E","Quảng Ninh",500000))
l.addQueue(KhachHangMuaVe(200,"Nguyễn Văn F","Hà Tĩnh",600000))
l.addQueue(KhachHangMuaVe(178,"Nguyễn Văn G","Nghệ An",700000)) 
l.addQueue(KhachHangMuaVe(288,"Nguyễn Văn H","Hà Nội",800000))
l.addQueue(KhachHangMuaVe(198,"Nguyễn Văn I","Hà Nội",95.500))
while True:
    os.system('cls')
    print("1. Thêm khách hàng vào hàng đợi")
    print("2. Xuất danh sách khách hàng")
    print("3. Tìm khách hàng theo CMND")
    print("4. Sắp xếp danh sách theo CMND")
    print("5. Xóa khách hàng ở đầu hàng đợi")
    print("6. Xóa khách hàng ở cuối hàng đợi")
    print("7. Xóa khách hàng theo CMND")
    print("8. Thêm khách hàng vào Stack")
    print("9. Xuất danh sách khách hàng trong Stack")
    print("10. Thoát")
    choice =input("Nhập lựa chọn của bạn: ")
    if choice == "1":
        cmnd = int(input("Nhập CMND: "))
        hoten = input("Nhập họ tên: ")
        gaden = input("Nhập ga đến: ")
        giave = float(input("Nhập giá vé: "))
        kh = KhachHangMuaVe(cmnd,hoten,gaden,giave)
        l.addQueue(kh)
    elif choice == "2":
        l.display()
    elif choice == "3":
        cmnd = int(input("Nhập CMND cần tìm: "))
        l.searchCMND(cmnd)
    elif choice == "4":
        l.sort()
        print("Danh sách sau khi sắp xếp: ")
        l.display()
    elif choice == "5":
        if l.isEmpty():
            print("Hàng đợi rỗng")
        else:
            print("Khách hàng ở đầu hàng đợi: ",l.removeQueue().hienthi())
    elif choice == "6":
        if l.isEmpty():
            print("Hàng đợi rỗng")
        else:
            print("Khách hàng ở cuối hàng đợi: ",l.removeQueueEnd().hienthi())
    elif choice == "7":
        cmnd = int(input("Nhập CMND cần xóa: "))
        kh = l.removeQueueCMND(cmnd)
        if kh == None:
            print("Không tìm thấy khách hàng")
        else:
            print("Đã xóa khách hàng: ",kh.hienthi())
    elif choice == "8":
        p = l.pHead
        while p != None:
            if p.data.getCMND() % 2 == 0:
                a.push(p.data)
            p = p.next
        print("Thêm thành công")
    elif choice == "9":
        a.display()
    elif choice == "10":
        print("Kết thúc chương trình")
        break
    input("Nhấn Enter để tiếp tục...")




