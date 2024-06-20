#Viết chương trình để chuyển đổi biểu thức có dạng trung tố sang 
#dạng hậu tố.
#Cho toi code chương trình trên

# Path: Stack/BaiTap3.py
# Compare this snippet from Stack/__pycache__/BaiTap1.py:
# #Cho một STACK đang chứa các phần tử sau: A, B, C, E, F. Biểu diễn STACK và viết lệnh tương ứng bằng
# #ngôn ngữ lập trình Python để thực hiện các thao tác sau:

class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def show(self):
        print(self.items)

s = Stack()
s.push('A')
s.push('B')
s.push('C')
s.push('E')
s.push('F')
s.show()
s.pop()
#Viết chương trình để chuyển đổi biểu thức có dạng trung tố sang
#dạng hậu tố.

#Cho toi code chương trình trên

# Path: Stack/BaiTap4.py





