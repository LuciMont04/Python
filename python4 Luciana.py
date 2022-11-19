# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 09:13:40 2022

@author: Escuela de Oficios
"""
"""registro"""
print("Ingrese su edad")
edad = int(input())
sul = int(input("Ingrese su sueldo mensual "))
if(edad >= 16):
    if(sul >= 1000):
        print("Puedes ser monotributista ")
    else:
        print("Tu sueldo deve ser mayor a 1000£ para ser motributisra ")
else:
    print("Debes ser mayos de 16 para ser monotributista ")