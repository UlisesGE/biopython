'''NAME
       AT-Rich

VERSION
        1.

AUTHOR
        Hector Ulises Gaspar <hectorgasp@gmail.com>

DESCRIPTION
        Este script obtiene las regiones ricas en AT de un archivo de secuencia dada por el usuario, y dado una cantidad mínima de AT. 

CATEGORY
        Script

USAGE
         python AT-rich.py


ARGUMENTS
        -f --file
        -s --tamaño minimo


    
SEE ALSO
        Ninguno

'''

import argparse
import re

arg_parser = argparse.ArgumentParser(description = "Obtiene las regiones ricas en AT y su posición, dado un archivo de secuencia y el tamaño minimo de la region")

#Se asignan argumentos para que el programa use
arg_parser.add_argument("-f", "--file",
                    metavar="path/to/file",
                    help="File with gene sequences",
                    required=True)


arg_parser.add_argument("-s", "--size",
                    help="Size of the region",
                    type=int,
                    required=False)
arguments = arg_parser.parse_args()

#Se abre el archivo de secuencia y se guarda en una variable 
with open(arguments.file, "r") as DNA_file:
    DNA = DNA_file.read().upper()
size = arguments.size

m = re.finditer("[^atgc]", DNA, re.IGNORECASE)
n = len([*re.finditer("[^atgc]", DNA, re.IGNORECASE)])
if n:
    print("Invalid sequence: ")
    for match in m:
        base = match.group()
        pos = match.start()
        print(base + " found at position " + str(pos))
else:
    at_region = re.finditer("AT", DNA)
    if at_region:
        for sequence in at_region:
            if len(sequence.group()) >= 2:
                print(f"AT rich region found at {sequence.span()}")
    else:
        print("No AT rich region found")

    
