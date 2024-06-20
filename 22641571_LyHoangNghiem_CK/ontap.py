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
        return 'CMND: '+str(self.cmnd)+" - Ho ten: "+self.hoten+" - Ga den: "+self.gaden+" - Gia ve: "+str(self.giave)
class QuanLyVeTau:
    def __init__(self,data):
        self.data = data
        self.pNext = None
pHead = None
class Linked_List:
    def __init__(self):
        self.pHead = None
    def isEmpty(self):
        return self.pHead == None
    def push(self,data):
        #kiểm tra trùng CMND
        p = self.pHead
        while p != None:
            if p.data.getCMND() == data.getCMND():
                return False
            p = p.pNext
        p = QuanLyVeTau(data)
        p.pNext = self.pHead
        self.pHead = p
        return True
    

    def pop(self):
        if self.isEmpty():
            return None
        p = self.pHead
        self.pHead = p.pNext
        return p.data
    def size(self):
        p = self.pHead
        size = 0
        while p != None:
            size += 1
            p = p.pNext
        return size
    def __str__(self):
        p = self.pHead
        kq = ''
        while p != None:
            kq+= p.data.hienthi()+'\n'
            p = p.pNext
        return kq
    def search(self,cmnd):
        p = self.pHead
        while p!= None:
            if p.data.getCMND() == cmnd:
                return p.data
            p=p.pNext
        return None
    def delete(self,cmnd):
        p = self.pHead
        q = None
        while p != None:
            if p.data.getCMND() == cmnd:
                if q == None:
                    self.pHead = p.pNext
                else:
                    q.pNext = p.pNext
                return True
            q = p
            p = p.pNext
        return False 
    def sapxeptheogiavetangdan(self):
        p = self.pHead
        while p!= None:
            q = p.pNext
            while q != None:
                if p.data.getGiaVe() > q.data.getGiaVe():
                    p.data,q.data = q.data,p.data
                q = q.pNext
            p = p.pNext
    def inthongtin(self):
        p = self.pHead
        while p != None:
            print(p.data.hienthi())
            p = p.pNext
    def hienthidsgadangchomuave(self):
        p = self.pHead
        while p != None:
            print(p.data.getGaDen())
            p = p.pNext
    def hienthisove(self,gaden):
        dem = 0
        tmp = self.pHead
        while tmp != None:
            if tmp.data.getGaDen().lower() == gaden.lower():
                dem += 1
            tmp = tmp.pNext
        return dem
l = Linked_List()
l.push(KhachHangMuaVe(123,'Lý Hoàng Nghiêm','Hà Nội',1000000))
l.push(KhachHangMuaVe(156,'Lý Hoàng Nhi','Nha Trang',5500000))
l.push(KhachHangMuaVe(312,'Nguyễn Đức Huy','Bến Tre',200000))
l.push(KhachHangMuaVe(986,'Dương Chí Việt','Sóc Trăng',375000))
l.push(KhachHangMuaVe(764,'Võ Tất Thiên','Long An',250000))
l.push(KhachHangMuaVe(247,'Along','Tiền Giang',123000))

while True:
    os.system('cls')
    print('1. Thêm khách hàng mua vé tàu')
    print('2. Xóa khách hàng mua vé tàu')
    print('3. Tìm kiếm khách hàng theo CMND')
    print('4. Sắp xếp khách hàng mua vé tàu theo giá vé tăng dần')
    print('5. Xuất danh sách khách hàng')
    print('6. Hiển thị số vé tương ứng cho ga đang chờ mua vé')
    print('7. Hiển thị danh sách ga đang chờ mua vé')
    print('8. Thoát')
    chon = input("Chọn chức năng: ")
    if chon == '1':
        cmnd = int(input("Nhập CMND khách hàng mua vé: "))
        hoten = input("Nhập họ tên khách hàng: ")
        gaden = input("Nhập ga đến: ")
        giave = int(input("Nhập giá vé: "))
        if l.push(KhachHangMuaVe(cmnd,hoten,gaden,giave)):
            print("Thêm thành công")
            l.inthongtin()
        else:
            print("Khách hàng đã tồn tại")
            
    elif chon == '2':
        cmnd = int(input("Nhập CMND khách hàng cần xóa: "))
        kh = l.search(cmnd)
        if kh != None:
            print("Khách hàng cần xóa: ",kh.hienthi())
            l.delete(cmnd)
            print("Xóa thành công")
            
        else:
            print('Không tìm thấy khách hàng cần xóa')
    elif chon == '3':
        cmnd = int(input("Nhập CMND khách hàng cần tìm: "))
        kh = l.search(cmnd)
        if kh != None:
            print("Thông tin khách hàng: ",kh.hienthi())
        else:
            print("Không tìm thấy khách hàng")
    elif chon == '4':
        l.sapxeptheogiavetangdan()
        print("Danh sách khách hàng mua vé tàu sau khi sắp xếp giá vé tăng dần: ")
        l.inthongtin()
    elif chon == '5':
        l.inthongtin()
    elif chon == '6':
        gaden = input("Nhập ga đến cần xem số vé tương ứng: ")
        print("Số vé tương ứng: ",l.hienthisove(gaden))
        

    elif chon == '7':
        print("Danh sách ga đang chờ mua vé: ")
        l.hienthidsgadangchomuave()
    elif chon =='8':
        print("Kết thúc chương trình")
        break    
    else:
        print('Chọn chức năng không hợp lệ')
    input("Enter để tiếp tục....")    

    