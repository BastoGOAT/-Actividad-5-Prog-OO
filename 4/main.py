import tkinter as tk
from tkinter import messagebox      

ventana = tk.Tk()
ventana.title("Menú Equipos de Programación") 
ventana.geometry("400x400+700+200")

# Componentes
class Etiqueta:
    def __init__(self, ventana, texto, x, y):
        self.label = tk.Label(ventana, text=texto)
        self.label.place(x=x, y=y)

class Entrada:
    def __init__(self, ventana, width, x, y):
        self.entry = tk.Entry(ventana, width=width)
        self.entry.place(x=x, y=y)
    def get(self):
        return self.entry.get() 

# Etiquetas y entradas principales
nombreL = Etiqueta(ventana, "Nombre del equipo:", 10, 10)
nombreE = Entrada(ventana, 20, 140, 10)
universidadL = Etiqueta(ventana, "Universidad:", 10, 40)
universidadE = Entrada(ventana, 20, 140, 40)
lenguajeL = Etiqueta(ventana, "Lenguaje de Programación:", 10, 70)
lenguajeE = Entrada(ventana, 15, 160, 70)

def next():
    equipo = nombreE.get()
    universidad = universidadE.get()
    lenguajeP = lenguajeE.get()
    integrantes = tk.Tk()
    integrantes.title("Integrantes") 
    integrantes.geometry("400x400+700+200")
    contador = {"valor": 0}
    entradas = []
    ventana.destroy()

    def add():
        if contador["valor"] == 0:
            contador["valor"] += 1
            persona1L = Etiqueta(integrantes, "Persona 1 Nombre:", 10, 10)
            persona1E = Entrada(integrantes, 20, 140, 10)
            persona1aL = Etiqueta(integrantes, "Persona 1 Apellido:", 10, 40)
            persona1aE = Entrada(integrantes, 20, 140, 40)
            entradas.append((persona1E, persona1aE))
        elif contador["valor"] == 1:
            contador["valor"] += 1
            persona2L = Etiqueta(integrantes, "Persona 2 Nombre:", 10, 70)
            persona2E = Entrada(integrantes, 20, 140, 70)
            persona2aL = Etiqueta(integrantes, "Persona 2 Apellido:", 10, 100)
            persona2aE = Entrada(integrantes, 20, 140, 100)
            entradas.append((persona2E, persona2aE))
        elif contador["valor"] == 2:
            contador["valor"] += 1
            persona3L = Etiqueta(integrantes, "Persona 3 Nombre:", 10, 130)
            persona3E = Entrada(integrantes, 20, 140, 130)
            persona3aL = Etiqueta(integrantes, "Persona 3 Apellido:", 10, 160)
            persona3aE = Entrada(integrantes, 20, 140, 160)
            entradas.append((persona3E, persona3aE))
        else:
            messagebox.showinfo("Limite alcanzado", "No puedes añadir más integrantes")
            añadir.config(state="disabled")

    def validar_texto(texto):
        if not texto.isalpha():
            raise ValueError("Solo se permiten letras, No use la tecla Espacio")
        if len(texto) >= 20:
            raise ValueError("El texto debe tener menos de 20 caracteres")

    def verificar():
        if contador["valor"] == 2 or contador["valor"] == 3:
            messagebox.showinfo("Válido", "Número de Integrantes Válido")
            def verificar_nombres():
                try:
                    integrantes_validados = []
                    for i, (nombreE, apellidoE) in enumerate(entradas):
                        nombre = nombreE.get()
                        apellido = apellidoE.get()
                        validar_texto(nombre)
                        validar_texto(apellido)
                        integrantes_validados.append(f"{nombre} {apellido}")
                    messagebox.showinfo("Correcto", "Todos los nombres y apellidos son válidos")
                    integrantes.destroy() 
                    imprimir = tk.Tk()
                    imprimir.title("Equipo de Programación")
                    imprimir.geometry("400x400+700+200")
                    Etiqueta(imprimir, f"Nombre del Equipo: {equipo}", 10, 10)
                    Etiqueta(imprimir, f"Nombre de la universidad: {universidad}", 10, 30)
                    Etiqueta(imprimir, f"Lenguaje de programación: {lenguajeP}", 10, 50)
                    Etiqueta(imprimir, "Conformado por:", 10, 70)
                    for idx, nombre_completo in enumerate(integrantes_validados):
                        Etiqueta(imprimir, nombre_completo, 10, 90 + idx*20)
                except ValueError as e:
                    messagebox.showerror("Error de validación", str(e))
            siguiente2 = tk.Button(integrantes, width=15, text="Verificar Nombres", command=verificar_nombres)
            siguiente2.place(x=130, y=250)
        else:
            messagebox.showinfo("Faltan Integrantes", "Añada mínimo 2 integrantes o máximo 3")

    verificarEquipo = tk.Button(integrantes, width=25, text="Verificar Número de Integrantes", command=verificar)
    verificarEquipo.place(x=90, y=220)
    añadir = tk.Button(integrantes, width=15, text="Añadir integrante", command=add)
    añadir.place(x=130, y=190)

siguiente = tk.Button(ventana, width=10, text="Siguiente", command=next)
siguiente.place(x=160, y=100)
ventana.mainloop()