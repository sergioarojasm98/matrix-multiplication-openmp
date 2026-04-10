#include <stdlib.h>
#include <omp.h>
#include <string.h>
#include <errno.h>
#include <sys/time.h>
#include <stdio.h>

#define MAX_THREADS 40

struct timeval start[MAX_THREADS];
struct timeval stop[MAX_THREADS];

static int N_THREADS;

void Sample_Start(int THR)
{
#pragma omp barrier
  gettimeofday(start + THR, (void *)0);
}

void Sample_Stop(int THR)
{
  gettimeofday(&(stop[THR]), (void *)0);
}

void Sample_Init(int argc, char *argv[])
{

  // int MAX_THREADS = omp_get_num_procs();

  if (argc < 3)
  {
    printf("Sample parameters: NumberThreads \n");
    exit(1);
  }

  N_THREADS = (int)atof(argv[1]);

  if (!N_THREADS || N_THREADS > MAX_THREADS)
  {
    printf("Number of Threads is not valid\n");
    exit(1);
  }

  omp_set_num_threads(N_THREADS);
}

int Sample_PAR_install()
{
  int THR;

  THR = omp_get_thread_num();

  return THR;
}

void Sample_End()
{
  int THR, i;

  for (THR = 0; THR < N_THREADS; THR++)
  {
    printf(" %1.0f:  ", (double)THR);
    stop[THR].tv_usec -= start[THR].tv_usec;
    if (stop[THR].tv_usec < 0)
    {
      stop[THR].tv_usec += 1000000;
      stop[THR].tv_sec--;
      // printf("\n");
    }
    stop[THR].tv_sec -= start[THR].tv_sec;

    printf("%9.0f\n", (double)(stop[THR].tv_sec * 1000000 + stop[THR].tv_usec));
  }
}
