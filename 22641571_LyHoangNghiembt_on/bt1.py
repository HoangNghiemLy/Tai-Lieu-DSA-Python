'''
Bài 1: Sử dụng cây nhị phân tìm kiếm để giải bài toán (thống kê) số lượng ký tự có trong văn bản (không dấu)
1.	Xây dựng cây cho biết nỗi ký tự có trong văn bản xuất hiện mấy lần
2.	Nhập vào 1 ký tự. Kiểm tra ký tự đó xuất hiện bao nhiêu lần trong văn bản
'''
import os
class Node:
    def __init__(self,key):
        self.key = key
        self.count = 1
        self.left = None
        self.right = None
def insert(root,key):
    if root is None:
        return Node(key)
    if key == root.key:
        root.count += 1
    elif key < root.key:
        root.left = insert(root.left,key)
    else:
        root.right = insert(root.right,key)
    return root
def buil_tree(text):
    root = None
    for char in text:
        if char.isalpha():
            char = char.lower()
            root = insert(root,char)
    return root
def count_char(root,key):
    if root is None:
        return 0
    if key == root.key:
        return root.count
    elif key < root.key:
        return count_char(root.left,key)
    else:
        return count_char(root.right,key)
while True:
    os.system('cls')
    print('1. Nhập văn bản')
    print('2. Thống kê số lần xuất hiện của ký tự')
    print('3. Thoát')
    choice = input('Chọn: ')
    if choice == "1":
        text = input('Nhập văn bản: ')
        root = buil_tree(text)
    elif choice == "2":
        key = input('Nhập ký tự cần thống kê: ')
        print(f'Số lần xuất hiện của ký tự {key} là: {count_char(root,key)}')
        input('Enter để tiếp tục...')
    elif choice == "3":
        print('Tạm biệt!')
        break
    else:
        print('Sai chức năng, vui lòng chọn lại!')

