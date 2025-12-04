#include <iostream>
using namespace std;

// Función que mezcla (merge) dos subarreglos ordenados:
// arr[l..m] y arr[m+1..r]
void merge(int arr[], int l, int m, int r) {
    int n1 = m - l + 1;  // tamaño del subarreglo izquierdo
    int n2 = r - m;      // tamaño del subarreglo derecho

    // arreglos temporales
    int* L = new int[n1];
    int* R = new int[n2];

    // copiar datos a L[] y R[]
    for (int i = 0; i < n1; i++)
        L[i] = arr[l + i];

    for (int j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];

    // mezclar los subarreglos L[] y R[] en arr[l..r]
    int i = 0;      // índice inicial de L[]
    int j = 0;      // índice inicial de R[]
    int k = l;      // índice inicial de arr[]

    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    // copiar los elementos restantes de L[], si hay
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    // copiar los elementos restantes de R[], si hay
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }

    // liberar memoria dinámica
    delete[] L;
    delete[] R;
}

// MergeSort recursivo
void mergeSort(int arr[], int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;  // punto medio

        // ordenar primera y segunda mitad
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);

        // mezclar las dos mitades ordenadas
        merge(arr, l, m, r);
    }
}

// Función para imprimir el arreglo
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++)
        cout << arr[i] << " ";
    cout << endl;
}

// Ejemplo de uso
int main() {
    int arr[] = {10, 7, 8, 9, 1, 5};
    int n = sizeof(arr) / sizeof(arr[0]);

    cout << "Arreglo original:" << endl;
    printArray(arr, n);

    mergeSort(arr, 0, n - 1);

    cout << "Arreglo ordenado:" << endl;
    printArray(arr, n);

    return 0;
