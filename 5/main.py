import tkinter as tk
from tkinter import messagebox
import os
ventana = tk.Tk()
ventana.title("Leer archivo: prueba.txt")
ventana.geometry("500x400+700+200")

class Etiqueta:
    def __init__(self, ventana, texto, x, y):
        self.label = tk.Label(ventana, text=texto)
        self.label.place(x=x, y=y)

def mostrar_archivo():
    try:
        ruta = os.path.join(os.path.dirname(__file__),"prueba.txt")
        with open(ruta, "rb") as f:  
            contenido = f.read().decode("utf-8")
        texto.delete(1.0, tk.END)
        texto.insert(tk.END, contenido)
    except FileNotFoundError:
        messagebox.showerror("Error", "El archivo prueba.txt no se encontró.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

Etiqueta(ventana, "Contenido de: prueba.txt", 10, 10)
texto = tk.Text(ventana, width=60, height=20, state="normal")
texto.place(x=10, y=40)

boton = tk.Button(ventana, text="Mostrar archivo", command=mostrar_archivo)
boton.place(x=200, y=350)

ventana.mainloop()