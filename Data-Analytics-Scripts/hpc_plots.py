import matplotlib.pyplot as plt
import pandas as pd
import os


# Función para generar gráficos a partir de datos de rendimiento computacional.
def generar_graficas(directorio, archivo_csv, prefijo):
    datos = pd.read_csv(os.path.join(directorio, archivo_csv))
    datos_filtrados = datos[datos["TotalCores"] > 1]  # Filtra para TotalCores > 1

    # Gráfico de Speedup vs. TotalCores
    plt.figure(figsize=(10, 7))
    for size in sorted(datos_filtrados["MatrixSize"].unique()):
        subset = datos_filtrados[datos_filtrados["MatrixSize"] == size]
        plt.plot(
            subset["TotalCores"], subset["Speedup"], marker="o", label=f"Tamaño {size}"
        )
    plt.xlabel("Total de Núcleos")
    plt.ylabel("Speedup")
    plt.title("Speedup vs. Total de Núcleos")
    plt.legend()
    plt.savefig(
        os.path.join(directorio, f"{prefijo}Speedup_vs_TotalCores.pdf"), format="pdf"
    )

    # Gráfico de Eficiencia vs. TotalCores
    plt.figure(figsize=(10, 8))
    for size in sorted(datos_filtrados["MatrixSize"].unique()):
        subset = datos_filtrados[datos_filtrados["MatrixSize"] == size]
        plt.plot(
            subset["TotalCores"],
            subset["Eficiencia"],
            marker="o",
            label=f"Tamaño {size}",
        )
    plt.xlabel("Total de Núcleos")
    plt.ylabel("Eficiencia")
    plt.title("Eficiencia vs. Total de Núcleos")
    plt.legend()
    plt.savefig(
        os.path.join(directorio, f"{prefijo}Eficiencia_vs_TotalCores.pdf"), format="pdf"
    )

    # Gráfico de Tiempo vs. TotalCores para diferentes tamaños de matriz
    plt.figure(figsize=(10, 8))
    for size in sorted(datos["MatrixSize"].unique()):
        subset = datos[datos["MatrixSize"] == size]
        plt.plot(
            subset["TotalCores"], subset["Time"], marker="o", label=f"Tamaño {size}"
        )
    plt.xlabel("Total de Núcleos")
    plt.ylabel("Tiempo (microsegundos)")
    plt.title(
        "Tiempo de Ejecución vs. Total de Núcleos para diferentes tamaños de Matriz"
    )
    plt.legend()
    plt.savefig(
        os.path.join(directorio, f"{prefijo}Time_vs_TotalCores.pdf"), format="pdf"
    )

    # Repetir para otros gráficos y guardarlos en formato PDF


# Solicita al usuario ingresar la ruta del directorio y un prefijo para los nombres de los archivos de gráficos
directorio = input(
    "Por favor, ingresa la ruta del directorio donde se encuentran los archivos: "
)
prefijo = input(
    "Por favor, ingresa el prefijo para los nombres de los archivos de gráficos: "
)
archivo_csv = "resultados_con_metricas.csv"

# Llama a la función para generar y guardar las gráficas
generar_graficas(directorio, archivo_csv, prefijo)

# Mensaje para informar al usuario que los gráficos han sido generados y guardados.
print(
    "Todos los gráficos han sido generados y guardados como archivos .pdf en el directorio proporcionado."
)
