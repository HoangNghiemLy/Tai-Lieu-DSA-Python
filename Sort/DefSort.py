'''
Viết tất cả các hàm sắp xếp sau:
- Sắp xếp chọn (Selection sort)
- Sắp xếp nổi bọt (Bubble sort)
- Sắp xếp chèn (Insertion sort)
- Sắp xếp nhanh (Quick sort)
- Sắp xếp trộn (Merge sort)
- Sắp xếp vun đống (Heap sort)
- Sắp xếp nổi (Shell sort)

'''
class Sort:
    def interchangeSort(self,arr):
        n=len(arr)
        for i in range(n):
            for j in range(i+1,n,1):
                if arr[i] > arr[j]:
                    arr[i],arr[j] = arr[j],arr[i]
        return arr
    def bubbleSort(self,arr):
        n=len(arr)
        for i in range(n):
            for j in range(0,n-i-1,1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr
    def insertionSort(self,arr):
        n=len(arr)
        for i in range(n):
            x=arr[i]
            pos=i
            while pos>0 and x<arr[pos-1]:
                arr[pos]=arr[pos-1]
                pos=pos-1
            arr[pos]=x
        return arr
    def selectionSort(self,arr):
        n=len(arr)
        for i in range(0,n-1,1):
            min=i
            for j in range(i+1,n,1):
                if arr[j]<arr[min]:
                    min=j
            if min!=i:
                arr[i],arr[min]=arr[min],arr[i]
        return arr
    def quickSort(self,arr):
        def partition(arr,left,right):
            pivot=arr[right]
            i=left-1
            for j in range(left,right):
                if arr[j]<=pivot:
                    i+=1
                    arr[i],arr[j]=arr[j],arr[i]
            arr[i+1],arr[right]=arr[right],arr[i+1]
            return i+1
        def QuickSort(arr,left,right):
            if left<right:
                pi=partition(arr,left,right)
                QuickSort(arr,left,pi-1)
                QuickSort(arr,pi+1,right)
            return arr
        return QuickSort(arr,0,len(arr)-1)
    def heapSort(self,arr):
        def heapify(arr,n,i):
            largest=i
            left =2*i+1
            right=2*i+2
            if left<n and arr[i]<arr[left]:
                largest=left
            if right<n and arr[largest]<arr[right]:
                largest=right
            if largest!=i:
                arr[i],arr[largest]=arr[largest],arr[i]
                heapify(arr,n,largest)
        def heapSort(arr):
            n=len(arr)
            for i in range(n,-1,-1):
                heapify(arr,n,i)
            for i in range(n-1,0,-1):
                arr[i],arr[0]=arr[0],arr[i]
                heapify(arr,i,0)
            return arr
        return heapSort(arr)
    
    def mergeSort(self,arr):
        n=len(arr)
        if n>1:
            mid = n//2
            left_half=arr[:mid]
            right_half=arr[mid:]
            self.mergeSort(left_half)
            self.mergeSort(right_half)
            i=j=k=0
            while i<len(left_half) and j<len(right_half):
                if left_half[i]<right_half[j]:
                    arr[k]=left_half[i]
                    i+=1
                else:
                    arr[k]=right_half[j]
                    j+=1
                k+=1
            while i<len(left_half):
                arr[k]=left_half[i]
                i+=1
                k+=1
            while j<len(right_half):
                arr[k]=right_half[j]
                j+=1
                k+=1
        return arr
    def shellSort(self,arr):
        n=len(arr)
        gap=n//2
        while gap>0:
            for i in range(gap,n):
                temp=arr[i]
                j=i
                while j>=gap and arr[j-gap]>temp:
                    arr[j]=arr[j-gap]
                    j-=gap
                arr[j]=temp
            gap//=2
        return arr
    def display(arr):
        print(arr)







