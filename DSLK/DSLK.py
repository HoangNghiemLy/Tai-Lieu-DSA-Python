#Danh sách liên kết đơn
class Nut:
    def __init__(self,gia_tri):
        self.gia_tri=gia_tri
        self.nut_ke_tiep=None
#def định hàm khởi tạo Node 
class DSLienKet: #danh sách lk rỗng
    def __init__(self):
        self.dau = None
        self.duoi = None
#def định nghĩa danh sách ban đầu
    def them(self,gia_tri):
        nut = Nut(gia_tri)
        if self.dau==None: #thêm vào đầu
            self.dau=nut
            self.duoi=nut
        else: #thêm vào cuối
            self.duoi.nut_ke_tiep=nut
            self.duoi=nut
#In danh sách
    def in_ds(self):
        stt = 0
        hien_tai = self.dau
        kq = 'DS['
        while hien_tai != None:
            stt+=1
            if stt == 1: #DS có 1 phần tử
                kq += ' '+str(hien_tai.gia_tri)
            else:
                kq += ' -> '+ str(hien_tai.gia_tri)
            hien_tai = hien_tai.nut_ke_tiep
        kq += ' ]'
        print(kq)
#Chèn vào danh sách
        
    def chen(self,chi_muc,gia_tri):
        #pass
        nut=Nut(gia_tri)
        truoc=None
        hien_tai=self.dau
        i=0
        while i<chi_muc and hien_tai!=None:
            i+=1
            truoc=hien_tai
            hien_tai=hien_tai.nut_ke_tiep
        if truoc==None:
            #Chèn vào đầu danh sách
            nut.nut_ke_tiep=self.dau
            self.dau=nut
            if self.duoi==None:
                self.duoi=nut
        else:
            if hien_tai == None:
                #Thêm vào cuối danh sách
                self.duoi.nut_ke_tiep=nut
                self.duoi=nut
            else:
                #Thêm vào giữa danh sách
                truoc.nut_ke_tiep=nut
                nut.nut_ke_tiep=hien_tai

        
    def tim(self,gia_tri):
        
        hien_tai = self.dau
        vi_tri = 0
        while hien_tai != None and hien_tai.gia_tri != gia_tri:
            hien_tai = hien_tai.nut_ke_tiep
            vi_tri += 1
        if hien_tai == None:
            return None
        else:
            return vi_tri
    def xoa(self,gia_tri):
        
        hien_tai = self.dau
        truoc = None
        while hien_tai !=None and hien_tai.gia_tri!=gia_tri:
            truoc = hien_tai
            hien_tai = hien_tai.nut_ke_tiep
        if hien_tai !=None:
            #Xử lý......
            if hien_tai == self.dau and hien_tai == self.duoi:
                self.dau=self.duoi=None
            elif hien_tai == self.dau:
                self.dau = self.dau.nut_ke_tiep
            elif hien_tai == self.duoi:
                truoc.nut_ke_tiep = None
                self.duoi = truoc
            else:
                truoc.nut_ke_tiep = hien_tai.nut_ke_tiep
            return True
        else:
            return False
        

    def cap_nhat(self,vi_tri,gia_tri):
        
        hien_tai = self.dau
        i = 0
        while i<vi_tri and hien_tai !=None:
            i +=1
            hien_tai = hien_tai.nut_ke_tiep
        if hien_tai !=None:
            hien_tai.gia_tri = gia_tri
            return True
        else:
            return False
        

    def xoa_het(self):
        
        self.dau = None
        self.duoi = None

