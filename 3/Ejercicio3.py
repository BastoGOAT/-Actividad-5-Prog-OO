import tkinter as tk
from tkinter import messagebox
import math
from Excepciones import *

ventana = tk.Tk()
ventana.title("Cálculos Numéricos")


etiqueta = tk.Label(ventana, text="Ingrese un valor numérico:")
etiqueta.pack(padx=10, pady=5)

entrada_valor = tk.Entry(ventana)
entrada_valor.pack(padx=10, pady=5)


boton = tk.Button(ventana, text="Calcular", command=lambda: CálculosNuméricos.calcular(entrada_valor.get()))
boton.pack(padx=10, pady=10)


ventana.mainloop()

