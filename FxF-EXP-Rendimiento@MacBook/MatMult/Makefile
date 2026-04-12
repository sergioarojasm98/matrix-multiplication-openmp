# Utilizamos Clang, el compilador de LLVM
CC = clang

# Rutas a las bibliotecas y encabezados de OpenMP y LLVM
LDFLAGS = -L/opt/homebrew/opt/llvm/lib -L/opt/homebrew/opt/libomp/lib
CPPFLAGS = -I/opt/homebrew/opt/llvm/include -I/opt/homebrew/opt/libomp/include

# Opciones de compilación
OPT = -fopenmp -O3 -std=c99

# Librerías matemáticas y banderas de enlace
CFLAGS = -lm $(LDFLAGS) $(CPPFLAGS)

# Archivos fuente
oL= Otime.c

# Directorio de destino para los binarios
BINDIR = ../BIN/
PROGS = $(BINDIR)MM1f 

all: MM1f

clean:
	$(RM) $(PROGS)

MM1f:
	$(CC) $(OPT) $(oL) $@.c -o $(BINDIR)$@ $(CFLAGS)
