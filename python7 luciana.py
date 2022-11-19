# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 09:29:00 2022

@author: Escuela de Oficios
"""

num = int(input("ingrese un numero "))
while(num  <0):
    print("El numero debe ser positivo")
    num = int(input("ingrese de nuevo numero"))
  
print(num)