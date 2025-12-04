def swap(arr, a, b):
    # En Python, puedes intercambiar valores de manera concisa
    arr[a], arr[b] = arr[b], arr[a]

def partition(arr, low, high):
    # Elegimos el último elemento como pivote
    pivot = arr[high]
    i = low - 1  # Índice del elemento más pequeño (y elemento al cual se hace el swap)

    for j in range(low, high):
        # Si el elemento actual es menor que el pivote
        if arr[j] < pivot:
            i += 1
            # Intercambia arr[i] y arr[j]
            swap(arr, i, j)

    # Intercambia el pivote con el elemento en la posición i + 1
    swap(arr, i + 1, high)
    return i + 1  # Nueva posición del pivote

def quick_sort(arr, low, high):
    """Implementación del algoritmo QuickSort."""
    if low < high:
        # pi es el índice de partición, arr[pi] está ahora en el lugar correcto
        pi = partition(arr, low, high)

        # Ordenar recursivamente los elementos antes y después de la partición
        quick_sort(arr, low, pi - 1)  # Sub-arreglo izquierda
        quick_sort(arr, pi + 1, high) # Sub-arreglo derecha

def print_array(arr):
    # En Python, simplemente imprimir la lista
    print(arr)

# -----------------
# Programa principal
# -----------------
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)

    print("Arreglo original:")
    print_array(arr)

    quick_sort(arr, 0, n - 1)

    print("Arreglo ordenado:")
    print_array(arr)
