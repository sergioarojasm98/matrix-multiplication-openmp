# matrix-multiplication-openmp

Parallel matrix multiplication with OpenMP, comparing sequential vs parallel performance across multiple hardware configurations.

## About

This project evaluates two matrix multiplication methods -- row-by-column and row-by-row -- parallelized with OpenMP on systems with 10, 20, and 40 cores. Matrices range from 100x100 to 1,000x1,000, and each configuration is repeated multiple times to produce statistically meaningful speedup and efficiency metrics. Built for the High-Performance Computing (HPC) course in the Electronics Engineering / MSc program at Pontificia Universidad Javeriana, Bogota.

The repository includes C source kernels with per-thread timing instrumentation, Perl launcher scripts for batch execution, Python scripts for result aggregation and plotting, and over 1,400 raw benchmark output files. A final report PDF (`InformeFinal_OpenMP_HPC.pdf`) documents the findings.

## Stack

| Component | Detail |
|---|---|
| Kernel language | C with OpenMP |
| Timing | `Otime.c` / `sample.h` (per-thread `gettimeofday`) |
| Batch launcher | Perl (`lanzador.pl`) |
| Analysis | Python (`hpc_results.py`, `hpc_metrics.py`, `hpc_plots.py`, `hpc_best.py`) |
| Build | Makefile per experiment directory |
| Matrix sizes | 100x100 to 1,000x1,000 |
| Platforms | MacBook, Sistemas cluster, Cratos server |

## How to Build / Run

```bash
# Compile
cd FxC-EXP-Rendimiento@Cratos/MatMult
make all

# Run batch experiment (30 repetitions)
cd ../TOOL
chmod +x lanzador.pl
perl lanzador.pl 30

# Analyze results
cd ../../Data-Analytics-Scripts
python hpc_results.py
python hpc_metrics.py
python hpc_plots.py
```

> **Note:** Paths in the launcher scripts are hardcoded to the original system. Adjust them to your local checkout before running.

## License

MIT
