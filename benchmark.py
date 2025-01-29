import time
import platform
import psutil
import numpy as np
import matplotlib.pyplot as plt


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


def benchmark_sorting_algorithms():
    sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
    algorithms = {'Insertion Sort': insertion_sort, 'Selection Sort': selection_sort, 'Bubble Sort': bubble_sort}
    results = {alg: [] for alg in algorithms}

    for size in sizes:
        test_data = np.random.randint(0, 10000, size)

        for name, sort_func in algorithms.items():
            arr = test_data.copy()
            start_time = time.time()
            sort_func(arr)
            end_time = time.time()
            results[name].append(end_time - start_time)

    plt.figure(figsize=(10, 6))
    for name, times in results.items():
        plt.plot(sizes, times, marker='o', label=name)

    plt.xlabel('Input Size (n)')
    plt.ylabel('Time (seconds)')
    plt.title('Sorting Algorithm Benchmark')
    plt.legend()
    plt.grid()
    plt.show()


def system_info():
    print("System Information:")
    print(f"Processor: {platform.processor()}")
    print(f"CPU Cores: {psutil.cpu_count(logical=False)}")
    print(f"Logical CPUs: {psutil.cpu_count(logical=True)}")
    print(f"RAM: {round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB")


if __name__ == "__main__":
    system_info()
    benchmark_sorting_algorithms()

    # Selection Sort Correctness Argument
   # print("\nSelection Sort Correctness Argument:")
   # print("Selection Sort works by repeatedly finding the smallest element in the unsorted portion ")
   # print("and swapping it with the current position. Since it always moves the smallest remaining ")
   # print("element into its correct place, and never disturbs sorted elements, it is guaranteed to ")
   # print("produce a sorted array in O(n^2) time complexity.")
