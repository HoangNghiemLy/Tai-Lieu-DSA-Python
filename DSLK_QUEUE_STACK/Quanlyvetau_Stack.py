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
        p = QuanLyVeTau(data)
        p.pNext = self.pHead
        self.pHead = p
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
            kq += p.data.hienthi()+'\n'
            p = p.pNext
        return kq
    def search(self,cmnd):
        p = self.pHead
        while p != None:
            if p.data.getCMND() == cmnd:
                return p.data
            p = p.pNext
        return None
   
    def sapxeptheogiavetangdan(self):
        p = self.pHead
        while p != None:
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
            if tmp.data.getGaDen() == gaden:
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
    print('1. Them khach hang mua ve tau')
    print('2. Xoa khach hang mua ve tau')
    print('3. Tim kiem khach hang mua ve tau')
    print('4. Sap xep khach hang mua ve tau theo gia ve tang dan')
    print('5. Xem danh sach khach hang mua ve tau')
    print('6. Hien thi so ve tuong ung cho ga dang cho mua ve')
    print('7. Hien thi danh sach ga dang cho mua ve tau')
    print('8. Thoat')
    chon = int(input('Chon chuc nang: '))
    if chon == 1:
        cmnd = input('Nhap CMND: ')
        hoten = input('Nhap ho ten: ')
        gaden = input('Nhap ga den: ')
        giave = int(input('Nhap gia ve: '))
        kh = KhachHangMuaVe(cmnd,hoten,gaden,giave)
        l.push(kh)
    elif chon == 2:
        cmnd = input('Nhap CMND can xoa: ')
        kh = l.search(cmnd)
        if kh != None:
            print('Khach hang can xoa: ',kh.hienthi())
            l.pop()
            print('Da xoa thanh cong')
            l.inthongtin()
        else:
            print('Khong tim thay khach hang can xoa')
    elif chon == 3:
        cmnd = input('Nhap CMND can tim: ')
        kh = l.search(cmnd)
        if kh != None:
            print('Thong tin khach hang: ',kh.hienthi())
        else:
            print('Khong tim thay khach hang')
    elif chon == 4:
        l.sapxeptheogiavetangdan()
        print('Danh sach khach hang mua ve tau sau khi sap xep: ')
        l.inthongtin()

    elif chon == 5:
        print('Danh sach khach hang mua ve tau: ')
        print(l.inthongtin())
    elif chon == 6:
        gaden = input('Nhap ga den: ')
        print('So ve tuong ung: ',l.hienthisove(gaden))
    elif chon == 7:
        print('Danh sach ga dang cho mua ve tau: ')
        l.hienthidsgadangchomuave()

    elif chon == 8:
        print('Ket thuc chuong trinh')
        break
        
    else:
        print('Chon chuc nang khong hop le')
    input('Enter de tiep tuc...')


