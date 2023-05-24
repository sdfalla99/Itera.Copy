import os
import csv
import funciones_reutilizable as re



#  Empezaremos con tres clases disponibles:


#1) Opcion_iterar: Como primera instancia el usuario elegira que desea hacer, si copiar, recortar o borrar los archivos a buscar, esta opcion si no se elige no se habilitaran las demas por lo cual conforme se vayan llenando los datos si elige la opcion continuamos a la siguiente clase.

# 2) Open_Carpeta: Esta tendra como tarea solicitar la ubicacion de la carpeta donde se iterara y buscara los archivos con cierta extension, y luego realizara la funcion indicada por el usuario ya sea corta, copiar o borrar, en caso de las dos primeras solicitara de igual forma la ubicacion de la carpeta de destino.

#  3) Open_CSV esta clase sera la encargada de abrir el documento CSV que se le entregue y recorrer la informacion que tiene en la fila correspondiente donde concatenara de igual manera la extension escogida por el usuario, verificando asi los nombres de cada fila sobre la columna.




class Opciones_iterar():
    pass


class Open_Carpeta():
    pass


class Open_CSV():
    pass





