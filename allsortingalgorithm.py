def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Given list
arr = [2, 29, 31, 6, 13]

# Sorting using different algorithms
print("Original List:", arr)
print("Sorted with Insertion Sort:", insertion_sort(arr.copy()))
print("Sorted with Selection Sort:", selection_sort(arr.copy()))
print("Sorted with Bubble Sort:", bubble_sort(arr.copy()))

# Selection Sort Correctness Argument
print("\nSelection Sort Correctness Argument:")
print("Selection Sort works by repeatedly finding the smallest element in the unsorted portion")
print("and swapping it with the current position. Since it always moves the smallest remaining")
print("element into its correct place, and never disturbs sorted elements, it is guaranteed to")
print("produce a sorted array in O(n^2) time complexity.")
