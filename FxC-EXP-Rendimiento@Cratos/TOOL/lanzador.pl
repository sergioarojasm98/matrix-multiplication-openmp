#!/usr/bin/perl

# Verifica si se ha proporcionado un argumento de línea de comandos.
if (@ARGV[0]) {
  $numRep = $ARGV[0];  # Asigna el primer argumento a la variable $numRep.
} else {
  usage();  # Llama a la función usage() si no se proporciona ningún argumento.
}

# Imprime el número de repeticiones de la experimentación.
print "\n Repeticiones de la experimentación: $numRep \n\n";

# Obtiene y almacena el directorio actual.
$path0 = `pwd`;
chomp($path0);  # Elimina el salto de línea del final del string.
$Path = $path0;
$Path =~ s/\/TOOL$//;  # Elimina la subcadena "/TOOL" del final del path.

# Define los ejecutables, el número de cores y los tamaños de los vectores para las pruebas.
@Ejecutables = ("MM1c");
@cores = (1..40);  # Rango de 1 a 40 para los cores.
@VectorSize = ("100", "200", "300", "400", "500", "600", "700", "800", "900", "1000");

# Itera a través de cada combinación de ejecutable, tamaño de vector y número de cores.
foreach $exe(@Ejecutables) {
  foreach $ves(@VectorSize) {
    foreach $c(@cores) {
      # Construye el nombre del archivo de salida para la experimentación actual.
      $file = "$Path/".
      "Soluciones/".
      "$exe".
      "-Size".
      "$ves".
      "-core".
      "$c";
      system("rm -f $file");  # Elimina el archivo de salida si ya existe.

      # Ejecuta el programa especificado con los parámetros dados varias veces.
      for ($i = 0; $i < $numRep; $i++) {
        print "Ejecutando: $Path/BIN/$exe $ves $c\n";  # Imprime el comando que se ejecutará.
        system("$Path/BIN/$exe $ves $c 0 >> $file 2>&1");  # Ejecuta el comando y redirige la salida al archivo.
      }
    }
  }
}

exit(1);  # Termina el script con un estado de salida 1.

# Función para mostrar el uso correcto del script en caso de que los argumentos no sean los adecuados.
sub usage {
  print "\n tst.pl: Uso incorrecto\n\n";
  print "\t revisar entradas o directorio de almacenaje \n\n\n";
  exit(1);  # Sale del script con un estado de salida 1.
}
