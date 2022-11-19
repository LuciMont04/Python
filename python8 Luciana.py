# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 09:45:54 2022

@author: Escuela de Oficios
"""

num = int(input("Ingrese un numero"))
while(num < 1 or num > 10):
    print("Debe ser un numero entre 0 y 10")
    num = int(input("Ingrese un numero"))
    
print(num)
    