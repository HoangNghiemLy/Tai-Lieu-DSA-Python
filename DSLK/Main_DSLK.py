from DSLK.DSLK import *
def main():
    ds = DSLienKet()
    ds.in_ds()

    #a - thêm
    print('a: Thêm -----------------')
    so = int(input('Nhập số cần thêm: '))
    print(f'Them {so}')
    ds.them(so)
    ds.in_ds()

    so = int(input('Nhập số cần thêm: '))
    print(f'Them {so}')
    ds.them(so)
    ds.in_ds()
    

    #b - chen
    print('b: Chèn -----------------')
    chi_muc = 2
    so = 15
    print(f'Chèn {so} vào vị trí {chi_muc}')
    ds.chen(chi_muc,so)
    ds.in_ds()


    so = 10
    chi_muc = 0
    print(f'Chèn {so} vào vị trí {chi_muc}')
    ds.chen(chi_muc,so)
    ds.in_ds()

    #c - tim
    print('c: Tìm -----------------')
    so = 10
    print(f'Tìm {so}')
    vi_tri = ds.tim(so)
    print(f'Vị trí {so} là {vi_tri}')
    so = 20
    print(f'Tìm {so}')
    vi_tri = ds.tim(so)
    print(f'Vị trí {so} là {vi_tri}')





    #d - xoa
    print('d: Xóa -----------------')
    so = 15
    print(f'Xóa {so}')
    ds.xoa(so)
    ds.in_ds()



    #e - cap nhat
    print('e: Cập nhật -----------------')
    vi_tri = 2
    so = 20
    print(f'Cập nhật giá trị tại vị trí {vi_tri} thành {so}')
    ds.cap_nhat(vi_tri,so)
    ds.in_ds()





    #f - xoa het 
    print('f: Xóa hết -----------------')
    ds.xoa_het()
    ds.in_ds()


#def 
if __name__ == '__main__':
    main()

