import csv
import os
from collections import defaultdict

# Solicita al usuario ingresar la ruta del directorio donde se encuentran los archivos
directorio = input("Ingresa la ruta del directorio donde se encuentran los archivos: ")

# Verifica si el directorio existe
if not os.path.exists(directorio):
    print(f"El directorio '{directorio}' no existe.")
    exit()

# Inicializa un diccionario para almacenar los datos agrupados
datos_agrupados = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))

# Itera a través de los archivos en el directorio
for nombre_archivo in os.listdir(directorio):
    if not nombre_archivo.startswith(
        "MM1"
    ):  # Solo procesa archivos que comiencen con MM1
        print(f"Ignorando archivo: {nombre_archivo}")
        continue  # Ignora archivos que no sigan la convención de nomenclatura

    print(f"Procesando archivo: {nombre_archivo}")
    # Extrae información del nombre del archivo
    partes_nombre = nombre_archivo.split("-")
    total_cores = partes_nombre[-1].replace("core", "")  # Número total de núcleos
    tamaño = partes_nombre[1].replace("Size", "")  # Tamaño de la matriz

    # Lee el contenido del archivo y extrae los tiempos
    with open(os.path.join(directorio, nombre_archivo), "r") as archivo:
        for linea in archivo:
            partes = linea.strip().split(":")
            core = int(partes[0].strip())
            tiempo = int(partes[1].strip())
            datos_agrupados[total_cores][tamaño][core].append(tiempo)

# Calcula los promedios y prepara los datos para el CSV
datos_csv = []
for total_cores, matrices in datos_agrupados.items():
    for tamaño, cores in matrices.items():
        for core, tiempos in cores.items():
            promedio = sum(tiempos) / len(tiempos)
            datos_csv.append(
                {
                    "TotalCores": int(total_cores),
                    "MatrixSize": int(tamaño),
                    "SingleCore": core,
                    "Time": promedio,
                }
            )

# Ordena los datos por TotalCores, MatrixSize y SingleCore en orden ascendente
datos_csv.sort(key=lambda x: (x["TotalCores"], x["MatrixSize"], x["SingleCore"]))

# Ruta donde se guardará el archivo CSV
ruta_csv = os.path.join(directorio, "resultados.csv")

# Escribe los datos en un archivo CSV en la misma ruta
with open(ruta_csv, mode="w", newline="") as archivo_csv:
    campos = ["TotalCores", "MatrixSize", "SingleCore", "Time"]
    escritor_csv = csv.DictWriter(archivo_csv, fieldnames=campos)

    # Escribe el encabezado
    escritor_csv.writeheader()

    # Escribe las filas de datos
    for fila in datos_csv:
        escritor_csv.writerow(fila)

# Mensaje de confirmación al guardar los datos
print(f"Los datos se han guardado en '{ruta_csv}'.")
