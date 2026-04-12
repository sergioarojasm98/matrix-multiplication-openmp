#include <stdlib.h>
#include <omp.h> // Incluye OpenMP para programación paralela.
#include <string.h>
#include <errno.h>
#include <sys/time.h> // Incluye funciones para medir el tiempo.
#include <stdio.h>

#define MAX_THREADS 40 // Define el número máximo de hilos permitidos.

struct timeval start[MAX_THREADS]; // Arrays para almacenar el tiempo de inicio de cada hilo.
struct timeval stop[MAX_THREADS];  // Arrays para almacenar el tiempo de finalización de cada hilo.

static int N_THREADS; // Variable para almacenar el número actual de hilos.

// Función para marcar el inicio de una medición de tiempo en un hilo.
void Sample_Start(int THR)
{
#pragma omp barrier                     // Barrera para sincronizar todos los hilos.
  gettimeofday(start + THR, (void *)0); // Registra el tiempo de inicio para el hilo THR.
}

// Función para marcar el fin de una medición de tiempo en un hilo.
void Sample_Stop(int THR)
{
  gettimeofday(&(stop[THR]), (void *)0); // Registra el tiempo de finalización para el hilo THR.
}

// Función para inicializar la configuración del muestreo, incluyendo el número de hilos.
void Sample_Init(int argc, char *argv[])
{
  if (argc < 3)
  {
    printf("Sample parameters: NumberThreads \n");
    exit(1); // Sale si no se proporcionan suficientes argumentos.
  }

  N_THREADS = (int)atof(argv[1]); // Convierte el argumento en el número de hilos.

  // Verifica que el número de hilos sea válido.
  if (!N_THREADS || N_THREADS > MAX_THREADS)
  {
    printf("Number of Threads is not valid\n");
    exit(1);
  }

  omp_set_num_threads(N_THREADS); // Establece el número de hilos para OpenMP.
}

// Función para asignar un identificador de hilo (THR) a cada hilo.
int Sample_PAR_install()
{
  int THR = omp_get_thread_num(); // Obtiene el número del hilo actual.
  return THR;
}

// Función para finalizar el muestreo y mostrar los resultados.
void Sample_End()
{
  int THR, i;
  // Recorre todos los hilos registrados.
  for (THR = 0; THR < N_THREADS; THR++)
  {
    printf(" %1.0f:  ", (double)THR); // Muestra el número del hilo.
    // Calcula el tiempo total que tomó el hilo.
    stop[THR].tv_usec -= start[THR].tv_usec;
    if (stop[THR].tv_usec < 0)
    {
      stop[THR].tv_usec += 1000000;
      stop[THR].tv_sec--;
    }
    stop[THR].tv_sec -= start[THR].tv_sec;

    // Muestra el tiempo total en microsegundos.
    printf("%9.0f\n", (double)(stop[THR].tv_sec * 1000000 + stop[THR].tv_usec));
  }
}
