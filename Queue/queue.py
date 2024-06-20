'''
-Queue là một danh sách mà các đối tượng được thêm vào ở một đầu của danh sách
và lấy ra ở một đầu kia của danh sách. 
-Việc thêm một đối tượng luôn diễn ra ở cuối Queue và việc lấy ra một đối tượng luôn diễn ra ở đầu Queue
-Queue theo cơ chế FIFO (First In First Out) nghĩa là đối tượng nào được thêm vào trước thì sẽ được lấy ra trước

Queue hỗ trợ 2 thao tác chính:
-AddQueue(): thêm một đối tượng vào cuối (rear) Queue
-RemoveQueue9(): Lấy một đối tượng ở đàu (front) Queue
Queue còn hỗ trợ các thao tác:
-isEmpty(): kiểm tra xem Queue có rỗng không
-front(): Trả về giá trị phần tử nẳm ở đầu Queue mà không hủy nó. Nếu Queue rỗng thì trả về None

Các phép cơ bản trên hàng đợi:
-Create_Queue(): Tạo một hàng đợi rỗng
-Front(): hàm trả về phần tử đầu tiên của hàng Q
-EnQueue(): hàm thêm một phần tử x vào cuối hàng Q
-DeQueue(): hàm xóa phần tử đầu tiên của hàng Q
-IsEmpty(): hàm kiểm tra hàng Q có rỗng không
-IsFull(): hàm kiểm tra hàng Q có đầy không
-Size(): hàm trả về số phần tử của hàng Q
-Delete_Queue(): hàm xóa hàng Q
-Print_Queue(): hàm in hàng Q

Hai cách hiện thực:
-Khi lấy ra một phần tử ra thì đồng thời dời các ô phía sau nó lên một vị trí:


size(Q): if (r>= f) return r-f; else return (max - f) + (r+1)

'''