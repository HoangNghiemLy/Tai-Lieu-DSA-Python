'''
Bài 2: Sử dụng cây nhị phân tìm kiếm để giải bài toán:
1.	Đếm có bao nhiêu giá trị phân biệt trong dãy số cho trước 
2.	Với mỗi giá trị phân biệt, cho biết số lượng phần tử
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
def build_tree(arr):
    root = None
    for key in arr:
        root = insert(root,key)
    return root
def count_distinct(root):
    if root is None:
        return 0
    return 1 + count_distinct(root.left) + count_distinct(root.right)
def count_element(root,key):
    if root is None:
        return 0
    if key == root.key:
        return root.count
    elif key < root.key:
        return count_element(root.left,key)
    else:
        return count_element(root.right,key)
while True:
    os.system('cls')
    print('1. Nhập dãy số')
    print('2. Đếm số giá trị phân biệt')
    print('3. Đếm số lần xuất hiện của giá trị')
    print('4. Thoát')
    choice = input('Chọn: ')
    if choice == "1":
        arr = list(map(int,input('Nhập dãy số: ').split()))
        root = build_tree(arr)
    elif choice == "2":
        print(f'Số giá trị phân biệt là: {count_distinct(root)}')
        input('Enter để tiếp tục...')
    elif choice == "3":
        key = int(input('Nhập giá trị cần thống kê: '))
        print(f'Số lần xuất hiện của giá trị {key} là: {count_element(root,key)}')
        input('Enter để tiếp tục...')
    elif choice == "4":
        print('Tạm biệt!')
        break
    else:
        print('Sai chức năng, vui lòng chọn lại!')
        