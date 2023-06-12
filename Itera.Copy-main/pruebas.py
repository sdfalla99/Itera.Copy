import tkinter as tk
from tkinter import ttk


def agregar_scrollbar(root, widget):
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=widget.yview)
    widget.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")


# Crear la ventana principal
root = tk.Tk()
root.geometry("400x300")

# Crear un widget Text
text_widget = tk.Text(root)
text_widget.pack(fill="both", expand=True)

# Agregar el contenido al widget Text
for i in range(20):
    text_widget.insert("end", f"Texto {i}\n")

# Agregar la barra de desplazamiento al widget Text
agregar_scrollbar(root, text_widget)

# Iniciar el bucle principal de la aplicación
root.mainloop()
