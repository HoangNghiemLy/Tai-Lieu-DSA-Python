class Node:
    def __init__(self, key):
        self.key = key
        self.count = 1
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    
    if key == root.key:
        root.count += 1
    elif key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    
    return root

def buildFrequencyTree(text):
    root = None
    for char in text:
        if char.isalpha():
            char = char.lower()  # Chuyển tất cả các ký tự thành chữ thường
            root = insert(root, char)
    return root

def countOccurrences(root, key):
    if root is None:
        return 0
    
    if key == root.key:
        return root.count
    elif key < root.key:
        return countOccurrences(root.left, key)
    else:
        return countOccurrences(root.right, key)


def main():
    text = "Hoàng Nghiêm"
    print(f"Văn bản: {text}")
    frequency_tree = buildFrequencyTree(text)

    print("Cây thống kê số lần xuất hiện của các ký tự:")
    print("(Ký tự, Số lần xuất hiện)")
   
    for char in text:
        
        char_to_check = input("Nhập vào 1 ký tự để kiểm tra: ").lower()
        if char_to_check.isalpha():
            occurrences = countOccurrences(frequency_tree, char_to_check)
            if occurrences == 0:
                print(f"Ký tự '{char_to_check}' không xuất hiện trong văn bản.")
                break
            else:

                print(f"Số lần xuất hiện của ký tự '{char_to_check}' trong văn bản: {occurrences}")
        
        else:
            print("Ký tự không hợp lệ.")
            break

if __name__ == "__main__":
    main()
