import tkinter as tk
from tkinter import ttk
import time


def iniciar_progreso():
    total_iteraciones = 10

    # Deshabilitar el botón de inicio para evitar múltiples clics
    boton_iniciar.config(state=tk.DISABLED)

    # Crear la barra de progreso
    barra_progreso = ttk.Progressbar(frame_progreso, length=200, mode='determinate')
    barra_progreso.pack()

    # Actualizar la barra de progreso
    for i in range(total_iteraciones):
        # Simular una operación que lleva tiempo
        time.sleep(0.5)

        # Actualizar el valor de la barra de progreso
        barra_progreso['value'] = (i + 1) * 10
        ventana.update()

    # Habilitar nuevamente el botón de inicio al finalizar el progreso
    boton_iniciar.config(state=tk.NORMAL)


# Crear la ventana principal
ventana = tk.Tk()

# Crear un Frame para contener la barra de progreso
frame_progreso = tk.Frame(ventana)
frame_progreso.pack()

# Crear un botón para iniciar el progreso
boton_iniciar = tk.Button(ventana, text="Iniciar", command=iniciar_progreso)
boton_iniciar.pack()

ventana.mainloop()
