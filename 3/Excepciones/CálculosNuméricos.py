import tkinter as tk
from tkinter import messagebox
import math
class CálculosNuméricos:
    def calcular(entrada):
        try:
            valor = float(entrada)


            if valor < 0:
                raise ArithmeticError("El valor debe ser un número positivo")
            resultado_log = math.log(valor)
            resultado_raiz = math.sqrt(valor)

            
            messagebox.showinfo("Resultados",
                                f"Logaritmo neperiano: {resultado_log:.4f}\n"
                                f"Raíz cuadrada: {resultado_raiz:.4f}")
        except ValueError:
            messagebox.showerror("Error", "Debe ingresar un número válido.")
        except ArithmeticError:
            messagebox.showerror("Error", "El valor debe ser un número positivo para calcular el logaritmo y la raiz cuadrada")



