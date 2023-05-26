import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

# CODIGO LOGICO EMPIEZA AQUI

class busqueda_init:

    def abrir_archivo(self):
        self.ruta_archivo = filedialog.askopenfilename(
            filetypes=[("Archivos CSV", "*.csv")])
        if self.ruta_archivo:
            # Obtener solo el nombre del archivo con extensión
            nombre_archivo = self.ruta_archivo.split("/")[-1]
            # Borrar cualquier texto existente en el Entry
            nombre_csv.delete(0, "end")
            # Insertar el nombre del archivo en el Entry
            nombre_csv.insert(0, nombre_archivo)
            nombre_csv.config(disabledforeground="forest green")
            nombre_csv.config(state="disabled")  # Deshabilitar el Entry
    def extension(self):
        pass

# CODIGO DE INTERFAZ EMPIEZA AQUI

# Funcion Center_Window: Ajusta la ventana principal en la posicion del centro de la pantalla de acuerdo a la resolucion
# que tenga el equipo a utilizar.

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")


def clear_placeholder(event):
    if extension_ingresada.get() == "Ejemplo: JPG y CLICK":
        extension_ingresada.delete(0, tk.END)
        extension_ingresada.configure(foreground='forest green')


# Configuraciones ventana principal: Carga el titulo, Carga el icono, Carga el color de fondo para el margen, y por ultimo
# deshabilita el tamaño de ajuste de la ventana para el usuario, se deja de un tamaño fijo.

window = tk.Tk()
window.title("Itera_Copy")
window.iconphoto(True, tk.PhotoImage(file="icon/escarabajo.png"))
window.configure(bg="forest green")
window.resizable(width=False, height=False)

# tamaño de la ventana principal
window_width = 307
window_height = 400
window.geometry(f"{window_width}x{window_height}")

# Centrar la ventana principal en la pantalla, se llama a la funcion  y se entrega el tamaño y las proporciones
center_window(window, window_width, window_height)

# Marco Principal, este marco es el que permite visualizar el borde del aplicativo en verde ya que cubre la ventana principal
# y dentro de este se agrega todo el codigo correspondiente, por lo cual vendria siendo la ventana_padre

frame_margen = tk.Frame(window, bd=2, relief=tk.SUNKEN)
frame_margen.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

#==========================================================================================
# Marco Superior 1
#==========================================================================================
# Se genera la margen Leyenda Label para que tenga un titulo de entrada, se centra el texto
# se verifica que el  tamaño de la ventana no se afecte por los elementos a agregar con sticky="nsew"

frame_colum1 = tk.LabelFrame(frame_margen, width=300, height=100, text="CSV - EXTENSION")
frame_colum1.configure(labelanchor="n")
frame_colum1.grid(row=0, column=0, padx=(10, 0), sticky="nsew")

# Botones Superior 1
# se genera el Boton Abrir CSV, permitira abrir el documento con el listado de archivos, y se almacenara
# el nombre del archivo en la variable de ENTRY asignada

# Se genera el Boton Extension, este solicitara como entrada la extension, cualquiera extension es valida
# la cual buscara el archivo con ese formato.

abrir_1 = busqueda_init()
abrir_csv = tk.Button(frame_colum1, text="Abrir CSV", width=10,height=1, command=abrir_1.abrir_archivo)
abrir_csv.grid(row=0, column=0, padx=10, pady=10)

Extension = tk.Button(frame_colum1, text="Extension", width=10,height=1)
Extension.grid(row=1, column=0,padx=10, pady=10)

nombre_csv = tk.Entry(
    frame_colum1, selectbackground="forest green", foreground="forest green")
nombre_csv.grid(row=0, column=1)
extension_ingresada = tk.Entry(
    frame_colum1, selectbackground="forest green", foreground="forest green")
extension_ingresada.insert(0, "Ejemplo: JPG y CLICK")
extension_ingresada.bind('<FocusIn>', clear_placeholder)
extension_ingresada.grid(row=1, column=1)

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

ruta_ubicacion = tk.Entry(frame_colum2, text=None, selectbackground="forest green").grid(row=0, column=1)
ruta_destino = tk.Entry(frame_colum2, text=None, selectbackground="forest green").grid(row=1, column=1)

#==========================================================================================
# Marco Inferior 1
#==========================================================================================

frame_colum3 = tk.LabelFrame(frame_margen, width=300,height=100, text="FUNCIONES")
frame_colum3.configure(labelanchor="n")
frame_colum3.grid(row=2, column=0, padx=(10, 0), sticky="nsew")

# Botones Inferior 1

Cortar_1 = tk.Button(frame_colum3, text="Cortar", width=10, height=1).grid(row=1, column=0, padx=(0,15), pady=(20))
Copiar_2 = tk.Button(frame_colum3, text="Copiar", width=10, height=1).grid(row=1, column=1, padx=(0,15))
Borrar_3 = tk.Button(frame_colum3, text="Borrar", width=10, height=1).grid(row=1, column=2, padx=(0,2))

#==========================================================================================
# Marco Inferior 2
#==========================================================================================
frame_colum4 = tk.Frame(frame_margen, background="forest green", bd=2, relief="sunken",height=68)
frame_colum4.grid(row=3, column=0, padx=(10, 0), pady=10, sticky="nesw")

# Botones Inferior 2
frame_separador1 = tk.Frame(frame_colum4, background="forest green")
frame_separador1.grid(row=0,column=0)

boton_inicio = tk.Button(frame_separador1, text="START",width=10, height=3, relief="ridge")
boton_inicio.grid(row=0, column=0, padx=(5, 0), pady=(5, 5))

frame_separador2 = tk.Frame(frame_colum4, background="forest green")
frame_separador2.grid(row=0, column=1, padx=(15,0))

elementos_buscados = tk.Label(frame_separador2, text="Objetivos de búsqueda [0]")
elementos_buscados.grid(row=0, column=1, pady=(0,7))

documentos_encontrados = tk.Label(frame_separador2, text="Objetivos encontrados [0]")
documentos_encontrados.grid(row=1, column=1)
#==========================================================================================

# Mostrar la ventana principal
window.mainloop()
