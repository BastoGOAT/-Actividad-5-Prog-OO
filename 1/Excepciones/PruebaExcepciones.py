import tkinter as tk
from tkinter import messagebox
class PruebaExcepciones:
    def primer_try():
        try:
            print("Ingresando al primer try")
            cociente = 10000 / 0  
            print("Después de la división")
        except ZeroDivisionError:
            messagebox.showerror("Error", "División por cero")
        finally:
            messagebox.showinfo("Finally", "Ingresando al primer finally")

    def segundo_try():
        try:
            print("Ingresando al segundo try")
            objeto = None
            objeto.toString()  
            print("Imprimiendo objeto")
        except ZeroDivisionError:
            messagebox.showerror("Error", "División por cero")
        except Exception:
            messagebox.showerror("Excepción", "Ocurrió una excepción")
        finally:
            messagebox.showinfo("Finally", "Ingresando al segundo finally")