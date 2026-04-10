#include <stdlib.h>
#include <stdio.h>
#include <omp.h>    // Incluye la biblioteca OpenMP para la programación paralela.
#include "sample.h" // Incluye las definiciones de las funciones de muestreo.

#ifndef MIN
#define MIN(x, y) ((x) < (y) ? (x) : (y)) // Define una macro para calcular el mínimo entre dos valores.
#endif

#define DATA_SZ (1024 * 1024 * 64 * 3) // Define el tamaño del búfer de memoria (192 MB).

static double MEM_CHUNK[DATA_SZ]; // Crea un búfer estático de gran tamaño para almacenar datos.

// Función para inicializar matrices.
void Matrix_Init_col(int SZ, double *a, double *b, double *c)
{
    int j, k;
    // Inicializa cada elemento de las matrices 'a', 'b', y 'c'.
    for (k = 0; k < SZ; k++)
    {
        for (j = 0; j < SZ; j++)
        {
            a[j + k * SZ] = 2.0 * (j + k); // Inicializa 'a' con valores basados en índices.
            b[j + k * SZ] = 3.2 * (j - k); // Inicializa 'b' de manera similar.
            c[j + k * SZ] = 0.0;           // Inicializa 'c' a cero.
        }
    }
}

int main(int argc, char **argv)
{
    int N;

    // Verifica los argumentos de entrada y obtiene el tamaño de la matriz.
    if (argc < 2)
    {
        printf("MM1c MatrixSize [Sample arguments ...]\n");
        exit(EXIT_FAILURE);
    }

    N = (int)atof(argv[1]); // Convierte el argumento a entero para el tamaño de la matriz.

    if (N > 1024 * 10)
    {
        printf("Invalid MatrixSize\n");
        exit(EXIT_FAILURE);
    }

    Sample_Init(argc, argv); // Inicializa las funciones de muestreo.

#pragma omp parallel
    {
        int i, j, k; // Variables de bucle.
        int NTHR, THR, SZ = N;
        double *a, *b, *c;

        // Asignación de segmentos del búfer de memoria a cada matriz.
        a = MEM_CHUNK;
        b = a + SZ * SZ;
        c = b + SZ * SZ;

        // El hilo maestro inicializa las matrices.
#pragma omp master
        {
            Matrix_Init_col(SZ, a, b, c);
        }

        // Espera a que todos los hilos alcancen este punto antes de continuar.
#pragma omp barrier

        THR = Sample_PAR_install(); // Obtiene el número del hilo actual.
        Sample_Start(THR);          // Comienza el muestreo para el hilo.

        // Multiplicación de matrices realizada en paralelo.
#pragma omp for private(i, j, k)
        for (i = 0; i < SZ; i++)
        {
            for (j = 0; j < SZ; j++)
            {
                double *pA = a + (i * SZ);
                double *pB = b + j;
                for (k = 0; k < SZ; k++, pA++, pB += SZ)
                {
                    c[i * SZ + j] += *pA * *pB; // Calcula el producto y acumula en 'c'.
                }
            }
        }

        Sample_Stop(THR); // Detiene el muestreo para el hilo.
    }

    Sample_End(); // Finaliza el proceso de muestreo y muestra los resultados.
    return EXIT_SUCCESS;
}
