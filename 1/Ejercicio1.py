import tkinter as tk
from tkinter import messagebox
from Excepciones import *


ventana = tk.Tk()
ventana.title("Manejo de Excepciones")
ventana.geometry("300x200")


label = tk.Label(ventana, text="Presiona un botón para lanzar una excepción")
label.pack(pady=10)


btn1 = tk.Button(ventana, text="Primer Try", command=PruebaExcepciones.primer_try)
btn1.pack(pady=10)


btn2 = tk.Button(ventana, text="Segundo Try", command=PruebaExcepciones.segundo_try)
btn2.pack(pady=10)


ventana.mainloop()