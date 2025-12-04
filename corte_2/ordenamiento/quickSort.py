def partition(arr, low, high):
    """
    Función de partición: toma el último elemento como pivote,
    coloca el pivote en su posición correcta en el array ordenado,
    y coloca todos los elementos más pequeños a su izquierda
    y todos los elementos más grandes a su derecha.
    """
    # Elegimos el último elemento como pivote
    pivot = arr[high]
    i = low - 1  # Índice del elemento más pequeño

    for j in range(low, high):
        # Si el elemento actual es menor que el pivote
        if arr[j] < pivot:
            i += 1
            # Intercambia arr[i] y arr[j] (swap)
            arr[i], arr[j] = arr[j], arr[i]

    # Intercambia el pivote (arr[high]) con el elemento en la posición i + 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # Nueva posición del pivote

def quick_sort(arr, low, high):
    """
    Implementación principal del algoritmo QuickSort.
    Ordena el array arr[low...high]
    """
    if low < high:
        # pi es el índice de partición
        pi = partition(arr, low, high)
        
        # Ordenar recursivamente los sub-arreglos
        quick_sort(arr, low, pi - 1)  # Sub-arreglo izquierda
        quick_sort(arr, pi + 1, high) # Sub-arreglo derecha

def print_array(arr):
    """Función para imprimir la lista."""
    print(arr)

# -----------------
# Programa principal (equivalente a main en C++)
# -----------------
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)

    print("Arreglo original:")
    print_array(arr)

    quick_sort(arr, 0, n - 1)

    print("Arreglo ordenado:")
    print_array(arr)
