import time
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Generate a random array of integers
arr = [random.randint(0, 1000) for _ in range(1000)]

# Measure the time taken by Bubble Sort
start_time = time.time()
bubble_sort(arr.copy())
end_time = time.time()
print(f"Bubble Sort took {end_time - start_time:.6f} seconds")

# Measure the time taken by QuickSort
start_time = time.time()
sorted_arr = quick_sort(arr.copy())
end_time = time.time()
print(f"QuickSort took {end_time - start_time:.6f} seconds")
