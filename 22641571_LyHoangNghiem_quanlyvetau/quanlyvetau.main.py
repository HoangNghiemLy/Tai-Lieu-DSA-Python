import HeThongVeTau as ht
import KhachHangMuaVe as kh
import os
menu_options={
    1:"Thêm một khách hàng mới vào hàng đợi mua vé.",
    2:"Tìm kiếm khách hàng đợi vé bằng cmnd",
    3:"Bán một vé cho khách hàng. Chỉ bán cho người đăng ký trước.",
    4:"Hiển thị danh sách khách hàng đang chờ mua vé.",
    5:"Hủy một khách hàng ra khỏi danh sách (khách hàng không mua vé nữa).",
    6:"Thống kê tình hình bán vé.",
    7:"Hiển thị danh sách các ga đang chờ mua vé ",
    8:"Số vé tương ứng cho ga đang chờ mua vé.",
    9:"Lưu dữ liệu vào file",
    10:"Đọc dữ liệu từ file",
    11:"Sửa thông tin khách hàng",
    'Others': "Thoát chương trình",
}
def print_menu():
    for key in menu_options.keys():
        print(key,'--',menu_options[key])

hq=ht.HeThongVeTau()
hq.them("082245789813", "Lương Ánh Huyền","TP - Hồ Chí Minh",150000)
hq.them("912301393922", "Nguyễn Thị Nam","Nha Trang",200000)
hq.them("321321332133", "Lê Xuân Bình","Đà Lạt",300000)

while(True):
    os.system("cls")
    print_menu()
    chon=''
    try:
        chon=int(input("Xin mời nhập tùy chọn: "))
    except:
        print("Nhập sai định dạng, hãy nhập lại...")
    if chon==1:
        cmnd=input("\nNhập số CMND: ")
        ten=input("Nhập tên khách hàng: ")
        gaden=input("Nhập ga đến: ")
        giave=float(input("Nhập giá vé: "))
        hq.them(cmnd, ten, gaden , giave)

        
    elif chon==2:
        cmnd=input("\nNhập số CMND: ")
        o= hq.timKiem(cmnd)
        if o!=None:
            print("\nKhách hàng tìm thấy: ", o.hienthi())
        else:
            print("\nKhông tìm thấy khách hàng này...")
        input("Nhập enter để tiếp tục")

    elif chon==3:
        a= hq.banve()
        if a != None:
            print("\nĐã bán vé cho khách hàng: ", a.hienthi())
        else:
            print("\nKhông có khách hàng nào đang chờ mua vé...")
        input("Nhấn enter để tiếp tục")
    elif chon==4:
        tmp = hq.hienthidanhsachkh()
        print("\nDanh sách khách hàng đang chờ mua vé: "+str(len(tmp)))
        for i in range(len(tmp)):
            print("\nKhách hàng thứ "+str(i+1)+": ")
            print(tmp[i].hienthi())
        input("Nhấn enter để tiếp tục!!!")
    elif chon==5:
        cmnd=input("\nNhập số CMND: ")
        if hq.huykhachhang(cmnd):
            print("\nĐã hủy khách hàng có số CMND: ",cmnd)
        else:
            print("\nKhông tìm thấy khách hàng này...")
        input("Nhấn enter để tiếp tục")
    elif chon==6:
        print("\nTổng số khách hàng đang chờ mua vé: ",hq.thongke()[0])
        print("Tổng số khách hàng đã mua vé: ",hq.thongke()[1])
        print("Tổng số tiền đã thu được: ",hq.thongke()[2])
        input("Nhấn enter để tiếp tục")
    elif chon==7:
        print("\nDanh sách các ga đang chờ mua vé: ")
        for gaden in hq.hienthidsgadangchomuave():
            print(gaden)
        input("Nhấn enter để tiếp tục!")
    elif chon==8:
        gaden=input("\nNhập ga đến: ")
        print("Số vé tương ứng cho ga đang chờ mua vé: ",hq.sovetuongung(gaden))
        input("NHẤN ENTER ĐỂ TIẾP TỤC!!!")
    elif chon==9:
        fr = open('dskhachhang.txt',mode='w',encoding='UTF-8')
        for item in hq.dskh:
            fr.write(f"CMND: {item.cmnd} - Họ tên: {item.ten} - Ga đến: {item.Gaden} - Giá vé: {item.Giave}\n")
        fr.close()
        print("Đã lưu dữ liệu vào file dskhachhang.txt")
        input("Nhấn enter để tiếp tục")
    elif chon==10:
        fr = open('dskhachhang.txt',mode='r',encoding='UTF-8')
        print(fr.read())
        fr.close()
        input("Nhấn enter để tiếp tục")    
    elif chon==11:
        cmnd=input("\nNhập số CMND cần sửa: ")
        c = hq.timKiem(cmnd)
        if c!=None:
            ten=input("Nhập tên khách hàng: ")
            gaden=input("Nhập ga đến: ")
            giave=float(input("Nhập giá vé: "))
            hq.sua(cmnd, ten, gaden , giave)
            print("Đã sửa thông tin khách hàng có số CMND: ",cmnd)
        else:
            print("\nKhông tìm thấy khách hàng này...")
        input("Nhấn enter để tiếp tục")
    else:
        print("Cảm ơn quý khách đã sử dụng dịch vụ của chúng tôi...")
        break
