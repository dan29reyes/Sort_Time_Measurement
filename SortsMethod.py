import random
import time

def InsertionSort(arr):
    print("InsertionSort") 
    elapsed_time = 0
    start_time = time.time()
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Tiempo de ejecución: ", elapsed_time, " segundos")

def HeapSort(arr):
    print("HeapSort")
    elapsed_time = 0
    start_time = time.time()
    
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Tiempo de ejecución: ", elapsed_time, " segundos")
    
def QuickSort(arr):
    print("QuickSort")
    elapsed_time = 0
    start_time = time.time()
    n = len(arr)
    if n <= 1:
        return arr
    pivot = arr[n // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    sorted_arr = QuickSort(left) + middle + QuickSort(right)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Tiempo de ejecución: ", elapsed_time, " segundos")
    return sorted_arr
    
def MergeSort(arr):
    print("MergeSort")
    elapsed_time = 0
    start_time = time.time()
    n = len(arr)
    mid = n // 2
    left_half = MergeSort(arr[:mid])
    right_half = MergeSort(arr[mid:])
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
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Tiempo de ejecución: ", elapsed_time, " segundos")
    return sorted_arr
    
def SelectionSort(arr):
    print("SelectionSort")
    elapsed_time = 0
    start_time = time.time()
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Tiempo de ejecución: ", elapsed_time, " segundos")
    return arr

def BubbleSort(arr):
    print("BubbleSort")
    elapsed_time = 0
    start_time = time.time()
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Tiempo de ejecución: ", elapsed_time, " segundos")
    return arr

def main():
    print("** Implementacion de Sorts **")
    arr = []
    arreglo = []
    
    # llenar el arreglo con valores random segun el tamano ingresado
    n = int(input("Ingrese el tamaño del arreglo: "))
    for i in range(n):
        arr.append(random.randint(1, 1000))
    
    print("** Menus **\n1.InsertionSort\n2.HeapSort\n3.QuickSort\n4.MergeSort\n5.SelectionSort\n6.BubbleSort")
    opcion = int(input("Ingrese el metodo a utilizar: "))
    if opcion == 1:
        arreglo = InsertionSort(arr)
    elif opcion == 2:
        arreglo = HeapSort(arr)
    elif opcion == 3:
        arreglo = QuickSort(arr)
    elif opcion == 4: 
        arreglo = MergeSort(arr)
    elif opcion == 5:
        arreglo = SelectionSort(arr)
    elif opcion == 6:
        arreglo = BubbleSort(arr)

    print("!! Arreglo ordenado !!")
    print(arreglo)
    
if __name__ == "__main__":
    main()