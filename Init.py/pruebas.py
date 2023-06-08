import csv
import os

with open(R"../../../../../../desaparecemos.csv", "r") as f:
    leer_fila = csv.reader(f)

    for line in leer_fila:
        print(line[0])

