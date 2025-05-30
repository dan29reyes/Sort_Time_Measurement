import random
import time

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def quick_sort_recursivo(arr):
    if len(arr) <= 1:
        return arr

    n = len(arr)
    pivot = arr[n // 2] 

    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    return quick_sort_recursivo(less) + equal + quick_sort_recursivo(greater)

def merge_sort_recursivo(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort_recursivo(left_half)
    right_half = merge_sort_recursivo(right_half)

    sorted_arr = []
    i = j = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            sorted_arr.append(left_half[i])
            i += 1
        else:
            sorted_arr.append(right_half[j])
            j += 1

    sorted_arr.extend(left_half[i:])
    sorted_arr.extend(right_half[j:])

    return sorted_arr

def InsertionSort(arr):
    print("InsertionSort")
    start_time = time.time()
    
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    return {"sorted_array": arr, "elapsed_time": elapsed_time}

def HeapSort(arr):
    print("HeapSort")
    start_time = time.time()
    n = len(arr)

    if n <= 1:
        end_time = time.time()
        elapsed_time = end_time - start_time
        return {"sorted_array": arr, "elapsed_time": elapsed_time}

    start_index_for_build = (n // 2) - 1
    
    for i in range(start_index_for_build, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    end_time = time.time()
    elapsed_time = end_time - start_time
    
    return {"sorted_array": arr, "elapsed_time": elapsed_time}
    
def QuickSort(arr):
    print("QuickSort")
    start_time = time.time()
    
    sorted_arr = quick_sort_recursivo(arr)
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    return {"sorted_array": sorted_arr, "elapsed_time": elapsed_time}
    
def MergeSort(arr):
    print("MergeSort")
    start_time = time.time()
    
    sorted_arr = merge_sort_recursivo(arr)
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    return {"sorted_array": sorted_arr, "elapsed_time": elapsed_time}
    
def SelectionSort(arr):
    print("SelectionSort")
    start_time = time.time()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    return {"sorted_array": arr, "elapsed_time": elapsed_time}

def BubbleSort(arr):
    print("BubbleSort")
    start_time = time.time()
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    return {"sorted_array": arr, "elapsed_time": elapsed_time}

def main():
    print("** Implementacion de Sorts **")
    
    while True:
        try:
            n = int(input("Ingrese el tamaño del arreglo: "))
            if n >= 0:
                break
            else:
                print("Por favor, ingrese un número no negativo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

    arr = [random.randint(1, 1000) for _ in range(n)]
    
    print("\n** Menus **")
    print("1. InsertionSort")
    print("2. HeapSort")
    print("3. QuickSort")
    print("4. MergeSort")
    print("5. SelectionSort")
    print("6. BubbleSort")

    while True:
        try:
            opcion = int(input("Ingrese el método a utilizar: "))
            if 1 <= opcion <= 6:
                break
            else:
                print("Opción inválida. Por favor, ingrese un número entre 1 y 6.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

    array_to_sort = arr[:] 
    
    print(f"\nArreglo original (primeros 20 elementos): {arr[:20]}{'...' if len(arr) > 20 else ''}")

    result = {}
    if opcion == 1:
        result = InsertionSort(array_to_sort)
    elif opcion == 2:
        result = HeapSort(array_to_sort)
    elif opcion == 3:
        result = QuickSort(array_to_sort)
    elif opcion == 4: 
        result = MergeSort(array_to_sort)
    elif opcion == 5:
        result = SelectionSort(array_to_sort)
    elif opcion == 6:
        result = BubbleSort(array_to_sort)
    
    print("\n!! Arreglo ordenado !!")
    print(f"Arreglo ordenado (primeros 20 elementos): {result['sorted_array'][:20]}{'...' if len(result['sorted_array']) > 20 else ''}")
    print(f"Tiempo de ejecución: {result['elapsed_time']:.6f} segundos")
    
if __name__ == "__main__":
    main()