class BangBam:
    #định nghĩa bảng băm
    def __init__(self,kich_thuoc=10):
        self.danh_sach = [None for _ in range(kich_thuoc)]
        #cho tất cả các phần tử trong danh sách đều là none
    #def
    #chuyển bảng băm về chuỗi
    def __str__(self):
        kq ='['
        #danh sách gồm 2 cấp
        stt1 = 0
        for x in self.danh_sach:
            stt1=stt1+1
            #Nếu không phải là phần tử đầu tiên
            if stt1 != 1:
                kq = kq +' ,'
            #if
            if x is None:
                kq = kq + '[None]'
            else:
                #không rỗng, không chứa các con bên trong
                kq = kq + '['
                stt2=0
                #duyệt qua các phần tử con
                for e in x:
                    stt2 = stt2 +1
                    #không phải là phần tử đầu tiên, nối thêm vào
                    if stt2 != 1:
                        kq = kq +' , '
                    #if
                    kq = kq + str(e[0])+': '+str(e[1])
                #for
                kq = kq +']'
            #if
        #for
        kq = kq + ']'
        return kq
    #def
    #thực hiện trả về chuyển giá trị băm của khóa
    def bam(self,khoa):
        kich_thuoc = len(self.danh_sach)
        return hash(khoa) % kich_thuoc
    #def
    #thực hiện thêm cặp (khóa, giá trị) vào bảng băm
    def them(self,khoa,gia_tri):
        chi_muc = self.bam(khoa)
        #chưa có phần tử đưa vào vị trí này
        if self.danh_sach[chi_muc] is None:
            #thêm mới
            self.danh_sach[chi_muc] = list() #vị trí bảng băm chứa nhiều phần tử vào mỗi khe
            self.danh_sach[chi_muc].append([khoa,gia_tri])
        else:
            #có rồi, cập nhật
            #Có 2 trường hợp: khe đã có, khe chưa có con
            #TH1: khóa mod 5 = thì khóa và giá trị sẽ được đưa vào khe = số dư
            # Nếu khe đó có giá trị khóa bằng với khóa đưa vào thì cập nhật lại giá trị của khóa đó
            # Nếu khe đó có giá trị khác với khóa đưa vào thì thêm vào cặp khóa (khóa, giá trị) mới vào khe đó
            # Một khe có thể có nhiều phần tử
            cap_nhat = False
            for x in self.danh_sach[chi_muc]:
                #xem có pt bằng nó không
                if x[0] == khoa: #cập nhật giá trị của khóa đó
                    x[1] = gia_tri
                    cap_nhat = True
                    break
                #if
            #for
            if cap_nhat == False: #không cập nhật phần tử mà còn thêm vào
                self.danh_sach[chi_muc].append([khoa,gia_tri])
            #if
        #if
    #def
    #lấy ra 1 giá trị từ bảng băm với khóa tương ứng
    def lay(self,khoa):
        chi_muc = self.bam(khoa)
        #nếu giá trị này none
        if self.danh_sach[chi_muc] is None:
            return None
        else:
            for x in self.danh_sach[chi_muc]:
                if x[0] == khoa:
                    return x[1]
                #if
            #for
        #if
    #def
    #thực hiện như phương thức thêm
    def __setitem__(self,khoa,gia_tri):
        self.them(khoa,gia_tri)
    #def
    #thực hiện như phương thức lấy
    def __getitem__(self,khoa):
        return self.lay(khoa)
    #def
#class
#tạo đối tượng bảng băm
#thêm vào bảng băm các giá trị ngẫu nhiên [khóa, giá trị] vào bảng băm, xuất chuỗi mô tả bảng băm sau mỗi lần thêm
#nhập vào 1 dãy khóa, lấy và xuất ra giá trị tương ứng với khóa đó trong bảng băm
def main():
    bang_bam = BangBam(5)
    import random
    for _ in range(18):
        khoa = random.randint(0,10)
        gia_tri = random.randint(0,100)
        print(f'*Thêm khóa = {khoa}, giá trị = {gia_tri}')
        #bang_bam.them(khoa,gia_tri)
        bang_bam[khoa] = gia_tri
        print(bang_bam)
        print()
    #for
    khoa = int(input('Nhập vào 1 khóa: '))
    #gia_tri = bang_bam.lay(khoa)
    gia_tri = bang_bam[khoa]
    print(f'Khóa ={khoa}, có giá trị = {gia_tri}')
#def 
if __name__ == '__main__':
    main()
    
