def merge(arr, l, m, r):
    """
    Mezcla dos sublistas ordenadas: arr[l..m] y arr[m+1..r].
    """
    n1 = m - l + 1  # Tamaño del sub-arreglo izquierdo
    n2 = r - m      # Tamaño del sub-arreglo derecho

    # 1. Crear sublistas temporales (L y R)
    # En Python, se usa slicing para copiar los elementos
    L = arr[l : l + n1]
    R = arr[m + 1 : m + 1 + n2]

    # 2. Inicializar índices
    i = 0     # Índice inicial de L[]
    j = 0     # Índice inicial de R[]
    k = l     # Índice inicial de arr[] (donde comienza la fusión)

    # 3. Mezclar los sub-arreglos de vuelta en arr[l..r]
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # 4. Copiar los elementos restantes de L[], si hay
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # 5. Copiar los elementos restantes de R[], si hay
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
    
    # Nota: No es necesario 'delete[]' en Python, ya que la recolección
    # de basura se encarga automáticamente de liberar la memoria de L y R.

def merge_sort(arr, l, r):
    """
    Implementación principal recursiva del Merge Sort.
    Ordena el rango arr[l..r].
    """
    if l < r:
        # Encuentra el punto medio para dividir el array
        # Se usa una sintaxis similar a C++ para evitar overflow en números muy grandes,
        # aunque en Python el simple (l + r) // 2 es seguro.
        m = l + (r - l) // 2

        # 1. Ordenar la primera mitad
        merge_sort(arr, l, m)
        # 2. Ordenar la segunda mitad
        merge_sort(arr, m + 1, r)

        # 3. Mezclar las dos mitades
        merge(arr, l, m, r)

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

    merge_sort(arr, 0, n - 1)

    print("Arreglo ordenado:")
    print_array(arr)
