'''
Cài đặt menu chương trình cài đặt các thuật toán sắp xếp
cho người dùng nhập số lượng phần tử của mảng
sau đó nhập các phần tử của mảng
sau đó hiển thị menu cho người dùng lựa chọn

'''
from DefSort import Sort
arr=[]

menu_options ={
    
    1: "Interchange sort",
    2: "Bubble Sort",
    3: "Insertion Sort",
    4: "Selection Sort",
    5: "Quick Sort",
    6: "Heap Sort",
    7: "Merge Sort",
    8: "Shell Sort",
    'Others': "Thoát chương trình",
}
def print_menu():
    for key in menu_options.keys():
        print(key,'--',menu_options[key])
while(True):
    arr=[]
    print_menu()
    chon = ''
    try:
        chon = int(input("Nhập tùy chọn: "))
    except:
        print("Nhập sai định dạng, hãy nhập lại..")
    if chon == 1:
        #1 - Interchange sort
        n=int(input("Nhập số lượng phần tử của mảng: "))
        for i in range(n):
            x=int(input("Nhập phần tử thứ "+str(i+1)+": "))
            arr.append(x)
        print("Mảng ban đầu: ",arr)
        
        s=Sort()
        print("Mảng sau khi sắp xếp: ",s.interchangeSort(arr))
        print()
    elif chon == 2:
        #2 - Bubble Sort
        n=int(input("Nhập số lượng phần tử của mảng: "))
        for i in range(n):
            x=int(input("Nhập phần tử thứ "+str(i+1)+": "))
            arr.append(x)
        print("Mảng ban đầu: ",arr)
        s=Sort()
        print("Mảng sau khi sắp xếp: ",s.bubbleSort(arr))
        
    elif chon == 3:
        #3 - Insertion Sort
        n=int(input("Nhập số lượng phần tử của mảng: "))
        for i in range(n):
            x=int(input("Nhập phần tử thứ "+str(i+1)+": "))
            arr.append(x)
        print("Mảng ban đầu: ",arr)
        s=Sort()
        print("Mảng sau khi sắp xếp: ",s.insertionSort(arr))
        print()
    elif chon == 4:
        #4 - Selection Sort
        n=int(input("Nhập số lượng phần tử của mảng: "))
        for i in range(n):
            x=int(input("Nhập phần tử thứ "+str(i+1)+": "))
            arr.append(x)
        print("Mảng ban đầu: ",arr)
        s=Sort()
        print("Mảng sau khi sắp xếp: ",s.selectionSort(arr))
        print()
    elif chon == 5:
        #5 - Quick Sort
        n=int(input("Nhập số lượng phần tử của mảng: "))
        for i in range(n):
            x=int(input("Nhập phần tử thứ "+str(i+1)+": "))
            arr.append(x)
        print("Mảng ban đầu: ",arr)
        s=Sort()
        print("Mảng sau khi sắp xếp: ",s.quickSort(arr))
        print()
    elif chon == 6:
        #6 - Heap Sort
        n=int(input("Nhập số lượng phần tử của mảng: "))
        for i in range(n):
            x=int(input("Nhập phần tử thứ "+str(i+1)+": "))
            arr.append(x)
        print("Mảng ban đầu: ",arr)
        s =Sort()
        print("Mảng sau khi sắp xếp: ",s.heapSort(arr))
        print()
    elif chon == 7:
        #7 - Merge Sort
        n=int(input("Nhập số lượng phần tử của mảng: "))
        for i in range(n):
            x=int(input("Nhập phần tử thứ "+str(i+1)+": "))
            arr.append(x)
        print("Mảng ban đầu: ",arr)
        s =Sort()
        print("Mảng sau khi sắp xếp: ", s.mergeSort(arr))
        print()
    elif chon == 8:
        #8 - Shell Sort
        n=int(input("Nhập số lượng phần tử của mảng: "))
        for i in range(n):
            x=int(input("Nhập phần tử thứ "+str(i+1)+": "))
            arr.append(x)
        print("Mảng ban đầu: ",arr)
        s=Sort()
        print("Mảng sau khi sắp xếp: ",s.shellSort(arr))
        print()
    else:
        print("Thoát chương trình")
        break



