GCC = gcc
oT = -fopenmp -O3 -std=c99   # Añadido -std=c99 para permitir declaraciones en bucles for

CFLAGS = -lm 

oL= Otime.c

BINDIR = ../BIN/
PROGS = $(BINDIR)MM1f 

all: MM1f

clean:
	$(RM) $(PROGS)

MM1f:
	$(GCC) $(oT) $(oL) $@.c -o $(BINDIR)$@ $(CFLAGS)
