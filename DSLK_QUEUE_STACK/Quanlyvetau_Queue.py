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
        return "CMND: "+self.cmnd+" - Họ tên: "+self.hoten+" - Ga đến: "+self.gaden+" - Giá vé: "+str(self.giave)
class QuanLyVeTau:
    def __init__(self,data):
        self.data = data
        self.pNext = None
pHead = None

class Linked_List:
    def __init__(self):
        #Queue
        self.pHead = None
    #Hàm kiểm tra Queue rỗng ko
    def isEmpty(self):
        return self.pHead == None
    #hàm thêm một đối tượng vào cuối Queue
    def addQueue(self,data):
        #duyệt qua toàn bộ danh sách để kiểm tra xem CMND đã tồn tại chưa
        p = self.pHead
        while p != None:
            if p.data.getCMND() == data.getCMND():
                print("Khách hàng đã tồn tại")    
                return
            
            p = p.pNext

        p = QuanLyVeTau(data)
        if self.isEmpty():
            self.pHead = p
            return
        q = self.pHead
        while q.pNext != None:
            q = q.pNext
        q.pNext = p
        print("Đã thêm khách hàng vào hàng đợi")



    #hàm lấy một đối tượng ở đầu Queue
    def removeQueue(self):
        if self.isEmpty():
            return None
        p = self.pHead
        self.pHead = p.pNext
        return p.data
    #hàm trả về giá trị phần tử nằm ở đầu Queue mà không hủy nó khỏi Queue. Nếu Queue rỗng thì trả về None
    def front(self):
        if self.isEmpty():
            return None
        return self.pHead.data
    #Hàm xóa phần tử đầu tiên của hàng Q
    def DeQueue(self):
        if self.isEmpty():
            return None
        p = self.pHead
        self.pHead = p.pNext
        return p.data
    #hàm trả về số phần tử của hàng Q
    def Size(self):
        p = self.pHead
        size = 0
        while p != None:
            size += 1
            p = p.pNext
        return size
    #Hàm in hàng Q
    def Print_Queue(self):
        p = self.pHead
        kq = ''
        while p != None:
            kq += p.data.hienthi()+'\n'
            p = p.pNext
        return kq
    #Hàm xóa hàng Q
    def Delete_Queue(self):
        self.pHead = None
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
    #in danh sách khách hàng đang chờ mua vé ra file
    def inThongTinRaFile(self):
        fr = open('DanhSachKhachHang.txt','w',encoding='utf-8')
        p = self.pHead
        while p != None:
            fr.write(p.data.hienthi()+'\n')
            p = p.pNext
        fr.close()
    #luu danh sách khách hàng đang chờ mua vé vào file
    def luuDanhSachRaFile(self):
        fr = open('DanhSachKhachHang.txt','a',encoding='utf-8')
        p = self.pHead
        while p != None:
            fr.write(p.data.hienthi()+'\n')
            p = p.pNext
        fr.close()
    

    
    


l = Linked_List()
while True:
    os.system('cls')
    print("1. Thêm một khách hàng vào cuối hàng đợi mua vé")
    print("2. Lấy một khách hàng ở đầu hàng đợi mua vé")
    print("3. Lấy một khách hàng nhưng không xóa khỏi hàng đợi")
    print("4. Xóa khách hàng ở đầu hàng đợi")
    print("5. Số lượng khách hàng đang chờ mua vé")
    print("6. In thông tin các khách hàng đang chờ mua vé")
    print("7. Tim kiếm thông tin khách hàng theo CMND")
    print("8. Sắp xếp thông tin khách hàng theo giá vé tăng dần")
    print("9. In thông tin các ga đang chờ mua vé")
    print("10. Đọc dữ liệu từ file")
    print("11. Lưu danh sách khách hàng đang chờ mua vé vào file")
    print("12. Xóa toàn bộ hàng đợi")
    print("13. Thoát")
    chon = input("Nhập lựa chọn của bạn: ")
    if chon == "1":
        cmnd = input("Nhập CMND: ")
        hoten = input("Nhập họ tên: ")
        gaden = input("Nhập ga đến: ")
        giave = int(input("Nhập giá vé: "))
        kh = KhachHangMuaVe(cmnd,hoten,gaden,giave)
        l.addQueue(kh)
    elif chon == "2":
        if l.isEmpty():
            print("Hàng đợi rỗng")
        else:
            print("Khách hàng ở đầu hàng đợi: ",l.front().hienthi())
    elif chon == "3":
        if l.isEmpty():
            print("Hàng đợi rỗng")
        else:
            print("Khách hàng ở đầu hàng đợi: ",l.front().hienthi())
    elif chon == "4":
        if l.isEmpty():
            print("Hàng đợi rỗng")
        else:
            print("Khách hàng ở đầu hàng đợi: ",l.DeQueue().hienthi())
    elif chon == "5":
        print("Số lượng khách hàng đang chờ mua vé: ",l.Size())
    elif chon == "6":
        if l.isEmpty():
            print("Hàng đợi rỗng")
        else:

             print("Danh sách khách hàng đang chờ mua vé: ")
             print(l.Print_Queue())
    elif chon == "7":
        cmnd = input("Nhập CMND cần tìm: ")
        kh = l.search(cmnd)
        if kh == None:
            print("Không tìm thấy khách hàng")
        else:
            print("Thông tin khách hàng: ",kh.hienthi())
    elif chon == "8":
        l.sapxeptheogiavetangdan()
        print("Danh sách khách hàng sau khi sắp xếp: ")
        l.inthongtin()
    elif chon == "9":
        print("Danh sách ga đang chờ mua vé: ")
        l.hienthidsgadangchomuave()
    elif chon == "10":
        fr = open('dskhdauvao.txt','r',encoding='utf-8')
        for line in fr.readlines():
            line = line.strip()
            cmnd,hoten,gaden,giave = line.split(' - ')
            kh = KhachHangMuaVe(cmnd,hoten,gaden,int(giave))
            
            l.addQueue(kh)
            
        fr.close()
    elif chon == "11":
        l.luuDanhSachRaFile()
        print("Đã lưu danh sách khách hàng đang chờ mua vé vào file")
    elif chon == "12":
        l.Delete_Queue()
        print("Đã xóa toàn bộ hàng đợi")
    elif chon == "13":
        print("Chương trình kết thúc")
        break
    input("Nhấn phím bất kỳ để tiếp tục...")
print("Cảm ơn bạn đã sử dụng dịch vụ của chúng tôi")
