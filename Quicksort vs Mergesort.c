#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

// Declaraciones de funciones
int compare(const void* a, const void* b);
void r_array(int *array, int n);
void merge(int arr[], int left, int mid, int right);
void mergesort(int arr[], int left, int right);

int main() {

    int base_size = 10000000;
   
    FILE *fptr_qs = fopen("runtime_qs.txt", "w");
    FILE *fptr_ms = fopen("runtime_ms.txt", "w");

    srand(time(NULL));

    // Bucle para generar y ordenar arrays de diferentes tamaños
    for (int i = 1; i <= 20; i++) {
        int size = base_size * i;

        // Asignación dinámica de memoria para los arrays
        int *numbers_qs = malloc(size * sizeof(int));
        int *numbers_ms = malloc(size * sizeof(int));

        if (numbers_qs == NULL || numbers_ms == NULL) {
            printf("Error alocando memoria");
            return 1;
        }

        // Encabezado para los archivos de salida
        fprintf(fptr_qs, "Runtime for list %d:\n", i);
        fprintf(fptr_ms, "Runtime for list %d:\n", i);

        // Bucle para realizar 5 ejecuciones por tamaño de array
        for (int j = 1; j <= 5; j++) {

            r_array(numbers_qs, size);
            r_array(numbers_ms, size);

            // Medición del tiempo para Quick Sort
            clock_t tic_qs = clock();
            qsort(numbers_qs, size, sizeof(int), compare);
            clock_t toc_qs = clock();

            // Medición del tiempo para Merge Sort
            clock_t tic_ms = clock();
            mergesort(numbers_ms, 0, size - 1);
            clock_t toc_ms = clock();

            // Escritura de los tiempos en los archivos
            fprintf(fptr_qs, "%f s - ", (double)(toc_qs - tic_qs) / CLOCKS_PER_SEC);
            fprintf(fptr_ms, "%f s - ", (double)(toc_ms - tic_ms) / CLOCKS_PER_SEC);
        }

        fprintf(fptr_qs, "\n");
        fprintf(fptr_ms, "\n");

        free(numbers_qs);
        free(numbers_ms);
    }

    fclose(fptr_qs);
    fclose(fptr_ms);

    return 0;
}

// Función de comparación para qsort
int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

// Función para generar un array con valores aleatorios
void r_array(int *array, int n) {
    for (int i = 0; i < n; i++) {
        array[i] = rand() % n;
    }
}

// Función para fusionar dos subarrays en Merge Sort
void merge(int arr[], int left, int mid, int right) {
    int i, j, k;
    int n1 = mid - left + 1;
    int n2 = right - mid;

    // Asignación de memoria para los subarrays
    int *L = malloc(n1 * sizeof(int));
    int *R = malloc(n2 * sizeof(int));

    // Copia de datos a los subarrays
    for (i = 0; i < n1; i++)
        L[i] = arr[left + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];

    // Fusión de los subarrays en el array original
    i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j])
            arr[k++] = L[i++];
        else
            arr[k++] = R[j++];
    }

    // Copia de los elementos restantes de L, si los hay
    while (i < n1) arr[k++] = L[i++];

    // Copia de los elementos restantes de R, si los hay
    while (j < n2) arr[k++] = R[j++];

    free(L);
    free(R);
}

// Función recursiva para Merge Sort
void mergesort(int arr[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergesort(arr, left, mid);
        mergesort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}
