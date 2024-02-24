import time


start_time = time.time()

import numpy as np

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = np.random.randint(1, 100, size=100)
print("Original array:", arr)

start_sort_time = time.time()
insertion_sort(arr)
end_sort_time = time.time()

swaps =insertion_sort(arr)
print("Sorted array:", arr)
sort_time_taken = end_sort_time - start_sort_time
print("Time taken for sorting:", sort_time_taken, "seconds")
end_total_time = time.time()
total_time_taken = end_total_time - start_time
print("Total time taken (including setup):", total_time_taken, "seconds")
