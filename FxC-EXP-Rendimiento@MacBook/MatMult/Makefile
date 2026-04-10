# Usamos Clang, el compilador de LLVM
CC = clang

# Añadimos las rutas para las bibliotecas y los headers de OpenMP y LLVM
LDFLAGS = -L/opt/homebrew/opt/llvm/lib -L/opt/homebrew/opt/libomp/lib
CPPFLAGS = -I/opt/homebrew/opt/llvm/include -I/opt/homebrew/opt/libomp/include

# Opciones de compilación
OPT = -fopenmp -O3 -std=c99

# Librerías, por ejemplo, matemáticas
CFLAGS = -lm $(LDFLAGS) $(CPPFLAGS)

# Archivos fuente
oL= Otime.c

# Directorio de destino para los binarios
BINDIR = ../BIN/
PROGS = $(BINDIR)MM1c 

all: MM1c

clean:
	$(RM) $(PROGS)

MM1c:
	$(CC) $(OPT) $(oL) $@.c -o $(BINDIR)$@ $(CFLAGS)
