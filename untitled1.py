# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 18:44:47 2022

@author: prestamour
"""

myList = []

count = 0
while count < 3:
    nombre = input("nombre: ")
    salario = int (input("salario: "))
    myList.append(salario)
    count=count+1
    if salario > 4000000 and salario < 10000000:
        impuesto = salario * 0.15
    elif salario >= 10000000 and salario < 15000000:
       impuesto = salario * 0.20
    else:
        impuesto = salario * 0.30
    print(nombre,"tiene que pagar", impuesto)
