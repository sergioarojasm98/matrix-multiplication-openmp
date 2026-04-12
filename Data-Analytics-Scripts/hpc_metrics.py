import csv
import os
from collections import defaultdict


# Función para calcular métricas de rendimiento computacional a partir de datos de tiempos de ejecución.
# Esta función calcula el promedio de tiempos, speedup y eficiencia para diferentes configuraciones de núcleos y tamaños de matriz.
def calcular_metricas(tiempos_base, datos):
    resultados_con_metricas = []
    for matrix_size, datos_cores in datos.items():
        for cores, tiempos in datos_cores.items():
            # Calcula el tiempo promedio para una configuración específica de tamaño de matriz y número de núcleos.
            promedio = sum(tiempos) / len(tiempos)

            # Calcula el speedup como la relación entre el tiempo base (1 núcleo) y el tiempo promedio actual.
            speedup = tiempos_base[matrix_size] / promedio

            # Calcula la eficiencia como el speedup dividido por el número de núcleos.
            eficiencia = speedup / int(cores)

            # Almacena los resultados en una lista para su posterior procesamiento.
            resultados_con_metricas.append(
                {
                    "TotalCores": cores,
                    "MatrixSize": matrix_size,
                    "Time": promedio,
                    "Speedup": speedup,
                    "Eficiencia": eficiencia,
                }
            )
    return resultados_con_metricas


# Pide al usuario ingresar la ruta del directorio donde se encuentran los archivos de datos.
directorio = input("Ingresa la ruta del directorio donde se encuentran los archivos: ")

# Verifica si el directorio ingresado existe, de lo contrario termina el programa.
if not os.path.exists(directorio):
    print(f"El directorio '{directorio}' no existe.")
    exit()

# Prepara estructuras de datos para almacenar y organizar los tiempos de ejecución.
tiempos_base = {}
datos_agrupados = defaultdict(lambda: defaultdict(list))

# Lee los datos de un archivo CSV, organizándolos por tamaño de matriz y número de núcleos.
with open(os.path.join(directorio, "resultados.csv"), mode="r") as archivo_base:
    lector_csv = csv.DictReader(archivo_base)
    for fila in lector_csv:
        cores = fila["TotalCores"]
        matrix_size = fila["MatrixSize"]
        tiempo = float(fila["Time"])
        datos_agrupados[matrix_size][cores].append(tiempo)
        if cores == "1":
            tiempos_base[
                matrix_size
            ] = tiempo  # Guarda el tiempo de referencia para 1 núcleo.

# Llama a la función para calcular las métricas de rendimiento.
resultados_con_metricas = calcular_metricas(tiempos_base, datos_agrupados)

# Ordena los resultados para facilitar su análisis y comparación.
resultados_con_metricas.sort(key=lambda x: (int(x["TotalCores"]), int(x["MatrixSize"])))

# Define la ruta para guardar el nuevo archivo CSV con los resultados.
ruta_csv = os.path.join(directorio, "resultados_con_metricas.csv")

# Guarda los resultados en un archivo CSV en la ruta especificada.
with open(ruta_csv, mode="w", newline="") as archivo_csv:
    campos = ["TotalCores", "MatrixSize", "Time", "Speedup", "Eficiencia"]
    escritor_csv = csv.DictWriter(archivo_csv, fieldnames=campos)
    escritor_csv.writeheader()  # Escribe el encabezado del CSV.
    for fila in resultados_con_metricas:
        escritor_csv.writerow(fila)  # Escribe cada fila de datos en el archivo CSV.

# Informa al usuario que los datos han sido guardados correctamente.
print(f"Los datos con métricas se han guardado en '{ruta_csv}'.")
