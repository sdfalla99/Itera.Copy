import tkinter as tk
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

# Crear ventana principal con Tkinter
ventana_tk = tk.Tk()
ventana_tk.geometry("400x300")

# Crear aplicación de PyQt
app = QApplication([])

# Crear ventana de PyQt
ventana_pyqt = QMainWindow()
ventana_pyqt.setCentralWidget(QLabel("Contenido de la ventana de PyQt"))

# Incrustar ventana de PyQt dentro de la ventana de Tkinter
frame = tk.Frame(ventana_tk)
frame.place(x=0, y=0, width=400, height=300)
embed = tk.Frame(frame, width=400, height=300)
embed.pack()
window_id = embed.winfo_id()
app.createWindowContainer(ventana_pyqt, window_id=window_id)

# Iniciar bucle principal de Tkinter
ventana_tk.mainloop()
