import tkinter as tk
from tkinter import messagebox
ventana=tk.Tk()
ventana.title("Menú Vendedor") 
ventana.geometry("400x400+700+200")
#Componentes
class Etiqueta:
    def __init__(self,ventana,texto,x,y):
        self.label=tk.Label(ventana,text=texto)
        self.label.place(x=x,y=y)
class Entrada:
    def __init__(self,ventana,width,x,y):
        self.entry=tk.Entry(ventana,width=width)
        self.entry.place(x=x,y=y)
    def get(self):
         return self.entry.get()    
#Aplicando
nombreL=Etiqueta(ventana,"Nombre del vendedor:",10,10)
nombreE=Entrada(ventana,20,140,10)
apellidosL=Etiqueta(ventana,"Apellidos del vendedor:",10,40)
apellidosE=Entrada(ventana,20,140,40)
edadL=Etiqueta(ventana,"Edad del vendedor:",10,70)
edadE=Entrada(ventana,10,140,70)
#Función
def verificarEdad():
    try:    
        lectura=int(edadE.get())
        if lectura >=0 and lectura <=120:
            if lectura >=18 and lectura <=120: 
                class Vendedor:
                    nombre=nombreE.get() 
                    apellidos=apellidosE.get()
                    edad=lectura
                caja=tk.Tk()
                caja.title('El Vendedor')
                caja.geometry("300x300+720+220")
                label1=Etiqueta(caja,'Nombre del vendedor:',10,10)
                label2=Etiqueta(caja,Vendedor.nombre,10,30)
                label3=Etiqueta(caja,'Apellidos del vendedor:',10,50)
                label4=Etiqueta(caja,Vendedor.apellidos,10,70)
                label4=Etiqueta(caja,'Edad del vendedor',10,90)
                label4=Etiqueta(caja,Vendedor.edad,10,110)
                caja.mainloop()

            else:
                messagebox.showinfo('Error', "El vendedor debe ser mayor de 18 años")
        else:
             messagebox.showinfo('Error', "La edad no puede ser negativa ni mayor a 120")
    except:
         messagebox.showinfo('Error', "La edad debe ser un número")
         
Boton=tk.Button(ventana,width=10, text="Verificar edad",command=verificarEdad)
Boton.place(x=140,y=100)

ventana.mainloop()