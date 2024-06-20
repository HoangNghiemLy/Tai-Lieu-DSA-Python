import time
from DefSort import Sort
arr=list(range(50000,0,-1))
dem = 0
s=Sort()
n = len(arr)
while True:
    #menu 
    print("1. Interchange Sort")
    print("2. Bubble Sort")
    print("3. Insertion Sort")
    print("4. Selection Sort")
    print("5. Quick Sort")
    print("6. Exit")
    chon = int(input("Chọn: "))

    if chon == 1:
        for i in range(n):
            print("21312341234")
        start_time = time.time()
        sorted_arr = Sort().interchangeSort(arr)
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000  # Đổi ra mili giây
        print("Thời gian thực thi: ",execution_time)
        
    elif chon == 2:
        for i in range(n):
            print("21312")
        start_time = time.time()
        sorted_arr = Sort().bubbleSort(arr)
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000
        print("Thời gian thực thi: ",execution_time)
        
    elif chon == 3:
        for i in range(n):
            print("213")
        start_time = time.time()
        sorted_arr = Sort().insertionSort(arr)
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000
        print("Thời gian thực thi: ",execution_time)
        
    elif chon == 4:
        for i in range(n):
            print("21312341234")
        start_time = time.time()
        sorted_arr = Sort().selectionSort(arr)
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000
        print("Thời gian thực thi: ",execution_time)
        
    elif chon == 5:
        for i in range(n):
            print("2131")
        start_time = time.time()
        sorted_arr = Sort().quickSort(arr)
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000
        print("Thời gian thực thi: ",execution_time)
        
    elif chon == 6:
        break
    else:
        print("Nhập sai, hãy nhập lại..")
        continue
    print("Nhấn phím bất kỳ để tiếp tục..")
print("Kết thúc chương trình")




