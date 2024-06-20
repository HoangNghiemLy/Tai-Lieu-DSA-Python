#Tìm tuyến tính (Linear Search)
print("1. Tìm kiếm tuyến tính")
def linear_search(a,x):
    #Duyệt qua từng phần tử của danh sách a
    for i in range(len(a)):
        #So sánh phần tử đang xét với giá trị cần tìm kiếm x
        if a[i]==x:
            #Trả về vị trí của phần tử tìm thấy
            return i
        #nếu duyệt qua toàn bộ danh sách mà không tìm thấy giá trị cần tìm kiếm,
        #Trả về giá trị không tìm thấy
    return -1

a=[10,30,20,45,67,32,15,90,86,120]
print(a)
print("Nhập giá trị cần tìm: ")
x=int(input())
kq = linear_search(a,x)
if kq == -1:
    print("Không tìm thấy giá trị",x)
else:
    print("Giá trị",x,"được tìm thấy tại vị trí",kq)
print()

#Tìm kiếm nhị phân (Binary Search)
print("2. Tìm kiếm nhị phân")
def binary_search(a,x):
    #Sắp xếp mảng a
    a.sort()
    #Tìm kiếm nhị phân
    left = 0
    right = len(a)-1
    while left <= right:
        mid = (left+right)//2
        if x == a[mid]:
            return mid
        elif x < a[mid]:
            right = mid - 1
        else:
            left = mid + 1
    #Kiểm tra
a=[10,30,20,45,67,32,15,90,86,120]
print(a)
print("Nhập giá trị cần tìm: ")
x=int(input())
kq = binary_search(a,x)
if kq == -1:
    print("Không tìm thấy giá trị",x)
else:
    print("Giá trị",x,"được tìm thấy tại vị trí",kq)
