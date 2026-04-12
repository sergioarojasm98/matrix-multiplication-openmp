GCC = gcc
oT = -fopenmp -O3 -std=c99   # Añadido -std=c99 para permitir declaraciones en bucles for

CFLAGS = -lm 

oL= Otime.c

BINDIR = ../BIN/
PROGS = $(BINDIR)MM1c 

all: MM1c

clean:
	$(RM) $(PROGS)

MM1c:
	$(GCC) $(oT) $(oL) $@.c -o $(BINDIR)$@ $(CFLAGS)