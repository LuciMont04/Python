# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 09:14:43 2022

@author: Escuela de Oficios
"""

print ("ingrese su nombre")
nom = input()
print ("Ingrese su edad")
edad = int(input())


if(edad <0):
     print("ERRO DE EDAD")
else:
    if(edad == 18):
        print("Tienes 18 años")
    else:   
        if(edad < 18):
            print("eres menor de edad " )
        else:
            print("Eres mayor de edad")


""" mostrar"""
print(" Me llamo {} y tengo {} años de edad".format(nom,edad))