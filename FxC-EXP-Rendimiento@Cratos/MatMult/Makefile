# Define el compilador de C a utilizar, en este caso, GCC (GNU Compiler Collection).
GCC = gcc

# Flags de compilación:
# -fopenmp: Habilita el soporte para OpenMP, una API para programación multiproceso.
# -O3: Optimización de nivel 3, que busca mejorar la velocidad de ejecución y puede aumentar el tamaño del binario.
# -std=c99: Especifica el estándar del lenguaje C a usar, en este caso C99, que permite por ejemplo la declaración de variables dentro de los bucles for.
oT = -fopenmp -O3 -std=c99

# Flags adicionales para la compilación, en este caso, -lm para vincular la biblioteca matemática.
CFLAGS = -lm 

# Archivo fuente para la compilación.
oL= Otime.c

# Directorio donde se colocarán los archivos binarios resultantes de la compilación.
BINDIR = ../BIN/

# Define el nombre del programa a compilar, en este caso, MM1c, ubicado en el directorio BINDIR.
PROGS = $(BINDIR)MM1c 

# Regla 'all': Es el objetivo por defecto que se ejecutará al invocar make sin argumentos.
# Esta regla depende del objetivo MM1c.
all: MM1c

# Regla 'clean': Limpia los archivos generados por la compilación.
# Utiliza la variable $(RM) que es una variable de make que se expande al comando de borrado (usualmente 'rm -f').
clean:
	$(RM) $(PROGS)

# Regla para compilar el programa MM1c.
# Utiliza el compilador definido en GCC, los flags de compilación en oT y CFLAGS,
# y compila el archivo fuente $@.c (que se expande a MM1c.c) generando
# el ejecutable en el directorio BINDIR.
MM1c:
	$(GCC) $(oT) $(oL) $@.c -o $(BINDIR)$@ $(CFLAGS)
