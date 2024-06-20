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

def buildSearchTree(arr):
    root = None
    for num in arr:
        root = insert(root, num)
    return root

def countDistinctValues(root):
    if root is None:
        return 0
    return 1 + countDistinctValues(root.left) + countDistinctValues(root.right)

def countElementsForDistinctValues(root):
    if root is None:
        return
    countElementsForDistinctValues(root.left)
    print(f"Giá trị: {root.key}, Số lượng: {root.count}")
    countElementsForDistinctValues(root.right)

# Ví dụ sử dụng
if __name__ == "__main__":
    arr = [4, 2, 6, 8, 2, 4, 6, 4, 2, 8, 4, 6, 4]
    print("Dãy số:", arr)
    search_tree = buildSearchTree(arr)

    distinct_values_count = countDistinctValues(search_tree)
    print("Số lượng giá trị phân biệt trong dãy số:", distinct_values_count)

    print("Số lượng phần tử cho mỗi giá trị phân biệt:")
    countElementsForDistinctValues(search_tree)
