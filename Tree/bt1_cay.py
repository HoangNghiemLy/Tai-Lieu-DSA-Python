'''
1)Yêu cầu: Bổ sung chương trình mẫu
1.Hàm tính và trả về tổng giá trị các node trên cây nhị phân gồm các giá trị nguyên
Gợi ý: tham khảo hàm NLR để viết hàm SumTree
2.Hàm tìm giá trị nguyên lớn nhất và nhỏ nhất trong số các phần tử nguyên trên cây nhị phân tìm kiếm gồm các giá trị nguyên
Gợi ý: dựa vào tính chất của cây nhị phân
3.Hàm tính và trả về số lượng các node của cây nhị phân gồm các giá trị nguyên
Gợi ý: tham khảo hàm NLR để viết hàm CountNode
4.Hàm tính và trả về số lượng các node lá trên cây.
Gợi ý: tham khảo hàm duyệt cây nhị phân NLR
'''



class Nut:
    #định nghĩa lớp nút
    def __init__(self,khoa=None):
        self.khoa = khoa
        self.trai = None
        self.phai =None
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
        #if
    #def
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
    #chèn vòa 1 giá trị khóa
    def chen(self,khoa):
        if self.goc == None:
            self.goc = Nut(khoa)
        else: #có nút rồi
            self.goc.chen(khoa)
        #if
    #def chèn 1 nút vào cây
    #Xóa 1 nút
    def xoa(self,khoa):
        nut_cha = None
        cha_con = None
        nut_ht = self.goc
        #tìm nút xóa,
        #các trường hợp xóa nút lá, xóa nút có 1 con trái, xóa nút có 1 con phải
        #xóa nút có cả 2 con, xóa nút gốc
        while nut_ht != None:
            if nut_ht.khoa > khoa: #khóa xóa nhỏ hơn
                nut_cha = nut_ht
                nut_ht = nut_ht.trai #tìm nhánh bên trái
                cha_con = 'trai'
            elif nut_ht.khoa < khoa:
                nut_cha = nut_ht
                nut_ht = nut_ht.phai
                cha_con ='phai'
            else: #bằng, tìm thấy nghĩa là xóa nút này
                if nut_cha == None: #nút gốc
                    #Xóa nút gốc
                    #nếu nút gốc không có 2 con
                    if nut_ht.trai == None and nut_ht.phai == None:
                        #xóa nút gốc mà không có con
                        self.goc = None
                    #if
                    elif nut_ht.trai == None:
                        #Nút trái không có con, xóa nút gốc chỉ có 1 nút con bên phải
                        self.goc = nut_ht.phai
                    elif nut_ht.phai == None:
                        #xóa nút chỉ có 1 con bên trái
                        self.goc = nut_ht.trai
                    else:
                        #xóa nút gốc có đủ 2 con
                        #xoay trái
                        self.goc = nut_ht.phai
                        tam = self.goc
                        while tam.trai != None:
                            #truy tìm đến cực trái để gắn nhánh trái xuống bên trái của nút trái
                            tam = tam.trai
                        #while
                        tam.trai = nut_ht.trai
                    #if
                elif nut_ht.trai == None and nut_ht.phai == None:
                    #Không phải nút gốc, xóa nút lá, không có con trái và phải
                    if cha_con =='trai':
                        nut_cha.trai = None
                    else:
                        nut_cha.phai = None
                    #if
                elif nut_ht.trai == None:
                    #không phải nút lá mà là nút giữa
                    #xóa nút chỉ có 1 con bên phải
                    if cha_con == 'trai':
                        nut_cha.trai = nut_ht.phai
                    else:
                        nut_cha.phai = nut_ht.phai
                    #if
                elif nut_ht.phai == None:
                    #xóa nút giữa chỉ có 1 con bên trái
                    if cha_con =='trai':
                        nut_cha.trai = nut_ht.trai
                    else:
                        nut_cha.phai = nut_ht.trai
                    #if
                else:
                    #xóa nút có đủ 2 con
                    #xoay trái
                    if cha_con == 'trai':
                        nut_cha.trai = nut_ht.phai
                    else:
                        nut_cha.phai = nut_ht.phai
                    #if
                    if nut_ht.phai.trai == None:
                        nut_ht.phai.trai = nut_ht.trai
                    else: #nút chưa là None, truy tìm nút tận cùng bên trái
                        tam = nut_ht.phai
                        while tam.trai != None:
                            tam = tam.trai
                        #while
                        tam.trai = nut_ht.trai
                    #if
                #if
                del nut_ht
                break
            #if
        #while
            
    #duyệt trai nut phai
    def duyet_trai_nut_phai(self,goc=0):
        #duyệt LNR
        nut_ht = goc
        if goc == 0:
            nut_ht = self.goc
        #if
        #kiểm tra nút hiện tại có bằng None không
        if nut_ht == None:
            return []
        else: #cây có giá trị
            kq = []
            kq_trai = self.duyet_trai_nut_phai(nut_ht.trai)
            #duyệt trái
            for x in kq_trai:
                kq.append(x)
            #for duyệt trái
            kq.append(nut_ht.khoa)
            #duyệt phải
            kq_phai = self.duyet_trai_nut_phai(nut_ht.phai)
            for x in kq_phai:
                kq.append(x)
            #for
            return kq
        #if
    #def
        
    #duyệt trái phải nút
    def duyet_trai_phai_nut(self,goc = 0):
        #duyệt theo LRN
        nut_ht = goc
        if goc == 0:
            nut_ht = self.goc
        #if
        #kiểm tra nút hiện tại có bằng None không
        if nut_ht == None:
            return []
        else: #cây có giá trị
            kq = []
            kq_trai = self.duyet_trai_phai_nut(nut_ht.trai)
            #duyệt trái
            for x in kq_trai:
                kq.append(x)
            #for duyệt trái
            #duyệt phải
            kq_phai = self.duyet_trai_phai_nut(nut_ht.phai)
            for x in kq_phai:
                kq.append(x)
            #for duyệt phải
            kq.append(nut_ht.khoa)
            return kq
        #if
    #def
           

    #duyệt NLR
    def duyet_nut_trai_phai(self,goc=0):
        #Duyệt theo NLR
        nut_ht = goc
        if goc == 0:
            nut_ht = self.goc
        #if
        #kiểm tra nút hiện tại có bằng None không
        if nut_ht == None:
            return []
        else: # cây có giá trị
            kq = []
            kq.append(nut_ht.khoa)
            #duyệt trái
            kq_trai = self.duyet_nut_trai_phai(nut_ht.trai)
            for x in kq_trai:
                kq.append(x)
            #for duyệt trái
            
            #duyệt phải
            kq_phai = self.duyet_nut_trai_phai(nut_ht.phai)
            for x in kq_phai:
                kq.append(x)
            #for duyệt phải
            return kq
        #if
    #def
    
    #tìm 
    def tim(self,khoa):
        if self.goc == None:
        #cây rỗng
            return
        #if
        nut_ht = self.goc
        kq=''
        while (nut_ht != None and nut_ht.khoa != khoa):
            kq = kq+ f'{nut_ht.khoa} -> '
            if khoa <= nut_ht.khoa:
                nut_ht = nut_ht.trai
            else:
                nut_ht = nut_ht.phai
            #if
        #while
        if nut_ht == None: #tìm không thấy
            return None
        else: #tìm thấy
            kq = kq +f'{nut_ht.khoa}'
            return kq
        #if
    #def
    
    #tính tổng các nút
    def SumTree(self,goc=0):
        #duyệt theo LNR
        nut_ht = goc
        if goc == 0:
            nut_ht = self.goc
        #if
        #kiểm tra nút hiện tại có bằng None không
        if nut_ht == None:
            return 0
        else: #cây có giá trị
            tong = 0
            tong_trai = self.SumTree(nut_ht.trai)
            tong_phai = self.SumTree(nut_ht.phai)
            tong = tong + tong_trai + tong_phai + nut_ht.khoa
            return tong
        #if
    #def
        
    #tìm giá trị lớn nhất 
        
    def max(self,goc=0):
        #duyệt theo tính chất của cây nhị phân
        nut_ht = goc
        if goc == 0:
            nut_ht = self.goc

        if nut_ht == None:
            return 0
        else:
            kq = nut_ht.khoa
            kq_trai = self.max(nut_ht.trai)
            kq_phai = self.max(nut_ht.phai)
            if kq_trai > kq:
                kq = kq_trai
            if kq_phai > kq:
                kq = kq_phai
            return kq
        #if
    #def
    #tìm giá trị nhỏ nhất
    def min(self,goc=0):
        #duyệt theo tính chất của cây nhị phân
        nut_ht = goc
        if goc == 0:
            nut_ht = self.goc
        if nut_ht == None:
            return 0
        else:
            kq = nut_ht.khoa
            kq_trai = self.min(nut_ht.trai)
            kq_phai = self.min(nut_ht.phai)
            if kq_trai < kq:
                kq = kq_trai
            if kq_phai < kq:
                kq = kq_phai
            return kq
        #if
    #đếm số nút
        
    def CountNode(self,goc=0):
        #duyệt theo LNR
        nut_ht = goc
        if goc == 0:
            nut_ht = self.goc
        #if
        #kiểm tra nút hiện tại có bằng None không
        if nut_ht == None:
            return 0
        else:
            #cây có giá trị
            dem = 1
            dem_trai = self.CountNode(nut_ht.trai)
            dem_phai = self.CountNode(nut_ht.phai)
            dem = dem + dem_trai + dem_phai
            return dem
        #if
    #def
    #đếm số nút lá
    def CountLeaf(self,goc=0):
        #duyệt theo NLR
        nut_ht = goc
        if goc == 0:
            nut_ht = self.goc
        #if
        #kiểm tra nút hiện tại có bằng None không
        if nut_ht == None:
            return 0
        else:
            #cây có giá trị
            if nut_ht.trai == None and nut_ht.phai == None:
                return 1
            dem_trai = self.CountLeaf(nut_ht.trai)
            dem_phai = self.CountLeaf(nut_ht.phai)
            return dem_trai + dem_phai
        #if
    #def
