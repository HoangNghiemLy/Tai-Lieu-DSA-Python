'''
Quản lý khách hàng xếp hàng mua vé tại nhà ga. Thông tin lưu trữ cho khách hàng gồm: 
số CMND (String), tên khách hàng, ga đến, giá tiền (double).  
Tạo hệ thống menu gồm các mục: 
o Thêm một khách hàng mới vào hàng đợi mua vé. 
o Bán một vé cho khách hàng. Chỉ bán cho người đăng ký trước. 
o Hiển thị danh sách khách hàng. 
o Hủy một khách hàng ra khỏi danh sách (khách hàng không mua vé nữa). 
o Thống kê tình hình bán vé. 
o Hiển thị danh sách các ga đang chờ mua vé. 
o Hiển thị danh sách các ga đang chờ mua vé và số vé tương ứng cho ga. 
Lưu ý:  o Số khách hàng trong danh sách hiện tại là số khách đang chờ, nhưng chưa có vé. Khi một khách hàng đã mua vé, thì loại khách hàng này ra khỏi danh sách chờ mua vé. 
o Việc mua vé phải có thứ tự: ai vào trước thì mua vé trước (FIFO). 
o Mỗi khi khách hàng mua được vé phải lưu lại khách hàng này để dùng cho việc thống kê. 
o Mỗi khi thêm một khác hàng mới, nếu số CMND khách hàng đã có thì không tạo phần tử mới mà chỉ cập nhật lại ga và giá tiền đến cho khác hàng đó.  
o Mục thống kê tình hình: cho biết còn bao nhiêu khách hàng chờ nhận vé, bao nhiêu khách hàng đã nhận vé, tổng số tiền đã thu về là bao nhiêu
o Khi hiển thị danh sách các ga đến đang chờ mua vé, chỉ hiển thị tên ga đó một lần. (Ví dụ: giả sử 10 khách hàng nhưng đăng ký đi đến 2 ga, thì chỉ hiển thị 2 hàng).
'''
import json
class KhachHang:
    def __init__(self,cmnd,ten,gaden,giave) :
        self.cmnd=cmnd
        self.ten=ten
        self.Gaden=gaden
        self.Giave=giave

    def hienthi(self):
        return "CMND: "+self.cmnd+"\nHọ và tên: " + self.ten +"\nGa Đến: " + self.Gaden  +"\nGiá vé: " + str(self.Giave)
    


 