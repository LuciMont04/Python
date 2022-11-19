# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 10:08:18 2022

@author: Escuela de Oficios
"""


num1 = int(input("Ingrese un numero"))
num2= num1
while( num1 != 0):
    num1= float(input("Ingrese otro numero"))
    num2 = num2 + num1
print(num2)