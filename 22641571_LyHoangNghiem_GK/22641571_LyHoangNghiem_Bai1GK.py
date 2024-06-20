import random
import time

def generate_array(n, filename):
    arr = [random.randint(1, 1000) for _ in range(n)]
    with open(filename, 'w') as f:
        f.write(' '.join(map(str, arr)))

def interchange_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            comparisons += 1
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1
    return comparisons, swaps

def bubble_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    return comparisons, swaps

def insertion_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        comparisons += 1
        while j >= 0 and key < arr[j]:
            comparisons += 1
            arr[j + 1] = arr[j]
            swaps += 1
            j -= 1
        arr[j + 1] = key
    return comparisons, swaps

def selection_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        swaps += 1
    return comparisons, swaps

def quick_sort(arr):
    comparisons = 0
    swaps = 0
    def partition(arr, low, high):
        nonlocal comparisons, swaps
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            comparisons += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        swaps += 1
        return i + 1
    
    def quick_sort_recursive(arr, low, high):
        nonlocal comparisons, swaps
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_recursive(arr, low, pi - 1)
            quick_sort_recursive(arr, pi + 1, high)
    
    start_time = time.time()
    quick_sort_recursive(arr, 0, len(arr) - 1)
    quick_time = (time.time() - start_time) * 1000  
    return comparisons, swaps, quick_time


filename = 'mang1.int'
generate_array(40000, filename)

with open(filename, 'r') as f:
    arr = list(map(int, f.read().split()))

start_time = time.time()
comp_interchange, swaps_interchange = interchange_sort(arr.copy())
interchange_time = (time.time() - start_time) * 1000 

start_time = time.time()
comp_bubble, swaps_bubble = bubble_sort(arr.copy())
bubble_time = (time.time() - start_time) * 1000  

start_time = time.time()
comp_insertion, swaps_insertion = insertion_sort(arr.copy())
insertion_time = (time.time() - start_time) * 1000  

start_time = time.time()
comp_selection, swaps_selection = selection_sort(arr.copy())
selection_time = (time.time() - start_time) * 1000  

comp_quick, swaps_quick, quick_time = quick_sort(arr.copy())


print("Do phuc tap cua thuat toan")
print("Ph")
print(f"1. (Interchange sort)\t{interchange_time:.2f}\t{comp_interchange}\t{swaps_interchange}")
print(f"2. (Bubble sort)\t{bubble_time:.2f}\t{comp_bubble}\t{swaps_bubble}")
print(f"3. (Insertion sort)\t{insertion_time:.2f}\t{comp_insertion}\t{swaps_insertion}")
print(f"4. (Selection sort)\t{selection_time:.2f}\t{comp_selection}\t{swaps_selection}")
print(f"5. (Quick sort)\t{quick_time:.2f}\t{comp_quick}\t{swaps_quick}")

