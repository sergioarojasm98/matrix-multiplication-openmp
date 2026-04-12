import pandas as pd
import os


# Función para encontrar y analizar las métricas óptimas de rendimiento computacional
# (tiempo, speedup y eficiencia) para diferentes tamaños de matrices de un conjunto de datos.
def mejores_metricas(directorio, archivo_csv):
    # Carga los datos desde un archivo CSV ubicado en 'directorio' con el nombre 'archivo_csv'.
    datos = pd.read_csv(os.path.join(directorio, archivo_csv))

    # Filtra los datos para considerar solo aquellos registros donde el número total de núcleos es mayor a 1.
    datos_multiples_cores = datos[datos["TotalCores"] > 1]

    # Encuentra el mejor tiempo (mínimo) de ejecución para cada tamaño de matriz.
    mejor_tiempo = datos.loc[datos.groupby("MatrixSize")["Time"].idxmin()][
        ["MatrixSize", "Time", "TotalCores"]
    ]
    mejor_tiempo.rename(
        columns={"Time": "Mejor Tiempo", "TotalCores": "Núcleos para Mejor Tiempo"},
        inplace=True,
    )

    # Encuentra el mejor speedup (máximo) para cada tamaño de matriz, excluyendo casos de un solo núcleo.
    mejor_speedup = datos_multiples_cores.loc[
        datos_multiples_cores.groupby("MatrixSize")["Speedup"].idxmax()
    ][["MatrixSize", "Speedup", "TotalCores"]]
    mejor_speedup.rename(
        columns={
            "Speedup": "Mejor Speedup",
            "TotalCores": "Núcleos para Mejor Speedup",
        },
        inplace=True,
    )

    # Encuentra la mejor eficiencia (máxima) para cada tamaño de matriz, también excluyendo casos de un solo núcleo.
    mejor_eficiencia = datos_multiples_cores.loc[
        datos_multiples_cores.groupby("MatrixSize")["Eficiencia"].idxmax()
    ][["MatrixSize", "Eficiencia", "TotalCores"]]
    mejor_eficiencia.rename(
        columns={
            "Eficiencia": "Mejor Eficiencia",
            "TotalCores": "Núcleos para Mejor Eficiencia",
        },
        inplace=True,
    )

    # Combina los dataframes de mejor tiempo, speedup y eficiencia en un solo dataframe para facilitar la comparación.
    resultados_combinados = pd.merge(mejor_tiempo, mejor_speedup, on="MatrixSize")
    resultados_combinados = pd.merge(
        resultados_combinados, mejor_eficiencia, on="MatrixSize"
    )

    # Guarda los resultados combinados en un nuevo archivo CSV dentro del mismo directorio.
    resultados_combinados.to_csv(
        os.path.join(directorio, "mejores_metricas.csv"), index=False
    )

    # Muestra los resultados combinados en la consola para una revisión rápida.
    print(resultados_combinados)


# Solicita al usuario ingresar la ruta del directorio donde se encuentran los archivos CSV con los datos.
directorio = input(
    "Por favor, ingresa la ruta del directorio donde se encuentran los archivos: "
)
archivo_csv = "resultados_con_metricas.csv"

# Ejecuta la función principales con los parámetros especificados para analizar las métricas.
mejores_metricas(directorio, archivo_csv)
