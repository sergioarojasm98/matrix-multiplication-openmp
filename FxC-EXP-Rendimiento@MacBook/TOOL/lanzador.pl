#!/usr/bin/perl

if (@ARGV[0]) {
  $numRep = $ARGV[0];
} else {
  usage();
}

print "\n Repeticiones de la experimentación: $numRep \n\n";

$path0 = `pwd`;
chomp($path0);
$Path = $path0;
$Path =~ s/\/TOOL$//;

@Ejecutables = ("MM1c");
@cores = (1..10); # Apple M1 Max @ 3.20GHz
@VectorSize = ("100", "200", "300", "400", "500", "600", "700", "800", "900", "1000");

foreach $exe(@Ejecutables) {
  foreach $ves(@VectorSize) {
    foreach $c(@cores) {
      $file = "$Path/".
      "Soluciones/".
      "$exe".
      "-Size".
      "$ves".
      "-core".
      "$c";
      system("rm -f $file");	
      for ($i = 0; $i < $numRep; $i++) {
        print "Ejecutando: $Path/BIN/$exe $ves $c\n";
	system("$Path/BIN/$exe $ves $c 0 >> $file 2>&1");
      }
    }
  }
}

exit(1);

sub usage {
  print "\n tst.pl: Uso incorrecto\n\n";
  print "\t revisar entradas o directorio de almacenaje \n\n\n";
  exit(1);
}
