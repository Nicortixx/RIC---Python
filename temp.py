
#Variables simples
"""
Script
"""
nombre = input("nombre: ")
salario = int (input("salario: "))

if salario > 4000000 and salario < 10000000:
    impuesto = salario * 0.15
elif salario >= 10000000 and salario < 15000000:
    impuesto = salario * 0.20
else:
    impuesto = salario * 0.30
print(nombre,"tiene que pagar", impuesto)