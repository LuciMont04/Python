# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 09:32:13 2022

@author: Incubadora
"""

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

users = [
    # Name      DNI         user_nick       C1  C2  C3  saldo   debe
    ["Felipe",  "41504299",   "felipe123",    0,  0,  0,  0,      0],
    ["pepe",    "231688",   "pepe123",      0,  0,  0,  0,      0],
    ["Pedro",   "897987",   "pedro123",     0,  0,  0,  0,      0]
]

"""Shir. 
falta mejorar la parte grafica pero creo que igual esta bien"""


def guardarDatos():
    masterUser = "a"
    masterPass = "b"
    user = usuario.get()
    pas = contra.get()
    if (user == masterUser and pas == masterPass):
        page2(pagina1)
    else:
        messagebox.showinfo(message="Contraseña o usuario incorrectos", title="ERROR")


def guardarDatos1(page, dni, alias):
    if (dni != "" or alias != ""):
        for alumno in users:
            if alumno[2].lower() == alias.lower() or alumno[1] == dni:
                page3(page, alumno)
                break
            elif alumno == users[-1]:
                messagebox.showinfo(message="Usuario no existe", title="ERROR")


def page2(page):
    page.destroy()
    pagina2 = Tk()
    pagina2.title("Cliente")
    pagina2.geometry("520x520")
    dni = ttk.Entry()
    dni.place(x=270, y=270)
    alias = ttk.Entry()
    alias.place(x=270, y=300)
    boton1 = ttk.Button(text="Valida", command=lambda: guardarDatos1(pagina2, dni.get(), alias.get()))
    boton1.place(x=270, y=330)
    lbltext1 = Label(text="Cliente:")
    lbltext1.place(x=270, y=248.58)
    lblusuario = Label(text="DNI:")
    lblusuario.place(x=240, y=270)
    lblcontra = Label(text="ALIAS:")
    lblcontra.place(x=230, y=300)

def pagar(alumno, dinero, deuda):
    if alumno[-1] <= alumno[-2]:
        alumno[-2] -= alumno[-1]
        alumno[-1] = deuda
        dinero.set(f"Saldo: {alumno[-2]}")
        deuda.set(f"Deuda: {alumno[-1]}")
    else:
        messagebox.showinfo(message=f"No tiene dinero suficiente, faltan ${alumno[-1] - alumno[-2]}", title="Falta Dinero!!")

def page3(page, alumno):
    page.destroy()
    pagina3 = Tk()
    pagina3.config(width=300, height=200)
    pagina3.title("Botón en Tk")
    boton1 = ttk.Button(text="cargar_saldo", command=lambda: page5(pagina3, alumno))
    boton1.place(x=10, y=90)
    boton2 = ttk.Button(text="realizar_compra", command=lambda: page4(pagina3, alumno))
    boton2.place(x=100, y=90)

    Dinero = StringVar()
    Deuda= StringVar()
    Dinero.set(f"Saldo: {alumno[-2]}")
    Deuda.set(f"Deuda: {alumno[-1]}")

    name=ttk.Label(text=f"Nombre: {alumno[0]}")
    balance= ttk.Label(textvariable=Dinero)
    deuda = ttk.Label(textvariable=Deuda)


    name.place(x=10, y=10)
    balance.place(x=10, y=35)
    deuda.place(x=10, y=35+25)

    boton_ret = ttk.Button(text="Regresar", command=lambda: page2(pagina3))
    boton_ret.place(x=10, y=120)

    boton_pay = ttk.Button(text="Pagar!", command=lambda: pagar(alumno, Dinero, Deuda))
    boton_pay.place(x=100, y=120)


def addCombo(precio, alumno, strUpdate):

    if precio == 100:
        alumno[3] += 1
    elif precio == 200:
        alumno[4] += 1
    elif precio == 300:
        alumno[5] += 1

    alumno[-1] += precio
    strUpdate.set(f"Precio: {alumno[-1]}")


def page4(page, alumno):
    page.destroy()
    pagina4 = Tk()
    pagina4.config(width=300, height=200)
    pagina4.title("Botón en Tk")
    precio = StringVar()  # Variable q se utiliza para el cambio dinamico del texto del label `mtpagar`
    precio.set(f"Precio: {alumno[-1]}")
    mtpagar = ttk.Label(textvariable=precio)  # Etiqueta q muestra el precio mtpagar.place(x=100, y=170)
    mtpagar.place(x=10, y=170)
    TextMain = ttk.Label(text="REALIZAR COMPRA")  # Etoqieta en la parte superior pa q luzca mas bonito :3
    TextMain.place(x=50, y=10)
    boton3 = ttk.Button(text="combo1", command=lambda: addCombo(100, alumno, precio))  # lambda es una declaracion a una funcion privada, la use xq los button no permiten pasar parametros a su funcion command asi puedo pasarselos
    # lambda: addCombo(100, precio)
    # es igual q decir
    # def lambda():
    #   addCombo(100, precio)
    boton3.place(x=10, y=80 - 50)
    boton4 = ttk.Button(text="combo2", command=lambda: addCombo(200, alumno, precio))
    boton4.place(x=10, y=110 - 50)
    boton5 = ttk.Button(text="combo3", command=lambda: addCombo(300, alumno, precio))
    boton5.place(x=10, y=140 - 50)
    lbltext1 = Label(text="Ingrese combo: ")
    lbltext1.place(x=10, y=170 - 50)
    pagina4.geometry("520x520")
    carga= ttk.Entry()
    carga.place(x=20, y=270)
    carga1=cargar.get()
   
    

    boton_ret = ttk.Button(text="Regresar", command=lambda: page3(pagina4, alumno))
    boton_ret.place(x=200, y=168)
    
    boton_asig = ttk.Button(text="Regresar1", command=lambda: guardarDeuda(alumno, carga1))
    boton_asig.place(x=300, y=300)
#,command=lambda: addCombo(0,alumno,precio)

def guardarDeuda(alumno, carga):
    alumno[7] = carga


def cargarSaldo(alumno, saldo, var):
    alumno[-2] += int(saldo)
    var.set(f"SALDO ACTUAL: {alumno[-2]}")

def page5(page, alumno):
    page.destroy()
    pagina5 = Tk()
    pagina5.config(width=300, height=200)
    pagina5.title("Botón en Tk")
    cargar = ttk.Entry()
    cargar.place(x=10, y=50)

    label1 = ttk.Label(text="MONTO A CARGAR")
    label1.place(x=10, y=20)

    saldoTXT = StringVar()
    saldoTXT.set(f"SALDO ACTUAL: {alumno[-2]}")

    label2 = ttk.Label(textvariable=saldoTXT)
    label2.place(x=10, y=80)

    Cargar = ttk.Button(text="Cargar!", command=lambda: cargarSaldo(alumno, cargar.get(), saldoTXT))
    Cargar.place(x=60, y=50)

    boton_ret = ttk.Button(text="Regresar", command=lambda: page3(pagina5, alumno))
    boton_ret.place(x=150, y=150)


pagina1 = Tk()
pagina1.title("Inicio de sesión")
pagina1.geometry("540x540")
usuario = ttk.Entry()
usuario.place(x=270, y=270)
contra = ttk.Entry(show="*")
contra.place(x=270, y=300)
boton = ttk.Button(text="Acceder", command=guardarDatos)
boton.place(x=270, y=330)
lbltext1 = Label(text="Iniciar sesión:")
lbltext1.place(x=270, y=248.58)
lblusuario = Label(text="Usuario:")
lblusuario.place(x=220, y=270)
lblcontra = Label(text="Contraseña:")
lblcontra.place(x=200, y=300)
pagina1.mainloop()
