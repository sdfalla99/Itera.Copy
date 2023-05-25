import tkinter as tk
from tkinter import ttk


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")


# ventana principal
window = tk.Tk()
window.title("Itera_Copy")
window.iconphoto(True, tk.PhotoImage(file="icon/escarabajo.png"))
window.configure(bg="forest green")
window.resizable(width=False, height=False)


# tamaño de la ventana principal
window_width = 307
window_height = 400
window.geometry(f"{window_width}x{window_height}")

# Centrar la ventana principal en la pantalla
center_window(window, window_width, window_height)

# Marco Principal
frame_margen = tk.Frame(window, bd=2, relief=tk.SUNKEN)
frame_margen.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

#==========================================================================================
# Marco Superior 1
#==========================================================================================

frame_colum1 = tk.LabelFrame(frame_margen, width=300, height=100, text="CSV - EXTENSION")
frame_colum1.configure(labelanchor="n")
frame_colum1.grid(row=0, column=0, padx=(10, 0), sticky="nsew")

# Botones Superior 1

abrir_csv = tk.Button(frame_colum1, text="Abrir CSV", width=10,height=1)
abrir_csv.grid(row=0, column=0, padx=10, pady=10)

Extension = tk.Label(frame_colum1, text="Extension",bg="#ececec", relief="raised", width=10, height=1)
Extension.grid(row=1, column=0,padx=10, pady=10)

datos_1 = tk.Entry(frame_colum1, text=None, selectbackground="forest green").grid(row=0, column=1)
datos_2 = tk.Entry(frame_colum1, text=None, selectbackground="forest green").grid(row=1, column=1)

#===========================================================================================
# Marco Superior 2
#==========================================================================================

frame_colum2 = tk.LabelFrame(frame_margen, width=300, height=100, text="CARPETAS")
frame_colum2.configure(labelanchor="n")
frame_colum2.grid(row=1, column=0, padx=(10,0) ,sticky="nsew")

# Botones Superior 2

ubicacion_carpeta = tk.Button(frame_colum2, text="Ubicacion", width=10, height=1)
ubicacion_carpeta.grid(row=0, column=0, padx=10, pady=10)

destino_carpeta = tk.Button(frame_colum2, text="Destino", width=10, height=1)
destino_carpeta.grid(row=1, column=0, padx=10, pady=10)

datos_3 = tk.Entry(frame_colum2, text=None, selectbackground="forest green").grid(row=0, column=1)
datos_4 = tk.Entry(frame_colum2, text=None, selectbackground="forest green").grid(row=1, column=1)

#==========================================================================================
# Marco Inferior 1
#==========================================================================================

frame_colum3 = tk.LabelFrame(frame_margen, width=300,height=100, text="FUNCIONES")
frame_colum3.configure(labelanchor="n")
frame_colum3.grid(row=2, column=0, padx=(10, 0), sticky="nsew")

# Botones Inferior 1

Cortar_1 = tk.Button(frame_colum3, text="Cortar", width=10, height=1).grid(row=1, column=0, padx=(0,15), pady=(20))
Cortar_1 = tk.Button(frame_colum3, text="Copiar", width=10, height=1).grid(row=1, column=1, padx=(0,15))
Cortar_1 = tk.Button(frame_colum3, text="Borrar", width=10, height=1).grid(row=1, column=2, padx=(0,2))

#==========================================================================================
# Marco Inferior 2
#==========================================================================================
frame_colum4 = tk.Frame(frame_margen, background="forest green", bd=2, relief="sunken",height=68)
frame_colum4.grid(row=3, column=0, padx=(10, 0), pady=10, sticky="nesw")

# Botones Inferior 2
frame_separador1 = tk.Frame(frame_colum4, background="forest green")
frame_separador1.grid(row=0,column=0)

ejecutar = tk.Button(frame_separador1, text="START",width=10, height=3, relief="ridge")
ejecutar.grid(row=0, column=0, padx=(5, 0), pady=(5, 5))

frame_separador2 = tk.Frame(frame_colum4, background="forest green")
frame_separador2.grid(row=0, column=1, padx=(15,0))

buscando = tk.Label(frame_separador2, text="Objetivos de búsqueda [0]")
buscando.grid(row=0, column=1, pady=(0,7))

encontrados = tk.Label(frame_separador2, text="Objetivos encontrados [0]")
encontrados.grid(row=1, column=1)
#==========================================================================================


# Mostrar la ventana principal
window.mainloop()