#class

#hàm main
def main():
    SO_PHAN_TU = 10
    cay = CayNhiPhanTimKiem()
    print('**********Chèn các phần tử vào cây**********')
    tap_gia_tri = set()
    from random import randint
    while len(tap_gia_tri) < SO_PHAN_TU:
        gt = randint(1,100) #lấy 10 phần tử không trùng nhau nên dùng tập hợp
        tap_gia_tri.add(gt)
    #while
    #tap_gia_tri = list(tap_gia_tri) #phát sinh danh sách ngẫu nhiên
    tap_gia_tri = [66,46,84,11,81,99,36,77,83,100,86,85]
    print('Chèn lần lượt',tap_gia_tri)
    for x in tap_gia_tri:
        cay.chen(x)
    kq = cay.duyet_trai_nut_phai()
    print('**********Duyệt cây theo Trai - Nut - Phai (LNR): ',kq)

    kq = cay.duyet_nut_trai_phai()  
    print('**********Duyệt cây theo Nut - Trai - Phai (NLR): ',kq)

    kq = cay.duyet_trai_phai_nut()
    print('**********Duyệt cây theo Trai - Phai - Nut (LRN): ',kq)

    print('**********Xóa 1 phần tử có trong cây**********') 
    gt = int(input('Nhập vào giá trị cần xóa'))
    print(f'Xoa {gt}')
    cay.xoa(gt)

    kq = cay.duyet_trai_nut_phai()
    print('**********Duyệt cây theo Trai - Nut - Phai (LNR): ',kq)

    kq = cay.duyet_nut_trai_phai()
    print('**********Duyệt cây theo Nut - Trai - Phai (NLR): ',kq)

    kq = cay.duyet_trai_phai_nut()
    print('**********Duyệt cây theo Trai - Phai - Nut (LRN): ',kq)

    #tìm
    while True:
        nhap = input('Nhập vào khóa cần tìm: ')
        if nhap =='':
            break
        #if
        gt = int(nhap)
        kq = cay.tim(gt)
        if kq == None:
            print(f'Không tìm thấy {gt}')
            break
        else: #tìm thấy
            print(f'Tìm thấy {gt}:{kq}')
            break
    

        #if
    #while
    tong = cay.SumTree()
    print(f'Tổng các nút: {tong}')
    max = cay.max()
    print(f'Giá trị lớn nhất: {max}')
    min = cay.min()
    print(f'Giá trị nhỏ nhất: {min}')
    dem = cay.CountNode()
    print(f'Số nút: {dem}')
    dem = cay.CountLeaf()
    print(f'Số nút lá: {dem}')
    
#def 

if __name__ == '__main__':
    main()             




                   
                
    

