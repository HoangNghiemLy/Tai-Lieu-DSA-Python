import os
class Node:
    def __init__(self, masv, hoten, malop, diemtb):
        self.masv = masv
        self.hoten = hoten
        self.malop = malop
        self.diemtb = diemtb
        self.left = None
        self.right = None

class Temp:
    def __init__(self):
        self.root = None
  
    def insert(self, masv, hoten, malop, diemtb):
        if self.root is None:
            self.root = Node(masv, hoten, malop, diemtb)
        else:
            self._insert_recursively(self.root, masv, hoten, malop, diemtb)
    #
    def _insert_recursively(self, node, masv, hoten, malop, diemtb):
        if masv == node.masv:
            print("MASV trùng. Vui lòng nhập lại MASV khác.")
            return
        elif masv < node.masv:
            if node.left is None:
                node.left = Node(masv, hoten, malop, diemtb)
            else:
                self._insert_recursively(node.left, masv, hoten, malop, diemtb)
        else:
            if node.right is None:
                node.right = Node(masv, hoten, malop, diemtb)
            else:
                self._insert_recursively(node.right, masv, hoten, malop, diemtb)

    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print("MASV:", node.masv)
            print("Ho ten:", node.hoten)
            print("Ma lop:", node.malop)
            print("Diem TB:", node.diemtb)
            print()
            self.inorder_traversal(node.right)

    def search(self, masv):
        return self._search_recursively(self.root, masv)

    def _search_recursively(self, node, masv):
        if node is None:
            return None
        elif masv == node.masv:
            return node
        elif masv < node.masv:
            return self._search_recursively(node.left, masv)
        else:
            return self._search_recursively(node.right, masv)


def print_menu():
    print("1. Them sinh vien: MASV, Ho ten, Ma lop, Diem TB")
    print("2. Duyệt và xuất dữ liệu theo thứ tự LNR")
    print("3. Tìm kiếm sinh viên theo MASV")
    print("4. Thoát")

def main():
    tmp = Temp()

    while True:
        os.system("cls")
        print("\n== MENU ==")
        print_menu()
        choice = input("Chọn chức năng: ")

        if choice == "1":
            masv = int(input("Nhập MASV: "))
            hoten = input("Nhập họ tên: ")
            malop = input("Nhập mã lớp: ")
            diemtb = float(input("Nhập điểm trung bình: "))
            if masv <= 0:
                print("Mã sinh viên phải lớn hơn 0!!!")
            else:
                tmp.insert(masv, hoten, malop, diemtb)
            os.system("pause")
        elif choice == "2":
            print("Danh sách sinh viên:")
            tmp.inorder_traversal(tmp.root)
            os.system("pause")
        elif choice == "3":
            search_masv = int(input("Nhập MASV cần tìm: "))
            result = tmp.search(search_masv)
            if result:
                print("Thông tin sinh viên:")
                print("MASV:", result.masv)
                print("Ho ten:", result.hoten)
                print("Ma lop:", result.malop)
                print("Diem TB:", result.diemtb)
            else:
                print("Không có sinh viên có MASV này.")
            os.system("pause")
        elif choice == "4":
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
            os.system("pause")

if __name__ == "__main__":
    main()
