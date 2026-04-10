# Paralelización de Multiplicación de Matrices con OpenMP

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![C](https://img.shields.io/badge/C-blue.svg?style=for-the-badge)]()
[![OpenMP](https://img.shields.io/badge/OpenMP-darkgreen.svg?style=for-the-badge)]()
[![Status](https://img.shields.io/badge/status-archived-lightgrey?style=for-the-badge)]()
[![Academic](https://img.shields.io/badge/academic-Javeriana-purple?style=for-the-badge)]()

Este repositorio contiene el código y la documentación de un proyecto de investigación enfocado en la multiplicación de matrices en el contexto de la computación de alto rendimiento. Se evalúan dos métodos de multiplicación de matrices, el tradicional de filas por columnas y uno alternativo de filas por filas, implementados y paralelizados con OpenMP. Los experimentos se realizaron en matrices de tamaño variable, desde 100x100 hasta 1000x1000, en sistemas con 10, 20 y 40 núcleos, buscando entender cómo la paralelización afecta el rendimiento y eficiencia en diferentes arquitecturas de hardware.

Este análisis detallado presenta comparaciones basadas en métricas como el speedup y la eficiencia, ofreciendo insights sobre la escalabilidad y las ventajas de distintas estrategias de paralelización aplicadas a la multiplicación de matrices, una operación crítica en numerosas aplicaciones de la ciencia y la ingeniería. Explora el código, los resultados de los benchmarks y las conclusiones para una comprensión profunda de la paralelización de una de las operaciones más fundamentales en el ámbito del cálculo numérico.

## Pasos para ejecutar un experimento: e.g. FxC-EXP-Rendimiento@Cratos

1. Ve a la carpeta `FxC-EXP-Rendimiento@Cratos > MatMult` y ejecuta el siguiente comando para compilar el programa `MM1c` usando el `Makefile` y guardarlo en `FxC-EXP-Rendimiento@Cratos > BIN`:
```console
make all
```

2. Asegurate que el script `lanzador.pl` y el archivo binario `MM1c` sea ejecutable (si aún no lo es) con el siguiente comando:
```console
chmod +x /FxC-EXP-Rendimiento@Cratos/TOOL/lanzador.pl && \
chmod +x /FxC-EXP-Rendimiento@Cratos/BIN/MM1c
```
3. Ve a la carpeta `FxC-EXP-Rendimiento@Cratos > TOOL` y ejecuta el lanzador con el siguiente comando:
```console
./lanzador.pl 30
```
4. Con esto, el script `lanzador.pl` ejecutará el programa `MM1c` 30 veces para cada combinación de tamaño de vector y número de cores especificados en el script.
```perl
...
@cores = (1..10); # Puedes modificar el rango de cores/hilos a usar
@VectorSize = ("100", "200", "300", "400", "500", "600", "700", "800", "900", "1000");
...
```
6. Los resultados de la ejecución se almacenarán en el directorio `FxC-EXP-Rendimiento@Cratos > Soluciones`.
7. Utiliza los siguientes scripts de python para obtener los resultados en CSV y los graficos vectorizados en formato PDF.
- **hpc_results.py:** Crea un compendio de los resultados de todos los experimentos en la carpeta `/Soluciones` y los guarda en `resultados.csv`.
- **hpc_metrics.py:** Toma el compendio de `resultados.csv` y calcula las metricas de speedup y eficiencia.
- **hpc_plots.py:** Grafica los resultados y metricas obtenidas en `hpc_metrics.py`.
- **hpc_best.py:** Imprime los mejores resultados de cada metrica para cada tamaño de matriz.


## Wiki

### Como funciona `MM1x.c`

Este código implementa una multiplicación de matrices utilizando programación paralela con OpenMP. Incluye la inicialización de matrices en el hilo maestro y luego realiza la multiplicación de las matrices en paralelo, utilizando cada hilo para trabajar en una parte de la matriz. Utiliza las funciones definidas en sample.h y Otime.c para medir y registrar el rendimiento de cada hilo durante la operación, ofreciendo una visión detallada del tiempo de ejecución de cada parte del proceso paralelizado. La barrera de OpenMP asegura que todos los hilos comiencen la multiplicación solo después de que las matrices estén completamente inicializadas.

### Como funciona `Otime.c`

Este código es parte de una implementación que mide el rendimiento de los hilos en un entorno de programación paralela con OpenMP. Utiliza estructuras timeval para registrar el tiempo de inicio y finalización de operaciones en cada hilo. La finalidad principal es medir el tiempo que tardan los hilos en ejecutar secciones específicas del código, lo cual es crucial para la optimización y el análisis del rendimiento en aplicaciones paralelas. Las funciones proporcionan un marco para iniciar y detener el muestreo, configurar el número de hilos y mostrar los resultados de los tiempos de ejecución al finalizar el programa.

### Como funciona `lanzador.pl`

Este script en Perl está diseñado para automatizar la ejecución de experimentos computacionales, específicamente para diferentes configuraciones de un programa. Acepta un argumento que define el número de repeticiones de cada experimento y luego itera sobre una serie de configuraciones predefinidas, incluyendo el tamaño del vector y el número de cores. Para cada configuración, ejecuta el programa correspondiente varias veces y guarda los resultados en un archivo. El script también incluye una función de utilidad para informar al usuario sobre el uso correcto en caso de que los argumentos de entrada no sean proporcionados adecuadamente.



## Author

[Sergio Rojas](https://github.com/sergioarojasm98) — Pontificia Universidad Javeriana.

## Status

This repository is **archived** as an academic artifact. Forks are welcome.
