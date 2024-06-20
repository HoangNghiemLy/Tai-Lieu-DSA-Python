###Ngăn xếp - Stack 
'''
-Stack là một danh sách mà các đối tượng được thêm vào và lấy ra chỉ ở một đầu của danh sách. 
-Các phần tử được đưa vào và lấy ra trong ngăn xếp theo nguyên tắc "vào sau ra trước" cà cấu
 trúc dữ liệu này còn được gọi là cấu trúc LIFO (Last In - First Out - Vào sau ra trước).
-Stack hỗ trợ 2 thao tác chính:
s.push(x): thêm 1 đối tượng vào Stack Push(x,S)
s.pop(): lấy 1 đối tượng ra khỏi Stack Pop(S)
-Stack cũng hỗ trợ một số thao tác khác:
s.is_empty(s): kiểm tra xem Stack có rỗng không Empty(s)
s.Top(): trả về giá trị của phần tử nằm ở đầu Stack mà ko hủy nó khỏi Stack. Nếu Stack rỗng thì 
sẽ xảy ra Top(s)
len(s): trả về số phần tử trong Stack
s.Create_Stack(): tạo ngăn xếp rỗng CreateStack(s)

Có 2 kiểu cài đặt: Mảng một chiều và danh sách liên kết

Các hàm cần cài đặt:
Init (stack &s): khởi tạo Stack
isEmpty(stack s): kiểm tra xem Stack có rỗng không
Push(x, stack &s): thêm 1 phần tử vào Stack
Pop(stack &s): lấy 1 phần tử ra khỏi Stack
Top(stack s): trả về giá trị của phần tử nằm ở đầu Stack mà ko hủy nó khỏi Stack
CreateStack(stack &s): tạo ngăn xếp rỗng

'''
class ArrayStack:
    
    def __init__ (self):
        self.data = []
     
    def is_empty(self):
        return len(self.data) == 0
    def push(self, e):
    #add element a to the top of the stack
        self.data.append(e)
    def pop(self):
    #remove and return the element from the top of the Stack
    #Raise empty excepty if the Stack is empty
        if self.is_empty():
            raise ArrayStack('Stack is empty')
        return self.data.pop()
    def top(self):
    #return the element at the top of the stack
    #Raise empty exception if the stack is empty
        if self.is_empty():
            raise ArrayStack('Stack is empty')
        return self.data[-1] #the last in the list 
    #đổi về kiểu chuỗi
    def __str__(self):
        return ''.join(str(self.data))+'->'
    
    def len(self):
        return len(self.data)
    

